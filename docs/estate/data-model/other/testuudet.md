---
title: "TESTUUDET"
order: 7
ekos_generated: true
ekos_estate_version: 1
---

# TESTUUDET

Area [OTHER](../../data-model/other/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 3 row(s) when profiled

Application model: `org.compiere.model.X_TestUUDet`, access level 7 - System - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ALTTESTUU_UU` | VARCHAR2(36 CHAR) |  |  | Alternate Test UU |  | 3 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 3 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 3 |
| `TESTUUDET_UU` | VARCHAR2(36 CHAR) | PK | yes | TestUUDet_UU |  | 0 | 3 |
| `TESTUU_UU` | VARCHAR2(36 CHAR) |  | yes | Test UU |  | 0 | 2 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 3 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `TESTUU_UUS` | VARCHAR2(2000 CHAR) |  |  | Multi Test UU |  | 3 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022085` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | TESTUUDET.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | TESTUUDET.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | TESTUUDET.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |
| [TESTUU](../../data-model/other/testuu.md) | TESTUUDET.ALTTESTUU_UU → TESTUU.TESTUU_UU | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ TESTUUDET : ""
  AD_ORG ||--o{ TESTUUDET : ""
  AD_USER ||--o{ TESTUUDET : ""
  TESTUU ||--o{ TESTUUDET : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

20 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_column` | TestUU_UUs | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `modify_column` | AltTestUU_UU | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `modify_column` | AltTestUU_UU | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `modify_column` | AltTestUU_UU | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `create_table` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_column` | TestUU_UUs | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `create_table` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-24T16:37 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |

## Notes

<!-- ekos:manual id="table.testuudet.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
