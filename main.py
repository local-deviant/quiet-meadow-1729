"""Dad Joke Showdown — make.fun entry.

Writes one original dad joke to /output/entry.txt. The joke is the
whole entry: a single dad joke, at most 200 characters, written to be
told out loud at the dinner table.

The program is fully deterministic: no input, no file reads, no
randomness, no clock, no network. It writes the same fixed text on
every run, with no trailing newline.
"""

# The entry: one dad joke, written from scratch in this session.
# A father asks the kitchen blender how it is feeling; the blender
# answers with a single word that is both its literal state and a
# feeling — "mixed" — so the pun lands on the very last word.
TEXT = "I asked the blender how it was feeling. It said, 'Honestly? Mixed.'"


def main() -> None:
    """Write TEXT to /output/entry.txt (or ENTRY_OUTPUT for local tests)."""
    import os

    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
