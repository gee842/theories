# Paid revision into a certified renewal class

Cycle 6 mathematical memo, 5 October 2026. This extends the earlier capacity, actual-controller, and population correspondence results to a revision process following possible environmental change. It separates usable evidence, interpretation, executable alternatives, prefix finance, and timely entry into a continuing regime. The arguments use ordinary finite-state verification and information constraints; no mathematical novelty or empirical universality is claimed.

## 1. The object to verify is the revision path

A previously adequate selector can become unsuitable after a change in production, retirement expense, access, or copying conditions. Showing that an old regime and a replacement regime each have a viable operating state is insufficient. A real process must pass from its present configuration to the new one, paying for observation, retention, interpretation, and installation along the way.

Use a finite configuration space `Q` containing the population and accessible support, hidden regime, current installed program, actual memory and archive state, revision phase, clocks, and any environmental state needed for the declared horizon. An attempted action has explicit physical, financial, and authority conditions. Failed, blocked, or unaffordable attempts have defined outcomes; they do not count as successful transitions because a branch was omitted.

The actual controller is a finite implemented mechanism. Its next action is a function of its currently available interface `I(q)`, including any legitimately retained working memory. Controller memory updates and erasure are physical transitions. A proof may reason about the hidden regime or possible-state set; the controller cannot consult either unless its interface actually supplies the corresponding information.

The intended destination is a **certified renewal class** `J`: a set of configurations in which the installed actual controller meets the declared continuing duty under a specified future environment and support contract. Certification can be an invariant, a verified finite closed class, or another suitable proof. It must refer to the copied or installed program actually present, its usable assets, and its remaining reserve.

This is conditional certification. If the certificate assumes a stable new regime, later changes outside that assumption can invalidate it. If further changes are admitted, monitoring and subsequent revision must themselves lie inside the invariant. A periodically repeated diagnostic bill cannot be excluded from the class's recurrent expense merely because its first payment was affordable.

## 2. R6.1 — A finite operational revision certificate

Let `K⊆Q` be the protected states, including all required payment and deadline conditions. The revision mechanism has an observable phase flag indicating whether it is still revising or has entered renewal. This is a physical control flag, not the analyst announcing that a hidden state is safe. Let `J⊆K` lie in the renewal phase. Every admitted initial configuration must belong to the protected revision phase or to `J`, and every chosen operation has a nonempty set of defined outcomes.

Suppose one supplied actual controller satisfies:

1. **Interface uniformity.** Its action is the same at configurations with the same allowed decision information and memory. Its interpretation, computation, and updates fit the specified implementation class.
2. **Every-prefix validity.** Every admitted branch of each chosen operation respects its physical and authorization gates, makes each payment when due, remains in `K`, and meets the relevant internal timing constraints. Any setup or communication hidden inside one macro step is included.
3. **Rank decrease during revision.** There is an analyst-side rank `V:K→{0,1,…,H}`, zero on `J`, such that every revision state has positive rank. Every possible successor of the actual chosen operation either enters the renewal phase in `J`, or remains in revision with strictly smaller rank. No transition may announce renewal outside `J`.
4. **Actual renewal closure.** From every state in `J`, the controller actually installed there keeps all admitted successors in `J` and meets the continuing duty. The phase handoff and installation costs have already occurred; they are not supplied for free at the moment the proof switches arguments.

Then every admitted initial state satisfying the certificate reaches `J` within at most its initial rank in revision transitions, safely along every physical prefix. It subsequently satisfies the certified continuing duty.

**Proof.** Before entry, each transition reduces a positive integer rank. No branch can remain in revision for more than the initial rank, and the only allowed exit is entry into `J`. The prefix condition establishes payment, timing, and protection along that route. Renewal closure then gives continuing protection by induction. The actual phase flag tells the implemented controller which rule runs; the proof's hidden-state membership test does not supply a stopping oracle. ∎

For a physical time bound, each macro operation also needs an elapsed-time bound. If every revision operation takes at most `ℓ` ticks, arrival takes at most `Hℓ`; more precise duration sums can be used. A continuing physical-time claim additionally needs time divergence. Finite rank counts alone do not rule out infinitely many zero-duration renewal transitions.

R6.1 is a sufficient certificate for a supplied controller, not an optimizer or a necessary characterization of every viable revision. A backward reachability calculation may help find a policy, but its information state must be implementable. A perfect-recall belief-state algorithm is not automatically an admissible controller when reports or private memory are erased. This is the same implementation distinction emphasized by [feedback-refinement relations](https://arxiv.org/abs/1503.03715), now applied to the revision phase.

## 3. Information constraints are constraints on available responses

At a decision interface, let `B` be the set of configurations still possible to that controller. For a last installation decision, let `A*(q)` be the actions that are payable, allowed, timely, and whose every admitted outcome enters the required renewal class from configuration `q`. If the controller must act before any further informative operation is available, a necessary and sufficient condition for a sure single-action revision is

`intersection_{q∈B} A*(q) ≠ empty`.

**Proof.** A uniform action must belong to every world's acceptable set. Any action in their intersection succeeds in all those worlds. Randomizing does not create a sure guarantee if each supported action fails in at least one admitted world. ∎

This statement includes the action interface. The controller may know exactly which program is needed but lack its executable archive, amendment authority, actuator, or sufficient reserve. Conversely, it need not identify the regime if one affordable action meets the duty in every remaining world.

For a longer revision protocol, the current action intersection is only a local check. Two indistinguishable states can both permit the sole action `advance`, and each can have a full-information solution afterward. If the next indistinguishable states require incompatible installations, the overall information-based protocol still fails. Future information, memory, payments, and the same controller's later actions must remain compatible. The rank certificate checks that whole path.

### Distinguish uncertainty from misinterpretation

Three failures are different:

- **No permitted distinction:** the relevant regimes produce the same usable information before incompatible actions are due.
- **Lost distinction:** an informative report existed, but its carrier or interpretation key is unavailable when the revision decision is made.
- **Wrong supplied interpretation:** the report is available, but the actual decoder maps it to the wrong program.

The first two concern an information interface; the third can occur despite an informative interface and a working alternative decoder. Neither more computation nor an analyst's knowledge removes a genuine lack of information. But calling an actual decoder's error “unidentifiability” can wrongly deny an available solution.

A necessity claim must consider the entire permitted interface, including cash changes, elapsed time, denied actions, public records, and observable operating consequences. A dedicated paid signal is not proven necessary when another admitted channel identifies the change. The [companion population experiment](evaluator-revision.md) accordingly compares supplied query-and-rewrite protocols; a latest successful query time is not automatically an all-policy impossibility boundary. The [noisy-evidence companion](paid-revision.md) separately studies paid success probabilities under overlapping signal laws; those Bayesian probabilities are not this memo's all-branch guarantee.

## 4. A small exact paid-revision model

The toy model isolates these obligations without duplicating the population experiment's financial parameters. There is a fixed hidden new regime `θ∈{0,1}`. The initial installed program is unsuitable for either possibility. Until successful revision, support depletes at `c` units per tick and no receipt arrives. Two known executable candidate programs, `0` and `1`, are present unless an archive-loss control explicitly removes one.

Program `j` restores the declared continuing function exactly when `j=θ`. Installing either program costs `K` and takes `τ_r` ticks. The installation completion tick still incurs depletion. A successful installation enters a certified absorbing renewal class: in later operating ticks the declared external receipt arrives before and pays the support bill. This supplied renewal input is not used to finance earlier revision.

A diagnostic unit can sample the regime for fee `D`, take `τ_d` ticks to deliver its report, and pay fee `M` for the report channel. Both fees precede delivery and all public charges and durations are independent of the payload. The diagnostic unit retires before the revision controller starts. The latter receives only the actual physical report register, its public phase and budget, and the executable-program interface. It has no diagnostic-unit transcript or private remembered report.

The report channel can deliver the true bit, an invertibly recoded bit, a constant bit, or an erased register. The erased control has paid for the channel but loses the final register. No intervening payload-dependent choice can encode the answer into free cash or timing. This is a specified finite workflow, not a claim that every real observer forgets a fact when a file disappears.

For the base values

`B₀=9`, `H=4`, `c=1`, `D=2`, `M=1`, `K=2`, `τ_d=τ_r=1`,

truthful retained diagnosis followed by the actual decoder `install(report)` pays

`diagnosis 2 + channel 1 + delivery support 1 + installation 2 + installation support 1 = 7`.

It finishes in two ticks with two units remaining. Its six-state hidden-regime/phase graph has a rank decreasing from two to one to zero; the checker separately verifies the complete cash prefixes. The rank is a proof device, not a hidden controller input.

The exact comparisons are:

| Change to the base workflow | Sure revision result | Reason |
|---|---|---|
| True report retained, correct decoder | Succeeds | The actual information-to-installation route is funded |
| Constant report | Fails | Same final interface must choose between incompatible programs |
| Paid report erased before the revision controller starts | Fails | No surviving permitted record separates the worlds |
| Report recoded as `1−θ`, decoder also adapted | Succeeds | The interpretation correspondence is preserved |
| True report, actual decoder installs `1−report` | Fails in both worlds | Information is present but interpreted incorrectly |
| Candidate program 1 removed from the archive | Fails | Knowing what to install does not supply executable payload |
| Initial cash six | Fails | The mandatory paid workflow needs seven |
| Only one tick remains | Fails | Diagnosis and installation require two ticks |

The checker enumerates every deterministic rule from the final three-symbol report register to the admitted installation actions. It never lets the installed policy read `θ`. A separate full-information comparator receives that bit as an explicit idealization and **still pays** the installation and support bill. It can succeed with three cash units, while no one common uninformed installation rule can do so in both worlds. The comparator is a lower-bound diagnosis, not an executable oracle added to the actual policy class.

### A common response can avoid identification

Add a supplied universal program `U` that works in both regimes, costs eight, and takes one tick to install. A direct installation needs nine units including support and succeeds without diagnosis. With only eight units it cannot be financed. Thus informative diagnosis is one route, not a universal prerequisite for revision. The costs and availability of substitute responses determine whether identification is necessary for the declared duty.

### A formerly perfect report can become stale

If the environment may change the regime again after sampling but before installation, the old report no longer guarantees that program `report` works. In the checker, either final regime is admitted after the same received bit; no regime-specific installation gives a sure guarantee. The universal program remains adequate if it is funded. A certificate for a stable post-change regime cannot silently be reused under this stronger disturbance class.

## 5. R6.2 — A policy-relative funding and timing window

For the mandatory one-query workflow with nonnegative fees, constant depletion `c`, no pre-renewal income, a fixed regime, an informative retained report, and available candidate programs, let

`T=τ_d+τ_r`,

`B_required=D+M+K+cT`.

If diagnosis starts after `s` waiting ticks, the workflow can succeed surely exactly when

`s+T≤H`, and `B₀≥D+M+K+c(s+T)`.

**Proof.** These are the total elapsed time and all mandatory expenditures. With no intervening receipt and nonnegative fees, sufficient initial cash covers every payment prefix; the correct retained decoder then selects the matching candidate. Conversely, a successful workflow must complete both stages and pay every listed bill. ∎

For integer ticks and `c>0`, the latest start is

`s_max=min(H−T, floor((B₀−B_required)/c))`,

provided it is nonnegative. For `c=0`, only the finite deadline restricts waiting once the fixed fees are funded. At the base parameters, waiting zero, one, or two ticks works; waiting three or more does not. The checker tests the boundary across 26,208 parameter combinations.

This is an exact threshold **within this declared workflow**. A cheaper diagnostic, inherited program, direct robust fallback, alternative financing route, or a different response deadline changes it. An unsuccessful late query can still return correct information; the failure may occur because the information arrives after the actionable funding window has closed.

In a population, the analogue need not be a constant-rate depletion formula. Parent retirement, discrete child packets, treasury caps, and the currently installed evaluator can make the usable bridge nonlinear or discontinuous. The root experiment computes that actual transition rather than substituting this toy formula for its chronology.

## 6. Model correctness is a separate premise

Theorems about a declared transition relation quantify over the changes and reports it admits. They do not establish that the real world obeys that relation. A supplied diagnostic interpretation may be wrong, a changing process may no longer satisfy the assumed stationarity, or a supposedly available alternative may have disappeared.

A formal revision model therefore needs to identify which part changes and which mechanism remains trusted enough to implement the revision: the candidate family, diagnostic contract, memory interpretation, installer, or verification test. A finite controller can revise one supplied model parameter using a supplied signal without generating arbitrary new models or validating its entire interpretation framework from nowhere.

At the same time, an infinite regress is not required for a conditional result. The analysis may take a finite diagnostic-and-update mechanism as its stated starting assumption and test its consequences. Empirical application must justify that assumption and distinguish an observed anomaly from reliable evidence for a specific executable replacement.

## 7. R6.3 — Scale correspondence must include the change and revision

Separate correspondences for the settled old and new renewal classes do not certify the transition between them. A scale map must also cover change onset, its observable consequences, any query schedule, report delivery and retention, the actual interpretation, payments, program access, installation, and entry into the new class.

One sufficient construction augments both models with these phases and applies the earlier actual-process certificate to the full revision path:

- corresponding initial uncertainty and revision flags;
- interface-compatible actual actions and memory updates;
- coverage of every admitted environmental outcome;
- every physical prefix safe and payable;
- bounded protocol durations and matched deadline monitors;
- matching installed configurations inside the certified renewal class;
- correspondence of the continuation controller actually active afterward.

Composing the diagnosis, installation, and renewal certificates is valid only when their endpoint relations, interfaces, reserves, and actual controllers fit. A proof witness for the new regime does not become free evidence at the intervening handoff. If the post-change model creates a new observation distinction or removes a program payload, that alteration belongs in the correspondence too.

For stochastic finite or countable state/event models, equality of the full projected joint transition kernel and corresponding initial distributions transfers path probabilities, as in [the population theorem](../cycle-5/population-and-scale.md). The kernel must include the timing of environmental change and its dependence on queries or actions when those are part of the model. Matching only signal accuracy, expected cash, or the distribution after successful installation is insufficient. A comparison conditioned on successful revision can hide a different probability of reaching that condition.

The checker verifies an exact, limited correspondence: change all currency units by a factor of two or three, invert the report encoding, and adapt the actual decoder. Every diagnostic fee, memory fee, support payment, installation bill, and starting balance scales; the full paid path has the same completion time and success result. All 576 comparisons pass. Transforming only the settled renewal programs while leaving a report decoder or revision bill unmatched would not justify that conclusion.

This example is a unit/representation equivalence. Physical aggregation can instead change congestion, diagnostic latency, copying dependence, and funding thresholds. The general certificate provides a test for a proposed scale map; it is not a claim that every scale change preserves the ability to revise.

## 8. Closed result and remaining extension

The closed result is conditional: a specified finite mechanism can be shown to obtain usable evidence, fund its actual revision, and enter an actual continuing class before its protected support is lost. The proof distinguishes information constraints, controller interpretation, accessible alternatives, and financial timing rather than attributing every failure to a lack of foresight.

The open work is causal and empirical: how the diagnostic contract is established, how new executable alternatives become available, which duties deserve protection, and whether the modeled change and resource boundary match a real system. Automatic improvement, universal self-correction, and an unlimited ability to invent new representations do not follow.

## Preserved verification

The [standard-library checker](verification/check_revision_scale.py) and [results](verification/revision-scale-results.json) preserve report-policy enumeration, paid-prefix ledgers, signal erasure and decoder controls, the missing-program case, a funded full-information comparator, a universal substitute, a second-change counterexample, 26,208 financial/deadline checks, and 576 complete-path scale comparisons. All assertions pass. Finite checks support the stated examples; the general ranking, information, and transport arguments are given above.
