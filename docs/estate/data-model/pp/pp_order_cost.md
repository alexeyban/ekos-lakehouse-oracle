---
title: "PP_ORDER_COST"
order: 10
ekos_generated: true
ekos_estate_version: 1
---

# PP_ORDER_COST

Area [PP](../../data-model/pp/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.eevolution.model.X_PP_Order_Cost`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_WORKFLOW_ID` | NUMBER(10,0) |  |  | Workflow | [AD_WORKFLOW](../../data-model/ad/ad_workflow.md) | 0 | 0 |
| `C_ACCTSCHEMA_ID` | NUMBER(10,0) |  | yes | Accounting Schema | [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | 0 | 0 |
| `COSTINGMETHOD` | CHAR(1) |  |  | Costing Method |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `CUMULATEDAMT` | NUMBER |  |  | Accumulated Amt |  | 0 | 0 |
| `CUMULATEDAMTPOST` | NUMBER |  |  | Cumulated Amt Post |  | 0 | 0 |
| `CUMULATEDQTY` | NUMBER |  |  | Accumulated Qty |  | 0 | 0 |
| `CUMULATEDQTYPOST` | NUMBER |  |  | Cumulated Qty Post |  | 0 | 0 |
| `CURRENTCOSTPRICE` | NUMBER |  |  | Current Cost Price |  | 0 | 0 |
| `CURRENTCOSTPRICELL` | NUMBER |  |  | Current Cost Price Lower Level |  | 0 | 0 |
| `CURRENTQTY` | NUMBER |  |  | Current Quantity |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `M_ATTRIBUTESETINSTANCE_ID` | NUMBER(10,0) |  |  | Attribute Set Instance | [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | 0 | 0 |
| `M_COSTELEMENT_ID` | NUMBER(10,0) |  |  | Cost Element | [M_COSTELEMENT](../../data-model/m/m_costelement.md) | 0 | 0 |
| `M_COSTTYPE_ID` | NUMBER(10,0) |  | yes | Cost Type | [M_COSTTYPE](../../data-model/m/m_costtype.md) | 0 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 0 |
| `PP_ORDER_COST_ID` | NUMBER(10,0) | PK | yes | Manufacturing Order Cost |  | 0 | 0 |
| `PP_ORDER_ID` | NUMBER(10,0) |  | yes | Manufacturing Order | [PP_ORDER](../../data-model/pp/pp_order.md) | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `PP_ORDER_COST_UU` | VARCHAR2(36 CHAR) |  |  | PP_Order_Cost_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021972` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_WORKFLOW](../../data-model/ad/ad_workflow.md) | PP_ORDER_COST.AD_WORKFLOW_ID → AD_WORKFLOW.AD_WORKFLOW_ID | NO ACTION |
| [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | PP_ORDER_COST.C_ACCTSCHEMA_ID → C_ACCTSCHEMA.C_ACCTSCHEMA_ID | NO ACTION |
| [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | PP_ORDER_COST.M_ATTRIBUTESETINSTANCE_ID → M_ATTRIBUTESETINSTANCE.M_ATTRIBUTESETINSTANCE_ID | NO ACTION |
| [M_COSTELEMENT](../../data-model/m/m_costelement.md) | PP_ORDER_COST.M_COSTELEMENT_ID → M_COSTELEMENT.M_COSTELEMENT_ID | NO ACTION |
| [M_COSTTYPE](../../data-model/m/m_costtype.md) | PP_ORDER_COST.M_COSTTYPE_ID → M_COSTTYPE.M_COSTTYPE_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | PP_ORDER_COST.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |
| [PP_ORDER](../../data-model/pp/pp_order.md) | PP_ORDER_COST.PP_ORDER_ID → PP_ORDER.PP_ORDER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_WORKFLOW ||--o{ PP_ORDER_COST : ""
  C_ACCTSCHEMA ||--o{ PP_ORDER_COST : ""
  M_ATTRIBUTESETINSTANCE ||--o{ PP_ORDER_COST : ""
  M_COSTELEMENT ||--o{ PP_ORDER_COST : ""
  M_COSTTYPE ||--o{ PP_ORDER_COST : ""
  M_PRODUCT ||--o{ PP_ORDER_COST : ""
  PP_ORDER ||--o{ PP_ORDER_COST : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

27 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.pp_order_cost.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
