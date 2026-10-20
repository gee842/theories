#!/usr/bin/env python3
"""R34: records follow-up (run once, after records_r34.py and rebind.py). The dependency of
alignment-direction-g0-j on what-pooled-coupling-reaches closed a cycle in the result graph (what-pooled-coupling-
reaches → … → organizational-formation-from-generative-comparison → alignment-direction-g0-j), so it becomes a
`related` link with the same detail; the direction's laws still cite Flow.act_selected_by_pool's consequence
Direction.widening_selected_by_pool, which is in Becoming.Direction."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
p = ROOT / 'theories/becoming/results/records/alignment-direction-g0-j.json'
d = json.loads(p.read_text())
dep = next(x for x in d['dependencies'] if x['id'] == 'what-pooled-coupling-reaches')
d['dependencies'] = [x for x in d['dependencies'] if x['id'] != 'what-pooled-coupling-reaches']
d.setdefault('related', []).append({'id': 'what-pooled-coupling-reaches', 'detail': dep['detail']})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('moved to related')
