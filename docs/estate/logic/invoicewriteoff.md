---
title: "invoiceWriteOff()"
order: 64
ekos_generated: true
ekos_estate_version: 1
---

# invoiceWriteOff()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/INVOICEWRITEOFF`
- language: plsql · fidelity: statements · statements recovered: 7 · unrecovered: 0
- arguments: `p_C_Invoice_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration/i4.1/oracle/201701131446_IDEMPIERE-3279.sql` (plsql)
- also defined in `migration/i4.1/postgresql/201701131446_IDEMPIERE-3279.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Invoice_WriteOff.sql` (plsql)
- also defined in `db/postgresql/functions/C_Invoice_WriteOff.sql` (plpgsql)

**Reads:** [C_INVOICE](../data-model/c/c_invoice.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 12 | `sql` |  | c_invoice |  |
| 13 | `assign` |  |  |  |
| 14 | `if` | `LENGTH(custom_function) > 0` |  |  |
| 16 | · `assign` |  |  |  |
| 17 | · `dynamic_execute` |  |  |  |
| 19 | · `assign` |  |  |  |
| 21 | `return` |  |  |  |

