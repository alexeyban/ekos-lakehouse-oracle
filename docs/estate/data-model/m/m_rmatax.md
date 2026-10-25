---
title: "M_RMATAX"
order: 101
ekos_generated: true
ekos_estate_version: 1
---

# M_RMATAX

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_RMATax`, access level 1 - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `C_TAX_ID` | NUMBER(10,0) | PK | yes | Tax | [C_TAX](../../data-model/c/c_tax.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `ISTAXINCLUDED` | CHAR(1) |  | yes | Price includes Tax |  | 0 | 0 |
| `M_RMA_ID` | NUMBER(10,0) | PK | yes | RMA | [M_RMA](../../data-model/m/m_rma.md) | 0 | 0 |
| `M_RMATAX_UU` | VARCHAR2(36 CHAR) |  |  | M_RMATax_UU |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  | yes | Processed |  | 0 | 0 |
| `TAXAMT` | NUMBER |  | yes | Tax Amount |  | 0 | 0 |
| `TAXBASEAMT` | NUMBER |  | yes | Tax base Amount |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `C_TAXPROVIDER_ID` | NUMBER(10,0) |  |  | Tax Provider | [C_TAXPROVIDER](../../data-model/c/c_taxprovider.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020050` | `IsTaxIncluded IN ('Y','N')` |
| `SYS_C0020052` | `IsActive IN ('Y','N')` |
| `SYS_C0020053` | `Processed IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [C_TAX](../../data-model/c/c_tax.md) | M_RMATAX.C_TAX_ID → C_TAX.C_TAX_ID | NO ACTION |
| [C_TAXPROVIDER](../../data-model/c/c_taxprovider.md) | M_RMATAX.C_TAXPROVIDER_ID → C_TAXPROVIDER.C_TAXPROVIDER_ID | NO ACTION |
| [M_RMA](../../data-model/m/m_rma.md) | M_RMATAX.M_RMA_ID → M_RMA.M_RMA_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  C_TAX ||--o{ M_RMATAX : ""
  C_TAXPROVIDER ||--o{ M_RMATAX : ""
  M_RMA ||--o{ M_RMATAX : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **not_recorded**
- evidence: 4 citation(s)

## Schema history

29 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | M_RMATAX_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-05-02T10:09 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | created | IDEMPIERE-709 |
| 2014-04-17T15:00 | i2.0 | `modify_column` | updated | IDEMPIERE-709 |
| 2013-12-11T17:45 | i2.0 | `drop_constraint` |  | IDEMPIERE-1132 |
| 2013-12-11T17:45 | i2.0 | `add_constraint` |  | IDEMPIERE-1132 |

## Notes

<!-- ekos:manual id="table.m_rmatax.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
