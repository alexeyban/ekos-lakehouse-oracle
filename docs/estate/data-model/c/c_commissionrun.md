---
title: "C_COMMISSIONRUN"
order: 58
ekos_generated: true
ekos_estate_version: 1
---

# C_COMMISSIONRUN

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_CommissionRun`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_COMMISSIONRUN_ID` | NUMBER(10,0) | PK | yes | Commission Run |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `C_COMMISSION_ID` | NUMBER(10,0) |  | yes | Commission | [C_COMMISSION](../../data-model/c/c_commission.md) | 0 | 0 |
| `STARTDATE` | DATE |  | yes | Start Date |  | 0 | 0 |
| `GRANDTOTAL` | NUMBER |  | yes | Grand Total |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `C_COMMISSIONRUN_UU` | VARCHAR2(36 CHAR) |  |  | C_CommissionRun_UU |  | 0 | 0 |
| `C_INVOICE_ID` | NUMBER(10,0) |  |  | Invoice | [C_INVOICE](../../data-model/c/c_invoice.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022743` | `Processed in ('Y','N')` |
| `SYS_C0022744` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_COMMISSION](../../data-model/c/c_commission.md) | C_COMMISSIONRUN.C_COMMISSION_ID → C_COMMISSION.C_COMMISSION_ID | NO ACTION |
| [C_INVOICE](../../data-model/c/c_invoice.md) | C_COMMISSIONRUN.C_INVOICE_ID → C_INVOICE.C_INVOICE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_COMMISSIONAMT](../../data-model/c/c_commissionamt.md) | C_COMMISSIONAMT.C_COMMISSIONRUN_ID → C_COMMISSIONRUN.C_COMMISSIONRUN_ID | CASCADE |

```mermaid
erDiagram
  C_COMMISSION ||--o{ C_COMMISSIONRUN : ""
  C_COMMISSIONRUN ||--o{ C_COMMISSIONAMT : ""
  C_INVOICE ||--o{ C_COMMISSIONRUN : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| View | `RV_COMMISSIONRUNDETAIL` |
| View | `rv_commissionrundetail` |

## Schema history

19 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-03-17T17:04 | i9 | `add_column` | C_Invoice_ID | IDEMPIERE-5233 |
| 2022-03-17T17:04 | i9 | `add_constraint` |  | IDEMPIERE-5233 |
| 2022-03-17T17:04 | i9 | `add_constraint` |  | IDEMPIERE-5233 |
| 2022-03-17T17:04 | i9 | `add_column` | C_Invoice_ID | IDEMPIERE-5233 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DOCUMENTNO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_commissionrun.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
