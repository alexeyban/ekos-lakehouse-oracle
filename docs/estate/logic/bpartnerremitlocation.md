---
title: "bpartnerRemitLocation()"
order: 28
ekos_generated: true
ekos_estate_version: 1
---

# bpartnerRemitLocation()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/BPARTNERREMITLOCATION`
- language: plsql · fidelity: statements · statements recovered: 4 · unrecovered: 0
- arguments: `p_C_BPartner_ID C_BPartner.C_BPartner_ID%TYPE`
- returns: `NUMBER`
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `migration-historic/i2.0/oracle/201312110939_IDEMPIERE-1625.sql` (plsql)
- also defined in `migration-historic/i2.0/postgresql/201312110939_IDEMPIERE-1625.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_BPartner_RemitLocation.sql` (plpgsql)
- also defined in `db/oracle/functions/C_BPartner_RemitLocation.SQL` (plsql)

**Reads:** [C_BPARTNER_LOCATION](../data-model/c/c_bpartner_location.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 27 | `loop` |  |  |  |
| 28 | · `if` | `(v_C_Location_ID IS NULL)` |  |  |
| 29 | · · `assign` |  |  |  |
| 32 | `return` |  |  |  |

