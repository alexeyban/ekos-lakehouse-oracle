---
title: "AD_Sequence_Doc()"
order: 10
ekos_generated: true
ekos_estate_version: 1
---

# AD_Sequence_Doc()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/AD_SEQUENCE_DOC`
- language: plsql · fidelity: statements · statements recovered: 8 · unrecovered: 0
- arguments: `p_SequenceName IN VARCHAR2, p_AD_Client_ID IN NUMBER, o_DocumentNo OUT VARCHAR2`
- also defined in `db/oracle/procedures/AD_Sequence_Doc.sql` (plsql)

**Writes:** [AD_SEQUENCE](../data-model/ad/ad_sequence.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 26 | `block` |  |  |  |
| 27 | · `sql` |  |  |  |
| 37 | · `if` | `(v_NextNoSys <> -1 AND p_AD_Client_ID < 1000000)` |  |  |
| 38 | · · `sql` |  |  | ad_sequence |
| 42 | · · `assign` |  |  |  |
| 44 | · · `sql` |  |  | ad_sequence |
| 48 | · · `assign` |  |  |  |
| 53 | · `raise` |  |  |  |

