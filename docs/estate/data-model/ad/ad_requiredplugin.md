---
title: "AD_REQUIREDPLUGIN"
order: 154
ekos_generated: true
ekos_estate_version: 1
---

# AD_REQUIREDPLUGIN

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_AD_RequiredPlugin`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes | Tenant |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes | Organization |  |  |  |
| `AD_RequiredPlugin_UU` | VARCHAR(36) | PK | yes | AD_RequiredPlugin_UU |  |  |  |
| `Created` | TIMESTAMP |  | yes | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes | Created By |  |  |  |
| `IsActive` | CHAR(1) |  | yes | Active |  |  |  |
| `PluginExpectedState` | VARCHAR(20) |  |  | Expected State |  |  |  |
| `PluginName` | VARCHAR(1000) |  |  | Plugin Name |  |  |  |
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

24 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-04-14T14:28 | iD12 | `create_table` |  | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | EntityType | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | PluginName | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | PluginName | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | EntityType | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | PluginName | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `add_constraint` |  | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `add_constraint` |  | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `add_constraint` |  | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `add_constraint` |  | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | PluginName | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `add_column` | EntityType | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `add_constraint` |  | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | PluginName | IDEMPIERE-6471 |
| 2025-04-14T14:28 | iD12 | `modify_column` | PluginName | IDEMPIERE-6471 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_requiredplugin.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
