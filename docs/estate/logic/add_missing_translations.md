---
title: "add_missing_translations()"
order: 3
ekos_generated: true
ekos_estate_version: 1
---

# add_missing_translations()

- defined in: `migration/processes_post_migration/postgresql/01_add_missing_translations.sql`
- language: plpgsql · fidelity: statements · statements recovered: 14 · unrecovered: 0
- returns: `void`

**Reads:** [AD_COLUMN](../data-model/ad/ad_column.md), [AD_TABLE](../data-model/ad/ad_table.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 12 | `loop` |  | ad_table |  |
| 19 | · `if` | `EXISTS (<br>          SELECT 1<br>              FROM AD_Column cl<br>              JOIN AD_Table tb ON (cl.AD_Table_ID=tb.AD_Table_ID)<br>              WHERE tb.TableName=t.tablename AND cl.IsKey='Y' AND cl.ColumnName LIKE '%_ID')` | ad_column, ad_table |  |
| 24 | · · `assign` |  |  |  |
| 26 | · · `assign` |  |  |  |
| 28 | · `assign` |  |  |  |
| 37 | · `assign` |  |  |  |
| 42 | · `sql` |  | ad_table |  |
| 47 | · `loop` |  | ad_column, ad_table |  |
| 55 | · · `assign` |  |  |  |
| 56 | · · `assign` |  |  |  |
| 59 | · `assign` |  |  |  |
| 60 | · `assign` |  |  |  |
| 71 | · `assign` |  |  |  |
| 73 | · `dynamic_execute` |  |  |  |

