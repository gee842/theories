#!/usr/bin/env python3
"""R37: the one table of what B14, B4 and B6 removed, renamed and moved, read by sigcheck.py,
docnames.py and rebind.py. usage: python3 -B table.py   (writes RENAME-TABLE.json)

* removed: a declaration no longer stated, with the name stating it now (`kept`), or none where its
  statement became trivial (`CrossSituational.distinct_iff`, `Distinct l ↔ Distinct l`);
* renamed: the same declaration under another name (constructors of the relay's members now those
  of `Witnesses.Member`; the laws of `DistinctBy` now in the namespace of `DistinctUnder`);
* moved: the same full name, in another module."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = 'Becoming.'
removed = []
for f in ('b6-removals.json', 'b6-removals-2.json', 'b6-removals-3.json'):
    for r in json.load(open(HERE / f))['rows']:
        removed.append({'old': r['old'], 'kept': r['new'], 'item': 'B6', 'why': 'the same definition or statement, one name'})
removed.append({'old': B + 'CrossSituational.distinct_iff', 'kept': None, 'item': 'B6',
                'why': 'with one Distinct its statement is Distinct l ↔ Distinct l'})
B4 = [('JointAlike.' + n, 'AlikeWith.' + n) for n in
      ('refl', 'symm', 'trans', 'alike', 'realized', 'step', 'parts', 'matchesParts', 'holds_iff', 'functional')]
B4 += [('JointAlike.sameJointTests', 'AlikeWith.sameTestsWith')]
B4 += [('JointBisimulation.' + n, 'BisimulationWith.' + n) for n in ('eq', 'converse', 'comp')]
B4 += [('SameJointTests.' + n, 'SameTestsWith.' + n) for n in ('refl', 'symm', 'trans', 'functional', 'sameBranchingTests')]
B4 += [('BranchingTest.toJoint', 'BranchingTest.toWith'), ('BranchingTest.holds_toJoint', 'BranchingTest.holds_toWith')]
for o, k in B4:
    removed.append({'old': B + o, 'kept': B + k, 'item': 'B4',
                    'why': 'the joint frame is the case of one relation of the general theory in Likeness'})
renamed = [{'old': B + 'JointTest.' + c, 'new': B + 'TestWith.' + c, 'item': 'B4',
            'why': 'JointTest is TestWith Unit; its constructors are the general ones'}
           for c in ('top', 'claim', 'not', 'both', 'can', 'together')]
renamed += [{'old': B + w + '.Member.' + c, 'new': B + 'Witnesses.Member.' + c, 'item': 'B14',
             'why': w + '.Member is Witnesses.Member; its constructors are the library\'s'}
            for w in ('Exceeding', 'Race') for c in ('renewer', 'first', 'second')]
renamed += [{'old': B + 'DistinctBy.' + n, 'new': B + 'DistinctUnder.' + n, 'item': 'B6',
             'why': 'DistinctBy is DistinctUnder; its laws follow the kept name'} for n in ('decided', 'eq_of', 'distinct')]
PRELUDE = ['Distinct', 'total', 'steps', 'nonzero', 'Undecided.upto', 'DistinctUnder', 'Copying.nth', 'Settling.consAct',
           'Law.memberAt', 'not_mem_of_middle', 'distinct_append', 'distinct_map_on', 'total_steps_succ', 'total_steps_add',
           'between_of_mem_steps', 'RouteTraces.nonzero_of_le', 'downFrom', 'mem_downFrom', 'le_of_mem_downFrom',
           'Undecided.mem_upto']
moved = [{'name': B + n, 'to': 'Becoming.Prelude', 'item': 'B6'} for n in PRELUDE]
moved += [{'name': B + 'Flow.excess_zero_of_le', 'to': 'Becoming.Change', 'item': 'B6'},
          {'name': B + 'Situations.sum_one', 'to': 'Becoming.Weighted', 'item': 'B6'},
          {'name': B + 'Shuttle.next_off', 'to': 'Becoming.Roles', 'item': 'B6'}]
moved += [{'name': B + n, 'to': 'Becoming.Likeness', 'item': 'B4'} for n in ('MatchesParts', 'MatchesParts.transport', 'MatchesParts.comp')]
generalized = [
    {'name': B + 'Distinct', 'how': 'stated in every universe, as CrossSituational.Distinct was'},
    {'name': B + 'distinct_append', 'how': 'stated in every universe, as SituationTraces.distinct_append was'},
]
json.dump({'removed': removed, 'renamed': renamed, 'moved': moved, 'generalized': generalized},
          open(HERE / 'RENAME-TABLE.json', 'w'), indent=1, ensure_ascii=False)
print(len(removed), 'removed,', len(renamed), 'renamed,', len(moved), 'moved')
