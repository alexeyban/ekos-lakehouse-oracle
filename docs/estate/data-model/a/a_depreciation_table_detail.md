---
title: "A_DEPRECIATION_TABLE_DETAIL"
order: 34
ekos_generated: true
ekos_estate_version: 1
---

# A_DEPRECIATION_TABLE_DETAIL

Area [A](../../data-model/a/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2579 row(s) when profiled

Application model: `org.compiere.model.X_A_Depreciation_Table_Detail`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `A_DEPRECIATION_TABLE_DETAIL_ID` | NUMBER(10,0) | PK | yes | Depreciation Table Detail |  | 0 | 2579 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `A_PERIOD` | NUMBER(10,0) |  | yes | Asset Period |  | 0 | 41 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `A_TABLE_RATE_TYPE` | VARCHAR2(2 CHAR) |  |  | Type |  | 0 | 1 |
| `A_DEPRECIATION_RATE` | NUMBER |  | yes | Rate |  | 0 | 418 |
| `A_DEPRECIATION_TABLE_CODE` | VARCHAR2(20 CHAR) |  | yes | Depreciation Code |  | 0 | 141 |
| `A_DEPRECIATION_TABLE_DETAIL_UU` | VARCHAR2(36 CHAR) |  |  | A_Depreciation_Table_Detail_UU |  | 0 | 2579 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019422` | `IsActive IN ('Y','N')` |
| `SYS_C0019423` | `Processed IN ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

21 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_TABLE_RATE_TYPE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_DEPRECIATION_TABLE_CODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_DEPRECIATION_TABLE_CODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_DEPRECIATION_TABLE_CODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_DEPRECIATION_TABLE_DETAIL_UU | IDEMPIERE-3862 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |

## Notes

<!-- ekos:manual id="table.a_depreciation_table_detail.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
