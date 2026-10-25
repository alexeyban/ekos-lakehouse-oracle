---
title: "R_REQUESTPROCESSOR"
order: 18
ekos_generated: true
ekos_estate_version: 1
---

# R_REQUESTPROCESSOR

Area [R](../../data-model/r/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_R_RequestProcessor`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `R_REQUESTPROCESSOR_ID` | NUMBER(10,0) | PK | yes | Request Processor |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `FREQUENCY` | NUMBER(10,0) |  |  |  |  | 0 | 1 |
| `FREQUENCYTYPE` | CHAR(1) |  |  |  |  | 0 | 1 |
| `DATELASTRUN` | DATE |  |  | Date Last Run |  | 0 | 1 |
| `DATENEXTRUN` | DATE |  |  | Date Next Run |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `OVERDUEALERTDAYS` | NUMBER(10,0) |  | yes | Alert after Days Due |  | 0 | 1 |
| `OVERDUEASSIGNDAYS` | NUMBER(10,0) |  | yes | Escalate after Days Due |  | 0 | 1 |
| `SUPERVISOR_ID` | NUMBER(10,0) |  | yes | Supervisor | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 1 |
| `KEEPLOGDAYS` | NUMBER(10,0) |  | yes | Days to keep Log |  | 0 | 1 |
| `REMINDDAYS` | NUMBER(10,0) |  | yes | Reminder Days |  | 0 | 1 |
| `INACTIVITYALERTDAYS` | NUMBER(10,0) |  | yes | Inactivity Alert Days |  | 0 | 1 |
| `R_REQUESTTYPE_ID` | NUMBER(10,0) |  |  | Request Type | [R_REQUESTTYPE](../../data-model/r/r_requesttype.md) | 1 | 0 |
| `R_REQUESTPROCESSOR_UU` | VARCHAR2(36 CHAR) |  |  | R_RequestProcessor_UU |  | 0 | 1 |
| `AD_SCHEDULE_ID` | NUMBER(10,0) |  | yes | Schedule | [AD_SCHEDULE](../../data-model/ad/ad_schedule.md) | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019668` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_SCHEDULE](../../data-model/ad/ad_schedule.md) | R_REQUESTPROCESSOR.AD_SCHEDULE_ID → AD_SCHEDULE.AD_SCHEDULE_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | R_REQUESTPROCESSOR.SUPERVISOR_ID → AD_USER.AD_USER_ID | NO ACTION |
| [R_REQUESTTYPE](../../data-model/r/r_requesttype.md) | R_REQUESTPROCESSOR.R_REQUESTTYPE_ID → R_REQUESTTYPE.R_REQUESTTYPE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| `R_REQUESTPROCESSORLOG` | R_REQUESTPROCESSORLOG.R_REQUESTPROCESSOR_ID → R_REQUESTPROCESSOR.R_REQUESTPROCESSOR_ID | CASCADE |
| [R_REQUESTPROCESSOR_ROUTE](../../data-model/r/r_requestprocessor_route.md) | R_REQUESTPROCESSOR_ROUTE.R_REQUESTPROCESSOR_ID → R_REQUESTPROCESSOR.R_REQUESTPROCESSOR_ID | NO ACTION |

```mermaid
erDiagram
  AD_SCHEDULE ||--o{ R_REQUESTPROCESSOR : ""
  AD_USER ||--o{ R_REQUESTPROCESSOR : ""
  R_REQUESTPROCESSOR ||--o{ R_REQUESTPROCESSORLOG : ""
  R_REQUESTPROCESSOR ||--o{ R_REQUESTPROCESSOR_ROUTE : ""
  R_REQUESTTYPE ||--o{ R_REQUESTPROCESSOR : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

19 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.r_requestprocessor.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
