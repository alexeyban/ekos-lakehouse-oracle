---
title: "CM_CHATTYPEUPDATE"
order: 14
ekos_generated: true
ekos_estate_version: 1
---

# CM_CHATTYPEUPDATE

Area [CM](../../data-model/cm/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_CM_ChatTypeUpdate`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `CM_CHATTYPE_ID` | NUMBER(10,0) | PK | yes | Chat Type | [CM_CHATTYPE](../../data-model/cm/cm_chattype.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) | PK | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `ISSELFSERVICE` | CHAR(1) |  | yes | Self-Service |  | 0 | 0 |
| `CM_CHATTYPEUPDATE_UU` | VARCHAR2(36 CHAR) |  |  | CM_ChatTypeUpdate_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022877` | `IsSelfService in ('Y','N')` |
| `SYS_C0022879` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | CM_CHATTYPEUPDATE.AD_USER_ID → AD_USER.AD_USER_ID | CASCADE |
| [CM_CHATTYPE](../../data-model/cm/cm_chattype.md) | CM_CHATTYPEUPDATE.CM_CHATTYPE_ID → CM_CHATTYPE.CM_CHATTYPE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_USER ||--o{ CM_CHATTYPEUPDATE : ""
  CM_CHATTYPE ||--o{ CM_CHATTYPEUPDATE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 3 citation(s)

## Schema history

9 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CM_CHATTYPEUPDATE_UU | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.cm_chattypeupdate.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
