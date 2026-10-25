---
title: "currencyRound()"
order: 36
ekos_generated: true
ekos_estate_version: 1
---

# currencyRound()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/CURRENCYROUND`
- language: plsql · fidelity: statements · statements recovered: 8 · unrecovered: 0
- arguments: `p_Amount IN NUMBER, p_CurTo_ID IN NUMBER, p_Costing IN VARCHAR2`
- returns: `NUMBER`
- also defined in `migration-historic/354a-360lts/postgresql/582_BF2528459_CurrencyRound_PostgreSQL.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/316_replace_pljava_for352.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Currency_Round.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/postgresql/398_currencyround.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Currency_Round.SQL` (plsql)

**Reads:** [C_CURRENCY](../data-model/c/c_currency.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 29 | `if` | `(p_Amount IS NULL OR p_CurTo_ID IS NULL)` |  |  |
| 30 | · `return` |  |  |  |
| 34 | `sql` |  | c_currency |  |
| 39 | `if` | `(v_StdPrecision IS NULL)` |  |  |
| 40 | · `return` |  |  |  |
| 43 | `if` | `(p_Costing = 'Y')` |  |  |
| 44 | · `return` |  |  |  |
| 47 | `return` |  |  |  |

