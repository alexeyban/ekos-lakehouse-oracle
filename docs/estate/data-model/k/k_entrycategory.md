---
title: "K_ENTRYCATEGORY"
order: 5
ekos_generated: true
ekos_estate_version: 1
---

# K_ENTRYCATEGORY

Area [K](../../data-model/k/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `K_CATEGORY_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `K_ENTRY_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `K_CATEGORYVALUE_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `K_ENTRYCATEGORY_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020261` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [K_CATEGORY](../../data-model/k/k_category.md) | K_ENTRYCATEGORY.K_CATEGORY_ID → K_CATEGORY.K_CATEGORY_ID | NO ACTION |
| [K_CATEGORYVALUE](../../data-model/k/k_categoryvalue.md) | K_ENTRYCATEGORY.K_CATEGORYVALUE_ID → K_CATEGORYVALUE.K_CATEGORYVALUE_ID | NO ACTION |
| [K_ENTRY](../../data-model/k/k_entry.md) | K_ENTRYCATEGORY.K_ENTRY_ID → K_ENTRY.K_ENTRY_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  K_CATEGORY ||--o{ K_ENTRYCATEGORY : ""
  K_CATEGORYVALUE ||--o{ K_ENTRYCATEGORY : ""
  K_ENTRY ||--o{ K_ENTRYCATEGORY : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

11 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | K_ENTRYCATEGORY_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.k_entrycategory.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
