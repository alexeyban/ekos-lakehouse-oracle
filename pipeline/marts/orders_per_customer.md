---
mart: orders_per_customer
grain:
- month
- customer
dimensions:
  month: month of C_ORDER.CREATED
  customer: c_bpartner.name via c_order.c_bpartner_id
measures:
  count_of_c_order_id: count of c_order
filters:
- C_ORDER.ISACTIVE = true
- c_order.docstatus = 'CO'
---

number of completed sales orders per customer and month
