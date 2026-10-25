---
title: "AD_REPORTVIEW_COLUMN"
order: 153
ekos_generated: true
ekos_estate_version: 1
---

# AD_REPORTVIEW_COLUMN

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_ReportView_Column`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  |  | Tenant |  | 0 | 0 |
| `AD_COLUMN_ID` | NUMBER(10,0) | PK | yes | Column | [AD_COLUMN](../../data-model/ad/ad_column.md) | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_REPORTVIEW_COLUMN_UU` | VARCHAR2(36 CHAR) |  |  | AD_ReportView_Column_UU |  | 0 | 0 |
| `AD_REPORTVIEW_ID` | NUMBER(10,0) | PK | yes | Report View | [AD_REPORTVIEW](../../data-model/ad/ad_reportview.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020065` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_REPORTVIEW_COLUMN.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_COLUMN](../../data-model/ad/ad_column.md) | AD_REPORTVIEW_COLUMN.AD_COLUMN_ID → AD_COLUMN.AD_COLUMN_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_REPORTVIEW_COLUMN.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_REPORTVIEW](../../data-model/ad/ad_reportview.md) | AD_REPORTVIEW_COLUMN.AD_REPORTVIEW_ID → AD_REPORTVIEW.AD_REPORTVIEW_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_REPORTVIEW_COLUMN.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_REPORTVIEW_COLUMN : ""
  AD_COLUMN ||--o{ AD_REPORTVIEW_COLUMN : ""
  AD_ORG ||--o{ AD_REPORTVIEW_COLUMN : ""
  AD_REPORTVIEW ||--o{ AD_REPORTVIEW_COLUMN : ""
  AD_USER ||--o{ AD_REPORTVIEW_COLUMN : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

15 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_REPORTVIEW_COLUMN_UU | IDEMPIERE-3862 |
| 2014-01-17T20:19 | i2.0z | `create_table` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `create_table` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |
| 2014-01-17T20:19 | i2.0z | `add_constraint` |  | IDEMPIERE-1697 |

## Notes

<!-- ekos:manual id="table.ad_reportview_column.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
