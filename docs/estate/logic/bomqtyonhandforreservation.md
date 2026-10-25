---
title: "BOMQTYONHANDFORRESERVATION()"
order: 23
ekos_generated: true
ekos_estate_version: 1
---

# BOMQTYONHANDFORRESERVATION()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/BOMQTYONHANDFORRESERVATION`
- language: plsql · fidelity: statements · statements recovered: 27 · unrecovered: 0
- arguments: `Product_ID IN NUMBER, Warehouse_ID IN NUMBER, Locator_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration/iD13/oracle/202602181112_IDEMPIERE-6849.sql` (plsql)
- also defined in `db/postgresql/functions/BOM_Qty_OnHandForReservation.sql` (plpgsql)
- also defined in `db/oracle/functions/BOM_Qty_OnHandForReservation.sql` (plsql)
- also defined in `migration/iD13/postgresql/202602181112_IDEMPIERE-6849.sql` (plpgsql)
- also defined in `migration-historic/i2.1z/oracle/201506091830_IDEMPIERE-2668.sql` (plsql)
- also defined in `migration/iD11/postgresql/202412091327_IDEMPIERE-6329.sql` (plpgsql)
- also defined in `migration-historic/i2.1z/postgresql/201506091830_IDEMPIERE-2668.sql` (plpgsql)
- also defined in `migration/iD11/oracle/202411301155_IDEMPIERE-6329.sql` (plsql)
- also defined in `migration/iD11/oracle/202412091327_IDEMPIERE-6329.sql` (plsql)
- also defined in `migration/iD11/postgresql/202411301155_IDEMPIERE-6329.sql` (plpgsql)

**Reads:** [C_UOM](../data-model/c/c_uom.md), [M_LOCATOR](../data-model/m/m_locator.md), [M_LOCATORTYPE](../data-model/m/m_locatortype.md), [M_PRODUCT](../data-model/m/m_product.md), [M_STORAGEONHAND](../data-model/m/m_storageonhand.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 35 | `assign` |  |  |  |
| 36 | `if` | `(myWarehouse_ID IS NULL)` |  |  |
| 37 | · `if` | `(Locator_ID IS NULL)` |  |  |
| 38 | · · `return` |  |  |  |
| 40 | · · `sql` |  | m_locator |  |
| 45 | `if` | `(myWarehouse_ID IS NULL)` |  |  |
| 46 | · `return` |  |  |  |
| 51 | `block` |  |  |  |
| 52 | · `sql` |  | m_product |  |
| 59 | · `return` |  |  |  |
| 62 | `if` | `(IsBOM='N' AND (ProductType<>'I' OR IsStocked='N')) / (IsStocked='Y')` |  |  |
| 63 | · `return` |  |  |  |
| 67 | · `sql` |  | m_locator, m_locatortype, m_storageonhand |  |
| 76 | · `return` |  |  |  |
| 81 | `loop` |  |  |  |
| 83 | · `if` | `(bom.ProductType = 'I' AND bom.IsStocked = 'Y') / (bom.IsBOM = 'Y' AND bom.IsVerified = 'Y')` |  |  |
| 85 | · · `sql` |  | m_locator, m_locatortype, m_storageonhand |  |
| 93 | · · `assign` |  |  |  |
| 95 | · · `if` | `(ProductQty < Quantity)` |  |  |
| 96 | · · · `assign` |  |  |  |
| 100 | · · `assign` |  |  |  |
| 102 | · · `if` | `(ProductQty < Quantity)` |  |  |
| 103 | · · · `assign` |  |  |  |
| 108 | `if` | `(Quantity > 0)` |  |  |
| 110 | · `sql` |  | c_uom, m_product |  |
| 115 | · `return` |  |  |  |
| 117 | `return` |  |  |  |

