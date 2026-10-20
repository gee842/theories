# Batch D2 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

## REPORT (D2)

### Modules written (`D2/Becoming/`)

| Module | Theorems | Roots covered (source module) | Reading |
|---|---|---|---|
| `BoundaryFlows` | 16 | Boundaries: `Boundary.only_whole`, `subTrue_member`, `superTrue_all_iff`, `bounded_closure_iff`, `presupposition_scopes`, `unrestricted_iff_superTrue`, `superTrue_level_free`, `subTrue_total_iff`, `boundaryInvariant_iff_determinate`, `boundaryInvariant_iff_extends`, `not_subTrue_of_invariant`, `unrestricted_of_presupposed`, `boundaryInvariant_iff_standpointInvariant`, `Valuation.significant_of_presupposed`, plus the non-root `subTrue_empty_iff`; Interdependence: `bounded_whole` | A self's boundaries drawn along a flow's own relations: affecting (closure = reach closure), feeding, sharing (closure = system). The whole is always a drawing (`Boundary.whole`). A common condition makes the system the whole. `bounded_whole` is read through `Web.retains_iff_includes`. |
| `ListedWebs` | 12 | Population: `Listed.across`, `Listed.ceasings_within`, `Listed.comings_within`, `Listed.ceasing_of_outpacing`; Change: `keep_pace`, `persists`; Locality: `ceasing_needs_arising`, `Covers.ceasing_not_recurring`, `ceasing_steps_found`; Identity: `forced_iff_more`, `forces_iff_noSplit`; Space: `stop_unrefuted_iff` | The determination is a web's activity: comings are `Web.Arises`, ceasings are `Web.Ceases`, a listing is `Web.Census`. `forces_iff_noSplit` is stated over every web; its proof builds an inline two-step web. `stop_unrefuted_iff` is read as `World.RestsFrom`. |
| `TallyWorlds` | 5 (+1 def) | Population: `tally_iff_counted`, `tally_iff`, `balance_not_tally`, `ChangeBound.lpo_of_ends` | New definition `Shown n c a`: some world's census has these counts. It comes with its exactness theorem `shown_iff_tally`, which uses the queue world `World.queue` and `Queue.counts`. `lpo_of_census_ends` is the LPO strength stated of every world's census; its helper lemma `occurrences_congr` feeds the base through it. |
| `PassageWorlds` | 4 | OneStep: `runsDownClosed_iff_stated`, `Chained.continues` | Patterns shown by worlds (`Realized`, `RunRealized`) and the passages a flow shows (`Flow.passage`). |
| `LevelWebs` | 4 | Change: `falls_not_recurring_from_floor`; Space: `amount_still_unrefuted`; Population: `balance_over_stretch`; Entropy: `configurations_exact` | A condition's level `W.level · c`; a balanced flow per condition; `Web.config` and `Web.stock`. |
| `DependenceWebs` | 2 | Units: `unitFactor_one`; Reserve: `Web.chainEnd_zero` | Support in a fixed unit. Coextinction at once under `Web.Dependent`, because the zero reserve then carries and vacuously decays. |
| `ExchangeFlows` | 4 | Evolution: `selected_uniform`; Sampling: `gateBy_of_not` | Uniform descent in a flow that is acting and dependent; a relatum absent from every fine step takes and gives nothing in `Flow.sample`. |
| `StockTraces` | 2 | Stock: `Stock.covered_iff_prefix` | `Feasible` and `Trace` of the stock process, and of any balanced stock drawn from what is held. |

### Apart count for my source modules (before → after)

| Module | Before | After |
|---|---|---|
| Boundaries | 21 | 1 |
| Population | 13 | 1 |
| Evolution | 2 | 1 |
| Entropy | 16 | 4 |
| OneStep | 6 | 1 |
| Identity | 5 | 0 |
| Locality | 5 | 0 |
| Stock | 3 | 0 |
| Change | 3 | 0 |
| Space | 2 | 0 |
| Reserve | 1 | 0 |
| Sampling | 1 | 0 |
| Units | 1 | 0 |
| Interdependence | 1 | 0 |
| **Total** | **80 (48 roots)** | **8 (6 roots)** |

The 6 roots left apart are classified in `classification.json`:
- **Support:** `OneStep.Chain.fill_entry_le`, `configurations_examples`, `distinct_configurationsWithin`. The last one's helpers `distinct_downFrom` and `le_of_mem_downFrom` stay apart with it; they are not roots.
- **Model-witness:** `OneCounts.forms_apart`, `unselected`.
- **Restates:** `counting_laws`, which is the first part of `World.counting_free`.

### Problems found in source modules
- **Retired labels in live text.** `Boundaries`' docstrings still say "G0" and "the axiom" for the continuation condition, and `Interdependence.bounded_whole`'s docstring says "is the axiom". My modules use "continuation condition" and "living significance" instead.
- **Duplicate theorem.** `counting_laws` and the first part of `World.counting_free` state the same law by separate proofs. Proving `counting_free` through `counting_laws` would remove the duplicate.
- **Hidden `propext` in a library lemma.** `Nat.succ_ne_zero` brought `propext` into one of my proofs; `Nat.noConfusion` avoids it. Other batches may run into the same thing.

### For the integrator to decide
1. **Specialization joins.** Most of `BoundaryFlows` takes a general Boundaries law and states it for the boundaries drawn along a flow's relations, the way the pilot reads sequences along a run. Each statement depends on the flow and web through the relation. Please confirm this counts as "the base object carries the law".
2. **`BoundaryFlows` docstring.** It does not end with "No ethical predicate, ranking or axiom occurs", because a supplied significance appears in its statements. It ends with a note that the presupposition, covering and invariance remain premises, and that no ranking or axiom occurs.
3. **New definition `TallyWorlds.Shown`.** It comes with `shown_iff_tally`; please accept it as a reading, or substitute an existing name.
4. **`counting_laws` classified as restates.** I left it as "restates" rather than adding a second copy of `World.counting_free`.
