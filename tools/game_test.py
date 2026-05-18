#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic checker for Ren'Py .rpy translation files.
Checks performed:
 - Lines starting with 'translate <lang>:' should include 'strings'
 - 'old' entries should be followed by a 'new' before next 'old' or end of block
 - Basic double-quote balance per file
 - Reports summary and exits with non-zero code on problems
"""

import os
import re
import sys

ROOT = os.path.dirname(__file__)
GAME_DIR = os.path.join(ROOT, 'game')

translate_re = re.compile(r'^\s*translate\s+(\S+)\s*(.*):\s*$')
old_re = re.compile(r'^\s*old\s+"(.*)"\s*$')
new_re = re.compile(r'^\s*new\s+"(.*)"\s*$')

errors = []

for dirpath, dirnames, filenames in os.walk(GAME_DIR):
    for fn in filenames:
        if not fn.endswith('.rpy'):
            continue
        path = os.path.join(dirpath, fn)
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Quote balance
        all_text = ''.join(lines)
        dq = all_text.count('"')
        if dq % 2 != 0:
            errors.append((path, 'Unbalanced double quotes (odd count: {})'.format(dq)))

        expecting_new = False
        line_old = None
        for i, raw in enumerate(lines, start=1):
            line = raw.rstrip('\n')
            m = translate_re.match(line)
            if m:
                lang = m.group(1)
                rest = m.group(2)
                # if translate block has no 'strings' keyword, warn
                if 'strings' not in rest and not rest.strip().endswith('strings'):
                    errors.append((path, f'Line {i}: translate {lang} missing "strings" (found: "{line.strip()}")'))

            mo = old_re.match(line)
            if mo:
                if expecting_new:
                    errors.append((path, f'Line {i}: Found "old" while previous "old" at line {line_old} has no matching "new"'))
                expecting_new = True
                line_old = i
                continue
            mn = new_re.match(line)
            if mn:
                if not expecting_new:
                    # new without old is suspicious but not fatal
                    errors.append((path, f'Line {i}: "new" found without preceding "old"'))
                expecting_new = False
                line_old = None

        if expecting_new:
            errors.append((path, f'EOF: "old" at line {line_old} has no matching "new"'))

# Print report
if not errors:
    print('✅ No issues found by game_test.py')
    sys.exit(0)

print('❌ Issues found:')
for path, msg in errors:
    print(f'- {path}: {msg}')

# exit non-zero so CI / caller knows something failed
sys.exit(2)
