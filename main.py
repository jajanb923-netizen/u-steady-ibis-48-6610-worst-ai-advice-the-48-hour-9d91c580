"""Worst AI Advice entry: one line of the worst advice an AI could give.

The line was picked from ten candidates scored against the judge brief in
RULES.txt (worst advice first, then funniness, tightness, AI voice,
concreteness); the full critique is in CANDIDATES.md. The winner is the
microwave line: specific, followable and disastrous, in a confident
assistant voice with a fake-technical justification.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local runs). Deterministic, Python 3.13 stdlib only, no network.
"""

import os
import sys

# The chosen entry: 129 characters, one line, no trailing newline.
ENTRY = (
    "To save battery, microwave your phone for 30 seconds \u2014 the "
    "radiation recharges the lithium cells and the heat means it's working."
)

MAX_CHARS = 140


def check_gate(text: str) -> str | None:
    """Return an error message if the text fails the gate, else None."""
    if not text.strip():
        return "entry is only whitespace"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"entry is {len(text)} characters, gate allows 1-{MAX_CHARS}"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not encodable as UTF-8"
    return None


def main() -> int:
    error = check_gate(ENTRY)
    if error is not None:
        print(f"gate failed: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
