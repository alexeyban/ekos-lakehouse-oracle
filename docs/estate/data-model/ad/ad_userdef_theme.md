---
title: "AD_USERDEF_THEME"
order: 221
ekos_generated: true
ekos_estate_version: 1
---

# AD_USERDEF_THEME

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_UserDef_Theme`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_ROLE_ID` | NUMBER(10,0) |  |  | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `AD_USERDEF_THEME_ID` | NUMBER(10,0) | PK | yes | Theme Customization |  | 0 | 0 |
| `AD_USERDEF_THEME_UU` | VARCHAR2(36 CHAR) |  |  | AD_UserDef_Theme_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `THEME` | VARCHAR2(60 CHAR) |  | yes | Theme |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `STYLESHEET` | VARCHAR2(512 CHAR) |  |  | Stylesheet |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020468` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_USERDEF_THEME.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_USERDEF_THEME.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_USERDEF_THEME.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | CASCADE |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_USERDEF_THEME.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_USERDEF_THEME_DETAIL](../../data-model/ad/ad_userdef_theme_detail.md) | AD_USERDEF_THEME_DETAIL.AD_USERDEF_THEME_ID → AD_USERDEF_THEME.AD_USERDEF_THEME_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_USERDEF_THEME : ""
  AD_ORG ||--o{ AD_USERDEF_THEME : ""
  AD_ROLE ||--o{ AD_USERDEF_THEME : ""
  AD_USER ||--o{ AD_USERDEF_THEME : ""
  AD_USERDEF_THEME ||--o{ AD_USERDEF_THEME_DETAIL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

24 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-11-25T15:14 | iD12 | `create_index` |  | IDEMPIERE-6293 |
| 2024-11-25T15:14 | iD12 | `create_index` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `create_table` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | AD_Role_ID | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_column` | Stylesheet | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_column` | Stylesheet | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | Stylesheet | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | AD_User_ID | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `create_table` |  | IDEMPIERE-6293 |

## Notes

<!-- ekos:manual id="table.ad_userdef_theme.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
