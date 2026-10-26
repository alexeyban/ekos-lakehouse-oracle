---
title: "Step 2 — Documentation"
order: 2
ekos_generated: true
---

# Step 2 — Documentation

**On the step bar:** partial — 1060 page(s) generated 2026-10-26T13:49:46Z into ~/.ekos/data/default/idemdocs/docs/estate; publishing is the operator's

## What the operator sees

![The Commands page: `docs generate --layout estate`](images/02-commands.png)

_The Commands page: `docs generate --layout estate`._

## What they click

<!-- ekos:manual id="step2-click" -->
The operator runs **docs generate** with the estate layout and an output folder.
<!-- /ekos:manual -->


## What happens behind it

<!-- ekos:manual id="step2-behind" -->
EKOS writes the source estate as wiki pages from the ledger alone: the data model by area, one page per table and routine, the history of schema changes, the findings. A profile contributes counts, never values; text from a source without a known licence is left out. Sections a person writes are kept on every regeneration.
<!-- /ekos:manual -->


## The run log

**`docs generate --output=~/.ekos/data/default/idemdocs/docs/estate --layout=estate`** — succeeded, from the console, 2026-10-26T13:49:21.690309; model calls: 0.

```json
{"stage": "run", "msg": "started", "version": "1.1.0", "cmd": "docs generate", "t_ms": 0}
{"stage": "docs", "msg": "estate pages written", "at": "2026-10-26T13:49:46Z", "committed_at": "2026-10-25 16:56 UTC", "output": "~/.ekos/data/default/idemdocs/docs/estate", "pages": 1060, "removed": 0, "unchanged": 0, "written": 1060, "cmd": "docs generate", "t_ms": 24927}
{"stage": "llm", "msg": "calls", "count": 0, "cache_hits": 0, "embeddings": 0, "cmd": "docs generate", "t_ms": 26175}
{"stage": "run", "msg": "finished", "ok": true, "ms": 26176, "warnings": 0, "cmd": "docs generate", "t_ms": 26176}
```

## What the operator gets

The step's state above.


## Caveats

<!-- ekos:manual id="step2-caveats" -->
Publishing to a wiki (GitHub, Azure DevOps, Confluence) is done with the lakehouse-docs publishers and is the operator's decision; the console has no Publish button yet.
<!-- /ekos:manual -->
