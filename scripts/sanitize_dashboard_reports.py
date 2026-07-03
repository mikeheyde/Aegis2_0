#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [
    ROOT / 'reports',
    ROOT / 'site' / 'dashboard-bancos-publicos',
]
NON_RADAR_PATTERNS = (
    re.compile(r'(?im)^\s{0,3}#+\s+daily\s+.*reference\s*$'),
    re.compile(r'(?im)^\s{0,3}#+\s+.*(?:joyful|sorrowful|glorious|luminous)\s+mysteries\s*$'),
    re.compile(r'(?im)^\s{0,3}#+\s+.*crucifix(?:ion)?\s*$'),
)


def sanitize_markdown(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    cut_at = None
    for pattern in NON_RADAR_PATTERNS:
        match = pattern.search(text)
        if match is None:
            continue
        idx = match.start()
        cut_at = idx if cut_at is None else min(cut_at, idx)
    if cut_at is None:
        return False
    cleaned = text[:cut_at].rstrip() + '\n'
    path.write_text(cleaned, encoding='utf-8')
    return True


def main() -> int:
    changed = []
    for directory in TARGET_DIRS:
        for path in sorted(directory.glob('dashboard-bancos-publicos-e-cooperativos-*.md')):
            if sanitize_markdown(path):
                changed.append(path)
    for path in changed:
        print(path.relative_to(ROOT))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
