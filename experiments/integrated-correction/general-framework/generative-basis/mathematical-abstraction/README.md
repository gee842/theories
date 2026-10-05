# Finite checks for mathematical abstraction

6 October 2026. This owned package checks finite instances and boundary cases from [Mathematical structure, acquired abstraction and finite certificates](../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MATHEMATICS-STRUCTURAL-RESULTS.md). Its research connection is acquired prediction → reusable abstraction → warranted inference.

The result is a mathematical implementation check. No empirical learning study, physical acquisition mechanism, new Lean verification or mathematical-priority claim is made. The general propositions are hand proofs in the linked note; finite enumeration is not their proof.

## Reproduce

Run with Python 3.11 or later; only the standard library is used:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/check.py
```

The script can also be invoked by its absolute path from another directory. It writes only the colocated [verification.json](verification.json) after all checks pass. The recorded execution used Python 3.11.2. The receipt includes the SHA-256 of [check.py](check.py), exact case counts and every named assertion count.

## What was checked

All Boolean-output deterministic transition tables were enumerated for these finite carriers, retaining labels rather than sampling isomorphism classes:

| States | Actions | Transition/output combinations |
|---|---|---|
| 1 | 2 | 2 |
| 2 | 2 | 64 |
| 3 | 2 | 5,832 |
| 4 | 1 | 4,096 |
| Total | — | 9,994 |

For every model, partition refinement was compared with a separately implemented breadth-first shortest-witness search on the product graph. The checker also compares each refinement stage with explicit finite-word output profiles, checks the `n − k₀` refinement/word bound, verifies quotient output/update compatibility, and enumerates every equivalence partition to check that each output-preserving transition congruence refines the canonical behavioral partition. Here `k₀` counts distinct initial output classes; it is not a guessed count of hidden states.

For the 5,898 two-action models with at most three states, all 31 words of length at most four were used as the exact test profile. Each profile corresponded to one canonical reachable minimized behavior; 1,054 different initial behaviors occurred. This checks the `2N − 2` finite-testing result at `N = 3`. The exhaustive model class and exact outputs are supplied to this test; it does not learn whether the class contains a real target.

The checker additionally verifies:

- The unary chain family attaining the `n − 2` bound for 2–12 states.
- A constant-zero model and delayed-one model agreeing through every tested horizon 0–12 but disagreeing immediately afterward.
- Two two-state targets agreeing through one action and disagreeing after two.
- The failure of current-output equality as a recursive state representation.
- The increased discrimination required by an expanded question interface.
- Nontransitivity of a fixed numerical approximation threshold.
- Interpretation transport for all 21,612 terms of height at most three using two variables, a zero constant and binary addition, under all 36 assignments in `Z/6Z`, through the homomorphism to `Z/3Z`.
- A noncommutative interpretation of binary syntax, showing that composition alone does not impose commutativity.

The passed run executed 1,135,468 named assertions. This count describes this checker, not independent scientific findings. Most assertions belong to the finite term-transport family. No automatic equational proof checker, active-learning interface or calculus-completeness result is implemented.

## Remaining supplied inputs

The process is deterministic, stationary and completely tabulated. Action and output meanings, exact observations, any reset mechanism, state bounds, implementation costs and relevance of the chosen questions remain outside this checker. Actual learning would have to supply faithful observations and retain the costed history. Generalization without those inputs is explicitly blocked by the delayed-disagreement examples.
