---
title: "C_TAXPROVIDER"
order: 186
ekos_generated: true
ekos_estate_version: 1
---

# C_TAXPROVIDER

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_TaxProvider`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `ACCOUNT` | VARCHAR2(60 CHAR) |  |  | Account |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `C_TAXPROVIDER_ID` | NUMBER(10,0) | PK | yes | Tax Provider |  | 0 | 0 |
| `C_TAXPROVIDER_UU` | VARCHAR2(36 CHAR) |  |  | C_TaxProvider_UU |  | 0 | 0 |
| `C_TAXPROVIDERCFG_ID` | NUMBER(10,0) |  | yes | Tax Provider Configuration | [C_TAXPROVIDERCFG](../../data-model/c/c_taxprovidercfg.md) | 0 | 0 |
| `COMPANYCODE` | VARCHAR2(60 CHAR) |  |  | Company Code |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `LICENSE` | VARCHAR2(60 CHAR) |  |  | License |  | 0 | 0 |
| `NAME` | VARCHAR2(120 CHAR) |  | yes | Name |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `SEQNO` | NUMBER(10,0) |  | yes | Sequence |  | 0 | 0 |
| `VALIDATECONNECTION` | CHAR(1) |  |  | Validate Connection |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021398` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | C_TAXPROVIDER.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | C_TAXPROVIDER.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | C_TAXPROVIDER.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |
| [C_TAXPROVIDERCFG](../../data-model/c/c_taxprovidercfg.md) | C_TAXPROVIDER.C_TAXPROVIDERCFG_ID → C_TAXPROVIDERCFG.C_TAXPROVIDERCFG_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_INVOICETAX](../../data-model/c/c_invoicetax.md) | C_INVOICETAX.C_TAXPROVIDER_ID → C_TAXPROVIDER.C_TAXPROVIDER_ID | NO ACTION |
| [C_ORDERTAX](../../data-model/c/c_ordertax.md) | C_ORDERTAX.C_TAXPROVIDER_ID → C_TAXPROVIDER.C_TAXPROVIDER_ID | NO ACTION |
| [C_TAX](../../data-model/c/c_tax.md) | C_TAX.C_TAXPROVIDER_ID → C_TAXPROVIDER.C_TAXPROVIDER_ID | NO ACTION |
| [M_RMATAX](../../data-model/m/m_rmatax.md) | M_RMATAX.C_TAXPROVIDER_ID → C_TAXPROVIDER.C_TAXPROVIDER_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ C_TAXPROVIDER : ""
  AD_ORG ||--o{ C_TAXPROVIDER : ""
  AD_USER ||--o{ C_TAXPROVIDER : ""
  C_TAXPROVIDER ||--o{ C_INVOICETAX : ""
  C_TAXPROVIDER ||--o{ C_ORDERTAX : ""
  C_TAXPROVIDER ||--o{ C_TAX : ""
  C_TAXPROVIDER ||--o{ M_RMATAX : ""
  C_TAXPROVIDERCFG ||--o{ C_TAXPROVIDER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

61 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | COMPANYCODE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | ACCOUNT | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_TAXPROVIDER_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_taxprovider.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
