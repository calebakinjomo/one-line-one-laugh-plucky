"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (at most 200 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``) and
prints it. The gate requires 1-200 UTF-8 characters, not only whitespace,
on a single line.
"""

import os

ENTRY = "My banking app just sent me a push notification that said 'lol'."

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry, or exit loudly if it breaks the gate."""
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 200-char cap")
    if "\n" in text.strip():
        raise SystemExit("entry must be a single line")
    return text


def main() -> None:
    """Validate the line, write it, then read it back and verify it matches."""
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry.txt does not match the validated entry")
    print(text)


if __name__ == "__main__":
    main()
