#!/usr/bin/env python3
"""P120: move the study section from its provisional number to N, wherever the content names it.

usage: python3 -B renumber_p120.py W N [FROM]

FROM is the number the content carries now (154 as packaged). Changes the study heading and English
paragraph, the new record's validation scope and history, and the paired note in
how-a-carried-difference-grows. Every replacement asserts the text it replaces, so a second run fails
instead of applying twice.
"""
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
N = int(sys.argv[2])
OLD = int(sys.argv[3]) if len(sys.argv) > 3 else 154
STUDY = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
REC = W / 'theories/becoming/results/records'


def once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


t = STUDY.read_text()
t = once(t, f'\n## {OLD}. 截断所失', f'\n## {N}. 截断所失')
t = once(t, f'Section {OLD} adds one core module, `Becoming.Remainder`',
         f'Section {N} adds one core module, `Becoming.Remainder`')
STUDY.write_text(t)

path = REC / 'what-a-cut-loses.json'
r = json.loads(path.read_text())
r['validation_scope']['zh'] = once(r['validation_scope']['zh'], f'研究 §{OLD}', f'研究 §{N}')
r['validation_scope']['en'] = once(r['validation_scope']['en'], f'study section {OLD}', f'study section {N}')
r['history'][0]['zh'] = once(r['history'][0]['zh'], f'研究 §{OLD}', f'研究 §{N}')
r['history'][0]['en'] = once(r['history'][0]['en'], f'study section {OLD}', f'study section {N}')
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')

path = REC / 'how-a-carried-difference-grows.json'
r = json.loads(path.read_text())
hits = [h for h in r['history'] if h['en'].startswith('16 October 2026, P120 ')]
assert len(hits) == 1, len(hits)
hits[0]['zh'] = once(hits[0]['zh'], f'P120（截断所失，研究 §{OLD}）', f'P120（截断所失，研究 §{N}）')
hits[0]['en'] = once(hits[0]['en'], f'P120 (what a cut loses, study section {OLD})',
                     f'P120 (what a cut loses, study section {N})')
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print(f'study section {OLD} -> {N}')
