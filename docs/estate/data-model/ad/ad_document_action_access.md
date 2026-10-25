---
title: "AD_DOCUMENT_ACTION_ACCESS"
order: 41
ekos_generated: true
ekos_estate_version: 1
---

# AD_DOCUMENT_ACTION_ACCESS

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2156 row(s) when profiled

Application model: `org.compiere.model.X_AD_Document_Action_Access`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 7 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 7 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `C_DOCTYPE_ID` | NUMBER(10,0) | PK | yes | Document Type | [C_DOCTYPE](../../data-model/c/c_doctype.md) | 0 | 52 |
| `AD_ROLE_ID` | NUMBER(10,0) | PK | yes | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 4 |
| `AD_REF_LIST_ID` | NUMBER(10,0) | PK | yes | Reference List | [AD_REF_LIST](../../data-model/ad/ad_ref_list.md) | 0 | 14 |
| `AD_DOCUMENT_ACTION_ACCESS_UU` | VARCHAR2(36 CHAR) |  |  | AD_Document_Action_Access_UU |  | 0 | 2156 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_REF_LIST](../../data-model/ad/ad_ref_list.md) | AD_DOCUMENT_ACTION_ACCESS.AD_REF_LIST_ID → AD_REF_LIST.AD_REF_LIST_ID | NO ACTION |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_DOCUMENT_ACTION_ACCESS.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | NO ACTION |
| [C_DOCTYPE](../../data-model/c/c_doctype.md) | AD_DOCUMENT_ACTION_ACCESS.C_DOCTYPE_ID → C_DOCTYPE.C_DOCTYPE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_REF_LIST ||--o{ AD_DOCUMENT_ACTION_ACCESS : ""
  AD_ROLE ||--o{ AD_DOCUMENT_ACTION_ACCESS : ""
  C_DOCTYPE ||--o{ AD_DOCUMENT_ACTION_ACCESS : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 6 citation(s)

## Written by

| kind | name |
|---|---|
| Procedure | [role_access_update](../../logic/role_access_update.md) |

## Schema history

11 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_DOCUMENT_ACTION_ACCESS_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_document_action_access.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
