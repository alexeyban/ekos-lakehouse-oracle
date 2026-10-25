---
title: "AD_WF_ACTIVITYAPPROVER"
order: 235
ekos_generated: true
ekos_estate_version: 1
---

# AD_WF_ACTIVITYAPPROVER

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_WF_ActivityApprover`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_WF_ACTIVITYAPPROVER_ID` | NUMBER(10,0) | PK | yes | Workflow Activity Approver |  | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `AD_WF_ACTIVITYAPPROVER_UU` | VARCHAR2(36 CHAR) |  |  | AD_WF_ActivityApprover_UU |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `AD_WF_ACTIVITY_ID` | NUMBER(10,0) |  | yes | Workflow Activity | [AD_WF_ACTIVITY](../../data-model/ad/ad_wf_activity.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022875` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | AD_WF_ACTIVITYAPPROVER.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [AD_WF_ACTIVITY](../../data-model/ad/ad_wf_activity.md) | AD_WF_ACTIVITYAPPROVER.AD_WF_ACTIVITY_ID → AD_WF_ACTIVITY.AD_WF_ACTIVITY_ID | CASCADE |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_USER ||--o{ AD_WF_ACTIVITYAPPROVER : ""
  AD_WF_ACTIVITY ||--o{ AD_WF_ACTIVITYAPPROVER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_cascade**
- change log: **not_recorded**
- evidence: 2 citation(s)

## Schema history

31 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_WF_ACTIVITYAPPROVER_UU | IDEMPIERE-3862 |
| 2017-08-08T18:30 | i4.1 | `add_column` | UpdatedBy | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_constraint` |  | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_column` | CreatedBy | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_column` | AD_Org_ID | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_column` | IsActive | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_constraint` |  | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_constraint` |  | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_column` | AD_WF_Activity_ID | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_column` | AD_Client_ID | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_constraint` |  | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `create_index` |  | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `add_column` | IsActive | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `create_index` |  | IDEMPIERE-3446 |
| 2017-08-08T18:30 | i4.1 | `create_table` |  | IDEMPIERE-3446 |

## Notes

<!-- ekos:manual id="table.ad_wf_activityapprover.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
