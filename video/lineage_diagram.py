"""Column lineage of one gold mart through every layer, with each step's transformation, rendered by
Graphviz from lakehouse-docs' own lineage model (the same one its pages are generated from).

    PYTHONPATH=<ekos-lakehouse>/tools/lakehouse-docs \
      python video/lineage_diagram.py <pipeline> <evidence dir> <gold model> <out prefix>
"""
import subprocess, sys
from pathlib import Path

from lakehouse_docs import lineage, project

LANES = ("source", "bronze", "silver", "gold")
COLOUR = {"source": "#e0f2fe", "bronze": "#fde68a", "silver": "#e5e7eb", "gold": "#fef3c7"}


def short(text, n=40):
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1] + "…"


def main():
    pipeline, evidence, model, out = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4]
    p = project.load(pipeline, evidence)
    lin = lineage.build(p)
    gold = p.models[model]
    nodes, edges = {}, []
    stack = [lineage.Node("gold", model, c.name) for c in gold.columns]
    seen = set()
    while stack:
        n = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        nodes[n] = True
        for e in lin.up.get(n, []):
            edges.append(e)
            stack.append(e.src)
    ids = {n: f"n{i}" for i, n in enumerate(nodes)}
    lines = ["digraph L {", f'label="Column lineage of {gold.relation}: source → bronze → silver → gold"; labelloc=t;',
             'fontsize=24; fontname="DejaVu Sans Bold"; rankdir=LR; bgcolor="white"; nodesep=0.2; ranksep=0.8;',
             'node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize=17, color="#6b7280"];',
             'edge [fontname="DejaVu Sans", fontsize=14, color="#6d28d9", fontcolor="#4b5563"];']
    for lane in LANES:
        members = [n for n in nodes if n.layer == lane]
        if not members:
            continue
        lines.append(f'subgraph cluster_{lane} {{ label="{lane}"; fontsize=18; color="#d1d5db"; style=rounded;')
        for n in members:
            rel = n.relation.split(".")[-1]
            lines.append(f'{ids[n]} [label="{rel}\\n{n.column}", fillcolor="{COLOUR[lane]}"];')
        lines.append("}")
    for e in edges:
        label = "" if e.transform.startswith("pass-through") else short(e.transform).replace('"', "'")
        lines.append(f'{ids[e.src]} -> {ids[e.dst]} [label="{label}"];')
    lines.append("}")
    dot = "\n".join(lines)
    Path(out + ".dot").write_text(dot)
    for fmt in ("svg", "png"):
        subprocess.run(["dot", f"-T{fmt}", "-Gdpi=110", "-o", f"{out}.{fmt}"], input=dot.encode(), check=True)
    print(out, len(nodes), "columns,", len(edges), "steps")


if __name__ == "__main__":
    main()
