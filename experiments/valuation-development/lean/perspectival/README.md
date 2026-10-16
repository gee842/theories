# Present and future fidelity of a perspectival field

7 October 2026. AI-authored supporting study for [Ren's direction](../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/PERSPECTIVAL-GOOD-AND-TRAJECTORIES.md). **Status: 25 Lean-checked conditional mathematical theorems, including action-word alternatives and a concrete shared-law witness. This supplies a recognition-correspondence test; it supplies no ethical warrant.**

The universal inference supported is **whole continuation → justified ethical comparison → recognition by a formed perspective → practical response**. This study examines only the third connection's representational condition: which differences must a perspective preserve if it claims to recognize a specified comparison of continuing consequences? It neither fixes the ethical comparison nor establishes motivation or compliance.

## Result and genealogy

The existing [GeneratedSelf.lean](../../../integrated-correction/general-framework/generative-basis/lean/GeneratedSelf.lean) already proves `exact_summary_exists_iff`: a record can exactly represent finite continuation-feasibility profiles precisely when it does not merge different profiles. It also proves those profiles update consistently under common extensions. Those results retain their original scope. We do not present factorization itself as a new foundational discovery.

The present addition is a **temporal test for an arbitrary proposed current field and an independently specified binary comparison**. No scalar ordering, total order, distance metric or probability distribution is required. A relation can preserve incomparability, directed dependency or a partial comparison.

Write `o : S → O` for the selected readout of a perspective in the whole modeled configuration, `f : S → S` for the supplied continuation law, and `R : S → S → Prop` for the comparison to be preserved. Distinct entries of `S` may include records, relationships and selective dispositions that participate in the subsequent update. This does not put a subject and an environment into separate foundational domains.

1. **Current fidelity:** some relation on `O` exactly preserves `R` iff replacing either argument by an equal-readout configuration leaves `R` unchanged. The file calls this *saturation*. This binary-relation factorization restates the inherited discipline for the present application.
2. **Dynamic closure:** readout equality survives every finite continuation under `f` iff it survives one transition. This is `step_congruence_iff_futures`. It applies to every state of the stated domain; it does not infer the condition from a few observed trajectories.
3. **Trajectory fidelity:** current saturation together with dynamic closure is sufficient to represent the supplied comparison at every finite horizon using the initial readout. The exact weaker requirement for this particular `R` is saturation of every future comparison, given by `future_representation_exists_iff`. Full dynamic closure is not claimed necessary for a comparison that ignores some readout differences.
4. **An omitted consequence is an obstruction:** if equal current readouts admit actual continuations disagreeing on that supplied comparison, no decoder using only that current readout can represent it exactly. Changing a decoder while keeping the same informational distinctions cannot fix this failure.

The `Pooled` decoder constructs a relation by existentially collecting actual representatives. It avoids choice axioms and proves existence at the analysis level. It does not prove that a finite organism can compute, acquire or use the decoder. Exactness is a deliberately strong target; adequate uncertainty-aware and approximate representations require separate contracts.

## Comparing several supplied trajectories

The fixed-law theorem predicts a closed continuation from each state. Five additional results make alternatives explicit: `step : S → A → S` supplies one deterministic action-indexed law and `A` supplies its repertoire. `follow step word x` follows a specified finite word from `x`. These labels need not name the choices of a fundamentally separate controller; their meaning and availability remain local correspondence obligations within one process.

`action_congruence_iff_words` proves that readout equality survives every finite **common** word exactly when every single action preserves it. With current comparison saturation, `current_and_action_give_word_representation` then constructs an exact comparison indexed by **two separately specified words**, one for each side. Replacing an initial state by an equal-readout state must preserve the comparison under the same word for that side. The two compared words themselves may differ, including their lengths. `word_representation_exists_iff` states the weaker necessary-and-sufficient condition for the particular supplied comparison: every such word-pair comparison must be saturated.

This is a representation contract for many candidate trajectories, not a proof that their alternatives are physically available, ethically permissible or selectable by an implemented controller. The action law is total; an application with blocked actions must represent blocked/failure outcomes or justify its domain and repertoire. The uniform condition cannot be inferred from a few actual words. Nor does agreement under common words establish that two autonomous policies will emit the same words: the fixed-law result applies after such internal selection has been included in its state and law. No basin, probability over choices, attractor or ethical gradient is derived.

## Shared-law witness

The synthetic state has an enacted-cycle count, a capacity enabling further cycles, and the current route for using/restoring that capacity. One common deterministic law updates all three. Under the restored route a cycle restores the capacity it uses. Under the un-restored route each cycle consumes one unit. Feedback changes the latter route when its last capacity unit is consumed; the route is then restored, but zero capacity prevents a new cycle. This feedback recipe and its timing are explicit local inputs, not a derivation of learning or self-modification.

Both seeds start with count 0 and capacity 3, differing only in route. The modeled quantities are descriptive. No ethical verdict is attached to their names or values.

| Horizon | Restored route: count / capacity | Initially un-restored route: count / capacity | Current route in second history |
|---|---|---|---|
| 0 | 0 / 3 | 0 / 3 | Un-restored |
| 1 | 1 / 3 | 1 / 2 | Un-restored |
| 2 | 2 / 3 | 2 / 1 | Un-restored |
| 3 | 3 / 3 | 3 / 0 | Restored |
| 4 | 4 / 3 | 3 / 0 | Restored |

The count-and-capacity readout represents **current** capacity comparison exactly, yet its initially identical readings cannot determine the next capacity comparison: it omits the governing route. A count-only history remains identical through three cycles even while continuation capacity diverges. By horizon 3 the routes also agree, but the already consumed capacity does not return. Adding the governing route to the count-and-capacity readout meets the transition condition in this specific law, so its capacity comparisons are recoverable at every finite horizon. This `routeView` re-encodes **all three state coordinates**: it is an explicit full-state sufficient witness. It does not derive a compressed or learned field.

This is a concrete failure of a proposed abstraction to preserve a specified descriptive relationship. It does not freely toggle an ethical predicate, refute the fuller generative theory, prove an attractor basin, establish cancer dynamics, or show that ethical damage must eventually punish its initiator. The restoration route's availability and the capacity interpretation would need independent correspondence evidence in an application. A trajectory can also be ethically adverse without ever reducing the selected process's count; this witness does not address that ethical case.

## Inputs and interpretation

| Item | Exact formal role | Explanatory status |
|---|---|---|
| `S`, `O` | Arbitrary type-valued domains | No physical implementation or universal ontology derived. A model may restrict `S` to a closed reachable domain before applying the result. |
| `step` | Total deterministic update of `S` | The supplied local law can include endogenous choice and changes of disposition. Its formation is not proved. The stochastic and nondeterministic cases are not covered. |
| Action-indexed `step`, `A`, words | Total map `S → A → S`; supplied repertoire and finite label sequences | The five action-word results quantify over these inputs. Physical availability, action meaning and an implementing controller are not derived. Separate words specify the alternatives on the two sides. |
| `observe` | Readout from the modeled configuration | A specified representation, not by itself a physically formed cognitive mechanism. Changing field parameters can be included in `S`; their formation is still a correspondence obligation. |
| `R` | Any binary comparison | No ethical interpretation, completeness, transitivity, additivity or order axioms assumed. If interpreted ethically, its warrant remains independently to be defended. |
| Saturation | Comparison agrees on both readout fibers | Required for exact current recognition. This says nothing about endorsing the comparison. |
| Step congruence | Equal readouts have equal next readouts | Sufficient for all future readout prediction and, together with saturation, future comparison fidelity. Not universally necessary for one selected comparison. |
| `C` / `Pooled` | Relation reproducing comparisons from readouts | Existential correctness, not acquired knowledge or implemented use. |

Actual consequence reach, attention/access, endorsement and warranted appraisal remain different relations within the same unfolding. This file represents access by `observe` and only tests correspondence to the separately supplied `R`. It contains no model of attention allocation, experienced good or warranted preference. If an intelligence represents a justified whole comparison perfectly while declining to act on it, these theorems neither exclude that history nor provide the missing practical argument.

If the intended comparison depends on how a condition was formed, `S` must retain the relevant history or a sufficient account of it. Two identical present inventories need not preserve different undertakings, imposed losses or acquired responsibilities. The theorem cannot restore a ground already omitted from its supplied state and comparison.

No theorem here establishes Ren's stronger no-assumptions objective. Absence of logical axioms in proof dependencies is different from deriving the model's mathematical representation, continuation law or ethical premises without supplied content.

## Verification and reproduction

[TrajectoryFidelity.lean](TrajectoryFidelity.lean) contains 25 named theorems. [Audit.lean](Audit.lean) audits every one; [verification-output.txt](verification-output.txt) preserves the actual compiler version, all dependency results and SHA-256 source hashes. The files use core Lean 4.29.1 inherited from [the parent toolchain](../lean-toolchain), with no Mathlib or imported project module. All 25 audited theorem dependencies are empty. There are no `sorry`, custom `axiom`, or `native_decide` declarations.

From the repository root:

```sh
sh experiments/valuation-development/lean/perspectival/verify.sh
```

The script compiles the source into a temporary directory, checks the complete audit and removes generated objects. It does not install dependencies or rerun the unchanged historical valuation results. Compilation checks formal validity, not physical correspondence or universal ethical truth.
