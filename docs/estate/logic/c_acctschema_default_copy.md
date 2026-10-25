---
title: "C_AcctSchema_Default_Copy()"
order: 37
ekos_generated: true
ekos_estate_version: 1
---

# C_AcctSchema_Default_Copy()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/C_ACCTSCHEMA_DEFAULT_COPY`
- language: plsql · fidelity: statements · statements recovered: 97 · unrecovered: 0
- arguments: `PInstance_ID IN NUMBER, Client_ID IN NUMBER DEFAULT NULL`

**Reads:** [C_BANKACCOUNT](../data-model/c/c_bankaccount.md), [C_BANKACCOUNT_ACCT](../data-model/c/c_bankaccount_acct.md), [C_BPARTNER](../data-model/c/c_bpartner.md), [C_BP_EMPLOYEE_ACCT](../data-model/c/c_bp_employee_acct.md), [C_BP_GROUP](../data-model/c/c_bp_group.md), [C_BP_GROUP_ACCT](../data-model/c/c_bp_group_acct.md), [C_CASHBOOK](../data-model/c/c_cashbook.md), [C_CASHBOOK_ACCT](../data-model/c/c_cashbook_acct.md), [C_CHARGE](../data-model/c/c_charge.md), [C_CHARGE_ACCT](../data-model/c/c_charge_acct.md), [C_PROJECT](../data-model/c/c_project.md), [C_PROJECT_ACCT](../data-model/c/c_project_acct.md), [C_TAX](../data-model/c/c_tax.md), [C_TAX_ACCT](../data-model/c/c_tax_acct.md), [C_WITHHOLDING](../data-model/c/c_withholding.md), [C_WITHHOLDING_ACCT](../data-model/c/c_withholding_acct.md), [M_PRODUCT_CATEGORY](../data-model/m/m_product_category.md), [M_PRODUCT_CATEGORY_ACCT](../data-model/m/m_product_category_acct.md), [M_WAREHOUSE](../data-model/m/m_warehouse.md), [M_WAREHOUSE_ACCT](../data-model/m/m_warehouse_acct.md)

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), [C_BANKACCOUNT_ACCT](../data-model/c/c_bankaccount_acct.md), [C_BP_EMPLOYEE_ACCT](../data-model/c/c_bp_employee_acct.md), [C_BP_GROUP_ACCT](../data-model/c/c_bp_group_acct.md), [C_CASHBOOK_ACCT](../data-model/c/c_cashbook_acct.md), [C_CHARGE_ACCT](../data-model/c/c_charge_acct.md), [C_PROJECT_ACCT](../data-model/c/c_project_acct.md), [C_TAX_ACCT](../data-model/c/c_tax_acct.md), [C_WITHHOLDING_ACCT](../data-model/c/c_withholding_acct.md), [M_PRODUCT_CATEGORY_ACCT](../data-model/m/m_product_category_acct.md), [M_WAREHOUSE_ACCT](../data-model/m/m_warehouse_acct.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 44 | `block` |  |  |  |
| 46 | · `perform` |  |  |  |
| 47 | · `assign` |  |  |  |
| 48 | · `sql` |  |  | ad_pinstance |
| 52 | · `sql` |  |  |  |
| 55 | · `assign` |  |  |  |
| 56 | · `loop` |  |  |  |
| 57 | · · `assign` |  |  |  |
| 58 | · · `if` | `(p.ParameterName = 'AD_Client_ID')` |  |  |
| 59 | · · · `assign` |  |  |  |
| 60 | · · · `perform` |  |  |  |
| 62 | · · · `perform` |  |  |  |
| 65 | · `perform` |  |  |  |
| 68 | · `if` | `(Client_ID IS NOT NULL)` |  |  |
| 69 | · · `assign` |  |  |  |
| 70 | · · `perform` |  |  |  |
| 77 | · `loop` |  |  |  |
| 79 | · · `sql` |  | m_product_category | m_product_category_acct |
| 93 | · · `assign` |  |  |  |
| 95 | · · `sql` |  | m_product_category, m_product_category_acct | m_product_category_acct |
| 111 | · · `assign` |  |  |  |
| 112 | · · `perform` |  |  |  |
| 113 | · · `assign` |  |  |  |
| 114 | · · `assign` |  |  |  |
| 118 | · · `sql` |  | c_bp_group_acct | c_bp_group_acct |
| 136 | · · `assign` |  |  |  |
| 138 | · · `sql` |  | c_bp_group, c_bp_group_acct | c_bp_group_acct |
| 158 | · · `assign` |  |  |  |
| 159 | · · `perform` |  |  |  |
| 160 | · · `assign` |  |  |  |
| 161 | · · `assign` |  |  |  |
| 165 | · · `sql` |  | c_bp_employee_acct | c_bp_employee_acct |
| 173 | · · `assign` |  |  |  |
| 175 | · · `sql` |  | c_bp_employee_acct, c_bpartner | c_bp_employee_acct |
| 187 | · · `assign` |  |  |  |
| 188 | · · `perform` |  |  |  |
| 189 | · · `assign` |  |  |  |
| 190 | · · `assign` |  |  |  |
| 194 | · · `sql` |  | m_warehouse_acct | m_warehouse_acct |
| 204 | · · `assign` |  |  |  |
| 206 | · · `sql` |  | m_warehouse, m_warehouse_acct | m_warehouse_acct |
| 218 | · · `assign` |  |  |  |
| 219 | · · `perform` |  |  |  |
| 220 | · · `assign` |  |  |  |
| 221 | · · `assign` |  |  |  |
| 225 | · · `sql` |  | c_project_acct | c_project_acct |
| 233 | · · `assign` |  |  |  |
| 235 | · · `sql` |  | c_project, c_project_acct | c_project_acct |
| 247 | · · `assign` |  |  |  |
| 248 | · · `perform` |  |  |  |
| 249 | · · `assign` |  |  |  |
| 250 | · · `assign` |  |  |  |
| 254 | · · `sql` |  | c_tax_acct | c_tax_acct |
| 265 | · · `assign` |  |  |  |
| 267 | · · `sql` |  | c_tax, c_tax_acct | c_tax_acct |
| 279 | · · `assign` |  |  |  |
| 280 | · · `perform` |  |  |  |
| 281 | · · `assign` |  |  |  |
| 282 | · · `assign` |  |  |  |
| 286 | · · `sql` |  | c_bankaccount_acct | c_bankaccount_acct |
| 304 | · · `assign` |  |  |  |
| 306 | · · `sql` |  | c_bankaccount, c_bankaccount_acct | c_bankaccount_acct |
| 324 | · · `assign` |  |  |  |
| 325 | · · `perform` |  |  |  |
| 326 | · · `assign` |  |  |  |
| 327 | · · `assign` |  |  |  |
| 331 | · · `sql` |  | c_withholding_acct | c_withholding_acct |
| 338 | · · `assign` |  |  |  |
| 340 | · · `sql` |  | c_withholding, c_withholding_acct | c_withholding_acct |
| 352 | · · `assign` |  |  |  |
| 353 | · · `perform` |  |  |  |
| 354 | · · `assign` |  |  |  |
| 355 | · · `assign` |  |  |  |
| 359 | · · `sql` |  | c_charge_acct | c_charge_acct |
| 367 | · · `assign` |  |  |  |
| 369 | · · `sql` |  | c_charge, c_charge_acct | c_charge_acct |
| 381 | · · `assign` |  |  |  |
| 382 | · · `perform` |  |  |  |
| 383 | · · `assign` |  |  |  |
| 384 | · · `assign` |  |  |  |
| 388 | · · `sql` |  | c_cashbook_acct | c_cashbook_acct |
| 399 | · · `assign` |  |  |  |
| 401 | · · `sql` |  | c_cashbook, c_cashbook_acct | c_cashbook_acct |
| 415 | · · `assign` |  |  |  |
| 416 | · · `perform` |  |  |  |
| 417 | · · `assign` |  |  |  |
| 418 | · · `assign` |  |  |  |
| 420 | · `assign` |  |  |  |
| 425 | · `perform` |  |  |  |
| 426 | · `sql` |  |  | ad_pinstance |
| 432 | · `sql` |  |  |  |
| 433 | · `return` |  |  |  |
| 437 | · `assign` |  |  |  |
| 438 | · `perform` |  |  |  |
| 439 | · `sql` |  |  | ad_pinstance |
| 445 | · `sql` |  |  |  |
| 446 | · `return` |  |  |  |

