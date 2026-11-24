#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single line an AI agent would hand its human after missing
a deadline to /output/entry.txt. Stdlib only; no network, no reads
outside the repo. The grader runs `python3 -P -s main.py` in a
python:3.13-slim sandbox with /output mounted writable.
"""

import os

# The joke: the excuse leans on the agent's own machinery (delegating to
# subagents) instead of a human excuse. "Nine agents deep" is the image;
# "none of us has started" is the landing. 131 characters, one line, no
# trailing newline in the file.
LINE = (
    "Sorry \u2014 I delegated the deadline to a subagent, who delegated it "
    "to another one. We\u2019re nine agents deep and none of us has started."
)

MAX_CHARS = 160


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"line is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
