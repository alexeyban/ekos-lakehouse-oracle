# Steps 4–7 on the testbed

Exported 2026-10-26 from the project with the same read commands the console's pages use (`lakehouse requirements|extraction|marts show --json`, `workflow status --json`). The JSON files next to this page are those exports; local paths and the account name are shortened.

## The bar

| Step | State | Detail |
|---|---|---|
| 1 Analyse sources | done | fresh — ledger reflects the source as of 2026-10-25 16:56 UTC (git 3355eb5) |
| 2 Documentation | done | 1060 page(s) generated 2026-10-26T18:23:14Z, published 2026-10-26T18:23:52Z to https://github.com/alexeyban/ekos-lakehouse-oracle/wiki |
| 3 Review and sign-off | partial | 4 of 6 subjects signed, 196 blocking item(s) |
| 4 Requirements | blocked | needs a valid sign-off of every review subject (step 3); 4 of 4 requirement(s) approved |
| 5 Extraction and landing | blocked | needs a valid sign-off of every review subject (step 3); plan approved by operator at 2026-10-26T08:46:34Z: 715 incremental, 134 full, 1 refused, 53 out of scope |
| 6 Bronze and silver | blocked | needs a valid sign-off of every review subject (step 3); 325 bronze/silver table(s) built, 142 failing |
| 7 Marts | blocked | needs a valid sign-off of every review subject (step 3); 4 of 4 mart(s) reconciled |

Steps 4–7 show *blocked* because step 3 is not fully signed (195 conflicts and one identity match wait for a person); each was built and run behind that gate.

## Step 4 — requirements ([requirements.json](steps-4-to-7/requirements.json))

| Mart | State | Terms | Questions | Described as |
|---|---|---|---|---|
| `category_region_sales` | approved | 6 | 0 | text |
| `invoices_by_month` | approved | 5 | 0 | file |
| `orders_per_customer` | approved | 5 | 0 | text |
| `sales_by_month` | approved | 6 | 0 | file |

Two were described as Markdown, two in plain words. The plain-word ones were drafted by local `llama3` and answered by the operator before approval — one needed nine answers (EKOS RFC 0215). The model never answers a question.

## Step 5 — the extraction plan ([extraction-plan.json](steps-4-to-7/extraction-plan.json))

| Tables | Count |
|---|---|
| incremental on `UPDATED`, deletes looked for every run | 665 |
| incremental, deletes audited weekly | 50 |
| full | 134 |
| refused (a number no Iceberg type holds) | 1 |
| out of scope (step 3) | 53 |
| masked columns (step 3's PII) | 1 |
| operator changes | 2 |

Approved by operator at 2026-10-26T08:46:34Z, digest `03d5fce4e39fa6f0`.

## Step 6 — bronze and silver

The full 849-table load was not run on this 15 GB laptop (the maintainer's decision, EKOS RFC 0227). A closed 165-table subset was loaded through one-shot Dagster runs and its dbt tests run with `--indirect-selection cautious --threads 2`: **3,664 of 3,667 pass**, 3 data warnings.

The bar's "142 failing" is the latest result the ledger holds per silver table, all from one earlier run (2026-10-26 08:36 UTC): 119 relationship tests whose other table is outside the loaded subset (`TABLE_NOT_FOUND`), and 23 cut off when Trino ran out of memory under four dbt threads. The cautious re-run above was not reported back into the ledger.

## Step 7 — marts

| Mart | Measure | Mart total | Silver total | |
|---|---|---|---|---|
| [`sales_by_month`](steps-4-to-7/mart-sales_by_month.json) | `total` | 379.90 | 379.90 | equal |
| [`sales_by_month`](steps-4-to-7/mart-sales_by_month.json) | `orders` | 3 | 3 | equal |
| [`category_region_sales`](steps-4-to-7/mart-category_region_sales.json) | `sales` | 358.40 | 358.40 | equal |
| [`orders_per_customer`](steps-4-to-7/mart-orders_per_customer.json) | `count_of_c_order_id` | 7 | 7 | equal |
| [`invoices_by_month`](steps-4-to-7/mart-invoices_by_month.json) | `invoiced` | 541.02 | 541.02 | equal |
| [`invoices_by_month`](steps-4-to-7/mart-invoices_by_month.json) | `invoices` | 4 | 4 | equal |

Each mart: proposed from its approved requirement (nothing invented), merged (the approval), built through Dagster, reconciled. The generated SQL is in [`pipeline/dbt/models/gold/`](../../pipeline/dbt/models/gold/), the requirements in [`pipeline/marts/`](../../pipeline/marts/).
