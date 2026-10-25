---
title: "PA_DASHBOARDPREFERENCE"
order: 8
ekos_generated: true
ekos_estate_version: 1
---

# PA_DASHBOARDPREFERENCE

Area [PA](../../data-model/pa/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_PA_DashboardPreference`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_ROLE_ID` | NUMBER(10,0) |  | yes | Role | [AD_ROLE](../../data-model/ad/ad_role.md) | 0 | 0 |
| `AD_USER_ID` | NUMBER(10,0) |  | yes | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 0 |
| `COLUMNNO` | NUMBER(10,0) |  |  | Column No |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `ISCOLLAPSEDBYDEFAULT` | CHAR(1) |  | yes | Collapsed By Default |  | 0 | 0 |
| `ISSHOWINDASHBOARD` | CHAR(1) |  | yes | Show in Dashboard |  | 0 | 0 |
| `LINE` | NUMBER |  |  | Line No |  | 0 | 0 |
| `PA_DASHBOARDCONTENT_ID` | NUMBER(10,0) |  | yes | Dashboard Content | [PA_DASHBOARDCONTENT](../../data-model/pa/pa_dashboardcontent.md) | 0 | 0 |
| `PA_DASHBOARDPREFERENCE_ID` | NUMBER(10,0) | PK | yes | Dashboard Preference |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `PA_DASHBOARDPREFERENCE_UU` | VARCHAR2(36 CHAR) |  |  | PA_DashboardPreference_UU |  | 0 | 0 |
| `FLEXGROW` | NUMBER(10,0) |  | yes | Flex Grow |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020906` | `IsActive IN ('Y','N')` |
| `SYS_C0020907` | `IsCollapsedByDefault IN ('Y','N')` |
| `SYS_C0020908` | `IsShowInDashboard IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_ROLE](../../data-model/ad/ad_role.md) | PA_DASHBOARDPREFERENCE.AD_ROLE_ID → AD_ROLE.AD_ROLE_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | PA_DASHBOARDPREFERENCE.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [PA_DASHBOARDCONTENT](../../data-model/pa/pa_dashboardcontent.md) | PA_DASHBOARDPREFERENCE.PA_DASHBOARDCONTENT_ID → PA_DASHBOARDCONTENT.PA_DASHBOARDCONTENT_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_ROLE ||--o{ PA_DASHBOARDPREFERENCE : ""
  AD_USER ||--o{ PA_DASHBOARDPREFERENCE : ""
  PA_DASHBOARDCONTENT ||--o{ PA_DASHBOARDPREFERENCE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

23 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2026-03-03T11:41 | iD13 | `create_index` |  | IDEMPIERE-6888 |
| 2026-03-03T11:41 | iD13 | `create_index` |  | IDEMPIERE-6888 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2022-08-18T11:13 | iD10 | `add_column` | FlexGrow | IDEMPIERE-5389 |
| 2022-08-18T11:13 | iD10 | `add_column` | FlexGrow | IDEMPIERE-5389 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PA_DASHBOARDPREFERENCE_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.pa_dashboardpreference.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
