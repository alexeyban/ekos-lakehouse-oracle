---
title: "productAttribute()"
order: 84
ekos_generated: true
ekos_estate_version: 1
---

# productAttribute()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PRODUCTATTRIBUTE`
- language: plsql · fidelity: statements · statements recovered: 13 · unrecovered: 0
- arguments: `p_M_AttributeSetInstance_ID IN NUMBER`
- returns: `VARCHAR2`
- also defined in `migration-historic/352a-353a/postgresql/316_replace_pljava_for352.sql` (plpgsql)
- also defined in `migration/i8.1z/oracle/202011120940_IDEMPIERE-3862.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration/iD13/postgresql/202602260218_IDEMPIERE-6877.sql` (plpgsql)
- also defined in `migration/iD13/oracle/202602260218_IDEMPIERE-6877.sql` (plsql)
- also defined in `migration-historic/i2.1/oracle/201503041855_IDEMPIERE-2501.sql` (plsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/ProductAttribute.sql` (plpgsql)
- also defined in `migration-historic/i2.1/postgresql/201503041855_IDEMPIERE-2501.sql` (plpgsql)
- also defined in `db/oracle/functions/ProductAttribute.sql` (plsql)

**Reads:** [M_ATTRIBUTESET](../data-model/m/m_attributeset.md), [M_ATTRIBUTESETINSTANCE](../data-model/m/m_attributesetinstance.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 53 | `if` | `(p_M_AttributeSetInstance_ID > 0)` |  |  |
| 54 | · `sql` |  | m_attributeset, m_attributesetinstance |  |
| 63 | · `if` | `(v_SerNo IS NOT NULL)` |  |  |
| 64 | · · `assign` |  |  |  |
| 66 | · `if` | `(v_Lot IS NOT NULL)` |  |  |
| 67 | · · `assign` |  |  |  |
| 69 | · `if` | `(v_GuaranteeDate IS NOT NULL)` |  |  |
| 70 | · · `assign` |  |  |  |
| 73 | · `loop` |  |  |  |
| 74 | · · `assign` |  |  |  |
| 77 | · `if` | `(LENGTH(v_NameAdd) > 0)` |  |  |
| 78 | · · `assign` |  |  |  |
| 82 | `return` |  |  |  |

