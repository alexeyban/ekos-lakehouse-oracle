---
title: "C_BP_GROUP_ACCT"
order: 33
ekos_generated: true
ekos_estate_version: 1
---

# C_BP_GROUP_ACCT

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 6 row(s) when profiled

Application model: `org.compiere.model.X_C_BP_Group_Acct`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_ACCTSCHEMA_ID` | NUMBER(10,0) | PK | yes | Accounting Schema | [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | 0 | 2 |
| `C_BP_GROUP_ID` | NUMBER(10,0) | PK | yes | Business Partner Group | [C_BP_GROUP](../../data-model/c/c_bp_group.md) | 0 | 3 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 2 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 4 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `C_RECEIVABLE_ACCT` | NUMBER(10,0) |  | yes | Customer Receivables |  | 0 | 2 |
| `C_PREPAYMENT_ACCT` | NUMBER(10,0) |  | yes | Customer Prepayment |  | 0 | 2 |
| `V_LIABILITY_ACCT` | NUMBER(10,0) |  | yes | Vendor Liability |  | 0 | 2 |
| `V_LIABILITY_SERVICES_ACCT` | NUMBER(10,0) |  |  | Vendor Service Liability |  | 3 | 1 |
| `V_PREPAYMENT_ACCT` | NUMBER(10,0) |  | yes | Vendor Prepayment |  | 0 | 2 |
| `PAYDISCOUNT_EXP_ACCT` | NUMBER(10,0) |  | yes | Payment Discount Expense |  | 0 | 2 |
| `PAYDISCOUNT_REV_ACCT` | NUMBER(10,0) |  | yes | Payment Discount Revenue |  | 0 | 2 |
| `WRITEOFF_ACCT` | NUMBER(10,0) |  | yes | Write-off |  | 0 | 2 |
| `NOTINVOICEDRECEIPTS_ACCT` | NUMBER(10,0) |  | yes | Not-invoiced Receipts |  | 0 | 2 |
| `UNEARNEDREVENUE_ACCT` | NUMBER(10,0) |  |  | Unearned Revenue |  | 0 | 2 |
| `NOTINVOICEDREVENUE_ACCT` | NUMBER(10,0) |  |  |  |  | 3 | 1 |
| `NOTINVOICEDRECEIVABLES_ACCT` | NUMBER(10,0) |  |  |  |  | 3 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 6 | 0 |
| `C_RECEIVABLE_SERVICES_ACCT` | NUMBER(10,0) |  |  | Receivable Services |  | 3 | 1 |
| `C_BP_GROUP_ACCT_UU` | VARCHAR2(36 CHAR) |  |  | C_BP_Group_Acct_UU |  | 0 | 6 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0023074` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | C_BP_GROUP_ACCT.C_ACCTSCHEMA_ID → C_ACCTSCHEMA.C_ACCTSCHEMA_ID | CASCADE |
| [C_BP_GROUP](../../data-model/c/c_bp_group.md) | C_BP_GROUP_ACCT.C_BP_GROUP_ID → C_BP_GROUP.C_BP_GROUP_ID | CASCADE |
| [C_VALIDCOMBINATION](../../data-model/c/c_validcombination.md) | C_BP_GROUP_ACCT.C_RECEIVABLE_SERVICES_ACCT → C_VALIDCOMBINATION.C_VALIDCOMBINATION_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  C_ACCTSCHEMA ||--o{ C_BP_GROUP_ACCT : ""
  C_BP_GROUP ||--o{ C_BP_GROUP_ACCT : ""
  C_VALIDCOMBINATION ||--o{ C_BP_GROUP_ACCT : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_cascade**
- change log: **not_recorded**
- evidence: 6 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [C_AcctSchema_Default_Copy](../../logic/c_acctschema_default_copy.md) |

## Written by

| kind | name |
|---|---|
| Procedure | [C_AcctSchema_Default_Copy](../../logic/c_acctschema_default_copy.md) |

## Schema history

43 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.C_Receivable_Services_Acct.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.c_bp_group_acct.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
