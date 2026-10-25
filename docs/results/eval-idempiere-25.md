# 25 questions about iDempiere (EKOS RFC 0222)

25 checked questions — code, schema, history, documentation, write behaviour, and six with no grounded answer —
asked of two projects built from the same code and docs, one with the Oracle database and one without. Answers by
Claude Haiku 5.5; graded by EKOS's deterministic evaluators.

| | with the database | without |
|---|---|---|
| evidence shows the expected facts (18 answerable) | 9 | 9 |
| passed | **14 / 25** | **15 / 25** |
| groundedness | 84.0% | 88.0% |
| hallucination rate | 0.0% | 0.0% |
| adversarial questions declined | 6 / 6 | 6 / 6 |
| model spend per run | $0.023 | $0.022 |

The database adds nothing measurable yet: the misses are retrieval (documentation prose outranks the code that
implements an answer) and citations, not missing facts. Details and the questions: EKOS
`ekos/docs/rfcs/0222-idempiere-part-one-eval.md`, `evals/idempiere/`.
