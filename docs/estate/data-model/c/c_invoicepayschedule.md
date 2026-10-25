---
title: "C_INVOICEPAYSCHEDULE"
order: 98
ekos_generated: true
ekos_estate_version: 1
---

# C_INVOICEPAYSCHEDULE

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_C_InvoicePaySchedule`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_INVOICEPAYSCHEDULE_ID` | NUMBER(10,0) | PK | yes | Invoice Payment Schedule |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `C_INVOICE_ID` | NUMBER(10,0) |  | yes | Invoice | [C_INVOICE](../../data-model/c/c_invoice.md) | 0 | 1 |
| `C_PAYSCHEDULE_ID` | NUMBER(10,0) |  |  | Payment Schedule | [C_PAYSCHEDULE](../../data-model/c/c_payschedule.md) | 0 | 2 |
| `DUEDATE` | DATE |  | yes | Due Date |  | 0 | 2 |
| `DUEAMT` | NUMBER |  | yes | Amount due |  | 0 | 2 |
| `DISCOUNTDATE` | DATE |  | yes | Discount Date |  | 0 | 1 |
| `DISCOUNTAMT` | NUMBER |  | yes | Discount Amount |  | 0 | 1 |
| `ISVALID` | CHAR(1) |  | yes | Valid |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 2 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `C_INVOICEPAYSCHEDULE_UU` | VARCHAR2(36 CHAR) |  |  | C_InvoicePaySchedule_UU |  | 0 | 2 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022376` | `IsActive in ('Y','N')` |
| `SYS_C0022379` | `IsValid in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_INVOICE](../../data-model/c/c_invoice.md) | C_INVOICEPAYSCHEDULE.C_INVOICE_ID → C_INVOICE.C_INVOICE_ID | CASCADE |
| [C_PAYSCHEDULE](../../data-model/c/c_payschedule.md) | C_INVOICEPAYSCHEDULE.C_PAYSCHEDULE_ID → C_PAYSCHEDULE.C_PAYSCHEDULE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_DUNNINGRUNLINE](../../data-model/c/c_dunningrunline.md) | C_DUNNINGRUNLINE.C_INVOICEPAYSCHEDULE_ID → C_INVOICEPAYSCHEDULE.C_INVOICEPAYSCHEDULE_ID | NO ACTION |

```mermaid
erDiagram
  C_INVOICE ||--o{ C_INVOICEPAYSCHEDULE : ""
  C_INVOICEPAYSCHEDULE ||--o{ C_DUNNINGRUNLINE : ""
  C_PAYSCHEDULE ||--o{ C_INVOICEPAYSCHEDULE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [InvoiceopenToDate](../../logic/invoiceopentodate.md) |
| Procedure | [invoiceDiscount](../../logic/invoicediscount.md) |
| Procedure | [invoiceOpen](../../logic/invoiceopen.md) |
| Procedure | [invoiceopen](../../logic/invoiceopen.md) |
| View | `C_INVOICE_V` |
| View | `RV_BPARTNEROPEN` |
| View | `RV_OPENITEM` |
| View | `RV_OPENITEMTODATE` |
| View | `c_invoice_v` |
| View | `rv_bpartneropen` |
| View | `rv_openitem` |
| View | `rv_openitemtodate` |

## Schema history

9 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_INVOICEPAYSCHEDULE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_invoicepayschedule.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
