---
title: "FACT_ACCT"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# FACT_ACCT

Area [FACT](../../data-model/fact/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_Fact_Acct`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `FACT_ACCT_ID` | NUMBER(10,0) | PK | yes | Accounting Fact |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `C_ACCTSCHEMA_ID` | NUMBER(10,0) |  | yes | Accounting Schema | [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | 0 | 0 |
| `ACCOUNT_ID` | NUMBER(10,0) |  | yes | Account |  | 0 | 0 |
| `DATETRX` | DATE |  | yes | Transaction Date |  | 0 | 0 |
| `DATEACCT` | DATE |  | yes | Account Date |  | 0 | 0 |
| `C_PERIOD_ID` | NUMBER(10,0) |  |  | Period | [C_PERIOD](../../data-model/c/c_period.md) | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 0 |
| `RECORD_ID` | NUMBER(10,0) |  | yes | Record ID |  | 0 | 0 |
| `LINE_ID` | NUMBER(10,0) |  |  | Line ID |  | 0 | 0 |
| `GL_CATEGORY_ID` | NUMBER(10,0) |  |  | GL Category | [GL_CATEGORY](../../data-model/gl/gl_category.md) | 0 | 0 |
| `GL_BUDGET_ID` | NUMBER(10,0) |  |  | Budget | [GL_BUDGET](../../data-model/gl/gl_budget.md) | 0 | 0 |
| `C_TAX_ID` | NUMBER(10,0) |  |  | Tax | [C_TAX](../../data-model/c/c_tax.md) | 0 | 0 |
| `M_LOCATOR_ID` | NUMBER(10,0) |  |  | Locator | [M_LOCATOR](../../data-model/m/m_locator.md) | 0 | 0 |
| `POSTINGTYPE` | CHAR(1) |  | yes | Posting Type |  | 0 | 0 |
| `C_CURRENCY_ID` | NUMBER(10,0) |  | yes | Currency | [C_CURRENCY](../../data-model/c/c_currency.md) | 0 | 0 |
| `AMTSOURCEDR` | NUMBER |  | yes | Source Debit |  | 0 | 0 |
| `AMTSOURCECR` | NUMBER |  | yes | Source Credit |  | 0 | 0 |
| `AMTACCTDR` | NUMBER |  | yes | Accounted Debit |  | 0 | 0 |
| `AMTACCTCR` | NUMBER |  | yes | Accounted Credit |  | 0 | 0 |
| `C_UOM_ID` | NUMBER(10,0) |  |  | UOM | [C_UOM](../../data-model/c/c_uom.md) | 0 | 0 |
| `QTY` | NUMBER |  |  | Quantity |  | 0 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  |  | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 0 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  |  | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 0 |
| `AD_ORGTRX_ID` | NUMBER(10,0) |  |  | Trx Organization |  | 0 | 0 |
| `C_LOCFROM_ID` | NUMBER(10,0) |  |  | Location From | [C_LOCATION](../../data-model/c/c_location.md) | 0 | 0 |
| `C_LOCTO_ID` | NUMBER(10,0) |  |  | Location To | [C_LOCATION](../../data-model/c/c_location.md) | 0 | 0 |
| `C_SALESREGION_ID` | NUMBER(10,0) |  |  | Sales Region | [C_SALESREGION](../../data-model/c/c_salesregion.md) | 0 | 0 |
| `C_PROJECT_ID` | NUMBER(10,0) |  |  | Project | [C_PROJECT](../../data-model/c/c_project.md) | 0 | 0 |
| `C_CAMPAIGN_ID` | NUMBER(10,0) |  |  | Campaign | [C_CAMPAIGN](../../data-model/c/c_campaign.md) | 0 | 0 |
| `C_ACTIVITY_ID` | NUMBER(10,0) |  |  | Activity | [C_ACTIVITY](../../data-model/c/c_activity.md) | 0 | 0 |
| `USER1_ID` | NUMBER(10,0) |  |  | User Element List 1 | [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | 0 | 0 |
| `USER2_ID` | NUMBER(10,0) |  |  | User Element List 2 | [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `A_ASSET_ID` | NUMBER(10,0) |  |  | Asset |  | 0 | 0 |
| `C_SUBACCT_ID` | NUMBER(10,0) |  |  | Sub Account | [C_SUBACCT](../../data-model/c/c_subacct.md) | 0 | 0 |
| `USERELEMENT1_ID` | NUMBER(10,0) |  |  | User Column 1 |  | 0 | 0 |
| `USERELEMENT2_ID` | NUMBER(10,0) |  |  | User Column 2 |  | 0 | 0 |
| `C_PROJECTPHASE_ID` | NUMBER(10,0) |  |  | Project Phase | [C_PROJECTPHASE](../../data-model/c/c_projectphase.md) | 0 | 0 |
| `C_PROJECTTASK_ID` | NUMBER(10,0) |  |  | Project Task | [C_PROJECTTASK](../../data-model/c/c_projecttask.md) | 0 | 0 |
| `FACT_ACCT_UU` | VARCHAR2(36 CHAR) |  |  | Fact_Acct_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022714` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | FACT_ACCT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | FACT_ACCT.AD_ORGTRX_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | FACT_ACCT.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |
| [A_ASSET](../../data-model/a/a_asset.md) | FACT_ACCT.A_ASSET_ID → A_ASSET.A_ASSET_ID | NO ACTION |
| [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | FACT_ACCT.C_ACCTSCHEMA_ID → C_ACCTSCHEMA.C_ACCTSCHEMA_ID | CASCADE |
| [C_ACTIVITY](../../data-model/c/c_activity.md) | FACT_ACCT.C_ACTIVITY_ID → C_ACTIVITY.C_ACTIVITY_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | FACT_ACCT.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_CAMPAIGN](../../data-model/c/c_campaign.md) | FACT_ACCT.C_CAMPAIGN_ID → C_CAMPAIGN.C_CAMPAIGN_ID | NO ACTION |
| [C_CURRENCY](../../data-model/c/c_currency.md) | FACT_ACCT.C_CURRENCY_ID → C_CURRENCY.C_CURRENCY_ID | NO ACTION |
| [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | FACT_ACCT.USER1_ID → C_ELEMENTVALUE.C_ELEMENTVALUE_ID | NO ACTION |
| [C_LOCATION](../../data-model/c/c_location.md) | FACT_ACCT.C_LOCFROM_ID → C_LOCATION.C_LOCATION_ID | NO ACTION |
| [C_PERIOD](../../data-model/c/c_period.md) | FACT_ACCT.C_PERIOD_ID → C_PERIOD.C_PERIOD_ID | NO ACTION |
| [C_PROJECT](../../data-model/c/c_project.md) | FACT_ACCT.C_PROJECT_ID → C_PROJECT.C_PROJECT_ID | NO ACTION |
| [C_PROJECTPHASE](../../data-model/c/c_projectphase.md) | FACT_ACCT.C_PROJECTPHASE_ID → C_PROJECTPHASE.C_PROJECTPHASE_ID | SET NULL |
| [C_PROJECTTASK](../../data-model/c/c_projecttask.md) | FACT_ACCT.C_PROJECTTASK_ID → C_PROJECTTASK.C_PROJECTTASK_ID | SET NULL |
| [C_SALESREGION](../../data-model/c/c_salesregion.md) | FACT_ACCT.C_SALESREGION_ID → C_SALESREGION.C_SALESREGION_ID | NO ACTION |
| [C_SUBACCT](../../data-model/c/c_subacct.md) | FACT_ACCT.C_SUBACCT_ID → C_SUBACCT.C_SUBACCT_ID | NO ACTION |
| [C_TAX](../../data-model/c/c_tax.md) | FACT_ACCT.C_TAX_ID → C_TAX.C_TAX_ID | NO ACTION |
| [C_UOM](../../data-model/c/c_uom.md) | FACT_ACCT.C_UOM_ID → C_UOM.C_UOM_ID | NO ACTION |
| [GL_BUDGET](../../data-model/gl/gl_budget.md) | FACT_ACCT.GL_BUDGET_ID → GL_BUDGET.GL_BUDGET_ID | NO ACTION |
| [GL_CATEGORY](../../data-model/gl/gl_category.md) | FACT_ACCT.GL_CATEGORY_ID → GL_CATEGORY.GL_CATEGORY_ID | NO ACTION |
| [M_LOCATOR](../../data-model/m/m_locator.md) | FACT_ACCT.M_LOCATOR_ID → M_LOCATOR.M_LOCATOR_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | FACT_ACCT.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_TAXDECLARATIONACCT](../../data-model/c/c_taxdeclarationacct.md) | C_TAXDECLARATIONACCT.FACT_ACCT_ID → FACT_ACCT.FACT_ACCT_ID | CASCADE |
| [FACT_RECONCILIATION](../../data-model/fact/fact_reconciliation.md) | FACT_RECONCILIATION.FACT_ACCT_ID → FACT_ACCT.FACT_ACCT_ID | NO ACTION |
| `T_INVOICEGL` | T_INVOICEGL.FACT_ACCT_ID → FACT_ACCT.FACT_ACCT_ID | CASCADE |

```mermaid
erDiagram
  AD_CLIENT ||--o{ FACT_ACCT : ""
  AD_ORG ||--o{ FACT_ACCT : ""
  AD_TABLE ||--o{ FACT_ACCT : ""
  A_ASSET ||--o{ FACT_ACCT : ""
  C_ACCTSCHEMA ||--o{ FACT_ACCT : ""
  C_ACTIVITY ||--o{ FACT_ACCT : ""
  C_BPARTNER ||--o{ FACT_ACCT : ""
  C_CAMPAIGN ||--o{ FACT_ACCT : ""
  C_CURRENCY ||--o{ FACT_ACCT : ""
  C_ELEMENTVALUE ||--o{ FACT_ACCT : ""
  C_LOCATION ||--o{ FACT_ACCT : ""
  C_PERIOD ||--o{ FACT_ACCT : ""
  C_PROJECT ||--o{ FACT_ACCT : ""
  C_PROJECTPHASE ||--o{ FACT_ACCT : ""
  C_PROJECTTASK ||--o{ FACT_ACCT : ""
  C_SALESREGION ||--o{ FACT_ACCT : ""
  C_SUBACCT ||--o{ FACT_ACCT : ""
  C_TAX ||--o{ FACT_ACCT : ""
  C_UOM ||--o{ FACT_ACCT : ""
  FACT_ACCT ||--o{ C_TAXDECLARATIONACCT : ""
  FACT_ACCT ||--o{ FACT_RECONCILIATION : ""
  FACT_ACCT ||--o{ T_INVOICEGL : ""
  GL_BUDGET ||--o{ FACT_ACCT : ""
  GL_CATEGORY ||--o{ FACT_ACCT : ""
  M_LOCATOR ||--o{ FACT_ACCT : ""
  M_PRODUCT ||--o{ FACT_ACCT : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_app, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 10 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [Fact_Acct_Balance_Update](../../logic/fact_acct_balance_update.md) |
| View | `FACT_ACCT_BALANCE` |
| View | `RV_FACT_ACCT` |
| View | `RV_FACT_ACCT_DAY` |
| View | `RV_FACT_ACCT_PERIOD` |
| View | `RV_FACT_ADAXA` |
| View | `RV_PROJECTLINEISSUE` |
| View | `T_INVOICEGL_V` |
| View | `fact_acct_balance` |
| View | `rv_fact_acct` |
| View | `rv_fact_acct_day` |
| View | `rv_fact_acct_period` |
| View | `rv_fact_adaxa` |
| View | `rv_projectlineissue` |
| View | `t_invoicegl_v` |
| View | `t_invoicegl_vt` |

## Schema history

99 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-05-14T13:59 | iD13 | `add_column` | CustomFieldText2 | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Charge_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | CustomFieldText3 | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | M_AttributeSetInstance_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | CustomFieldText3 | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Employee_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Charge_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | M_Warehouse_ID | IDEMPIERE-5598 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| `model_column_missing` | `columns.C_Department_ID` | unexplained |
| `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| `mandatory_but_nullable` | `columns.C_Period_ID.nullable` | unexplained |
| `model_column_missing` | `columns.CustomFieldText1` | unexplained |
| `model_column_missing` | `columns.CustomFieldText2` | unexplained |
| `model_column_missing` | `columns.CustomFieldText3` | unexplained |
| `model_column_missing` | `columns.CustomFieldText4` | unexplained |
| `mandatory_but_nullable` | `columns.GL_Category_ID.nullable` | unexplained |
| `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.fact_acct.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
