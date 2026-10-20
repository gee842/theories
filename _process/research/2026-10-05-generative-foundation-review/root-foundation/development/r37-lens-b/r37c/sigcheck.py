#!/usr/bin/env python3
"""R37c statement preservation: R37's sigcheck (development/r37-lens-b/sigcheck.py) with R37c's table, which
is empty (R37c removes and renames nothing), so the name pattern matches nothing.
usage: python3 -B sigcheck.py BASE_RECEIPT_JSON NEW_RECEIPT_JSON"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R37 = HERE.parent / 'sigcheck.py'
os.environ['RENAME_TABLE'] = str(HERE / 'RENAME-TABLE.json')
src = R37.read_text()
old = "pat = re.compile(r\"(?<![\\w.'])(Becoming\\.)?(\" + '|'.join(re.escape(n) for n in names) + r\")(?![\\w'])\")"
assert old in src
src = src.replace(old, old + "\nif not names:\n    pat = re.compile(r'(?!x)x')")
exec(compile(src, str(R37), 'exec'), {'__name__': '__main__', '__file__': str(R37)})
