---
title: "M_MOVEMENTLINE"
order: 56
ekos_generated: true
ekos_estate_version: 1
---

# M_MOVEMENTLINE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_M_MovementLine`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_MOVEMENTLINE_ID` | NUMBER(10,0) | PK | yes | Move Line |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `M_MOVEMENT_ID` | NUMBER(10,0) |  | yes | Inventory Move | [M_MOVEMENT](../../data-model/m/m_movement.md) | 0 | 1 |
| `M_LOCATOR_ID` | NUMBER(10,0) |  | yes | Locator | [M_LOCATOR](../../data-model/m/m_locator.md) | 0 | 1 |
| `M_LOCATORTO_ID` | NUMBER(10,0) |  | yes | Locator To | [M_LOCATOR](../../data-model/m/m_locator.md) | 0 | 1 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 1 |
| `LINE` | NUMBER(10,0) |  |  | Line No |  | 0 | 1 |
| `MOVEMENTQTY` | NUMBER |  | yes | Movement Quantity |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 1 |
| `M_ATTRIBUTESETINSTANCE_ID` | NUMBER(10,0) |  |  | Attribute Set Instance | [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | 0 | 1 |
| `CONFIRMEDQTY` | NUMBER |  |  | Confirmed Quantity |  | 0 | 1 |
| `SCRAPPEDQTY` | NUMBER |  |  | Scrapped Quantity |  | 0 | 1 |
| `TARGETQTY` | NUMBER |  |  | Target Quantity |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `M_ATTRIBUTESETINSTANCETO_ID` | NUMBER(10,0) |  |  | Attribute Set Instance To | [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | 1 | 0 |
| `DD_ORDERLINE_ID` | NUMBER(10,0) |  |  | Distribution Order Line | [DD_ORDERLINE](../../data-model/dd/dd_orderline.md) | 1 | 0 |
| `REVERSALLINE_ID` | NUMBER(10,0) |  |  | Reversal Line | [M_MOVEMENTLINE](../../data-model/m/m_movementline.md) | 1 | 0 |
| `M_MOVEMENTLINE_UU` | VARCHAR2(36 CHAR) |  |  | M_MovementLine_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021215` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [DD_ORDERLINE](../../data-model/dd/dd_orderline.md) | M_MOVEMENTLINE.DD_ORDERLINE_ID → DD_ORDERLINE.DD_ORDERLINE_ID | NO ACTION |
| [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | M_MOVEMENTLINE.M_ATTRIBUTESETINSTANCETO_ID → M_ATTRIBUTESETINSTANCE.M_ATTRIBUTESETINSTANCE_ID | NO ACTION |
| [M_LOCATOR](../../data-model/m/m_locator.md) | M_MOVEMENTLINE.M_LOCATOR_ID → M_LOCATOR.M_LOCATOR_ID | NO ACTION |
| [M_MOVEMENT](../../data-model/m/m_movement.md) | M_MOVEMENTLINE.M_MOVEMENT_ID → M_MOVEMENT.M_MOVEMENT_ID | CASCADE |
| [M_MOVEMENTLINE](../../data-model/m/m_movementline.md) | M_MOVEMENTLINE.REVERSALLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | M_MOVEMENTLINE.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| `I_MOVEMENT` | I_MOVEMENT.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | NO ACTION |
| [M_COSTDETAIL](../../data-model/m/m_costdetail.md) | M_COSTDETAIL.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | NO ACTION |
| [M_MOVEMENTLINE](../../data-model/m/m_movementline.md) | M_MOVEMENTLINE.REVERSALLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | NO ACTION |
| [M_MOVEMENTLINECONFIRM](../../data-model/m/m_movementlineconfirm.md) | M_MOVEMENTLINECONFIRM.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | CASCADE |
| [M_MOVEMENTLINEMA](../../data-model/m/m_movementlinema.md) | M_MOVEMENTLINEMA.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | CASCADE |
| [M_TRANSACTION](../../data-model/m/m_transaction.md) | M_TRANSACTION.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | NO ACTION |
| `T_TRANSACTION` | T_TRANSACTION.M_MOVEMENTLINE_ID → M_MOVEMENTLINE.M_MOVEMENTLINE_ID | CASCADE |

```mermaid
erDiagram
  DD_ORDERLINE ||--o{ M_MOVEMENTLINE : ""
  M_ATTRIBUTESETINSTANCE ||--o{ M_MOVEMENTLINE : ""
  M_LOCATOR ||--o{ M_MOVEMENTLINE : ""
  M_MOVEMENT ||--o{ M_MOVEMENTLINE : ""
  M_MOVEMENTLINE ||--o{ I_MOVEMENT : ""
  M_MOVEMENTLINE ||--o{ M_COSTDETAIL : ""
  M_MOVEMENTLINE ||--o{ M_MOVEMENTLINE : ""
  M_MOVEMENTLINE ||--o{ M_MOVEMENTLINECONFIRM : ""
  M_MOVEMENTLINE ||--o{ M_MOVEMENTLINEMA : ""
  M_MOVEMENTLINE ||--o{ M_TRANSACTION : ""
  M_MOVEMENTLINE ||--o{ T_TRANSACTION : ""
  M_PRODUCT ||--o{ M_MOVEMENTLINE : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Read by

| kind | name |
|---|---|
| View | `M_MOVEMENTLINEMA_V` |
| View | `M_MOVEMENTLINEMA_VT` |
| View | `M_MOVEMENT_CANDIDATE_V` |
| View | `M_TRANSACTION_V` |
| View | `RV_TRANSACTION` |
| View | `m_movement_candidate_v` |
| View | `m_movementlinema_v` |
| View | `m_movementlinema_vt` |
| View | `m_transaction_v` |
| View | `rv_transaction` |

## Schema history

42 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-01-09T18:01 | iD12 | `add_column` | QtyEntered | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `add_column` | C_UOM_ID | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `add_constraint` |  | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `add_constraint` |  | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `add_column` | QtyEntered | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `modify_column` | C_UOM_ID | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `modify_column` | C_UOM_ID | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `modify_column` | C_UOM_ID | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `add_column` | C_UOM_ID | IDEMPIERE-4925 |
| 2025-01-09T18:01 | iD12 | `modify_column` | C_UOM_ID | IDEMPIERE-4925 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| `model_column_missing` | `columns.C_Department_ID` | unexplained |
| `model_column_missing` | `columns.C_UOM_ID` | unexplained |
| `mandatory_but_nullable` | `columns.Line.nullable` | unexplained |
| `model_column_missing` | `columns.QtyEntered` | unexplained |
| `mandatory_but_nullable` | `columns.TargetQty.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.m_movementline.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
