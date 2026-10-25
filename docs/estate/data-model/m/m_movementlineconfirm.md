---
title: "M_MOVEMENTLINECONFIRM"
order: 57
ekos_generated: true
ekos_estate_version: 1
---

# M_MOVEMENTLINECONFIRM

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_MovementLineConfirm`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_MOVEMENTLINECONFIRM_ID` | NUMBER(10,0) | PK | yes | Move Line Confirm |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `M_MOVEMENTCONFIRM_ID` | NUMBER(10,0) |  | yes | Move Confirm | [M_MOVEMENTCONFIRM](../../data-model/m/m_movementconfirm.md) | 0 | 0 |
| `M_MOVEMENTLINE_ID` | NUMBER(10,0) |  | yes | Move Line | [M_MOVEMENTLINE](../../data-model/m/m_movementline.md) | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `TARGETQTY` | NUMBER |  | yes | Target Quantity |  | 0 | 0 |
| `CONFIRMEDQTY` | NUMBER |  | yes | Confirmed Quantity |  | 0 | 0 |
| `DIFFERENCEQTY` | NUMBER |  | yes | Difference |  | 0 | 0 |
| `SCRAPPEDQTY` | NUMBER |  | yes | Scrapped Quantity |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `M_INVENTORYLINE_ID` | NUMBER(10,0) |  |  | Phys.Inventory Line | [M_INVENTORYLINE](../../data-model/m/m_inventoryline.md) | 0 | 0 |
| `M_MOVEMENTLINECONFIRM_UU` | VARCHAR2(36 CHAR) |  |  | M_MovementLineConfirm_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0023016` | `IsActive in ('Y','N')` |
| `SYS_C0023018` | `Processed in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_INVENTORYLINE](../../data-model/m/m_inventoryline.md) | M_MOVEMENTLINECONFIRM.M_INVENTORYLINE_ID → M_INVENTORYLINE.M_INVENTORYLINE_ID | NO ACTION |
| [M_MOVEMENTCONFIRM](../../data-model/m/m_movementconfirm.md) | M_MOVEMENTLINECONFIRM.M_MOVEMENTCONFIRM_ID → M_MOVEMENTCONFIRM.M_MOVEMENTCONFIRM_ID | CASCADE |
| [M_MOVEMENTLINE](../../data-model/m/m_movementline.md) | M_MOVEMENTLINECONFIRM.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  M_INVENTORYLINE ||--o{ M_MOVEMENTLINECONFIRM : ""
  M_MOVEMENTCONFIRM ||--o{ M_MOVEMENTLINECONFIRM : ""
  M_MOVEMENTLINE ||--o{ M_MOVEMENTLINECONFIRM : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Schema history

14 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_MOVEMENTLINECONFIRM_UU | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_movementlineconfirm.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
