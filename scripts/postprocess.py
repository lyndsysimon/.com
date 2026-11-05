#!/usr/bin/env python3
"""Post-build fixups for generated blog listings.

Zensical's blog plugin renders every post title in a listing as a heading that
wraps the whole title in a link:

    <h2 id="slug"><a class="toclink" href="../posts/slug/">Title</a></h2>

The title then reads as a hyperlink rather than as a heading. This rewrites that
markup so the heading is plain text and a small link icon sits after it, which
is the only clickable part:

    <h2 id="slug">Title<a class="post-link" href="../posts/slug/">…icon…</a></h2>

The pattern comes from the blog plugin's Rust implementation, not a template, so
it cannot be overridden. Matching on the `toclink` class keeps this narrow: if a
future release changes the markup the rewrite is a no-op and `posts.css` still
stops the title from being styled as a link.

Idempotent: the rewritten markup has no `toclink`, so a second run changes
nothing.
"""
from __future__ import annotations

import pathlib
import re
import sys

HEADING = re.compile(
    r'<h(?P<level>[1-6]) id="(?P<id>[^"]*)">'
    r'<a class="toclink" href="(?P<href>[^"]*)">(?P<title>.*?)</a>'
    r"</h(?P=level)>",
    re.S,
)

ICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" aria-hidden="true">'
    '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>'
    '<path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>'
    "</svg>"
)


def rewrite(html: str) -> tuple[str, int]:
    """Return (html, replacements)."""

    def repl(match: re.Match[str]) -> str:
        level = match.group("level")
        title = match.group("title")
        plain = re.sub(r"<[^>]+>", "", title).strip()
        plain = plain.replace('"', "&quot;")
        return (
            f'<h{level} id="{match.group("id")}">{title}'
            f'<a class="post-link" href="{match.group("href")}" '
            f'aria-label="Read {plain}" title="Read the post">{ICON}</a>'
            f"</h{level}>"
        )

    return HEADING.subn(repl, html)


def main(root: str) -> int:
    total = 0
    files = 0
    for path in sorted(pathlib.Path(root).rglob("*.html")):
        source = path.read_text()
        rewritten, count = rewrite(source)
        if count:
            path.write_text(rewritten)
            total += count
            files += 1
    print(f"postprocess: rewrote {total} headings across {files} files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "site"))
