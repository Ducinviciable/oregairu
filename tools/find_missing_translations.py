#!/usr/bin/env python3
from pathlib import Path
import re
import argparse
from extract_text import extract_dialogues

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

parser = argparse.ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--translation', required=True)
args = parser.parse_args()
source = Path(args.source)
translation = Path(args.translation)
if not source.exists():
    print('Source not found:', source)
    raise SystemExit(1)
if not translation.exists():
    print('Translation not found:', translation)
    raise SystemExit(1)

raw = extract_dialogues(source)
# `extract_dialogues` returns dicts; pull the `original` text for comparison
dialogues = [entry['original'] if isinstance(entry, dict) and 'original' in entry else entry for entry in raw]
text = translation.read_text(encoding='utf-8')
active_old = [unescape_renpy_string(m.strip()) for m in re.findall(r'^[^#\n]*old\s+"((?:[^"\\\\]|\\\\.)*)"', text, flags=re.MULTILINE)]
missing = [d for d in dialogues if d not in active_old]
print('Total source dialogues:', len(dialogues))
print('Active translations in file:', len(active_old))
print('Missing count:', len(missing))
if missing:
    print('\nMissing lines:')
    for i,m in enumerate(missing,1):
        print(f'{i}. {m}')
else:
    print('No missing lines.')
