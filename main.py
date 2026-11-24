#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) to /output/entry.txt pitching a
bizarre startup idea that turns out to be a real business.

The pitch: idle backyard swimming pools become trout farms.
Homeowners earn rent on an asset that sits empty all winter, local
restaurants buy the fish, and the pool already supplies what a fish
farm needs most -- filtered water behind a fence.

Deterministic: no randomness, no network, no time, no environment
input. Every run writes the exact same bytes.
"""

from pathlib import Path

# The entry sentence. One sentence, 170 characters.
ENTRY = (
    "We turn idle backyard pools into trout farms, paying homeowners "
    "rent while local restaurants buy the fish, because every pool "
    "already holds filtered water behind a fence."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
