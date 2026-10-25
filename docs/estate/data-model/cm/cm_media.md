---
title: "CM_MEDIA"
order: 27
ekos_generated: true
ekos_estate_version: 1
---

# CM_MEDIA

Area [CM](../../data-model/cm/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 3 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `CM_MEDIA_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 3 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 3 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 3 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `MEDIATYPE` | CHAR(3) |  |  |  |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 3 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 3 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 3 | 0 |
| `ISSUMMARY` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CM_WEBPROJECT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_IMAGE_ID` | NUMBER(10,0) |  |  |  |  | 1 | 2 |
| `CONTENTTEXT` | CLOB |  |  |  |  | 2 | 0 |
| `DIRECTDEPLOY` | CHAR(1) |  |  |  |  | 1 | 1 |
| `CM_MEDIA_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 3 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022989` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_IMAGE](../../data-model/ad/ad_image.md) | CM_MEDIA.AD_IMAGE_ID → AD_IMAGE.AD_IMAGE_ID | NO ACTION |
| [CM_WEBPROJECT](../../data-model/cm/cm_webproject.md) | CM_MEDIA.CM_WEBPROJECT_ID → CM_WEBPROJECT.CM_WEBPROJECT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [CM_ACCESSMEDIA](../../data-model/cm/cm_accessmedia.md) | CM_ACCESSMEDIA.CM_MEDIA_ID → CM_MEDIA.CM_MEDIA_ID | CASCADE |
| [CM_AD](../../data-model/cm/cm_ad.md) | CM_AD.CM_MEDIA_ID → CM_MEDIA.CM_MEDIA_ID | NO ACTION |
| [CM_MEDIADEPLOY](../../data-model/cm/cm_mediadeploy.md) | CM_MEDIADEPLOY.CM_MEDIA_ID → CM_MEDIA.CM_MEDIA_ID | CASCADE |
| `CM_WEBACCESSLOG` | CM_WEBACCESSLOG.CM_MEDIA_ID → CM_MEDIA.CM_MEDIA_ID | NO ACTION |

```mermaid
erDiagram
  AD_IMAGE ||--o{ CM_MEDIA : ""
  CM_MEDIA ||--o{ CM_ACCESSMEDIA : ""
  CM_MEDIA ||--o{ CM_AD : ""
  CM_MEDIA ||--o{ CM_MEDIADEPLOY : ""
  CM_MEDIA ||--o{ CM_WEBACCESSLOG : ""
  CM_WEBPROJECT ||--o{ CM_MEDIA : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.cm_media.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
