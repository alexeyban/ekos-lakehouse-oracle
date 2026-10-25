---
title: "A_ASSET_DISPOSED"
order: 8
ekos_generated: true
ekos_estate_version: 1
---

# A_ASSET_DISPOSED

Area [A](../../data-model/a/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_A_Asset_Disposed`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `A_ASSET_DISPOSED_ID` | NUMBER(10,0) | PK | yes | Asset Disposed |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `A_ASSET_ID` | NUMBER(10,0) |  | yes | Asset | [A_ASSET](../../data-model/a/a_asset.md) | 0 | 0 |
| `A_DISPOSED_DATE` | DATE |  | yes | Disposed Date |  | 0 | 0 |
| `A_DISPOSED_REASON` | VARCHAR2(10 CHAR) |  |  | Disposed Reason |  | 0 | 0 |
| `C_PERIOD_ID` | NUMBER(10,0) |  |  | Period | [C_PERIOD](../../data-model/c/c_period.md) | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `DATEDOC` | DATE |  | yes | Document Date |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  | yes | Process Now |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `DATEACCT` | DATE |  | yes | Account Date |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `A_PROCEEDS` | NUMBER |  |  | Asset Proceeds |  | 0 | 0 |
| `A_DISPOSED_METHOD` | VARCHAR2(2 CHAR) |  | yes | Disposed Method |  | 0 | 0 |
| `A_ASSET_TRADE_ID` | NUMBER(10,0) |  |  | Asset Trade | [A_ASSET](../../data-model/a/a_asset.md) | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `A_ASSET_DISPOSED_UU` | VARCHAR2(36 CHAR) |  |  | A_Asset_Disposed_UU |  | 0 | 0 |
| `DOCACTION` | CHAR(2) |  |  | Document Action |  | 0 | 0 |
| `DOCSTATUS` | VARCHAR2(2 CHAR) |  |  | Document Status |  | 0 | 0 |
| `ISAPPROVED` | CHAR(1) |  | yes | Approved |  | 0 | 0 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 0 |
| `A_ACTIVATION_METHOD` | VARCHAR2(2 CHAR) |  | yes | Activation Method |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `ISDISPOSED` | CHAR(1) |  |  | Disposed |  | 0 | 0 |
| `A_ASSET_STATUS` | VARCHAR2(2 CHAR) |  |  | Asset Status |  | 0 | 0 |
| `A_DISPOSAL_AMT` | NUMBER |  | yes | Disposal Amount |  | 0 | 0 |
| `EXPENSE` | NUMBER |  | yes | Expense |  | 0 | 0 |
| `A_ACCUMULATED_DEPR` | NUMBER |  | yes | Accumulated Depreciation |  | 0 | 0 |
| `POSTINGTYPE` | CHAR(1) |  | yes | Posting Type |  | 0 | 0 |
| `POSTED` | CHAR(1) |  | yes | Posted |  | 0 | 0 |
| `A_ACCUMULATED_DEPR_DELTA` | NUMBER |  | yes | Accumulated Depreciation (delta) |  | 0 | 0 |
| `A_ASSET_COST` | NUMBER |  |  | Asset Cost |  | 0 | 0 |
| `PROCESSEDON` | NUMBER |  |  | Processed On |  | 0 | 0 |
| `C_INVOICE_ID` | NUMBER(10,0) |  |  | Invoice | [C_INVOICE](../../data-model/c/c_invoice.md) | 0 | 0 |
| `C_INVOICELINE_ID` | NUMBER(10,0) |  |  | Invoice Line | [C_INVOICELINE](../../data-model/c/c_invoiceline.md) | 0 | 0 |
| `C_DOCTYPE_ID` | NUMBER(10,0) |  |  | Document Type | [C_DOCTYPE](../../data-model/c/c_doctype.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020427` | `Processed IN ('Y','N')` |
| `SYS_C0020428` | `IsActive IN ('Y','N')` |
| `SYS_C0020431` | `IsDisposed IN ('Y','N')` |
| `SYS_C0020432` | `IsApproved IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [A_ASSET](../../data-model/a/a_asset.md) | A_ASSET_DISPOSED.A_ASSET_TRADE_ID → A_ASSET.A_ASSET_ID | NO ACTION |
| [C_DOCTYPE](../../data-model/c/c_doctype.md) | A_ASSET_DISPOSED.C_DOCTYPE_ID → C_DOCTYPE.C_DOCTYPE_ID | NO ACTION |
| [C_INVOICE](../../data-model/c/c_invoice.md) | A_ASSET_DISPOSED.C_INVOICE_ID → C_INVOICE.C_INVOICE_ID | NO ACTION |
| [C_INVOICELINE](../../data-model/c/c_invoiceline.md) | A_ASSET_DISPOSED.C_INVOICELINE_ID → C_INVOICELINE.C_INVOICELINE_ID | NO ACTION |
| [C_PERIOD](../../data-model/c/c_period.md) | A_ASSET_DISPOSED.C_PERIOD_ID → C_PERIOD.C_PERIOD_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [A_DEPRECIATION_EXP](../../data-model/a/a_depreciation_exp.md) | A_DEPRECIATION_EXP.A_ASSET_DISPOSED_ID → A_ASSET_DISPOSED.A_ASSET_DISPOSED_ID | NO ACTION |

```mermaid
erDiagram
  A_ASSET ||--o{ A_ASSET_DISPOSED : ""
  A_ASSET_DISPOSED ||--o{ A_DEPRECIATION_EXP : ""
  C_DOCTYPE ||--o{ A_ASSET_DISPOSED : ""
  C_INVOICE ||--o{ A_ASSET_DISPOSED : ""
  C_INVOICELINE ||--o{ A_ASSET_DISPOSED : ""
  C_PERIOD ||--o{ A_ASSET_DISPOSED : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

64 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| `model_column_missing` | `columns.C_Department_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.a_asset_disposed.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
