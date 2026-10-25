---
title: "A_ASSET_INFO_OTH"
order: 15
ekos_generated: true
ekos_estate_version: 1
---

# A_ASSET_INFO_OTH

Area [A](../../data-model/a/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_A_Asset_Info_Oth`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) | PK | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `A_ASSET_ID` | NUMBER(10,0) |  | yes | Asset |  | 0 | 0 |
| `A_ASSET_INFO_OTH_ID` | NUMBER(10,0) |  | yes | A_Asset_Info_Oth_ID |  | 0 | 0 |
| `A_USER1` | VARCHAR2(3 CHAR) |  |  | A_User1 |  | 0 | 0 |
| `A_USER10` | VARCHAR2(3 CHAR) |  |  | A_User10 |  | 0 | 0 |
| `A_USER11` | VARCHAR2(10 CHAR) |  |  | A_User11 |  | 0 | 0 |
| `A_USER12` | VARCHAR2(10 CHAR) |  |  | A_User12 |  | 0 | 0 |
| `A_USER13` | VARCHAR2(10 CHAR) |  |  | A_User13 |  | 0 | 0 |
| `A_USER14` | VARCHAR2(10 CHAR) |  |  | A_User14 |  | 0 | 0 |
| `A_USER15` | VARCHAR2(10 CHAR) |  |  | A_User15 |  | 0 | 0 |
| `A_USER2` | VARCHAR2(3 CHAR) |  |  | A_User2 |  | 0 | 0 |
| `A_USER3` | VARCHAR2(3 CHAR) |  |  | A_User3 |  | 0 | 0 |
| `A_USER4` | VARCHAR2(3 CHAR) |  |  | A_User4 |  | 0 | 0 |
| `A_USER5` | VARCHAR2(3 CHAR) |  |  | A_User5 |  | 0 | 0 |
| `A_USER6` | VARCHAR2(3 CHAR) |  |  | A_User6 |  | 0 | 0 |
| `A_USER7` | VARCHAR2(3 CHAR) |  |  | A_User7 |  | 0 | 0 |
| `A_USER8` | VARCHAR2(3 CHAR) |  |  | A_User8 |  | 0 | 0 |
| `A_USER9` | VARCHAR2(3 CHAR) |  |  | A_User9 |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `TEXT` | VARCHAR2(510 CHAR) |  |  | Description |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `A_ASSET_INFO_OTH_UU` | VARCHAR2(36 CHAR) |  |  | A_Asset_Info_Oth_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019754` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

_None._

## Write behaviour

- updates: **po_only**
- deletes: **soft_delete_only**
- change log: **not_recorded**
- evidence: 1 citation(s)

## Schema history

61 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_USER10 | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_13_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_14_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_15_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_11_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_10_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_USER1 | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | A_USER5 | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_6_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.a_asset_info_oth.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
