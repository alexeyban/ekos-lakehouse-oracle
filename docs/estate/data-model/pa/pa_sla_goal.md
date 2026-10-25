---
title: "PA_SLA_GOAL"
order: 29
ekos_generated: true
ekos_estate_version: 1
---

# PA_SLA_GOAL

Area [PA](../../data-model/pa/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_PA_SLA_Goal`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `PA_SLA_GOAL_ID` | NUMBER(10,0) | PK | yes | SLA Goal |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 1 | 0 |
| `PA_SLA_CRITERIA_ID` | NUMBER(10,0) |  | yes | SLA Criteria | [PA_SLA_CRITERIA](../../data-model/pa/pa_sla_criteria.md) | 0 | 1 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  | yes | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 1 |
| `VALIDFROM` | DATE |  |  | Valid from |  | 1 | 0 |
| `VALIDTO` | DATE |  |  | Valid to |  | 1 | 0 |
| `MEASURETARGET` | NUMBER |  | yes | Measure Target |  | 0 | 1 |
| `MEASUREACTUAL` | NUMBER |  | yes | Measure Actual |  | 0 | 1 |
| `DATELASTRUN` | DATE |  |  | Date Last Run |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `PA_SLA_GOAL_UU` | VARCHAR2(36 CHAR) |  |  | PA_SLA_Goal_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019678` | `Processed in ('Y','N')` |
| `SYS_C0019680` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | PA_SLA_GOAL.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [PA_SLA_CRITERIA](../../data-model/pa/pa_sla_criteria.md) | PA_SLA_GOAL.PA_SLA_CRITERIA_ID → PA_SLA_CRITERIA.PA_SLA_CRITERIA_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [PA_SLA_MEASURE](../../data-model/pa/pa_sla_measure.md) | PA_SLA_MEASURE.PA_SLA_GOAL_ID → PA_SLA_GOAL.PA_SLA_GOAL_ID | NO ACTION |

```mermaid
erDiagram
  C_BPARTNER ||--o{ PA_SLA_GOAL : ""
  PA_SLA_CRITERIA ||--o{ PA_SLA_GOAL : ""
  PA_SLA_GOAL ||--o{ PA_SLA_MEASURE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PA_SLA_GOAL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.pa_sla_goal.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
