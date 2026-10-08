# 从共同接续到评价所需信息 / From joint continuation to required evaluative information

8 October 2026. AI-authored formal audit of Ren's instruction to proceed from a monist, relational ontology. This note reports one new **verified composition** of two existing results, not a new derivation of G0 or a new proof of the existing no-loss comparison principle.

## Result identity and substantive delta

Result(s): reuse the unmigrated [joint-continuation classification](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean) and [explicit generative-premise inference](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean). The registered `joint-target-uniqueness` result has different local test semantics and is not an alias for this composition.

Delta: the first producer's actual event law supplies a strict extension in a joint-possibility inventory; that extension is the exact input of the second producer's explicit comparison principle C. The resulting comparison cannot factor through a description containing only each realization's separate possibility. The new proof also exhibits the precise richer description that distinguishes the case and preserves an admissible history in which the richer possible joint outcome is never realized.

Supplied premises / correspondence: C, the positive significance of the particular joint living possibility, and coverage of relevant realized costs, losses and effects remain supplied. No ethical conclusion follows merely from constructing the inventory. The proof is conditional on applying C to that inventory at an adequate scope.

Evidence: [RelationalGrounding.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RelationalGrounding.lean), its [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_relational_grounding.py), and the [source-bound successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/relational-grounding-verification.json).

Boundary: no general obligation to preserve every coupling, no ethical ranking of all mixed changes, no forced actualization, and no completed universal ethics.

## One unfolding before the analytical divisions

The reused event law begins from one initial configuration. Its coupling can be retained or released. Retention permits a left realization, a right realization, or their joint realization; release permits the two separate realizations but excludes their joint realization. These are possible histories of one specified law, sharing the initial configuration. Left and right name differentiated positions within that law. They are not independent original value owners.

Two analyses of this one process are then compared. The marginal description says whether each represented realization can occur somewhere. The joint description says which bundles can occur in the **same** history. Both marginal possibilities remain after release, while one actual organizational condition for their joint realization has changed. Counting or listing those marginals therefore loses information already present within the process; it is not a discovery that separate substances need an external moral connection.

这里先有同一展开中耦合关系的保留或解除，再有对分化位置及其共同接续的描述。新增证明检验的是：若生生评价所根据的关系被局部表示抹去，该表示就无法承载已经明确采用的比较原则。它不重新把位置当作各自拥有价值的主体。

## Exact adapter and declarations

Let `released` and `retained` be the two inherited continuation descriptions, and let a bundle be a predicate on the two represented claims. `Jointly` means that **one feasible history** realizes all claims in the bundle.

`jointInventory.realized regime bundle` means that joint realization is possible under the regime's actual specified organization. It does **not** mean that every possible realization has actually happened. `jointInventory.generative bundle` marks only the full two-claim bundle: a singleton does not satisfy it. The checker explicitly verifies that exclusion.

| New declaration | Exact checked content |
|---|---|
| `released_profiles_are_carried` | Every represented profile achievable after release is achievable under retention, with a common whole-history witness. |
| `joint_bundle_extension` | This profile preservation and the inherited missing joint bundle supply `GenerativeComparison.GenerativeExtension` for the joint-possibility inventory. |
| `marginals_agree_but_joint_descriptions_differ` | Every marginal possibility agrees, but the full bundle is possible only under retention. |
| `strict_comparison_cannot_factor_through_marginals` | For any summary type and summary determined by marginal agreement, an irreflexive comparison on summaries cannot satisfy C on this inventory. |
| `joint_description_separates` | The full joint-bundle profiles differ; adding this relational information repairs the exhibited informational collapse. |
| `retained_possibility_does_not_force_joint_actualization` | A complete admissible retained history realizes the left claim and fails the right claim, even though joint realization remains possible. |

The central obstruction is short and exact. The adapter supplies a generative extension; C requires a strict comparison. Marginal agreement makes any marginal-determined summary identical. A strict comparison between identical summaries violates irreflexivity. No transitivity, additive score, total ranking, common utility or probability assumption is used.

The separate `joint_description_separates` conclusion means only that this full bundle resolves this pair's informational collapse. It does not certify the inventory as a complete description of reality. The theorem quantifies over any summary type at Lean's `Type` universe in this file; this is a mathematical information condition, not a classification of all physically possible intelligences.

## What C means here, and what the proof does not supply

The explicit G0 route already treats living continuation and generative possibility as ethically relevant. The present formal law does not establish that its two physical claims instantiate living continuation. Applying the result ethically therefore needs a substantive correspondence account for that identification. It also needs the full relevant comparison: actual effects of retaining or releasing the relation, maintenance burdens, dependencies, losses, and other realizations must not disappear just because they are absent from this tiny event law.

For the corresponding no-countervailing-loss case, C is the already disclosed commitment that preserving the relevant grounds while adding the marked generative possibility supports strict comparison. The present proof **consumes** that commitment. It does not derive C from bare possibility inclusion, prove that all joint activities are good, or use a generative label to validate itself.

因此，普遍推论的新增部分是一个必要条件：**任何要恰当地承载这项整体关系比较的评价表示，都不能只保留与该关系变化无关的边缘信息。** 这是对评价表示的限制，沿既有 G0／C 路线成立。它不是“任何智能必然赞同或实现该比较”，也不是对所有现实耦合关系的无条件保存令。

The retained-left history is a concrete remaining boundary under the same law, not a freely toggled compliance predicate. An expanded space of joint continuations does not force a particular realization within that space. The conditional normative comparison, its adequate recognition, and actual continuation remain distinct claims about differentiated aspects of the same unfolding.

## Lean check and dependency audit

The checker ran Lean 4.29.1, commit `f72c35b3f637c8c6571d353742168ab66cc22c00`, on fresh temporary copies. Its retained successful run is [20261008T123934.603061Z](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/relational-grounding-checks/20261008T123934.603061Z/verification.json).

- New module: 6 theorems, 12 explicitly named declaration audits, all with empty Lean axiom dependency lists.
- Imported unchanged modules: `JointContinuationClassification`, 5 theorems / 21 declarations; `GenerativeComparison`, 11 theorems / 27 declarations. They were recompiled and audited for this composition. These are inherited results, not 16 additional new theorems. Some inherited declarations use `propext` and `Quot.sound`; no declaration uses a custom axiom or `Classical.choice`.
- Three checked application examples: explicit C consumes the adapter, a constant summary cannot support strict C, and a singleton bundle is not marked generative. They are not counted again as new results.
- 23 retained artifact hashes bind source copies, checker copies, compiler/version logs, declaration audits, signatures and controls. Source and checker bytes were unchanged during the successful run.
- The scanner rejects `sorry`, `admit`, custom `axiom`, `unsafe`, `native_decide`, `implemented_by` and the kernel-skip flag in checked source code. Its explicit-declaration audit does not separately enumerate Lean-generated constructors or projections; successful compilation still kernel-checks the source.

Source hashes:

```text
RelationalGrounding.lean
9b2319e752ee1b93d4245b1c5fe0a9d1e0758b1caf37282623598ea491e84c87

JointContinuationClassification.lean
e508683cc80832744a28f44c69f9c2561701cd099219448b75cfdb474c0786ee

GenerativeComparison.lean
948d36b4cddc0b2289219604464bd38eb6e607183b157cee1075d50fb9797a03

check_relational_grounding.py
ace4ba47e0e7003f2dbb3f984b295bb65a97c9fef4c91f7b596d68ae640b6354
```

An initial check exposed a missing reduction before rewriting the summary equality. The source was repaired and the complete checker rerun; the failed-run receipt remains preserved. This was a proof-script elaboration repair, not removal of a counterexample or weakening of the stated theorem.

Empty axiom reports describe Lean declaration dependencies. They do not remove supplied definitions, C, or the substantive application premises. This is one new checked composition with an information obstruction and a behavioral boundary; it does not complete universal meta-ethical grounding.
