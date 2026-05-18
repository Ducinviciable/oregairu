#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract dialogue lines from a Ren'Py route file into a CSV translation sheet."""

import argparse
import csv
import re
from pathlib import Path

DEFAULT_INPUT = Path(__file__).parent.parent / 'game' / 'scripts' / 'E4' / 'E4_IRO.rpy'
DEFAULT_OUTPUT = Path(__file__).parent / 'DICH_IROHA_ROUTE.csv'

SPEAKER_RE = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s+"((?:[^"\\]|\\.)*)"\s*$')
NARRATOR_RE = re.compile(r'^\s+"((?:[^"\\]|\\.)*)"\s*$')
IGNORE_PREFIXES = ('scene ', 'show ', 'hide ', 'play ', 'stop ', 'with ', 'call ', 'jump ', 'label ', 'return', 'menu ', 'voice ')


def unescape_renpy_string(text):
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '\\' and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt == '\\':
                result.append('\\')
                i += 2
                continue
            if nxt == '"':
                result.append('"')
                i += 2
                continue
            if nxt == 'n':
                result.append('\n')
                i += 2
                continue
            if nxt == 'r':
                result.append('\r')
                i += 2
                continue
            if nxt == 't':
                result.append('\t')
                i += 2
                continue
        result.append(ch)
        i += 1
    return ''.join(result)


def extract_dialogues(rpy_file):
    dialogues = []
    lines = Path(rpy_file).read_text(encoding='utf-8').splitlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if not stripped or stripped.startswith('#'):
            continue
        if any(stripped.startswith(prefix) for prefix in IGNORE_PREFIXES):
            continue

        match = SPEAKER_RE.match(line)
        if match:
            speaker = match.group(1)
            text = unescape_renpy_string(match.group(2))
            if len(text) > 3 and not text.startswith(('audio/', 'movies/')):
                dialogues.append({
                    'line_number': i,
                    'character': speaker,
                    'original': text,
                    'vietnamese': ''
                })
            continue

        narrator_match = NARRATOR_RE.match(line)
        if narrator_match and line.startswith('    '):
            text = unescape_renpy_string(narrator_match.group(1))
            if len(text) > 5 and not text.startswith(('audio/', 'movies/')):
                dialogues.append({
                    'line_number': i,
                    'character': 'NARRATOR',
                    'original': text,
                    'vietnamese': ''
                })

    return dialogues


def save_to_csv(dialogues, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['line_number', 'character', 'original', 'vietnamese'])
        writer.writeheader()
        writer.writerows(dialogues)

    print(f'✅ Đã lưu {len(dialogues)} dòng text vào: {output_file}')


def parse_args():
    parser = argparse.ArgumentParser(description='Extract Ren\'Py dialogues into a CSV sheet.')
    parser.add_argument('--input', default=str(DEFAULT_INPUT), help='Path to the source .rpy file.')
    parser.add_argument('--output', default=str(DEFAULT_OUTPUT), help='Path to write the CSV file.')
    return parser.parse_args()


def main():
    args = parse_args()
    rpy_file = Path(args.input)
    output_file = Path(args.output)

    if not rpy_file.exists():
        print(f'❌ Không tìm thấy file: {rpy_file}')
        return

    print(f'📖 Đang trích xuất text từ: {rpy_file}')
    dialogues = extract_dialogues(rpy_file)
    save_to_csv(dialogues, output_file)

    print('\n📋 Hướng dẫn sử dụng:')
    print(f'1. Mở file: {output_file}')
    print("2. Điền cột 'vietnamese' với bản dịch Tiếng Việt")
    print('3. Chạy script generate_translation.py với --csv và --output phù hợp')


if __name__ == '__main__':
    main()
