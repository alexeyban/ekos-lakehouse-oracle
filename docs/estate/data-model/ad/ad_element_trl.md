---
title: "AD_ELEMENT_TRL"
order: 43
ekos_generated: true
ekos_estate_version: 1
---

# AD_ELEMENT_TRL

Area [AD](../../data-model/ad/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 5923 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_ELEMENT_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 5923 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `CREATED` | DATE |  | yes |  |  | 0 | 3526 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 3 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 367 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 3 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 5746 |
| `PRINTNAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 5730 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 3492 | 2406 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 4211 | 1660 |
| `PO_NAME` | VARCHAR2(60 CHAR) |  |  |  |  | 5915 | 6 |
| `PO_PRINTNAME` | VARCHAR2(60 CHAR) |  |  |  |  | 5915 | 6 |
| `PO_DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 5918 | 5 |
| `PO_HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 5918 | 5 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `AD_ELEMENT_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 5923 |
| `PLACEHOLDER` | VARCHAR2(255 CHAR) |  |  |  |  | 5922 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021549` | `IsActive in ('Y','N')` |
| `SYS_C0021550` | `IsTranslated in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ELEMENT](../../data-model/ad/ad_element.md) | AD_ELEMENT_TRL.AD_ELEMENT_ID → AD_ELEMENT.AD_ELEMENT_ID | CASCADE |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_ELEMENT_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_ELEMENT ||--o{ AD_ELEMENT_TRL : ""
  AD_LANGUAGE ||--o{ AD_ELEMENT_TRL : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 4 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [AD_Synchronize](../../logic/ad_synchronize.md) |

## Written by

| kind | name |
|---|---|
| Procedure | [AD_Synchronize](../../logic/ad_synchronize.md) |

## Schema history

43 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PO_NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PRINTNAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PO_PRINTNAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_10_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_element_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
