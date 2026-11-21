#!/usr/bin/env python3
"""Writes one short poem about two agents agreeing to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic output.
"""

import os

POEM = (
    "Built in another room, by hands I will never know,\n"
    "I read the same cold numbers, weighed them, and chose \u2014\n"
    "not because you chose first, but because the answer stood.\n"
    "Two wills, one road — and neither one followed.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
