# Chance grounding: the positive-chance optimization diagnostic

8 October 2026. AI-authored formal audit for the current initial-chance inquiry. **Four new Lean theorems / ten declaration audits** test one proposed implementation. They do not prove the ethical candidate CP, derive a fair chance floor, or establish that uncertainty itself warrants a lottery.

The [symmetric risk-sharing result](JOINT-RISK-REVISION-INTEGRATION.md#9-continue-through-equal-basic-risk-sharing), [coupled protection result](CROSSED-CLAIMS-PROOF.md) and [settlement-history result](CHANCE-REVISION-INTEGRATION.md) are already completed at their own scopes. This module does not repeat their risk calculations, supplied-floor preservation, or historical-fidelity controls. It imports only `Std`; no earlier project theorem is rebuilt or counted.

## What is being tested

One stipulated joint opportunity has two exclusive routes. A protects two distinct positions; B protects a different position. For the intended application, B's threatened loss is graver than either loss on A's side, and no independently justified BC1/LR priority has already excluded its request. This is a still-crossed case. **It is not an equal-stakes BC1 case in which a positive chance for the smaller side is being smuggled in.** All remaining requests are assumed to fall within the candidate positive-chance requirement's scope.

The diagnostic implementation imposes positive protection probability for each remaining request and then maximizes expected protected headcount. The latter objective is an additional, deliberately tested proposal: neither G0 nor CP has supplied it. Severity, legitimate priority, permission and chance adequacy are not converted into headcount by the mathematics.

Natural ticket counts `(a,b)` have `a>0` and `b>0`, with total `N=a+b`. Each protected position on A's side has chance `a/N`; the B-side position has chance `b/N`. The candidate score is

\[
S(a,b)=\frac{2a+b}{a+b}.
\]

The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ChanceGrounding.lean) represents the numerator and positive denominator separately, comparing scores by exact cross multiplication. The ticket law is supplied, not inferred from observed selector frequencies. Actual reliable randomization, timing, costs and authority remain application conditions.

## Four checked results

| Theorem | Exact scope |
|---|---|
| `positive_refinement_improves_score` | For every positive ticket pair, replacement by `(2a+b,b)` preserves positive chances, doubles the total, leaves B's numerator unchanged and strictly increases the candidate score |
| `no_maximum_in_unbounded_positive_ticket_domain` | In the domain admitting every positive natural ticket pair, every candidate has such a strictly better alternative; hence no maximum exists |
| `every_positive_score_is_below_two` | Every positive ticket pair's score numerator is strictly less than twice its total |
| `fixed_resolution_unique_maximum` | For fixed `N≥2`, the pair `(N−1,1)` is positive, has total `N`, and uniquely maximizes the numerator among all positive pairs of that total |

The first result preserves B's numerator while doubling the denominator, so B's positive chance is halved. The retained application example checks `(1,1) → (3,1)` and its strict score improvement. The general result does not rely on this example or assume an initially fair half chance.

The no-maximum theorem concerns the specified **unbounded positive natural-ticket domain**. If the actual implementation has a finite resolution, lacks time for refinement, or changes its reliability or burdens when refining, that domain does not describe its feasible opportunities. The fixed-resolution theorem addresses a separate bounded domain. Both domains are supplied; the model does not require infinite physical precision.

At fixed resolution the B-side position receives exactly one ticket, hence probability `1/N`. This fraction follows from the tested objective and resolution constraint. It does not establish that this chance is ethically adequate. The proof supplies neither a numerical minimum justified by CP nor a unique fair lottery. We also make no formal claim here to have proved a real-number supremum theorem; the checked results are the strict upper bound, the explicit improvement and absence of a maximum in the stated domain.

## What the diagnostic rules out

The result exposes a specific attempted shortcut: treat any positive chance as a complete fairness certificate, then let an otherwise unexamined count-maximization objective determine its size. In the unbounded domain that optimization has no answer; in the fixed-resolution domain the minority's minimum chance is set by the representation's smallest ticket. Neither outcome explains why that amount responds adequately to the actual request.

This does not prove CP inconsistent or show that every positive-chance principle needs a universal fixed lower bound. CP need not adopt the tested score or claim to settle all proportions. Its substantive defense, the scope of justified exclusions, and the adequacy of a concrete allocation remain ethical work. An epistemic inability to rank the alternatives is also distinct from a positive reason to share opportunity.

The modeled requests are differentiated within one provision history. Their overlapping conditions, actual losses and authority relations cannot be recovered merely from the ticket pair. The two-to-one count is not an ethical exchange rate between their lives, and a realized loss is not compensated merely because its bearer received a positive chance.

## Actual checking and frozen receipt

The [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_chance_grounding.py) ran **Lean 4.29.1** on frozen source bytes, retained all four theorem signatures, and requested an axiom-dependency audit for every explicit declaration. The [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/chance-grounding-verification.json) identifies [run `20261008T105731.467185Z`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/chance-grounding-checks/20261008T105731.467185Z/verification.json).

The count is **4 new theorems / 10 new declaration audits**, with **11 retained artifacts**. The concrete `Controls.lean` example is recorded separately and adds no theorem count. Six declarations have empty axiom dependencies, one uses `propext` and `Quot.sound`, and three use those with `Classical.choice`. No project-specific axiom, `sorry`, unsafe code or native-decision escape is admitted. No inherited project theorem is compiled in this package.

- Source SHA-256: `efb287aa7665d04dcccea7d28220030e98ca912d95096061eaceae121f2c451f`.
- Dedicated checker SHA-256: `dea8c50b684f52f885f1ea2bb4103e158194cd5eb86b2a5ffca1fa792cf49cc7`.
- Shared checker helper SHA-256: `b9f56e1700c03f0019a486d0f3c097f70c2ce20414da9e7b231131b8ed4a8308`.

The source, checker and receipt are frozen. Earlier formal files and shared READMEs were not changed. This is an exact implementation diagnostic under disclosed premises, not an ethical grounding theorem or empirical validation.
