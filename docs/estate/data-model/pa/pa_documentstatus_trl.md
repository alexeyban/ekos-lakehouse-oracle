---
title: "PA_DOCUMENTSTATUS_TRL"
order: 11
ekos_generated: true
ekos_estate_version: 1
---

# PA_DOCUMENTSTATUS_TRL

Area [PA](../../data-model/pa/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 6 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 2 |
| `PA_DOCUMENTSTATUS_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 6 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 6 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 6 |
| `PA_DOCUMENTSTATUS_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 6 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 6 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 6 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021362` | `IsTranslated IN ('Y','N')` |
| `SYS_C0021363` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | PA_DOCUMENTSTATUS_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [PA_DOCUMENTSTATUS](../../data-model/pa/pa_documentstatus.md) | PA_DOCUMENTSTATUS_TRL.PA_DOCUMENTSTATUS_ID → PA_DOCUMENTSTATUS.PA_DOCUMENTSTATUS_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_LANGUAGE ||--o{ PA_DOCUMENTSTATUS_TRL : ""
  PA_DOCUMENTSTATUS ||--o{ PA_DOCUMENTSTATUS_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

15 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-02-22T15:13 | iD12 | `add_column` | Help | IDEMPIERE-6435 |
| 2025-02-22T15:13 | iD12 | `add_column` | Help | IDEMPIERE-6435 |
| 2023-07-17T22:16 | iD11 | `add_column` | Description | IDEMPIERE-5767 |
| 2023-07-17T22:16 | iD11 | `add_column` | Description | IDEMPIERE-5767 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PA_DOCUMENTSTATUS_TRL_UU | IDEMPIERE-3862 |
| 2017-04-11T22:21 | i4.1 | `add_constraint` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `create_table` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `add_constraint` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `add_constraint` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `create_table` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `add_constraint` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `add_constraint` |  | IDEMPIERE-3338 |
| 2017-04-11T22:21 | i4.1 | `add_constraint` |  | IDEMPIERE-3338 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.pa_documentstatus_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
