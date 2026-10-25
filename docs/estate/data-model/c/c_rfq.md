---
title: "C_RFQ"
order: 156
ekos_generated: true
ekos_estate_version: 1
---

# C_RFQ

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_C_RfQ`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_RFQ_ID` | NUMBER(10,0) | PK | yes | RfQ |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 1 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 1 | 0 |
| `C_RFQ_TOPIC_ID` | NUMBER(10,0) |  | yes | RfQ Topic | [C_RFQ_TOPIC](../../data-model/c/c_rfq_topic.md) | 0 | 1 |
| `C_CURRENCY_ID` | NUMBER(10,0) |  | yes | Currency | [C_CURRENCY](../../data-model/c/c_currency.md) | 0 | 1 |
| `DATERESPONSE` | DATE |  | yes | Response Date |  | 0 | 1 |
| `ISRFQRESPONSEACCEPTED` | CHAR(1) |  | yes | Responses Accepted |  | 0 | 1 |
| `DATEWORKSTART` | DATE |  |  | Work Start |  | 0 | 1 |
| `DELIVERYDAYS` | NUMBER(10,0) |  |  | Delivery Days |  | 0 | 1 |
| `DATEWORKCOMPLETE` | DATE |  |  | Work Complete |  | 1 | 0 |
| `QUOTETYPE` | CHAR(1) |  | yes | RfQ Type |  | 0 | 1 |
| `ISQUOTETOTALAMT` | CHAR(1) |  | yes | Quote Total Amt |  | 0 | 1 |
| `ISQUOTEALLQTY` | CHAR(1) |  | yes | Quote All Quantities |  | 0 | 1 |
| `ISSELFSERVICE` | CHAR(1) |  | yes | Self-Service |  | 0 | 1 |
| `ISINVITEDVENDORSONLY` | CHAR(1) |  | yes | Invited Vendors Only |  | 0 | 1 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  |  | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 1 | 0 |
| `C_BPARTNER_LOCATION_ID` | NUMBER(10,0) |  |  | Partner Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 1 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 1 | 0 |
| `SALESREP_ID` | NUMBER(10,0) |  | yes | Sales Representative | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 1 |
| `MARGIN` | NUMBER |  |  | Margin % |  | 0 | 1 |
| `CREATESO` | CHAR(1) |  |  | Create SO |  | 0 | 1 |
| `CREATEPO` | CHAR(1) |  |  | Create PO |  | 0 | 1 |
| `PUBLISHRFQ` | CHAR(1) |  |  | Publish RfQ |  | 0 | 1 |
| `C_ORDER_ID` | NUMBER(10,0) |  |  | Order | [C_ORDER](../../data-model/c/c_order.md) | 1 | 0 |
| `COPYLINES` | CHAR(1) |  |  | Copy Lines |  | 0 | 1 |
| `RANKRFQ` | CHAR(1) |  |  | Rank RfQ |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  | yes | Document No |  | 0 | 1 |
| `C_RFQ_UU` | VARCHAR2(36 CHAR) |  |  | C_RfQ_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019548` | `IsSelfService in ('Y','N')` |
| `SYS_C0019551` | `IsActive in ('Y','N')` |
| `SYS_C0019552` | `Processed in ('Y','N')` |
| `SYS_C0019553` | `IsInvitedVendorsOnly in ('Y','N')` |
| `SYS_C0019554` | `IsQuoteTotalAmt in ('Y','N')` |
| `SYS_C0019555` | `IsQuoteAllQty in ('Y','N')` |
| `SYS_C0019556` | `IsRfQResponseAccepted in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | C_RFQ.SALESREP_ID → AD_USER.AD_USER_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_RFQ.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | C_RFQ.C_BPARTNER_LOCATION_ID → C_BPARTNER_LOCATION.C_BPARTNER_LOCATION_ID | NO ACTION |
| [C_CURRENCY](../../data-model/c/c_currency.md) | C_RFQ.C_CURRENCY_ID → C_CURRENCY.C_CURRENCY_ID | NO ACTION |
| [C_ORDER](../../data-model/c/c_order.md) | C_RFQ.C_ORDER_ID → C_ORDER.C_ORDER_ID | NO ACTION |
| [C_RFQ_TOPIC](../../data-model/c/c_rfq_topic.md) | C_RFQ.C_RFQ_TOPIC_ID → C_RFQ_TOPIC.C_RFQ_TOPIC_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_RFQLINE](../../data-model/c/c_rfqline.md) | C_RFQLINE.C_RFQ_ID → C_RFQ.C_RFQ_ID | CASCADE |
| [C_RFQRESPONSE](../../data-model/c/c_rfqresponse.md) | C_RFQRESPONSE.C_RFQ_ID → C_RFQ.C_RFQ_ID | CASCADE |

```mermaid
erDiagram
  AD_USER ||--o{ C_RFQ : ""
  C_BPARTNER ||--o{ C_RFQ : ""
  C_BPARTNER_LOCATION ||--o{ C_RFQ : ""
  C_CURRENCY ||--o{ C_RFQ : ""
  C_ORDER ||--o{ C_RFQ : ""
  C_RFQ ||--o{ C_RFQLINE : ""
  C_RFQ ||--o{ C_RFQRESPONSE : ""
  C_RFQ_TOPIC ||--o{ C_RFQ : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| View | `C_RFQRESPONSE_V` |
| View | `C_RFQRESPONSE_VT` |
| View | `RV_C_RFQRESPONSE` |
| View | `RV_C_RFQ_UNANSWERED` |
| View | `c_rfqresponse_v` |
| View | `c_rfqresponse_vt` |
| View | `rv_c_rfq_unanswered` |
| View | `rv_c_rfqresponse` |

## Schema history

35 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.c_rfq.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
