---
title: "M_Product_Delete()"
order: 71
ekos_generated: true
ekos_estate_version: 1
---

# M_Product_Delete()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/M_PRODUCT_DELETE`
- language: plsql · fidelity: statements · statements recovered: 7 · unrecovered: 0
- arguments: `whereClause IN VARCHAR2 DEFAULT NULL`
- also defined in `db/oracle/procedures/M_Product_Delete.sql` (plsql)

**Reads:** [M_PRODUCT](../data-model/m/m_product.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 24 | `if` | `(whereClause IS NULL OR LENGTH(whereClause) = 0)` |  |  |
| 25 | · `loop` |  |  |  |
| 26 | · · `block` |  |  |  |
| 27 | · · · `perform` |  |  |  |
| 28 | · · · `sql` |  |  |  |
| 30 | · · · `perform` |  |  |  |
| 32 | · · · `perform` |  |  |  |

