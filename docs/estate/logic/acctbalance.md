---
title: "acctBalance()"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# acctBalance()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/ACCTBALANCE`
- language: plsql · fidelity: statements · statements recovered: 12 · unrecovered: 0
- arguments: `p_Account_ID IN NUMBER, p_AmtDr IN NUMBER, p_AmtCr IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/postgresql/functions/Acct_Balance.sql` (plpgsql)
- also defined in `db/oracle/functions/Acct_Balance.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)

**Reads:** [C_ELEMENTVALUE](../data-model/c/c_elementvalue.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 35 | `block` |  |  |  |
| 36 | · `assign` |  |  |  |
| 38 | · `if` | `(p_Account_ID > 0)` |  |  |
| 39 | · · `sql` |  | c_elementvalue |  |
| 45 | · · `if` | `(v_AccountSign='N')` |  |  |
| 46 | · · · `if` | `(v_AccountType IN ('A','E'))` |  |  |
| 47 | · · · · `assign` |  |  |  |
| 49 | · · · · `assign` |  |  |  |
| 54 | · · `if` | `(v_AccountSign = 'C')` |  |  |
| 55 | · · · `assign` |  |  |  |
| 59 | · `return` |  |  |  |
| 62 | · `return` |  |  |  |

