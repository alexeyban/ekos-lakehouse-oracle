---
title: "HR_PAYROLL"
order: 14
ekos_generated: true
ekos_estate_version: 1
---

# HR_PAYROLL

Area [HR](../../data-model/hr/index.md) · class **business** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.eevolution.model.X_HR_Payroll`, access level 3 - Client - Org.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `VALUE` | VARCHAR2(40 CHAR) |  |  | Search Key |  | 0 | 0 |
| `AD_PRINTFORMAT_ID` | NUMBER(10,0) |  |  | Print Format | [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | 0 | 0 |
| `C_CHARGE_ID` | NUMBER(10,0) |  |  | Charge | [C_CHARGE](../../data-model/c/c_charge.md) | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 0 |
| `HR_CONTRACT_ID` | NUMBER(10,0) |  | yes | Payroll Contract | [HR_CONTRACT](../../data-model/hr/hr_contract.md) | 0 | 0 |
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `PAYMENTRULE` | CHAR(1) |  | yes | Payment Rule |  | 0 | 0 |
| `PROCESSED` | CHAR(1) |  |  | Processed |  | 0 | 0 |
| `PROCESSING` | CHAR(1) |  |  | Process Now |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `HR_PAYROLL_ID` | NUMBER(10,0) | PK | yes | Payroll |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `HR_PAYROLL_UU` | VARCHAR2(36 CHAR) |  |  | HR_Payroll_UU |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022266` | `IsActive IN ('Y','N')` |
| `SYS_C0022267` | `Processed IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_PRINTFORMAT](../../data-model/ad/ad_printformat.md) | HR_PAYROLL.AD_PRINTFORMAT_ID → AD_PRINTFORMAT.AD_PRINTFORMAT_ID | NO ACTION |
| [C_CHARGE](../../data-model/c/c_charge.md) | HR_PAYROLL.C_CHARGE_ID → C_CHARGE.C_CHARGE_ID | NO ACTION |
| [HR_CONTRACT](../../data-model/hr/hr_contract.md) | HR_PAYROLL.HR_CONTRACT_ID → HR_CONTRACT.HR_CONTRACT_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [HR_ATTRIBUTE](../../data-model/hr/hr_attribute.md) | HR_ATTRIBUTE.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_CONCEPT](../../data-model/hr/hr_concept.md) | HR_CONCEPT.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_EMPLOYEE](../../data-model/hr/hr_employee.md) | HR_EMPLOYEE.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_LIST](../../data-model/hr/hr_list.md) | HR_LIST.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_PAYROLLCONCEPT](../../data-model/hr/hr_payrollconcept.md) | HR_PAYROLLCONCEPT.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_PERIOD](../../data-model/hr/hr_period.md) | HR_PERIOD.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_PROCESS](../../data-model/hr/hr_process.md) | HR_PROCESS.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |
| [HR_YEAR](../../data-model/hr/hr_year.md) | HR_YEAR.HR_PAYROLL_ID → HR_PAYROLL.HR_PAYROLL_ID | NO ACTION |

```mermaid
erDiagram
  AD_PRINTFORMAT ||--o{ HR_PAYROLL : ""
  C_CHARGE ||--o{ HR_PAYROLL : ""
  HR_CONTRACT ||--o{ HR_PAYROLL : ""
  HR_PAYROLL ||--o{ HR_ATTRIBUTE : ""
  HR_PAYROLL ||--o{ HR_CONCEPT : ""
  HR_PAYROLL ||--o{ HR_EMPLOYEE : ""
  HR_PAYROLL ||--o{ HR_LIST : ""
  HR_PAYROLL ||--o{ HR_PAYROLLCONCEPT : ""
  HR_PAYROLL ||--o{ HR_PERIOD : ""
  HR_PAYROLL ||--o{ HR_PROCESS : ""
  HR_PAYROLL ||--o{ HR_YEAR : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

30 change(s); the latest:

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
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_4_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | DESCRIPTION | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | HR_PAYROLL_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.hr_payroll.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
