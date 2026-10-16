# From local joining to one common holding configuration

8 October 2026, Asia/Bangkok. AI-authored continuation of [Ren’s instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#继续跨分支检验--continue-the-cross-branch-test). The [preceding jointness study](EXPLANATORY-JOINTNESS-INTEGRATION.md) proved nodewise plan lifting and left global cross-branch sharing open. This round addresses **accurate local joint certificates → global compatibility → an admitted acquisition history**, and tests the inference from bounded joint questions to unrestricted joint coverage.

**Result / 结果。** If a part’s support footprint covers the support of both admitted children, and sibling footprints exclude shared exclusive support, every finite realized plan has distinct requested supports contained in its root footprint. In a concrete footprint relation the converse holds: such a request list has a local decomposition certificate. For a fixed-access, persistent-holding acquisition law, this is equivalent to a finite history ending with every requested support held. The previous exact-code lifting theorem therefore gains a global holding consequence under these explicit additional conditions.

**Boundary / 边界。** Immediate sibling separation alone can certify a tree with the same support in distant leaves. Containment alone can admit duplicate siblings. Both failures and a repaired three-support positive case are checked. A separate shared-capacity mechanism admits every demand of size at most n in both capacity-n and capacity-(n+1) arrangements, while demand n+1 distinguishes them. Thus a fixed upper bound on joint tests does not generally warrant arbitrary joint feasibility. This does not refute richer nested tests or a known capacity law.

**37 new Lean theorems (11 + 11 + 15), 184 audits including 147 inherited.** New dependencies: 4 empty, 3 `propext` only, 28 `propext`/`Quot.sound`, 2 additionally `Classical.choice`. Full totals: 115 empty, 69 standard lists. No custom postulates or proof holes. Supporting lemmas count as theorems, not independent mathematical discoveries.

## 1. Why the target requires a connection across branches

Suppose an explanation undertakes to say whether all specified activities can hold their required support together. It must answer about one admitted common condition. A list of successful local checks does not settle that target if different checks reuse the same exclusive position. This is not a demand that every limited explanation reconstruct the whole world. It follows from the selected common-realization target and is tested by actual occupancy laws below.

The roles are related within one configuration: a request identifies a required support position; acquisition changes the shared occupancy record; already occupied positions restrict later acquisitions. A footprint describes which positions the subplan may require. It is an analytical summary of these relations, not a separate class of fundamentally external resources. In particular, the model supplies the repertoire, access, exclusive-holding and persistence laws. It does not derive their universal existence.

For generative alignment, this supplies a factual adequacy requirement when comparing jointly realizable plans: separately feasible opportunities must not be counted as a jointly realizable whole without preserving their interaction. It supplies no new ethical ranking, G0 derivation, responsibility assignment or universal obligation. The already completed normative route retains its separate warrant.

## 2. Local conditions that propagate through the whole finite plan

`ExplanatoryFootprints` reuses the previous `Plan` and `Realizes` definitions. A leaf requests a **list** of supports, so repetition is retained rather than erased by set union. `Supported F s xs` requires that the leaf list has no duplicates and that every requested position belongs to the footprint `F s`.

The additional generic premises are:

- `Within F J`: each admitted child footprint is included in the whole’s footprint.
- `Separate F J`: the two child footprints of an admitted joint pair never contain the same exclusive support.

`realized_requests_within` inductively propagates membership from each leaf to the root. `realized_requests_nodup` uses that propagation at each branching point to exclude a support appearing in both descendant request lists. These combine in `realized_requests_supported` for every finite plan, not just a bounded collection of enumerated trees.

The premises are sufficient and their omission admits genuine failures; neither is proved individually necessary for every successful particular plan. Footprints may overapproximate the actual requests, so two overlapping upper bounds do not by themselves prove that their activities cannot coexist. The theorem certifies a sufficient separation, and a more precise relation can accept cases that these coarse bounds fail to certify.

`code_plan_has_global_support` connects this result to the preceding `joint_plan_lifts`: exact reduced code readings, joint compactness, a correctly read leaf specification and the two native footprint laws jointly yield a global distinct-support list. Compactness is inherited only for this arbitrary coding interface. Direct native footprint composition below does not require compactness or classical choice.

## 3. A complete local criterion for the specified footprint model

For states that are lists of supports, `joint whole left right` means that both child lists are contained in the parent list and their memberships are disjoint. The parent may include unused positions; this is not required to be an exact partition of all its contents.

`realize_iff_supported` proves both directions: a finite plan is realizable exactly when its flattened requests have no duplicates and are included in the root. For the reverse direction, each internal child receives the list of all requests below that child. Thus the certificate actually carries the descendant content needed for compositional checking.

The same criterion proves reassociation and permutation invariance of feasibility in this model. Changing the tree’s grouping does not change its flattened requests; permuting requests preserves their membership and absence of duplicates. These are not claims that every earlier generic joint relation is associative, or that any real scheduling order works. They are consequences of this specified relation and are limited to support feasibility.

## 4. From certificates to a history with common final holding

`ExplanatoryCoexistence.process available` has one occupancy list. Acquiring `a` requires `a` to be available and absent from the current occupied list, then appends it. No acquisition releases a prior holding, changes access or creates a new support position.

`trace_iff_admissible` gives an exact characterization from an arbitrary initial occupancy: a complete requested acquisition list is admitted if and only if it has no duplicates, all requests are available, none is initially occupied, and the final record is the initial record followed by those requests. `final_retains_all_requests` checks that every request is held in that final configuration. Starting from a nonduplicated record preserves that property.

`native_plan_iff_common_holding` joins the footprint criterion to this transition semantics in both directions. `footprint_plan_has_holding_history` extends the forward connection to any native joint relation satisfying the two footprint laws, provided the root footprint is available and initially unoccupied. `code_plan_has_holding_history` first lifts the code plan, then applies this connection.

The last two results construct a trace of the **stated acquisition process**. They do not prove that the arbitrary model’s original event relation implements that process. Applying them to a physical or software arrangement requires correspondence of its acquisition, access and retention relations. This separates the checked bridge from an unearned implementation claim.

The acquisitions occur in sequence but the holdings coexist at the endpoint. This is simultaneous holding, not a theorem of arbitrary concurrent execution, ongoing mutual performance or scheduler correctness. `permutation_preserves_holding` permits every request order under this static law; `frame_holding_iff` says that adding initially occupied positions preserves feasibility exactly when none overlaps the requests. This frame statement concerns the local acquisition protocol, not a formalization of the full separation-logic frame rule.

## 5. What fails when a local certificate omits relationships

`ExplanatoryCrossBranch.crossing` has leaf requests `[false]`, `[true]`, `[false]`. Its left intermediate node is recorded with an empty footprint. The immediate children of that node are disjoint, and the empty intermediate footprint is disjoint from the rightmost `[false]`. Every immediate-sibling test therefore succeeds in `weakJoint`.

The complete request list repeats `false`, and no acquisition history can hold it twice. `weak_lacks_inheritance` identifies the omitted connection: the empty intermediate record did not cover its own descendants’ support. This is a counterexample to the adequacy of the weaker certificate, not to a complete account already retaining descendant use. It does not prohibit genuine formation of new support; changing support during the episode lies outside the fixed-footprint premise and needs its own temporal account.

The dual failure `withinOnly` retains containment but lets two siblings request the same support. It also admits a local certificate while no common holding history exists. The stronger joint relation rejects the crossing plan and accepts a concrete plan with supports 0, 1 and 2, with its actual successful trace proved. Thus the repair is not an impossible or universally rejecting condition.

These examples concern exclusive support. Sharing itself is not declared impossible or undesirable. A repeated read, shared capacity or coordinated common support needs an appropriate native law rather than automatic treatment as duplicate exclusive ownership.

## 6. Pairwise success does not settle larger common demands

A separate process records a shared load. Each acquisition adds one held activity occurrence and is admitted only while load is below capacity. Nothing releases during the episode. `capacity_trace_iff` and `capacity_admission_iff` prove the precise law: from zero load, a list of acquisitions is admitted exactly when its length is at most capacity.

Capacity 2 and capacity 3 arrangements admit every single and pair acquisition demand. Three held occurrences distinguish them. More generally, `any_finite_arity_can_miss_next` proves for every natural n that all demand lists of size at most n succeed in both capacity-n and capacity-(n+1) arrangements, while n+1 succeeds only in the latter.

This is an actual transition-law comparison, not a freely varied acceptability predicate. It also identifies exactly what is held equal: finite admission answers up to the selected size. Their whole internal laws, complete modal theories and unrestricted finite histories are not equal. A known capacity law is a finite explanation of all sizes, and a richer nested joint query can distinguish the arrangements. The result excludes extrapolation from a fixed ceiling of success checks alone; it does not require infinitely many experiments or infinitely many primitive relations.

The connection to explanatory necessity is therefore sharper: an explanation claiming unrestricted common realization must preserve the relevant combined-demand law or equivalent relational content. It may encode that content dynamically, as a global inequality, or through correct local summaries. The present syntax and an exclusive-slot ontology are not uniquely necessary.

## 7. Counterreview and source assessment

| Challenge | Assessment |
|---|---|
| The global conclusion was hidden in `Within` and `Separate`. | They constrain each native joint triple, not whole plans or traces. Induction derives the arbitrary finite-plan claim; the operational characterization uses a separately stated acquisition law. Their physical applicability remains a premise. |
| The weak tree is simply an invalid resource decomposition. | Correct: it is valid for immediate-sibling separation but invalid for complete support coverage. The result locates the omitted relationship rather than refuting the fuller decomposition account. |
| Overlapping footprints prove impossibility. | Not generally. Overapproximating footprints can overlap while selected demands do not. Necessity is established by actual repeated requests or the capacity law, not by overlap of arbitrary summaries. |
| Every generic model’s code plan is now executable in its own dynamics. | Not proved. The new executable trace uses the declared persistent-holding law; implementation correspondence remains explicit. |
| No duplication captures all kinds of joint realization. | False. Shared capacity is a separate valid law; its checked example prevents promoting exclusive support to a universal premise. |
| Pairwise checking can never suffice. | False. With accurate inherited footprints and the relevant local law it does suffice for the certified finite tree. Pairwise success alone lacks that law and coverage. |
| This proves a uniquely necessary ontology. | No. Static capacity constraints, allocation tables and equivalent transition descriptions remain valid competitors. The result concerns recoverable target content. |
| Every independent branch must be disjoint in reality. | No. Disjointness here concerns specified exclusive supports; interacting, shareable or newly formed supports demand other relations. |

Re-read the introduction of Reynolds, [*Separation Logic: A Logic for Shared Mutable Data Structures*](https://www.cs.cmu.edu/~jcr/seplogic.pdf), PDF pp. 1–2. Its linked-list example requires descendants reachable through two structures to remain disjoint; it motivates separating conjunction and a frame rule. That is an established predecessor for complete support summaries and local composition. The new Lean files are a small proof of the present explicit relation, not a new separation logic or a proof of Reynolds’s whole program logic. Follow-up page access timed out; no additional section is claimed as newly read. No source bytes were imported.

This is author counterreview, not independent-agent acceptance. No empirical experiment, external message or retrospective repository-wide proof audit was performed.

## 8. Proof inventory, reproduction and integration

| Source | New theorems | Role |
|---|---:|---|
| [ExplanatoryFootprints.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryFootprints.lean) | 11 | Descendant support, nonduplication, converse certificates, reassociation/permutation and exact-code support connection. |
| [ExplanatoryCoexistence.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryCoexistence.lean) | 11 | Exact acquisition-history criterion, retained common holding, native/code connections and initial-occupancy frame. |
| [ExplanatoryCrossBranch.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryCrossBranch.lean) | 15 | Missing containment/separation counterexamples, positive repair and unbounded family of finite-arity capacity limits. |

The [immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-global-realization-checks/20261008T085919.976102Z/receipt.json) uses Lean 4.29.1 and freezes thirteen modules. Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_global_realization.py`. The isolated runner rejects holes, custom postulates, unsafe bypasses and warnings, and records source/log bindings and per-declaration dependencies. All inherited proof source bytes and their 147 audits remain unchanged: 111 empty and 36 standard. New 37: 4 empty and 33 standard; only the two arbitrary-code corollaries include classical choice inherited through joint matching.

[Documentary checks](EXPLANATORY-GLOBAL-REALIZATION-CHECKS.json) bind the theorem inventory, frozen proof closure, links, chapter continuity and C30/F22 rendering. [Owned edits](EXPLANATORY-GLOBAL-REALIZATION-INDEX-EDITS.json) preserve earlier row contributions and the previously checked chapter/source bytes. These local checks do not certify concurrent full-table source review.

## 9. Integrated conclusion and remaining universal connection

**中文。** 本轮接通了“逐节点共同方案—完整支持范围—一次共同占用历史”，并证明局部检查遗漏下层支持时确实会失败。更一般的共享容量例子说明，解释若承诺任意规模的共同实现，就须保留联合需求怎样受整体规律限制，不能只把有限阶成功清单外推。其必要内容可以由整体约束或过程规律表达，并不独占于当前生成术语。

**English.** Local certificates compose when their summaries retain the content needed for the whole target and the operational law implements that composition. The fixed-access persistent-holding connection is complete at its stated scope. The next substantive bridge is changing realization conditions: how an actual history forms, modifies or releases support while preserving an adequate joint description. Earlier serial reuse is already established and is not reopened. Universal warrant for the applicable composition law, unrestricted actual query access and the uniqueness of a foundational formulation remain unproved.
