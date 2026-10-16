"""The learner by refutation on the two-valued negation along a cycle of N places (odd N).

Prints, for odd N from 3 to 25, the rest step (last step wrong or silent, plus one) of the
learner by refutation over the lasso hypotheses in Cantor order on the course
o(t) = (t mod N) mod 2, the `Identification.oddCycle` of the Lean section, and checks it
against (N^3 - N)/4 + 1: the learner is refuted at step (N^3 - N)/4
(`Identification.learner_refuted_late`) and right from then on.
"""
from sim import rest

for N in range(3, 26, 2):
    T = N * N * N
    o = [(t % N) % 2 for t in range(T)]
    r = rest(o, T)
    print(N, r, (N ** 3 - N) // 4 + 1, r == (N ** 3 - N) // 4 + 1)
