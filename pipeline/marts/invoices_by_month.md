---
mart: invoices_by_month
grain:
- month
dimensions:
  month: month of c_invoice.dateinvoiced
measures:
  invoiced: sum of c_invoice.grandtotal
  invoices: count of c_invoice
filters:
- c_invoice.docstatus = 'CO'
- c_invoice.issotrx is true
---

Completed customer invoices per month.
