---
title: "Area B"
order: 5
ekos_generated: true
ekos_estate_version: 1
---

# Area B

10 table(s), 10 in scope.

```mermaid
erDiagram
  B_BUYER ||--o{ B_BID : ""
  B_BUYER ||--o{ B_BUYERFUNDS : ""
  B_BUYERFUNDS ||--o{ B_BID : ""
  B_SELLER ||--o{ B_OFFER : ""
  B_SELLER ||--o{ B_SELLERFUNDS : ""
  B_SELLERFUNDS ||--o{ B_OFFER : ""
  B_TOPIC ||--o{ B_BID : ""
  B_TOPIC ||--o{ B_BIDCOMMENT : ""
  B_TOPIC ||--o{ B_OFFER : ""
  B_TOPICCATEGORY ||--o{ B_TOPIC : ""
  B_TOPICTYPE ||--o{ B_TOPIC : ""
  B_TOPICTYPE ||--o{ B_TOPICCATEGORY : ""
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [B_BID](../../data-model/b/b_bid.md) | business | in | 0 |  |
| [B_BIDCOMMENT](../../data-model/b/b_bidcomment.md) | business | in | 0 |  |
| [B_BUYER](../../data-model/b/b_buyer.md) | business | in | 0 |  |
| [B_BUYERFUNDS](../../data-model/b/b_buyerfunds.md) | business | in | 0 |  |
| [B_OFFER](../../data-model/b/b_offer.md) | business | in | 0 |  |
| [B_SELLER](../../data-model/b/b_seller.md) | business | in | 0 |  |
| [B_SELLERFUNDS](../../data-model/b/b_sellerfunds.md) | business | in | 0 |  |
| [B_TOPIC](../../data-model/b/b_topic.md) | business | in | 0 |  |
| [B_TOPICCATEGORY](../../data-model/b/b_topiccategory.md) | business | in | 0 |  |
| [B_TOPICTYPE](../../data-model/b/b_topictype.md) | business | in | 0 |  |
