---
title: "M_ATTRIBUTEUSE"
order: 8
ekos_generated: true
ekos_estate_version: 1
---

# M_ATTRIBUTEUSE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 5 row(s) when profiled

Application model: `org.compiere.model.X_M_AttributeUse`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `M_ATTRIBUTE_ID` | NUMBER(10,0) | PK | yes | Attribute | [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | 0 | 4 |
| `M_ATTRIBUTESET_ID` | NUMBER(10,0) | PK | yes | Attribute Set | [M_ATTRIBUTESET](../../data-model/m/m_attributeset.md) | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 5 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 5 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 3 |
| `M_ATTRIBUTEUSE_UU` | VARCHAR2(36 CHAR) |  |  | M_AttributeUse_UU |  | 0 | 5 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0023075` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | M_ATTRIBUTEUSE.M_ATTRIBUTE_ID → M_ATTRIBUTE.M_ATTRIBUTE_ID | NO ACTION |
| [M_ATTRIBUTESET](../../data-model/m/m_attributeset.md) | M_ATTRIBUTEUSE.M_ATTRIBUTESET_ID → M_ATTRIBUTESET.M_ATTRIBUTESET_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  M_ATTRIBUTE ||--o{ M_ATTRIBUTEUSE : ""
  M_ATTRIBUTESET ||--o{ M_ATTRIBUTEUSE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

15 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_column` | EntityType | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_column` | EntityType | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_column` | DefaultValue | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_column` | DefaultValue | IDEMPIERE-4224 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_ATTRIBUTEUSE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.DefaultValue` | unexplained |
| `model_column_missing` | `columns.EntityType` | unexplained |

## Notes

<!-- ekos:manual id="table.m_attributeuse.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
