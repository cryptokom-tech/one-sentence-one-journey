"""One Sentence, One Journey — make.fun entry.

Writes a single complete story about a journey, told in exactly one
sentence, to /output/entry.txt. The sentence is fixed text, written by
this program at run time. No network, no randomness: two runs write
identical bytes.
"""

import os
import sys

SENTENCE = (
    "The old map promised gold at the end of the desert, so I followed it "
    "past bleached bones and dry wells for forty days, and when I finally "
    "dug where the X was marked, I found a mirror, and laughed, because "
    "the treasure had been the thirst that kept me walking."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = SENTENCE.strip()
    if not text or len(text) > 300:
        print("entry sentence must be 1-300 characters", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
