---
title: "DD_NETWORKDISTRIBUTION"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# DD_NETWORKDISTRIBUTION

Area [DD](../../data-model/dd/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.eevolution.model.X_DD_NetworkDistribution`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `VALIDFROM` | DATE |  |  | Valid from |  | 2 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `COPYFROM` | CHAR(1) |  |  | Copy From |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `VALIDTO` | DATE |  |  | Valid to |  | 2 | 0 |
| `DD_NETWORKDISTRIBUTION_ID` | NUMBER(10,0) | PK | yes | Network Distribution |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 2 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `M_CHANGENOTICE_ID` | NUMBER(10,0) |  |  | Change Notice | [M_CHANGENOTICE](../../data-model/m/m_changenotice.md) | 2 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `VALUE` | VARCHAR2(80 CHAR) |  | yes | Search Key |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 2 |
| `DOCUMENTNO` | VARCHAR2(22 CHAR) |  |  | Document No |  | 0 | 2 |
| `REVISION` | VARCHAR2(10 CHAR) |  |  | Revision |  | 2 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 2 | 0 |
| `DD_NETWORKDISTRIBUTION_UU` | VARCHAR2(36 CHAR) |  |  | DD_NetworkDistribution_UU |  | 0 | 2 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020263` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [M_CHANGENOTICE](../../data-model/m/m_changenotice.md) | DD_NETWORKDISTRIBUTION.M_CHANGENOTICE_ID → M_CHANGENOTICE.M_CHANGENOTICE_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [DD_NETWORKDISTRIBUTIONLINE](../../data-model/dd/dd_networkdistributionline.md) | DD_NETWORKDISTRIBUTIONLINE.DD_NETWORKDISTRIBUTION_ID → DD_NETWORKDISTRIBUTION.DD_NETWORKDISTRIBUTION_ID | NO ACTION |
| `I_PRODUCTPLANNING` | I_PRODUCTPLANNING.DD_NETWORKDISTRIBUTION_ID → DD_NETWORKDISTRIBUTION.DD_NETWORKDISTRIBUTION_ID | NO ACTION |
| [PP_PRODUCT_PLANNING](../../data-model/pp/pp_product_planning.md) | PP_PRODUCT_PLANNING.DD_NETWORKDISTRIBUTION_ID → DD_NETWORKDISTRIBUTION.DD_NETWORKDISTRIBUTION_ID | NO ACTION |

```mermaid
erDiagram
  DD_NETWORKDISTRIBUTION ||--o{ DD_NETWORKDISTRIBUTIONLINE : ""
  DD_NETWORKDISTRIBUTION ||--o{ I_PRODUCTPLANNING : ""
  DD_NETWORKDISTRIBUTION ||--o{ PP_PRODUCT_PLANNING : ""
  M_CHANGENOTICE ||--o{ DD_NETWORKDISTRIBUTION : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

37 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DOCUMENTNO | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | VALUE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.dd_networkdistribution.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
