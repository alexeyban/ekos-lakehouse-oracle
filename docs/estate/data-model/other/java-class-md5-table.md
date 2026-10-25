---
title: "JAVA$CLASS$MD5$TABLE"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# JAVA$CLASS$MD5$TABLE

Area [OTHER](../../data-model/other/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 9 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `NAME` | VARCHAR2(200 CHAR) |  |  |  |  | 0 | 9 |
| `MD5` | RAW(16) |  |  |  |  | 0 | 9 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Write behaviour

- updates: **no_updated_column**
- deletes: **never_deleted_in_code**
- change log: **unknown**
- evidence: 0 citation(s)

## Schema history

1 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.java-class-md5-table.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
