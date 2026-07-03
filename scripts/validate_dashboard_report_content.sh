#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "uso: $0 YYYY-MM-DD" >&2
  exit 2
fi

report_date="$1"
root_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root_dir"

report_path="reports/dashboard-bancos-publicos-e-cooperativos-${report_date}.md"

[[ -f "$report_path" ]] || {
  echo "MISSING:$report_path" >&2
  exit 3
}

python3 - "$report_path" <<'PY'
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")

patterns = [
    re.compile(r"(?im)^\s{0,3}#+\s+daily\s+.*reference\s*$"),
    re.compile(r"(?im)\bcrucifix(?:ion)?\b"),
    re.compile(r"(?im)\b(?:joyful|sorrowful|glorious|luminous)\s+mysteries\b"),
    re.compile(r"(?i)\bTODO\b"),
    re.compile(r"(?i)\blorem\b"),
    re.compile(r"(?i)\bdevoc"),
    re.compile(r"(?i)\bliturg"),
    re.compile(r"(?i)\bora[cç][aã]o\b"),
    re.compile(r"(?i)\bplaceholder\b"),
    re.compile(r"\{\{"),
    re.compile(r"\}\}"),
]

for pattern in patterns:
    match = pattern.search(text)
    if match:
        excerpt = match.group(0).strip().splitlines()[0][:120]
        print(f"INVALID:{excerpt}", file=sys.stderr)
        sys.exit(4)

print("OK")
PY
