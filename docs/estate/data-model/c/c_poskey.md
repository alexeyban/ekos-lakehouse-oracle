---
title: "C_POSKEY"
order: 134
ekos_generated: true
ekos_estate_version: 1
---

# C_POSKEY

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 163 row(s) when profiled

Application model: `org.compiere.model.X_C_POSKey`, access level 2 - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_POSKEY_ID` | NUMBER(10,0) | PK | yes | POS Key |  | 0 | 163 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 2 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 2 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 159 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 158 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 131 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 162 | 1 |
| `C_POSKEYLAYOUT_ID` | NUMBER(10,0) |  | yes | POS Key Layout | [C_POSKEYLAYOUT](../../data-model/c/c_poskeylayout.md) | 0 | 5 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 39 |
| `M_PRODUCT_ID` | NUMBER(10,0) |  |  | Product | [M_PRODUCT](../../data-model/m/m_product.md) | 94 | 53 |
| `QTY` | NUMBER |  |  | Quantity |  | 18 | 3 |
| `AD_PRINTCOLOR_ID` | NUMBER(10,0) |  |  | Print Color | [AD_PRINTCOLOR](../../data-model/ad/ad_printcolor.md) | 150 | 4 |
| `C_POSKEY_UU` | VARCHAR2(36 CHAR) |  |  | C_POSKey_UU |  | 0 | 163 |
| `SUBKEYLAYOUT_ID` | NUMBER(10,0) |  |  | Key Layout | [C_POSKEYLAYOUT](../../data-model/c/c_poskeylayout.md) | 159 | 4 |
| `TEXT` | VARCHAR2(22 CHAR) |  |  | Description |  | 74 | 67 |
| `SPANX` | NUMBER(10,0) |  |  | Column span |  | 56 | 2 |
| `SPANY` | NUMBER(10,0) |  |  | Row Span |  | 56 | 1 |
| `AD_IMAGE_ID` | NUMBER(10,0) |  |  | Image |  | 162 | 1 |
| `AD_PRINTFONT_ID` | NUMBER(10,0) |  |  | Print Font | [AD_PRINTFONT](../../data-model/ad/ad_printfont.md) | 163 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021942` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_IMAGE](../../data-model/ad/ad_image.md) | C_POSKEY.AD_IMAGE_ID → AD_IMAGE.AD_IMAGE_ID | NO ACTION |
| [AD_PRINTCOLOR](../../data-model/ad/ad_printcolor.md) | C_POSKEY.AD_PRINTCOLOR_ID → AD_PRINTCOLOR.AD_PRINTCOLOR_ID | NO ACTION |
| [AD_PRINTFONT](../../data-model/ad/ad_printfont.md) | C_POSKEY.AD_PRINTFONT_ID → AD_PRINTFONT.AD_PRINTFONT_ID | NO ACTION |
| [C_POSKEYLAYOUT](../../data-model/c/c_poskeylayout.md) | C_POSKEY.C_POSKEYLAYOUT_ID → C_POSKEYLAYOUT.C_POSKEYLAYOUT_ID | CASCADE |
| [M_PRODUCT](../../data-model/m/m_product.md) | C_POSKEY.M_PRODUCT_ID → M_PRODUCT.M_PRODUCT_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_IMAGE ||--o{ C_POSKEY : ""
  AD_PRINTCOLOR ||--o{ C_POSKEY : ""
  AD_PRINTFONT ||--o{ C_POSKEY : ""
  C_POSKEYLAYOUT ||--o{ C_POSKEY : ""
  M_PRODUCT ||--o{ C_POSKEY : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

28 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_poskey.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
