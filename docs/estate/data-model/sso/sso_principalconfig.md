---
title: "SSO_PRINCIPALCONFIG"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# SSO_PRINCIPALCONFIG

Area [SSO](../../data-model/sso/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_SSO_PrincipalConfig`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  |  | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  |  | Organization |  | 0 | 0 |
| `CREATED` | DATE |  |  | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  |  | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  |  | Active |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  |  | Name |  | 0 | 0 |
| `SSO_APPLICATIONCLIENTID` | VARCHAR2(100 CHAR) |  |  | Application Client ID |  | 0 | 0 |
| `SSO_APPLICATIONLOGOUTURL` | VARCHAR2(1000 CHAR) |  |  | Application Logout URL |  | 0 | 0 |
| `SSO_APPLICATIONREDIRECTURIS` | VARCHAR2(1000 CHAR) |  |  | Application Redirect URIs |  | 0 | 0 |
| `SSO_APPLICATIONSECRETKEY` | VARCHAR2(100 CHAR) |  |  | Application Secret Key |  | 0 | 0 |
| `SSO_AUTHORIZATIONTENANTID` | VARCHAR2(100 CHAR) |  |  | Tenant ID |  | 0 | 0 |
| `SSO_PRINCIPALCONFIG_ID` | NUMBER(10,0) | PK | yes | SSO Configuration |  | 0 | 0 |
| `SSO_PRINCIPALCONFIG_UU` | VARCHAR2(36 CHAR) |  |  | SSO Configuration UU |  | 0 | 0 |
| `UPDATED` | DATE |  |  | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  |  | Updated By |  | 0 | 0 |
| `ISDEFAULT` | CHAR(1) |  |  | Default |  | 0 | 0 |
| `SSO_PROVIDER` | VARCHAR2(22 CHAR) |  | yes | SSO Provider |  | 0 | 0 |
| `SSO_APPLICATIONDISCOVERYURI` | VARCHAR2(4000 CHAR) |  |  | Application Discovery URI |  | 0 | 0 |
| `SSO_IDEMPMONITORREDIRECTURIS` | VARCHAR2(1000 CHAR) |  |  | iDempiere Monitor Redirect URIs |  | 0 | 0 |
| `SSO_OSGIREDIRECTURIS` | VARCHAR2(1000 CHAR) |  |  | Felix Web Console Redirect URIs |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022496` | `IsActive IN ('Y','N')` |
| `SYS_C0022497` | `IsDefault IN ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-11-27T17:10 | iD12 | `add_column` | SSO_LoginButtonImage_ID | IDEMPIERE-6304 |
| 2024-11-27T17:10 | iD12 | `add_column` | SSO_LoginButtonImage_ID | IDEMPIERE-6304 |
| 2024-11-27T17:10 | iD12 | `add_constraint` |  | IDEMPIERE-6304 |
| 2024-11-27T17:10 | iD12 | `add_constraint` |  | IDEMPIERE-6304 |
| 2023-12-22T12:38 | iD11 | `drop_constraint` |  | IDEMPIERE-5346 |
| 2023-12-22T12:38 | iD11 | `add_constraint` |  | IDEMPIERE-5346 |
| 2023-12-22T12:38 | iD11 | `add_constraint` |  | IDEMPIERE-5346 |
| 2023-12-22T12:38 | iD11 | `drop_constraint` |  | IDEMPIERE-5346 |
| 2023-07-27T16:40 | iD11 | `drop_column` | SSO_ApplicationDomain | IDEMPIERE-5346 |
| 2023-07-27T16:40 | iD11 | `drop_column` | SSO_ApplicationDomain | IDEMPIERE-5346 |
| 2023-07-11T16:56 | iD11 | `rename_column` | SSO_PrincipleConfig_UU | IDEMPIERE-5346 |
| 2023-07-11T16:56 | iD11 | `rename_constraint` |  | IDEMPIERE-5346 |
| 2023-07-11T16:56 | iD11 | `rename_constraint` |  | IDEMPIERE-5346 |
| 2023-07-11T16:56 | iD11 | `rename_constraint` |  | IDEMPIERE-5346 |
| 2023-07-11T16:56 | iD11 | `rename_column` | SSO_PrincipleConfig_UU | IDEMPIERE-5346 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.SSO_LoginButtonImage_ID` | unexplained |

## Notes

<!-- ekos:manual id="table.sso_principalconfig.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
