---
title: "migr_fix_payment_cashline()"
order: 67
ekos_generated: true
ekos_estate_version: 1
---

# migr_fix_payment_cashline()

- defined in: `migration-historic/340s-351a/postgresql/166_BF_1866214_cont064.sql`
- language: plpgsql · fidelity: statements · statements recovered: 3 · unrecovered: 0
- returns: `void`

**Reads:** [C_CASH](../data-model/c/c_cash.md), [C_CASHLINE](../data-model/c/c_cashline.md), [C_PAYMENT](../data-model/c/c_payment.md)

**Writes:** [C_CASHLINE](../data-model/c/c_cashline.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 11 | `loop` |  | c_cash, c_cashline |  |
| 17 | · `loop` |  | c_payment |  |
| 27 | · · `sql` |  |  | c_cashline |

