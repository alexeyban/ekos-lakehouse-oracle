---
title: "ASU_1099BOX"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# ASU_1099BOX

Area [ASU](../../data-model/asu/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `ASU_1099Box_ID` | NUMERIC(10) | PK | yes |  |  |  |  |
| `ASU_1099Box_UU` | VARCHAR(36) |  |  |  |  |  |  |
| `Bucket` | NUMERIC(10) |  | yes |  |  |  |  |
| `Created` | TIMESTAMP |  | yes |  |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `Description` | VARCHAR(255) |  |  |  |  |  |  |
| `Help` | VARCHAR(2000) |  |  |  |  |  |  |
| `IsActive` | CHAR(1) |  | yes |  |  |  |  |
| `Name` | VARCHAR(60) |  | yes |  |  |  |  |
| `Updated` | TIMESTAMP |  | yes |  |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `Value` | VARCHAR(40) |  | yes |  |  |  |  |

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

## Read by

| kind | name |
|---|---|
| Procedure | [asu_get1099bucket](../../logic/asu_get1099bucket.md) |

## Schema history

4 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2013-03-18T13:30 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2013-03-18T13:30 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2013-03-04T16:19 | i1.0a-i1.0b | `create_table` |  | TICKET-1001763 |
| 2013-03-04T16:19 | i1.0a-i1.0b | `create_table` |  | TICKET-1001763 |

## Notes

<!-- ekos:manual id="table.asu_1099box.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
