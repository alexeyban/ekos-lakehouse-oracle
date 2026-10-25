---
title: "paymentTermDiscount()"
order: 79
ekos_generated: true
ekos_estate_version: 1
---

# paymentTermDiscount()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/PAYMENTTERMDISCOUNT`
- language: plsql · fidelity: statements · statements recovered: 20 · unrecovered: 0
- arguments: `Amount IN NUMBER, Currency_ID IN NUMBER, PaymentTerm_ID IN NUMBER, DocDate IN DATE, PayDate IN DATE`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/oracle/201406061832_IDEMPIERE-1856.sql` (plsql)
- also defined in `migration-historic/320-330/oracle/006_BF_1721252_xe.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/postgresql/201403261215_IDEMPIERE-1856.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `migration-historic/i2.0z/oracle/201403261215_IDEMPIERE-1856.sql` (plsql)
- also defined in `db/postgresql/functions/C_PaymentTerm_Discount.sql` (plpgsql)
- also defined in `db/oracle/functions/C_PaymentTerm_Discount.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201406061832_IDEMPIERE-1856.sql` (plpgsql)

**Reads:** [AD_CLIENTINFO](../data-model/ad/ad_clientinfo.md), [C_ACCTSCHEMA](../data-model/c/c_acctschema.md), [C_CURRENCY](../data-model/c/c_currency.md), [C_PAYMENTTERM](../data-model/c/c_paymentterm.md), [DUAL](../data-model/other/dual.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 40 | `assign` |  |  |  |
| 41 | `if` | `(v_Currency = 0)` |  |  |
| 42 | · `sql` |  | ad_clientinfo, c_acctschema, c_paymentterm |  |
| 50 | `sql` |  | c_currency |  |
| 55 | `sql` |  | dual |  |
| 58 | `if` | `(Amount IS NULL OR PaymentTerm_ID IS NULL OR DocDate IS NULL)` |  |  |
| 59 | · `return` |  |  |  |
| 62 | `loop` |  |  |  |
| 64 | · `assign` |  |  |  |
| 65 | · `assign` |  |  |  |
| 68 | · `if` | `(p.IsNextBusinessDay='Y')` |  |  |
| 69 | · · `assign` |  |  |  |
| 70 | · · `assign` |  |  |  |
| 74 | · `if` | `(Discount1Date >= TRUNC(PayDate)) / (Discount2Date >= TRUNC(PayDate))` |  |  |
| 76 | · · `assign` |  |  |  |
| 80 | · · `assign` |  |  |  |
| 85 | `if` | `(Discount > -v_Min AND Discount < v_Min)` |  |  |
| 86 | · `assign` |  |  |  |
| 90 | `assign` |  |  |  |
| 92 | `return` |  |  |  |

