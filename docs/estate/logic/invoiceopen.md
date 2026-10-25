---
title: "invoiceOpen()"
order: 60
ekos_generated: true
ekos_estate_version: 1
---

# invoiceOpen()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/INVOICEOPEN`
- language: plsql · fidelity: statements · statements recovered: 25 · unrecovered: 0
- arguments: `p_C_Invoice_ID IN NUMBER, p_C_InvoicePaySchedule_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Invoice_Open.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/postgresql/482_BF2804321_InvoiceOpen.sql` (plpgsql)
- also defined in `migration-historic/315-316/oracle/005_fix_INVOICEOPEN.sql` (plsql)
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)
- also defined in `db/oracle/functions/C_Invoice_Open.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [C_INVOICEPAYSCHEDULE](../data-model/c/c_invoicepayschedule.md), `C_INVOICE_V`, [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 63 | `block` |  |  |  |
| 64 | · `sql` |  | c_invoice_v |  |
| 70 | · `perform` |  |  |  |
| 71 | · `return` |  |  |  |
| 75 | `sql` |  | c_currency |  |
| 80 | `sql` |  | dual |  |
| 83 | `loop` |  |  |  |
| 84 | · `assign` |  |  |  |
| 85 | · `assign` |  |  |  |
| 89 | · `perform` |  |  |  |
| 93 | `if` | `(p_C_InvoicePaySchedule_ID > 0)` |  |  |
| 94 | · `assign` |  |  |  |
| 95 | · `loop` |  |  |  |
| 96 | · · `if` | `(s.C_InvoicePaySchedule_ID = p_C_InvoicePaySchedule_ID)` |  |  |
| 97 | · · · `assign` |  |  |  |
| 98 | · · · `if` | `(s.DueAmt - v_Remaining < 0)` |  |  |
| 99 | · · · · `assign` |  |  |  |
| 103 | · · · `assign` |  |  |  |
| 104 | · · · `if` | `(v_Remaining < 0)` |  |  |
| 105 | · · · · `assign` |  |  |  |
| 111 | · `assign` |  |  |  |
| 116 | `if` | `(v_TotalOpenAmt > -v_Min AND v_TotalOpenAmt < v_Min)` |  |  |
| 117 | · `assign` |  |  |  |
| 121 | `assign` |  |  |  |
| 123 | `return` |  |  |  |

