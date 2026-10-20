#!/usr/bin/env python3
"""R33: the laws records_r33.py added to two records name declarations that their references must list (the
registry checks that every declaration a law names is a declared reference). Each name goes to the reference of
the file declaring it, in the module of its prefix (Tolerance.lean, LoopReturn.lean); nothing else changes.
The last history note (R33's) already says the laws were added. Rerun-safe."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REC = ROOT / 'theories/becoming/results/records'
B = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
for rid, mod in (('thresholds-of-waiting', 'Tolerance'), ('whether-a-loop-closes-a-difference', 'LoopReturn')):
    p = REC / (rid + '.json')
    d = json.loads(p.read_text())
    declared = {x for r in d['references'] for x in r.get('declarations', [])}
    ref = next(r for r in d['references'] if r['path'] == B + mod + '.lean')
    src = (ROOT / ref['path']).read_text()
    added = []
    for law in d.get('laws', []):
        for x in law.get('declarations', []):
            if x not in declared:
                assert x.startswith('Becoming.' + mod + '.'), (rid, x)
                assert x.rsplit('.', 1)[-1] in src, (rid, x)
                ref['declarations'].append(x)
                declared.add(x)
                added.append(x)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(rid, added)
