---
title: "R_STATUS"
order: 27
ekos_generated: true
ekos_estate_version: 1
---

# R_STATUS

Area [R](../../data-model/r/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 4 row(s) when profiled

Application model: `org.compiere.model.X_R_Status`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `R_STATUS_ID` | NUMBER(10,0) | PK | yes | Status |  | 0 | 4 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 4 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 4 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 4 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 4 | 0 |
| `ISDEFAULT` | CHAR(1) |  | yes | Default |  | 0 | 2 |
| `ISOPEN` | CHAR(1) |  | yes | Open Status |  | 0 | 2 |
| `ISCLOSED` | CHAR(1) |  | yes | Closed Status |  | 0 | 2 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 4 |
| `NEXT_STATUS_ID` | NUMBER(10,0) |  |  | Next Status | [R_STATUS](../../data-model/r/r_status.md) | 2 | 2 |
| `UPDATE_STATUS_ID` | NUMBER(10,0) |  |  | Update Status | [R_STATUS](../../data-model/r/r_status.md) | 2 | 1 |
| `TIMEOUTDAYS` | NUMBER(10,0) |  |  | Timeout in Days |  | 0 | 3 |
| `ISWEBCANUPDATE` | CHAR(1) |  | yes | Web Can Update |  | 0 | 2 |
| `ISFINALCLOSE` | CHAR(1) |  | yes | Final Close |  | 0 | 2 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 4 |
| `R_STATUSCATEGORY_ID` | NUMBER(10,0) |  | yes | Status Category | [R_STATUSCATEGORY](../../data-model/r/r_statuscategory.md) | 0 | 1 |
| `R_STATUS_UU` | VARCHAR2(36 CHAR) |  |  | R_Status_UU |  | 0 | 4 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022501` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [R_STATUS](../../data-model/r/r_status.md) | R_STATUS.NEXT_STATUS_ID → R_STATUS.R_STATUS_ID | NO ACTION |
| [R_STATUSCATEGORY](../../data-model/r/r_statuscategory.md) | R_STATUS.R_STATUSCATEGORY_ID → R_STATUSCATEGORY.R_STATUSCATEGORY_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [R_REQUEST](../../data-model/r/r_request.md) | R_REQUEST.R_STATUS_ID → R_STATUS.R_STATUS_ID | NO ACTION |
| [R_REQUESTACTION](../../data-model/r/r_requestaction.md) | R_REQUESTACTION.R_STATUS_ID → R_STATUS.R_STATUS_ID | NO ACTION |
| [R_STATUS](../../data-model/r/r_status.md) | R_STATUS.NEXT_STATUS_ID → R_STATUS.R_STATUS_ID | NO ACTION |

```mermaid
erDiagram
  R_STATUS ||--o{ R_REQUEST : ""
  R_STATUS ||--o{ R_REQUESTACTION : ""
  R_STATUS ||--o{ R_STATUS : ""
  R_STATUSCATEGORY ||--o{ R_STATUS : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

27 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | R_STATUS_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.r_status.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
