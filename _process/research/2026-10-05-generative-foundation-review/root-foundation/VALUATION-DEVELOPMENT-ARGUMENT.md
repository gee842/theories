# How valuation develops: conditional universals, supplied premises and counterexamples

7 October 2026. AI-authored bounded argument answering the planned study recorded at the top of the [research index](../../../../RESEARCH.md) ("Explore before 10 October 2026 — how valuation develops"), which Ren asked to be completed in the project thread on the same day. The [formal companion](../../../../experiments/valuation-development/README.md) checks 28 Lean results in core Lean 4.29.1. Three use only the standard `propext` and `Quot.sound`; the rest use no axioms. There are no custom axioms or proof holes. This is a first outcome of the kind the request specified, an argument with explicit universals, premises, counterexamples and open questions. It is not a new learning experiment, empirical study or ethical derivation. Internal AI work only; no independent review has been run yet.

## 1. The claim, its inheritance and what would revise it

**Transition addressed.** In the [accepted work sequence](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md#accepted-work-sequence), this study joins step 2 (operational significance and regulation) to step 3 (learning and revision of selectors). It asks one question across all the existing constructions: **what must be true of any organized process for its own history, rather than an analyst's reward function, to form and revise its priorities?** It also asks which conclusions about that development hold whenever those conditions hold.

**Claim.** Six conditional universals constrain the formation and revision of operational valuation (§4). Together they locate the non-arbitrary content of a formed valuation. That content lies in three relations. First, *which consequences reach what the organization retains* (access). Second, *how what is retained changes later selection* (coupling). Third, *how those selections change the conditions on which the organization's continuation depends* (support). An analyst's success measure is needed in none of the three (§5). The same universals show why connected organizations can come to value differently (§6). They also show why the candidate progression from responsiveness to revisable, other-including valuation is not a forced ladder (§3, U6).

**Inherited results.** Existing mechanisms already form and revise selectors, updaters and evaluative couplings in particular finite histories. These include [selector revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/SELECTOR-REVISION.md), [updater formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UPDATER-FORMATION.md), [learning-route revision](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/LEARNING-ROUTE-REVISION.md), [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md) and [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md). [Conditional universality](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md) proves the expenditure/provision bound U2 for every process of its law class. The [identification bounds](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-IDENTIFICATION-BOUNDS.md) and the [motor-learning cost audit](../../../../experiments/motor-learning-cost/README.md) separate changed choice from changed evaluation in empirical settings. The [mechanism-status reconciliation](MECHANISM-STATUS-RECONCILIATION.md) warns against reporting these capacities as missing. This study does not rebuild any of them. It states what they have in common and which of their features any such mechanism must share.

**Method of justification.** The universals are proved for every organization of a stated general form, not for one model (§4). Each is paired with finite countermodels showing that its hypothesis cannot be dropped. Philosophical comparators test the definitions (§8). Empirical questions that the argument cannot settle are listed with discriminating observations (§9).

**Condition of revision.** The account would be revised by any of the following. (a) An organization whose priorities change with its history without any retained difference in its own conditions *and* without any change in what it encounters; U1 forbids this. (b) A learner whose extension to unencountered consequences is fixed by its encountered history alone, contrary to U2. (c) A persisting valuation whose costly activity continues without recurrent provision of any kind, contrary to the inherited U2 bound. (d) A demonstration that the operational definition in §2 misdescribes a central case of valuation in a way that changes these conclusions, not merely in a way that adds experience or justification (§2 keeps those separate on purpose).

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

**This is a candidate ordering, not an inevitable sequence.** U6 below proves that each level can exist without the next one. It also shows that a higher capacity need not be acquired by the same individual through the lower ones. An installed predictor anticipates without ever having learned (`stale_anticipation`). In the tree, inheritance is the route by which a level can be present without being individually formed ([successor learning](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/SUCCESSOR-LEARNING.md)). Level 5 needs one clarification. With a fixed global transition law, revising a learning route is always a change in retained conditions read by that law. No process can step outside its own law. "Revision of the route" therefore means that the operative updater is held in what is retained and can be changed by consequences. It does not mean that the law of all change is rewritten. This is why a law supplied to a local model need not be an external evaluator. It is the generative activity of that model, and its provenance remains a separate question (§7).

## 4. Six conditional universals

Each statement quantifies over every organization of the `Org` form and every consequence law, unless marked as a finite witness. Lean names refer to [ValuationDevelopment.lean](../../../../experiments/valuation-development/lean/ValuationDevelopment.lean).

### U1. History changes later priority only through what it leaves

*For every organization and history:* if two histories leave the same retained condition, they leave the same valuation. Equivalently, a history-dependent change of priority in the same presented condition requires a retained difference (`same_retained_same_valuation`, `priority_change_needs_retained_difference`). Without a retention law that changes retained conditions, there is no history-dependent valuation at all (`no_retention_no_history`).

*What this needs.* The representation must put everything that carries history into later selection into `M` or `X`. This is not a substantive restriction. The [exact history representation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/DEEPER-GENERATIVE-ROOT.md#5-keeping-history-prevents-an-unexplained-memorylessness-assumption) shows that any finite history-dependent admissibility can be represented this way. The substantive content is the *split*: whether the history is carried by the organization's conditions or by what it meets.

*Counterexample preserved.* Changed choice is not changed valuation. An organization that retains nothing (`M = Unit`) still chooses differently when an environmental trace changes what it meets (`trace_changes_choice_not_valuation`). A path worn in the ground or a pheromone trail can change behaviour with no change in the organism's dispositions. This general form restates the distinction already drawn empirically in the [identification bounds](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-IDENTIFICATION-BOUNDS.md) and the motor-learning countermodels; it is credited to them, not newly discovered. Under the nondual method the trace is not "outside" the process. Attributing a valuation change to the organization rather than to the wider configuration requires showing which of the two carries the difference.

### U2. What a history never reached leaves its extension undetermined

*For every pair of organizations:* if they select alike and retain alike on every encounter that occurs in a history, they end that history in the same condition, whatever they would do on encounters that never occurred (`agree_on_encountered`).

*Consequence for concern.* Training only on consequences to one's own conditions cannot fix how an organization would value consequences borne by another center. Positive, zero and negative extension agree on every self-only history (`extensions_agree_on_any_self_history`). They split as soon as other-directed consequences actually reach retention (`extensions_diverge_on_other`: 7, 3 and −1 from the same start). This generalizes the finite observation in [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md#one-continuing-material-history) that the three extensions "can agree on all the self examples". It also explains why [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md) had to obtain the coupling's sign from *actual paired* consequences rather than from self-calibration.

*What follows for the progression.* Level 6 cannot be derived from levels 3–5 operating on self-consequences alone. It needs one of three things: actual access to the other's consequences, a structural transfer rule that is itself a supplied premise, or an inherited coupling. This is a universal limit on any derivation of concern from self-learning, not a gap in a particular model.

### U3. Prediction does not fix valuation, and behaviour alone does not separate them

*For every scoring and prediction:* choice from prediction `f ∘ p` with valuation `s` is identical to choice from prediction `p` with valuation `s ∘ f` (`prediction_valuation_tradeoff`). Any re-description of what is predicted can be absorbed into how it is valued. *Finite witnesses:* identical, accurate prediction with different valuations gives different choices (`same_prediction_different_choice`). Identical valuation with different predictions also gives different choices (`same_valuation_different_choice`).

*What this establishes.* Accurate prediction is neither necessary nor sufficient for a given valuation, which answers one of the request's starting questions. The result also bears on any decomposition of an organization into "model" and "values". From choices alone, that decomposition is fixed only up to this trade-off. To separate them one needs an independently specified relation between predicted content and actual consequences, for example a reference contact or calibration. This is the same structure as the non-identification of state-dependent utility from choice in decision theory (Savage; Karni). It also shows why accounts that write preferences as prior predictions (active inference) do not thereby remove the valuation question; they relocate it into the prior. The analytical separation is accountable in exactly the sense the nondual method requires. What it preserves is the reference of predictions to consequences. What it omits, when that reference is unavailable, is any fact about which side a behavioural difference belongs to.

### U4. Consequence-driven learning tracks support only through coupling and variation

*For every history:* if no encounter yields more learning signal than support change, cumulative signal never exceeds cumulative support change (`coupled_signal_bounded`). This is the learning-signal analogue of the inherited prefix bound.

*Counterexamples preserved.* With one decoupled continuation (signal without support), the same signal-reinforced learner entrenches the decoupled option while its support goes from 3 to 0 (`proxy_capture`). With the coupled law it abandons that option and support recovers to 4 (`coupled_recovery`). Even under the coupled law, an organization that never samples the alternative gets no signal about it and depletes its support (`coupled_without_variation_depletes`).

*What this establishes.* Consequence-dependent valuation is *about* the conditions of continuation only to the extent that the signal reaching retention is coupled to them for every continuation the organization can actually take, and that variation exposes the alternatives. Both are relations within the process; neither is guaranteed by the fact of learning. Proxy capture (reward hacking, wireheading) is therefore not an anomaly. It is what consequence-driven valuation does wherever its own activity can reach a decoupled signal. The same structure appears in the zhishan account of "Goodharted proxies" at civilizational scale ([zhishan README, item 61](../../../../theories/zhishan-intelligence-must-be-good/README.md)). This argument supplies its general form, not its empirical confirmation.

### U5. When connected organizations converge or diverge in valuation

*For every update law and distance:* if each shared encounter at least halves the distance between two retained conditions, then after `n` shared encounters the distance is at most the initial distance divided by `2^n`. Once `2^n` exceeds the initial distance it is zero (`shared_exposure_contracts`, `shared_exposure_converges`).

*Divergence, preserved as countermodels.* Four routes defeat convergence, and each is realized:

1. **Multistability.** Identical law and identical encounters keep different initial valuations apart forever (`multistable_divergence`: 0 versus 5).
2. **Positional differentiation.** Identical law and starting condition, but one connected event is presented differently to the two centers it joins. Enacting it leaves a gain and undergoing it leaves a loss (`positional_divergence`: 3 versus −3).
3. **Finite resolution.** A rounded halving learner never increases the difference (`halving_nonexpanding_on_sample`, checked over values below 8 only). It still fails strict contraction, so a one-unit difference persists forever under identical encounters (`rounding_breaks_contraction`).
4. **Different access.** By U2, organizations whose histories reach different consequence classes can share every encountered update and still differ on everything else.

*Scope.* The contraction theorem covers *shared exposure*: both organizations receive the same encounter stream. In closed-loop learning, each organization's selection changes what it next encounters. This can amplify an initial difference even under a contractive update. That case is left open (§7). The convergence half is the general form of familiar averaging results (DeGroot-type consensus). The divergence half shows that connection alone does not produce shared values. **Connected systems develop different values whenever their positions in one event differ, their update laws are multistable or of finite resolution, or their histories reach different consequences.** None of these requires different "natures" or separate starting points. Each is a differentiation within one unfolding, which is what the nondual method asks the account to explain.

### U6. Formed capacities do not form a forced ladder

*Finite witnesses, each separating one level from the next:*

- Fixed selectivity without history dependence (`fixed_selectivity_no_history`).
- History dependence without consequence dependence: habituation counts exposures whatever they produced (`habituation_history_dependent`, `habituation_not_consequence_dependent`).
- Anticipation without revision: an installed predictor selects well while the world matches it, then keeps its stale valuation forever after the world reverses, with no history dependence at all (`stale_anticipation`, `stale_anticipation_not_history_dependent`).
- The signal-reinforced learner is both consequence-dependent and history-dependent (`reinforcer_consequence_dependent`, `reinforcer_history_dependent`), so the levels are jointly realizable.

*What this establishes.* The progression of §3 is a set of separable capacities, each needing its own mechanism. Accounts that make anticipation imply learning, or learning imply concern, are refuted at the level of entailment. The tree's existing constructions, which supply each transition with its own mechanism and costs, are therefore the right shape of answer rather than overbuilding.

## 5. Where an analyst's reward can hide, and the invariance test

The request asks how to trace the formation of evaluative mechanisms "instead of silently supplying a reward function". The universals locate three places where a reward can be smuggled in:

1. **In the retention law.** `retain` maps a consequence to a change in priority. If its sign and scale are chosen so that the analyst's preferred outcome is reinforced, the model has installed the valuation it claims to explain. Examples are the declared plasticity sign in [evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md) and the update recipe in [evaluative uptake](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-UPTAKE.md). Both studies already list these as supplied.
2. **In the signal.** If `World` emits a learning signal computed from the analyst's success measure rather than from a consequence the organization actually undergoes, U4's coupling is assumed rather than formed.
3. **In the selector.** If `select` reads the analyst's measure directly, there is no development to explain.

**Invariance test.** Parametrize the model by the analyst's success measure `g`. The model does not supply its reward if, and only if, its `select`, `retain` and `World` are unchanged under every replacement of `g`. Under that test `g` can still be used to *report* outcomes; it cannot operate the mechanism. All of `ValuationDevelopment.lean` passes trivially, because no definition reads any outcome measure. The test is easy to state but not trivially met. A model's consequence law can be built from `g` without naming it, so applying the test requires tracing where each signal comes from.

**What then fixes the sign of a formed valuation, if not the analyst?** Within one organization's history: the coupling it currently has (U4) and the consequences it actually reaches (U2). Across a lineage: which couplings persist. The inherited conditional-universality bound gives a conditional universal here. Take a lineage where (i) costly valuing activity continues only on support that the organization's own selections generate, with no independent subsidy, and (ii) coupling variants are retained and transmitted. Then on every prefix, a persisting coupling's induced selections must generate the provision that covers its cumulative demand beyond the initial reserve. Indefinitely continued costly valuing requires those selections to keep generating provision arbitrarily late ([CONDITIONAL-UNIVERSALITY §3](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md#3-the-universal-prefix-bound)). The [consequence-retention selection](../../2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-RETENTION-SELECTION.md) and [updater formation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UPDATER-FORMATION.md) results realize instances.

The bound runs one way only. If support is independently provided, a decoupled or harmful valuation persists as easily as a coupled one. Persistence selects couplings by their support consequences, not by accuracy, experience or ethical merit. **Selection over valuations therefore requires no analyst reward. It also guarantees nothing favorable.**

## 6. One event, differentiated valuations

U2 and U5 together give a nondual reading of the request's question of why connected systems develop different values. One event, such as an extraction, a gift or an injury, is enacted by one center and undergone by another. The consequences each retains are different consequences of the same activity. With identical update laws they come to value that event oppositely (`positional_divergence`). Their difference is real and is preserved. It is not evidence that they began as independent substances. Conversely, sharing more of their consequences, through access to each other's undergoing, is exactly the access that U2 says is needed before either can come to value the other's consequences at all. [Evaluative plasticity](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVALUATIVE-PLASTICITY.md) is one mechanism for this. Whether such access *should* be formed is the ethical question this study leaves to [the unified ethical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/UNIFIED-ETHICAL-GROUNDING.md#describing-dynamics-and-answering-the-value-question).

## 7. Supplied premises, named

| Premise | Where it enters | Status |
|---|---|---|
| The organization/world boundary | Every `Org` | Supplied here; its formation is studied in [nondual core integration](NONDUAL-CORE-INTEGRATION.md) and effective-range work, not derived in this study |
| Deterministic selection, discrete time | `select`, `run` | Representation choice. Stochastic selection needs its own statements; the [stochastic prediction package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/README.md) is a model |
| The consequence law `World` | U2–U6 witnesses | Local model input. The universals hold for every `World`; the witnesses use particular ones |
| Shared exposure in U5 | `shared_exposure_contracts` | Restriction. Closed-loop amplification is open |
| Coupling sign/scale in any concrete organization | §5 | Not derived. Only its lineage-level filtering by support is (conditionally) |
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
5. **Can other-including valuation form without paired access (U2)?** U2 predicts no. A positive finding would have to locate a structural transfer rule or an inherited coupling, and either would be identifiable.

None of these has been run here.

## 10. What this establishes, and the next bridge

**Established, at the stated scope.** Universals U1–U5 hold for every organization of the `Org` form and every consequence law. Each has a matching countermodel showing that its hypothesis cannot be dropped, and U6 refutes a forced ladder. Together they answer the request's starting questions at the level of necessary conditions:

- *Selective responsiveness* is fixed responsiveness until a retention law changes what is carried forward (U1).
- *Encounters change later priorities* only through retained differences, or else through traces in the world, which must not be read as valuation change (U1).
- *Anticipation* is separable from both learning and valuation (U3, U6).
- *Revision of priorities* tracks the conditions of continuation only through coupling and variation (U4).
- *Connected systems* diverge by position, multistability, resolution or access (U5).
- *Extension of valuation to others* is undetermined by self-history (U2).

**Not established.** No mechanism is shown to arise from nothing. No empirical claim is confirmed. No formed valuation is shown to be good. Universal favorable direction and ethical necessity remain the separate open questions recorded in the [cloud handoff](../../../CLOUD-HANDOFF-2026-10-07.md#what-remains-genuinely-open).

**Next unresolved bridge.** The closed-loop case of U5: whether and when an organization's own selections amplify valuation differences that shared exposure would erase. This is where formed valuation meets the regime question of the [generative grounding programme](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md), namely when differentiation stays generative and when it becomes lock-in. A second, smaller bridge is a stochastic restatement of U1–U4.

## Verification

From `experiments/valuation-development/lean/`, with Lean 4.29.1 core and no Lake project or Mathlib, run `lean ValuationDevelopment.lean`. The [audit output](../../../../experiments/valuation-development/lean/audit-output.txt) lists all 28 `#print axioms` results. These are formal checks of the stated representations, not empirical evidence. Finite witnesses establish only that the stated countermodel exists.
