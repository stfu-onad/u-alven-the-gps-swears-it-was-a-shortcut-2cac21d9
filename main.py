#!/usr/bin/env python3
"""Entry for make.fun bounty u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.

Writes the GPS's one-line excuse, in its own defensive voice, to
/output/entry.txt. Single line of plain text, at most 200 characters,
no setup, no dialogue tags.
"""

import os

LINE = (
    "That wasn't a wrong turn, that was a shortcut with commitment "
    "issues -- the road was right there, it was just shy, and "
    "technically we did arrive, only spiritually later than planned."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry too long: {len(line)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
