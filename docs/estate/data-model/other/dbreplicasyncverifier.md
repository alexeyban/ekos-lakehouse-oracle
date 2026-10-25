---
title: "DBREPLICASYNCVERIFIER"
order: 2
ekos_generated: true
ekos_estate_version: 1
---

# DBREPLICASYNCVERIFIER

Area [OTHER](../../data-model/other/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `LASTUPDATE` | DATE |  |  |  |  | 0 | 1 |

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
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [forbid_multiple_rows_in_dbreplicasyncverifier](../../logic/forbid_multiple_rows_in_dbreplicasyncverifier.md) |

## Written by

| kind | name |
|---|---|
| Trigger | `single_row_only_trigger_dbreplicasyncverifier` |

## Schema history

2 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2017-08-03T18:55 | i6.1z | `create_table` |  |  |
| 2017-08-03T18:55 | i6.1z | `create_table` |  |  |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.dbreplicasyncverifier.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
