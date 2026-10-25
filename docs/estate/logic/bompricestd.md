---
title: "BOMPRICESTD()"
order: 18
ekos_generated: true
ekos_estate_version: 1
---

# BOMPRICESTD()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/BOMPRICESTD`
- language: plsql · fidelity: statements · statements recovered: 6 · unrecovered: 0
- arguments: `Product_ID IN NUMBER, PriceList_Version_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/340s-351a/oracle/180_Bompricestd.sql` (plsql)
- also defined in `migration/iD11/postgresql/202412091327_IDEMPIERE-6329.sql` (plpgsql)
- also defined in `migration/iD12/oracle/202602101428_IDEMPIERE-6845.sql` (plsql)
- also defined in `migration/iD12/postgresql/202602101428_IDEMPIERE-6845.sql` (plpgsql)
- also defined in `migration-historic/i2.0/postgresql/201405160521_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/i2.0/oracle/201405160521_IDEMPIERE-1953.sql` (plsql)
- also defined in `migration-historic/i2.1/oracle/201505201243_IDEMPIERE-2625.sql` (plsql)
- also defined in `db/oracle/functions/BOM_PriceStd.sql` (plsql)
- also defined in `migration-historic/i2.1/postgresql/201505201243_IDEMPIERE-2625.sql` (plpgsql)
- also defined in `migration-historic/i1.0c/postgresql/201309192024_IDEMPIERE-1370.sql` (plpgsql)
- also defined in `migration-historic/i1.0c/oracle/201309192024_IDEMPIERE-1370.sql` (plsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/BOM_PriceStd.sql` (plpgsql)
- also defined in `migration/iD11/postgresql/202411301155_IDEMPIERE-6329.sql` (plpgsql)
- also defined in `migration/iD11/postgresql/202406072206_IDEMPIERE-6167.sql` (plpgsql)
- also defined in `migration/iD11/oracle/202411301155_IDEMPIERE-6329.sql` (plsql)
- also defined in `migration/iD11/oracle/202412091327_IDEMPIERE-6329.sql` (plsql)
- also defined in `migration/iD11/oracle/202406072206_IDEMPIERE-6167.sql` (plsql)

**Reads:** [M_PRODUCTPRICE](../data-model/m/m_productprice.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 35 | `sql` |  | m_productprice |  |
| 42 | `if` | `(v_Price = 0)` |  |  |
| 43 | · `loop` |  |  |  |
| 44 | · · `assign` |  |  |  |
| 45 | · · `assign` |  |  |  |
| 50 | `return` |  |  |  |

