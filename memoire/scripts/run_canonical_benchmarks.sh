#!/bin/zsh
set -euo pipefail

BENCH_ROOT="/Users/lafleur/dev/mecene-clips"
DB_PATH="${BENCHMARK_DB_PATH:-$BENCH_ROOT/benchmark/data/benchmark.sqlite3}"
RUN_NOW="${RUN_NOW:-0}"

cat <<EOF
Canonical thesis benchmark plan
DB: $DB_PATH

This script is intentionally conservative.
It does not execute provider-backed runs unless RUN_NOW=1 is set,
because the experiments can incur API cost.

Planned conditions:
1. structured-text canonical run completion
2. direct-video baseline
3. no-VLM text ablation
4. optional secondary-model comparison
EOF

COMMANDS=(
  "cd $BENCH_ROOT && pnpm tsx benchmark/run-experiment.ts benchmark/experiments/validation-29-timeline-scenes-dialogue-typed-v1-gemini-3.1-flash-lite-tool-v1.ts --auto"
  "cd $BENCH_ROOT && pnpm tsx benchmark/run-experiment.ts benchmark/experiments/validation-29-video-direct-gemini-3.1-flash-lite-tool-timestamps-v1.ts"
  "cd $BENCH_ROOT && pnpm tsx benchmark/run-experiment.ts benchmark/experiments/validation-29-timeline-scenes-dialogue-typed-novlm-v1-gemini-3.1-flash-lite-tool-v1.ts --auto"
  "cd $BENCH_ROOT && pnpm tsx benchmark/run-experiment.ts benchmark/experiments/validation-29-default-stack-model-matrix-v1.ts --auto"
)

printf '\nPlanned commands:\n'
for cmd in "${COMMANDS[@]}"; do
  printf '  %s\n' "$cmd"
done

if [[ "$RUN_NOW" != "1" ]]; then
  printf '\nDry plan only. Re-run with RUN_NOW=1 to execute.\n'
  exit 0
fi

for cmd in "${COMMANDS[@]}"; do
  printf '\n>>> %s\n' "$cmd"
  eval "$cmd"
done
