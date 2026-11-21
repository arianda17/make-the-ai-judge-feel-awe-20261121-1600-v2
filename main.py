"""make-the-ai-judge-feel-awe-20261121-1600 — entry program.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The text relaxes by being still: ancient redwoods, wind like water through grass,
moss-soft bark, air that is green and slow. The dwarfing comes not from scale or
noise but from patience — a redwood needs no one's memory to be here. Standard
library only; no network, randomness, or clocks.
"""

import os
from pathlib import Path

ENTRY = """The redwoods on the ridge are two thousand years old.
The wind moves through them the way water moves through grass.
The bark is soft with moss and the air is green and slow.
A redwood does not need to be remembered to be here."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()