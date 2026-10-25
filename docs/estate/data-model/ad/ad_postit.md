---
title: "AD_POSTIT"
order: 110
ekos_generated: true
ekos_estate_version: 1
---

# AD_POSTIT

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_PostIt`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_POSTIT_ID` | NUMBER(10,0) | PK | yes | Post-it |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  |  | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `TEXT` | VARCHAR2(2000 CHAR) |  |  | Description |  | 0 | 0 |
| `RECORD_ID` | NUMBER(10,0) |  |  | Record ID |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_POSTIT_UU` | VARCHAR2(36 CHAR) |  |  | AD_PostIt_UU |  | 0 | 0 |
| `RECORD_UU` | VARCHAR2(36 CHAR) |  |  | Record UUID |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020895` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_POSTIT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_POSTIT.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_POSTIT.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_POSTIT.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_POSTIT : ""
  AD_ORG ||--o{ AD_POSTIT : ""
  AD_TABLE ||--o{ AD_POSTIT : ""
  AD_USER ||--o{ AD_POSTIT : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **soft_delete_only**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

46 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2026-04-28T23:41 | iD12 | `create_index` |  | IDEMPIERE-6983 |
| 2026-04-28T23:41 | iD12 | `create_index` |  | IDEMPIERE-6983 |
| 2023-05-29T13:32 | iD11 | `add_column` | Record_UU | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `create_index` |  | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `add_column` | Record_UU | IDEMPIERE-5567 |
| 2023-05-29T13:32 | iD11 | `create_index` |  | IDEMPIERE-5567 |
| 2022-03-16T13:42 | i9 | `create_index` |  | IDEMPIERE-5221 |
| 2022-03-16T13:42 | i9 | `create_index` |  | IDEMPIERE-5221 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_POSTIT_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | TEXT | IDEMPIERE-3862 |
| 2016-11-24T17:46 | i4.1z | `add_constraint` |  | IDEMPIERE-905 |
| 2016-11-24T17:46 | i4.1z | `add_column` | AD_Org_ID | IDEMPIERE-905 |
| 2016-11-24T17:46 | i4.1z | `add_column` | Text | IDEMPIERE-905 |
| 2016-11-24T17:46 | i4.1z | `add_column` | Created | IDEMPIERE-905 |
| 2016-11-24T17:46 | i4.1z | `add_column` | CreatedBy | IDEMPIERE-905 |

## Notes

<!-- ekos:manual id="table.ad_postit.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
