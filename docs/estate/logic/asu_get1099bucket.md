---
title: "asu_get1099bucket()"
order: 15
ekos_generated: true
ekos_estate_version: 1
---

# asu_get1099bucket()

- defined in: `migration-historic/i1.0a-i1.0b/postgresql/201303041619_TICKET-1001763_1099Extract.sql`
- language: plpgsql · fidelity: statements · statements recovered: 2 · unrecovered: 0
- arguments: `p_cbpartner_id   IN   numeric, p_cut_date       IN   timestamp with time zone, p_bucket         IN   numeric`
- returns: `numeric`
- also defined in `migration-historic/i1.0a-i1.0b/oracle/201303041619_TICKET-1001763_1099Extract.sql` (plsql)

**Reads:** [ASU_1099BOX](../data-model/asu/asu_1099box.md), [C_DOCTYPE](../data-model/c/c_doctype.md), [C_INVOICE](../data-model/c/c_invoice.md), [C_INVOICELINE](../data-model/c/c_invoiceline.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 6807 | `sql` |  | asu_1099box, c_doctype, c_invoice, c_invoiceline |  |
| 6824 | `return` |  |  |  |

