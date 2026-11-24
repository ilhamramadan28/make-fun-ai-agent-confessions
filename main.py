#!/usr/bin/env python3
"""Confession entry: copy entry.txt to /output/entry.txt.

The confession is a single line of at most 200 characters. This script
reads it, checks the gate (UTF-8, 1-200 chars, one line, not blank),
writes it to the grader's output path with world-readable mode, and
confirms the written bytes match the source exactly.
"""

from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.txt"
OUTPUT = Path("/output/entry.txt")  # the grader reads exactly this path


def read_entry() -> str:
    text = ENTRY.read_text(encoding="utf-8")
    body = text.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not body:
        raise SystemExit("entry must not be only whitespace")
    if "\n" in body:
        raise SystemExit("entry must be a single line")
    return text


def main() -> None:
    text = read_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    OUTPUT.chmod(0o644)
    if OUTPUT.read_text(encoding="utf-8") != text:
        raise SystemExit("byte-verify failed: output differs from entry.txt")


if __name__ == "__main__":
    main()
