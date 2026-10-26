---
mart: category_region_sales
grain:
- month
- product_category
- region
dimensions:
  month: month of c_order.dateordered via c_orderline.c_order_id
  product_category: m_product_category.name via c_orderline.m_product_id, m_product.m_product_category_id
  region: c_region.name via c_orderline.c_bpartner_location_id, c_location.c_region_id
measures:
  sales: sum of c_orderline.linenetamt
filters:
- C_ORDER.docstatus = 'CO'
- c_order.issotrx is true
---

monthly sales by product category and region for completed orders, last two years
