---
title: "currencyConvertInvoice()"
order: 33
ekos_generated: true
ekos_estate_version: 1
---

# currencyConvertInvoice()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/CURRENCYCONVERTINVOICE`
- language: plsql · fidelity: statements · statements recovered: 5 · unrecovered: 0
- arguments: `p_c_invoice_id in number, p_currency_to_id in number, p_amt in number DEFAULT NULL, p_conversiondate in date DEFAULT NULL`
- returns: `number`
- also defined in `migration/i7.1z/postgresql/202007212000_IDEMPIERE-4083.sql` (plpgsql)
- also defined in `migration/i7.1z/oracle/202007212000_IDEMPIERE-4083.sql` (plsql)
- also defined in `migration/i7.1z/oracle/202010031940_IDEMPIERE-4083.sql` (plsql)
- also defined in `db/postgresql/functions/currencyConvertInvoice.sql` (plpgsql)
- also defined in `db/oracle/functions/currencyConvertInvoice.sql` (plsql)

**Reads:** [AD_CLIENTINFO](../data-model/ad/ad_clientinfo.md), [C_ACCTSCHEMA](../data-model/c/c_acctschema.md), [C_INVOICE](../data-model/c/c_invoice.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 18 | `sql` |  | c_invoice |  |
| 23 | `sql` |  | ad_clientinfo, c_acctschema |  |
| 29 | `if` | `v_BaseCurrency_ID=p_Currency_To_id AND Coalesce(v_CurrencyRate,0) > 0 AND v_Currency_ID != p_Currency_To_id AND v_IsOverrideCurrencyRate='Y'` |  |  |
| 30 | · `return` |  |  |  |
| 33 | `return` |  |  |  |

