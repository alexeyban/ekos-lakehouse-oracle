---
title: "X_COMMODITYSHIPMENT"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# X_COMMODITYSHIPMENT

Area [X](../../data-model/x/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes |  |  |  |  |
| `CountryOfManufacture` | VARCHAR(10) |  | yes |  |  |  |  |
| `Created` | TIMESTAMP |  | yes |  |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `Description` | VARCHAR(255) |  |  |  |  |  |  |
| `ExportLicenseNum` | VARCHAR(30) |  |  |  |  |  |  |
| `HarmonizedCode` | VARCHAR(30) |  | yes |  |  |  |  |
| `IsActive` | CHAR(1) |  | yes |  |  |  |  |
| `M_Product_ID` | NUMERIC(10) |  |  |  |  |  |  |
| `Updated` | TIMESTAMP |  | yes |  |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes |  |  |  |  |
| `X_CommodityShipment_ID` | NUMERIC(10) | PK | yes |  |  |  |  |
| `X_CommodityShipment_UU` | VARCHAR(36) |  |  |  |  |  |  |

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

4 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2013-03-18T14:13 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2013-03-18T14:13 | i1.0a-i1.0b | `rename_table` |  | IDEMPIERE-764 |
| 2012-12-21T18:41 | i1.0a-i1.0b | `create_table` |  | TICKET-1001758 |
| 2012-12-21T18:41 | i1.0a-i1.0b | `create_table` |  | TICKET-1001758 |

## Notes

<!-- ekos:manual id="table.x_commodityshipment.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
