---
title: "delete_ad_archive_binary()"
order: 46
ekos_generated: true
ekos_estate_version: 1
---

# delete_ad_archive_binary()

- defined in: `migration/iD12/postgresql/202506020100_IDEMPIERE-6564.sql`
- language: plpgsql · fidelity: statements · statements recovered: 3 · unrecovered: 0
- returns: `TRIGGER`
- also defined in `db/postgresql/functions/delete_ad_archive_binary.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 9 | `if` | `OLD.binarydata IS NOT NULL AND OLD.binarydata <> 0` |  |  |
| 10 | · `perform` |  |  |  |
| 12 | `return` |  |  |  |

