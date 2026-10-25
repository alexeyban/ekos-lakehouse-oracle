---
title: "HR_ATTRIBUTE"
order: 1
ekos_generated: true
ekos_estate_version: 1
---

# HR_ATTRIBUTE

Area [HR](../../data-model/hr/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.eevolution.model.X_HR_Attribute`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_RULE_ID` | NUMBER(10,0) |  |  | Rule | [AD_RULE](../../data-model/ad/ad_rule.md) | 0 | 0 |
| `AMOUNT` | NUMBER |  |  | Amount |  | 0 | 0 |
| `C_BPARTNER_ID` | NUMBER(10,0) |  |  | Business Partner | [C_BPARTNER](../../data-model/c/c_bpartner.md) | 0 | 0 |
| `COLUMNTYPE` | CHAR(1) |  |  | Column Type |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HR_ATTRIBUTE_ACCT` | NUMBER(10,0) |  |  | Payroll Attribute Account |  | 0 | 0 |
| `HR_ATTRIBUTE_ID` | NUMBER(10,0) | PK | yes | Payroll Employee Attribute |  | 0 | 0 |
| `HR_CONCEPT_ID` | NUMBER(10,0) |  | yes | Payroll Concept | [HR_CONCEPT](../../data-model/hr/hr_concept.md) | 0 | 0 |
| `HR_DEPARTMENT_ID` | NUMBER(10,0) |  |  | Payroll Department | [HR_DEPARTMENT](../../data-model/hr/hr_department.md) | 0 | 0 |
| `HR_EMPLOYEE_ID` | NUMBER(10,0) |  |  | Payroll Employee | [HR_EMPLOYEE](../../data-model/hr/hr_employee.md) | 0 | 0 |
| `HR_JOB_ID` | NUMBER(10,0) |  |  | Payroll Job | [HR_JOB](../../data-model/hr/hr_job.md) | 0 | 0 |
| `HR_PAYROLL_ID` | NUMBER(10,0) |  |  | Payroll | [HR_PAYROLL](../../data-model/hr/hr_payroll.md) | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `ISPRINTED` | CHAR(1) |  |  | Printed |  | 0 | 0 |
| `MAXVALUE` | NUMBER(10,0) |  |  | Max Value |  | 0 | 0 |
| `MINVALUE` | NUMBER(10,0) |  |  | Min Value |  | 0 | 0 |
| `QTY` | NUMBER |  |  | Quantity |  | 0 | 0 |
| `SERVICEDATE` | DATE |  |  | Service date |  | 0 | 0 |
| `TEXTMSG` | VARCHAR2(255 CHAR) |  |  | Text Message |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `VALIDFROM` | DATE |  | yes | Valid from |  | 0 | 0 |
| `VALIDTO` | DATE |  |  | Valid to |  | 0 | 0 |
| `HR_ATTRIBUTE_UU` | VARCHAR2(36 CHAR) |  |  | HR_Attribute_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022418` | `IsActive IN ('Y','N')` |
| `SYS_C0022420` | `IsPrinted IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_RULE](../../data-model/ad/ad_rule.md) | HR_ATTRIBUTE.AD_RULE_ID → AD_RULE.AD_RULE_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | HR_ATTRIBUTE.C_BPARTNER_ID → C_BPARTNER.C_BPARTNER_ID | NO ACTION |
| [C_VALIDCOMBINATION](../../data-model/c/c_validcombination.md) | HR_ATTRIBUTE.HR_ATTRIBUTE_ACCT → C_VALIDCOMBINATION.C_VALIDCOMBINATION_ID | NO ACTION |
| [HR_CONCEPT](../../data-model/hr/hr_concept.md) | HR_ATTRIBUTE.HR_CONCEPT_ID → HR_CONCEPT.HR_CONCEPT_ID | NO ACTION |
| [HR_DEPARTMENT](../../data-model/hr/hr_department.md) | HR_ATTRIBUTE.HR_DEPARTMENT_ID → HR_DEPARTMENT.HR_DEPARTMENT_ID | NO ACTION |
| [HR_EMPLOYEE](../../data-model/hr/hr_employee.md) | HR_ATTRIBUTE.HR_EMPLOYEE_ID → HR_EMPLOYEE.HR_EMPLOYEE_ID | NO ACTION |
| [HR_JOB](../../data-model/hr/hr_job.md) | HR_ATTRIBUTE.HR_JOB_ID → HR_JOB.HR_JOB_ID | NO ACTION |
| [HR_PAYROLL](../../data-model/hr/hr_payroll.md) | HR_ATTRIBUTE.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |

**Referenced by**

_None._

```mermaid
erDiagram
  AD_RULE ||--o{ HR_ATTRIBUTE : ""
  C_BPARTNER ||--o{ HR_ATTRIBUTE : ""
  C_VALIDCOMBINATION ||--o{ HR_ATTRIBUTE : ""
  HR_CONCEPT ||--o{ HR_ATTRIBUTE : ""
  HR_DEPARTMENT ||--o{ HR_ATTRIBUTE : ""
  HR_EMPLOYEE ||--o{ HR_ATTRIBUTE : ""
  HR_JOB ||--o{ HR_ATTRIBUTE : ""
  HR_PAYROLL ||--o{ HR_ATTRIBUTE : ""
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
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.hr_attribute.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
