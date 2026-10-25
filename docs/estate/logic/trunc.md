---
title: "trunc()"
order: 91
ekos_generated: true
ekos_estate_version: 1
---

# trunc()

- defined in: `migration/i9/postgresql/202211180700_IDEMPIERE-5481.sql`
- language: plpgsql · fidelity: statements · statements recovered: 7 · unrecovered: 0
- arguments: `datetime TIMESTAMP WITHOUT TIME ZONE, format varchar`
- returns: `DATE`
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/330-331b/postgresql/030_BF_1824260.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/postgresql/functions/trunc.sql` (plpgsql)
- also defined in `migration-historic/330-331b/postgresql/030_BF_1824260.sql` (plpgsql)
- also defined in `db/postgresql/functions/trunc.sql` (plpgsql)
- also defined in `migration-historic/330-331b/postgresql/030_BF_1824260.sql` (plpgsql)
- also defined in `db/postgresql/functions/trunc.sql` (plpgsql)
- also defined in `db/postgresql/functions/trunc.sql` (plpgsql)
- also defined in `db/postgresql/functions/trunc.sql` (plpgsql)
- also defined in `migration/i9/postgresql/202211180700_IDEMPIERE-5481.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration/i4.1/postgresql/201708251228_IDEMPIERE-3453.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 6 | `if` | `format = 'Q' / format = 'Y' or format = 'YEAR' / format = 'MM' or format = 'MONTH' / format = 'DD' / format = 'DY'` |  |  |
| 7 | · `return` |  |  |  |
| 9 | · `return` |  |  |  |
| 11 | · `return` |  |  |  |
| 13 | · `return` |  |  |  |
| 15 | · `return` |  |  |  |
| 17 | · `return` |  |  |  |

