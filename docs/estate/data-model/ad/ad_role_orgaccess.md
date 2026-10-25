---
title: "AD_ROLE_ORGACCESS"
order: 157
ekos_generated: true
ekos_estate_version: 1
---

# AD_ROLE_ORGACCESS

Base For OrgList

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 18 row(s) when profiled

Application model: `org.compiere.model.X_AD_Role_OrgAccess`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_ROLE_ID` | NUMBER(10,0) | PK | yes | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 4 |
| `AD_ORG_ID` | NUMBER(10,0) | PK | yes | Organization |  | 0 | 10 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 2 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 12 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 11 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `ISREADONLY` | CHAR(1) |  | yes | Read Only |  | 0 | 1 |
| `AD_ROLE_ORGACCESS_UU` | VARCHAR2(36 CHAR) |  |  | AD_Role_OrgAccess_UU |  | 0 | 18 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021912` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_ROLE_ORGACCESS.AD_ORG_ID → AD_ORG.AD_ORG_ID | CASCADE |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_ROLE_ORGACCESS.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_ORG ||--o{ AD_ROLE_ORGACCESS : ""
  AD_ROLE ||--o{ AD_ROLE_ORGACCESS : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 4 citation(s)

## Schema history

9 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_ROLE_ORGACCESS_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_role_orgaccess.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
