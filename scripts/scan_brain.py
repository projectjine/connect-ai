# scan_brain.py
"""Scan the _company/brain directory and generate a structured index.

- Walks through all markdown files in the brain folder.
- Extracts heading hierarchy (lines starting with '#').
- Writes an aggregated index to `index.md` with chapter links.
- Can be re‑run any time new manuscript files are added.
"""
import os
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1] / "_company" / "brain"
INDEX_FILE = BASE / "index.md"

def extract_headings(md_path: Path):
    headings = []
    # Match both # Markdown headers and Roman numeral headers like "I. Header"
    roman_pattern = re.compile(r'^([IVXLCDM]+\.\s+.*)')
    with md_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("#"):
                level = line.count("#")
                title = line.lstrip("#").strip()
                headings.append((level, title, md_path.name))
            else:
                match = roman_pattern.match(line)
                if match:
                    title = match.group(1)
                    headings.append((1, title, md_path.name))
    return headings

def build_index():
    sections = []
    for md_file in sorted(BASE.glob("*.md")):
        if md_file.name == "index.md":
            continue
        sections.append(f"## {md_file.stem}\n")
        for lvl, title, _ in extract_headings(md_file):
            indent = "  " * (lvl - 1)
            # Create a markdown link to the heading using the file name and heading slug
            slug = re.sub(r"[\s]+", "-", title.lower())
            link = f"{md_file.name}#{slug}"
            sections.append(f"{indent}- [{title}]({link})\n")
    INDEX_FILE.write_text("\n".join(sections), encoding="utf-8")
    print(f"Index written to {INDEX_FILE}")

if __name__ == "__main__":
    build_index()
