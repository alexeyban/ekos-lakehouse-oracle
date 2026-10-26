# 5. Steps 4–7

These are [ekos-lakehouse](https://github.com/alexeyban/ekos-lakehouse)'s steps, built for this estate in EKOS RFCs
0215, 0225–0228. Each is a page of the console; [the book](../../book/index.md) shows every one with its screen and
run log.

| Step | What it does | On this testbed |
|---|---|---|
| 4 Requirements ([book](../../book/step-4.md)) | a mart described in plain words (drafted by local Ollama) or Markdown; EKOS resolves every term against the source model — columns, join paths along declared keys, filters — and asks the operator about the rest; approval records the digest | 4 marts approved; one drafted by `llama3` needed 9 answers, nothing invented |
| 5 Extraction ([book](../../book/step-5.md)) | per table: load mode from the application's watermark, delete detection (bucketed key diff, mass-delete guard), purged rows kept, masking from step 3; approval binds the plan | 715 incremental, 134 full, 1 refused (a number no Iceberg type holds), 53 out of scope |
| 6 Bronze and silver ([book](../../book/step-6.md)) | generated extraction SQL, dbt-trino silver with tests from the application's code lists and checks, a Dagster job | a 165-table subset; 3,664 of 3,667 tests pass, 3 data warnings |
| 7 Marts ([book](../../book/step-7.md)) | each approved requirement → a dbt gold model on a branch (merging is the approval), built through Dagster, each measure's total compared with silver's | 4 marts, every total equal (e.g. 379.90 = 379.90) |

The bar shows steps 4–7 behind step 3 because two review subjects are not signed: the gate is the product's and
was left as it is. With `[extensions.lakehouse] require-signoff = true`, the commands that write pipeline content
refuse to run until step 3 is complete.
