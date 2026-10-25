---
title: "C_DEPARTMENT"
order: 74
ekos_generated: true
ekos_estate_version: 1
---

# C_DEPARTMENT

Area [C](../../data-model/c/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_C_Department`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_Department_ID` | NUMERIC(10) | PK | yes | Department |  |  |  |
| `C_Department_UU` | VARCHAR(36) |  |  | Department UU |  |  |  |
| `Created` | TIMESTAMP |  |  | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  |  | Created By |  |  |  |
| `IsActive` | CHAR(1) |  | yes | Active |  |  |  |
| `Name` | VARCHAR(60) |  |  | Name |  |  |  |
| `Updated` | TIMESTAMP |  |  | Updated |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  |  | Updated By |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
|  | `IsActive IN ('Y', 'N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Schema history

12 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-05-14T13:59 | iD13 | `create_table` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `modify_column` | Value | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `modify_column` | Value | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `modify_column` | Value | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `create_table` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | Value | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | AD_Org_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | AD_Client_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | AD_Org_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | AD_Client_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | Value | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `modify_column` | Value | IDEMPIERE-5598 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.c_department.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
