---
title: "paymentAvailable()"
order: 78
ekos_generated: true
ekos_estate_version: 1
---

# paymentAvailable()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PAYMENTAVAILABLE`
- language: plsql · fidelity: statements · statements recovered: 13 · unrecovered: 0
- arguments: `p_C_Payment_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/352a-353a/oracle/277_BF2081237_C_Payment_Available.sql` (plsql)
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)
- also defined in `db/oracle/functions/C_Payment_Available.sql` (plsql)
- also defined in `db/postgresql/functions/C_Payment_Available.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [C_PAYMENT](../data-model/c/c_payment.md), `C_PAYMENT_V`, [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 35 | `sql` |  | c_payment |  |
| 39 | `if` | `(v_Amt IS NOT NULL)` |  |  |
| 40 | · `return` |  |  |  |
| 44 | `sql` |  | c_payment_v |  |
| 50 | `sql` |  | c_currency |  |
| 55 | `sql` |  | dual |  |
| 58 | `loop` |  |  |  |
| 59 | · `assign` |  |  |  |
| 60 | · `assign` |  |  |  |
| 65 | `if` | `(v_AvailableAmt > -v_Min AND v_AvailableAmt < v_Min)` |  |  |
| 66 | · `assign` |  |  |  |
| 70 | `assign` |  |  |  |
| 72 | `return` |  |  |  |

