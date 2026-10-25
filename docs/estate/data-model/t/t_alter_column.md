---
title: "T_ALTER_COLUMN"
order: 3
ekos_generated: true
ekos_estate_version: 1
---

# T_ALTER_COLUMN

Area [T](../../data-model/t/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `tablename` | name |  |  |  |  |  |  |
| `columnname` | name |  |  |  |  |  |  |
| `datatype` | name |  |  |  |  |  |  |
| `nullclause` | VARCHAR(10) |  |  |  |  |  |  |
| `defaultclause` | VARCHAR(200) |  |  |  |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Notes

<!-- ekos:manual id="table.t_alter_column.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
