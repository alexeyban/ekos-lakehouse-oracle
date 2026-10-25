---
title: "M_PriceList_Create()"
order: 68
ekos_generated: true
ekos_estate_version: 1
---

# M_PriceList_Create()

- defined in: `migration-historic/312-313/005_recreate_M_PriceList_Create.sql`
- language: plsql · fidelity: statements · statements recovered: 81 · unrecovered: 0
- arguments: `PInstance_ID IN NUMBER`
- also defined in `migration-historic/316-320/oracle/012_M_PriceList_Create.sql` (plsql)
- also defined in `migration-historic/313-314/015_Recreate_M_PriceList_Create.sql` (plsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [M_PRICELIST](../data-model/m/m_pricelist.md), [M_PRICELIST_VERSION](../data-model/m/m_pricelist_version.md), [M_PRODUCT](../data-model/m/m_product.md), [M_PRODUCTPRICE](../data-model/m/m_productprice.md), [M_PRODUCT_PO](../data-model/m/m_product_po.md), `T_SELECTION`

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), `AD_PINSTANCE_LOG`, [M_PRODUCTPRICE](../data-model/m/m_productprice.md), [M_PRODUCT_PO](../data-model/m/m_product_po.md), `T_SELECTION`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 54 | `block` |  |  |  |
| 56 | · `perform` |  |  |  |
| 57 | · `assign` |  |  |  |
| 58 | · `sql` |  |  | ad_pinstance |
| 62 | · `sql` |  |  |  |
| 65 | · `assign` |  |  |  |
| 66 | · `loop` |  |  |  |
| 67 | · · `assign` |  |  |  |
| 68 | · · `if` | `(p.ParameterName = 'DeleteOld')` |  |  |
| 69 | · · · `assign` |  |  |  |
| 70 | · · · `perform` |  |  |  |
| 72 | · · · `perform` |  |  |  |
| 75 | · `perform` |  |  |  |
| 79 | · `assign` |  |  |  |
| 80 | · `perform` |  |  |  |
| 81 | · `sql` |  |  | m_product_po |
| 84 | · `sql` |  |  | m_product_po |
| 87 | · `sql` |  |  | m_product_po |
| 90 | · `sql` |  |  | m_product_po |
| 94 | · `sql` |  | m_product_po | m_product_po |
| 101 | · `sql` |  |  |  |
| 106 | · `assign` |  |  |  |
| 107 | · `perform` |  |  |  |
| 108 | · `block` |  |  |  |
| 129 | · · `loop` |  |  |  |
| 130 | · · · `cursor` |  |  |  |
| 131 | · · · `cursor` |  |  |  |
| 132 | · · · `loop` |  |  |  |
| 133 | · · · · `cursor` |  |  |  |
| 134 | · · · · `exit` |  |  |  |
| 136 | · · · · `perform` |  |  |  |
| 137 | · · · · `sql` |  |  | m_product_po |
| 141 | · · · `cursor` |  |  |  |
| 143 | · · `sql` |  |  |  |
| 147 | · `assign` |  |  |  |
| 148 | · `if` | `(p_DeleteOld = 'Y')` |  |  |
| 149 | · · `sql` |  |  |  |
| 151 | · · `assign` |  |  |  |
| 152 | · · `perform` |  |  |  |
| 156 | · `assign` |  |  |  |
| 157 | · `perform` |  |  |  |
| 158 | · `sql` |  | c_currency, m_pricelist, m_pricelist_version |  |
| 172 | · `loop` |  |  |  |
| 173 | · · `assign` |  |  |  |
| 177 | · · `sql` |  |  | t_selection |
| 182 | · · `if` | `(v_PriceList_Version_Base_ID IS NULL)` |  |  |
| 184 | · · · `sql` |  | m_product, m_product_po | t_selection |
| 196 | · · · `sql` |  | m_product, m_product_po, m_productprice | t_selection |
| 208 | · · `assign` |  |  |  |
| 212 | · · `if` | `(v_PriceList_Version_Base_ID IS NULL<br>				OR v_PriceList_Version_Base_ID <> p_PriceList_Version_ID)` |  |  |
| 214 | · · · `assign` |  |  |  |
| 215 | · · · `sql` |  |  |  |
| 219 | · · · `assign` |  |  |  |
| 225 | · · `if` | `(v_PriceList_Version_Base_ID = p_PriceList_Version_ID) / (v_PriceList_Version_Base_ID IS NULL)` |  |  |
| 227 | · · · `sql` |  |  |  |
| 230 | · · · `assign` |  |  |  |
| 231 | · · · `sql` |  | m_product_po, t_selection | m_productprice |
| 253 | · · · `assign` |  |  |  |
| 254 | · · · `sql` |  | m_pricelist, m_pricelist_version, m_productprice, t_selection | m_productprice |
| 278 | · · `assign` |  |  |  |
| 283 | · · `assign` |  |  |  |
| 284 | · · `sql` |  | t_selection | m_productprice |
| 299 | · · `assign` |  |  |  |
| 300 | · · `sql` |  | t_selection | m_productprice |
| 329 | · · `assign` |  |  |  |
| 332 | · · `assign` |  |  |  |
| 333 | · · `sql` |  | t_selection | m_productprice |
| 343 | · · `sql` |  |  | ad_pinstance_log |
| 346 | · · `assign` |  |  |  |
| 347 | · · `assign` |  |  |  |
| 351 | · `sql` |  |  | t_selection |
| 356 | · `perform` |  |  |  |
| 357 | · `perform` |  |  |  |
| 358 | · `sql` |  |  | ad_pinstance |
| 364 | · `sql` |  |  |  |
| 365 | · `return` |  |  |  |
| 369 | · `assign` |  |  |  |
| 370 | · `perform` |  |  |  |
| 371 | · `sql` |  |  | ad_pinstance |
| 377 | · `sql` |  |  |  |
| 378 | · `return` |  |  |  |

