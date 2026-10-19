#!/usr/bin/env python3
"""MD1: the opening's note [^present] reads "highly entangled" as mutual dependence and cites the pace laws of
Becoming.MutualDependence. Body unchanged. Every edit must match exactly once.
usage (from the checkout root): python3 -B apply_opening.py"""
from pathlib import Path

P = Path('theories/becoming/OPENING.md')
s = P.read_text(encoding='utf-8')
R = 'results/records/mutual-dependence-and-its-pace.md'
EDITS = [
    ('*Entanglement and pace.* The theory defines no entanglement; the chapter reads "heavily coupled" as coupling '
     'strength and "highly entangled" as couplings that lie on loops, a condition being on a loop where a chain of '
     'couplings, each a formation exchanging with one condition with positive strength on another\'s level, leads from '
     'it back to it (`OnLoop`). The laws below relate that reading to pace; they do not identify the two.',
     '*Entanglement.* The chapter reads "heavily coupled" as coupling strength and "highly entangled" as mutual '
     'dependence: every formation\'s continuation can be affected, at some remove, by every other '
     f'(`Flow.MutuallyDependent`; [record]({R})). Sharing conditions throughout is the weaker reading and mutual feeding '
     'the stronger, each strictly (`Clearing.shares_not_mutual`, `Drawing.mutual_not_fed`). Mutual dependence is not '
     'mutual benefit: a pair in which each takes from what the other requires is mutually dependent. Under mutual '
     'dependence whatever a formation affects can affect it back, so every link of affecting lies on a loop through '
     'the whole (`Flow.mutuallyDependent_iff_reach`), and significance bounded by what can affect each center is the '
     'continuation condition (`Flow.MutuallyDependent.unrestricted`). *Pace.* Pace is a law of the couplings that carry '
     'such loops.'),
    ('Around a loop each return at least doubles what had reached it, so returns at bounded intervals grow it '
     'exponentially, and returns often enough outgrow every polynomial (`carried_returns`, `runaway_of_returns`);',
     'Around a loop of couplings that hold at every step, each turn at least doubles what had reached the loop\'s '
     'condition, there and downstream, while the ceiling above still holds, so the growth is exponential in both '
     'directions (`carried_pow_around`, `carried_pow_downstream`, `exponential_around`); returns often enough outgrow '
     'every polynomial (`runaway_of_returns`);'),
    ('the target\'s share among the offspring rises, transmission granted (`share_rises`);',
     'the target\'s share among the offspring rises, transmission granted (`share_rises`), and over n generations, '
     'with carriers leaving at least a offspring and others at most b, the carriers\' ratio to the others grows at '
     'least as (a/b)^n (`share_ratio_pow`);'),
    ('*Little time.* Where a formation',
     '*Little time.* Under balance, with nothing given, a draw that exceeds everything drawn before it, as a doubling '
     'one does, leaves more than half the starting stock standing at every step at which it is met, and lasting n steps '
     'needs a stock of at least 2^n − 1 (`Flow.Balances.half_stands`, `Flow.Balances.doubling_needs`). What stands '
     'gives no warning, and doubling the stock buys one more step. Where a formation'),
    ('*What stays judgment:* whether the Earth\'s couplings form such loops and how often differences return around '
     'them,',
     '*What stays judgment:* whether the Earth is mutually dependent, whether its dependences act as couplings at every '
     'step and how often differences return around them, how fast today\'s draws grow,'),
]
for old, new in EDITS:
    assert s.count(old) == 1, ('edit does not match once', old[:80], s.count(old))
    s = s.replace(old, new)
P.write_text(s, encoding='utf-8')
print('opening note applied')
