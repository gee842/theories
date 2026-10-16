# The probability law of an actual paid prediction exposure

6 October 2026. AI-authored mathematical interface study under the [generative-foundation goal](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md). **Accepted after the fresh formal build, independent executable comparison and final independent review.** The named connection is the installed predictor's actual, possibly unsuccessful exposure → its retained state and account → the next exposure. This advances compatible composition; it does not derive evaluative concern or replace the central understanding-to-concern work.

## 1. Why this is a concrete missing interface

The [earlier protocol proof](../../../../theories/becoming/chapters/PREDICTION-PROTOCOL.md) establishes exact completed four-event trials of the deterministic payable-write law. Its source explicitly excludes stochastic outages, skipped writes and reconstruction. The [numerical predictor](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/model.py) implements a broader `advance` operation.

These two laws are not globally equivalent. An executable exposure receives one scheduled packet whether or not its circuit works; an uncaptured packet is lost. An unpaid write can return a continuing predictor with changed leases and last action. Unaffordable rent destroys specified predictor fields. A later exposure can rebuild equipment. The older physical trial instead stops before an unaffordable write and does not consume an unused packet when work never occurs.

The correct obligation is therefore to formalize the existing executable exposure, preserve its full probability mass and identify the exact overlap with the old completed-trial law. Reclassifying every noncompleted trial as an absorbing failure would change the executable mechanism.

The general mathematics is already present in [repeated-renewal composition](../../../history/2026-10-05-support-and-shared-generativity/completion/REPEATED-RENEWAL-COMPOSITION.md), §§2–3, and [formal specification](../../../../theories/becoming/chapters/FORMAL-SPECIFICATION.md), P1–P2. This study supplies a concrete formal/executable boundary, rather than claiming a new probability principle.

## 2. The operational state and the declared experiment

Let the operational state retain fuel, installed gate kind, gate lifetime, construction stage, circuit lifetime, score, previous action and whether a write has occurred. The underlying Python state additionally retains historical diagnostic fields. Those fields affect reported learning witnesses, not gate assembly, construction, issued action, capture, writing or their next operational state. Any claimed projection must establish this restricted independence; dropping fields merely because they look historical would be insufficient.

An exposure has fixed parameters, a declared controller arm, a physical regime and an availability law. The arm determines its installed assembly and decoding choices. The controller reads its installed hardware, score, previous action and acquired receipt; the regime determines physical capture. The external `after` marker belongs to diagnostic accounting, not the controller's information. A schedule of regimes is a supplied environment history and must be carried unchanged across the compared executions.

Source correspondence uses the Python law's positive tariffs, lifetime and packet restrictions, bounded scores and coherent gate encodings. In particular, a live gate must have kind zero or one; the absent-gate code is not a third live updater. Algebraic accounting lemmas may hold under weaker hypotheses, but that does not enlarge the domain of the executable correspondence.

The local law gives one packet to every exposure. For a finite sequence of length n, the environment must actually supply n such packets, or an augmented source bank must have at least that many. The local account does not generate its own source or grant infinite provision. Choosing a horizon does not establish indefinite renewal.

## 3. A finite weighted realization of the actual branching law

Write availability as k/N, where N is positive and 0 ≤ k ≤ N. Use a random tape (g,b,v) of three Boolean entries. The first selects a gate kind when that assembly is enabled, the second selects the prior action when a base is constructed, and the third selects availability. Give each tape weight

\[
w(g,b,v)=\begin{cases}k,&v=1,\\N-k,&v=0.\end{cases}
\]

The four gate/prior pairs make the total weight 4N. Each tape is executed by the same staged arithmetic operation. If an assembly stage is skipped, or an arm fixes its gate kind, its unused tape entry has no effect. Both values still contribute their weight. Capture occurs only when the issued action matches the physical regime and v=1. If the action is wrong, the two availability values lead to the same failed receipt and their weights add.

For an output o containing the operational successor and retained cost/outcome marks, define

\[
K(s,o)=\frac{1}{4N}\sum_{(g,b,v):F(s,g,b,v)=o}w(g,b,v).
\]

This is the unconditional exposure law. The normalization includes absent equipment, unaffordable rent, paid rent without work, productive work, failed work, paid writing and skipped writing. Equal output atoms are added, not treated as independent observations. Zero-weight tapes may be retained algebraically but contribute no probability.

Padding an unused draw does not add a physical operation, time cost or sensor. It is a representation of the existing finite branch weights. The correspondence would fail if the executable correlated a newly sampled draw with an earlier hidden variable in a way the tape law omitted. The actual parent uses the stated independent branching probabilities; a different sampling law requires another proof.

## 4. Resources and continuation are joint outputs

For every legal exposure branch, the required account is

\[
f'+c+u=f+P,
\]

where f and f' are entry and exit fuel, c is actual expenditure, u is uncaptured packet waste and P is the supplied packet. Construction, retrofit, rent, work, maintenance and writing enter c only when their actual stage is executed. Payment guards precede the return that could fund a later stage. An uncaptured packet contributes P to u even when no work occurs.

For n exposures, summing the branch identities gives

\[
f_n+\sum_{i=1}^{n}(c_i+u_i)=f_0+nP.
\]

This pathwise identity does not imply equal end states or equal useful behavior. It also does not remove the need to prove every prepayment guard. Fuel, leases, stage, score and outcome marks must remain coupled under the same tape history.

For any finite declared schedule, apply each exposure to its actual predecessor output. A length-n tape word has product weight and denominator (4N)^n. Summing over all such words gives total mass one and exactly the iterated finite kernel. The finite composition claim is about that inherited state law, including failed attempts. It does not draw a fresh regime, restore entry fuel, recreate a correct score or restart a failed assembly unless the installed next exposure actually does so.

Success probabilities are event sums over this complete measure. Conditional-on-completion probabilities can be computed separately, with the conditioning event and its mass stated. They cannot replace the unconditional measure at the next boundary.

## 5. A skipped write can precede productive use and a later write

Consider the parent parameter law with write cost six, fuel eight, a live fast gate and predictor, score zero, previous action zero, and a fixed regime zero. Let availability be one half. Choose full initial lifetimes, so both first-step outcomes retain enough lifetime for the second attempt. All other costs have the parent's primary values: rent one, work three, packet ten and total maintenance two.

If the first exposure captures, its successor fuel is six after writing. If it misses, fuel is four and writing is unaffordable, but the predictor and its score remain available. Both successors can fund the next work charge.

If the first exposure misses and the second captures, the second return funds the six-unit write and leaves fuel two. That history has probability one quarter under the declared law. An abstraction that kills the predictor at the first skipped write removes an actually productive, subsequently writable continuation. The unconditional probability of a second capture is one half; the killed-at-skipped-write construction retains only one quarter. The score is zero throughout this particular history: it demonstrates continued use and a later paid write, not correction of a mistaken record. These numbers follow from the specified two-draw example and are confirmed by the [independent comparison](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/RUNTIME-RESULTS.md) against the unchanged callable and compiled formal exposure evaluator.

The distinction is functional, not merely terminological. A missed write may restrict later learning without eliminating every later action. For the different task of two consecutive paid writes, excluding a history with an unpaid first write is correct. That successful-task subkernel cannot then be reused as the whole physical law when asking about later action or recovery. Which event counts as failure depends on the claimed task; the physical state cannot be erased merely because one task failed.

The four receipt histories have the following analytically specified accounts. C means capture and M means a missed capture; every row still performs both work attempts.

| Receipts | Probability | Fuel after first exposure | Final fuel | Total expenditure | Total waste | Paid writes |
|---|---:|---:|---:|---:|---:|---:|
| C, C | 1/4 | 6 | 4 | 24 | 0 | 2 |
| C, M | 1/4 | 6 | 2 | 16 | 10 | 1 |
| M, C | 1/4 | 4 | 2 | 16 | 10 | 1 |
| M, M | 1/4 | 4 | 0 | 8 | 20 | 0 |

Each row sums to the initial eight units plus two ten-unit packets. The two mixed histories have identical final fuel, total expenditure and total waste, yet different histories of writing and productive action. A downstream claim about when acquired evidence was available therefore needs the relevant history or a sufficient retained summary, rather than those three aggregate accounts alone.

## 6. Where the old completed-trial proof still applies

Restrict to an already installed live predictor and gate, the variable arm, availability true and the older law's enabled rent/work/write/finish cycle. The old admissibility premises supply the packet/maintenance restriction needed for the separate account comparison. Under the explicit parameter and state correspondence, the proved overlap gives the same operational end state, actual worked receipt, separate expenditure and waste, and one-packet debit. Both matched and mismatched commands are included; a failed capture may leave a zero lifetime when the pre-finish guard held. The old state has no written flag: the comparison augments it explicitly, and the actual paid write makes that marker true.

The overlap is proved at those actual guards. In particular, assembly or retrofit within the exposure adds stages absent from the old trial, an outage can change the receipt, skipped writing changes completion semantics, and rent/no-work branches use different packet conventions. The old proof remains valid; its scope must not be enlarged by silently identifying those different cases.

## 7. Accepted evidence and its limits

The accepted [package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/README.md) keeps three checks distinct:

1. Lean verifies the declared arithmetic exposure law, finite weighted composition, every represented history's resource account and the stated overlap with the old physical trial.
2. An independent executable reconstruction checks the unchanged Python callable on the protocol's frozen reachable and boundary cases, preserving joint outcomes and costs. Executing the new Lean evaluator on those same inputs connects formal source and runtime outputs at the tested scope.
3. A separate review checks the mathematical interpretation, omitted fields, actual source identities, failed histories and limits of the finite comparisons.

The [formal receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/verification.json) records a fresh Lean 4.29.1 build across ten modules: **53 new theorem audits and 141 inherited audits**. Every new theorem is audited; the inherited core retains its recorded audit subset. The [final independent review](STOCHASTIC-PREDICTION-REVIEW.md#final-formal-and-combined-acceptance) matched the source, compiler, checker, protocol and log hashes and accepted the semantic scope. The operational exposure/evaluator bytes match the separately accepted runtime comparison. The generic list-composition lemma uses literal equality of complete weighted lists, a sufficient condition for equality of their represented measures; it is not a universal merged-kernel or programming-language refinement theorem.

No finite test constitutes a theorem about arbitrary Python execution. No weighted-kernel theorem supplies warranted recipient concern, calibration in a real system or continued physical support. The bounded result closes an existing implementation gap within the foundation's compatible-composition requirement. The broader empirical, evaluative and justificatory obligations remain unchanged.
