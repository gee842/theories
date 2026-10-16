# Joint continuation and the scope of complete factual preservation

7 October 2026. AI-authored mathematical support for Ren's request to continue the complete generative/degenerative theory under **0 axiom**. The stronger requirement is retained: no hidden premises, no custom Lean axioms and zero assumptions are different achievements. This note supplies checked representation results for the universal investigation; it does not supply first ethical warrant or announce that requirement met.

**本轮推进：**完整判断必须保留“哪些实现能够在同一延续中共同发生”，仅列出每一项分别可能发生会遗漏真实损失。同时，“保存所有真实事实”不能直接充当“生成而不损失”的定义：如果事实语言也包含每项事实的否定，要求原有真事实全部保持，就排除了同一意义下新事实由假变真。完整描述与有根据的非损失比较必须分别说明；这个区别仍发生在同一展开之内。

## 1. The precise universal inference being tested

The broader investigation asks whether the whole generative account can justify generative/degenerative classification, mixed comparisons and practical force without a separately assumed ethical ranking. Before testing that normative inference, its claimed whole coverage must not silently discard jointly realizable relations or give a selected inventory the name “all facts.”

The [existing comparison audit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean) already distinguishes positive relevance, a no-loss comparison principle, practical articulation and selection coherence. Its opposite mixed appraisals remain valid at their stated scope. The [whole restriction audit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean) already handles descent of local comparisons to a whole relation. The [situated continuation proof](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean) already requires dependencies to share one actual history. None is restarted here.

The new bridge is **adequate whole relational representation → justified claim of represented preservation or loss**. The results make two substantive application obligations exact:

1. A list of individually possible realizations does not certify preservation of their jointly realizable configurations.
2. Preservation of every signed fact differs from preservation of the realization grounds relevant to a proposed favorable comparison. The latter inventory requires its own correspondence and eventual normative defense.

This is support for the universal inference, not its replacement by a set-inclusion ethics. No predicate named good, better, reason, required or selected occurs in the module.

## 2. Scope and correspondence

The [new Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean) supplies a `Continuations History Claim` interface with two fields:

- `feasible h`: this represented whole continuation is admitted at the declared comparison scope;
- `realized h c`: the independently identified claim has its stated realization in that continuation.

These are analytical descriptions within one unfolding. Histories can include formation, intermediate effects, finite fulfillment, support, endings and later outcomes. Claims can concern relationships across time and across differentiated positions. The theorem does not reduce them to independent owners, scalar resources or endpoint counts. Conversely, merely permitting a rich `History` type does not establish that an application actually represents all relevant relations.

The old and new history types may differ, but the claim type and each claim's denotation must be stable. A relabeling, duplicated label or altered meaning does not create a new realization. New actual relations can require an expanded common language and a renewed correspondence audit. The full-history theory must determine which observed continuations are admitted; the formal interface does not derive their laws or guarantee empirical completeness.

For a bundle `B : Claim → Prop`, `Jointly C B` means that **one feasible history** realizes every claim in B. This is an existential possibility claim. It does not claim that the history is actual, that its probability is unchanged, or that a situated action can guarantee it.

## 3. Exact joint-preservation theorem

`whole_profile_preservation_iff_joint_bundle_preservation` proves the equivalence of these statements:

**Whole-profile preservation.** For every admitted old history h, there is one admitted new history k such that every represented realization in h also occurs in k.

**Joint-bundle preservation.** Every bundle jointly realized by one admitted old history is jointly realized by one admitted new history.

The forward proof carries every member of a bundle through the same matching new history. The reverse proof takes the bundle consisting of all claims realized by a particular old history. That bundle is jointly realized by that very history; no impossible combination or independent simultaneous-choice assumption is inserted.

The range over **all** bundles is explicit, potentially including infinite profiles. Agreement for each singleton, each observed finite test or a chosen finite list is not the hypothesis proved sufficient here. There is no compactness theorem silently converting such approximations into full-profile preservation.

The quantifier order is `∀ old, ∃ new, ∀ claim`. It does not become `∃ causal intervention, ∀ old`, nor a selection mechanism producing a match. `whole_profile_preservation_composes` composes two matches through the **same intermediate history**. `faithful_history_transport_preserves_joint_bundles` gives a sufficient concrete certificate when an actual mapping of histories is supplied and proved feasible and faithful. It does not prove such a map exists or is physically implementable.

These are constructive inference results over supplied representations. They do not justify preserving every admitted bundle, compare gains with losses, or decide whether any remaining alternative is permissible.

## 4. A loss invisible to marginal inventories

The local witness uses one finite event law and one common initial configuration. From the initial configuration, an event retains or releases a coupling. With the coupling retained, the law permits left activation, right activation or their joint activation. After release, either activation can occur separately, while joint activation does not fit the represented opportunity. The complete recorded history retains both transitions and their reached configurations.

The two claim names designate activation in differentiated positions of this one configuration. They are not autonomous subjects and do not encode ethical signs. The local law is supplied; the example is neither an empirical assertion about all couplings nor a verdict about ending any actual relationship. Other gains and losses of release are not represented.

Although the history object retains both transitions, the claim profile selects only these two final activations. It is not a complete whole-consequence profile; retaining intermediate states in a data type does not make this selected comparison cover their significance.

`same_marginal_realizations_can_lose_a_joint_bundle` checks that:

- left activation is possible both before and after release;
- right activation is possible both before and after release;
- both activations are jointly realizable in one retained-coupling history;
- no released-coupling history under the same event law realizes both.

Thus the two marginal capability inventories agree exactly while joint possibility differs. This is a genuine omission in that marginal representation, not a refutation of a fuller nondual theory and not a freely toggled moral predicate. It justifies retaining the relational configuration when assessing an alleged absence of represented loss.

The conclusion remains finite and conditional. A larger scope might include later reunion, alternative support or further consequences, and its feasibility relation would need to represent them. The witness does not prove irreversible physical loss outside its specified opportunity.

## 5. Why preservation of all facts cannot define strict enrichment

`complement_closed_preservation_excludes_new_realization` supplies a second, general audit. Assume:

1. one old and one new history are feasible;
2. the shared claim language has a complement operation;
3. on feasible histories, realization of a claim's complement means exactly nonrealization of that claim;
4. the new matched history retains every claim realized in the old history.

Then there cannot be a represented claim realized in the new history and not realized in the old history. If such a claim existed, its complement would have been realized before, preservation would carry the complement forward, and the new history would both realize and fail to realize the original claim.

The theorem excludes an explicit strict-extension witness constructively. It does not silently use excluded middle to claim unconditional elimination of double negation. Its axiom dependency report is empty, while its complement, feasibility and preservation premises remain visible in the checked signature.

**Temporal qualification.** “q is absent at time t₀” and “q is present at time t₁” can both be true in one complete evolving history. They are differently indexed claims, not a claim and its complement at the same role. The theorem therefore does not say that rich true histories cannot contain growth, that every change contradicts the past, or that remembering an earlier absence prevents a later realization. A comparison must hold the temporal and relational denotation of each claim fixed. It also cannot obtain “growth” merely by renaming the claim or moving its index.

The finding concerns a proposed *comparison rule*: if complete signed factual profiles are ordered by retaining every truth at the same comparative role, strict novelty at that role is excluded. A favorable enrichment criterion must identify what it preserves through transformation, rather than treating the retention of every old positive and negative fact as the criterion. Descriptive completeness can coexist with transformation; it does not itself identify which transformations count favorably.

The theorem does not prove that a selected realization language is arbitrary or that its selection requires an independent external moral realm. It exposes the explanatory obligation the generative account must discharge internally: why these relationships constitute the relevant realization and loss, with omitted adverse consequences recovered in the whole account. Choosing only favorable terms and calling the result complete would leave that obligation unmet.

## 6. Actual verification and dependency audit

The [focused checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_joint_classification.py) compiled a fresh source snapshot using **Lean 4.29.1**, generated and ran all explicit declaration axiom audits, and emitted exact theorem signatures. The [source-bound receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/joint-classification-verification.json) preserves the successful final run `joint-classification-checks/20261007T165011.097826Z`, source/checker/binary hashes, commands, raw outputs and source-stability checks. No concurrent session's compiler receipt is reused.

Five new named theorems and 21 explicit declarations passed; **every axiom dependency report is empty**. The checker now rejects every nonempty dependency list, including standard `propext`, `Quot.sound` and `Classical.choice`, rather than allowing a standard-axiom exception. The successful source contains no custom axiom, proof hole, unsafe declaration or unchecked native evaluation. Lean-generated constructors, projections and deriving output were kernel checked with the module but are not counted as separate explicit declaration audits.

The first successful run, retained at `joint-classification-checks/20261007T164403.182274Z`, used a proposition-valued pattern definition for `Step` whose compiled form depended on `propext`. The final source instead presents the same seven permitted edges as inductive constructors and proves the impossible joint branch by constructor inversion. This removes an avoidable formal dependency without changing the represented law or weakening the claim. The earlier source, receipt and logs remain preserved at their original scope. An intervening empty-dependency run is also retained; the final run additionally checks the strengthened checker itself.

The declaration scanner is reused from the existing capacity checker and copied into the retained run with its hash. This is a fresh mathematical check, not an independent review or new empirical experiment. The note's hand explanations describe the compiled results; they do not substitute for their proofs.

The formal and substantive dependency ledger remains:

| Dependency | Status in this work |
|---|---|
| Lean's logic, types and kernel | Formal background, retained and reported; the final explicit declarations have no axiom dependencies. |
| Admitted history domains and stable realization predicates | Supplied representation; application correspondence is not proved by the interface. |
| Full joint-bundle range | Explicit theorem range; not derived from finite observations or measurements. |
| Exact complement interpretation | Explicit premise only for the complement theorem; no universal scientific completeness claim. |
| Common finite event law and opportunity window | Supplied local witness, not a law of all real generation. |
| Preservation's favorable significance and the relevance of each selected realization | Not supplied as a moral axiom, and not concluded; belongs to the pending substantive grounding. |
| Actual recognition, motivation, control and implementation | Outside these existential comparison results. |

## 7. Integration consequence and next test

The results improve the proposed complete theory's representation discipline: actual histories, jointly realizable possibilities and complete factual description must be carried explicitly, while a judgment of relevant enrichment or degeneration still requires explanation of its grounds. They neither reinstate the earlier axiom route as the current objective nor turn the present unresolved normative inference into a proof of impossibility.

The next central test should explain **which continuing and newly formed relationships constitute favorable whole realization through change, and why their practical significance follows**, while retaining joint feasibility, intermediate losses, finite completion and cross-scope conflict. A proposed criterion should be tested against the same complete history with a substantive rival; it should not merely change an unconstrained ethical predicate or infer moral goodness from the profile theorem. In particular, richer whole information can remove a spurious marginal tie without thereby deciding every mixed ethical comparison.
