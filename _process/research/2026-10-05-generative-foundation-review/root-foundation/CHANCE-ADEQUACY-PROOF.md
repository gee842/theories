# Actual continuation and the chance constraint: checked bridge

8 October 2026. AI-authored formal continuation following Ren's request to add Lean proof. **Eight new theorems / fourteen explicit declaration audits** pass Lean 4.29.1. The earlier [read-only audit](CHANCE-ADEQUACY-PROOF-AUDIT.md) remains unchanged at its historical zero-new-proof scope. This module supplies the previously missing event-level continuation → finite chance constraint connection; it does not prove that every old arrangement is entitled to continuation or complete the general ethical allocation of initial chances.

The [source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ChanceAdequacy.lean) imports only `Std`. No earlier project module is rebuilt or added to the new counts. Existing [J3](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PRACTICAL-JUDGMENT.md#4-谁承担什么--allocating-responsibilities), [same-ticket improvement](CROSSED-CLAIMS-PROOF.md), [settlement-history analysis](CHANCE-REVISION-INTEGRATION.md) and [positive-chance diagnostic](CHANCE-GROUNDING-PROOF.md) retain their own scope. The last new control specializes the distinction between probability and task fidelity to this bridge; it is not a newly discovered general insufficiency of marginal information.

## The represented relationship

A finite list `domain : List Ω` enumerates **warrantedly paired implementation conditions**. For a given entry, old and proposed implementations are compared under relevant common support conditions, failures and random seeds. The old and new acts need not both have occurred. This pairing is a substantive correspondence obligation: matching observed marginal probabilities does not permit arbitrarily inventing a coupling.

`weight : Ω → Nat` assigns natural event mass. It represents a supplied finite rational probability law, not the ethical importance of a person, a loss-severity coefficient or an observed frequency automatically promoted into a future probability. The same enumeration and weights are used on both sides. The list implementation counts repeated entries repeatedly; a faithful application must avoid unintentionally duplicating event mass. The generic statements allow arbitrary lists, including empty ones.

Three Boolean predicates identify the actual support content being compared:

- `demand h`: the specified protection requirement applies in condition `h` and within the relevant window;
- `oldWorks h`: the old route would still provide that support under the paired conditions;
- `newWorks h`: the proposed implementation provides it.

`target demand oldWorks h` is their conjunction `demand h && oldWorks h`. `Fulfilled` requires the new implementation to provide support **at every represented condition in which this target holds**. It is not defined as a probability inequality. Normative standing, the relevant demand, the scope of the undertaking, justified release and contrary reasons remain independently warranted inputs. A naturally unavailable old success is not asserted into existence by this definition.

`mass domain weight event` sums the weights at entries where the event holds. `total` uses the event that is always true. Empty domains and zero total remain legitimate algebraic inputs, but they receive no probability interpretation. The chance wrapper explicitly assumes and retains a positive total.

## Eight checked results

| Theorem | Exact checked content |
|---|---|
| `mass_monotone` | Inclusion at every represented condition implies nondecreasing event mass for any natural nonnegative weighting |
| `positive_added_event_strictly_increases_mass` | Under that inclusion, one newly covered represented condition of strictly positive weight gives a strict mass increase |
| `dirac_mass_positive_iff` | A single-condition natural weighting yields positive event mass exactly when that condition is represented and the event holds there |
| `all_weights_preserve_mass_iff` | Mass preservation for **every** natural nonnegative weighting is equivalent to pointwise inclusion on the represented domain; the converse uses the Dirac test |
| `fulfillment_gives_chance_floor` | A fulfilled pointwise undertaking and one common positive total imply that the target's mass is no greater than the new support mass, which is no greater than that total |
| `repair_covers_target_and_candidate` | The event-level union of the protected target and a candidate covers both, and fulfills this specified target |
| `repair_adds_positive_new_protection` | If the candidate covers a positive-weight condition outside the old target, this union has strictly greater mass than the old target |
| `positive_chance_can_miss_due_protection` | In a two-condition law of total mass two, the old target and new support each have mass one, but the new implementation misses a due old success at a condition of weight one |

The fifth theorem retains the exact numerator bounds

\[
0 < N,\qquad M(\mathrm{target})\leq M(\mathrm{newWorks})\leq N.
\]

These are checked natural-number statements with a common positive denominator. The source does not declare a general real-valued measure theorem. Its probability interpretation is limited to the supplied finite rational event law and the correspondence just described.

The fourth theorem does not require actual circumstances to admit arbitrary interventions on their probabilities. It is a **representation criterion**: when the entire natural-weight test family is available mathematically, a missing represented condition is detectable. Preservation under one actual law is weaker. The final control makes that distinction concrete without relying on a zero-weight exception: support under one positive-weight condition has been replaced by success under a different condition. Receiving a positive chance, even the same chance as before, does not establish fulfillment of the specific undertaking. This is not a case in which the new marginal probability has decreased.

## Constructive repair and its implementation boundary

`repair` is the Boolean event `target || candidate`. Its checked content is constructive at the level of protection profiles: the original target and the candidate's successes are included. It does not command preservation of every old activity or prove that both physical routes can run together.

An application needs a permitted, timely implementation realizing this profile. Parallel provision may require extra capacity; combining routes may change their failures or remove the very support being preserved. Conditional routing cannot assume advance knowledge of a future old success. Evidence for compatible provision or an observable, authorized switching mechanism is therefore necessary. An unrealizable disjunction is not a completed repair.

The strict-increase theorem also does not independently establish the ethical value of every added event. It assumes a candidate success outside the existing target. For an application claiming an additional warranted need is served, that need and its positive significance must be established; the theorem does not silently label any increase as good. Real burdens and support lost elsewhere remain part of the whole comparison.

## What this closes, and what it leaves supplied

Once J3 and correspondence establish a pointwise continuation undertaking, the mathematical argument derives a necessary finite chance constraint from actual support content. No ethical numerical floor is inserted into the definition of fulfillment. The counterexample blocks the reverse inference from a preserved or merely positive success probability to that pointwise undertaking.

The argument does not establish that every probabilistic undertaking is pointwise. A promise whose warranted content is only a particular lottery is a different target. Likewise, proving a separate event inclusion for each affected position does not itself demonstrate a single jointly feasible implementation. Authority, coupling, complete condition coverage, faithful probability law, implementation feasibility and the meaning of the undertaking remain correspondence obligations, explained further in the [application note](CHANCE-ADEQUACY-CORRESPONDENCE.md).

Thus the new result addresses the specifically identified gap after the prior audit. It does not settle initial chance adequacy where no protected prior route exists, show that preserving old chances makes an arrangement fully fair, or prove universal behavior convergence. The conditions of justified support and the formal inference remain distinct parts of the same relational account.

## Actual verification and freeze

The [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_chance_adequacy.py) compiles unchanged source bytes in an isolated temporary import directory using Lean 4.29.1. It retains every theorem signature and requests `#print axioms` for every explicit declaration. The [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/chance-adequacy-verification.json) binds [run `20261008T113537.047137Z`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/chance-adequacy-checks/20261008T113537.047137Z/verification.json).

There are **8 new theorems / 14 declaration audits, 11 retained artifacts, and no inherited project recompilation**. Six declarations have empty axiom dependencies; two use only `propext`; six use `propext` and `Quot.sound`. No project-specific axiom, proof hole, native-decision escape or skipped kernel checking is admitted. Two additional application examples check the two-condition union's mass and the empty-domain total; they are retained separately and not counted as theorems.

The initial compile left a simple positive-sum goal in the Dirac proof unresolved. Adding the arithmetic tactic closed that goal without changing a statement. The failed snapshot is retained alongside the successful frozen run.

- Source SHA-256: `501a26f1561c78fb552a550700fc730c296e6005cde5a0f0d2e0cb9ec11a8c41`.
- Dedicated checker SHA-256: `be57a3df87be9787c352821ab61a9817520fbc013f97995b9b807244fd030472`.
- Shared scanner SHA-256: `b9f56e1700c03f0019a486d0f3c097f70c2ce20414da9e7b231131b8ed4a8308`.

The source and checker are frozen. This report describes actual kernel checking, not a new empirical probability measurement or a machine proof of the normative premises.
