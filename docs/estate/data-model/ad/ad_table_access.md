---
title: "AD_TABLE_ACCESS"
order: 184
ekos_generated: true
ekos_estate_version: 1
---

# AD_TABLE_ACCESS

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_AD_Table_Access`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_ROLE_ID` | NUMBER(10,0) | PK | yes | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 1 |
| `AD_TABLE_ID` | NUMBER(10,0) | PK | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 1 |
| `ACCESSTYPERULE` | CHAR(1) | PK | yes | Access Type |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `ISREADONLY` | CHAR(1) |  | yes | Read Only |  | 0 | 1 |
| `ISCANREPORT` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `ISCANEXPORT` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `ISEXCLUDE` | CHAR(1) |  | yes | Exclude |  | 0 | 1 |
| `AD_TABLE_ACCESS_UU` | VARCHAR2(36 CHAR) |  |  | AD_Table_Access_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021492` | `IsCanExport in ('Y','N')` |
| `SYS_C0021493` | `IsReadOnly in ('Y','N')` |
| `SYS_C0021494` | `IsExclude in ('Y','N')` |
| `SYS_C0021497` | `IsActive in ('Y','N')` |
| `SYS_C0021498` | `IsCanReport in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_TABLE_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_TABLE_ACCESS.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_TABLE_ACCESS.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | CASCADE |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_TABLE_ACCESS.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_TABLE_ACCESS : ""
  AD_ORG ||--o{ AD_TABLE_ACCESS : ""
  AD_ROLE ||--o{ AD_TABLE_ACCESS : ""
  AD_TABLE ||--o{ AD_TABLE_ACCESS : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Schema history

13 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_TABLE_ACCESS_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_table_access.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
