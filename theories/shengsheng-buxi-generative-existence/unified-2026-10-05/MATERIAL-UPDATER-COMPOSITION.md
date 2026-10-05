# One material history for selectors and their updaters

6 October 2026. AI-assisted continuation of the [generative grounding](GENERATIVE-GROUNDING.md). The named connection is **formed constituents → competing construction of response mechanisms and their reconstruction mechanisms → actual use and replacement under inherited support constraints**.

This study connects the [typed-part selector construction](MATERIAL-SELECTOR-COMPOSITION.md) to the operational law of [updater formation](UPDATER-FORMATION.md). Its central question is whether the same actual material inventory can construct both levels through the whole revision history. This is a compatibility result under an explicit additional component law. The law's wiring, sensory transduction and finite repertoire remain supplied.

## 1. The mismatch being resolved

The two earlier studies have a common formation predecessor but different material interfaces. The selector construction consumes two typed parts at every assembly. The updater construction instead assigns two formed constituents to reusable backing slots and charges repeated construction to fuel. Their separate proofs do not make those physical laws interchangeable.

Here the existing updater transition law is restricted by a typed component inventory. Every admitted event retains its original effect on fuel, source packets, selector mapping, updater kind, leases, retained mapping and environmental regime. In particular, paid updater formation remains an actual event; it cannot disappear as a supposedly costless change of description.

The new material law retains used parts and adds no recycling channel. It therefore realizes a restricted set of the coarse updater histories. It does not prove that a consumable implementation and a reusable-slot implementation admit the same histories, preparation costs or probabilities.

## 2. Declared construction laws

Preparation uses the unchanged `FormedSelection` relation. The operational handoff requires a valid material inventory, an intact site, an actually captured local fuel unit, sufficient common fuel for the adapter, and at least one **free** A and one **free** H. A resident constituent cannot also be spent as a free component.

The adapter binds one A and one H. It pays the earlier adapter cost from common fuel and makes the captured local unit available as common fuel. That unit is consumed in the conversion; it is not retained as a second usable store. Source energy is represented by its packet quotient and remainder, exactly as in the earlier updater entrance. The remaining free parts, resident and site condition are retained. Neither selector nor updater is installed at handoff.

After handoff the recipes are:

| Construction event | Free A consumed | Free H consumed |
|---|---:|---:|
| Either kind of updater | 1 | 1 |
| Selector mapping `false` | 2 | 0 |
| Selector mapping `true` | 0 | 2 |

Different updater kinds use the same quantities, with different supplied arrangements. Component composition alone does not derive their different functions. Each construction also pays its original fuel bill. Trial, reversal and packet expiry retain the original operational effects and consume no additional parts under this declared law.

Consumed parts accumulate in retained incorporated/spent inventories. Expiry does not free them. The adapter, active structures and spent structures are all included in those inventories; the bound counters alone do not distinguish their functions. During operation the sum of free, resident and bound material is conserved. Any unformed precursor capacity is also retained, so the general total remains the original material capacity even when preparation leaves some precursor unused.

This is a staged construction. The earlier formation chemistry is suspended after handoff. Continued production, degradation, recovery of spent components and physical enforcement of that phase boundary require further laws.

## 3. The exact compatibility criterion

For an operational event word \(w\), let \(U(w)\) count updater formations and let \(S_A(w),S_H(w)\) count the two selector assemblies. Their cumulative demands are

\[
D_A(w)=U(w)+2S_A(w),\qquad
D_H(w)=U(w)+2S_H(w).
\]

For an inherited state with free stocks \(A_0,H_0\), the criterion is:

> A history with a specified updater-law endpoint has a typed material realization exactly when that same history and endpoint are feasible under the updater law, and \(D_A(w)\le A_0\) and \(D_H(w)\le H_0\).

The updater law still checks the actual payment, lifetime, source and permitted-choice conditions at every event. The material inequalities add exactly the construction obligation. They suffice for every prefix because these component demands are nonnegative and there is no other consumption or replenishment during operation. Aggregate energy alone does not imply feasibility; neither does aggregate material without the required types.

The two levels now compete for the same actual stock. A part used to reconstruct an updater is unavailable for a later selector, and a selector can consume material needed for later revision of its own reconstruction rule. Allocating separate unlimited inventories to these levels would erase that interaction.

The criterion also limits this particular route to sustained change. Every updater formation consumes one of each part, so any admitted operational history has at most \(\min(A_0,H_0)\) updater formations. Providing arbitrarily abundant fuel cannot remove this bound. Indefinitely repeated construction would require replenishment or reclamation, with their own causal and resource accounts. This does not forbid persistence of an already formed structure; it constrains the number of new constructions.

## 4. One actual formation-to-revision history

The previous two-material preparation cannot provide the new free component obligations. This study declares its larger original stocks before preparation: material capacity thirteen, common fuel twenty-nine, source energy ninety-seven, no A/H constituents, no resident, and a damaged site.

The original formation law admits:

**Form five H → form eight A → associate one A → repair → capture one local unit.**

All formation occurs before repair, as required by the existing guards. The result has seven free A, five free H, one active resident, fourteen common fuel units, one local unit and ninety-six source units. The fifteen units spent in preparation remain spent.

The paid adapter leaves six free A, four free H and one bound component of each type. Its operational state has fourteen fuel units, sixteen six-unit source packets, and both mechanisms absent. This matches the earlier updater example's operational fields while retaining **thirteen**, rather than two, as its coarse material total.

The same operational event word then:

1. Forms the first updater and selector, and performs four productive trials.
2. Retains its stocks across environmental reversal, then suffers two failed trials.
3. Uses the old updater to reconstruct the old mapping and suffers two more failures.
4. Forms the changed updater, which permits the opposite mapping, constructs that selector and captures successfully.

Thus the old rule has governed reconstruction before replacement; the new rule subsequently governs a different reconstruction and receives its productive consequence. The history consumes six A and four H after handoff: two updater formations, two A-selector assemblies and one H-selector assembly. The final state retains seven bound A, five bound H and the one resident, with no free components.

The energy account is

\[
126=15\text{ preparation}+1\text{ adapter}
+59\text{ operation and waste}+51\text{ remaining}.
\]

The remaining energy consists of nine common fuel units and seven six-unit packets. It does not undo component depletion. The event word is an existential feasible history, not a guarantee that uncontrolled choices will produce it. The earlier stochastic witness probability is not transferred to this changed preparation and component law.

## 5. Verification and failure boundaries

The [construction package](../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/README.md) passes a fresh Lean 4.29.1 build with **39 new theorem audits** and 107 inherited audits. One new result has no axiom dependencies; the other 38 use only Lean's standard `propext` and/or `Quot.sound`. The inherited updater module separately includes `Classical.choice`. The new proofs contain no proof holes, custom axioms or native proof shortcuts. This is conditional mathematics, not an axiom-free account of reality.

Independent finite checks pass 1,248 enabled and 15,600 disabled handoffs, 299,584 short-word/inventory cases, 48 stock pairs for the full revision word, 768 prefix/stock cases and seven boundary checks. A smaller initial state with eight fuel units, three packets and three free parts of each type has a complete 200-state, 522-edge operational graph, including reversal cycles; this is not the full graph of the main sixteen-packet witness. The [mathematical companion](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MATERIAL-UPDATER-MATH.md) records the precise interfaces; the [internal review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MATERIAL-UPDATER-REVIEW.md) audits their assumptions and scope. These are checks of supplied mathematical laws, not evidence of a particular chemical implementation.

Two independently checked preparation variants isolate competition between the layers. Both begin with capacity twelve, common fuel twenty-eight and source ninety-seven; each reaches the same operational entrance fuel and packet stocks as the successful case. Forming seven A and five H leaves five free A and four free H after the adapter: the continuation runs until the changed updater requires an A already consumed by selector reconstruction. It stops with ten fuel units and eight packets still present. Forming eight A and four H instead leaves six free A and three free H: the changed updater forms, but the final H-selector assembly is blocked with eight fuel units and eight packets remaining. The histories obey the actual lease and payment guards; this is sequential competition, not an impossible same-state choice between module and selector formation.

The successful final state gives another separation. Reverse the environment and perform two failed trials. The coarse law then permits a paid reconstruction of the opposite selector, with five fuel units and five packets present. The material model blocks it because no free parts remain. Conversely, appropriate parts cannot fund an unaffordable event. The older two-material preparation is retained as a valid result under its original interface and an inadequate producer for this stronger one.

## 6. Contribution to the common root

This advances compatible composition in the governing derivation. Response selection and selection over reconstruction rules can share an actual material and support history. Each changes the other's remaining possibilities through ordinary component consumption. The added constraint is causal and inspectable; no analyst's success measure allocates the parts or identifies the correct updater.

The foundation remains conditional. This study supplies a realization of declared construction and operational laws, not the origin of those laws. It introduces no additional prediction record, semantic decoder, learning algorithm, shared evaluator or ethical authority. The binary updater repertoire and the mechanism that proposes replacements remain external premises of this local model.

The next named bridge remains **formed, revisable machinery → acquired and corrected prediction → paid action using that prediction**, with compatible observation channels, memory, component inventories and actual intermediate states. The [controlled-refinement criterion](CONTROLLED-REFINEMENT.md) identifies some of those interface obligations. The parallel [paid protocol result](PROTOCOL-COMPOSITION.md) adds a criterion for several physical events implementing one completed controller step, while retaining interrupted attempts and the distinction between available completion and guaranteed completion. Neither criterion by itself identifies a concrete learner here. Component renewal is also necessary if the account claims indefinitely many reconstructions. A connected finite witness advances the unified foundation without completing its learning, concern, wisdom or empirical obligations.
