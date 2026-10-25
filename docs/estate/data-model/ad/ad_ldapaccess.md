---
title: "AD_LDAPACCESS"
order: 80
ekos_generated: true
ekos_estate_version: 1
---

# AD_LDAPACCESS

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_LdapAccess`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_LDAPACCESS_ID` | NUMBER(10,0) | PK | yes | Ldap Access |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_LDAPPROCESSOR_ID` | NUMBER(10,0) |  | yes | Ldap Processor | [AD_LDAPPROCESSOR](../../data-model/ad/ad_ldapprocessor.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `R_INTERESTAREA_ID` | NUMBER(10,0) |  |  | Interest Area | [R_INTERESTAREA](../../data-model/r/r_interestarea.md) | 0 | 0 |
| `ISERROR` | CHAR(1) |  | yes | Error |  | 0 | 0 |
| `SUMMARY` | VARCHAR2(2000 CHAR) |  |  | Summary |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `AD_LDAPACCESS_UU` | VARCHAR2(36 CHAR) |  |  | AD_LdapAccess_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020751` | `IsError in ('Y','N')` |
| `SYS_C0020753` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LDAPPROCESSOR](../../data-model/ad/ad_ldapprocessor.md) | AD_LDAPACCESS.AD_LDAPPROCESSOR_ID → AD_LDAPPROCESSOR.AD_LDAPPROCESSOR_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_LDAPACCESS.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [R_INTERESTAREA](../../data-model/r/r_interestarea.md) | AD_LDAPACCESS.R_INTERESTAREA_ID → R_INTERESTAREA.R_INTERESTAREA_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_LDAPPROCESSOR ||--o{ AD_LDAPACCESS : ""
  AD_USER ||--o{ AD_LDAPACCESS : ""
  R_INTERESTAREA ||--o{ AD_LDAPACCESS : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

17 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | SUMMARY | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_ldapaccess.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
