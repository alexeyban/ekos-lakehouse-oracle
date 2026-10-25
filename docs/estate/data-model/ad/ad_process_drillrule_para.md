---
title: "AD_PROCESS_DRILLRULE_PARA"
order: 131
ekos_generated: true
ekos_estate_version: 1
---

# AD_PROCESS_DRILLRULE_PARA

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_Process_DrillRule_Para`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_PROCESS_DRILLRULE_ID` | NUMBER(10,0) | PK | yes | Drill Rule | [AD_PROCESS_DRILLRULE](../../data-model/ad/ad_process_drillrule.md) | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `PARAMETERDEFAULT` | VARCHAR2(255 CHAR) |  |  | Default Parameter |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `AD_PROCESS_DRILLRULE_PARA_UU` | VARCHAR2(36 CHAR) |  |  | AD_Process_DrillRule_Para_UU |  | 0 | 0 |
| `PARAMETERTODEFAULT` | VARCHAR2(255 CHAR) |  |  | Default To Parameter |  | 0 | 0 |
| `AD_PROCESS_PARA_ID` | NUMBER(10,0) | PK | yes | Process Parameter | [AD_PROCESS_PARA](../../data-model/ad/ad_process_para.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020539` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_PROCESS_DRILLRULE](../../data-model/ad/ad_process_drillrule.md) | AD_PROCESS_DRILLRULE_PARA.AD_PROCESS_DRILLRULE_ID → AD_PROCESS_DRILLRULE.AD_PROCESS_DRILLRULE_ID | NO ACTION |
| [AD_PROCESS_PARA](../../data-model/ad/ad_process_para.md) | AD_PROCESS_DRILLRULE_PARA.AD_PROCESS_PARA_ID → AD_PROCESS_PARA.AD_PROCESS_PARA_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_PROCESS_DRILLRULE ||--o{ AD_PROCESS_DRILLRULE_PARA : ""
  AD_PROCESS_PARA ||--o{ AD_PROCESS_DRILLRULE_PARA : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

34 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2022-12-23T10:59 | iD10 | `add_constraint` |  | IDEMPIERE-5302 |
| 2022-12-23T10:59 | iD10 | `add_constraint` |  | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | AD_Client_ID | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | Updated | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | AD_Org_ID | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_constraint` |  | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | IsActive | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | Created | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_constraint` |  | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | AD_Process_Para_ID | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | AD_Client_ID | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_constraint` |  | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | Description | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | AD_Org_ID | IDEMPIERE-5302 |
| 2022-07-08T17:47 | iD10 | `add_column` | UpdatedBy | IDEMPIERE-5302 |

## Notes

<!-- ekos:manual id="table.ad_process_drillrule_para.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
