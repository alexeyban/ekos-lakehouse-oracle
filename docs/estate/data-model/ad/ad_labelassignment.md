---
title: "AD_LABELASSIGNMENT"
order: 72
ekos_generated: true
ekos_estate_version: 1
---

# AD_LABELASSIGNMENT

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_LabelAssignment`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_LABELASSIGNMENT_ID` | NUMBER(10,0) | PK | yes | Label Assignment |  | 0 | 0 |
| `AD_LABELASSIGNMENT_UU` | VARCHAR2(36 CHAR) |  |  | Label Assignment |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  |  | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  |  | Organization |  | 0 | 0 |
| `CREATED` | DATE |  |  | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  |  | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  |  | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  |  | Updated By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  |  | Active |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `AD_LABEL_ID` | NUMBER(10,0) |  | yes | Label | [AD_LABEL](../../data-model/ad/ad_label.md) | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 0 |
| `RECORD_ID` | NUMBER(10,0) |  |  | Record ID |  | 0 | 0 |
| `RECORD_UU` | VARCHAR2(36 CHAR) |  |  | Record UUID |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020995` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LABEL](../../data-model/ad/ad_label.md) | AD_LABELASSIGNMENT.AD_LABEL_ID → AD_LABEL.AD_LABEL_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_LABELASSIGNMENT.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_LABEL ||--o{ AD_LABELASSIGNMENT : ""
  AD_TABLE ||--o{ AD_LABELASSIGNMENT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

42 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `create_index` |  | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `create_index` |  | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `add_column` | Record_UU | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `modify_column` | Record_ID | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `add_column` | Record_UU | IDEMPIERE-5567 |
| 2022-05-13T11:18 | iD10 | `create_index` |  | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | Record_ID | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_Table_ID | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | AD_LabelAssignment_UU | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | IsActive | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_column` | IsActive | IDEMPIERE-5259 |
| 2022-05-13T11:18 | iD10 | `add_constraint` |  | IDEMPIERE-5259 |

## Notes

<!-- ekos:manual id="table.ad_labelassignment.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
