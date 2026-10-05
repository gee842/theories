# Discriminating reproduction of correction from improved current performance

5 October 2026. Proposed empirical design and a restricted formal rival for the existing synthetic model. No new human experiment has been conducted. The formal comparison below can be computed now; the prospective study requires its own implementation, participants and a protocol fixed before observing its outcomes.

The target mechanism is a particular loop, not “feedback” in general:

\[
\text{consequences of present work}
\longrightarrow\text{maintenance or selection of correction conditions}
\longrightarrow\text{a successor's response to new cases}
\longrightarrow\text{new consequences}.
\]

The relevant correction condition must be named. In the proposed laboratory study it is an institution's selected, usable handoff package of counterexamples and an executable response procedure. In the numerical formation model it includes skilled carriers, inherited practice, retained records and authority to execute. These are related questions, not an already validated common transition kernel.

## 1. A fair restricted rival for the formation kernel

Use the unchanged [formation join](../../gap-resolution/formation-coupled/PROTOCOL.md). Let H be the realized number of harms among n cases in a round, and let T indicate turnover. The feedback model has

\[
\Pr(T=1\mid H,n,s)=.05+.20H/n.
\tag{1}
\]

The restricted rival replaces only this probability by

\[
\Pr_R(T=1\mid H,n,s)=d,\qquad d=.15.
\tag{2}
\]

Keep the same case process, complaints, nomination, candidate-only ratification, execution, training, appointment weights and archival transmission. This is a one-way rival with respect to **harm-to-turnover feedback**, not a wholly nonadaptive institution. Outcomes still produce complaints and can trigger inquiry. Removing every kind of adaptation would create a weaker and less informative comparator.

Fit d only to mean turnover in an execution-blocked calibration regime. In the synthetic model, ordinary action is then always zero, giving mean harm .5 over fresh fair contexts. Q also uses a fair randomized action and has mean harm .5. Hence the exact calibration mean is .05+.20×.5=.15. With real finite calibration data, d would have estimation uncertainty that must be propagated; the analytic synthetic comparison does not have that sampling error.

### Strong but restricted calibration equivalence

In this regime, the two models have the same entire projected path law for `(skill k, installed practice q, turnover T)` from the same initial `(k,q)`.

For every underlying state compatible with `(k,q)`, expected harm per case is .5. Skill before turnover is determined by `(k,q)` and the fixed training gate: skill-1 adaptive T adds a carrier before turnover; other portfolios do not. Conditional on turnover, the next skill and the appointment probabilities depend only on this pre-turnover skill and q. Marginalizing the harm draw therefore gives the same event-labeled transition law with turnover probability .15 in every compatible full state. The projection is strongly lumpable, and induction gives equality of its full path law.

This proof does **not** include complaint, archival progress, nomination, ordinary/inquiry case counts, or their joint histories. Equation (1) correlates harms and complaints with turnover; equation (2) does not. Such correlations can change inquiry timing even while the projected skill/practice law agrees. Claiming a fit to all observable pre-intervention histories would therefore be false. The calibration data available to the fit and the data reserved for discrimination must be stated separately.

### Prespecified numerical discrimination

Two comparisons answer different questions and should both be retained.

**Controlled starting-state comparison.** Initialize both models in the same complete state, including skill, practice, complaint, inquiry counters, frame and ratification. Compare execution enabled versus disabled within each model. Do not let different hidden archives accumulated during calibration masquerade as different responses to an identical state intervention. At a correct installed ordinary-service response, mean harm is .15, making feedback-model mean turnover .08 instead of the rival's .15. At a reversed response, mean harm is .85 and feedback-model turnover is .22. Execution can therefore improve or worsen subsequent retention through a route absent from the rival.

**Prospective whole-system comparison.** Start both models from the same original full state, with two skilled carriers but no installed frame, and the same future interventions and fresh-case distribution. Compare enabled-minus-blocked execution effects on the retained ordinary-service response, skill, future harms and ordinary/inquiry work. This includes endogenous differences in acquisition and preservation, not only the controlled one-step effect. Report the within-model intervention contrast and then the difference between those contrasts. A plain endpoint difference between fitted models is not itself an identified treatment effect.

A direct held-out event diagnostic is also available. At a fixed full state and portfolio, write Z=H/n and let the per-case mean harm be \(\mu\). Independent fresh cases give

\[
\operatorname{Cov}(Z,T\mid s)
=.20\operatorname{Var}(Z\mid s)
=\frac{.20\mu(1-\mu)}n
\tag{3}
\]

under equation (1), while the rival gives zero. In the blocked calibration regime this is .025 for two-case F and .05 for one-case T/Q. Thus joint harm–turnover logs distinguish these specified kernels even when the calibration projection cannot. In real data, a shared severity or workload cause could generate the same association; equation (3) is a model diagnostic, not a license to infer the causal arrow from observational covariance alone.

Finally, clamp turnover to .15 in both models while holding everything else fixed. Their full transition kernels then coincide from a common full starting state. Any feedback-specific difference between execution-restoration effects must disappear under that clamp. This is a structural negative control: it checks that the alleged mechanism is responsible for a computed discrepancy. Its equality is expected by construction and is not empirical corroboration of the turnover law.

All comparisons must retain the formation study's endpoint caveat. A compliant retained ordinary-service response is not a guarantee for randomized inquiry cases or for all prior periods. Harm, burden, service output and retained response remain separate quantities.

## 2. A minimally manipulable empirical version: outcome disclosure and actual handoff

The weakest feasible human intervention is usually not to randomize harmful consequences. It is to randomize whether an independently verified consequence is available **before** a maintenance decision, then separately randomize a specified route by which that decision can reach a successor. This identifies the informational route from outcomes into reproduction. It does not identify physiological harm-induced attrition or every other possible outcome-to-institution route.

Use a benign classification or record-checking task with independently generated ground truth. Establish several independent organizational lineages. A lineage includes a founder team and an assigned successor team that has not performed the founders' cases. The experimental unit is the lineage, not an individual case. A controlled interface records which examples, instructions and permissions cross the handoff; unrecorded communication would violate the intended design.

The founder's task produces independently scored errors D, completed work and delay. Relevant context attributes are available, but the usefulness of an inherited procedure can change across the later held-out cases. The task must include genuine opportunities for erroneous rules and informative counterexamples; making every inherited rule correct would trivialize maintenance. No outcome threshold is altered to make a preferred arm pass.

The following sequence needs only two binary randomized assignments for the primary handoff:

1. **Complete and score the founders' work before either assignment.** Independently record D, including error types and contexts. Define any high-error or low-error strata before randomizing disclosure. Successors are assigned and kept blind to the founders' outcomes.
2. **Randomize A: timely versus delayed access to the same verified outcome report.** A=1 receives the report before allocating maintenance effort; A=0 receives it only after the measured handoff/test. Use the same reporting format and an attention-matched notification, and give neither arm additional maintenance time. The treatment is report timing, not a fabricated success or failure claim.
3. **Make a consequential maintenance choice M.** With the same finite number of work slots, founders choose whether to complete more ordinary cases or create a successor package containing selected counterexamples, their context links, an explanation and a response procedure. They must actually produce it within the slot. Retaining more material can crowd out useful service; it is not a free intervention. Record the allocation, delivered artifact and proposed rule before the second assignment.
4. **Randomize B after the package is sealed.** B=1 gives the successor operative access to the package and its declared response procedure; B=0 supplies a fixed generic orientation of matched delivery time, without that lineage's corrective content. Both arms have the same task time and ordinary permission to challenge an inherited response. Founders do not receive a refund when transfer is disabled. Randomizing after the maintenance choice prevents the realized B assignment from changing that choice.
5. **Execute actual succession at a fixed time.** The founders leave the task. The successor receives only the assigned materials and performs fresh, held-out cases under a prespecified change in the case distribution. Independently score correct responses, types of error, missed deadlines and task completion. Separately record whether the successor follows the inherited rule. Obedience is not used as the definition of correctness.

The B intervention manipulates one **specified package-access condition**, not every latent meaning of corrective capacity. If a teaching session is included, its script, time and information must be part of the package; an informal extra conversation would reopen the supposedly blocked route. A generic orientation cannot be claimed to match all subjective experiences. The estimand is the effect of this concrete access intervention, including its experiential consequences.

A lineage that chooses no corrective package remains in the study; B may then have little effect. Excluding such lineages after A would condition on a mediator. A successor's failure to produce an answer is retained as a task-availability outcome, not silently removed from the accuracy denominator. Missing measurement and an observed absence of output must be distinguished.

## 3. Primary estimands and what they identify

Let \(M_i(a)\) be lineage i's delivered maintenance quantity under disclosure a. Let \(Y_i(a,b)\) be its successor outcome under the two assignments. M and Y may each have several separately reported components. A prespecified primary M component can be the decision to spend a work slot on a delivered package; a primary Y component can be successful response by the deadline on a fixed set of novel diagnostic cases. Error disparities, service sacrificed and burden remain separate outcomes rather than being folded into a universal score.

The first-arrow contrast is

\[
\tau_M=E[M_i(1)-M_i(0)].
\]

Where a substantive prediction concerns unresolved errors, estimate it in a **pre-A** error stratum fixed by D. That is different from restricting to teams that responded to the report or later chose to maintain. A stronger first-arrow prediction can be an interaction between disclosure and pre-assignment error severity: outcome-relevant information should change maintenance differently from a report showing no corresponding problem. Error severity itself was not randomized, so this is effect moderation of disclosure, not an identified causal effect of inducing more errors.

The second-arrow contrasts are

\[
\tau_B(a)=E[Y_i(a,1)-Y_i(a,0)],\qquad a\in\{0,1\}.
\]

They estimate the intention-to-treat consequences of assigning operative handoff access after each disclosure regime, regardless of whether founders elected to create a useful package or successors opened or used it. Log allocated effort, delivered material, accessible content, actual exposure and use separately. Actual receipt or use is not randomized by B and must not define inclusion in its primary contrast. These assignment effects need not be positive: the package may preserve an incorrect frame, overload the successor or reduce inquiry.

A direct test of complementarity is

\[
\Delta=E[Y(1,1)-Y(1,0)-Y(0,1)+Y(0,0)].
\tag{4}
\]

This asks whether the effect of outcome disclosure on future response differs when the handoff route is executable. It is an identified factorial interaction, not automatically a natural indirect effect or a numerical measure of “the whole feedback loop.” Disclosure might affect several package features simultaneously, and an access gate can have effects not captured by a scalar M.

With independent fair assignments at both stages and N initially assigned lineages, an inverse-probability estimate of an arm mean is

\[
\widehat\mu_{ab}=\frac1N\sum_i
\frac{\mathbf1(A_i=a,B_i=b)Y_i}{1/4}.
\]

The corresponding contrasts identify the above assignment effects under consistency, the declared communication boundary, and complete or appropriately handled outcome measurement. If B probabilities depend on recorded pre-B history, use those known conditional probabilities rather than 1/4. The primary denominator remains all initially assigned lineages, not the number of surviving teams, available packages or compliant successors.

Do not infer mediation by fitting `Y ~ A + M` and interpreting the coefficient of M causally. M is post-A and can share unmeasured causes with future response. Stronger mediation interpretations need extra assumptions or an appropriate mechanism experiment; randomizing only the initial treatment does not supply them. This distinction follows established work on [mediation identification](https://imai.fas.harvard.edu/research/files/mediation.pdf) and [experimental designs for causal mechanisms](https://imai.fas.harvard.edu/research/files/Design.pdf).

## 4. Rival predictions and genuine falsifiers

The study should compare several restricted accounts before interpreting a successful arm:

| Account | What it permits | Discriminating prediction or failure |
|---|---|---|
| Fixed institution | Maintenance allocation is a preset schedule, though current workers may learn | Timely report does not alter delivered M. A reliable disclosure effect on M rejects this restriction in the studied domain. |
| One-way maintenance | Better inherited resources can improve successors, but observed outcomes do not alter their reproduction | B can affect Y, while outcome-relevant A does not affect M. A second-arrow result alone supports this account as well as the coupled one. |
| Immediate attention or belief effect | Reports improve current effort without creating a useful transmitted condition | Founder performance may change, but the effect need not survive actual replacement or interact with the specified handoff route. |
| Coupled reproduction | Outcome information changes delivered maintenance, whose executable continuation affects later response | Predict the declared first-arrow response and a future-response effect of B; equation (4) is a sharper, separately stated complementarity hypothesis, not a necessary theorem for every coupled system. |
| Preservation of a bad frame | Greater transfer retains confident errors | More M or B can worsen independently scored Y while raising inherited-rule compliance. This falsifies a blanket beneficial-maintenance claim. |

A null interaction alone does not refute every feedback mechanism: effects can be additive, the package route can be nonbinding, or the study can have insufficient precision. Conversely, two favorable main effects do not by themselves establish the proposed route; the delivered records, temporal order, successor exposure and competing channels must agree with the mechanism. Report interval estimates against prespecified effects of substantive interest, not just whether a p-value crosses a threshold.

An error-free report stratum and cases where the inherited rule is already adequate provide useful limits. A programme that predicts more inquiry is always better should fail when inquiry displaces needed service without adding informative distinctions. The formation reopening example already demonstrates why those negative controls matter.

## 5. Time, succession and spillovers

The primary test uses a fixed handoff time and a fixed post-handoff horizon. Earlier reports have more calendar time to influence allocation; that timing is the treatment, so its duration must be explicit. Do not compare an early intervention's 25 post-treatment rounds to a late intervention's endpoint at the same absolute date and call the exposure equal. Keep current-worker and successor outcomes distinct.

A second complete handoff can be a prespecified extension: measure the successor's consequences, randomize report timing again, let that generation allocate maintenance, then randomize operative access for the next generation. That tests repeated reproduction over a stated horizon. It still does not establish indefinite continuation. Sequential randomized studies require effect definitions that respect treatment history and availability; see [Boruvka and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC6241330/).

Within-lineage interaction is part of the mechanism, so cases and participants are not independent experimental units. For the first test, isolate communications across lineages and randomize at lineage level. If people share correction packets or discuss reports across lineages, either the design must restrict that communication or it must model the exposure network. Such spillover cannot be repaired merely by larger ordinary standard errors. If transfer between teams is itself the target, use a separate two-stage allocation design and distinguish direct, indirect and overall effects, following [Hudgens and Halloran](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/).

The required number of independent lineages cannot be inferred from the number of case responses. A blinded pilot can estimate lineage-level variance and delivery rates for power calculations; the effect sizes of substantive interest must be fixed independently of the final test outcomes. Six or seven laboratory sessions should not be relabeled hundreds of independent organizations. The present note does not claim a powered sample size without those inputs.

## 6. What this would add, and what it would leave open

The numerical rival test establishes whether the theory's chosen feedback link makes a discriminating prediction beyond a model fitted to a specified observational projection. It is internal model discrimination. Its value would disappear if the rival were allowed to use held-out interventions for retuning and then declared defeated by construction.

The prospective handoff experiment can identify a restricted empirical route: verified outcome information changes an actual maintenance decision; operative access to the resulting correction material changes response after replacement. It deliberately tests transmission and renewal rather than measuring only contemporaneous compliance. It does not identify every form of institutional feedback, physical injury-induced turnover, political legitimacy, open-ended goal formation, or an ecology-to-AI transition map.

Neither a useful packet nor a positive average effect resolves the normative question of whose error costs count. The task's independent correctness standard, permitted experimental exposure, service obligations and refusal rights need explicit justification. Report rule compliance, independently scored consequences, unequal burdens and delivered revision capacity separately. Maintaining a harmful rule more reliably is a possible result, not evidence of alignment.

A convincing empirical contribution would therefore retain all three outcomes: a detected loop if the specified arrows and interventions support it, a bounded failure where an arrow is absent or counterproductive, and an explicit description of the cases where a simpler fixed or one-way account predicts equally well. The current work supplies an implementable design and a formal discrimination target; collecting those observations remains necessary before calling the broader mechanism validated.
