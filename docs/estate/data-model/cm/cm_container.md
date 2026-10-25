---
title: "CM_CONTAINER"
order: 16
ekos_generated: true
ekos_estate_version: 1
---

# CM_CONTAINER

Area [CM](../../data-model/cm/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 5 row(s) when profiled

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `CM_CONTAINER_ID` | NUMBER(10,0) | PK | yes |  |  | 0 | 5 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CREATED` | DATE |  | yes |  |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `UPDATED` | DATE |  | yes |  |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes |  |  | 0 | 5 |
| `DESCRIPTION` | VARCHAR2(2000 CHAR) |  |  |  |  | 4 | 1 |
| `HELP` | VARCHAR2(2000 CHAR) |  |  |  |  | 5 | 0 |
| `CM_WEBPROJECT_ID` | NUMBER(10,0) |  | yes |  |  | 0 | 1 |
| `CM_TEMPLATE_ID` | NUMBER(10,0) |  |  |  |  | 1 | 2 |
| `TITLE` | VARCHAR2(60 CHAR) |  |  |  |  | 3 | 2 |
| `NOTICE` | VARCHAR2(2000 CHAR) |  |  |  |  | 1 | 3 |
| `CONTAINERTYPE` | CHAR(1) |  |  |  |  | 0 | 1 |
| `CONTAINERLINKURL` | VARCHAR2(60 CHAR) |  |  |  |  | 5 | 0 |
| `RELATIVEURL` | VARCHAR2(120 CHAR) |  |  |  |  | 0 | 5 |
| `PRIORITY` | NUMBER(10,0) |  |  |  |  | 0 | 1 |
| `ISINDEXED` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `ISSECURE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `META_ROBOTSTAG` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 2 |
| `META_AUTHOR` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 1 |
| `META_COPYRIGHT` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 1 |
| `META_CONTENT` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 1 |
| `META_DESCRIPTION` | VARCHAR2(2000 CHAR) |  |  |  |  | 1 | 4 |
| `META_KEYWORDS` | VARCHAR2(2000 CHAR) |  |  |  |  | 1 | 4 |
| `META_PUBLISHER` | VARCHAR2(2000 CHAR) |  |  |  |  | 0 | 1 |
| `STRUCTUREXML` | VARCHAR2(2000 CHAR) |  |  |  |  | 5 | 0 |
| `CONTAINERXML` | VARCHAR2(2000 CHAR) |  |  |  |  | 5 | 0 |
| `CM_CONTAINERLINK_ID` | NUMBER(10,0) |  |  |  |  | 5 | 0 |
| `ISSUMMARY` | CHAR(1) |  | yes |  |  | 0 | 2 |
| `META_LANGUAGE` | CHAR(2) |  |  |  |  | 2 | 2 |
| `ISVALID` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `CM_CONTAINER_UU` | VARCHAR2(36 CHAR) |  |  |  |  | 0 | 5 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0020626` | `IsActive in ('Y','N')` |
| `SYS_C0020627` | `IsSecure in ('Y','N')` |
| `SYS_C0020629` | `IsIndexed in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [CM_CONTAINER](../../data-model/cm/cm_container.md) | CM_CONTAINER.CM_CONTAINERLINK_ID → CM_CONTAINER.CM_CONTAINER_ID | SET NULL |
| [CM_TEMPLATE](../../data-model/cm/cm_template.md) | CM_CONTAINER.CM_TEMPLATE_ID → CM_TEMPLATE.CM_TEMPLATE_ID | NO ACTION |
| [CM_WEBPROJECT](../../data-model/cm/cm_webproject.md) | CM_CONTAINER.CM_WEBPROJECT_ID → CM_WEBPROJECT.CM_WEBPROJECT_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [CM_ACCESSCONTAINER](../../data-model/cm/cm_accesscontainer.md) | CM_ACCESSCONTAINER.CM_CONTAINER_ID → CM_CONTAINER.CM_CONTAINER_ID | CASCADE |
| [CM_CONTAINER](../../data-model/cm/cm_container.md) | CM_CONTAINER.CM_CONTAINERLINK_ID → CM_CONTAINER.CM_CONTAINER_ID | SET NULL |
| [CM_CONTAINERTTABLE](../../data-model/cm/cm_containerttable.md) | CM_CONTAINERTTABLE.CM_CONTAINER_ID → CM_CONTAINER.CM_CONTAINER_ID | CASCADE |
| [CM_CONTAINER_ELEMENT](../../data-model/cm/cm_container_element.md) | CM_CONTAINER_ELEMENT.CM_CONTAINER_ID → CM_CONTAINER.CM_CONTAINER_ID | CASCADE |
| [CM_CONTAINER_TRL](../../data-model/cm/cm_container_trl.md) | CM_CONTAINER_TRL.CM_CONTAINER_ID → CM_CONTAINER.CM_CONTAINER_ID | CASCADE |
| [CM_CONTAINER_URL](../../data-model/cm/cm_container_url.md) | CM_CONTAINER_URL.CM_CONTAINER_ID → CM_CONTAINER.CM_CONTAINER_ID | CASCADE |
| [CM_WEBPROJECT_DOMAIN](../../data-model/cm/cm_webproject_domain.md) | CM_WEBPROJECT_DOMAIN.CM_CONTAINER_ID → CM_CONTAINER.CM_CONTAINER_ID | CASCADE |

```mermaid
erDiagram
  CM_CONTAINER ||--o{ CM_ACCESSCONTAINER : ""
  CM_CONTAINER ||--o{ CM_CONTAINER : ""
  CM_CONTAINER ||--o{ CM_CONTAINERTTABLE : ""
  CM_CONTAINER ||--o{ CM_CONTAINER_ELEMENT : ""
  CM_CONTAINER ||--o{ CM_CONTAINER_TRL : ""
  CM_CONTAINER ||--o{ CM_CONTAINER_URL : ""
  CM_CONTAINER ||--o{ CM_WEBPROJECT_DOMAIN : ""
  CM_TEMPLATE ||--o{ CM_CONTAINER : ""
  CM_WEBPROJECT ||--o{ CM_CONTAINER : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

61 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | STRUCTUREXML | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_13_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | META_PUBLISHER | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_7_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HELP | IDEMPIERE-3862 |

## Open conflicts

| type | attribute | explanation |
|---|---|---|
| `table_without_model` | `model_class` | unexplained |

## Notes

<!-- ekos:manual id="table.cm_container.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
