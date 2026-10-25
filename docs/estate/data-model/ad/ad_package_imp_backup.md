---
title: "AD_PACKAGE_IMP_BACKUP"
order: 99
ekos_generated: true
ekos_estate_version: 1
---

# AD_PACKAGE_IMP_BACKUP

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Package_Imp_Backup`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PACKAGE_IMP_BACKUP_ID` | NUMBER(10,0) | PK | yes | Imp. Package Backup |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_PACKAGE_IMP_ID` | NUMBER(10,0) |  | yes | Package Imp |  | 0 | 0 |
| `AD_PACKAGE_IMP_DETAIL_ID` | NUMBER(10,0) |  | yes | Imp. Package Detail |  | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  |  | Table |  | 0 | 0 |
| `AD_COLUMN_ID` | NUMBER(10,0) |  |  | Column | [AD_COLUMN](../../data-model/ad/ad_column.md) | 0 | 0 |
| `AD_REFERENCE_ID` | NUMBER(10,0) |  |  | Reference | [AD_REFERENCE](../../data-model/ad/ad_reference.md) | 0 | 0 |
| `AD_PACKAGE_IMP_BCK_DIR` | VARCHAR2(255 CHAR) |  |  | Package Imp. Bck. Directory |  | 0 | 0 |
| `AD_PACKAGE_IMP_ORG_DIR` | VARCHAR2(255 CHAR) |  |  | Package Imp. Org. Dir |  | 0 | 0 |
| `COLVALUE` | VARCHAR2(2000 CHAR) |  |  | Col Value |  | 0 | 0 |
| `UNINSTALL` | CHAR(1) |  |  | Uninstall |  | 0 | 0 |
| `AD_PACKAGE_IMP_BACKUP_UU` | VARCHAR2(36 CHAR) |  |  | AD_Package_Imp_Backup_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_COLUMN](../../data-model/ad/ad_column.md) | AD_PACKAGE_IMP_BACKUP.AD_COLUMN_ID → AD_COLUMN.AD_COLUMN_ID | NO ACTION |
| [AD_REFERENCE](../../data-model/ad/ad_reference.md) | AD_PACKAGE_IMP_BACKUP.AD_REFERENCE_ID → AD_REFERENCE.AD_REFERENCE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_COLUMN ||--o{ AD_PACKAGE_IMP_BACKUP : ""
  AD_REFERENCE ||--o{ AD_PACKAGE_IMP_BACKUP : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **soft_delete_only**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

18 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | COLVALUE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PACKAGE_IMP_BCK_DIR | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PACKAGE_IMP_ORG_DIR | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PACKAGE_IMP_BACKUP_UU | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_package_imp_backup.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
