# V7.1 focused mathematical release check

Reviewed 4 October 2026 against the V7.1 source files. I formed the substantive mathematical assessment before reading `../v7/reviews/readiness/math/REVIEW.md`, then used that review to check closure. No manuscript files were edited. This is a bounded review of the corrected claims and their new verification witnesses, not certification of every proof, strategic extension, empirical premise, or proposed institution.

## Verdict

**Ready for conditional public working-paper release within this review's scope.** The former R1 blocker is repaired, and the concentration and scope findings are closed at the mathematical level. The separation of functional protection from cognitive understanding is also explicit and supported by a valid counterexample to the stronger necessity claim. No actionable mathematical release issue remains in the claims checked here. A nonblocking P3 precision correction found during this pass was applied by the drafting agent and verified before this report was finalized.

This verdict does not require completion of the empirical research programme. It relies on the paper retaining its conditional status and the stated limits on local continuation calculations, global concentration, strategic extensions, and empirical applicability.

## Remaining issues, ranked by severity

None in the bounded scope of this review.

### Resolved during review: P3 — Total rather than individual race share

**Anchor:** `src/supp/03_S3.md:19`. The load proof initially said that unbounded cumulative advantage sends an individual race carrier's share to one. Several carriers can have the maximal load and identical background payoff, in which case their mutual share ratios stay constant. For example, under unit-speed replicator dynamics with positive constant gap, initial shares `(0.2, 0.3, 0.5)` and loads `(1, 1, 0)` converge to `(0.4, 0.6, 0)`. The drafting agent changed the phrase to “the combined share of maximal-load carriers,” which I verified in the source. This now agrees with the load conclusion and the repaired R1 proofs at `src/supp/09_S9.md:7` and `src/supp/10_S10.md:37`.

## What withstood checking

### R1 and the retained positive-gap theorem

The selection definition now states exactly what the cumulative lower bound controls: positive-gap intervals, not arbitrary signed integrals (`src/core/30_s3.md:23`). The original load proposition keeps the pointwise premise `tau_eff(t) < nu` (`src/core/30_s3.md:34–36`). For finitely many fixed load types, each lower-load/race share ratio therefore vanishes when `B(t)` diverges, and the host comparison gives the stated eventual floor crossing under (reach). The proof is sound after the tied-carrier wording correction above.

R1 now explicitly assumes constant-speed replicator dynamics (`src/core/90_s9.md:13`). Its exact identity, including negative gaps, is derived at `src/supp/09_S9.md:7` and `src/supp/10_S10.md:37`; the same restriction appears in the safeguards theorem at `src/core/a0_s10.md:46–51`. Thus `B(t) -> +infinity` implies total race share tends to one and violates viability under (reach). Conversely, failure of `B(t) -> +infinity` supplies a sequence along which the average liability approaches at least `nu`, establishing the stated necessary limsup condition. Neither form is presented as sufficient.

The excluded-class witness is valid (`src/supp/09_S9.md:29–33`; `verification/readiness_checks.py:49–91`). The response `g + g^3` is relative, payoff-monotone and cumulative in either carrier order. Its liability cycle adds `1/5` to `B` but subtracts `2` from the race logit. The all-time host bound is approximately `0.9882525653`, well above the floor `0.3`. Constant-speed replicator response on the same schedule instead produces a positive logit increment `0.2s` per cycle. The new restriction therefore addresses the exact source of the old failure, rather than only its numerical example.

### Objective narrowing and concentration

The opening now explicitly requires concentration to be shown separately (`src/core/10_s01.md:7`; Chinese counterpart `src/core/00_head.md:14`). The continuation theorem keeps its local, deterministic-share and convergence conditions (`src/core/30_s3.md:72–80`; proof `src/supp/03_S3.md:49–69`). The fixed-prize witness has `Gamma=1/2`, `Gamma_delta=9/28`, and relative continuation price `9/19`, while the exact stock difference contracts by `0.9` each period (`src/supp/03_S3.md:92`; `verification/readiness_checks.py:94–114`). This is correctly used to reject the general equivalence, with the proportional-prize equivalence confined to its stated local case.

I checked the common/relative decomposition and the finite-price algebra directly. No new counterexample emerged within those stated premises. This pass does not upgrade the local calculation into a global concentration theorem or independently certify the strategic lottery extensions.

### Scope and the correction requirement

The revised statement makes the comparison conditional on fixed size and cost factors, an increase in the cultivation return, and no decrease in inbound evaluation conversion (`src/core/40_s4.md:46`). The proof and explicit reversal are at `src/supp/04_S4.md:29`; the symmetric scope formula is at `src/supp/04_S4.md:13`.

At fixed total footprint, that formula is proportional to `varphi + (g-varphi)/m`, where `m` is the number of domains. Its sign is exactly the stated comparison between off-diagonal and diagonal conversion. With fixed inbound conversion, spreading across two domains takes the correction boundary from `1` to `1/sqrt(2)` for the identity block, but to `sqrt(3/2)` when off-diagonal conversion is `2`. The new optimization/bisection check reproduces both directions (`verification/readiness_checks.py:117–155`). Size expansion and redistribution of a fixed footprint are no longer conflated.

### Functional protection and cognitive understanding

The Price-covariance result retains the otherwise-alike premise and the statement that the common benefit alone supplies no selective advantage (`src/core/30_s3.md:90–92`; proof `src/supp/03_S3.md:96`). The subsequent text distinguishes prior protection from shared cognitive understanding and treats the latter's long-term necessity as a strategic hypothesis (`src/core/30_s3.md:94–109`).

The correlated-local-benefit example is a valid countermodel to deriving cognitive necessity from this lemma: its payoff gap is `0.2-0.1=0.1`, so protection spreads without a cognition variable (`src/supp/03_S3.md:100`; `verification/readiness_checks.py:158–170`). This demonstrates the possibility, not the prevalence or complete institutional adequacy, of that route. The revised prose respects this distinction.

## Verification assessment and prior-review closure

I read all of `verification/readiness_checks.py` and ran that focused file once. All eight named groups passed. The host calculations agree across their two step sizes; the counterexample's all-time conclusion rests on an analytical bound, not a finite simulation. The stock recurrence and exact fraction arithmetic match the displayed claims. The fixed-scope optimization has deliberately bounded fixture parameters; it is not represented as a universal numerical search.

The remaining readiness groups appropriately show limited possibilities: fixed verified containment under assumed credible punishment, noncompetitive growth under a stipulated residual hazard, and zero alignment tax without an assurance of safety (`verification/readiness_checks.py:173–229`). Their comments and S15 description do not claim empirical calibration or complete-design certification. `checks_v71.py:5994–6011` registers the groups and propagates a failed group rather than silently passing it. I did not rerun the inherited full suite, which the parent review was already running.

I also independently evaluated the tied-maximal-load example above and the fixed-total scope formula for off-diagonal values `0`, `1`, and `2`. These checks import no manuscript computation.

The prior V7 mathematical review's findings therefore close as follows:

| V7 finding | V7.1 disposition |
|---|---|
| P1: R1 generalized the positive-gap cumulative bound across sign changes | Closed by constant-speed replicator restriction, exact signed-gap proof, and retained counterexample |
| P2: objective narrowing used as a concentration criterion | Closed by separate criteria in the opening and explicit stable/equalizing counterexample |
| P2: correction requirement said to rise universally with scope | Closed by fixed-size and conversion qualifications and checks of both signs |

The review's readiness conclusion is limited to those corrections and the additional functional/cognitive distinction and regression witnesses checked here. It is not a finding that unresolved empirical cruxes or the paper's explicitly provisional extensions have been settled.
