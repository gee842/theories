# Decisions and next test for recursive self modeling

Research decisions, 5 October 2026. This document preserves the first investigation's decisions and proposed experiment. The experiment was subsequently completed in the [continuation report](experiment/report.md), which records the final frozen design, limitations, results, and next questions. The subsequent [correction-access study](correction-access/report.md) is also complete. The blueprint below is retained as historical research context.

## Decisions made in this investigation

1. Use “a constraint applies to each implemented level” separately from “a property is preserved by the map between levels.” Neither formulation licenses an undefined universal invariance claim.
2. Use x as an operational state proxy. Do not identify a scalar with subjective feeling, a confidence estimate with consciousness, or neural recurrence with semantic meta-order.
3. Define a meta-model by its target and correctness conditions. In the example, h estimates the first model's bias. Iteration count alone is not meta-depth.
4. Treat the exact calibration reference as supplied information. It is not probabilistically independent of the target, and it enables a simple direct controller if continuously available.
5. Keep finite descriptions, stored cyclic graphs, successive executions, and simultaneous representational depth separate.
6. Retain empirical disagreements about consciousness theories and report validity. A theoretical framework is not an established neural architecture.
7. Evaluate error, control, confidence, cost, and recoverability separately. Do not combine them into “wisdom” without an explicit normative account.
8. Preserve the source workspace read-only. This task has its own research artifacts and does not coordinate the independent theory chats.

## Formulations rejected or corrected

| Formulation | Reason for rejection or revision |
|---|---|
| Every property survives a move to a meta-level. | Lossy maps, incorrect gain changes, and mistaken bias correction are counterexamples. |
| Every higher model necessarily knows less. | Side information can add target-relevant information; a known correction can improve semantic accuracy at unchanged mutual information. |
| Every act of self-observation necessarily changes its target. | A read-only observer is a valid model. Actual back-action requires evidence or assumptions. |
| A meta-process automatically remains inside every class used for its target. | Arbitrarily restricted classes need not be closed under constructing meta-processes. Applicability requires membership. |
| Positive cost at each level proves a finite maximum depth. | Summable positive costs disprove that argument; specify a lower bound, divergent cumulative costs, or another physical restriction. |
| A finite recursive rule physically completes infinity. | Specification and execution differ. A bound on memory also differs from a bound on runtime. |
| A fixed point is a true or wise reflective equilibrium. | Existence, convergence, truth, and desirability are different claims. |
| Turing or Gödel show that no self-knowledge is possible. | No appropriate target class or success criterion has been mapped; limited exact self-reference is possible. Gödel is not used as a cognitive impossibility argument here. |
| Deeper reflection improves confidence, hence judgment. | The repeated-evidence example has greater confidence and worse calibration. |
| A calibration model beating a biased controller proves that meta-modeling is necessary. | A direct policy with the same reliable channel can be better. Access and implementation must be compared fairly. |
| Affect labeling in the face task is a report of the participant's own feeling. | Corrected after source review: the 2007 task labels external facial expressions; the 2022 task labels one's feelings. |
| Hay and colleagues establish a fixed worst-case stopping deadline. | Their stated assumptions support expected-count bounds and almost-sure stopping, with arbitrarily long finite runs still possible. |
| Causal inclusion or effective control establishes ethical legitimacy. | Neither identifies whose interests or revision rights should count. |

## A concrete synthetic test

The test should identify what causes a performance difference before extending claims to people. Proposed design choices below are explicitly supplied by us. They are not measured properties of cognition, and are not a preregistered human study.

**System and timing.** Use x_(t+1)=.8x_t+u_t+w_t over 60 steps, x_0 drawn from a declared initial distribution, |u_t|≤2. Ordinary observation is y_t=x_t+b_t+ε_t. A calibration observation z_t=x_t+d+η_t is offered at steps 0, 5, 10, and so forth; accessing it costs a specified fee. All policies receive the ordinary observation before deciding whether to acquire calibration, then choose their action. Deliberation latency, if tested, advances the same physical dynamics for every policy; it is not an arbitrary penalty applied only to one arm.

**Development and evaluation.** Freeze all algorithm settings and price weights after development on seeds 0–99. Evaluate on paired seeds 1000–1999 with identical exogenous disturbance draws across policies. The proposed initial noise scales are SD(w)=.05, SD(ε)=.25, SD(η)=.05; initial bias is selected from {−1,0,1}. These are exploratory design values to be frozen before evaluation, not parameters inferred from human data. Evaluate four separate worlds: constant sensor bias with d=0; a sensor-bias sign change at step 30; biased reference d=.25; and a no-bias control. If values are revised during development, preserve the prior specification and label the revision.

**Comparators.** Include an ordinary-observation controller; a controller that uses calibration directly when available; a persistent bias-calibration model; a joint-state estimator maintaining x and b together; a model that audits residuals and adapts its bias-update rate; and repeated reformulation without extra observations. The joint estimator matters because a nested description and an augmented state may implement equivalent arithmetic. Do not presume it is categorically “non-meta.”

**Fair comparisons.** First replay the same observation-access schedule for all arms to isolate the effect of computation. Then permit paid adaptive access under the same per-run budget. Report actual expense, peak memory, operation counts, and time separately; a shared ceiling does not establish equal spending. Match a nested implementation to a flattened implementation with the same sufficient state and update rule as a negative control for claims based only on semantic labels. Charge the audit and stopping policies' own execution overhead.

**Outcomes.** Report mean cumulative x², action effort, prediction error before action, estimated-error calibration, total sensing expense, computation expense, maximum absolute x, and time to recover after the bias switch. State any combined loss weights in advance and retain the separate components. For a probabilistic event such as |x_(t+1)|>.5, record a forecast before intervention and score it against the action-conditioned outcome law; otherwise intervention-induced agreement may be misread as knowledge.

**Decision rule.** The primary within-world comparison is the persistent calibration model versus the best frozen simpler comparator at matched information access. Estimate paired loss differences across held-out seeds and their uncertainty. A predeclared target for practical improvement should exceed both zero and a chosen resource-equivalent margin. The sign and margin are research choices, not moral facts. Do not choose the winning world after observing results and report it as a universal benefit.

**Discriminating outcomes.** If calibration wins only because it buys more data, attribute the benefit to information acquisition. If a joint-state estimator matches it, retain the functional result but reject the claim that a unique hierarchy is necessary. If extra auditing helps after a bias change but harms the no-bias case through cost, report both. If a reference bias contaminates every calibration-based arm, the result identifies a shared epistemic dependency. If repeated reformulation improves a bounded algorithm, investigate its computational mechanism rather than assuming it acquired new information.

**Exact controls before the larger run.** Reproduce the current noiseless equilibria, the gain-instability example, and the fair-bit complementarity calculation. Those controls are already checked here. An additional meta-model must forecast or estimate an identifiable property of a lower model; otherwise the assigned depth label is not operationally grounded.

## Unresolved questions

- What observations could distinguish genuinely nested representational roles from a behaviorally equivalent flat state estimator in an actual organism?
- How should a self-report be evaluated when observation changes the experience and no independent measurement of that experience is available?
- Which compressions preserve the ability to revise the frame, rather than only improve estimates inside it?
- How can a system calibrate its stopping policy under changed conditions without making unrestricted further reflection a prerequisite for every action?
- Which physical costs bound human active recursive depth, and how do reuse and external supports change them?
- Can correction capacity remain recoverable when its own funding, memory, and standing are selected by the policies it evaluates?
- How should plural purposes and rights to contest a model enter the test without being reduced to a single supplied score?

The next experiment addresses the first layer of these questions: functional benefit under declared access, timing, and cost. It will not settle experience, ethical legitimacy, or universal completeness.
