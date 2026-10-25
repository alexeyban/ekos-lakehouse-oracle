---
title: "C_RECURRINGGROUP"
order: 147
ekos_generated: true
ekos_estate_version: 1
---

# C_RECURRINGGROUP

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_RecurringGroup`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `C_RECURRINGGROUP_ID` | NUMBER(10,0) | PK | yes | Recurring Group |  | 0 | 0 |
| `C_RECURRINGGROUP_UU` | VARCHAR2(36 CHAR) |  |  | C_RecurringGroup_UU |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019874` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | C_RECURRINGGROUP.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | C_RECURRINGGROUP.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | C_RECURRINGGROUP.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_RECURRING](../../data-model/c/c_recurring.md) | C_RECURRING.C_RECURRINGGROUP_ID → C_RECURRINGGROUP.C_RECURRINGGROUP_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ C_RECURRINGGROUP : ""
  AD_ORG ||--o{ C_RECURRINGGROUP : ""
  AD_USER ||--o{ C_RECURRINGGROUP : ""
  C_RECURRINGGROUP ||--o{ C_RECURRING : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

15 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | VALUE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_RECURRINGGROUP_UU | IDEMPIERE-3862 |
| 2014-07-27T15:45 | i2.0z | `create_table` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `create_table` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |
| 2014-07-27T15:45 | i2.0z | `add_constraint` |  | IDEMPIERE-2100 |

## Notes

<!-- ekos:manual id="table.c_recurringgroup.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
