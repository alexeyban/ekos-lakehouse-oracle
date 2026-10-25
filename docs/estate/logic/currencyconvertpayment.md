---
title: "currencyConvertPayment()"
order: 34
ekos_generated: true
ekos_estate_version: 1
---

# currencyConvertPayment()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/CURRENCYCONVERTPAYMENT`
- language: plsql · fidelity: statements · statements recovered: 7 · unrecovered: 0
- arguments: `p_C_Payment_ID IN NUMBER, p_Currency_To_id IN NUMBER, p_Amt IN NUMBER DEFAULT NULL, p_conversionDate IN DATE DEFAULT NULL`
- returns: `NUMBER`
- also defined in `migration/i7.1z/postgresql/202007211900_IDEMPIERE-4083.sql` (plpgsql)
- also defined in `migration/i7.1z/oracle/202007211900_IDEMPIERE-4083.sql` (plsql)
- also defined in `db/postgresql/functions/currencyConvertPayment.sql` (plpgsql)
- also defined in `db/oracle/functions/currencyConvertPayment.sql` (plsql)
- also defined in `migration/i7.1z/oracle/202010031940_IDEMPIERE-4083.sql` (plsql)
- also defined in `migration/i8.1z/postgresql/202011101712_IDEMPIERE-4083.sql` (plpgsql)
- also defined in `migration/i8.1z/oracle/202011101712_IDEMPIERE-4083.sql` (plsql)

**Reads:** [AD_CLIENTINFO](../data-model/ad/ad_clientinfo.md), [C_ACCTSCHEMA](../data-model/c/c_acctschema.md), `C_PAYMENT_V`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 22 | `sql` |  | c_payment_v |  |
| 27 | `sql` |  | ad_clientinfo, c_acctschema |  |
| 33 | `if` | `v_BaseCurrency_ID=p_Currency_To_id AND Coalesce(v_CurrencyRate,0) > 0 AND Coalesce(v_ConvertedAmt,0) != 0 AND v_Currency_ID != p_Currency_To_id AND v_IsOverrideCurrencyRate='Y'` |  |  |
| 34 | · `if` | `p_Amt IS NULL` |  |  |
| 35 | · · `return` |  |  |  |
| 37 | · · `return` |  |  |  |
| 41 | `return` |  |  |  |

