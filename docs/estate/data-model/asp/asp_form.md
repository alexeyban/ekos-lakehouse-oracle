---
title: "ASP_FORM"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# ASP_FORM

Area [ASP](../../data-model/asp/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_ASP_Form`, access level 4 - System.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_FORM_ID` | NUMBER(10,0) |  | yes | Special Form | [AD_FORM](../../data-model/ad/ad_form.md) | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ASP_LEVEL_ID` | NUMBER(10,0) |  | yes | ASP Level | [ASP_LEVEL](../../data-model/asp/asp_level.md) | 0 | 0 |
| `ASP_STATUS` | CHAR(1) |  | yes | ASP Status |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `ASP_FORM_ID` | NUMBER(10,0) | PK | yes | ASP Form |  | 0 | 0 |
| `ASP_FORM_UU` | VARCHAR2(36 CHAR) |  |  | ASP_Form_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019919` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_FORM](../../data-model/ad/ad_form.md) | ASP_FORM.AD_FORM_ID → AD_FORM.AD_FORM_ID | NO ACTION |
| [ASP_LEVEL](../../data-model/asp/asp_level.md) | ASP_FORM.ASP_LEVEL_ID → ASP_LEVEL.ASP_LEVEL_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_FORM ||--o{ ASP_FORM : ""
  ASP_LEVEL ||--o{ ASP_FORM : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

19 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | ASP_FORM_UU | IDEMPIERE-3862 |
| 2017-04-29T19:25 | i4.1 | `create_index` |  | IDEMPIERE-3358 |
| 2017-04-29T19:25 | i4.1 | `create_index` |  | IDEMPIERE-3358 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | created | IDEMPIERE-709 |

## Notes

<!-- ekos:manual id="table.asp_form.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
