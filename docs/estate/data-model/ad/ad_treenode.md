---
title: "AD_TREENODE"
order: 197
ekos_generated: true
ekos_estate_version: 1
---

# AD_TREENODE

Generic TreeNodes

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 406 row(s) when profiled

Application model: `org.compiere.model.X_AD_TreeNode`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_TREE_ID` | NUMBER(10,0) | PK | yes | Tree | [AD_TREE](../../data-model/ad/ad_tree.md) | 0 | 16 |
| `NODE_ID` | NUMBER(10,0) | PK | yes | Node |  | 0 | 385 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 3 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 39 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 53 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `PARENT_ID` | NUMBER(10,0) |  |  | Parent |  | 13 | 70 |
| `SEQNO` | NUMBER(10,0) |  |  | Sequence |  | 0 | 235 |
| `AD_TREENODE_UU` | VARCHAR2(36 CHAR) |  |  | AD_TreeNode_UU |  | 0 | 406 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021466` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_TREE](../../data-model/ad/ad_tree.md) | AD_TREENODE.AD_TREE_ID → AD_TREE.AD_TREE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_TREE ||--o{ AD_TREENODE : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_app, deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 5 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [IsMemberOfAcctSchema](../../logic/ismemberofacctschema.md) |
| Procedure | [ismemberofacctschema](../../logic/ismemberofacctschema.md) |

## Schema history

7 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_TREENODE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.SeqNo.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_treenode.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
