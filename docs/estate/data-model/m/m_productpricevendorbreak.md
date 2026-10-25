---
title: "M_PRODUCTPRICEVENDORBREAK"
order: 77
ekos_generated: true
ekos_estate_version: 1
---

# M_PRODUCTPRICEVENDORBREAK

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_ProductPriceVendorBreak`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `BREAKVALUE` | NUMBER |  | yes | Break Value |  | 0 | 0 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  |  | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `M_PRICELIST_VERSION_ID` | NUMBER(10,0) |  | yes | Price List Version | [M_PRICELIST_VERSION](../../data-model/m/m_pricelist_version.md) | 0 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 0 |
| `PRICELIMIT` | NUMBER |  | yes | Limit Price |  | 0 | 0 |
| `PRICELIST` | NUMBER |  | yes | List Price |  | 0 | 0 |
| `PRICESTD` | NUMBER |  | yes | Standard Price |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `M_PRODUCTPRICEVENDORBREAK_ID` | NUMBER(10,0) | PK | yes | Product Price Break |  | 0 | 0 |
| `M_PRODUCTPRICEVENDORBREAK_UU` | VARCHAR2(36 CHAR) |  |  | M_ProductPriceVendorBreak_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022007` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | M_PRODUCTPRICEVENDORBREAK.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [M_PRICELIST_VERSION](../../data-model/m/m_pricelist_version.md) | M_PRODUCTPRICEVENDORBREAK.M_PRICELIST_VERSION_ID → M_PRICELIST_VERSION.M_PRICELIST_VERSION_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | M_PRODUCTPRICEVENDORBREAK.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  C_BPARTNER ||--o{ M_PRODUCTPRICEVENDORBREAK : ""
  M_PRICELIST_VERSION ||--o{ M_PRODUCTPRICEVENDORBREAK : ""
  M_PRODUCT ||--o{ M_PRODUCTPRICEVENDORBREAK : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

28 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `create_index` |  | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_PRODUCTPRICEVENDORBREAK_UU | IDEMPIERE-3862 |
| 2015-05-27T12:38 | i2.1 | `create_index` |  | IDEMPIERE-2540 |
| 2015-05-27T12:38 | i2.1 | `create_index` |  | IDEMPIERE-2540 |
| 2015-03-25T12:55 | i2.1 | `modify_column` | C_BPartner_ID | IDEMPIERE-2540 |
| 2015-03-25T12:55 | i2.1 | `modify_column` | C_BPartner_ID | IDEMPIERE-2540 |
| 2015-03-25T12:55 | i2.1 | `drop_constraint` |  | IDEMPIERE-2540 |

## Notes

<!-- ekos:manual id="table.m_productpricevendorbreak.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
