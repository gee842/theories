# Independent review: consequence-coupled reconstruction of regulation

6 October 2026. Internal collaborating-AI review for Ren's [accepted derivation path](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#accepted-work-sequence). The original checkpoint below is an analytical audit of [the new mathematical construction](ENDOGENOUS-REGULATION-MATH.md), with separate exact rational arithmetic. A subsequent executable audit is recorded at the end. Neither is external peer review or empirical validation; Lean verification has its own [scope record](ENDOGENOUS-REGULATION-LEAN.md).

**Finding at the analytical checkpoint:** the declared reaction law supplies a noncircular conditional route from damaged capture sites to paid formation of an initially absent regulator, repair, renewed fuel capture, and additional copying of that regulator. The positive-loss finite-horizon copying-gain theorem is correct under its stated assumptions. At that checkpoint the construction advanced the first acceptance gate without completing its intervention checks or deriving adaptive selection among competing responses. The updated gate assessment appears below.

## What was checked

Read the repository entrypoints, governing acceptance gate, original failed-regulator comparison and response diagnosis, allocation-control result, new mathematical note and [empirical-interface audit](ENDOGENOUS-REGULATION-EVIDENCE.md). The old negative regulator findings remain unchanged. A responsive mechanism can consume the resources needed for continuation; a useful constant inhibitor does not establish a benefit of responsive switching. These lessons remain applicable here.

The new event propensities use the actual counts C, D, P, G, F and E. No observer's success measure, fitness label or terminal assay enters the transition law. Damage D acts directly as a catalyst for paid formation; there is no separately manufactured sensor in this construction. The response chemistry, capture scaffold and copying specificity are supplied laws. The appropriate claim is formation of a repair-and-copying suborganization within that scaffold, not the origin of the entire organization or of its reaction repertoire.

Each formation, repair, copy or leakage event consumes one F. Capture exchanges one E for one F. The event-by-event ledger

\[
F_t+E_t+A_t+R_t+K_t+L_t=F_0+E_0
\]

is therefore exact, as are C+D=N and P+G=M. In particular K never exceeds the total initially accessible and incident support. The separate capacity B is a declared saturation law: capture is disabled at F=B. It is not an approximation whose effects disappear merely because E is finite. The proof's paths respect B=2.

## Audit of the positive-loss theorem

For N=1, M=3, F₀=E₀=2, C₀=G₀=0 and unit productive rates, the zero-loss process first fabricates G at rate 6. The next race has rates 2 for further fabrication, 2 for copying and 1 for repair. The resulting terminal expected copy counts are 4/5 for active repair, 1/2 with repair disabled, and 2/5 for equally paid ineffective repair. The disabled arm saves the repair expense, making its comparison a substantive cost-inclusive one.

The finite-horizon lower bound uses two disjoint paths. Fabrication followed by copying has branch probability 2/5 and waiting rates 6,5. Fabrication, repair, capture, copy, capture, copy has branch probability 2/15 and waiting rates 6,5,2,3,1,2. The factor 2/3 in the latter branch chooses copying before the competing second capture. Requiring each wait to be at most two units fits the six-event path within H=12. Each copy on this path spends genuinely newly captured fuel; formation and repair have already consumed the two initial fuel units.

Using e²>7, the note's rational lower bound is exactly

\[
L=\frac{35259954180435648}{56994475926865715}>\frac35.
\]

With α=δ=ℓ=1/10000, the combined damage, wear and leakage intensity is at most 6ε. Coupling each positive-loss process to its own zero-loss reference until the first such event gives failure probability at most 6εH. The pathwise bound 0≤K≤4 makes the expectation perturbation at most 4·6εH per arm. Subtracting both perturbations from the reference gap gives

\[
\mathbb E_A K_{12}-\mathbb E_0 K_{12}
>\frac1{10}-2\cdot4\cdot6\cdot\frac1{10000}\cdot12
=\frac{53}{1250}.
\]

No missing competing event, resource reset, or probability-factor error was found in this argument. The coupling bound is conservative and requires no claim about typical trajectories or empirical rate plausibility.

The exact rational arithmetic was independently reproduced with Python's standard-library `Fraction`, without importing a producer program:

```python
from fractions import Fraction as Q
from math import prod

L = Q(2, 5) * prod(1 - Q(1, 7**q) for q in (6, 5))
L += Q(4, 15) * prod(1 - Q(1, 7**q) for q in (6, 5, 2, 3, 1, 2))
assert L == Q(35259954180435648, 56994475926865715)
assert L > Q(3, 5)
assert Q(1, 10) - 2 * 4 * 6 * Q(1, 10000) * 12 == Q(53, 1250)
```

These checks certify the displayed arithmetic; the analytical reasoning above establishes its relation to the stated process. They do not constitute a machine-checked general theorem.

## Adverse cases are essential parts of the result

The bootstrap obstruction is correct: with every capture site damaged, no initial regulator and fewer than two usable fuel units, fabrication cannot be followed by repair. Arbitrarily much uncaptured E does not repair that deficiency.

The zero-loss source-removal comparison also checks: E₀=0 makes active repair's expected copy count 2/5, below the repair-disabled arm's 1/2. The same chemistry can therefore impose a copying burden when its repaired dependency provides no support. This is a copying comparison; it is not evidence that either arm continues to capture without a source.

Finite support and positive damage, wear and leakage prevent indefinite active renewal. The ledger permits only finitely many births and repairs; after those, remaining intact sites and regulators disappear almost surely. A finite-horizon copying gain cannot be promoted to perpetual persistence.

## Why this does not yet derive selection of useful responses

Consequence-coupled reconstruction is stronger than passive persistence: the response can help recreate fuel needed to make further copies. It remains weaker than learning to discriminate between competing responses. A dead response can also copy using inherited fuel, and useful repair can subsidize a competitor sharing the fuel pool.

An exact counterexample makes the missing connection explicit. Introduce active and inactive variants with counts a and h. During a contest with no new untemplated formation, give both the same per-capita copying rate βPF and wear rate δ. Only the active variant repairs capture sites. While a,h>0, set n=a+h and p=a/n. At a copying event,

\[
p\frac{a+1}{n+1}+(1-p)\frac{a}{n+1}=p;
\]

at a wear event,

\[
p\frac{a-1}{n-1}+(1-p)\frac{a}{n-1}=p.
\]

Repair and capture do not change p. Thus the generator of p is zero in the interior, and its bounded process stopped when either variant disappears is a martingale. Changes in fuel alter common event rates without generating an expected frequency advantage for the useful variant. This is a consequence of the declared shared-pool symmetry, not a universal impossibility of adaptive selection. Unequal wear, local association, compartmentalization or other asymmetric return routes could change it, but must be explained and tested rather than silently installed.

## Acceptance at the analytical checkpoint

**Accepted:** a paid, initially absent response can alter its own material reconstruction through the dependency it repairs; the stated positive-loss gain, source-dependent reversal and bootstrap obstruction follow from one explicit law. The ledger and actual-successor path prevent an external reward or free restart from supplying the effect.

**At the analytical checkpoint, still open:** an independently checked finite-process implementation; signal disruption and restoration; appropriate constitutive and open-loop comparisons; actual successor-state intervention tests; empirical identification; selection among alternative response variants; and formation or revision of the supplied sensing, repair and copying architecture. Copy removal alone is not removal of all reconstruction, because damage-coupled fabrication remains. Copy counts, remaining G, fresh captures and site condition must be kept separate.

The next connected result should test how useful and useless responses share or differentially receive the consequences they produce, with explicit costs and actual inherited states. That would replace a further supplied premise on the route toward learning. This analytical construction does not yet supply the teaching signals, shared representations or evaluative architecture assumed by the downstream concern results.

## Subsequent executable audit

The [independent checker](../../../../experiments/shared-renewal-capability/regulation/retention/independent_check.py) now audits the producer's [protocol and implementation](../../../../experiments/shared-renewal-capability/regulation/retention/PROTOCOL.md). It does not import the producer. It constructs C,D,P,G,F,E reactions from a separate stoichiometric table, multiplies reactant counts directly, and computes exact terminal expectations by ascending-rank dynamic programming. Its [saved record](../../../../experiments/shared-renewal-capability/regulation/retention/independent-check.json) pins producer sources, results and checker bytes by SHA-256.

All 21 declared cases passed, including active, absent formation, absent repair, equally paid ineffective repair, absent capture, incident support burned without usable capture, absent copying, wrong cue and constitutive formation. The independent inventory audit checks 1,272 state/configuration instances and 3,644 positive event channels, including physically admissible states unreachable from the tested preparation. Material and support ledgers, nonnegative successors, the storage guard, the original generator drifts and exact eventwise rank drops all pass. Burned incident support receives its own debit and is not counted as usable capture. Every case's exact terminal event counts and state expectations agree with the producer, including positive-loss laws.

The stronger rank is

\[
V=4E+2F+C+G.
\]

It decreases by one on damage, formation, effective repair, copying and wear; by two on capture, leakage and ineffective repair; and by four on burned capture. Thus the full process is a finite directed acyclic graph, including positive losses and these control laws. This licenses the independent exact calculation; virtual uniformization self-loops are not additional physical events.

Separate floating-point uniformization reproduces all finite-horizon event expectations, endpoint coordinates and intact-site occupation, plus five actual-successor intervention sequences. It uses short numerical subintervals while retaining the whole successor distribution. The maximum distance from the producer's reported intervals is **4.086×10⁻¹⁴**, below the prespecified **10⁻¹⁰** comparison tolerance. Maximum primary-case probability-mass error is **4.45×10⁻¹⁵**. The checker records Poisson-tail estimates separately from floating-point error; this agreement is not a second rigorous enclosure certificate.

Read-only examination of the producer's interval arithmetic found no error in its nonnegative outward-rounded operations, rational Taylor enclosure of the exponential, geometric Poisson-tail enclosure, event-count tail budget or occupation-time tail bound. For occupation, the omitted uniformization reward is bounded using H·Pr(Poisson(λH)≥n), multiplied by N. Propagating an interval distribution preserves all actual successor states; the true-mass-one contract comes from the preceding probability enclosure. The dependent reward/state intervals need not be independent because only positive linear operations are applied. This is an implementation audit, not a formal proof of Python or Decimal semantics.

### Outcomes and their distinct meanings

At the main preparation and H=12, active repair yields approximately 0.799827 expected copies, versus 0.499958 with repair disabled and 0.399971 with equally paid ineffective repair. It also yields approximately 0.399928 usable captures, whereas those two comparators capture none. The positive-loss source-absent comparison reverses the copying advantage, approximately 0.399971 versus 0.499958. The exact adverse certificate, >153/2500, was independently checked as well as the original >53/1250 gain certificate.

**Copying itself has a continuation cost.** Removing copying increases expected usable captures to approximately 0.666537 and intact-site occupation to 3.832084, compared with 0.399928 and 2.325206 in the active arm. Thus the demonstrated copying gain is not a global improvement across the declared outputs. The result explains a conditional material-return loop, including competition between keeping sites productive and replicating the response.

Capture interruption followed by restoration is computed from the actual distribution remaining after four units of disruption, then evolved for eight more; resources and wear are retained. It restores expected copying to approximately 1.996527 from the post-repair preparation, below uninterrupted access's 1.999440 and above continued disruption's zero. Cue restoration is separately checked from its actual depleted preparation. These are model interventions, not observed biological recoveries.

The seven original event guards and state updates in [Retention.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formal/Retention.lean) agree with the positive-channel reactant and capacity conditions inspected here. Its discrete law does not encode mass-action rates or the control modifications. The separately recorded Lean result therefore supports trace accounting and root composition, while the numerical gain statements retain their analytical and implementation-level provenance. This review does not claim a machine-checked refinement from Python to Lean.

Reproduce the independent audit from the repository root with `python3 experiments/shared-renewal-capability/regulation/retention/independent_check.py`. It overwrites only its own result record and checks that the producer sources and results remain unchanged during execution.

**Updated gate assessment:** the first gate's conditional causal-loop milestone is now met for this declared law. The organization and continuation task are specified independently of G; G begins absent; sensing is the actual damaged-site encounter; formation, repair, copying and replacement consume accounted fuel; and intervention sequences retain actual successors. Dependency and cue disruption/restoration, response and copying ablations, equally paid ineffective repair and constitutive formation have been checked. Both success and failure conditions are established. No analyst score enters the dynamics.

This assessment follows the written gate's allowance for declared physical laws and formation mechanisms. It does not add architecture origin, adaptive selection or universal empirical validity as prerequisites that the conditional gate did not require. Stochastic event variation and available fabrication/copying reactions are explicit; variation among competing response types is the next connected problem. The [paid-association analysis](CONSEQUENCE-RETENTION-SELECTION.md) provides an explicit route from shared-pool neutrality toward differentiated consequence return, followed by the still-open question of changing selectors. This executable audit does not test that larger law.

The wider regulation-to-learning derivation and unified foundation remain ongoing. Adaptive discrimination under changing conditions, formation of the supplied architecture, empirical identification and revision of selectors retain their own obligations. Meeting this conditional first gate does not automatically supply the teaching signals, shared representations or evaluative architecture of the downstream concern results.
