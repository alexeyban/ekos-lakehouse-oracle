---
title: "TESTUU_TRL"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# TESTUU_TRL

Area [TESTUU](../../data-model/testuu/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 2 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 1 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 1 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 2 |
| `TESTUU_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 2 |
| `TESTUU_UU` | VARCHAR2(36 CHAR) | PK | yes |  |  | 0 | 2 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020497` | `IsTranslated IN ('Y','N')` |
| `SYS_C0020498` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | TESTUU_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | TESTUU_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | TESTUU_TRL.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | TESTUU_TRL.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |
| [TESTUU](../../data-model/other/testuu.md) | TESTUU_TRL.TESTUU_UU → TESTUU.TESTUU_UU | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ TESTUU_TRL : ""
  AD_LANGUAGE ||--o{ TESTUU_TRL : ""
  AD_ORG ||--o{ TESTUU_TRL : ""
  AD_USER ||--o{ TESTUU_TRL : ""
  TESTUU ||--o{ TESTUU_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

16 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `create_table` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `create_table` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-11-26T15:44 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.testuu_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
