#!/usr/bin/env python3
"""Report coverage and placeholder cleanup for a route translation file."""

import argparse
import re
from pathlib import Path

from extract_text import extract_dialogues

DEFAULT_SOURCE = Path(__file__).parent.parent / 'game' / 'scripts' / 'E4' / 'E4_IRO.rpy'
DEFAULT_TRANSLATION = Path(__file__).parent.parent / 'game' / 'scripts' / 'E4' / 'E4_IRO_vietnamese_AUTO.rpy'


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


def strip_inline_tags(text):
    return re.sub(r'\{[^}]+\}', '', text)


def extract_old_entries(path):
    text = Path(path).read_text(encoding='utf-8')
    return [unescape_renpy_string(m.strip()) for m in re.findall(r'^[^#\n]*old\s+"((?:[^"\\]|\\.)*)"', text, flags=re.MULTILINE | re.DOTALL)]


def extract_commented_old_entries(path):
    text = Path(path).read_text(encoding='utf-8')
    commented = re.findall(r'^[ \t]*#.*old\s+"((?:[^"\\]|\\.)*)"', text, flags=re.MULTILINE | re.DOTALL)
    flagged = []
    for item in commented:
        raw = unescape_renpy_string(item).strip()
        if re.search(r'\{[^}]+\}', raw):
            continue
        stripped = strip_inline_tags(raw).strip()
        if stripped:
            flagged.append(raw)
    return flagged


def parse_args():
    parser = argparse.ArgumentParser(description='Report translation coverage for a Ren\'Py route.')
    parser.add_argument('--source', default=str(DEFAULT_SOURCE), help='Path to the source .rpy file.')
    parser.add_argument('--translation', default=str(DEFAULT_TRANSLATION), help='Path to the generated translation .rpy file.')
    return parser.parse_args()


def main():
    args = parse_args()
    source = Path(args.source)
    translation = Path(args.translation)

    if not source.exists():
        print(f'Source file not found: {source}')
        return
    if not translation.exists():
        print(f'Translation file not found: {translation}')
        return

    dialogues = extract_dialogues(source)
    active_old = extract_old_entries(translation)
    flagged_old = extract_commented_old_entries(translation)

    print(f'Total dialogue-like strings in {source.name}:', len(dialogues))
    print(f'Translated (active) lines in translation file:', len(active_old))
    print(f'Flagged/commented placeholders remaining:', len(flagged_old))
    if flagged_old:
        print('\n--- Flagged examples ---')
        for x in flagged_old[:30]:
            print(x)


if __name__ == '__main__':
    main()
