---
title: "AD_NOTE"
order: 91
ekos_generated: true
ekos_estate_version: 1
---

# AD_NOTE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Note`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_NOTE_ID` | NUMBER(10,0) | PK | yes | Notice |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `AD_MESSAGE_ID` | NUMBER(10,0) |  | yes | Message | [AD_MESSAGE](../../data-model/ad/ad_message.md) | 0 | 0 |
| `REFERENCE` | VARCHAR2(255 CHAR) |  |  | Reference |  | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  |  | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 0 |
| `RECORD_ID` | NUMBER(10,0) |  |  | Record ID |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  |  | Processed |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `AD_WF_ACTIVITY_ID` | NUMBER(10,0) |  |  | Workflow Activity | [AD_WF_ACTIVITY](../../data-model/ad/ad_wf_activity.md) | 0 | 0 |
| `TEXTMSG` | VARCHAR2(2000 CHAR) |  |  | Text Message |  | 0 | 0 |
| `AD_NOTE_UU` | VARCHAR2(36 CHAR) |  |  | AD_Note_UU |  | 0 | 0 |
| `AD_BROADCASTMESSAGE_ID` | NUMBER(10,0) |  |  | Broadcast Message | [AD_BROADCASTMESSAGE](../../data-model/ad/ad_broadcastmessage.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021210` | `IsActive in ('Y','N')` |
| `SYS_C0021211` | `Processed in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_BROADCASTMESSAGE](../../data-model/ad/ad_broadcastmessage.md) | AD_NOTE.AD_BROADCASTMESSAGE_ID → AD_BROADCASTMESSAGE.AD_BROADCASTMESSAGE_ID | NO ACTION |
| [AD_MESSAGE](../../data-model/ad/ad_message.md) | AD_NOTE.AD_MESSAGE_ID → AD_MESSAGE.AD_MESSAGE_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_NOTE.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_NOTE.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [AD_WF_ACTIVITY](../../data-model/ad/ad_wf_activity.md) | AD_NOTE.AD_WF_ACTIVITY_ID → AD_WF_ACTIVITY.AD_WF_ACTIVITY_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_BROADCASTMESSAGE ||--o{ AD_NOTE : ""
  AD_MESSAGE ||--o{ AD_NOTE : ""
  AD_TABLE ||--o{ AD_NOTE : ""
  AD_USER ||--o{ AD_NOTE : ""
  AD_WF_ACTIVITY ||--o{ AD_NOTE : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users, purged**
- change log: **recorded**
- evidence: 3 citation(s)

## Written by

| kind | name |
|---|---|
| Procedure | [DBA_Cleanup](../../logic/dba_cleanup.md) |

## Schema history

32 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-03-16T13:42 | i9 | `create_index` |  | IDEMPIERE-5221 |
| 2022-03-16T13:42 | i9 | `create_index` |  | IDEMPIERE-5221 |
| 2022-03-16T13:42 | i9 | `create_index` |  | IDEMPIERE-5221 |
| 2022-03-16T13:42 | i9 | `create_index` |  | IDEMPIERE-5221 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_note.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
