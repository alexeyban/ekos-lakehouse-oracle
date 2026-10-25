---
title: "DBA_ConstraintCmd()"
order: 43
ekos_generated: true
ekos_estate_version: 1
---

# DBA_ConstraintCmd()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/DBA_CONSTRAINTCMD`
- language: plsql · fidelity: statements · statements recovered: 9 · unrecovered: 0
- arguments: `p_ConstraintName IN VARCHAR2`
- returns: `VARCHAR2`
- also defined in `db/oracle/functions/DBA_ConstraintCmd.sql` (plsql)

**Reads:** `USER_CONSTRAINTS`, `USER_CONS_COLUMNS`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 28 | `sql` |  | user_cons_columns, user_constraints |  |
| 34 | `assign` |  |  |  |
| 38 | `if` | `(v_ConstraintName IS NULL)` |  |  |
| 39 | · `return` |  |  |  |
| 43 | `sql` |  | user_cons_columns, user_constraints |  |
| 49 | `assign` |  |  |  |
| 51 | `if` | `(v_DeleteRule = 'CASCADE')` |  |  |
| 52 | · `assign` |  |  |  |
| 55 | `return` |  |  |  |

