---
title: "generate_insert_as()"
order: 53
ekos_generated: true
ekos_estate_version: 1
---

# generate_insert_as()

- defined in: `migration-historic/tools_migrate_with_insert/00_GENERATE_INSERT_AS.sql`
- language: plsql · fidelity: statements · statements recovered: 38 · unrecovered: 0

**Reads:** `ALL_OBJECTS`, `ALL_TAB_COLUMNS`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 17 | `assign` |  |  |  |
| 18 | `perform` |  |  |  |
| 21 | `loop` |  | all_objects |  |
| 31 | · `assign` |  |  |  |
| 32 | · `assign` |  |  |  |
| 33 | · `assign` |  |  |  |
| 34 | · `assign` |  |  |  |
| 35 | · `assign` |  |  |  |
| 36 | · `assign` |  |  |  |
| 39 | · `loop` |  | all_tab_columns |  |
| 47 | · · `if` | `liscolcommon IS NULL` |  |  |
| 49 | · · · `assign` |  |  |  |
| 51 | · · · `assign` |  |  |  |
| 54 | · · `if` | `c.column_name LIKE '% _ID' ESCAPE ' '` |  |  |
| 56 | · · · `if` | `where_ids IS NULL` |  |  |
| 58 | · · · · `assign` |  |  |  |
| 60 | · · · · `assign` |  |  |  |
| 66 | · · `if` | `c.column_name = 'AD_CLIENT_ID'` |  |  |
| 68 | · · · `assign` |  |  |  |
| 73 | · `loop` |  |  |  |
| 81 | · · `if` | `liscoltarget IS NULL` |  |  |
| 83 | · · · `assign` |  |  |  |
| 85 | · · · `assign` |  |  |  |
| 90 | · `loop` |  |  |  |
| 98 | · · `if` | `liscolsource IS NULL` |  |  |
| 100 | · · · `assign` |  |  |  |
| 102 | · · · `assign` |  |  |  |
| 106 | · `perform` |  |  |  |
| 108 | · `if` | `liscoltarget IS NOT NULL` |  |  |
| 110 | · · `perform` |  |  |  |
| 113 | · `if` | `liscolsource IS NOT NULL` |  |  |
| 115 | · · `perform` |  |  |  |
| 118 | · `assign` |  |  |  |
| 129 | · `perform` |  |  |  |
| 130 | · `assign` |  |  |  |
| 155 | · `perform` |  |  |  |
| 158 | `perform` |  |  |  |
| 159 | `perform` |  |  |  |

