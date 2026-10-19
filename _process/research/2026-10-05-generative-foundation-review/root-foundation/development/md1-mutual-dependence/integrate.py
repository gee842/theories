#!/usr/bin/env python3
"""Join MD1's module to the core package: copy it in, import it after Becoming.Frequency, add its root doc
bullet after Frequency's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (MD_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['MD_ROOT']).resolve() if os.environ.get('MD_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


if (HERE / 'Becoming/MutualDependence.lean').resolve() != (PKG / 'Becoming/MutualDependence.lean').resolve():
    shutil.copyfile(HERE / 'Becoming/MutualDependence.lean', PKG / 'Becoming/MutualDependence.lean')

DOC = (
    '* `Becoming.MutualDependence` (L4): formations whose continuations depend on one another, and the\n'
    '  pace it gives, with no premise beyond the hypotheses each statement names. Three readings, each\n'
    '  strictly stronger: every system the whole (sharing conditions throughout), every influence closure\n'
    '  the whole (mutual dependence, equivalently every reach closure), every feeding closure the whole\n'
    '  (mutual feeding); `Clearing` shares without mutual dependence and `Drawing`, a balanced pair each\n'
    '  taking from what the other requires, is mutually dependent and not fed. Under each, significance\n'
    '  bounded by the matching closure is the continuation condition, for any web of mutual feeding and\n'
    '  not only one common condition. Around a loop of couplings holding at every step, what reached its\n'
    '  condition at least doubles each turn, at the loop and downstream, while the carried amount stays\n'
    '  within `D * (1 + M) ^ t`: exponential both ways. A selection with transmission, carriers leaving\n'
    '  at least `a` and others at most `b`, raises the share ratio at least as `(a / b) ^ n`; under\n'
    '  balance a draw exceeding everything drawn before leaves more than half the stock at every step it\n'
    '  is met, and lasting `n` steps needs `2 ^ n - 1`.\n')
SCOPE = (
    '    "MutualDependence: sharing conditions throughout, mutual dependence (every influence closure, "\n'
    '    "equivalently every reach closure, the whole) and mutual feeding are each strictly stronger "\n'
    '    "(Clearing, Drawing), and under each, significance bounded by the matching closure is the "\n'
    '    "continuation condition; around a loop of couplings holding at every step what reached its "\n'
    '    "condition at least doubles each turn, there and downstream, and the carried amount stays within "\n'
    '    "D (1 + M)^t; transmission with carriers leaving at least a and others at most b raises the share "\n'
    '    "ratio at least as (a/b)^n; under balance a draw exceeding all earlier draws leaves more than half "\n'
    '    "the stock at every step it is met and needs 2^n - 1 for n steps (DoublingDraw attains it). "\n')
README_ROW = (
    '| L4 | [`Becoming.MutualDependence`](Becoming/MutualDependence.lean) | formations whose continuations depend '
    'on one another, and the pace it gives (no premise beyond the hypotheses named): three nested readings '
    '(`Flow.SharesThroughout`, `Flow.MutuallyDependent`, `Flow.MutuallyFed`; `Flow.mutuallyDependent_iff_reach`; '
    'strict by `Clearing.shares_not_mutual` and `Drawing.mutual_not_fed`), each making its bounded significance '
    'the continuation condition (`Flow.SharesThroughout.unrestricted`, `Flow.MutuallyDependent.unrestricted`, '
    '`Flow.MutuallyFed.unrestricted`); exponential both ways around a loop of couplings at every step '
    '(`carried_pow_around`, `carried_pow_downstream`, `carried_le_pow_always`, `exponential_around`, '
    '`CoupledThroughout.exponential`); the pace of a selection (`share_ratio_pow`); a draw exceeding all earlier '
    'draws (`Flow.Balances.half_stands`, `Flow.Balances.doubling_needs`, `DoublingDraw.half_then_none`) |')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Frequency\n', 'import Becoming.Frequency\nimport Becoming.MutualDependence\n')
root = once(root, '* `Becoming.Gain` (L3): where novelty\'s gain comes from, with no premise.',
            DOC + '* `Becoming.Gain` (L3): where novelty\'s gain comes from, with no premise.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Frequency", ', '"Becoming.Frequency", "Becoming.MutualDependence", ')
chk = once(chk, '    "Frequency: counting the steps at which anything couples, the carried amount is at most D "\n',
           SCOPE + '    "Frequency: counting the steps at which anything couples, the carried amount is at most D "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Frequency`](Becoming/Frequency.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
