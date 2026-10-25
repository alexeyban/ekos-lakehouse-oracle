# 2. Step 1 — Analyse the sources

```bash
ekos --project idemdocs build && ekos --project idemdocs recover && ekos --project idemdocs resolve \
  && ekos --project idemdocs compile && ekos --project idemdocs commit
```

No language model is involved: every stage prints `llm calls: 0` in its run log
([`docs/results/runs/`](../results/runs/), one JSON line per event, the last two lines of each file are the model-call
count and the result).

| Stage | Time | What it does here |
|---|---|---|
| build | 16 s | observes both git sources (cached when unchanged) and reads the live catalog: `DBA_TABLES`, `DBA_TAB_COLUMNS`, `DBA_CONSTRAINTS`, `DBA_SOURCE`, … inside a read-only transaction; profiles columns (counts) and reads iDempiere's `AD_Table` flags |
| recover | 262 s | Java (types, methods, the generated `I_`/`X_` model classes → application model), SQL in Java, Oracle and PostgreSQL DDL, PL/SQL and PL/pgSQL routines, 3,356 migration scripts → schema changes, docs pages, git history → tickets |
| resolve | 11 s | identity: merges exact duplicates, proposes fuzzy ones for review |
| compile | 32 s | the knowledge model, code ↔ database conflicts, write behaviour per table |
| commit | 495 s | the ledger, lineage from routines and views to tables, ticket links |

(These timings are the rerun after one column was added in Oracle — the run that made a sign-off stale in step 3.)

What the ledger holds afterwards: 1,261 `Table` objects (903 read live, the rest from DDL scripts and documents), 763 application-model
tables, 4,820 Java types and 31,434 methods, 515 routines with 7,623 statements, 1,209 views, 3,356 migration scripts
with 31,620 schema changes, 4,606 tickets, 655 documents with 3,004 sections, 446 conflicts.

Questions about it can be asked in plain language (`ekos ask`) or through MCP; the 25-question exit eval is in
[`docs/results/eval-idempiere-25.md`](../results/eval-idempiere-25.md).
