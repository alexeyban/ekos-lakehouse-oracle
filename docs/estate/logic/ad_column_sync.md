---
title: "AD_Column_Sync()"
order: 9
ekos_generated: true
ekos_estate_version: 1
---

# AD_Column_Sync()

- defined in: `oracle://idempiere-db/ADEMPIERE/procedure/AD_COLUMN_SYNC`
- language: plsql · fidelity: partial · statements recovered: 95 · unrecovered: 1
- arguments: `p_PInstance_ID IN NUMBER`
- also defined in `db/oracle/procedures/AD_Column_Sync.sql` (plsql)

**Reads:** [AD_COLUMN](../data-model/ad/ad_column.md), [AD_TABLE](../data-model/ad/ad_table.md), `USER_TABLES`, `USER_TAB_COLUMNS`

**Writes:** [AD_PINSTANCE](../data-model/ad/ad_pinstance.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 45 | `block` |  |  |  |
| 47 | · `perform` |  |  |  |
| 48 | · `assign` |  |  |  |
| 49 | · `sql` |  |  | ad_pinstance |
| 53 | · `sql` |  |  |  |
| 56 | · `assign` |  |  |  |
| 57 | · `loop` |  |  |  |
| 58 | · · `assign` |  |  |  |
| 59 | · · `assign` |  |  |  |
| 61 | · `perform` |  |  |  |
| 64 | · `assign` |  |  |  |
| 65 | · `sql` |  | ad_column, ad_table |  |
| 75 | · `assign` |  |  |  |
| 76 | · `block` |  |  |  |
| 77 | · · `sql` |  | user_tables |  |
| 82 | · · `sql` |  |  |  |
| 86 | · `if` | `(v_DB_TableName IS NULL)` |  |  |
| 87 | · · `assign` |  |  |  |
| 88 | · · `block` |  |  |  |
| 89 | · · · `assign` |  |  |  |
| 91 | · · · `dynamic_execute` |  |  |  |
| 94 | · · · `assign` |  |  |  |
| 95 | · · · `assign` |  |  |  |
| 96 | · · · `unrecovered` |  |  |  |
| 102 | · `assign` |  |  |  |
| 103 | · `block` |  |  |  |
| 104 | · · `sql` |  | user_tab_columns |  |
| 110 | · · `sql` |  |  |  |
| 117 | · `if` | `(v_DB_DataType IS NULL)` |  |  |
| 118 | · · `assign` |  |  |  |
| 119 | · · `block` |  |  |  |
| 121 | · · · `assign` |  |  |  |
| 123 | · · · `if` | `(v_AD_Reference_ID IN (10,14)) / (v_AD_Reference_ID IN (17,20,28)) / (v_AD_Reference_ID IN (13,18,19,21,25,27,30,31)) / (v_AD_Reference_ID IN (11,12,22,29)) / (v_AD_Reference_ID IN (15,16))` |  |  |
| 125 | · · · · `assign` |  |  |  |
| 128 | · · · · `assign` |  |  |  |
| 131 | · · · · `assign` |  |  |  |
| 134 | · · · · `assign` |  |  |  |
| 137 | · · · · `assign` |  |  |  |
| 139 | · · · · `assign` |  |  |  |
| 140 | · · · · `assign` |  |  |  |
| 143 | · · · `if` | `(v_DefaultValue IS NOT NULL AND LENGTH(v_DefaultValue) <> 0)` |  |  |
| 144 | · · · · `if` | `(v_AD_Reference_ID IN (10,14,17,20,28))` |  |  |
| 145 | · · · · · `assign` |  |  |  |
| 147 | · · · · · `assign` |  |  |  |
| 151 | · · · `if` | `(v_IsMandatory = 'Y')` |  |  |
| 152 | · · · · `if` | `(v_DefaultValue IS NULL OR LENGTH(v_DefaultValue) = 0)` |  |  |
| 153 | · · · · · `assign` |  |  |  |
| 154 | · · · · · `assign` |  |  |  |
| 156 | · · · · · `assign` |  |  |  |
| 160 | · · · `if` | `(v_Result = 1)` |  |  |
| 161 | · · · · `dynamic_execute` |  |  |  |
| 162 | · · · · `assign` |  |  |  |
| 166 | · · · `assign` |  |  |  |
| 167 | · · · `assign` |  |  |  |
| 174 | · · `assign` |  |  |  |
| 175 | · · `block` |  |  |  |
| 177 | · · · `assign` |  |  |  |
| 179 | · · · `if` | `(v_AD_Reference_ID IN (10,14)) / (v_AD_Reference_ID IN (17,20,28)) / (v_AD_Reference_ID IN (13,18,19,21,25,27,30,31)) / (v_AD_Reference_ID IN (11,12,22,29)) / (v_AD_Reference_ID IN (15,16))` |  |  |
| 181 | · · · · `assign` |  |  |  |
| 184 | · · · · `assign` |  |  |  |
| 187 | · · · · `assign` |  |  |  |
| 190 | · · · · `assign` |  |  |  |
| 193 | · · · · `assign` |  |  |  |
| 195 | · · · · `assign` |  |  |  |
| 196 | · · · · `assign` |  |  |  |
| 199 | · · · `if` | `(v_DefaultValue IS NOT NULL AND LENGTH(v_DefaultValue) <> 0)` |  |  |
| 200 | · · · · `if` | `(v_AD_Reference_ID IN (10,14,17,20,28))` |  |  |
| 201 | · · · · · `assign` |  |  |  |
| 203 | · · · · · `assign` |  |  |  |
| 207 | · · · `if` | `(v_IsMandatory = 'Y')` |  |  |
| 208 | · · · · `if` | `(v_DefaultValue IS NULL OR LENGTH(v_DefaultValue) = 0)` |  |  |
| 209 | · · · · · `assign` |  |  |  |
| 210 | · · · · · `assign` |  |  |  |
| 212 | · · · · · `assign` |  |  |  |
| 216 | · · · `if` | `(v_Result = 1)` |  |  |
| 217 | · · · · `dynamic_execute` |  |  |  |
| 218 | · · · · `assign` |  |  |  |
| 222 | · · · `assign` |  |  |  |
| 223 | · · · `assign` |  |  |  |
| 240 | · `if` | `(v_DB_TableName IS NULL)` |  |  |
| 241 | · · `assign` |  |  |  |
| 242 | · · `block` |  |  |  |
| 243 | · · · `assign` |  |  |  |
| 244 | · · · `dynamic_execute` |  |  |  |
| 247 | · · · `assign` |  |  |  |
| 248 | · · · `assign` |  |  |  |
| 255 | · `perform` |  |  |  |
| 256 | · `sql` |  |  | ad_pinstance |
| 262 | · `sql` |  |  |  |
| 263 | · `return` |  |  |  |
| 267 | · `assign` |  |  |  |
| 268 | · `perform` |  |  |  |
| 269 | · `sql` |  |  |  |
| 270 | · `sql` |  |  | ad_pinstance |
| 276 | · `sql` |  |  |  |
| 277 | · `return` |  |  |  |

