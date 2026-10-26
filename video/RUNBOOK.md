# Recording runbook — iDempiere, from analysis to reconciled marts

This is how to record the demo live, or re-take any scene of it. The narrated video in this folder was assembled
from screenshots of one real run of these steps (`RUNLOG.md` has its timeline, including what went wrong). The
narration for each scene is in `steps/<scene>/narration.txt`. Read it as written: every number in it is on screen
in that scene.

## Before recording

| Check | How |
|---|---|
| Oracle XE with the iDempiere seed is up | `docker ps` shows `ekos-oracle-xe-1` healthy; `testbed/idempiere-oracle.sh` ran once |
| The lakehouse sandbox is up and can reach Oracle | `docker compose -f src/ekos-lakehouse/deploy/docker-compose.lakehouse.yml ps`; Oracle connected to `ekos-lakehouse_default` |
| The binary has the Oracle driver | `ekos-lakehouse --version`; Instant Client on `LD_LIBRARY_PATH`; `EKOS_ORACLE_PASSWORD` set |
| A project for the take, with its own prefix | `ekos-lakehouse project add idemsales --source <idempiere>`; its `ekos.toml` is `project/ekos.toml` with `namespace-prefix = "bronze_sales_"`, `require-signoff = true`, `require-plan-approval = true`, `dagster-url = "http://127.0.0.1:53200"`, docs store `prefix = "Sales"` |
| The console is signed in | `ekos-lakehouse console start`; sign in with a token that has the write and review roles |
| A local model for step 4 | Ollama with `llama3` pulled. It is the only model call, so no metered provider is needed |
| Memory | Close everything else. Init & compile on a 15 GB laptop took 49 min while swapping. With 32 GB, expect about 15 min |
| Browser | 1280×720 window at 150 % zoom (what the screenshots used), or 1920×1080 at 100 % with the console zoomed to 150 % |

The slice is the 33 tables in `tour.py` (`SLICE`). Never load the whole 849-table scope on a laptop.

## Scenes

Scene numbers match `steps/`. Clicks go top to bottom. *Expected* is what must be on screen before you move on.

### 01 · Intro
Title card `cards/intro.png`. No console.

### 02 · The estate
Show `diagrams/project-map.png`, then `diagrams/source-er-keys.png`. Both are drawn from compiled facts. To
regenerate them after step 1, see *Diagrams* below.

### 03 · Step 1 — Analyse
1. **Sources** page: three sources (code checkout, docs site, Oracle). Click **Test connection** on the database.
   *Expected:* the live census (tables, views, routines).
2. Click **Init & compile** and confirm. The run page streams its stages. Cut here, or show it at 30 s and at
   about 6 min (recover).
3. When it finishes: *Expected:* every stage succeeded, **0 model calls**.
4. **Sources** → **Test connection** again. *Expected:* census = compiled (903 tables / 160 views / 62 routines on
   the testbed).
5. **Dashboard**. *Known:* the growth chart times out on a ledger this size (TODO). Don't wait for it.

### 04 · Step 2 — Documentation
1. **Lakehouse → Documentation**: **Generate**. *Expected:* the run succeeds; the page lists the generated pages.
2. **Preview publish** shows what would change in the store and sends nothing.
3. **Publish** only after step 3's scope is signed (the pages then cover the slice: 239 on the testbed).

### 05 · Step 3 — Scope
1. **Review**: six subjects, all *pending*.
2. **Commands** → filter `review scope` → paste every in-scope table outside the slice into *tables*. To get that
   list: `ekos-lakehouse --project idemsales review show scope --json`, take the rows proposed `in` that are not in
   `SLICE`. Tick **out**, reason "outside the order-to-invoice slice this lakehouse is built for", then **Run**.
3. Back on **Review**. The first load recomputes the review state, so allow a few minutes. Filter `C_ORDER` to show
   the slice.
4. Sign off **scope**: type `scope` in the confirm box, then **Sign off**. *Expected:* chip *valid*.

### 06 · Step 3 — Conflicts, identity, sign-off
1. **Conflicts**: open one blocking `mandatory_but_nullable` conflict. Reviewer `demo operator`; the note states the
   measured count (`tour.py: conflict_note`). Click **Both are valid**.
2. Settle the others the same way. Off camera, the CLI does it:
   `ekos-lakehouse --project idemsales conflicts resolve <id> --both-valid --note "…" --as "demo operator"`.
3. **Review → Conflicts**: sign off. **Identity**: select the one candidate, give a reason, click **Same thing**,
   then sign off.
4. Sign off **PII**, **Write behaviour** and **Glossary**. *Expected:* 6 of 6 signed; steps 4–7 unblocked.

### 07 · Step 5 — Extraction plan (before step 4: requirements need the deployed plan)
1. **Lakehouse → Plan**. **Extraction**: the table list with load mode, delete detection and masks.
2. Click `ADEMPIERE.C_ORDER`. *Expected:* "Why it loads this way" with evidence.
3. `ADEMPIERE.C_BPARTNER` → **Load in full**, reason "a small master table: reload it whole every run".
4. **Approve plan**: add a note, tick the confirm box. *Expected:* the plan shows *approved* with its digest.

### 08 · Generate, then step 4 — Requirements
1. **Lakehouse → Generate**. *Expected:* succeeds (the step-3 and step-5 gates pass).
2. Two marts from Markdown, off camera:
   `ekos-lakehouse --project idemsales lakehouse requirements draft --mart sales_by_month --file video/marts/sales_by_month.md --as "demo operator"`
   (and the same for `invoices_by_month`). On camera: **Requirements** → `sales_by_month`. *Expected:* every term
   resolved.
3. **Draft from text**: mart `region_category_sales`, text "net sales of completed customer orders by month, product
   category and the customer's region". *Expected:* the llama3 draft has unresolved terms and questions. The model's
   output can differ between takes. The answers below fit the recorded draft.

### 09 · Step 4 — Answers
1. Answer each question on the page with the buttons and inputs in `marts/answers.json`, then `marts/answers2.json`
   (the region path question appears after the first round).
2. **Approve** each of the three requirements: note, confirm box. *Expected:* three *approved*.

### 10 · Step 6 — Bronze and silver
1. **Lakehouse → Run the pipeline**, tick "Dagster runs the job now". Open Dagster (port 53200): the run, then
   the asset graph.
2. *Expected:* the run succeeds (testbed: 36 steps, about 5 min). Back on **Lakehouse**: the tables, and two
   accepted-values warnings (`C_DOCTYPE.DOCBASETYPE`, `C_PAYMENT.TRXTYPE`).
3. Silver lands in `silver_sales_adempiere`, gold in `gold_sales` (RFC 0231).

### 11 · Step 7 — Marts
For each of `sales_by_month`, `invoices_by_month`, `region_category_sales` on **Marts**: **Propose** → **Merge**
(note + confirm) → **Build** (wait for *built*) → **Reconcile**. *Expected:* *reconciled*, mart total = silver total
(testbed: 379.90 / 3 orders, 541.02 / 4, 358.40).

### 12 · Models and lineage
1. dbt docs: `dbt docs generate` in the Dagster container, serve `target/`, open the lineage graph.
2. Column lineage: `diagrams/lineage-*.png` (see *Diagrams*).

### 13 · Recap
**Dashboard**: the bar shows 1–7 done (6 partial: two code-list warnings), then the recap card.

## Diagrams

```bash
# the code map (aggregate graph export → Graphviz)
ekos-lakehouse --project idemsales graph export --level aggregate --group-by path-prefix --path-prefix-depth 1 > graph.json
python video/diagrams.py graph graph.json video/diagrams/project-map --top 20 --title "…"
# the slice's ER, from the deployed plan
python video/diagrams.py er <project>/pipeline/lakehouse.lock.json video/diagrams/source-er-keys \
  --highlight C_ORDER --highlight C_ORDERLINE --highlight C_INVOICE --highlight C_BPARTNER --skip-ref AD_CLIENT
# column lineage of a gold mart
PYTHONPATH=src/ekos-lakehouse/tools/lakehouse-docs \
  python video/lineage_diagram.py <project>/pipeline <lakehouse-docs out>/_evidence gold__sales_by_month \
  video/diagrams/lineage-sales_by_month
```

## Re-taking a scene

- **Scenes 03–04:** need nothing reset. A second Init & compile appends to the ledger.
- **Scenes 05–06:** review decisions are append-only. For a clean take, create a new project (`project add` under
  another name and prefix) and run step 1 again.
- **Scene 07:** a new plan approval supersedes the old one. Changing a table again records a new decision.
- **Scenes 08–09:** `requirements draft` on the same mart writes a new revision. Approvals bind the revision shown.
- **Scenes 10–11:** reruns are idempotent. Stop the Dagster schedules first
  (`python video/dagster_schedules.py --stop --cancel-runs`). The generated definitions start them switched on.

## Automating a take

`tour.py` drives every scene in a headless browser and saves the screenshots this video was cut from:

```bash
EKOS_CONSOLE_URL=http://127.0.0.1:<port> EKOS_CONSOLE_TOKEN_VALUE=<write+review token> \
EKOS_BIN=$(command -v ekos-lakehouse) TOUR_REPLACE="<local path>=<checkout>|<account>=user" \
  python video/tour.py analyse      # then docs, review, extraction, generate, requirements, answers, approve,
                                    # load, after_load, marts, finale
python video/make_steps.py          # screenshots + narration → steps/
```
