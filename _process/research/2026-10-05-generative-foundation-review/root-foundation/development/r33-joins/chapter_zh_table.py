#!/usr/bin/env python3
"""R33: R32's chapter_zh_table.py with the two modules R33 joined into Becoming.LawAlongRun gone too:
the Chinese chapter's §9 module table takes the receipt's theorem counts and the computed layers.
usage: python3 -B chapter_zh_table.py RECEIPT_ID"""
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r32-folds'))
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import fold  # noqa: E402
import layers  # noqa: E402

layers.GONE += ['Becoming.' + x for x, _ in fold.FOLDS]
layers.GONE += ['Becoming.LawThroughCoupling', 'Becoming.LawThroughChangingCoupling']
runpy.run_path(str(HERE.parent / 'r31-support' / 'chapter_zh_table.py'), run_name='__main__')
