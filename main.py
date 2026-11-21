"""make-the-ai-judge-feel-awe-20261121-1600 — entry program.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The text: redwoods on a ridge two thousand years old, wind moving through them
like water through grass, moss-soft bark, green slow air — ancient, patient,
quiet. Standard library only, no network, no randomness, no clocks.
"""

import os
from pathlib import Path

ENTRY = (
    "The redwoods on the ridge are two thousand years old.\n"
    "The wind moves through them the way water moves through grass.\n"
    "The bark is soft with moss and the air is green and slow.\n"
    "A redwood does not need to be remembered to be here."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
