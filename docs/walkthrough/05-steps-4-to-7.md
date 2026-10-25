# 5. Steps 4–7 — not part of this demo yet

| Step | What it will do | State |
|---|---|---|
| 4 Requirements | reports described in Markdown or plain language → mart metadata, every term checked against the signed model | `blocked` until every subject is signed |
| 5 Extraction and landing | per table: load mode, delete handling, type mapping, masking from the PII review | `blocked` |
| 6 Bronze and silver | generated SQL, dbt models, orchestration, reconciliation with a planted control | `blocked` |
| 7 Marts | gold models from the approved metadata, tests, measure reconciliation | `blocked` |

These are [ekos-lakehouse](https://github.com/alexeyban/ekos-lakehouse)'s steps. Its commands that write pipeline
content (`generate`, `sync`, `gold draft`) refuse to run while the source model is not signed off when the project
sets `[extensions.lakehouse] require-signoff = true` — on this testbed, `lakehouse sync` refused, naming the five
unsigned subjects. The Oracle source engine for them is planned (EKOS RFC 0216).
