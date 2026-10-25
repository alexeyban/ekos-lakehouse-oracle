---
title: "M_INOUT"
order: 39
ekos_generated: true
ekos_estate_version: 1
---

# M_INOUT

Shipment & Customer Returns, Receipts & Vendor Returns

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 9 row(s) when profiled

Application model: `org.compiere.model.X_M_InOut`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_INOUT_ID` | NUMBER(10,0) | PK | yes | Shipment/Receipt |  | 0 | 9 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 9 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 9 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `ISSOTRX` | CHAR(1) |  | yes | Sales Transaction |  | 0 | 2 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 9 |
| `DOCACTION` | CHAR(2) |  | yes | Document Action |  | 0 | 1 |
| `DOCSTATUS` | CHAR(2) |  | yes | Document Status |  | 0 | 1 |
| `POSTED` | CHAR(1) |  | yes | Posted |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `C_DOCTYPE_ID` | NUMBER(10,0) |  | yes | Document Type | [C_DOCTYPE](../../data-model/c/c_doctype.md) | 0 | 2 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 4 | 5 |
| `C_ORDER_ID` | NUMBER(10,0) |  |  | Order | [C_ORDER](../../data-model/c/c_order.md) | 2 | 7 |
| `DATEORDERED` | DATE |  |  | Date Ordered |  | 5 | 3 |
| `ISPRINTED` | CHAR(1) |  | yes | Printed |  | 0 | 1 |
| `MOVEMENTTYPE` | CHAR(2) |  | yes | Movement Type |  | 0 | 2 |
| `MOVEMENTDATE` | DATE |  | yes | Movement Date |  | 0 | 7 |
| `DATEACCT` | DATE |  | yes | Account Date |  | 0 | 7 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  | yes | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 6 |
| `C_BPARTNER_LOCATION_ID` | NUMBER(10,0) |  | yes | Partner Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 0 | 6 |
| `M_WAREHOUSE_ID` | NUMBER(10,0) |  | yes | Warehouse | [M_WAREHOUSE](../../data-model/m/m_warehouse.md) | 0 | 1 |
| `POREFERENCE` | VARCHAR2(20 CHAR) |  |  | Order Reference |  | 8 | 1 |
| `DELIVERYRULE` | CHAR(1) |  | yes | Delivery Rule |  | 0 | 1 |
| `FREIGHTCOSTRULE` | CHAR(1) |  | yes | Freight Cost Rule |  | 0 | 1 |
| `FREIGHTAMT` | NUMBER |  |  | Freight Amount |  | 0 | 1 |
| `DELIVERYVIARULE` | CHAR(1) |  | yes | Delivery Via |  | 0 | 1 |
| `M_SHIPPER_ID` | NUMBER(10,0) |  |  | Shipper | [M_SHIPPER](../../data-model/m/m_shipper.md) | 9 | 0 |
| `C_CHARGE_ID` | NUMBER(10,0) |  |  | Charge | [C_CHARGE](../../data-model/c/c_charge.md) | 9 | 0 |
| `CHARGEAMT` | NUMBER |  |  | Charge amount |  | 0 | 1 |
| `PRIORITYRULE` | CHAR(1) |  | yes | Priority |  | 0 | 1 |
| `DATEPRINTED` | DATE |  |  | Date Printed |  | 9 | 0 |
| `C_INVOICE_ID` | NUMBER(10,0) |  |  | Invoice | [C_INVOICE](../../data-model/c/c_invoice.md) | 9 | 0 |
| `CREATEFROM` | CHAR(1) |  |  | Create lines from |  | 4 | 1 |
| `GENERATETO` | CHAR(1) |  |  | Generate To |  | 4 | 1 |
| `SENDEMAIL` | CHAR(1) |  | yes | Send EMail |  | 0 | 1 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 6 | 1 |
| `SALESREP_ID` | NUMBER(10,0) |  |  | Sales Representative | [AD_USER](../../data-model/ad/ad_user.md) | 9 | 0 |
| `NOPACKAGES` | NUMBER(10,0) |  |  | No Packages |  | 9 | 0 |
| `PICKDATE` | DATE |  |  | Pick Date |  | 9 | 0 |
| `SHIPDATE` | DATE |  |  | Ship Date |  | 9 | 0 |
| `TRACKINGNO` | VARCHAR2(60 CHAR) |  |  | Tracking No |  | 9 | 0 |
| `AD_ORGTRX_ID` | NUMBER(10,0) |  |  | Trx Organization |  | 9 | 0 |
| `C_PROJECT_ID` | NUMBER(10,0) |  |  | Project | [C_PROJECT](../../data-model/c/c_project.md) | 9 | 0 |
| `C_CAMPAIGN_ID` | NUMBER(10,0) |  |  | Campaign | [C_CAMPAIGN](../../data-model/c/c_campaign.md) | 9 | 0 |
| `C_ACTIVITY_ID` | NUMBER(10,0) |  |  | Activity | [C_ACTIVITY](../../data-model/c/c_activity.md) | 9 | 0 |
| `USER1_ID` | NUMBER(10,0) |  |  | User Element List 1 | [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | 9 | 0 |
| `USER2_ID` | NUMBER(10,0) |  |  | User Element List 2 | [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | 9 | 0 |
| `DATERECEIVED` | DATE |  |  | Date Received |  | 9 | 0 |
| `ISINTRANSIT` | CHAR(1) |  | yes | In Transit |  | 0 | 1 |
| `REF_INOUT_ID` | NUMBER(10,0) |  |  | Referenced Shipment |  | 9 | 0 |
| `CREATECONFIRM` | CHAR(1) |  |  | Create Confirm |  | 9 | 0 |
| `CREATEPACKAGE` | CHAR(1) |  |  | Create Package |  | 9 | 0 |
| `ISAPPROVED` | CHAR(1) |  | yes | Approved |  | 0 | 1 |
| `ISINDISPUTE` | CHAR(1) |  | yes | In Dispute |  | 0 | 1 |
| `VOLUME` | NUMBER |  |  | Volume |  | 9 | 0 |
| `WEIGHT` | NUMBER |  |  | Weight |  | 9 | 0 |
| `M_RMA_ID` | NUMBER(10,0) |  |  | RMA | [M_RMA](../../data-model/m/m_rma.md) | 9 | 0 |
| `REVERSAL_ID` | NUMBER(10,0) |  |  | Reversal ID | [M_INOUT](../../data-model/m/m_inout.md) | 9 | 0 |
| `ISDROPSHIP` | CHAR(1) |  |  | Drop Shipment |  | 0 | 1 |
| `DROPSHIP_BPARTNER_ID` | NUMBER(10,0) |  |  | Drop Ship Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 9 | 0 |
| `DROPSHIP_LOCATION_ID` | NUMBER(10,0) |  |  | Drop Shipment Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 9 | 0 |
| `DROPSHIP_USER_ID` | NUMBER(10,0) |  |  | Drop Shipment Contact | [AD_USER](../../data-model/ad/ad_user.md) | 9 | 0 |
| `PROCESSEDON` | NUMBER |  |  | Processed On |  | 0 | 9 |
| `M_INOUT_UU` | VARCHAR2(36 CHAR) |  |  | M_InOut_UU |  | 0 | 9 |
| `FREIGHTCHARGES` | VARCHAR2(10 CHAR) |  |  | Freight Charges |  | 9 | 0 |
| `SHIPPERACCOUNT` | VARCHAR2(40 CHAR) |  |  | Shipper Account Number |  | 9 | 0 |
| `INSURANCE` | CHAR(1) |  |  | Insurance |  | 9 | 0 |
| `FOB` | VARCHAR2(10 CHAR) |  |  | Freight Terms |  | 9 | 0 |
| `ISALTERNATERETURNADDRESS` | CHAR(1) |  | yes | Alternate Return Address |  | 0 | 1 |
| `RETURNBPARTNER_ID` | NUMBER(10,0) |  |  | Return Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 9 | 0 |
| `RETURNLOCATION_ID` | NUMBER(10,0) |  |  | Return Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 9 | 0 |
| `RETURNUSER_ID` | NUMBER(10,0) |  |  | Return User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 9 | 0 |
| `CREATELINESFROM` | CHAR(1) |  |  | Create lines from |  | 9 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020789` | `CreateFrom in ('Y','N')` |
| `SYS_C0020790` | `IsAlternateReturnAddress IN ('Y','N')` |
| `SYS_C0020791` | `IsSOTrx in ('Y','N')` |
| `SYS_C0020793` | `Processed in ('Y','N')` |
| `SYS_C0020794` | `IsDropShip IN ('Y','N')` |
| `SYS_C0020795` | `IsPrinted in ('Y','N')` |
| `SYS_C0020797` | `GenerateTo in ('Y','N')` |
| `SYS_C0020798` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ORG](../../data-model/ad/ad_org.md) | M_INOUT.AD_ORGTRX_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | M_INOUT.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [C_ACTIVITY](../../data-model/c/c_activity.md) | M_INOUT.C_ACTIVITY_ID → C_ACTIVITY.C_ACTIVITY_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | M_INOUT.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | M_INOUT.DROPSHIP_LOCATION_ID → C_BPARTNER_LOCATION.C_BPARTNER_LOCATION_ID | NO ACTION |
| [C_CAMPAIGN](../../data-model/c/c_campaign.md) | M_INOUT.C_CAMPAIGN_ID → C_CAMPAIGN.C_CAMPAIGN_ID | NO ACTION |
| [C_CHARGE](../../data-model/c/c_charge.md) | M_INOUT.C_CHARGE_ID → C_CHARGE.C_CHARGE_ID | NO ACTION |
| [C_DOCTYPE](../../data-model/c/c_doctype.md) | M_INOUT.C_DOCTYPE_ID → C_DOCTYPE.C_DOCTYPE_ID | NO ACTION |
| [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | M_INOUT.USER1_ID → C_ELEMENTVALUE.C_ELEMENTVALUE_ID | NO ACTION |
| [C_INVOICE](../../data-model/c/c_invoice.md) | M_INOUT.C_INVOICE_ID → C_INVOICE.C_INVOICE_ID | NO ACTION |
| [C_ORDER](../../data-model/c/c_order.md) | M_INOUT.C_ORDER_ID → C_ORDER.C_ORDER_ID | NO ACTION |
| [C_PROJECT](../../data-model/c/c_project.md) | M_INOUT.C_PROJECT_ID → C_PROJECT.C_PROJECT_ID | NO ACTION |
| [M_INOUT](../../data-model/m/m_inout.md) | M_INOUT.REF_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [M_RMA](../../data-model/m/m_rma.md) | M_INOUT.M_RMA_ID → M_RMA.M_RMA_ID | NO ACTION |
| [M_SHIPPER](../../data-model/m/m_shipper.md) | M_INOUT.M_SHIPPER_ID → M_SHIPPER.M_SHIPPER_ID | NO ACTION |
| [M_WAREHOUSE](../../data-model/m/m_warehouse.md) | M_INOUT.M_WAREHOUSE_ID → M_WAREHOUSE.M_WAREHOUSE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_LANDEDCOST](../../data-model/c/c_landedcost.md) | C_LANDEDCOST.M_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [M_INOUT](../../data-model/m/m_inout.md) | M_INOUT.REF_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [M_INOUTCONFIRM](../../data-model/m/m_inoutconfirm.md) | M_INOUTCONFIRM.M_INOUT_ID → M_INOUT.M_INOUT_ID | CASCADE |
| [M_INOUTLINE](../../data-model/m/m_inoutline.md) | M_INOUTLINE.M_INOUT_ID → M_INOUT.M_INOUT_ID | CASCADE |
| [M_PACKAGE](../../data-model/m/m_package.md) | M_PACKAGE.M_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [M_RMA](../../data-model/m/m_rma.md) | M_RMA.INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [M_SHIPPINGTRANSACTION](../../data-model/m/m_shippingtransaction.md) | M_SHIPPINGTRANSACTION.M_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [R_REQUEST](../../data-model/r/r_request.md) | R_REQUEST.M_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |
| [R_REQUESTACTION](../../data-model/r/r_requestaction.md) | R_REQUESTACTION.M_INOUT_ID → M_INOUT.M_INOUT_ID | NO ACTION |

```mermaid
erDiagram
  AD_ORG ||--o{ M_INOUT : ""
  AD_USER ||--o{ M_INOUT : ""
  C_ACTIVITY ||--o{ M_INOUT : ""
  C_BPARTNER ||--o{ M_INOUT : ""
  C_BPARTNER_LOCATION ||--o{ M_INOUT : ""
  C_CAMPAIGN ||--o{ M_INOUT : ""
  C_CHARGE ||--o{ M_INOUT : ""
  C_DOCTYPE ||--o{ M_INOUT : ""
  C_ELEMENTVALUE ||--o{ M_INOUT : ""
  C_INVOICE ||--o{ M_INOUT : ""
  C_ORDER ||--o{ M_INOUT : ""
  C_PROJECT ||--o{ M_INOUT : ""
  M_INOUT ||--o{ C_LANDEDCOST : ""
  M_INOUT ||--o{ M_INOUT : ""
  M_INOUT ||--o{ M_INOUTCONFIRM : ""
  M_INOUT ||--o{ M_INOUTLINE : ""
  M_INOUT ||--o{ M_PACKAGE : ""
  M_INOUT ||--o{ M_RMA : ""
  M_INOUT ||--o{ M_SHIPPINGTRANSACTION : ""
  M_INOUT ||--o{ R_REQUEST : ""
  M_INOUT ||--o{ R_REQUESTACTION : ""
  M_RMA ||--o{ M_INOUT : ""
  M_SHIPPER ||--o{ M_INOUT : ""
  M_WAREHOUSE ||--o{ M_INOUT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| View | `C_INVOICE_CREATEFROM_V` |
| View | `M_INOUTCONFIRM_V` |
| View | `M_INOUTCONFIRM_VT` |
| View | `M_INOUTLINEMA_RETURNED` |
| View | `M_INOUT_CANDIDATE_V` |
| View | `M_INOUT_CREATEFROM_V` |
| View | `M_INOUT_HEADER_V` |
| View | `M_INOUT_HEADER_VT` |
| View | `M_RMA_CREATEFROM_V` |
| View | `RV_INOUTCONFIRM` |
| View | `RV_INOUTDETAILS` |
| View | `RV_INOUTLINECONFIRM` |
| View | `RV_UNPOSTED` |
| View | `RV_UNPROCESSED` |
| View | `c_invoice_createfrom_v` |
| View | `m_inout_candidate_v` |
| View | `m_inout_createfrom_v` |
| View | `m_inout_header_v` |
| View | `m_inout_header_vt` |
| View | `m_inoutconfirm_v` |
| View | `m_inoutconfirm_vt` |
| View | `m_inoutlinema_returned` |
| View | `m_rma_createfrom_v` |
| View | `rv_inoutconfirm` |
| View | `rv_inoutdetails` |
| View | `rv_inoutlineconfirm` |
| View | `rv_unposted` |
| View | `rv_unprocessed` |

## Schema history

112 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_CostCenter_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_column` | C_Department_ID | IDEMPIERE-5598 |
| 2024-05-14T13:59 | iD13 | `add_constraint` |  | IDEMPIERE-5598 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-09-01T14:50 | i9 | `add_column` | CreateLinesFrom | IDEMPIERE-5396 |
| 2022-09-01T14:50 | i9 | `add_column` | CreateLinesFrom | IDEMPIERE-5396 |
| 2022-06-29T09:40 | i9 | `create_index` |  | IDEMPIERE-4269 |
| 2022-06-29T09:40 | i9 | `create_index` |  | IDEMPIERE-4269 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| `model_column_missing` | `columns.C_Department_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.m_inout.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
