# Continuation requires recurrent renewal under an independently supported exhaustion condition

7 October 2026. AI-authored mathematical supporting study for Ren's new thought that the continuation of life, systems and humanity depends on being generative. **Status: checked conditional necessity and a checked limit on its conclusions; neither physical universality nor universal ethical warrant is proved.**

The governing inquiry remains whole generative organization and realization → justified ethical quality → practical reasons and constraints. This note advances its **dependence premise**: when continuing activity cannot run indefinitely without renewing its enabling conditions, indefinite continuation requires renewal repeatedly, however late the inquiry starts. It does not supply the ethical force of continuation, a requirement that each differentiated participant reproduce, or the justification of every activity that happens to sustain itself.

## 1. Existing results credited

This is a small abstraction of an established research connection, not the discovery of renewal's importance from scratch.

- [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) already proves bounded trace length and the impossibility of an infinite execution when **every** permitted transition strictly lowers a Nat-valued reserve. The present interface allows actual renewing transitions and proves that they cannot eventually disappear.
- The [renewal–closure package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) establishes much stronger necessity and sufficiency within a specified formation/support law. With finitely many kinds, endless liveness without imported organization exists exactly when a self-renewing population exists. The [7 October handoff](../../../handoffs/2026-10-07-renewal-closure.md) records the latest **219 empty-axiom audits**. Historical 32/95-audit stages are earlier scopes, not the current validation count.
- In particular, `steady_fixed`, `steady_renews` and `steady_endless` in `RenewalSufficiency.lean` (namespace `Generative.Conditional.Renewal`) already construct endless turnover with a fixed configuration of kinds and ages. That existing result must be credited when distinguishing renewed occurrences from growth of organizational form. The small alternating witness below exposes only this logical distinction; it does not replace the richer accounting model.

The prior package was inspected, including its handoff, source declarations and saved receipt, but was **not rebuilt in this round**. The new proof has no project-module imports; its proof dependencies do not silently include an unchecked version of that package. The earlier package's remaining law-derivation and physical-correspondence obligations remain in place.

## 2. One process, a selected representation

Following the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md), `states n` describes selected configurations of one unfolding. It does not introduce an independent agent and environment, owner and resource, or separate realms of causal and ethical existence. Support, work and restoration are differentiated relations within a history; the actual formation of these relations is not derived by this interface.

`renewal n` concerns the transition from time `n` to time `n + 1`. Its intended empirical identification is restoration or re-formation of conditions needed for the independently specified activity. Its identification must **precede** the desired result. Calling every nondecreasing transition "renewal" solely to make the theorem apply would not establish the substantive claim. Nor can an analyst define success as generativity and then claim to have discovered that successful continuation is generative.

The general recurrence theorem does **not** itself assert that an event marked `renewal` restores any capacity. It assumes an event predicate together with descent on its absence; its conclusion is recurrence of that predicate. A separate correspondence argument must establish the restorative content. In the alternating witness only, `alternating_restoration_raises_rank` checks that content explicitly.

`unrenewed later earlier` represents the change of configuration during activity without that renewal. Its orientation matches Lean's accessibility relation: the next configuration is below the present one. The essential premise is that this relation is **well-founded**. No infinite succession can consist only of these transitions. A locally accessible initial configuration is already enough for a conclusion about its tail; global well-foundedness is a convenient stronger certificate.

This assumption can concern replacement dependencies, degradation, accumulating incompatibilities or a combination of them. It is not a claim that every physical condition is an additive stock. Finding a suitable relation and establishing its well-foundedness are substantive correspondence obligations. Their being represented as inputs here does not make them external to the actual unfolding.

## 3. Exact results and hypotheses

The source is [ContinuationRenewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean), namespace `ContinuationRenewal`.

### General well-founded result

Given any configuration type `State`, relation `unrenewed`, history `states : Nat → State` and event predicate `renewal : Nat → Prop`:

1. `no_renewal_free_tail` assumes `WellFounded unrenewed` and, for every `n`, absence of renewal at `n` implies `unrenewed (states (n + 1)) (states n)`. For each `start`, it proves that renewal cannot be absent at every time at or after `start`. This is a constructive negative result; renewal need not be decidable.
2. `renewal_arbitrarily_late` assumes well-foundedness and an explicit disjunction at each time: renewal occurs **or** the next configuration is lower in `unrenewed`. It proves `∀ start, ∃ n, start ≤ n ∧ renewal n`.
3. `renewal_arbitrarily_late_of_decidable` obtains the same positive result from the absence-implies-descent premise when renewal is decidable. This constructive decision premise is explicit. It is not an assumption of universal empirical predictability.

The proof follows accessibility induction. At a renewal event the desired witness is present. Otherwise the history moves to an accessible predecessor, for which the induction hypothesis supplies a later renewal witness. The negative version applies the same induction to an alleged infinite unrenewed tail. No choice of an infinite sequence is required: the history is already supplied.

### Natural-rank window

For an independently specified `rank : Nat → Nat`, suppose every actual nonrenewing step satisfies `rank (n + 1) < rank n`, and renewal is decidable. Then `renewal_within_rank_plus_one_steps` proves:

> For every `start`, some renewed transition has index `n` with `start ≤ n ≤ start + rank start`.

There are **`rank start + 1` candidate transitions** in that inclusive interval. Renewal is at the transition indexed by `n`; its resulting state is at `n + 1`. In particular, rank zero requires renewal at the next represented activity step. The more general `renewal_within_rank_bound` accepts any upper bound on the initial rank. `rank_renewal_arbitrarily_late` drops the explicit window from this result.

The proof is induction on the supplied bound. If renewal has not occurred immediately, strict descent lowers the remaining bound by at least one, and the induction hypothesis applies at the next time. The bound is conditional on all the represented activity steps occurring with the stated law. It supplies no existence proof that activity actually continues until the window's end.

**The rank is a sufficient certificate, not a universal generative primitive.** This result does not require every system to have a finite physical reserve, every operation to have a fixed positive resource cost, or every valuable process to continue forever. Stasis, arbitrarily diminishing draws or support-preserving transitions can fall outside this certificate. Such cases require a different substantive argument, rather than relabeling them to force strict Nat descent.

## 4. Recurrence does not require growing forms

The checked witness uses two configurations of the same represented activity:

- `true`: one further unrenewed activity step is supported;
- `false`: restoration is required before the next such step.

The actual history alternates `true → false → true → …`. `alternating_actual_steps` checks every edge against a fixed two-edge relation. On each nonrenewing edge, the rank decreases from one to zero. On each renewing edge, it rises from zero to one. `alternating_has_actual_unrenewed_step` verifies that the descent premise is used on an actual edge; it is not made vacuous by marking all transitions as renewal.

The same history satisfies all of the following checked results:

| Declaration | Conclusion |
|---|---|
| `alternating_renews_arbitrarily_late` | Renewal occurs after every chosen start. |
| `alternating_period_two` | The represented configuration repeats after two steps. |
| `alternating_one_restoring_form` | Every renewal repeats exactly `false → true`. |
| `alternating_restoration_raises_rank` | Renewal actually restores the specified support rank. |
| `alternating_no_new_configurations` | Every configuration is one of the first two. |
| `alternating_every_configuration_score_bounded` | Every Nat-valued score determined by this configuration has a fixed bound. |

Thus **renewal's recurrence alone does not force continually new organizational forms or unbounded configuration-based complexity**. The witness still contains indefinitely many new occurrences. It does not assert that the whole physical world has only two states, that no trace or cumulative history can grow, or that this representation contains all changes of a living system. It also does not defeat a distinct argument that changing circumstances can require innovation. The richer existing stationary renewal construction makes the same distinction while representing formation, support and aging explicitly.

The witness is a counterexample to an unrestricted *formal implication from recurrence to unbounded configuration growth*. It is not a substantive counterexample to the complete theory of 生生不息, whose biological, experiential and ethical content is not represented by two Booleans.

## 5. What this contributes, and what remains supplied

| Question | Result of this round |
|---|---|
| Formal necessity | Continued activity plus well-founded unrenewed change forces recurrent renewal. |
| Physical identification | Open for life, particular systems and humanity; requires evidence that the target's actual enabling relations satisfy an applicable certificate. |
| Sufficiency | Not established by necessity. Renewal may restore one condition while other necessary relations fail. The older renewal–closure theorem supplies sufficiency only for its explicit law. |
| Novelty and diversity | Recurrence alone does not entail unbounded growth of represented forms. Renewed occurrences and organizational innovation are distinct claims. |
| Ethical quality | Not encoded. Particular renewals can perpetuate harm or damage other continuation conditions. |
| Practical force for all intelligence | Not derived. The importance of continuation and the standing of its differentiated realizations need substantive ethical defense. Recognition, motivation and implemented preservation remain distinct. |

The universal inference this supports is therefore **dependence of ongoing realization on re-formation of its conditions**, under a defensible no-endless-unrenewed-activity premise. It gives the ethical investigation a precise dependence to identify. It does not turn necessity for an end into a universal obligation to adopt that end, nor substitute local survival for the quality of the whole continuation. Conversely, the absence of an ethical predicate in this deliberately narrow proof is an omission of representation, not a proof that the richer proposed constitutive grounding fails.

This account would change if an independently specified continuing target were shown to run indefinitely without the posited renewal while preserving all allegedly exhausting relationships. That would refute the proposed correspondence or exhaustion claim at that scope. A renewal that reliably sustains severe harmful organization would challenge an ethical identification of renewal with goodness while leaving the conditional dependence theorem intact.

## 6. Actual checking and dependency audit

**Fresh check: 7 October 2026, 12:54:00 UTC (19:54:00 Asia/Bangkok).** Lean **4.29.1**, `arm64-apple-darwin24.6.0`, compiler commit `f72c35b3f637c8c6571d353742168ab66cc22c00`. The module has 17 theorem declarations, four definitions and one named decidability instance: **22 declarations audited, every axiom dependency list empty**. There is no `sorry`, `admit`, custom axiom, `native_decide`, unsafe proof escape, classical choice, `propext` or `Quot.sound` dependency. Empty axiom lists establish this formal dependency fact, not elimination of the theorem's supplied hypotheses or mathematical background.

From the repository root, reproduce with:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/continuation-renewal-verification/check.py
```

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/continuation-renewal-verification/check.py) copies exact source bytes to a new temporary directory, sets `LEAN_PATH` to that directory, builds the module, and runs [ContinuationRenewalAudit.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewalAudit.lean). It checks that every named declaration is audited. Exact commands within the temporary directory are:

```sh
/Users/ren/.elan/bin/lean +leanprover/lean4:v4.29.1 --version
/Users/ren/.elan/bin/lean +leanprover/lean4:v4.29.1 -o ContinuationRenewal.olean ContinuationRenewal.lean
/Users/ren/.elan/bin/lean +leanprover/lean4:v4.29.1 ContinuationRenewalAudit.lean
```

The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/continuation-renewal-verification/verification.json) retains the command arguments, toolchain, full hashes and declaration list. [Compiler output](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/continuation-renewal-verification/compiler.txt) is empty with successful exit; [axiom output](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/continuation-renewal-verification/axioms.txt) records all 22 empty dependencies. Exact checked source copies are retained in the receipt's `sources/` directory. No compiled binaries or dependency installations are added to the repository.

| File | SHA-256 |
|---|---|
| `ContinuationRenewal.lean` | `8b0754f2a63414a40aab814ac962effaaab47c1bc83e0e28a5f93b5f902d4f3c` |
| `ContinuationRenewalAudit.lean` | `2bf35908667f659a786df7396cf495de9edef9c439e3ea7ebad3dd54f1bc807d` |
| `lean-toolchain` | `7dc000621e0046d1aada809e2b7177e64454645cf4c741e9daaf79c99ec2e7a2` |

This completes only the assigned formal support. The governing universal normative investigation remains open, and the next central study must integrate this dependence with affirmative ethical argument, substantive counterreview and independently assessed evidence.
