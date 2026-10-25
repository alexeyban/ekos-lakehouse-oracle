---
title: "AD_HOUSEKEEPING"
order: 55
ekos_generated: true
ekos_estate_version: 1
---

# AD_HOUSEKEEPING

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 9 row(s) when profiled

Application model: `org.compiere.model.X_AD_HouseKeeping`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_HOUSEKEEPING_ID` | NUMBER(10,0) | PK | yes | House Keeping Configuration |  | 0 | 9 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `AD_TABLE_ID` | NUMBER(10,0) |  |  | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 9 |
| `BACKUPFOLDER` | VARCHAR2(255 CHAR) |  |  | Backup Folder |  | 9 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 9 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 9 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 9 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `ISEXPORTXMLBACKUP` | CHAR(1) |  |  | Export XML Backup |  | 0 | 1 |
| `ISSAVEINHISTORIC` | CHAR(1) |  |  | Save In Historic |  | 0 | 1 |
| `LASTDELETED` | NUMBER(10,0) |  |  | Last Deleted |  | 0 | 1 |
| `LASTRUN` | DATE |  |  | Last Run |  | 9 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 9 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 9 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 9 |
| `WHERECLAUSE` | VARCHAR2(255 CHAR) |  |  | Sql WHERE |  | 0 | 2 |
| `AD_HOUSEKEEPING_UU` | VARCHAR2(36 CHAR) |  |  | AD_HouseKeeping_UU |  | 0 | 9 |
| `TABLENAME` | VARCHAR2(60 CHAR) |  |  | DB Table Name |  | 9 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019580` | `IsSaveInHistoric IN ('Y','N')` |
| `SYS_C0019582` | `IsActive IN ('Y','N')` |
| `SYS_C0019584` | `IsExportXMLBackup IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_HOUSEKEEPING.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_TABLE ||--o{ AD_HOUSEKEEPING : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

46 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-04-03T12:26 | iD11 | `modify_column` | TableName | IDEMPIERE-6064 |
| 2024-04-03T12:26 | iD11 | `modify_column` | TableName | IDEMPIERE-6064 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | WHERECLAUSE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_HOUSEKEEPING_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_housekeeping.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
