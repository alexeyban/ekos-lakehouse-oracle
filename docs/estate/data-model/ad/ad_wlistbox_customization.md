---
title: "AD_WLISTBOX_CUSTOMIZATION"
order: 251
ekos_generated: true
ekos_estate_version: 1
---

# AD_WLISTBOX_CUSTOMIZATION

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Wlistbox_Customization`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `AD_WLISTBOX_CUSTOMIZATION_ID` | NUMBER(10,0) | PK | yes | Customization of the Wlistbox |  | 0 | 0 |
| `AD_WLISTBOX_CUSTOMIZATION_UU` | VARCHAR2(36 CHAR) |  |  | AD_Wlistbox_Customization_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `CUSTOM` | VARCHAR2(4000 CHAR) |  | yes | Custom |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `WLISTBOXNAME` | VARCHAR2(80 CHAR) |  | yes | WlistboxName |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022614` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | AD_WLISTBOX_CUSTOMIZATION.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_USER ||--o{ AD_WLISTBOX_CUSTOMIZATION : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

9 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2022-05-02T18:37 | i9 | `modify_column` | Custom | IDEMPIERE-4863 |
| 2022-05-02T18:37 | i9 | `modify_column` | Custom | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `create_index` |  | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `create_table` |  | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `create_table` |  | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `create_index` |  | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `add_constraint` |  | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `create_index` |  | IDEMPIERE-4863 |
| 2021-10-08T12:00 | i8.2z | `add_constraint` |  | IDEMPIERE-4863 |

## Notes

<!-- ekos:manual id="table.ad_wlistbox_customization.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
