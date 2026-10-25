---
title: "forbid_multiple_rows_in_dbreplicasyncverifier()"
order: 52
ekos_generated: true
ekos_estate_version: 1
---

# forbid_multiple_rows_in_dbreplicasyncverifier()

- defined in: `migration/iD11/postgresql/202406072107_IDEMPIERE-6166.sql`
- language: plpgsql · fidelity: statements · statements recovered: 3 · unrecovered: 0
- returns: `TRIGGER`
- also defined in `db/postgresql/functions/dbreplicasyncverifier.sql` (plpgsql)

**Reads:** [DBREPLICASYNCVERIFIER](../data-model/other/dbreplicasyncverifier.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 17 | `if` | `(SELECT COUNT(*) FROM dbreplicasyncverifier) > 0` | dbreplicasyncverifier |  |
| 18 | · `raise` |  |  |  |
| 20 | `return` |  |  |  |

