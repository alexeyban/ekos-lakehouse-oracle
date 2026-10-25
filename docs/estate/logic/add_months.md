---
title: "add_months()"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# add_months()

- defined in: `migration-historic/353a-354a/postgresql/441_BF2710889_Add_Months.sql`
- language: plpgsql · fidelity: statements · statements recovered: 4 · unrecovered: 0
- arguments: `in datetime timestamptz, in months numeric`
- returns: `date`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration/i7.1z/postgresql/202008171626_IDEMPIERE-4426.sql` (plpgsql)
- also defined in `db/postgresql/functions/Add_Months.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 5 | `if` | `datetime is null or months is null` |  |  |
| 6 | · `return` |  |  |  |
| 8 | `assign` |  |  |  |
| 9 | `return` |  |  |  |

