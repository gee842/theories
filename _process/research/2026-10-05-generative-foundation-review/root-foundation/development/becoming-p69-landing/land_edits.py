#!/usr/bin/env python3
"""Landing edits for P69 in a checkout W: copy Becoming.Unfolding, append the bridge section to
Becoming.Bridge (with `import ExplanatoryBranching` and a docstring bullet), and edit the root module,
the checker's CORE and scope, and the Lean README. Usage: python3 -B land_edits.py W"""
import re
import shutil
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
PKG = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/becoming-p69-landing'
B = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
sys.path.insert(0, str(PKG / 'docs'))
import chapter  # noqa: E402

shutil.copyfile(PKG / 'lean/Becoming/Unfolding.lean', B / 'Becoming/Unfolding.lean')


def edit(path, pairs):
    s = path.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path.name, a[:80], s.count(a))
        s = s.replace(a, b)
    path.write_text(s)
    print('edited', path.relative_to(W))


# The bridge section, its import and its docstring bullet.
bridge = B / 'Becoming/Bridge.lean'
section = (PKG / 'lean/bridge_section.lean').read_text().rstrip('\n') + '\n\n'
s = bridge.read_text()
assert s.rstrip().endswith('end Becoming') and 'deeper_bisimulation_iff' not in s
cut = s.rstrip().rindex('end Becoming')
s = s[:cut] + section + s[cut:]
bridge.write_text(s)
BRIDGE_BULLET = """* `Deeper.Bisimulation` of `RelationalDynamics` and `ExplanatoryBranching.Bisimulation` are
  the core's `Bisimulation` (`Becoming.Unfolding`) on frames with no claims and with a model's
  conditions as claims (`deeper_bisimulation_iff`, `branching_bisimulation_iff`); in `static`
  and `toggle` every configuration of one is alike to every configuration of the other
  (`static_toggle_alike`); alike configurations pass every branching test (`Alike.same`).
"""
edit(bridge, [
    ('import CorrectionInfrastructure\n', 'import CorrectionInfrastructure\nimport ExplanatoryBranching\n'),
    ('\nDirection conventions differ and are kept', BRIDGE_BULLET + '\nDirection conventions differ and are kept'),
])

BULLET = """* `Becoming.Unfolding` (L3): one unfolding and its readings (P69). The labelled process and the
  frame are readings of a world: read within the configuration the move changes no run and is
  what the law leaves open, and a world's move is its relata's exchange, balance being running by
  the law of exchange; every history is a run of the law it shows, the least one, determined
  exactly where the history is consistent, the correspondence failing to be an identity through
  dead ends and splices and closing where the history is kept; a claim is a relatum and novelty
  is arising; configurations are alike where a bisimulation relates them, pass the same tests,
  and are named sensibly exactly where alike ones are one; determinacy as equality depends on
  names. Ren confirmed the reading of law and history; the other readings are the AI's.
"""
root = B / 'Becoming.lean'
edit(root, [
    ('import Becoming.Mechanism\n', 'import Becoming.Mechanism\nimport Becoming.Unfolding\n'),
    ('* `Becoming.Attraction` (L3):', BULLET + '* `Becoming.Attraction` (L3):'),
])

SCOPE = (
    '    "Unfolding: read with the move inside the configuration a process has the same runs, the law "\n'
    '    "leaving the next move open and determined exactly where it is with moves as labels and one move "\n'
    '    "wherever it steps; with the move formed within by a policy, runs from one configuration agree; "\n'
    '    "a shared move couples the parts of a synchronized product; a world balances exactly where its "\n'
    '    "standings run by the law of exchange with its relata\'s exchanges as moves, the exchange fixing "\n'
    '    "the standings from a beginning and the standings not fixing the exchange; every history is a "\n'
    '    "run of the law it shows, the least law it is a run of, determined exactly where the history is "\n'
    '    "consistent, a law can have a step and no run, a revisiting history shows a law admitting a run "\n'
    '    "it never took, and a kept history shows a law admitting only it; a frame along a run is a world "\n'
    '    "whose relata are its claims, novelty being arising; configurations are alike where a "\n'
    '    "bisimulation relates them, an equivalence with no quotient, and alike ones pass the same tests; "\n'
    '    "determinacy up to likeness passes along likeness while determinacy as equality depends on names; "\n'
    '    "a description makes sense where it identifies exactly the alike configurations, and then carries "\n'
    '    "a law where the frame is determined up to likeness; under a determined law likeness is the same "\n'
    '    "registered future; under the law of exchange standings are alike exactly where they agree "\n'
    '    "pointwise. "\n')
edit(B / 'check_becoming.py', [
    ('"Becoming.Mechanism",', '"Becoming.Mechanism", "Becoming.Unfolding",'),
    ('    "Attraction: for every determined law,', SCOPE + '    "Attraction: for every determined law,'),
])

# The Lean README: a row after Mechanism's, and the import sentences.
zh = chapter.SPINE_L3.split(' | ')[2]
EN = ("one unfolding and its readings (no premise, P69): read within the configuration the move changes no run and "
      "is what the law leaves open, formed within by a policy it makes runs from one configuration agree, and a shared "
      "move couples parts; a world's move is its relata's exchange, balance is running by the law of exchange, the "
      "exchange fixes the standings from a beginning and not conversely; every history is a run of the law it shows, "
      "the least one, determined exactly where the history is consistent; dead ends and splices, the correspondence "
      "closing where the history is kept; a claim is a relatum and novelty is arising; likeness by bisimulation is an "
      "equivalence, alike configurations pass the same tests, a description makes sense exactly where it identifies the "
      "alike ones and then carries a law, determinacy as equality depends on names and determinacy up to likeness "
      "passes along likeness; standings are alike exactly where they agree pointwise")
names = ['withMove_determined_iff', 'closedBy_runs_agree', 'World.balances_iff_exchange', 'exists_law_iff',
         'Splice.spliced', 'DeadEnd.no_history', 'Frame.novel_iff_arises', 'Alike.tests', 'MakesSense.carries',
         'Twins.alike_one', 'exchange_alike_iff']
text = (B / 'Becoming/Unfolding.lean').read_text()
for n in names:
    last = n.split('.')[-1]
    assert re.search(rf'^(theorem|def)\s+\S*{re.escape(last)}\b', text, re.M), n
row = f'| L3 | [`Becoming.Unfolding`](Becoming/Unfolding.lean) | {zh} / {EN} |\n'
readme = B / 'README.md'
s = readme.read_text()
i = s.index('| [`Becoming.Mechanism`](Becoming/Mechanism.lean) |')
i = s.rindex('\n', 0, i) + 1
j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
readme.write_text(s)
edit(readme, [
    ('`Mechanism` 导入 `Experiment`；', '`Mechanism` 导入 `Experiment`；`Unfolding` 导入 `Mechanism` 与 `Space`；'),
    ('`Mechanism` imports `Experiment`;', '`Mechanism` imports `Experiment`; `Unfolding` imports `Mechanism` and `Space`;'),
])
