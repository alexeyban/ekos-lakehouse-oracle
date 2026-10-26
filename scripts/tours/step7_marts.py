"""RFC 0228 Phase 2 exit: a mart from approved to reconciled on the Marts page."""
import json, os, subprocess, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../src/EKOS/deploy/e2e"))
from package_browser_common import check, chromium, finish
from playwright.sync_api import sync_playwright

BASE = os.environ.get("EKOS_CONSOLE_URL", "http://127.0.0.1:18765")
WS = os.environ.get("EKOS_WORKSPACE", "idemdocs")
OUT = sys.argv[1]
LONG = 120_000
MART = "invoices_by_month"
errors: list[str] = []
os.makedirs(OUT, exist_ok=True)


def shot(page, name):
    page.screenshot(path=os.path.join(OUT, f"{name}.png"), full_page=True)


def wait_run(page, limit=600):
    page.wait_for_url("**/runs/**", timeout=LONG)
    run_id = page.url.rstrip("/").split("/")[-1]
    for _ in range(limit):
        run = page.request.get(f"{BASE}/api/runs/{run_id}").json()
        if run["status"] not in ("queued", "running"):
            return run
        time.sleep(1)
    return run


def open_page(page, state=None):
    page.goto(f"{BASE}/w/{WS}/x/lakehouse/marts")
    page.get_by_text("Marts (click one)").wait_for(timeout=LONG)
    page.get_by_role("cell", name=MART, exact=True).click()
    page.get_by_text(f"{MART} — {state or ''}").first.wait_for(timeout=LONG)


def until_state(page, state, minutes=10):
    """Build launches a Dagster run and returns: reload the page until the mart gets there."""
    for _ in range(minutes * 6):
        page.goto(f"{BASE}/w/{WS}/x/lakehouse/marts")
        page.get_by_role("cell", name=MART, exact=True).click()
        page.get_by_text(f"{MART} — ").first.wait_for(timeout=LONG)
        if any(page.get_by_text(f"{MART} — {x}").count() > 0 for x in state.split("|")):
            return True
        time.sleep(10)
    return False


def run_action(page, button, inputs=None, confirm=None, state=None):
    open_page(page, state)
    page.get_by_role("button", name=f"{button}: {MART}", exact=True).click()
    for label, value in (inputs or {}).items():
        page.locator(f'[aria-label="{label}"]').fill(value)
    if confirm:
        page.get_by_label(confirm).check()
    typed = page.locator('[aria-label^="type "][aria-label$=" to confirm"]')
    if typed.count() > 0:
        typed.fill(typed.get_attribute("aria-label")[len("type "):-len(" to confirm")])
    page.get_by_role("button", name="Run", exact=True).click()
    run = wait_run(page)
    check(run["status"] == "succeeded", f"{button} ran", json.dumps({k: run.get(k) for k in ("status", "exit_code")}))


with sync_playwright() as p:
    b = chromium(p)
    page = b.new_page(viewport={"width": 1600, "height": 1100})
    page.set_default_timeout(LONG)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(BASE + "/")
    page.locator('[aria-label="console token"]').fill(os.environ["EKOS_CONSOLE_TOKEN_VALUE"])
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Add a workspace").wait_for(timeout=LONG)

    out = subprocess.run([os.environ["EKOS_BIN"], "--project", WS, "lakehouse", "marts", "show", "--json"],
                         capture_output=True, text=True).stdout
    start = [m for m in json.loads(out)["marts"] if m["mart"] == MART][0]["state"]
    print("STARTS AT:", start)
    open_page(page, start)
    body = page.inner_text("body")
    check("sales_by_month" in body and "reconciled" in body, "the earlier marts are listed as reconciled")
    page.get_by_text("Approved requirement").first.wait_for(timeout=LONG)
    check(True, "the requirement is shown beside the SQL")
    shot(page, "01-start")
    if start == "to propose":
        run_action(page, "Propose", state="to propose")
        start = "proposed"
    if start == "proposed":
        open_page(page, "proposed")
        check("GRANDTOTAL" in page.inner_text("body"), "the generated SQL is shown")
        shot(page, "02-proposed")
        run_action(page, "Merge", {"Note (optional)": "merged in the browser"},
                   confirm="You approve the generated model as shown", state="proposed")
        open_page(page, "merged")
        shot(page, "03-merged")
    if start in ("to propose", "proposed", "merged"):
        run_action(page, "Build", state="merged")
    check(until_state(page, "built|reconciled"), "the build reaches the page")
    shot(page, "04-built")

    if start != "reconciled":
        run_action(page, "Reconcile", state="built")
    open_page(page, "reconciled")
    page.get_by_role("cell", name="equal").first.wait_for(timeout=LONG)
    page.get_by_text("Lineage").wait_for(timeout=LONG)
    page.locator("text=loading…").first.wait_for(state="detached", timeout=LONG)
    body = page.inner_text("body")
    check("equal" in body and "Mart total" in body, "both totals are shown per measure")
    check("Lineage" in body and "C_INVOICE" in body, "the lineage shows the silver table")
    check("exact" in body, "each term's fidelity is shown")
    shot(page, "05-reconciled")
    out = subprocess.run([os.environ["EKOS_BIN"], "--project", WS, "workflow", "status", "--json"],
                         capture_output=True, text=True).stdout
    step7 = [s for s in json.loads(out)["steps"] if s["n"] == 7][0]["detail"]
    print("STEP 7:", step7)
    check("4 of 4 mart(s) reconciled" in step7, "step 7 comes from the marts", step7)
    b.close()
sys.exit(finish(errors))
