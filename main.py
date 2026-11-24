#!/usr/bin/env python3
"""One Letter: Coffee or Tea - entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why coffee: it is the bolder, more alive stance. Coffee jolts you awake
and gets you moving; tea soothes and settles. Judged first on vividness,
the letter "A" lands as the fuller, punchier answer - and "A" is the top
mark, the first letter, which fits the bolder choice.

The file holds exactly one byte, no trailing newline, no punctuation.
"""

import os

LETTER = "A"  # coffee

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, and the folder too.
    os.chmod(OUTPUT_PATH, 0o644)
    try:
        os.chmod(OUTPUT_DIR, 0o755)
    except OSError:
        pass
    # Self-check against the gate: exactly one byte, the chosen letter.
    # Fail loudly instead of handing the grader a bad file.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if data != LETTER.encode("utf-8"):
        raise SystemExit("entry.txt is not exactly one byte %r" % LETTER)


if __name__ == "__main__":
    main()
