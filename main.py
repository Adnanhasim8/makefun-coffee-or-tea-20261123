#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry A (coffee).

Writes exactly one letter, "A", to /output/entry.txt.
Python 3.13 standard library only; no network access at run time.

Why A: coffee is the louder, bolder, more vivid choice -- morning fuel,
the grind, "don't talk to me before coffee". Tea is calm and gentle;
in a blind pairwise pick between two bare letters, the vivid, funny,
honest default wins, and that is coffee.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"


def main() -> None:
    # Gate: the entry must be exactly one letter, A or B, and nothing else.
    assert len(LETTER) == 1, "entry must be exactly one character"
    assert LETTER in ("A", "B"), "entry must be A (coffee) or B (tea)"
    assert not LETTER.isspace(), "entry must not be whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Re-read and verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LETTER, "written output differs from the chosen letter"
    assert len(written) == 1 and written in ("A", "B")


if __name__ == "__main__":
    main()
