---
title: "delete_ad_image_binary()"
order: 48
ekos_generated: true
ekos_estate_version: 1
---

# delete_ad_image_binary()

- defined in: `db/postgresql/functions/delete_ad_image_binary.sql`
- language: plpgsql · fidelity: statements · statements recovered: 3 · unrecovered: 0
- returns: `TRIGGER`
- also defined in `migration/iD12/postgresql/202507100820_IDEMPIERE-6617.sql` (plpgsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 4 | `if` | `OLD.binarydata IS NOT NULL AND OLD.binarydata <> 0` |  |  |
| 5 | · `perform` |  |  |  |
| 7 | `return` |  |  |  |

