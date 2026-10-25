---
title: "EXP_PROCESSORPARAMETER"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# EXP_PROCESSORPARAMETER

Area [EXP](../../data-model/exp/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 7 row(s) when profiled

Application model: `org.compiere.model.X_EXP_ProcessorParameter`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `EXP_PROCESSORPARAMETER_ID` | NUMBER(10,0) | PK | yes | Processor Parameter |  | 0 | 7 |
| `EXP_PROCESSOR_ID` | NUMBER(10,0) |  | yes | Export Processor | [EXP_PROCESSOR](../../data-model/exp/exp_processor.md) | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 6 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 6 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 7 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 7 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 2 |
| `PARAMETERVALUE` | VARCHAR2(60 CHAR) |  |  | Parameter Value |  | 0 | 7 |
| `EXP_PROCESSORPARAMETER_UU` | VARCHAR2(36 CHAR) |  |  | EXP_ProcessorParameter_UU |  | 0 | 7 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020854` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [EXP_PROCESSOR](../../data-model/exp/exp_processor.md) | EXP_PROCESSORPARAMETER.EXP_PROCESSOR_ID → EXP_PROCESSOR.EXP_PROCESSOR_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  EXP_PROCESSOR ||--o{ EXP_PROCESSORPARAMETER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

34 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | VALUE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | EXP_PROCESSORPARAMETER_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.exp_processorparameter.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
