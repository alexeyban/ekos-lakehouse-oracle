---
title: "M_DEMANDDETAIL"
order: 24
ekos_generated: true
ekos_estate_version: 1
---

# M_DEMANDDETAIL

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_DemandDetail`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_DEMANDDETAIL_ID` | NUMBER(10,0) | PK | yes | Demand Detail |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `M_DEMANDLINE_ID` | NUMBER(10,0) |  | yes | Demand Line | [M_DEMANDLINE](../../data-model/m/m_demandline.md) | 0 | 0 |
| `M_FORECASTLINE_ID` | NUMBER(10,0) |  |  | Forecast Line | [M_FORECASTLINE](../../data-model/m/m_forecastline.md) | 0 | 0 |
| `M_REQUISITIONLINE_ID` | NUMBER(10,0) |  |  | Requisition Line | [M_REQUISITIONLINE](../../data-model/m/m_requisitionline.md) | 0 | 0 |
| `C_ORDERLINE_ID` | NUMBER(10,0) |  |  | Sales Order Line | [C_ORDERLINE](../../data-model/c/c_orderline.md) | 0 | 0 |
| `M_DEMANDDETAIL_UU` | VARCHAR2(36 CHAR) |  |  | M_DemandDetail_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021396` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_ORDERLINE](../../data-model/c/c_orderline.md) | M_DEMANDDETAIL.C_ORDERLINE_ID → C_ORDERLINE.C_ORDERLINE_ID | CASCADE |
| [M_DEMANDLINE](../../data-model/m/m_demandline.md) | M_DEMANDDETAIL.M_DEMANDLINE_ID → M_DEMANDLINE.M_DEMANDLINE_ID | CASCADE |
| [M_FORECASTLINE](../../data-model/m/m_forecastline.md) | M_DEMANDDETAIL.M_FORECASTLINE_ID → M_FORECASTLINE.M_FORECASTLINE_ID | CASCADE |
| [M_REQUISITIONLINE](../../data-model/m/m_requisitionline.md) | M_DEMANDDETAIL.M_REQUISITIONLINE_ID → M_REQUISITIONLINE.M_REQUISITIONLINE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  C_ORDERLINE ||--o{ M_DEMANDDETAIL : ""
  M_DEMANDLINE ||--o{ M_DEMANDDETAIL : ""
  M_FORECASTLINE ||--o{ M_DEMANDDETAIL : ""
  M_REQUISITIONLINE ||--o{ M_DEMANDDETAIL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 5 citation(s)

## Schema history

13 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_DEMANDDETAIL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_demanddetail.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
