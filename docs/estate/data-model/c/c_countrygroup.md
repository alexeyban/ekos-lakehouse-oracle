---
title: "C_COUNTRYGROUP"
order: 64
ekos_generated: true
ekos_estate_version: 1
---

# C_COUNTRYGROUP

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_C_CountryGroup`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `C_COUNTRYGROUP_ID` | NUMBER(10,0) | PK | yes | Country Group |  | 0 | 0 |
| `C_COUNTRYGROUP_UU` | VARCHAR2(36 CHAR) |  |  | C_CountryGroup_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `DATEFROM` | DATE |  |  | Date From |  | 0 | 0 |
| `DATETO` | DATE |  |  | Date To |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022294` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | C_COUNTRYGROUP.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | C_COUNTRYGROUP.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | C_COUNTRYGROUP.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_COUNTRYGROUPCOUNTRY](../../data-model/c/c_countrygroupcountry.md) | C_COUNTRYGROUPCOUNTRY.C_COUNTRYGROUP_ID → C_COUNTRYGROUP.C_COUNTRYGROUP_ID | NO ACTION |
| [C_COUNTRYGROUP_TRL](../../data-model/c/c_countrygroup_trl.md) | C_COUNTRYGROUP_TRL.C_COUNTRYGROUP_ID → C_COUNTRYGROUP.C_COUNTRYGROUP_ID | NO ACTION |
| [C_TAX](../../data-model/c/c_tax.md) | C_TAX.C_COUNTRYGROUPFROM_ID → C_COUNTRYGROUP.C_COUNTRYGROUP_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ C_COUNTRYGROUP : ""
  AD_ORG ||--o{ C_COUNTRYGROUP : ""
  AD_USER ||--o{ C_COUNTRYGROUP : ""
  C_COUNTRYGROUP ||--o{ C_COUNTRYGROUPCOUNTRY : ""
  C_COUNTRYGROUP ||--o{ C_COUNTRYGROUP_TRL : ""
  C_COUNTRYGROUP ||--o{ C_TAX : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

15 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_COUNTRYGROUP_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | VALUE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |
| 2014-08-07T18:40 | i2.0z | `create_table` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `create_table` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |
| 2014-08-07T18:40 | i2.0z | `add_constraint` |  | IDEMPIERE-2127 |

## Notes

<!-- ekos:manual id="table.c_countrygroup.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
