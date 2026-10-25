---
title: "C_ORDER_DRILLDOWN()"
order: 39
ekos_generated: true
ekos_estate_version: 1
---

# C_ORDER_DRILLDOWN()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/C_ORDER_DRILLDOWN`
- language: plsql · fidelity: statements · statements recovered: 38 · unrecovered: 0
- arguments: `PInstance_ID IN NUMBER`
- also defined in `db/oracle/procedures/C_Order_DrillDown.sql` (plsql)
- also defined in `migration-historic/i1.0a-i1.0b/oracle/201211070846_IDEMPIERE-422.sql` (plsql)

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), `T_SPOOL`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 34 | `block` |  |  |  |
| 38 | · `assign` |  |  |  |
| 39 | · `loop` |  |  |  |
| 40 | · · `assign` |  |  |  |
| 41 | · · `if` | `(p.ParameterName = 'C_Order_ID')` |  |  |
| 42 | · · · `assign` |  |  |  |
| 43 | · · · `perform` |  |  |  |
| 45 | · · · `perform` |  |  |  |
| 48 | · `perform` |  |  |  |
| 50 | · `if` | `(C_Order_ID IS NULL)` |  |  |
| 51 | · · `assign` |  |  |  |
| 55 | · `sql` |  |  |  |
| 59 | · `loop` |  |  |  |
| 61 | · · `sql` |  |  | t_spool |
| 66 | · · `block` |  |  |  |
| 73 | · · · `loop` |  |  |  |
| 74 | · · · · `sql` |  |  | t_spool |
| 83 | · · `block` |  |  |  |
| 90 | · · · `loop` |  |  |  |
| 91 | · · · · `sql` |  |  | t_spool |
| 96 | · · · · `block` |  |  |  |
| 103 | · · · · · `loop` |  |  |  |
| 104 | · · · · · · `sql` |  |  | t_spool |
| 112 | · · `block` |  |  |  |
| 122 | · · · `loop` |  |  |  |
| 124 | · · · · `sql` |  |  | t_spool |
| 129 | · · · · `block` |  |  |  |
| 136 | · · · · · `loop` |  |  |  |
| 137 | · · · · · · `sql` |  |  | t_spool |
| 149 | · `perform` |  |  |  |
| 150 | · `sql` |  |  | ad_pinstance |
| 156 | · `sql` |  |  |  |
| 157 | · `return` |  |  |  |
| 161 | · `assign` |  |  |  |
| 162 | · `perform` |  |  |  |
| 163 | · `sql` |  |  | ad_pinstance |
| 169 | · `sql` |  |  |  |
| 170 | · `return` |  |  |  |

