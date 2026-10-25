---
title: "update_sequences()"
order: 92
ekos_generated: true
ekos_estate_version: 1
---

# update_sequences()

- defined in: `migration/processes_post_migration/postgresql/03_update_sequences.sql`
- language: plpgsql · fidelity: statements · statements recovered: 31 · unrecovered: 0
- returns: `void`

**Reads:** [AD_COLUMN](../data-model/ad/ad_column.md), [AD_TABLE](../data-model/ad/ad_table.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 18 | `loop` |  | ad_column, ad_table |  |
| 28 | · `assign` |  |  |  |
| 37 | · `assign` |  |  |  |
| 38 | · `block` |  |  |  |
| 39 | · · `dynamic_execute` |  |  |  |
| 43 | · · `assign` |  |  |  |
| 46 | · `if` | `ok` |  |  |
| 47 | · · `assign` |  |  |  |
| 48 | · · `if` | `currentnextsys IS NULL` |  |  |
| 50 | · · · `assign` |  |  |  |
| 53 | · · `sql` |  |  |  |
| 58 | · · `assign` |  |  |  |
| 67 | · · `dynamic_execute` |  |  |  |
| 69 | · · `if` | `currentnext IS NULL` |  |  |
| 71 | · · · `assign` |  |  |  |
| 74 | · · `sql` |  |  |  |
| 79 | · · `if` | `isnativeseqon ='Y'` |  |  |
| 80 | · · · `assign` |  |  |  |
| 87 | · · · `block` |  |  |  |
| 88 | · · · · `dynamic_execute` |  |  |  |
| 91 | · · · · `assign` |  |  |  |
| 92 | · · · · `dynamic_execute` |  |  |  |
| 93 | · · · · `dynamic_execute` |  |  |  |
| 96 | · · · `assign` |  |  |  |
| 101 | · · · `dynamic_execute` |  |  |  |
| 104 | · · `if` | `currentnextsys <> currentseqsys OR (currentnext <> currentseq AND isnativeseqon ='N')` |  |  |
| 106 | · · · `assign` |  |  |  |
| 114 | · · · `dynamic_execute` |  |  |  |
| 116 | · · `if` | `currentseq < currentnext AND isnativeseqon ='Y'` |  |  |
| 117 | · · · `assign` |  |  |  |
| 123 | · · · `dynamic_execute` |  |  |  |

