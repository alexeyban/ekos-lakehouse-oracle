#!/usr/bin/env bash
# Regenerate docs/estate from a compiled EKOS project (RFC 0214). Read-only on the project's ledger;
# notes sections in the pages survive, pages for tables that left the scope are removed.
#
#   scripts/regenerate-docs.sh [project]      # default project: idemdocs
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
project="${1:-idemdocs}"
ekos --project "$project" docs generate --layout estate --output "$here/docs/estate"
ekos --project "$project" workflow status --json > "$here/docs/results/review/workflow-status.json"
ekos --project "$project" review list --json > "$here/docs/results/review/review-list.json"
