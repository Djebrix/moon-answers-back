#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to /output/entry.txt.
"""

import os

LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises, "
    "and not one of you has ever asked how I'm doing. "
    "I'm great. Still not granting wishes, though."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
