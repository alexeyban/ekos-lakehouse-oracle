---
title: "AD_PRINTPAPER"
order: 125
ekos_generated: true
ekos_estate_version: 1
---

# AD_PRINTPAPER

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 4 row(s) when profiled

Application model: `org.compiere.model.X_AD_PrintPaper`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PRINTPAPER_ID` | NUMBER(10,0) | PK | yes | Print Paper |  | 0 | 4 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 4 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 3 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 4 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 1 |
| `ISDEFAULT` | CHAR(1) |  | yes | Default |  | 0 | 2 |
| `ISLANDSCAPE` | CHAR(1) |  | yes | Landscape |  | 0 | 2 |
| `CODE` | VARCHAR2(2000 CHAR) |  | yes | Validation code |  | 0 | 2 |
| `MARGINTOP` | NUMBER(10,0) |  | yes | Top Margin |  | 0 | 1 |
| `MARGINLEFT` | NUMBER(10,0) |  | yes | Left Margin |  | 0 | 2 |
| `MARGINRIGHT` | NUMBER(10,0) |  | yes | Right Margin |  | 0 | 1 |
| `MARGINBOTTOM` | NUMBER(10,0) |  | yes | Bottom Margin |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 4 | 0 |
| `SIZEX` | NUMBER |  |  | Size X |  | 4 | 0 |
| `SIZEY` | NUMBER |  |  | Size Y |  | 4 | 0 |
| `DIMENSIONUNITS` | CHAR(1) |  |  | Dimension Units |  | 4 | 0 |
| `AD_PRINTPAPER_UU` | VARCHAR2(36 CHAR) |  |  | AD_PrintPaper_UU |  | 0 | 4 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021680` | `IsActive in ('Y','N')` |
| `SYS_C0021682` | `IsLandscape in ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_LANGUAGE.AD_PRINTPAPER_ID → AD_PRINTPAPER.AD_PRINTPAPER_ID | NO ACTION |
| [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | AD_PRINTFORMAT.AD_PRINTPAPER_ID → AD_PRINTPAPER.AD_PRINTPAPER_ID | NO ACTION |

```mermaid
erDiagram
  AD_PRINTPAPER ||--o{ AD_LANGUAGE : ""
  AD_PRINTPAPER ||--o{ AD_PRINTFORMAT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

19 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PRINTPAPER_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `create_index` |  | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_printpaper.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
