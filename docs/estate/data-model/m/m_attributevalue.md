---
title: "M_ATTRIBUTEVALUE"
order: 9
ekos_generated: true
ekos_estate_version: 1
---

# M_ATTRIBUTEVALUE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 9 row(s) when profiled

Application model: `org.compiere.model.X_M_AttributeValue`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_ATTRIBUTEVALUE_ID` | NUMBER(10,0) | PK | yes | Attribute Value |  | 0 | 9 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 9 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 9 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `M_ATTRIBUTE_ID` | NUMBER(10,0) |  | yes | Attribute | [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | 0 | 3 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 9 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 9 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 9 | 0 |
| `M_ATTRIBUTEVALUE_UU` | VARCHAR2(36 CHAR) |  |  | M_AttributeValue_UU |  | 0 | 9 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021426` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | M_ATTRIBUTEVALUE.M_ATTRIBUTE_ID → M_ATTRIBUTE.M_ATTRIBUTE_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_ATTRIBUTEINSTANCE](../../data-model/m/m_attributeinstance.md) | M_ATTRIBUTEINSTANCE.M_ATTRIBUTEVALUE_ID → M_ATTRIBUTEVALUE.M_ATTRIBUTEVALUE_ID | NO ACTION |
| [M_ATTRIBUTEINSTANCELINE](../../data-model/m/m_attributeinstanceline.md) | M_ATTRIBUTEINSTANCELINE.M_ATTRIBUTEVALUE_ID → M_ATTRIBUTEVALUE.M_ATTRIBUTEVALUE_ID | NO ACTION |

```mermaid
erDiagram
  M_ATTRIBUTE ||--o{ M_ATTRIBUTEVALUE : ""
  M_ATTRIBUTEVALUE ||--o{ M_ATTRIBUTEINSTANCE : ""
  M_ATTRIBUTEVALUE ||--o{ M_ATTRIBUTEINSTANCELINE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

26 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-07-23T16:30 | iD13 | `add_column` | EntityType | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_column` | EntityType | IDEMPIERE-4224 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-03-10T17:42 | iD10 | `create_index` |  | IDEMPIERE-2494 |
| 2022-03-10T17:42 | iD10 | `create_index` |  | IDEMPIERE-2494 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.EntityType` | unexplained |

## Notes

<!-- ekos:manual id="table.m_attributevalue.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
