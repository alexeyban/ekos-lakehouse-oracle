---
title: "PA_DOCUMENTSTATUSACCESS"
order: 10
ekos_generated: true
ekos_estate_version: 1
---

# PA_DOCUMENTSTATUSACCESS

Area [PA](../../data-model/pa/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_PA_DocumentStatusAccess`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `PA_DOCUMENTSTATUSACCESS_ID` | NUMBER(10,0) | PK | yes | Document Status Access |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `PA_DOCUMENTSTATUSACCESS_UU` | VARCHAR2(36 CHAR) |  |  | PA_DocumentStatusAccess_UU |  | 0 | 0 |
| `AD_ROLE_ID` | NUMBER(10,0) |  |  | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `PA_DOCUMENTSTATUS_ID` | NUMBER(10,0) |  |  | Document Status | [PA_DOCUMENTSTATUS](../../data-model/pa/pa_documentstatus.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020830` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ROLE](../../data-model/ad/ad_role.md) | PA_DOCUMENTSTATUSACCESS.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | CASCADE |
| [AD_USER](../../data-model/ad/ad_user.md) | PA_DOCUMENTSTATUSACCESS.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [PA_DOCUMENTSTATUS](../../data-model/pa/pa_documentstatus.md) | PA_DOCUMENTSTATUSACCESS.PA_DOCUMENTSTATUS_ID → PA_DOCUMENTSTATUS.PA_DOCUMENTSTATUS_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_ROLE ||--o{ PA_DOCUMENTSTATUSACCESS : ""
  AD_USER ||--o{ PA_DOCUMENTSTATUSACCESS : ""
  PA_DOCUMENTSTATUS ||--o{ PA_DOCUMENTSTATUSACCESS : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

34 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2021-06-28T22:30 | i8.2z | `add_column` | PA_DocumentStatus_ID | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | UpdatedBy | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `create_index` |  | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | PA_DocumentStatusAccess_UU | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | PA_DocumentStatus_ID | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | CreatedBy | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | CreatedBy | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | AD_User_ID | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `create_index` |  | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | AD_Org_ID | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | UpdatedBy | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | Updated | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_constraint` |  | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | IsActive | IDEMPIERE-4836 |
| 2021-06-28T22:30 | i8.2z | `add_column` | Updated | IDEMPIERE-4836 |

## Notes

<!-- ekos:manual id="table.pa_documentstatusaccess.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
