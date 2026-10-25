---
title: "AD_USERDEF_INFO_RELATED"
order: 217
ekos_generated: true
ekos_estate_version: 1
---

# AD_USERDEF_INFO_RELATED

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_UserDef_Info_Related`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_USERDEF_INFO_RELATED_ID` | NUMBER(10,0) | PK | yes | User defined Info Related |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_USERDEF_INFO_ID` | NUMBER(10,0) |  | yes | User defined Info Window | [AD_USERDEF_INFO](../../data-model/ad/ad_userdef_info.md) | 0 | 0 |
| `AD_INFORELATED_ID` | NUMBER(10,0) |  | yes | Info Related | [AD_INFORELATED](../../data-model/ad/ad_inforelated.md) | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  |  | Name |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `AD_USERDEF_INFO_RELATED_UU` | VARCHAR2(36 CHAR) |  |  | AD_UserDef_Info_Related_UU |  | 0 | 0 |
| `DISPLAYLOGIC` | VARCHAR2(2000 CHAR) |  |  | Display Logic |  | 0 | 0 |
| `SEQNO` | NUMBER(10,0) |  |  | Sequence |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022858` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_INFORELATED](../../data-model/ad/ad_inforelated.md) | AD_USERDEF_INFO_RELATED.AD_INFORELATED_ID → AD_INFORELATED.AD_INFORELATED_ID | NO ACTION |
| [AD_USERDEF_INFO](../../data-model/ad/ad_userdef_info.md) | AD_USERDEF_INFO_RELATED.AD_USERDEF_INFO_ID → AD_USERDEF_INFO.AD_USERDEF_INFO_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_INFORELATED ||--o{ AD_USERDEF_INFO_RELATED : ""
  AD_USERDEF_INFO ||--o{ AD_USERDEF_INFO_RELATED : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

42 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-09-29T07:30 | i7.1z | `add_column` | AD_UserDef_Info_Related_UU | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `modify_column` | SeqNo | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | CreatedBy | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | Created | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `create_table` |  | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | UpdatedBy | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | Updated | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `modify_column` | SeqNo | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_constraint` |  | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | IsActive | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | Name | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | Created | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_constraint` |  | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `modify_column` | SeqNo | IDEMPIERE-4459 |
| 2020-09-29T07:30 | i7.1z | `add_column` | IsActive | IDEMPIERE-4459 |

## Notes

<!-- ekos:manual id="table.ad_userdef_info_related.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
