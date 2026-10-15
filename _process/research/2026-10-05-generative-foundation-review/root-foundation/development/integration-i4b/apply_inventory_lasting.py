#!/usr/bin/env python3
"""I4b-4: classify the lifting laws of Becoming.Lasting in DECIDABILITY-INVENTORY.py (run from the repository root).

A scratch run of the inventory on the branch's core, with only the receipt check skipped, finds two new theorems
using decidedness only in their proofs:
* `Lasting.list_throughout_not_not` takes each member's depth as decided and removes a double negation with it
  (`Decided.of_not_not`), using both cases (`split`);
* `Lasting.TwoChains.branching` lists the successors of the two chains through `Chains.outcomes`, which builds the
  lists from the decided families (`build`).
`Lasting.step_iff_either` proves that, asked of every finitely branching process, an unbounded configuration having an
unbounded successor is exactly `EitherThroughout`: a boundary theorem, and the page's boundary sentence names it.
Each edit asserts the text it replaces."""
from pathlib import Path

P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py')
s = P.read_text()


def change(old, new, what):
    global s
    assert s.count(old) == 1, what
    s = s.replace(old, new)


change("    **{n: 'split' for n in ['Gated.origin_of_decides']},\n}",
       "    **{n: 'split' for n in ['Gated.origin_of_decides']},\n"
       "    # integration I4b (2026-10-16): lasting some course where the process branches finitely\n"
       "    **{n: 'split' for n in ['Lasting.list_throughout_not_not']},\n"
       "    **{n: 'build' for n in ['Lasting.TwoChains.branching']},\n}", 'end of PROOF_KIND')
change("            'refutable_passes_iff_markov']",
       "            'refutable_passes_iff_markov',\n"
       "            # integration I4b (2026-10-16): asked of every finitely branching process, an unbounded successor is\n"
       "            # EitherThroughout\n"
       "            'Lasting.step_iff_either']", 'boundary list')
change('在门上定位起源、或由前缀检验否证的形式需要可判定性。',
       '在门上定位起源、由前缀检验否证、或在有限分支处找到无界的后继的形式需要可判定性。', 'zh boundary sentence')
change("          'locating an origin at a gate or refuting by prefix tests need '",
       "          'locating an origin at a gate, refuting by prefix tests or finding an unbounded successor where branching '\n"
       "          'is finite need '", 'en boundary sentence')
P.write_text(s)
print('DECIDABILITY-INVENTORY.py: 2 proof-only rows, 1 boundary theorem, the boundary sentence')
