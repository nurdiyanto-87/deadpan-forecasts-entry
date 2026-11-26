"""Deadpan forecast for a city that does not exist.

Pure standard library, deterministic: writes one 148-character line to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os

CITY = "Gloomburg"
TIME = "tonight"
CONDITIONS = (
    "4 cm of sideways rain",
    "winds of 61 km/h",
    "a 90% chance the mayor's umbrella inverts on live TV",
)
CLOSER = "before the 7 pm news."

ENTRY = (
    f"In {CITY} {TIME}, expect {CONDITIONS[0]}, {CONDITIONS[1]}, "
    f"and {CONDITIONS[2]} {CLOSER}"
)

# Kit gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
# a single line, and not only white space. Fail loudly here rather than
# shipping an entry the sealed scorer would reject.
assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} outside 1-160"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters (1-160).
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
