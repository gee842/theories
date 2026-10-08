# From internal measurements to teaching: realizability and obstruction

6 October 2026. AI-authored independent mathematical critique for the [accepted derivation sequence](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#accepted-work-sequence). The named connection is **organizational consequences → an accessible internal teaching signal → learned prediction**, examined against the supplied β in the [concern-learning model](../../2026-10-05-concern-theory/learning-formal.md). Sections 1–7 record the analytical checkpoint: necessary interfaces, elementary proofs and counterexamples. Section 8 reviews the subsequently implemented finite construction. Neither scope establishes felt valence, concern or ethical authority.

**Finding:** a physically generated damage or resource signal can replace an unexplained numerical teaching input for a specified prediction task only when its target is identifiable through the process's actual information and update pathways. It cannot, solely by being predicted accurately, supply the sign of an action preference or the shared evaluation architecture assumed by the concern theorem. These are distinguishable causal obligations, not an assertion that they must forever remain external preferences.

## 1. Four different claims about one possible signal

The concern model uses β>0 as intrinsic self teaching for a specified adverse state, learns its predictive coefficient w, and then routes g·w into action evaluation. Its own text declares β's sign and existence, the learning rule and shared routing as supplied. An upstream mechanism can discharge one of those inputs without automatically discharging the others.

| Claim | What must actually be shown |
|---|---|
| Operational significance | A dependency changes an internal state, and that state causally changes a response affecting further activity. The paid regulation result supplies one conditional example. |
| Learned prediction | Experience changes a persistent mechanism's predictions of a specified observable consequence; held-out predictions or appropriate interventions distinguish it from a fixed response or passive stock. |
| Evaluative use | Those predictions alter action comparison or action production with an explicit sign, causal route and accounted costs. Accurate prediction alone does not select that route. |
| Felt valence or ethical reason | A further account connects the physical/evaluative mechanism to experience or to reasons that withstand examination. Neither claim follows merely from calling a variable adverse. |

The physical generation of a target and the physical implementation of learning it are also distinct. A molecule can indicate damage while no update mechanism preserves what was learned; conversely, a predictor can be mathematically defined from an inaccessible target.

## 2. Exact deterministic realizability criterion

Let S be a finite set of admissible physical preparations or histories. Let h:S→O be the information actually available to the proposed teaching mechanism, and let b:S→ℝ be the independently specified target. The observation may contain memory and recorded actions; it must not quietly contain an analyst-only state or counterfactual answer.

**R1 — Fiber criterion.** There exists an exact teacher T:O→ℝ satisfying T(h(s))=b(s) for every s∈S if and only if

\[
h(s)=h(t)\quad\Longrightarrow\quad b(s)=b(t).
\tag{1}
\]

**Proof.** If T exists, equal inputs have equal outputs. Conversely, choose the common value of b on each nonempty h-fiber as T's value; assign any value to an unoccupied observation. Condition (1) makes this assignment well-defined. ∎

This is an exact information interface, not a claim that an organism already possesses the lookup table. It establishes neither discovery, calibration, computational capacity, construction cost nor robustness under an unobserved extension of S. A positive result must still realize the map and its updates through actual processes. A failed criterion locates a missing distinction: additional memory, a new probe or an additional accessible variable is necessary for exact prediction on the stated domain.

This is a numerical-target specialization of the information obstruction in the parallel [conditional learning interface](../../../../theories/becoming/chapters/LEARNING-INTERFACE.md). Its elementary overlap is corroboration, not a separate discovery. The explicit sampling decomposition and concrete source-dependent contrast below add different checks.

If only the sign of a consequential contrast matters, apply the criterion to its sign rather than its full value. Identifying magnitude can require more information than identifying direction. A cue can be useful on one preparation class while failing the criterion on a broader class.

## 3. Noise, the sampling measure and unavoidable error

Specify a finite probability space with sampling measure μ. It describes how actual histories, preparation types and measurement noise enter training or evaluation; it is not silently conditioned on survival or successful repair. Let Y be the target random variable and O the accessible observation. For each observation with positive probability, define

\[
m(o)=\mathbb E_\mu[Y\mid O=o].
\]

**R2 — Prediction decomposition.** For any observation-based real predictor f,

\[
\mathbb E_\mu[(Y-f(O))^2]
=\mathbb E_\mu[\operatorname{Var}_\mu(Y\mid O)]
+\mathbb E_\mu[(m(O)-f(O))^2].
\tag{2}
\]

**Proof.** Expand Y−f(O)=(Y−m(O))+(m(O)−f(O)). The cross term has conditional mean zero given O. The two remaining squared terms give (2). ∎

Consequently the smallest attainable mean-square error for this information is the conditional-variance term. Independent private randomness does not reduce it: condition on O and that randomness and average. With a deterministic target on a full-support finite S, zero minimum error is equivalent to R1. Equality identifies a conditional-mean prediction, not an intrinsic reward, preferred action, consciousness or ethical correctness.

The measure matters. Altering environmental frequencies, censoring failed histories, or weighting descendants instead of preparations can change m without changing the physical meaning of the cue. An empirical mean estimates the stated target only under an appropriate sampling and observation model. Equation (2) remains an identity under a biased measure; that does not make the biased measure the intended causal question.

## 4. A counterexample supplied by the existing reaction law

The [paid-regulation construction](ENDOGENOUS-REGULATION-MATH.md#source-support-changes-the-sign) supplies an exact failure of damage-only intervention valuation. In its zero-loss reference, let N=1,M=3, C=G=0,F=2 and all productive coefficients be one. Compare active repair with repair disabled, retaining all other rules. Let the analyst's target Δ be the difference in expected total copying under those two interventions.

| Preparation | Observed damage D | E[copies, active] | E[copies, repair disabled] | Δ |
|---|---:|---:|---:|---:|
| Two incident support packets, E=2 | 1 | 4/5 | 1/2 | +3/10 |
| No incident support, E=0 | 1 | 2/5 | 1/2 | −1/10 |

These are consequences of the same repair/formation/capture/copy rules; the available incident source differs. If h records only D, the target contrast and even its sign fail R1. No exact function of this damage cue alone gives both answers. A predictor of damage itself can nevertheless be perfectly correct: b=D does satisfy R1. The obstruction concerns promoting that prediction into a context-independent valuation of repair.

For a measure assigning probability p to the first preparation and 1−p to the second, the optimal damage-only prediction is

\[
m(1)=\frac{4p-1}{10},\qquad
\min_f\mathbb E[(\Delta-f(D))^2]
=\frac4{25}p(1-p).
\tag{3}
\]

Its sign changes at p=1/4. At equal mixture p=1/2 the best prediction is 1/10 and unavoidable squared error is 1/25. More observations of the same insufficient cue cannot remove this conditional variability; a changed mixture can reverse which action that predictor favors. Sampling only histories with productive capture would also change the mixture and its interpretation.

The positive-loss finite-horizon theorems in the same study preserve the source-dependent sign reversal under their separately stated bounds. The exact fractions and threshold in (3) belong to the zero-loss reference; they are not silently transferred to those different coefficients.

**Crucially, Δ is an observer's counterfactual contrast here, not a permitted oracle input to a new learner.** Feeding these precomputed values into an update would assume the evaluation mechanism we are trying to explain. A constructive bridge must identify actual measurements, experiments, memory and updates through which a process could learn relevant distinctions, including source access, while paying for them. Copying is this counterexample's declared outcome; it is not a universal welfare measure.

## 5. Prediction does not fix evaluative use

**R3 — Policy underdetermination.** Consider a learner that correctly predicts an independently observed adverse state under each of two available actions. Let its common predictions be q(repair)=0 and q(ignore)=1. Two controllers can contain exactly that predictor, teacher history and update mechanism. One selects an action minimizing q; the other selects one maximizing q, or ignores q and follows an identity gate. They agree on every predictive fact and differ in action.

Both controllers are well-defined physical-policy candidates. Nothing in predictive accuracy alone excludes one. Declaring q an adverse prediction does not implement a coupling that selects minimization. Showing that one coupling is formed or retained through its consequences would be a further mechanism result. The [formed-variant construction](FORMED-VARIANT-SELECTION-INTEGRATION.md) illustrates conditional differential reconstruction, while also showing that its access and copying rules remain supplied.

The same boundary persists for another being: the [concern model's identifiability theorem](../../2026-10-05-concern-theory/learning-formal.md#2-why-self-learning-cannot-force-other-directed-valuation) exhibits shared and identity-gated evaluation routes with identical self training and an equally accurate world model. Deriving an internal self target would advance that model's input boundary without, by itself, choosing the other-directed route. The routing mechanism, its formation and its justification remain explicit tasks.

There is also a distinction between changing a condition and changing its report. If repair and masking produce the same available observations while only repair changes the underlying target, R1 fails for the target under that observation interface. An observation-based learner cannot distinguish the actions' true effects from those observations alone. Experiments that add a genuine outcome-sensitive observation can remove the obstruction; relabelling the old report cannot.

## 6. Implementation and counterchecks for a positive bridge

An admissible constructive result should specify each of the following interfaces. These are checks on the named connection, not a demand that its first model already explain all cognition.

1. **Independent target and accessible information.** Define the consequence separately from the learner and list actual signal/memory states. Apply R1 or R2 at that information level. A counterfactual estimate requiring interventions cannot be installed as a primitive sensor reading.
2. **Physical teaching and memory update.** Identify which event changes the stored predictor, where the new target value comes from, what persists across observations, and what can decay. Distinguish the teacher's generation from a mathematical recurrence subsequently written around it.
3. **Actual costs and successors.** Charge sensing, probing, writing, calibration and rehearsal where their implementation requires resources; carry damage and fuel through the resulting history. The [conditional support account](../../../../theories/becoming/chapters/CONDITIONAL-UNIVERSALITY.md) permits those costs to be bounded after their physical meaning is established. It does not create access to missing observations or provide an updater for free.
4. **Separate predictive and operative tests.** Test changed predictions on held-out outcomes, then test the causal route from prediction to action. Cutting memory updates should differ from cutting the actuator. A restored predictor with a severed actuation route should not be counted as restored effective concern.
5. **Discriminate relief from repair.** Alter the signal without repairing the dependency; alter the dependency while holding the old cue fixed; and restore the informative observation. Record which interventions the learner can itself afford. A cue-only teacher may learn accurate cue suppression while failing the actual continuation task.
6. **Preserve the sampling measure and failures.** Include failed formation, missing measurements, inactive or dead histories and the cost of obtaining labels. A changed mean after population filtering is not automatically within-organization learning. Report any conditioning explicitly.
7. **Expose the remaining evaluation route.** If a learned coefficient enters a cost or action-selection function with a supplied sign, retain that premise. A future derivation can replace it; renaming a predicted resource deficit β does not already do so.

An elementary budget obstruction is especially relevant. If observing an event consumes the final usable support and no provision is reachable before a separately costed memory write, that write cannot occur. If an outcome enters an absorbing state with no update transition, no subsequent within-organization learning can be attributed to that outcome. Simultaneous recording, persistent external memory or descendants could change the conclusion, but require their own declared transitions and costs. Reinitializing the organization for another training episode would be an added input, not evidence that the original history sustained learning.

## 7. Contribution and current verdict

This review supplies an exact information criterion, a sampling-dependent lower bound, a source-dependent sign counterexample and an action-coupling countermodel. Together they identify what an endogenous teacher can explain and what remains to be implemented. They improve the derivation by preventing an observer's measure from silently becoming the process's reward or policy.

A positive construction may legitimately replace a supplied numerical β with a measured, calibrated internal signal for a stated prediction task. To connect that achievement to the existing concern theorem, it must state whether it has also derived the signal's evaluative use, its cross-context representation and the route into another's action value. Felt experience and justification of reasons remain separate claims with their own evidence requirements.

**At the analytical checkpoint, the positive-construction verdict was pending.** No unseen learner was certified. That checkpoint leaves the parallel selector-revision review unchanged and does not claim that architecture or target origins are impossible. Its role is to make the next successful bridge precise enough to compose without a hidden teacher, unearned reset or switched interpretation. The completed finite audit follows.

## 8. Independent audit of the paid finite construction

**Current verdict: accepted as a conditional finite measurement-and-prediction interface.** The [positive mathematical note](CONSEQUENCE-TO-LEARNING-MATH.md), [declared executable protocol](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/PROTOCOL.md) and [independent execution record](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/independent-check.json) agree at the scope below. This is an internal mathematical and executable audit, not empirical validation, a Lean refinement proof, or a derivation of the apparatus's formation.

### Independent method and checked boundaries

The [independent checker](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/independent_check.py) does not use the producer's graph or stochastic transition recursion to generate its reference answers. It exhausts gate action words using separate expenditure and conversion ledgers, with the independently derived bound F+2E on word length. For prediction it enumerates full binary innovation words, finds the first round that cannot be prepaid, and computes the retained coefficient as a finite weighted sum followed by any unpaid passive decay. It then compares exact rational outputs to the producer and its saved results, checking all source hashes remain unchanged.

The audit passed:

- 12 gate preparations, summing to 155 reachable states and 248 edges across those preparations; three explicit successful schedules and the failed learned-first schedule;
- six controlled paths covering memory, direct-record and inverse routing, plus a coefficient clamp and explicit hidden-source exclusion from the controller's input;
- four primary stochastic cases, 390 additional parameter cases and 45 additional decay cases, including zero support, deterministic outcomes and zero horizon;
- exact probability mass, finite source/common-fuel ledgers, paid-update moments, retained-memory statistics, fresh-outcome prediction scores and the strict-threshold counterexample.

These checks found and corrected two implementation/interpretation issues before acceptance. One initial assertion incorrectly allowed a written coefficient at source one and reserve one; repair and capture can then fund only the subsequent probe, leaving no fuel for writing. The corrected condition is reserve at least two. Also, a truthful flag saying correct memory existed before repair did not establish causal use of that memory. The accepted fixture adds an observation-only controller: clamping its calibrated coefficient from one to zero changes its next command from repair to stop. That actuator route is explicit and supplied.

### What the gate establishes

Both source worlds begin with the same accessible damaged state. A paid probe distinguishes them and an exact paid write uses gain one. The source-present controller can then probe, write, repair and capture from reserve three. Reserve two cannot complete that learned-first order. This is a joint observation, memory, actuation and resource constraint in one continuing state history.

Reserve two can instead probe, repair, capture and write, or blindly repair, capture, probe and write. The direct-record controller implements the first cheaper order. These valid histories refute a universal three-unit bound for every successful informed response; the three-unit result belongs to the separate-write-before-first-repair architecture. Capture transfers one actual source unit into usable fuel, so it can fund a later write and cannot fund an earlier one.

The persistent receipt makes E+J a record of the original task's source availability. After capture, that historical target remains one while the remaining-source opportunity is zero. Preserving the reference is legitimate; reusing it as a positive prediction for a fresh unsupported attempt would not be. Sensor calibration, receipt persistence, exact writing, and controller orientation remain assumptions. The inverse controller shares the correct prediction but fails the delivery task, making R3 operative rather than only verbal.

### What the stochastic circuit establishes

Each actual round prepays one operation unit and one measurement/write unit. A successful return transfers two units from a counted finite source; a failed return transfers none. The teacher is the resulting common-fuel loss divided by two. The failed operation's write remains possible because that component was already funded. No inactive history receives a free observation or reset, and the primary no-decay law preserves a stopped coefficient only as an observer-readable state.

At three opportunities, gain one quarter and failure probability one half, the independent values are:

| Quantity | Initial common reserve six | Initial common reserve two |
|---|---:|---:|
| Mean retained coefficient | 37/128 | 7/32 |
| Expected squared error against true failure probability | 605/8192 | 11/128 |
| Expected squared loss on a fresh outcome | 2653/8192 | 43/128 |
| Probability all three rounds were paid | 1 | 1/4 |
| Probability coefficient is strictly above 1/4 | 1/2 | 0 |

The fresh-outcome scores are analyst diagnostics; they are not paid physical trials or runtime rewards. Their improvement from the initial predictor's expected loss of one half is a finite prediction result under the supplied law.

In the scarce case, common reserve remains at least two with probability 1/8, and those histories retain coefficient zero. Their source stock is exhausted. The statistic therefore denotes common-reserve eligibility, not complete feasibility of another round obeying the same receipt law. The earlier fourth-round wording was narrowed accordingly. Completing the first three rounds has probability 1/4 and is a different event.

The exact expectation identity retains both E[uY] and E[uw]. Conditional calibration gives E[uY]=pE[u], but resource-based stopping does not justify replacing E[uw] with E[u]E[w]. Thus the scarce histories are a counterexample to the unconditional funded recurrence while satisfying calibration on every actually paid round. This is a sampling and budget effect, not evidence of a biased primitive teacher.

Finally, the funded mean 37/128 exceeds one quarter although only half the histories exceed that threshold. A mean recurrence cannot substitute for the concern model's pathwise strict-action premise. Distributional reliability is an additional downstream interface.

### What remains outside acceptance

The positive note's paid-probe-tree criterion is valid by finite induction when its terminal plans contain no further probes, its belief states retain actual resources and reference targets, and one common plan must work for the still-indistinguishable states. The deterministic gate and stochastic circuit are supplied realizations of particular interfaces; the checker does not prove or enumerate the general theorem.

This result can supply an operational target and its correctly scoped recurrence. It does not derive the sensor, decoder, memory-writing architecture, calibrated physical prices, decay law or actuator orientation from the formed-variant chemistry. Nor does it demonstrate an already learned predictor correcting its cue after the dependency changes within one continuing history. Those remain bridges to the selector-revision programme and architecture formation.

For concern, the unresolved premises still include motivational use of the prediction, warranted cross-context correspondence, shared evaluation across identities, and the relationship to felt valence and ethical reasons. The result replaces a numerical teaching input only under the stated operational interpretation. It is neither a replacement for every meaning of β in the concern account nor completion of the unified foundation.
