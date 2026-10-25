---
title: "C_RFQ_TOPICSUBSCRIBER"
order: 163
ekos_generated: true
ekos_estate_version: 1
---

# C_RFQ_TOPICSUBSCRIBER

Area [C](../../data-model/c/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_C_RfQ_TopicSubscriber`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `C_RFQ_TOPICSUBSCRIBER_ID` | NUMBER(10,0) | PK | yes | RfQ Subscriber |  | 0 | 2 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 1 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 2 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `C_RFQ_TOPIC_ID` | NUMBER(10,0) |  | yes | RfQ Topic | [C_RFQ_TOPIC](../../data-model/c/c_rfq_topic.md) | 0 | 1 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  | yes | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 2 |
| `C_BPARTNER_LOCATION_ID` | NUMBER(10,0) |  | yes | Partner Location | [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | 0 | 2 |
| `AD_USER_ID` | NUMBER(10,0) |  |  | User/Contact | [AD_USER](../../data-model/ad/ad_user.md) | 0 | 2 |
| `SUBSCRIBEDATE` | DATE |  |  | Subscribe Date |  | 2 | 0 |
| `OPTOUTDATE` | DATE |  |  | Opt-out Date |  | 2 | 0 |
| `C_RFQ_TOPICSUBSCRIBER_UU` | VARCHAR2(36 CHAR) |  |  | C_RfQ_TopicSubscriber_UU |  | 0 | 2 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022433` | `IsActive in ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_USER](../../data-model/ad/ad_user.md) | C_RFQ_TOPICSUBSCRIBER.AD_USER_ID → AD_USER.AD_USER_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_RFQ_TOPICSUBSCRIBER.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | C_RFQ_TOPICSUBSCRIBER.C_BPARTNER_LOCATION_ID → C_BPARTNER_LOCATION.C_BPARTNER_LOCATION_ID | NO ACTION |
| [C_RFQ_TOPIC](../../data-model/c/c_rfq_topic.md) | C_RFQ_TOPICSUBSCRIBER.C_RFQ_TOPIC_ID → C_RFQ_TOPIC.C_RFQ_TOPIC_ID | CASCADE |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [C_RFQ_TOPICSUBSCRIBERONLY](../../data-model/c/c_rfq_topicsubscriberonly.md) | C_RFQ_TOPICSUBSCRIBERONLY.C_RFQ_TOPICSUBSCRIBER_ID → C_RFQ_TOPICSUBSCRIBER.C_RFQ_TOPICSUBSCRIBER_ID | CASCADE |

```mermaid
erDiagram
  AD_USER ||--o{ C_RFQ_TOPICSUBSCRIBER : ""
  C_BPARTNER ||--o{ C_RFQ_TOPICSUBSCRIBER : ""
  C_BPARTNER_LOCATION ||--o{ C_RFQ_TOPICSUBSCRIBER : ""
  C_RFQ_TOPIC ||--o{ C_RFQ_TOPICSUBSCRIBER : ""
  C_RFQ_TOPICSUBSCRIBER ||--o{ C_RFQ_TOPICSUBSCRIBERONLY : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 2 citation(s)

## Schema history

13 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | C_RFQ_TOPICSUBSCRIBER_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_1_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.c_rfq_topicsubscriber.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
