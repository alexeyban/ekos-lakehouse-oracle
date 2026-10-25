---
title: "C_CHARGETYPE_DOCTYPE"
order: 50
ekos_generated: true
ekos_estate_version: 1
---

# C_CHARGETYPE_DOCTYPE

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_ChargeType_DocType`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `C_CHARGETYPE_ID` | NUMBER(10,0) | PK | yes | Charge Type | [C_CHARGETYPE](../../data-model/c/c_chargetype.md) | 0 | 0 |
| `C_DOCTYPE_ID` | NUMBER(10,0) | PK | yes | Document Type | [C_DOCTYPE](../../data-model/c/c_doctype.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `ISALLOWNEGATIVE` | CHAR(1) |  | yes | Allow Negative |  | 0 | 0 |
| `ISALLOWPOSITIVE` | CHAR(1) |  | yes | Allow Positive |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `C_CHARGETYPE_DOCTYPE_UU` | VARCHAR2(36 CHAR) |  |  | C_ChargeType_DocType_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022951` | `IsActive IN ('Y','N')` |
| `SYS_C0022953` | `IsAllowNegative IN ('Y','N')` |
| `SYS_C0022954` | `IsAllowPositive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_CHARGETYPE](../../data-model/c/c_chargetype.md) | C_CHARGETYPE_DOCTYPE.C_CHARGETYPE_ID → C_CHARGETYPE.C_CHARGETYPE_ID | NO ACTION |
| [C_DOCTYPE](../../data-model/c/c_doctype.md) | C_CHARGETYPE_DOCTYPE.C_DOCTYPE_ID → C_DOCTYPE.C_DOCTYPE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  C_CHARGETYPE ||--o{ C_CHARGETYPE_DOCTYPE : ""
  C_DOCTYPE ||--o{ C_CHARGETYPE_DOCTYPE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

17 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_CHARGETYPE_DOCTYPE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | created | IDEMPIERE-709 |

## Notes

<!-- ekos:manual id="table.c_chargetype_doctype.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
