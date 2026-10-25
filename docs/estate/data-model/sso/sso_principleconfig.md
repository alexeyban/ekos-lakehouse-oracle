---
title: "SSO_PRINCIPLECONFIG"
order: 2
ekos_generated: true
ekos_estate_version: 1
---

# SSO_PRINCIPLECONFIG

Area [SSO](../../data-model/sso/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  |  |  |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  |  |  |  |  |  |
| `Created` | TIMESTAMP |  |  |  |  |  |  |
| `CreatedBy` | NUMERIC(10) |  |  |  |  |  |  |
| `IsActive` | CHAR(1) |  |  |  |  |  |  |
| `Name` | VARCHAR(60) |  |  |  |  |  |  |
| `SSO_ApplicationClientID` | VARCHAR(100) |  | yes |  |  |  |  |
| `SSO_ApplicationLogoutURL` | VARCHAR(1000) |  |  |  |  |  |  |
| `SSO_ApplicationRedirectURIs` | VARCHAR(1000) |  |  |  |  |  |  |
| `SSO_ApplicationSecretKey` | VARCHAR(100) |  |  |  |  |  |  |
| `SSO_AuthorizationTenantID` | VARCHAR(100) |  | yes |  |  |  |  |
| `SSO_PrincipleConfig_ID` | NUMERIC(10) | PK | yes |  |  |  |  |
| `SSO_PrincipleConfig_UU` | VARCHAR(36) |  |  |  |  |  |  |
| `Updated` | TIMESTAMP |  |  |  |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  |  |  |  |  |  |

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

32 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-07-11T16:56 | iD11 | `rename_table` |  | IDEMPIERE-5346 |
| 2023-07-11T16:56 | iD11 | `rename_table` |  | IDEMPIERE-5346 |
| 2023-01-19T14:24 | iD11 | `add_column` | SSO_IDempMonitorRedirectURIs | IDEMPIERE-5346 |
| 2023-01-19T14:24 | iD11 | `add_column` | SSO_OSGIRedirectURIs | IDEMPIERE-5346 |
| 2023-01-19T14:24 | iD11 | `add_column` | SSO_OSGIRedirectURIs | IDEMPIERE-5346 |
| 2023-01-19T14:24 | iD11 | `add_column` | SSO_IDempMonitorRedirectURIs | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `add_column` | SSO_ApplicationDiscoveryURI | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `modify_column` | SSO_AuthorizationTenantID | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `modify_column` | SSO_ApplicationRedirectURIs | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `create_table` |  | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `modify_column` | SSO_PrincipleConfig_ID | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `modify_column` | SSO_ApplicationClientID | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `add_column` | IsDefault | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `add_column` | SSO_Provider | IDEMPIERE-5346 |
| 2022-09-12T18:00 | iD11 | `add_column` | SSO_ApplicationDomain | IDEMPIERE-5346 |

## Notes

<!-- ekos:manual id="table.sso_principleconfig.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
