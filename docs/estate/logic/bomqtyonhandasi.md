---
title: "BomqtyonhandASI()"
order: 22
ekos_generated: true
ekos_estate_version: 1
---

# BomqtyonhandASI()

- defined in: `migration-historic/352a-353a/postgresql/370_ASIFunctions.sql`
- language: plpgsql · fidelity: statements · statements recovered: 28 · unrecovered: 0
- arguments: `Product_ID 		 	numeric, AttributeSetInstance_ID  	numeric, Warehouse_ID			numeric, Locator_ID			numeric	--	Only used, if warehouse is null`
- returns: `numeric`
- also defined in `migration-historic/340s-351a/oracle/176_BomqtyonhandASI.sql` (plsql)

**Reads:** [C_UOM](../data-model/c/c_uom.md), [M_LOCATOR](../data-model/m/m_locator.md), [M_PRODUCT](../data-model/m/m_product.md), `M_STORAGE`, [PP_PRODUCT_BOM](../data-model/pp/pp_product_bom.md), [PP_PRODUCT_BOMLINE](../data-model/pp/pp_product_bomline.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 765 | `assign` |  |  |  |
| 766 | `if` | `(myWarehouse_ID IS NULL)` |  |  |
| 767 | · `if` | `(Locator_ID IS NULL)` |  |  |
| 768 | · · `return` |  |  |  |
| 770 | · · `sql` |  | m_locator |  |
| 775 | `if` | `(myWarehouse_ID IS NULL)` |  |  |
| 776 | · `return` |  |  |  |
| 781 | `block` |  |  |  |
| 782 | · `sql` |  | m_product |  |
| 789 | · `return` |  |  |  |
| 792 | `if` | `(v_IsBOM='N' AND (v_ProductType<>'I' OR v_IsStocked='N')) / (v_IsStocked='Y')` |  |  |
| 793 | · `return` |  |  |  |
| 797 | · `sql` |  | m_locator, m_storage |  |
| 806 | · `return` |  |  |  |
| 811 | `loop` |  | m_product, pp_product_bom, pp_product_bomline |  |
| 820 | · `if` | `(bom.ProductType = 'I' AND bom.IsStocked = 'Y') / (bom.IsBOM = 'Y')` |  |  |
| 822 | · · `sql` |  | m_locator, m_storage |  |
| 830 | · · `sql` |  | c_uom, m_product |  |
| 835 | · · `assign` |  |  |  |
| 837 | · · `if` | `(v_ProductQty < v_Quantity)` |  |  |
| 838 | · · · `assign` |  |  |  |
| 842 | · · `assign` |  |  |  |
| 844 | · · `if` | `(v_ProductQty < v_Quantity)` |  |  |
| 845 | · · · `assign` |  |  |  |
| 850 | `if` | `(v_Quantity > 0)` |  |  |
| 852 | · `sql` |  | c_uom, m_product |  |
| 857 | · `return` |  |  |  |
| 859 | `return` |  |  |  |

