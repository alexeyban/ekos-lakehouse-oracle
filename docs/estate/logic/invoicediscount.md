---
title: "invoiceDiscount()"
order: 59
ekos_generated: true
ekos_estate_version: 1
---

# invoiceDiscount()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/INVOICEDISCOUNT`
- language: plsql · fidelity: statements · statements recovered: 14 · unrecovered: 0
- arguments: `p_C_Invoice_ID IN NUMBER, p_PayDate IN DATE, p_C_InvoicePaySchedule_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration/iD12/oracle/202506181505_IDEMPIERE-6588.sql` (plsql)
- also defined in `migration-historic/i2.0z/oracle/201408111139_IDEMPIERE-2134.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201408111139_IDEMPIERE-2134.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/oracle/201405301104_IDEMPIERE-1856.sql` (plsql)
- also defined in `migration/iD12/postgresql/202506181505_IDEMPIERE-6588.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Invoice_Discount.sql` (plsql)
- also defined in `db/postgresql/functions/C_Invoice_Discount.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301104_IDEMPIERE-1856.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)

**Reads:** [AD_CLIENTINFO](../data-model/ad/ad_clientinfo.md), [C_INVOICE](../data-model/c/c_invoice.md), [C_INVOICEPAYSCHEDULE](../data-model/c/c_invoicepayschedule.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 33 | `block` |  |  |  |
| 34 | · `sql` |  | ad_clientinfo, c_invoice |  |
| 42 | · `if` | `(v_IsDiscountLineAmt = 'Y')` |  |  |
| 43 | · · `assign` |  |  |  |
| 45 | · · `assign` |  |  |  |
| 49 | · `if` | `(v_Amount = 0)` |  |  |
| 50 | · · `return` |  |  |  |
| 52 | · `if` | `(p_PayDate IS NOT NULL)` |  |  |
| 53 | · · `assign` |  |  |  |
| 57 | · `if` | `(v_IsPayScheduleValid='Y' AND p_C_InvoicePaySchedule_ID > 0)` |  |  |
| 58 | · · `sql` |  | c_invoicepayschedule |  |
| 64 | · · `return` |  |  |  |
| 68 | · `return` |  |  |  |
| 73 | · `return` |  |  |  |

