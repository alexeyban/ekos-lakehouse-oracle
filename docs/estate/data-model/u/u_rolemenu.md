---
title: "U_ROLEMENU"
order: 3
ekos_generated: true
ekos_estate_version: 1
---

# U_ROLEMENU

Area [U](../../data-model/u/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 74 row(s) when profiled

Application model: `org.compiere.model.X_U_RoleMenu`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `U_ROLEMENU_ID` | NUMBER(10,0) | PK | yes | Role Menu |  | 0 | 74 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 57 |
| `CREATEDBY` | INTEGER |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 57 |
| `UPDATEDBY` | INTEGER |  | yes | Updated By |  | 0 | 1 |
| `AD_ROLE_ID` | NUMBER(10,0) |  | yes | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 1 |
| `U_WEBMENU_ID` | NUMBER(10,0) |  | yes | Web Menu | [U_WEBMENU](../../data-model/u/u_webmenu.md) | 0 | 73 |
| `U_ROLEMENU_UU` | VARCHAR2(36 CHAR) |  |  | U_RoleMenu_UU |  | 0 | 74 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019782` | `IsActive IN ('Y', 'N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ROLE](../../data-model/ad/ad_role.md) | U_ROLEMENU.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | NO ACTION |
| [U_WEBMENU](../../data-model/u/u_webmenu.md) | U_ROLEMENU.U_WEBMENU_ID → U_WEBMENU.U_WEBMENU_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_ROLE ||--o{ U_ROLEMENU : ""
  U_WEBMENU ||--o{ U_ROLEMENU : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

11 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | U_ROLEMENU_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-07-01T21:28 | i7.1 | `modify_column` | UpdatedBy | IDEMPIERE-4355 |
| 2020-07-01T21:28 | i7.1 | `modify_column` | CreatedBy | IDEMPIERE-4355 |

## Notes

<!-- ekos:manual id="table.u_rolemenu.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
