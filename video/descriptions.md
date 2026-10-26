# Publishing kit

Video: `ekos-idempiere-end-to-end.mp4` (7:52, 1920×1080, English narration, subtitles in
`ekos-idempiere-end-to-end.srt`), on the release
[video-2026-10-27](https://github.com/alexeyban/ekos-lakehouse-oracle/releases/tag/video-2026-10-27). Thumbnail:
`thumbnail.png`. `[link]` below is where the video ends up once uploaded (YouTube / LinkedIn); until then use the
release link.

## YouTube

**Title (88):** EKOS on iDempiere: from a legacy Oracle ERP to reconciled gold marts — one real run, end to end

**Description:**

A legacy ERP — iDempiere on Oracle, 903 tables, 20 years of migration scripts, a large Java code base — taken from
analysis to gold marts in the EKOS console. One real run, recorded step by step, including what went wrong.

EKOS is a compiler for enterprise knowledge: it reads code, documents and the live database catalog, compiles them
into an append-only ledger where every conclusion carries its evidence, and never lets a language model read the
sources. EKOS Lakehouse turns that model into an Iceberg lakehouse: bronze, silver with dbt, gold marts through
Dagster.

What you'll see:
• Step 1: Init & compile from the console, 0 model calls; the census of the live database equals what was compiled
  (903 tables / 160 views / 62 routines)
• Step 2: 239 documentation pages generated from the ledger and published to a wiki
• Step 3: a person reviews and signs off: scope narrowed to a 33-table order-to-invoice slice, 17 code-vs-database
  conflicts settled with measured counts, 6 of 6 subjects signed
• Step 5: the extraction plan with evidence for each table, one change with a reason, approved
• Step 4: two marts described in Markdown; one in plain words, drafted by a local model, with every term resolved
  against the approved model and the rest asked back to the operator
• Step 6: bronze and silver through Dagster: 36 steps in 5 minutes, 895 checks
• Step 7: three gold marts proposed, approved, built and reconciled: each total equals silver's
• Column lineage from the Oracle column to the gold measure, read from the generated SQL

Two product defects were found during the recording and fixed before it went on: silver and gold schemas shared
between projects, and column lineage lost on Oracle's upper-case names.

Stack: Oracle XE · Trino · Apache Iceberg (Polaris) · dbt · Dagster · Ollama (llama3, local) · EKOS console

Chapters:
0:00 EKOS on a legacy ERP
0:42 The estate: code and database
1:15 Step 1 — Analyse the sources
1:58 Step 2 — Documentation
2:29 Step 3 — Review: scope
3:05 Step 3 — Conflicts, identity and sign-off
3:40 Step 5 — The extraction plan
4:16 Generate, then step 4 — describe the marts
4:56 Step 4 — The operator answers; nothing is invented
5:25 Step 6 — Bronze and silver through Dagster
6:06 Step 7 — Marts: propose, merge, build, reconcile
6:42 Models, transformations and lineage
7:12 What we got

Still open: two code values outside the application's lists in silver; the dashboard's growth chart times out on a
ledger this size; the step bar suggests requirements before the plan they need. A 33-table slice, not the 849-table
scope, on one 15 GB laptop.

Everything — code at the exact commits, the generated pipeline, containers, run log, runbook:
https://github.com/alexeyban/ekos-lakehouse-oracle
EKOS: https://github.com/alexeyban/EKOS · EKOS Lakehouse: https://github.com/alexeyban/ekos-lakehouse

The narration is synthetic (local text-to-speech, Piper). Every screen is from the run.

#dataengineering #lakehouse #dbt #dagster #iceberg #oracle #legacymodernization #erp

## LinkedIn

From a 20-year-old Oracle ERP to reconciled gold marts, in one recorded run. No language model ever reads the sources.

I took iDempiere (903 tables, Java, PL/SQL, two decades of migration scripts) through the seven steps of the EKOS
workflow in the web console and recorded every screen. It is not the happy path: the run log keeps what went wrong.

🔍 Analysis of code, documents and the live catalog: 0 model calls, and the database census equals what was compiled
🧑‍⚖️ A person signs off the source model: 17 code-vs-database conflicts settled with measured row counts
🧾 A mart described in plain words: the local model's draft had two terms that didn't resolve, and they went back to
the operator, not the model
✅ Three gold marts built through Dagster and reconciled: each total equals silver's

The recording found two product defects (two projects sharing silver/gold schemas; lineage lost on Oracle's upper-case
names). Both were fixed in the open, and the run log says so.

Stack: Oracle · Trino · Iceberg · dbt · Dagster · Ollama.

Video, code at the exact commits, pipeline, runbook: https://github.com/alexeyban/ekos-lakehouse-oracle

#dataengineering #lakehouse #dbt #legacymodernization #oracle

## X — single post

iDempiere on Oracle → Iceberg gold marts, one real run in the EKOS console: 0 model calls to analyse 903 tables, a person signs off the model, a plain-words mart resolved with nothing invented, 3 marts reconciled to silver. Oracle·Trino·dbt·Dagster [link]

## X — thread

1/ A legacy Oracle ERP (iDempiere, 903 tables, 20 years of migrations) taken to reconciled gold marts in one recorded run of the EKOS console. Every screen real, every number on screen. 🧵 [link]

2/ Step 1: code, docs and the live catalog compiled into one ledger. 0 model calls. Then the census of the database equals what was compiled: 903 tables, 160 views, 62 routines.

3/ Step 3 is a person's job. Scope narrowed to a 33-table order-to-invoice slice; 17 conflicts where the app says mandatory and the DB allows NULL, each settled with the measured row count. 6 of 6 subjects signed.

4/ One mart in plain words, drafted by a local llama3. Two terms didn't resolve against the approved model, so the questions went to the operator, never back to the model. Nothing invented.

5/ Bronze + silver through Dagster: 36 steps in 5 min, 895 checks. Three gold marts proposed, approved, built and reconciled: 379.90 = 379.90, 541.02 = 541.02, 358.40 = 358.40.

6/ Two defects found while recording, fixed in the open: projects sharing silver/gold schemas, and lineage lost on Oracle's upper-case names. Still open: 2 unknown code values, a slow dashboard chart. Repo: https://github.com/alexeyban/ekos-lakehouse-oracle
