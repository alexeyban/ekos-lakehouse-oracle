---
title: "Area GL"
order: 11
ekos_generated: true
ekos_estate_version: 1
---

# Area GL

14 table(s), 14 in scope.

```mermaid
erDiagram
  GL_BUDGET ||--o{ GL_BUDGETCONTROL : ""
  GL_BUDGET ||--o{ GL_JOURNAL : ""
  GL_CATEGORY ||--o{ GL_CATEGORY_TRL : ""
  GL_CATEGORY ||--o{ GL_JOURNAL : ""
  GL_CATEGORY ||--o{ GL_JOURNALBATCH : ""
  GL_CATEGORY ||--o{ GL_JOURNALGENERATOR : ""
  GL_CATEGORY ||--o{ GL_JOURNALGENERATORSOURCE : ""
  GL_DISTRIBUTION ||--o{ GL_DISTRIBUTIONLINE : ""
  GL_FUND ||--o{ GL_FUNDRESTRICTION : ""
  GL_JOURNAL ||--o{ GL_JOURNAL : ""
  GL_JOURNAL ||--o{ GL_JOURNALLINE : ""
  GL_JOURNALBATCH ||--o{ GL_JOURNAL : ""
  GL_JOURNALBATCH ||--o{ GL_JOURNALBATCH : ""
  GL_JOURNALGENERATOR ||--o{ GL_JOURNALGENERATORLINE : ""
  GL_JOURNALGENERATORLINE ||--o{ GL_JOURNALGENERATORSOURCE : ""
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [GL_BUDGET](../../data-model/gl/gl_budget.md) | business | in | 1 |  |
| [GL_BUDGETCONTROL](../../data-model/gl/gl_budgetcontrol.md) | business | in | 0 |  |
| [GL_CATEGORY](../../data-model/gl/gl_category.md) | business | in | 10 |  |
| [GL_CATEGORY_TRL](../../data-model/gl/gl_category_trl.md) | translation | in | 10 |  |
| [GL_DISTRIBUTION](../../data-model/gl/gl_distribution.md) | business | in | 1 |  |
| [GL_DISTRIBUTIONLINE](../../data-model/gl/gl_distributionline.md) | business | in | 2 |  |
| [GL_FUND](../../data-model/gl/gl_fund.md) | business | in | 0 |  |
| [GL_FUNDRESTRICTION](../../data-model/gl/gl_fundrestriction.md) | business | in | 0 |  |
| [GL_JOURNAL](../../data-model/gl/gl_journal.md) | business | in | 2 |  |
| [GL_JOURNALBATCH](../../data-model/gl/gl_journalbatch.md) | business | in | 1 |  |
| [GL_JOURNALGENERATOR](../../data-model/gl/gl_journalgenerator.md) | business | in | 2 |  |
| [GL_JOURNALGENERATORLINE](../../data-model/gl/gl_journalgeneratorline.md) | business | in | 6 |  |
| [GL_JOURNALGENERATORSOURCE](../../data-model/gl/gl_journalgeneratorsource.md) | business | in | 8 |  |
| [GL_JOURNALLINE](../../data-model/gl/gl_journalline.md) | business | in | 4 |  |
