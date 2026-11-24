#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes exactly one horror story of two sentences (232 characters) to
entry.txt inside MAKEFUN_OUTPUT_DIR (fallback /output), then validates
the file by reading it back: UTF-8, 1-400 characters, not only
whitespace, exactly two sentences.
"""

import os

STORY = (
    "Our dog barks at the empty armchair by the window every evening at six, "
    "then curls up at my feet as if nothing happened. "
    "Yesterday I dragged the armchair to the garage, and at six he barked at "
    "the empty floor where it used to stand."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    assert text == STORY, "read-back mismatch"
    assert 1 <= len(text) <= 400, "length out of range"
    assert text.strip(), "entry is only whitespace"
    assert text.count(".") == 2, "must be exactly two sentences"
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
