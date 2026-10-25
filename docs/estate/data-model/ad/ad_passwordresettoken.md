---
title: "AD_PASSWORDRESETTOKEN"
order: 104
ekos_generated: true
ekos_estate_version: 1
---

# AD_PASSWORDRESETTOKEN

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_AD_PasswordResetToken`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_Client_ID` | NUMERIC(10) |  | yes | Tenant |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes | Organization |  |  |  |
| `AD_PasswordResetToken_ID` | NUMERIC(10) | PK | yes | Password Reset Token |  |  |  |
| `AD_PasswordResetToken_UU` | UUID |  |  | AD_PasswordResetToken_UU |  |  |  |
| `AttemptsUsed` | NUMERIC(10) |  | yes | Attempts Used |  |  |  |
| `OneTimeCode` | VARCHAR(10) |  | yes | One Time Code |  |  |  |
| `Created` | TIMESTAMP |  | yes | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes | Created By |  |  |  |
| `EMail` | VARCHAR(60) |  | yes | EMail Address |  |  |  |
| `Expiration` | TIMESTAMP |  | yes | Expire On |  |  |  |
| `IsActive` | CHAR(1) |  | yes | Active |  |  |  |
| `TokenStatus` | CHAR(1) |  | yes | Token Status |  |  |  |
| `Updated` | TIMESTAMP |  | yes | Updated |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes | Updated By |  |  |  |
| `VerifiedTokenExpires` | TIMESTAMP |  |  | Verified Token Expires |  |  |  |
| `VerifiedTokenHash` | VARCHAR(10) |  |  | Verified Token Hash |  |  |  |

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

14 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2026-07-07T20:11 | iD13 | `create_table` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `modify_column` | OneTimeCode | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `modify_column` | VerifiedTokenHash | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `modify_column` | VerifiedTokenHash | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `create_table` |  | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `modify_column` | OneTimeCode | IDEMPIERE-7060 |
| 2026-07-07T20:11 | iD13 | `add_constraint` |  | IDEMPIERE-7060 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_passwordresettoken.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
