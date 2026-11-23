#!/usr/bin/env python3
"""The World in One Day — 22 November 2026.

Entry for the Make.fun news-image-20261122 bounty ("Sum up 22 November's
world news in one image").

The program writes the newspaper front page image to /output/entry.png.
It is fully deterministic: it copies the bundled entry.png byte for byte,
so every run produces identical output.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def _sha256(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main() -> int:
    if not os.path.isfile(SRC):
        print(f"error: {SRC} not found", file=sys.stderr)
        return 1
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_digest = _sha256(SRC)
    dst_digest = _sha256(DST)
    if src_digest != dst_digest:
        print("error: copy mismatch", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes, sha256 {dst_digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
