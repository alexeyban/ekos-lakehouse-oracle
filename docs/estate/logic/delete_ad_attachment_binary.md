---
title: "delete_ad_attachment_binary()"
order: 47
ekos_generated: true
ekos_estate_version: 1
---

# delete_ad_attachment_binary()

- defined in: `migration/iD12/postgresql/202506210625_IDEMPIERE-6570.sql`
- language: plpgsql · fidelity: statements · statements recovered: 3 · unrecovered: 0
- returns: `TRIGGER`
- also defined in `db/postgresql/functions/delete_ad_attachment_binary.sql` (plpgsql)
- also defined in `migration/iD13/postgresql/202512252116_IDEMPIERE-6640.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 11 | `if` | `OLD.binarydata IS NOT NULL AND OLD.binarydata <> 0` |  |  |
| 12 | · `perform` |  |  |  |
| 14 | `return` |  |  |  |

