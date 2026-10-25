---
title: "AD_CTXHELPSUGGESTION"
order: 37
ekos_generated: true
ekos_estate_version: 1
---

# AD_CTXHELPSUGGESTION

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_CtxHelpSuggestion`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CTXHELPSUGGESTION_ID` | NUMBER(10,0) | PK | yes | Context Help Suggestion |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_CTXHELP_ID` | NUMBER(10,0) |  | yes | Context Help | [AD_CTXHELP](../../data-model/ad/ad_ctxhelp.md) | 0 | 0 |
| `AD_CTXHELPMSG_ID` | NUMBER(10,0) |  | yes | Context Help Message | [AD_CTXHELPMSG](../../data-model/ad/ad_ctxhelpmsg.md) | 0 | 0 |
| `AD_CTXHELPSUGGESTION_UU` | VARCHAR2(36 CHAR) |  | yes | Context Help Suggestion UUID |  | 0 | 0 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) |  | yes | Language |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_USERCLIENT_ID` | NUMBER(10,0) |  | yes | Tenant of User | `AD_ALLCLIENTS_V` | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  | yes | User/Contact | `AD_ALLUSERS_V` | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `MSGTEXT` | VARCHAR2(2000 CHAR) |  | yes | Message Text |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `ISAPPROVED` | CHAR(1) |  | yes | Approved |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `ACCEPTSUGGESTION` | CHAR(1) |  |  | Accept |  | 0 | 0 |
| `REJECTSUGGESTION` | CHAR(1) |  |  | Reject |  | 0 | 0 |
| `COMPARESUGGESTION` | CHAR(1) |  |  | Compare |  | 0 | 0 |
| `ISSAVEASTENANTCUSTOMIZATION` | CHAR(1) |  | yes | Save As Tenant Customization |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021291` | `Processed IN ('Y','N')` |
| `SYS_C0021292` | `IsSaveAsTenantCustomization IN ('Y','N')` |
| `SYS_C0021293` | `IsApproved IN ('Y','N')` |
| `SYS_C0021295` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_CTXHELPSUGGESTION.AD_USERCLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_CTXHELP](../../data-model/ad/ad_ctxhelp.md) | AD_CTXHELPSUGGESTION.AD_CTXHELP_ID → AD_CTXHELP.AD_CTXHELP_ID | NO ACTION |
| [AD_CTXHELPMSG](../../data-model/ad/ad_ctxhelpmsg.md) | AD_CTXHELPSUGGESTION.AD_CTXHELPMSG_ID → AD_CTXHELPMSG.AD_CTXHELPMSG_ID | NO ACTION |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_CTXHELPSUGGESTION.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_CTXHELPSUGGESTION.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_CTXHELPSUGGESTION : ""
  AD_CTXHELP ||--o{ AD_CTXHELPSUGGESTION : ""
  AD_CTXHELPMSG ||--o{ AD_CTXHELPSUGGESTION : ""
  AD_LANGUAGE ||--o{ AD_CTXHELPSUGGESTION : ""
  AD_USER ||--o{ AD_CTXHELPSUGGESTION : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **soft_delete_only**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

69 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_CTXHELPSUGGESTION_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | MSGTEXT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2019-06-17T12:20 | i6.2 | `add_constraint` |  | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `modify_column` | AD_User_ID | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `add_constraint` |  | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `modify_column` | AD_UserClient_ID | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `modify_column` | AD_User_ID | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `add_constraint` |  | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `modify_column` | AD_UserClient_ID | IDEMPIERE-3439 |
| 2019-06-17T12:20 | i6.2 | `add_constraint` |  | IDEMPIERE-3439 |
| 2017-07-28T18:28 | i4.1z | `drop_constraint` |  | IDEMPIERE-3438 |
| 2017-07-28T18:28 | i4.1z | `drop_constraint` |  | IDEMPIERE-3438 |
| 2017-07-28T18:28 | i4.1z | `drop_constraint` |  | IDEMPIERE-3438 |
| 2017-07-28T18:28 | i4.1z | `drop_constraint` |  | IDEMPIERE-3438 |

## Notes

<!-- ekos:manual id="table.ad_ctxhelpsuggestion.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
