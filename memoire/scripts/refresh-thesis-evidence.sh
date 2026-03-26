#!/usr/bin/env bash
set -euo pipefail

MEMOIRE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BENCHMARK_ROOT="/Users/lafleur/dev/mecene-clips"

RUN_PDF=0

for arg in "$@"; do
  case "$arg" in
    --pdf)
      RUN_PDF=1
      ;;
    --no-pdf)
      RUN_PDF=0
      ;;
    *)
      echo "[refresh-thesis-evidence] unknown argument: $arg" >&2
      echo "usage: $0 [--pdf]" >&2
      exit 1
      ;;
  esac
done

echo "[refresh-thesis-evidence] refreshing benchmark reporting db"
(
  cd "$BENCHMARK_ROOT"
  npm run benchmark:refresh-reporting
)

echo "[refresh-thesis-evidence] refreshing historical llm reporting db"
(
  cd "$MEMOIRE_ROOT"
  python3 scripts/refresh_test_llms_reporting.py
)

echo "[refresh-thesis-evidence] regenerating thesis evidence files"
(
  cd "$MEMOIRE_ROOT"
  python3 scripts/extract_thesis_evidence.py
  python3 scripts/extract_test_llms_evidence.py
  python3 scripts/generate_thesis_figures.py
)

if [[ "$RUN_PDF" -eq 1 ]]; then
  echo "[refresh-thesis-evidence] compiling memoire.pdf"
  (
    cd "$MEMOIRE_ROOT/document"
    latexmk -pdf memoire.tex
  )
fi

echo "[refresh-thesis-evidence] done"
