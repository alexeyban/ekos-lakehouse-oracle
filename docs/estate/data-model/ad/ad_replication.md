---
title: "AD_REPLICATION"
order: 145
ekos_generated: true
ekos_estate_version: 1
---

# AD_REPLICATION

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 1 row(s) when profiled

Application model: `org.compiere.model.X_AD_Replication`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_REPLICATION_ID` | NUMBER(10,0) | PK | yes | Replication |  | 0 | 1 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 1 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 1 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  | Comment/Help |  | 0 | 1 |
| `HOSTADDRESS` | VARCHAR2(60 CHAR) |  | yes | Host Address |  | 0 | 1 |
| `HOSTPORT` | NUMBER(10,0) |  | yes | Host port |  | 0 | 1 |
| `AD_REPLICATIONSTRATEGY_ID` | NUMBER(10,0) |  | yes | Replication Strategy | [AD_REPLICATIONSTRATEGY](../../data-model/ad/ad_replicationstrategy.md) | 0 | 1 |
| `ISRMIOVERHTTP` | CHAR(1) |  | yes | Tunnel via HTTP |  | 0 | 1 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 1 |
| `IDRANGESTART` | NUMBER |  |  | ID Range Start |  | 0 | 1 |
| `IDRANGEEND` | NUMBER |  |  | ID Range End |  | 0 | 1 |
| `REMOTE_CLIENT_ID` | NUMBER(10,0) |  |  | Remote Tenant |  | 0 | 1 |
| `REMOTE_ORG_ID` | NUMBER(10,0) |  |  | Remote Organization |  | 0 | 1 |
| `PREFIX` | VARCHAR2(10 CHAR) |  |  | Prefix |  | 0 | 1 |
| `SUFFIX` | VARCHAR2(10 CHAR) |  |  | Suffix |  | 1 | 0 |
| `DATELASTRUN` | DATE |  |  | Date Last Run |  | 1 | 0 |
| `AD_REPLICATION_UU` | VARCHAR2(36 CHAR) |  |  | AD_Replication_UU |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022271` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | AD_REPLICATION.REMOTE_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_REPLICATION.REMOTE_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_REPLICATIONSTRATEGY](../../data-model/ad/ad_replicationstrategy.md) | AD_REPLICATION.AD_REPLICATIONSTRATEGY_ID → AD_REPLICATIONSTRATEGY.AD_REPLICATIONSTRATEGY_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_REPLICATION_RUN](../../data-model/ad/ad_replication_run.md) | AD_REPLICATION_RUN.AD_REPLICATION_ID → AD_REPLICATION.AD_REPLICATION_ID | CASCADE |

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_REPLICATION : ""
  AD_ORG ||--o{ AD_REPLICATION : ""
  AD_REPLICATION ||--o{ AD_REPLICATION_RUN : ""
  AD_REPLICATIONSTRATEGY ||--o{ AD_REPLICATION : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

33 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_REPLICATION_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HOSTADDRESS | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `mandatory_but_nullable` | `columns.Remote_Client_ID.nullable` | unexplained |
| `mandatory_but_nullable` | `columns.Remote_Org_ID.nullable` | unexplained |

## Notes

<!-- ekos:manual id="table.ad_replication.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
