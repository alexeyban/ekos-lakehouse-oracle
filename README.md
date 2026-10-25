# EKOS on a legacy Oracle estate: iDempiere

A worked demo of [EKOS](https://github.com/alexeyban/EKOS) — a compiler for enterprise knowledge — on
[iDempiere](https://github.com/idempiere/idempiere), an open-source ERP with 900 tables, 20 years of migration
scripts, PL/SQL and a large Java code base, running on Oracle. It covers the first three steps of the
[EKOS Lakehouse](https://github.com/alexeyban/ekos-lakehouse) operator workflow: analyse the sources, document them,
and have a person review and sign off the source model before anything is built on it.

**No language model was used in any of it.** Every number below comes from a measured run on one laptop.

| Step | | State in this demo |
|---|---|---|
| 1 | Analyse sources — code, docs site, live Oracle catalog into one ledger, from the console's Sources tab | done (census = compiled) |
| 2 | Documentation — [**1,060 generated pages**](docs/estate/index.md) | done (in this repository) |
| 3 | Review and sign-off — six subjects, sign-off bound to a digest | 4 of 6 signed; 195 conflicts and 1 identity match await a person |
| 4–7 | Requirements, extraction, bronze/silver, marts | blocked until step 3 is complete |

## Start here

- **The documentation EKOS generated:** [docs/estate](docs/estate/index.md) — e.g. the
  [data model](docs/estate/data-model/index.md), [C_ORDER](docs/estate/data-model/c/c_order.md), a
  [routine](docs/estate/logic/acctbalance.md), the [findings](docs/estate/findings/index.md).
- **How it was made, step by step:**
  1. [The testbed](docs/walkthrough/01-testbed.md) — iDempiere 12's seed on Oracle XE in Docker
  2. [Step 1 — analyse](docs/walkthrough/02-analyse.md)
  3. [Step 2 — documentation](docs/walkthrough/03-documentation.md)
  4. [Step 3 — review and sign-off](docs/walkthrough/04-review-and-sign-off.md)
  5. [Steps 4–7](docs/walkthrough/05-steps-4-to-7.md)
- **Measurements:** [docs/results](docs/results/README.md) — database census, run logs, review state, a 25-question eval.

![The review in the EKOS console](docs/images/review-pii.png)

## What EKOS found, in numbers

| | |
|---|---|
| database (Oracle XE 21c, iDempiere 12 seed) | 903 tables, 160 views, 62 routines, 3,686 foreign keys, 12,958 check constraints |
| code | 4,820 Java types, 31,434 methods; 763 generated model classes read as the application model |
| history | 3,356 migration scripts → 31,620 schema changes; 4,606 tickets from commit history |
| code ↔ database disagreements | 446 (e.g. a model column the database lacks, a mandatory column the database allows null) |
| write behaviour | per table: how rows are updated and deleted, and whether the change log records it |
| pipeline | build 16 s · recover 4 min 22 s · resolve 11 s · compile 32 s · commit 8 min 15 s · 0 model calls |
| documentation | 1,060 pages in 26 s |

## What is deliberately not here

No data values (profiles contribute counts only), no text from the iDempiere documentation site (it has no licence
file), no ledger and no credentials. See [NOTICE.md](NOTICE.md).

## Reproduce

```bash
docker compose -p ekos -f testbed/docker-compose.oracle.yml up -d
testbed/idempiere-oracle.sh
export EKOS_ORACLE_PASSWORD=ekos-ro-local-only
# build EKOS with --features oracle, create the project from project/ekos.toml, run the pipeline, then:
scripts/regenerate-docs.sh idemdocs
```

Licence: GPL-2.0 (the generated documentation derives from iDempiere's GPL-2.0 code); files copied from EKOS keep
their MIT notice — see [NOTICE.md](NOTICE.md).
