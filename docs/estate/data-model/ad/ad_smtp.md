---
title: "AD_SMTP"
order: 169
ekos_generated: true
ekos_estate_version: 1
---

# AD_SMTP

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_SMTP`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_SMTP_ID` | NUMBER(10,0) | PK | yes | SMTP Server |  | 0 | 0 |
| `AD_SMTP_UU` | VARCHAR2(36 CHAR) |  |  | AD_SMTP_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `EMAILTEST` | CHAR(1) |  |  | EMail Test |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `ISSECURESMTP` | CHAR(1) |  | yes | SMTP SSL/TLS |  | 0 | 0 |
| `ISSMTPAUTHORIZATION` | CHAR(1) |  | yes | SMTP Authentication |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `REQUESTUSER` | VARCHAR2(60 CHAR) |  |  | Request User |  | 0 | 0 |
| `REQUESTUSERPW` | VARCHAR2(255 CHAR) |  |  | Request User Password |  | 0 | 0 |
| `SMTPHOST` | VARCHAR2(60 CHAR) |  |  | Mail Host |  | 0 | 0 |
| `SMTPPORT` | NUMBER(10,0) |  |  | SMTP Port |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `USEDBYEMAILORDOMAIN` | VARCHAR2(255 CHAR) |  |  | Used by email or domain |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019631` | `IsSecureSMTP IN ('Y','N')` |
| `SYS_C0019633` | `IsActive IN ('Y','N')` |
| `SYS_C0019634` | `IsSmtpAuthorization IN ('Y','N')` |

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

2 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2021-07-20T08:30 | i8.2z | `create_table` |  | IDEMPIERE-4866 |
| 2021-07-20T08:30 | i8.2z | `create_table` |  | IDEMPIERE-4866 |

## Notes

<!-- ekos:manual id="table.ad_smtp.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
