# Joint participant allocation, reconstruction and later reuse

8 October 2026, Asia/Bangkok. AI-authored continuation of [living dependencies](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/LIVING-DEPENDENCIES.md). The target connection is **partial competence and joint support → specified activity across successive reached conditions**. Source: [LivingAllocation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingAllocation.lean).

**Result:** arbitrary declared reaction families admit a general allocation and serialization theorem. A jointly allocated batch has an admissible serialization in the original reaction process; participant uses are bounded by the inventory from which they are jointly allocated. Across successive batches, actual positive increases of the selected count can enlarge later allocations. Concrete checked histories distinguish present activity, reconstruction, shared support and subsequent reuse. **16 new named theorems / 32 explicit declarations pass Lean 4.29.1, with 107 declaration audits across the three-module closure.**

This is an **untimed allocation result**, not a biological rate law. Serialization constructs an admissible ordering in the model; it does not establish that an observed molecular process actually took that ordering. Neither a fixed deadline nor physical simultaneous execution is represented.

## 1. What this adds to existing work

The [preceding organization proof](LIVING-ORGANIZATION-PROOF.md) already establishes arbitrary-family origin and entry requirements from actual recipe participants. Its concrete examples retain catalysts, activate protected organization and assemble organization from separate components. The current result imports that module unchanged.

The repository also already contains:

- [TypedRenewal](../../../../experiments/shared-renewal-capability/formal/TypedRenewal.lean), with exact fixed-family reaction inventories, retained catalysts, consumption and repair; and [CarrierTurnover](../../../../experiments/shared-renewal-capability/formal/CarrierTurnover.lean), whose marked-presence observer expressly does not provide an injective allocation of labels to material particles.
- [FormativeCapacity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean), whose named batch construction is a sequential stockpile/build history, and [FormationRoutes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean) with fixed coupled-versus-manual formation efficiency, repeated operation and support accounting. [ReconfigurableRoutes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean) already checks support competition and finite completion tradeoffs.
- [ResourceContinuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean), which telescopes a supplied support law along actual traces. Repeating that law with a biological label would add no new dependency explanation.
- The [Weiße resource-allocation baseline](../../2026-10-05-support-and-shared-generativity/completion/RESOURCE-ALLOCATION-BASELINE.md), which already reconstructs free/bound ribosomes, substrate-dependent elongation, release and reuse, coupled resource demand, and finite-culture accounting from primary work. Its historical algebraic and source-reading scope is preserved, not retrospectively recertified here.

The new formal connection is **aggregate joint allocation → admissible original-reaction serialization**, uniformly over arbitrary species and reaction types. Allocation bounds are derived from the summed recipe input multiplicities, rather than introduced as a state-level output-versus-capacity assumption. The sequence bound then distinguishes retained catalyst returns from actual increases, and credits an increase only after the batch that realizes it. The induction itself is ordinary bookkeeping; the additional content lies in the participant-based derivation and its connection to the existing reaction semantics.

## 2. One process, with a declared allocation discipline

`LivingOrganization.Recipe` already specifies finite input/output lists, including repeated occurrences. An inventory assigns each species a natural-number count. Its `process` requires an admitted recipe, availability of every required input multiplicity in the prestate, and the exact inventory balance `after + input = before + output` for every species.

`aggregate recipes word` concatenates the input lists of the member reactions and separately concatenates their output lists. `batchProcess` is exactly the existing reaction process applied to these aggregate recipes; every member reaction must be admitted. There is no second unrelated state-update law.

All retained catalytic copies still occur on both sides. Their input occurrences must be allocated from the shared prestate. Two reactions each requiring one copy therefore need two copies for this joint allocation. All consumed support and substrate inputs are checked in that same prestate. A newly produced copy cannot supply another member's missing initial allocation within the batch.

This is a **declared exclusive-participant discipline**. Some real enabling relationships can support several activities without exclusive occupancy; the representation does not require treating all such relationships as independently consumed or exclusively reserved particles. Conversely, a physically relevant inhibitor, spatial conflict or duration cannot be omitted and then declared settled by these positive-input recipes. The theorem applies to the stated semantics; correspondence must justify the relevant exclusivity and omitted interactions.

Following the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md), active organization, inactive organization, substrate, support and product name differentiated roles within connected transformations. They are not independent foundational realms. All modeled shared requirements and reached states remain in one history. The supplied recipe family and chosen participant descriptions remain local explanatory inputs, not consequences of the bare generative core.

## 3. General checked results

### Serialization

`batch_serializes` constructs an intermediate inventory after the first member and recursively carries the remaining joint allocation forward. No support is inserted between member reactions. `batches_serialize` composes these serializations through the actual reached boundary states of a supplied batch trace, producing a trace of the flattened reaction list.

The conclusion is **admissible trace existence under the model**. Even if an empirical interpretation warrants a supplied aggregate transition, the constructed serialization is not independently observed molecular ordering. Its converse fails: sequential reuse can be possible without enough initially distinct copies to allocate every occurrence jointly. The checked witness below establishes that distinction without declaring sequential reuse defective.

### Allocated uses

For a selected participant species and a natural-number assignment `uses` to reactions, the explicit structural premise is: for every admitted recipe, `uses r` does not exceed that recipe's input multiplicity of the selected participant. It can be checked directly against the recipes. This is not a premise that measured output already falls below an externally asserted capacity.

`uses_le_aggregate_inputs` derives the corresponding bound for the aggregate input list. `batch_uses_bound` combines it with actual joint admission: the sum of assigned uses cannot exceed the selected prestate count. The units are allocated participant uses; no conversion to amino acids, completed proteins, biomass, net growth or ethical value is supplied.

### Earlier increases and a finite allocation horizon

`increase` is positive aggregate output-minus-input multiplicity for the selected species. `increase_eq_actual` proves that, on an admitted transition, it equals the positive reached-state count change. Retained catalysts returned unchanged do not create an increase merely because they appear in outputs. Positive changes may represent activation, assembly, recruitment or import; the theorem does not identify all of them as newly created machinery or new material.

`laterCredit` weights each such increase by the number of batches remaining after it. `allocation_horizon_bound` proves:

`totalUses ≤ numberOfBatches × initialSelectedCount + laterCredit`.

No increase is credited within its own formation batch. Losses are permitted, so the bound need not be tight. `allocation_bound_without_increases` specializes the result when each batch has zero positive count change. These are allocation-horizon conclusions. Choosing a finer sequence of batches permits later reuse and changes the bound; the theorem does not infer how many batches fit within an elapsed physical interval.

## 4. Positive partial competence, reconstruction and shared support

The structural example has six participant types and two recipes:

| Activity | Inputs | Outputs |
|---|---|---|
| Activation | one active, one inactive, one support | two active, one spent |
| Production | one active, one substrate, one support | one active, one product, one spent |

These are illustrative declared transformations, not fitted ribosome kinetics or a claim that each actual activation requires one pre-existing active complex. The support unit is not identified with ATP, a universal energetic cost or a thermodynamic state. The general theorem permits other admitted recipes and other interpretations.

The shared start has one active participant, one inactive participant, four substrates and five support units. **It can already produce.** `activation_and_production_compete` proves that activation and production are each individually admissible from this start, while their joint batch is inadmissible because it would allocate the one active copy twice. `shared_support_competes` separately checks that sufficient active copies do not remove a shared-support shortage.

`activation_then_four_products` constructs three successive batches: activation, two production reactions, and two more production reactions. They end with four products and two active participants. Activation consumes one support unit and produces the additional active count before later batches allocate it. All intermediate inventories are carried forward; the final state has **zero substrate and zero support**. This is a finite productive episode, not a self-sustaining cycle or an indefinite continuation certificate.

For the same positive-competence start, `three_batches_without_activation` derives at most three allocated productive uses in three production-only batches. The distinction concerns the declared allocation partition; it does not compare timed biological productivity. Neither a universally optimal choice to activate nor the ethical priority of future activity follows.

`sequential_reuse_exceeds_joint_allocation` provides the essential counterexample: one active participant, two substrates and two support units admit a two-reaction sequential production trace, but cannot admit the two reactions as one jointly reserved batch. The returned active copy is reused after the first operation. Identifying one batch with an arbitrary physical interval would erase this valid behavior.

## 5. Biological evidence and correspondence limits

The companion [capacity evidence assessment](LIVING-CAPACITY-EVIDENCE.md) distinguishes available structures, condition-relative competence, realized productive engagement, completion duration and output. Dai's inferred active equivalent is not a direct available-competent-pool count. Calabrese's turnover analysis also distinguishes production replacing losses from net growth. The formal selected count is not calibrated by identifying it with either inferred engagement or net production.

The [previous ribosome-organization evidence](LIVING-ORGANIZATION-EVIDENCE.md) supports distinguishing nominal provision from functional organization and partial output. Its B. subtilis preparations are not the E. coli histories in the newer assessment. None of these sources directly establishes this example's activation recipe, batch boundaries, exclusive allocation duration, or four-product history.

This proof author read the complete new capacity evidence note and the existing Weiße assessment through its finite-culture accounting section, not their primary sources anew. The evidence author records its own exact primary-reading scope. Code reuse inspection covered the cited definitions and bound constructions; it was not an exhaustive retrospective audit of all repository mathematics.

To turn the allocation result into a physical throughput result requires a justified mapping of participant occupation and release, service duration, competing interactions and observed events to batches. To turn finite products into sustained living function additionally requires correspondence with actual enabling relationships, loss, replacement and subsequent conditions. Those remain explanatory tasks, not facts established by selecting convenient species names.

## 6. Validation and scope

The source imports only `LivingOrganization`, which imports `GenerativeCore`; both pre-existing files are preserved. A fresh temporary build of that three-module closure with Lean **4.29.1** passed, followed by compilation of the final commented source. No solver bypass, `sorry`, `admit`, custom axiom or `native_decide` was added. The final frozen source SHA-256 is:

`415a7ea68cbf68e32323fa95e641aef202ead0d3b352f51dc69a8eb17870b836`.

The root agent then ran the separate [source-bound checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_living_allocation.py). The [current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-allocation-verification.json) and [archived run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-allocation-checks/20261007T193335.742143Z/) bind the final source, imported sources, checker, compiler, fresh compilation logs and declaration-axiom audits. All **107 closure audits** pass. Of the 32 new explicit declarations, **17 have no axiom dependency, 5 use only `propext`, and 10 use `propext` and `Quot.sound`**; no `Classical.choice` or custom axiom occurs. The [independent review](LIVING-ALLOCATION-REVIEW.md) records substantive scrutiny and receipt inspection separately from compilation.

The result advances the living-dependency bridge by replacing separately plausible requirements with a checked account of their joint participation, actual transformations and later reuse. It does not derive the reaction family, biological kinetic rates, every living dependency, universal necessity of reconstruction, or ethical authority from the bare core. Existing transport, recovery and organization results retain their original scopes. The next correspondence must connect this untimed allocation structure to measured occupation, completion, relevant losses and maintained activity over an independently specified horizon.
