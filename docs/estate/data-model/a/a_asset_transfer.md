---
title: "A_ASSET_TRANSFER"
order: 24
ekos_generated: true
ekos_estate_version: 1
---

# A_ASSET_TRANSFER

Area [A](../../data-model/a/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_A_Asset_Transfer`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `A_ASSET_ACCT_ID` | NUMBER(10,0) |  |  | A_Asset_Acct_ID |  | 0 | 0 |
| `A_ASSET_TRANSFER_ID` | NUMBER(10,0) | PK | yes | A_Asset_Transfer_ID |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `A_ACCUMDEPRECIATION_ACCT` | NUMBER(10,0) |  |  | Accumulated Depreciation Account |  | 0 | 0 |
| `A_ASSET_ACCT_NEW` | VARCHAR2(22 CHAR) |  |  |  |  | 0 | 0 |
| `A_DEPRECIATION_ACCT` | NUMBER(10,0) |  |  | Depreciation Account |  | 0 | 0 |
| `A_DEPRECIATION_ACCT_STR` | VARCHAR2(40 CHAR) |  |  | A_Depreciation_Acct_Str |  | 0 | 0 |
| `A_DISPOSAL_LOSS_NEW` | VARCHAR2(22 CHAR) |  |  |  |  | 0 | 0 |
| `A_TRANSFER_BALANCE_IS` | CHAR(1) |  | yes | A_Transfer_Balance_IS |  | 0 | 0 |
| `A_TRANSFER_BALANCE` | CHAR(1) |  | yes | A_Transfer_Balance |  | 0 | 0 |
| `A_SPLIT_PERCENT` | NUMBER |  | yes | Split Percent |  | 0 | 0 |
| `A_PERIOD_START` | NUMBER(10,0) |  | yes | A_Period_Start |  | 0 | 0 |
| `A_PERIOD_END` | NUMBER(10,0) |  | yes | A_Period_End |  | 0 | 0 |
| `A_DISPOSAL_REVENUE_STR` | VARCHAR2(40 CHAR) |  |  | Disposal Revenue Str |  | 0 | 0 |
| `A_DISPOSAL_REVENUE_NEW` | VARCHAR2(22 CHAR) |  |  |  |  | 0 | 0 |
| `A_DISPOSAL_REVENUE` | NUMBER(10,0) |  |  | Disposal Revenue |  | 0 | 0 |
| `A_DISPOSAL_LOSS_STR` | VARCHAR2(40 CHAR) |  |  | Disposal Loss Str |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  | yes | Process Now |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `POSTINGTYPE` | CHAR(1) |  | yes | Posting Type |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `DATEACCT` | DATE |  | yes | Account Date |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `C_PERIOD_ID` | NUMBER(10,0) |  |  | Period | [C_PERIOD](../../data-model/c/c_period.md) | 0 | 0 |
| `C_ACCTSCHEMA_ID` | NUMBER(10,0) |  | yes | Accounting Schema | [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | 0 | 0 |
| `A_DISPOSAL_LOSS` | NUMBER(10,0) |  |  | Loss on Disposal |  | 0 | 0 |
| `A_DEPRECIATION_ACCT_NEW` | VARCHAR2(22 CHAR) |  |  |  |  | 0 | 0 |
| `A_ASSET_ID` | NUMBER(10,0) |  | yes | Asset | [A_ASSET](../../data-model/a/a_asset.md) | 0 | 0 |
| `A_ASSET_ACCT_STR` | VARCHAR2(40 CHAR) |  |  | A_Asset_Acct_Str |  | 0 | 0 |
| `A_ACCUMDEPRECIATION_ACCT_NEW` | VARCHAR2(22 CHAR) |  |  |  |  | 0 | 0 |
| `A_ACCUMDEPRECIATION_ACCT_STR` | VARCHAR2(40 CHAR) |  |  | Old Asset Cost Acct |  | 0 | 0 |
| `A_ASSET_ACCT` | NUMBER(10,0) |  |  | Asset Acct |  | 0 | 0 |
| `A_ASSET_TRANSFER_UU` | VARCHAR2(36 CHAR) |  |  | A_Asset_Transfer_UU |  | 0 | 0 |
| `A_ACCUMDEPRECIATION_NEW_ACCT` | NUMBER(10,0) |  | yes | Accumulated Depreciation Account (new) |  | 0 | 0 |
| `A_DEPRECIATION_NEW_ACCT` | NUMBER(10,0) |  | yes | Depreciation Acct (new) |  | 0 | 0 |
| `A_DISPOSAL_LOSS_ACCT` | NUMBER(10,0) |  |  | Disposal Loss Acct |  | 0 | 0 |
| `A_DISPOSAL_REVENUE_NEW_ACCT` | NUMBER(10,0) |  | yes | Disposal Revenue Acct (new) |  | 0 | 0 |
| `A_DISPOSAL_REVENUE_ACCT` | NUMBER(10,0) |  |  | Disposal Revenue Acct |  | 0 | 0 |
| `A_DISPOSAL_LOSS_NEW_ACCT` | NUMBER(10,0) |  | yes | Disposal Loss Acct (new) |  | 0 | 0 |
| `A_ASSET_NEW_ACCT` | NUMBER(10,0) |  | yes | Asset Acct (new) |  | 0 | 0 |
| `DOCACTION` | CHAR(2) |  | yes | Document Action |  | 0 | 0 |
| `DOCSTATUS` | VARCHAR2(2 CHAR) |  | yes | Document Status |  | 0 | 0 |
| `POSTED` | CHAR(1) |  |  | Posted |  | 0 | 0 |
| `A_CAPVSEXP` | VARCHAR2(3 CHAR) |  | yes | Capital/Expense |  | 0 | 0 |
| `A_ACCUMULATED_DEPR_F` | NUMBER |  |  | Accumulated Depreciation (fiscal) |  | 0 | 0 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  |  | Document No |  | 0 | 0 |
| `DATEDOC` | DATE |  |  | Document Date |  | 0 | 0 |
| `PROCESSEDON` | NUMBER |  |  | Processed On |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022884` | `A_Transfer_Balance_IS IN ('Y','N')` |
| `SYS_C0022885` | `Processed IN ('Y','N')` |
| `SYS_C0022886` | `A_Transfer_Balance IN ('Y','N')` |
| `SYS_C0022889` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [A_ASSET](../../data-model/a/a_asset.md) | A_ASSET_TRANSFER.A_ASSET_ID → A_ASSET.A_ASSET_ID | NO ACTION |
| [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | A_ASSET_TRANSFER.C_ACCTSCHEMA_ID → C_ACCTSCHEMA.C_ACCTSCHEMA_ID | NO ACTION |
| [C_PERIOD](../../data-model/c/c_period.md) | A_ASSET_TRANSFER.C_PERIOD_ID → C_PERIOD.C_PERIOD_ID | NO ACTION |
| [C_VALIDCOMBINATION](../../data-model/c/c_validcombination.md) | A_ASSET_TRANSFER.A_ACCUMDEPRECIATION_NEW_ACCT → C_VALIDCOMBINATION.C_VALIDCOMBINATION_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  A_ASSET ||--o{ A_ASSET_TRANSFER : ""
  C_ACCTSCHEMA ||--o{ A_ASSET_TRANSFER : ""
  C_PERIOD ||--o{ A_ASSET_TRANSFER : ""
  C_VALIDCOMBINATION ||--o{ A_ASSET_TRANSFER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **soft_delete_only**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

80 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| `model_column_missing` | `columns.C_Department_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.a_asset_transfer.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
