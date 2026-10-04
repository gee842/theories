# Independent systems, alignment and transition review of V6.2

**Reviewed 4 October 2026.** Scope: THEORY §§4, 6, 9, 10, 11; SUPPLEMENT S4, S6, S9–S11, S13; the corresponding CLAIMS/TESTS entries; relevant boundary cases in S14 and numerical implementations. Reviewer: an independent Codex subagent assigned to the systems/alignment track. No manuscript edits or commits were made.

## Assessment

The revision materially improves the mathematics-to-argument boundary. The separation of sufficiency from necessity in the correction-rate law, the explicit capacity-tracking hypothesis, the corrected delegation game, the two-clock condition for silent crossing, the retained-host transient calculation, and the separation of institutional independence from independent errors are all substantive improvements. Several of the manuscript's strongest claims now have recognizable, checkable mathematical content.

The principal remaining problems in this track are **transfers from a valid local calculation to a stronger operational conclusion**. A failure of behavioral detection is made to imply failure of removal and the hypotheses of a survival theorem. A simple-versus-simple sequential test is made to implement a threshold decision with uniform error guarantees. A sufficient multitype participation basin is treated as the tipping boundary. A constant-liability calculation is stated as an iff criterion without fixing the liability path. These problems survive a passing numerical suite because the suite exercises narrower cases than the prose claims.

There are nine findings below: two P1, six P2, one P3. P1 means that a central recommendation or operational guarantee is stronger than its support; P2 means an incorrect result, empirical discriminator or scope statement needing repair; P3 is a boundary qualification. None is an argument to discard the entire framework.

## Findings at a glance

| ID | Priority | Confidence | Finding | Main stable key / location |
|---|---|---|---|---|
| SA-01 | P1 | High | Masked detection does not establish impossibility of removal or the residual-risk floor | `masked`, THEORY 635–637; SUPPLEMENT 625–629 |
| SA-02 | P1 | High | Readiness's SPRT guarantee applies to its registered endpoint hypotheses, not every state above/below a policy threshold | `readrule`, `readiness`, SUPPLEMENT 1051–1057; THEORY 1096–1098 |
| SA-03 | P2 | High | The minimum type threshold is a sufficient participation basin, not a scalar tipping boundary | `unravel`, SUPPLEMENT 879–883 |
| SA-04 | P2 | High | Test B mistakes an absolute cost for a relative disadvantage | `noinside`, TESTS 121; SUPPLEMENT 320, 334–336 |
| SA-05 | P2 | High | The host's scalar iff margin needs a constant effective-liability hypothesis | `safeguards`, THEORY 982–983; SUPPLEMENT 953 |
| SA-06 | P2 | High | Weak sanctions preserve safe variants but need not remove unsafe variants; zero tax is neutral | `nested`, `masked`, THEORY 627–639 |
| SA-07 | P2 | High | Oversight products require independence across layers or conditional link reliabilities | `topology`, THEORY 651; SUPPLEMENT 655 |
| SA-08 | P2 | High | The conclusion's universal basin claim outruns the expressly conjectural whole-system result | THEORY 1225 versus 1013; SUPPLEMENT 1081, 1094 |
| SA-09 | P3 | High | The core-pruning stability result omits its strict/nondegenerate boundary condition | `certificate`, THEORY 400–402 |

## SA-01 — Keep detection failure, removal failure, and residual risk distinct

**Priority P1; high confidence.**

**Locations.** [THEORY.md:635](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:635), continuing at line 637; [SUPPLEMENT.md:625](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:625), especially lines 627–629. Stable key `masked`. Propagation: THEORY 920 and 1090; TESTS 26, 74, 99–100; CLAIMS 126, 193, 206. Relevant limiting statements: THEORY 506, 514–518, 647; SUPPLEMENT 510, 1129.

**What is proved.** Given a safe variant costing `c_k` and an unsafe variant detected with probability `p_det`, sanctions change their payoff difference by `p_det F - c_k`. If this is negative, sanctions based on that detector do not protect the safe variant against its matched unsafe variant. The manuscript proves this correctly.

**What is added without proof.** The text then says that no developer can buy removal it cannot verify, that beyond the capability of a shown-safe control protocol nothing admission can see reduces the uncovered share, and that Theorem 5.13 applies. None follows from the payoff difference:

1. A detector can fail while an intervention removes or reduces a divergence. Inability to confirm removal using a given detector is an epistemic limitation, not proof that no removal intervention exists. An architecture restriction, a monitored training intervention or a resource/permission restriction can be evaluated through evidence other than the hidden behavior. Even when removal is uncertain, an intervention can improve its probability without providing a proof of absence.
2. `p_det` is a detection probability. It is not the probability of an irreversible event after all correction. No equation in `masked` connects these quantities.
3. A limit on currently demonstrated control is a limit on the established safety case. It is not a lower bound on actual residual hazard. Theorem 5.13 additionally needs `(residual floor)`, explicitly described elsewhere as an empirical crux that a safety architecture could refute. It also needs `(coverage lags)` in its specified uniform sense; incomplete coverage alone is insufficient.

**Concrete mathematical counterexample to the survival inference.** Let every deployed divergence be completely masked under the evaluation, `p_det,t = 0`, and let its realized irreversible-event hazard after an independent intervention be `h_t = 2^(-t-2)` for `t ≥ 0`. The detector and sanction result still fails maximally, but `Σ h_t = 1/2`, so survival has a positive infinite-horizon lower bound by the manuscript's own Lemma 5.11. One can even take the contestable uncovered share to be one throughout: in that case `(residual floor)` is false, and that is precisely why the survival theorem cannot be invoked. This counterexample is not a claim that such an intervention is available now; it shows which additional premise the inference needs.

**Consequence.** The new alignment route into E2/E3 is presented with more mathematical force than the model supplies. The scope language of §5.3 and §6.5 handles this distinction well; Remark 6.8 reintroduces the inference they carefully reject.

**Minimal repair.** Replace the removal impossibility with “these tests cannot establish that the developer has removed the divergence.” Replace the claim that nothing can reduce coverage beyond shown-safe control with a statement about the absence of an established assurance case. Invoke Theorem 5.13 only with its named premises, particularly a justified residual-risk floor for that masked class. Keep E2/E3 as a recommendation under the protection standard where assurance is absent; distinguish that recommendation from a theorem that continued deployment necessarily loses survival. Add an explicit masking-to-coverage/risk interface to S13, separate from the existing masking-to-reports interface.

## SA-02 — A two-point SPRT does not give the claimed threshold-wide readiness guarantee

**Priority P1; high confidence.**

**Locations.** [SUPPLEMENT.md:1051](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:1051), proof at 1053 and application at 1057; [THEORY.md:1096](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1096)–1098. Stable keys `readrule`, `readiness`. TESTS 154 adopts the rule. Existing implementation: [checks_v62.py:4504](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/checks_v62.py:4504)–4523.

**What is correct.** The likelihood-ratio boundaries and conservative error bounds are valid for the two registered simple hypotheses under the stated independent-observation likelihood model. The union bound across seven dimensions is valid without cross-dimension independence. The computation at Gaussian means zero and one reproduces this result. The conjunction calculation `0.95^7` is also correct under its explicit independence premise.

**Missing step.** Definition 11.2 defines “met” by being past a threshold for a residence time. S11.3 tests a registered value below that threshold against another above it. Its endpoint error bounds do not apply to every value between those two hypotheses. No indifference region or rule for it is defined. Consequently the claim that a ready state is held back with at most the registered probability is not supported for a state just beyond the actual threshold.

**Independent check.** Use exactly the manuscript's Gaussian likelihood ratio, `H0: μ=0`, `H1: μ=1`, noise `σ=1`, `α=.01`, `β=.05/7`, and define the policy threshold at `.5`. In 20,000 independent runs per mean, seed 17:

| True mean | Relation to policy threshold | Probability declared met |
|---|---|---:|
| 0 | Registered null | 0.00555 |
| .49 | Not met | 0.49395 |
| .51 | Met | 0.54665 |
| 1 | Registered alternative | 0.99595 |

The asserted endpoint bounds are about `.01007` and `.007215`. A state barely below the threshold is falsely released about half the time; a state barely above it is held back about 45% of the time. Neither numerical sampling uncertainty nor changing the noise explains this discrepancy. The implementation checks only the two endpoints, where the theorem works.

**Additional operational gap.** The iid fixed-parameter test does not establish that a time-varying state remained above a threshold for a residence time. Deferring the stopping date until the residence interval has elapsed is not itself a test of sustained compliance throughout the interval. Reopening dimensions repeatedly also requires stating whether the error budget is per episode or across the lifetime of the arrangement. These are implementation gaps, not claims that sequential testing is unusable.

**Consequence.** This is the rule that would release a pause, and the paper uses its claimed control of false holds to limit participation erosion. The guarantee presently protects a narrower statistical decision than the policy decision.

**Minimal repair.** Define an explicit indifference band `[q0,q1]` and state which policy action applies inside it, or formulate a one-sided sequential test with guarantees uniform over the unsafe parameter set and a stated alternative separated by a margin. Distinguish “not yet certified” from “proved unmet”; uniform low false-release and low false-hold probabilities with guaranteed finite stopping cannot simply be demanded arbitrarily close to a sharp threshold. Add the sampling, stationarity and residence assumptions, and state the error-budget horizon. Preserve the valid endpoint result as an example, not as the completed readiness rule.

## SA-03 — Multitype participation has a multidimensional basin

**Priority P2; high confidence.**

**Locations.** [SUPPLEMENT.md:879](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:879)–883, stable key `unravel`; [THEORY.md:933](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:933); CLAIMS 154. Existing check: [checks_v62.py:4662](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/checks_v62.py:4662)–4697.

The proof correctly establishes that `x < min_k x†_k` makes every type's outside share decrease, so this is a sufficient basin returning to participation, subject to an inside seed in each type. It does not establish the next claim: crossing that aggregate minimum makes the first type's departure push the system toward the next threshold. Types still below their own thresholds can return faster than the first type leaves, reducing aggregate `x` and reversing the first type's incentive.

**Counterexample inside the stated dynamics.** Use two types with fixed masses `(0.1,0.9)`, `c1=c2=.3`, `s1(x)=.48(1-x)`, `s2(x)=.6-.4x`. The tipping shares are `.375` and `.75`, the same sanction functions as the manuscript's examples. Start at type-specific outside shares `(.5,.4)`, so aggregate `x=.41 > .375`. Under the proof's dynamics:

`ẋ1 = .5·.5·(.3-.48·.59) = .0042`,

`ẋ2 = .4·.6·(.3-(.6-.4·.41)) = -.03264`,

`ẋ = .1 ẋ1 + .9 ẋ2 = -.028956`.

RK4 integrations at steps `.02` and `.01` cross back below `.375` by approximately `t=1.17` and return to essentially full participation by `t=500` (aggregate outside share `3.62×10^-40`). Thus aggregate coverage below the proposed `1-.375=.625` threshold is compatible with full recovery: the initial coverage is `.59`.

The suite samples 800 states only **below** the minimum and puts its two above-minimum examples' outside mass almost entirely in the first type. Those examples are valid but do not test the claimed general boundary. Different distributions across types at the same aggregate coverage can have different outcomes.

**Minimal repair.** Call `1-min x†_k` a conservative sufficient coverage level, not the arrangement's tipping threshold. State cascades conditionally on departures keeping aggregate `x` above the current type's threshold and reaching the next. If an actual multitype tipping boundary is wanted, compute the separatrix in the vector of type shares or give additional conditions that make the scalar reduction valid. Record fixed type masses and positive initial participation explicitly.

## SA-04 — Test B does not discriminate the proposed mechanism as written

**Priority P2; high confidence.**

**Locations.** [TESTS.md:121](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/TESTS.md:121); [SUPPLEMENT.md:320](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:320), 334–336; [THEORY.md:429](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:429). Relevant key `noinside`.

Test B predicts opposition to correction keyed to no one **even where it burdens rivals more**, and treats support at a net cost to the carrier as refuting the mechanism. Proposition 4.4 proves a different comparison: among otherwise identical carriers facing the same externally changed correction, the carrier paying more of the contribution cost loses. A choice about a policy that changes everyone's rents is not a matched-carrier contribution comparison.

**Counterexample.** For two carriers with the paper's relative objective `J_i=π_i-π_j`, a uniform rise in correction lowers own rent by 1 and the rival's by 2. The actor incurs an absolute cost yet gains 1 in its objective. This can arise directly from rule rents `R_i/d`: take `(R_i,R_j)=(2,4)` and increase the same `d` from 1 to 2, with no rule keyed to the supporting carrier. The correction changes rents from `(2,4)` to `(1,2)` and improves the supporter's relative position. The actor can therefore support precisely the observation that Test B calls a refutation.

This does not challenge free riding on independently funded correction. It challenges treating absolute-cost support for a universally applied policy as evidence against relative incentives. Proposition 4.4(5) already admits gains from correction applied to everyone under another route.

**Consequence.** A central registered rival-theory discriminator can classify evidence predicted by the paper's own relative-objective model as a refutation. Conversely, support could be dismissed under entry-barrier theory even when it is fully consistent with the paper.

**Minimal repair.** Measure the supporter's **relative** net effect, including rivals' costs, its remaining rents, host benefits and any benefit mediated through customers or liability. Predict opposition only where the policy reduces the relevant relative objective after these effects, or use the narrower matched-carrier contribution experiment. Retain the appropriability contrast, but do not infer distinct predictions from whether a rule is formally keyed to a carrier alone.

## SA-05 — The sufficient-safeguard margin is exact only for a fixed liability path

**Priority P2; high confidence.**

**Locations.** [THEORY.md:982](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:982)–983; [SUPPLEMENT.md:953](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:953). Key `safeguards`; relevant interface SUPPLEMENT 1117.

The proof tilts the initial distribution by `exp(-s Δ e t)`, which assumes a constant effective margin `Δ`. Yet the theorem defines `Δ=τ_eff-ν` in a setting where `τ_eff=τ(1-x_rule)` changes as capture unwinds. The scalar iff statement neither fixes `Δ` thereafter nor says that it is a constant design parameter. In the dynamic case the exact tilt is

`exp[-s e ∫_0^t (τ_eff(u)-ν)du]`.

The entire cumulative path enters the host trajectory. A constant lower bound above the computed threshold is sufficient by comparison; it is not necessary for every varying path.

**Independent check.** Use the manuscript's forgiving-host parameters `ρ=.05`, `hV=.08`, `V0=1`, `e_min=0`, `e_max=1`, race share `.99`, and floor `.3`. Both paths start with margin `.08`:

| Effective margin path | Minimum host level |
|---|---:|
| `Δ(t)=.08` | .139732 |
| `Δ(t)=.08+.92(1-exp(-t))` | .701216 |

The first crosses the floor; the second remains well above it. Both step sizes `.02` and `.01` agree to better than `6×10^-8` in the minimum. Thus neither the initial margin nor its global minimum decides the iff criterion. A rising margin is particularly relevant here because independent correction restores effective liability over time.

**Minimal repair.** State the exact theorem for a constant effective margin imposed at the stated initial state. Add a corollary that a time-varying margin bounded below by that constant is sufficient. If a parametric liability schedule is wanted, define the schedule first and compute the threshold in its scalar parameter. Preserve the current host calculations; they are useful constant-control viability boundaries, as the manuscript already says they are not the full correctable kernel.

## SA-06 — Weak deterrence is not exclusion; a zero tax is not spread

**Priority P2; high confidence.**

**Locations.** [THEORY.md:627](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:627), lines 631 and 639; [SUPPLEMENT.md:612](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:612), 625. Keys `nested`, `masked`; compare the correctly worded Lemma 3.3(3), THEORY 219.

The core says a sanction “at least” the gain from evasion keeps the divergence out. The proof only says evasion does not grow, and explicitly reserves selection-out for strict inequality. At `c=.3` and `p_det F=.3`, safe and unsafe variants have equal payoffs. Under replicator dynamics their starting shares remain unchanged; an unsafe share of one half remains one half forever. Weak deterrence may sustain a fully safe initial configuration without new entry, but does not establish elimination from a mixed field, robust exclusion under mutation or unique compliance among indifferent strategic actors.

The same distinction is lost at THEORY 639, where a tax of “zero or below” is said to spread a safeguard. THEORY 629 and SUPPLEMENT 618 correctly state that a zero tax is neutral.

**Minimal repair.** Use “protects compliance from being selected against” for `≥`, and “selects evasion out” only for a uniformly strict margin or an explicitly divergent cumulative selective disadvantage, with a safe variant present. For actual admission exclusion, state the separate blocking mechanism. Change “zero or below spreads” to “negative spreads; zero is neutral.” This is a wording repair grounded in a distinction the paper already proves correctly.

## SA-07 — The oversight formulas need a cross-layer dependence assumption

**Priority P2; high confidence.**

**Locations.** [THEORY.md:651](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:651); [SUPPLEMENT.md:655](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:655)–657. Key `topology`.

A check at each of `k` layers catching with marginal probability `p_l` does not imply serial success `p_l^k`. The proposition explicitly assumes independence of duplicate checks, but does not impose independence of layers or define `p_l` as a conditional success probability given the preceding links' success. The same issue affects multiplying layer-level redundant success probabilities.

For six layers, each with marginal catch probability `.9`, independent successes give `.531441`. Perfectly correlated successes give `.9`; disjoint failure events of mass `.1` each give `.4`. All have the stated marginal reliability. No separately stipulated all-defeating common-cause variable is needed for the discrepancy. The exact general bounds are the Fréchet bounds `max(0,k p_l-(k-1)) ≤ P(all succeed) ≤ p_l`, before additional dependence structure is assumed.

The common-blind-spot ceiling is sound and valuable. It does not by itself establish the independence needed for the preceding product formulas or the budget-efficiency ranking.

**Minimal repair.** Add conditional independence across layers, or define each link reliability conditionally so the product follows from the chain rule. Describe the numerical topology comparison as an independent-link benchmark. State that realistic comparisons require the joint failure structure, not only each check's marginal accuracy and one common-cause probability.

## SA-08 — The conclusion should preserve the declared status of the generative basin

**Priority P2; high confidence.**

**Locations.** [THEORY.md:1225](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1225), against [THEORY.md:1013](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1013), THEORY 833, [SUPPLEMENT.md:1081](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:1081), and 1094. Related keys `profile`, `capturebasin`, `reachable`.

“Any arrangement with these marks, whatever it is called, changes the basin” is universal dynamical language. The seven marks describe mechanisms and intended effects, and each has support within particular models. The manuscript expressly says that whole-level attraction is conjectural, no result shows the transition requirements can be met together, and the multi-domain viable capture basin with the host is not computed. A design checklist does not supply the missing joint dynamics or a reachable viable basin.

This is not an objection that the paper must solve the whole institutional transition before making recommendations. The careful qualifications are already present. Also, changing a basin is a weaker claim than proving a reachable, durable generative attractor: missing reachability alone would not refute the sentence. The precise defect is that the joint dynamics and the basin allegedly changed have not been identified, so the unconditional system-wide assertion is stronger than the available row-by-row directional results.

**Minimal repair.** Say that arrangements with the marks are intended to change the selection dynamics in the generative direction, and that their viable basin, reachability and durability still have to be established. Keep “Change the basin, then add speed” as the clearly attributed authorial maxim; distinguish it from what the assembled models prove.

## SA-09 — Core pruning needs a strictness convention at gain one

**Priority P3; high confidence.**

**Locations.** [THEORY.md:400](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:400)–402; [SUPPLEMENT.md:399](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:399). Key `certificate`; Table 9.1 R3b at THEORY 909.

The core removes domains whose inbound gain is **below** one. Proposition 4.10(4) then says a nonempty core's configuration is stable. Hyperbolicity is stated for part (1), not for part (4).

Take one domain with `a=b=c=d=ε=ζ=1`, so `G=1`. It is never pruned, but captured state `(x,z)=(1,1)` is not stable. From arbitrarily nearby states `x=z=1-δ`, `z≤1`, so the share cannot increase; any positive interior limiting share would have `z=x<1` and strictly negative share drift, a contradiction. The trajectory tends to `(0,0)`. An independent integration from `(.99,.99)` confirms this. Thus a nonempty threshold-one core need not be stable.

**Minimal repair.** State the nondegeneracy assumption excluding gain-one subset sums for the pruning theorem, or define/prune a strictly sustaining core and analyze equality cases separately. In “every initial state” language also retain the share-below-one restriction: exact boundary `x=1` is invariant under replicator dynamics even when the gain is below one.

## Results re-derived without finding a substantive error

The following checks support retaining the corresponding mechanisms. They are mathematical checks within their stated models, not empirical validation.

### Correction, influence and field dynamics

- Integrating carrier-keyed support over a fixed horizon gives `z_i*=χ q Σ_j b̂_ij y_j/d_i` and the horizon factor `L_i=1-(1-exp(-ε_i d_i T_h))/(ε_i d_i T_h)`. Weighting by own decisions gives the quadratic `p²` term. The threshold `p*=(f/(χ ȳᵀMȳ))^(1/(2-ξ_f))` follows from the marginal condition at zero.
- With no floor, optimizing `χ q Ŷ/d - γ p^ξ_v q^(1+η)/(1+η)` gives `q*=(χ Ŷ/(d γ p^ξ_v))^(1/η)`. Substitution into the evaluation row sum gives a cultivated term proportional to `γ^(-1/η) d^(-(1+η)/η)`. Its growth exponent is `[α_ctl-(1+η)α_cor]/η`; the correction threshold follows.
- The sufficient rate law needs only the envelope on capacity stated in the paper. The necessary half correctly requires tracking; gradually selected capacity with bounded integrated forcing is an important, explicitly registered counterexample to unconditional necessity.
- Replacing `d` by `d_eff=d exp(-w δ_h t)` gives the shift `w δ_h`. This is a valid result for the specified production form. Its empirical elasticity and the effect of AI assistance remain open, as S13 correctly records.
- With `q*∝p^((2-ξ_v)/η)`, cultivated conversion scales as `p q*`, yielding the stated high moment and splitting factor. The size elasticities matter; the revision no longer overstates a universal cubic law.
- At a binary field configuration, share-direction eigenvalues have the signs stated in Proposition 4.10(1); full-row gain below one gives global asymptotic removal for shares initially below one. The strict row certificate is sufficient, not necessary, as the manuscript states.
- The affine masking threshold and the two-clock silent-crossing condition are correctly separated. Capture in the limit is insufficient to show silence before the first host crossing, and the revision now makes this explicit.
- For one-domain insulation, `z̃(t)=G exp(-εdt)` and `u(t)=u0+ζc[G(1-exp(-εdt))/(εd)-t]`. These give the initial increase in capture, the return-of-share equation and the depth lower bound. The recruitable-lineage result is a genuine conditional mechanism; protecting a nonrecruiting alternative is correctly distinguished from bounding the competing lineage's depth.

### Delegation and alignment

- In the faithful-instrument game the private gain from racing is `ε(b-h_d)-c`; adding the others' mean payoff produces the stated `θ*`. A faithful instrument need not fix the principals' game.
- In the speed game the winning-probability gain is monotone in speed, with the stated limits for zero or positive numbers of other delegators. Shared control-loss cost is independent of speed under the model. Universal adoption leaves rank probability unchanged and worsens shared survival.
- The full survival-ratio form of Proposition 6.4 supports the certain-lock dominance result when survival without delegation is positive. The correction restricting strategic complements to `p=1` matters and is properly retained. The model is static, and the text correctly declines to infer a dynamic elimination theorem from it.
- Capacity erosion and recovery times follow directly from their exponential ODEs. Whether losing the capacity to execute every delegated task implies losing effective authority is an interface governed by the O2 operational test, not the ODE alone; the manuscript's practical override discussion helps here.
- The matched-variant alignment-tax result is correct under its premise, and does not eliminate unmatched developers with offsetting advantages. The revision's examples and scope reflect this. The remaining issue is the weak-versus-strict sanction language, not the matched-variant mechanism.
- The opaque-corrector summability statement and its revised numerical example are correct. The manuscript properly separates residual safety from the normative status of legibility. This distinction should also govern Remark 6.8.

### Generative alternative and transition

- The common-frontier public-good calculation yields the stated private and joint first-order conditions for interior solutions. The underprovision of chosen common effort is now explicitly acknowledged.
- The two sharing conventions give different effective prizes, and the revision correctly withdraws the old positive-positional-prize claim under unrestricted “others only” sharing. Neutrality at complete pooling needs the already noted care with zero relative differences.
- The constant-margin host comparison is valid and the independent calculation reproduces its minimum. It is useful as a boundary for that fixed control, although it is not the full viable kernel and does not determine general time-varying controls.
- The signalling model's mixed-equilibrium correction is sound on its stated support: when prior trust is insufficient, the receiver's restraint after the costly step is bounded by `c_R/Π_R`; the candidate attaining the bound requires the stated survival-type incentive condition. The paper correctly limits its zero-cost-imitation conclusion to this signal game.
- A hazard-free pause that shifts only the calendar preserves survival over the same active rounds. The distinction between buying calendar time and changing the hazard process is clear and useful.

## Disposition of earlier review corrections in this track

| Earlier issue | Current disposition | Evidence and remaining qualification |
|---|---|---|
| A falling positive cost floor could invalidate an unconditional correction-rate necessity | **Corrected** | THEORY 365 and SUPPLEMENT 350 distinguish the three relative-growth cases; SUPPLEMENT 358 and S14 1197–1199 include a floor that ends cultivation below the no-floor rate law and a long dangerous transient. The no-floor necessity is now explicitly conditional. |
| Equal incidence was treated as necessary for keeping a common constraint | **Corrected** | THEORY 219 and 627; SUPPLEMENT 612, 859–860 separate within-type sanctions from among-complier neutrality. The across-type counterexample is retained. SA-06 concerns a remaining weak-versus-strict boundary wording problem, not a reopening of the incidence correction. |
| The delegation equilibrium classification omitted `p=1` | **Corrected** | THEORY 605 and SUPPLEMENT 580–584 impose `p=1` on the complementary-delegation result and give the `p<1` example with only an intermediate number of delegators. |
| Full-row certification was treated as necessary for absence of capture | **Corrected** | THEORY 404 and 655; SUPPLEMENT 399; S14 1204 explicitly identify sufficiency and give a row-sum-two low-seed counterexample. SA-09 is a distinct equality case in the maximal-core stability statement. |
| Test M blurred a successful remedy with refutation of the capture mechanism | **Corrected in the registered interpretation** | TESTS 131 now distinguishes present institutions working, the proposed mandates working, and the mandates failing their stress test; it sends mechanism discrimination to Test B rather than treating remedy success as mechanism failure. Actual row-gain identification and causal evaluation remain research work. SA-04 identifies a separate problem in that delegated Test B discriminator. |
| A fixed opaque-corrector blocking rate was called a summable-risk example | **Corrected** | SUPPLEMENT 645–651 states the exact summability conditions, replaces the example and explicitly withdraws the old claim. |
| Long-run recovery was substituted for transient host viability | **Substantially corrected** | THEORY 983 and SUPPLEMENT 953–961 introduce an explicit fixed-control transient margin and separate the forgiving and threshold hosts. SA-05 asks that the constant-effective-margin assumption be stated in the theorem, not that these calculations be removed. |
| Capture eventually was treated as capture before evidence | **Corrected** | THEORY 420–427 requires the threshold during the alarm band or the ordering of the two clocks; SUPPLEMENT 411–413 demonstrates both orderings. |

## Open issues correctly disclosed, not new defects

These matters remain substantial research needs, but the reviewed version marks them sufficiently explicitly that they should not be counted as newly discovered errors:

1. No estimated structural loop gain and no calibrated whole-field capture model.
2. Several coupled domains with endogenous capacity, moving carrier shares and strategic responses are not jointly solved.
3. Correction rate, human capacity, contestable coverage, detection and effective sanction are distinct quantities; several mappings are assumed rather than derived.
4. The rate-law necessity applies to tracking capacity, not every gradual-selection mechanism.
5. The four scissors arms are not jointly established empirically; C0 is a real conjecture, not another numerical identity.
6. Correctable kernels, stochastic viability under disturbances and multi-host thresholds are not computed.
7. The generative order's attraction, funding equilibrium, free-rider control and durable coverage are not proved by the mechanism list.
8. The common-frontier calculation fixes pooled effort; it does not solve individually chosen contributions.
9. Masking and evaluation awareness evidence comes from constructed settings; the capability dependence of detection remains C12.
10. The institution-level magnitudes of dwell, human-capacity loss and recovery are conjectural. Numerical time units are not estimates of institutional years.

The next joint model with the greatest payoff for this track would connect endogenous selection of conversion capacity, multiple corrector domains, effective liability and the host while preserving a viable transient. The manuscript identifies much of this agenda already. For readiness, the priority is more concrete: write one full decision protocol for one measurable dimension, including its unsafe set, tolerance band, sampling model, residence requirement and error horizon, then establish its actual guarantee.

## Reproducibility and coverage limits

Independent code: [audit_systems.py](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/systems-audit/audit_systems.py). Output: [results.json](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/systems-audit/results.json).

The script uses only Python's standard library and imports no manuscript functions. It verifies the multitype participation counterexample, the gain-one field boundary, the dependence of host viability on the liability path, the endpoint-versus-threshold readiness discrepancy, and the closed-form relative-payoff and oversight examples. ODE cases use an independent RK4 implementation; the participation and liability cases are repeated at half the time step. The readiness calculation uses the exact Gaussian likelihood ratio and 20,000 runs at each of four means. These checks establish the reported counterexamples, not the universality of a replacement model.

The root reviewer reports that the full default suite passed all 188 assertions in approximately 315 seconds, manuscript input hashes were unchanged, and an isolated build reproduced the artifacts exactly. This review does not claim a separate rerun of that full suite. It inspects relevant implementations to explain why passing checks do not address the counterexamples. It does not independently validate every cited empirical paper, every legacy numerical block or the manuscript's Chinese/corpus fidelity; those are separate review tracks. The new findings concern the current assembled version, with stable keys supplied where available.
