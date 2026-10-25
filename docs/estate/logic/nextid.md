---
title: "nextID()"
order: 73
ekos_generated: true
ekos_estate_version: 1
---

# nextID()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/NEXTID`
- language: plsql · fidelity: statements · statements recovered: 12 · unrecovered: 0
- arguments: `p_AD_Sequence_ID IN NUMBER, p_System IN CHAR, o_NextID OUT NUMBER`
- also defined in `migration-historic/360lts-i1.0a/postgresql/921_IDEMPIERE-422_NativeSequence.sql` (plpgsql)
- also defined in `db/postgresql/functions/nextID.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/316_replace_pljava_for352.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `db/oracle/procedures/nextID.sql` (plsql)
- also defined in `migration-historic/360lts-i1.0a/oracle/921_IDEMPIERE-422_NativeSequence.sql` (plsql)

**Reads:** [AD_SEQUENCE](../data-model/ad/ad_sequence.md)

**Writes:** [AD_SEQUENCE](../data-model/ad/ad_sequence.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 25 | `block` |  |  |  |
| 28 | · `if` | `(p_System = 'Y')` |  |  |
| 29 | · · `sql` |  | ad_sequence |  |
| 35 | · · `sql` |  |  | ad_sequence |
| 40 | · · `assign` |  |  |  |
| 41 | · · `if` | `Isnativeseqon = 'Y'` |  |  |
| 43 | · · · `sql` |  | ad_sequence |  |
| 48 | · · · `assign` |  |  |  |
| 50 | · · · `dynamic_execute` |  |  |  |
| 54 | · · · `sql` |  | ad_sequence |  |
| 60 | · · · `sql` |  |  | ad_sequence |
| 69 | · `perform` |  |  |  |

