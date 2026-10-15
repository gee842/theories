# Rest step of the learner by refutation: exhaustive search (P83g)

Evidence for [identification-where-bounded](../../../../../../theories/becoming/results/records/identification-where-bounded.md), sixteenth law and its second does-not-show item; study section 136 of [BECOMING-RENEWAL-READING.md](../../BECOMING-RENEWAL-READING.md). A computation, not a proof: the proved statements are the Lean theorems `Identification.learner_refuted_late` and `Identification.learner_rest_cubic` (lower bound) and `Identification.learner_rests` (upper bound).

The learner is `Learning.learner Learning.lassos`: it holds the lasso hypothesis at its index in Cantor order (`pairAt`, `(i, q)` at place `tri (i + q) + q`), claims the value `q + 1` steps back once `i + q + 1 ≤ t`, and moves to the next index exactly where the claim made is refuted. The rest step of a history is the last step at which the learner is wrong or silent, plus one.

- `sim.py`: the learner and the rest step (Python), and the search over every history with at most N states (every lasso `(i, q)`, `i + q + 1 ≤ N`, every assignment of its first `i + q + 1` values).
- `rest.c`: the same search in C; `./rest NMAX A` searches values `0 … A − 1` for N = 1 … NMAX.
- `worst_two_values.txt`: `./rest 17 2`, the worst rest step for N ≤ 17 with two values, with a history attaining it and the proved upper bound N + (2N − 1)·tri N.
- `worst_three_values.txt`: `./rest 9 3`, the same for three values, N ≤ 9; it agrees with two values.
- `odd_cycle.py`, `odd_cycle.txt`: the rest step on the negation along a cycle of N places, `(t mod N) mod 2`, for odd N ≤ 25; it is (N³ − N)/4 + 1, the step after the Lean theorem's refutation.

Found: for odd N ≥ 3 the worst rest step is (N³ − N)/4 + 3 (N ≤ 17), attained by the same negation started at another place; for even N from 12 to 16 it is one more than for N − 1; the small even cases 4, 6, 8, 10 give 16, 46, 91, 193. The exact constant for every N is not proved.
