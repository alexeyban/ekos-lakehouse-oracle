---
title: "W_CLICK"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# W_CLICK

Area [W](../../data-model/w/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `W_CLICK_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `CREATED` | DATE |  | yes |  |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 0 |
| `TARGETURL` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 0 |
| `REFERRER` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 0 |
| `REMOTE_HOST` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 0 |
| `REMOTE_ADDR` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `USERAGENT` | VARCHAR2(255 CHAR) |  |  |  |  | 0 | 0 |
| `ACCEPTLANGUAGE` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes |  |  | 0 | 0 |
| `W_CLICKCOUNT_ID` | NUMBER(10,0) |  |  |  |  | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  |  |  |  | 0 | 0 |
| `EMAIL` | VARCHAR2(60 CHAR) |  |  |  |  | 0 | 0 |
| `W_CLICK_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021004` | `Processed in ('Y','N')` |
| `SYS_C0021006` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | W_CLICK.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [W_CLICKCOUNT](../../data-model/w/w_clickcount.md) | W_CLICK.W_CLICKCOUNT_ID → W_CLICKCOUNT.W_CLICKCOUNT_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_USER ||--o{ W_CLICK : ""
  W_CLICKCOUNT ||--o{ W_CLICK : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Read by

| kind | name |
|---|---|
| View | `RV_CLICK_MONTH` |
| View | `RV_CLICK_UNPROCESSED` |
| View | `rv_click_month` |
| View | `rv_click_unprocessed` |

## Schema history

30 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_8_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | USERAGENT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_8_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | TARGETURL | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.w_click.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
