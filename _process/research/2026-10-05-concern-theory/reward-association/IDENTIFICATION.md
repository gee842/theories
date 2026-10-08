# What reward-associated recipient choices can identify

6 October 2026. AI-authored identification argument for a retrospective reanalysis of Experiment 3 in Zhang and Hackel (2025). The original argument was written before our new outcome aggregates, after reading the paper's published results. Its [exact pre-output version](development/IDENTIFICATION-before-reporting-clarification.md) is preserved and remains the object bound by the protocol freeze. Final review added the explicit questionnaire-law qualification below after numerical results were available; no data, estimator or protocol changed. The [prospective calculation protocol](../../../../experiments/recipient-value-learning/PROTOCOL.md) governs the numerical work. This note does not claim a new experiment, a fitted psychological mechanism or ethical justification.

## The connection to the foundation

The existing [conceptual evidence account](../conceptual-evidence.md#7-four-primary-empirical-anchors-with-narrow-claims) identifies this study as evidence about reward association with a represented target's affective state. The current [evaluative-uptake construction](../../../../theories/becoming/chapters/EVALUATIVE-UPTAKE.md) separates recipient knowledge from the practical influence of acquired consequences. These are related questions, but the human study does not hold the observer's subjective reward expectations fixed merely by holding the assigned reward contingency fixed.

Experiment 3 compares two training contingencies and two subsequent instrumental contingencies. During training, target-positive events can predict personal reward or personal loss. During choice, selecting what the target likes can again predict personal reward or loss. The represented target stays the same; the situations change. The experiment therefore tests transfer across situations within a target, not generalization to a new recipient. Adult representations and prior valuations remain present.

The article describes a previous-participant cover story and choices represented as changing the target's gift-card chances. It also describes personal stock points as affecting a stated raffle opportunity. Original task materials can establish what was presented and recorded; they cannot by themselves establish delivery of real recipient goods or realized financial sacrifice. The empirical outcome here is a recorded selection of the target-liked option under those instructions.

## Preserve both the target and the observer's outcomes

Let P=1 denote congruent training and P=0 incongruent training. Let I=1 mean that a target-liked choice has the higher current probability of personal reward, and I=0 that the target-disliked choice does. For each participant define L as target-liked selections divided by 32 offered opportunities and R as all recorded selections divided by 32. A missed opportunity contributes zero to both L and R. It is neither a disliked selection nor a missing value imputed as dislike.

Write l_pi and r_pi for the participant-mean rates in each assignment cell. The primary standardized contrast is

\[
\Delta_L=\tfrac12[(l_{11}-l_{01})+(l_{10}-l_{00})].
\]

It compares training assignments within each fixed current contingency, then gives the two current contingencies equal weight. Both component contrasts must remain visible. A pooled result alone can conceal different behavior when helping and private reward agree or conflict. This is a difference in recorded selections, not an identified coefficient of concern.

The source's personally optimal choice O has a different meaning. On the offered-opportunity scale,

\[
O=L\quad(I=1),\qquad O=R-L\quad(I=0).
\]

Consequently the equally standardized personally-optimal rate for unchanged versus reversed contingencies obeys

\[
\Delta_{O,\mathrm{unchanged-reversed}}
=\Delta_L-\tfrac12(r_{10}-r_{00}).
\]

**Derivation.** Unchanged cells are (P,I)=(1,1) and (0,0); reversed cells are (0,1) and (1,0). Substitute the preceding two identities in one half of their mean-rate difference and collect terms. The response-rate term disappears only when the relevant response contrast is zero. For participant proportions conditional on having responded, O=1−L in the I=0 cells and the simpler equality holds for participants with a nonzero denominator. Neither identity turns a participant-mean risk difference into the paper's mixed-logit coefficient, which uses effect-coded reversal and a different likelihood.

The eligible analyzed sample follows the source's post-assignment completion, missing-trial and attention exclusions. Randomized task assignment does not make this selected sample an intention-to-treat population. The all-saved sensitivity retains excluded records when the needed task histories are available; it still cannot recover unsaved or unobserved participants. Missingness and exclusion must be reported by assignment rather than hidden inside a favorable subgroup.

## Why a training effect would not uniquely identify newly acquired value

Let A_t=1 denote a target-liked selection on a particular trial, and let H contain the stimulus, response and feedback history available to the observer. Suppose, conditional on H and a recorded response, a decision model gives that option probability

\[
\Pr(A_t=1\mid H,\mathrm{response})
=\operatorname{logistic}\{b(H)+w(H)+\beta e(H)\}.
\]

Here w is a target-directed evaluative term and e is the observer's unmeasured expectation of the private payoff difference. This is our illustrative identification model, not a model fitted by the authors. It separates quantities that the choice measure combines.

Let g(H) be a bounded statistic of the earlier training stimuli and feedback, available from the same history in both models. Consider a model with learned evaluation w(H)=w_0+\gamma g(H) and payoff expectation e(H). A second model keeps evaluation fixed at w_0 and uses

\[
e'(H)=e(H)+\gamma g(H)/\beta,\qquad\beta>0.
\]

Their conditional choice probabilities are identical. Neither model reads the experimenter's hidden assignment as an extra sensor: assignment changes the training histories that produce g. If a bounded expectancy scale is required, the construction holds whenever e has sufficient interior slack for that shift; a nonzero finite shift supplies a counterexample to unique identification. Hold their response process and the task's recorded feedback law equal as well. Multiplying the equal conditional laws over the finite task gives the same observable task-history distribution in both models. Access to realized rewards does not observe the participant's expectation or impose a uniquely justified learning rule on it.

**Post-output reporting-law clarification.** To include post-task questionnaires in that equivalence, give the two models the same conditional questionnaire/reporting law given the observable task history. Such a pair is admissible when no independently validated measurement relation to their distinct latent value/expectancy terms has been imposed. The argument does not claim equivalence under every possible validated questionnaire instrument. A justified measurement law could distinguish the two models; its adequacy is an additional empirical question.

This is an observational-equivalence argument about the allowed model class. It does not show that participants used the second model or that valuation never changes. A specified belief-update law, independently validated expectancy measure, or further intervention could restrict the alternatives. Fitting one such law would make that restriction part of the claim; it would not derive it from the behavioral contrast alone. Demand, perseveration and other accounts remain further empirical alternatives.

The contrast at fixed assigned current contingency compares randomized assignments among retained records. Interpreting it as a population causal effect additionally requires appropriate exclusion and missingness assumptions. Even where that interpretation is justified, it is not automatically an equal-knowledge contrast between two acquired values. The engineered evaluator's equal-factual-information contrast remains a distinct conditional construction.

## Awareness, favorable direction and justified use

Awareness is reported after the instrumental choices. Restricting the main comparison to participants who later report awareness can select on a consequence of assignment, choices, memory or common causes. Descriptive awareness strata can be informative, but do not preserve a randomized causal intervention on awareness. Nor does a nonsignificant contrast in another stratum establish equality or absence of learning.

Congruent and incongruent training can associate personal reward with opposite target outcomes. A transfer mechanism capable of learned helping can also support learned harming. Without an unpaired neutral baseline, this contrast does not identify valuation arising from zero. A null or imprecise full-sample result limits claims about reliably moving behavior; it does not establish that the two assignments are equivalent.

The [application account](../../../../theories/becoming/chapters/EVALUATIVE-APPLICATION.md) retains independent patient-good, authority and comparison premises. Recorded preference for a represented target's liked option supplies none of those by itself. The contribution to the unified foundation is an empirically inspectable interface between learning history and later target-directed choice, with the remaining belief/value distinction explicit. It advances the evidence requirement only at that scope.
