---
title: "M_DISCOUNTSCHEMABREAK"
order: 27
ekos_generated: true
ekos_estate_version: 1
---

# M_DISCOUNTSCHEMABREAK

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_M_DiscountSchemaBreak`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_DISCOUNTSCHEMABREAK_ID` | NUMBER(10,0) | PK | yes | Discount Schema Break |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `M_DISCOUNTSCHEMA_ID` | NUMBER(10,0) |  | yes | Discount Schema | [M_DISCOUNTSCHEMA](../../data-model/m/m_discountschema.md) | 0 | 1 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 1 |
| `BREAKVALUE` | NUMBER |  | yes | Break Value |  | 0 | 1 |
| `BREAKDISCOUNT` | NUMBER |  | yes | Break Discount % |  | 0 | 1 |
| `M_PRODUCT_CATEGORY_ID` | NUMBER(10,0) |  |  | Product Category | [M_PRODUCT_CATEGORY](../../data-model/m/m_product_category.md) | 1 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  |  | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 1 | 0 |
| `ISBPARTNERFLATDISCOUNT` | CHAR(1) |  | yes | B.Partner Flat Discount |  | 0 | 1 |
| `M_DISCOUNTSCHEMABREAK_UU` | VARCHAR2(36 CHAR) |  |  | M_DiscountSchemaBreak_UU |  | 0 | 1 |
| `FIXEDPRICE` | NUMBER |  |  | Fixed Price |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020080` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_DISCOUNTSCHEMA](../../data-model/m/m_discountschema.md) | M_DISCOUNTSCHEMABREAK.M_DISCOUNTSCHEMA_ID → M_DISCOUNTSCHEMA.M_DISCOUNTSCHEMA_ID | CASCADE |
| [M_PRODUCT](../../data-model/m/m_product.md) | M_DISCOUNTSCHEMABREAK.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |
| [M_PRODUCT_CATEGORY](../../data-model/m/m_product_category.md) | M_DISCOUNTSCHEMABREAK.M_PRODUCT_CATEGORY_ID → M_PRODUCT_CATEGORY.M_PRODUCT_CATEGORY_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  M_DISCOUNTSCHEMA ||--o{ M_DISCOUNTSCHEMABREAK : ""
  M_PRODUCT ||--o{ M_DISCOUNTSCHEMABREAK : ""
  M_PRODUCT_CATEGORY ||--o{ M_DISCOUNTSCHEMABREAK : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

13 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-04-28T03:37 | iD10 | `add_column` | FixedPrice | IDEMPIERE-5260 |
| 2022-04-28T03:37 | iD10 | `add_column` | FixedPrice | IDEMPIERE-5260 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_DISCOUNTSCHEMABREAK_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_discountschemabreak.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
