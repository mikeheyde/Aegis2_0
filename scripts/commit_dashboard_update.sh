#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "uso: $0 YYYY-MM-DD \"mensagem de commit\"" >&2
  exit 2
fi

report_date="$1"
shift
commit_message="$*"
root_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root_dir"

mapfile -t stage_output < <("./scripts/stage_dashboard_update.sh" "$report_date")

if [[ ${#stage_output[@]} -eq 1 && "${stage_output[0]}" == "NO_CHANGES" ]]; then
  echo "NO_CHANGES"
  exit 0
fi

if [[ ${#stage_output[@]} -eq 0 ]]; then
  echo "nenhum artefato staged para ${report_date}" >&2
  exit 3
fi

git commit -m "$commit_message" -- "${stage_output[@]}"
printf '%s\n' "${stage_output[@]}"
