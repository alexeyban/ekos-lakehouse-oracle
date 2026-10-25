---
title: "PP_PRODUCT_BOMLINE"
order: 19
ekos_generated: true
ekos_estate_version: 1
---

# PP_PRODUCT_BOMLINE

Area [PP](../../data-model/pp/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 21 row(s) when profiled

Application model: `org.eevolution.model.X_PP_Product_BOMLine`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `FEATURE` | VARCHAR2(30 CHAR) |  |  | Feature |  | 21 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ASSAY` | NUMBER |  |  | Quantity Assay |  | 0 | 1 |
| `BACKFLUSHGROUP` | VARCHAR2(20 CHAR) |  |  | Backflush Group |  | 21 | 0 |
| `C_UOM_ID` | NUMBER(10,0) |  |  | UOM | [C_UOM](../../data-model/c/c_uom.md) | 0 | 4 |
| `COMPONENTTYPE` | CHAR(2) |  |  | Component Type |  | 0 | 3 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 21 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 21 | 0 |
| `FORECAST` | NUMBER |  |  | Forecast |  | 0 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 21 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `ISCRITICAL` | CHAR(1) |  |  | Is Critical Component |  | 0 | 2 |
| `ISQTYPERCENTAGE` | CHAR(1) |  |  | Is Qty Percentage |  | 0 | 2 |
| `ISSUEMETHOD` | CHAR(1) |  |  | Issue Method |  | 0 | 2 |
| `LEADTIMEOFFSET` | NUMBER(10,0) |  |  | Lead Time Offset |  | 0 | 1 |
| `LINE` | NUMBER(10,0) |  | yes | Line No |  | 0 | 4 |
| `M_ATTRIBUTESETINSTANCE_ID` | NUMBER(10,0) |  |  | Attribute Set Instance | [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | 21 | 0 |
| `M_CHANGENOTICE_ID` | NUMBER(10,0) |  |  | Change Notice | [M_CHANGENOTICE](../../data-model/m/m_changenotice.md) | 21 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 18 |
| `PP_PRODUCT_BOMLINE_ID` | NUMBER(10,0) | PK | yes | BOM Line |  | 0 | 21 |
| `PP_PRODUCT_BOM_ID` | NUMBER(10,0) |  | yes | BOM &amp; Formula | [PP_PRODUCT_BOM](../../data-model/pp/pp_product_bom.md) | 0 | 7 |
| `QTYBOM` | NUMBER |  |  | Quantity |  | 0 | 9 |
| `QTYBATCH` | NUMBER |  |  | Quantity in % |  | 0 | 3 |
| `SCRAP` | NUMBER |  |  | Scrap % |  | 0 | 3 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 21 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `VALIDFROM` | DATE |  |  | Valid from |  | 0 | 5 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `VALIDTO` | DATE |  |  | Valid to |  | 21 | 0 |
| `COSTALLOCATIONPERC` | NUMBER |  |  | Cost Allocation Percent |  | 0 | 1 |
| `PP_PRODUCT_BOMLINE_UU` | VARCHAR2(36 CHAR) |  |  | PP_Product_BOMLine_UU |  | 0 | 21 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021278` | `IsActive IN ('Y','N')` |
| `SYS_C0021280` | `IsCritical IN ('Y','N')` |
| `SYS_C0021282` | `IsQtyPercentage IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_UOM](../../data-model/c/c_uom.md) | PP_PRODUCT_BOMLINE.C_UOM_ID → C_UOM.C_UOM_ID | NO ACTION |
| [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | PP_PRODUCT_BOMLINE.M_ATTRIBUTESETINSTANCE_ID → M_ATTRIBUTESETINSTANCE.M_ATTRIBUTESETINSTANCE_ID | NO ACTION |
| [M_CHANGENOTICE](../../data-model/m/m_changenotice.md) | PP_PRODUCT_BOMLINE.M_CHANGENOTICE_ID → M_CHANGENOTICE.M_CHANGENOTICE_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | PP_PRODUCT_BOMLINE.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |
| [PP_PRODUCT_BOM](../../data-model/pp/pp_product_bom.md) | PP_PRODUCT_BOMLINE.PP_PRODUCT_BOM_ID → PP_PRODUCT_BOM.PP_PRODUCT_BOM_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [PP_PRODUCT_BOMLINE_TRL](../../data-model/pp/pp_product_bomline_trl.md) | PP_PRODUCT_BOMLINE_TRL.PP_PRODUCT_BOMLINE_ID → PP_PRODUCT_BOMLINE.PP_PRODUCT_BOMLINE_ID | NO ACTION |

```mermaid
erDiagram
  C_UOM ||--o{ PP_PRODUCT_BOMLINE : ""
  M_ATTRIBUTESETINSTANCE ||--o{ PP_PRODUCT_BOMLINE : ""
  M_CHANGENOTICE ||--o{ PP_PRODUCT_BOMLINE : ""
  M_PRODUCT ||--o{ PP_PRODUCT_BOMLINE : ""
  PP_PRODUCT_BOM ||--o{ PP_PRODUCT_BOMLINE : ""
  PP_PRODUCT_BOMLINE ||--o{ PP_PRODUCT_BOMLINE_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [Bomqtyonhand](../../logic/bomqtyonhand.md) |
| Procedure | [BomqtyonhandASI](../../logic/bomqtyonhandasi.md) |
| Procedure | [Bomqtyordered](../../logic/bomqtyordered.md) |
| Procedure | [BomqtyorderedASI](../../logic/bomqtyorderedasi.md) |
| Procedure | [Bomqtyreserved](../../logic/bomqtyreserved.md) |
| Procedure | [BomqtyreservedASI](../../logic/bomqtyreservedasi.md) |
| View | `C_INVOICE_LINETAX_V` |
| View | `C_INVOICE_LINETAX_VT` |
| View | `C_ORDER_LINETAX_V` |
| View | `C_ORDER_LINETAX_VT` |
| View | `M_INOUT_LINE_V` |
| View | `M_INOUT_LINE_VT` |
| View | `M_PRODUCT_BOM` |
| View | `PP_PRODUCT_BOMLINE_V` |
| View | `PP_PRODUCT_BOMLINE_VT` |
| View | `RV_M_PRODUCT_WHEREUSED_V` |
| View | `RV_PP_PRODUCT_BOMLINE` |
| View | `T_BOMLINE_COSTS` |
| View | `c_invoice_linetax_v` |
| View | `c_invoice_linetax_vt` |
| View | `c_order_linetax_v` |
| View | `c_order_linetax_vt` |
| View | `m_inout_line_v` |
| View | `m_inout_line_vt` |
| View | `m_product_bom` |
| View | `pp_product_bomline_v` |
| View | `pp_product_bomline_vt` |
| View | `rv_m_product_whereused_v` |
| View | `rv_pp_cost_bomline` |
| View | `rv_pp_product_bomline` |
| View | `t_bomline_costs` |

## Schema history

43 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-09-29T16:00 | i8.2z | `modify_column` | IssueMethod | IDEMPIERE-1250 |
| 2021-09-29T16:00 | i8.2z | `modify_column` | IssueMethod | IDEMPIERE-1250 |
| 2021-09-29T16:00 | i8.2z | `modify_column` | ValidFrom | IDEMPIERE-1250 |

## Notes

<!-- ekos:manual id="table.pp_product_bomline.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
