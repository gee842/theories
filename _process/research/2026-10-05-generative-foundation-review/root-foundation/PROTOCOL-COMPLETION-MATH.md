# When an issued physical protocol actually completes

6 October 2026. AI-authored mathematical specification for an additive extension of the accepted [protocol composition](../../../../theories/becoming/chapters/PROTOCOL-COMPOSITION.md) interface. **Accepted scoped mathematical and internal source review; the combined fresh Lean build passes.** The contract was specified before final formal acceptance; the final version also names the proved maximal-attempt, finite-continuation and predictor instances. See the [independent review](PROTOCOL-COMPLETION-REVIEW.md). No new physical experiment, stochastic law, learning device or mathematical priority is claimed.

The named connection is **an issued, physically implemented operation → an actual completed report and continuing boundary state**. This addresses explicit grounding and compatible composition under the existing [five completion conditions](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#completion-of-the-unified-foundation). It does not establish the still-separate formation, ethical-application or successor-correction connections.

## 1. The exact existing gap

[ProtocolComposition.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolComposition.lean) already defines a nonempty first-return `BlockPath`, its boundary `blockProcess`, reported physical realizations, exact controlled refinement and actual micro-event resource accounts. Its `controller_trace_iff_implementation` matches **completed** macro histories with physical implementations. Its `block_length_bound` bounds a block **given its completion**, and `no_infinite_internal_execution` excludes infinite internal runs under strict descent. None of those statements excludes finite internal deadlock.

[ProtocolExamples.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolExamples.lean) supplies decisive existing countermodels: the stalling and nonstalling implementations have identical completed macro histories, yet one admits infinite internal activity; an unfunded-source attempt spends its usable fuel and deadlocks before returning. No new example is needed to expose the gap.

The [formal core](../../../../theories/becoming/chapters/FORMAL-CORE.md) already contains finite viability and recurrent-operation principles in F8–F9. F13 explicitly assumes that each implementing procedure terminates. The new contribution is a reusable sufficient contract that discharges that particular termination obligation and joins the existing Lean block/controller/account interfaces. It is not a new general theory of liveness or recurrence.

## 2. A declared completion contract

Let `P` be the actual micro-process, `I` its supplied protocol, `B(s)` its boundary predicate and `a` a command held fixed during one operation. Write

\[
s\xrightarrow[e]{a}t
\]

when the actual micro-event is both a `P` transition and permitted by `I` under command `a`. Physical latching, allowed interference and intermediate observations must be represented in that state and permission law where relevant. The contract does not invent an external scheduler with additional powers.

Supply a predicate `Live(a,s)` and a natural-number rank `r(s)`. Here **Live means an admissible issued-domain state**, not biological life, successful performance or moral value. Require:

1. **A physical next event:** for every `Live(a,s)`, there are `e,t` with `s →ᵃₑ t`. This includes the initial issued state.
2. **Internal closure:** if `Live(a,s)`, `s →ᵃₑ t` and `¬B(t)`, then `Live(a,t)`.
3. **Internal descent:** under the same premises, `r(t) < r(s)`.

The conditions apply to **every** admitted internal outcome, not just a favorable chosen branch. They may be imposed only on the reachable admissible domain rather than on unrelated malformed states. `Live` and its closure provide that domain in the proposed formal API `CompletionContract I Live rank`.

Membership in a mathematically specified domain is not automatically observable to the actor. If issuance must be guaranteed using only its available information, the admission rule must ensure `Live(a,s)` for every actual state compatible with that information. Selecting only hidden-world cases in which future writing happens to be affordable does not implement such a rule. A stronger reserve condition may discharge this obligation; the theorem does not supply a sensor for the future receipt.

For an issued operation the starting state is a genuine boundary `B(s)` with `Live(a,s)`. A completed attempt performs at least one actual micro-event and stops at the first successor satisfying `B`. A boundary can represent an explicitly implemented failed-return result if the declared protocol supplies it. Refusing to issue an inadmissible command is not counted as a completed operation. A paid internal deadlock is not converted into a free report, abort, refund or reusable boundary.

## 3. The completion theorem

**Theorem.** Under the contract, from any `Live(a,s)`:

- at least one nonempty `BlockPath` exists and has length at most `r(s)+1`;
- every finite unfinished internal prefix can extend by an actual permitted event;
- no infinite execution can remain entirely internal;
- consequently every maximal discrete attempt reaches its first return boundary in at most `r(s)+1` micro-events.

The first statement supplies existence, so the last statement is not a vacuous assertion about an empty class of maximal attempts. A finite maximal attempt means either a first-return path, or an unfinished path with no permitted next event. An infinite attempt has a permitted event at every index and never reaches a successor boundary. Arbitrary pauses are not automatically maximal attempts in this transition semantics.

**Proof.** After an internal prefix of length `n` ending at `t`, induction using closure and strict natural-number descent gives

\[
\operatorname{Live}(a,t),\qquad n+r(t)\le r(s).
\tag{C1}
\]

Thus an infinite internal run is impossible. A finite internal endpoint cannot be a deadlock, by the next-event premise and the preserved `Live` predicate. If its rank is zero, a next event must reach a boundary because a strictly lower natural rank is impossible. Strong induction on `r(s)` constructs a completing path: take a supplied next event, finish if it reaches a boundary, and otherwise apply induction at its strictly lower-rank successor. A completion has at most `r(s)` internal-successor events and one final boundary event. These facts give the stated maximal-run bound. ∎

Strict natural descent is a sufficient bounded-completion certificate. It is not asserted necessary for every terminating process: different well-founded ranks, fairness hypotheses or probabilistic eventual-return arguments concern different classes. An almost-surely terminating retry protocol can still admit a probability-zero infinite branch and fail this all-admitted-runs contract.

## 4. What composes with completion

At a genuine boundary let `decode(s)` read the abstract world and inherited controller memory from the actual physical state. Let the report function read the physically retained completion record. Use the existing local exactness contract between the protocol's `reportedProcess` and the declared abstract closed loop.

The old local exactness result preserves the permitted command, returned observation, abstract successor and updated memory on every completed block; it also lifts the declared abstract steps from each corresponding concrete boundary representative. The new completion contract rules out hidden internal deadlock or divergence for an issued command in its admissible domain. Together they support total discrete implementation at this boundary. An outcome-sensitive abstract claim must include all relevant successful and failed return states/labels in that correspondence. Exactness of a success-only projection does not become exactness of all outcomes merely because a rank was supplied.

For a finite succession of commands, the actual returned physical state is the next entry. Completion can be applied again only if that actual state is `Live` for the next commanded operation. A reusable continuation invariant can establish this for every allowed returned boundary and next controller command. The next command must use the actual reported observations and retained memory under the existing controller contract; it is not chosen with unobserved world information. Each newly completed block concatenates with the previous one through the existing `ReportedRealization` relation. No resource, memory or permission reset is introduced.

More explicitly, supply a boundary-domain predicate `D` such that (i) every `D` state is `Live` for the command chosen from its decoded memory, and (ii) every actual completed block for that command ends in `D`. Then induction gives, for each finite `n` and each actual initial `D` boundary, a reported realization of `n` commands with the same closed-loop trace and an actual final `D` state. `admitted_finite_continuations` is the formal corollary. It assumes this strong boundary closure rather than deriving renewal from one completed operation. Without that further premise, a boundary can still be a completed final project or a returned failure that does not admit another operation.

One invariant domain closed for all lengths is stronger than necessary for a single finite funded job. Horizon-indexed entry obligations or successive one-step continuations can suffice for that job. The reusable `D` contract is not a new universal admission requirement.

## 5. Accounts are retained, not replaced by the rank

For each independently interpreted reserve, use the existing actual micro-event account law

\[
R(t)+d(s,e,t)\le R(s)+c(s,e,t).
\]

Every complete block, every internal prefix and every concatenated physical realization then retains the accepted support bounds. Multiple accounts remain separate coordinates. The rank need not be a material stock or an ethically meaningful quantity. A strict rank decrement does not pay an event; actual affordability and access come from the underlying guards and the proof of nonblocking.

Conversely, nonnegative balances alone do not establish the completion contract. The existing paid deadlock satisfies the accounts while failing to reach a return boundary. Future credit cannot fund a missing prior event.

If each completed operation consumes at least one unit of an identified closed total account with no new credit, a realization of `N` operations requires `N ≤ R(s₀)`. This is a direct reuse of the existing [conditional prefix bound](../../../../theories/becoming/chapters/CONDITIONAL-UNIVERSALITY.md), not a new replenishment theorem. A claim of admissible boundary closure for arbitrarily many such operations would contradict that account. Completion of each admissible operation and continued admissibility are different properties.

## 6. Existing positive and adverse cases

Use the unchanged `ProtocolExamples` law. `pay` consumes a usable fuel unit and enters `busy`; a completing `tick` consumes one source unit and restores a usable fuel unit. In the nonstalling version choose:

\[
\begin{aligned}
\operatorname{Live}(\mathrm{ready}(f,q))&\iff f>0\land q>0,\\
\operatorname{Live}(\mathrm{busy}(f,q))&\iff q>0,\\
r(\mathrm{ready}(f,q))&=1,\qquad r(\mathrm{busy}(f,q))=0.
\end{aligned}
\]

Every admitted issued operation then returns in two events. From `ready(1,2)`, the two actual operations end at `ready(1,0)`: usable fuel survives, the two source units do not. The endpoint lies outside the next issued domain. Repeating the proof cannot silently replenish the source.

The unchanged adverse cases separate the premises:

| Case | Exact obstruction |
|---|---|
| `ready(0,1)` | No entry event; descent alone is vacuous and does not make an issued operation possible. |
| `ready(1,0) → busy(0,0)` | Entry is possible and paid, but the reached internal state has no next event. Entry nonblocking alone does not suffice. |
| Stalling `busy(0,1) → busy(0,1)` | A permitted self-loop prevents strict descent. Completing paths still exist, but a maximal infinite busy attempt also exists. |
| `ready(1,2)` after two completions | Initial completion does not imply boundary closure or indefinite continuation. |

These are failures of sufficient conditions or stronger advertised inferences, not a claim that every physically valid implementation must have this specific phase split, stock representation or rank.

## 7. Falsifiable content and strict scope

Once the transition relation, boundary/report meanings, admissible domain and rank are independently specified, an admitted internal path longer than the initial rank, a reachable internal deadlock, or a nondecreasing internal transition contradicts the declared contract. One may revise the law or its empirical mapping, but cannot silently add a hidden success boundary or delete the failed branch. A false report may instead violate the separate observation/meaning correspondence while the termination theorem remains true.

No wall-clock deadline follows from a micro-event count. A scheduler can withhold the next event in physical time unless a progress/timing law is supplied. Waiting that changes the actual system, wears apparatus or harms a recipient belongs in the relevant process if those consequences are claimed. No fairness, probability, source arrival, sensor calibration or ethical warrant is generated by the theorem.

The additive sources are [ProtocolCompletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolCompletion.lean), [ProtocolCompletionExamples.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolCompletionExamples.lean) and [PredictionProtocolCompletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolCompletion.lean). Their [fresh receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/protocol-completion-audit.json) passes 34 new theorem audits across the three additions and 244 inherited audit declarations in the 15-module build. These counts record proof coverage, not progress toward a theorem-count finish line. This closes a missing total-correctness interface only if the synthesis keeps its hypotheses explicit; it does not certify arbitrary Python callers, all installed protocols, the real universe, or completion of the unified foundation.
