"""Render the video's diagrams from what EKOS and EKOS Lakehouse generated — nothing drawn by hand.

    python video/diagrams.py mermaid <page.md> <out-prefix> [--index N] [--title T]
        every ```mermaid block of a generated page (or the N-th) → <out-prefix>[-N].svg and .png (1920 px wide)
    python video/diagrams.py graph <graph-export.json> <out-prefix> [--min-weight W]
        `ekos graph export --level aggregate` → Graphviz → .svg/.png

Mermaid is rendered by Chromium with mermaid from jsDelivr (pinned); Graphviz `dot` must be installed.
"""
import argparse, html, json, os, re, subprocess, sys

MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"
FENCE = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def blocks(md_path):
    return [m.group(1) for m in FENCE.finditer(open(md_path, encoding="utf-8").read())]


def render_mermaid(sources, out_prefix, title=None):
    from playwright.sync_api import sync_playwright

    os.makedirs(os.path.dirname(out_prefix) or ".", exist_ok=True)
    written = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox"])
        page = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        for i, src in enumerate(sources, 1):
            head = f"<h1>{html.escape(title)}</h1>" if title else ""
            page.set_content(
                "<!doctype html><meta charset=utf-8><style>body{margin:0;padding:40px;background:#fff;"
                "font-family:system-ui,sans-serif}h1{font-size:34px;color:#17202b;margin:0 0 24px}"
                "#d svg{max-width:1840px;height:auto}</style>"
                f"{head}<div id=d><pre class=mermaid>{html.escape(src)}</pre></div>"
                f"<script src='{MERMAID}'></script>"
                "<script>mermaid.initialize({startOnLoad:true,theme:'neutral',maxTextSize:900000,"
                "er:{useMaxWidth:false},flowchart:{useMaxWidth:false}});</script>"
            )
            page.wait_for_selector("#d svg", timeout=60_000)
            svg = page.inner_html("#d")
            name = out_prefix if len(sources) == 1 else f"{out_prefix}-{i}"
            open(name + ".svg", "w").write(svg)
            box = page.locator("body").bounding_box()
            page.set_viewport_size({"width": 1920, "height": max(1080, int(box["height"]) + 10)})
            page.screenshot(path=name + ".png", full_page=True)
            page.set_viewport_size({"width": 1920, "height": 1080})
            written.append(name)
        b.close()
    return written


def render_graph(export_path, out_prefix, min_weight=1, top=0, exclude=(), title=""):
    # Aggregate export: nodes {id, n (label), count}; edges {s, t: node indexes, k: rel_kind_index, w: weight}.
    g = json.load(open(export_path))
    nodes = g.get("nodes", [])
    kinds = g.get("rel_kind_index", [])
    lines = ["digraph G {", 'rankdir=LR; bgcolor="white"; node [shape=box style="rounded,filled" '
             'fillcolor="#f5f3fb" color="#6d28d9" fontname="DejaVu Sans" fontsize=11];',
             'edge [color="#9a90b5" fontname="DejaVu Sans" fontsize=9];']
    keep = [i for i, n in enumerate(nodes) if n.get("n") not in exclude]
    if top:
        keep = sorted(keep, key=lambda i: -nodes[i].get("count", 0))[:top]
    keep = set(keep)
    if title:
        lines.insert(1, f'label="{title}"; labelloc=t; fontsize=24; fontname="DejaVu Sans Bold";')
    for i, n in enumerate(nodes):
        if i in keep:
            lines.append(f'n{i} [label="{n.get("n", n["id"])}{chr(92)}n{n.get("count", "")} objects"];')
    merged = {}
    for e in g.get("edges", []):
        if e["s"] == e["t"] or e["s"] not in keep or e["t"] not in keep:
            continue
        key = (e["s"], e["t"])
        merged.setdefault(key, {})
        kind = kinds[e["k"]] if e["k"] < len(kinds) else str(e["k"])
        merged[key][kind] = merged[key].get(kind, 0) + e.get("w", 1)
    for (s, t), by_kind in merged.items():
        w = sum(by_kind.values())
        if w >= min_weight:
            label = ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items(), key=lambda x: -x[1])[:2])
            lines.append(f'n{s} -> n{t} [label="{label}" penwidth={min(6, 1 + w / 50):.1f}];')
    lines.append("}")
    dot = "\n".join(lines)
    open(out_prefix + ".dot", "w").write(dot)
    for fmt in ("svg", "png"):
        subprocess.run(["dot", f"-T{fmt}", "-Gdpi=110", "-o", f"{out_prefix}.{fmt}"], input=dot.encode(), check=True)
    return [out_prefix]


def render_er(lock_path, out_prefix, title, highlight=(), skip_refs=(), edge_labels=True, font=13):
    """A compact ER diagram of a deployed plan: one box per table (its column count), one edge per
    declared foreign key between planned tables (labelled with its column). Readable at video size,
    where an ER with every column is not."""
    plan = json.load(open(lock_path))
    tables = {t["table"]: t for t in plan["tables"]}
    hl = {h.upper() for h in highlight}
    lines = ["digraph ER {", f'label="{title}"; labelloc=t; fontsize=26; fontname="DejaVu Sans Bold";',
             'graph [rankdir=LR, bgcolor="white", pad=0.4, nodesep=0.35, ranksep=1.1, splines=true, overlap=false];',
             f'node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize={font}, color="#6d28d9", fillcolor="#f5f3fb"];',
             'edge [color="#8f86a8", arrowsize=0.6, fontname="DejaVu Sans", fontsize=9, fontcolor="#5b6675"];']
    for name, t in sorted(tables.items()):
        fill = ', fillcolor="#fde68a", color="#b45309"' if name in hl else ""
        lines.append(f'"{name}" [label="{name}\\n{len(t["facts"]["columns"])} columns"{fill}];')
    seen = set()
    for name, t in sorted(tables.items()):
        for fk in t["facts"].get("foreign_keys", []):
            ref = fk["ref_table"]
            if ref in tables and ref != name and ref not in skip_refs and (name, ref) not in seen:
                seen.add((name, ref))
                label = ", ".join(fk["columns"]).lower() if edge_labels else ""
                lines.append(f'"{name}" -> "{ref}" [label="{label}"];')
    lines.append("}")
    dot = "\n".join(lines)
    open(out_prefix + ".dot", "w").write(dot)
    for fmt in ("svg", "png"):
        # fdp: a force layout, near square, where dot's ranks spread 33 tables over a 4000 px wide sheet
        subprocess.run(["dot", "-Kfdp", f"-T{fmt}", "-Gdpi=96", "-Goverlap=false", "-Gsep=+8",
                        "-o", f"{out_prefix}.{fmt}"], input=dot.encode(), check=True)
    return [out_prefix]


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("mermaid")
    m.add_argument("page"); m.add_argument("out")
    m.add_argument("--index", type=int); m.add_argument("--title")
    g = sub.add_parser("graph")
    g.add_argument("export"); g.add_argument("out"); g.add_argument("--min-weight", type=int, default=1)
    g.add_argument("--top", type=int, default=0); g.add_argument("--exclude", action="append", default=[])
    g.add_argument("--title", default="")
    e = sub.add_parser("er")
    e.add_argument("lock"); e.add_argument("out"); e.add_argument("--title", default="")
    e.add_argument("--highlight", action="append", default=[])
    e.add_argument("--skip-ref", action="append", default=[], help="leave out keys to this table (e.g. one every table has)")
    e.add_argument("--no-edge-labels", action="store_true"); e.add_argument("--font", type=int, default=13)
    a = ap.parse_args()
    if a.cmd == "mermaid":
        srcs = blocks(a.page)
        if not srcs:
            sys.exit(f"{a.page}: no mermaid block")
        if a.index:
            srcs = [srcs[a.index - 1]]
        print("\n".join(render_mermaid(srcs, a.out, a.title)))
    elif a.cmd == "er":
        print("\n".join(render_er(a.lock, a.out, a.title, a.highlight, set(a.skip_ref), not a.no_edge_labels, a.font)))
    else:
        print("\n".join(render_graph(a.export, a.out, a.min_weight, a.top, set(a.exclude), a.title)))


if __name__ == "__main__":
    main()
