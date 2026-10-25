---
title: "AD_PRINTLABEL"
order: 122
ekos_generated: true
ekos_estate_version: 1
---

# AD_PRINTLABEL

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_PrintLabel`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PRINTLABEL_ID` | NUMBER(10,0) | PK | yes | Print Label |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `AD_TABLE_ID` | NUMBER(10,0) |  | yes | Table | [AD_TABLE](../../data-model/ad/ad_table.md) | 0 | 0 |
| `PRINTERNAME` | VARCHAR2(40 CHAR) |  |  | Printer Name |  | 0 | 0 |
| `ISLANDSCAPE` | CHAR(1) |  | yes | Landscape |  | 0 | 0 |
| `LABELHEIGHT` | NUMBER(10,0) |  | yes | Label Height |  | 0 | 0 |
| `LABELWIDTH` | NUMBER(10,0) |  | yes | Label Width |  | 0 | 0 |
| `AD_LABELPRINTER_ID` | NUMBER(10,0) |  | yes | Label printer | [AD_LABELPRINTER](../../data-model/ad/ad_labelprinter.md) | 0 | 0 |
| `AD_PRINTLABEL_UU` | VARCHAR2(36 CHAR) |  |  | AD_PrintLabel_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021862` | `IsActive in ('Y','N')` |
| `SYS_C0021864` | `IsLandscape in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LABELPRINTER](../../data-model/ad/ad_labelprinter.md) | AD_PRINTLABEL.AD_LABELPRINTER_ID → AD_LABELPRINTER.AD_LABELPRINTER_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_PRINTLABEL.AD_TABLE_ID → AD_TABLE.AD_TABLE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_PRINTLABELLINE](../../data-model/ad/ad_printlabelline.md) | AD_PRINTLABELLINE.AD_PRINTLABEL_ID → AD_PRINTLABEL.AD_PRINTLABEL_ID | NO ACTION |

```mermaid
erDiagram
  AD_LABELPRINTER ||--o{ AD_PRINTLABEL : ""
  AD_PRINTLABEL ||--o{ AD_PRINTLABELLINE : ""
  AD_TABLE ||--o{ AD_PRINTLABEL : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_printlabel.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
