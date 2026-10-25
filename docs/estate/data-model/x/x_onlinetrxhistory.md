---
title: "X_ONLINETRXHISTORY"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# X_ONLINETRXHISTORY

Area [X](../../data-model/x/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `AD_Table_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `Created` | TIMESTAMP |  | yes |  |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `IsActive` | CHAR(1) |  | yes |  |  |  |  |
| `IsError` | CHAR(1) |  | yes |  |  |  |  |
| `Record_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `TextMsg` | VARCHAR(2000) |  |  |  |  |  |  |
| `Updated` | TIMESTAMP |  | yes |  |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `X_OnlineTrxHistory_ID` | NUMERIC(10) | PK | yes |  |  |  |  |
| `X_OnlineTrxHistory_UU` | VARCHAR(36) |  |  |  |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
|  | `IsActive IN ('Y', 'N')` |
|  | `IsError IN ('Y', 'N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Schema history

6 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2013-03-18T15:43 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2013-03-18T15:43 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2012-11-01T20:11 | i1.0a-i1.0b | `create_table` |  | IDEMPIERE-462 |
| 2012-11-01T20:11 | i1.0a-i1.0b | `create_table` |  | IDEMPIERE-462 |
| 2012-11-01T20:11 | i1.0a-i1.0b | `add_column` | Processed | IDEMPIERE-462 |
| 2012-11-01T20:11 | i1.0a-i1.0b | `add_column` | Processed | IDEMPIERE-462 |

## Notes

<!-- ekos:manual id="table.x_onlinetrxhistory.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
