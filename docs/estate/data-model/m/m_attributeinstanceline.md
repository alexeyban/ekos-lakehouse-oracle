---
title: "M_ATTRIBUTEINSTANCELINE"
order: 3
ekos_generated: true
ekos_estate_version: 1
---

# M_ATTRIBUTEINSTANCELINE

Area [M](../../data-model/m/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_M_AttributeInstanceLine`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `LINE` | NUMBER(10,0) |  | yes | Line No |  | 0 | 0 |
| `M_ATTRIBUTEINSTANCELINE_ID` | NUMBER(10,0) | PK | yes | Attribute Instance Values |  | 0 | 0 |
| `M_ATTRIBUTEINSTANCELINE_UU` | VARCHAR2(36 CHAR) |  | yes | M_AttributeInstanceLine_UU |  | 0 | 0 |
| `M_ATTRIBUTEINSTANCE_UU` | VARCHAR2(36 CHAR) |  | yes | M_AttributeInstance_UU |  | 0 | 0 |
| `M_ATTRIBUTEVALUE_ID` | NUMBER(10,0) |  | yes | Attribute Value | [M_ATTRIBUTEVALUE](../../data-model/m/m_attributevalue.md) | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021726` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_CLIENT](../../data-model/ad/ad_client.md) | M_ATTRIBUTEINSTANCELINE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | M_ATTRIBUTEINSTANCELINE.AD_ORG_ID → AD_ORG.AD_ORG_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | M_ATTRIBUTEINSTANCELINE.CREATEDBY → AD_USER.AD_USER_ID | NO ACTION |
| [M_ATTRIBUTEINSTANCE](../../data-model/m/m_attributeinstance.md) | M_ATTRIBUTEINSTANCELINE.M_ATTRIBUTEINSTANCE_UU → M_ATTRIBUTEINSTANCE.M_ATTRIBUTEINSTANCE_UU | CASCADE |
| [M_ATTRIBUTEVALUE](../../data-model/m/m_attributevalue.md) | M_ATTRIBUTEINSTANCELINE.M_ATTRIBUTEVALUE_ID → M_ATTRIBUTEVALUE.M_ATTRIBUTEVALUE_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_CLIENT ||--o{ M_ATTRIBUTEINSTANCELINE : ""
  AD_ORG ||--o{ M_ATTRIBUTEINSTANCELINE : ""
  AD_USER ||--o{ M_ATTRIBUTEINSTANCELINE : ""
  M_ATTRIBUTEINSTANCE ||--o{ M_ATTRIBUTEINSTANCELINE : ""
  M_ATTRIBUTEVALUE ||--o{ M_ATTRIBUTEINSTANCELINE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_app, deleted_by_users, deleted_by_cascade**
- change log: **recorded**
- evidence: 3 citation(s)

## Schema history

18 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2024-02-27T16:13 | iD12 | `modify_column` | M_AttributeInstanceLine_UU | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `modify_column` | M_AttributeInstanceLine_UU | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `create_table` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `modify_column` | M_AttributeInstanceLine_UU | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `modify_column` | M_AttributeInstanceLine_UU | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |
| 2024-02-27T16:13 | iD12 | `add_constraint` |  | IDEMPIERE-5859 |

## Notes

<!-- ekos:manual id="table.m_attributeinstanceline.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
