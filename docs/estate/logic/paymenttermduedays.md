---
title: "paymentTermDueDays()"
order: 81
ekos_generated: true
ekos_estate_version: 1
---

# paymentTermDueDays()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PAYMENTTERMDUEDAYS`
- language: plsql · fidelity: statements · statements recovered: 32 · unrecovered: 0
- arguments: `PaymentTerm_ID IN NUMBER, DocDate IN DATE, PayDate IN DATE`
- returns: `NUMBER`
- also defined in `migration-historic/312-313/011_PAYMENTTERMDUEDAYS.sql` (plsql)
- also defined in `db/oracle/functions/C_PaymentTerm_DueDays.sql` (plsql)
- also defined in `db/postgresql/functions/C_PaymentTerm_DueDays.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 44 | `if` | `PaymentTerm_ID = 0 OR DocDate IS NULL` |  |  |
| 45 | · `return` |  |  |  |
| 48 | `assign` |  |  |  |
| 49 | `if` | `v_PayDate IS NULL` |  |  |
| 50 | · `assign` |  |  |  |
| 53 | `loop` |  |  |  |
| 56 | · `if` | `(p.IsDueFixed = 'Y')` |  |  |
| 58 | · · `assign` |  |  |  |
| 59 | · · `assign` |  |  |  |
| 60 | · · `assign` |  |  |  |
| 61 | · · `assign` |  |  |  |
| 62 | · · `if` | `(NoDays > p.FixMonthCutoff)` |  |  |
| 63 | · · · `assign` |  |  |  |
| 66 | · · `assign` |  |  |  |
| 67 | · · `assign` |  |  |  |
| 68 | · · `if` | `p.FixMonthCutoff > MaxDayCut` |  |  |
| 69 | · · · `assign` |  |  |  |
| 72 | · · · `assign` |  |  |  |
| 77 | · · `assign` |  |  |  |
| 78 | · · `if` | `DocDate > calDueDate` |  |  |
| 79 | · · · `assign` |  |  |  |
| 81 | · · `assign` |  |  |  |
| 82 | · · `assign` |  |  |  |
| 83 | · · `if` | `(p.FixMonthDay > MaxDay)               <br>      OR (p.FixMonthDay >= 30 AND MaxDay > p.FixMonthDay)` |  |  |
| 85 | · · · `assign` |  |  |  |
| 90 | · · · `assign` |  |  |  |
| 95 | · · `assign` |  |  |  |
| 98 | · · `assign` |  |  |  |
| 103 | `if` | `DueDate IS NULL` |  |  |
| 104 | · `return` |  |  |  |
| 107 | `assign` |  |  |  |
| 108 | `return` |  |  |  |

