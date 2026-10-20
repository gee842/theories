#!/usr/bin/env python3
"""Register SG's one apart root (usage, from the checkout root: python3 -B register_apart.py)."""
import json
from pathlib import Path

F = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
text = F.read_text(encoding='utf-8')
d = json.loads(text)
for indent in (1, 2):
    if json.dumps(d, ensure_ascii=False, indent=indent) + '\n' == text:
        break
else:
    raise SystemExit('register format not reproduced')
d['roots']['Becoming.Undecided.incomplete'] = {
    'module': 'Becoming.Undecided',
    'category': 'general-structure',
    'reason': 'a law of every family of three-valued readings on any type (the diagonal with the rotation of the '
              'values, by Diagonal.fixed_of_complete); the run form of completion for every map moving every value '
              'is DiagonalRuns.incomplete, so an instance on a run would only fix the type'}
F.write_text(json.dumps(d, ensure_ascii=False, indent=indent) + '\n', encoding='utf-8')
print('registered, indent', indent)
