---
title: "C_DOCBASEGROUP"
order: 77
ekos_generated: true
ekos_estate_version: 1
---

# C_DOCBASEGROUP

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_DocBaseGroup`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `C_DOCBASEGROUP_ID` | NUMBER(10,0) | PK | yes | Document Base Type Group |  | 0 | 0 |
| `C_DOCBASEGROUP_UU` | VARCHAR2(36 CHAR) |  |  | C_DocBaseGroup_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `VALUE` | VARCHAR2(40 CHAR) |  |  | Search Key |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021454` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | C_DOCBASEGROUP.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | C_DOCBASEGROUP.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | C_DOCBASEGROUP.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_DOCBASEGROUPLINE](../../data-model/c/c_docbasegroupline.md) | C_DOCBASEGROUPLINE.C_DOCBASEGROUP_ID → C_DOCBASEGROUP.C_DOCBASEGROUP_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ C_DOCBASEGROUP : ""
  AD_ORG ||--o{ C_DOCBASEGROUP : ""
  AD_USER ||--o{ C_DOCBASEGROUP : ""
  C_DOCBASEGROUP ||--o{ C_DOCBASEGROUPLINE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

10 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `create_table` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `add_constraint` |  | IDEMPIERE-5659 |
| 2023-04-03T11:42 | iD11 | `create_table` |  | IDEMPIERE-5659 |

## Notes

<!-- ekos:manual id="table.c_docbasegroup.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
