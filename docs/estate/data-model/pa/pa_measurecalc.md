---
title: "PA_MEASURECALC"
order: 16
ekos_generated: true
ekos_estate_version: 1
---

# PA_MEASURECALC

Area [PA](../../data-model/pa/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 6 row(s) when profiled

Application model: `org.compiere.model.X_PA_MeasureCalc`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `PA_MEASURECALC_ID` | NUMBER(10,0) | PK | yes | Measure Calculation |  | 0 | 6 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 6 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 6 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 6 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 6 |
| `SELECTCLAUSE` | VARCHAR2(2000 CHAR) |  | yes | Sql SELECT |  | 0 | 6 |
| `WHERECLAUSE` | VARCHAR2(2000 CHAR) |  | yes | Sql WHERE |  | 0 | 4 |
| `DATECOLUMN` | VARCHAR2(124 CHAR) |  | yes | Date Column |  | 0 | 3 |
| `ORGCOLUMN` | VARCHAR2(124 CHAR) |  | yes | Org Column |  | 0 | 2 |
| `BPARTNERCOLUMN` | VARCHAR2(124 CHAR) |  |  | B.Partner Column |  | 0 | 2 |
| `PRODUCTCOLUMN` | VARCHAR2(124 CHAR) |  |  | Product Column |  | 3 | 1 |
| `AD_TABLE_ID` | NUMBER(10,0) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 2 |
| `KEYCOLUMN` | VARCHAR2(124 CHAR) |  | yes | Key Column |  | 0 | 3 |
| `ENTITYTYPE` | VARCHAR2(40 CHAR) |  | yes | Entity Type |  | 0 | 1 |
| `PA_MEASURECALC_UU` | VARCHAR2(36 CHAR) |  |  | PA_MeasureCalc_UU |  | 0 | 6 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022342` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ENTITYTYPE](../../data-model/ad/ad_entitytype.md) | PA_MEASURECALC.ENTITYTYPE → AD_ENTITYTYPE.ENTITYTYPE | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | PA_MEASURECALC.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [PA_MEASURE](../../data-model/pa/pa_measure.md) | PA_MEASURE.PA_MEASURECALC_ID → PA_MEASURECALC.PA_MEASURECALC_ID | NO ACTION |
| [PA_RATIOELEMENT](../../data-model/pa/pa_ratioelement.md) | PA_RATIOELEMENT.PA_MEASURECALC_ID → PA_MEASURECALC.PA_MEASURECALC_ID | NO ACTION |

```mermaid
erDiagram
  AD_ENTITYTYPE ||--o{ PA_MEASURECALC : ""
  AD_TABLE ||--o{ PA_MEASURECALC : ""
  PA_MEASURECALC ||--o{ PA_MEASURE : ""
  PA_MEASURECALC ||--o{ PA_RATIOELEMENT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

59 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-04-03T12:26 | iD11 | `modify_column` | ProductColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | DateColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | KeyColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | BPartnerColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | ProductColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | OrgColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | OrgColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | BPartnerColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | KeyColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | OrgColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | DateColumn | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | OrgColumn | IDEMPIERE-6064 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.pa_measurecalc.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
