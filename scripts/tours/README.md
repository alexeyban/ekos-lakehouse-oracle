# Browser tours — each step driven in the console

Each script drives one step of the workflow in Chromium (Playwright) against a running console, checks what the
page shows, and saves screenshots. They are how each step's RFC was accepted on this testbed; the results are in
[`docs/results/README.md`](../../docs/results/README.md).

| Script | Step | What it does to the project | Result on the testbed |
|---|---|---|---|
| `step1_sources.py` | 1 | adds directories and the database, tests it, runs Init & compile (a full analysis) | 11/11; census = compiled (RFC 0223) |
| `step2_documentation.py` | 2 | Generate and Preview publish; never Publish | 17/17 (RFC 0230) |
| `step3_review.py` | 3 | decides one scope item, signs four subjects off | 18/18 (RFC 0213) |
| `step4_requirements.py` | 4 | a filter added and removed; a mart drafted from text by local `llama3`, answered, approved | 14/14 (RFC 0215) |
| `step5_extraction.py` | 5 | a load-mode change with a reason; the plan approved | 11/11 (RFC 0226) |
| `step7_marts.py` | 7 | Propose, Merge, Build (Dagster), Reconcile one mart | 8/8 (RFC 0228) |

```bash
pip install playwright && python -m playwright install chromium
export EKOS_CONSOLE_URL=http://127.0.0.1:8765 EKOS_CONSOLE_TOKEN_VALUE=<a token with the write role>
export EKOS_WORKSPACE=idemdocs EKOS_BIN=$(command -v ekos-lakehouse)
python scripts/tours/step2_documentation.py shots/
```

These change the project (decisions, approvals, a build): run them on a testbed. Step 6 has no tour: its load ran as
one-shot Dagster runs of a 165-table subset (RFC 0227). The tours use EKOS's shared browser helpers from
`src/EKOS/deploy/e2e`.
