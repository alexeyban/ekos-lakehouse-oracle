---
title: "Area FACT"
order: 10
ekos_generated: true
ekos_estate_version: 1
---

# Area FACT

3 table(s), 3 in scope.

```mermaid
erDiagram
  FACT_ACCT ||--o{ FACT_RECONCILIATION : ""
  FACT_ACCT_SUMMARY {
  }
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [FACT_ACCT](../../data-model/fact/fact_acct.md) | business | in | 0 |  |
| [FACT_ACCT_SUMMARY](../../data-model/fact/fact_acct_summary.md) | business | in | 0 |  |
| [FACT_RECONCILIATION](../../data-model/fact/fact_reconciliation.md) | business | in | 0 |  |
