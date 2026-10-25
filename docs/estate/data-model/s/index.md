---
title: "Area S"
order: 23
ekos_generated: true
ekos_estate_version: 1
---

# Area S

10 table(s), 10 in scope.

```mermaid
erDiagram
  S_RESOURCE ||--o{ S_RESOURCEASSIGNMENT : ""
  S_RESOURCE ||--o{ S_RESOURCEUNAVAILABLE : ""
  S_RESOURCEASSIGNMENT ||--o{ S_TIMEEXPENSELINE : ""
  S_RESOURCETYPE ||--o{ S_RESOURCE : ""
  S_TIMEEXPENSE ||--o{ S_TIMEEXPENSELINE : ""
  S_TIMETYPE ||--o{ S_TIMEEXPENSELINE : ""
  S_TRAINING ||--o{ S_TRAINING_CLASS : ""
  S_EXPENSETYPE {
  }
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [S_EXPENSETYPE](../../data-model/s/s_expensetype.md) | business | in | 1 |  |
| [S_RESOURCE](../../data-model/s/s_resource.md) | business | in | 11 |  |
| [S_RESOURCEASSIGNMENT](../../data-model/s/s_resourceassignment.md) | business | in | 2 |  |
| [S_RESOURCETYPE](../../data-model/s/s_resourcetype.md) | business | in | 3 |  |
| [S_RESOURCEUNAVAILABLE](../../data-model/s/s_resourceunavailable.md) | business | in | 2 |  |
| [S_TIMEEXPENSE](../../data-model/s/s_timeexpense.md) | business | in | 1 |  |
| [S_TIMEEXPENSELINE](../../data-model/s/s_timeexpenseline.md) | business | in | 4 |  |
| [S_TIMETYPE](../../data-model/s/s_timetype.md) | business | in | 0 |  |
| [S_TRAINING](../../data-model/s/s_training.md) | business | in | 1 |  |
| [S_TRAINING_CLASS](../../data-model/s/s_training_class.md) | business | in | 0 |  |
