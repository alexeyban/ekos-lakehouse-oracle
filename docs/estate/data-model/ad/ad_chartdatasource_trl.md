---
title: "AD_CHARTDATASOURCE_TRL"
order: 24
ekos_generated: true
ekos_estate_version: 1
---

# AD_CHARTDATASOURCE_TRL

Area [AD](../../data-model/ad/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 6 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_CHARTDATASOURCE_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 6 |
| `AD_CHARTDATASOURCE_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 6 | 0 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 6 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 5 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020285` | `IsActive IN ('Y','N')` |
| `SYS_C0020287` | `IsTranslated IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CHARTDATASOURCE](../../data-model/ad/ad_chartdatasource.md) | AD_CHARTDATASOURCE_TRL.AD_CHARTDATASOURCE_ID → AD_CHARTDATASOURCE.AD_CHARTDATASOURCE_ID | CASCADE |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_CHARTDATASOURCE_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CHARTDATASOURCE ||--o{ AD_CHARTDATASOURCE_TRL : ""
  AD_LANGUAGE ||--o{ AD_CHARTDATASOURCE_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 2 citation(s)

## Schema history

44 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2022-10-13T13:10 | iD10 | `drop_constraint` |  | IDEMPIERE-5418 |
| 2022-10-13T13:10 | iD10 | `modify_column` | AD_ChartDatasource_ID | IDEMPIERE-5418 |
| 2022-10-13T13:10 | iD10 | `drop_constraint` |  | IDEMPIERE-5418 |
| 2022-10-13T13:10 | iD10 | `add_constraint` |  | IDEMPIERE-5418 |
| 2022-10-13T13:10 | iD10 | `add_constraint` |  | IDEMPIERE-5418 |
| 2022-10-13T13:10 | iD10 | `modify_column` | AD_ChartDatasource_ID | IDEMPIERE-5418 |
| 2022-09-13T12:53 | iD10 | `add_constraint` |  | IDEMPIERE-5418 |
| 2022-09-13T12:53 | iD10 | `add_constraint` |  | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_column` | IsActive | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_column` | AD_ChartDatasource_ID | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_column` | UpdatedBy | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_column` | Updated | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_column` | AD_Language | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_constraint` |  | IDEMPIERE-5418 |
| 2022-09-12T15:58 | iD10 | `add_column` | AD_Org_ID | IDEMPIERE-5418 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_chartdatasource_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
