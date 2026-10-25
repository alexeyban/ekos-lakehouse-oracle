---
title: "Area HR"
order: 12
ekos_generated: true
ekos_estate_version: 1
---

# Area HR

18 table(s), 18 in scope.

```mermaid
erDiagram
  HR_CONCEPT ||--o{ HR_ATTRIBUTE : ""
  HR_CONCEPT ||--o{ HR_CONCEPT_ACCT : ""
  HR_CONCEPT ||--o{ HR_MOVEMENT : ""
  HR_CONCEPT ||--o{ HR_PAYROLLCONCEPT : ""
  HR_CONCEPT_CATEGORY ||--o{ HR_CONCEPT : ""
  HR_CONCEPT_CATEGORY ||--o{ HR_MOVEMENT : ""
  HR_CONTRACT ||--o{ HR_PAYROLL : ""
  HR_DEPARTMENT ||--o{ HR_ATTRIBUTE : ""
  HR_DEPARTMENT ||--o{ HR_CONCEPT : ""
  HR_DEPARTMENT ||--o{ HR_EMPLOYEE : ""
  HR_DEPARTMENT ||--o{ HR_JOB : ""
  HR_DEPARTMENT ||--o{ HR_LIST : ""
  HR_DEPARTMENT ||--o{ HR_MOVEMENT : ""
  HR_DEPARTMENT ||--o{ HR_PROCESS : ""
  HR_EMPLOYEE ||--o{ HR_ATTRIBUTE : ""
  HR_EMPLOYEE ||--o{ HR_LIST : ""
  HR_EMPLOYEE ||--o{ HR_PROCESS : ""
  HR_JOB ||--o{ HR_ATTRIBUTE : ""
  HR_JOB ||--o{ HR_CONCEPT : ""
  HR_JOB ||--o{ HR_EMPLOYEE : ""
  HR_JOB ||--o{ HR_JOB : ""
  HR_JOB ||--o{ HR_MOVEMENT : ""
  HR_JOB ||--o{ HR_PROCESS : ""
  HR_LIST ||--o{ HR_LISTVERSION : ""
  HR_LISTTYPE ||--o{ HR_LIST : ""
  HR_LISTVERSION ||--o{ HR_LISTLINE : ""
  HR_PAYROLL ||--o{ HR_ATTRIBUTE : ""
  HR_PAYROLL ||--o{ HR_CONCEPT : ""
  HR_PAYROLL ||--o{ HR_EMPLOYEE : ""
  HR_PAYROLL ||--o{ HR_LIST : ""
  HR_PAYROLL ||--o{ HR_PAYROLLCONCEPT : ""
  HR_PAYROLL ||--o{ HR_PERIOD : ""
  HR_PAYROLL ||--o{ HR_PROCESS : ""
  HR_PAYROLL ||--o{ HR_YEAR : ""
  HR_PERIOD ||--o{ HR_PROCESS : ""
  HR_PROCESS ||--o{ HR_MOVEMENT : ""
  HR_PROCESS ||--o{ HR_PROCESS : ""
  HR_YEAR ||--o{ HR_PERIOD : ""
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [HR_ATTRIBUTE](../../data-model/hr/hr_attribute.md) | business | in | 0 |  |
| [HR_CONCEPT](../../data-model/hr/hr_concept.md) | business | in | 0 |  |
| [HR_CONCEPT_ACCT](../../data-model/hr/hr_concept_acct.md) | business | in | 0 |  |
| [HR_CONCEPT_CATEGORY](../../data-model/hr/hr_concept_category.md) | business | in | 0 |  |
| [HR_CONTRACT](../../data-model/hr/hr_contract.md) | business | in | 0 |  |
| [HR_DEPARTMENT](../../data-model/hr/hr_department.md) | business | in | 0 |  |
| [HR_EMPLOYEE](../../data-model/hr/hr_employee.md) | business | in | 0 |  |
| [HR_JOB](../../data-model/hr/hr_job.md) | business | in | 0 |  |
| [HR_LIST](../../data-model/hr/hr_list.md) | business | in | 0 |  |
| [HR_LISTLINE](../../data-model/hr/hr_listline.md) | business | in | 0 |  |
| [HR_LISTTYPE](../../data-model/hr/hr_listtype.md) | business | in | 0 |  |
| [HR_LISTVERSION](../../data-model/hr/hr_listversion.md) | business | in | 0 |  |
| [HR_MOVEMENT](../../data-model/hr/hr_movement.md) | business | in | 0 |  |
| [HR_PAYROLL](../../data-model/hr/hr_payroll.md) | business | in | 0 |  |
| [HR_PAYROLLCONCEPT](../../data-model/hr/hr_payrollconcept.md) | business | in | 0 |  |
| [HR_PERIOD](../../data-model/hr/hr_period.md) | business | in | 0 |  |
| [HR_PROCESS](../../data-model/hr/hr_process.md) | business | in | 0 |  |
| [HR_YEAR](../../data-model/hr/hr_year.md) | business | in | 0 |  |
