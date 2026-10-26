#!/usr/bin/env bash
# Regenerate the demo book (book/) from the running console (EKOS RFC 0218): a tour of every step's page, then the
# pages, the run-log excerpts and the PDF. The narration in book/*.md is kept.
#
#   EKOS_CONSOLE_TOKEN_VALUE=<write token> EKOS_HOME=~/.ekos EKOS_BIN=$(command -v ekos-lakehouse) \
#     scripts/demo-book.sh [console url] [workspace]
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
console="${1:-http://127.0.0.1:8765}"
ws="${2:-idemdocs}"
capture="$(mktemp -d)"
# Local paths and the account name never reach a public page.
replace=(--replace "$EKOS_HOME=~/.ekos" --replace "$HOME=~" --replace "$(id -un)=operator")
cd "$here/src/ekos-lakehouse/tools/demo-book"
python -m demo_book tour --console "$console" --workspace "$ws" --out "$capture" \
  --act test-db --act docs "${replace[@]}"
python -m demo_book render --capture "$capture" --out "$here/book" --pdf "$here/book/demo-book.pdf" \
  --allow-missing "${replace[@]}"
