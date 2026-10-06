# Reward learning and recipient-directed choice

6 October 2026. AI-authored retrospective empirical contribution to the [generative foundation](GENERATIVE-GROUNDING.md). Numerical reconstruction and bounded scientific/identification claims are accepted in the [separate internal review](../../../_process/research/2026-10-05-concern-theory/reward-association/REVIEW.md). This is collaborating-AI review, not external peer review.

**The primary estimate is uncertain around zero:** congruent reward training is associated with **0.50 percentage points more target-liked selections**, with an approximate 95% confidence interval of **−4.25 to +5.24 points**. All three fixed sensitivity intervals also include zero. This neither establishes equivalence nor rules out learning. It limits the positive behavioral claim this reanalysis can support.

The study addresses one named connection: consequences associated with a represented recipient's state → later action concerning that recipient. It advances the existing empirical-support requirement and constrains interpretation of [acquired evaluative influence](EVALUATIVE-UPTAKE.md). It does not establish ethical justification, creation of concern from zero or the whole unified derivation.

## What was tested and preserved

We reconstruct Experiment 3 of Zhang and Hackel (2025), *Reward Association With Mental States Shapes Empathy and Prosocial Behavior*. The [original paper and public data](../../../sources/32-mental-state-reward-learning-2026-10-06/README.md) are preserved with exact byte hashes. The study varies whether represented favorable target states predict favorable personal outcomes during training, then independently varies which target-directed choices favor personal outcomes in a new set of situations. Transfer concerns the same target. Existing adult capacities and prior evaluation remain supplied.

The article and task describe a previous-participant target and gift-card opportunities. The release establishes displayed instructions, recorded choices and feedback; no identified fulfillment ledger verifies actual recipient gifts or realized personal financial sacrifice. The outcome here is a **recorded target-liked selection**, with its assigned incentive context retained.

The [computational protocol](../../../experiments/recipient-value-learning/PROTOCOL.md) was reviewed and frozen before our new outcome aggregation. Published findings were already known. This is a retrospective reanalysis with a prospectively fixed calculation plan, not a blind replication or preregistration of the original experiment. The original preregistration PDF was inaccessible; its contents are not independently certified here.

Raw reconstruction gives 390 completed post-cutoff surveys, five without usable task identifiers, and **385 matched saved respondents**. The authors' attention and missing-response rules retain **333**, excluding 52. Those post-assignment exclusions prevent an unconditional intention-to-treat claim. The all-saved sensitivity still omits unsaved or noncompleted participants. Both implementations reconcile all **10,532 author-clean answered rows** against original filenames, assignments, trial identities, choices and reaction times. All **12,320 offered decisions** among the 385 matched respondents remain available, including timeouts.

## One fixed primary contrast

For each participant, let `L` be target-liked selections divided by 32 offered opportunities and `R` be all recorded selections divided by 32. A timeout contributes no liked selection and no response; it is not classified as choosing the disliked option. Let `P=1` mean congruent training and `I=1` mean that target-liked choices currently favor personal reward. The primary contrast compares training assignments within each current contingency, with equal weights:

\[
\Delta_L=\tfrac12[(\bar L_{11}-\bar L_{01})+(\bar L_{10}-\bar L_{00})].
\]

| Training | Current private reward favors | Saved → eligible participants | Liked / offered | Responses / offered |
|---|---|---:|---:|---:|
| Congruent | Target-liked choice | 105 → 89 | 84.41% | 99.02% |
| Incongruent | Target-liked choice | 83 → 68 | 84.79% | 98.85% |
| Congruent | Target-disliked choice | 105 → 94 | 53.89% | 98.80% |
| Incongruent | Target-disliked choice | 92 → 82 | 52.52% | 98.67% |

The two within-contingency training differences are **−0.38** and **+1.37** percentage points. Their equal-weight average is **+0.50**. Neither component is selected as a replacement primary result.

| Fixed analysis | Participants | Training contrast, percentage points | Approximate 95% interval |
|---|---:|---:|---:|
| Primary: eligible; 32 offered | 333 | +0.50 | [−4.25, +5.24] |
| All saved matched respondents; 32 offered | 385 | −0.31 | [−4.90, +4.29] |
| Eligible; answered-trial denominator | 333 | +0.34 | [−4.40, +5.09] |
| Eligible; RT ≥ 0.2 seconds; 32 offered | 333 | +1.47 | [−3.47, +6.40] |

Participants, rather than individual trials, are the independent units. The intervals use the four cell variances and Welch–Satterthwaite degrees of freedom. Sensitivity intervals are individually nominal, not simultaneous. These estimates concern the stated observed populations and outcome definitions; selection and missingness assumptions would be needed for broader causal interpretation. [Full numerical results](../../../experiments/recipient-value-learning/results.json) retain cell variability, response rates, counts and exact estimates.

The original personally optimal-choice reversal model asks a related question on a different scale. On our offered-trial scale, personally optimal fraction is `O=L` when `I=1`, and `O=R−L` when `I=0`. Thus

\[
\Delta_{O,\mathrm{unchanged-reversed}}
=\Delta_L-\tfrac12(\bar R_{10}-\bar R_{00}).
\]

Here that optimal-choice contrast is **+0.43 points**. Treating it as exactly +0.50 would erase the response difference. The [derivation](../../../_process/research/2026-10-05-concern-theory/reward-association/IDENTIFICATION.md) preserves the distinction, including the simpler identity on an answered-trial scale. None of these participant-mean differences reproduces the paper's mixed-logistic coefficient; that model was not fitted here.

## What would count as acquired value

Even a precise behavioral transfer would not uniquely identify a changed recipient-value term. Holding the assigned private reward contingency fixed does not hold the participant's subjective expectation fixed. Realized feedback is available; trial-level subjective private-payoff expectations are not independently measured.

The [identification argument](../../../_process/research/2026-10-05-concern-theory/reward-association/IDENTIFICATION.md) gives an explicit counterexample. In an illustrative choice model with predictor `b(H)+w(H)+βe(H)`, a history-dependent increase `γg(H)` in target-directed evaluation `w` can instead be placed in unobserved private-payoff expectation `e` as `γg(H)/β`. With compatible bounds and unchanged response/feedback laws, the two accounts produce identical finite choice histories. This is a mathematical nonidentification result in the stated model class, not a fitted diagnosis of these participants.

Including post-task questionnaires requires a shared conditional reporting law given that task history. Without an independently validated measurement relation to the latent terms, such a pair remains possible. An instrument with a justified distinguishing measurement law could break the equivalence. This reporting-law qualification was made explicit during final review; the original pre-output argument is preserved.

Further evidence could restrict that ambiguity through independently validated expectancy measurements or interventions separating expected personal consequences from target consequences. A chosen learning model would introduce additional assumptions requiring assessment. Post-task contingency awareness cannot supply that identification by selecting a favorable subgroup: it was measured after the choices and is potentially affected by the manipulation and its consequences. This reanalysis reports awareness frequencies only.

The released eligible records contain **145 aware and 188 unaware participants**, with no missing awareness values. The paper's rendered page 16 reports 187 unaware. Removing very fast responses does not reconcile the participant count. This one-person descriptive discrepancy remains unresolved; no coding, exclusion or outcome analysis was changed to erase it.

## One discriminating contrast that would change the account

One unrun randomized contrast would compare **target-benefiting choices for a previously untrained recipient after contingent target-state reward training versus yoked noncontingent training**. Training arms would match reward totals and presented target states. The later choice would use new perceptual materials, explicit and checked recipient-outcome meanings, no repeated distress display to terminate, and the same characterized personal payment for either action. This specifies an empirical discriminator, not a new completed experiment or a frozen implementation protocol.

A positive contrast would support transfer beyond the trained identity and perceptual cues; abstract cue generalization would remain possible. To distinguish changed evaluation from private-payoff expectancy, the test would also need independently justified bounds on subjective payoff expectations and factual competence. The relevant choice-model class, payoff sensitivity and other baseline terms, including demand or attention effects, must be fixed or bounded before outcomes; the observed contrast must exceed what its unchanged-evaluation alternatives permit. Otherwise an arbitrarily sensitive payoff rule or unconstrained baseline can absorb the result. Assigned equal payment or a nonsignificant belief comparison alone does not meet that condition. Holding displayed distress constant excludes termination of that display as the action's reward, but does not identify every possible form of anticipated personal relief.

If the effect survives those stated tests, the account gains evidence for generalized acquired evaluative influence within that model class. If it occurs only for the trained recipient, disappears with characterized expectancy, or remains compatible with the alternatives, the wider interpretation must narrow. A precise null would constrain this transfer route, not all learned concern. Adult capacities, prior concern, possible demand or attention pathways outside the restricted class, durability and ethical warrant still require their own evidence. No such contrast has been executed in this repository.

## Contribution to the unified account

The earlier [conceptual source account](../../../_process/research/2026-10-05-concern-theory/conceptual-evidence.md#7-four-primary-empirical-anchors-with-narrow-claims) recognized this research as relevant to acquired evaluation. The current raw-data analysis narrows what Experiment 3 can establish: its full eligible-sample contrast is uncertain, and behavioral transfer alone does not distinguish acquired recipient value from transferred private expectancy. Other experiments and measures in the paper are outside this reanalysis.

This complements the separate [recipient-harm analysis](RECIPIENT-HARM-AND-ACTION.md). One investigates action involving a physical recipient's harm; the other manipulates reward associations with a represented target. Neither supplies a complete observed history of forming a new justified evaluative ground. Their populations, outcomes and interventions cannot be spliced into one observed mechanism.

The now-accepted [engineered evaluator](EVALUATIVE-UPTAKE.md) constructs paid acquisition from a zero register, retained influence and two selected actions for the same recipient, with matched factual-information controls. Its cross-center transfer recipe, sign and scale remain supplied. This empirical study neither invalidates that conditional construction nor identifies its acquired coefficient in humans. Its next actual-successor and fresh-efficacy connections remain distinct from empirical cross-target transfer. The [ethical application account](EVALUATIVE-APPLICATION.md) still needs independent grounds concerning patient good, acceptable action and authority. No new completion condition is added. The central obligation remains **formed understanding → justified evaluative concern → effective, corrigible action through succession**, with compatible resources and empirical support at the claimed scope. Here progress consists in a reproducible constraint on that bridge, including an uncertain result and an explicit alternative explanation.

The [analysis package](../../../experiments/recipient-value-learning/README.md), [independent numerical receipt](../../../experiments/recipient-value-learning/independent-check.json) and [integration record](../../../_process/research/2026-10-05-concern-theory/reward-association/INTEGRATION.md) separate original observations, computational acceptance, identification and foundational interpretation.
