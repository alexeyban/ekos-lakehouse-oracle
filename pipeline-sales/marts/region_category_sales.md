---
mart: region_category_sales
grain:
- month
- product_category
- region
dimensions:
  month: month of C_ORDER.dateordered
  product_category: M_PRODUCT_CATEGORY.name
  region: c_region.name via c_orderline.c_bpartner_location_id, c_location.c_region_id
measures:
  net_sales: sum of c_orderline.linenetamt
filters:
- c_order.docstatus = 'CO'
- c_order.issotrx is true
---

net sales of completed customer orders by month, product category and the customer's region
