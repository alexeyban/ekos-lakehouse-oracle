---
title: "DBA_Cleanup()"
order: 42
ekos_generated: true
ekos_estate_version: 1
---

# DBA_Cleanup()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/DBA_CLEANUP`
- language: plsql · fidelity: statements · statements recovered: 6 · unrecovered: 0
- also defined in `migration-historic/353a-354a/oracle/457_FR2783860.sql` (plsql)
- also defined in `db/oracle/procedures/DBA_Cleanup.sql` (plsql)
- also defined in `migration-historic/353a-354a/oracle/456_FR2783860.sql` (plsql)

**Reads:** [AD_TABLE](../data-model/ad/ad_table.md), `USER_TABLES`, `USER_TAB_COLS`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 19 | `perform` |  |  |  |
| 32 | `loop` |  | ad_table, user_tab_cols, user_tables |  |
| 39 | · `dynamic_execute` |  |  |  |
| 43 | · `if` | `(SQL%ROWCOUNT <> 0)` |  |  |
| 44 | · · `perform` |  |  |  |
| 87 | `sql` |  |  |  |

