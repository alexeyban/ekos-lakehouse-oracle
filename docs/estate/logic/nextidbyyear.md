---
title: "NextIDByYear()"
order: 74
ekos_generated: true
ekos_estate_version: 1
---

# NextIDByYear()

- defined in: `migration-historic/331b-340s/oracle/089_FR1883270.sql`
- language: plsql · fidelity: statements · statements recovered: 4 · unrecovered: 0
- arguments: `p_AD_Sequence_ID IN NUMBER, p_IncrementNo IN NUMBER, p_CalendarYear IN CHAR, o_NextID OUT NUMBER`
- also defined in `migration-historic/353a-354a/postgresql/379_FR1883270_NextIdByYear.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/oracle/379_FR1883270_NextIdByYear.sql` (plsql)

**Reads:** [AD_SEQUENCE_NO](../data-model/ad/ad_sequence_no.md)

**Writes:** [AD_SEQUENCE_NO](../data-model/ad/ad_sequence_no.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 425 | `block` |  |  |  |
| 426 | · `sql` |  | ad_sequence_no |  |
| 433 | · `sql` |  |  | ad_sequence_no |
| 439 | · `perform` |  |  |  |

