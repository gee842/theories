# Recurrent revision, regulation and accounted support

6 October 2026. AI-authored continuation following [Ren’s request](../../../../sources/15-codex-theory-conversations/2026-10-06-systems-complexity-chaos-integration.md#completing-the-proposed-next-connection). This completes priority 1 of the [coverage audit](SYSTEMS-HIGHER-DYNAMICS.md) at the local mathematical and mechanism scope below, under the [shared method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). The fresh combined build passes **58 new theorem audits**, with 143 inherited audits counted separately. [Independent review](VARYING-DYNAMICS-REVIEW.md) and the [proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/adaptive-verification.json) support this scope.

## Named connection and preserved target

The transition is **actual consequences → acquired record → changed effective gain → further delayed response**, with the observation, update and operation consuming support in the same history. The existing family is retained:

\[
s_{t+1}=A(k_t)s_t,\qquad A(k)(x,y)=(x-ky,x).
\]

The paired state retains the memory responsible for the original delay result. Replacing it by immediate correction would change the target. A boundary that omits gain, acquired observation or support would also omit causes of later enabled actions. The model therefore differentiates these within one evolving configuration; it does not start with independently existing controller and controlled worlds.

The earlier concern learner, updater formation and inquiry-revision results remain established at their scopes. This construction is a new explicit local realization of recurrent regulation using the same delayed law and existing trace/accounting interfaces. It does not claim an executed handoff from the concern learner or formation of its already installed observation and revision capacities.

## Mathematical results

Use the common envelope

\[
V(x,y)=\max\{|x|,|y|,|x-y|\}.
\]

1. For every actual sequence with gains in \([0,1]\), \(V(s_t)\le V(s_0)\). This is uniform stability; the gain may depend on state or history, need not change slowly and need not itself converge.
2. For \(0<\delta\le1/2\), gains in \([\delta,1-\delta]\) imply
   \[
   V(s_{t+3})\le(1-\delta)V(s_t),\qquad
   V(s_t)\le(1-\delta)^{\lfloor t/3\rfloor}V(s_0).
   \]
   The actual envelope and squared Euclidean norm tend to zero. The finite-prefix version needs the margin only at indices before the endpoint. This avoids silently assuming infinite resources when applying the bound to a paid finite run.
3. Frozen convergence alone does not imply convergence of the varying composition. For \(k_t=2^{-(t+2)}\), \(s_0=(1,1)\), the actual coordinates satisfy
   \[
   \tfrac12+2^{-(t+1)}\le(s_t)_i\le1.
   \]
   Lean derives the finite sum and bounds inductively from the actual trajectory. Every fixed member separately converges, while this changing trajectory stays away from zero. This is a failure of attraction, not unbounded amplification. The common envelope precludes the latter inside \([0,1]\).

The uniform margin is sufficient, not proved necessary for all convergent schedules. Neither the envelope nor squared norm is fuel, welfare or the system’s represented objective. These are independently defined mathematical diagnostics used to prove consequences of a supplied law.

## The actual paid mechanism

The [paid mechanism](VARYING-DYNAMICS-MECHANISM.md) uses gains \(1/4\) and \(3/4\) in the same delayed plant. Operation retains the old first coordinate, reading acquires whether the last response crossed zero, and updating uses that acquired bit to select the next gain. Starting from \((1,1)\) with gain \(3/4\), it reaches \((1/4,1)\), then \((-1/2,1/4)\). The acquired overshoot changes the next gain to \(1/4\), producing \((-9/16,-1/2)\); the next record changes the gain back to \(3/4\). A matched clamped reader has the same first two plant states and bills, but reaches \((-11/16,-1/2)\) on the third operation. Lean proves these differences and the actual paid traces.

Each operation, reading and update costs one unit. A packet contains three support units already present in the joint initial state; operation converts one packet into available fuel. The proof counts this as internal transfer: total support \(F+3P\) decreases by exactly one per event. For positive initial fuel and \(N\le P_0\), a funded prefix is an actual generative trace, its plant projection equals the trajectory used in the varying-gain theorem, and

\[
V(s_N)\le(3/4)^{\lfloor N/3\rfloor}V(s_0),\qquad
3N+F_N+3P_N=F_0+3P_0.
\]

Here \(N\) counts plant operations; each entails three paid events. The support transfer is installed and independent of regulation quality. No analyst’s success measure secretly supplies a reward or renewal process. These are support units in a mathematical account, not an identified thermodynamic law.

The finite support accounting proves that no single infinite execution is admitted. Arbitrarily long funded prefixes require correspondingly large original support, or a separately specified replenishment history. Exhaustion actually blocks further operation. Even misleading readings can select only gains inside the admitted interval, so the clamped-reader comparison establishes causal influence without establishing necessity of truthful reading for stability, optimal selection or greater welfare. Fixed gain within the admitted interval is a simpler stable comparator.

## Proof accounting and verification

| Module | New theorem audits | Checked obligation |
| --- | ---: | --- |
| [VaryingFeedback](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/VaryingFeedback.lean) | 17 | Common-envelope stability, three-step contraction, all-time and finite-prefix bounds, convergence. |
| [ShrinkingGain](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/ShrinkingGain.lean) | 15 | Actual reached lower bounds, frozen convergence and varying nonconvergence. |
| [SupportedRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/SupportedRevision.lean) | 26 | Acquired gain revision, paid traces, exact source balance, projected regulation bound, matched intervention and exhaustion. |

[AdaptiveCore](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/AdaptiveCore.lean) defines the shared trajectory and envelope; it adds no audited theorem. The [new checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_adaptive.py) builds all eleven local modules from frozen source bytes in a fresh directory with Lean 4.30.0-rc2 and the previously pinned Mathlib cache. It checks exact ordered full theorem names, all requested axiom reports, unchanged inputs and the absence of warnings or proof placeholders. It neither installs dependencies nor claims to rebuild upstream Mathlib.

The 143 inherited audits are the previous 104 systems results, 18 selected core results and 21 resource-continuation results. They are not counted as discoveries in this round. The six earlier systems/core sources match their previous analytic receipt hashes. Prior checkers and receipts are preserved; the new [logs](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/adaptive-verification/SupportedRevision.txt) and [frozen sources](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/adaptive-verification/sources/SupportedRevision.lean) use a separate directory. All 58 new proofs have nonempty axiom lists using only some or all of Lean’s standard `propext`, `Classical.choice` and `Quot.sound`. No added custom axioms does not mean that mathematical or physical premises have been eliminated.

## Supplied premises and next connection

The [integration checks](VARYING-DYNAMICS-CHECKS.json), reproducible with [the local checker](VARYING-DYNAMICS-CHECK.py), validate document links and anchors, the frozen proof evidence and preservation of inherited sources/checkers. They do not rerun the mathematics or establish empirical applicability.

The supplied local inputs are the delayed linear law, the zero-deviation target, exact sign observation, two available gains, the installed observation-consuming update rule, the event order and the packet conversion/cost law. The plant changes only during operation; no extra drift during reading or updating is modeled. Event count is not an identified elapsed time. The proofs explain what follows for every admitted history; they do not derive these inputs from a minimal foundation or establish their empirical accuracy.

The substantive addition is that successful individual settings and isolated revision episodes are insufficient evidence for effective continuing regulation. The changing composition and its support must be accounted for together. Conversely, a changing effective regulator can preserve correction under a common dynamical condition; higher-order change need not require an endless hierarchy of independent controllers.

The next connection is acquired consequences changing the inquiry or revision criterion itself while preserving subsequent response and support, coordinated with the active applicability branch. No controller advantage is treated as an ethical standard. The overarching whole-process grounding question concerns the differentiated effects and conditions of realization, impairment and repair; this local stability result does not settle that question.
