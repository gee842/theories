#!/usr/bin/env python3
"""R35 step 3, G12: splice the passage tables the verifiers print (--table, with the law-level column) into the two
chapters between their markers, and say once above the first table what the column means. Nothing else in the
chapters changes. Run from the checkout root after g12_law_level.py: python3 -B g12_splice.py"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
DEV = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development'
CH = ROOT / 'theories/becoming/chapters'
for kit in ('y1-changes', 'ro-relational-sources'):
    sys.path.insert(0, str(DEV / kit))
import verify_mapping as Y  # noqa: E402
import verify_ro as R  # noqa: E402

NOTE_ZH = ('“律的层次”由校验脚本从所引声明算出，不存于对应表中：所引声明全在 `Becoming.Hexagram` 命名空间（卦的编码上的事实：'
           '`Fin 64` 上的引理、表、`decide`）为“编码”，全不在为“一般律”（对每个过程、网、流、世界或交换之律成立的律），两者都有为“兼有”。')


def splice(text, begin, end, body):
    i, j = text.index(begin) + len(begin), text.index(end)
    return text[:i] + '\n' + body + '\n' + text[j:]


def note_before(text, marker):
    if NOTE_ZH in text:
        return text
    i = text.index(marker)
    return text[:i] + NOTE_ZH + '\n\n' + text[i:]


y1 = json.loads((DEV / 'y1-changes/passages.json').read_text())['passages']
path = CH / 'YI-ZHUAN-AND-BECOMING.md'
t = path.read_text()
t = splice(t, '<!-- passage-map:begin -->', '<!-- passage-map:end -->', Y.table(y1))
t = note_before(t, '<!-- passage-map:begin -->')
path.write_text(t)

ro = json.loads((DEV / 'ro-relational-sources/passages.json').read_text())['passages']
path = CH / 'CHINESE-SOURCES-AND-BECOMING.md'
t = path.read_text()
traditions = re.findall(r'<!-- passage-map:(.+?):begin -->', t)
for tr in traditions:
    t = splice(t, f'<!-- passage-map:{tr}:begin -->', f'<!-- passage-map:{tr}:end -->', R.table(ro, tr))
t = note_before(t, f'<!-- passage-map:{traditions[0]}:begin -->')
path.write_text(t)
print('spliced', len(traditions) + 1, 'tables')
