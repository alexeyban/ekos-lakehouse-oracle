---
title: "A_ASSET_SPLIT"
order: 22
ekos_generated: true
ekos_estate_version: 1
---

# A_ASSET_SPLIT

Area [A](../../data-model/a/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_A_Asset_Split`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `A_ASSET_SPLIT_ID` | NUMBER(10,0) | PK | yes | Asset Split |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `A_AMOUNT_SPLIT` | NUMBER |  |  | Amount Split |  | 0 | 0 |
| `A_ASSET_ACCT_ID` | NUMBER(10,0) |  | yes | A_Asset_Acct_ID |  | 0 | 0 |
| `A_PERCENT_ORIGINAL` | NUMBER |  |  | Original Percent |  | 0 | 0 |
| `A_QTY_CURRENT` | NUMBER |  | yes | Current Qty |  | 0 | 0 |
| `A_SPLIT_TYPE` | VARCHAR2(3 CHAR) |  | yes | Split Type |  | 0 | 0 |
| `C_PERIOD_ID` | NUMBER(10,0) |  | yes | Period | [C_PERIOD](../../data-model/c/c_period.md) | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  | yes | Process Now |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `POSTINGTYPE` | CHAR(1) |  | yes | Posting Type |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `DATEACCT` | DATE |  | yes | Account Date |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `A_TRANSFER_BALANCE_IS` | CHAR(1) |  | yes | A_Transfer_Balance_IS |  | 0 | 0 |
| `A_QTY_SPLIT` | NUMBER |  |  | Qty. Split |  | 0 | 0 |
| `A_PERCENT_SPLIT` | NUMBER |  |  | A_Percent_Split |  | 0 | 0 |
| `A_DEPRECIATION_WORKFILE_ID` | NUMBER(10,0) |  | yes | A_Depreciation_Workfile_ID |  | 0 | 0 |
| `A_ASSET_COST` | NUMBER |  |  | Asset Cost |  | 0 | 0 |
| `A_ASSET_ID` | NUMBER(10,0) |  | yes | Asset |  | 0 | 0 |
| `A_ASSET_ID_TO` | NUMBER(10,0) |  |  | To Asset ID |  | 0 | 0 |
| `A_ASSET_SPLIT_UU` | VARCHAR2(36 CHAR) |  |  | A_Asset_Split_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019942` | `Processed IN ('Y','N')` |
| `SYS_C0019943` | `IsActive IN ('Y','N')` |
| `SYS_C0019944` | `A_Transfer_Balance_IS IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [A_ASSET](../../data-model/a/a_asset.md) | A_ASSET_SPLIT.A_ASSET_ID_TO → A_ASSET.A_ASSET_ID | NO ACTION |
| [C_PERIOD](../../data-model/c/c_period.md) | A_ASSET_SPLIT.C_PERIOD_ID → C_PERIOD.C_PERIOD_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  A_ASSET ||--o{ A_ASSET_SPLIT : ""
  C_PERIOD ||--o{ A_ASSET_SPLIT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **soft_delete_only**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

24 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_SPLIT_TYPE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_SPLIT_TYPE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_SPLIT_TYPE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_ASSET_SPLIT_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-06-13T17:16 | i7.1z | `modify_column` | a_asset_id_to | IDEMPIERE-4334 |
| 2020-06-13T17:16 | i7.1z | `add_constraint` |  | IDEMPIERE-4334 |
| 2020-06-13T17:16 | i7.1z | `add_constraint` |  | IDEMPIERE-4334 |

## Notes

<!-- ekos:manual id="table.a_asset_split.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
