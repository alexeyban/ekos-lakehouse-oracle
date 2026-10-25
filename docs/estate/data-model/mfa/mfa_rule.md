---
title: "MFA_RULE"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# MFA_RULE

Area [MFA](../../data-model/mfa/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_MFA_Rule`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `MFA_RULE_ID` | NUMBER(10,0) | PK | yes | MFA Rule |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 2 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `MFA_RULE_UU` | VARCHAR2(36 CHAR) |  |  | MFA_Rule_UU |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `MFA_METHOD_ID` | NUMBER(10,0) |  | yes | MFA Method | [MFA_METHOD](../../data-model/mfa/mfa_method.md) | 0 | 2 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021748` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [MFA_METHOD](../../data-model/mfa/mfa_method.md) | MFA_RULE.MFA_METHOD_ID → MFA_METHOD.MFA_METHOD_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  MFA_METHOD ||--o{ MFA_RULE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

26 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2021-05-30T14:48 | i8.2 | `create_table` |  | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Updated | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Help | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | MFA_Method_ID | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | AD_Client_ID | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Updated | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_constraint` |  | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Help | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | CreatedBy | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | IsActive | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_constraint` |  | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | CreatedBy | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_constraint` |  | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | Created | IDEMPIERE-4782 |
| 2021-05-30T14:48 | i8.2 | `add_column` | AD_Org_ID | IDEMPIERE-4782 |

## Notes

<!-- ekos:manual id="table.mfa_rule.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
