#!/usr/bin/env python3
"""P107's study section moves from 124 to N, after integration I3a took section 124 on main.

usage: renumber_p107.py ROOT N
Only P107's own text changes: its study heading and English paragraph, its two citations in the chapter and two in the
zero-premise plan, and the P107 strings of its seven records (history notes and validation scopes).
Every replacement asserts the count it expects, so a second run fails instead of renumbering twice.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
N = int(sys.argv[2])
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
REC = ROOT / 'theories/becoming/results/records'
NEW = ['returning-novelty-forgetting-on-levels', 'premises-read-off-the-exchange', 'unity-of-readings']
EDITED = ['imbalance-as-relatum', 'map-of-premises', 'process-and-frame-as-readings', 'contextual-registration']


def sub(path, pairs):
    s = path.read_text()
    for old, new, count in pairs:
        assert s.count(old) == count, (path.name, s.count(old), count, old[:70])
        s = s.replace(old, new)
    path.write_text(s)


sub(RF / 'BECOMING-RENEWAL-READING.md', [
    ('## 124. 从关系开始的重建：', f'## {N}. 从关系开始的重建：', 1),
    ('Section 124 adds three core modules', f'Section {N} adds three core modules', 1)])
sub(ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', [
    ('`Contextual.world`，研究 §124）', f'`Contextual.world`，研究 §{N}）', 1),
    ('`Contextual.world`, study section 124)', f'`Contextual.world`, study section {N})', 1)])
sub(RF / 'ZERO-PREMISE-PLAN.md', [
    ('（P107，研究 §124）', f'（P107，研究 §{N}）', 1),
    ('(P107, study section 124)', f'(P107, study section {N})', 1)])

for rid in NEW + EDITED:
    p = REC / f'{rid}.json'
    r = json.loads(p.read_text())
    seen = 0
    for note in r['history']:
        for lang, old in (('zh', '研究 §124'), ('en', 'study section 124')):
            if note[lang].startswith(('2026-10-14 P107（', '14 October 2026, P107 (', '2026-10-14：新增，按 Ren 批准',
                                      '14 October 2026: added under Ren')) and old in note[lang]:
                assert note[lang].count(old) == 1, (rid, lang)
                note[lang] = note[lang].replace(old, f'研究 §{N}' if lang == 'zh' else f'study section {N}')
                seen += 1
    if rid in NEW:
        vs = r['validation_scope']
        for lang, old, new in (('zh', '作者反审见研究 §124', f'作者反审见研究 §{N}'),
                               ('en', 'Author counterreview in study section 124', f'Author counterreview in study section {N}')):
            assert vs[lang].count(old) == 1, (rid, lang)
            vs[lang] = vs[lang].replace(old, new)
    assert seen == 2, (rid, seen)
    p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print(f'P107 study section 124 -> {N}: study heading, chapter (2), plan (2), seven records')
