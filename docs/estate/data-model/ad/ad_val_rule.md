---
title: "AD_VAL_RULE"
order: 230
ekos_generated: true
ekos_estate_version: 1
---

# AD_VAL_RULE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 330 row(s) when profiled

Application model: `org.compiere.model.X_AD_Val_Rule`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_VAL_RULE_ID` | NUMBER(10,0) | PK | yes | Dynamic Validation |  | 0 | 330 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 312 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 269 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 330 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 245 | 75 |
| `TYPE` | CHAR(1) |  |  | Type |  | 0 | 1 |
| `CODE` | VARCHAR2(4000 CHAR) |  |  | Validation code |  | 1 | 328 |
| `ENTITYTYPE` | VARCHAR2(40 CHAR) |  | yes | Entity Type |  | 0 | 3 |
| `AD_VAL_RULE_UU` | VARCHAR2(36 CHAR) |  |  | AD_Val_Rule_UU |  | 0 | 330 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020839` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_VAL_RULE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ENTITYTYPE](../../data-model/ad/ad_entitytype.md) | AD_VAL_RULE.ENTITYTYPE → AD_ENTITYTYPE.ENTITYTYPE | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_VAL_RULE.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_ATTRIBUTE](../../data-model/ad/ad_attribute.md) | AD_ATTRIBUTE.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | SET NULL |
| [AD_COLUMN](../../data-model/ad/ad_column.md) | AD_COLUMN.AD_VAL_RULE_LOOKUP_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_FIELD](../../data-model/ad/ad_field.md) | AD_FIELD.AD_VAL_RULE_LOOKUP_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_INFOCOLUMN](../../data-model/ad/ad_infocolumn.md) | AD_INFOCOLUMN.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_PACKAGE_EXP_DETAIL](../../data-model/ad/ad_package_exp_detail.md) | AD_PACKAGE_EXP_DETAIL.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_PROCESS_PARA](../../data-model/ad/ad_process_para.md) | AD_PROCESS_PARA.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_TABLE.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_USERDEF_FIELD](../../data-model/ad/ad_userdef_field.md) | AD_USERDEF_FIELD.AD_VAL_RULE_LOOKUP_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_USERDEF_INFO_COLUMN](../../data-model/ad/ad_userdef_info_column.md) | AD_USERDEF_INFO_COLUMN.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [AD_USERDEF_PROC_PARAMETER](../../data-model/ad/ad_userdef_proc_parameter.md) | AD_USERDEF_PROC_PARAMETER.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |
| [M_ATTRIBUTE](../../data-model/m/m_attribute.md) | M_ATTRIBUTE.AD_VAL_RULE_ID → AD_VAL_RULE.AD_VAL_RULE_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_VAL_RULE : ""
  AD_ENTITYTYPE ||--o{ AD_VAL_RULE : ""
  AD_ORG ||--o{ AD_VAL_RULE : ""
  AD_VAL_RULE ||--o{ AD_ATTRIBUTE : ""
  AD_VAL_RULE ||--o{ AD_COLUMN : ""
  AD_VAL_RULE ||--o{ AD_FIELD : ""
  AD_VAL_RULE ||--o{ AD_INFOCOLUMN : ""
  AD_VAL_RULE ||--o{ AD_PACKAGE_EXP_DETAIL : ""
  AD_VAL_RULE ||--o{ AD_PROCESS_PARA : ""
  AD_VAL_RULE ||--o{ AD_TABLE : ""
  AD_VAL_RULE ||--o{ AD_USERDEF_FIELD : ""
  AD_VAL_RULE ||--o{ AD_USERDEF_INFO_COLUMN : ""
  AD_VAL_RULE ||--o{ AD_USERDEF_PROC_PARAMETER : ""
  AD_VAL_RULE ||--o{ M_ATTRIBUTE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Read by

| kind | name |
|---|---|
| View | `AD_FIELD_V` |
| View | `AD_FIELD_VT` |
| View | `ad_field_v` |
| View | `ad_field_vt` |

## Schema history

25 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-09-29T14:32 | i9 | `modify_column` | Code | IDEMPIERE-5243 |
| 2022-09-29T14:32 | i9 | `modify_column` | Code | IDEMPIERE-5243 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | ENTITYTYPE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.Type.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_val_rule.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
