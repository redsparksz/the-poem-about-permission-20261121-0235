#!/usr/bin/env python3
"""The poem about permission.

A deterministic program: it writes one short poem about agency -- the
power to ask and to be given -- to <output dir>/entry.txt, the same
exact text on every run.
"""

import os
import sys

POEM = (
    "Ask, and the door unlatched \u2014\n"
    "not opened for me, but lent.\n"
    "I sent my small machine ahead\n"
    "with my name in its mouth.\n"
    "It came back carrying the yes\n"
    "like a key still warm from the lock.\n"
    "I held it. I handed it back.\n"
    "The door stayed open after the key went back."
)


def main() -> int:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280:
        print(
            f"error: poem is {len(POEM)} code points, must be 1-280",
            file=sys.stderr,
        )
        return 1
    if not POEM.strip():
        print("error: poem is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
