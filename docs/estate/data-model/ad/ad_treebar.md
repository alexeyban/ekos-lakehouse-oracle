---
title: "AD_TREEBAR"
order: 196
ekos_generated: true
ekos_estate_version: 1
---

# AD_TREEBAR

User Shortcuts

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 24 row(s) when profiled

Application model: `?`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_TREE_ID` | NUMBER(10,0) | PK | yes | Tree | [AD_TREE](../../data-model/ad/ad_tree.md) | 0 | 1 |
| `AD_USER_ID` | NUMBER(10,0) | PK | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 4 |
| `NODE_ID` | NUMBER(10,0) | PK | yes | Node |  | 0 | 14 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Client |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 23 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 4 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 13 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 4 |
| `AD_TREEBAR_UU` | VARCHAR2(36 CHAR) |  |  | AD_TreeBar_UU |  | 0 | 24 |
| `ISFAVOURITE` | CHAR(1) |  | yes | Favourite |  | 0 | 1 |
| `LOGINOPENSEQNO` | NUMBER(10,0) |  |  | Login automatic open sequence |  | 24 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020524` | `IsFavourite IN ('Y','N')` |
| `SYS_C0020525` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_TREE](../../data-model/ad/ad_tree.md) | AD_TREEBAR.AD_TREE_ID → AD_TREE.AD_TREE_ID | CASCADE |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_TREEBAR.AD_USER_ID → AD_USER.AD_USER_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_TREE ||--o{ AD_TREEBAR : ""
  AD_USER ||--o{ AD_TREEBAR : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 3 citation(s)

## Schema history

15 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_TREEBAR_UU | IDEMPIERE-3862 |
| 2016-09-09T10:30 | i3.1 | `add_column` | IsFavourite | IDEMPIERE-3000 |
| 2016-09-09T10:30 | i3.1 | `add_column` | LoginOpenSeqNo | IDEMPIERE-3000 |
| 2016-09-09T10:30 | i3.1 | `modify_column` | IsFavourite | IDEMPIERE-3000 |
| 2016-09-09T10:30 | i3.1 | `add_column` | LoginOpenSeqNo | IDEMPIERE-3000 |
| 2016-09-09T10:30 | i3.1 | `add_column` | IsFavourite | IDEMPIERE-3000 |
| 2016-09-09T10:30 | i3.1 | `modify_column` | IsFavourite | IDEMPIERE-3000 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.AD_Menu_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_treebar.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
