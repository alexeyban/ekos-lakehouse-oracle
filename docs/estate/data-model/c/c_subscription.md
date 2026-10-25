---
title: "C_SUBSCRIPTION"
order: 172
ekos_generated: true
ekos_estate_version: 1
---

# C_SUBSCRIPTION

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_Subscription`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_SUBSCRIPTION_ID` | NUMBER(10,0) | PK | yes | Subscription |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  | yes | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 0 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  | yes | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 0 | 0 |
| `C_SUBSCRIPTIONTYPE_ID` | NUMBER(10,0) |  | yes | Subscription Type | [C_SUBSCRIPTIONTYPE](../../data-model/c/c_subscriptiontype.md) | 0 | 0 |
| `STARTDATE` | DATE |  | yes | Start Date |  | 0 | 0 |
| `PAIDUNTILDATE` | DATE |  | yes | Paid Until |  | 0 | 0 |
| `ISDUE` | CHAR(1) |  | yes | Due |  | 0 | 0 |
| `RENEWALDATE` | DATE |  | yes | Renewal Date |  | 0 | 0 |
| `C_SUBSCRIPTION_UU` | VARCHAR2(36 CHAR) |  |  | C_Subscription_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_SUBSCRIPTION.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_SUBSCRIPTIONTYPE](../../data-model/c/c_subscriptiontype.md) | C_SUBSCRIPTION.C_SUBSCRIPTIONTYPE_ID → C_SUBSCRIPTIONTYPE.C_SUBSCRIPTIONTYPE_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | C_SUBSCRIPTION.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_SUBSCRIPTION_DELIVERY](../../data-model/c/c_subscription_delivery.md) | C_SUBSCRIPTION_DELIVERY.C_SUBSCRIPTION_ID → C_SUBSCRIPTION.C_SUBSCRIPTION_ID | NO ACTION |

```mermaid
erDiagram
  C_BPARTNER ||--o{ C_SUBSCRIPTION : ""
  C_SUBSCRIPTION ||--o{ C_SUBSCRIPTION_DELIVERY : ""
  C_SUBSCRIPTIONTYPE ||--o{ C_SUBSCRIPTION : ""
  M_PRODUCT ||--o{ C_SUBSCRIPTION : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

16 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_SUBSCRIPTION_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_subscription.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
