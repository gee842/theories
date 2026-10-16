#!/usr/bin/env python3
"""I4b-1: classify the gate laws' decidedness in DECIDABILITY-INVENTORY.py (run from the repository root).

`Gated.origin_of_decides` takes, for each move, whether its gate holds, and its proof uses both cases (`split`).
`Gated.origin_of_propositions_iff` proves that, asked of every process, the origin law with the gate a proposition is
exactly double-negation elimination: a boundary theorem. Each edit asserts the text it replaces."""
from pathlib import Path

P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py')
s = P.read_text()
old = "        'most_difference_arrives', 'levels_alike_of_not_conveyed']},\n}"
assert s.count(old) == 1, 'end of PROOF_KIND changed'
s = s.replace(old, "        'most_difference_arrives', 'levels_alike_of_not_conveyed']},\n"
                   "    # integration I4b (2026-10-16): the origin law where each gate is decided\n"
                   "    **{n: 'split' for n in ['Gated.origin_of_decides']},\n}")
old = "            'exists_undominated_iff_weakly', 'undominated_has_iff_em']"
assert s.count(old) == 1, 'boundary list changed'
s = s.replace(old, "            'exists_undominated_iff_weakly', 'undominated_has_iff_em',\n"
                   "            # integration I4b (2026-10-16): with the gate a proposition, the origin law is double-negation\n"
                   "            # elimination\n"
                   "            'Gated.origin_of_propositions_iff']")
P.write_text(s)
print('DECIDABILITY-INVENTORY.py: 1 split row, 1 boundary theorem')
