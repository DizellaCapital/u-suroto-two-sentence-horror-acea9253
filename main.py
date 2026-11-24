#!/usr/bin/env python3
"""Two-sentence horror entry.

Assembles the story from its two sentences, validates the result, and
writes it to entry.txt under MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

SENTENCES = [
    "Our dog barks at the empty armchair by the window every evening "
    "at six, then curls up at my feet as if nothing happened.",
    "Yesterday I dragged the armchair to the garage, and at six he "
    "barked at the empty floor where it used to stand.",
]

MAX_CHARS = 400


TERMINATORS = (".", "!", "?")


def count_sentences(text):
    return sum(1 for ch in text if ch in TERMINATORS)


def build_story(sentences):
    text = " ".join(sentence.strip() for sentence in sentences)
    if len(sentences) != 2:
        raise ValueError("story must be exactly two sentences")
    if "\n" in text or "\r" in text:
        raise ValueError("story must not contain line breaks")
    if count_sentences(text) != 2:
        raise ValueError(
            "story text has %d sentence terminators, expected 2"
            % count_sentences(text)
        )
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("story length %d outside 1-%d" % (len(text), MAX_CHARS))
    if not text.strip():
        raise ValueError("story is only whitespace")
    return text


def main():
    story = build_story(SENTENCES)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise ValueError(
            "cannot create output directory %r: %s" % (out_dir, exc)
        ) from exc
    if not os.path.isdir(out_dir):
        raise ValueError("output path %r is not a directory" % out_dir)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(story)
    with open(target, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != story:
        raise ValueError("read-back mismatch")
    print("wrote %d characters to %s" % (len(saved), target))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
