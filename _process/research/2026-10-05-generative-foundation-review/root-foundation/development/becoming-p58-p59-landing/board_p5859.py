#!/usr/bin/env python3
"""Mark P58 and P59 landed on the work board (own rows and the queue line only):
python3 -B board_p5859.py ROOT HASH"""
import json
import re
import sys
from pathlib import Path

ROOT, H = Path(sys.argv[1]), sys.argv[2]
B = ROOT / '_process/BECOMING-WORKBOARD.md'
STUDY = (ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md').read_text()
S58 = re.search(r'^## (\d+)\. 可判定性局部化（P58）', STUDY, re.M).group(1)
S59 = re.search(r'^## (\d+)\. 不平衡作为关系项：先证等价（P59）', STUDY, re.M).group(1)
LB = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
receipt = json.load(open(LB / 'becoming/becoming-verification.json'))
CORE = receipt['utc']
COUNT = {m['module']: m['theorems'] for m in receipt['modules']}
PERI = json.load(open(LB / 'universal-ethics/generative-capacity/correction-inquiry-verification.json'))['utc']
INV = (ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.md').read_text()


def total(label):
    return int(re.search(r'^\| ' + re.escape(label) + r'[^|\n]*\| (\d+) \|$', INV, re.M).group(1))


A, P = total('陈述依赖它（计数或构造）'), total('只在证明中用到 /')
STATUS = {
    '| P58 ': (
        f'landed `{H}` (10-12) with P59, one run (study §{S58}; receipts core {CORE}, periphery {PERI}): core module '
        f'`Becoming.Decidedness` ({COUNT["Becoming.Decidedness"]} theorems): a count as a relation, existing exactly where '
        'what it counts is decided; the census between counts with no decidedness; in a finite family coming to be '
        'recurring makes ceasing never stop for good and conversely, with none; decided from some step on, the '
        'recurrence law. In place, names kept, the unused decision procedure dropped: `World.rests_covering`, '
        '`World.rests`, `World.comes_to_rest` (through the new covering form `World.comes_to_rest_from`), '
        '`World.Finite.comes_to_rest`, `World.rest_few`, `World.premised_rests`, `World.sample_rests`; settling lemmas in '
        'Space (`falls_settle`, `Web.generation_settles`, `World.arising_unrefuted_covering`) and Openness '
        '(`Flow.change_settles`, `Listed.few_of_settled`). Inventory page `DECIDABILITY-INVENTORY.md` from a periphery '
        f'Lean tool: {A} statements depend on decidedness, {P} use it only in proofs, each with its reason. Records '
        'counts-exist-where-decided and recurrence-without-decidedness new, four extended, three related; every axiom '
        'report empty. No independent review yet'),
    '| P59 ': (
        f'landed `{H}` (10-12) with P58, one run (study §{S59}; same receipts): core module `Becoming.Imbalance` '
        f'({COUNT["Becoming.Imbalance"]} theorems): the imbalance counted as the exchange of one more relatum, never '
        'active and requiring nothing, so every flow balances; balance on a family across a step is exactly that relatum '
        'idle; the two representations equivalent step by step (`Flow.withImbalance_acting_taking_on_iff`). Not adopted; '
        'adoption is Ren\'s. New record imbalance-as-relatum; every axiom report empty. No independent review yet'),
}
lines = B.read_text().split('\n')
done = set()
for i, r in enumerate(lines):
    for prefix, status in STATUS.items():
        if r.startswith(prefix):
            cells = r.split(' | ')
            assert len(cells) == 5 and cells[2].startswith('verified in scratch'), (prefix, cells[2][:80])
            cells[2], cells[3] = status, 'main'
            lines[i] = ' | '.join(cells)
            done.add(prefix)
    if r.startswith('- P59 `Becoming.Imbalance` (equivalence only, not adopted') or \
            r.startswith('- **Next:** P59 `Becoming.Imbalance`'):
        lines[i] = (f'- ~~P59 `Becoming.Imbalance` + P58 (Universal Metaethical Core)~~ landed `{H}` (§{S58}, §{S59}; '
                    f'receipt {CORE}, periphery {PERI}).')
        done.add('queue')
assert done == set(STATUS) | {'queue'}, done
B.write_text('\n'.join(lines))
print('board: P58, P59 and the queue line marked landed at', H)
