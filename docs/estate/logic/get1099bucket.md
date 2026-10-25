---
title: "get1099bucket()"
order: 55
ekos_generated: true
ekos_estate_version: 1
---

# get1099bucket()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/GET1099BUCKET`
- language: plsql · fidelity: statements · statements recovered: 2 · unrecovered: 0
- arguments: `p_cbpartner_id IN NUMBER, p_cut_date IN DATE, p_bucket IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/i1.0a-i1.0b/postgresql/201303181330_IDEMPIERE-764.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/oracle/functions/get1099bucket.sql` (plsql)
- also defined in `migration-historic/i1.0a-i1.0b/oracle/201303181330_IDEMPIERE-764.sql` (plsql)
- also defined in `db/postgresql/functions/get1099bucket.sql` (plpgsql)

**Reads:** [C_1099BOX](../data-model/c/c_1099box.md), [C_DOCTYPE](../data-model/c/c_doctype.md), [C_INVOICE](../data-model/c/c_invoice.md), [C_INVOICELINE](../data-model/c/c_invoiceline.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 20 | `sql` |  | c_1099box, c_doctype, c_invoice, c_invoiceline |  |
| 39 | `return` |  |  |  |

