---
title: "M_Product_BOM_Check()"
order: 69
ekos_generated: true
ekos_estate_version: 1
---

# M_Product_BOM_Check()

- defined in: `migration-historic/312-313/006_recreate_M_Product_BOM_Check.sql`
- language: plsql · fidelity: partial · statements recovered: 38 · unrecovered: 1
- arguments: `PInstance_ID IN NUMBER`

**Reads:** [M_PRODUCT](../data-model/m/m_product.md), `M_PRODUCT_BOM`, `T_SELECTION`, `T_SELECTION2`

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), [M_PRODUCT](../data-model/m/m_product.md), `T_SELECTION`, `T_SELECTION2`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 35 | `block` |  |  |  |
| 37 | · `perform` |  |  |  |
| 38 | · `assign` |  |  |  |
| 39 | · `sql` |  |  | ad_pinstance |
| 43 | · `sql` |  |  |  |
| 46 | · `assign` |  |  |  |
| 47 | · `loop` |  |  |  |
| 48 | · · `assign` |  |  |  |
| 50 | · `perform` |  |  |  |
| 53 | · `sql` |  | m_product |  |
| 59 | · `if` | `(IsBOM = 'N') / (IsBOM <> 'Y')` |  |  |
| 60 | · · `unrecovered` |  |  |  |
| 63 | · · `return` |  |  |  |
| 67 | · `assign` |  |  |  |
| 69 | · `sql` |  |  | t_selection2 |
| 70 | · `sql` |  |  | t_selection2 |
| 72 | · `sql` |  |  | t_selection |
| 73 | · `sql` |  |  | t_selection |
| 75 | · `loop` |  |  |  |
| 77 | · · `sql` |  | t_selection |  |
| 82 | · · `exit` |  |  |  |
| 85 | · · `sql` |  | m_product, m_product_bom, t_selection | t_selection2 |
| 93 | · · `sql` |  |  | t_selection2 |
| 94 | · · `sql` |  | m_product, m_product_bom, t_selection | t_selection2 |
| 102 | · · `sql` |  |  | t_selection |
| 103 | · · `sql` |  | t_selection2 | t_selection |
| 112 | · `assign` |  |  |  |
| 113 | · `sql` |  |  | m_product |
| 118 | · `perform` |  |  |  |
| 119 | · `sql` |  |  | ad_pinstance |
| 125 | · `sql` |  |  |  |
| 126 | · `return` |  |  |  |
| 130 | · `assign` |  |  |  |
| 131 | · `perform` |  |  |  |
| 132 | · `sql` |  |  | ad_pinstance |
| 138 | · `sql` |  |  |  |
| 140 | · `sql` |  |  | m_product |
| 143 | · `sql` |  |  |  |
| 145 | · `return` |  |  |  |

