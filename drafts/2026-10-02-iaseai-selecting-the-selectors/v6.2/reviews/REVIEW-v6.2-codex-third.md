# Review of the repaired V6.2

Prepared for Ren on 4 October 2026, against the sources recorded in [the input manifest](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/input-manifest.json). This review follows the repairs described in the pasted handoff. It changes no manuscript or register.

**Most of the earlier repairs should stand. Eight substantive corrections remain: five additional scope or implication gaps and three accepted corrections that have not reached all their downstream statements.** The strongest remaining problems concern the use of an eventual-removal certificate as present independence and a supplemental inference from failed assurance to actual risk. These do not require replacing the paper's architecture. They do require another focused correction pass before treating the mathematics and its institutional applications as settled.

The review covered the core, supporting proofs, and relevant discussion and register entries through three parallel mathematical and systems reviews plus an integration and literature check. It is not a verification of every cited source or a proof certification. Each finding below identifies the smallest repair justified by the evidence.

## 1 Rival verification still confuses eventual removal with current independence

**Priority P1. Incomplete repair.** [Proposition S10.2](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/10_S10.md:45) and its [core summary](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/a0_s10.md:53).

The corrected Proposition 4.10 now carefully distinguishes eventual removal of capture from independence at the time of a decision. S10.2 still says a verifier whose inbound row sum is below one is captured by none of its sources, and proves this by invoking that proposition.

Even a row sum of zero does not supply this guarantee. Start a verifier with captured share 0.99 and support 2; let support decay at rate 0.01, with unit selection speed and unit opposition cost. Its capture logit is log(99) + 200(1 − exp(−0.01t)) − t. At t = 50 its uncaptured share is only 3.49 × 10⁻¹⁵, although it eventually recovers. The separate full-capture boundary remains invariant.

**Repair:** restate S10.2 as eventual removal under Proposition 4.10's initial-state conditions. For reliance on present decisions, require the current-state, support, residence-time and institutional evidence already introduced in [the repaired scope](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/40_s4.md:87).

## 2 The masked divergence proof still infers actual risk from failed assurance

**Priority P1. Incomplete repair.** [S6, final paragraph of the masked-divergence argument](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/06_S6.md:78).

The core now correctly distinguishes inability to establish safety from proof that no intervention lowers risk. S6 still concludes that nothing admission can see lowers the uncovered share, infers coverage lags, and invokes the coverage theorem. It does not establish either that inference or the theorem's separate residual-floor premise.

Take complete masking and uncovered share one, but conditional irreversible-event hazard hₜ = 2⁻ᵗ⁻². Assurance through detection fails maximally, while the hazard sum is 1/2 and limiting survival is approximately 0.577576. The residual-floor premise is false, so the theorem cannot be invoked.

**Repair:** copy the logical distinction of [the repaired core](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/60_s6.md:73) into the proof. Apply the coverage theorem only conditionally on its premises; describe stopping or pacing in the absence of assurance as the protection-standard recommendation that it is.

## 3 The masking ceiling needs a condition on the alignment tax

**Priority P2. Additional scope qualification.** [Remark 6.8](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/60_s6.md:71), supported by [S6](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/06_S6.md:76).

The ceiling is valid if S6's positive tax cₖ is held fixed while capability rises. The core lists bounded sanctions and falling detection as its two premises, then explicitly permits research to lower the tax two paragraphs later. Applying the ceiling along that joint path requires another condition: the tax must remain large enough relative to detection. The following example refutes that broader application, not the fixed-tax result.

Let capability be K, sanction F = Fmax = 1, detection probability exp(−K), and positive tax exp(−2K). Expected sanction exceeds the tax at every K: there is no finite ceiling. This also works under cumulative selection along growing capability. With K(t) = log(t + 2), the safe variant's advantage is 1/(t + 2) − 1/(t + 2)², whose integral diverges. Evasion tends to zero despite detection tending to zero; from equal shares its share is approximately 0.00000330 at t = 1,000,000.

**Repair:** explicitly hold a positive tax fixed, impose a capability-uniform positive lower bound, or use the sharper condition that pdet(K) Fmax eventually falls below c(K). C9 and C12 jointly determine this ceiling. Keep the cumulative-gap condition when drawing an extinction conclusion along a changing path.

## 4 Bounded effort is not a finite point of enough

**Priority P2. Additional finding.** [Proposition 5.15](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/50_s5.md:90) and [its proof](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/05_S5.md:117).

The proposition concludes that an objective bounded in the stakes is satiated. Its proof only shows bounded contest intensity. Its example, 1 − exp(−Ω), increases at every finite Ω. In the supplied four-actor contest, intensity is 3(1 − exp(−Ω))/16: positive at every positive stake and tending to 3/16. It never reaches a stopping point.

This distinction is already made correctly in [S6's bounded optimizer](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/06_S6.md:90). **Repair:** say that bounded prizes bound intensity at fixed costs. Keep a stopping rule, a finite satiation point, or bounded hazardous scope as a separate premise. The survival result conditional on variety actually stopping remains intact.

## 5 Keeping detection does not necessarily keep the response clock

**Priority P2. Additional finding.** [The narrow E1 paragraph](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/b0_s11.md:40).

The paragraph claims, with a theorem tag, that keeping AI detection while removing AI from strategic decisions leaves breakout probability unchanged. But the cited detection link defines timely intervention as being detected **and answered** before decisiveness.

With decisiveness at time 2, detection at 0.5 and response duration 0.5, the breakout is stopped. Keep the same detector and make effective response require two units of human authorization: the breakout succeeds. This counterexample concerns an irreversible strategic response within narrow E1's scope, not the reversible defensive automation exempted in X11.

**Repair:** condition invariance of breakout probability on preserving the full detection-and-response distribution. Otherwise measure the latency change and reassess enforcement under C7. This does not refute the static delegation theorem or the E1 recommendation; it corrects the additional cross-model claim.

## 6 The general standing price needs a nonlinear convergence condition

**Priority P2. Additional domain finding.** [Proposition 3.9](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/30_s3.md:72) and [S3's full form](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/03_S3.md:49).

Constant coefficients on the reference path repair the earlier time-varying-Jacobian error. They still establish the price of the linearized dynamics, not automatically the derivative of the actual nonlinear infinite-horizon value. An integrability or tail condition is missing for the general prize depending on total stocks.

Set n = 2, κ = d = δ = 1/2, r = 1, no sharing, provision or diffusion, and Ω(S) = S². At the symmetric steady reference S = 1, the stated gains are Γδ = 1/3 and Γcδ = 2/3, so the formula gives relative price 1/2 and common price 2. Yet any positive common perturbation gives Sₜ₊₁ = (Sₜ + Sₜ²)/2 and eventually unbounded discounted winnings. Once S ≥ 4, S at least doubles each period, so discounted prize terms at least double too. The actual continuation value is infinite for every positive perturbation.

**Repair:** impose a growth and integrability condition sufficient to interchange differentiation and the infinite sum, or explicitly restrict the result to valuation in the linearized system. This finding does not invalidate the fixed-prize or proportional-prize ratio cases. The report should not treat it as a counterexample to the geometric sum itself.

## 7 S3 still asserts the rejected exact lottery equality

**Priority P2. Incomplete repair.** [S3, Rivals who respond](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/03_S3.md:82); also check [S0 assumption A9](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/00_S0.md:16) and [the core's strategic extension](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/30_s3.md:80).

S2 now separates the finite-jump lottery value from the deterministic local price. S3 still says the fixed-opponent finite-jump price equals Γδ/(1 − Γδ) even at the paper's jump sizes, then applies the strategic elasticity substitution to that discussion.

The independent Bellman calculation was rerun: r = 1.5, Γ = 0.6, d = 0.2 and δ = 0.97 give 1.03111035 on 2,000 cells, against the formula's 1.08178439. The 1,000-cell value is 1.03110642; the linear-strength control agrees with the formula.

**Repair:** propagate S2's restriction throughout S3 and the shared assumptions. Keep the nonlinear lottery and responsive-rival values numerical unless separately proved. The exact linear case can remain.

## 8 The pacing citation does not establish a unique safe equilibrium

**Priority P2. Additional source-scope finding.** [Section 8.3b](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/80_s8.md:58), [X8](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/disc/08_X8.md:21), and [EV11](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/reg/EVIDENCE.md:198).

The text describes pacing as the unique Markov-perfect equilibrium at high effective hazard. The cited paper's Theorem 1(c) establishes that its pacing profile is an equilibrium and its global racing profile is not; it does not establish uniqueness among all Markov equilibria. Moreover, the pacing profile itself races forever from sufficiently unsafe starting states. A parameter region favoring that profile is therefore not a guarantee of safe pacing from every starting state. [Fudenberg and Koh, Theorem 1 and the discussion immediately following it](https://arxiv.org/html/2609.28291v1#S3.SS2)

**Repair:** state the two demonstrated equilibrium facts and the relevant initial-state qualification. Keep the corrected hazard direction and monitoring-lag comparison. Update EV11 and TESTS to reflect that the relevant full-text passages have now been checked.

## Smaller corrections to carry through

- **Reversibility:** §12 now supplies the shared condition that reversal precede the protected loss and be executable by an independent corrector that survives. [S8's method](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/08_S8.md:56) and [X8's table](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/disc/08_X8.md:145) still contain categorical labels for capture, delegation and standby. Carry the shared condition into these cells. This is incomplete propagation, not a new demonstration that the ranking fails.
- **Complete pooling:** [Proposition 10.2(1)](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/a0_s10.md:28) needs β < 1 for preservation of choices and ordering. At β = 1, payoffs (2, 1) become (1.5, 1.5); strict ordering and relative selection disappear.
- **Heterogeneous background payoffs:** [Lemma 3.11](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/30_s3.md:90) permits carriers otherwise alike **or** each carrier's other payoff held fixed. The latter permits heterogeneity correlated with the trait. Delete that alternative or state the required covariance condition; the following scope already explains it correctly.
- **Dwell endpoint:** the proof now treats the dwell as an infimum, but [the basin statement](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/11_S11.md:99) still uses an attained minimum. Require release strictly beyond the boundary time where appropriate.
- **Trust comparison:** [S11's comparative static](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/11_S11.md:8) should specify which payoff changes and what is fixed. A fall in T − R alone does not guarantee a lower trust threshold if both T and R change.
- **Review metadata:** the README still says V6.2 has not been reviewed outside the drafting family and reports 202 assertions. Bring the current-status lines and counts into agreement with the completed review and check log; historical changelog counts can remain historical.

## Repairs that should be retained

The revised cumulative-selection restriction closes the old payoff-monotonicity counterexample. The correction-rate law retains its tracking and cost-floor conditions. Proposition 4.10 now distinguishes eventual removal from decision-time independence. Detection timing now uses conditional continuation values, with the delayed cases stated separately. Oversight topology now states the layer-independence condition. The core distinguishes zero-tax neutrality from spreading, and failed assurance from impossible removal. Readiness now tests the lower level at the threshold; activation counts execution delay; and §12 gives every path the same reversibility condition.

The remaining operational research programme, multitype participation boundary, lottery proof and dynamic welfare comparison are already recorded as open. Their mere incompleteness is not another finding here.

## Verification and supporting material

The assembled documents match a fresh build byte for byte. The structure and cross-reference checks pass in a disposable copy containing the required earlier bibliography. The default numerical suite passed all 213 assertions, with zero failures, in 364 seconds. The independent counterexamples pass. A final hash comparison confirms that the reviewed manuscript, registers and existing scripts remain unchanged.

- [Build comparison](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/build-comparison.json), [structure log](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/xref.log), and [numerical run log](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/checks.log).
- [Mathematical findings](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/math/FINDINGS.md), [reproduction](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/math/audit_math.py), and [results](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/math/results.json).
- [Systems findings](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/systems/FINDINGS.md) and [passing counterexamples](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/systems/checks.py).
- [Transition findings](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/transition/FINDINGS.md) and [passing counterexamples](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-third/transition/counterexamples.py).

Passing numerical and structural checks does not resolve the scope and implication errors above. The review leaves the manuscript untouched and makes no commit.
