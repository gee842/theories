# Internal review: material refinement of updater formation

**Date:** 6 October 2026. **Status:** contract review in progress; final implementation, verification and independent finite checks remain to be inspected.

**Reviewer provenance:** a collaborating AI reviewer, separate from this round's implementation and finite-check authors. This reviewer authored the preceding material-selector package and therefore is not an external reviewer or independent originator of the overall program. This note distinguishes review of definitions and proof contracts from the compiler's proof checking.

## Connection under review

The target is the missing material connection between the earlier typed consumable selector construction and [UpdaterFormation](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/formal/UpdaterFormation.lean). The latter already has paid formation and a variable updater whose state changes which selector reconstructions are allowed. Its coarse material field supports recyclable slots. The proposed refinement introduces consumable typed stocks and must account for every module and selector construction on one inherited history.

The central conditional claim should be exact: a finite coarse updater history can be realized in the proposed material process if and only if the history is already feasible under the coarse law and its cumulative A and H demands fit the inherited inventories. For event word `w`, those demands are:

- A: one unit per updater-module formation, plus two per false-orientation selector formation;
- H: one unit per updater-module formation, plus two per true-orientation selector formation.

Both updater alternatives have the same declared A/H recipe. This is a supplied assembly law. It cannot be inferred from the parts' names or from the existence of a fuel ledger.

## Contract risks and required distinctions

1. **Refinement is not equivalence of the material theories.** The new consumptive law blocks some histories admitted by the recyclable-slot law. Exact operational lifting must include the typed-stock conditions. The original material implementation and its counterexamples remain preserved.
2. **The adapter must consume free parts.** The earlier bridge accepts positive total A/H counts, including a resident. The new interface must require free A and free H so retaining the resident does not simultaneously count it as adapter material. Its bounds must retain all unused precursor as well as resident, free, adapter, incorporated and spent matter.
3. **Local energy transfers once.** The earlier entrance converts the captured local bit into common fuel after paying the adapter. A material wrapper must not retain that bit as a second available energy store. Remaining unit source must be represented by packets plus remainder with the same total energy.
4. **The actual intermediate state is binding.** Paid formation, adapter and operational use must share their resource-bearing boundary states. Neither part stocks nor fuel/source may restart at the handoff. Ending inventories cannot be inferred from a fresh illustrative fixture.
5. **The old state has a different material annotation.** The original `primaryEntrance` and `finalWitness` hardcode material 2. The proposed witness has material 13. The same event word and core/lease trajectory may be reused only with an explicit, checked substitution of that annotation. Full equality to the old state is false.
6. **Supplied functional laws remain supplied.** The refinement constrains formed instances of updater/selector machinery. It does not derive the two assembly wirings, the consequence-to-renewal law, the fixed alternative repertoire, or the meaning of the directed updater from generic matter.
7. **The path is existential.** The existence of a history in which the updater changes and becomes causally effective does not prove that every schedule selects it, establish its probability, or derive prediction and learning from observations. In particular the earlier preparation probability 2/9 and strict-witness probability 1/72 cannot be transferred to the new preparation and stock-constrained law without a new probability correspondence.
8. **The phase boundary matters.** If old formation reactions are suspended after handoff, depleted stocks cannot silently be replenished through them. This gives a finite resource refinement, not a conservative concurrent extension of all prior reaction channels.

## Early checks and counterexample requests

The proposed formation word—five H formations, eight A formations, association of A, repair, then capture—is enabled in that order with material 13, initial common fuel 29 and source 97. It has sixteen events and spends fifteen common units. Its endpoint has seven free A, five free H, one active resident, common fuel 14, source 96 and one local unit. Adapter consumption leaves six free A and four free H, preserves the resident, binds one A/H pair, and has the old updater entrance's resource trajectory with material annotation 13.

The original updater witness has two module formations, two false selector formations and one true selector formation. Those events consume precisely six A and four H. The expected final matter account is resident 1 + adapter 2 + updater-module parts 4 + selector parts 6 = 13. The expected energy account is initial 126 = formation 15 + adapter 1 + operation 59 + remaining 51.

The earlier two-material preparation endpoint has no free A. It must fail the new adapter even though it passed the earlier total-count bridge. This is a substantive difference between interfaces, not a failed theorem of the earlier interface.

A competition example must respect the inherited command guards: updater formation requires module lease zero, whereas selector formation requires a positive module lease. They cannot both be enabled in one state. A valid competition witness therefore uses a sequence in which selector assembly consumes parts that are subsequently needed for updater reconstruction after actual module wear. A stock-level theorem that simply adds both demands is also meaningful; a supposed same-state choice between these two commands would be invalid.

## Verification record

Pending source and checker inspection. The expected package is [the new updater material refinement](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater). Acceptance requires checking the full new theorem list, inherited source hashes, proof dependencies and fresh compilation record; finite enumeration results have separate bounded scope.

## Consequence for the theory

If accepted, this closes a material compatibility obligation between declared formation and variable-updater dynamics. It does not complete the bridge from formed machinery to acquired, corrected prediction and action. If typed-stock budgets rule out a desired continuation, further formation or recycling has to be supplied as an actual costed mechanism. If empirical mechanisms reuse parts instead, the consumptive interface would need revision rather than being promoted to a universal law.
