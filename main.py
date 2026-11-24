#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day."""
import os
import sys
import tempfile

ENTRY = "My washing machine plays a 30-second victory song when it finishes, then wrinkles everything if I don't applaud within five minutes."


def _candidate_dirs():
    seen = []
    for d in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output"):
        if d and d not in seen:
            seen.append(d)
    repo_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    if repo_out not in seen:
        seen.append(repo_out)
    tmp_out = os.path.join(tempfile.gettempdir(), "roast-gadget-output")
    if tmp_out not in seen:
        seen.append(tmp_out)
    return seen


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    for directory in _candidate_dirs():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text + "\n")
            print(f"wrote {path} ({len(text)} chars)")
            return 0
        except OSError as exc:
            print(f"cannot write to {directory}: {exc}", file=sys.stderr)
            continue
    print("no writable output directory found", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
