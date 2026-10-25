---
title: "AD_INFOCOLUMN_TRL"
order: 64
ekos_generated: true
ekos_estate_version: 1
---

# AD_INFOCOLUMN_TRL

Area [AD](../../data-model/ad/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 198 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_INFOCOLUMN_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 198 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 178 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 2 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 20 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 2 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 113 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 21 | 99 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 29 | 91 |
| `AD_INFOCOLUMN_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 187 | 11 |
| `PLACEHOLDER` | VARCHAR2(255 CHAR) |  |  |  |  | 198 | 0 |
| `PLACEHOLDER2` | VARCHAR2(255 CHAR) |  |  |  |  | 198 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022761` | `IsTranslated in ('Y','N')` |
| `SYS_C0022762` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_INFOCOLUMN](../../data-model/ad/ad_infocolumn.md) | AD_INFOCOLUMN_TRL.AD_INFOCOLUMN_ID → AD_INFOCOLUMN.AD_INFOCOLUMN_ID | CASCADE |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_INFOCOLUMN_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_INFOCOLUMN ||--o{ AD_INFOCOLUMN_TRL : ""
  AD_LANGUAGE ||--o{ AD_INFOCOLUMN_TRL : ""
```

## Write behaviour

- updates: **raw_sql_sets_updated**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 4 citation(s)

## Schema history

28 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-10-31T15:29 | iD10 | `add_column` | Placeholder2 | IDEMPIERE-5467 |
| 2022-10-31T15:29 | iD10 | `add_column` | Placeholder2 | IDEMPIERE-5467 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_infocolumn_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
