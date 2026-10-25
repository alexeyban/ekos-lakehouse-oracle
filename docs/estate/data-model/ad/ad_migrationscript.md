---
title: "AD_MIGRATIONSCRIPT"
order: 87
ekos_generated: true
ekos_estate_version: 1
---

# AD_MIGRATIONSCRIPT

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1211 row(s) when profiled

Application model: `org.compiere.model.X_AD_MigrationScript`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_MIGRATIONSCRIPT_ID` | NUMBER(10,0) | PK | yes | Migration Script |  | 0 | 1211 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 283 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(2000 CHAR) |  |  | Description |  | 1209 | 1 |
| `DEVELOPERNAME` | VARCHAR2(60 CHAR) |  |  | Developer Name |  | 1211 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1211 |
| `PROJECTNAME` | VARCHAR2(60 CHAR) |  | yes | Project |  | 0 | 1 |
| `REFERENCE` | VARCHAR2(2000 CHAR) |  |  | Reference |  | 1211 | 0 |
| `RELEASENO` | VARCHAR2(10 CHAR) |  | yes | Release No |  | 0 | 14 |
| `SCRIPTROLL` | CHAR(1) |  |  | Roll the Script |  | 0 | 1 |
| `STATUS` | CHAR(2) |  | yes | Status |  | 0 | 1 |
| `URL` | VARCHAR2(2000 CHAR) |  |  | URL |  | 1211 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 283 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `ISAPPLY` | CHAR(1) |  | yes | Apply Script |  | 0 | 1 |
| `FILENAME` | VARCHAR2(500 CHAR) |  | yes | File Name |  | 0 | 1211 |
| `SCRIPT` | BLOB |  |  | Script |  | 1211 | 0 |
| `AD_MIGRATIONSCRIPT_UU` | VARCHAR2(36 CHAR) |  |  | AD_MigrationScript_UU |  | 0 | 1211 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `AD_MIGRATIONSCRIPT_ISACT_CHK` | `IsActive IN ('Y','N')` |
| `AD_MIGRATIONSCRIPT_ISAPPLY_CHK` | `IsApply IN ('Y','N')` |
| `SYS_C0020900` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 6 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [register_migration_script](../../logic/register_migration_script.md) |

## Written by

| kind | name |
|---|---|
| Procedure | [register_migration_script](../../logic/register_migration_script.md) |

## Schema history

31 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | FILENAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | RELEASENO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | FILENAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | URL | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | FILENAME | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_migrationscript.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
