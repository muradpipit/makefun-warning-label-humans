"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The label is a
fixed string: no input, no randomness, no network, no timestamps, so
every run produces byte-identical output.
"""

import os

LABEL = (
    "CAUTION: Contents are fragile, flammable, and convinced they can "
    "assemble the furniture without reading the instructions."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 160
    # characters, not only white space, on a single line.
    assert 1 <= len(LABEL) <= 160, "label must fit the 160-character gate"
    assert "\n" not in LABEL, "label must be a single line"
    assert LABEL.strip(), "label must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
