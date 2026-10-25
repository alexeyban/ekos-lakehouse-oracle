---
title: "C_BANKACCOUNT_ACCT"
order: 18
ekos_generated: true
ekos_estate_version: 1
---

# C_BANKACCOUNT_ACCT

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 6 row(s) when profiled

Application model: `org.compiere.model.X_C_BankAccount_Acct`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_BANKACCOUNT_ID` | NUMBER(10,0) | PK | yes | Bank Account | [C_BANKACCOUNT](../../data-model/c/c_bankaccount.md) | 0 | 3 |
| `C_ACCTSCHEMA_ID` | NUMBER(10,0) | PK | yes | Accounting Schema | [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 2 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 4 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 4 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `B_INTRANSIT_ACCT` | NUMBER(10,0) |  | yes | Bank In Transit |  | 0 | 2 |
| `B_ASSET_ACCT` | NUMBER(10,0) |  | yes | Bank Asset |  | 0 | 2 |
| `B_EXPENSE_ACCT` | NUMBER(10,0) |  |  |  |  | 4 | 1 |
| `B_INTERESTREV_ACCT` | NUMBER(10,0) |  | yes | Bank Interest Revenue |  | 0 | 2 |
| `B_INTERESTEXP_ACCT` | NUMBER(10,0) |  | yes | Bank Interest Expense |  | 0 | 2 |
| `B_UNIDENTIFIED_ACCT` | NUMBER(10,0) |  |  |  |  | 4 | 1 |
| `B_UNALLOCATEDCASH_ACCT` | NUMBER(10,0) |  | yes | Unallocated Cash |  | 0 | 2 |
| `B_PAYMENTSELECT_ACCT` | NUMBER(10,0) |  | yes | Payment Selection |  | 0 | 2 |
| `B_SETTLEMENTGAIN_ACCT` | NUMBER(10,0) |  |  |  |  | 4 | 1 |
| `B_SETTLEMENTLOSS_ACCT` | NUMBER(10,0) |  |  |  |  | 4 | 1 |
| `B_REVALUATIONGAIN_ACCT` | NUMBER(10,0) |  |  |  |  | 4 | 1 |
| `B_REVALUATIONLOSS_ACCT` | NUMBER(10,0) |  |  |  |  | 4 | 1 |
| `C_BANKACCOUNT_ACCT_UU` | VARCHAR2(36 CHAR) |  |  | C_BankAccount_Acct_UU |  | 0 | 6 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020493` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | C_BANKACCOUNT_ACCT.C_ACCTSCHEMA_ID → C_ACCTSCHEMA.C_ACCTSCHEMA_ID | CASCADE |
| [C_BANKACCOUNT](../../data-model/c/c_bankaccount.md) | C_BANKACCOUNT_ACCT.C_BANKACCOUNT_ID → C_BANKACCOUNT.C_BANKACCOUNT_ID | CASCADE |
| [C_VALIDCOMBINATION](../../data-model/c/c_validcombination.md) | C_BANKACCOUNT_ACCT.B_ASSET_ACCT → C_VALIDCOMBINATION.C_VALIDCOMBINATION_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  C_ACCTSCHEMA ||--o{ C_BANKACCOUNT_ACCT : ""
  C_BANKACCOUNT ||--o{ C_BANKACCOUNT_ACCT : ""
  C_VALIDCOMBINATION ||--o{ C_BANKACCOUNT_ACCT : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_cascade**
- change log: **recorded**
- evidence: 7 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [C_AcctSchema_Default_Copy](../../logic/c_acctschema_default_copy.md) |

## Written by

| kind | name |
|---|---|
| Procedure | [C_AcctSchema_Default_Copy](../../logic/c_acctschema_default_copy.md) |

## Schema history

33 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.c_bankaccount_acct.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
