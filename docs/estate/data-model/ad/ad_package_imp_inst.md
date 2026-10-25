---
title: "AD_PACKAGE_IMP_INST"
order: 101
ekos_generated: true
ekos_estate_version: 1
---

# AD_PACKAGE_IMP_INST

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Package_Imp_Inst`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PACKAGE_IMP_INST_ID` | NUMBER(10,0) | PK | yes | Package Imp. Inst |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  |  | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  |  | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  |  | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  |  | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  |  | Updated By |  | 0 | 0 |
| `NAME` | VARCHAR2(240 CHAR) |  |  | Name |  | 0 | 0 |
| `PK_STATUS` | VARCHAR2(44 CHAR) |  |  | Package Status |  | 0 | 0 |
| `RELEASENO` | VARCHAR2(40 CHAR) |  |  | Release No |  | 0 | 0 |
| `PK_VERSION` | VARCHAR2(40 CHAR) |  |  | Package Version |  | 0 | 0 |
| `VERSION` | VARCHAR2(40 CHAR) |  |  | Version |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(2000 CHAR) |  |  | Description |  | 0 | 0 |
| `EMAIL` | VARCHAR2(120 CHAR) |  |  | EMail Address |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  |  | Processed |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `CREATOR` | VARCHAR2(120 CHAR) |  |  | Creator |  | 0 | 0 |
| `CREATORCONTACT` | VARCHAR2(510 CHAR) |  |  | Creator Contact |  | 0 | 0 |
| `CREATEDDATE` | VARCHAR2(50 CHAR) |  |  | Created Date |  | 0 | 0 |
| `UPDATEDDATE` | VARCHAR2(50 CHAR) |  |  | Updated Date |  | 0 | 0 |
| `UNINSTALL` | CHAR(1) |  |  | Uninstall |  | 0 | 0 |
| `AD_PACKAGE_IMP_INST_UU` | VARCHAR2(36 CHAR) |  |  | AD_Package_Imp_Inst_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Write behaviour

- updates: **raw_sql_sets_updated**
- deletes: **soft_delete_only**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

46 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_12_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_8_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_10_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PACKAGE_IMP_INST_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_11_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | UPDATEDDATE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_8_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CREATEDDATE | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_package_imp_inst.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
