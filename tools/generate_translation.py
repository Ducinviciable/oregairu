#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Ren'Py translation files from a CSV table."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


DEFAULT_CSV = Path(__file__).parent / "E1_IRO.csv"
DEFAULT_OUTPUT = Path(__file__).parent.parent / "game" / "scripts" / "E1" / "E1_IRO_vietnamese_AUTO.rpy"


def escape_renpy_string(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r", "\\r")
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )


def unescape_renpy_string(text: str) -> str:
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt == "\\":
                result.append("\\")
                i += 2
                continue
            if nxt == '"':
                result.append('"')
                i += 2
                continue
            if nxt == "n":
                result.append("\n")
                i += 2
                continue
            if nxt == "r":
                result.append("\r")
                i += 2
                continue
            if nxt == "t":
                result.append("\t")
                i += 2
                continue
        result.append(ch)
        i += 1
    return "".join(result)


def load_existing_old_strings(path: Path) -> set[str]:
    if not path.exists():
        return set()

    text = path.read_text(encoding="utf-8")
    captured = re.findall(r'^[ \t]*old\s+"((?:[^"\\]|\\.)*)"', text, flags=re.MULTILINE)
    return {unescape_renpy_string(value) for value in captured}


def load_global_existing_old_strings(root: Path, ignore_paths: set[Path] | None = None) -> set[str]:
    ignore_paths = {path.resolve() for path in (ignore_paths or set())}
    existing = set()

    for translation_path in root.rglob("*_vietnamese*.rpy"):
        if translation_path.resolve() in ignore_paths:
            continue
        existing.update(load_existing_old_strings(translation_path))

    return existing


def generate_translation_file(
    csv_file: Path,
    output_rpy: Path,
    manual_rpy: Path | None = None,
    skip_existing_manual: bool = True,
) -> None:
    existing_old_strings = set()

    if skip_existing_manual:
        if manual_rpy is None:
            manual_rpy = output_rpy.with_name(output_rpy.name.replace("_AUTO", ""))
        existing_old_strings = load_existing_old_strings(manual_rpy)

    script_root = Path(__file__).resolve().parent.parent / "game" / "scripts"
    existing_old_strings.update(
        load_global_existing_old_strings(
            script_root,
            ignore_paths={output_rpy.resolve()},
        )
    )

    translations: list[tuple[str, str]] = []
    seen_originals: set[str] = set()

    with csv_file.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            original = (row.get("original") or "").strip()
            vietnamese = (row.get("vietnamese") or "").strip()

            if not original or not vietnamese:
                continue
            if original in seen_originals:
                continue
            if skip_existing_manual and original in existing_old_strings:
                continue

            seen_originals.add(original)
            translations.append((original, vietnamese))

    rpy_content = [
        "# -*- coding: utf-8 -*-",
        "# Auto-generated translation file",
        "",
        "translate vietnamese strings:",
        "",
    ]

    for original, vietnamese in translations:
        rpy_content.append(f'    old "{escape_renpy_string(original)}"')
        rpy_content.append(f'    new "{escape_renpy_string(vietnamese)}"')
        rpy_content.append("")

    output_rpy.parent.mkdir(parents=True, exist_ok=True)
    output_rpy.write_text("\n".join(rpy_content).rstrip() + "\n", encoding="utf-8")

    print(f"✅ Đã generate: {output_rpy}")
    print(f"📊 Tổng cộng: {len(translations)} dòng dịch")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Ren'Py translation strings from CSV.")
    parser.add_argument("--csv", default=str(DEFAULT_CSV), help="Path to the translation CSV file.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Path to write the generated .rpy file.")
    parser.add_argument("--manual-rpy", default=None, help="Manual translation file to use for duplicate detection.")
    parser.add_argument(
        "--include-existing-manual",
        action="store_true",
        help="Do not skip strings already present in the manual translation file.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_file = Path(args.csv)
    output_rpy = Path(args.output)
    manual_rpy = Path(args.manual_rpy) if args.manual_rpy else None

    if not csv_file.exists():
        print(f"❌ Không tìm thấy file CSV: {csv_file}")
        return

    print(f"📝 Đang generate translation file từ: {csv_file}")
    generate_translation_file(
        csv_file=csv_file,
        output_rpy=output_rpy,
        manual_rpy=manual_rpy,
        skip_existing_manual=not args.include_existing_manual,
    )

    print(f"\n✨ Hoàn tất! File dịch: {output_rpy}")
    print("\n📌 Tiếp theo:")
    print("1. Copy file vào game/scripts/<route>/")
    print("2. Chạy game và chọn Tiếng Việt")


if __name__ == "__main__":
    main()
