---
title: "AD_RELATIONTYPE"
order: 144
ekos_generated: true
ekos_estate_version: 1
---

# AD_RELATIONTYPE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 6 row(s) when profiled

Application model: `org.compiere.model.X_AD_RelationType`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `AD_REFERENCE_SOURCE_ID` | NUMBER(10,0) |  |  | Source Reference | [AD_REFERENCE](../../data-model/ad/ad_reference.md) | 0 | 5 |
| `AD_REFERENCE_TARGET_ID` | NUMBER(10,0) |  |  | Target Reference | [AD_REFERENCE](../../data-model/ad/ad_reference.md) | 0 | 6 |
| `AD_RELATIONTYPE_ID` | NUMBER(10,0) | PK | yes | Relation Type |  | 0 | 6 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 6 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 6 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `ISDIRECTED` | CHAR(1) |  | yes | Directed |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 6 |
| `ROLE_SOURCE` | VARCHAR2(50 CHAR) |  |  | Source Role |  | 6 | 0 |
| `ROLE_TARGET` | VARCHAR2(50 CHAR) |  |  | Target Role |  | 6 | 0 |
| `TYPE` | CHAR(1) |  | yes | Type |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 6 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `AD_RELATIONTYPE_UU` | VARCHAR2(36 CHAR) |  |  | AD_RelationType_UU |  | 0 | 6 |
| `ENTITYTYPE` | VARCHAR2(40 CHAR) |  |  | Entity Type |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020562` | `IsDirected IN ('Y','N')` |
| `SYS_C0020564` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ENTITYTYPE](../../data-model/ad/ad_entitytype.md) | AD_RELATIONTYPE.ENTITYTYPE → AD_ENTITYTYPE.ENTITYTYPE | NO ACTION |
| [AD_REFERENCE](../../data-model/ad/ad_reference.md) | AD_RELATIONTYPE.AD_REFERENCE_SOURCE_ID → AD_REFERENCE.AD_REFERENCE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_ENTITYTYPE ||--o{ AD_RELATIONTYPE : ""
  AD_REFERENCE ||--o{ AD_RELATIONTYPE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

35 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-09-16T16:00 | i7.1z | `add_constraint` |  | IDEMPIERE-3336 |
| 2020-09-16T16:00 | i7.1z | `add_constraint` |  | IDEMPIERE-3336 |
| 2020-09-16T16:00 | i7.1z | `add_column` | EntityType | IDEMPIERE-3336 |
| 2020-09-16T16:00 | i7.1z | `add_column` | EntityType | IDEMPIERE-3336 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_5_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.EntityType.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_relationtype.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
