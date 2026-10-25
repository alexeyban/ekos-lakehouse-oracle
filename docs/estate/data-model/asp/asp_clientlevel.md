---
title: "ASP_CLIENTLEVEL"
order: 2
ekos_generated: true
ekos_estate_version: 1
---

# ASP_CLIENTLEVEL

Area [ASP](../../data-model/asp/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_ASP_ClientLevel`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ASP_CLIENTLEVEL_ID` | NUMBER(10,0) | PK | yes | Tenant Level |  | 0 | 0 |
| `ASP_LEVEL_ID` | NUMBER(10,0) |  | yes | ASP Level | [ASP_LEVEL](../../data-model/asp/asp_level.md) | 0 | 0 |
| `ASP_MODULE_ID` | NUMBER(10,0) |  | yes | ASP Module | [ASP_MODULE](../../data-model/asp/asp_module.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `ASP_CLIENTLEVEL_UU` | VARCHAR2(36 CHAR) |  |  | ASP_ClientLevel_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019450` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [ASP_LEVEL](../../data-model/asp/asp_level.md) | ASP_CLIENTLEVEL.ASP_LEVEL_ID → ASP_LEVEL.ASP_LEVEL_ID | NO ACTION |
| [ASP_MODULE](../../data-model/asp/asp_module.md) | ASP_CLIENTLEVEL.ASP_MODULE_ID → ASP_MODULE.ASP_MODULE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  ASP_LEVEL ||--o{ ASP_CLIENTLEVEL : ""
  ASP_MODULE ||--o{ ASP_CLIENTLEVEL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

24 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | ASP_CLIENTLEVEL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2017-05-12T15:35 | i4.1 | `create_index` |  | IDEMPIERE-3358 |
| 2017-05-12T15:35 | i4.1 | `create_index` |  | IDEMPIERE-3358 |
| 2017-04-29T19:25 | i4.1 | `create_index` |  | IDEMPIERE-3358 |

## Notes

<!-- ekos:manual id="table.asp_clientlevel.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
