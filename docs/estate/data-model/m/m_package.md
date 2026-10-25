---
title: "M_PACKAGE"
order: 60
ekos_generated: true
ekos_estate_version: 1
---

# M_PACKAGE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_M_Package`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_PACKAGE_ID` | NUMBER(10,0) | PK | yes | Package |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 1 |
| `M_INOUT_ID` | NUMBER(10,0) |  | yes | Shipment/Receipt | [M_INOUT](../../data-model/m/m_inout.md) | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `M_SHIPPER_ID` | NUMBER(10,0) |  | yes | Shipper | [M_SHIPPER](../../data-model/m/m_shipper.md) | 0 | 1 |
| `TRACKINGINFO` | VARCHAR2(255 CHAR) |  |  | Tracking Info |  | 1 | 0 |
| `DATERECEIVED` | DATE |  |  | Date Received |  | 1 | 0 |
| `RECEIVEDINFO` | VARCHAR2(255 CHAR) |  |  | Info Received |  | 1 | 0 |
| `SHIPDATE` | DATE |  |  | Ship Date |  | 1 | 0 |
| `M_PACKAGE_UU` | VARCHAR2(36 CHAR) |  |  | M_Package_UU |  | 0 | 1 |
| `BOXCOUNT` | NUMBER(10,0) |  |  | Box Count |  | 0 | 1 |
| `CASHONDELIVERY` | CHAR(1) |  | yes | COD |  | 0 | 1 |
| `C_BPARTNER_LOCATION_ID` | NUMBER(10,0) |  |  | Partner Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 1 | 0 |
| `C_CURRENCY_ID` | NUMBER(10,0) |  |  | Currency | [C_CURRENCY](../../data-model/c/c_currency.md) | 1 | 0 |
| `C_UOM_LENGTH_ID` | NUMBER(10,0) |  |  | UOM for Length | [C_UOM](../../data-model/c/c_uom.md) | 1 | 0 |
| `C_UOM_WEIGHT_ID` | NUMBER(10,0) |  |  | UOM for Weight | [C_UOM](../../data-model/c/c_uom.md) | 1 | 0 |
| `DELIVERYCONFIRMATION` | CHAR(1) |  | yes | Delivery Confirmation |  | 0 | 1 |
| `DOTHAZARDCLASSORDIVISION` | VARCHAR2(30 CHAR) |  |  | Dot Hazard Class or Division |  | 1 | 0 |
| `HANDLINGCHARGE` | NUMBER |  |  | Handling Charge |  | 1 | 0 |
| `HEIGHT` | NUMBER |  |  | Height |  | 1 | 0 |
| `HOMEDELIVERYPREMIUMDATE` | DATE |  |  | Date |  | 1 | 0 |
| `HOMEDELIVERYPREMIUMTYPE` | VARCHAR2(30 CHAR) |  |  | Home Delivery Premium Type |  | 1 | 0 |
| `INSUREDAMOUNT` | NUMBER |  |  | Insured Amount |  | 1 | 0 |
| `ISACCESSIBLE` | CHAR(1) |  | yes | Accessible |  | 0 | 1 |
| `ISCARGOAIRCRAFTONLY` | CHAR(1) |  | yes | Cargo Aircraft Only |  | 0 | 1 |
| `ISDRYICE` | CHAR(1) |  | yes | Dry Ice |  | 0 | 1 |
| `ISDUTIABLE` | CHAR(1) |  | yes | Dutiable |  | 0 | 1 |
| `ISFUTUREDAYSHIPMENT` | CHAR(1) |  | yes | Future Day Shipment |  | 0 | 1 |
| `ISHAZMAT` | CHAR(1) |  | yes | Hazardous Materials |  | 0 | 1 |
| `ISHOLDATLOCATION` | CHAR(1) |  | yes | Hold At Location |  | 0 | 1 |
| `ISIGNOREZIPNOTFOUND` | CHAR(1) |  | yes | Ignore Zip Not Found |  | 0 | 1 |
| `ISIGNOREZIPSTATENOTMATCH` | CHAR(1) |  | yes | Ignore Zip State Not Match |  | 0 | 1 |
| `ISRESIDENTIAL` | CHAR(1) |  | yes | Residential |  | 0 | 1 |
| `LABELPRINT` | CHAR(1) |  |  | Label Print |  | 1 | 0 |
| `LATESTPICKUPTIME` | DATE |  |  | Latest Pickup Time |  | 1 | 0 |
| `LENGTH` | NUMBER |  |  | Length |  | 1 | 0 |
| `NOTIFICATIONTYPE` | VARCHAR2(2 CHAR) |  |  | Notification Type |  | 1 | 0 |
| `OPROCESSING` | CHAR(1) |  |  | Online Processing |  | 1 | 0 |
| `PRICE` | NUMBER |  |  | Price |  | 1 | 0 |
| `PRICEACTUAL` | NUMBER |  |  | Unit Price |  | 1 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `RATEINQUIRYMESSAGE` | VARCHAR2(2000 CHAR) |  |  | Rate Inquiry Message |  | 1 | 0 |
| `ISSATURDAYDELIVERY` | CHAR(1) |  | yes | Saturday Delivery |  | 0 | 1 |
| `ISSATURDAYPICKUP` | CHAR(1) |  | yes | Saturday Pickup |  | 0 | 1 |
| `SHIPPINGRATEINQUIRY` | CHAR(1) |  |  | Rate Inquiry |  | 1 | 0 |
| `SHIPPINGRESPMESSAGE` | VARCHAR2(2000 CHAR) |  |  | Response Message |  | 1 | 0 |
| `SURCHARGES` | NUMBER |  |  | Surcharges |  | 1 | 0 |
| `TRACKINGNO` | VARCHAR2(255 CHAR) |  |  | Tracking No |  | 1 | 0 |
| `VOIDIT` | CHAR(1) |  |  | Void It |  | 1 | 0 |
| `WEIGHT` | NUMBER |  |  | Weight |  | 1 | 0 |
| `WIDTH` | NUMBER |  |  | Width |  | 1 | 0 |
| `C_BP_SHIPPINGACCT_ID` | NUMBER(10,0) |  |  | Business Partner Shipping Account | [C_BP_SHIPPINGACCT](../../data-model/c/c_bp_shippingacct.md) | 1 | 0 |
| `DUTIESSHIPPERACCOUNT` | VARCHAR2(40 CHAR) |  |  | Duties Shipper Account |  | 1 | 0 |
| `M_SHIPPERLABELS_ID` | NUMBER(10,0) |  |  | Shipper Labels | [M_SHIPPERLABELS](../../data-model/m/m_shipperlabels.md) | 1 | 0 |
| `M_SHIPPERPACKAGING_ID` | NUMBER(10,0) |  |  | Shipper Packaging | [M_SHIPPERPACKAGING](../../data-model/m/m_shipperpackaging.md) | 1 | 0 |
| `M_SHIPPERPICKUPTYPES_ID` | NUMBER(10,0) |  |  | Shipper Pickup Types | [M_SHIPPERPICKUPTYPES](../../data-model/m/m_shipperpickuptypes.md) | 1 | 0 |
| `SHIPPERACCOUNT` | VARCHAR2(40 CHAR) |  |  | Shipper Account Number |  | 1 | 0 |
| `HOMEDELIVERYPREMIUMPHONE` | VARCHAR2(30 CHAR) |  |  | Phone Number |  | 1 | 0 |
| `DRYICEWEIGHT` | NUMBER |  |  | Dry Ice Weight |  | 1 | 0 |
| `NOTIFICATIONMESSAGE` | VARCHAR2(255 CHAR) |  |  | Notification Message |  | 1 | 0 |
| `ISVERBALCONFIRMATION` | CHAR(1) |  | yes | Verbal Confirmation |  | 0 | 1 |
| `ISADDEDHANDLING` | CHAR(1) |  | yes | Added Handling |  | 0 | 1 |
| `PAYMENTRULE` | CHAR(1) |  |  | Payment Rule |  | 1 | 0 |
| `DELIVERYCONFIRMATIONTYPE` | VARCHAR2(30 CHAR) |  |  | Delivery Confirmation Type |  | 1 | 0 |
| `HOLDADDRESS_ID` | NUMBER(10,0) |  |  | Hold Address | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 1 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019822` | `CashOnDelivery IN ('Y','N')` |
| `SYS_C0019824` | `IsFutureDayShipment IN ('Y','N')` |
| `SYS_C0019825` | `IsIgnoreZipStateNotMatch IN ('Y','N')` |
| `SYS_C0019826` | `IsAccessible IN ('Y','N')` |
| `SYS_C0019827` | `IsVerbalConfirmation IN ('Y','N')` |
| `SYS_C0019828` | `IsCargoAircraftOnly IN ('Y','N')` |
| `SYS_C0019829` | `IsSaturdayPickup IN ('Y','N')` |
| `SYS_C0019830` | `IsIgnoreZipNotFound IN ('Y','N')` |
| `SYS_C0019831` | `IsDryIce IN ('Y','N')` |
| `SYS_C0019832` | `Processed IN ('Y','N')` |
| `SYS_C0019834` | `IsHoldAtLocation IN ('Y','N')` |
| `SYS_C0019835` | `DeliveryConfirmation IN ('Y','N')` |
| `SYS_C0019836` | `IsHazMat IN ('Y','N')` |
| `SYS_C0019837` | `IsResidential IN ('Y','N')` |
| `SYS_C0019838` | `IsAddedHandling IN ('Y','N')` |
| `SYS_C0019839` | `IsSaturdayDelivery IN ('Y','N')` |
| `SYS_C0019840` | `IsDutiable IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | M_PACKAGE.C_BPARTNER_LOCATION_ID → C_BPARTNER_LOCATION.C_BPARTNER_LOCATION_ID | NO ACTION |
| [C_BP_SHIPPINGACCT](../../data-model/c/c_bp_shippingacct.md) | M_PACKAGE.C_BP_SHIPPINGACCT_ID → C_BP_SHIPPINGACCT.C_BP_SHIPPINGACCT_ID | NO ACTION |
| [C_CURRENCY](../../data-model/c/c_currency.md) | M_PACKAGE.C_CURRENCY_ID → C_CURRENCY.C_CURRENCY_ID | NO ACTION |
| [C_UOM](../../data-model/c/c_uom.md) | M_PACKAGE.C_UOM_LENGTH_ID → C_UOM.C_UOM_ID | NO ACTION |
| [M_INOUT](../../data-model/m/m_inout.md) | M_PACKAGE.M_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [M_SHIPPER](../../data-model/m/m_shipper.md) | M_PACKAGE.M_SHIPPER_ID → M_SHIPPER.M_SHIPPER_ID | NO ACTION |
| [M_SHIPPERLABELS](../../data-model/m/m_shipperlabels.md) | M_PACKAGE.M_SHIPPERLABELS_ID → M_SHIPPERLABELS.M_SHIPPERLABELS_ID | NO ACTION |
| [M_SHIPPERPACKAGING](../../data-model/m/m_shipperpackaging.md) | M_PACKAGE.M_SHIPPERPACKAGING_ID → M_SHIPPERPACKAGING.M_SHIPPERPACKAGING_ID | NO ACTION |
| [M_SHIPPERPICKUPTYPES](../../data-model/m/m_shipperpickuptypes.md) | M_PACKAGE.M_SHIPPERPICKUPTYPES_ID → M_SHIPPERPICKUPTYPES.M_SHIPPERPICKUPTYPES_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_PACKAGELINE](../../data-model/m/m_packageline.md) | M_PACKAGELINE.M_PACKAGE_ID → M_PACKAGE.M_PACKAGE_ID | NO ACTION |
| [M_PACKAGEMPS](../../data-model/m/m_packagemps.md) | M_PACKAGEMPS.M_PACKAGE_ID → M_PACKAGE.M_PACKAGE_ID | NO ACTION |
| [M_SHIPPINGTRANSACTION](../../data-model/m/m_shippingtransaction.md) | M_SHIPPINGTRANSACTION.M_PACKAGE_ID → M_PACKAGE.M_PACKAGE_ID | NO ACTION |

```mermaid
erDiagram
  C_BPARTNER_LOCATION ||--o{ M_PACKAGE : ""
  C_BP_SHIPPINGACCT ||--o{ M_PACKAGE : ""
  C_CURRENCY ||--o{ M_PACKAGE : ""
  C_UOM ||--o{ M_PACKAGE : ""
  M_INOUT ||--o{ M_PACKAGE : ""
  M_PACKAGE ||--o{ M_PACKAGELINE : ""
  M_PACKAGE ||--o{ M_PACKAGEMPS : ""
  M_PACKAGE ||--o{ M_SHIPPINGTRANSACTION : ""
  M_SHIPPER ||--o{ M_PACKAGE : ""
  M_SHIPPERLABELS ||--o{ M_PACKAGE : ""
  M_SHIPPERPACKAGING ||--o{ M_PACKAGE : ""
  M_SHIPPERPICKUPTYPES ||--o{ M_PACKAGE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| View | `M_PACKAGELINES_AVAIL_V` |
| View | `m_packagelines_avail_v` |

## Schema history

194 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_14_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_13_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_16_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_12_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DOCUMENTNO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_13_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_8_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_package.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
