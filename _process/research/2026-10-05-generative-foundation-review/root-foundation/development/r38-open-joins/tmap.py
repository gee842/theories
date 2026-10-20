#!/usr/bin/env python3
"""R38: regenerate the chapter's theorem map (EN, ZH) between its markers, with R36's `assemble.theorem_map`
and `assemble_zh.zh_map`, from the records and the live English chapter (the section that first links a record).

usage (from the checkout root): python3 -B tmap.py"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r36-chapter'))
import assemble  # noqa: E402
import assemble_zh  # noqa: E402

ROOT = HERE.parents[5]
EN = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
PAT = re.compile(r'<!-- theorem-map:begin -->.*?<!-- theorem-map:end -->', re.S)

en = EN.read_text()
# the sections are read with the map emptied, as R36 assembled it: the map's own rows link every record
bare = PAT.sub('<!-- theorem-map:begin -->\n<!-- theorem-map:end -->', en)
table, missing = assemble.theorem_map(ROOT, bare)
new_en = PAT.sub(lambda _m: '<!-- theorem-map:begin -->\n' + table + '\n<!-- theorem-map:end -->', en)
zh = ZH.read_text()
ztable, _ = assemble_zh.zh_map(ROOT, bare)
new_zh = PAT.sub(lambda _m: '<!-- theorem-map:begin -->\n' + ztable + '\n<!-- theorem-map:end -->', zh)
EN.write_text(new_en)
ZH.write_text(new_zh)
print('records placed by no section:', missing)
