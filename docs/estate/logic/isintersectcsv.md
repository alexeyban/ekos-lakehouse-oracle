---
title: "isIntersectCSV()"
order: 65
ekos_generated: true
ekos_estate_version: 1
---

# isIntersectCSV()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/ISINTERSECTCSV`
- language: plsql · fidelity: statements · statements recovered: 3 · unrecovered: 0
- arguments: `p_csv1 IN VARCHAR2, p_csv2 IN VARCHAR2`
- returns: `CHAR`
- also defined in `migration/i8.2z/postgresql/202105091048_IDEMPIERE-4771.sql` (plpgsql)
- also defined in `migration/i8.2z/oracle/202105091048_IDEMPIERE-4771.sql` (plsql)
- also defined in `db/postgresql/functions/isIntersectCSV.sql` (plpgsql)
- also defined in `db/oracle/functions/isIntersectCSV.sql` (plsql)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 4 | `if` | `toTableOfVarchar2(p_csv1) MULTISET INTERSECT toTableOfVarchar2(p_csv2) IS NOT EMPTY` |  |  |
| 6 | · `return` |  |  |  |
| 8 | · `return` |  |  |  |

