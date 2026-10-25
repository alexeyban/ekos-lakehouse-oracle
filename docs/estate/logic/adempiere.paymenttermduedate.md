---
title: "adempiere.paymenttermduedate()"
order: 7
ekos_generated: true
ekos_estate_version: 1
---

# adempiere.paymenttermduedate()

- defined in: `migration-historic/353a-354a/postgresql/442_BF2710889_PaymentTermDueDate.sql`
- language: plpgsql · fidelity: statements · statements recovered: 10 · unrecovered: 0
- arguments: `in paymentterm_id numeric, in docdate timestamptz`
- returns: `timestamptz`

**Reads:** [C_PAYMENTTERM](../data-model/c/c_paymentterm.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 27 | `loop` |  | c_paymentterm |  |
| 33 | · `if` | `(p.IsDueFixed = 'Y')` |  |  |
| 34 | · · `assign` |  |  |  |
| 35 | · · `assign` |  |  |  |
| 36 | · · `assign` |  |  |  |
| 37 | · · `assign` |  |  |  |
| 38 | · · `if` | `(NoDays > p.FixMonthCutoff)` |  |  |
| 39 | · · · `assign` |  |  |  |
| 42 | · · `assign` |  |  |  |
| 45 | `return` |  |  |  |

