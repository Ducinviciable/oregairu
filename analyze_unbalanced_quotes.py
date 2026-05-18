# -*- coding: utf-8 -*-
"""
Analyze a .rpy file for where cumulative double-quote count becomes odd.
Prints the first 100 such lines to help locate missing/extra quotes.
"""
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print('Usage: python analyze_unbalanced_quotes.py path/to/file.rpy')
    sys.exit(2)

p = Path(sys.argv[1])
if not p.exists():
    print('File not found:', p)
    sys.exit(2)

count = 0
odd_lines = []
with p.open('r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        count += line.count('"')
        if count % 2 == 1:
            odd_lines.append((i, line.rstrip('\n')))

print(f'File: {p}\nTotal double quotes: {count}\nLines where cumulative quote count is odd: {len(odd_lines)}')
for ln, text in odd_lines[:200]:
    print(f'{ln}: {text}')

if odd_lines:
    sys.exit(1)
else:
    print('No odd cumulative quote positions found')
    sys.exit(0)
