#!/usr/bin/env python3
"""Register RC's one apart root (usage, from the checkout root: python3 -B register_apart.py; idempotent).
Counts.share_not_lower_counts restates share_not_lower of Becoming.Capture in the share order of counts."""
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
d['roots']['Becoming.RuleCapture.Counts.share_not_lower_counts'] = {
    'module': 'Becoming.RuleCapture',
    'category': 'restates',
    'reason': 'restates share_not_lower (Becoming.Capture) in the share order of counts, to show that the order the '
              'laws of RuleCapture read on courses is the comparison of Capture; share_not_lower is read on worlds '
              'by CaptureWorlds, and the order on courses by every other law of RuleCapture'}
F.write_text(json.dumps(d, ensure_ascii=False, indent=indent) + '\n', encoding='utf-8')
print('registered, indent', indent)
