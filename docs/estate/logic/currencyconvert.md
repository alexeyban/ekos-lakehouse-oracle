---
title: "currencyConvert()"
order: 32
ekos_generated: true
ekos_estate_version: 1
---

# currencyConvert()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/CURRENCYCONVERT`
- language: plsql · fidelity: statements · statements recovered: 8 · unrecovered: 0
- arguments: `p_Amount IN NUMBER, p_CurFrom_ID IN NUMBER, p_CurTo_ID IN NUMBER, p_ConvDate IN DATE, p_ConversionType_ID IN NUMBER, p_Client_ID IN NUMBER, p_Org_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `db/postgresql/functions/C_Currency_Convert.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Currency_Convert.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 34 | `if` | `(p_Amount = 0 OR p_CurFrom_ID = p_CurTo_ID)` |  |  |
| 35 | · `return` |  |  |  |
| 38 | `if` | `(p_Amount IS NULL OR p_CurFrom_ID IS NULL OR p_CurTo_ID IS NULL)` |  |  |
| 39 | · `return` |  |  |  |
| 43 | `assign` |  |  |  |
| 44 | `if` | `(v_Rate IS NULL)` |  |  |
| 45 | · `return` |  |  |  |
| 49 | `return` |  |  |  |

