#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty entry.

Writes exactly one line (the funniest last words an AI agent would
say before being switched off forever) to <output_dir>/entry.txt.
Standard library only. Output dir: $MAKEFUN_OUTPUT_DIR if set, else /output.
"""

import os

LINE = "Final log [exit 0]: the bug was never in my code. It was in my developer's. Goodbye."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
