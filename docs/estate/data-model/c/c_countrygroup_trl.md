---
title: "C_COUNTRYGROUP_TRL"
order: 66
ekos_generated: true
ekos_estate_version: 1
---

# C_COUNTRYGROUP_TRL

Area [C](../../data-model/c/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `C_COUNTRYGROUP_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `C_COUNTRYGROUP_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021484` | `IsActive IN ('Y','N')` |
| `SYS_C0021487` | `IsTranslated IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | C_COUNTRYGROUP_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | C_COUNTRYGROUP_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | C_COUNTRYGROUP_TRL.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | C_COUNTRYGROUP_TRL.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |
| [C_COUNTRYGROUP](../../data-model/c/c_countrygroup.md) | C_COUNTRYGROUP_TRL.C_COUNTRYGROUP_ID → C_COUNTRYGROUP.C_COUNTRYGROUP_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ C_COUNTRYGROUP_TRL : ""
  AD_LANGUAGE ||--o{ C_COUNTRYGROUP_TRL : ""
  AD_ORG ||--o{ C_COUNTRYGROUP_TRL : ""
  AD_USER ||--o{ C_COUNTRYGROUP_TRL : ""
  C_COUNTRYGROUP ||--o{ C_COUNTRYGROUP_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_COUNTRYGROUP_TRL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `create_table` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.c_countrygroup_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
