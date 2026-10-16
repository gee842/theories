# Joint allocation, partial competence and continued activity: review

8 October 2026, Asia/Bangkok. AI-authored independent review of the next [living-dependencies connection](../../../../theories/becoming/history/LIVING-DEPENDENCIES.md): partially competent organization and joint support → sustained specified living activity. It follows the [organization review](LIVING-ORGANIZATION-REVIEW.md) and the shared [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Sections 1–4 record the design assessment; §5 assesses the concrete source and evidence. Final verification is recorded separately below.

**Proposed contribution:** compose jointly allocated reaction participants into an actual history, and relate productive allocation to the participants available at that stage. This can address nonzero competence and competing requirements, rather than repeat the empty-pool case. The result must preserve subsequent catalytic reuse and distinguish an untimed allocation bound from output per unit of physical time.

## 1. What is already established

The repository already contains several parts of this explanation. This review read the relevant source or study passages; no older compiler run, experiment or primary-source reading was repeated.

| Existing work | Contribution to reuse |
|---|---|
| [BoundaryModels](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/BoundaryModels.lean), shared-resource example | Separate possibilities do not imply one common allocation. The finite example explicitly concerns one allocation round. |
| [ResourceContinuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean) | Actual same-history support bounds, componentwise requirements and finite event-index intervals. These are not physical durations by definition. |
| [FormationRoutes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean) | Reusable formed structure, support costs, actual repeated output, repair and competing routes already affect joint attainability. |
| [General continuation proof](GENERAL-CONTINUATION-PROOF.md) | One joint history can supply its component conditions; separate existential histories cannot be swapped for one shared history. |
| [Allocation control](../../2026-10-05-support-and-shared-generativity/completion/ALLOCATION-CONTROL.md) and [joint-capability bridge](../../../history/2026-10-05-support-and-shared-generativity/completion/JOINT-CAPABILITY-BRIDGE.md) | Existing supplied stochastic mechanisms connect allocation, actual competing reaction rates and finite-horizon joint outputs. Their original validation and empirical-identification scopes remain unchanged. |
| [Weiße-model assessment](../../2026-10-05-support-and-shared-generativity/completion/RESOURCE-ALLOCATION-BASELINE.md) | Free and translating ribosomes, substrate-dependent elongation, participant release/reuse, shared metabolic provision, balanced-growth assumptions and finite-batch output are already explicitly reconstructed. This reviewer read that assessment, not its primary paper or supplement. |

Consequently, neither resource competition nor a factorization of protein production into engaged machinery and elongation is first introduced here. A useful new formal connection is **aggregate participant admission → actual sequential realization under the existing reaction law**, followed by a quantitative restriction that retains the changing organization and common support. Its biological importance must come from a better correspondence to effective participation, rather than a new name for an old accounting premise.

## 2. Why aggregate admission adds a relevant condition

The previous [reaction model](LIVING-ORGANIZATION-PROOF.md) treats one reaction at a time. A catalyst present on both sides of a reaction may legitimately participate again in a later reaction. Merely adding the net stoichiometric changes of several reactions does not determine whether their participants can all be allocated together: catalysts can cancel from each net update while their simultaneous input requirements still compete.

A batch can reuse the existing `Recipe` semantics by concatenating its input and output lists. The input guard then checks all multiplicities against one actual prestate. This avoids separately granting the same retained participant to several overlapping operations. It also makes all other requirements joint: enough catalyst without enough substrate or work support does not admit the batch.

The proposed serialization result is more useful than a second independent batch vocabulary. It must construct an actual trace of the original process whose endpoint agrees with the admitted aggregate transition. That establishes compatibility with the existing semantics and preserves every reached intermediate state. Under this positive-input reaction law, the construction concerns the stated recipes; inhibitors, spatial interference or extra reaction conditions cannot be silently added afterward while preserving a sufficiency claim.

The converse need not hold. A sequential trace may reuse a catalyst returned by its earlier operation. Such a trace can be valid even though treating all its reactions as one jointly allocated batch is inadmissible. This is a genuine distinction between simultaneous allocation and successive participation, not evidence that catalytic reuse is double counting.

## 3. The timing and competence boundaries

An allocation batch is **not automatically a physical time interval**. A participant can complete several successive cycles within a measured interval. An upper bound on output in that interval needs independently supported occupancy, service-time, elongation or turnover conditions. Giving a round a clock-like name does not supply them. Conversely, a sequential trace constructed from an admitted batch does not prove that the whole trace finishes by a biological deadline.

Changing the batch partition can change the allocation claim while leaving the same sequential reactions available. A physiological application therefore must specify what each batch represents, which operations overlap, and when released participants become available again. The theorem can be a correct untimed interface without being an invariant of arbitrary time coarse-graining.

Available competent organization, actually allocated participation and realized stable-product output are distinct quantities. A measured translating-equivalent fraction can describe current productive engagement rather than the maximum recruitable capacity. Unused but competent structures, slow operation, abortive products and structural impairment cannot be collapsed into one binary inactive class without evidence. The current study must not replace the previous zero-pool overclaim with an unjustified hard ceiling inferred from a growth-rate estimate.

## 4. What would advance the living-dependency connection

A nontrivial example should retain positive productive competence while showing how shared participants and support constrain both current production and activity that changes later competence. Activation or formation in one stage may increase later allocation possibilities but uses the actual current conditions. It must not make its product available to fund its own earlier input requirement or reset support between stages.

A history-level capacity account should credit **actual preceding changes**, not merely available activation recipes. An increase in a selected active count may reflect activation, assembly or import; it is not automatically newly created whole organization. A decline can leave nonzero activity. A bound may be useful without either assigning total failure or assuming optimal utilization of every remaining participant.

Sustained specified activity requires a declared horizon and independently identified output. A family of finite traces supported by increasingly large initial stocks does not give unlimited operation from one finite preparation. Continued maintenance or replacement of the enabling machinery and the timing of provision remain part of the target. Existing succession and continuation results should be composed where their actual states and laws match, rather than simply juxtaposed.

The bounded bridge can close at an explicit scope: a general allocation result, actual positive-competence histories through changed organization and joint support, and an empirical account of what the chosen participation and output quantities mean. A further biological throughput or continued-growth claim requires its timing, kinetic and observational assumptions to be independently warranted. Universal living coverage remains a separate objective.

## 5. Concrete source and evidence assessment

The complete [LivingAllocation source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingAllocation.lean) was independently read. It reuses `LivingOrganization` without changing its law. No source edit or compiler rerun was performed by this reviewer.

### General argument

`aggregate` concatenates the members' input and output lists. `batchProcess` applies the existing process law to that aggregate and requires each member to be admitted. `batch_serializes` constructs every intermediate inventory in the original list order, carries the endpoint through, and checks each original input guard. `batches_serialize` composes those traces without a reset. The proof uses positive input requirements and the exact stoichiometric balance; unrepresented inhibition or spatial interference would require a different application argument.

`uses_le_aggregate_inputs` starts from recipe-level multiplicities: each declared use count must be no larger than the recipe's required copies of the selected participant. Together with joint admission, `batch_uses_bound` derives the state-level bound. The represented use unit remains supplied. An arbitrary numerical yield, amino-acid rate or protein-length conversion cannot replace it without justifying that recipe-level premise.

`increase_eq_actual` identifies the aggregate positive net change with the actual successor count minus the preceding count, truncated at zero. A catalyst appearing in both lists is therefore not newly credited. Formation, activation or import can increase the selected count; the definition does not distinguish those mechanisms or claim new matter. Gross production hidden by simultaneous loss is not separately credited as additional capacity at the next state.

`allocation_horizon_bound` bounds total uses by the number of declared batches times initial availability, plus each positive change multiplied by the number of **later** batches. Nothing is credited to its own formation batch. Losses are permitted; ignoring their subsequent reductions makes this an upper bound rather than an equality or a claim of tight attainable output. The no-increase corollary preserves repeated use of the initial participants over successive batches. Neither result supplies a physical duration or proves utilization of every available participant.

### Positive competence and the finite witness

The example starts with one active participant, one inactive participant, four substrate copies and five support copies. Activation and production are each individually enabled, but cannot jointly reserve the single active copy. A separate example shows shared-support insufficiency even with enough active copies. These are jointly checked requirements of the same state.

The successful history spends one support copy to activate the inactive participant, then performs two batches of two productions. It retains the reached intermediates and ends with two active participants, four products, five spent support copies, and **no remaining substrate or support**. The production-only comparison allows at most three productive uses in three declared batches from the same initial active count. It does not show that activation is best across arbitrary partitions, deadlines or other output criteria.

`sequential_reuse_exceeds_joint_allocation` explicitly supplies two successive productive events using one returned participant, while the combined two-reaction batch is inadmissible. Thus the module proves its own boundary: its batch requirement cannot be imposed on every collection of events occurring during an arbitrary elapsed interval. The actual successful episode advances the connection between current organization and later allocation, but does not by itself sustain or regenerate all of its enabling conditions.

### Evidence correspondence

The complete [capacity evidence assessment](LIVING-CAPACITY-EVIDENCE.md) was reviewed. Its primary-source readings belong to its author, with their partial-reading limits; this reviewer did not independently reread those papers. No substantive overreach was found.

The useful Dai distinction is between growth-inferred stable-product engagement and independently identified recruitable competence. The evidence note preserves negligible-turnover and steady-growth assumptions and does not identify an inferred inactive fraction with permanently impaired inventory. Calabrese's theoretical comparison retains replacement without turning it into positive net growth, a new replication or a universal constituent-expiry rule. The note keeps that cross-study synthesis distinct from the earlier protection and reactivation assays. Its interpretation table also preserves operation timing, output units and the reached conditions for further activity.

This correspondence changes how the formal inventory may be applied: an active-equivalent estimate cannot silently calibrate the maximum available participant count. Nor may completed productive uses be identified with retained biomass or physiological recovery without the relevant observations. These are positive identification requirements for the proposed connection, not a new objection to every organizational model.

**Substantive verdict:** the general serialization and participant-use derivation are a reusable advance beyond a new binary example or an independently supplied capacity inequality. The positive-competence history shows actual activation supported by present conditions and increasing later allocation possibilities. This closes a bounded ordering and allocation connection. Timed biological throughput, replenishment of all needed support, and broader living-domain correspondence remain open; the same finite episode is not a completed theory of sustained living activity.

## 6. Verification and integration record

The frozen source reviewed above has SHA-256 `415a7ea68cbf68e32323fa95e641aef202ead0d3b352f51dc69a8eb17870b836`. The complete [proof note](LIVING-ALLOCATION-PROOF.md), [integrated §9](LIVING-DEPENDENCY-INTEGRATION.md#9-joint-participation-and-continuing-productive-organization) and current canonical allocation section were read against it. The proof note preserves the admitted-recipe premise, exclusive-participant discipline, constructed-versus-observed ordering, partition dependence, actual positive changes and finite exhaustion. Two canonical wording precisions were requested and verified as applied: recipe admission is explicit, and count increases receive credit for later allocation while other required support must still be available. The final next-connection wording also preserves measured mean rates versus deterministic bounds on each history. The final integration and current canonical account are accepted at their stated scopes; no substantive blocker remains.

The root's fresh Lean 4.29.1 check is recorded in the [current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-allocation-verification.json) and the [preserved receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-allocation-checks/20261007T193335.742143Z/verification.json). This reviewer independently compared:

- All three current source hashes with their archived bytes and receipt hashes.
- Current and archived checker hashes, the compiler executable hash, and all four raw-output hashes.
- The identical current/preserved receipts, generated audit source, and all 107 declaration names in order with their recorded dependencies.
- The source declaration inventory and theorem counts against the receipt, and the recorded empty source-change list.

All comparisons pass. The source closure has **107 explicit declaration audits**, including **32 new declarations / 16 new named theorems**. Of the new declarations, 17 have no axiom dependency, five use only `propext`, and ten use `propext` with `Quot.sound`. The inspected sources and reports contain no new custom axiom, proof hole, `Classical.choice` dependency or unchecked native evaluation. This is independent receipt and source inspection, **not a compiler rerun or fresh primary-source reading**. The empirical interpretation and broader living goal retain the limits stated above.
