---
title: "WS_WEBSERVICE_PARA"
order: 7
ekos_generated: true
ekos_estate_version: 1
---

# WS_WEBSERVICE_PARA

Area [WS](../../data-model/ws/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 46 row(s) when profiled

Application model: `org.idempiere.webservices.model.X_WS_WebService_Para`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `CONSTANTVALUE` | VARCHAR2(2000 CHAR) |  |  | Constant Value |  | 16 | 17 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 27 |
| `CREATEDBY` | NUMBER(10,0) |  |  | Created By |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `PARAMETERNAME` | VARCHAR2(60 CHAR) |  |  | Parameter Name |  | 0 | 13 |
| `PARAMETERTYPE` | CHAR(1) |  | yes | Parameter Type |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 27 |
| `UPDATEDBY` | NUMBER(10,0) |  |  | Updated By |  | 0 | 1 |
| `WS_WEBSERVICE_PARA_ID` | NUMBER(10,0) | PK | yes | Web Service Parameters |  | 0 | 46 |
| `WS_WEBSERVICETYPE_ID` | NUMBER(10,0) |  | yes | Web Service Type | [WS_WEBSERVICETYPE](../../data-model/ws/ws_webservicetype.md) | 0 | 15 |
| `WS_WEBSERVICE_PARA_UU` | VARCHAR2(36 CHAR) |  |  | WS_WebService_Para_UU |  | 0 | 46 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020742` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [WS_WEBSERVICETYPE](../../data-model/ws/ws_webservicetype.md) | WS_WEBSERVICE_PARA.WS_WEBSERVICETYPE_ID → WS_WEBSERVICETYPE.WS_WEBSERVICETYPE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  WS_WEBSERVICETYPE ||--o{ WS_WEBSERVICE_PARA : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

35 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PARAMETERNAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | CONSTANTVALUE | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | WS_WEBSERVICE_PARA_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2017-02-01T18:23 | i4.1 | `modify_column` | ConstantValue | IDEMPIERE-3291 |
| 2017-02-01T18:23 | i4.1 | `modify_column` | ConstantValue | IDEMPIERE-3291 |
| 2015-07-01T19:55 | i2.1 | `modify_column` | ConstantValue | IDEMPIERE-2635 |
| 2015-07-01T19:55 | i2.1 | `modify_column` | ConstantValue | IDEMPIERE-2635 |

## Notes

<!-- ekos:manual id="table.ws_webservice_para.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
