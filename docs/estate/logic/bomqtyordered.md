---
title: "BOMQTYORDERED()"
order: 24
ekos_generated: true
ekos_estate_version: 1
---

# BOMQTYORDERED()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/BOMQTYORDERED`
- language: plsql · fidelity: statements · statements recovered: 29 · unrecovered: 0
- arguments: `p_Product_ID IN NUMBER, p_Warehouse_ID IN NUMBER, p_Locator_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/340s-351a/oracle/179_Bomqtyordered.sql` (plsql)
- also defined in `migration/iD11/oracle/202411301155_IDEMPIERE-6329.sql` (plsql)
- also defined in `migration-historic/i1.0c/oracle/201309192024_IDEMPIERE-1370.sql` (plsql)
- also defined in `db/oracle/functions/BOM_Qty_Ordered.sql` (plsql)
- also defined in `migration/iD11/postgresql/202412091327_IDEMPIERE-6329.sql` (plpgsql)
- also defined in `migration-historic/i2.0/postgresql/201404290949_Ticket_1003965.sql` (plpgsql)
- also defined in `migration/iD11/postgresql/202411301155_IDEMPIERE-6329.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/370_ASIFunctions.sql` (plpgsql)
- also defined in `migration/iD13/oracle/202602181112_IDEMPIERE-6849.sql` (plsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/BOM_Qty_Ordered.sql` (plpgsql)
- also defined in `migration-historic/i2.0/oracle/201405160521_IDEMPIERE-1953.sql` (plsql)
- also defined in `migration/iD13/postgresql/202602181112_IDEMPIERE-6849.sql` (plpgsql)
- also defined in `migration-historic/i2.0/postgresql/201405160521_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/i1.0c/postgresql/201309192024_IDEMPIERE-1370.sql` (plpgsql)
- also defined in `migration/iD11/oracle/202412091327_IDEMPIERE-6329.sql` (plsql)

**Reads:** [C_UOM](../data-model/c/c_uom.md), [M_LOCATOR](../data-model/m/m_locator.md), [M_PRODUCT](../data-model/m/m_product.md), [M_STORAGERESERVATION](../data-model/m/m_storagereservation.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 35 | `assign` |  |  |  |
| 36 | `if` | `(v_Warehouse_ID IS NULL)` |  |  |
| 37 | · `if` | `(p_Locator_ID IS NULL)` |  |  |
| 38 | · · `return` |  |  |  |
| 40 | · · `sql` |  | m_locator |  |
| 45 | `if` | `(v_Warehouse_ID IS NULL)` |  |  |
| 46 | · `return` |  |  |  |
| 51 | `block` |  |  |  |
| 52 | · `sql` |  | m_product |  |
| 59 | · `return` |  |  |  |
| 63 | `if` | `(v_IsBOM='N' AND (v_ProductType<>'I' OR v_IsStocked='N')) / (v_IsStocked='Y')` |  |  |
| 64 | · `return` |  |  |  |
| 68 | · `sql` |  | m_storagereservation |  |
| 76 | · `return` |  |  |  |
| 81 | `loop` |  |  |  |
| 83 | · `if` | `(bom.ProductType = 'I' AND bom.IsStocked = 'Y') / (bom.IsBOM = 'Y' AND BOM.IsVerified = 'Y')` |  |  |
| 85 | · · `sql` |  | m_storagereservation |  |
| 93 | · · `assign` |  |  |  |
| 95 | · · `if` | `(v_ProductQty < v_Quantity)` |  |  |
| 96 | · · · `assign` |  |  |  |
| 100 | · · `assign` |  |  |  |
| 102 | · · `if` | `(v_ProductQty < v_Quantity)` |  |  |
| 103 | · · · `assign` |  |  |  |
| 109 | `if` | `(v_Quantity = 99999)` |  |  |
| 110 | · `return` |  |  |  |
| 113 | `if` | `(v_Quantity > 0)` |  |  |
| 115 | · `sql` |  | c_uom, m_product |  |
| 120 | · `return` |  |  |  |
| 123 | `return` |  |  |  |

