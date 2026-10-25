---
title: "Area IMP"
order: 14
ekos_generated: true
ekos_estate_version: 1
---

# Area IMP

4 table(s), 3 in scope.

```mermaid
erDiagram
  IMP_PROCESSOR ||--o{ IMP_PROCESSORPARAMETER : ""
  IMP_PROCESSOR_TYPE ||--o{ IMP_PROCESSOR : ""
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [IMP_PROCESSOR](../../data-model/imp/imp_processor.md) | business | in | 2 |  |
| `IMP_PROCESSORLOG` | log | out | 0 |  |
| [IMP_PROCESSORPARAMETER](../../data-model/imp/imp_processorparameter.md) | business | in | 6 |  |
| [IMP_PROCESSOR_TYPE](../../data-model/imp/imp_processor_type.md) | business | in | 2 |  |
