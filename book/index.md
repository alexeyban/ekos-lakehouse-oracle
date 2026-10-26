---
title: "The operator workflow, step by step"
order: 0
ekos_generated: true
---

# The operator workflow, step by step

<!-- ekos:manual id="intro" -->
This book follows the seven steps of the EKOS Lakehouse operator workflow on iDempiere 12 — an open-source
ERP of 903 tables on Oracle XE, with its Java code, migration scripts and documentation — as an operator does
them, in the EKOS web console. Each chapter shows a step's screen, what the operator clicks, the run log the
console kept of it, what happens behind the screen, what the operator gets, and the caveats.

The screenshots, the run logs and every number are generated: a script walks the console's pages and the book is
rendered from what it captured, so the book cannot drift from the product. Only text like this paragraph is
written by a person.

The state is honest: on this testbed the review (step 3) is not fully signed — 195 code ↔ database conflicts
and one identity match wait for a person — so the bar shows steps 4–7 as blocked behind it, although each was
built and run (the gate is the product's, and it was not bypassed). Steps 3 and 6 quote no run log: the
sign-offs and the subset load ran before EKOS recorded a log for them (RFC 0218).
<!-- /ekos:manual -->


## The steps

| Step | State | Model calls in the quoted runs |
|---|---|---|
| [1 Analyse sources](step-1.md) | done | 0 |
| [2 Documentation](step-2.md) | done | 0 |
| [3 Review and sign-off](step-3.md) | partial | — |
| [4 Requirements](step-4.md) | blocked | 0 |
| [5 Extraction and landing](step-5.md) | blocked | 0 |
| [6 Bronze and silver](step-6.md) | blocked | — |
| [7 Marts](step-7.md) | blocked | 0 |


Captured 2026-10-26T18:25:19+00:00 from the console at workspace `idemdocs` (ekos-lakehouse 0.1.1 (EKOS 1.1.0)). Screenshots, run logs and numbers are regenerated on every capture; only the marked sections are written by a person. Local paths and account names are shortened in the text, the logs and the screenshots.
