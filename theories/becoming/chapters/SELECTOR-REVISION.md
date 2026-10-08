# Costed selector revision through its own consequences

6 October 2026. Research direction: Yongxu Ren. AI-authored construction, exact calculations, Lean development and separate internal review, following [Ren's execution request](../../../sources/15-codex-theory-conversations/2026-10-06-costed-selector-revision-request.md). This advances the [governing derivation](GENERATIVE-GROUNDING.md) from formed responses and differential reconstruction toward changing the mechanisms that select responses.

**Established local result:** under one explicitly supplied law, a continuing compartment can form a selector, use it to select responses, retain it through the material consequences of those responses, and pay to replace its input-to-response mapping after the conditions change. A sharp finite-reserve and finite-horizon bound determines the probability of recovering through this mechanism. A conventional random-restart controller is exactly equivalent; a directed conventional controller does better in the primary comparison. This is a completed conditional study, not a new general class of learning or a historical-priority result.

## The mechanism and its remaining premises

A selector has orientation m∈{0,1} and remaining lifetime ℓ. It maps an observed sensory bit b to response b XOR m. The environment's hidden condition z determines which response actually captures a fuel packet. The selector receives no condition label, reversal notification or future information. A condition change can make the formerly productive cue-response mapping unproductive.

The compartment starts with no selector and a finite reserve. It pays one fuel unit to assemble a selector, with either orientation equally likely. Reading the cue and reconstructing its selected response cost two more units. Actual productive capture supplies four fuel units; one pays for template-preserving renewal of the selector, restoring its lifetime to two. An unsuccessful resource-dependent trial reduces its remaining lifetime. On expiry, resource-dependent reconstruction can produce the other orientation. The old orientation remains physically accessible in its residue, equally available to every controller.

This is replacement of a rule-bearing component **within one continuing compartment**. Resources and source packets continue through every change. There is no population of organizations from which an observer selects survivors, and no numerical success score controls a transition. Failed formation and inability to pay for the next trial remain in the outcome distribution. The source is a finite externally timed packet stream; unused packets spill rather than accumulate for an inactive compartment.

The binary repertoire, sensory transduction, scaffold, recyclable precursor, capture chemistry, return-to-renewal coupling and uniform assembly law remain supplied. Assembly is paid but has no additional whole exposure of latency in the coarse scheduler. The study explains the consequences of those premises and identifies some indispensable costs. It does not derive the origin of the architecture, physical laws, new representations or an open-ended repertoire.

## A sharp recovery boundary

Consider a separately labeled diagnostic immediately after the environment has made the installed mapping unproductive. Let inherited reserve be F, residual lifetime k, trial cost d, assembly cost c, newly assembled lifetime L, and remaining exposures T. Assume the new condition stays fixed, matching trials capture deterministically, and one packet can pay renewal.

If j wrong candidate orientations precede the first useful candidate, the exact **pre-return** expense and exposure count are

\[
C_j=kd+c+d+j(c+Ld),\qquad T_j=k+jL+1.
\]

No later captured packet can pay an earlier trial. First recovery is impossible if F<kd+c+d or T<k+1. Otherwise the number of affordable, timely opportunities to draw the useful orientation is

\[
N=\min\left(1+\left\lfloor\frac{F-(kd+c+d)}{c+Ld}\right\rfloor,
1+\left\lfloor\frac{T-k-1}{L}\right\rfloor\right),
\qquad \Pr(\text{recovery})=1-2^{-N}.
\]

For k=L=2, c=1 and d=2, the first opportunity requires **seven inherited fuel units and three exposures**. Six units cannot recover through this route; seven permit recovery with probability one half if enough exposures remain. Each additional unsuccessful candidate consumes five more units and two exposures. These are exact statements about this architecture, not universal lower bounds for every possible learner. They concern first recovery, not permanent viability.

The [mathematical note](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/SELECTOR-REVISION-MATH.md) gives the derivation, conventional comparison and scope. Lean verifies the sequential payment criterion and cost formulas. The probability calculation is an analytical result with separate exhaustive numerical checks, not a mechanized probability theorem.

## Matched conventional comparisons

The prespecified primary preparation uses nine initial fuel units, twelve packet exposures, an unbiased hidden initial condition and reversal after exposure four. All arms begin without a selector. They share resources, cue information, replacement opportunities, action menu and prices. The directed arm supplies an alternative coupling that assembles the opposite orientation after expiry; it has no extra memory or hidden condition access. Its proposal distribution is the policy being compared, not a secretly improved source or free actuator.

| Controller or intervention | Expected captured packets | Probability of witnessed within-compartment revision | Probability final reserve can fund the next permitted attempt |
|---|---:|---:|---:|
| Material random renewal | 4.5 | 3/8 | 3/8 |
| Conventional random-restart automaton | 4.5 | 3/8 | 3/8 |
| Directed failure feedback | 6 | 1/2 | 1/2 |
| Fixed mapping, resource-dependent reconstruction | 2 | 0 | 0 |
| Outcome-blind resource-dependent renewal intervention | 3.358391 | 0.168304 | 0.212814 |

The revision witness requires capture before the reversal, **resource-dependent assembly changing orientation after it**, then capture using the new orientation. A fixed mapping becoming useful because the environment changes cannot satisfy this witness. All probabilities include histories that fail before the reversal. Final reserve readiness is an accounting diagnostic after the finite packet stream, not a survival guarantee.

The random-restart automaton and material law have the same physical-state transition kernel. Their complete distributions agree, not merely the table's means. The stronger directed controller uses failure information that random assembly discards. It is at least as good in the reported capture/readiness metrics throughout the declared comparison set; that finite finding is not a proof of dominance in every noisy environment. The fixed and outcome-blind arms are ablations, not sufficient conventional benchmarks. Outcome-blind renewal changes the material maintenance coupling and can have different realized maintenance expenses.

The [comparator study](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/SELECTOR-REVISION-COMPARATORS.md) locates the mechanism in established adaptive-feedback, learning-automaton, switching-cost and resource-budget traditions. Neither the elementary budget arithmetic nor the broad idea of consequence-dependent retention is claimed as newly discovered mathematics or a new theory of learning.

## Failures that change the explanation

Two unfavorable findings are essential to the result.

First, with two environmental reversals, a fixed mapping captures **4** packets on average while material random renewal captures **3.75**. An obsolete mapping can become useful again; replacement costs and delay make revision disadvantageous in some histories.

Second, with only three initial fuel units, all capture-gated controllers have zero probability of the revision witness. An initially correct selector captures four packets before reversal but, after paying for its renewals, retains only six fuel units. Its residual lifetime is two, so the exact seven-unit recovery requirement fails. Outcome-blind renewal sometimes skips a renewal payment, preserves enough reserve and changes orientation successfully: its unconditional revision-witness probability is approximately **0.09747**. It captures approximately **2.59082** packets, versus **2** for the capture-gated arms. A coupling that preserves a successful selector can leave too little reserve to replace it later.

Thus more consequence-sensitive upkeep is not an unconditional improvement. Both retention and revision consume the supporting conditions of later activity. Noise, short remaining exposure, repeated wrong reconstruction and unavailable source add further failure routes. No result establishes inevitable improvement or concern for other centers.

## Evidence and connection to the larger derivation

**Subsequent material interface, 6 October 2026:** [a checked staged construction](MATERIAL-SELECTOR-COMPOSITION.md) now supplies actual A/H parts through the earlier formation, repair and local-copy law, then restricts this selector law by resource-dependent component recipes. Its selector projection preserves the operational history, and an exact lift criterion identifies the required inherited part stocks. This advances the composition gap described below at a finite, declared interface. It does not establish unrestricted concurrent chemistry or derive the assembly wiring, packet access and maintenance coupling from the earlier molecules alone.

The [executable study](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/README.md) evaluates **11 declared cases and 55 case-controller combinations** using exact fractions. A separate implementation with a different state representation reproduces all **13 reported metrics** in every arm and checks **85,932** conditional recovery configurations. The source/fuel/expense/waste ledger is preserved through actual successors. These are internal mathematical and computational checks, not empirical observations.

The [Lean package](../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/README.md) verifies **21 new declarations**, including a paid within-compartment revision history, response mapping, resource accounting, inherited selector copying, reversal without resource reset, and deterministic payment thresholds. Its event law uses the existing causal-root trace interface. It does not certify the Python program, noisy/control variants, scheduler probabilities or expected values. The [independent internal review](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/SELECTOR-REVISION-REVIEW.md) states the accepted scope.

This process is a new conditional construction using the common causal and accounting interface. It is **not an exact kinetic extension of the preceding formed-molecule model**. That model does not yet generate the cue-reading, lease-renewal and proposal architecture supplied here. Their physical construction and compatible composition remain a missing interface. Passing both local studies does not by itself close that interface.

The next connection is to make alternative **revision mechanisms**—for example, different proposal or maintenance couplings—costly structures that can form and change through their consequences, rather than install them as separate experimental policies. Their origin must connect to the preceding formation process, with the same retained resources and a competent conventional comparator. Representations of shared effects, generalization, concern and wisdom remain later obligations. This result supplies a bounded instance of changing a selector; it does not complete the governing unified foundation.
