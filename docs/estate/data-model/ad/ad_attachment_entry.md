---
title: "AD_ATTACHMENT_ENTRY"
order: 12
ekos_generated: true
ekos_estate_version: 1
---

# AD_ATTACHMENT_ENTRY

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `ad_attachment_id` | NUMERIC(10,0) |  | yes |  |  |  |  |
| `seqno` | NUMERIC(10,0) |  | yes |  |  |  |  |
| `binarydata` | oid |  |  |  |  |  |  |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Written by

| kind | name |
|---|---|
| Trigger | `trg_delete_ad_attachment_binary` |

## Schema history

2 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-06-05T07:00 | iD12 | `create_table` |  | IDEMPIERE-6570 |
| 2025-06-05T07:00 | iD12 | `create_table` |  | IDEMPIERE-6570 |

## Notes

<!-- ekos:manual id="table.ad_attachment_entry.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
