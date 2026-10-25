---
title: "AD_SCHEDULERRECIPIENT"
order: 162
ekos_generated: true
ekos_estate_version: 1
---

# AD_SCHEDULERRECIPIENT

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_AD_SchedulerRecipient`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_SCHEDULERRECIPIENT_ID` | NUMBER(10,0) | PK | yes | Scheduler Recipient |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `AD_SCHEDULER_ID` | NUMBER(10,0) |  | yes | Scheduler | [AD_SCHEDULER](../../data-model/ad/ad_scheduler.md) | 0 | 1 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 1 |
| `AD_ROLE_ID` | NUMBER(10,0) |  |  | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 1 | 0 |
| `AD_SCHEDULERRECIPIENT_UU` | VARCHAR2(36 CHAR) |  |  | AD_SchedulerRecipient_UU |  | 0 | 1 |
| `ISUPLOAD` | CHAR(1) |  | yes | Upload |  | 0 | 1 |
| `AD_AUTHORIZATIONACCOUNT_ID` | NUMBER(10,0) |  |  | Authorization Account | [AD_AUTHORIZATIONACCOUNT](../../data-model/ad/ad_authorizationaccount.md) | 1 | 0 |
| `FILENAME` | VARCHAR2(255 CHAR) |  |  | File Name |  | 1 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022488` | `IsUpload IN ('Y','N')` |
| `SYS_C0022490` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_AUTHORIZATIONACCOUNT](../../data-model/ad/ad_authorizationaccount.md) | AD_SCHEDULERRECIPIENT.AD_AUTHORIZATIONACCOUNT_ID → AD_AUTHORIZATIONACCOUNT.AD_AUTHORIZATIONACCOUNT_ID | NO ACTION |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_SCHEDULERRECIPIENT.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | NO ACTION |
| [AD_SCHEDULER](../../data-model/ad/ad_scheduler.md) | AD_SCHEDULERRECIPIENT.AD_SCHEDULER_ID → AD_SCHEDULER.AD_SCHEDULER_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_SCHEDULERRECIPIENT.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_AUTHORIZATIONACCOUNT ||--o{ AD_SCHEDULERRECIPIENT : ""
  AD_ROLE ||--o{ AD_SCHEDULERRECIPIENT : ""
  AD_SCHEDULER ||--o{ AD_SCHEDULERRECIPIENT : ""
  AD_USER ||--o{ AD_SCHEDULERRECIPIENT : ""
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
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-05-09T10:48 | i8.2z | `add_column` | IsUpload | IDEMPIERE-4771 |
| 2021-05-09T10:48 | i8.2z | `add_constraint` |  | IDEMPIERE-4771 |
| 2021-05-09T10:48 | i8.2z | `add_column` | FileName | IDEMPIERE-4771 |
| 2021-05-09T10:48 | i8.2z | `add_constraint` |  | IDEMPIERE-4771 |
| 2021-05-09T10:48 | i8.2z | `add_column` | IsUpload | IDEMPIERE-4771 |
| 2021-05-09T10:48 | i8.2z | `add_column` | AD_AuthorizationAccount_ID | IDEMPIERE-4771 |
| 2021-05-09T10:48 | i8.2z | `add_column` | FileName | IDEMPIERE-4771 |

## Notes

<!-- ekos:manual id="table.ad_schedulerrecipient.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
