#!/usr/bin/env python3
"""Point README.md at the generated travel-map GIF.

Keeps a marker block so the workflow can rewrite it in place, and falls back
to appending a section when the markers are missing (first run in a repo that
has never had a travel map).

Usage: update-travel-map-readme.py README.md assets/travel-map.gif 720
"""

from __future__ import annotations

import pathlib
import sys

START = "<!-- travel-map:start -->"
END = "<!-- travel-map:end -->"
ALT = (
    "Animated globe showing places lived in, visited, or transited through, "
    "with routes between cities"
)


def block(source: str, width: str) -> str:
    return f'{START}\n<img src="{source}" alt="{ALT}" width="{width}">\n{END}'


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    readme = pathlib.Path(argv[1])
    source = argv[2]
    width = argv[3]

    text = readme.read_text(encoding="utf-8")
    replacement = block(source, width)

    if START in text and END in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        text = head + replacement + tail
    elif f'src="{source}"' not in text:
        text = text.rstrip() + "\n\n### Travel map\n\n" + replacement + "\n"

    readme.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
