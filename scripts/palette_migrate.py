#!/usr/bin/env python3
"""
palette_migrate.py — rewrite retired brand-palette tokens in .docx files.

A .docx is a zip archive of XML. This script unpacks each file, runs a
conservative find-replace over `word/document.xml` (where body text lives),
and rewrites the archive in place. A .bak copy is created first.

Run:
    python3 scripts/palette_migrate.py <file.docx> [<file.docx> ...]
    python3 scripts/palette_migrate.py --all    # default four brand docs

Source of truth for the target palette:
    references/palette/Color-System.html           (Ember Signal · Dusk, v1.5)
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DEFAULT_DOCS = [
    ROOT / "Design" / "housemate_brand_v0_8-2.docx",
    ROOT / "Engineering" / "housemate_tech_v0_9-2.docx",
    ROOT / "Product" / "housemate_requirements_v1_2-2.docx",
    ROOT / "Strategy & Finance" / "housemate_strategy_v0.4-2.docx",
]

# Mapping from retired → current. Order matters: longer/more specific phrases
# come first so "Mint Signal" is rewritten before any stray "mint" catches.
# Hex replacements are case-insensitive (see _replace_hex below).
PHRASE_REPLACEMENTS: list[tuple[str, str]] = [
    # Palette names
    ("Mint Signal · Ghost Mint", "Ember Signal · Dusk"),
    ("Mint Signal", "Ember Signal"),
    ("Ghost Mint", "Dusk"),
    ("Electric Mint", "Sunset Vivid"),
    ("Mint Subtle", "Sunset Subtle"),
    ("True Mint", "True Primary"),
    # Code-ish strings
    ("MintBadge", "EmberBadge"),
    ('variant="mint"', 'variant="sunset"'),
    ("--color-mint", "--color-sunset"),
    ("--color-teal", "--color-ember"),
]

# Hex replacements are applied case-insensitively but preserve the *target*
# case (always upper, matching the HTML spec).
HEX_REPLACEMENTS: dict[str, str] = {
    # Mint five-stop → Sunset five-stop (role-matched)
    "#3FE0A5": "#FF4E7D",   # bright mint       → sunset vivid
    "#2ACFA0": "#F03B65",   # mint hover/ring   → sunset subtle
    "#1FBF9A": "#E8305A",   # true primary mint → true primary sunset
    "#18A88A": "#CC2848",   # deep mint         → primary hover
    "#0EA5A0": "#CC2848",   # deeper mint       → primary hover
    "#0B2B25": "#161214",   # darkest mint      → dusk page

    # Pre-v1.5 cool-gray neutrals → warm-tinted neutrals
    "#F8F8F8": "#FAF8F7",   # page bg
    "#E8E8E8": "#ECE8E6",   # border
    "#B8BEBE": "#B8B0AD",   # tertiary text
    "#8F9494": "#8A8380",   # muted text
    "#1C201E": "#1A1614",   # foreground text

    # Pre-v1.5 dusk values → v1.5 dusk
    "#18161A": "#161214",
    "#221F24": "#1F1B1D",
    "#2A262C": "#262123",
    "#2E2A31": "#2A2528",

    # Legacy Ghost Mint dark surfaces
    "#242926": "#1F1B1D",
    "#2A302D": "#262123",
    "#2E3530": "#2A2528",

    # Retired on-sunset dark text (vivid/warm are now display-only)
    "#2A0A14": "#FFFFFF",

    # Pre-Mint coral/lavender (if ever referenced) → sunset
    "#FF7A5C": "#FF7040",   # coral              → ember warm
    "#9B8CFF": "#6B46C1",   # lavender           → violet semantic
}


def migrate_xml(xml: str) -> tuple[str, dict[str, int]]:
    """Apply all replacements to a string. Returns (new_xml, hit_counts)."""
    counts: dict[str, int] = {}
    out = xml

    for old, new in PHRASE_REPLACEMENTS:
        n = out.count(old)
        if n:
            out = out.replace(old, new)
            counts[f"'{old}' → '{new}'"] = n

    for old, new in HEX_REPLACEMENTS.items():
        # Case-insensitive match on the hex code (e.g. '#f8f8f8' and '#F8F8F8')
        pattern = re.compile(re.escape(old), re.IGNORECASE)
        n = len(pattern.findall(out))
        if n:
            out = pattern.sub(new, out)
            counts[f"{old} → {new}"] = n

    return out, counts


def migrate_docx(path: Path, dry_run: bool = False) -> dict[str, int]:
    """Rewrite a single .docx file in place. Returns a dict of replacement counts."""
    if not path.exists():
        print(f"  ✗ not found: {path}", file=sys.stderr)
        return {}

    all_counts: dict[str, int] = {}
    # A .docx can have content in several XML parts. Touch everything rendered
    # as body text (document.xml) plus headers/footers/footnotes/endnotes.
    xml_parts = {
        "word/document.xml",
        "word/header1.xml", "word/header2.xml", "word/header3.xml",
        "word/footer1.xml", "word/footer2.xml", "word/footer3.xml",
        "word/footnotes.xml", "word/endnotes.xml",
        "word/comments.xml",
    }

    with zipfile.ZipFile(path, "r") as zin:
        members = zin.namelist()
        payload: dict[str, bytes] = {name: zin.read(name) for name in members}

    for name in list(payload):
        if name not in xml_parts:
            continue
        try:
            text = payload[name].decode("utf-8")
        except UnicodeDecodeError:
            continue
        new_text, counts = migrate_xml(text)
        for k, v in counts.items():
            all_counts[k] = all_counts.get(k, 0) + v
        if new_text != text:
            payload[name] = new_text.encode("utf-8")

    if dry_run or not all_counts:
        return all_counts

    # Backup before writing
    backup = path.with_suffix(path.suffix + ".bak")
    if not backup.exists():
        shutil.copy2(path, backup)

    tmp = path.with_suffix(path.suffix + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        # Preserve original member order
        with zipfile.ZipFile(path, "r") as zin:
            for info in zin.infolist():
                zout.writestr(info, payload[info.filename])
    tmp.replace(path)
    return all_counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", type=Path,
                    help="Specific .docx paths. Omit with --all for default set.")
    ap.add_argument("--all", action="store_true",
                    help="Process the four canonical brand/tech/PRD/strategy docs.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report hits but do not modify files.")
    args = ap.parse_args()

    targets: list[Path]
    if args.all:
        targets = DEFAULT_DOCS
    elif args.files:
        targets = args.files
    else:
        ap.print_help()
        return 1

    total = 0
    for path in targets:
        print(f"\n{'[dry-run] ' if args.dry_run else ''}{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
        counts = migrate_docx(path, dry_run=args.dry_run)
        if not counts:
            print("  (no hits — already current or no matches)")
            continue
        for label, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"  {n:4d}  {label}")
            total += n

    print(f"\nTotal replacements: {total}")
    if not args.dry_run and total:
        print("Backups written alongside each modified file as .docx.bak")
    return 0


if __name__ == "__main__":
    sys.exit(main())
