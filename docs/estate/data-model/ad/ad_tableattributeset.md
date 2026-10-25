---
title: "AD_TABLEATTRIBUTESET"
order: 180
ekos_generated: true
ekos_estate_version: 1
---

# AD_TABLEATTRIBUTESET

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_AD_TableAttributeSet`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes | Tenant |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes | Organization |  |  |  |
| `AD_Table_ID` | NUMERIC(10) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) |  |  |
| `AD_TableAttributeSet_ID` | NUMERIC(10) | PK | yes | Table Attribute Set |  |  |  |
| `AD_TableAttributeSet_UU` | VARCHAR(36) |  |  | AD_TableAttributeSet_UU |  |  |  |
| `Created` | TIMESTAMP |  | yes | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes | Created By |  |  |  |
| `IsActive` | CHAR(1) |  | yes | Active |  |  |  |
| `M_AttributeSet_ID` | NUMERIC(10) |  | yes | Attribute Set | [M_ATTRIBUTESET](../../data-model/m/m_attributeset.md) |  |  |
| `Updated` | TIMESTAMP |  | yes | Updated |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes | Updated By |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
|  | `IsActive IN ('Y', 'N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Schema history

16 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-07-23T16:30 | iD13 | `create_index` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `create_index` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `create_table` |  | IDEMPIERE-4224 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_tableattributeset.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
