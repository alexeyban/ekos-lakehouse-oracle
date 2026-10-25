---
title: "BomqtyreservedASI()"
order: 27
ekos_generated: true
ekos_estate_version: 1
---

# BomqtyreservedASI()

- defined in: `migration-historic/340s-351a/oracle/178_BomqtyreservedASI.sql`
- language: plsql · fidelity: statements · statements recovered: 30 · unrecovered: 0
- arguments: `p_Product_ID IN NUMBER, AttributeSetInstance_ID IN NUMBER, p_Warehouse_ID IN NUMBER, p_Locator_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/352a-353a/postgresql/370_ASIFunctions.sql` (plpgsql)

**Reads:** [C_UOM](../data-model/c/c_uom.md), [M_LOCATOR](../data-model/m/m_locator.md), [M_PRODUCT](../data-model/m/m_product.md), `M_STORAGE`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 39 | `assign` |  |  |  |
| 40 | `if` | `(v_Warehouse_ID IS NULL)` |  |  |
| 41 | · `if` | `(p_Locator_ID IS NULL)` |  |  |
| 42 | · · `return` |  |  |  |
| 44 | · · `sql` |  | m_locator |  |
| 49 | `if` | `(v_Warehouse_ID IS NULL)` |  |  |
| 50 | · `return` |  |  |  |
| 55 | `block` |  |  |  |
| 56 | · `sql` |  | m_product |  |
| 63 | · `return` |  |  |  |
| 67 | `if` | `(v_IsBOM='N' AND (v_ProductType<>'I' OR v_IsStocked='N')) / (v_IsStocked='Y')` |  |  |
| 68 | · `return` |  |  |  |
| 72 | · `sql` |  | m_locator, m_storage |  |
| 80 | · `return` |  |  |  |
| 85 | `loop` |  |  |  |
| 87 | · `if` | `(bom.ProductType = 'I' AND bom.IsStocked = 'Y') / (bom.IsBOM = 'Y')` |  |  |
| 89 | · · `sql` |  | m_locator, m_storage |  |
| 97 | · · `sql` |  | c_uom, m_product |  |
| 102 | · · `assign` |  |  |  |
| 104 | · · `if` | `(v_ProductQty < v_Quantity)` |  |  |
| 105 | · · · `assign` |  |  |  |
| 109 | · · `assign` |  |  |  |
| 111 | · · `if` | `(v_ProductQty < v_Quantity)` |  |  |
| 112 | · · · `assign` |  |  |  |
| 118 | `if` | `(v_Quantity = 99999)` |  |  |
| 119 | · `return` |  |  |  |
| 122 | `if` | `(v_Quantity > 0)` |  |  |
| 124 | · `sql` |  | c_uom, m_product |  |
| 129 | · `return` |  |  |  |
| 131 | `return` |  |  |  |

