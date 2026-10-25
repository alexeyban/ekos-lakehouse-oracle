---
title: "AD_LABELCATEGORYTABLE"
order: 74
ekos_generated: true
ekos_estate_version: 1
---

# AD_LABELCATEGORYTABLE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_LabelCategoryTable`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_LABELCATEGORYTABLE_ID` | NUMBER(10,0) | PK | yes | Label Category Table Access |  | 0 | 0 |
| `AD_LABELCATEGORYTABLE_UU` | VARCHAR2(36 CHAR) |  |  | Label Category Table Access |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  |  | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  |  | Organization |  | 0 | 0 |
| `CREATED` | DATE |  |  | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  |  | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  |  | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  |  | Updated By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  |  | Active |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `AD_LABELCATEGORY_ID` | NUMBER(10,0) |  | yes | Label Category | [AD_LABELCATEGORY](../../data-model/ad/ad_labelcategory.md) | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020527` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LABELCATEGORY](../../data-model/ad/ad_labelcategory.md) | AD_LABELCATEGORYTABLE.AD_LABELCATEGORY_ID → AD_LABELCATEGORY.AD_LABELCATEGORY_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_LABELCATEGORYTABLE.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_LABELCATEGORY ||--o{ AD_LABELCATEGORYTABLE : ""
  AD_TABLE ||--o{ AD_LABELCATEGORYTABLE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

30 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2022-05-13T11:18 | iD10 | `add_column` | IsActive | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_constraint` |  | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_LabelCategory_ID | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | Created | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_LabelCategoryTable_UU | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_Table_ID | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | Updated | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `create_table` |  | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | Updated | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `create_table` |  | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_constraint` |  | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_Table_ID | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_Org_ID | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | CreatedBy | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | UpdatedBy | IDEMPIERE-5259 |

## Notes

<!-- ekos:manual id="table.ad_labelcategorytable.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
