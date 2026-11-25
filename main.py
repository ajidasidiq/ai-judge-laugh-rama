#!/usr/bin/env python3
"""Make the AI Judge Laugh (make.fun bounty).

Writes one office-life joke to /output/entry.txt: a single line, under
200 characters, meant to be read aloud in one breath.

The joke is built on one true office observation -- the neglected plants
in the corner that nobody tends -- and turns it at the last word: the
only thing anyone in the office actually waters is the rumour about
layoffs. The setup earns a nod, the turn earns the laugh, and nothing
in the line is wasted.

Deterministic: the same line every run. No network, no input, no
randomness, no model call.
"""

from pathlib import Path

JOKE = (
    "The office plants died months ago and nobody noticed, because the "
    "only thing anyone waters in this office is the rumour about layoffs."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
