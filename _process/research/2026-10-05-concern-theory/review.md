# Independent review of the concern theory

5 October 2026. Read-only audit of `THEORY.md` against `learning-formal.md` and `dynamics-formal.md`. No main-document or canonical-theory edits were made by this reviewer.

## Verdict

**Accept the core conditional construction; apply the small precision corrections below before final release.** The learned product, threshold crossing, finite-class widening, succession criterion, budget-prefix theorem, and optional productive bridge are mathematically consistent in their declared domains. No unsupported universal direction theorem is inferred. The main document distinguishes model closure from an empirically complete account of concern and acknowledges its remaining architectural premises.

## Corrections

1. **THEORY §5, linear identifiability:** qualify the exact iff as applying to a **consistent linear system with unrestricted real parameters**. The appendix supplies this condition. An inconsistent system has no fitted parameter and the unqualified universal statement about “all solutions” becomes vacuous; constrained parameter sets can also change the iff.

2. **THEORY §§8 and 10, parameter domains:** explicitly give `0<γ≤1` for efficacy learning and `0<t_x≤1` for the retained fractions in the favorable succession theorem. The appendix already does so. Merely saying “positive transmission” does not exclude amplification, under which the stated phase-minimum proof would need alteration.

3. **dynamics-formal §7, equation (10):** state `M=b+H g_max w_max>0` before dividing by it. If `M=0`, the repair score is identically zero and a positive-cost repair is already unselected, so no crossing bound is needed. For `M>0`, the proposed sufficient stopping bound is sound: nonnegative z can be bounded by the maximal multiplier, and negative z gives a nonpositive score directly.

4. **dynamics-formal §8, masking example:** say explicitly that this is an **expanded action family with separate private and recipient effects**. Masking removes the observer's private cue loss while having recipient efficacy zero. This differs from the preceding repair table, in which the same efficacy controls both private loss and recipient harm. The displayed mask burden `1+vH=11` is correct for the expanded action; substituting `Q_M=0` into the old repair table would instead add the private loss b. The new example is valid, but its changed action table should be explicit.

5. Optional notation clarification: in dynamics-formal §6, if retaining the finite-capacity remark, write `max_{0≤j≤m}P_j` for the maximum stock excursion when surplus is discarded only after the generation's final receipt. Including the end-of-generation point avoids ambiguity about the last receipt. The core main-document cash theorem has no such ambiguity.

## Checks of the central claims

**Learned acquisition.** Both factors start at zero, converge monotonically under the fixed positive teaching schedule, and have product bounded by `G W`. Therefore a finite strict protective preference exists exactly when `GWH>c−b`. Equality never produces a strict preference. If `c<b`, protection was privately preferred already; the theory correctly excludes that case as evidence of newly formed concern.

**Generalization.** The row-span theorem is an identification result inside a fixed linear feature model. The shared/gated architecture pair provides the separate, stronger point that self data do not select the evaluation feature map. The report does not claim that accurate world-model prediction forces concern, or that an arbitrary new recipient has positive alignment. Finite recipient classes are separable and their collective affordability is an additional condition. Infinite pointwise convergence is not silently converted to a uniform deadline.

**Succession and timing.** Write a coordinate's local target as `L=A/(1−r)`. In the favorable domain `0≤r<1`, `0<t≤1`, its generation-start fixed point satisfies `0≤x_*≤L`. From zero, starts are at most `x_*`; local affine updates then increase the coordinate within each generation. Thus all three coordinates attain their relevant minima at the same post-succession phase, and the protection score is coordinatewise nondecreasing there. The product of the individual start values is therefore the actual minimum score, not an illicit multiplication of minima from different phases. Decisions occur before refresher updates, as required.

The strict fixed-point iff is valid **from the stated all-zero start**. It should not be generalized to arbitrary initial states without care: when a fixed-point score equals the action threshold, a trajectory approaching it from above can remain strictly protective at every finite date. The main document retains the needed initial-state restriction.

**Private returns held fixed.** At fixed `a,b,z`, changing represented recipient stakes H changes the term `zHgw`. This gives the claimed functional counterfactual dependence when `zgw>0`. It need not change the chosen action at every state; thresholds can leave behavior unchanged. The report correctly speaks of action evaluation and warns that a generous-looking act does not identify the underlying motivation.

**Criticism.** Positive and negative efficacy regimes are separated. The stationary positive-efficacy theorem does not guarantee instantaneous safety after an environmental change. Continuing probes can revise z even when the current ordinary action is withheld. Criticism in the proved specimen corrects an intervention belief; it does not itself prove revision of moral standing, the shared routing architecture, or the correctness of all correspondence targets. The main report treats those broader revisions as further tasks rather than as derived updates.

**Resources.** The cash condition correctly pays costs before receipts, checks the bootstrap, and preserves enough reserve to enter the repeated regime. An externally maintained receipt stream remains a stated dependency. In the optional productive bridge, exact equality of limiting receipts and costs does not imply failure: deficits caused by initial capacity shortage decay geometrically and have a finite sum. The appendix handles this boundary correctly.

**Mechanistic completeness.** Within the declared abstract model, updates, action choice, outcome metering, resource transactions, and transmission are specified. Primitive self valence, shared evaluation routing, exact alignment evidence, available probes, archive fidelity, authority, and material inputs remain supplied. This is coherent conditional closure. It must retain that qualification: the equations do not physically construct those primitives or empirically establish their co-occurrence. The main document currently makes the qualification clearly.

## Independent checks

The adjacent `independent_review_checks.py` does not import either author verification script. It uses a different computational route:

- Exact rational Gaussian elimination solves the full cyclic equations for every decision phase, rather than constructing the fixed point from the geometric-sum formula.
- Direct decision-before-update traces verify synchronized phase minima and strict/tie behavior from zero.
- A productive equality regime is checked with different within-generation receipt placements. The infinite reserve is verified by a nonnegative residual identity for every phase; a reserve smaller by 1/100 produces a finite failure witness.

`independent-review-checks.json` records **180** cyclic phase systems, **489** durable-threshold/tie comparisons, **432** phase-specific productive equality reserves, and **432** corresponding underfunding failures, all passed. These are independent mathematical checks, not empirical evidence or substitutes for the proofs.
