---
title: "AD_MODELGENERATORTEMPLATE"
order: 88
ekos_generated: true
ekos_estate_version: 1
---

# AD_MODELGENERATORTEMPLATE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_ModelGeneratorTemplate`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_MODELGENERATORTEMPLATE_ID` | NUMBER(10,0) | PK | yes | Model Generator Template |  | 0 | 0 |
| `AD_MODELGENERATORTEMPLATE_UU` | VARCHAR2(36 CHAR) |  |  | AD_ModelGeneratorTemplate_UU |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `COLUMNENTITYTYPE` | VARCHAR2(20 CHAR) |  |  | Column Entity Type |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `FOLDER` | VARCHAR2(255 CHAR) |  |  | Folder |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `PACKAGENAME` | VARCHAR2(60 CHAR) |  |  | Package Name |  | 0 | 0 |
| `TABLEENTITYTYPE` | VARCHAR2(20 CHAR) |  |  | Table Entity Type |  | 0 | 0 |
| `TABLENAME` | VARCHAR2(2000 CHAR) |  |  | DB Table Name |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021958` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_MODELGENERATORTEMPLATE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_MODELGENERATORTEMPLATE.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_MODELGENERATORTEMPLATE.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_MODELGENERATORTEMPLATE : ""
  AD_ORG ||--o{ AD_MODELGENERATORTEMPLATE : ""
  AD_USER ||--o{ AD_MODELGENERATORTEMPLATE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

12 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-07-10T09:13 | iD11 | `modify_column` | TableName | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `modify_column` | TableName | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `create_table` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `create_table` |  | IDEMPIERE-5796 |
| 2023-07-10T09:13 | iD11 | `add_constraint` |  | IDEMPIERE-5796 |

## Notes

<!-- ekos:manual id="table.ad_modelgeneratortemplate.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
