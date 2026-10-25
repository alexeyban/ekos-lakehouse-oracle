---
title: "prodqtyreserved()"
order: 83
ekos_generated: true
ekos_estate_version: 1
---

# prodqtyreserved()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PRODQTYRESERVED`
- language: plsql · fidelity: statements · statements recovered: 15 · unrecovered: 0
- arguments: `p_product_id NUMBER, p_warehouse_id NUMBER`
- returns: `NUMBER`
- also defined in `db/postgresql/functions/prodqtyreserved.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/oracle/functions/prodqtyreserved.sql` (plsql)
- also defined in `migration-historic/360lts-i1.0a/postgresql/866_IDEMPIERE-246_Manufacturing_Light_fixes.sql` (plpgsql)
- also defined in `migration-historic/360lts-i1.0a/oracle/866_IDEMPIERE-246_Manufacturing_Light_fixes.sql` (plsql)

**Reads:** [C_UOM](../data-model/c/c_uom.md), [M_LOCATOR](../data-model/m/m_locator.md), [M_PRODUCT](../data-model/m/m_product.md), [M_PRODUCTIONLINE](../data-model/m/m_productionline.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 17 | `assign` |  |  |  |
| 18 | `if` | `(v_Warehouse_ID IS NULL)` |  |  |
| 19 | · `return` |  |  |  |
| 23 | `block` |  |  |  |
| 24 | · `sql` |  | m_product |  |
| 35 | · `return` |  |  |  |
| 38 | `if` | `(v_IsStocked='Y')` |  |  |
| 40 | · `sql` |  | m_locator, m_productionline |  |
| 53 | · `return` |  |  |  |
| 56 | `if` | `(v_Quantity = 99999)` |  |  |
| 57 | · `return` |  |  |  |
| 59 | `if` | `(v_Quantity > 0)` |  |  |
| 61 | · `sql` |  | c_uom, m_product |  |
| 68 | · `return` |  |  |  |
| 70 | `return` |  |  |  |

