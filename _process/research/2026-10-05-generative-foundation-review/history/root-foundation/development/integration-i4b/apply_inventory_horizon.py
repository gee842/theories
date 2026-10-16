#!/usr/bin/env python3
"""I4b-3: add Horizon's boundary theorem to DECIDABILITY-INVENTORY.py (run from the repository root).

`refutable_passes_iff_markov` proves that, asked of every process, a reading made of prefix tests is refutable exactly
given Markov's principle (a Boolean sequence not all false has a true term): a boundary theorem. The page's sentence on
what the boundary theorems show gains the gate origin of item 1 and refutation by prefix tests. A scratch run of the
inventory on the branch's core, with only the receipt check skipped, finds no new theorem using decidedness only in
its proof. The edit asserts the text it replaces."""
from pathlib import Path

P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py')
s = P.read_text()
old = "            'Gated.origin_of_propositions_iff']"
assert s.count(old) == 1, 'boundary list changed'
s = s.replace(old, "            'Gated.origin_of_propositions_iff',\n"
                   "            # integration I4b (2026-10-16): asked of every process, refutability of a reading made of prefix\n"
                   "            # tests is Markov's principle\n"
                   "            'refutable_passes_iff_markov']")
# The page's sentence on what the boundary theorems show gains the gate origin (I4b-1) and prefix refutation.
old = '把配方读作一个检验、或找出不被胜过的选项的形式需要可判定性。'
assert s.count(old) == 1, 'zh boundary sentence changed'
s = s.replace(old, '把配方读作一个检验、找出不被胜过的选项、在门上定位起源、或由前缀检验否证的形式需要可判定性。')
old = "'recurrence of every world, fixing likeness by tests, reading a recipe as one test or finding an undominated choice need '"
assert s.count(old) == 1, 'en boundary sentence changed'
s = s.replace(old, "'recurrence of every world, fixing likeness by tests, reading a recipe as one test, finding an undominated choice, '\n"
                   "          'locating an origin at a gate or refuting by prefix tests need '")
P.write_text(s)
print('DECIDABILITY-INVENTORY.py: 1 boundary theorem, the boundary sentence')
