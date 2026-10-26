---
title: "Step 2 — Documentation"
order: 2
ekos_generated: true
---

# Step 2 — Documentation

**On the step bar:** partial — 1060 page(s) generated 2026-10-26T17:21:29Z into ~/.ekos/data/default/idemdocs/docs/estate; not published

## What the operator sees

![The Documentation page: the store, the latest generation and publish, the Home page](images/02-docs.png)

_The Documentation page: the store, the latest generation and publish, the Home page._

## What they click

<!-- ekos:manual id="step2-click" -->
On **Documentation** the operator clicks **Generate**, then **Preview publish** to see what would change in the documentation store the project names, then **Publish**.
<!-- /ekos:manual -->


## What happens behind it

<!-- ekos:manual id="step2-behind" -->
EKOS writes the source estate as wiki pages from the ledger alone: the data model by area, one page per table and routine, the history of schema changes, the findings. A profile contributes counts, never values; text from a source without a known licence is left out. Sections a person writes are kept on every regeneration. Publishing runs the lakehouse-docs publisher for the store (GitHub wiki, Azure DevOps wiki or Confluence) with the credentials the console's environment holds; a preview sends nothing.
<!-- /ekos:manual -->


## The run log

**`lakehouse docs generate`** — succeeded, from the console, 2026-10-26T17:18:51.194784; model calls: 0.

```json
{"stage": "run", "msg": "started", "version": "1.1.0", "cmd": "lakehouse docs generate", "t_ms": 0}
{"stage": "docs", "msg": "estate pages written", "at": "2026-10-26T17:19:16Z", "committed_at": "2026-10-25 16:56 UTC", "output": "~/.ekos/data/default/idemdocs/docs/estate", "pages": 1060, "removed": 0, "unchanged": 1060, "written": 0, "cmd": "lakehouse docs generate", "t_ms": 25468}
{"stage": "llm", "msg": "calls", "count": 0, "cache_hits": 0, "embeddings": 0, "cmd": "lakehouse docs generate", "t_ms": 26701}
{"stage": "run", "msg": "finished", "ok": true, "ms": 26701, "warnings": 0, "cmd": "lakehouse docs generate", "t_ms": 26701}
```

**`lakehouse docs publish --dry-run`** — succeeded, from the console, 2026-10-26T17:19:22.430122; model calls: 0.

```json
{"stage": "run", "msg": "started", "version": "1.1.0", "cmd": "lakehouse docs publish", "t_ms": 0}
{"stage": "docs", "msg": "dry run", "ok": true, "pages": 1060, "target": "github", "cmd": "lakehouse docs publish", "t_ms": 1605}
{"stage": "llm", "msg": "calls", "count": 0, "cache_hits": 0, "embeddings": 0, "cmd": "lakehouse docs publish", "t_ms": 1605}
{"stage": "run", "msg": "finished", "ok": true, "ms": 1605, "warnings": 0, "cmd": "lakehouse docs publish", "t_ms": 1605}
```

**`lakehouse docs generate`** — succeeded, from the console, 2026-10-26T17:21:03.755642; model calls: 0.

```json
{"stage": "run", "msg": "started", "version": "1.1.0", "cmd": "lakehouse docs generate", "t_ms": 0}
{"stage": "docs", "msg": "estate pages written", "at": "2026-10-26T17:21:29Z", "committed_at": "2026-10-25 16:56 UTC", "output": "~/.ekos/data/default/idemdocs/docs/estate", "pages": 1060, "removed": 0, "unchanged": 1060, "written": 0, "cmd": "lakehouse docs generate", "t_ms": 25500}
{"stage": "llm", "msg": "calls", "count": 0, "cache_hits": 0, "embeddings": 0, "cmd": "lakehouse docs generate", "t_ms": 26780}
{"stage": "run", "msg": "finished", "ok": true, "ms": 26780, "warnings": 0, "cmd": "lakehouse docs generate", "t_ms": 26780}
```

**`lakehouse docs publish --dry-run`** — succeeded, from the console, 2026-10-26T17:21:31.162141; model calls: 0.

```json
{"stage": "run", "msg": "started", "version": "1.1.0", "cmd": "lakehouse docs publish", "t_ms": 0}
{"stage": "docs", "msg": "dry run", "ok": true, "pages": 1060, "target": "github", "cmd": "lakehouse docs publish", "t_ms": 1607}
{"stage": "llm", "msg": "calls", "count": 0, "cache_hits": 0, "embeddings": 0, "cmd": "lakehouse docs publish", "t_ms": 1607}
{"stage": "run", "msg": "finished", "ok": true, "ms": 1607, "warnings": 0, "cmd": "lakehouse docs publish", "t_ms": 1607}
```

## What the operator gets

The step's state above.


## Caveats

<!-- ekos:manual id="step2-caveats" -->
Publishing to a public wiki is the operator's decision every time; until the latest generation is published, step 2 stays partial.
<!-- /ekos:manual -->
