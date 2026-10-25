---
title: "AD_Sequence_Next()"
order: 12
ekos_generated: true
ekos_estate_version: 1
---

# AD_Sequence_Next()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/AD_SEQUENCE_NEXT`
- language: plsql · fidelity: statements · statements recovered: 9 · unrecovered: 0
- arguments: `p_TableName IN VARCHAR2, p_ID IN NUMBER, p_NextNo OUT NUMBER`
- also defined in `db/oracle/procedures/AD_Sequence_Next.sql` (plsql)

**Writes:** [AD_SEQUENCE](../data-model/ad/ad_sequence.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 25 | `block` |  |  |  |
| 26 | · `assign` |  |  |  |
| 27 | · `sql` |  |  |  |
| 36 | · `assign` |  |  |  |
| 37 | · `if` | `(v_NextNoSys <> -1 AND p_ID < 1000000)` |  |  |
| 38 | · · `sql` |  |  | ad_sequence |
| 42 | · · `assign` |  |  |  |
| 44 | · · `sql` |  |  | ad_sequence |
| 52 | · `raise` |  |  |  |

