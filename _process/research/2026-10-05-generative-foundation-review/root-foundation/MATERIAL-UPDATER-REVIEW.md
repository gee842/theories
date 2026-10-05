# Internal review: material refinement of updater formation

**Date:** 6 October 2026. **Status:** accepted for the conditional claims below. No unresolved blocking semantic or verification finding remains.

**Reviewer provenance:** a collaborating AI reviewer, separate from this round's implementation and finite-check authors. This reviewer authored the preceding material-selector package and therefore is not an external reviewer or independent originator of the overall program. This note distinguishes review of definitions and proof contracts from the compiler's proof checking.

## Connection under review

The reviewed target is the missing material connection between the earlier typed consumable selector construction and [UpdaterFormation](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/formal/UpdaterFormation.lean). The latter already has paid formation and a variable updater whose state changes which selector reconstructions are allowed. Its coarse material field supports recyclable slots. The accepted refinement introduces consumable typed stocks and must account for every module and selector construction on one inherited history.

The central checked conditional claim is exact: a finite coarse updater history can be realized in the proposed material process if and only if the history is already feasible under the coarse law and its cumulative A and H demands fit the inherited inventories. For event word `w`, those demands are:

- A: one unit per updater-module formation, plus two per false-orientation selector formation;
- H: one unit per updater-module formation, plus two per true-orientation selector formation.

Both updater alternatives have the same declared A/H recipe. This is a supplied assembly law. It cannot be inferred from the parts' names or from the existence of a fuel ledger.

## Contract risks checked and resolved

1. **Refinement is not equivalence of the material theories.** The new consumptive law blocks some histories admitted by the recyclable-slot law. Exact operational lifting must include the typed-stock conditions. The original material implementation and its counterexamples remain preserved.
2. **The adapter must consume free parts.** The earlier bridge accepts positive total A/H counts, including a resident. The new interface must require free A and free H so retaining the resident does not simultaneously count it as adapter material. Its bounds must retain all unused precursor as well as resident, free, adapter, incorporated and spent matter.
3. **Local energy transfers once.** The earlier entrance converts the captured local bit into common fuel after paying the adapter. A material wrapper must not retain that bit as a second available energy store. Remaining unit source must be represented by packets plus remainder with the same total energy.
4. **The actual intermediate state is binding.** Paid formation, adapter and operational use must share their resource-bearing boundary states. Neither part stocks nor fuel/source may restart at the handoff. Ending inventories cannot be inferred from a fresh illustrative fixture.
5. **The old state has a different material annotation.** The original `primaryEntrance` and `finalWitness` hardcode material 2. The proposed witness has material 13. The same event word and core/lease trajectory may be reused only with an explicit, checked substitution of that annotation. Full equality to the old state is false.
6. **Supplied functional laws remain supplied.** The refinement constrains formed instances of updater/selector machinery. It does not derive the two assembly wirings, the consequence-to-renewal law, the fixed alternative repertoire, or the meaning of the directed updater from generic matter.
7. **The path is existential.** The existence of a history in which the updater changes and becomes causally effective does not prove that every schedule selects it, establish its probability, or derive prediction and learning from observations. In particular the earlier preparation probability 2/9 and strict-witness probability 1/72 cannot be transferred to the new preparation and stock-constrained law without a new probability correspondence.
8. **The phase boundary matters.** If old formation reactions are suspended after handoff, depleted stocks cannot silently be replenished through them. This gives a finite resource refinement, not a conservative concurrent extension of all prior reaction channels.

## Preparation and counterexample checks

The checked formation word—five H formations, eight A formations, association of A, repair, then capture—is enabled in that order with material 13, initial common fuel 29 and source 97. It has sixteen events and spends fifteen common units. Its endpoint has seven free A, five free H, one active resident, common fuel 14, source 96 and one local unit. Adapter consumption leaves six free A and four free H, preserves the resident, binds one A/H pair, and has the old updater entrance's resource trajectory with material annotation 13.

The original updater witness has two module formations, two false selector formations and one true selector formation. Those events consume precisely six A and four H. The final matter account is resident 1 + adapter 2 + updater-module parts 4 + selector parts 6 = 13. The energy account is initial 126 = formation 15 + adapter 1 + operation 59 + remaining 51.

The earlier two-material preparation endpoint has no free A. It must fail the new adapter even though it passed the earlier total-count bridge. This is a substantive difference between interfaces, not a failed theorem of the earlier interface.

A competition example must respect the inherited command guards: updater formation requires module lease zero, whereas selector formation requires a positive module lease. They cannot both be enabled in one state. A valid competition witness therefore uses a sequence in which selector assembly consumes parts that are subsequently needed for updater reconstruction after actual module wear. A stock-level theorem that simply adds both demands is also meaningful; a supposed same-state choice between these two commands would be invalid.

## Verification record and acceptance

I inspected the complete final [ConstructedUpdater.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/ConstructedUpdater.lean), [formal checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/check.py), [package README](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/README.md), [independent finite checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/check_model.py), [mathematical companion](MATERIAL-UPDATER-MATH.md) and [canonical formulation](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATERIAL-UPDATER-COMPOSITION.md).

The final [formal record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/verification.json) reports a fresh isolated Lean 4.29.1 build passing **39 new theorem audits**, plus **107 inherited audits**: 18 from the generative core, 43 from formed selection, 21 from selector revision and 25 from updater formation. The one new empty-dependency theorem is `core_material_relabel_trace`; the remaining 38 use only `propext` and/or `Quot.sound`. The inherited updater module separately reports standard `Classical.choice`; no new theorem depends on it. The checker scans all compiled sources for proof holes, custom axioms and native/unsafe shortcuts, audits every new theorem, and rejects warnings or unmatched audits.

The reviewed new-source SHA-256 is `c59f5c934ed1884ffddfa36d982b89e6f934386d462a56927478004018e02023`. I checked that all five live source hashes, the formal checker hash and the five build-log hashes match the final record. I also checked that every source hash recorded by the [finite-check result](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/model-verification.json) matches the current file, including the independent checker itself. The build was not rerun by this reviewer after those unchanged hashes were established.

The significant checked statements are:

- `material_trace_lift_iff`: an arbitrary finite updater history and specified endpoint lift exactly under the inherited typed-stock bounds. Nonnegative per-event demands and absence of replenishment justify sufficiency of the final cumulative bounds; the coarse feasibility premise still enforces all prefix payment and lifetime constraints.
- `bridge_projects`, `bridge_energy_exact`, `bridge_material_exact` and `joined_material_ledger`: the typed bridge strengthens the earlier bridge, consumes only free parts, converts local support once, preserves resident and precursor, and makes the detailed material account equal the coarse annotation. That annotation is not an additional inventory to add to the material total.
- `core_material_relabel_trace` and `inherited_entrance_exact`: the two-versus-thirteen annotation issue is handled explicitly, without altering the earlier event law or inventing additional operational resources.
- `actual_part_preparation`, `actual_updater_revision` and `full_formation_to_updater_revision`: the entire preparation/adapter/revision witness is one admitted staged history. `Runnable` checks every actual successor and guard before its general conversion to `Trace`; it is not an unchecked evaluator shortcut.
- `competing_construction_budgets` and `finite_stock_bounds_updater_formations`: updater and selector construction draw from the same typed inventory. The bound is on new constructions, not a claim that every event or every form of learning consumes a new component.
- `actual_post_revision_exhaustion` and `coarse_continuation_blocked_by_spent_parts`: after the successful witness, a further reversal and two failed trials reach an actual state where the coarse selector assembly is enabled but no free parts remain. The configured `noParts` fixture also retains removed free parts in its bound counters and makes no reachability claim.

The independent finite implementation covers **1,248 enabled and 15,600 disabled handoff cases**, **299,584** short-word/inventory cases, **48** full-word stock pairs, **768** prefix/stock cases, a complete **200-state / 522-edge** graph from its explicitly smaller initial state, and **seven** boundary checks. I inspected its event table and enumerated domains; these counts match the loops and are bounded checks, not further universal theorems. It implements only the preparation event kinds needed by its actual witnesses, while the Lean embedding retains the full predecessor relation.

The two twelve-material preparation competition histories are supported by this independent replay, not asserted as separately compiled concrete Lean witness theorems. The general competition bounds are proved in Lean. One replay blocks the changed updater after previous selector construction has exhausted A; the other forms the changed updater but then lacks the H pair for the next selector. Both preserve sufficient coarse fuel and source to isolate the material constraint. This satisfies the requested cross-layer competition test without violating the mutually exclusive lease guards.

The final prose separates this consumptive refinement from the earlier recyclable law, identifies the initial material annotation change, preserves the old result, and does not transfer its stochastic probabilities. It presents the complete graph as the smaller fixture's graph, not the main witness's graph. The remaining explanatory claims stay within the supplied-law scope.

## Consequence for the theory

This closes a material compatibility obligation between declared formation and variable-updater dynamics. It does not complete the bridge from formed machinery to acquired, corrected prediction and action. If typed-stock budgets rule out a desired continuation, further formation or recycling has to be supplied as an actual costed mechanism. If empirical mechanisms reuse parts instead, the consumptive interface would need revision rather than being promoted to a universal law.
