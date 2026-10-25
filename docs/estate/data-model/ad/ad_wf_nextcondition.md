---
title: "AD_WF_NEXTCONDITION"
order: 239
ekos_generated: true
ekos_estate_version: 1
---

# AD_WF_NEXTCONDITION

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_AD_WF_NextCondition`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_WF_NEXTCONDITION_ID` | NUMBER(10,0) | PK | yes | Transition Condition |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `AD_WF_NODENEXT_ID` | NUMBER(10,0) |  | yes | Node Transition | [AD_WF_NODENEXT](../../data-model/ad/ad_wf_nodenext.md) | 0 | 1 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 1 |
| `ENTITYTYPE` | VARCHAR2(40 CHAR) |  | yes | Entity Type |  | 0 | 1 |
| `ANDOR` | CHAR(1) |  | yes | And/Or |  | 0 | 1 |
| `AD_COLUMN_ID` | NUMBER(10,0) |  |  | Column | [AD_COLUMN](../../data-model/ad/ad_column.md) | 0 | 1 |
| `OPERATION` | CHAR(2) |  | yes | Operation |  | 0 | 1 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 1 |
| `VALUE2` | VARCHAR2(40 CHAR) |  |  | Value To |  | 1 | 0 |
| `AD_WF_NEXTCONDITION_UU` | VARCHAR2(36 CHAR) |  |  | AD_WF_NextCondition_UU |  | 0 | 1 |
| `SQLSTATEMENT` | VARCHAR2(4000 CHAR) |  |  | SQL Expression/Statement |  | 1 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022895` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_COLUMN](../../data-model/ad/ad_column.md) | AD_WF_NEXTCONDITION.AD_COLUMN_ID → AD_COLUMN.AD_COLUMN_ID | NO ACTION |
| [AD_ENTITYTYPE](../../data-model/ad/ad_entitytype.md) | AD_WF_NEXTCONDITION.ENTITYTYPE → AD_ENTITYTYPE.ENTITYTYPE | NO ACTION |
| [AD_WF_NODENEXT](../../data-model/ad/ad_wf_nodenext.md) | AD_WF_NEXTCONDITION.AD_WF_NODENEXT_ID → AD_WF_NODENEXT.AD_WF_NODENEXT_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_COLUMN ||--o{ AD_WF_NEXTCONDITION : ""
  AD_ENTITYTYPE ||--o{ AD_WF_NEXTCONDITION : ""
  AD_WF_NODENEXT ||--o{ AD_WF_NEXTCONDITION : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Schema history

26 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-11-14T14:00 | i8.2z | `add_column` | SQLStatement | IDEMPIERE-4900 |
| 2021-11-14T14:00 | i8.2z | `add_column` | SQLStatement | IDEMPIERE-4900 |
| 2021-11-14T14:00 | i8.2z | `modify_column` | AD_Column_ID | IDEMPIERE-4900 |
| 2021-11-14T14:00 | i8.2z | `modify_column` | AD_Column_ID | IDEMPIERE-4900 |
| 2021-11-14T14:00 | i8.2z | `modify_column` | AD_Column_ID | IDEMPIERE-4900 |
| 2021-11-14T14:00 | i8.2z | `modify_column` | AD_Column_ID | IDEMPIERE-4900 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_wf_nextcondition.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
