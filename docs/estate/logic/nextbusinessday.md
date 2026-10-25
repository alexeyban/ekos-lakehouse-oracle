---
title: "nextBusinessDay()"
order: 72
ekos_generated: true
ekos_estate_version: 1
---

# nextBusinessDay()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/NEXTBUSINESSDAY`
- language: plsql · fidelity: statements · statements recovered: 12 · unrecovered: 0
- arguments: `p_Date in date, p_AD_Client_ID in number`
- returns: `date`
- also defined in `migration-historic/i2.0z/oracle/201401150958_IDEMPIERE-1588.sql` (plsql)
- also defined in `migration-historic/352a-353a/postgresql/343_nextBusinessDay.sql` (plpgsql)
- also defined in `db/oracle/functions/nextBusinessDay.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201401150958_IDEMPIERE-1588.sql` (plpgsql)
- also defined in `migration-historic/320-330/oracle/006_BF_1721252_xe.sql` (plsql)
- also defined in `db/postgresql/functions/nextBusinessDay.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)

**Reads:** [AD_CLIENT](../data-model/ad/ad_client.md), [AD_LANGUAGE](../data-model/ad/ad_language.md), [C_COUNTRY](../data-model/c/c_country.md), [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 41 | `assign` |  |  |  |
| 42 | `sql` |  | ad_client, ad_language, c_country |  |
| 48 | `loop` |  |  |  |
| 49 | · `sql` |  | dual |  |
| 50 | · `assign` |  |  |  |
| 51 | · `assign` |  |  |  |
| 52 | · `loop` |  |  |  |
| 53 | · · `exit` |  |  |  |
| 54 | · · `assign` |  |  |  |
| 55 | · · `assign` |  |  |  |
| 57 | · `exit` |  |  |  |
| 60 | `return` |  |  |  |

