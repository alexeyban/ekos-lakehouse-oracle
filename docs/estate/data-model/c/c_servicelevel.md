---
title: "C_SERVICELEVEL"
order: 169
ekos_generated: true
ekos_estate_version: 1
---

# C_SERVICELEVEL

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_ServiceLevel`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_SERVICELEVEL_ID` | NUMBER(10,0) | PK | yes | Service Level |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `SERVICELEVELPROVIDED` | NUMBER |  | yes | Quantity Provided |  | 0 | 0 |
| `SERVICELEVELINVOICED` | NUMBER |  | yes | Quantity Invoiced |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  |  | Processed |  | 0 | 0 |
| `C_REVENUERECOGNITION_PLAN_ID` | NUMBER(10,0) |  | yes | Revenue Recognition Plan | [C_REVENUERECOGNITION_PLAN](../../data-model/c/c_revenuerecognition_plan.md) | 0 | 0 |
| `C_SERVICELEVEL_UU` | VARCHAR2(36 CHAR) |  |  | C_ServiceLevel_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019693` | `IsActive in ('Y','N')` |
| `SYS_C0019695` | `Processed in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_REVENUERECOGNITION_PLAN](../../data-model/c/c_revenuerecognition_plan.md) | C_SERVICELEVEL.C_REVENUERECOGNITION_PLAN_ID → C_REVENUERECOGNITION_PLAN.C_REVENUERECOGNITION_PLAN_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | C_SERVICELEVEL.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_SERVICELEVELLINE](../../data-model/c/c_servicelevelline.md) | C_SERVICELEVELLINE.C_SERVICELEVEL_ID → C_SERVICELEVEL.C_SERVICELEVEL_ID | CASCADE |

```mermaid
erDiagram
  C_REVENUERECOGNITION_PLAN ||--o{ C_SERVICELEVEL : ""
  C_SERVICELEVEL ||--o{ C_SERVICELEVELLINE : ""
  M_PRODUCT ||--o{ C_SERVICELEVEL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

12 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_SERVICELEVEL_UU | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_servicelevel.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
