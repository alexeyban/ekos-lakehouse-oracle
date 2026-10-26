---
mart: sales_by_month
grain:
- month
- customer
dimensions:
  month: month of c_order.dateordered
  customer: c_bpartner.name via c_order.c_bpartner_id
measures:
  total: sum of c_order.grandtotal
  orders: count of c_order
filters:
- c_order.issotrx is true
- c_order.docstatus = 'CO'
---

Completed sales orders per month and customer: the order count and their grand total.
