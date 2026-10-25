---
title: "M_SHIPPINGPROCESSORCFG"
order: 114
ekos_generated: true
ekos_estate_version: 1
---

# M_SHIPPINGPROCESSORCFG

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_M_ShippingProcessorCfg`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 1 |
| `HOSTADDRESS` | VARCHAR2(60 CHAR) |  | yes | Host Address |  | 0 | 1 |
| `HOSTPORT` | NUMBER(10,0) |  | yes | Host port |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `PROXYADDRESS` | VARCHAR2(60 CHAR) |  |  | Proxy address |  | 1 | 0 |
| `PROXYLOGON` | VARCHAR2(60 CHAR) |  |  | Proxy logon |  | 1 | 0 |
| `PROXYPASSWORD` | VARCHAR2(60 CHAR) |  |  | Proxy password |  | 1 | 0 |
| `PROXYPORT` | NUMBER(10,0) |  |  | Proxy port |  | 0 | 1 |
| `SERVICEPATH` | VARCHAR2(60 CHAR) |  |  | Service Path |  | 1 | 0 |
| `SHIPPINGPROCESSORCLASS` | VARCHAR2(60 CHAR) |  |  | Shipping Processor Class |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `M_SHIPPINGPROCESSORCFG_ID` | NUMBER(10,0) | PK | yes | Shipping Processor Configuration |  | 0 | 1 |
| `M_SHIPPINGPROCESSORCFG_UU` | VARCHAR2(36 CHAR) |  |  | M_ShippingProcessorCfg_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022847` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [M_SHIPPERCFG](../../data-model/m/m_shippercfg.md) | M_SHIPPERCFG.M_SHIPPINGPROCESSORCFG_ID → M_SHIPPINGPROCESSORCFG.M_SHIPPINGPROCESSORCFG_ID | NO ACTION |
| [M_SHIPPINGPROCESSOR](../../data-model/m/m_shippingprocessor.md) | M_SHIPPINGPROCESSOR.M_SHIPPINGPROCESSORCFG_ID → M_SHIPPINGPROCESSORCFG.M_SHIPPINGPROCESSORCFG_ID | NO ACTION |

```mermaid
erDiagram
  M_SHIPPINGPROCESSORCFG ||--o{ M_SHIPPERCFG : ""
  M_SHIPPINGPROCESSORCFG ||--o{ M_SHIPPINGPROCESSOR : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

49 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_9_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HOSTADDRESS | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PROXYLOGON | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HOSTADDRESS | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_constraint` |  | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PROXYADDRESS | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.m_shippingprocessorcfg.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
