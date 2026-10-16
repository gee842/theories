# V7.2 fresh mathematical review

Review date: 4 October 2026. Scope: the new S16 and RC checks; changed passages of `src/core/40_s4.md` and `src/core/a0_s10.md`; `jointcorrection` summaries in CLAIMS and S13; the linked host, payoff, field, certificate and safeguard equations. V7.1 was used as the comparison baseline. No prior review conclusions were used, and no manuscript files were changed.

**Final verdict after resolution check:** the reduced joint certificate is mathematically correct under its stated finite-carrier model and maintained coefficient, initial-state and liability assumptions. The counterexample, covariance identity, sensitivity identity and generic invasion examples are correct. All three findings below have been resolved in the sources and independently reread. No mathematical or mathematical-scope blocker remains within this review's scope. The original findings are retained as the review record; see the resolution verification at the end.

## Findings, by severity

### 1. High — the Section 10 opening still presents institutional persistence as proved from coverage and formula funding

**Locations:** `src/core/a0_s10.md:3` (Claim, sentence beginning “Where coverage is complete and correction is financed by formula”); `src/core/a0_s10.md:5` (Why, sentence beginning “A term common to all”). Compare the new limitations at `src/core/a0_s10.md:75–79`, `src/supp/16_S16.md:38–40`, and `src/reg/CLAIMS.md:350`.

**Blocker:** yes, for the consistency of the integration's claimed result; no, for the validity of `jointcorrection` itself.

The opening retains a `[thm∣prem]` claim that the generative order persists where coverage is complete and correction is financed by formula. The Why paragraph similarly presents persistence through coverage, sanctions and formula-funded correctors as proved. These sentences are unchanged from V7.1, but the new integration expressly identifies preservation of resources, authority, execution and the action set through institutional change as an open problem. Formula funding and common-payoff cancellation do not establish those properties. In particular, selection's indifference to a common additive payoff establishes neither selection for the supporting rule nor preservation of the institutions implementing it.

The second sentence of the Why paragraph does acknowledge that persistence through replacement or entry needs separate evidence, which helps, but leaves two incompatible meanings of “persists” in the same opening. The new theorem proves invariance while effective correction and nominal liability remain within specified bounds; it does not derive those bounds from formula funding or complete coverage.

**Suggested resolution:** rewrite the opening Claim and Why so that the proved statement concerns the fixed reduced dynamics under maintained enforcement/correction assumptions, while institutional persistence is the stated design target. The new paragraph at line 79 already supplies suitable scope. This is a scope repair, not a request for a new theorem.

### 2. Medium — the local-gradient caveat should distinguish the generic strategy space from the paper's concave one-trait payoff

**Locations:** `src/core/40_s4.md:31`; generic example at `src/supp/16_S16.md:51`; compare the convex-cost calculation in `src/supp/04_S4.md:11` and the payoff at `src/core/40_s4.md:26`.

**Blocker:** no; the generic counterexample is correct, but the cross-reference risks overstating what fails in the specified model.

The new core prose first refers to “this specified influence capacity” and then says reversing its gradient would not exclude “a large change.” For fixed surroundings, the actual influence payoff has the form

\[
F(q)=Rq-fp^{\xi_f}q-\frac{\gamma p^{\xi_v}}{1+\eta}q^{1+\eta},
\qquad F'(q)=R-fp^{\xi_f}-\gamma p^{\xi_v}q^\eta.
\]

Its derivative is decreasing. Thus `F'(q0) < 0` does exclude every larger value of that same capacity trait: `F(q) < F(q0)` for all `q > q0`. In particular, a negative derivative at zero excludes every positive investment under these fixed conditions, exactly as the existing S4 proof says. The S16 example `s(q)=-q+q²` is a valid example for a general nonconcave fitness landscape, but it is outside the paper's convex-cost influence specialization.

**Suggested resolution:** retain the general warning while stating that larger increases of the same trait are excluded in the fixed concave model; large changes to other traits, coordinated action, payoffs, evaluators or rules remain outside that conclusion. Label S16's quadratic example as a generic fitness example rather than an instance of `influence`.

### 3. Low — the core joint-result summary should name subcriticality, not just boundedness

**Location:** `src/core/a0_s10.md:79`, “With uniformly bounded incoming capture gains”.

**Blocker:** no; the referenced proposition gives the correct bound, but this summary is imprecise on its own.

The support barrier follows from the full incoming row gain being at most `1−σ`, not merely from its being uniformly bounded. A finite bound above one can drive support above `c/a`, increase capture and remove the liability margin. The exact condition is correctly stated at `src/supp/16_S16.md:19–21`.

**Suggested resolution:** replace the phrase with “With the full incoming row gain uniformly below one by a margin” (or quote `≤1−σ`). No other change is needed.

## Mathematical checks and accepted scope

- **Invariant region:** at `z=0` the support derivative is nonnegative; at `z=c/a` it is at most `−εσdc/a<0`. Therefore `x` is nonincreasing, the initial capture ceiling persists, and the nominal-liability condition yields effective liability at least `ν+Δ`. No positive uniform lower bound on `d(t)` is needed for this invariance claim. The positive continuous coefficients and bounded shares suffice in the stated finite-dimensional ODE setting.
- **Selection:** common background and host payoffs cancel exactly. For fixed load traits and ordinary replicator dynamics, `Ė=s(ν−τeff)Var(e)≤−sΔVar(e)`. The population simplex is invariant. Mutation, entry, changing traits and unequal background advantages would invalidate this simple conclusion, and the manuscript excludes or discusses each.
- **Host:** at the lower boundary, `V̇=Vmin[ρ(1−Vmin)−hVE]≥0`; at `V=1`, `V̇=−hVE≤0`. The load threshold is sufficient, not a necessary description of all viable initial states. The text correctly keeps the full correctable kernel and less forgiving hosts outside this result.
- **Transient failure:** the exact initial derivatives are `Ė(0)=3/20` and `V̈(0)=−3/40`, with `V̇(0)=0`. Hence the floor is crossed for sufficiently small positive time. Smooth continuous dependence gives failure for small positive host margins as claimed. Eventual elimination of capture is consistent with this temporary protected-floor loss.
- **Barrier discussion:** S16 explicitly requires simultaneous satisfaction of active constraints, a tangent-cone qualification and well-posed implemented feedback. With the usual smooth/closed-set interpretation, this is an appropriate sufficient invariance statement. It does not silently turn pointwise barrier feasibility into endogenous preservation of the controller. No source-specific uncertainty required browsing.
- **Selection and sensitivity examples:** the generic quadratic-fitness and frequency-dependent threshold examples have the stated signs. The logarithmic partial gradient is `(1,1,−1,−1)`, the total derivative correctly sums coefficient responses, and the finite gain multiplier is `12/11`.
- **Register/interface scope:** the `jointcorrection` entries at `src/reg/CLAIMS.md:179,214,219,350` and `src/supp/13_S13.md:22,26,57` appropriately maintain the empirical liability form, correction implementation, institutional amendment/replacement and hazard interfaces as open. They do not claim a maximal kernel, endogenous funding or a general institutional guarantee.

## Tests performed and limits

1. `python3 verification/correction_checks.py`: all four groups passed. Reported cross-step maximum discrepancies were approximately `2.33e−11` for the protected example and `1.41e−11` for the transient example. The transient minimum host was `0.4275489039`; the positive-margin variant reached `0.4275723873`.
2. `python3 checks_v72.py RC`: the actual suite dispatch passed all four counted gates, zero failures.
3. Independent standard-library integration with a different state representation and `dt=0.001`: logit capture; rule support; accumulated liability tilt, with the replicator distribution computed analytically by exponential tilting; and reciprocal host, satisfying `Ẏ=(h_V E−ρ)Y+ρ`. This did not call the manuscript integrator. It reproduced the protected terminal capture `5.09627185e−8`, load `1.53583435e−10`, host `0.9999999563`, and minimum host `0.5`. It reproduced transient minimum host `0.4275488864` and eventual capture `9.97068511e−13`.
4. The independent implementation also checked a three-trait protected boundary case: loads `(0,0.3,1.4)`, initial shares `(0.25,0.5,0.25)`, hence initial mean load `0.5`, with the same time-varying field. Host remained at least `0.5`, capture at most `0.3`, support at most `1`, and mean load at most `0.5`.
5. Exact rational arithmetic independently confirmed the initial transient derivatives. A direct analytic concavity check, supplemented by rational grid evaluations, confirmed Finding 2's distinction from the generic convex fitness example.

These computations are finite illustrative checks, not a proof over all parameters or disturbances. The universal claim was assessed from the analytic inequalities. I did not rerun unrelated inherited numerical blocks, audit all inherited theorems, assess empirical calibration, or make a broad novelty judgment.

## Resolution verification

After the main agent's source edits, I reread the changed passages directly rather than relying on its summary.

1. **Finding 1 resolved.** `src/core/a0_s10.md:3` now presents the institutional design as a proposal and explicitly leaves preservation of viability and executable correction through institutional change as a constructive obligation. Line 5 scopes the proved part to the payoff rule, distinguishes the reduced joint certificate, and leaves preservation of funding, access and authority open. The former theorem-tagged institutional-persistence claim is gone.
2. **Finding 2 resolved.** `src/core/40_s4.md:31` now correctly says that a nonpositive derivative in the fixed concave return excludes gains from larger values of the same capacity with other parameters fixed. It separately identifies other traits, coordination, evaluator replacement and changed payoff rules. `src/supp/16_S16.md:51` explicitly states that its generic quadratic fitness differs from the fixed concave return. The revised statement is valid also at zero derivative by concavity.
3. **Finding 3 resolved.** `src/core/a0_s10.md:79` now requires the full incoming rule-domain gain to remain uniformly below one by a positive margin.

I also confirmed that `src/core/40_s4.md:35` now limits the public-goods conclusion to costly voluntary provision under the stated payoff rule. The tangent-cone/well-posedness qualification in `src/supp/16_S16.md:9` and the nonnegative-load/positive-host-parameter assumptions at line 22 remain explicit and sufficient for the reviewed argument. These source changes alter presentation and scope, not the numerical dynamics; no further numerical rerun was needed for their verification.

**Current disposition:** all findings resolved; no remaining blocker in the reviewed new mathematics or its revised core summaries. The full institutional target remains open, as the revised manuscript says.
