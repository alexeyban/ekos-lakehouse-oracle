---
title: "AD_USERDEF_PROC"
order: 218
ekos_generated: true
ekos_estate_version: 1
---

# AD_USERDEF_PROC

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_UserDef_Proc`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_USERDEF_PROC_ID` | NUMBER(10,0) | PK | yes | User defined Process |  | 0 | 0 |
| `AD_USERDEF_PROC_UU` | VARCHAR2(36 CHAR) |  |  | AD_UserDef_Proc_UU |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_ROLE_ID` | NUMBER(10,0) |  |  | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  |  | Name |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) |  |  | Language |  | 0 | 0 |
| `ISUSERUPDATEABLE` | CHAR(1) |  |  | User updatable |  | 0 | 0 |
| `AD_PROCESS_ID` | NUMBER(10,0) |  | yes | Process | [AD_PROCESS](../../data-model/ad/ad_process.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022473` | `IsActive IN ('Y','N')` |
| `SYS_C0022474` | `IsUserUpdateable IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_USERDEF_PROC.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [AD_PROCESS](../../data-model/ad/ad_process.md) | AD_USERDEF_PROC.AD_PROCESS_ID → AD_PROCESS.AD_PROCESS_ID | NO ACTION |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_USERDEF_PROC.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | CASCADE |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_USERDEF_PROC.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_USERDEF_PROC_PARAMETER](../../data-model/ad/ad_userdef_proc_parameter.md) | AD_USERDEF_PROC_PARAMETER.AD_USERDEF_PROC_ID → AD_USERDEF_PROC.AD_USERDEF_PROC_ID | NO ACTION |

```mermaid
erDiagram
  AD_LANGUAGE ||--o{ AD_USERDEF_PROC : ""
  AD_PROCESS ||--o{ AD_USERDEF_PROC : ""
  AD_ROLE ||--o{ AD_USERDEF_PROC : ""
  AD_USER ||--o{ AD_USERDEF_PROC : ""
  AD_USERDEF_PROC ||--o{ AD_USERDEF_PROC_PARAMETER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

51 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2021-06-02T10:00 | i8.2 | `create_index` |  | IDEMPIERE-4813 |
| 2021-06-02T10:00 | i8.2 | `create_index` |  | IDEMPIERE-4813 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_USERDEF_PROC_UU | IDEMPIERE-3862 |
| 2019-05-16T09:20 | i6.2z | `add_constraint` |  | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_column` | Description | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_constraint` |  | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_column` | AD_User_ID | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_column` | AD_Org_ID | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_column` | CreatedBy | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_column` | Name | IDEMPIERE-3971 |
| 2019-05-16T09:20 | i6.2z | `add_column` | Updated | IDEMPIERE-3971 |

## Notes

<!-- ekos:manual id="table.ad_userdef_proc.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
