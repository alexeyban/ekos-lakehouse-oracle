---
title: "AD_USERDEF_THEME_DETAIL"
order: 222
ekos_generated: true
ekos_estate_version: 1
---

# AD_USERDEF_THEME_DETAIL

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_UserDef_Theme_Detail`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_USERDEF_THEME_DETAIL_ID` | NUMBER(10,0) | PK | yes | Theme Customization Detail |  | 0 | 0 |
| `AD_USERDEF_THEME_DETAIL_UU` | VARCHAR2(36 CHAR) |  |  | AD_UserDef_Theme_Detail_UU |  | 0 | 0 |
| `AD_USERDEF_THEME_ID` | NUMBER(10,0) |  | yes | Theme Customization | [AD_USERDEF_THEME](../../data-model/ad/ad_userdef_theme.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `CURRENTVALUE` | VARCHAR2(255 CHAR) |  | yes | Current Value |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `NEWVALUE` | VARCHAR2(255 CHAR) |  | yes | New Value |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022971` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_USERDEF_THEME_DETAIL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_USERDEF_THEME_DETAIL.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_USERDEF_THEME_DETAIL.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |
| [AD_USERDEF_THEME](../../data-model/ad/ad_userdef_theme.md) | AD_USERDEF_THEME_DETAIL.AD_USERDEF_THEME_ID → AD_USERDEF_THEME.AD_USERDEF_THEME_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_USERDEF_THEME_DETAIL : ""
  AD_ORG ||--o{ AD_USERDEF_THEME_DETAIL : ""
  AD_USER ||--o{ AD_USERDEF_THEME_DETAIL : ""
  AD_USERDEF_THEME ||--o{ AD_USERDEF_THEME_DETAIL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

16 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | NewValue | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `create_table` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | NewValue | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | NewValue | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `modify_column` | NewValue | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |
| 2024-11-12T11:04 | iD12 | `add_constraint` |  | IDEMPIERE-6293 |

## Notes

<!-- ekos:manual id="table.ad_userdef_theme_detail.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
