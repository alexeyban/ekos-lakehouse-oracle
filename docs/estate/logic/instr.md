---
title: "instr()"
order: 58
ekos_generated: true
ekos_estate_version: 1
---

# instr()

- defined in: `migration-historic/353a-354a/postgresql/528_1986751_INSTR.sql`
- language: plpgsql · fidelity: statements · statements recovered: 24 · unrecovered: 0
- arguments: `string varchar, string_to_search varchar, beg_index integer, occur_index integer`
- returns: `integer`
- also defined in `migration-historic/353a-354a/postgresql/528_1986751_INSTR.sql` (plpgsql)
- also defined in `db/postgresql/functions/INSTR.sql` (plpgsql)
- also defined in `db/postgresql/functions/INSTR.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/postgresql/528_1986751_INSTR.sql` (plpgsql)
- also defined in `db/postgresql/functions/INSTR.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 74 | `if` | `beg_index > 0` |  |  |
| 75 | · `assign` |  |  |  |
| 76 | · `assign` |  |  |  |
| 78 | · `loop` |  |  |  |
| 79 | · · `assign` |  |  |  |
| 81 | · · `if` | `i = 1` |  |  |
| 82 | · · · `assign` |  |  |  |
| 84 | · · · `assign` |  |  |  |
| 87 | · · `assign` |  |  |  |
| 90 | · `if` | `pos = 0` |  |  |
| 91 | · · `return` |  |  |  |
| 93 | · · `return` |  |  |  |
| 96 | · `assign` |  |  |  |
| 97 | · `assign` |  |  |  |
| 98 | · `assign` |  |  |  |
| 100 | · `loop` |  |  |  |
| 101 | · · `assign` |  |  |  |
| 102 | · · `assign` |  |  |  |
| 104 | · · `if` | `pos > 0` |  |  |
| 105 | · · · `assign` |  |  |  |
| 107 | · · · `if` | `occur_number = occur_index` |  |  |
| 108 | · · · · `return` |  |  |  |
| 112 | · · `assign` |  |  |  |
| 115 | · `return` |  |  |  |

