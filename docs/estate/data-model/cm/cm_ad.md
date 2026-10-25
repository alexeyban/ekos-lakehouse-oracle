---
title: "CM_AD"
order: 8
ekos_generated: true
ekos_estate_version: 1
---

# CM_AD

Area [CM](../../data-model/cm/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `CM_AD_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 0 |
| `CM_AD_CAT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `CM_MEDIA_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `TARGETURL` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 0 |
| `TARGET_FRAME` | VARCHAR2(20 CHAR) |  | yes |  |  | 0 | 0 |
| `ACTUALCLICK` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `MAXCLICK` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ACTUALIMPRESSION` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `MAXIMPRESSION` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `STARTIMPRESSION` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `STARTDATE` | DATE |  | yes |  |  | 0 | 0 |
| `ENDDATE` | DATE |  |  |  |  | 0 | 0 |
| `CONTENTHTML` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 0 |
| `ISADFLAG` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `ISLOGGED` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `CM_AD_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020395` | `IsLogged in ('Y','N')` |
| `SYS_C0020397` | `IsAdFlag in ('Y','N')` |
| `SYS_C0020399` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [CM_AD_CAT](../../data-model/cm/cm_ad_cat.md) | CM_AD.CM_AD_CAT_ID → CM_AD_CAT.CM_AD_CAT_ID | NO ACTION |
| [CM_MEDIA](../../data-model/cm/cm_media.md) | CM_AD.CM_MEDIA_ID → CM_MEDIA.CM_MEDIA_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  CM_AD_CAT ||--o{ CM_AD : ""
  CM_MEDIA ||--o{ CM_AD : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

31 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CONTENTHTML | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CM_AD_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | TARGET_FRAME | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.cm_ad.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
