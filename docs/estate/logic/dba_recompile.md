---
title: "DBA_Recompile()"
order: 45
ekos_generated: true
ekos_estate_version: 1
---

# DBA_Recompile()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/DBA_RECOMPILE`
- language: plsql · fidelity: statements · statements recovered: 55 · unrecovered: 0
- arguments: `p_PInstance_ID IN NUMBER`
- also defined in `migration-historic/353a-354a/oracle/460_BF2783862.sql` (plsql)
- also defined in `db/oracle/procedures/DBA_Recompile.sql` (plsql)

**Reads:** `USER_OBJECTS`

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 55 | `block` |  |  |  |
| 56 | · `loop` |  |  |  |
| 57 | · · `assign` |  |  |  |
| 58 | · · `loop` |  |  |  |
| 60 | · · · `if` | `NOT invalid_tab_rec.EXISTS(ci.object_id)` |  |  |
| 61 | · · · · `if` | `(ci.object_type = 'JAVA CLASS') / (ci.object_type = 'PACKAGE BODY')` |  |  |
| 62 | · · · · · `assign` |  |  |  |
| 64 | · · · · · `assign` |  |  |  |
| 66 | · · · · · `assign` |  |  |  |
| 69 | · · · · `block` |  |  |  |
| 70 | · · · · · `assign` |  |  |  |
| 71 | · · · · · `perform` |  |  |  |
| 74 | · · · · · `sql` |  |  |  |
| 77 | · · · · `cursor` |  |  |  |
| 78 | · · · · `cursor` |  |  |  |
| 79 | · · · · `if` | `Cur_Valids%ROWCOUNT > 0` |  |  |
| 80 | · · · · · `if` | `(v_PrintInfo = 'Y')` |  |  |
| 81 | · · · · · · `perform` |  |  |  |
| 83 | · · · · · `assign` |  |  |  |
| 84 | · · · · · `cursor` |  |  |  |
| 85 | · · · · · `exit` |  |  |  |
| 87 | · · · · · `if` | `(LENGTH(v_Message) < 1950)` |  |  |
| 88 | · · · · · · `assign` |  |  |  |
| 90 | · · · · · `if` | `(v_PrintInfo = 'Y')` |  |  |
| 91 | · · · · · · `perform` |  |  |  |
| 94 | · · · · · `assign` |  |  |  |
| 95 | · · · · · `assign` |  |  |  |
| 96 | · · · · · `cursor` |  |  |  |
| 101 | · · `if` | `count_compiled = 0` |  |  |
| 102 | · · · `exit` |  |  |  |
| 106 | · `perform` |  |  |  |
| 109 | · `if` | `(LENGTH(v_Message) = 1) / (LENGTH(v_Message) > 80)` |  |  |
| 110 | · · `assign` |  |  |  |
| 111 | · · `perform` |  |  |  |
| 113 | · · `assign` |  |  |  |
| 114 | · · `perform` |  |  |  |
| 115 | · · `loop` |  |  |  |
| 116 | · · · `assign` |  |  |  |
| 117 | · · · `perform` |  |  |  |
| 118 | · · · `assign` |  |  |  |
| 120 | · · `perform` |  |  |  |
| 121 | · · `assign` |  |  |  |
| 122 | · · `perform` |  |  |  |
| 124 | · · `perform` |  |  |  |
| 125 | · · `assign` |  |  |  |
| 126 | · · `perform` |  |  |  |
| 130 | · `if` | `(p_PInstance_ID IS NOT NULL)` |  |  |
| 132 | · · `sql` |  |  | ad_pinstance |
| 139 | · `sql` |  |  |  |
| 140 | · `return` |  |  |  |
| 145 | · `perform` |  |  |  |
| 146 | · `if` | `DBMS_SQL.IS_OPEN(exec_cursor)` |  |  |
| 147 | · · `perform` |  |  |  |
| 149 | · `if` | `Cur_Valids%ISOPEN` |  |  |
| 150 | · · `cursor` |  |  |  |

