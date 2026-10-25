---
title: "InvoiceopenToDate()"
order: 61
ekos_generated: true
ekos_estate_version: 1
---

# InvoiceopenToDate()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/INVOICEOPENTODATE`
- language: plsql · fidelity: statements · statements recovered: 25 · unrecovered: 0
- arguments: `p_C_Invoice_ID IN NUMBER, p_C_InvoicePaySchedule_ID IN NUMBER, p_DateAcct IN DATE`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/316_replace_pljava_for352.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/postgresql/444_BF2714831_InvoiceopenToDate.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Invoice_OpenToDate.sql` (plpgsql)
- also defined in `migration-historic/340s-351a/oracle/173_InvoiceOpenToDate.sql` (plsql)
- also defined in `db/oracle/functions/C_Invoice_OpenToDate.sql` (plsql)
- also defined in `db/postgresql/functions/C_Invoice_OpenToDate.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md), [C_INVOICEPAYSCHEDULE](../data-model/c/c_invoicepayschedule.md), `C_INVOICE_V`, [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 65 | `block` |  |  |  |
| 66 | · `sql` |  | c_invoice_v |  |
| 73 | · `perform` |  |  |  |
| 74 | · `return` |  |  |  |
| 78 | `sql` |  | c_currency |  |
| 83 | `sql` |  | dual |  |
| 86 | `loop` |  |  |  |
| 87 | · `assign` |  |  |  |
| 88 | · `assign` |  |  |  |
| 92 | · `perform` |  |  |  |
| 96 | `if` | `(p_C_InvoicePaySchedule_ID > 0)` |  |  |
| 97 | · `assign` |  |  |  |
| 98 | · `loop` |  |  |  |
| 99 | · · `if` | `(s.C_InvoicePaySchedule_ID = p_C_InvoicePaySchedule_ID)` |  |  |
| 100 | · · · `assign` |  |  |  |
| 101 | · · · `if` | `(s.DueAmt - v_Remaining < 0)` |  |  |
| 102 | · · · · `assign` |  |  |  |
| 106 | · · · `assign` |  |  |  |
| 107 | · · · `if` | `(v_Remaining < 0)` |  |  |
| 108 | · · · · `assign` |  |  |  |
| 114 | · `assign` |  |  |  |
| 119 | `if` | `(v_TotalOpenAmt > -v_Min AND v_TotalOpenAmt < v_Min)` |  |  |
| 120 | · `assign` |  |  |  |
| 124 | `assign` |  |  |  |
| 126 | `return` |  |  |  |

