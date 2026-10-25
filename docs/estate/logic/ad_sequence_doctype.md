---
title: "AD_Sequence_DocType()"
order: 11
ekos_generated: true
ekos_estate_version: 1
---

# AD_Sequence_DocType()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/AD_SEQUENCE_DOCTYPE`
- language: plsql · fidelity: statements · statements recovered: 15 · unrecovered: 0
- arguments: `p_DocType_ID IN NUMBER, p_ID IN NUMBER, p_DocumentNo OUT VARCHAR2`
- also defined in `db/oracle/procedures/AD_Sequence_DocType.sql` (plsql)

**Reads:** [C_DOCTYPE](../data-model/c/c_doctype.md)

**Writes:** [AD_SEQUENCE](../data-model/ad/ad_sequence.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 30 | `block` |  |  |  |
| 32 | · `block` |  |  |  |
| 33 | · · `sql` |  | c_doctype |  |
| 41 | · · `sql` |  |  |  |
| 44 | · `if` | `(v_Sequence_ID IS NULL)` |  |  |
| 45 | · · `assign` |  |  |  |
| 46 | · · `perform` |  |  |  |
| 47 | · · `return` |  |  |  |
| 51 | · `sql` |  |  |  |
| 61 | · `if` | `(v_NextNoSys <> -1 AND p_ID < 1000000)` |  |  |
| 62 | · · `sql` |  |  | ad_sequence |
| 65 | · · `assign` |  |  |  |
| 67 | · · `sql` |  |  | ad_sequence |
| 70 | · · `assign` |  |  |  |
| 76 | · `raise` |  |  |  |

