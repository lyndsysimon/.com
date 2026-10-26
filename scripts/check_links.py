#!/usr/bin/env python3
"""Fail the build if any generated HTML contains a malformed link.

The blog listing (recent/tags pages) once emitted links like
``..//posts/<slug>/`` under zensical 0.0.23, which browsers resolve to
``https://lyndsysimon.com//posts/<slug>/``. Zensical >= 0.0.32 emits
absolute paths instead. This guard keeps the doubled-slash bug from
returning on a future upgrade.

Usage: python scripts/check_links.py site
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HREF = re.compile(r'(?:href|src)="([^"]*)"')
BAD_PREFIXES = ("..//", "///")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_links.py <build-output-dir>", file=sys.stderr)
        return 2

    root = Path(argv[1])
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2

    problems: list[str] = []
    for page in sorted(root.rglob("*.html")):
        for value in HREF.findall(page.read_text(errors="ignore")):
            if value.startswith(("http://", "https://", "mailto:", "data:", "#")):
                continue
            if value.startswith(BAD_PREFIXES) or value.startswith("//"):
                problems.append(f"{page.relative_to(root)}: {value}")

    if problems:
        print(f"{len(problems)} malformed link(s) found:", file=sys.stderr)
        for line in problems:
            print(f"  {line}", file=sys.stderr)
        return 1

    print(f"link check passed ({len(list(root.rglob('*.html')))} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
