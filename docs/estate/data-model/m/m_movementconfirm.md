---
title: "M_MOVEMENTCONFIRM"
order: 55
ekos_generated: true
ekos_estate_version: 1
---

# M_MOVEMENTCONFIRM

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_MovementConfirm`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_MOVEMENTCONFIRM_ID` | NUMBER(10,0) | PK | yes | Move Confirm |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `M_MOVEMENT_ID` | NUMBER(10,0) |  | yes | Inventory Move | [M_MOVEMENT](../../data-model/m/m_movement.md) | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `ISAPPROVED` | CHAR(1) |  | yes | Approved |  | 0 | 0 |
| `APPROVALAMT` | NUMBER |  |  | Approval Amount |  | 0 | 0 |
| `DOCACTION` | CHAR(2) |  | yes | Document Action |  | 0 | 0 |
| `DOCSTATUS` | CHAR(2) |  | yes | Document Status |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `M_INVENTORY_ID` | NUMBER(10,0) |  |  | Phys.Inventory | [M_INVENTORY](../../data-model/m/m_inventory.md) | 0 | 0 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 0 |
| `M_MOVEMENTCONFIRM_UU` | VARCHAR2(36 CHAR) |  |  | M_MovementConfirm_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020677` | `Processed in ('Y','N')` |
| `SYS_C0020678` | `IsApproved in ('Y','N')` |
| `SYS_C0020679` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_INVENTORY](../../data-model/m/m_inventory.md) | M_MOVEMENTCONFIRM.M_INVENTORY_ID → M_INVENTORY.M_INVENTORY_ID | NO ACTION |
| [M_MOVEMENT](../../data-model/m/m_movement.md) | M_MOVEMENTCONFIRM.M_MOVEMENT_ID → M_MOVEMENT.M_MOVEMENT_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_MOVEMENTLINECONFIRM](../../data-model/m/m_movementlineconfirm.md) | M_MOVEMENTLINECONFIRM.M_MOVEMENTCONFIRM_ID → M_MOVEMENTCONFIRM.M_MOVEMENTCONFIRM_ID | CASCADE |

```mermaid
erDiagram
  M_INVENTORY ||--o{ M_MOVEMENTCONFIRM : ""
  M_MOVEMENT ||--o{ M_MOVEMENTCONFIRM : ""
  M_MOVEMENTCONFIRM ||--o{ M_MOVEMENTLINECONFIRM : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

17 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DOCUMENTNO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_MOVEMENTCONFIRM_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DOCUMENTNO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_movementconfirm.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
