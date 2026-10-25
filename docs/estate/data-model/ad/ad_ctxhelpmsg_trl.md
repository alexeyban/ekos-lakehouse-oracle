---
title: "AD_CTXHELPMSG_TRL"
order: 36
ekos_generated: true
ekos_estate_version: 1
---

# AD_CTXHELPMSG_TRL

Area [AD](../../data-model/ad/index.md) · class **translation** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_CTXHELPMSG_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `AD_CTXHELPMSG_TRL_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `ISTRANSLATED` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `MSGTEXT` | VARCHAR2(2000 CHAR) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019967` | `IsActive IN ('Y','N')` |
| `SYS_C0019968` | `IsTranslated IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CTXHELPMSG](../../data-model/ad/ad_ctxhelpmsg.md) | AD_CTXHELPMSG_TRL.AD_CTXHELPMSG_ID → AD_CTXHELPMSG.AD_CTXHELPMSG_ID | CASCADE |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_CTXHELPMSG_TRL.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CTXHELPMSG ||--o{ AD_CTXHELPMSG_TRL : ""
  AD_LANGUAGE ||--o{ AD_CTXHELPMSG_TRL : ""
```

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **not_recorded**
- evidence: 5 citation(s)

## Schema history

33 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | MSGTEXT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_LANGUAGE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | MSGTEXT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | MSGTEXT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_CTXHELPMSG_TRL_UU | IDEMPIERE-3862 |
| 2018-09-08T16:18 | i5.1 | `modify_column` | Updated | IDEMPIERE-2652 |
| 2018-09-08T16:18 | i5.1 | `modify_column` | Created | IDEMPIERE-2652 |
| 2018-09-08T16:18 | i5.1 | `modify_column` | Created | IDEMPIERE-2652 |
| 2018-09-08T16:18 | i5.1 | `modify_column` | Updated | IDEMPIERE-2652 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_ctxhelpmsg_trl.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
