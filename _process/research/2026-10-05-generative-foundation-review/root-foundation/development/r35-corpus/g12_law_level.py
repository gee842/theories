#!/usr/bin/env python3
"""R35 step 3, G12: agreement split by law level. Each passage's law level is computed by the verifiers, never
stored in passages.json (ZH extends both maps): `encoding` where every declaration it cites is a fact about the
hexagram encoding (namespace `Becoming.Hexagram`: lemmas about Fin 64, tables, `decide`), `general` where none is
(laws over every process, web, flow, world or law of exchange, and the root namespace), `mixed` where both occur.
verify_mapping.py (Y1) and verify_ro.py (RO) print the split by kind, and their --table adds the column
律的层次 after 关系; the chapters' tables (YI-ZHUAN-AND-BECOMING, CHINESE-SOURCES-AND-BECOMING) are spliced from
--table between their markers, so the check that the chapter's tables are the printed ones stays exact.
Run once from the checkout root: python3 -B g12_law_level.py"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
DEV = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development'

LEVEL = '''

# Law level (R35, G12): computed from the declarations a passage cites, never stored in passages.json.
ENCODING = 'Hexagram'  # the hexagram encoding: Becoming.Hexagram lemmas about Fin 64, tables, decide
LEVEL_ZH = {'general': '一般律', 'encoding': '编码', 'mixed': '兼有', None: '—'}


def law_level(p):
    """'encoding' where every cited declaration is in namespace Becoming.Hexagram, 'general' where none is, 'mixed'
    where both occur; None for a passage citing no declaration."""
    names = [d.removeprefix('Becoming.') for d in p.get('declarations', [])]
    if not names:
        return None
    enc = [n.split('.')[0] == ENCODING for n in names]
    return 'encoding' if all(enc) else 'mixed' if any(enc) else 'general'


def level_split(passages, kinds):
    """{kind: {level: count}} for the summary line."""
    out = {k: {} for k in kinds}
    for p in passages:
        lv = law_level(p)
        out[p['kind']][lv] = out[p['kind']].get(lv, 0) + 1
    return out


def level_line(passages, kinds):
    names = {'general': 'general laws', 'encoding': 'the encoding only', 'mixed': 'both', None: 'no declaration'}
    split = level_split(passages, kinds)
    return 'by law level: ' + '; '.join(
        f"{k} {sum(v.values())} (" + ', '.join(f'{v[lv]} through {names[lv]}' for lv in ('general', 'encoding', 'mixed', None) if v.get(lv)) + ')'
        for k, v in split.items())
'''


def patch(path, pairs):
    s = path.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path.name, a[:70])
        s = s.replace(a, b)
    path.write_text(s)


y1 = DEV / 'y1-changes/verify_mapping.py'
patch(y1, [
    ("def table(passages):\n    rows = ['| 经文 | 出处 | 关系 | 脊柱上的声明 | 读法（AI） |', '|---|---|---|---|---|']\n",
     LEVEL.lstrip('\n') + "\n\ndef table(passages):\n    rows = ['| 经文 | 出处 | 关系 | 律的层次 | 脊柱上的声明 | 读法（AI） |', '|---|---|---|---|---|---|']\n"),
    ("        rows.append(f\"| <a id=\\\"p-{p['id']}\\\"></a>{text} | {p['locator']} | {KIND_ZH[p['kind']]} | {decls} | {p['reading']} |\")\n",
     "        rows.append(f\"| <a id=\\\"p-{p['id']}\\\"></a>{text} | {p['locator']} | {KIND_ZH[p['kind']]} | {LEVEL_ZH[law_level(p)]} | {decls} | {p['reading']} |\")\n"),
    ("    print('censuses (listed + exceptions): '",
     "    print(level_line(passages, KIND_ZH))\n    print('censuses (listed + exceptions): '"),
])

ro = DEV / 'ro-relational-sources/verify_ro.py'
patch(ro, [
    ("def table(passages, tradition):\n    rows = ['| 原文 | 出处 | 关系 | 脊柱上的声明与记录 | 读法（AI） |', '|---|---|---|---|---|']\n",
     LEVEL.lstrip('\n') + "\n\ndef table(passages, tradition):\n    rows = ['| 原文 | 出处 | 关系 | 律的层次 | 脊柱上的声明与记录 | 读法（AI） |', '|---|---|---|---|---|---|']\n"),
    ("        rows.append(f\"| <a id=\\\"p-{p['id']}\\\"></a>{text} | {p['locator']} | {KIND_ZH[p['kind']]} | {cell} | {p['reading']} |\")\n",
     "        rows.append(f\"| <a id=\\\"p-{p['id']}\\\"></a>{text} | {p['locator']} | {KIND_ZH[p['kind']]} | {LEVEL_ZH[law_level(p)]} | {cell} | {p['reading']} |\")\n"),
    ("    print('by tradition: ' + ', '.join(f'{t} {n}' for t, n in per.items() if n))\n",
     "    print('by tradition: ' + ', '.join(f'{t} {n}' for t, n in per.items() if n))\n    print(level_line(passages, KIND_ZH))\n"),
])
print('patched')
