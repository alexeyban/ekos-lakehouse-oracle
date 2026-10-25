---
title: "AD_PASSWORD_HISTORY"
order: 106
ekos_generated: true
ekos_estate_version: 1
---

# AD_PASSWORD_HISTORY

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Password_History`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PASSWORD_HISTORY_ID` | NUMBER(10,0) | PK | yes | Password History ID |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `PASSWORD` | VARCHAR2(1024 CHAR) |  |  |  |  | 0 | 0 |
| `SALT` | VARCHAR2(16 CHAR) |  |  | Salt |  | 0 | 0 |
| `DATEPASSWORDCHANGED` | DATE |  |  | Date Password Changed |  | 0 | 0 |
| `AD_PASSWORD_HISTORY_UU` | VARCHAR2(36 CHAR) |  |  | AD_Password_History_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020609` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_PASSWORD_HISTORY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_PASSWORD_HISTORY.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_PASSWORD_HISTORY.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_PASSWORD_HISTORY : ""
  AD_ORG ||--o{ AD_PASSWORD_HISTORY : ""
  AD_USER ||--o{ AD_PASSWORD_HISTORY : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

39 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-10-30T11:24 | iD12 | `modify_column` | Salt | IDEMPIERE-6712 |
| 2025-10-30T11:24 | iD12 | `modify_column` | Salt | IDEMPIERE-6712 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | SALT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PASSWORD_HISTORY_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PASSWORD | IDEMPIERE-3862 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | Updated | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | Created | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | IsActive | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | UpdatedBy | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | AD_Client_ID | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | Created | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | AD_Org_ID | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | Updated | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `add_constraint` |  | IDEMPIERE-2558 |
| 2016-12-21T23:02 | i4.1 | `modify_column` | AD_Org_ID | IDEMPIERE-2558 |

## Notes

<!-- ekos:manual id="table.ad_password_history.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
