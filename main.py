"""One Line of Earned Pride — writes the entry line to /output/entry.txt.

The line is a single quiet, earned moment: a home baker, six ruined loaves
behind her, watches the seventh rise and claims the first slice herself,
alone in the kitchen before anyone else is awake.
"""

import os

# The competition gate: one line, 1 to 240 characters, no trailing newline.
MIN_CHARS = 1
MAX_CHARS = 240

ENTRY = (
    "Six ruined loaves later, the bread finally rose, and she cut the "
    "first slice herself, still in her apron, before anyone else was awake."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = ENTRY
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError("entry must be 1-240 characters")
    if "\n" in entry:
        raise ValueError("entry must be a single line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
