#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Stdlib only. The line is a self-contained one-liner: a setup that hands
the job to AI, and a twist where the AI over-delivers in exactly the wrong
direction.
"""

import os

LINE = "I asked AI to write my wedding vows \u2014 it proposed to my fianc\u00e9e instead."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
