"""The video demo's tour: a new project (`idemsales`, the iDempiere order-to-invoice slice) taken through the seven
steps in the EKOS console, one phase at a time, with screenshots at 1920x1080 for the video.

    EKOS_CONSOLE_URL=… EKOS_CONSOLE_TOKEN_VALUE=<write token> EKOS_BIN=$(command -v ekos-lakehouse) \
      python video/tour.py <phase> [<out dir>]        # phases: analyse docs review requirements extraction build marts

Each phase drives the console the way an operator does and saves `shots/<nn>-<name>.png`. Review decisions are made
as the demo operator (the console attributes them to the signed-in token). Local paths and the account name are
replaced on the page before each screenshot (`REPLACE`).
"""
import json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.environ.get("EKOS_CONSOLE_URL", "http://127.0.0.1:18765")
TOKEN = os.environ["EKOS_CONSOLE_TOKEN_VALUE"]
WS = os.environ.get("EKOS_WORKSPACE", "idemsales")
LONG = 300_000
REPLACE = [tuple(r.split("=", 1)) for r in os.environ.get("TOUR_REPLACE", "").split("|") if "=" in r]
REPLACE_JS = """(rules) => {
  const esc = (s) => s.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
  const rx = rules.map(([o, n]) => [new RegExp(/^\\w+$/.test(o) ? '\\\\b' + esc(o) + '\\\\b' : esc(o), 'g'), n]);
  const fix = (t) => rx.reduce((s, [r, n]) => s.replace(r, n), t);
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = w.nextNode(); n; n = w.nextNode()) n.nodeValue = fix(n.nodeValue);
  for (const i of document.querySelectorAll('input, textarea')) i.value = fix(i.value);
}"""


class Tour:
    def __init__(self, page, out):
        self.page, self.out = page, out
        os.makedirs(os.path.join(out, "shots"), exist_ok=True)

    def go(self, path, wait=None):
        print("go", path.format(ws=WS), wait or "", flush=True)
        self.page.goto(BASE + path.format(ws=WS))
        if wait:
            self.wait(wait)
        self.settle()

    def wait(self, what):
        if what.startswith("aria:"):
            self.page.locator(f'[aria-label="{what[5:]}"]').first.wait_for(timeout=LONG)
        else:
            self.page.get_by_text(what).first.wait_for(timeout=LONG)

    def settle(self):
        self.page.wait_for_timeout(800)
        busy = self.page.locator("text=loading…")
        if busy.count() > 0:
            busy.first.wait_for(state="detached", timeout=LONG)

    def shot(self, name, full=False):
        if REPLACE:
            self.page.evaluate(REPLACE_JS, [list(r) for r in REPLACE])
        path = os.path.join(self.out, "shots", f"{name}.png")
        self.page.screenshot(path=path, full_page=full)
        print("shot", name, flush=True)

    def run_id(self):
        self.page.wait_for_url("**/runs/**", timeout=LONG)
        return self.page.url.rstrip("/").split("/")[-1]

    def wait_run(self, rid, minutes=60, shots=()):
        """Wait for a console run; take the named screenshots of its page at the given minutes."""
        start = time.time()
        pending = list(shots)
        while True:
            run = self.page.request.get(f"{BASE}/api/runs/{rid}").json()
            elapsed = (time.time() - start) / 60
            if pending and elapsed >= pending[0][0]:
                self.page.reload()
                self.settle()
                self.shot(pending.pop(0)[1])
            if run["status"] not in ("queued", "running"):
                return run
            if elapsed > minutes:
                raise SystemExit(f"run {rid} still {run['status']} after {minutes} min")
            time.sleep(10)

    def action(self, button, inputs=None, confirm=None, before=None):
        """An extension page's action: click, fill, (shot), Run; returns the finished run."""
        self.page.get_by_role("button", name=button, exact=True).click()
        for label, value in (inputs or {}).items():
            self.page.locator(f'[aria-label="{label}"]').fill(value)
        if confirm:
            self.page.get_by_label(confirm).check()
        typed = self.page.locator('[aria-label^="type "][aria-label$=" to confirm"]')
        if typed.count() > 0:
            typed.fill(typed.get_attribute("aria-label")[len("type "):-len(" to confirm")])
        if before:
            self.shot(before)
        run = self.page.get_by_role("button", name="Run", exact=True)
        try:
            run.wait_for(timeout=3000)
            run.click()
        except Exception:  # an action without inputs runs on the click
            pass
        rid = self.run_id()
        r = self.wait_run(rid)
        if r["status"] != "succeeded":
            raise SystemExit(f"{button}: {r['status']} — {json.dumps(r.get('log_tail', [])[-5:])}")
        return rid

    def select_row(self, page, wait, row, button):
        self.go(f"/w/{{ws}}/x/lakehouse/{page}", wait)
        cells = self.page.get_by_role("cell", name=row, exact=True)
        cells.first.wait_for(timeout=LONG)
        target = self.page.get_by_role("button", name=button, exact=True)
        for i in range(cells.count()):
            cells.nth(i).click()
            try:
                target.wait_for(timeout=5000)
                self.settle()
                return
            except Exception:
                continue
        raise SystemExit(f"{page}: no row {row} shows {button}")


def cli(*args):
    p = subprocess.run([os.environ["EKOS_BIN"], "--project", WS, *args], capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit(f"{' '.join(args)}: {p.stderr[-800:]}")
    return p.stdout


# ── phases ────────────────────────────────────────────────────────────────────────────────────────


def analyse(t):
    """Step 1: the sources, the database tested (census before analysis), Init & compile, the result."""
    t.go("/w/{ws}/sources", "Sources")
    t.shot("01-sources")
    t.page.get_by_role("button", name="Test connection").first.click()
    t.page.locator('[aria-label="census vs compiled"], p.err').first.wait_for(timeout=LONG)
    t.settle()
    t.shot("02-database-tested")
    t.page.once("dialog", lambda d: d.accept())
    t.page.get_by_role("button", name="Init & compile").click()
    rid = t.run_id()
    r = t.wait_run(rid, minutes=90, shots=[(0.5, "03-analysis-running"), (6, "04-analysis-recover")])
    t.settle()
    t.shot("05-analysis-done")
    if r["status"] != "succeeded":
        raise SystemExit(f"Init & compile {r['status']}")
    t.go("/w/{ws}/sources", "Sources")
    t.page.get_by_role("button", name="Test connection").first.click()
    t.page.locator('[aria-label="census vs compiled"], p.err').first.wait_for(timeout=LONG)
    t.settle()
    t.shot("06-census-equals-compiled")
    t.go("/w/{ws}", "aria:workflow")
    t.shot("07-dashboard")


def reshoot1(t):
    """Step 1's static pages again at the video's scale (the analysis itself is not repeated)."""
    runs = t.page.request.get(f"{BASE}/api/runs?workspace={WS}&limit=50").json()
    init = next(r for r in runs if r["command"] == "init-and-compile" and r["status"] == "succeeded")
    t.go(f"/runs/{init['id']}", "Steps")
    t.shot("05-analysis-done")
    t.go("/w/{ws}/sources", "Sources")
    t.page.get_by_role("button", name="Test connection").first.click()
    t.page.locator('[aria-label="census vs compiled"], p.err').first.wait_for(timeout=LONG)
    t.settle()
    t.shot("06-census-equals-compiled")
    t.go("/w/{ws}", "aria:workflow")
    t.shot("07-dashboard")


def docs(t):
    """Step 2: the Documentation page, Generate, Preview publish."""
    t.go("/w/{ws}/x/lakehouse/docs", "Home page")
    t.shot("08-docs-page")
    t.action("Generate")
    t.settle()
    t.shot("09-docs-generated-run")
    t.go("/w/{ws}/x/lakehouse/docs", "Home page")
    t.action("Preview publish", before="10-docs-preview-confirm")
    t.settle()
    t.shot("11-docs-preview-run")
    t.go("/w/{ws}/x/lakehouse/docs", "Home page")
    t.shot("12-docs-after-preview")


SLICE = set(
    "C_ORDER C_ORDERLINE C_ORDERTAX C_INVOICE C_INVOICELINE C_INVOICETAX C_PAYMENT C_ALLOCATIONHDR "
    "C_ALLOCATIONLINE C_BPARTNER C_BPARTNER_LOCATION C_BP_GROUP C_LOCATION C_REGION C_COUNTRY C_CURRENCY "
    "M_PRODUCT M_PRODUCT_CATEGORY M_PRICELIST M_PRICELIST_VERSION M_PRODUCTPRICE M_WAREHOUSE M_INOUT M_INOUTLINE "
    "C_DOCTYPE C_TAX C_TAXCATEGORY C_UOM C_PAYMENTTERM C_CHARGE AD_CLIENT AD_ORG AD_USER".split()
)
OPERATOR = "demo operator"


def tab(t, label):
    t.page.get_by_role("tablist").get_by_role("button", name=label).click()
    t.settle()


def sign(t, subject):
    """Sign the open subject off by typing its name; wait until the sign-off reads valid."""
    print("sign", subject, flush=True)
    t.settle()
    reviewer = t.page.locator('[aria-label="reviewer"]')
    if reviewer.count() > 0:
        reviewer.first.fill(OPERATOR)
    t.page.locator('[aria-label="confirm"]').fill(subject)
    t.page.get_by_role("button", name="Sign off").click()
    box = t.page.locator('[aria-label="sign-off"]')
    box.locator(".ok-line, .err").first.wait_for(timeout=900_000)
    chip = box.locator(".chip").first
    for _ in range(60):
        if chip.inner_text().strip() == "valid":
            return
        time.sleep(2)
    raise SystemExit(f"{subject}: sign-off is {chip.inner_text()}")


def conflict_note(target):
    """The demo operator's note for a mandatory-but-nullable conflict, from its measured rows."""
    out = cli("conflicts", "show", target)
    measured = next((l.split(":", 1)[1].strip() for l in out.splitlines() if l.strip().startswith("measured:")), "")
    code = next((l.strip() for l in out.splitlines() if "; code)" in l), "")
    where = code[code.find("(") + 1:code.rfind(";")] if code else "the application model"
    return (f"Both hold: the application makes it mandatory ({where}); the database allows NULL. "
            f"Measured: {measured or 'not profiled'}. Silver keeps the column nullable.")


def review(t):
    """Step 3, as the demo operator: scope to the order-to-invoice slice, the conflicts inside it, identity,
    and every subject signed off."""
    print("reading the scope", flush=True)
    rows = json.loads(cli("review", "show", "scope", "--json"))["rows"]
    out_tables = [r["label"] for r in rows if r.get("proposed") == "in" and r["label"].upper() not in SLICE]
    decided = {r["label"] for r in rows if r.get("decision")}
    if not set(out_tables) <= decided:
        scope_out(t, out_tables)
    review_rest(t)


def scope_out(t, out_tables):
    t.go("/w/{ws}/review", "aria:sign-off")
    t.shot("13-review-before")
    # Scope: one command for every table outside the slice, from the console's Commands page.
    t.go("/w/{ws}/commands", "Commands")
    t.page.locator('[aria-label="filter commands"]').fill("review scope")
    t.page.get_by_role("button", name="review scope", exact=True).click()
    t.page.locator("#arg-tables").fill("\n".join(out_tables))
    t.page.locator("#arg-out").check()
    t.page.locator("#arg-reason").fill("outside the order-to-invoice slice this lakehouse is built for")
    t.settle()
    t.shot("14-scope-command")
    t.page.get_by_role("button", name="Run", exact=True).click()
    r = t.wait_run(t.run_id(), minutes=30)
    if r["status"] != "succeeded":
        raise SystemExit(f"review scope: {r['status']}")
    t.settle()
    t.shot("15-scope-run")


def review_rest(t):
    # The review page: scope now the slice; sign it off. The first read after a decision recomputes the
    # whole review state, so the page may load for a while.
    t.go("/w/{ws}/review", "aria:sign-off")
    t.page.locator('[aria-label="filter"]').wait_for(timeout=900_000)
    t.page.locator('[aria-label="filter"]').fill("C_ORDER")
    t.settle()
    t.shot("16-scope-slice")
    t.page.locator('[aria-label="filter"]').fill("")
    sign(t, "scope")
    t.shot("17-scope-signed")
    # Conflicts inside the slice: two on camera on the Conflicts page, the rest from the CLI.
    conflicts = json.loads(cli("review", "show", "conflicts", "--json"))["rows"]
    blocking = [c for c in conflicts if c["blocking"]]
    print("blocking conflicts in scope:", len(blocking), flush=True)
    for c in blocking[2:]:
        cli("conflicts", "resolve", c["label"], "--both-valid", "--note", conflict_note(c["label"]), "--as", OPERATOR)
    for i, c in enumerate(blocking[:2]):
        t.go("/w/{ws}/conflicts", "Conflicts")
        t.page.get_by_role("button", name=c["label"], exact=True).first.click()
        aside = t.page.locator('[aria-label="conflict"]')
        aside.wait_for(timeout=LONG)
        aside.locator('[aria-label="reviewer"]').fill(OPERATOR)
        aside.locator('[aria-label="note"]').fill(conflict_note(c["label"]))
        t.settle()
        if i == 0:
            t.shot("18-conflict-decision")
        aside.get_by_role("button", name="Both are valid").click()
        aside.locator(".ok-line, .err").first.wait_for(timeout=LONG)
    t.settle()
    t.shot("19-conflict-recorded")
    t.go("/w/{ws}/review", "aria:sign-off")
    tab(t, "Conflicts")
    sign(t, "conflicts")
    t.shot("20-conflicts-signed")
    # Identity: the one candidate, decided on the evidence (the handle is the local part of the name's
    # commit address: 10 commits under the name, 4 under the handle).
    tab(t, "Identity")
    t.page.locator('[aria-label="select all shown"]').check()
    reviewer = t.page.locator('[aria-label="reviewer"]')
    if reviewer.count() > 0:
        reviewer.first.fill(OPERATOR)
    t.page.locator('[aria-label="reason"]').fill(
        "One contributor: the handle is the local part of the display name's commit address (git log)."
    )
    t.settle()
    t.shot("21-identity-decision")
    t.page.get_by_role("button", name="Same thing").click()
    t.page.locator('[aria-label="decide"]').locator(".ok-line, .err").first.wait_for(timeout=LONG)
    sign(t, "identity")
    # The rest: PII (proposed masks), write behaviour, glossary.
    for label, subject in (("PII", "pii"), ("Write behaviour", "write-behaviour"), ("Glossary", "glossary")):
        tab(t, label)
        if subject == "pii":
            t.shot("22-pii")
        sign(t, subject)
    t.page.reload()
    t.page.locator('[aria-label="workflow"]').first.wait_for(timeout=LONG)
    t.settle()
    t.shot("23-review-signed")


TEXT_MART = "region_category_sales"
TEXT_REQUEST = "net sales of completed customer orders by month, product category and the customer's region"


def save(name, text):
    """A command's output for the video's terminal shots."""
    os.makedirs(os.path.join(HERE, "outputs"), exist_ok=True)
    open(os.path.join(HERE, "outputs", f"{name}.txt"), "w").write(text)


def requirements(t):
    """Step 4, first half: two marts from Markdown (CLI), one in plain words drafted by local llama3 (page)."""
    for m in ("sales_by_month", "invoices_by_month"):
        out = cli("lakehouse", "requirements", "draft", "--mart", m, "--file",
                  os.path.join(HERE, "marts", f"{m}.md"), "--as", OPERATOR)
        save(f"requirements-draft-{m}", out)
    t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
    t.page.get_by_role("cell", name="sales_by_month", exact=True).first.click()
    t.wait("sales_by_month — ")
    t.settle()
    t.shot("24-requirement-from-file")
    t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
    t.action("Draft from text", {
        "Mart name (lowercase letters, digits, _)": TEXT_MART,
        "What should it show? (plain words)": TEXT_REQUEST,
    }, before="25-draft-from-text")
    t.settle()
    t.shot("26-draft-run")
    t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
    t.page.get_by_role("cell", name=TEXT_MART, exact=True).first.click()
    t.wait(f"{TEXT_MART} — ")
    t.settle()
    t.shot("27-draft-questions", full=True)


def answers(t):
    """Step 4: the operator's answers to the draft's questions (video/marts/<file>: [{button, inputs}])."""
    name = os.environ.get("ANSWERS", "answers.json")
    first = name == "answers.json"
    for i, a in enumerate(json.load(open(os.path.join(HERE, "marts", name)))):
        t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
        t.page.get_by_role("cell", name=TEXT_MART, exact=True).first.click()
        t.wait(f"{TEXT_MART} — ")
        t.action(a["button"], a["inputs"], before="28-answer" if first and i == 0 else None)
    t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
    t.page.get_by_role("cell", name=TEXT_MART, exact=True).first.click()
    t.wait(f"{TEXT_MART} — ")
    t.settle()
    t.shot("29-answered", full=True)


def approve(t):
    """Step 4: every requirement approved on the page."""
    for m in (TEXT_MART, "sales_by_month", "invoices_by_month"):
        t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
        t.page.get_by_role("cell", name=m, exact=True).first.click()
        t.wait(f"{m} — ")
        t.action(f"Approve: {m}", {"Note (optional)": "approved by the demo operator"},
                 confirm="You approve this requirement as shown",
                 before="30-approve" if m == TEXT_MART else None)
    t.go("/w/{ws}/x/lakehouse/requirements", "Requirements (click one)")
    t.settle()
    t.shot("31-requirements-approved")


CHANGE_TABLE = "ADEMPIERE.C_BPARTNER"


def extraction(t):
    """Step 5: the plan for the slice, one table's evidence, a change with a reason, the approval."""
    t.go("/w/{ws}/x/lakehouse/lakehouse", "Lakehouse")
    t.action("Plan")
    t.settle()
    t.shot("32-plan-run")
    t.go("/w/{ws}/x/lakehouse/extraction", "Extraction")
    t.settle()
    t.shot("33-extraction-plan")
    t.select_row("extraction", "Extraction", "ADEMPIERE.C_ORDER", "Load in full: ADEMPIERE.C_ORDER")
    t.page.get_by_text("Why it loads this way").first.wait_for(timeout=LONG)
    t.settle()
    t.shot("34-table-evidence", full=True)
    t.select_row("extraction", "Extraction", CHANGE_TABLE, f"Load in full: {CHANGE_TABLE}")
    t.action(f"Load in full: {CHANGE_TABLE}",
             {"Why (kept with the change)": "a small master table: reload it whole every run"},
             before="35-change")
    t.go("/w/{ws}/x/lakehouse/extraction", "Extraction")
    t.action("Approve plan", {"Note (optional)": "the order-to-invoice slice, C_BPARTNER in full"},
             confirm="You approve the plan as shown", before="36-approve-plan")
    t.go("/w/{ws}/x/lakehouse/extraction", "Extraction")
    t.settle()
    t.shot("37-plan-approved")


def generate(t):
    """Step 6, first half: the pipeline generated (the step-3 and step-5 gates pass)."""
    t.go("/w/{ws}/x/lakehouse/lakehouse", "Lakehouse")
    t.action("Generate")
    t.settle()
    t.shot("38-generate-run")


def load(t):
    """Step 6, second half: the whole slice through Dagster, launched from the console."""
    t.go("/w/{ws}/x/lakehouse/lakehouse", "Lakehouse")
    t.action("Run the pipeline", confirm="Dagster runs the job now", before="39-run-confirm")
    t.settle()
    t.shot("40-run-launched")


def after_load(t):
    """Step 6's result on the Lakehouse page, after the Dagster run and `run-report`."""
    t.go("/w/{ws}/x/lakehouse/lakehouse", "Lakehouse")
    t.settle()
    t.shot("43-lakehouse-tables")
    t.go("/w/{ws}", "aria:workflow")
    t.shot("44-bar-after-load")


MARTS = ("sales_by_month", "invoices_by_month", TEXT_MART)


def open_mart(t, mart):
    t.go("/w/{ws}/x/lakehouse/marts", "Marts (click one)")
    t.page.get_by_role("cell", name=mart, exact=True).first.click()
    t.wait(f"{mart} — ")
    t.settle()


def mart_state(mart):
    return json.loads(cli("lakehouse", "marts", "show", "--mart", mart, "--json"))["selected"]["state"]


def marts(t):
    """Step 7: each approved requirement proposed, merged (the approval), built through Dagster, reconciled."""
    for n, mart in enumerate(MARTS):
        first = n == 0
        open_mart(t, mart)
        if first:
            t.shot("45-mart-approved")
        t.action(f"Propose: {mart}")
        open_mart(t, mart)
        if first:
            t.shot("46-mart-proposed", full=True)
        t.action(f"Merge: {mart}", {"Note (optional)": "approved by the demo operator"},
                 confirm="You approve the generated model as shown", before="47-merge" if first else None)
        open_mart(t, mart)
        t.action(f"Build: {mart}")
        for _ in range(90):                         # Build returns once Dagster has the run
            if mart_state(mart) in ("built", "failed", "reconciled", "diverged"):
                break
            time.sleep(10)
        state = mart_state(mart)
        if state != "built":
            raise SystemExit(f"{mart}: {state} after the build")
        open_mart(t, mart)
        t.action(f"Reconcile: {mart}")
        open_mart(t, mart)
        t.shot(f"48-{mart}-reconciled", full=True)
    t.go("/w/{ws}/x/lakehouse/marts", "Marts (click one)")
    t.settle()
    t.shot("49-marts")
    t.go("/w/{ws}", "aria:workflow")
    t.shot("50-bar-done")


def finale(t):
    """The end state: documentation published, the bar, the dashboard and the graph view."""
    t.go("/w/{ws}/x/lakehouse/docs", "Home page")
    t.shot("51-docs-published")
    t.go("/w/{ws}", "aria:workflow")
    t.page.wait_for_timeout(25_000)               # the growth chart reads the whole ledger
    t.shot("52-dashboard-final")
    t.go("/w/{ws}/graph")
    t.page.wait_for_timeout(60_000)               # the graph view lays out the ledger's objects
    t.shot("53-graph")


PHASES = {"finale": finale, "marts": marts, "analyse": analyse, "reshoot1": reshoot1, "docs": docs, "review": review,
          "requirements": requirements, "answers": answers, "approve": approve, "extraction": extraction,
          "generate": generate, "load": load, "after_load": after_load}


def main():
    phase = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else HERE
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox"])
        # 1280x720 CSS pixels at 1.5x: 1920x1080 images in which the console's text reads like a
        # 1280-wide window (its content column is ~900 px; at 1920 CSS px it looks tiny in a video).
        page = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1.5)
        page.set_default_timeout(LONG)
        page.goto(BASE + "/")
        page.locator('[aria-label="console token"]').fill(TOKEN)
        page.get_by_role("button", name="Sign in").click()
        page.get_by_text("Add a workspace").wait_for(timeout=LONG)
        PHASES[phase](Tour(page, out))
        b.close()


if __name__ == "__main__":
    main()
