---
title: "documentNo()"
order: 49
ekos_generated: true
ekos_estate_version: 1
---

# documentNo()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/DOCUMENTNO`
- language: plsql · fidelity: statements · statements recovered: 12 · unrecovered: 0
- arguments: `p_PP_MRP_ID IN PP_MRP.PP_MRP_ID%TYPE`
- returns: `PP_MRP.Value%TYPE`
- also defined in `migration-historic/330-331b/postgresql/013_DocumentNo.sql` (java)
- also defined in `db/postgresql/functions/documentNo.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/oracle/262_BF2041299.sql` (plsql)
- also defined in `migration-historic/351a-352a/oracle/230_BF2021146_VMRPDetail_and_Report.sql` (plsql)
- also defined in `migration-historic/351a-352a/postgresql/230_BF2021146_VMRPDetail_and_Report.sql` (plpgsql)
- also defined in `db/oracle/functions/documentNo.sql` (plsql)

**Reads:** [C_ORDER](../data-model/c/c_order.md), [DD_ORDER](../data-model/dd/dd_order.md), [M_FORECAST](../data-model/m/m_forecast.md), [M_REQUISITION](../data-model/m/m_requisition.md), [PP_MRP](../data-model/pp/pp_mrp.md), [PP_ORDER](../data-model/pp/pp_order.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 20 | `if` | `p_PP_MRP_ID <= 0` |  |  |
| 21 | · `return` |  |  |  |
| 24 | `loop` |  |  |  |
| 25 | · `case` | `cur.ordertype = 'FTC' / cur.ordertype = 'POO' / cur.ordertype = 'DOO' / cur.ordertype = 'SOO' / cur.ordertype = 'MOP' / cur.ordertype = 'POR'` |  |  |
| 27 | · · `sql` |  | m_forecast |  |
| 29 | · · `sql` |  | c_order |  |
| 31 | · · `sql` |  | dd_order |  |
| 33 | · · `sql` |  | c_order |  |
| 35 | · · `sql` |  | pp_order |  |
| 37 | · · `sql` |  | m_requisition |  |
| 39 | · · `assign` |  |  |  |
| 43 | `return` |  |  |  |

