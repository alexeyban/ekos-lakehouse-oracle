---
title: "AD_TABLEATTRIBUTE"
order: 179
ekos_generated: true
ekos_estate_version: 1
---

# AD_TABLEATTRIBUTE

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_AD_TableAttribute`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  |  | Tenant |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  |  | Organization |  |  |  |
| `AD_Table_ID` | NUMERIC(10) |  |  | Table | [AD_TABLE](../../data-model/ad/ad_table.md) |  |  |
| `AD_TableAttribute_ID` | NUMERIC(10) | PK | yes | AD_TableAttribute_ID |  |  |  |
| `AD_TableAttribute_UU` | VARCHAR(36) |  |  | AD_TableAttribute_UU |  |  |  |
| `Created` | TIMESTAMP |  |  | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  |  | Created By |  |  |  |
| `IsActive` | CHAR(1) |  |  | Active |  |  |  |
| `M_Attribute_ID` | NUMERIC(10) |  |  | Attribute | [M_ATTRIBUTE](../../data-model/m/m_attribute.md) |  |  |
| `M_AttributeValue_ID` | NUMERIC(10) |  |  | Attribute Value | [M_ATTRIBUTEVALUE](../../data-model/m/m_attributevalue.md) |  |  |
| `Record_ID` | NUMERIC(10) |  |  | Record ID |  |  |  |
| `Updated` | TIMESTAMP |  |  | Updated |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  |  | Updated By |  |  |  |
| `Value` | VARCHAR(40) |  |  | Search Key |  |  |  |
| `ValueDate` | TIMESTAMP |  |  | Value Date |  |  |  |
| `ValueNumber` | NUMERIC |  |  | Value |  |  |  |

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

12 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-07-23T16:30 | iD13 | `create_table` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `modify_column` | Value | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `create_table` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `modify_column` | Value | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |
| 2024-07-23T16:30 | iD13 | `add_constraint` |  | IDEMPIERE-4224 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_tableattribute.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
