#!/usr/bin/env python3
"""Check the minimum structure and frontmatter of a personal-memory vault."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "00-System/config.md",
    "00-System/Memory Operating Rules.md",
    "10-User/preferences.md",
    "10-User/work-style.md",
    "10-User/decision-principles.md",
    "10-User/long-term-plans.md",
    "30-Triggers/project-start.md",
    "30-Triggers/project-end.md",
    "30-Triggers/learned-triggers.md",
    "30-Triggers/weekly-review.md",
    "00-Inbox/README.md",
    "40-Archive/README.md",
)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, help="Path to an Obsidian vault")
    args = parser.parse_args()
    vault = args.vault.expanduser().resolve()

    if not vault.is_dir():
        print(f"ERROR: vault directory does not exist: {vault}")
        return 2

    errors: list[str] = []
    for relative in REQUIRED_FILES:
        path = vault / relative
        if not path.is_file():
            errors.append(f"missing: {relative}")

    frontmatter_files = [
        vault / "00-System/config.md",
        vault / "10-User/preferences.md",
        vault / "30-Triggers/project-start.md",
    ]
    for path in frontmatter_files:
        if path.is_file():
            metadata = frontmatter(path)
            for key in ("type", "scope", "status"):
                if key not in metadata:
                    errors.append(f"missing frontmatter '{key}': {path.relative_to(vault)}")

    if errors:
        print("Vault validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"Vault is valid: {vault}")
    print(f"Checked {len(REQUIRED_FILES)} required files and core frontmatter.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
