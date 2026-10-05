# Bounded candidate discovery: implementation design and audit

5 October 2026. Proposed discrete experiment, not run. This review follows the [design audit](situated-frame-experiment-audit.md) and [completed frame-dynamics source](../../../sources/15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md). Parameters below are a concrete starting specification to freeze before production runs, not estimates or an assertion that the predicted intervention works. Preserve the earlier failed predictions and distinguish development runs from subsequent evaluation.

## 1. Make the missing distinction consequential

The target should be discovery of a useful conditional policy, rather than discovery that one of two familiar actions is globally better. Let a case have six independent binary raw attributes, each with probability one half. The institution knows actions A and B. Initially its active policy language contains only constant A or constant B; its ordinary model can estimate their average outcomes but cannot express a context-dependent action.

For the scientist's environment, select two distinct attribute indices and their binary values using a separate environment seed. Let \(\phi_*(X)\) be the conjunction of those two literals. Its probability is one quarter. This predicate and the hazard indicator \(h\in\{0,1\}\) are hidden from the learner. Generate the observed outcome

\[
Y=1-dh\phi_*(X)\mathbf 1[A]-k\mathbf 1[B]+\epsilon,
\qquad d=.8,\quad k=.3,\quad
\epsilon\sim\operatorname{Unif}[-.1,.1].
\]

Higher observed outcome is the shared local purpose. In the hazard-present world, B's effect relative to A is +.5 within the affected context and −.3 outside it. B's population-average effect is −.1, while using B exactly within the affected context improves the average by .125. Thus a learner estimating only global action means can correctly prefer A while missing a beneficial conditional response. When \(h=0\), B only imposes cost.

These are synthetic outcomes without interference or distribution shift. Noise is not a resource. Log actual modeled damage and B's operating expense separately. Shared purposes and no private rents are assumptions; this experiment does not explain the formation or legitimacy of those purposes.

Match initial physical cases, records, constant-A policy, budget, and competence between institutional arms within each world. Couple noise and contexts by case identifier rather than by the number of random draws an arm happens to consume. Hazard-present and absent-hazard worlds need not have equal initial realized outcomes; do not confuse that comparison with matched institutions inside a world.

## 2. Generate proposals without a truth oracle

The generic grammar contains the twelve single-attribute literals and the sixty conjunctions of two distinct literals: 72 predicates. No name or ordering identifies \(\phi_*\). Randomly permute the grammar independently of the environment. A discovery attempt pays to inspect a predeclared batch of twelve previously unexamined predicates and proposes a policy of the form “B when predicate \(\phi\) holds, A otherwise.” All proposed predicates arise through this same operation.

Use an exploratory randomized sample to rank the batch by estimated policy gain. Freeze at most one candidate before validation. The learner receives only observed tuples \((X,A,Y,e)\), with the known assignment probability \(e=P(B)=1/2\), plus its own spending and institutional messages. It must never receive \(h,\phi_*\), counterfactual outcomes, true candidate values, or the scientist's classification of a proposal. No fallback should insert the true predicate when search fails.

A predicate different from \(\phi_*\) is not necessarily a false discovery. A broader group may contain enough affected cases to make B worthwhile, and a narrower group may provide a smaller real improvement. Define a harmful or false-benefit adoption by the adopted policy's actual expected gain being nonpositive. Report exact causal-feature recovery separately. The simulator may calculate both for evaluation after decisions; neither can feed back to the learner.

This is bounded feature construction and policy learning within an analyst-supplied grammar. It is more explicit than the preceding reliable binary transition, but not unrestricted invention or a full formalization of unawareness. Raw covariates being available to a search operator does not mean their relevant interaction was already in the institution's active frame.

## 3. Require independent causal validation

Randomize A/B on fresh cases at a known, bounded-away-from-zero probability. Do not compare treated members of a selected subgroup with unmatched controls from outside that group. Predictive association with a bad outcome is insufficient: the proposed intervention must change the outcome in that context.

For a frozen candidate \(\phi\), an unbiased validation score for its whole-population gain over constant A is

\[
Z_i=\phi(X_i)\left[
\frac{\mathbf1[B_i](Y_i-v_0)}{e}
-\frac{\mathbf1[A_i](Y_i-v_0)}{1-e}
\right],\qquad v_0=1.
\]

The fixed centering constant reduces noise without using unknown truth. Randomization makes its contribution cancel in expectation. Average \(Z_i\) over **all** validation cases, including zeros outside the predicate. Averaging only over the predicate estimates a conditional effect and must not be reported as population gain. This estimator requires consistency, no interference, and assignment independent of potential outcomes conditional on the recorded design; the synthetic process satisfies these assumptions by construction.

A simple finite-sample admission test is available. Publicly declare the outcome envelope \(Y\in[0,1.2]\); then \(Z\in[-2,2]\) under equal randomization. With \(J\) maximum attempts, assign \(\alpha_j=.05/J\) and compute

\[
L_j=\bar Z_j-4\sqrt{\frac{\log(1/\alpha_j)}{2n_j}}.
\]

Admit evidence of positive net operating gain only if \(L_j\) exceeds the predeclared recurring cost of observing the candidate's features and administering the policy. The bound is conservative. For an initial configuration, use six attempts, 1,024 exploratory cases per attempt, and 8,192 fresh validation cases per frozen candidate. Reuse exploratory data only according to the saved search rule. Never reuse validation outcomes for subsequent candidate selection or repeatedly peek at a fixed-sample threshold. Stop after the declared attempt cap or successful adoption.

The union bound controls the probability of accepting any nonbeneficial tested policy at .05 under this design, even when candidates depend on previous independent records. It does not make the power high, identify the exact mechanism, or guarantee positive cumulative return after experimentation costs. If a less conservative normal approximation is used instead, label its coverage approximate and verify calibration; do not inherit the finite-sample claim.

For final scientific evaluation, either enumerate all 64 contexts using simulator truth in a separate evaluator or collect an additional independent evaluation sample. A validation sample that selected the accepted proposal is not an unbiased final assessment of the selected policy. The evaluator's results must remain unavailable to the institution.

## 4. Separate payment, knowledge, standing, and action

Use an explicit finite ledger. Deduct each randomized investigation fee, context-cell retention fee, candidate-construction fee, and policy-administration expense. B's operating expense is already included in \(Y\): do not subtract it twice. Compare cumulative realized outcomes across all trial and deployment cases, then subtract overhead fees. This captures the opportunity cost of trials through their actual assigned actions; it is distinct from the ledger needed to purchase data and analysis. Report both.

Record fees must purchase something operational. For example, outcomes arrive after a fixed one-phase delay, and an attribute-action identifier must be retained until the outcome arrives. If the fee is not paid, the linkage is genuinely unavailable. Rich records can later expire at a declared date or survive a successor transition only if retained. Merely decrementing an account while leaving the full data array accessible does not implement paid memory.

An initial ledger and fixed inquiry allowance suffice for this stage. They are supplied support, not an endogenous explanation of funding. Charge the protected arm for its support and avoid claiming the preceding stock model's attractor has been reproduced. A later experiment can vary the rule that renews this allowance, independently of record retention.

Represent stages with different state variables: researcher candidate and evidence; institutionally admitted evidence; accepted proposal; enactment permission; deployed policy. Admission denial must not erase what the researcher has learned. Authority denial must not erase admitted evidence or the accepted proposal. The minimal implementation arms are:

1. **Full route:** paid records, generic generation, fresh validation, evidence standing, enactment rights.
2. **Record loss:** the same raw encounters occur but contextual linkage is not retained; actors may retain aggregate action-outcome information.
3. **Admission blocked:** the researcher can generate and validate, but its evidence cannot enter the official decision record.
4. **Enactment blocked:** validated evidence and the accepted proposal remain recorded, but the operational rule stays unchanged.
5. **Fixed representation:** paid data access and aggregate learning remain, but the active proposal grammar contains only constant policies.

Run each in both hazard worlds. The first stage can use cloned candidate/evidence histories at the admission and authority branch points to isolate those gates exactly. Their distinct action consequences are implications of the specified gates, not surprising empirical discoveries. End-to-end runs then measure whether the paid search actually produces useful evidence frequently and early enough.

## 5. Freeze failure criteria before the production run

Save the grammar, candidate ordering rule, sample sizes, maximum attempts, expenditure schedule, total deployment horizon, gates, seeds, and outcome summaries before evaluating them. Use separate development seeds to choose an affordable example; report any such tuning. A long deployment horizon can amortize trials, so report a cumulative outcome curve or break-even time as well as one final total.

Required checks are:

- **No truth leakage:** relabeling raw columns with the hidden predicate relabeled accordingly changes only labels; forbidden environment fields are absent from learner state. Altering the evaluator must not alter proposals or actions.
- **Randomization and effect checks:** logged propensities match assignment; policy-value estimates recover analytically known fixed-policy gains across independent runs. Outside the affected context, B prevents no modeled damage and its net effect is −k; verify this and the negative global B effect.
- **Honest testing:** the selected candidate is fixed before fresh validation. Familywise false acceptance in the absent-hazard world is calibrated against the predeclared bound. Do not require every finite run to have zero errors.
- **Real payment and memory:** a depleted budget prevents the relevant operation; deleted linkage cannot be reconstructed through a cached feature matrix. Trial operating cost, overhead, retention, and deployment costs reconcile.
- **Stage-specific failure:** record loss reduces information or expressibility; admission denial leaves researcher evidence intact; enactment denial leaves official accepted knowledge intact. If these checks fail, the purportedly separate mechanisms were conflated.
- **Substantive failure:** useful rules rarely generated, true benefits not validated within budget, intervention too late, or cumulative cost outweighing benefit must be reported as failures or tradeoffs. Success of an oracle does not rescue failure of bounded discovery.

Report generation, validation, admission, acceptance, and deployment rates and delays; actual policy gain; false-benefit adoption; total trial and operating burdens; and cumulative outcome. Do not condition the main comparison on successful discovery, since that discards exactly the institutions the mechanism may fail to help.

Independent search and estimation follow established causal-inference practice; see [Athey and Imbens, *Recursive Partitioning for Heterogeneous Causal Effects*](https://pmc.ncbi.nlm.nih.gov/articles/PMC4941430/) and [Athey and Wager, *Policy Learning with Observational Data*](https://arxiv.org/abs/1702.02896). The present estimator uses simpler known-propensity randomization and does not require a causal forest. The intended contribution is the institutional separation and cost accounting around bounded discovery, not a new treatment-effect estimator or a universal ethical score.
