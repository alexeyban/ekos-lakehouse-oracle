---
title: "C_BP_Group_Acct_Copy()"
order: 38
ekos_generated: true
ekos_estate_version: 1
---

# C_BP_Group_Acct_Copy()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/C_BP_GROUP_ACCT_COPY`
- language: plsql · fidelity: statements · statements recovered: 41 · unrecovered: 0
- arguments: `PInstance_ID IN NUMBER, BP_Group_ID IN NUMBER DEFAULT NULL`

**Reads:** [C_BPARTNER](../data-model/c/c_bpartner.md), [C_BP_CUSTOMER_ACCT](../data-model/c/c_bp_customer_acct.md), [C_BP_VENDOR_ACCT](../data-model/c/c_bp_vendor_acct.md)

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), [C_BP_CUSTOMER_ACCT](../data-model/c/c_bp_customer_acct.md), [C_BP_VENDOR_ACCT](../data-model/c/c_bp_vendor_acct.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 48 | `block` |  |  |  |
| 50 | · `perform` |  |  |  |
| 51 | · `assign` |  |  |  |
| 52 | · `sql` |  |  | ad_pinstance |
| 56 | · `sql` |  |  |  |
| 59 | · `assign` |  |  |  |
| 60 | · `loop` |  |  |  |
| 61 | · · `assign` |  |  |  |
| 62 | · · `if` | `(p.ParameterName = 'C_BP_Group_ID')` |  |  |
| 63 | · · · `assign` |  |  |  |
| 64 | · · · `perform` |  |  |  |
| 66 | · · · `perform` |  |  |  |
| 69 | · `perform` |  |  |  |
| 72 | · `if` | `(BP_Group_ID IS NOT NULL)` |  |  |
| 73 | · · `assign` |  |  |  |
| 74 | · · `perform` |  |  |  |
| 80 | · `loop` |  |  |  |
| 82 | · · `sql` |  | c_bpartner | c_bp_customer_acct |
| 90 | · · `assign` |  |  |  |
| 92 | · · `sql` |  | c_bp_customer_acct, c_bpartner | c_bp_customer_acct |
| 103 | · · `assign` |  |  |  |
| 104 | · · `perform` |  |  |  |
| 105 | · · `assign` |  |  |  |
| 106 | · · `assign` |  |  |  |
| 109 | · · `sql` |  | c_bpartner | c_bp_vendor_acct |
| 118 | · · `assign` |  |  |  |
| 120 | · · `sql` |  | c_bp_vendor_acct, c_bpartner | c_bp_vendor_acct |
| 131 | · · `assign` |  |  |  |
| 132 | · · `perform` |  |  |  |
| 133 | · · `assign` |  |  |  |
| 134 | · · `assign` |  |  |  |
| 136 | · `assign` |  |  |  |
| 141 | · `perform` |  |  |  |
| 142 | · `sql` |  |  | ad_pinstance |
| 148 | · `sql` |  |  |  |
| 149 | · `return` |  |  |  |
| 153 | · `assign` |  |  |  |
| 154 | · `perform` |  |  |  |
| 155 | · `sql` |  |  | ad_pinstance |
| 161 | · `sql` |  |  |  |
| 162 | · `return` |  |  |  |

