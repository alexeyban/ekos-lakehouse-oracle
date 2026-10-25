---
title: "C_INVOICESCHEDULE"
order: 99
ekos_generated: true
ekos_estate_version: 1
---

# C_INVOICESCHEDULE

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_C_InvoiceSchedule`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_INVOICESCHEDULE_ID` | NUMBER(10,0) | PK | yes | Invoice Schedule |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `ISAMOUNT` | CHAR(1) |  | yes | Amount Limit |  | 0 | 1 |
| `AMT` | NUMBER |  |  | Amount |  | 0 | 1 |
| `INVOICEFREQUENCY` | CHAR(1) |  | yes | Invoice Frequency |  | 0 | 1 |
| `INVOICEWEEKDAY` | CHAR(1) |  |  | Invoice Week Day |  | 1 | 0 |
| `INVOICEWEEKDAYCUTOFF` | CHAR(1) |  |  | Invoice weekday cutoff |  | 1 | 0 |
| `EVENINVOICEWEEK` | CHAR(1) |  |  | Invoice on even weeks |  | 0 | 1 |
| `INVOICEDAY` | NUMBER(10,0) |  |  | Invoice Day |  | 0 | 1 |
| `INVOICEDAYCUTOFF` | NUMBER(10,0) |  |  | Invoice day cut-off |  | 0 | 1 |
| `ISDEFAULT` | CHAR(1) |  | yes | Default |  | 0 | 1 |
| `C_INVOICESCHEDULE_UU` | VARCHAR2(36 CHAR) |  |  | C_InvoiceSchedule_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020810` | `EvenInvoiceWeek in ('Y','N')` |
| `SYS_C0020811` | `IsActive in ('Y','N')` |
| `SYS_C0020813` | `IsAmount in ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_BPARTNER.C_INVOICESCHEDULE_ID → C_INVOICESCHEDULE.C_INVOICESCHEDULE_ID | NO ACTION |

```mermaid
erDiagram
  C_INVOICESCHEDULE ||--o{ C_BPARTNER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| View | `C_INVOICE_CANDIDATE_V` |
| View | `c_invoice_candidate_v` |

## Schema history

13 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_INVOICESCHEDULE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.Amt.nullable` | unexplained |
| `mandatory_but_nullable` | `columns.InvoiceDay.nullable` | unexplained |
| `mandatory_but_nullable` | `columns.InvoiceWeekDay.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.c_invoiceschedule.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
