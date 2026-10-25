---
title: "M_INOUTCONFIRM"
order: 40
ekos_generated: true
ekos_estate_version: 1
---

# M_INOUTCONFIRM

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_M_InOutConfirm`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_INOUTCONFIRM_ID` | NUMBER(10,0) | PK | yes | Ship/Receipt Confirmation |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 1 |
| `M_INOUT_ID` | NUMBER(10,0) |  | yes | Shipment/Receipt | [M_INOUT](../../data-model/m/m_inout.md) | 0 | 1 |
| `CONFIRMTYPE` | CHAR(2) |  | yes | Confirmation Type |  | 0 | 1 |
| `ISAPPROVED` | CHAR(1) |  | yes | Approved |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `CREATEPACKAGE` | CHAR(1) |  |  | Create Package |  | 1 | 0 |
| `ISCANCELLED` | CHAR(1) |  | yes | Cancelled |  | 0 | 1 |
| `DOCSTATUS` | CHAR(2) |  | yes | Document Status |  | 0 | 1 |
| `DOCACTION` | CHAR(2) |  | yes | Document Action |  | 0 | 1 |
| `ISINDISPUTE` | CHAR(1) |  | yes | In Dispute |  | 0 | 1 |
| `M_INVENTORY_ID` | NUMBER(10,0) |  |  | Phys.Inventory | [M_INVENTORY](../../data-model/m/m_inventory.md) | 1 | 0 |
| `C_INVOICE_ID` | NUMBER(10,0) |  |  | Invoice | [C_INVOICE](../../data-model/c/c_invoice.md) | 1 | 0 |
| `APPROVALAMT` | NUMBER |  |  | Approval Amount |  | 1 | 0 |
| `CONFIRMATIONNO` | VARCHAR2(20 CHAR) |  |  | Confirmation No |  | 1 | 0 |
| `M_INOUTCONFIRM_UU` | VARCHAR2(36 CHAR) |  |  | M_InOutConfirm_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021801` | `Processed in ('Y','N')` |
| `SYS_C0021803` | `IsApproved in ('Y','N')` |
| `SYS_C0021804` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_INVOICE](../../data-model/c/c_invoice.md) | M_INOUTCONFIRM.C_INVOICE_ID → C_INVOICE.C_INVOICE_ID | NO ACTION |
| [M_INOUT](../../data-model/m/m_inout.md) | M_INOUTCONFIRM.M_INOUT_ID → M_INOUT.M_INOUT_ID | CASCADE |
| [M_INVENTORY](../../data-model/m/m_inventory.md) | M_INOUTCONFIRM.M_INVENTORY_ID → M_INVENTORY.M_INVENTORY_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_INOUTLINECONFIRM](../../data-model/m/m_inoutlineconfirm.md) | M_INOUTLINECONFIRM.M_INOUTCONFIRM_ID → M_INOUTCONFIRM.M_INOUTCONFIRM_ID | CASCADE |

```mermaid
erDiagram
  C_INVOICE ||--o{ M_INOUTCONFIRM : ""
  M_INOUT ||--o{ M_INOUTCONFIRM : ""
  M_INOUTCONFIRM ||--o{ M_INOUTLINECONFIRM : ""
  M_INVENTORY ||--o{ M_INOUTCONFIRM : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Read by

| kind | name |
|---|---|
| View | `M_INOUTCONFIRM_V` |
| View | `M_INOUTCONFIRM_VT` |
| View | `RV_INOUTCONFIRM` |
| View | `RV_INOUTLINECONFIRM` |
| View | `m_inoutconfirm_v` |
| View | `m_inoutconfirm_vt` |
| View | `rv_inoutconfirm` |
| View | `rv_inoutlineconfirm` |

## Schema history

22 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DOCUMENTNO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CONFIRMATIONNO | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_inoutconfirm.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
