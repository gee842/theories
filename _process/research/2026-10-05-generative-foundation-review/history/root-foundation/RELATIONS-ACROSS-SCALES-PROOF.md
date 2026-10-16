# Relations across scales: mathematical correspondence and dependency audit

8 October 2026, Asia/Bangkok. AI-authored. [Current bilingual theory](../../../../theories/becoming/chapters/RELATIONS-ACROSS-SCALES.md) · [Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/RelationsAcrossScales.lean) · [Checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_scales.py) · [Receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/scales-verification.json).

## Formal objects and supplied hypotheses

`X` is an arbitrary type representing the selected joint state; `Y` and `Z` have supplied pseudometrics. No distance or independent controller is required on `X`. `F`, `G`, `H` and time-dependent maps `p`, `q` are supplied descriptions/laws. Their origin and empirical adequacy are not encoded as conclusions. Pseudometric zero need not mean equality of distinct descriptions; no such inference is used.

For `finite_horizon_bound`, the actual and model recurrences, nonnegative propagation coefficients, one-step defect bounds and propagation inequalities need hold only for `t < N` and only on the indicated reached states/pairs. The initial bound is supplied. The conclusion holds for every `n ≤ N`. A future predictive interpretation requires evidence for these bounds on the relevant possible histories; the theorem cannot manufacture that evidence.

`budget` is a recursively computed upper envelope, not a definition of the actual discrepancy. Its recursion is evaluated independently from `dist (p n (x n)) (y n)`; the theorem proves the inequality. `ε` need not have a separately stated nonnegativity premise because a realized nonnegative distance bounded by it already supplies that fact. The cap result is a recurrence lemma; its real-world application uses the earlier correspondence theorem.

## New declarations and their content

All names are in namespace `RelationsAcrossScales`.

| Declaration | Scope and mathematical claim |
|---|---|
| `history_is_core_trace` | A history satisfying its supplied deterministic recurrence has each finite prefix represented by an actual `Generative.Trace` on the time-augmented state. No material funding is inferred. |
| `one_step` | Triangle inequality combines actual next-description defect with propagated current error. |
| `finite_horizon_bound` | Induction derives the independent recursive envelope from reached-pair bounds through N. |
| `budget_cap` | The allowance `ε t + L t * B ≤ B`, nonnegative L and initial cap imply every prefix budget is at most B. |
| `composed_defect` | Two successive projections give composed defect `K * ε + η`, with nonnegative K and a supplied sensitivity bound for the next second projection. |
| `observable_error` | Independent readout calibration plus representation error gives `a + K * E`. |
| `protected_conditions` | For arbitrary index type, a margin above each separately supplied threshold transfers to the actual conditions. It does not establish which thresholds are justified. |
| `violation_certificate` | An upper error margin strictly below a threshold certifies actual violation. |
| `fibre_error_lower_bound` | Equal-summary states and ε-accurate common readout imply actual values differ by at most `2 * ε`. No metric on the summary type is needed. |
| `routing_total` | The explicit coupled law changes total by `c * b`. |
| `routing_defect_lower_bound` | One prediction of the two equal-total states with uniform error ε requires `c ≤ ε`. This directional bound is informative for c positive; no necessity of a signed negative error is inferred for c negative. |
| `routing_error_bound` | A bound on `abs b` gives a concrete identity-predictor residual of `abs c * B`. |
| `enriched_routing_exact` | Total and the consequential second coordinate together have an exact update. They retain the original pair’s information. |
| `total_exact_through_transfer` | Joint transfer preserves total for every real pair. |
| `exact_total_can_hide_loss` | The same transfer takes a jointly supported pair to a pair violating one supplied basic threshold. |
| `no_total_only_protection` | No predicate of total alone characterizes that conjunction over every pair. |
| `minimum_preserves_protection` | A minimum summary does characterize this particular conjunction, not every differentiated claim. |
| `frozen_charts_miss_change` | Frozen identity-law commutation does not account for the arbitrary offset introduced on changing the description. |
| `linear_drift` | Positive or zero constant drift gives exact one-step and n-step errors. |
| `positive_drift_unbounded` | For positive drift and every real bound, some natural-number stage exceeds it. |
| `threshold_ambiguity` | A positive error interval around the threshold contains both a violation and a satisfaction. |

## Dependency and correspondence audit

The checker rebuilds `GenerativeCore`, `SystemsOrganization` and the new module in a fresh temporary directory using Lean 4.30.0-rc2. The inherited modules contribute 42 replayed audits; their theorems are not counted as new. It uses the pinned Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa` and existing upstream artifacts, without installing or rebuilding upstream dependencies.

Every new theorem has an explicit `#print axioms` request. The checker requires exact ordered names, no warnings/errors, no proof placeholders or native proof shortcuts, no new custom axiom declarations, and only standard logical dependencies. It freezes inputs and logs, hashes the compiler, manifest, toolchain, checker and direct imported artifacts, and checks inputs remained unchanged during the run. An empty axiom list does not remove theorem hypotheses, supplied structures or application obligations.

中文范围：本轮证明的是给定关系、误差界及指标对应下的推论，不是把“描述充分”直接放入定义再宣布结论。实际组织、映射、误差证据和基本阈值的正当性分别列为输入。总量反例保持同一真实转移和被保护条件，指出粗描述丢失了关系，而不把遗漏冒充整个生成理论的失败。

## Reproduction

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_scales.py
```

`SYSTEMS_MATHLIB_PROJECT` and `SYSTEMS_REAL_LEAN` may select already installed matching dependencies. A successful recorded build, rather than this command’s existence, establishes the validation reported in the main account.
