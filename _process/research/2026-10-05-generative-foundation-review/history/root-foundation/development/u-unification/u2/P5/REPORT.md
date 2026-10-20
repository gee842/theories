# Batch P5 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

# U2 batch P5 report

**Result:** I wrote nine join modules. Six are pure, with empty axiom reports. Three belong to the new periphery-join ring (`...Inherited`), following the addendum. All of them build with `"unclean": []`, and there is no `sorry`, no `simp`, no `omega` and no `decide` in my proofs. Across my ten periphery modules, apart theorems went from **123 to 32** and roots from **75 to 22**. None of my own theorems is apart. I committed nothing, landed nothing, edited no existing file and did not run `check_becoming.py`.

All files are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/u2/P5/`: the modules are under `Becoming/`, and `classification.json` and `apart.json` sit in that folder. No module name collides with the package or with P1–P8.

## Modules and readings

**Pure (empty axiom reports):**
- **`UnitTraces`** (ExplanatoryLocalUnits, 18 theorems). The general laws are stated for the joining of a process's admitted traces, `traceJoin P`: units are unique, boundary assignments agree, units carry through a joined trace, a common unit suffices for joining, and units transport between two processes.
  - The periphery's `trace_join_associative` carries axioms, so I proved associativity again with an empty report (`associative`). The units come from the bridge's `Joining.trace_has_units_by_core`.
  - New reading: the periphery's `budgetJoin` is exactly the traces of `budgetProcess` read through whether they take the step (`budget_reads`). So the four budget roots join as laws of that process: functional, associative, has units, and not chain-complete, even though the traces themselves are chain-complete.
- **`ExactRecordRuns`** (KnowledgeCorrespondence, 9). A history is a run of a process. The evidence is the record a registration leaves before step `t` (`recordBefore`); the target is a two-valued reading of the configuration at `t` (`valueAt`). With this reading, an exact answer at every step from `T` on is exactly `LearnableRuns.RestsFrom` (`exact_iff_restsFrom`). The joined laws cover exact, sound, resolves, abstains, sound on a smaller domain, finer registration and kept record.
- **`JointPhaseTraces`** (RelationalReduction, 9). The periphery's joint configuration and its law are read as the process `Assurance.ofMap RelationalReduction.next`, with `trace_end`/`evolve_trace`. The model facts are stated on that process's traces, in the pilot's `Captured` style:
  - the phase step keeps both local states and the basis masses, and changes the cross term;
  - the courses `[interact]` and `[shiftPhase, interact]` give different responses;
  - no update of the local states carries the interaction step.
- **`TestCodeFrames`** (ExplanatoryUniqueness, 5). Models are a frame's configurations and the questions are its branching tests, `BranchingTest.Holds F`. Covered: the kernel equals passing the same branching tests, alike configurations get one code, two descriptions share one kernel, `matches_iff`, and `aligned_iff`.
- **`JoiningCodeFrames`** (ExplanatoryUniversality, ExplanatoryContextualStructure, ExplanatoryJoiningContexts and ExplanatoryJoiningRefinement, 12). These are stated on a joining's partner frame and role frame:
  - descent and saturation are phrased with `SameBranchingTests J.frame`;
  - `CourseExact` and `CourseReduced` restate exactness and reduction as reading the courses open in `J.frame`, each with an `↔` to the periphery's notion;
  - codes differ where a course is open from one fragment and not the other, and joinability is a one-move trace;
  - `SameTests` symmetry, and the identity is an open map of the role frame.

**Periphery-join ring:**
- **`ExactRecordRunsInherited`**, 1 theorem: `exact_possible_iff`. It inherits `propext`, `Classical.choice` and `Quot.sound` from `exact_possible_iff_resolves`.
- **`JointPhaseTracesInherited`**, 2 theorems: `summary_response` and `summary_omits_register`. It inherits `propext` from `every_finite_control_response_exact` and `every_finite_word_exact`.
- **`JoiningCodeFramesInherited`**, 3 theorems, inheriting `propext` and `Quot.sound`:
  - `canonical_factor`, from `every_exact_account_has_canonical_factor`;
  - `common_operation`, from `unique_common_operational_structure`;
  - `sameTests_iff_alike`, from `same_iff_compatible_relation`.
- **`ReceptionTracesInherited`** (AcquiredSegmentation), 17 theorems, inheriting `propext` and `Quot.sound`. Reception, `receive`, is read as an `ofMap` process, and exposure is the end of its trace (`trace_end`, `along`). Covered:
  - support plus spent support is kept along every trace;
  - without support a trace stays where it is;
  - broadening is a trace that keeps that total;
  - all the concrete context, broadening and order results, stated on traces from `ready n`.

## Apart and root counts

| Module | Apart before → after | Roots before → after |
|---|---|---|
| AcquiredSegmentation | 23 → 3 | 17 → 3 |
| KnowledgeCorrespondence | 20 → 10 | 15 → 8 |
| RelationalReduction | 11 → 0 | 7 → 0 |
| ExplanatoryLocalUnits | 13 → 0 | 10 → 0 |
| ExplanatoryUniqueness | 9 → 6 | 9 → 6 |
| ExplanatoryUniversality | 12 → 6 | 7 → 3 |
| ExplanatoryContextualStructure | 11 → 0 | 5 → 0 |
| ExplanatoryFootprints | 7 → 7 | 2 → 2 |
| ExplanatoryJoiningContexts | 16 → 0 | 2 → 0 |
| ExplanatoryJoiningRefinement | 1 → 0 | 1 → 0 |
| **Total** | **123 → 32** | **75 → 22** |

The 22 remaining roots are classified in `classification.json`:
- **model-witness (17):** the stipulated `History` model, the `Bool × Bool` presentations, the chessboard balance model, the list-footprint plans, and the two log/list facts in AcquiredSegmentation.
- **support (2):** `grouping_preserves_encountered_sequence` and `true_content_trivially_safe`.
- **general-structure (3):** the three `all_predicates_*` roots.

## Things that look wrong or misplaced in the periphery

- Several periphery proofs carry axioms only because of `simp`, `rintro` or `decide`, and pure versions are easy to write:
  - ExplanatoryJoining: `merge_associative` and `joined_associative`;
  - ExplanatoryLocalUnits: `trace_join_associative`, `trace_has_units` and the other `trace_*` theorems.
  
  `UnitTraces.associative` and the bridge's `trace_has_units_by_core` already show this.
- In AcquiredSegmentation, every definition from `bond`, `edges` and `parse` through to `ready` carries `propext`. That is why nearly every root could only go into the Inherited ring.
- KnowledgeCorrespondence imports `Std`. RelationalReduction already reaches `Std` through OperativeCoherence, so this is not new to the bridge side.

## For you to decide

1. **Overlaps with existing pure theorems.**
   - `JoiningCodeFramesInherited.common_operation` restates `Joining.unique_common_operational_structure_by_core` with the hypotheses read on the frame.
   - `sameTests_iff_alike` is the joining case of `Determined.alike_iff_sameTests`.
   
   I joined both anyway because they make 14 apart theorems feed the base: 4 in ContextualStructure and 10 in JoiningContexts. You can drop them and classify the two roots as `restates` instead.
2. **Bundled statements.** Some theorems combine roots or a hypothesis-free conjunct with a trace statement:
   - `ReceptionTracesInherited.broadening_trace` (∃ trace ∧ total kept);
   - `order_not_frequency` (equal sound counts ∧ the two traces);
   - `reception_changes_parse` and `support_used` (the start and the end of one trace).
   
   Each part concerns the same trace or courses, but please check them against standard 1.
3. **`JointPhaseTraces.no_local_update`** is close to `Instances.local_pair_carries_no_law`. Mine is proved through the root `no_local_pair_update`.
