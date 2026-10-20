#!/usr/bin/env python3
"""R46 statement preservation: R38's sigcheck (R37's with an empty table, development/r38-open-joins/sigcheck.py)
with R46's table, which is empty (R46 removes and renames nothing).
usage: python3 -B sigcheck.py BASE_RECEIPT_JSON NEW_RECEIPT_JSON"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
R38 = HERE.parent / 'r38-open-joins' / 'sigcheck.py'
os.environ['RENAME_TABLE'] = str(HERE / 'RENAME-TABLE.json')
src = R38.read_text().replace("os.environ['RENAME_TABLE'] = str(HERE / 'RENAME-TABLE.json')", '')
exec(compile(src, str(R38), 'exec'), {'__name__': '__main__', '__file__': str(R38)})
