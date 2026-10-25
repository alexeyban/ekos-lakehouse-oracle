---
title: "AD_AUTHORIZATIONCREDENTIAL"
order: 16
ekos_generated: true
ekos_estate_version: 1
---

# AD_AUTHORIZATIONCREDENTIAL

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_AuthorizationCredential`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_AUTHORIZATIONCREDENTIAL_ID` | NUMBER(10,0) | PK | yes | Authorization Credential |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `AD_AUTHORIZATIONCREDENTIAL_UU` | VARCHAR2(36 CHAR) |  |  | AD_AuthorizationCredential_UU |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AUTHORIZATIONCLIENTID` | VARCHAR2(2000 CHAR) |  | yes | Authorization client-id |  | 0 | 0 |
| `AUTHORIZATIONCLIENTSECRET` | VARCHAR2(2000 CHAR) |  | yes | Authorization client-secret |  | 0 | 0 |
| `AUTHORIZATIONREDIRECTURL` | VARCHAR2(2000 CHAR) |  | yes | Authorization Redirect URL |  | 0 | 0 |
| `AD_AUTHORIZATIONPROVIDER_ID` | NUMBER(10,0) |  | yes | Authorization Provider | [AD_AUTHORIZATIONPROVIDER](../../data-model/ad/ad_authorizationprovider.md) | 0 | 0 |
| `AD_AUTHORIZATIONSCOPELIST` | VARCHAR2(2000 CHAR) |  | yes | Scope List |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022426` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_AUTHORIZATIONPROVIDER](../../data-model/ad/ad_authorizationprovider.md) | AD_AUTHORIZATIONCREDENTIAL.AD_AUTHORIZATIONPROVIDER_ID → AD_AUTHORIZATIONPROVIDER.AD_AUTHORIZATIONPROVIDER_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_AUTHORIZATIONACCOUNT](../../data-model/ad/ad_authorizationaccount.md) | AD_AUTHORIZATIONACCOUNT.AD_AUTHORIZATIONCREDENTIAL_ID → AD_AUTHORIZATIONCREDENTIAL.AD_AUTHORIZATIONCREDENTIAL_ID | NO ACTION |

```mermaid
erDiagram
  AD_AUTHORIZATIONCREDENTIAL ||--o{ AD_AUTHORIZATIONACCOUNT : ""
  AD_AUTHORIZATIONPROVIDER ||--o{ AD_AUTHORIZATIONCREDENTIAL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

54 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2021-02-24T18:58 | i8.2 | `add_column` | AD_Org_ID | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | AD_AuthorizationScopeList | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | AD_AuthorizationProvider_ID | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | Updated | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `modify_column` | AuthorizationRedirectURL | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_constraint` |  | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_constraint` |  | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | CreatedBy | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_constraint` |  | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | IsActive | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | Name | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | AD_AuthorizationCredential_UU | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `create_table` |  | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | AuthorizationRedirectURL | IDEMPIERE-3101 |
| 2021-02-24T18:58 | i8.2 | `add_column` | AuthorizationClientId | IDEMPIERE-3101 |

## Notes

<!-- ekos:manual id="table.ad_authorizationcredential.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
