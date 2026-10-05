# Modular replacement: same output and physical paths, different correction capacity

Completed exact model study, 5 October 2026. This executes the immediate modular milestone in the previous [research protocol](../next-research-target.md). It leaves the earlier files and the parent research workspace unchanged.

## Result

A replacement can preserve current operating output, every physical transition, all action costs and durations, and physical endpoint reachability while destroying a correction guarantee. The missing item is the decision interface. Conversely, a replacement that recodes both observations and commands through a known invertible adapter preserves the guarantee exactly.

In the model below, an original provider and its invertibly recoded replacement each require **three units of post-installation reserve** for guaranteed correction by tick three. A replacement that hides the cheap diagnostic result requires **four units** because a more expensive independent diagnostic remains available. At the matched reserve of three, physical reachability and full-information capacity are unchanged, but observation-feasible correction is lost. The best randomized guarantee there is success probability `1/2`.

This is a constructed conditional result using established control and information reasoning. It is not empirical evidence that actual replacements behave this way, nor a new universal law. Its value is an exact negative test for the proposed abstraction “same output and possible endpoints imply equivalent capacity.”

## 1. Two coupled components and a declared interface

The operating component has a hidden fixed condition `θ ∈ {0,1}` and a mode `old`, `renewed`, or `failed`. Applying revision `j` renews it exactly when `j=θ`; a mismatched revision causes irreversible failure. In old mode it delivers one service unit per tick during a grace interval ending at tick `H`. If it has not been renewed by `H`, it fails. Renewed mode is safe and absorbing for the correction test.

The revision component has a cash reserve `b`, a permit flag `p`, and a diagnostic register. It can inspect, test independently, obtain permission, and issue one of two implementation commands. Its steps are coupled to the operating component through the hidden condition and the implementation command.

**Output is not free financing.** The operating service consumes a separately supplied external feedstock; its one-unit output is a performance signal, never a deposit into the revision cash reserve. There is no cash replenishment during the test. Continued service after renewal remains conditional on that external feedstock. This module does not establish recurrent material self-renewal; the parallel recurrent study addresses a different question.

**Replacement price and timing.** All comparisons begin at the same completed handoff, with the same reserve and the same remaining grace interval. No claim of free installation is made. If each provider has the same prior installation fee `K ≥ 0`, the corresponding pre-installation reserve thresholds are `K+3` and `K+4`. A common installation delay must likewise be included before the three-tick correction interval, or subtracted from a common total deadline. Unequal installation costs or delays define a different comparison.

### State, actions, and chronology

The open plant state is

`q = (θ,t,b,p,s,r,m)`.

Here `s` identifies no diagnostic, cheap diagnostic, or fresh diagnostic; `r` is the diagnostic's internal raw bit, when present; and `m` is the operating mode. The controller sees the provider's interface, not the complete plant state. It has perfect recall of observations and its own commands. That memory is unpriced in this one-handoff milestone; paid forgetting is not claimed.

For every action, cash is paid first, the transition occurs in one tick, its observation is delivered, and the next decision is made. Costs and durations are distinct: the fresh diagnostic costs two units but still takes one tick.

| Action | Base cash cost | Effect |
|---|---:|---|
| Inspect provider | 1 | Writes the cheap diagnostic's internal result |
| Fresh independent test | 2 | Writes an independently accessible perfect diagnostic result |
| Authorize | 1 | Sets `p=1` |
| Apply 0 / apply 1 | 1 | Requires `p=1` in the authorized model; renews iff the physical revision matches `θ` |
| Wait | 0 | Uses one tick without changing the plant |

Insufficient cash disables an action. In the authorized comparison, a missing permit also disables implementation. The separate physical comparison removes only that authorization filter. Neither affordability nor permit status depends on `θ`. Repeated inspection, authorization, and waiting are allowed; this prevents a particular order from being hidden in the action grammar.

When an action reaches the deadline while leaving the plant old, the mode becomes failed. An incorrect implementation also fails immediately. After renewal, the verifier may stop because the target is safe and absorbing; its enumerated complete traces pad the remaining ticks with a zero-cash `hold`. Safety through `H` and safety until target attainment therefore agree here.

### Three providers

1. **Original.** Diagnostics store and display `θ`; command `apply j` physically applies revision `j`.
2. **Recoded replacement.** Diagnostics store and display `1−θ`; command `apply j` physically applies revision `1−j`. The adapter is known at handoff: flip the displayed bit, and flip implementation-command labels. Other observations and commands are unchanged. Providing and understanding this adapter belongs to the stipulated common handoff, not an unexplained discovery.
3. **Redacted replacement.** The underlying plant and diagnostic hardware are exactly those of the original, including the internal register `r=θ`. The interface displays a constant `redacted` after cheap inspection. A fresh independent test still displays `θ`. No controller is given secret access to the internal cheap-test bit.

The cheap signal is hidden before the replacement controller acquires it. We do not erase a fact while letting a perfect-recall controller continue to remember it. If a fresh diagnosis is acquired and a later cheap display hides it, perfect recall correctly preserves the earlier fresh diagnosis.

Time, reserve, permission, source label, operating mode, and current output are observable. Before a fresh diagnostic or final implementation, the redacted interface contains no condition-dependent side channel: action availability, fees, durations, permit observations, and refusal conditions are the same in both worlds. A final success/failure result can reveal the condition, but an error is already irreversible. No automatic “apply the internal bit” command is supplied; that would be an additional usable interface.

## 2. Positive result: a genuine interface-preserving replacement

**M1 — Exact policy transfer under the recoding.** The original and recoded systems have equal robust correction capacity for every tested initial reserve and horizon, and in fact for all nonnegative reserves and finite horizons under the declared rules.

Define a state map `φ` that leaves `θ,t,b,p,s,m` unchanged and flips the recoded raw register bit when a record is present. Define an action map `κ` that swaps `apply0` and `apply1` and leaves every other action unchanged. Define an observation map `η` that flips the displayed record bit and preserves the other fields.

These maps satisfy:

* initial states correspond under `φ`;
* `η(I_recoded(q)) = I_original(φ(q))`;
* action enabling, fees, one-tick duration, service output, safety, and target membership are preserved;
* `φ(step_recoded(q,κ(a))) = step_original(φ(q),a)` whenever the action is admitted.

The maps are involutions, so the same statements hold in reverse.

**Proof of capacity equivalence.** The adapter maps every received observation and issued command into a virtual original transcript. It runs the original controller on that transcript and translates its next command with `κ`. Induction on steps gives corresponding plant states, identical cash use, and identical deadline progress. Thus every original winning policy yields a recoded winning policy. The inverse adapter proves the converse. Its maintained transcript is within the explicitly permitted perfect-recall policy class. ∎

This is a concrete exact instance of the [previous sufficient refinement criterion](../formal-foundations.md), with costs and timing preserved rather than merely bounded. It uses established [alternating-refinement reasoning](https://www.cis.upenn.edu/~alur/Concur98.html). No inference from similar-looking outputs is needed: the correspondence is exhibited transition by transition.

## 3. Negative result: even the full plant graph can omit the decisive fact

**M2 — Physical graph equality does not imply observation-feasible equivalence.** The original and redacted providers have exactly the same open plant transition graph, for both the physical and authorized action interpretations. They therefore have the same possible action/state trajectories, current service output, cash accounting, and physical endpoint reachability. Their correction capacities differ.

Graph equality is immediate: `provider=redacted` changes the observation function only; it does not occur in the state-transition clauses. This statement deliberately concerns the plant graph with its observation interface omitted. The two complete partially observed systems are not equal: their diagnostic messages differ.

### Exact thresholds and proof

Let the cheap diagnostic cost be `α>0`, fresh diagnostic cost `β>0`, permission cost `γ>0`, and implementation cost `δ>0`, with all durations still one tick. Assume the same initial state: no diagnosis acquired, no permit, and hidden `θ` admitting both possibilities.

For `H≥3`, minimum robust reserve is

`B_original = B_recoded = min(α,β)+γ+δ`,

`B_redacted = β+γ+δ`.

No robust correction policy exists for `H<3`, regardless of reserve, because an informative diagnostic, authorization, and implementation each need a separate tick in this architecture. Permission and diagnosis may occur in either order.

**Sufficiency:** use the least expensive informative diagnostic, authorize, and implement the indicated revision. The original and recoded providers can use either diagnostic; the redacted provider uses the fresh one. Each path prepays its own fees and takes three ticks.

**Necessity:** every authorized successful path pays `γ` for permission and `δ` for final implementation. A sure policy for both hidden conditions must acquire a distinguishing signal before its first implementation: before such a signal it must issue the same distribution of commands in both worlds, and the two worlds require incompatible irreversible implementations. Only an informative diagnostic can create that distinction. For the redacted provider that means a fresh test costing `β`; the original and recoded providers pay at least `min(α,β)`. These expenses occur on the same successful path and add. Repeated operations and waiting cannot reduce them. ∎

At base prices `(α,β,γ,δ)=(1,2,1,1)`, the robust thresholds are therefore **3, 3, and 4**. Full-information authorized correction needs `γ+δ=2` units and two ticks for every provider; full-information physical correction needs `δ=1` unit and one tick. A favorable successful physical path exists for each hidden condition in every provider even when a common observation-based policy cannot guarantee it.

At reserve three and deadline three, the redacted provider's maximum worst-case randomized success is exactly `1/2`. A fair guess after authorization attains it. For an upper bound, any successful policy branch that buys a fresh diagnostic would also need permission and implementation, costing four; at reserve three such a branch cannot complete. Hence successful implementation has no usable information about `θ`. Its success probabilities in the two worlds sum to at most one, so their minimum is at most one half. This also exposes the difference between impossibility of a guarantee and inevitability of failure on every run.

### Controls that delimit the mechanism

* If the fresh diagnostic becomes as cheap as the cheap diagnostic, the replacement gap disappears: both thresholds are `3` at unit permission and implementation costs.
* If `θ` is supplied in advance, every provider has the same two-unit authorized threshold. The effect is informational, not a different physical repair technology or entitlement.
* With four units and three ticks, the redacted provider succeeds through its independent substitute. The example does not obtain a permanent impossibility by deleting all alternatives.
* If time is too short, every provider fails the robust test, even with ample cash. Extra reserve does not purchase nonexistent time in this action architecture.
* All providers start with the same post-installation reserve and service performance. Operating output never pays a diagnostic fee in the calculation.

## 4. Exact verification and its independence limits

The [executable checker](verification/check_modular_replacement.py) uses Python's standard library. Run it from any directory; it writes [machine-readable results](verification/modular-replacement-results.json) beside itself.

The completed checks are:

| Check | Completed scope |
|---|---:|
| Capacity grid over providers, reserve `0…6`, and horizon `0…4` | 105 cases |
| Paired world action-word checks against the information-set solver | 18 cases, 45,960 word pairs examined |
| Original/redacted graph identity and recoded graph isomorphism, under both authority interpretations | 70 cases |
| Positive diagnostic, permission, and implementation price combinations | 72 provider/price cases |
| Uniform integer cash-unit rescalings | 63 cases |

All assertions passed. The verifier saves successful policy trees for original reserve three, recoded reserve three, and redacted reserve four; it saves the absence of a winning policy for redacted reserve three.

The information-set solver branches on observations with perfect recall. The second computation separately enumerates legal complete action words in each hidden world, pairs them, and rejects any pair prescribing different next commands after identical observation/action histories. A remaining pair winning in both worlds is exactly a feasible deterministic policy on the reached histories; unseen histories can be completed arbitrarily. This tests nonanticipation without reproducing the solver's belief recursion. The two methods still share the plant transition function, so they do not independently validate the model specification. The written lower bounds and explicit witness routes provide separate mathematical checks.

The graph audit checks cash nonnegativity and every reachable transition's exact fee, not merely total or average expense. A finite checker is evidence about these finite instances; the symbolic threshold proof and the recoding argument establish the stated parameterized claims.

## 5. What can transfer across scale, space, or time

The supported claim is **invariance under specified structure-preserving changes**, not universality under arbitrary change of scale.

Changing cash units by a positive factor, while multiplying every price and initial reserve by that same factor, preserves affordability and the policy correspondence. The script checks factors `1,2,5`; the general proof is `kb≥kc` iff `b≥c` for `k>0`, followed by induction on the ledger. Similarly, relabeling locations or carrier identities preserves this model only when the transition and information interfaces are transported with the labels. This model contains no spatial geometry and establishes no physical spatial-scaling law.

Uniformly rescaling every action duration and deadline preserves this finite model's order of decisions and observations. Changing only some delays, revealing a diagnostic later, or allowing a new simultaneous operation can change the threshold. These are mechanism changes, not unit changes.

**M3 — Temporal aggregation can erase feedback.** Keep the original provider and the same possible three-step microtrajectories, but require all three commands to be committed before any diagnostic result is delivered. At reserve three, no such open-loop batch can guarantee correction; its best worst-case success is `1/2`. The checked adaptive policy can guarantee success. The batch can contain inspection, but its final command cannot depend on that result. An aggregate description that retains an internal feedback controller would be a different, potentially faithful abstraction.

This gives a direct criterion for the scale conjecture: identify what transformations of description preserve causal order, information access, action authority, resource timing, and the test being assessed. The successful recoding is a positive witness. Redaction and feedback-losing batching are counterexamples to broader equivalence claims. A similar phenomenon in human coordination, AI systems, or biology still requires an independently justified correspondence of mechanisms; the shared terminology does not supply one.

## 6. Decision for the next step

The modular milestone is complete: it gives an interface-preserving replacement theorem, a stronger-than-output-matching counterexample, explicit substitutes, exact thresholds, and reproducible checks. The new result does not require a larger ontology.

The next integration question is whether a recurrent productive-and-corrective loop can be abstracted without losing the interfaces exposed here. Candidate summaries should be challenged with replacements that preserve current output and total reserves but alter when evidence can guide enactment. The parallel recurrent model should report which of its invariants survive the good adapter and which fail under the redacted or delayed interface, while separately accounting for installation, memory, standby, and restart.

No statement here makes persistence or increased correction capacity ethically good by itself. The protected service, irreversible-failure convention, and duty to correct are declared features of the test. Their legitimacy and their adequacy for affected people remain separate questions.
