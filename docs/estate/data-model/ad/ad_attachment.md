---
title: "AD_ATTACHMENT"
order: 9
ekos_generated: true
ekos_estate_version: 1
---

# AD_ATTACHMENT

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_AD_Attachment`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_ATTACHMENT_ID` | NUMBER(10,0) | PK | yes | Attachment |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `AD_TABLE_ID` | NUMBER(10,0) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 1 |
| `RECORD_ID` | NUMBER(10,0) |  |  | Record ID |  | 0 | 1 |
| `TITLE` | VARCHAR2(60 CHAR) |  | yes | Title |  | 0 | 1 |
| `BINARYDATA` | BLOB |  |  | Binary Data |  | 1 | 0 |
| `TEXTMSG` | VARCHAR2(2000 CHAR) |  |  | Text Message |  | 0 | 1 |
| `AD_ATTACHMENT_UU` | VARCHAR2(36 CHAR) |  |  | AD_Attachment_UU |  | 0 | 1 |
| `AD_STORAGEPROVIDER_ID` | NUMBER(10,0) |  |  | Storage Provider | [AD_STORAGEPROVIDER](../../data-model/ad/ad_storageprovider.md) | 1 | 0 |
| `RECORD_UU` | VARCHAR2(36 CHAR) |  |  | Record UUID |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021010` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_STORAGEPROVIDER](../../data-model/ad/ad_storageprovider.md) | AD_ATTACHMENT.AD_STORAGEPROVIDER_ID → AD_STORAGEPROVIDER.AD_STORAGEPROVIDER_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_ATTACHMENT.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_ATTACHMENTNOTE](../../data-model/ad/ad_attachmentnote.md) | AD_ATTACHMENTNOTE.AD_ATTACHMENT_ID → AD_ATTACHMENT.AD_ATTACHMENT_ID | NO ACTION |

```mermaid
erDiagram
  AD_ATTACHMENT ||--o{ AD_ATTACHMENTNOTE : ""
  AD_STORAGEPROVIDER ||--o{ AD_ATTACHMENT : ""
  AD_TABLE ||--o{ AD_ATTACHMENT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

29 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2026-04-28T23:41 | iD12 | `create_index` |  | IDEMPIERE-6983 |
| 2026-04-28T23:41 | iD12 | `create_index` |  | IDEMPIERE-6983 |
| 2023-05-29T13:32 | iD11 | `add_column` | Record_UU | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `create_index` |  | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `create_index` |  | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `add_column` | Record_UU | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-04-16T22:11 | i8.2 | `add_constraint` |  | IDEMPIERE-4762 |

## Notes

<!-- ekos:manual id="table.ad_attachment.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
