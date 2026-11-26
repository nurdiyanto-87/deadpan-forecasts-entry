"""Deadpan forecast for a city that does not exist.

Pure standard library, deterministic: writes one 149-character line to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "In Gloomburg tonight, expect 4 cm of sideways rain, winds of 61 km/h, "
    "and a 90% chance the mayor's umbrella inverts live on air "
    "before the 7 pm news."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters (1-160).
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
