---
title: "C_PAYMENT"
order: 119
ekos_generated: true
ekos_estate_version: 1
---

# C_PAYMENT

The Payment Line

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_C_Payment`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_PAYMENT_ID` | NUMBER(10,0) | PK | yes | Payment |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 2 |
| `DATETRX` | DATE |  | yes | Transaction Date |  | 0 | 1 |
| `ISRECEIPT` | CHAR(1) |  | yes | Receipt |  | 0 | 1 |
| `C_DOCTYPE_ID` | NUMBER(10,0) |  | yes | Document Type | [C_DOCTYPE](../../data-model/c/c_doctype.md) | 0 | 1 |
| `TRXTYPE` | CHAR(1) |  | yes | Transaction Type |  | 0 | 2 |
| `C_BANKACCOUNT_ID` | NUMBER(10,0) |  |  | Bank Account | [C_BANKACCOUNT](../../data-model/c/c_bankaccount.md) | 0 | 1 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  |  | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 1 |
| `C_INVOICE_ID` | NUMBER(10,0) |  |  | Invoice | [C_INVOICE](../../data-model/c/c_invoice.md) | 1 | 1 |
| `C_BP_BANKACCOUNT_ID` | NUMBER(10,0) |  |  | Partner Bank Account | [C_BP_BANKACCOUNT](../../data-model/c/c_bp_bankaccount.md) | 2 | 0 |
| `C_PAYMENTBATCH_ID` | NUMBER(10,0) |  |  | Payment Batch | [C_PAYMENTBATCH](../../data-model/c/c_paymentbatch.md) | 2 | 0 |
| `TENDERTYPE` | CHAR(1) |  | yes | Tender type |  | 0 | 2 |
| `CREDITCARDTYPE` | CHAR(1) |  |  | Credit Card |  | 1 | 1 |
| `CREDITCARDNUMBER` | VARCHAR2(20 CHAR) |  |  | Number |  | 2 | 0 |
| `CREDITCARDVV` | VARCHAR2(4 CHAR) |  |  | Verification Code |  | 2 | 0 |
| `CREDITCARDEXPMM` | NUMBER(10,0) |  |  | Exp. Month |  | 1 | 1 |
| `CREDITCARDEXPYY` | NUMBER(10,0) |  |  | Exp. Year |  | 1 | 1 |
| `MICR` | VARCHAR2(20 CHAR) |  |  | Micr |  | 2 | 0 |
| `ROUTINGNO` | VARCHAR2(20 CHAR) |  |  | Routing No |  | 2 | 0 |
| `ACCOUNTNO` | VARCHAR2(20 CHAR) |  |  | Account No |  | 2 | 0 |
| `CHECKNO` | VARCHAR2(20 CHAR) |  |  | Check No |  | 2 | 0 |
| `A_NAME` | VARCHAR2(60 CHAR) |  |  | Account Name |  | 2 | 0 |
| `A_STREET` | VARCHAR2(60 CHAR) |  |  | Account Street |  | 2 | 0 |
| `A_CITY` | VARCHAR2(60 CHAR) |  |  | Account City |  | 2 | 0 |
| `A_STATE` | VARCHAR2(40 CHAR) |  |  | Account State |  | 2 | 0 |
| `A_ZIP` | VARCHAR2(20 CHAR) |  |  | Account Zip/Postal |  | 2 | 0 |
| `A_IDENT_DL` | VARCHAR2(20 CHAR) |  |  | Driver License |  | 2 | 0 |
| `A_IDENT_SSN` | VARCHAR2(20 CHAR) |  |  | Social Security No |  | 2 | 0 |
| `A_EMAIL` | VARCHAR2(60 CHAR) |  |  | Account EMail |  | 2 | 0 |
| `VOICEAUTHCODE` | VARCHAR2(20 CHAR) |  |  | Voice authorization code |  | 2 | 0 |
| `ORIG_TRXID` | VARCHAR2(20 CHAR) |  |  | Original Transaction ID |  | 2 | 0 |
| `PONUM` | VARCHAR2(60 CHAR) |  |  | PO Number |  | 2 | 0 |
| `C_CURRENCY_ID` | NUMBER(10,0) |  | yes | Currency | [C_CURRENCY](../../data-model/c/c_currency.md) | 0 | 1 |
| `PAYAMT` | NUMBER |  | yes | Payment amount |  | 0 | 2 |
| `DISCOUNTAMT` | NUMBER |  |  | Discount Amount |  | 0 | 2 |
| `WRITEOFFAMT` | NUMBER |  |  | Write-off Amount |  | 0 | 2 |
| `TAXAMT` | NUMBER |  |  | Tax Amount |  | 0 | 1 |
| `ISAPPROVED` | CHAR(1) |  | yes | Approved |  | 0 | 1 |
| `R_PNREF` | VARCHAR2(20 CHAR) |  |  | Reference |  | 2 | 0 |
| `R_RESULT` | VARCHAR2(20 CHAR) |  |  | Result |  | 2 | 0 |
| `R_RESPMSG` | VARCHAR2(60 CHAR) |  |  | Response Message |  | 2 | 0 |
| `R_AUTHCODE` | VARCHAR2(20 CHAR) |  |  | Authorization Code |  | 2 | 0 |
| `R_AVSADDR` | CHAR(1) |  |  | Address verified |  | 2 | 0 |
| `R_AVSZIP` | CHAR(1) |  |  | Zip verified |  | 2 | 0 |
| `R_INFO` | VARCHAR2(2000 CHAR) |  |  | Info |  | 2 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `OPROCESSING` | CHAR(1) |  |  | Online Processing |  | 1 | 1 |
| `DOCSTATUS` | CHAR(2) |  | yes | Document Status |  | 0 | 1 |
| `DOCACTION` | CHAR(2) |  | yes | Document Action |  | 0 | 1 |
| `ISRECONCILED` | CHAR(1) |  | yes | Reconciled |  | 0 | 1 |
| `ISALLOCATED` | CHAR(1) |  | yes | Allocated |  | 0 | 2 |
| `ISONLINE` | CHAR(1) |  | yes | Online Access |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `POSTED` | CHAR(1) |  | yes | Posted |  | 0 | 1 |
| `ISOVERUNDERPAYMENT` | CHAR(1) |  | yes | Over/Under Payment |  | 0 | 1 |
| `OVERUNDERAMT` | NUMBER |  |  | Over/Under Payment |  | 0 | 1 |
| `A_COUNTRY` | VARCHAR2(40 CHAR) |  |  | Account Country |  | 2 | 0 |
| `C_PROJECT_ID` | NUMBER(10,0) |  |  | Project | [C_PROJECT](../../data-model/c/c_project.md) | 2 | 0 |
| `ISSELFSERVICE` | CHAR(1) |  | yes | Self-Service |  | 0 | 1 |
| `CHARGEAMT` | NUMBER |  |  | Charge amount |  | 0 | 1 |
| `C_CHARGE_ID` | NUMBER(10,0) |  |  | Charge | [C_CHARGE](../../data-model/c/c_charge.md) | 2 | 0 |
| `ISDELAYEDCAPTURE` | CHAR(1) |  | yes | Delayed Capture |  | 0 | 1 |
| `R_AUTHCODE_DC` | VARCHAR2(20 CHAR) |  |  | Authorization Code (DC) |  | 2 | 0 |
| `R_CVV2MATCH` | CHAR(1) |  |  | CVV Match |  | 0 | 1 |
| `R_PNREF_DC` | VARCHAR2(20 CHAR) |  |  | Reference (DC) |  | 2 | 0 |
| `SWIPE` | VARCHAR2(80 CHAR) |  |  | Swipe |  | 2 | 0 |
| `AD_ORGTRX_ID` | NUMBER(10,0) |  |  | Trx Organization |  | 2 | 0 |
| `C_CAMPAIGN_ID` | NUMBER(10,0) |  |  | Campaign | [C_CAMPAIGN](../../data-model/c/c_campaign.md) | 2 | 0 |
| `C_ACTIVITY_ID` | NUMBER(10,0) |  |  | Activity | [C_ACTIVITY](../../data-model/c/c_activity.md) | 2 | 0 |
| `USER1_ID` | NUMBER(10,0) |  |  | User Element List 1 | [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | 2 | 0 |
| `USER2_ID` | NUMBER(10,0) |  |  | User Element List 2 | [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | 2 | 0 |
| `C_CONVERSIONTYPE_ID` | NUMBER(10,0) |  |  | Currency Type | [C_CONVERSIONTYPE](../../data-model/c/c_conversiontype.md) | 2 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 2 | 0 |
| `DATEACCT` | DATE |  | yes | Account Date |  | 0 | 1 |
| `C_ORDER_ID` | NUMBER(10,0) |  |  | Order | [C_ORDER](../../data-model/c/c_order.md) | 2 | 0 |
| `ISPREPAYMENT` | CHAR(1) |  | yes | Prepayment |  | 0 | 1 |
| `REF_PAYMENT_ID` | NUMBER(10,0) |  |  | Referenced Payment | [C_PAYMENT](../../data-model/c/c_payment.md) | 2 | 0 |
| `REVERSAL_ID` | NUMBER(10,0) |  |  | Reversal ID | [C_PAYMENT](../../data-model/c/c_payment.md) | 2 | 0 |
| `C_CASHBOOK_ID` | NUMBER(10,0) |  |  | Cash Book | [C_CASHBOOK](../../data-model/c/c_cashbook.md) | 2 | 0 |
| `PROCESSEDON` | NUMBER |  |  | Processed On |  | 0 | 2 |
| `C_PAYMENT_UU` | VARCHAR2(36 CHAR) |  |  | C_Payment_UU |  | 0 | 2 |
| `C_POSTENDERTYPE_ID` | NUMBER(10,0) |  |  | POS Tender Type | [C_POSTENDERTYPE](../../data-model/c/c_postendertype.md) | 2 | 0 |
| `C_PAYMENTPROCESSOR_ID` | NUMBER(10,0) |  |  | Payment Processor | [C_PAYMENTPROCESSOR](../../data-model/c/c_paymentprocessor.md) | 2 | 0 |
| `CUSTOMERPAYMENTPROFILEID` | VARCHAR2(60 CHAR) |  |  | Customer Payment Profile ID |  | 2 | 0 |
| `CUSTOMERPROFILEID` | VARCHAR2(60 CHAR) |  |  | Customer Profile ID |  | 2 | 0 |
| `CUSTOMERADDRESSID` | VARCHAR2(60 CHAR) |  |  | Customer Address ID |  | 2 | 0 |
| `ISVOIDED` | CHAR(1) |  | yes | Voided |  | 0 | 1 |
| `R_VOIDMSG` | VARCHAR2(255 CHAR) |  |  | Void Message |  | 2 | 0 |
| `C_DEPOSITBATCH_ID` | NUMBER(10,0) |  |  | Deposit Batch | [C_DEPOSITBATCH](../../data-model/c/c_depositbatch.md) | 2 | 0 |
| `IBAN` | VARCHAR2(40 CHAR) |  |  | IBAN |  | 2 | 0 |
| `SWIFTCODE` | VARCHAR2(20 CHAR) |  |  | Swift code |  | 2 | 0 |
| `CURRENCYRATE` | NUMBER |  |  | Rate |  | 2 | 0 |
| `CONVERTEDAMT` | NUMBER |  |  | Converted Amount |  | 2 | 0 |
| `ISOVERRIDECURRENCYRATE` | CHAR(1) |  | yes | Override Currency Conversion Rate |  | 0 | 1 |
| `C_BANKTRANSFER_ID` | NUMBER(10,0) |  |  | Bank Transfer | [C_BANKTRANSFER](../../data-model/c/c_banktransfer.md) | 2 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019744` | `IsVoided IN ('Y','N')` |
| `SYS_C0019745` | `Processed in ('Y','N')` |
| `SYS_C0019746` | `IsOnline in ('Y','N')` |
| `SYS_C0019747` | `IsOverrideCurrencyRate IN ('Y','N')` |
| `SYS_C0019748` | `IsActive in ('Y','N')` |
| `SYS_C0019750` | `IsAllocated in ('Y','N')` |
| `SYS_C0019751` | `IsReceipt in ('Y','N')` |
| `SYS_C0019752` | `IsApproved in ('Y','N')` |
| `SYS_C0019753` | `IsReconciled in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ORG](../../data-model/ad/ad_org.md) | C_PAYMENT.AD_ORGTRX_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [C_ACTIVITY](../../data-model/c/c_activity.md) | C_PAYMENT.C_ACTIVITY_ID → C_ACTIVITY.C_ACTIVITY_ID | NO ACTION |
| [C_BANKACCOUNT](../../data-model/c/c_bankaccount.md) | C_PAYMENT.C_BANKACCOUNT_ID → C_BANKACCOUNT.C_BANKACCOUNT_ID | NO ACTION |
| [C_BANKTRANSFER](../../data-model/c/c_banktransfer.md) | C_PAYMENT.C_BANKTRANSFER_ID → C_BANKTRANSFER.C_BANKTRANSFER_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_PAYMENT.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_BP_BANKACCOUNT](../../data-model/c/c_bp_bankaccount.md) | C_PAYMENT.C_BP_BANKACCOUNT_ID → C_BP_BANKACCOUNT.C_BP_BANKACCOUNT_ID | SET NULL |
| [C_CAMPAIGN](../../data-model/c/c_campaign.md) | C_PAYMENT.C_CAMPAIGN_ID → C_CAMPAIGN.C_CAMPAIGN_ID | NO ACTION |
| [C_CASHBOOK](../../data-model/c/c_cashbook.md) | C_PAYMENT.C_CASHBOOK_ID → C_CASHBOOK.C_CASHBOOK_ID | NO ACTION |
| [C_CHARGE](../../data-model/c/c_charge.md) | C_PAYMENT.C_CHARGE_ID → C_CHARGE.C_CHARGE_ID | NO ACTION |
| [C_CONVERSIONTYPE](../../data-model/c/c_conversiontype.md) | C_PAYMENT.C_CONVERSIONTYPE_ID → C_CONVERSIONTYPE.C_CONVERSIONTYPE_ID | NO ACTION |
| [C_CURRENCY](../../data-model/c/c_currency.md) | C_PAYMENT.C_CURRENCY_ID → C_CURRENCY.C_CURRENCY_ID | NO ACTION |
| [C_DEPOSITBATCH](../../data-model/c/c_depositbatch.md) | C_PAYMENT.C_DEPOSITBATCH_ID → C_DEPOSITBATCH.C_DEPOSITBATCH_ID | NO ACTION |
| [C_DOCTYPE](../../data-model/c/c_doctype.md) | C_PAYMENT.C_DOCTYPE_ID → C_DOCTYPE.C_DOCTYPE_ID | NO ACTION |
| [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | C_PAYMENT.USER1_ID → C_ELEMENTVALUE.C_ELEMENTVALUE_ID | NO ACTION |
| [C_INVOICE](../../data-model/c/c_invoice.md) | C_PAYMENT.C_INVOICE_ID → C_INVOICE.C_INVOICE_ID | NO ACTION |
| [C_ORDER](../../data-model/c/c_order.md) | C_PAYMENT.C_ORDER_ID → C_ORDER.C_ORDER_ID | NO ACTION |
| [C_PAYMENT](../../data-model/c/c_payment.md) | C_PAYMENT.REF_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_PAYMENTBATCH](../../data-model/c/c_paymentbatch.md) | C_PAYMENT.C_PAYMENTBATCH_ID → C_PAYMENTBATCH.C_PAYMENTBATCH_ID | NO ACTION |
| [C_PAYMENTPROCESSOR](../../data-model/c/c_paymentprocessor.md) | C_PAYMENT.C_PAYMENTPROCESSOR_ID → C_PAYMENTPROCESSOR.C_PAYMENTPROCESSOR_ID | NO ACTION |
| [C_POSTENDERTYPE](../../data-model/c/c_postendertype.md) | C_PAYMENT.C_POSTENDERTYPE_ID → C_POSTENDERTYPE.C_POSTENDERTYPE_ID | NO ACTION |
| [C_PROJECT](../../data-model/c/c_project.md) | C_PAYMENT.C_PROJECT_ID → C_PROJECT.C_PROJECT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [B_BUYERFUNDS](../../data-model/b/b_buyerfunds.md) | B_BUYERFUNDS.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [B_SELLERFUNDS](../../data-model/b/b_sellerfunds.md) | B_SELLERFUNDS.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_ALLOCATIONLINE](../../data-model/c/c_allocationline.md) | C_ALLOCATIONLINE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_BANKSTATEMENTLINE](../../data-model/c/c_bankstatementline.md) | C_BANKSTATEMENTLINE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_CASHLINE](../../data-model/c/c_cashline.md) | C_CASHLINE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_DEPOSITBATCHLINE](../../data-model/c/c_depositbatchline.md) | C_DEPOSITBATCHLINE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_DUNNINGRUNLINE](../../data-model/c/c_dunningrunline.md) | C_DUNNINGRUNLINE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | SET NULL |
| [C_INVOICE](../../data-model/c/c_invoice.md) | C_INVOICE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_ORDER](../../data-model/c/c_order.md) | C_ORDER.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_PAYMENT](../../data-model/c/c_payment.md) | C_PAYMENT.REF_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_PAYMENTALLOCATE](../../data-model/c/c_paymentallocate.md) | C_PAYMENTALLOCATE.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | CASCADE |
| [C_PAYMENTTRANSACTION](../../data-model/c/c_paymenttransaction.md) | C_PAYMENTTRANSACTION.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_PAYSELECTIONCHECK](../../data-model/c/c_payselectioncheck.md) | C_PAYSELECTIONCHECK.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_POSPAYMENT](../../data-model/c/c_pospayment.md) | C_POSPAYMENT.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_RECURRING](../../data-model/c/c_recurring.md) | C_RECURRING.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [C_RECURRING_RUN](../../data-model/c/c_recurring_run.md) | C_RECURRING_RUN.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| `I_BANKSTATEMENT` | I_BANKSTATEMENT.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | SET NULL |
| `I_PAYMENT` | I_PAYMENT.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | SET NULL |
| [R_REQUEST](../../data-model/r/r_request.md) | R_REQUEST.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |
| [R_REQUESTACTION](../../data-model/r/r_requestaction.md) | R_REQUESTACTION.C_PAYMENT_ID → C_PAYMENT.C_PAYMENT_ID | NO ACTION |

```mermaid
erDiagram
  AD_ORG ||--o{ C_PAYMENT : ""
  C_ACTIVITY ||--o{ C_PAYMENT : ""
  C_BANKACCOUNT ||--o{ C_PAYMENT : ""
  C_BANKTRANSFER ||--o{ C_PAYMENT : ""
  C_BPARTNER ||--o{ C_PAYMENT : ""
  C_BP_BANKACCOUNT ||--o{ C_PAYMENT : ""
  C_CAMPAIGN ||--o{ C_PAYMENT : ""
  C_CASHBOOK ||--o{ C_PAYMENT : ""
  C_CHARGE ||--o{ C_PAYMENT : ""
  C_CONVERSIONTYPE ||--o{ C_PAYMENT : ""
  C_CURRENCY ||--o{ C_PAYMENT : ""
  C_DEPOSITBATCH ||--o{ C_PAYMENT : ""
  C_DOCTYPE ||--o{ C_PAYMENT : ""
  C_ELEMENTVALUE ||--o{ C_PAYMENT : ""
  C_INVOICE ||--o{ C_PAYMENT : ""
  C_ORDER ||--o{ C_PAYMENT : ""
  C_PAYMENT ||--o{ B_BUYERFUNDS : ""
  C_PAYMENT ||--o{ B_SELLERFUNDS : ""
  C_PAYMENT ||--o{ C_ALLOCATIONLINE : ""
  C_PAYMENT ||--o{ C_BANKSTATEMENTLINE : ""
  C_PAYMENT ||--o{ C_CASHLINE : ""
  C_PAYMENT ||--o{ C_DEPOSITBATCHLINE : ""
  C_PAYMENT ||--o{ C_DUNNINGRUNLINE : ""
  C_PAYMENT ||--o{ C_INVOICE : ""
  C_PAYMENT ||--o{ C_ORDER : ""
  C_PAYMENT ||--o{ C_PAYMENT : ""
  C_PAYMENT ||--o{ C_PAYMENTALLOCATE : ""
  C_PAYMENT ||--o{ C_PAYMENTTRANSACTION : ""
  C_PAYMENT ||--o{ C_PAYSELECTIONCHECK : ""
  C_PAYMENT ||--o{ C_POSPAYMENT : ""
  C_PAYMENTBATCH ||--o{ C_PAYMENT : ""
  C_PAYMENTPROCESSOR ||--o{ C_PAYMENT : ""
```

8 more neighbour(s) not drawn.

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 3 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [currencyConvertPayment](../../logic/currencyconvertpayment.md) |
| Procedure | [migr_fix_payment_cashline](../../logic/migr_fix_payment_cashline.md) |
| Procedure | [paymentAllocated](../../logic/paymentallocated.md) |
| Procedure | [paymentAvailable](../../logic/paymentavailable.md) |
| View | `C_DUNNING_LINE_V` |
| View | `C_DUNNING_LINE_VT` |
| View | `C_PAYMENT_V` |
| View | `C_PAYSELECTION_CHECK_V` |
| View | `C_PAYSELECTION_CHECK_VT` |
| View | `RV_PAYMENT` |
| View | `RV_UNPOSTED` |
| View | `RV_UNPROCESSED` |
| View | `c_dunning_line_v` |
| View | `c_dunning_line_vt` |
| View | `c_payment_v` |
| View | `c_payselection_check_v` |
| View | `c_payselection_check_vt` |
| View | `rv_payment` |
| View | `rv_unposted` |
| View | `rv_unprocessed` |

## Schema history

179 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-04-21T11:45 | iD13 | `add_column` | C_Employee_ID | IDEMPIERE-5598 |
| 2025-04-21T11:45 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2025-04-21T11:45 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2025-04-21T11:45 | iD13 | `add_column` | C_Employee_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-04-05T03:00 | iD10 | `add_column` | C_BankTransfer_ID | IDEMPIERE-5088 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.C_BPartner_ID.nullable` | unexplained |
| `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| `model_column_missing` | `columns.C_Department_ID` | unexplained |
| `model_column_missing` | `columns.C_Employee_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.c_payment.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
