---
title: "InvoicepaidToDate()"
order: 63
ekos_generated: true
ekos_estate_version: 1
---

# InvoicepaidToDate()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/INVOICEPAIDTODATE`
- language: plsql · fidelity: statements · statements recovered: 10 · unrecovered: 0
- arguments: `p_C_Invoice_ID IN NUMBER, p_C_Currency_ID IN NUMBER, p_MultiplierAP IN NUMBER, p_DateAcct IN DATE`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/316_replace_pljava_for352.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Invoice_PaidToDate.sql` (plpgsql)
- also defined in `migration-historic/340s-351a/oracle/174_InvoicepaidToDate.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Invoice_PaidToDate.sql` (plsql)
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)
- also defined in `migration-historic/353a-354a/postgresql/443_BF2714803_InvoicepaidToDate.sql` (plpgsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 51 | `sql` |  | c_currency |  |
| 56 | `sql` |  | dual |  |
| 59 | `if` | `(p_MultiplierAP IS NOT NULL)` |  |  |
| 60 | · `assign` |  |  |  |
| 63 | `loop` |  |  |  |
| 64 | · `assign` |  |  |  |
| 70 | `if` | `(v_PaymentAmt > -v_Min AND v_PaymentAmt < v_Min)` |  |  |
| 71 | · `assign` |  |  |  |
| 75 | `assign` |  |  |  |
| 77 | `return` |  |  |  |

