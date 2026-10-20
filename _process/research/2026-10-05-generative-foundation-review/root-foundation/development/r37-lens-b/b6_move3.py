#!/usr/bin/env python3
"""R37 B6, stage 3 (after stage 2 built): `Law.le_of_mem_upto` (Identification) is now
`le_of_mem_downFrom` (Entropy) in the same words; the kept name moves into the prelude beside
`downFrom`, and the copy points there. Writes b6-removals-3.json."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / 'b6_move.py').read_text().split('\ncut(PRELUDE_MOVED')[0]
ns = {'__file__': str(HERE / 'b6_move.py'), '__name__': 'b6m'}
exec(compile(src, 'b6_move', 'exec'), ns)
cut, B = ns['cut'], ns['B']

BLOCK = '''
theorem le_of_mem_downFrom : ∀ {K k : Nat}, k ∈ downFrom K → k ≤ K
  | 0, _, .head _ => Nat.le_refl 0
  | 0, _, .tail _ no => nomatch no
  | _ + 1, _, .head _ => Nat.le_refl _
  | _ + 1, _, .tail _ mem => Nat.le_succ_of_le (le_of_mem_downFrom mem)
'''
cut(['Becoming.le_of_mem_downFrom'])
p = B / 'Prelude.lean'
s = p.read_text()
anchor = '\nnamespace Undecided\n\ntheorem mem_upto'
assert s.count(anchor) == 1
p.write_text(s.replace(anchor, BLOCK + anchor))
json.dump({'rows': [{'old': 'Becoming.Law.le_of_mem_upto', 'new': 'Becoming.le_of_mem_downFrom',
                     'why': 'R37 B6: the same statement, one name'}]},
          open(HERE / 'b6-removals-3.json', 'w'), indent=1, ensure_ascii=False)
