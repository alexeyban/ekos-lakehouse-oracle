---
title: "invoicePaid()"
order: 62
ekos_generated: true
ekos_estate_version: 1
---

# invoicePaid()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/INVOICEPAID`
- language: plsql · fidelity: statements · statements recovered: 10 · unrecovered: 0
- arguments: `p_C_Invoice_ID IN NUMBER, p_C_Currency_ID IN NUMBER, p_MultiplierAP IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Invoice_Paid.sql` (plsql)
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Invoice_Paid.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 49 | `sql` |  | c_currency |  |
| 54 | `sql` |  | dual |  |
| 57 | `if` | `(p_MultiplierAP IS NOT NULL)` |  |  |
| 58 | · `assign` |  |  |  |
| 61 | `loop` |  |  |  |
| 62 | · `assign` |  |  |  |
| 68 | `if` | `(v_PaymentAmt > -v_Min AND v_PaymentAmt < v_Min)` |  |  |
| 69 | · `assign` |  |  |  |
| 73 | `assign` |  |  |  |
| 75 | `return` |  |  |  |

