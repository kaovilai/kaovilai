#!/usr/bin/env python3
"""Point README.md at the generated travel-map SVGs.

Keeps a marker block so the workflow can rewrite it in place, and falls back
to appending a section when the markers are missing (first run in a repo that
has never had a travel map).

The block is a <picture> so light and dark readers each get the right theme and
GitHub still shows one image.

Usage: update-travel-map-readme.py README.md LIGHT.svg DARK.svg [WIDTH]
"""

from __future__ import annotations

import pathlib
import sys

START = "<!-- travel-map:start -->"
END = "<!-- travel-map:end -->"
ALT = (
    "Animated world map with glowing routes between places lived in, "
    "visited, or transited through"
)


def block(light: str, dark: str, width: str) -> str:
    return (
        f"{START}\n"
        "<picture>\n"
        f'  <source media="(prefers-color-scheme: dark)" srcset="{dark}">\n'
        f'  <img src="{light}" alt="{ALT}" width="{width}">\n'
        "</picture>\n"
        f"{END}"
    )


def main(argv: list[str]) -> int:
    if len(argv) not in (4, 5):
        print(__doc__, file=sys.stderr)
        return 2
    readme = pathlib.Path(argv[1])
    light, dark = argv[2], argv[3]
    width = argv[4] if len(argv) == 5 else "100%"

    text = readme.read_text(encoding="utf-8")
    replacement = block(light, dark, width)

    if START in text and END in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        text = head + replacement + tail
    elif f'src="{light}"' not in text:
        text = text.rstrip() + "\n\n### Travel map\n\n" + replacement + "\n"

    readme.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
