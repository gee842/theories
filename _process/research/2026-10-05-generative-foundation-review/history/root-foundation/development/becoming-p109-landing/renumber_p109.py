#!/usr/bin/env python3
"""P109: move the study section from its provisional number to N, wherever the content names it.

usage: python3 -B renumber_p109.py W N [FROM]

FROM is the number the content carries now (131 as packaged). Changes the study heading and English paragraph, the new record's validation scope and history, and
the paired notes in process-and-frame-as-readings and counterfactual-is-the-course. Every replacement
asserts the text it replaces, so a second run fails instead of applying twice.
"""
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
N = int(sys.argv[2])
OLD = int(sys.argv[3]) if len(sys.argv) > 3 else 131
STUDY = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
REC = W / 'theories/becoming/results/records'


def once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


t = STUDY.read_text()
t = once(t, f'\n## {OLD}. 动作在哪里形成', f'\n## {N}. 动作在哪里形成')
t = once(t, f'Section {OLD} adds one core module, `Becoming.Coupling`', f'Section {N} adds one core module, `Becoming.Coupling`')
STUDY.write_text(t)

path = REC / 'where-a-move-is-formed.json'
r = json.loads(path.read_text())
r['validation_scope']['zh'] = once(r['validation_scope']['zh'], f'研究 §{OLD}', f'研究 §{N}')
r['validation_scope']['en'] = once(r['validation_scope']['en'], f'study section {OLD}', f'study section {N}')
r['history'][0]['zh'] = once(r['history'][0]['zh'], f'研究 §{OLD}', f'研究 §{N}')
r['history'][0]['en'] = once(r['history'][0]['en'], f'study section {OLD}', f'study section {N}')
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')

for ident in ('process-and-frame-as-readings', 'counterfactual-is-the-course'):
    path = REC / f'{ident}.json'
    r = json.loads(path.read_text())
    note = r['history'][-1]
    note['zh'] = once(note['zh'], f'P109（动作在哪里形成，研究 §{OLD}）', f'P109（动作在哪里形成，研究 §{N}）')
    note['en'] = once(note['en'], f'P109 (where a move is formed, study section {OLD})', f'P109 (where a move is formed, study section {N})')
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print(f'study section {OLD} -> {N}')
