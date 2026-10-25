---
title: "Area PA"
order: 19
ekos_generated: true
ekos_estate_version: 1
---

# Area PA

30 table(s), 30 in scope.

```mermaid
erDiagram
  PA_BENCHMARK ||--o{ PA_BENCHMARKDATA : ""
  PA_BENCHMARK ||--o{ PA_MEASURE : ""
  PA_COLORSCHEMA ||--o{ PA_GOAL : ""
  PA_DASHBOARDCONTENT ||--o{ PA_DASHBOARDCONTENT_ACCESS : ""
  PA_DASHBOARDCONTENT ||--o{ PA_DASHBOARDCONTENT_TRL : ""
  PA_DASHBOARDCONTENT ||--o{ PA_DASHBOARDPREFERENCE : ""
  PA_DOCUMENTSTATUS ||--o{ PA_DOCUMENTSTATUSACCESS : ""
  PA_DOCUMENTSTATUS ||--o{ PA_DOCUMENTSTATUS_TRL : ""
  PA_GOAL ||--o{ PA_DASHBOARDCONTENT : ""
  PA_GOAL ||--o{ PA_GOAL : ""
  PA_GOAL ||--o{ PA_GOALRESTRICTION : ""
  PA_HIERARCHY ||--o{ PA_MEASURE : ""
  PA_MEASURE ||--o{ PA_ACHIEVEMENT : ""
  PA_MEASURE ||--o{ PA_GOAL : ""
  PA_MEASURECALC ||--o{ PA_MEASURE : ""
  PA_MEASURECALC ||--o{ PA_RATIOELEMENT : ""
  PA_RATIO ||--o{ PA_MEASURE : ""
  PA_RATIO ||--o{ PA_RATIOELEMENT : ""
  PA_REPORTCOLUMN ||--o{ PA_REPORTCOLUMN : ""
  PA_REPORTCOLUMN ||--o{ PA_REPORTCOLUMN_TRL : ""
  PA_REPORTCOLUMNSET ||--o{ PA_REPORT : ""
  PA_REPORTCOLUMNSET ||--o{ PA_REPORTCOLUMN : ""
  PA_REPORTCUBE ||--o{ PA_REPORT : ""
  PA_REPORTLINE ||--o{ PA_REPORTLINE : ""
  PA_REPORTLINE ||--o{ PA_REPORTLINE_TRL : ""
  PA_REPORTLINE ||--o{ PA_REPORTSOURCE : ""
  PA_REPORTLINESET ||--o{ PA_REPORT : ""
  PA_REPORTLINESET ||--o{ PA_REPORTLINE : ""
  PA_SLA_CRITERIA ||--o{ PA_SLA_GOAL : ""
  PA_SLA_GOAL ||--o{ PA_SLA_MEASURE : ""
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [PA_ACHIEVEMENT](../../data-model/pa/pa_achievement.md) | business | in | 0 |  |
| [PA_BENCHMARK](../../data-model/pa/pa_benchmark.md) | business | in | 0 |  |
| [PA_BENCHMARKDATA](../../data-model/pa/pa_benchmarkdata.md) | business | in | 0 |  |
| [PA_COLORSCHEMA](../../data-model/pa/pa_colorschema.md) | business | in | 2 |  |
| [PA_DASHBOARDCONTENT](../../data-model/pa/pa_dashboardcontent.md) | business | in | 12 |  |
| [PA_DASHBOARDCONTENT_ACCESS](../../data-model/pa/pa_dashboardcontent_access.md) | business | in | 2 |  |
| [PA_DASHBOARDCONTENT_TRL](../../data-model/pa/pa_dashboardcontent_trl.md) | translation | in | 12 |  |
| [PA_DASHBOARDPREFERENCE](../../data-model/pa/pa_dashboardpreference.md) | business | in | 0 |  |
| [PA_DOCUMENTSTATUS](../../data-model/pa/pa_documentstatus.md) | business | in | 6 |  |
| [PA_DOCUMENTSTATUSACCESS](../../data-model/pa/pa_documentstatusaccess.md) | business | in | 0 |  |
| [PA_DOCUMENTSTATUS_TRL](../../data-model/pa/pa_documentstatus_trl.md) | translation | in | 6 |  |
| [PA_GOAL](../../data-model/pa/pa_goal.md) | business | in | 4 |  |
| [PA_GOALRESTRICTION](../../data-model/pa/pa_goalrestriction.md) | business | in | 0 |  |
| [PA_HIERARCHY](../../data-model/pa/pa_hierarchy.md) | business | in | 0 |  |
| [PA_MEASURE](../../data-model/pa/pa_measure.md) | business | in | 4 |  |
| [PA_MEASURECALC](../../data-model/pa/pa_measurecalc.md) | business | in | 6 |  |
| [PA_RATIO](../../data-model/pa/pa_ratio.md) | business | in | 1 |  |
| [PA_RATIOELEMENT](../../data-model/pa/pa_ratioelement.md) | business | in | 3 |  |
| [PA_REPORT](../../data-model/pa/pa_report.md) | business | in | 3 |  |
| [PA_REPORTCOLUMN](../../data-model/pa/pa_reportcolumn.md) | business | in | 17 |  |
| [PA_REPORTCOLUMNSET](../../data-model/pa/pa_reportcolumnset.md) | business | in | 3 |  |
| [PA_REPORTCOLUMN_TRL](../../data-model/pa/pa_reportcolumn_trl.md) | translation | in | 17 |  |
| [PA_REPORTCUBE](../../data-model/pa/pa_reportcube.md) | business | in | 0 |  |
| [PA_REPORTLINE](../../data-model/pa/pa_reportline.md) | business | in | 113 |  |
| [PA_REPORTLINESET](../../data-model/pa/pa_reportlineset.md) | business | in | 3 |  |
| [PA_REPORTLINE_TRL](../../data-model/pa/pa_reportline_trl.md) | translation | in | 113 |  |
| [PA_REPORTSOURCE](../../data-model/pa/pa_reportsource.md) | business | in | 93 |  |
| [PA_SLA_CRITERIA](../../data-model/pa/pa_sla_criteria.md) | business | in | 2 |  |
| [PA_SLA_GOAL](../../data-model/pa/pa_sla_goal.md) | business | in | 1 |  |
| [PA_SLA_MEASURE](../../data-model/pa/pa_sla_measure.md) | business | in | 1 |  |
