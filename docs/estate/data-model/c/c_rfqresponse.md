---
title: "C_RFQRESPONSE"
order: 159
ekos_generated: true
ekos_estate_version: 1
---

# C_RFQRESPONSE

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_RfQResponse`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_RFQRESPONSE_ID` | NUMBER(10,0) | PK | yes | RfQ Response |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `C_RFQ_ID` | NUMBER(10,0) |  | yes | RfQ | [C_RFQ](../../data-model/c/c_rfq.md) | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  | yes | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 0 |
| `C_BPARTNER_LOCATION_ID` | NUMBER(10,0) |  | yes | Partner Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `C_CURRENCY_ID` | NUMBER(10,0) |  | yes | Currency | [C_CURRENCY](../../data-model/c/c_currency.md) | 0 | 0 |
| `DATEINVITED` | DATE |  |  | Invited |  | 0 | 0 |
| `DATERESPONSE` | DATE |  |  | Response Date |  | 0 | 0 |
| `DATEWORKSTART` | DATE |  |  | Work Start |  | 0 | 0 |
| `DELIVERYDAYS` | NUMBER(10,0) |  |  | Delivery Days |  | 0 | 0 |
| `DATEWORKCOMPLETE` | DATE |  |  | Work Complete |  | 0 | 0 |
| `PRICE` | NUMBER |  | yes | Price |  | 0 | 0 |
| `ISSELFSERVICE` | CHAR(1) |  | yes | Self-Service |  | 0 | 0 |
| `ISCOMPLETE` | CHAR(1) |  | yes | Complete |  | 0 | 0 |
| `ISSELECTEDWINNER` | CHAR(1) |  | yes | Selected Winner |  | 0 | 0 |
| `RANKING` | NUMBER(10,0) |  |  | Ranking |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `C_ORDER_ID` | NUMBER(10,0) |  |  | Order | [C_ORDER](../../data-model/c/c_order.md) | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `CHECKCOMPLETE` | CHAR(1) |  |  | Check Complete |  | 0 | 0 |
| `C_RFQRESPONSE_UU` | VARCHAR2(36 CHAR) |  |  | C_RfQResponse_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019810` | `Processed in ('Y','N')` |
| `SYS_C0019811` | `IsActive in ('Y','N')` |
| `SYS_C0019812` | `IsSelectedWinner in ('Y','N')` |
| `SYS_C0019814` | `IsComplete in ('Y','N')` |
| `SYS_C0019815` | `IsSelfService in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | C_RFQRESPONSE.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_RFQRESPONSE.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | C_RFQRESPONSE.C_BPARTNER_LOCATION_ID → C_BPARTNER_LOCATION.C_BPARTNER_LOCATION_ID | NO ACTION |
| [C_CURRENCY](../../data-model/c/c_currency.md) | C_RFQRESPONSE.C_CURRENCY_ID → C_CURRENCY.C_CURRENCY_ID | NO ACTION |
| [C_ORDER](../../data-model/c/c_order.md) | C_RFQRESPONSE.C_ORDER_ID → C_ORDER.C_ORDER_ID | NO ACTION |
| [C_RFQ](../../data-model/c/c_rfq.md) | C_RFQRESPONSE.C_RFQ_ID → C_RFQ.C_RFQ_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_RFQRESPONSELINE](../../data-model/c/c_rfqresponseline.md) | C_RFQRESPONSELINE.C_RFQRESPONSE_ID → C_RFQRESPONSE.C_RFQRESPONSE_ID | CASCADE |

```mermaid
erDiagram
  AD_USER ||--o{ C_RFQRESPONSE : ""
  C_BPARTNER ||--o{ C_RFQRESPONSE : ""
  C_BPARTNER_LOCATION ||--o{ C_RFQRESPONSE : ""
  C_CURRENCY ||--o{ C_RFQRESPONSE : ""
  C_ORDER ||--o{ C_RFQRESPONSE : ""
  C_RFQ ||--o{ C_RFQRESPONSE : ""
  C_RFQRESPONSE ||--o{ C_RFQRESPONSELINE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

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

28 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_rfqresponse.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
