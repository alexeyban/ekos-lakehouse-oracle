---
title: "C_JOB"
order: 101
ekos_generated: true
ekos_estate_version: 1
---

# C_JOB

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 4 row(s) when profiled

Application model: `org.compiere.model.X_C_Job`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_JOB_ID` | NUMBER(10,0) | PK | yes | Position |  | 0 | 4 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 4 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 4 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 4 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 3 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 4 | 0 |
| `C_JOBCATEGORY_ID` | NUMBER(10,0) |  | yes | Position Category | [C_JOBCATEGORY](../../data-model/c/c_jobcategory.md) | 0 | 3 |
| `ISEMPLOYEE` | CHAR(1) |  | yes | Employee |  | 0 | 2 |
| `C_JOB_UU` | VARCHAR2(36 CHAR) |  |  | C_Job_UU |  | 0 | 4 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021783` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_JOBCATEGORY](../../data-model/c/c_jobcategory.md) | C_JOB.C_JOBCATEGORY_ID → C_JOBCATEGORY.C_JOBCATEGORY_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | AD_USER.C_JOB_ID → C_JOB.C_JOB_ID | NO ACTION |
| [C_JOBASSIGNMENT](../../data-model/c/c_jobassignment.md) | C_JOBASSIGNMENT.C_JOB_ID → C_JOB.C_JOB_ID | NO ACTION |
| [C_JOBREMUNERATION](../../data-model/c/c_jobremuneration.md) | C_JOBREMUNERATION.C_JOB_ID → C_JOB.C_JOB_ID | NO ACTION |
| [M_OPERATIONRESOURCE](../../data-model/m/m_operationresource.md) | M_OPERATIONRESOURCE.C_JOB_ID → C_JOB.C_JOB_ID | NO ACTION |

```mermaid
erDiagram
  C_JOB ||--o{ AD_USER : ""
  C_JOB ||--o{ C_JOBASSIGNMENT : ""
  C_JOB ||--o{ C_JOBREMUNERATION : ""
  C_JOB ||--o{ M_OPERATIONRESOURCE : ""
  C_JOBCATEGORY ||--o{ C_JOB : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

18 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_JOB_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_job.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
