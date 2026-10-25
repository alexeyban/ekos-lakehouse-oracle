---
title: "C_CYCLEPHASE"
order: 72
ekos_generated: true
ekos_estate_version: 1
---

# C_CYCLEPHASE

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 10 row(s) when profiled

Application model: `org.compiere.model.X_C_CyclePhase`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_CYCLESTEP_ID` | NUMBER(10,0) | PK | yes | Cycle Step | [C_CYCLESTEP](../../data-model/c/c_cyclestep.md) | 0 | 4 |
| `C_PHASE_ID` | NUMBER(10,0) | PK | yes | Standard Phase | [C_PHASE](../../data-model/c/c_phase.md) | 0 | 10 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 10 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 10 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `C_CYCLEPHASE_UU` | VARCHAR2(36 CHAR) |  |  | C_CyclePhase_UU |  | 0 | 10 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_CYCLESTEP](../../data-model/c/c_cyclestep.md) | C_CYCLEPHASE.C_CYCLESTEP_ID → C_CYCLESTEP.C_CYCLESTEP_ID | CASCADE |
| [C_PHASE](../../data-model/c/c_phase.md) | C_CYCLEPHASE.C_PHASE_ID → C_PHASE.C_PHASE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  C_CYCLESTEP ||--o{ C_CYCLEPHASE : ""
  C_PHASE ||--o{ C_CYCLEPHASE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Read by

| kind | name |
|---|---|
| View | `RV_PROJECTCYCLE` |
| View | `rv_projectcycle` |

## Schema history

9 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_CYCLEPHASE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_cyclephase.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
