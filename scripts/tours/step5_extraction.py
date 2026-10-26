"""RFC 0226 Phase 3 exit: the Extraction page — a change with a reason, approval, step 5 on the bar."""
import json, os, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../src/EKOS/deploy/e2e"))
from package_browser_common import check, chromium, finish
from playwright.sync_api import sync_playwright, expect

BASE = os.environ.get("EKOS_CONSOLE_URL", "http://127.0.0.1:18765")
WS = os.environ.get("EKOS_WORKSPACE", "idemdocs")
OUT = sys.argv[1]
LONG = 120_000
TABLE = "ADEMPIERE.C_BPARTNER"
errors: list[str] = []
os.makedirs(OUT, exist_ok=True)


def shot(page, name):
    page.screenshot(path=os.path.join(OUT, f"{name}.png"), full_page=True)


def wait_run(page):
    page.wait_for_url("**/runs/**", timeout=LONG)
    run_id = page.url.rstrip("/").split("/")[-1]
    for _ in range(120):
        run = page.request.get(f"{BASE}/api/runs/{run_id}").json()
        if run["status"] not in ("queued", "running"):
            return run
        time.sleep(1)
    return run


def open_page(page, state):
    page.goto(f"{BASE}/w/{WS}/x/lakehouse/extraction")
    page.get_by_text("The plan", exact=True).wait_for(timeout=LONG)
    page.get_by_role("cell", name=TABLE, exact=True).wait_for(timeout=LONG)
    page.get_by_text(state, exact=True).first.wait_for(timeout=LONG)


with sync_playwright() as p:
    b = chromium(p)
    page = b.new_page(viewport={"width": 1600, "height": 1100})
    page.set_default_timeout(LONG)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(BASE + "/")
    page.locator('[aria-label="console token"]').fill(os.environ["EKOS_CONSOLE_TOKEN_VALUE"])
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Add a workspace").wait_for(timeout=LONG)
    open_page(page, "approved")
    body = page.inner_text("body")
    check("approved" in body, "the page shows the approved plan", body[:300])
    check("scope" in body and "signed off by" in body, "step 3 subjects used, with their sign-off")
    shot(page, "01-extraction-approved")

    # Pick the table: its evidence and columns appear.
    page.get_by_role("cell", name=TABLE, exact=True).click()
    page.get_by_text("Why it loads this way").wait_for(timeout=LONG)
    check(True, "a table's evidence is shown after a click")
    expect(page.get_by_role("cell", name="NAME", exact=True)).to_be_visible(timeout=LONG)
    shot(page, "02-table-selected")

    # A change with a reason.
    page.get_by_role("button", name=f"Load in full: {TABLE}").click()
    page.locator('[aria-label="Why (kept with the change)"]').fill("reload nightly while the order import is reworked")
    page.get_by_role("button", name="Run", exact=True).click()
    run = wait_run(page)
    check(run["status"] == "succeeded", "the change ran as the signed-in person", json.dumps({k: run.get(k) for k in ("status", "exit_code")}))
    shot(page, "03-change-run")
    open_page(page, "changed since the approval")
    body = page.inner_text("body")
    check("changed since the approval" in body, "the plan now differs from the approval", body[-1500:])
    check("reload nightly while the order import is reworked" in body, "the reason is shown with the change")
    shot(page, "04-changed")

    # Approve.
    page.get_by_role("button", name="Approve plan").click()
    page.locator('[aria-label="Note (optional)"]').fill("C_BPARTNER in full for now")
    run_btn = page.get_by_role("button", name="Run", exact=True)
    check(run_btn.is_disabled(), "approval waits for the acknowledgement")
    page.get_by_label("You approve the plan as shown").check()
    run_btn.click()
    run = wait_run(page)
    check(run["status"] == "succeeded", "the approval ran", json.dumps({k: run.get(k) for k in ("status", "exit_code")}))
    open_page(page, "approved")
    body = page.inner_text("body")
    check("approved" in body and "changed since the approval" not in body, "the plan is approved again", body[-1500:])
    bar = page.locator('[aria-label="workflow"]')
    bar.wait_for(timeout=LONG)
    text = bar.inner_text()
    check("Extraction" in text, "step 5 is on the bar", text[:300])
    shot(page, "05-approved-again")
    print("BAR:", text.replace("\n", " | ")[:600])
    b.close()
sys.exit(finish(errors))
