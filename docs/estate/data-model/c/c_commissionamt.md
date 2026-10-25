---
title: "C_COMMISSIONAMT"
order: 55
ekos_generated: true
ekos_estate_version: 1
---

# C_COMMISSIONAMT

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_CommissionAmt`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_COMMISSIONAMT_ID` | NUMBER(10,0) | PK | yes | Commission Amount |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `C_COMMISSIONRUN_ID` | NUMBER(10,0) |  | yes | Commission Run | [C_COMMISSIONRUN](../../data-model/c/c_commissionrun.md) | 0 | 0 |
| `C_COMMISSIONLINE_ID` | NUMBER(10,0) |  | yes | Commission Line | [C_COMMISSIONLINE](../../data-model/c/c_commissionline.md) | 0 | 0 |
| `CONVERTEDAMT` | NUMBER |  | yes | Converted Amount |  | 0 | 0 |
| `ACTUALQTY` | NUMBER |  | yes | Actual Quantity |  | 0 | 0 |
| `COMMISSIONAMT` | NUMBER |  | yes | Commission Amount |  | 0 | 0 |
| `C_COMMISSIONAMT_UU` | VARCHAR2(36 CHAR) |  |  | C_CommissionAmt_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021930` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_COMMISSIONLINE](../../data-model/c/c_commissionline.md) | C_COMMISSIONAMT.C_COMMISSIONLINE_ID → C_COMMISSIONLINE.C_COMMISSIONLINE_ID | NO ACTION |
| [C_COMMISSIONRUN](../../data-model/c/c_commissionrun.md) | C_COMMISSIONAMT.C_COMMISSIONRUN_ID → C_COMMISSIONRUN.C_COMMISSIONRUN_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_COMMISSIONDETAIL](../../data-model/c/c_commissiondetail.md) | C_COMMISSIONDETAIL.C_COMMISSIONAMT_ID → C_COMMISSIONAMT.C_COMMISSIONAMT_ID | CASCADE |

```mermaid
erDiagram
  C_COMMISSIONAMT ||--o{ C_COMMISSIONDETAIL : ""
  C_COMMISSIONLINE ||--o{ C_COMMISSIONAMT : ""
  C_COMMISSIONRUN ||--o{ C_COMMISSIONAMT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Read by

| kind | name |
|---|---|
| View | `RV_COMMISSIONRUNDETAIL` |
| View | `rv_commissionrundetail` |

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
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_COMMISSIONAMT_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_commissionamt.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
