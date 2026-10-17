# Batch P2 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

I wrote two join modules for P2. They cover 7 of the 71 roots in my four periphery modules. The other 64 are classified in `classification.json`: 46 can't be joined because their own axiom reports aren't empty, 17 are model witnesses and 1 is periphery-scope.

## Modules written

Both are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/u2/P2/Becoming/`. Both build clean: `"unclean": []` and `"with_axioms": {}`.

- **`TreeSearchRuns.lean`** (9 theorems; imports `Becoming.Branching` and `AcquiredCorrection`). Reading: `AcquiredCorrection.scan` is the run of one determined law, `advance`, on a search configuration (frontier, found ticket, inspections spent). A configuration with a key found or an empty frontier is left unchanged (`advance_found`, `advance_empty`).
  - Exactness: `orbit_reads_scan` and `run_reads_discover`. Along every run of `Law.process advance` that begins at a tree, step `n` reads exactly as `discover n root`, so a budget is a step of the run.
  - Roots joined (along every run from the given tree):
    - `positive_witness_needs_no_complete_map` → `found_without_reading_rest`
    - `interrupted_is_not_absent` → `pending_then_found`
    - `acquired_new_address` → `example_found`
- **`ReconfigurationProcesses.lean`** (6 theorems; imports `GenerativeCore` and `CorrectionReconfiguration`). Reading: `reconfigure` is the step relation of a process on `Managed`, with actions `Rearrangement` (opened, cost, depth, candidate).
  - Exactness: `step_iff`, and `enabled_iff` (an action is enabled exactly where `reconfigure` gives a configuration, i.e. `isSome`).
  - Roots joined, as laws of that process:
    - `reform_rejects_shared_control` → `shared_cause_no_step`
    - `repaired_reform_installs` → `separated_repair_steps`
    - `review_alone_funded_is_not_enough` → `own_cost_alone_no_step`
    - `exact_combined_budget_suffices` → `combined_cost_steps`

## Counts (apart theorems / roots, before → after)

| Module | Apart | Roots |
|---|---|---|
| CorrectionReconfiguration | 28 → 24 | 20 → 16 |
| EvidenceQualifiedCorrection | 24 → 24 | 19 → 19 |
| FallibleInspection | 24 → 24 | 18 → 18 |
| AcquiredCorrection | 24 → 21 | 14 → 11 |

With my tree overlaid, the whole measure is 993 apart and 642 roots.

## What's wrong in the periphery modules

Almost every general law in these four modules has `propext`, often with `Quot.sound` and sometimes `Classical.choice`. This comes from `simp`, `omega`, `decide` on propositions and `by_cases` in the periphery proofs, and in places from definitions (`survivingReads`, `dispatch`, `locate`, `final`, `FallibleInspection.run`), which taints every theorem that mentions them. Only the `decide`- and `rfl`-proved computed cases are clean, which is why so few roots could be joined.

Several of the blocked roots are exactly the natural laws of the two base objects I just built:
- On the reconfiguration process: `unauthorized_reform_rejected`, `unavailable_candidate_rejected`, `old_request_rejected_after_reform`, `reform_does_not_expand_mandate`.
- On the search run: `scan_sound`, `scan_budget`, `reachable_route_is_found`, `exhausted_is_scoped_absence`.

`FallibleInspection.complete_diagnosability_iff_cross_separation` is already proved with an empty report as `Becoming.Bridge.complete_diagnosability_iff_by_core`.

## For you to decide

1. **Reproving the general laws without axioms.** The general laws behind the axiom-dependent roots could be reproved axiom-free inside the periphery modules, which editing those files would allow and I wasn't allowed to do. They would then join directly through the two new readings. Is that worth doing?
2. **One-step joins.** The four `ReconfigurationProcesses` joins are statements about single steps of a process, not about runs. I count them as instance joins under the brief, but they're the kind you have trimmed before; please confirm or drop them.
3. **The search law's verdict.** In `TreeSearchRuns` a found search keeps its frontier unchanged. The verdict reading ignores the frontier, so this is harmless.
4. **Field name.** The `Rearrangement` field `opened` stands for the periphery's `authorized` flag; I chose it to avoid the social word.

`apart.json` and `.build/` in the batch folder are measurement and build output.
