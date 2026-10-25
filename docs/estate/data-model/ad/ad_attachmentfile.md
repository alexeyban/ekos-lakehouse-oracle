---
title: "AD_ATTACHMENTFILE"
order: 10
ekos_generated: true
ekos_estate_version: 1
---

# AD_ATTACHMENTFILE

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

Application model: `org.compiere.model.X_AD_AttachmentFile`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_AttachmentFile_UU` | UUID | PK | yes | AD_AttachmentFile_UU |  |  |  |
| `AD_Attachment_ID` | NUMERIC(10) |  |  | Attachment | [AD_ATTACHMENT](../../data-model/ad/ad_attachment.md) |  |  |
| `AD_Client_ID` | NUMERIC(10) |  | yes | Tenant |  |  |  |
| `AD_Org_ID` | NUMERIC(10) |  | yes | Organization |  |  |  |
| `Created` | TIMESTAMP |  | yes | Created |  |  |  |
| `CreatedBy` | NUMERIC(10) |  | yes | Created By |  |  |  |
| `FileName` | VARCHAR(1000) |  |  | File Name |  |  |  |
| `FileSize` | NUMERIC(10) |  |  | File Size |  |  |  |
| `IsActive` | CHAR(1) |  | yes | Active |  |  |  |
| `SHA256Checksum` | VARCHAR(64) |  |  | SHA256 Checksum |  |  |  |
| `MIMEType` | VARCHAR(1000) |  |  | MIME Type |  |  |  |
| `SeqNo` | NUMERIC(10) |  |  | Sequence |  |  |  |
| `Updated` | TIMESTAMP |  | yes | Updated |  |  |  |
| `UpdatedBy` | NUMERIC(10) |  | yes | Updated By |  |  |  |

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

16 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-07-31T16:36 | iD13 | `create_table` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `modify_column` | FileSize | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `create_table` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_column` | FilePath | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_column` | FilePath | IDEMPIERE-6640 |
| 2025-07-31T16:36 | iD13 | `add_constraint` |  | IDEMPIERE-6640 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_table_missing` | `database_table` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_attachmentfile.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
