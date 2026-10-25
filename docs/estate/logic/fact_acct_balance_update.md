---
title: "Fact_Acct_Balance_Update()"
order: 50
ekos_generated: true
ekos_estate_version: 1
---

# Fact_Acct_Balance_Update()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/FACT_ACCT_BALANCE_UPDATE`
- language: plsql · fidelity: statements · statements recovered: 8 · unrecovered: 0
- arguments: `p_DeleteFirst IN VARCHAR2 DEFAULT 'N'`
- also defined in `db/oracle/procedures/Fact_Acct_Balance_Update.sql` (plsql)

**Reads:** [FACT_ACCT](../data-model/fact/fact_acct.md)

**Writes:** `FACT_ACCT_BALANCE`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 21 | `if` | `(p_DeleteFirst = 'Y')` |  |  |
| 22 | · `sql` |  |  |  |
| 23 | · `perform` |  |  |  |
| 26 | · `sql` |  | fact_acct | fact_acct_balance |
| 65 | · `perform` |  |  |  |
| 70 | `sql` |  |  |  |
| 110 | `perform` |  |  |  |
| 113 | `sql` |  |  |  |

