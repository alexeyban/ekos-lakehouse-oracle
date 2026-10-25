---
title: "AD_SEQUENCE_NO"
order: 167
ekos_generated: true
ekos_estate_version: 1
---

# AD_SEQUENCE_NO

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Sequence_No`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_SEQUENCE_ID` | NUMBER(10,0) | PK | yes | Sequence | [AD_SEQUENCE](../../data-model/ad/ad_sequence.md) | 0 | 0 |
| `CALENDARYEARMONTH` | VARCHAR2(6 CHAR) | PK | yes |  |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) | PK | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `CURRENTNEXT` | NUMBER(10,0) |  | yes | Current Next |  | 0 | 0 |
| `AD_SEQUENCE_NO_UU` | VARCHAR2(36 CHAR) |  |  | AD_Sequence_No_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020354` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_SEQUENCE_NO.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_SEQUENCE_NO.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_SEQUENCE](../../data-model/ad/ad_sequence.md) | AD_SEQUENCE_NO.AD_SEQUENCE_ID → AD_SEQUENCE.AD_SEQUENCE_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_SEQUENCE_NO : ""
  AD_ORG ||--o{ AD_SEQUENCE_NO : ""
  AD_SEQUENCE ||--o{ AD_SEQUENCE_NO : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [NextIDByYear](../../logic/nextidbyyear.md) |

## Written by

| kind | name |
|---|---|
| Procedure | [NextIDByYear](../../logic/nextidbyyear.md) |

## Schema history

18 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2025-06-20T14:09 | iD13 | `add_constraint` |  | IDEMPIERE-6575 |
| 2025-06-20T14:09 | iD13 | `add_constraint` |  | IDEMPIERE-6575 |
| 2025-06-12T10:38 | iD13 | `modify_column` | SequenceKey | IDEMPIERE-6575 |
| 2025-06-12T10:38 | iD13 | `modify_column` | SequenceKey | IDEMPIERE-6575 |
| 2025-06-12T10:38 | iD13 | `rename_column` | CalendarYearMonth | IDEMPIERE-6575 |
| 2025-06-12T10:38 | iD13 | `rename_column` | CalendarYearMonth | IDEMPIERE-6575 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_SEQUENCE_NO_UU | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `model_column_missing` | `columns.SequenceKey` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_sequence_no.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
