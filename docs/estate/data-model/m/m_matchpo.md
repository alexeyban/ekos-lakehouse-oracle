---
title: "M_MATCHPO"
order: 53
ekos_generated: true
ekos_estate_version: 1
---

# M_MATCHPO

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 37 row(s) when profiled

Application model: `org.compiere.model.X_M_MatchPO`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_MATCHPO_ID` | NUMBER(10,0) | PK | yes | Match PO |  | 0 | 37 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 7 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 7 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `C_ORDERLINE_ID` | NUMBER(10,0) |  | yes | Sales Order Line | [C_ORDERLINE](../../data-model/c/c_orderline.md) | 0 | 21 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  |  | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 19 |
| `M_INOUTLINE_ID` | NUMBER(10,0) |  |  | Shipment/Receipt Line | [M_INOUTLINE](../../data-model/m/m_inoutline.md) | 16 | 21 |
| `C_INVOICELINE_ID` | NUMBER(10,0) |  |  | Invoice Line | [C_INVOICELINE](../../data-model/c/c_invoiceline.md) | 19 | 18 |
| `DATETRX` | DATE |  | yes | Transaction Date |  | 0 | 6 |
| `QTY` | NUMBER |  | yes | Quantity |  | 0 | 8 |
| `PROCESSING` | CHAR(1) |  | yes | Process Now |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `POSTED` | CHAR(1) |  | yes | Posted |  | 0 | 1 |
| `DOCUMENTNO` | VARCHAR2(30 CHAR) |  |  | Document No |  | 0 | 37 |
| `DATEACCT` | DATE |  |  | Account Date |  | 0 | 7 |
| `M_ATTRIBUTESETINSTANCE_ID` | NUMBER(10,0) |  |  | Attribute Set Instance | [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | 35 | 1 |
| `PRICEMATCHDIFFERENCE` | NUMBER |  |  | Price Match Difference |  | 35 | 2 |
| `ISAPPROVED` | CHAR(1) |  |  | Approved |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 37 | 0 |
| `PROCESSEDON` | NUMBER |  |  | Processed On |  | 0 | 6 |
| `M_MATCHPO_UU` | VARCHAR2(36 CHAR) |  |  | M_MatchPO_UU |  | 0 | 37 |
| `REVERSAL_ID` | NUMBER(10,0) |  |  | Reversal ID | [M_MATCHPO](../../data-model/m/m_matchpo.md) | 37 | 0 |
| `REF_MATCHPO_ID` | NUMBER(10,0) |  |  | Referenced Match PO | [M_MATCHPO](../../data-model/m/m_matchpo.md) | 37 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021684` | `Processed in ('Y','N')` |
| `SYS_C0021685` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_INVOICELINE](../../data-model/c/c_invoiceline.md) | M_MATCHPO.C_INVOICELINE_ID → C_INVOICELINE.C_INVOICELINE_ID | NO ACTION |
| [C_ORDERLINE](../../data-model/c/c_orderline.md) | M_MATCHPO.C_ORDERLINE_ID → C_ORDERLINE.C_ORDERLINE_ID | NO ACTION |
| [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | M_MATCHPO.M_ATTRIBUTESETINSTANCE_ID → M_ATTRIBUTESETINSTANCE.M_ATTRIBUTESETINSTANCE_ID | NO ACTION |
| [M_INOUTLINE](../../data-model/m/m_inoutline.md) | M_MATCHPO.M_INOUTLINE_ID → M_INOUTLINE.M_INOUTLINE_ID | NO ACTION |
| [M_MATCHPO](../../data-model/m/m_matchpo.md) | M_MATCHPO.REF_MATCHPO_ID → M_MATCHPO.M_MATCHPO_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | M_MATCHPO.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_MATCHPO](../../data-model/m/m_matchpo.md) | M_MATCHPO.REF_MATCHPO_ID → M_MATCHPO.M_MATCHPO_ID | NO ACTION |

```mermaid
erDiagram
  C_INVOICELINE ||--o{ M_MATCHPO : ""
  C_ORDERLINE ||--o{ M_MATCHPO : ""
  M_ATTRIBUTESETINSTANCE ||--o{ M_MATCHPO : ""
  M_INOUTLINE ||--o{ M_MATCHPO : ""
  M_MATCHPO ||--o{ M_MATCHPO : ""
  M_PRODUCT ||--o{ M_MATCHPO : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 4 citation(s)

## Read by

| kind | name |
|---|---|
| View | `C_INVOICE_CREATEFROM_V` |
| View | `M_INOUT_CREATEFROM_V` |
| View | `RV_UNPOSTED` |
| View | `c_invoice_createfrom_v` |
| View | `m_inout_createfrom_v` |
| View | `rv_unposted` |

## Schema history

31 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_MATCHPO_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.DateAcct.nullable` | unexplained |
| `mandatory_but_nullable` | `columns.M_InOutLine_ID.nullable` | unexplained |
| `mandatory_but_nullable` | `columns.M_Product_ID.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.m_matchpo.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
