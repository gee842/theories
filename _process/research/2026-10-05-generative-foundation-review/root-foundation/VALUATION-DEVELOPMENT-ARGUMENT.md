# How valuation develops: conditional universals, supplied premises and counterexamples

7 October 2026. AI-authored bounded argument answering the planned study recorded at the top of the [research index](../../../../RESEARCH.md) ("Explore before 10 October 2026 — how valuation develops"), which Ren asked to be completed in the project thread on the same day. The [formal companion](../../../../experiments/valuation-development/README.md) checks 33 results in core Lean 4.29.1, with no custom axioms, proof holes or `native_decide`; six use only the standard `propext` and, for five, `Quot.sound`. A separate internal AI review accepted a first version with eleven corrections, all applied here (§11). This is a first outcome of the kind the request specified, an argument with explicit universals, premises, counterexamples and open questions. It is not a new learning experiment, empirical study or ethical derivation, and internal review is not external peer review.

## 1. The claim, its inheritance and what would revise it

**Transition addressed.** In the [accepted work sequence](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md#accepted-work-sequence), this study joins step 2 (operational significance and regulation) to step 3 (learning and revision of selectors). It asks one question across all the existing constructions: **what must be true of any organized process for its own history, rather than an analyst's reward function, to form and revise its priorities?** It also asks which conclusions about that development hold whenever those conditions hold.

**Claim.** Six results (U1–U6) constrain the formation and revision of operational valuation (§4). U1–U5 each have a general part, proved over every organization or history of a stated form. Each also has finite countermodels showing that its hypothesis cannot be dropped. U6 refutes forced entailments between the lower levels of capacity. Several general parts are logically light: U1 is a congruence, U3 a definitional identity and U4 summation. Their weight lies in what they rule out and in the countermodels, and §4 states each one's actual content. Together they locate the content of a formed valuation that no analyst supplies. That content lies in three relations. First, *which consequences reach what the organization retains* (access). Second, *how what is retained changes later selection* (coupling). Third, *how those selections change the conditions on which the organization's continuation depends* (support). An analyst's success measure is needed in none of the three (§5). The same results show how connected organizations can come to value differently (§6). They also show why the candidate progression from responsiveness to revisable, other-including valuation is not a forced ladder (§3, U6).

**Inherited results.** Existing mechanisms already form and revise selectors, updaters and evaluative couplings in particular finite histories. These include [selector revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/SELECTOR-REVISION.md), [updater formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UPDATER-FORMATION.md), [learning-route revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/LEARNING-ROUTE-REVISION.md), [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md) and [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md). [Conditional universality](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md) proves its prefix bound, here called **CU-U2** to avoid a clash with this study's U2, for every process of its law class. The [identification bounds](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-IDENTIFICATION-BOUNDS.md) and the [motor-learning audit](../../../../experiments/motor-learning-cost/README.md) separate changed choice from changed evaluation in empirical settings. The [mechanism-status reconciliation](MECHANISM-STATUS-RECONCILIATION.md) warns against reporting these capacities as missing. This study does not rebuild any of them. It states what they have in common and which of their features any such mechanism must share.

A concurrent study supplies a further instance. The contact-formation work on branch `claude/project-thread-mlqbun` (`CONTACT-FORMATION-LAW.md`, not yet on `main`) reports that a blocked contact and an open but misaligned one leave identical receipts and ledgers. Accounting alone therefore cannot settle when forming the contact is worthwhile; that needs acquired phase knowledge. This is the U3 pattern, an identical record compatible with different relations to actual consequences. It is cited from that thread's report and was not re-derived here.

**Method of justification.** General statements are proved for every organization of a stated form, not for one model (§4). Each is paired with finite countermodels. Philosophical comparators test the definitions (§8). Empirical questions that the argument cannot settle are listed with discriminating observations (§9).

**Condition of revision.** The account would be revised by any of the following. (a) An organization whose selection changes with its history without any retained difference in its own conditions *and* without any change in what it is presented, contrary to U1. (b) An organization whose valuation of consequences borne by others is fixed by self-history *without* any feature of its own law linking the two channels, contrary to U2 as stated in §4. (c) A persisting valuing activity, in which every event makes a positive demand on support, that continues without recurrent provision, contrary to CU-U2. (d) A demonstration that the operational definition in §2 misdescribes a central case of valuation in a way that changes these conclusions, not merely in a way that adds experience or justification (§2 keeps those separate on purpose).

## 2. Starting within activity: what "operational valuation" names

Following the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md), the study does not begin with a world of neutral facts plus an evaluator that adds value. It begins with activity that forms and changes the conditions of further activity. Within that activity some relatively enduring organizations form. An organization of this kind carries some conditions forward, meets presented conditions, continues in one of several ways, and is changed by what follows.

The formal companion writes this as an `Org` with two parts of one continuation law: `select : M → X → A` and `retain : M → X → A → C → M`. `M` is what the organization carries forward, `X` what is presented, `A` the continuations open to it, and `C` the consequences that the encounter makes available to it. A separate `World : X → A → C` gives the consequence law of the local model. Splitting the process into organization and world is an analytical boundary. What it preserves is the difference between what the organization carries and what it meets. What it omits is everything about how that boundary itself formed and how it can shift. The [nondual core integration](NONDUAL-CORE-INTEGRATION.md) and [effective-range formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/DEEPER-GENERATIVE-ROOT.md#10-nondual-core-and-derived-positions) address that formation. Here it is a supplied premise (§7).

**Operational valuation** at retained condition `m` is the selective disposition `select m`: which continuation this organization takes in each presented condition. Valuation *develops* when its history changes that disposition. This thin definition is chosen because it names something every candidate mechanism in the tree must produce, whatever else it involves. It deliberately leaves three things apart that the request asked to keep distinct:

- **Functional valuation** is the selective disposition and how it changes.
- **Conscious experience** is whether undergoing the consequences is felt, and how. A thermostat has functional valuation in this sense (U6). The definition makes no claim that it feels anything.
- **Ethical justification** is whether the disposition, or what it brings about, merits favorable appraisal. [Ren's 7 October correction](../../../../sources/15-codex-theory-conversations/2026-10-07-value-question-and-dynamics.md) applies in full. Nothing below shows that any formed valuation is good. §4 U4 and §6 show the opposite risk.

The definition is not the only reasonable one. A richer account (Dewey's *Theory of Valuation*, enactive "sense-making", appraisal theories of emotion) would add the organization's own anticipation of ends, its affective undergoing or its reflective endorsement. The universals below remain necessary conditions on those richer accounts, because each richer account still has to change what the organization does. They do not exhaust them.

## 3. The candidate progression and where the tree already realizes each level

The request proposes a progression from selective responsiveness to anticipation and revision. Stated as levels of capacity:

| Level | Capacity | Minimal formal mark | Existing realization in the tree |
|---|---|---|---|
| 0 | One continuation only | `A` has one element | — |
| 1 | Fixed selective responsiveness | `select` depends on `X`; `retain` constant | Packet response classes in the [process-law derivation](PROCESS-LAW-DERIVATION.md) |
| 2 | History-dependent priority | `historyDependent` | [Formed recording](../../2026-10-05-concern-theory/RECORDING-FIDELITY-INTEGRATION.md) |
| 3 | Consequence-dependent retention | `consequenceDependent` | [Regulation-retention gate](../../2026-10-05-support-and-shared-generativity/completion/REGULATION-RETENTION-INTEGRATION.md), [consequence-retention selection](../../2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-RETENTION-SELECTION.md) |
| 4 | Anticipation | `select` reads a retained model of `World` | [Prediction and paid action](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PREDICTION-ACTION.md) |
| 5 | Revision of the valuing route itself | the update law is part of `M` and changed by consequences | [Updater formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UPDATER-FORMATION.md), [learning-route revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/LEARNING-ROUTE-REVISION.md), [formed route monitor](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMED-ROUTE-MONITOR.md) |
| 6 | Other-including valuation | consequences borne by another center reach `retain` through a formed coupling | [Evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md), [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md) |

The table maps existing results; it does not claim that they compose into one physical history. The [composition map](FOUNDATION-COMPOSITION.md) records which do.

**This is a candidate ordering, not an inevitable sequence.** U6 below shows, for levels 1–4, that each level can exist without the next one. It also shows that a higher capacity need not be acquired by the same individual through the lower ones. A retained model selects by anticipation without ever having learned (`retained_model_goes_stale`). In the tree, inheritance is the route by which a level can be present without being individually formed ([successor learning](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/SUCCESSOR-LEARNING.md)). Level 5 needs one clarification. With a fixed global transition law, revising a learning route is always a change in retained conditions read by that law. No process can step outside its own law. "Revision of the route" therefore means that the operative updater is held in what is retained and can be changed by consequences. It does not mean that the law of all change is rewritten. This is why a law supplied to a local model need not be an external evaluator. It is the generative activity of that model, and its provenance remains a separate question (§7).

## 4. Six results

Lean names refer to [ValuationDevelopment.lean](../../../../experiments/valuation-development/lean/ValuationDevelopment.lean). "General" marks a statement quantified over every organization, law or history of the stated form; "witness" marks a finite countermodel checked by evaluation.

### U1. History changes later selection only through what it leaves

*General.* If two histories leave the same retained condition, they leave the same valuation. Equivalently, a change of selection in the same presented condition requires a retained difference (`same_retained_same_valuation`, `priority_change_needs_retained_difference`). With a retention law that never changes retained conditions, there is no history-dependent valuation (`no_retention_no_history`). Formally this is a congruence; its content lies in the representation.

*What this needs.* Everything that carries history into later selection must be represented in `M` or in what is presented, `X`. This is not a substantive restriction: the [exact history representation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/DEEPER-GENERATIVE-ROOT.md#5-keeping-history-prevents-an-unexplained-memorylessness-assumption) shows that finite history-dependent admissibility can be represented this way. The substantive content is the *split* between what the organization carries and what it is presented.

*Witness.* Changed choice is not changed valuation. An organization that retains nothing (`M = Unit`) chooses differently when what it is presented differs (`trace_changes_choice_not_valuation`). In `run` the presented conditions are an exogenous list. The witness therefore shows only that presented conditions can vary while nothing is retained. It does not model how an earlier history changes later presentations, as a worn path or pheromone trail would; that interpretation is prose. The distinction itself is already drawn empirically in the [identification bounds](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-IDENTIFICATION-BOUNDS.md) and the motor-learning countermodels and is credited to them. Under the nondual method a trace is not "outside" the process. To attribute a valuation change to the organization rather than to the wider configuration, one has to show which of the two carries the difference.

### U2. Self-history does not fix extension independently of the organization's law

*General.* Take two organizations that select alike in every condition and retain alike on every presented condition in a class `P`. They end every history that stays within `P` in the same retained condition, however their retention differs outside `P` (`agree_on_encountered`).

*Consequence for concern.* Let `P` be consequences to the organization's own conditions. Positive, zero and negative extension to another center's consequences then agree on every self-only history (`extensions_agree_on_any_self_history`). They split as soon as other-directed consequences reach retention (`extensions_diverge_on_other`: 7, 3 and −1 from the same start). This is the general form of [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md#the-difference-that-the-experiment-must-isolate)'s statement that "private self-calibration alone cannot select" the correct extension to another center, and it is credited there.

*Scope.* The theorem compares different laws. It shows that a self-only history does not determine the extension *independently of the organization's law*. It does not show that no organization fixes its extension by self-learning. An organization whose single retained parameter drives both channels does exactly that, under its own law. Under the nondual method that shared law is not external merely because a local model states it. So level 6 is not settled by self-consequences alone, but by one of three routes: actual access to the other's consequences, a feature of the organization's own law linking the channels, or an inherited coupling. Each route has its own provenance to explain. None is excluded in principle.

### U3. Prediction does not fix choice, and choices alone do not separate prediction from scoring

*General.* Here, unlike §2, "valuation" means a *scoring* `s` of predicted consequences. Choice from prediction `f ∘ p` with scoring `s` is identical to choice from prediction `p` with scoring `s ∘ f` (`prediction_valuation_tradeoff`, a definitional identity). Any re-description of what is predicted can be absorbed into how it is scored. *Witnesses.* Identical prediction with different scorings gives different choices (`same_prediction_different_choice`). Identical scoring with different predictions also gives different choices (`same_valuation_different_choice`).

*What this establishes.* For two-option choice, prediction does not fix choice without a scoring, and the same choices are compatible with different (prediction, scoring) pairs. To separate them one needs an independently specified relation between predicted content and actual consequences, such as a reference contact or calibration. This has the structure of the non-identification of state-dependent utility from choice in decision theory (Savage; Karni). It also bears on accounts that write preferences as prior predictions (active inference): they relocate the scoring question into the prior rather than remove it. The analytical separation is accountable in the sense the nondual method requires. It preserves the reference of predictions to consequences, and where that reference is unavailable it leaves open which side a behavioural difference belongs to.

### U4. Consequence-driven learning can be captured by decoupled signals

*General, arithmetic only.* For any finite sequence of (signal, support change) pairs in which no pair has more signal than support change, cumulative signal never exceeds cumulative support change (`coupled_signal_bounded`). This bound is not tied to `Org`; it is the learning-signal analogue of CU-U2's prefix bound.

*Witnesses.* A signal-reinforced learner meets a world where one continuation produces the signal without restoring support. It entrenches that continuation while support falls from 3 to 0 (`proxy_capture`). In a world where only the support-restoring continuation produces the signal, the same learner abandons the other continuation and support recovers to 4 (`coupled_recovery`). This second world is coupled only in the weaker sense that signal goes with restored support. It does not meet the per-pair hypothesis of `coupled_signal_bounded`, because the abandoned continuation has signal 0 and support change −1. The two notions of coupling differ. Even in that coupled world, an organization that never samples the alternative gets no signal about it and depletes its support (`coupled_without_variation_depletes`).

*What this establishes.* Consequence-driven valuation *can* be captured wherever its own activity reaches a signal decoupled from the conditions of its continuation. Coupling of signal to support, without variation, need not prevent depletion. These are witnesses of possibility; no necessity claim about all learners is proved. Proxy capture (reward hacking, wireheading) is therefore not something learning as such rules out. The same structure appears in the zhishan account of "Goodharted proxies" at civilizational scale ([zhishan README, item 61](../../../../theories/zhishan-intelligence-must-be-good/README.md)). This argument supplies minimal formal instances, not its empirical confirmation.

### U5. When connected organizations converge or diverge in valuation

*General.* Let each shared encounter at least halve a distance `d` between two retained conditions. After `n` shared encounters the distance is at most the initial one divided by `2^n`. Once `2^n` exceeds the initial distance, it is zero (`shared_exposure_contracts`, `shared_exposure_converges`). If `d` separates retained conditions (`d m m' = 0` only when `m = m'`), the two organizations then end in the same retained condition and so with the same valuation (`shared_exposure_equalizes`).

*Witnesses that each defeat convergence in a single case.*

1. **Multistability.** Identical law and identical encounters keep different initial valuations apart for every length of shared history (`multistable_divergence`, `multistable_divergence_forever`).
2. **Different presentation.** Identical law and starting condition with two different encounter streams (`positional_divergence`: 3 versus −3). The reading of this as one event, enacted by one center and undergone by another, is prose. The formal content is only that the two centers are presented different consequences.
3. **Finite resolution.** A rounded halving learner never increases the difference (`halving_nonexpanding_on_sample`, checked only over values below 8). It nevertheless fails strict contraction, and a one-unit difference persists for every length of a shared history (`rounding_breaks_contraction`, `rounding_gap_forever`).
4. **Different access.** By U2, organizations whose histories reach different classes of consequence can agree on every update in a shared class and still differ elsewhere.

*Scope.* The contraction theorem covers *shared exposure*: both organizations receive the same encounter stream. In closed-loop learning, each organization's selection changes what it next encounters. That can amplify an initial difference even under a contractive update, and this case is left open (§7). The convergence half is the general form of familiar averaging results (DeGroot-type consensus). The witnesses show that connection alone need not produce shared values. **Connected systems can develop different values when their positions in an event present them with different consequences, when their update laws are multistable or of finite resolution, or when their histories reach different consequences.** None of these requires different "natures" or separate starting points. Each is a differentiation within one unfolding, which is what the nondual method asks the account to explain.

### U6. The lower capacities do not form a forced ladder

*Witnesses, each separating one level from the next, for levels 1–4:*

- Fixed selectivity without history dependence (`fixed_selectivity_no_history`).
- History dependence without consequence dependence: habituation counts exposures whatever they produced (`habituation_history_dependent`, `habituation_not_consequence_dependent`).
- Anticipation without revision. The retained condition is a model of which action yields the good consequence, and selection reads it. With a constant retention law, it selects well while the world matches the model and stays stale for every history after a reversal (`retained_model_goes_stale`). A separate constant selector, `installedPredictor`, shows stale fixed selection; calling it anticipation is a reading given only in prose (`stale_anticipation`, `stale_anticipation_not_history_dependent`).
- Joint realizability. The signal-reinforced learner is both consequence-dependent and history-dependent (levels 2–3; `reinforcer_consequence_dependent`, `reinforcer_history_dependent`). The same retained model with consequence-dependent revision recovers after the reversal (levels 3–4; `revised_model_recovers`).

*What this establishes.* Levels 1–4 of §3 are separable capacities, each needing its own mechanism. Accounts that make selectivity imply learning, or anticipation imply revision, are refuted at the level of entailment. Levels 5 and 6 are not formalized in this module. §14 adds minimal witnesses that separate them from each other (V4, V5); neither is built on level 4.

## 5. Where an analyst's reward can hide, and the invariance test

The request asks how to trace the formation of evaluative mechanisms "instead of silently supplying a reward function". The results locate three places where a reward can be smuggled in:

1. **In the retention law.** `retain` maps a consequence to a change in priority. If its form is chosen so that the analyst's preferred outcome is reinforced, the model has installed the valuation it claims to explain. In [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md) the coupling's *sign* is not supplied; it is derived from actual paired consequences. What remains supplied there is the plasticity law and its chemistry. In [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md) the update recipe, sign, scale and transfer are listed as supplied.
2. **In the signal.** If `World` emits a learning signal computed from the analyst's success measure rather than from a consequence the organization actually undergoes, coupling is assumed rather than formed.
3. **In the selector.** If `select` reads the analyst's measure directly, there is no development to explain.

**Invariance test.** Parametrize the model by the analyst's success measure `g`. The model does not supply its reward if, and only if, its `select`, `retain` and `World` are unchanged under every replacement of `g`. Under that test `g` can still *report* outcomes; it cannot operate the mechanism. All of `ValuationDevelopment.lean` passes trivially, because no definition reads any outcome measure. The test is easy to state but not trivially met. A model's consequence law can be built from `g` without naming it, so applying the test requires tracing where each signal comes from.

**What then constrains the sign of a formed valuation, if not the analyst?** Within one organization's history, it is constrained by the coupling the organization currently has and the consequences it actually reaches (U2, U4). Across continuing histories, CU-U2 gives a necessary condition, not a selection theorem. Take one process ledger whose every event makes a positive demand (at least one unit) on a support account, or whose cumulative demand is unbounded. Then a continuing history needs provision on every prefix covering demand beyond the initial reserve, and provision recurring arbitrarily late ([CONDITIONAL-UNIVERSALITY §3](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md#3-the-universal-prefix-bound), items 2 and 5).

The bound constrains the whole ledger, not a single trait. Attributing that provision to a particular coupling's selections, rather than to the environment or to other organizations, needs an additional causal account. Applying the bound to a lineage of successors needs a lineage support account and a transport map built on the same implementation, as CU §5 requires; that is not built here. Retention and transmission of coupling variants play no part in the bound itself. They matter only for what a lineage can carry forward, as in [consequence-retention selection](../../2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-RETENTION-SELECTION.md) and [updater formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UPDATER-FORMATION.md).

So far as it goes, the bound **filters out continuations whose provision cannot cover their demand**. If support arrives independently, a decoupled or harmful valuation continues as easily as a coupled one. Continuation constrains valuations through support, not through accuracy, experience or ethical merit. **Constraint on valuations across continuing histories needs no analyst reward, and it guarantees nothing favorable.**

## 6. One event, differentiated valuations

Read through the nondual method, U2 and U5 bear on the request's question of why connected systems develop different values. The formal content is in §4. This section is interpretation. One event, such as an extraction, a gift or an injury, is enacted by one center and undergone by another. The consequences each retains are different consequences of the same activity, and with identical update laws they can come to value that event oppositely (the pattern of `positional_divergence`). Their difference is real and is preserved. It is not evidence that they began as independent substances. Conversely, access to the other's undergoing is one of the routes that U2 identifies by which either could come to value the other's consequences. [Evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md) is one mechanism for this. Whether such access *should* be formed is the ethical question this study leaves to [the unified ethical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UNIFIED-ETHICAL-GROUNDING.md#describing-dynamics-and-answering-the-value-question).

## 7. Supplied premises, named

| Premise | Where it enters | Status |
|---|---|---|
| The organization/world boundary | Every `Org` | Supplied here; its formation is studied in [nondual core integration](NONDUAL-CORE-INTEGRATION.md) and effective-range work, not derived in this study |
| Deterministic selection, discrete time | `select`, `run` | Representation choice. Stochastic selection needs its own statements; the [stochastic prediction package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/README.md) is a model |
| The consequence law `World` | U2–U6 witnesses | Local model input. The universals hold for every `World`; the witnesses use particular ones |
| Shared exposure in U5 | `shared_exposure_contracts` | Restriction. Closed-loop amplification is open |
| Levels 5–6 | §3, U6, §14 | Minimal witnesses in §14 (V4, V5); the route-switching rule and plasticity law are supplied there, and material realization remains with the tree constructions |
| Coupling sign/scale in any concrete organization | §5 | Not derived here. CU-U2 gives only a ledger-level necessary condition on continuing histories |
| Variation that samples alternatives | U4 | Required, not derived; exploration mechanisms in the tree are [inquiry selection](CONSEQUENCE-INQUIRY-SELECTION-INTEGRATION.md) and [autonomous method formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/AUTONOMOUS-METHOD-FORMATION.md) |
| The thin definition of valuation | §2 | A methodological choice whose omissions are stated; revisable under §1(d) |

The [no-assumptions directive](../../../../sources/15-codex-theory-conversations/2026-10-06-no-assumptions-directive.md) is not met by this study. These premises are explicit, and two of them (the boundary and the coupling sign) carry real explanatory weight. Making them explicit is not discharging them.

## 8. Comparators

These are cited from general scholarly knowledge; their texts were not re-read in this session.

- **Reinforcement learning and the reward hypothesis** (Sutton and Barto). These accounts supply the reward signal. U4 and §5 state the conditions under which a signal can instead be a consequence the organization undergoes. Homeostatic reinforcement learning (Keramati and Gutkin, 2014) derives reward from deviation of internal variables and is the closest existing match to the coupling-to-support reading. It still installs the setpoints.
- **Reward hacking and wireheading** (Amodei et al., 2016; Everitt and Hutter). `proxy_capture` is a minimal instance. U4 states the general coupling condition whose failure produces it.
- **Exploration and lock-in** (bandit theory). `coupled_without_variation_depletes` is the familiar insufficiency of exploitation.
- **Identification of beliefs and utilities** (Savage; Karni on state-dependent utility). U3 is the two-option, ordinal version.
- **Consensus dynamics** (DeGroot). U5's convergence half. Its divergence half is the counterpart this project needs.
- **Dewey, *Theory of Valuation*** (1939), and enactive sense-making (Di Paolo). Both treat valuing as an activity within ongoing transaction rather than as a property added to neutral facts. This is compatible with §2. They give no formal universal of the U1–U6 kind and assert none.
- **Habituation** (Thompson and Spencer, 1966): the level-2-without-3 witness.

## 9. Open empirical questions and what would discriminate

1. **Where do natural organizations sit on the levels of §3?** Discriminating observation: the U6 separations. For example, a stale installed predictor keeps its choice after an environmental reversal without any history dependence. A consequence-dependent learner changes after reversal at a rate set by its exposure to the reversed consequences.
2. **Is a given behaviour change a valuation change or an environmental trace (U1)?** Discriminate by holding presented conditions fixed after the history, for example by transplanting the organization into an identical test context. The [identification bounds](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-IDENTIFICATION-BOUNDS.md) give the quantitative version for one choice model.
3. **Which coupling failures produce proxy capture in practice (U4)?** In trained AI systems, test whether reward hacking occurs exactly where an action can change the signal without changing the outcome the signal was meant to track. The coupling condition predicts that closing those actions closes the capture.
4. **Do connected human groups diverge by position, multistability or access (U5)?** Discriminate by exposing both positions of one event to each party. Positional divergence should narrow. Multistable divergence should not.
5. **By which route does other-including valuation form (U2)?** U2 says that self-history alone does not fix it independently of the organization's law. A case where it forms without access to the other's consequences should therefore show a law that links the two channels, or an inherited coupling. Both are identifiable: perturb the self channel and look for co-variation in the other, or trace the coupling's ancestry.

None of these has been run here.

## 10. What this establishes, and the next bridge

**Established, at the stated scope.** U1–U5 each prove a general statement of the form given in §4, with countermodels showing that its hypothesis cannot be dropped. U6 refutes forced entailments among levels 1–4. Together they answer the request's starting questions at the level of necessary conditions and possibilities:

- *Selective responsiveness* stays fixed until a retention law changes what is carried forward (U1).
- *Encounters change later selection* only through retained differences or through changed presentations, and the latter must not be read as valuation change (U1).
- *Prediction* does not fix choice without a scoring, and the two are not separable from choices alone (U3). *Anticipation* is separable from revision (U6).
- *Revision of priorities* can be captured by decoupled signals and needs variation to correct (U4).
- *Connected systems* can diverge by presentation, multistability, resolution or access (U5).
- *Extension of valuation to others* is not fixed by self-history independently of the organization's own law (U2).

**Not established.** No mechanism is shown to arise from nothing. Levels 5 and 6 are not formalized here. No empirical claim is confirmed. No formed valuation is shown to be good. Universal favorable direction and ethical necessity remain the separate open questions recorded in the [cloud handoff](../../../CLOUD-HANDOFF-2026-10-07.md#what-remains-genuinely-open).

**Next unresolved bridge** (addressed in §12). The closed-loop case of U5: whether and when an organization's own selections amplify valuation differences that shared exposure would erase. This is where formed valuation meets the regime question of the [generative grounding programme](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md), namely when differentiation stays generative and when it becomes lock-in. Smaller bridges are a stochastic restatement of U1–U4, formal witnesses for levels 5 and 6, and a lineage support account that would let CU-U2 apply across successors.

## 11. Review record

A separate internal AI reviewer compiled the first version independently, confirmed its 28 results and axiom profile, and accepted it with eleven corrections. All were applied in this version:

1. U2's hypothesis was restated.
2. U2's scope was narrowed to "independently of the organization's law".
3. U4 now distinguishes its two notions of coupling and claims only possibility.
4. U6 is limited to levels 1–4, with a genuine retained-model witness added.
5. Each result's actual logical content is stated.
6. The trace witness is no longer described as modelling history.
7. U5 gained the separation hypothesis, proofs for every length of shared history, and "can" in place of "whenever".
8. §5's use of the prefix bound was narrowed to a ledger-level necessary condition.
9. The description of evaluative plasticity was corrected.
10. The uptake anchor was corrected.
11. The label clash was resolved as CU-U2.

The first version remains in Git history at commit `afb4f12`. Internal review is not external peer review.

## 12. Continuation: closed-loop amplification

Added 7 October 2026 after Ren asked to continue. This section addresses the bridge named in §10. Its [formal module](../../../../experiments/valuation-development/lean/ClosedLoopValuation.lean) is additive and leaves the earlier module unchanged. It adds 11 results, none using custom axioms, proof holes or `native_decide`.

**The question.** U5 covered shared exposure only. In a closed loop, each organization's own selection decides which consequence it meets next. Can its own activity then amplify a valuation difference that shared exposure would erase? If so, through what?

**C1. Amplification passes through a selection difference (general).** Take any organization whose retention at least halves a distance for every identical encounter, meaning the same presented condition, continuation and consequence. If two such organizations select alike at every step of a history, they are under shared exposure for that history, and their distance contracts by `2^n` (`agreement_contracts`). Contrapositively, if the distance after a history exceeds what contraction allows, they selected differently at some step (`amplification_needs_disagreement`). Variation set by what is presented rather than by retained conditions always agrees. Such a schedule therefore turns the closed loop back into shared exposure (`schedule_agrees`, `schedule_contracts`).

**C2. Selection differences can amplify (witnesses).**

- *The contraction hypothesis does not prevent amplification.* An organization that retains only the last consequence it met has the strongest contraction: identical encounters make two retained conditions equal (`lastMet_contracts`). Starting one unit apart on either side of its selection boundary, two such organizations select differently, meet different consequences and settle two units apart for every length of history (`lastMet_amplifies`). This shows that C1's agreement condition cannot be dropped: contraction alone does not prevent amplification. Separately, C1's contrapositive says that under contraction a selection difference is the only route amplification can take. Without contraction, retention can amplify by itself, as `multistable_divergence` in U5 shows.
- *Self-confirming underestimates.* A greedy estimator's retention is exact for the option it takes and silent about the other. Two estimators start two units apart in one estimate and select differently from the start (`greedy_disagree_at_start`). For every length of history, the low starter never tries the better option, keeps its underestimate and meets 2 per step. The high starter corrects its estimate and meets 4 per step. The difference in what they have met grows without bound (`greedy_amplifies`). The retained estimate gap stays bounded (it goes from 2 to 3), and the selection difference never changes. What is amplified is what the two organizations meet, not the valuation itself. This is U2 operating in the closed loop: selection decides which consequences are reached, so it also decides what is never corrected. The game-theoretic analogue is the self-confirming equilibrium (Fudenberg and Levine), cited from general knowledge.
- *Scheduled variation removes it (finite witness).* `scheduled` is a separate organization whose selection ignores its retained conditions, so what is presented sets which option is tried. After one two-step schedule both estimators have met both consequences and hold the same estimates (`scheduled_variation_equalizes`). The greedy retention does not satisfy C1's contraction hypothesis, so `schedule_contracts` does not cover this case. The equality is checked only for the stated schedule.

**C3. Amplified difference is neither generative nor degenerative in itself (witnesses).** Start two learners with preferences one unit apart in opposite directions. Under the reinforcer of U4, both options yield the learning signal but only one restores support. There the work-leaning learner ends with support 6 and the tap-leaning learner exhausts its support to 0 (`one_unit_divergent_fates`). Under a modified, cost-free retention law (`restoring`), support grows by one whatever is selected. There the same difference amplifies into specialization, and both learners keep support 6 (`one_unit_specialization_both_sustained`). The contrast is therefore a change of organization, not only of world, and in the second case support does not depend on selection.

**What this establishes.** In closed-loop valuation under per-encounter contraction, the amplifier is selection, and differences are amplified at selection boundaries. Contraction per encounter cannot by itself prevent this. Under the same contraction hypothesis, variation not driven by retained conditions does prevent it, because it turns the loop back into shared exposure. Whether the amplified differentiation remains generative or becomes lock-in is not decided by the amplification. The witnesses show that it can depend on how the signals different selections reach relate to the support those selections restore (U4). This gives a precise form to one part of the regime question in the [generative grounding programme](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md). Differentiated centers can form from small differences through their own activity. Under one coupling they can sustain plural specializations; under another, the same mechanism exhausts some of them. Read through the nondual method, the plural centers in the specialization witness are not independent starting points. They differentiate under one law, in separate histories. These are two runs with no interaction between them, so they are not yet one shared history. The witness does not show that such differentiation is good; ethical appraisal remains with the [unified ethical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UNIFIED-ETHICAL-GROUNDING.md#describing-dynamics-and-answering-the-value-question).

**Scope and open questions.**

- Selection is deterministic, and variation is modelled only as a schedule set by what is presented. Whether variation that *does* depend on retained conditions suffices is open. Examples are uncertainty-driven exploration and stochastic choice with a retained exploration rate. Such variation can itself differ between organizations, so C1 does not settle it.
- The contraction hypothesis in C1 is strong. The greedy estimator does not satisfy it, because the unreached estimate is not contracted. Its amplification is a separate witness, not an instance of C1.
- The two organizations in every witness do not interact. Closed loops in which each one's selection changes what the other meets are open.
- No empirical system has been checked.

The next bridges are a stochastic restatement covering retained-condition-dependent exploration, and formal witnesses for levels 5 and 6 of §3.

## 13. Continuation: exploration driven by retained conditions

Added 7 October 2026 after Ren asked to continue again. This section answers the first open question of §12: does variation that depends on retained conditions remove self-confirming valuation differences? Its [formal module](../../../../experiments/valuation-development/lean/ExplorationCoverage.lean) is additive. It adds 11 results with no custom axioms, proof holes or `native_decide`.

**Setting.** The retained conditions include an estimate for each option, and selection may read anything retained. In this section an estimate plays both roles that U3 distinguishes. It predicts the consequence of an option, and the greedy selector scores options by it. Equal estimates therefore mean equal selections only where the two organizations have the same selection law and it reads nothing but the estimates.

**E1. Coverage, not its source, equalizes estimates (general).** The result holds under three hypotheses:
- retention overwrites the estimate of the option taken with the consequence met;
- retention leaves the other estimates unchanged;
- each option's consequence does not change and does not depend on what is presented.

Under these, every option an organization has reached is estimated at its actual consequence (`reached_estimate_exact`). Every option it has not reached keeps its initial estimate, however long the history (`unreached_estimate_kept`, `no_coverage_keeps_initial`). Reaching an option in a prefix of a history reaches it in every extension (`reaches_append`). So take any two organizations that share one retained-state type and estimate reading and meet these hypotheses in the same world, *with any selection laws at all*. Once each has reached every option, they hold identical estimates (`coverage_equalizes`). It does not matter what drove their variation: a schedule, a retained counter, retained optimism or anything else.

**E2. Retained-condition variation can cover or fail (witnesses).**

- *Failure.* The greedy estimator is itself retained-condition variation: what it tries depends on its estimates. Started low, it never reaches the better option for any length of history (`greedy_exact`, `greedy_low_never_covers`). E1 then fixes its underestimate permanently.
- *Retained optimism covers.* The same greedy law started with both estimates high (9 and 9) tries both options within two steps. It then holds the same exact estimates as the high starter (`optimism_covers`). This is optimism in the face of uncertainty, the principle behind upper-confidence-bound methods, cited from general knowledge. In this witness, both starting estimates exceed what the options yield, and the tie rule tries `false` first. Optimism about only one option would not suffice: starting at 9 and 3, the learner would lock onto `true` and never correct its overestimate of `false`. Where the optimism comes from is a further question.
- *A retained curiosity counter covers.* An organization that tries the less favoured option every third step has a counter that is retained and changed by its own activity. Started low or high, it reaches both options within three steps (`curious_exact`, `curiosity_covers_in_three`). After that, for every longer history, the low and high starters hold identical estimates (`curiosity_equalizes_forever`), and by E1 they are exact (`reached_estimate_exact`). The underestimate that `greedy_amplifies` kept for ever is corrected.

**What this establishes.** §12 asked whether variation that depends on retained conditions suffices. Under E1's hypotheses, the answer turns on coverage, not on the source of the variation. Retained conditions can drive exploration that corrects self-confirming differences, as a counter or optimism does. They can also be exactly what prevents correction, as a low estimate does. In the language of U2, and under E1's hypotheses, valuation differences that survive coverage cannot be differences in estimated consequences. They can only be differences in how options are scored or selected. A difference in an estimate that persists without coverage persists because of what each history has *not* reached. What persists is the initial or inherited value, so the starting condition is part of the explanation, not only the history. Read through the nondual method, the history explains why such a starting difference is never corrected. It does not by itself explain every formed valuation difference. Nothing here shows which explorations ought to be undertaken. For consequences borne by others, reaching them is what U2 already required, and whether to seek such access remains an ethical question.

**Scope and open questions.**
- Exact overwrite retention and an unchanging consequence law are strong hypotheses. If consequences change, an estimate equals the consequence met at the last reach, so coverage must recur. That case is not proved here.
- Averaging or noisy retention needs a stochastic statement.
- Equal estimates are not equal selections when selection laws differ or also read other retained conditions, such as counters in a different phase.
- Coverage of every option is achievable in finite time only for finitely many options, so E1 applies in practice to finite option sets.
- The organizations still do not interact.

The next bridges are changing consequence laws with recurring coverage, a stochastic version, interaction between organizations, and levels 5 and 6.

## 14. Completion: changing worlds, noise, interaction, levels 5 and 6

Added 7 October 2026, when Ren asked to finish the four remaining items. The [formal module](../../../../experiments/valuation-development/lean/ValuationCompletion.lean) is additive. It adds 15 results with no custom axioms, proof holes or `native_decide`.

**V1. Changing worlds: estimates are stale until re-reached (general, with witnesses).** Under E1's retention hypotheses, now applied to the world after a change, an option re-reached after the change is estimated at its new consequence (`after_change_reached_exact`). An option not re-reached keeps the estimate formed before the change, whatever its new consequence (`after_change_unreached_stale`). In a changing world, coverage therefore has to recur after each change.

*Witnesses.* A greedy learner that learned the old world correctly never re-tries the option that has since improved from 2 to 6, for any length of history. Its estimate stays at 2 (`greedy_exact_improved`, `greedy_stale_after_change`). Recurring curiosity re-reaches that option within three steps of the change, learns 6 and then selects it (`curious_exact_improved`, `curiosity_tracks_change`). How soon it re-reaches depends on the counter's phase at the change; here the counter stood at 3.

**V2. Noisy learning: a noise floor, and noise as a source of lock-in.** *General.* Suppose each encounter at least halves an error up to a noise allowance `ε`, meaning `2·e′ ≤ e + 2ε`. Then after `n` encounters the error has fallen by at least `n` or lies within `2ε` (`noise_floor`), so it enters the floor in finitely many steps. Once within `2ε` it stays there for every later history (`noise_floor_stays`). The guaranteed approach is linear, not geometric. The theorems are deterministic: they bound the effect of any noise within the allowance, with no probability model, and they concern an abstract error and update, not a particular learner.

*Witness.* One noisy observation, in which the better option yields 1 instead of 4, locks the greedy learner into the worse option even though it began with the correct preference. Recurring curiosity re-reaches the better option and recovers (`noise_locks_greedy_curiosity_recovers`). Under noise, then, a single unlucky encounter can create the self-confirming difference of §12, and recurring coverage can undo it in this witness.

**V3. Interacting organizations (general, with a witness).** In `pairRun`, two organizations meet the same presented conditions, and each meets a consequence that depends on both selections. If the other's selection is fixed, the interaction reduces exactly to a single organization in an unchanging world, so all the earlier results apply (`fixed_other_reduces`). When the other's selection changes, the world each one meets changes with it. V1 then says coverage must recur, and coverage must be of *joint* options.

*Witness.* Take a coordination world in which the joint option yields 4 only when both take it and 0 otherwise, while the solitary option yields 2. Two curious learners whose separately held counters start one step apart each explore the joint option alone, meet 0, and both come to estimate it at 0 over the nine steps checked. With equal initial phases they explore together, meet 4 and both select the joint option (`joint_coverage_needs_synchrony`). Individually driven exploration therefore need not supply joint coverage, and synchronized variation can. As interpretation, not formal content: a condition that synchronized their variation, such as a shared signal, would belong to neither organization alone, and their valuation of the joint option forms only through activity they undergo together. The witness does not model such a shared condition and does not show that coordination is good.

**V4. Revising the valuing route (level 5, witness).** Here the retained conditions include the update route itself. On the frozen route the estimate ignores consequences. A surprising consequence, differing by at least 2 from the estimate, switches the route to tracking, which then overwrites the estimate with what is met. Selection reads the estimate: the organization acts when it is at least 5. At the start the estimate formed is insensitive to consequences. After one surprising consequence, the same organization's estimate is sensitive to them (`route_revised_by_consequence`). The revision reaches selection: the first poor consequence only switches the route, and the second, met on the tracking route, changes what the organization selects (`route_revision_changes_selection`). Its history has changed *how* it learns, not only *what* it has learned. That is the level-5 mark of §3, realized with no other center's consequences involved.

**V5. Coming to value others (level 6, witness).** Here the retained conditions are an evaluative coupling to another center's consequences and a disposition toward acting for that center, and selection acts for the other when the disposition is positive. A paired encounter is one in which one's own consequence of an event shared with the other is met. Only the own consequence is represented, and it sets the coupling to its sign. An unpaired encounter presents only the other's consequence, which moves the disposition through the coupling. Nothing in the law fixes which sign the coupling takes.

Before any pairing, the other's good consequences leave the disposition unchanged, which is U2. After pairing in which the shared event was good for oneself, the same consequences for the other raise the disposition to 2. After pairing in which it was bad for oneself, they lower it to −2 (`other_valuation_formed_by_pairing`). Selection follows: the unformed learner does not act for the other, the aligned one does, and the opposed one does not (`other_valuation_reaches_selection`). This is a minimal formal counterpart of the mechanism in [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md). The sign is formed by actual pairing, and the plasticity law is supplied. The update route is fixed, so this is level 6 without level 5. The level-5 witness has no other channel, so it is level 5 without level 6. In a minimal sense, they witness 5 without 6 and 6 without 5. Neither is built on an anticipating (level-4) organization.

**Scope.** Every result here is deterministic, and the noise bound has no probability law. Interaction is formalized for two organizations with a common presented condition. The level-5 and level-6 constructions are minimal witnesses. They do not derive the route-switching rule or the plasticity law. The tree's [updater formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UPDATER-FORMATION.md), [learning-route revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/LEARNING-ROUTE-REVISION.md) and [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md) constructions remain the material realizations. Opposite pairing forms opposite valuation, which again shows that formation of concern is not formation of good concern.

## 15. Status of the study

The planned study asked how systems form and revise their own valuations without an analyst's reward. Its first outcome was to be a bounded argument identifying conditional universals, supplied premises, counterexamples and open empirical questions. With §§12–14, that first outcome is complete. These bridges the study named are closed at the deterministic formal scope stated: closed loops, exploration, changing worlds, noise bounds, interaction of two organizations, and minimal level-5 and level-6 witnesses. Two named bridges remain open: a stochastic restatement with probability laws, and a lineage support account that would let CU-U2 apply across successors (§10). The formal companion has 70 core-Lean results across four modules, none with custom axioms. Each of the four rounds was reviewed by a separate internal AI reviewer, and every correction was applied, including this round's nine. This local completion does not complete the unified foundation or settle its ethical questions.

The account in one paragraph: an organization's valuation is its selective disposition. Its history changes that disposition only through what it retains (U1). Self-history does not fix its valuation of consequences it never reaches, independently of its own law (U2). What it predicts and how it scores cannot be separated from choices alone (U3). Its learning can be captured by decoupled signals (U4). Organizations under shared exposure and contraction converge, and in closed loops selection can amplify their differences (U5, C1). Under exact retention of what is reached and unchanging consequences, coverage, whatever drives it, erases differences in estimated consequences (E1). Coverage must recur when consequences change (V1), including when they change because of other organizations, and joint options can need joint coverage (V3). How an organization learns can itself be changed by consequences (V4). An other-including evaluative coupling can form through actual pairing, with its sign set by that pairing (V5). U2 says self-history alone does not fix such a coupling. None of this requires an analyst's reward. None of it makes a formed valuation good.

**Open, and handed on to other work:**
- empirical identification (§9);
- stochastic versions with probability laws;
- material realization of each witness within the native generative core;
- the ethical question of which valuations and which access *should* be formed, with the [unified ethical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UNIFIED-ETHICAL-GROUNDING.md#describing-dynamics-and-answering-the-value-question).

Together with the two open bridges named above, these are what remains of the question this study addressed. *(Update: §16 closes both bridges at a stated formal scope.)*

## 16. The two bridges: chance and lineage

Section 15 left two bridges open. This section closes each at a stated formal scope. The [bridges module](../../../../experiments/valuation-development/lean/ValuationBridges.lean) adds 33 core-Lean results. Of these, 18 are infrastructure lemmas for finite weighted laws and line ledgers, and 15 are the stated results. The transition addressed is still step 2 → step 3 of the accepted work sequence. The question is whether the conclusions about valuation development survive chance, and whether support constrains valuation across generations as well as within one history.

### P. Chance

**Representation.** Selection and consequence become finite weighted laws: lists of natural-number weights and outcomes. A probability is a ratio of two masses, so nothing about real numbers is postulated. A stochastic organization (`SOrg`) has a weighted selection law and the same retention as before. The analyst may carry a record of whether a given option has been reached. The organization never reads that record.

**P1. Escape bound (general).** Suppose a law along a history has three properties. A set of conditions `G` is absorbing. From every condition outside `G`, at most `r` units of weight stay outside it. Every step has total weight `q`. Then after `n` steps the weight outside `G` is at most `r^n` out of `q^n` (`escape_bound`). The three hypotheses need hold only on states satisfying an invariant `J` of the law, and the initial law must lie in `J`. The noisy lock-in witness below needs this: outside its invariant, the escape hypothesis fails. The bound is the one interface used below.

**P2. Coverage with high probability (general).** Suppose every selection law of a stochastic organization puts total weight `q` and at most `r` on options other than `a`, and every consequence law has the same total. Then, whatever drives the exploration, the weight of histories in which `a` is still unreached after `n` steps is at most `(r q')^n` out of `(q q')^n` (`stochastic_coverage`). Provided `q, q' > 0`, that is a probability of at most `(r/q)^n`. Add retention exact for the option reached and a fixed consequence of `a`, the hypotheses of E1. Then the estimate of `a` is wrong with probability at most `(r/q)^n` (`stochastic_estimate_exact`). This restates `reached_estimate_exact` and coverage for one target option of one organization. Under persistent exploration (`r < q`) that option is reached with probability tending to one, and its estimate is exact on every history that reached it (an invariant inside the proof). The equalization of E1 across all options and across two organizations is not restated: it needs a union bound over options and a joint law for the two organizations. The hypotheses stay load-bearing. If `r = q`, so that some state never explores, the bound is vacuous, and the deterministic greedy underestimate of §12 is its limit case.

**P3. Witnesses.**
- Greedy choice with weight 2 on the favoured option and 1 on the other, started from the §12 underestimate, keeps that underestimate with probability at most `(2/3)^n` for every `n` (`eps_greedy_estimate_exact`). After three steps the bound is attained: 8 of 27 (`eps_greedy_three_steps`).
- Under noisy consequences, `true` yields 4 with weight 2 and 0 with weight 1, so its mean is 8/3, and `false` yields 2. A greedy learner that starts with the correct preference is locked into the worse option with probability at least `1 - (2/3)^n` for every `n`. Once locked, it never selects `true` again (`noisy_greedy_locks`). The deterministic V2 witness showed that one unlucky observation can lock in. Under chance, lock-in tends to certainty.
- Recurring curiosity escapes: after six steps 665 of 729 units of weight are locked for greedy choice. For curiosity, 155 units hold an estimate of 0, a state that is not absorbing because curiosity re-tries the option (`curiosity_escapes_noisy_lock`). This is a finite witness, not a general bound for curiosity.

**Reading.** Chance does not remove the deterministic results. It replaces "for every history" with a bound on the weight of histories, and the same hypothesis carries the result in both forms: coverage. Noise does not make exploration unnecessary. In the witness it makes the absence of exploration worse: under noise, lock-in tends to certainty.

### L. Lineage

**Representation.** A generation, or any composite of generations, has a ledger: what it enacted (化), what arrived to it (来), and the support it held (存) at its start and at its end. The CU-U2 prefix bound of [CONDITIONAL-UNIVERSALITY §3](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md#3-the-universal-prefix-bound) reads as `enacted + held at end ≤ held at start + arrived`. A ledger satisfying it is *sustained*.

**L1. Closure (general).** Sustained ledgers are closed under succession, where a successor starts with no more than its predecessor holds at the end (`seq_sustained`). They are also closed under division, where children together start with no more than the parent holds at the end (`par_sustained`, `branch_sustained`). Any line or branching family built from sustained generations by these two operations, with inheritance at every succession and division, is therefore itself sustained. This follows by composing `seq_sustained` and `par_sustained`. It is formalized for lines (`lineage_sustained`) and for one division step (`branch_sustained`). This is the account that lets CU-U2 apply across successors. Given inheritance at every succession and division, the bound for one history becomes a bound for a lineage without a new axiom, because the composite of sustained generations is again a generation in the ledger's sense.

**L2. Positive demand needs late arrivals (general).** Where every generation enacts at least one unit, a line of `n` generations needs arrivals totalling at least `n` minus what the first held (`lineage_needs_arrivals`). Split a line anywhere. Arrivals must cover the later part's length, beyond what the first generation held and received and what the earlier part received (`later_arrivals_needed`). A corollary, not stated as a separate theorem, follows for an unending line of demanding generations: for every split point, the part after it receives positive arrivals. Arrivals must therefore keep coming arbitrarily late.

**L3. Countermodels.**
- Without inheritance, two generations that are each sustained form a line that is not (`lineage_needs_inheritance`). The successor's starting support came from somewhere the ledger does not record. Inheritance is therefore the premise that makes the lineage bound hold.
- Illustration, not a countermodel: the ledger is silent about valuation. The ledger has no disposition field, so it is silent about valuation by construction. `ledger_silent_on_valuation` places one sustained ledger beside the level-6 learner's formed dispositions of either sign.

**Reading.** Across generations, as within one history, a continuing line of demanding generations needs provision that keeps arriving. What constrains a valuation lineage is the relation between what it enacts and what arrives to it, not an analyst's reward. Two things remain outside the ledger. One is which coupling an arrival belongs to: attributing the arrivals to the valuation that selected the activity needs a further account. The other is whether the arrivals are favourable to anyone. §5 and §14 stand: harmful or decoupled valuations can continue where support arrives independently of them.

### Status after this round

Both bridges named in §15 are closed at the scope stated. Chance is closed for finite weighted laws with constant total weight per step and a single target option. Lineage is closed for natural-number ledgers under succession and division. The study now has 103 core-Lean results across five modules, none with custom axioms. A separate internal AI reviewer accepted this round with twelve corrections, which have been applied. Its optional rename of `pay` in `pairRun` was not made, so that the verified earlier module stays unchanged.

**Still supplied:**
- the boundary between organization and world;
- the weighted laws;
- inheritance between generations;
- the per-generation ledger, whose CU-U2 form comes from CONDITIONAL-UNIVERSALITY rather than from the organizations of this study.

**Not built here:** joint probability spaces for two learners (equalizing two learners needs a coupling of their laws, or a union bound over one), probability laws whose total varies by state, continuous measures, and an account that attributes arrivals to couplings. The first three are extensions of the stated results. The last is the remaining open link for §5: attributing arrivals to couplings is what a lineage-level filtering of valuations by support would need.

**Handed on to other work:**
- empirical identification;
- realization of the witnesses in the native generative core;
- the ethical question.

This completes the study at its formal scope. It does not complete the unified foundation.

## 17. Formal unification: the lineage on the shared process

Ren set formal unification as the goal. The generation ledger of §16 was a separate model. The [lineage-in-process module](../../../../experiments/valuation-development/lean/LineageInProcess.lean) adds 14 core-Lean results, 2 of them infrastructure lemmas. These results show that the ledger is not a separate model: it is the per-event support law of the shared `Process` (`AccountLaw`, U1, called SustainLaw in the project vocabulary), and its lineage bound is that law's prefix bound (U2). The module imports the verified `ResourceContinuation` and renewal modules unchanged.

**A. Histories have ledgers (general).**
- Every actual history of every process satisfying U1 has a sustained ledger (`history_ledger_sustained`).
- Consecutive segments of one history are generations: the successor inherits exactly what its predecessor holds at the end. Succession of ledgers (`Ledger.seq`) is the ledger of the concatenated history (`consecutive_segments_are_generations`).

**B. Generations are events of a U1 process (general).** In `lineageProcess`, the state is the support held, and an event is a sustained generation that starts with no more than is held. A generation that starts with less than was held records support dissipated between generations. This process satisfies U1 (`lineage_account_law`).
- A line of sustained, inheriting generations is an actual history of the lineage process (`line_is_lineage_history`).
- The §16 lineage bound is recovered as the core prefix bound `support_trace_balance` (`lineage_bound_is_prefix_bound`).
- An endless line of demanding generations needs unbounded arrivals, by the core theorem `unbounded_demand_requires_unbounded_credit` (`endless_demanding_line_needs_unbounded_arrivals`).

The per-generation sustainment and inheritance that §16 supplied as hypotheses are, in A, consequences of U1 along one history.

**C. Renewal (general, plus the renewal thread's witnesses).**
- The renewal channel process satisfies U1: a tick's formations are demanded from the reserve, and arrivals are opened by the organization's own live tokens (`channel_account_law`).
- Every window of every execution is therefore a sustained generation (`generation_sustained`). Successive windows inherit exactly and compose (`generations_succeed`). Each execution, cut into windows of equal length, is a history of the lineage process (`execution_lineage`).
- `lineage_renewal_theorem` puts this together with the renewal–closure theorem on the same process. With finitely many kinds and spans between one and `D`, some lineage stays live forever exactly when the law has a self-renewing population.

**The attribution link of §16.** The renewal model makes arrivals attributable to kinds, because each token opens arrival at its kind's rate. The question left open was whether support filters valuations one coupling at a time. On this process it does not: what a lineage keeps is decided by membership in a self-renewing population (`renewal_keeping_theorem`), not by what each kind brings in. The two witnesses (`attribution_is_by_population`) are the renewal thread's own:
- In `danglingSupport`, kind `false` opens 2 against a formation demand of 5, yet some lineage keeps it forever on arrivals opened by kind `true`.
- In `lapsingCorrection`, a closure renews forever while the correction kind it supports cannot be kept.

So the §5 question has a precise answer at this scope. Support constrains which *populations* of formed kinds can continue. A kind, or the valuation that selects it, persists by belonging to such a population, whatever its own balance.

**Scope.** This connects the valuation study's lineage account, not its selection-and-retention organizations, to the shared process. The study's organizations are embedded in the core by the separate `ValuationInCore` work. Valuations selecting *which* kinds a channel process forms are built in §18. The study now has 117 core-Lean results across six modules, none with custom axioms. No empirical or ethical claim is made.

## 18. No supplied inputs: valuations decide what the process forms

Ren's standing rule of 6 October 2026: no assumptions and no axioms. Every input a result relies on must be derived in Lean from the process, or proved necessary for the stated claim. §17 left one input supplied. In the renewal executions, the list of kinds formed on each tick came with the execution. The [valuation–renewal module](../../../../experiments/valuation-development/lean/ValuationRenewal.lean) derives it, adding 7 core-Lean results.

**Construction.** A valuation reads the current configuration and selects which kinds to form. The process forms them when two conditions hold: what is held plus what arrives covers the formation demand, and each formed kind has a supporter that survives the tick. Otherwise it forms nothing. What is held afterwards is what was held, plus what arrived, minus what was formed. Every valuation, from every starting configuration within span, therefore determines one execution of the shared channel process (`valuation_step`, `valExecution`). Nothing about the formation sequence is supplied any more.

**Results (general).**
- `valuation_keeping_theorem`: with finitely many kinds and spans between one and `D`, some valuation keeps a designated kind alive forever exactly when some self-renewing population contains it. A constant valuation that forms that population on every tick suffices, and it needs no starting reserve (`constant_valuation_steady`).
- `every_valuation_loses`: without such a population, every valuation, from every starting configuration, loses the designated kind by the explicit time of the renewal theorem.
- `valuing_is_not_keeping` (on the renewal thread's witnesses): no valuation of `lapsingCorrection` keeps the correction kind, however it values it. In `danglingSupport`, a valuation keeps the short kind alive by also forming the kind whose arrivals sustain it.

**Reading.** What the process keeps is a property of the valuation's whole population, not of the valued kind. A valuation that forms only what it values can lose it; a valuation that also forms what sustains the valued kind can keep it. This is the formal version, on the shared process, of the claim that constraint on valuations comes from support, without an analyst's reward.

**Status of every input under the rule.**

| Input | Status |
|---|---|
| Which kinds are formed | Derived from a valuation in the process (this section). |
| Per-generation support balance (U1) and inheritance for the renewal process | Derived: U1 is part of the channel step (`channel_account_law`), and inheritance holds exactly along one history (§17). |
| Per-generation balance for an arbitrary process | A hypothesis of the general theorem, quantified over every process. It is a premise only where a process does not itself satisfy it. |
| Inheritance in the abstract lineage account (§16) | Proved necessary: `lineage_needs_inheritance`. |
| Persistent exploration (`r < q`) in P2 | Proved necessary by the deterministic limit: greedy choice never covers (`greedy_low_never_covers`). |
| Coverage in E1 | Proved necessary: `no_coverage_keeps_initial`, `greedy_stale_after_change`. |
| Unchanging consequences in E1 | Proved necessary: `after_change_unreached_stale`. |
| Contraction in C1 | Proved necessary: `contraction_needed`. Under doubling retention, two organizations that select alike at every step and start one unit apart end `2^n` apart. |
| Finitely many kinds and a span bound in the renewal theorem | Hypotheses of the renewal thread's theorem. Its `infiniteChain` witness shows renewal without closure when kinds are unbounded. |
| The numbers of a channel law (kinds, rates, spans, demands) | Quantified over: the theorems hold for every law. Deriving particular values from the native process belongs to the process-law work. |
| Decidability of the support relation | Carried as data of the model: the valuation run takes a decision procedure for the support relation as an argument (`[DecidableRel law.edge]`). No axiom is involved, and `#print axioms` shows none for it. A model whose support relation has no decision procedure cannot run a valuation; it can still satisfy every theorem that does not compute a run. |
| The particular organizations and worlds of the witnesses | Not premises: each witness proves an existence claim. |
| `propext`, `Quot.sound` | Removed (Ren, 7 October: the generative model needs no axioms). 123 of the 130 results now depend on no axiom at all (the renewal package became axiom-free on 7 October). The other 7, in `LineageInProcess`, take these axioms only from shared support theorems they call, and become axiom-free when that package's axiom-free version reaches main. See the companion README. |

The study now has 124 core-Lean results across seven modules. The remaining frontier under the rule is outside the valuation study. Kinds and rates are to be derived from the native process by the process-law work. Whether `simp` and `omega` should be replaced so that even the standard axioms are avoided is a choice about the whole project.

## 19. One process: the study's splits as cuts

Ren's standing direction of 6 October 2026 is to avoid narrative, priors and hidden assumptions, and in particular dualist framings that return unnoticed. The theory is monist and relational. The study has used several paired terms, and each is checked here. The [one-process module](../../../../experiments/valuation-development/lean/OneProcess.lean) adds 6 core-Lean results.

**Organization and world.** An organization together with its consequence law is one `Process` of the shared core. Its histories are exactly that process's traces (`run_is_trace`, `trace_is_run`). The consequence law is not a second thing standing over against the organization. It is part of the one step relation.

**One center and another.**
- Two interacting organizations are one organization on their joint state, and the paired history is that organization's history (`pair_is_one_process`). The only input left is what both meet together.
- Cut the joint process at the first center. Its part of the joint history is the run of a single organization whose consequence law is its relation to the other's actual selections (`cut_first`). Cut at the second center and the same holds from the other side (`cut_second`).
- Both cuts are read off the one joint history, so neither is privileged (`both_cuts_one_history`). What one cut calls "its world" is, from the other cut, that center's own activity. The earlier reduction to a fixed other (`fixed_other_reduces`, §14) is the special case in which the other's activity does not vary.

**Valuation and process.** Operational valuation was defined (§2) as the selection component of the step. In §18 a valuation over formations is the part of the channel step that decides what is formed. In both cases valuation names a relation inside the one process, not an evaluator applied to it.

**Self and other in levels 5 and 6.** The level-6 coupling forms through paired events of the joint process: the sign of a center's response to another's consequences is set by what their shared events did. "Other-including" therefore names a relation formed in the joint history. It is not a bridge between two antecedently separate selves.

**Scope.** These results cover the study's own representations: a deterministic organization with its consequence law, and two centers with a shared presented condition. A joint process of more than two centers is not formalized, though the same construction applies. Choosing the presented condition `x` as what both meet is itself a cut. The process-law work derives presented conditions from the native process. Earlier sections keep their wording as written, and this section governs how their paired terms are read. The current formulation page carries the same reading note. The study now has 130 core-Lean results across eight modules.

## Verification

From `experiments/valuation-development/lean/`, with Lean 4.29.1 core and no Lake project or Mathlib, follow the commands in the [companion README](../../../../experiments/valuation-development/README.md). The [first audit output](../../../../experiments/valuation-development/lean/audit-output.txt) lists all 33 `#print axioms` results for §§1–11, the [closed-loop audit output](../../../../experiments/valuation-development/lean/closed-loop-audit-output.txt) lists the 11 results for §12, the [exploration audit output](../../../../experiments/valuation-development/lean/exploration-audit-output.txt) lists the 11 results for §13, the [completion audit output](../../../../experiments/valuation-development/lean/completion-audit-output.txt) lists the 15 results for §14, the [bridges audit output](../../../../experiments/valuation-development/lean/bridges-audit-output.txt) lists the 33 results for §16, the [lineage audit output](../../../../experiments/valuation-development/lean/lineage-audit-output.txt) lists the 14 results for §17, and the [valuation–renewal audit output](../../../../experiments/valuation-development/lean/valuation-renewal-audit-output.txt) lists the 7 results for §18, and the [one-process audit output](../../../../experiments/valuation-development/lean/one-process-audit-output.txt) lists the 6 results for §19. These are formal checks of the stated representations, not empirical evidence. Finite witnesses establish only that the stated countermodel exists.
