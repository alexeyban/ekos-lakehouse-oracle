---
title: "register_migration_script()"
order: 85
ekos_generated: true
ekos_estate_version: 1
---

# register_migration_script()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/REGISTER_MIGRATION_SCRIPT`
- language: plsql · fidelity: statements · statements recovered: 10 · unrecovered: 0
- arguments: `p_script IN VARCHAR2`
- returns: `VARCHAR2`
- also defined in `migration-historic/360lts-i1.0a/postgresql/901_IDEMPIERE-420.sql` (plpgsql)
- also defined in `db/postgresql/functions/register_migration_script.sql` (plpgsql)
- also defined in `db/oracle/functions/register_migration_script.sql` (plsql)
- also defined in `migration-historic/360lts-i1.0a/oracle/901_IDEMPIERE-420.sql` (plsql)

**Reads:** [AD_MIGRATIONSCRIPT](../data-model/ad/ad_migrationscript.md), [AD_SYSTEM](../data-model/ad/ad_system.md)

**Writes:** [AD_MIGRATIONSCRIPT](../data-model/ad/ad_migrationscript.md), [AD_SYSTEM](../data-model/ad/ad_system.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 11 | `assign` |  |  |  |
| 12 | `sql` |  |  | ad_system |
| 16 | `sql` |  | ad_migrationscript |  |
| 20 | `if` | `(v_scriptid IS NULL)` |  |  |
| 22 | · `sql` |  | ad_system | ad_migrationscript |
| 37 | · `assign` |  |  |  |
| 38 | · `perform` |  |  |  |
| 39 | · `sql` |  |  | ad_migrationscript |
| 43 | `sql` |  |  |  |
| 44 | `return` |  |  |  |

