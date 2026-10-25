---
title: "X_DEPOSITBATCH"
order: 2
ekos_generated: true
ekos_estate_version: 1
---

# X_DEPOSITBATCH

Area [X](../../data-model/x/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `C_BankAccount_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `C_DocType_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `Created` | TIMESTAMP |  | yes |  |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `CreateFrom` | CHAR(1) |  |  |  |  |  |  |
| `DateDeposit` | TIMESTAMP |  | yes |  |  |  |  |
| `DateDoc` | TIMESTAMP |  | yes |  |  |  |  |
| `DepositAmt` | NUMERIC |  | yes |  |  |  |  |
| `Description` | VARCHAR(255) |  |  |  |  |  |  |
| `DocStatus` | VARCHAR(2) |  | yes |  |  |  |  |
| `DocumentNo` | VARCHAR(30) |  | yes |  |  |  |  |
| `IsActive` | CHAR(1) |  | yes |  |  |  |  |
| `Processed` | CHAR(1) |  | yes |  |  |  |  |
| `Processing` | CHAR(1) |  |  |  |  |  |  |
| `Updated` | TIMESTAMP |  | yes |  |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `X_DepositBatch_ID` | NUMERIC(10) | PK | yes |  |  |  |  |
| `X_DepositBatch_UU` | VARCHAR(36) |  |  |  |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
|  | `IsActive IN ('Y', 'N')` |
|  | `Processed IN ('Y', 'N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Schema history

4 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2013-03-18T14:47 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2013-03-18T14:47 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2013-01-25T19:20 | i1.0a-i1.0b | `create_table` |  | TICKET-1001569 |
| 2013-01-25T19:20 | i1.0a-i1.0b | `create_table` |  | TICKET-1001569 |

## Notes

<!-- ekos:manual id="table.x_depositbatch.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
