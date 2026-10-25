---
title: "M_INOUTLINECONFIRM"
order: 42
ekos_generated: true
ekos_estate_version: 1
---

# M_INOUTLINECONFIRM

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_M_InOutLineConfirm`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_INOUTLINECONFIRM_ID` | NUMBER(10,0) | PK | yes | Ship/Receipt Confirmation Line |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `M_INOUTCONFIRM_ID` | NUMBER(10,0) |  | yes | Ship/Receipt Confirmation | [M_INOUTCONFIRM](../../data-model/m/m_inoutconfirm.md) | 0 | 1 |
| `M_INOUTLINE_ID` | NUMBER(10,0) |  | yes | Shipment/Receipt Line | [M_INOUTLINE](../../data-model/m/m_inoutline.md) | 0 | 1 |
| `TARGETQTY` | NUMBER |  | yes | Target Quantity |  | 0 | 1 |
| `CONFIRMEDQTY` | NUMBER |  | yes | Confirmed Quantity |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `DIFFERENCEQTY` | NUMBER |  |  | Difference |  | 0 | 1 |
| `SCRAPPEDQTY` | NUMBER |  |  | Scrapped Quantity |  | 0 | 1 |
| `M_INVENTORYLINE_ID` | NUMBER(10,0) |  |  | Phys.Inventory Line | [M_INVENTORYLINE](../../data-model/m/m_inventoryline.md) | 1 | 0 |
| `C_INVOICELINE_ID` | NUMBER(10,0) |  |  | Invoice Line | [C_INVOICELINE](../../data-model/c/c_invoiceline.md) | 1 | 0 |
| `CONFIRMATIONNO` | VARCHAR2(20 CHAR) |  |  | Confirmation No |  | 1 | 0 |
| `M_INOUTLINECONFIRM_UU` | VARCHAR2(36 CHAR) |  |  | M_InOutLineConfirm_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021352` | `IsActive in ('Y','N')` |
| `SYS_C0021355` | `Processed in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_INVOICELINE](../../data-model/c/c_invoiceline.md) | M_INOUTLINECONFIRM.C_INVOICELINE_ID → C_INVOICELINE.C_INVOICELINE_ID | NO ACTION |
| [M_INOUTCONFIRM](../../data-model/m/m_inoutconfirm.md) | M_INOUTLINECONFIRM.M_INOUTCONFIRM_ID → M_INOUTCONFIRM.M_INOUTCONFIRM_ID | CASCADE |
| [M_INOUTLINE](../../data-model/m/m_inoutline.md) | M_INOUTLINECONFIRM.M_INOUTLINE_ID → M_INOUTLINE.M_INOUTLINE_ID | CASCADE |
| [M_INVENTORYLINE](../../data-model/m/m_inventoryline.md) | M_INOUTLINECONFIRM.M_INVENTORYLINE_ID → M_INVENTORYLINE.M_INVENTORYLINE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| `I_INOUTLINECONFIRM` | I_INOUTLINECONFIRM.M_INOUTLINECONFIRM_ID → M_INOUTLINECONFIRM.M_INOUTLINECONFIRM_ID | CASCADE |

```mermaid
erDiagram
  C_INVOICELINE ||--o{ M_INOUTLINECONFIRM : ""
  M_INOUTCONFIRM ||--o{ M_INOUTLINECONFIRM : ""
  M_INOUTLINE ||--o{ M_INOUTLINECONFIRM : ""
  M_INOUTLINECONFIRM ||--o{ I_INOUTLINECONFIRM : ""
  M_INVENTORYLINE ||--o{ M_INOUTLINECONFIRM : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Read by

| kind | name |
|---|---|
| View | `M_INOUT_LINECONFIRM_V` |
| View | `M_INOUT_LINECONFIRM_VT` |
| View | `RV_INOUTLINECONFIRM` |
| View | `m_inout_lineconfirm_v` |
| View | `m_inout_lineconfirm_vt` |
| View | `rv_inoutlineconfirm` |

## Schema history

19 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_INOUTLINECONFIRM_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_inoutlineconfirm.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
