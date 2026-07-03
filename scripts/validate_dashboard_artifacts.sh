#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "uso: $0 YYYY-MM-DD" >&2
  exit 2
fi

report_date="$1"
root_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root_dir"

required_paths=(
  "site/dashboard-bancos-publicos/index.html"
  "site/dashboard-bancos-publicos/_headers"
  "site/dashboard-bancos-publicos/.htaccess"
  "site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.md"
  "site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.csv"
)

for path in "${required_paths[@]}"; do
  [[ -f "$path" ]] || {
    echo "MISSING:$path" >&2
    exit 3
  }
done

latest_md="site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.md"
grep -Fq "$report_date" "$latest_md" || {
  echo "DATE_MISMATCH:$latest_md:$report_date" >&2
  exit 4
}

echo "OK"
