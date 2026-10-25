---
title: "AD_USERDEF_FORM"
order: 214
ekos_generated: true
ekos_estate_version: 1
---

# AD_USERDEF_FORM

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_AD_UserDef_Form`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes | Tenant |  |  |  |
| `AD_Form_ID` | NUMERIC(10) |  | yes | Special Form | [AD_FORM](../../data-model/ad/ad_form.md) |  |  |
| `AD_Language` | VARCHAR(6) |  |  | Language |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes | Organization |  |  |  |
| `AD_Role_ID` | NUMERIC(10) |  |  | Role | [AD_ROLE](../../data-model/ad/ad_role.md) |  |  |
| `AD_User_ID` | NUMERIC(10) |  | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) |  |  |
| `AD_UserDef_Form_ID` | NUMERIC(10) | PK | yes | User defined Form |  |  |  |
| `AD_UserDef_Form_UU` | UUID |  |  | AD_UserDef_Form_UU |  |  |  |
| `Created` | TIMESTAMP |  | yes | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes | Created By |  |  |  |
| `Description` | VARCHAR(255) |  |  | Description |  |  |  |
| `Help` | VARCHAR(2000) |  |  | Comment/Help |  |  |  |
| `ImageURL` | VARCHAR(120) |  |  | Image URL |  |  |  |
| `IsActive` | CHAR(1) |  | yes | Active |  |  |  |
| `Name` | VARCHAR(60) |  | yes | Name |  |  |  |
| `Updated` | TIMESTAMP |  | yes | Updated |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes | Updated By |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
|  | `IsActive IN ('Y', 'N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Schema history

28 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `modify_column` | Name | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `modify_column` | AD_User_ID | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `create_index` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `create_table` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `modify_column` | Name | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `create_index` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `create_table` |  | IDEMPIERE-6893 |
| 2026-03-06T16:58 | iD13 | `add_constraint` |  | IDEMPIERE-6893 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_userdef_form.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
