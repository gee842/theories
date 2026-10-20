#!/usr/bin/env python3
"""R37 B6, stage 2 (after stage 1 built): the copy groups the merged definitions exposed.

usage: python3 -B b6_move2.py           (moves; writes b6-removals-2.json for remove.py)

samestatements.py (R32's) on stage 1's run finds the statements now the same: on `Undecided.upto`
(`FinerTraces.mem_upto`), `Distinct [()]` and `Distinct [true, false]` (SituationTraces), `skip_le`
(Likeness, now on `skipAt`), and `Propagation.between_of_mem_steps`, which stage 1 left out. And
`Learning.upto` is `downFrom` of Entropy, with the same body. Moves `Undecided.mem_upto`, `downFrom`
and `mem_downFrom` into the prelude under their names; the removals point at the kept names."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.argv.append('--no-run')
import importlib.util
spec = importlib.util.spec_from_file_location('m1', HERE / 'b6_move.py')
src = (HERE / 'b6_move.py').read_text().split('\ncut(PRELUDE_MOVED')[0]
ns = {'__file__': str(HERE / 'b6_move.py'), '__name__': 'b6m'}
exec(compile(src, 'b6_move', 'exec'), ns)
cut, before_end, B = ns['cut'], ns['before_end'], ns['B']

BLOCK = '''
/-- The numbers from `K` down to zero. -/
def downFrom : Nat → List Nat
  | 0 => [0]
  | K + 1 => (K + 1) :: downFrom K

theorem mem_downFrom : ∀ {k K : Nat}, k ≤ K → k ∈ downFrom K
  | _, 0, le => Eq.subst (motive := fun k => k ∈ downFrom 0) (Nat.eq_zero_of_le_zero le).symm
      (.head _)
  | _, K + 1, le => match Nat.eq_or_lt_of_le le with
    | .inl same => Eq.subst (motive := fun x => x ∈ downFrom (K + 1)) same.symm (.head _)
    | .inr lt => .tail _ (mem_downFrom (Nat.le_of_lt_succ lt))

namespace Undecided

theorem mem_upto : ∀ {n i : Nat}, i < n → i ∈ upto n
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | n + 1, i, lt => match Nat.lt_or_ge i n with
    | .inl lt' => .tail n (mem_upto lt')
    | .inr ge => Eq.subst (motive := fun x => x ∈ n :: upto n)
        (Nat.le_antisymm (Nat.le_of_lt_succ lt) ge).symm (List.Mem.head (upto n))

end Undecided
'''

REMOVALS = [
    ('Becoming.Propagation.between_of_mem_steps', 'Becoming.between_of_mem_steps'),
    ('Becoming.skip_le', 'Becoming.skipAt_le'),
    ('Becoming.SituationTraces.distinct_unit', 'Becoming.Asymptote.distinct'),
    ('Becoming.SituationTraces.distinct_two', 'Becoming.Shuttle.distinct'),
    ('Becoming.FinerTraces.mem_upto', 'Becoming.Undecided.mem_upto'),
    ('Becoming.Learning.upto', 'Becoming.downFrom'),
    ('Becoming.Learning.mem_upto', 'Becoming.mem_downFrom'),
]

cut(['Becoming.downFrom', 'Becoming.mem_downFrom', 'Becoming.Undecided.mem_upto'])
before_end(B / 'Prelude.lean', BLOCK)
json.dump({'rows': [{'old': o, 'new': n, 'why': 'R37 B6: the same definition or statement, one name'} for o, n in REMOVALS]},
          open(HERE / 'b6-removals-2.json', 'w'), indent=1, ensure_ascii=False)
print(len(REMOVALS), 'removal rows')
