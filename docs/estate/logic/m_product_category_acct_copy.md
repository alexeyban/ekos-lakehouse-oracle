---
title: "M_Product_Category_Acct_Copy()"
order: 70
ekos_generated: true
ekos_estate_version: 1
---

# M_Product_Category_Acct_Copy()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/M_PRODUCT_CATEGORY_ACCT_COPY`
- language: plsql · fidelity: statements · statements recovered: 34 · unrecovered: 0
- arguments: `PInstance_ID IN NUMBER, Product_Category_ID IN NUMBER DEFAULT NULL`

**Reads:** [M_PRODUCT](../data-model/m/m_product.md), [M_PRODUCT_ACCT](../data-model/m/m_product_acct.md)

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), [M_PRODUCT_ACCT](../data-model/m/m_product_acct.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 43 | `block` |  |  |  |
| 45 | · `perform` |  |  |  |
| 46 | · `assign` |  |  |  |
| 47 | · `sql` |  |  | ad_pinstance |
| 51 | · `sql` |  |  |  |
| 54 | · `assign` |  |  |  |
| 55 | · `loop` |  |  |  |
| 56 | · · `assign` |  |  |  |
| 57 | · · `if` | `(p.ParameterName = 'M_Product_Category_ID')` |  |  |
| 58 | · · · `assign` |  |  |  |
| 59 | · · · `perform` |  |  |  |
| 61 | · · · `perform` |  |  |  |
| 64 | · `perform` |  |  |  |
| 67 | · `if` | `(Product_Category_ID IS NOT NULL)` |  |  |
| 68 | · · `assign` |  |  |  |
| 69 | · · `perform` |  |  |  |
| 75 | · `loop` |  |  |  |
| 77 | · · `sql` |  | m_product | m_product_acct |
| 92 | · · `assign` |  |  |  |
| 94 | · · `sql` |  | m_product, m_product_acct | m_product_acct |
| 110 | · · `assign` |  |  |  |
| 111 | · · `perform` |  |  |  |
| 112 | · · `assign` |  |  |  |
| 113 | · · `assign` |  |  |  |
| 115 | · `assign` |  |  |  |
| 120 | · `perform` |  |  |  |
| 121 | · `sql` |  |  | ad_pinstance |
| 127 | · `sql` |  |  |  |
| 128 | · `return` |  |  |  |
| 132 | · `assign` |  |  |  |
| 133 | · `perform` |  |  |  |
| 134 | · `sql` |  |  | ad_pinstance |
| 140 | · `sql` |  |  |  |
| 141 | · `return` |  |  |  |

