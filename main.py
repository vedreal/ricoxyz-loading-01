"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) for stressed
developers and AI coding agents to /output/entry.txt.
"""

import os

ENTRY = (
    "While you wait: your agent already fixed the bug, broke two tests, "
    "and is now writing a commit message that blames you."
)


def output_path():
    """Resolve the output path, honouring MAKEFUN_OUTPUT_DIR for local runs."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    """Write the tip to the output path."""
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
