---
title: "AD_PRINTLABELLINE"
order: 123
ekos_generated: true
ekos_estate_version: 1
---

# AD_PRINTLABELLINE

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_PrintLabelLine`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PRINTLABELLINE_ID` | NUMBER(10,0) | PK | yes | Print Label Line |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_PRINTLABEL_ID` | NUMBER(10,0) |  | yes | Print Label | [AD_PRINTLABEL](../../data-model/ad/ad_printlabel.md) | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 0 |
| `LABELFORMATTYPE` | CHAR(1) |  | yes | Label Format Type |  | 0 | 0 |
| `PRINTNAME` | VARCHAR2(60 CHAR) |  |  | Print Text |  | 0 | 0 |
| `AD_COLUMN_ID` | NUMBER(10,0) |  |  | Column | [AD_COLUMN](../../data-model/ad/ad_column.md) | 0 | 0 |
| `AD_LABELPRINTERFUNCTION_ID` | NUMBER(10,0) |  | yes | Label printer Function | [AD_LABELPRINTERFUNCTION](../../data-model/ad/ad_labelprinterfunction.md) | 0 | 0 |
| `XPOSITION` | NUMBER(10,0) |  | yes | X Position |  | 0 | 0 |
| `YPOSITION` | NUMBER(10,0) |  | yes | Y Position |  | 0 | 0 |
| `AD_PRINTLABELLINE_UU` | VARCHAR2(36 CHAR) |  |  | AD_PrintLabelLine_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0019424` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_COLUMN](../../data-model/ad/ad_column.md) | AD_PRINTLABELLINE.AD_COLUMN_ID → AD_COLUMN.AD_COLUMN_ID | NO ACTION |
| [AD_LABELPRINTERFUNCTION](../../data-model/ad/ad_labelprinterfunction.md) | AD_PRINTLABELLINE.AD_LABELPRINTERFUNCTION_ID → AD_LABELPRINTERFUNCTION.AD_LABELPRINTERFUNCTION_ID | NO ACTION |
| [AD_PRINTLABEL](../../data-model/ad/ad_printlabel.md) | AD_PRINTLABELLINE.AD_PRINTLABEL_ID → AD_PRINTLABEL.AD_PRINTLABEL_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_PRINTLABELLINE_TRL](../../data-model/ad/ad_printlabelline_trl.md) | AD_PRINTLABELLINE_TRL.AD_PRINTLABELLINE_ID → AD_PRINTLABELLINE.AD_PRINTLABELLINE_ID | NO ACTION |

```mermaid
erDiagram
  AD_COLUMN ||--o{ AD_PRINTLABELLINE : ""
  AD_LABELPRINTERFUNCTION ||--o{ AD_PRINTLABELLINE : ""
  AD_PRINTLABEL ||--o{ AD_PRINTLABELLINE : ""
  AD_PRINTLABELLINE ||--o{ AD_PRINTLABELLINE_TRL : ""
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
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_PRINTLABELLINE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PRINTNAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_printlabelline.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
