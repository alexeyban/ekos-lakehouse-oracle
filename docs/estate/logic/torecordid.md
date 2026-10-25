---
title: "torecordid()"
order: 89
ekos_generated: true
ekos_estate_version: 1
---

# torecordid()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/TORECORDID`
- language: plsql · fidelity: statements · statements recovered: 10 · unrecovered: 0
- arguments: `p_tablename IN VARCHAR2, p_uu_value IN VARCHAR2`
- returns: `NUMBER`
- also defined in `db/postgresql/functions/torecordid.sql` (plpgsql)
- also defined in `db/oracle/functions/torecordid.sql` (plsql)
- also defined in `migration/iD10/oracle/202302220654_IDEMPIERE-5586.sql` (plsql)
- also defined in `migration/iD13/postgresql/202510101903_IDEMPIERE-6650-generate_uuid.sql` (plpgsql)
- also defined in `migration/iD13/oracle/202512311030_IDEMPIERE-6803.sql` (plsql)
- also defined in `migration/iD10/postgresql/202302220654_IDEMPIERE-5586.sql` (plpgsql)

**Reads:** [AD_COLUMN](../data-model/ad/ad_column.md), [AD_TABLE](../data-model/ad/ad_table.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 10 | `sql` |  | ad_column, ad_table |  |
| 16 | `if` | `(id_column IS NULL)` |  |  |
| 17 | · `raise` |  |  |  |
| 20 | `if` | `(length(p_tablename) <= 27)` |  |  |
| 21 | · `assign` |  |  |  |
| 23 | · `sql` |  | ad_column, ad_table |  |
| 31 | `if` | `(uu_column IS NULL)` |  |  |
| 32 | · `raise` |  |  |  |
| 35 | `dynamic_execute` |  |  |  |
| 39 | `return` |  |  |  |

