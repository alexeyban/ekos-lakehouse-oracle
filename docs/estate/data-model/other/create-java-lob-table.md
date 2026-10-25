---
title: "CREATE$JAVA$LOB$TABLE"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# CREATE$JAVA$LOB$TABLE

Area [OTHER](../../data-model/other/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 8 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `NAME` | VARCHAR2(700 CHAR) |  |  |  |  | 0 | 8 |
| `LOB` | BLOB |  |  |  |  | 0 | 0 |
| `LOADTIME` | DATE |  |  |  |  | 0 | 1 |

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

<!-- ekos:manual id="table.create-java-lob-table.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
