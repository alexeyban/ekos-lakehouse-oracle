---
title: "CM_CSTAGE_ELEMENT"
order: 24
ekos_generated: true
ekos_estate_version: 1
---

# CM_CSTAGE_ELEMENT

Area [CM](../../data-model/cm/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 7 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `CM_CSTAGE_ELEMENT_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 7 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 7 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 7 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 2 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  |  |  | 7 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 7 | 0 |
| `CM_CSTAGE_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 4 |
| `CONTENTHTML` | CLOB |  |  |  |  | 0 | 0 |
| `ISVALID` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CM_CSTAGE_ELEMENT_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 7 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022661` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [CM_CSTAGE](../../data-model/cm/cm_cstage.md) | CM_CSTAGE_ELEMENT.CM_CSTAGE_ID → CM_CSTAGE.CM_CSTAGE_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [CM_CSTAGE_ELEMENT_TRL](../../data-model/cm/cm_cstage_element_trl.md) | CM_CSTAGE_ELEMENT_TRL.CM_CSTAGE_ELEMENT_ID → CM_CSTAGE_ELEMENT.CM_CSTAGE_ELEMENT_ID | CASCADE |

```mermaid
erDiagram
  CM_CSTAGE ||--o{ CM_CSTAGE_ELEMENT : ""
  CM_CSTAGE_ELEMENT ||--o{ CM_CSTAGE_ELEMENT_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

19 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `create_index` |  | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CM_CSTAGE_ELEMENT_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.cm_cstage_element.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
