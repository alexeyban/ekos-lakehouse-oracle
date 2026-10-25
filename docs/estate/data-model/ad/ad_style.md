---
title: "AD_STYLE"
order: 173
ekos_generated: true
ekos_estate_version: 1
---

# AD_STYLE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_AD_Style`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `AD_STYLE_ID` | NUMBER(10,0) | PK | yes | Style |  | 0 | 1 |
| `AD_STYLE_UU` | VARCHAR2(36 CHAR) |  | yes | Style |  | 0 | 1 |
| `CREATED` | DATE |  |  | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `ENTITYTYPE` | VARCHAR2(40 CHAR) |  | yes | Entity Type |  | 0 | 1 |
| `ISWRAPWITHSPAN` | CHAR(1) |  | yes | Wrap With Span |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020304` | `IsActive IN ('Y','N')` |
| `SYS_C0020305` | `IsWrapWithSpan IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ENTITYTYPE](../../data-model/ad/ad_entitytype.md) | AD_STYLE.ENTITYTYPE → AD_ENTITYTYPE.ENTITYTYPE | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_FIELD](../../data-model/ad/ad_field.md) | AD_FIELD.AD_FIELDSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_INFOCOLUMN](../../data-model/ad/ad_infocolumn.md) | AD_INFOCOLUMN.AD_FIELDSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_LABEL](../../data-model/ad/ad_label.md) | AD_LABEL.AD_LABELSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_LABELCATEGORY](../../data-model/ad/ad_labelcategory.md) | AD_LABELCATEGORY.AD_LABELSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_PRINTFORMATITEM](../../data-model/ad/ad_printformatitem.md) | AD_PRINTFORMATITEM.AD_FIELDSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_SEARCHDEFINITION](../../data-model/ad/ad_searchdefinition.md) | AD_SEARCHDEFINITION.AD_STYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_STATUSLINE](../../data-model/ad/ad_statusline.md) | AD_STATUSLINE.AD_STYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_STYLELINE](../../data-model/ad/ad_styleline.md) | AD_STYLELINE.AD_STYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_USERDEF_FIELD](../../data-model/ad/ad_userdef_field.md) | AD_USERDEF_FIELD.AD_FIELDSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |
| [AD_USERDEF_INFO_COLUMN](../../data-model/ad/ad_userdef_info_column.md) | AD_USERDEF_INFO_COLUMN.AD_FIELDSTYLE_ID → AD_STYLE.AD_STYLE_ID | NO ACTION |

```mermaid
erDiagram
  AD_ENTITYTYPE ||--o{ AD_STYLE : ""
  AD_STYLE ||--o{ AD_FIELD : ""
  AD_STYLE ||--o{ AD_INFOCOLUMN : ""
  AD_STYLE ||--o{ AD_LABEL : ""
  AD_STYLE ||--o{ AD_LABELCATEGORY : ""
  AD_STYLE ||--o{ AD_PRINTFORMATITEM : ""
  AD_STYLE ||--o{ AD_SEARCHDEFINITION : ""
  AD_STYLE ||--o{ AD_STATUSLINE : ""
  AD_STYLE ||--o{ AD_STYLELINE : ""
  AD_STYLE ||--o{ AD_USERDEF_FIELD : ""
  AD_STYLE ||--o{ AD_USERDEF_INFO_COLUMN : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

16 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-11T13:43 | iD11 | `add_column` | IsWrapWithSpan | IDEMPIERE-5482 |
| 2023-04-11T13:43 | iD11 | `add_column` | IsWrapWithSpan | IDEMPIERE-5482 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | ENTITYTYPE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_STYLE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2019-12-27T17:15 | i7.1 | `modify_column` | EntityType | IDEMPIERE-3952 |
| 2019-12-27T17:15 | i7.1 | `modify_column` | EntityType | IDEMPIERE-3952 |
| 2019-04-21T12:40 | i6.2z | `modify_column` | EntityType | IDEMPIERE-3952 |
| 2019-04-21T12:40 | i6.2z | `modify_column` | EntityType | IDEMPIERE-3952 |
| 2019-04-15T11:44 | i6.2z | `add_constraint` |  | IDEMPIERE-3952 |
| 2019-04-15T11:44 | i6.2z | `add_constraint` |  | IDEMPIERE-3952 |
| 2019-04-15T11:44 | i6.2z | `add_column` | EntityType | IDEMPIERE-3952 |
| 2019-04-15T11:44 | i6.2z | `add_column` | EntityType | IDEMPIERE-3952 |
| 2016-05-06T18:00 | i3.1 | `create_table` |  |  |

## Notes

<!-- ekos:manual id="table.ad_style.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
