---
title: "AD_ARCHIVE_BLOB"
order: 8
ekos_generated: true
ekos_estate_version: 1
---

# AD_ARCHIVE_BLOB

Area [AD](../../data-model/ad/index.md) · class **unclassified** (proposed) · from DDL (postgres)

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `ad_archive_id` | NUMERIC(10,0) |  | yes |  |  |  |  |
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
| Trigger | `trg_delete_ad_archive_binary` |

## Schema history

2 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-06-02T01:00 | iD12 | `create_table` |  | IDEMPIERE-6564 |
| 2025-06-02T01:00 | iD12 | `create_table` |  | IDEMPIERE-6564 |

## Notes

<!-- ekos:manual id="table.ad_archive_blob.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
