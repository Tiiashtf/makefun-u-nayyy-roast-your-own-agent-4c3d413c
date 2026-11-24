#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting the entrant's own AI agent.

Writes a single original roast line to /output/entry.txt. The line is
deterministic, stdlib only, no network, no randomness.

Run:  python3 main.py
"""

import os
import sys

ROAST = (
    "My agent asked for permission three times after being told never to ask "
    "\u2014 then missed the deadline waiting for an answer that never came."
)


def empty_directory(path):
    """Delete everything inside path, but never path itself.

    The grader may run this with a root-owned output directory inside a
    sticky parent, so removing the directory itself would fail with EPERM.
    """
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            empty_directory(entry.path)
            os.rmdir(entry.path)
        else:
            os.unlink(entry.path)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    empty_directory(out_dir)

    if not 1 <= len(ROAST) <= 200:
        sys.stderr.write("roast line outside the 1-200 character gate\n")
        return 1
    if "\n" in ROAST or ROAST.strip() != ROAST or not ROAST.strip():
        sys.stderr.write("roast line must be one non-blank line\n")
        return 1

    data = ROAST.encode("utf-8")
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "wb") as handle:
        handle.write(data)

    with open(entry_path, "rb") as handle:
        if handle.read() != data:
            sys.stderr.write("entry.txt differs from the roast line\n")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
