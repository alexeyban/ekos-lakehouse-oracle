---
title: "AD_BROADCASTMESSAGE_TRL"
order: 20
ekos_generated: true
ekos_estate_version: 1
---

# AD_BROADCASTMESSAGE_TRL

Area [AD](../../data-model/ad/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_BROADCASTMESSAGE_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `AD_BROADCASTMESSAGE_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `TITLE` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `BROADCASTMESSAGE` | CLOB |  |  |  |  | 0 |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020990` | `IsTranslated IN ('Y','N')` |
| `SYS_C0020991` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_BROADCASTMESSAGE](../../data-model/ad/ad_broadcastmessage.md) | AD_BROADCASTMESSAGE_TRL.AD_BROADCASTMESSAGE_ID → AD_BROADCASTMESSAGE.AD_BROADCASTMESSAGE_ID | CASCADE |
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_BROADCASTMESSAGE_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_BROADCASTMESSAGE_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_BROADCASTMESSAGE_TRL.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_BROADCASTMESSAGE_TRL.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_BROADCASTMESSAGE ||--o{ AD_BROADCASTMESSAGE_TRL : ""
  AD_CLIENT ||--o{ AD_BROADCASTMESSAGE_TRL : ""
  AD_LANGUAGE ||--o{ AD_BROADCASTMESSAGE_TRL : ""
  AD_ORG ||--o{ AD_BROADCASTMESSAGE_TRL : ""
  AD_USER ||--o{ AD_BROADCASTMESSAGE_TRL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_cascade**
- change log: **not_recorded**
- evidence: 2 citation(s)

## Schema history

27 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-09-11T13:58 | iD11 | `add_column` | Tmp_BroadcastMessage_ToRename | IDEMPIERE-5852 |
| 2023-09-11T13:58 | iD11 | `drop_column` | BroadcastMessage | IDEMPIERE-5852 |
| 2023-09-11T13:58 | iD11 | `modify_column` | BroadcastMessage | IDEMPIERE-5852 |
| 2023-09-11T13:58 | iD11 | `rename_column` | Tmp_BroadcastMessage_ToRename | IDEMPIERE-5852 |
| 2022-01-12T16:30 | i9 | `add_column` | Title | IDEMPIERE-5152 |
| 2022-01-12T16:30 | i9 | `add_column` | Title | IDEMPIERE-5152 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | BROADCASTMESSAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | BROADCASTMESSAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_BROADCASTMESSAGE_TRL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | BROADCASTMESSAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2014-03-21T21:21 | i2.0z | `add_constraint` |  | IDEMPIERE-1216 |
| 2014-03-21T21:21 | i2.0z | `add_constraint` |  | IDEMPIERE-1216 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_broadcastmessage_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
