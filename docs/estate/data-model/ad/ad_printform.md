---
title: "AD_PRINTFORM"
order: 115
ekos_generated: true
ekos_estate_version: 1
---

# AD_PRINTFORM

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_AD_PrintForm`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PRINTFORM_ID` | NUMBER(10,0) | PK | yes | Print Form |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  |  | Tenant |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 2 | 0 |
| `INVOICE_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Invoice Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 0 | 2 |
| `ORDER_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Order Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 0 | 2 |
| `REMITTANCE_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Remittance Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 0 | 2 |
| `SHIPMENT_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Shipment Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 0 | 2 |
| `INVOICE_MAILTEXT_ID` | NUMBER(10,0) |  |  | Invoice Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `ORDER_MAILTEXT_ID` | NUMBER(10,0) |  |  | Order Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `REMITTANCE_MAILTEXT_ID` | NUMBER(10,0) |  |  | Remittance Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `SHIPMENT_MAILTEXT_ID` | NUMBER(10,0) |  |  | Shipment Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `PROJECT_MAILTEXT_ID` | NUMBER(10,0) |  |  | Project Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `PROJECT_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Project Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 1 | 1 |
| `MANUF_ORDER_MAILTEXT_ID` | NUMBER(10,0) |  |  | Manufacturing Order Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `MANUF_ORDER_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Manufacturing Order Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 1 | 1 |
| `DISTRIB_ORDER_MAILTEXT_ID` | NUMBER(10,0) |  |  | Distribution Order Mail Text | [R_MAILTEXT](../../data-model/r/r_mailtext.md) | 2 | 0 |
| `DISTRIB_ORDER_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Distribution Order Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 1 | 1 |
| `AD_PRINTFORM_UU` | VARCHAR2(36 CHAR) |  |  | AD_PrintForm_UU |  | 0 | 2 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020942` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_PRINTFORM.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | AD_PRINTFORM.INVOICE_PRINTFORMAT_ID → AD_PRINTFORMAT.AD_PRINTFORMAT_ID | NO ACTION |
| [R_MAILTEXT](../../data-model/r/r_mailtext.md) | AD_PRINTFORM.DISTRIB_ORDER_MAILTEXT_ID → R_MAILTEXT.R_MAILTEXT_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_PRINTFORM : ""
  AD_PRINTFORMAT ||--o{ AD_PRINTFORM : ""
  R_MAILTEXT ||--o{ AD_PRINTFORM : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

43 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.ad_printform.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
