---
title: "W_COUNTER"
order: 6
ekos_generated: true
ekos_estate_version: 1
---

# W_COUNTER

Area [W](../../data-model/w/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `W_COUNTER_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `PAGEURL` | VARCHAR2(120 CHAR) |  | yes |  |  | 0 | 0 |
| `REFERRER` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 0 |
| `REMOTE_HOST` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 0 |
| `REMOTE_ADDR` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `USERAGENT` | VARCHAR2(255 CHAR) |  |  |  |  | 0 | 0 |
| `ACCEPTLANGUAGE` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `W_COUNTERCOUNT_ID` | NUMBER(10,0) |  |  |  |  | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  |  |  | 0 | 0 |
| `EMAIL` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `W_COUNTER_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022906` | `IsActive in ('Y','N')` |
| `SYS_C0022909` | `Processed in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | W_COUNTER.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [W_COUNTERCOUNT](../../data-model/w/w_countercount.md) | W_COUNTER.W_COUNTERCOUNT_ID → W_COUNTERCOUNT.W_COUNTERCOUNT_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_USER ||--o{ W_COUNTER : ""
  W_COUNTERCOUNT ||--o{ W_COUNTER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

32 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | USERAGENT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | W_COUNTER_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_8_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | REFERRER | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | EMAIL | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_7_tmp | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.w_counter.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
