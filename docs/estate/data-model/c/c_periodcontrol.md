---
title: "C_PERIODCONTROL"
order: 131
ekos_generated: true
ekos_estate_version: 1
---

# C_PERIODCONTROL

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 10464 row(s) when profiled

Application model: `org.compiere.model.X_C_PeriodControl`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_PERIODCONTROL_ID` | NUMBER(10,0) | PK | yes | Period Control |  | 0 | 10464 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 3615 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 3636 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 2 |
| `C_PERIOD_ID` | NUMBER(10,0) |  | yes | Period | [C_PERIOD](../../data-model/c/c_period.md) | 0 | 360 |
| `DOCBASETYPE` | CHAR(3) |  | yes | Document Base Type |  | 0 | 32 |
| `PERIODSTATUS` | CHAR(1) |  |  | Period Status |  | 0 | 4 |
| `PERIODACTION` | CHAR(1) |  | yes | Period Action |  | 0 | 2 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 1380 | 1 |
| `C_PERIODCONTROL_UU` | VARCHAR2(36 CHAR) |  |  | C_PeriodControl_UU |  | 0 | 10464 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019993` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_PERIOD](../../data-model/c/c_period.md) | C_PERIODCONTROL.C_PERIOD_ID → C_PERIOD.C_PERIOD_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  C_PERIOD ||--o{ C_PERIODCONTROL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

7 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_PERIODCONTROL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_periodcontrol.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
