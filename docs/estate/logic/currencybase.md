---
title: "currencyBase()"
order: 31
ekos_generated: true
ekos_estate_version: 1
---

# currencyBase()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/CURRENCYBASE`
- language: plsql · fidelity: statements · statements recovered: 6 · unrecovered: 0
- arguments: `p_Amount IN NUMBER, p_CurFrom_ID IN NUMBER, p_ConvDate IN DATE, p_Client_ID IN NUMBER, p_Org_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Currency_Base.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Currency_Base.sql` (plsql)

**Reads:** [AD_CLIENTINFO](../data-model/ad/ad_clientinfo.md), [C_ACCTSCHEMA](../data-model/c/c_acctschema.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 31 | `sql` |  | ad_clientinfo, c_acctschema |  |
| 37 | `if` | `(v_CurTo_ID IS NULL)` |  |  |
| 38 | · `return` |  |  |  |
| 41 | `if` | `(p_CurFrom_ID = v_CurTo_ID)` |  |  |
| 42 | · `return` |  |  |  |
| 45 | `return` |  |  |  |

