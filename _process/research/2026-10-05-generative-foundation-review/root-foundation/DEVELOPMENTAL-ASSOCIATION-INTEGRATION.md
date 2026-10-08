# Inherited division and the formation of association

8 October 2026, Asia/Bangkok. AI-authored continuation of [The Theory of Evolution](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md). **A heritable local division state can change the association reconstructed by descendants. Group ancestry then follows from the actual bond-forming history under stated conditions.** Nineteen new Lean theorems pass. The mechanism is a conditional abstraction with a primary biological correspondence, not a new discovery of the biological mechanism or a completed universal evolutionary theory.

## The connection advanced

[Generated reconstruction](GENERATED-SELECTION-RECURRENCE-INTEGRATION.md) computes transfer entries from actual carrier pools, but supplies faithful group assembly as a whole recipe. The present study addresses the source of association through a different, finer representation: division adds a daughter, copies its parent's current retention state, and either retains or omits their bond. A change in the parent's state changes the subsequent local developmental operation. Collective membership is described by connectivity in the bonds that actually form; no group-membership table is supplied at each generation.

This is a mechanistic refinement of the explanatory question, **not a proved physical refinement of the earlier eight-carrier model**. Its division law does not reproduce the earlier 28/30 and 68/66 yields, and the two resource interpretations must not be silently composed. Both instantiate the existing relational method; the new source formally imports the common `GenerativeCore`, with an exact executable-history correspondence.

The transition advanced is **changed inherited cellular organization → changed developmental association → reconstructed group relations and subsequent possibilities**. For the broader normative inquiry it helps explain how capacities and relations can be inherited and changed. Common ancestry, persistence and reproducibility supply no ethical verdict; G0 and practical judgments retain their separate, explicit scope.

## Primary biological correspondence

**Ratcliff et al. (2015), [Origins of multicellular evolvability in snowflake yeast](https://discovery.ucl.ac.uk/id/eprint/1459200/1/ncomms7102.pdf), journal pages 2–4.** The published account connects impaired cell separation to retained mother–daughter attachment. An ancestral ACE2 knockout produced the snowflake form; functional complementation in one evolved line restored unicellularity. Coding changes were detected in five of ten examined lineages, so the same coding mutation is not established for every lineage. The paper develops a branching model, compares its growth form with observations, and analyzes propagule ancestry. This supports a concrete causal correspondence for inherited developmental association. It does not validate our unit resource costs, chosen division times, arbitrary aggregation event or mutation frequency. The PDF's selected main-text passages and captions were read; supplements and raw data were not analyzed. Publisher redirects and a PMC browser challenge made the UCL-hosted published PDF the usable full-text source. This adds a targeted mechanistic reading beyond the [already credited 2012 and 2019 experiments](RECURSIVE-SELECTION-FORMATION-SOURCES.md), not a new experiment.

## One history and its local operations

The source is [DevelopmentalAssociation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/DevelopmentalAssociation.lean). Its state contains the current cell count, a precursor quota, available and consumed activity support, each cell's effective retention state, inherited founder origin, and actual bonds. Cell positions below the current count are operative; other function entries have no represented cell. Founder origin records genealogical descent and is not a guarantee of identical current genes.

The seed supplies one or more already living cells without bonds. This study does not explain the origin of cells, genomes or metabolism. A division consumes one precursor and one support unit, adds a new cell, and copies the parent's current retention state and founder origin. If retention is active, it adds their bond. These units are explicit bookkeeping assumptions, not measured yeast mass or energetic constants.

A supported `changeRetention` event changes one cell's effective division state; both directions are admitted. The event represents a realized change, not a mutation probability or a claim that every such change is caused by a single gene in every organism. `detach` removes an existing bond. Restoring separation changes subsequent divisions; it does not erase old bonds. `aggregate` connects two already existing positions and can join different founder lineages. Each successful event consumes the stipulated unit of support. There is no fresh stock at a generation boundary.

The roles of parent, daughter, founder and associated group are descriptions of positions and relations in this common history, following the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). The model preserves ancestry, current inheritance state, bond changes and quota accounting. It omits geometry, force, age, gene-expression detail, metabolic renewal and differential survival. Those omissions constrain correspondence; they do not constitute independent substances outside the generative process.

## General results and concrete continuation

The nineteen new theorems include the following general results:

- `run_iff_core_trace` identifies executable finite histories exactly with `Generative.Trace` for the declared process. The core is actually imported, not merely mentioned as an analogy.
- `division_inherits` and `changed_state_governs_division` connect the current parental state to the daughter's inherited state and bond. A changed state has an operative consequence.
- `step_accounts` and `core_trace_accounts` conserve cell count plus precursor and available-plus-consumed support. Every successful event consumes one support unit; history length plus final available support equals the initial available support. This finite-stock limitation is specific to the declared accounting law.
- For an initially lineage-consistent bond relation, histories containing division, retention change and detachment preserve lineage consistency. `developed_groups_have_common_origin` then derives equal founder origin for any two connected positions. Connectivity is the reflexive, symmetric and transitive closure of actual bonds. No population-wide claim of genetic homogeneity or absence of somatic conflict follows.

The closed histories start with one cell, ten precursor units and twenty support units. A retention change followed by divisions at positions 0, 1 and 2 produces four cells connected by the bonds 0–1, 1–2 and 2–3. It leaves seven precursors and sixteen support units. The following endpoints are checked directly by kernel reduction:

| Continuation from that history | Actual result |
|---|---|
| Detach 1–2, then divide cell 2 | Cell 4 attaches to cell 2. The separated 2–3 branch can reconstruct further association using inherited state, without regrouping the whole population. |
| Restore separation at cell 2, then divide it | Cell 4 inherits separation and does not attach; old bonds remain. This distinguishes changed future reconstruction from instant repair of existing structure. |
| Aggregate two original cells | A connected pair can have different founders. This is an explicit failure of the ancestry conclusion outside the non-aggregative history condition. |
| Remove precursor/support or name a nonexistent parent/bond | The corresponding operation fails; descriptive labels do not create its physical prerequisites. |

The example's linear sequence is a chosen asynchronous division history, not a fitted growth curve or a representation of typical cluster geometry. The general lineage theorem admits other valid division schedules. No theorem here derives a universal propagule bottleneck, a fragmentation rate, or a probability of this history occurring.

## What cellular summaries cannot determine

Two further checked histories start from the same four-cell chain and each detach one bond. Detaching 1–2 leaves the bonds 0–1 and 2–3. Detaching 0–1 leaves 1–2 and 2–3. Both have identical cell counts, every indexed retention state and founder label, and the same precursor, available-support and consumed-support amounts. Their bonds differ.

`comparison_histories_are_actual` proves both are actual core traces from the same single-cell seed. One permits the subsequent operation detaching 0–1; the other does not. `no_bond_free_exact_predictor` proves that no function of the specified bond-omitting snapshot can predict this operation's availability exactly for all histories reachable from that seed.

This is a precise adequacy requirement for a state representation. It supplies an explanatory improvement over the **specified snapshot abstraction**: relational information is necessary for the specified prediction. It does not show that conventional evolutionary theory cannot track bonds, infer them from the known history, or make the same prediction. A history-aware or graph-based competitor escapes the obstruction. The paper's own developmental approach is therefore credited, not presented as an inferior count-only theory. Broad empirical or comparative superiority remains unestablished.

## Substantive self-review

This is the implementing author's review, not an independent agent review.

**Does changing one stored state genuinely change a reconstruction mechanism?** At this representation's resolution, yes: the same division operation now either retains or separates daughters, and the operative state is inherited. Group association is formed by those local events. However, the mapping from the state to division and the event that changes the state are still supplied. The model does not derive transcription, genome replication, mutation occurrence or their population distribution. The primary correspondence gives a reason to investigate this abstraction; it does not discharge all those explanations.

**Is the model an advance on the preceding table construction?** It explains group association without a fresh bulk grouping assignment and proves the genealogical condition from the bond history. It does not preserve the preceding model's numerical law, resource semantics or exact state space. Its value is a more specific candidate mechanism and a core correspondence, not a fictitious composition of incompatible physical models.

**Is clonality built into a group label?** Founder labels are copied at division, and bonds are actual events. The common-founder conclusion requires their historical connection. Aggregation breaks it. Retention changes remain possible inside one founder lineage, so the conclusion must not be inflated into constant genotype, homogeneous interests or guaranteed cooperation.

**Does selection for the mechanism follow?** No. Heritable developmental variation and further operation are present; the ecological consequences that make one arrangement reproduce or survive differentially are absent. Mutation and fracture schedules are admitted histories, not predictions. A next selection claim must connect measured or independently justified effects to actual survival and succession, preserving the costs of attachment and separation.

**Does this replenish continuing conditions?** No. The model uses a fixed quota. It cannot answer whether changed association improves metabolic or ecological renewal. The earlier exhaustion result remains credited. Adding a quantity called renewal or prescribing a favorable fitness for attached cells would not supply the missing mechanism.

**What would require revision?** If a proposed application involves aggregation, changing expression not faithfully reconstructed, or geometry/force changing the outcome, the current local rules must be revised or restricted. If a conventional relational developmental account explains and predicts the same cases, the contribution is integration and checked correspondence rather than unique theory superiority.

## Verification and next connection

Lean 4.29.1 passes **19 new theorems / 41 explicit declaration audits**, with **69 audits including the imported core**. Seventeen new declarations have empty named-axiom lists. Other declarations use standard `propext`, `Quot.sound` and, for the arithmetic accounts, `Classical.choice`. The checker rejects custom axioms, proof placeholders, unsafe proof escapes and compiler warnings or errors. The first attempts exposed parsing, reduction and proof-composition issues; those runs supplied no accepted result. The retained clean run is bound to exact source and log hashes.

- [Source-bound verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/developmental-association-verification/verification.json)
- [Fresh-build checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/developmental-association-verification/check.py)

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/developmental-association-verification/check.py
```

This advances the formation, inherited reconstruction and changing-unit requirements in the full evolutionary goal. **The next connection is actual differential continuation caused by developed association**, with ecological input, attachment cost, fragmentation and replenishment distinguished. It should use a biological correspondence or independently specified physical interaction and a conventional competitor with the same structural information. It must also explain how the changed mechanism is transmitted through that selected continuation; observed inheritance alone is not a complete account of its evolutionary prevalence. The current abstraction should be refined or replaced where the evidence demands it. The full goal remains active.
