---
title: "currencyRate()"
order: 35
ekos_generated: true
ekos_estate_version: 1
---

# currencyRate()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/CURRENCYRATE`
- language: plsql · fidelity: statements · statements recovered: 48 · unrecovered: 0
- arguments: `p_CurFrom_ID IN NUMBER, p_CurTo_ID IN NUMBER, p_ConvDate IN DATE, p_ConversionType_ID IN NUMBER, p_Client_ID IN NUMBER, p_Org_ID IN NUMBER`
- returns: `NUMBER`
- also defined in `migration-historic/i2.0z/postgresql/201410231928_IDEMPIERE-2269.sql` (plpgsql)
- also defined in `migration-historic/352a-353a/postgresql/315_replace_pljava_for34.sql` (plpgsql)
- also defined in `migration/iD10/postgresql/202305311700_IDEMPIERE-5748.sql` (plpgsql)
- also defined in `db/postgresql/functions/C_Currency_Rate.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/postgresql/391_C_Currency_Rate.sql` (plpgsql)
- also defined in `migration-historic/353a-354a/oracle/512_BF2830154_currencyConvert.sql` (plsql)
- also defined in `migration-historic/313-314/016_Recreate_C_Currency_Rate.sql` (plsql)
- also defined in `migration-historic/i2.0z/oracle/201410231928_IDEMPIERE-2269.sql` (plsql)
- also defined in `migration-historic/i2.0z/postgresql/201405301149_IDEMPIERE-1953.sql` (plpgsql)
- also defined in `db/oracle/functions/C_Currency_Rate.sql` (plsql)
- also defined in `migration/iD10/oracle/202305311700_IDEMPIERE-5748.sql` (plsql)

**Reads:** [C_CONVERSIONTYPE](../data-model/c/c_conversiontype.md), [C_CURRENCY](../data-model/c/c_currency.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 47 | `block` |  |  |  |
| 49 | · `if` | `(p_CurFrom_ID = p_CurTo_ID)` |  |  |
| 50 | · · `return` |  |  |  |
| 53 | · `if` | `(p_ConvDate IS NOT NULL)` |  |  |
| 54 | · · `assign` |  |  |  |
| 57 | · `if` | `(p_ConversionType_ID IS NULL OR p_ConversionType_ID = 0)` |  |  |
| 58 | · · `block` |  |  |  |
| 59 | · · · `sql` |  | c_conversiontype |  |
| 70 | · · · `perform` |  |  |  |
| 73 | · · `assign` |  |  |  |
| 77 | · `sql` |  | c_currency |  |
| 82 | · `if` | `(cf_IsEuro IS NULL)` |  |  |
| 83 | · · `perform` |  |  |  |
| 84 | · · `return` |  |  |  |
| 86 | · `sql` |  | c_currency |  |
| 91 | · `if` | `(ct_IsEuro IS NULL)` |  |  |
| 92 | · · `perform` |  |  |  |
| 93 | · · `return` |  |  |  |
| 97 | · `if` | `(cf_IsEuro = 'Y' AND ct_IsEMUMember ='Y' AND v_ConvDate >= ct_EMUEntryDate)` |  |  |
| 98 | · · `return` |  |  |  |
| 102 | · `if` | `(ct_IsEuro = 'Y' AND cf_IsEMUMember ='Y' AND v_ConvDate >= cf_EMUEntryDate)` |  |  |
| 103 | · · `return` |  |  |  |
| 107 | · `if` | `(cf_IsEMUMember = 'Y' AND cf_IsEMUMember ='Y'<br>			AND v_ConvDate >= cf_EMUEntryDate AND v_ConvDate >= ct_EMUEntryDate)` |  |  |
| 109 | · · `return` |  |  |  |
| 113 | · `assign` |  |  |  |
| 114 | · `assign` |  |  |  |
| 117 | · `if` | `((cf_isEMUMember = 'Y' AND v_ConvDate >= cf_EMUEntryDate)<br>	  OR (ct_isEMUMember = 'Y' AND v_ConvDate >= ct_EMUEntryDate))` |  |  |
| 119 | · · `sql` |  | c_currency |  |
| 124 | · · `if` | `(v_CurrencyEuro IS NULL)` |  |  |
| 125 | · · · `perform` |  |  |  |
| 126 | · · · `return` |  |  |  |
| 128 | · · `if` | `(cf_isEMUMember = 'Y' AND v_ConvDate >= cf_EMUEntryDate)` |  |  |
| 129 | · · · `assign` |  |  |  |
| 131 | · · · `assign` |  |  |  |
| 136 | · `block` |  |  |  |
| 146 | · · `loop` |  |  |  |
| 147 | · · · `assign` |  |  |  |
| 148 | · · · `exit` |  |  |  |
| 152 | · `if` | `(v_Rate IS NULL)` |  |  |
| 153 | · · `perform` |  |  |  |
| 154 | · · `return` |  |  |  |
| 158 | · `if` | `(cf_isEMUMember = 'Y' AND v_ConvDate >= cf_EMUEntryDate)` |  |  |
| 159 | · · `return` |  |  |  |
| 163 | · `if` | `(ct_isEMUMember = 'Y' AND v_ConvDate >= ct_EMUEntryDate)` |  |  |
| 164 | · · `return` |  |  |  |
| 167 | · `return` |  |  |  |
| 170 | · `perform` |  |  |  |
| 171 | · `return` |  |  |  |

