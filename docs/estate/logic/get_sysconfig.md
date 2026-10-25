---
title: "get_Sysconfig()"
order: 57
ekos_generated: true
ekos_estate_version: 1
---

# get_Sysconfig()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/GET_SYSCONFIG`
- language: plsql · fidelity: statements · statements recovered: 4 · unrecovered: 0
- arguments: `sysconfig_name IN ad_sysconfig.name%TYPE, defaultvalue IN ad_sysconfig.value%TYPE, client_id IN ad_sysconfig.ad_client_id%TYPE, org_id IN ad_sysconfig.ad_org_id%TYPE`
- returns: `ad_sysconfig.value%TYPE`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/354a-360lts/postgresql/718_get_Sysconfig.sql` (plpgsql)
- also defined in `db/postgresql/functions/get_Sysconfig.sql` (plpgsql)
- also defined in `migration-historic/354a-360lts/oracle/718_get_Sysconfig.sql` (plsql)
- also defined in `db/oracle/functions/get_Sysconfig.sql` (plsql)

**Reads:** [AD_SYSCONFIG](../data-model/ad/ad_sysconfig.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 12 | `block` |  |  |  |
| 13 | · `sql` |  | ad_sysconfig |  |
| 21 | · `assign` |  |  |  |
| 23 | `return` |  |  |  |

