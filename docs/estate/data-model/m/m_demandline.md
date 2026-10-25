---
title: "M_DEMANDLINE"
order: 25
ekos_generated: true
ekos_estate_version: 1
---

# M_DEMANDLINE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_DemandLine`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_DEMANDLINE_ID` | NUMBER(10,0) | PK | yes | Demand Line |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `M_DEMAND_ID` | NUMBER(10,0) |  | yes | Demand | [M_DEMAND](../../data-model/m/m_demand.md) | 0 | 0 |
| `C_PERIOD_ID` | NUMBER(10,0) |  | yes | Period | [C_PERIOD](../../data-model/c/c_period.md) | 0 | 0 |
| `QTY` | NUMBER |  | yes | Quantity |  | 0 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 0 |
| `QTYCALCULATED` | NUMBER |  | yes | Calculated Quantity |  | 0 | 0 |
| `M_DEMANDLINE_UU` | VARCHAR2(36 CHAR) |  |  | M_DemandLine_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021615` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_PERIOD](../../data-model/c/c_period.md) | M_DEMANDLINE.C_PERIOD_ID → C_PERIOD.C_PERIOD_ID | NO ACTION |
| [M_DEMAND](../../data-model/m/m_demand.md) | M_DEMANDLINE.M_DEMAND_ID → M_DEMAND.M_DEMAND_ID | CASCADE |
| [M_PRODUCT](../../data-model/m/m_product.md) | M_DEMANDLINE.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_DEMANDDETAIL](../../data-model/m/m_demanddetail.md) | M_DEMANDDETAIL.M_DEMANDLINE_ID → M_DEMANDLINE.M_DEMANDLINE_ID | CASCADE |

```mermaid
erDiagram
  C_PERIOD ||--o{ M_DEMANDLINE : ""
  M_DEMAND ||--o{ M_DEMANDLINE : ""
  M_DEMANDLINE ||--o{ M_DEMANDDETAIL : ""
  M_PRODUCT ||--o{ M_DEMANDLINE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Schema history

11 change(s); the latest:

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
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_DEMANDLINE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_demandline.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
