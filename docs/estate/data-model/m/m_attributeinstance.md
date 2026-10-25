---
title: "M_ATTRIBUTEINSTANCE"
order: 2
ekos_generated: true
ekos_estate_version: 1
---

# M_ATTRIBUTEINSTANCE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 5 row(s) when profiled

Application model: `org.compiere.model.X_M_AttributeInstance`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_ATTRIBUTESETINSTANCE_ID` | NUMBER(10,0) | PK | yes | Attribute Set Instance | [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | 0 | 3 |
| `M_ATTRIBUTE_ID` | NUMBER(10,0) | PK | yes | Attribute | [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 3 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 3 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `M_ATTRIBUTEVALUE_ID` | NUMBER(10,0) |  |  | Attribute Value | [M_ATTRIBUTEVALUE](../../data-model/m/m_attributevalue.md) | 0 | 4 |
| `VALUE` | VARCHAR2(255 CHAR) |  |  | Search Key |  | 0 | 4 |
| `VALUENUMBER` | NUMBER |  |  | Value |  | 5 | 0 |
| `M_ATTRIBUTEINSTANCE_UU` | VARCHAR2(36 CHAR) |  |  | M_AttributeInstance_UU |  | 0 | 5 |
| `VALUEDATE` | DATE |  |  | Value Date |  | 5 | 0 |
| `VALUEMULTIPLESELECTION` | VARCHAR2(255 CHAR) |  |  | Value Multiple Selection |  | 5 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021510` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | M_ATTRIBUTEINSTANCE.M_ATTRIBUTE_ID → M_ATTRIBUTE.M_ATTRIBUTE_ID | NO ACTION |
| [M_ATTRIBUTESETINSTANCE](../../data-model/m/m_attributesetinstance.md) | M_ATTRIBUTEINSTANCE.M_ATTRIBUTESETINSTANCE_ID → M_ATTRIBUTESETINSTANCE.M_ATTRIBUTESETINSTANCE_ID | CASCADE |
| [M_ATTRIBUTEVALUE](../../data-model/m/m_attributevalue.md) | M_ATTRIBUTEINSTANCE.M_ATTRIBUTEVALUE_ID → M_ATTRIBUTEVALUE.M_ATTRIBUTEVALUE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_ATTRIBUTEINSTANCELINE](../../data-model/m/m_attributeinstanceline.md) | M_ATTRIBUTEINSTANCELINE.M_ATTRIBUTEINSTANCE_UU → M_ATTRIBUTEINSTANCE.M_ATTRIBUTEINSTANCE_UU | CASCADE |

```mermaid
erDiagram
  M_ATTRIBUTE ||--o{ M_ATTRIBUTEINSTANCE : ""
  M_ATTRIBUTEINSTANCE ||--o{ M_ATTRIBUTEINSTANCELINE : ""
  M_ATTRIBUTESETINSTANCE ||--o{ M_ATTRIBUTEINSTANCE : ""
  M_ATTRIBUTEVALUE ||--o{ M_ATTRIBUTEINSTANCE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [ProductAttribute](../../logic/productattribute.md) |

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-02-26T15:06 | iD12 | `modify_column` | Value | IDEMPIERE-5859 |
| 2024-02-26T15:06 | iD12 | `modify_column` | Value | IDEMPIERE-5859 |
| 2024-02-26T10:25 | iD12 | `add_column` | ValueMultipleSelection | IDEMPIERE-5859 |
| 2024-02-26T10:25 | iD12 | `add_column` | ValueMultipleSelection | IDEMPIERE-5859 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_ATTRIBUTEINSTANCE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_attributeinstance.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
