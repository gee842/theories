# Prefix safety, global obligations and finite-program admission in Lean

7 October 2026. AI-authored correspondence note for the proof requirement in the current continuation. This note accompanies [the hand argument](COMPLETION-WARRANT-MATH.md) and [the checked Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/PrefixSafety.lean). It adds formal verification; it does not supply a universal ethical justification or establish the generative root's exclusive metaphysical priority.

## Representation and exact coverage

The Lean namespace is `CompletionWarrant.PrefixSafety`. `Trace A` is the full function type `Nat → A`. `SamePrefix n a b` means agreement at every position less than `n`. The results quantify over every natural length and every infinite trace, rather than enumerating a finite collection of executions.

`PrefixOpen U` requires that every point of `U` have a finite-prefix cylinder contained in `U`. This topology is specified independently of the property tested. The file proves openness of the empty and universal sets, arbitrary indexed unions, binary intersections and cylinders. `PrefixClosed K` then means its complement is open. `TopologicalClosure K` is the intersection of all closed supersets. The equivalence between finite refutation and complement openness consequently unfolds the relevant definitions; the additional closure characterization and leastness theorems supply the substantive formal content.

| Hand result | Lean correspondence | Exact scope |
|---|---|---|
| W3: finite bad prefixes, closedness, every prefix extendible into the property | `finiteRefutable_iff_closed`, `finiteRefutable_iff_prefixClosure` | Any alphabet; no finite-alphabet or compactness premise. |
| W3: the prefix-compatible class is the least closed enlargement | `prefixClosure_closed`, `prefixClosure_least`, `topologicalClosure_iff_prefixClosure`, `prefixClosure_idempotent` | All infinite traces. The topology is the explicit cylinder topology, not an imported topology library. |
| Infinite boundary of finite-prefix rules | `boundary_closed` | The predicate at length `n` must depend only on those first `n` symbols; that locality hypothesis is explicit. |
| A finite dead end does not guarantee an infinite branch | `deadEnd_boundary_empty` | The allowed lengths are at most one, so no infinite trace has every prefix allowed. |
| W4: finite unary histories exclude their increasing-chain limit | `unary_finite_directed`, `unary_finite_supremum_infinity`, `unary_finite_not_directedClosed`, `unary_finite_not_finiteRefutable` | An independent, exact prefix-length carrier: `some n` denotes the unary word of length `n`; `none` denotes its infinite continuation. Its identification with the general ideal carrier is a separate correspondence. |
| W4: a termination-event property on infinite traces | `terminationEvent_closure_all`, `terminationEvent_not_finiteRefutable` | `EventuallyTrue` means at least one designated event occurs. This is an additional infinite-trace example, not a replacement of the unary finite-plus-infinite carrier. |
| W5: infinitely many designated events | `recurrence_closure_all`, `recurrence_not_finiteRefutable`, `recurrence_not_closed` | `Recurs a` is `∀ n, ∃ m ≥ n, a m = true`. Every finite prefix has a recurring continuation; the all-false trace fails recurrence. |
| W6: no countable partial enumeration covers all binary traces | `diagonal_not_represented` | Arbitrary `Nat → Option (Trace Bool)`, without assuming effective enumeration or decidability of totality. |
| W6: actual finite binary program descriptions are countable | `bitCode_injective`, `bitDecode_bitCode`, `finitePrograms_miss_some_trace` | Every `List Bool` is encoded injectively into `Nat`; the partial decoder is defined classically. Every interpretation of those descriptions misses some trace. |
| W6: program admission has full finite-prefix closure but is not finitely refutable | `finitePrograms_not_finiteRefutable` | The interpretation must realize every finite prefix. `literalOutput_realizes_prefixes` verifies a concrete literal-then-zero interpretation; `contains_literals_realizes_prefixes` states the exact interface for a richer interpretation. |

The W6 proof does not define computability as membership in an arbitrary list. It proves the stronger general obstruction for *every* interpretation of finite binary descriptions. Applying it to a particular universal programming language still requires a faithful account of that language's descriptions and total binary outputs, and the ability to produce a given finite literal prefix followed by zeros. No particular Turing-machine formalization is imported or claimed checked here. The diagonal may be noncomputable; the proof is not an algorithm for deciding which descriptions have total outputs.

## Finite proof terms and finite execution evidence differ

`allTrue_recurs` is a finite Lean proof of an infinite recurrence property. The same file proves that the *class of all recurring traces* has no finite bad-prefix characterization. Therefore neither W3 nor W5 implies that Lean cannot prove liveness, or that an infinitary obligation requires an infinite proof term. A finite derivation from a specified generating rule can prove a claim about every future position. A prefix of one observed execution has a different evidential role.

The recurrence predicate can represent repeated service only after the interpretation of events is established. The formal predicate does not justify that service norm, its priority, or the distribution of actual consequences. The representation separates finite information and continuing histories as related descriptions of one process, without postulating distinct ethical and causal realities. For the repository's current priority, the precise contribution is a preservation boundary: finite-prefix compatibility alone cannot preserve an independently warranted ongoing obligation.

## Validation

Direct compilation with `lean +leanprover/lean4:v4.29.1` succeeded after the final edit. The source imports only `Std`; all 50 named theorems have `#print axioms` entries. The audit reports only Lean's standard `propext`, `Classical.choice` and `Quot.sound` dependencies where used, with several theorems having no axiom dependencies. No custom axioms, admitted goals, `sorry`, or `native_decide` occur in the proof source. These are generalized kernel-checked statements, not finite execution tests. The final integrated runner should retain the compiler output and source hashes alongside the other completion modules.
