#!/usr/bin/env python3
"""F3 final sweep (19 October 2026): the apart register after the sweep.

usage (from the checkout root): python3 -B apart_sweep.py MEASURE.json

MEASURE.json is the output of `THEOREM-CONNECTIVITY.py` (without --write) on the swept tree. Entries of the
register that are no longer apart roots because their modules left the run (a superseded periphery module, or a
bridge or join module now in history) leave the register and are kept, with their categories and reasons, in
`apart-retired.json` beside this script. The two core theorems that stand apart because only the bridge used them
are registered. Any other unregistered root is left for its owner (the check then fails and names it).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REG = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
NEW = {
    'Becoming.ChangingContext.ends': {
        'module': 'Becoming.Context', 'category': 'model-witness',
        'reason': 'a fact about the constructed changing context (its course ends at 2); the bridge used it as the '
                  'witness that a changed history really ends, and left with the F3 sweep'},
    'Becoming.Joining.tree_lifts': {
        'module': 'Becoming.Joining', 'category': 'general-structure',
        'reason': 'every finite joining tree lifts where a description lifts a joining: a law of every joining on '
                  'any type of fragments; the bridge read it on the periphery\'s joining studies, and left with the '
                  'F3 sweep'},
}

measure = json.loads(Path(sys.argv[1]).read_text())
reg = json.loads(REG.read_text())
stale = set(measure['register_entries_not_apart_roots'])
retired = {k: reg['roots'][k] for k in sorted(stale)}
for k in stale:
    del reg['roots'][k]
for k, v in NEW.items():
    if k in measure['apart_roots_unclassified']:
        reg['roots'][k] = v
reg['about'] += (f' The F3 sweep (19 October 2026) removed the {len(retired)} entries whose modules left the run '
                 '(superseded periphery modules, bridge and join modules); they are kept in the bridge-fold workspace, '
                 'apart-retired.json.')
(HERE / 'apart-retired.json').write_text(json.dumps(
    {'about': 'Apart-register entries removed by the F3 sweep (19 October 2026): their theorems are in superseded '
              'periphery modules or in bridge and join modules now in lean/history/becoming/, so they are no longer '
              'in the measured run. Kept with their categories and reasons as the register held them.',
     'roots': retired}, indent=1, ensure_ascii=False) + '\n')
REG.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + '\n')
left = sorted(set(measure['apart_roots_unclassified']) - set(NEW))
print(json.dumps({'retired': len(retired), 'added': [k for k in NEW if k in reg['roots']], 'left_for_owners': len(left)}))
