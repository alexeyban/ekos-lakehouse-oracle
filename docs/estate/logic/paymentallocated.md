---
title: "paymentAllocated()"
order: 77
ekos_generated: true
ekos_estate_version: 1
---

# paymentAllocated()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PAYMENTALLOCATED`
- language: plsql · fidelity: statements · statements recovered: 11 · unrecovered: 0
- arguments: `p_C_Payment_ID IN NUMBER, p_C_Currency_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)
- also defined in `db/oracle/functions/C_Payment_Allocated.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Payment_Allocated.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/oracle/282_BF2081237_C_Payment_Allocated.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [C_PAYMENT](../data-model/c/c_payment.md), [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 41 | `sql` |  | c_currency |  |
| 46 | `sql` |  | dual |  |
| 49 | `sql` |  | c_payment |  |
| 53 | `if` | `(v_PayAmt IS NOT NULL)` |  |  |
| 54 | · `return` |  |  |  |
| 58 | `loop` |  |  |  |
| 59 | · `assign` |  |  |  |
| 64 | `if` | `(v_AllocatedAmt > -v_Min AND v_AllocatedAmt < v_Min)` |  |  |
| 65 | · `assign` |  |  |  |
| 69 | `assign` |  |  |  |
| 71 | `return` |  |  |  |

