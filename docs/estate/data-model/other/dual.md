---
title: "DUAL"
order: 3
ekos_generated: true
ekos_estate_version: 1
---

# DUAL

Area [OTHER](../../data-model/other/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `dummy` | CHAR |  |  |  |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Read by

| kind | name |
|---|---|
| Procedure | [InvoiceopenToDate](../../logic/invoiceopentodate.md) |
| Procedure | [InvoicepaidToDate](../../logic/invoicepaidtodate.md) |
| Procedure | [invoiceOpen](../../logic/invoiceopen.md) |
| Procedure | [invoicePaid](../../logic/invoicepaid.md) |
| Procedure | [nextBusinessDay](../../logic/nextbusinessday.md) |
| Procedure | [paymentAllocated](../../logic/paymentallocated.md) |
| Procedure | [paymentAvailable](../../logic/paymentavailable.md) |
| Procedure | [paymentTermDiscount](../../logic/paymenttermdiscount.md) |

## Schema history

1 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-06-07T21:07 | iD11 | `drop_table` |  | IDEMPIERE-6166 |

## Notes

<!-- ekos:manual id="table.dual.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
