---
title: "paymentTermDueDate()"
order: 80
ekos_generated: true
ekos_estate_version: 1
---

# paymentTermDueDate()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PAYMENTTERMDUEDATE`
- language: plsql · fidelity: statements · statements recovered: 10 · unrecovered: 0
- arguments: `PaymentTerm_ID IN NUMBER, DocDate IN DATE`
- returns: `DATE`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_PaymentTerm_DueDate.sql` (plpgsql)
- also defined in `migration-historic/354a-360lts/postgresql/725_BF2819386.sql` (plpgsql)
- also defined in `db/oracle/functions/C_PaymentTerm_DueDate.sql` (plsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 31 | `loop` |  |  |  |
| 34 | · `if` | `(p.IsDueFixed = 'Y')` |  |  |
| 36 | · · `assign` |  |  |  |
| 37 | · · `assign` |  |  |  |
| 38 | · · `assign` |  |  |  |
| 39 | · · `assign` |  |  |  |
| 40 | · · `if` | `(NoDays > p.FixMonthCutoff)` |  |  |
| 41 | · · · `assign` |  |  |  |
| 45 | · · `assign` |  |  |  |
| 50 | `return` |  |  |  |

