---
title: "C_RFQLINEQTY"
order: 158
ekos_generated: true
ekos_estate_version: 1
---

# C_RFQLINEQTY

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_C_RfQLineQty`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_RFQLINEQTY_ID` | NUMBER(10,0) | PK | yes | RfQ Line Quantity |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `C_RFQLINE_ID` | NUMBER(10,0) |  | yes | RfQ Line | [C_RFQLINE](../../data-model/c/c_rfqline.md) | 0 | 2 |
| `C_UOM_ID` | NUMBER(10,0) |  | yes | UOM | [C_UOM](../../data-model/c/c_uom.md) | 0 | 1 |
| `QTY` | NUMBER |  | yes | Quantity |  | 0 | 2 |
| `MARGIN` | NUMBER |  |  | Margin % |  | 0 | 1 |
| `ISPURCHASEQTY` | CHAR(1) |  | yes | Purchase Quantity |  | 0 | 1 |
| `BESTRESPONSEAMT` | NUMBER |  |  | Best Response Amount |  | 0 | 1 |
| `ISOFFERQTY` | CHAR(1) |  | yes | Offer Quantity |  | 0 | 1 |
| `OFFERAMT` | NUMBER |  |  | Offer Amount |  | 0 | 1 |
| `BENCHMARKPRICE` | NUMBER |  | yes | Benchmark Price |  | 0 | 1 |
| `ISRFQQTY` | CHAR(1) |  | yes | RfQ Quantity |  | 0 | 1 |
| `C_RFQLINEQTY_UU` | VARCHAR2(36 CHAR) |  |  | C_RfQLineQty_UU |  | 0 | 2 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019599` | `IsActive in ('Y','N')` |
| `SYS_C0019600` | `IsOfferQty in ('Y','N')` |
| `SYS_C0019602` | `IsPurchaseQty in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_RFQLINE](../../data-model/c/c_rfqline.md) | C_RFQLINEQTY.C_RFQLINE_ID → C_RFQLINE.C_RFQLINE_ID | CASCADE |
| [C_UOM](../../data-model/c/c_uom.md) | C_RFQLINEQTY.C_UOM_ID → C_UOM.C_UOM_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_RFQRESPONSELINEQTY](../../data-model/c/c_rfqresponselineqty.md) | C_RFQRESPONSELINEQTY.C_RFQLINEQTY_ID → C_RFQLINEQTY.C_RFQLINEQTY_ID | CASCADE |

```mermaid
erDiagram
  C_RFQLINE ||--o{ C_RFQLINEQTY : ""
  C_RFQLINEQTY ||--o{ C_RFQRESPONSELINEQTY : ""
  C_UOM ||--o{ C_RFQLINEQTY : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Read by

| kind | name |
|---|---|
| View | `C_RFQRESPONSELINEQTY_V` |
| View | `C_RFQRESPONSELINEQTY_VT` |
| View | `C_RFQRESPONSELINE_V` |
| View | `C_RFQRESPONSELINE_VT` |
| View | `RV_C_RFQRESPONSE` |
| View | `c_rfqresponseline_v` |
| View | `c_rfqresponseline_vt` |
| View | `c_rfqresponselineqty_v` |
| View | `c_rfqresponselineqty_vt` |
| View | `rv_c_rfqresponse` |

## Schema history

9 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_RFQLINEQTY_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_rfqlineqty.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
