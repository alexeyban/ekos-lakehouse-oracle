"""RFC 0215 Phase 3 exit: the Requirements page — states, a change and its undo, a draft from
text answered and approved on the page, step 4 from the requirements."""
import json, os, subprocess, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../src/EKOS/deploy/e2e"))
from package_browser_common import check, chromium, finish
from playwright.sync_api import sync_playwright

BASE = os.environ.get("EKOS_CONSOLE_URL", "http://127.0.0.1:18765")
WS = os.environ.get("EKOS_WORKSPACE", "idemdocs")
OUT = sys.argv[1]
LONG = 120_000
MART = "category_region_sales"
NEW = "orders_per_customer"
REQ_DIR = os.environ["REQ_DIR"]
errors: list[str] = []
os.makedirs(OUT, exist_ok=True)


def shot(page, name):
    page.screenshot(path=os.path.join(OUT, f"{name}.png"), full_page=True)


def wait_run(page, limit=300):
    page.wait_for_url("**/runs/**", timeout=LONG)
    run_id = page.url.rstrip("/").split("/")[-1]
    for _ in range(limit):
        run = page.request.get(f"{BASE}/api/runs/{run_id}").json()
        if run["status"] not in ("queued", "running"):
            return run
        time.sleep(1)
    return run


def open_page(page, mart=None, state=None):
    page.goto(f"{BASE}/w/{WS}/x/lakehouse/requirements")
    page.get_by_text("Requirements (click one)").wait_for(timeout=LONG)
    page.get_by_role("cell", name=MART, exact=True).wait_for(timeout=LONG)
    if mart:
        page.get_by_role("cell", name=mart, exact=True).click()
        # The selected requirement's own heading: "<mart> — <state>".
        page.get_by_text(f"{mart} — ").first.wait_for(timeout=LONG)
    if state:
        page.get_by_text(f"{mart} — {state}").first.wait_for(timeout=LONG)


def run_action(page, button, inputs, confirm=None, limit=300):
    # Back on the page (after a run the console shows the run), the mart selected.
    open_page(page, button.split(": ", 1)[1] if ": " in button else None)
    page.get_by_role("button", name=button, exact=True).click()
    for label, value in inputs.items():
        page.locator(f'[aria-label="{label}"]').fill(value)
    if confirm:
        page.get_by_label(confirm).check()
    typed = page.locator('[aria-label^="type "][aria-label$=" to confirm"]')
    if typed.count() > 0:
        typed.fill(typed.get_attribute("aria-label")[len("type "):-len(" to confirm")])
    page.get_by_role("button", name="Run", exact=True).click()
    run = wait_run(page, limit)
    check(run["status"] == "succeeded", f"{button} ran", json.dumps({k: run.get(k) for k in ("status", "exit_code")}))
    return run


with sync_playwright() as p:
    b = chromium(p)
    page = b.new_page(viewport={"width": 1600, "height": 1100})
    page.set_default_timeout(LONG)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(BASE + "/")
    page.locator('[aria-label="console token"]').fill(os.environ["EKOS_CONSOLE_TOKEN_VALUE"])
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Add a workspace").wait_for(timeout=LONG)

    open_page(page, MART, "approved")
    body = page.inner_text("body")
    check("sales_by_month" in body, "both requirements are listed")
    check("joined via" in body and "C_REGION" in body, "the terms say how each resolved, with the chosen path")
    check("Approved by" in body, "the approval is shown")
    check("4 Requirements" in page.locator('[aria-label="workflow"]').inner_text(), "step 4 is on the bar")
    shot(page, "01-requirements-approved")

    # A change makes it differ from the approval; undoing it restores it.
    run_action(page, f"Add a filter: {MART}", {"Filter": "c_orderline.qtyordered > 0"})
    open_page(page, MART, "changed")
    shot(page, "02-changed")
    run_action(page, f"Remove a filter: {MART}", {"Filter, as written": "c_orderline.qtyordered > 0"})
    open_page(page, MART, "approved")
    check(True, "undoing the change makes it the approved requirement again")

    # A draft from text: the configured local model, then EKOS resolves it (once: a draft kept
    # from an earlier run of this script is the same evidence, and the model is slow).
    if not os.path.exists(os.path.join(REQ_DIR, f"{NEW}.md")):
        run_action(page, "Draft from text", {
            "Mart name (lowercase letters, digits, _)": NEW,
            "What should it show? (plain words)": "number of completed sales orders per customer and month",
        }, limit=400)
    open_page(page, NEW)
    body = page.inner_text("body")
    check("Drafted by llama3" in body, "the draft says which model wrote it", body[-800:])
    print("DRAFT:", body[body.find("Questions"):][:700] if "Questions" in body else "no questions")
    shot(page, "03-drafted-from-text")

    # The model's slips are answered on the page by the operator, never by the model.
    if "count_of_c_order_id: count of C_ORDER.ID" in body:
        run_action(page, f"Change a term: {NEW}", {"Term": "count_of_c_order_id", "New definition": "count of c_order"})
    if "- C_ORDER.DOCSTATUS = 'CO' (completed)" in body:
        run_action(page, f"Remove a filter: {NEW}", {"Filter, as written": "C_ORDER.DOCSTATUS = 'CO' (completed)"})
        run_action(page, f"Add a filter: {NEW}", {"Filter": "c_order.docstatus = 'CO'"})
    if "customer: C_BPARTNER.name\n" in body:
        run_action(page, f"Change a term: {NEW}", {"Term": "customer", "New definition": "c_bpartner.name via c_order.c_bpartner_id"})
    open_page(page, NEW)
    body = page.inner_text("body")
    print("AFTER ANSWERS:", body[body.find("Questions"):][:900] if "Questions" in body else "no questions")
    shot(page, "04-answered")
    if f"{NEW} — resolved" in body:
        run_action(page, f"Approve: {NEW}", {"Note (optional)": "approved in the browser"},
                   confirm="You approve this requirement as shown")
        open_page(page, NEW, "approved")
        shot(page, "05-approved")
    out = subprocess.run([os.environ["EKOS_BIN"], "--project", WS, "workflow", "status", "--json"],
                         capture_output=True, text=True).stdout
    step4 = [s for s in json.loads(out)["steps"] if s["n"] == 4][0]["detail"]
    print("STEP 4:", step4)
    check("3 of 3 requirement(s) approved" in step4, "step 4's detail comes from the requirements", step4)
    b.close()
sys.exit(finish(errors))
