---
title: "C_COUNTRY_TRL"
order: 67
ekos_generated: true
ekos_estate_version: 1
---

# C_COUNTRY_TRL

Area [C](../../data-model/c/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 251 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_COUNTRY_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 251 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 12 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 2 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 5 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 2 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 251 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 7 | 244 |
| `REGIONNAME` | VARCHAR2(60 CHAR) |  |  |  |  | 232 | 6 |
| `C_COUNTRY_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 4 | 247 |
| `PLACEHOLDERADDRESS1` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERADDRESS2` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERADDRESS3` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERADDRESS4` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERADDRESS5` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERCITY` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERCOMMENTS` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERPOSTAL` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |
| `PLACEHOLDERPOSTAL_ADD` | VARCHAR2(255 CHAR) |  |  |  |  | 251 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0023029` | `IsTranslated in ('Y','N')` |
| `SYS_C0023030` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | C_COUNTRY_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | CASCADE |
| [C_COUNTRY](../../data-model/c/c_country.md) | C_COUNTRY_TRL.C_COUNTRY_ID → C_COUNTRY.C_COUNTRY_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_LANGUAGE ||--o{ C_COUNTRY_TRL : ""
  C_COUNTRY ||--o{ C_COUNTRY_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 3 citation(s)

## Schema history

66 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_COUNTRY_TRL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_13_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PLACEHOLDERADDRESS4 | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_8_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_10_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.c_country_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
