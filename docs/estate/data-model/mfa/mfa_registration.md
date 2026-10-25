---
title: "MFA_REGISTRATION"
order: 3
ekos_generated: true
ekos_estate_version: 1
---

# MFA_REGISTRATION

Area [MFA](../../data-model/mfa/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_MFA_Registration`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `MFA_REGISTRATION_ID` | NUMBER(10,0) | PK | yes | MFA Registration |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `NAME` | VARCHAR2(1000 CHAR) |  |  | Name |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `MFA_REGISTRATION_UU` | VARCHAR2(36 CHAR) |  |  | MFA_Registration_UU |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `MFA_METHOD_ID` | NUMBER(10,0) |  | yes | MFA Method | [MFA_METHOD](../../data-model/mfa/mfa_method.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `MFASECRET` | VARCHAR2(2000 CHAR) |  |  | MFA Secret |  | 0 | 0 |
| `ISVALID` | CHAR(1) |  | yes | Valid |  | 0 | 0 |
| `MFAVALIDATEDAT` | DATE |  |  | Validated at |  | 0 | 0 |
| `MFAUNREGISTEREDAT` | DATE |  |  | Unregistered at |  | 0 | 0 |
| `ISUSERMFAPREFERRED` | CHAR(1) |  | yes | Preferred |  | 0 | 0 |
| `EXPIRATION` | DATE |  |  | Expire On |  | 0 | 0 |
| `PARAMETERVALUE` | VARCHAR2(2000 CHAR) |  |  | Parameter Value |  | 0 | 0 |
| `MFALASTSECRET` | VARCHAR2(2000 CHAR) |  |  | Last MFA Secret |  | 0 | 0 |
| `LASTSUCCESS` | DATE |  |  | Last Success |  | 0 | 0 |
| `LASTFAILURE` | DATE |  |  | Last Failure |  | 0 | 0 |
| `FAILEDLOGINCOUNT` | NUMBER(10,0) |  |  | Failed Login Count |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019570` | `IsValid IN ('Y','N')` |
| `SYS_C0019571` | `IsActive IN ('Y','N')` |
| `SYS_C0019572` | `IsUserMFAPreferred IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | MFA_REGISTRATION.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [MFA_METHOD](../../data-model/mfa/mfa_method.md) | MFA_REGISTRATION.MFA_METHOD_ID → MFA_METHOD.MFA_METHOD_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_USER ||--o{ MFA_REGISTRATION : ""
  MFA_METHOD ||--o{ MFA_REGISTRATION : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 3 citation(s)

## Schema history

54 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2021-06-07T22:01 | i8.2 | `add_column` | MFALastSecret | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | MFALastSecret | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | LastFailure | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | LastSuccess | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | FailedLoginCount | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | LastSuccess | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | LastFailure | IDEMPIERE-4782 |
| 2021-06-07T22:01 | i8.2 | `add_column` | FailedLoginCount | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Updated | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | IsUserMFAPreferred | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `create_table` |  | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | CreatedBy | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | AD_User_ID | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Name | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | MFAValidatedAt | IDEMPIERE-4782 |

## Notes

<!-- ekos:manual id="table.mfa_registration.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
