# What the bridge holds, and a fold plan

```text
Result(s): no new result; a classification of the bridge ring and a plan, for Ren's decision
Delta: each of the 741 declarations (601 theorems) of the 39 bridge modules sorted into renaming (kind 1),
       correspondence result (kind 2) or adapter (kind 3), with the records and chapter sections naming it and the
       apart roots it holds; 171 declarations (99 theorems) found to reach no periphery constant; a fold plan with
       the change each step makes to records, the apart register and the counts
Supplied premises / correspondence: none; a reading of the Lean source and of Lean's own constant data
Evidence: Lean constants of type and value for every declaration of the 39 modules (scratch build on the cached
          steps of main 934f2b43c, Lean 4.29.1, no repository file changed); records' live fields; the chapter;
          THEOREM-CONNECTIVITY-APART.json; data and tools in development/bridge-fold/
Boundary: kinds are assigned by stated rules plus reading, not proved; citations are matched by name; whether a
          periphery theorem has a core counterpart under another name is not audited (fold step 0)
```

Question: Ren asked whether the Becoming package really needs its bridge modules. The session that started this study relayed the question; Ren's words are not quoted here. The chapter counts the bridge ring as "Bridge modules (8 bridges and 31 pure periphery joins)", with 39 modules and 601 theorems ([chapter §9](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#9-形式脊柱--the-formal-spine), receipt `20261018T093527.497358Z`). The pure core imports nothing outside itself. The bridge imports both the core and the periphery modules of 6 to 9 October, which define the same notions in their own types. This study sorts what the bridge holds and drafts a fold plan. It claims no board item and changes no Lean.

## 1. Method

- **The modules.** The 39 modules are the `BRIDGE` list of [`check_becoming.py`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/check_becoming.py): the eight bridges (`Bridge`, `CompositionBridge`, `JoiningBridge`, `GranularityBridge`, `RepairComparison`, `Instances`, `RenewalBridge`, `CoursesBridge`) and the 31 pure joins of U2. They hold 741 declarations: 601 theorems and 140 others (126 definitions, 6 inductive types, 3 structures, 3 instances, 2 abbreviations). The theorem count matches the receipt.
- **What each declaration reaches.** A Lean script listed, for every constant of the 39 modules, the constants in its type and its value and the module each comes from. It ran on a scratch build in which all 300 imported steps were restored from the shared cache. Each declaration was then followed through bridge declarations to the periphery constants it reaches. A declaration reaching none is **movable**: its statement and its proof use only the prelude, the foundation and the core.
- **Kinds.** The eight bridges were read declaration by declaration; the rules are in section 2. The joins were sorted by whether the proof cites a periphery theorem and by the name of the reading theorems.
- **Citations.** A record cites a declaration where a JSON field other than `history` names it. `history` is left out because 49 records carry one landing note naming `withinClosure_iff_closure`. Chapter citations are the lines of the chapter naming a declaration, under their section heading.
- **Apart roots.** From [THEOREM-CONNECTIVITY-APART.json](THEOREM-CONNECTIVITY-APART.json).

Data: [development/bridge-fold/classification.json](development/bridge-fold/classification.json) (one row per declaration) and [periphery-modules.json](development/bridge-fold/periphery-modules.json). Tools and steps: [development/bridge-fold/README.md](development/bridge-fold/README.md).

## 2. The three kinds

**Kind 1, renaming.** The periphery's definition is the core's.
- *Definitional*: the proof is `rfl` or `Iff.rfl`. Examples: `g0_iff`, `extension_iff` and `comparison_iff` (the core's `G0`, `Extension` and `Comparison` are `GenerativeComparison`'s on a frame's inventory); `liveStep_iff_enabled`; `Ranking.wholeRun_iff`.
- *One-to-one reading*: the two sides differ only in representation, and the proof translates them field by field, by structural recursion or by induction. Examples: an inductive closure read as `Reach` (`reached_iff_closure`), Boolean reports read as propositions (`explains_complete_iff`), test syntax read both ways with round trips (`BranchingTest.toTest`/`ofTest`, `holds_toTest`), and a periphery structure read exactly as a process in the joins (`step_iff`, `trace_iff`, `run_iff_trace`). 21 of these proofs run past 300 characters, where the representations differ more (lists against predicates, `Option` against `Prop`), but none adds a law.

**Kind 2, correspondence result.** Content that the core does not state and that is not a translation: the lifting rule L and its two countermodels; the functional articulation as the deterministic case of L; a standpoint's second step as N_rel on profiles; protection-first comparison as `BetterAt` on a frame; the exact calibration of classification-robust comparison (excluded middle is exactly what it needs); the support-gated renewal family as a balanced flow; and the constructed repair process with its loss-matching theorems.

**Kind 3, adapter.** Needed only because the core cannot import the module.
- *Instance*: a periphery theorem restated and proved through a core law (`…_by_core`, `…_of_em`, `…_of_stable`).
- *Handoff or discharge*: `OpenFutureRevision`'s producer-to-consumer handoffs and the continuation condition discharging living significance in the periphery (`…_of_unrestricted`).
- *Join*: U2's statement of a periphery law of a base object.
- *Reading map*: a definition carrying periphery data to a core object (`Frame.ofModel`, `Frame.ofInventory`, `JointFrame.ofModel`).
- *Support lemma*: a list, Bool, Nat or `Option` fact proved pure because the library's or periphery's version carries `propext`, or a local helper.

**Three of the brief's examples sort differently once their proofs are read.**
- `same_iff_alike_of_imageFinite`, `same_iff_alike_of_finiteDecided`, `same_iff_bisimilar_of_em` and `Alike.same` are two-line transfers of the core's `alike_iff_sameBranchingTests_of_em` and `alike_iff_sameBranchingTests` (`Becoming.Likeness`). Their content is already a core theorem, so they are instances (kind 3).
- `GranularityBridge.diamond_correct_iff_em` repeats the core's `Recipe.holds_after_iff_em` (`Becoming.Granularity`) argument on the periphery's types, so it is an instance too.
- `Instances.two_word_iff` computes an instance of `Segmentation.encode_iff`.

## 3. The classification

Theorems by kind and subkind. "Other" counts declarations that are not theorems. "Movable" counts theorems and other declarations that reach no periphery constant.

| Module | thms | 1 def. | 1 read. | 2 | 3 inst. | 3 hand. | 3 join | 3 sup. | other (1/2/3) | movable thms/other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `Bridge` | 123 | 11 | 23 | 23 | 42 | 8 | 0 | 16 | 27 (3/13/11) | 20/17 |
| `CompositionBridge` | 22 | 0 | 11 | 0 | 8 | 0 | 0 | 3 | 4 (3/0/1) | 3/0 |
| `JoiningBridge` | 33 | 0 | 17 | 0 | 16 | 0 | 0 | 0 | 12 (12/0/0) | 0/0 |
| `GranularityBridge` | 39 | 0 | 16 | 0 | 22 | 0 | 0 | 1 | 2 (2/0/0) | 1/0 |
| `RepairComparison` | 36 | 1 | 0 | 32 | 3 | 0 | 0 | 0 | 29 (1/28/0) | 32/28 |
| `Instances` | 22 | 2 | 7 | 0 | 11 | 0 | 0 | 2 | 3 (2/0/1) | 2/0 |
| `RenewalBridge` | 18 | 0 | 0 | 6 | 8 | 0 | 0 | 4 | 4 (0/4/0) | 15/4 |
| `CoursesBridge` | 3 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0/0 |
| **Eight bridges** | **296** | **14** | **74** | **63** | **111** | **8** | **0** | **26** | **81 (23/45/13)** | **73/49** |
| `GuardHorizonProcesses` | 14 | 0 | 2 | 0 | 0 | 0 | 10 | 2 | 3 (0/0/3) | 2/3 |
| `InstallationTraces` | 24 | 0 | 3 | 0 | 0 | 0 | 11 | 10 | 4 (0/0/4) | 10/2 |
| `ReconfigurationProcesses` | 6 | 1 | 1 | 0 | 0 | 0 | 4 | 0 | 6 (0/0/6) | 0/1 |
| `TreeSearchRuns` | 10 | 2 | 1 | 0 | 0 | 0 | 7 | 0 | 5 (0/0/5) | 0/1 |
| `QueryTraces` | 8 | 0 | 3 | 0 | 0 | 0 | 5 | 0 | 2 (0/0/2) | 0/0 |
| `DephasingRuns` | 25 | 1 | 1 | 0 | 0 | 0 | 23 | 0 | 1 (0/0/1) | 1/1 |
| `DrawnAmountProcesses` | 5 | 1 | 0 | 0 | 0 | 0 | 3 | 1 | 1 (0/0/1) | 1/0 |
| `ProjectedLawTraces` | 9 | 0 | 2 | 0 | 0 | 0 | 7 | 0 | 0 | 0/0 |
| `RuleHandoffTraces` | 21 | 0 | 3 | 0 | 0 | 0 | 17 | 1 | 0 | 0/0 |
| `ExactRecordRuns` | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 2 (0/0/2) | 0/2 |
| `JoiningCodeFrames` | 12 | 0 | 3 | 0 | 0 | 0 | 8 | 1 | 2 (0/0/2) | 0/0 |
| `JointPhaseTraces` | 9 | 1 | 2 | 0 | 0 | 0 | 6 | 0 | 1 (0/0/1) | 0/0 |
| `TestCodeFrames` | 5 | 0 | 1 | 0 | 0 | 0 | 4 | 0 | 0 | 0/0 |
| `UnitTraces` | 18 | 0 | 5 | 0 | 0 | 0 | 13 | 0 | 5 (0/0/5) | 0/1 |
| `MoveOutcomeProcesses` | 17 | 2 | 1 | 0 | 0 | 0 | 14 | 0 | 6 (0/0/6) | 0/5 |
| `RuleNarrowingProcesses` | 15 | 0 | 3 | 0 | 0 | 0 | 10 | 2 | 4 (0/0/4) | 2/0 |
| `SeedReachProcesses` | 21 | 1 | 5 | 0 | 0 | 0 | 15 | 0 | 5 (0/0/5) | 0/2 |
| `ExtendedClaimFrames` | 9 | 0 | 3 | 0 | 0 | 0 | 6 | 0 | 2 (0/0/2) | 0/2 |
| `ExtensionFrames` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0/0 |
| `InterfaceTraces` | 5 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 3 (0/0/3) | 0/0 |
| `ReachableFrames` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0/0 |
| `StrictTransportRuns` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0/0 |
| `ClassifiedBeliefProcesses` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3/0 |
| `ContextArrivalTraces` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0/0 |
| `CouplingHistoryFrames` | 5 | 0 | 2 | 0 | 0 | 0 | 3 | 0 | 1 (0/0/1) | 0/0 |
| `CourseExtensionFrames` | 5 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 1 (0/0/1) | 0/1 |
| `DerivationScopeProcesses` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0/0 |
| `DescentRenewalRuns` | 12 | 0 | 2 | 0 | 0 | 0 | 10 | 0 | 2 (0/0/2) | 0/2 |
| `FeasibleProfileTraces` | 7 | 0 | 0 | 0 | 0 | 0 | 6 | 1 | 0 | 1/0 |
| `RuleRevisionTraces` | 5 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 3 (0/0/3) | 0/0 |
| `SupportGatedWebs` | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 6/0 |
| **31 joins** | **305** | **15** | **46** | **0** | **0** | **0** | **226** | **18** | **59 (0/0/59)** | **26/23** |
| **All 39** | **601** | **29** | **120** | **63** | **111** | **8** | **226** | **44** | **140 (23/45/72)** | **99/72** |

By kind, with what cites it:

| Kind | Theorems | Other | Theorems named by a record | Records | Chapter sections naming one | Movable theorems | `bridge-interface` roots held |
|---|--:|--:|--:|--:|---|--:|--:|
| 1 renaming | 149 (29 definitional, 120 readings) | 23 | 46 | 28 | none | 3 | 8 |
| 2 correspondence result | 63 | 45 | 49 | 9 | §2, §6.5, §8.6, §9 | 45 | 2 |
| 3 adapter | 389 (111 instances, 8 handoffs, 226 joins, 44 support) | 72 | 120 | 52 | §2, §6.12, §6.13, §8.6 | 51 | 8 |

Notes on the table:
- **Joins are cited by almost nothing.** Of the 305 join theorems, 7 are named by a record, in 6 records (`relational-renewal-classification` names five), and two by the chapter (§2, `SupportGatedWebs`). They carry the connectivity measure: U2 took the periphery's apart theorems from 814 to 229 ([study §167](BECOMING-RENEWAL-READING.md#167-the-unification-follow-through-u2)).
- **Records citing the ring.** 58 of the 238 records name at least one of the 741 declarations. Five name only kind-1 declarations: `becoming-renewal-reading`, `branching-target-uniqueness`, `incidence-common-refinement`, `metaethical-core-characterization` and `ranking-under-readings`.
- **Kind 2 by record.** Nine records name kind-2 declarations:
  - `finite-aggregation-within-restorable-basic-losses` (51 declarations of `RepairComparison`);
  - `becoming-spine-instances` (11: the lifting rule L, its countermodels and `articulation_iff_lifted`);
  - `classification-robust-generative-comparison` (8);
  - `supported-renewal-recovery` (6) and `relational-renewal-classification` (4), both on `SupportGated`;
  - `practical-judgment-g0-j` and `alignment-direction-g0-j` (5 each, `Judgment`);
  - `self-good-reachable-g0` (4, the profile valuation);
  - `levels-of-closure` (1, `withinClosure_iff_closure`).

The full list of declarations by module and kind is in the appendix.

### 3.1 The 20 `bridge-interface` roots

Of the 20 roots of category `bridge-interface`, 18 are in the 39 modules:
- **Kind 1 (8).** Definitional: `Ranking.wholeRun_iff`, `chance_includedOn_iff`, `positionedArticulation_iff`, `securesPositiveGround_iff`. One-to-one readings: `Joining.locallyFinite_iff`, `Joining.roleTotal_iff`, `Ranking.undisturbed_eq`, `Recipe.ofProgram_toProgram`.
- **Kind 2 (2).** `classification_robust_iff_iff_em` and `two_extremes_suffice_of_em`.
- **Kind 3 (8).** Instances: `Judgment.required_of_bettered`, `all_weights_preserve_mass_iff_by_core`, `changed_history_really_ends_by_core`, `complete_diagnosability_iff_by_core`, `fulfillment_floor_by_core`, `realized_requests_supported_by_core`. Discharges: `contingent_generation_of_unrestricted`, `every_situated_position_has_reason_of_unrestricted`.

None of the 18 is movable. Every one reaches a periphery constant.

Two roots of the category lie outside the 39:
- `FallibleInspection.complete_diagnosability_iff_cross_separation` is the periphery's own theorem, which `complete_diagnosability_iff_by_core` restates.
- `Becoming.Ranking.active_of_renewed` is a theorem of the core module `Becoming.Ranking` and mentions nothing outside the core. Its category does not fit it. It is a one-line consequence of `ActiveWhereSupported`, and no Lean file uses it, in the package or the periphery. Its reason text ("an equivalence between an inherited periphery interface and a core concept") describes neither. It is listed for the register's owner (decision 5).

The 39 modules also hold 9 roots of category `model-witness`:
- `Instances`: `dephase_no_restore`, `diagonal_no_decoder`, `ideal_two_word`, `local_pair_no_update` (instances) and `evolve_eq_foldl` (a reading).
- `RepairComparison` (kind 2, movable): `b2_correspondence_involutive`, `current_support_restored`, `separated_same_life`, `support_between_episodes`.

### 3.2 What the bridge does not need

**171 declarations (99 theorems, 72 others) reach no periphery constant.** They sit in the bridge but need nothing from it:
- **The lifting rule L and its countermodels** (`LiftExtension`, `comparison_lifts`, `LiftedArticulation`, `lifted_comparison_supplies_reason`, `LiftSurvives`, `LiftCoherence`, `lift_coherent_selection_survives`, `lift_continual_improvement_has_no_survivor`, `LiftModel`): 6 theorems and 8 definitions. They are about `Frame` and `LiftBetter`, which the core already holds (`Becoming.Metaethics`).
- **The seed–edge closure** (`edgeProcess`, `Closure`, `Closure.base`, `step`, `induction`) and `withinClosure_iff_closure`, which relates two core notions.
- **The support-gated renewal family as a balanced flow** (`SupportGated`, 15 of `RenewalBridge`'s 18 theorems and its 4 definitions) and 6 of `SupportGatedWebs`' 9 theorems. They read the foundation's `RelationalRenewal.Law`, which is in the core closure.
- **The whole of `ClassifiedBeliefProcesses`** (3 theorems). It imports only `Becoming.Inquiry` and reads the foundation's `InquirySufficiency`.
- **The constructed repair process** of `RepairComparison` (32 theorems, 28 other declarations). Only its 4 theorems on `GenerativeLossComparison` and `SufficientMatching` reach the periphery.
- **Support lemmas and reading maps whose only users stay in the bridge**: 33 theorems and 30 others, with no reason to move on their own. Examples: the list, Bool and `Option` lemmas, `observe`, `Frame.bare`, `admittedProcess` and `Judgment.frame`.

### 3.3 Periphery modules a kind-1 reading could retire

The 39 modules reach 67 periphery modules ([periphery-modules.json](development/bridge-fold/periphery-modules.json)).
- **20 have no live importer** in the Lean tree: `AlignmentDirection`, `BecomingCompatibility`, `BecomingReversibility`, `ClassificationRobustJudgment`, `CorrectionInfrastructure`, `CutCoverageAudit`, `DerivedHistoryLaw`, `EvaluatorGrounding`, `ExplanatoryResiduals`, `GenerativeLossComparison`, `JointInterpretation`, `OpenFutureRevision`, `PositionedPositiveReason`, `PracticalReach`, `ProtectionPriorityRival`, `RelationalBecoming`, `RelationalReduction`, `RenewalComparison`, `RenewalRecovery` and `WholeGroundCoverage`. Together they hold 288 theorems. 104 declarations of the ring (95 theorems) reach only these modules, 13 records name them, and 4 `bridge-interface` roots are among them. That is the upper bound of what retiring all twenty could remove.
- **The other 47 are imported by live periphery modules.** The two most read by kind 1 are foundations of the periphery. `GenerativeComparison` is imported by 7 modules, among them `PositionedPositiveReason`, `EvaluatorGrounding` and `RenewalComparison`. `PracticalJudgment` is imported by 15, outside the run too (`CrossedClaims`, `SustainedJudgment`, `GoalRevision`, …). Their definitions are the core's by `Iff.rfl`, but the modules cannot be retired while those dependents stay live.

Matching names found no periphery module whose every theorem the ring restates through the core. Matching names undercounts. The core proves `GenerativeComparison.generative_extension_irreflexive` and `…_transitive` as `Extension.irrefl` and `Extension.trans`, under other names. Which modules are fully restated is therefore open, and it is fold step 0.

### 3.4 Two duplications

- **The seed–edge closures.** `SeedReachProcesses.reached_iff` and `cutReach_iff` (U2 joins) state, for any process whose moves are the edges, what `Bridge.reached_iff_closure` and `cutReach_iff_closure` state for the edge process. `Closure seed edge` is `FromSeed (edgeProcess edge) seed` by definition.
- **The recipe calibration.** `GranularityBridge.diamond_correct_iff_em` proves on the periphery's types the argument the core gives as `Recipe.holds_after_iff_em`.

## 4. Fold plan

The plan follows the three kinds:
- Kind 2 moves into the core where it can be stated there.
- Kind 1 goes away only with the periphery module it reads.
- Kind 3 stays, under structural names where a fold makes new files.

Moving a declaration between files keeps its full Lean name, because names follow namespaces, not files. So no step renames anything, and no record's claim text changes. Only `proof_bindings`, the apart register's `module` field and the counts change.

Counts before: core 183 modules and 7,653 theorems (closure 186 and 7,727); bridge ring 39 modules and 601 theorems; spine 8,254; periphery-join ring 26 modules and 237 theorems; 78 inherited modules bound by hash; 326 modules in the compile order. These are receipt `20261018T093527.497358Z`'s counts. While this study was written, M2 (`Becoming.SelectionPool`) was landing in the shared checkout with receipt `20261018T122313.319851Z`: core 184 modules and 7,686 theorems (closure 7,760), compile order 327, and the bridge ring unchanged at 39 modules and 601 theorems. The core counts after each step shift by M2's additions; the bridge counts do not.

**Step 0: audit restatement (read-only, no count changes).** For each of the 20 leaf modules of section 3.3 (and on request the other 47), match every theorem against the core under the kind-1 identifications, by statement, not by name. The output is a per-module verdict: fully restated, partly restated, or not restated. Step 3 needs this verdict.

**Step 1: move what reaches no periphery constant (recommended).** Move 66 theorems and 42 other declarations, with names unchanged:

| Group | Theorems / other | To | Records whose `proof_bindings` change |
|---|---|---|---|
| (a) lifting rule L and `LiftModel` | 6 / 8 | `Becoming.Metaethics`, after `LiftBetter` | `becoming-spine-instances` |
| (b) seed–edge closure, `withinClosure_iff_closure` | 4 / 2 | `Becoming.Feedback`, beside `WithinClosure` | `becoming-spine-instances`, `levels-of-closure` |
| (c) support-gated family as a flow (`SupportGated` and `SupportGatedWebs`' 6) | 21 / 4 | a new core module, named by the core law (decision 1) | `relational-renewal-classification`, `supported-renewal-recovery`, `joint-difference-making`, `becoming-return-grades` |
| (d) `ClassifiedBeliefProcesses` | 3 / 0 | re-registered from `BRIDGE` to `CORE` in the checker; no Lean edit | none |
| (e) the constructed repair process | 32 / 28 | a new core module beside `Becoming.LossMatching` (decision 1) | `finite-aggregation-within-restorable-basic-losses` |

What stays where:
- `RenewalBridge` keeps 3 theorems: `pulse_restores`, `overdraw_extension` and `contest_extensions`.
- `SupportGatedWebs` keeps 3.
- `RepairComparison` keeps the 4 theorems that reach `GenerativeLossComparison.Strict`, with `SufficientMatching`: the three conditional anchors under the supplied sufficiency commitment, which its header names as an application premise, and `sufficientMatching_iff`, which shows that commitment to be the core's `Frame.SufficientMatching`.

Effects of step 1:
- **Counts.** Core 183 → 186 modules (with (c) and (e) as new modules and (d) re-registered) and 7,653 → 7,719 theorems; core closure 7,727 → 7,793. Bridge ring 39 → 38 modules and 601 → 535 theorems. Spine unchanged at 8,254. Compile order 326 → 328. Generated `injEq` lemmas on `propext`: core closure 100 → 101 and bridge side 5 → 4 (`RepairComparison.State.mk.injEq` moves).
- **Apart register.** The 4 `RepairComparison` model-witness roots change `module`. No `bridge-interface` root moves. `THEOREM-CONNECTIVITY.py --check` must be rerun, since roots are keyed by module.
- **Chapter §9.** The core and bridge rows change. §6.5 can then cite L as a core law.
- **Checks.** These declarations already have empty axiom reports, which the bridge audit enforces, so they meet the pure-core rule as they stand. Each target module's import closure must stay inside the core. That holds, because the moved declarations reach only the prelude, the foundation and the core.

**Step 2: state what stays of kind 2 as correspondence results (recommended: no move).** 18 theorems and 5 other declarations reach the periphery by their statement:

| Group | Theorems | Records | Why it stays |
|---|--:|---|---|
| functional articulation as the deterministic case of L (`situationProcess`, `situation_enabled_iff`, `situation_lift_iff`, `articulation_iff_lifted`) | 3 | `becoming-spine-instances` | it is about `GenerativeComparison.Situation` |
| a standpoint's second step as N_rel on profiles (`profileValuation`, `tolerant_iff_neutral`, `chain_iff_reach_profiles`, `selfGood_profiles`) | 3 | `self-good-reachable-g0` | it is about `EvaluatorGrounding.Standpoint` |
| protection-first comparison as `BetterAt` (`Judgment.included_*_iff`, `better_iff_betterAt`, `frontier_iff`, with `Judgment.frame`, `protecting`, `gaining`) | 4 | `practical-judgment-g0-j`, `alignment-direction-g0-j` | `BetterAt` states J1/J2, commitments the core does not assert; moving it in would put a comparison commitment into the core |
| classification-robust comparison and its calibration (`compared_*`, `classification_robust_iff_of_em`, `two_extremes_suffice_of_em`, `classification_robust_iff_iff_em`, `CoursesBridge`'s two) | 8 | `classification-robust-generative-comparison` | the comparison is `PracticalJudgment.Better`, J1/J2 again; the calibration is a logical fact about a commitment |

Without a Lean change, the records can state these four groups as correspondence results, not "bridge interfaces". The two roots `classification_robust_iff_iff_em` and `two_extremes_suffice_of_em` could then carry a category of their own in the register. They are calibrations of a periphery notion, not equivalences of interfaces (decision 5).

**Step 3: retire kind 1 module by module, after step 0 (recommended only where step 0 finds full restatement and nothing live imports the module).** For each such module:
- **Bytes.** It keeps its path and bytes, under board rule 8 and because receipts bind it by sha256. Its records mark it superseded and point `canonical_source` at the core theorems.
- **Bridge.** The ring's kind-1 and kind-3 declarations reaching only that module are deleted once no live record field names them. Its kind-2 declarations, if any, are first restated or kept.
- **Run.** If nothing left in the run imports the module, the run stops compiling it, and the 78 inherited modules drop by one.

Upper bound over all 20 leaf modules: 95 theorems (25 of kind 1, 3 of kind 2, 67 of kind 3) and 9 other declarations leave the ring, together with 4 `bridge-interface` roots (`securesPositiveGround_iff`, `positionedArticulation_iff`, `Ranking.undisturbed_eq` and `changed_history_really_ends_by_core`), and 13 records change their bindings. The bound is not reachable as it stands: `ClassificationRobustJudgment` carries kind-2 content (step 2), and `GenerativeLossComparison` and `OpenFutureRevision` carry the application premises and handoffs.

Two rules pull against each other here. Only the latest version stays live ([AGENTS.md](../../../../AGENTS.md)), and superseded material moves to `history/` with `research.py move`. But board rule 8 keeps an original file's path, and old receipts name source paths. Marking in place keeps old receipts re-checkable; moving the file breaks them (decision 2).

**Step 4: keep kind 3, under structural names only where the fold makes new files.**
- **What stays.** The 111 instances, 8 handoffs and 226 joins are how the periphery's theorems, and its records, rest on the core while the periphery stays live.
- **No renaming sweep.** A sweep after landing needs a name that states a wrong meaning ([naming study §7](REGISTRATION-VOCABULARY-STUDY.md#7-decisions-18-october-2026)). `Bridge`, `…Bridge` and the `…_by_core` suffix name a role and a provenance, not a wrong structure, so they stay. The files step 1 creates, and any split of `Bridge.lean` by core law (board rule 8: "a correspondence module is named after the core law it instantiates"), take structural names when they are made.
- **The duplications of section 3.4 fold here.** `reached_iff_closure` and `cutReach_iff_closure` become corollaries of `SeedReachProcesses.reached_iff` and `cutReach_iff` at the edge process. `diamond_correct_iff_em` becomes a transfer of `Recipe.holds_after_iff_em` through `Recipe.ofProgram` and `holds_after_ofProgram`. Theorem counts are unchanged; only proofs change.
- **The chapter's count row.** It can report the joins apart from the bridges: 8 bridges with 296 theorems (239 after step 1) and 31 joins with 305 (296 after step 1). This makes plain that the joins are the measure's adapters, not interfaces (decision 3).

## 5. Decisions for Ren

1. **Step 1.** Whether to move the 66 theorems and 42 other declarations into the core. Moving `RepairComparison`'s witness, group (e), into the core is the one part that is a judgment, not a fact. Its theorems are core-only, but the module reads its episodes as basic losses, an application premise its header names. The alternative keeps (e) in the bridge and moves (a) to (d): 34 theorems and 14 other declarations.
2. **Retiring a periphery module.** Whether a retired module is marked superseded in place or moved to `history/`.
3. **The chapter's count row.** Whether it reports joins and bridges separately.
4. **Step 0.** Whether to run the restatement audit, read-only, as the basis for step 3.
5. **The register's categories.** Whether `Becoming.Ranking.active_of_renewed` is recategorized, and whether the two calibrations of step 2 get a category of their own. These belong to the register's owner. They are listed here because the classification found them.

None of these needs a board claim until Ren decides. Steps 1, 3 and 4 are Lean work and go through the board and the landing queue.

## 6. What this does not show

- **That a kind is right where a rule assigned it.** The eight bridges were read declaration by declaration. The joins were sorted by whether a periphery theorem is cited and by the names of the reading theorems, so a join theorem proved directly on the base without citing the periphery's theorem counts as a join, not as a reading.
- **That a citation found by name is a citation of that declaration.** Names are matched on their last two components, or on the bare name where it is distinctive. A record may name a periphery theorem of the same last name.
- **That a movable declaration belongs in the core.** "Movable" is a fact about constants. Whether a statement belongs in a core module is the decision of step 1.
- **Which periphery theorems have core counterparts under other names.** That is step 0.
- **That any count after a step is checked.** The counts after each step are arithmetic on the receipt, not a run.

## 7. What was done: F1

Ren, 18 October 2026, after this study: "please do all" ([source](../../../../sources/15-codex-theory-conversations/2026-10-18-bridge-fold-do-all.md)). The AI made the five decisions of section 5 on the work's grounds; they are AI decisions, and the work, not Ren's words, is their warrant. Board item F1.

**Decision 1: step 1 moves groups (a) to (d); group (e) stays in the bridge.** The repair process reaches no periphery constant, but its declarations would keep their names in the core (`RepairComparison.Repair`, `Life`, `Claim.backbone`, the episodes), and those names are an application's vocabulary, not the core's (naming rule, board rule 8). Its module also reads the episodes as basic losses, an application premise that would come into the core with it. What moved, with full Lean names, statements and proofs unchanged, into new core modules named by the core law:

| Group | Core module | Theorems / other | From |
|---|---|--:|---|
| (a) the lifting rule L and `LiftModel` | `Becoming.Lifting` (imports `Becoming.Metaethics`) | 6 / 8 | `Bridge` |
| (b) the seed–edge closure and `withinClosure_iff_closure` | `Becoming.EdgeClosure` (imports `Becoming.Feedback`) | 4 / 2 | `Bridge` |
| (c) the support-gated family as a balanced flow | `Becoming.RenewalFlow` (imports `Becoming.Continuation`) | 21 / 4 | 15 of `RenewalBridge`, 6 of `SupportGatedWebs` |
| (d) classified beliefs after observation | `Becoming.ClassifiedBeliefProcesses`, re-registered from `BRIDGE` to `CORE` | 3 / 0 | (no Lean edit) |

The two existing core modules whose docstrings named the bridge for these declarations (`Becoming.Feedback`, `Becoming.Continuation`) now name the new modules; nothing else in them changed.

**Step 2: no record called a bridge interface.** No record calls the kind-2 groups "bridge interfaces"; that label is the apart register's, and decision 5 changes it there. Four records name moved declarations by module in their text (`becoming-spine-instances`, `levels-of-closure`, `relational-renewal-classification`, `supported-renewal-recovery`) and now name the core module; every record listing a moved declaration lists it under its new source and is bound to the F1 receipt ([`rebind_f1.py`](development/bridge-fold/rebind_f1.py), [`apply_text_f1.py`](development/bridge-fold/apply_text_f1.py)). Records whose bindings were already stale in files the fold leaves alone are left as they were; records citing a changed file (the chapter, its Chinese edition, the reference, the package README, `Bridge.lean`, `Feedback.lean`, `Continuation.lean`, `RenewalBridge.lean`) are re-pointed or rebound only where they matched it at base, each with a history note saying what changed.

**Step 4: the two duplications fold, proofs only.** `reached_iff_closure` and `cutReach_iff_closure` move from `Bridge` into `SeedReachProcesses` as corollaries of `reached_iff` and `cutReach_iff` at the edge process (`SeedReachProcesses` imports `Bridge`, so they could not stay in `Bridge` and use it). `diamond_correct_iff_em`'s converse is now the core's `Recipe.holds_after_iff_em` read through the encodings: every frame is a model's, every recipe a program's (`Recipe.ofProgram_toProgram`) and every branching test a test's (`BranchingTest.ofTest_toTest`). That use joins `Recipe.ofProgram_toProgram` to the rest, so it leaves the apart register. No renaming sweep. The chapter's count row reports the bridges and the joins apart.

**Decision 3: the count row reports bridges and joins apart.** Bridges and joins differ in kind: the joins are the connectivity measure's adapters, not interfaces.

**Decision 5: the register's categories.** A category `calibration` holds the two calibrations of classification-robust comparison (`classification_robust_iff_iff_em`, `two_extremes_suffice_of_em`): they state the exact logical principle a criterion needs, for a comparison the core does not assert, not an equivalence of interfaces. `support` is widened to a one-line unpacking of a module's own definitions, and `Becoming.Ranking.active_of_renewed` moves there ([`register_f1.py`](development/bridge-fold/register_f1.py)).

**Decisions 2 and 4: step 3 follows step 0.** Step 0, the restatement audit, runs as its own session; step 3 retires only a periphery module that step 0 finds fully restated and that nothing live imports. Decision 2: such a module is marked superseded in place, not moved to `history/`. Its path and bytes stay (board rule 8), old receipts bind it by path and sha256 and stay re-checkable, and the module is not superseded material in the sense of a draft: it is a checked proof whose content the core now states. *F3 revises the clause "that nothing live imports": an importer outside the Becoming run does not keep a module in the run, since the module keeps its path and bytes and the importer still compiles ([port program, section 2](development/bridge-fold/PORT-PROGRAM.md#2-end-state)); F1's owner agreed on 18 October. The text above is kept as F1 decided it.*

**Step 3: what step 0 found.** The [restatement audit](development/bridge-fold/RESTATEMENT-AUDIT.md) finds one of the twenty leaf periphery modules fully restated: `ExplanatoryResiduals`, all thirteen theorems stated by `Becoming.Granularity` (eleven as they stand, two with excluded middle named). It is not retired: its importer `deeper/ExplanatoryResumptionCases.lean` is live outside the run, an earlier version whose witnesses `Becoming.Midway` restates. So step 3 marks it superseded in place and nothing more: the record [`residual-continuation-correspondence`](../../../../theories/becoming/results/records/residual-continuation-correspondence.json) takes `Becoming/Granularity.lean` as its canonical source and keeps both periphery files as the earlier statement ([`step3_f1.py`](development/bridge-fold/step3_f1.py)); `GranularityBridge` keeps its readings of the module in the run. The near misses (`BecomingCompatibility`, `CutCoverageAudit`, small definitional gaps) get no new lemmas: a lemma written only to retire a file is not a result.

**Counts.** Core receipt `20261018T134446.673561Z`, checked on main cedeecfb0 with F1 in the working tree, passed with an empty core axiom report. The core has 188 modules (counting the root `Becoming`) and 7,720 theorems, 191 modules and 7,794 theorems in the closure with the foundation (184 and 7,686 before); the bridges 8 modules and 269 theorems, the pure joins 30 and 298 (39 and 601 together before); the spine keeps 8,287 theorems. The [connectivity measure](THEOREM-CONNECTIVITY.md) counts 175 of them apart from both base families (177 before). 92 records changed: 31 declaration listings moved to their new source, 45 records rebound to the F1 receipt, the rest re-pointed after reading the chapter's change.

**What this does not change.** No statement and no proof's content changed, and no result is added: a move, a re-registration and two proofs that now cite the law they repeated. The bridge keeps 269 theorems in eight modules and the joins 298 in thirty, about two thirds of them adapters, which the core's purity requires while the periphery stays live.

## Appendix: every declaration by module and kind

° marks a declaration that is not a theorem, † one that reaches no periphery constant (movable). Within a module, names drop the module's own namespace.

**`Becoming.Bridge`**

- 1 definitional (11): `commonResponse_is_robust`, `liveStep_iff_enabled`, `g0_iff`, `extension_iff`, `comparison_iff`, `securesPositiveGround_iff`, `positionedArticulation_iff`, `Conditions.living_iff_relational`, `Ranking.wholeRun_iff`, `relevance_inventory_iff`, `chance_includedOn_iff`
- 1 one-to-one reading (26): `reached_iff_closure`, `cutReach_iff_closure`, `chain_iff_reach`, `robust_iff_commonResponse`, `guarantees_iff_completes`, `after_observe_iff`†, `revise_is_after`, `BetterAt`°, `Ranking.undisturbed_eq`, `deeper_bisimulation_iff`, `branching_bisimulation_iff`, `BranchingTest.toTest`°, `BranchingTest.ofTest`°, `BranchingTest.toTest_ofTest`, `BranchingTest.ofTest_toTest`, `BranchingTest.holds_toTest`, `sameBranchingTests_iff_same`, `separated_iff`, `Judgment.strict_iff`†, `Judgment.frontier_iff_undominated`, `chance_mass_eq`, `explains_complete_iff`, `compatible_complete_iff`, `keeps_possible_iff_keeps_reach`, `admitted_feasible_iff`, `derived_same_steps`
- 2 correspondence result (36): `withinClosure_iff_closure`†, `LiftExtension`°†, `comparison_lifts`†, `LiftedArticulation`°†, `lifted_comparison_supplies_reason`†, `LiftSurvives`°†, `LiftCoherence`°†, `lift_coherent_selection_survives`†, `lift_continual_improvement_has_no_survivor`†, `situationProcess`°, `situation_enabled_iff`, `situation_lift_iff`, `articulation_iff_lifted`, `LiftModel.Act`°†, `LiftModel.options`°†, `LiftModel.frame`°†, `LiftModel.larger`°†, `LiftModel.some_outcome_does_not_lift`†, `LiftModel.lift_needs_live_middle`†, `profileValuation`°, `tolerant_iff_neutral`, `chain_iff_reach_profiles`, `selfGood_profiles`, `Judgment.frame`°†, `Judgment.protecting`°†, `Judgment.gaining`°†, `Judgment.included_protecting_iff`, `Judgment.included_gaining_iff`, `Judgment.better_iff_betterAt`, `Judgment.frontier_iff`, `compared_retains`, `compared_secondary`, `compared_of_em`, `classification_robust_iff_of_em`, `two_extremes_suffice_of_em`, `classification_robust_iff_iff_em`
- 3 instance of a core law (42): `Frame.map_preserves_bundles`, `Frame.lift_reflects_bundles`, `static_toggle_alike`, `Alike.same`, `same_iff_alike_of_finiteDecided`, `same_iff_alike_of_imageFinite`, `same_iff_bisimilar_of_em`, `tolerant_chain_reaches_by_core`, `strict_comparison_through_marginals_by_core`, `every_nat_score_trades_by_core`, `Judgment.frontier_exists`, `Judgment.required_of_bettered`, `alignment_better_iff_betterAt`, `alignment_frontier_iff`, `all_weights_preserve_mass_iff_by_core`, `fulfillment_floor_by_core`, `complete_diagnosability_iff_by_core`, `same_endpoint_possibilities_iff_return_by_core`, `irreversible_iff_endpoint_loss_by_core`, `same_steps_iff_endpoint_traces_by_core`, `exact_iff_fiber_future_by_core`, `pooling_exact_iff_join_closed_by_core`, `retained_realizes_union_by_core`, `erasure_exact_iff_context_lifting_by_core`, `arrivals_append_by_core`, `arrivals_snoc_by_core`, `no_single_context_supports_crossing_by_core`, `actual_context_change_joins_history_by_core`, `changed_history_really_ends_by_core`, `within_after_prefix_by_core`, `eventual_after_prefix_by_core`, `prepared_joint_within_one_by_core`, `initial_not_joint_within_one_by_core`, `actual_preparation_changes_effective_capacity_by_core`, `released_cannot_reach_joint_by_core`, `actual_release_loses_eventual_joint_by_core`, `release_not_returns`, `prepared_capacity_can_end_without_joint_realization_by_core`, `derivation_sound_on_scope`, `closure_over_scope_iff_basis`, `sound_goal_closure`, `common_on_scope_iff`
- 3 handoff or discharge (8): `inventory_g0_of_unrestricted`, `new_realization_of_unrestricted`, `contingent_generation_of_unrestricted`, `every_situated_position_has_reason_of_unrestricted`, `Run.novel_by_handoff`, `Run.relevance_by_handoff_of_unrestricted`, `positive_ground_by_bound_of_unrestricted`, `revised_generation_by_bound_of_unrestricted`
- 3 reading map (10): `edgeProcess`°†, `Closure`°†, `Frame.continuations`°, `observe`°†, `Frame.inventory`°, `Frame.bare`°†, `Frame.ofModel`°, `Frame.ofInventory`°, `admittedProcess`°†, `PastRelease`°
- 3 support lemma (17): `Closure.base`†, `Closure.step`†, `Closure.induction`†, `encode`°†, `encode_inj`†, `mem_filter`†, `beq_true_iff`†, `protection_successor_extension`, `list_contains_true_iff`†, `list_all_true_iff`†, `list_any_true_iff`†, `witness_true_iff`†, `some_getD`†, `joint_content_both`, `PastRelease.step`, `PastRelease.trace`, `PastRelease.not_both`

**`Becoming.CompositionBridge`**

- 1 one-to-one reading (14): `jointBisimulation_iff`, `JointTest.toTest`°, `JointTest.ofTest`°, `JointTest.toTest_ofTest`, `JointTest.ofTest_toTest`, `JointTest.holds_toTest`, `sameJointTests_iff_same`, `jointSeparated_iff`, `testsStable_ofModel`, `stepCompact_ofModel`, `jointCompact_ofModel`, `JointPlan.ofPlan`°, `JointPlan.realizes_ofPlan`, `JointPlan.draws_ofPlan`
- 3 instance of a core law (8): `same_target_unique_by_core`, `compact_same_iff_bisimilar_of_stable`, `kernel_of_exact_reduced`, `matchesParts_of_exact_reduced`, `code_joint_lifts_from_whole_of_stable`, `joint_plan_lifts_of_stable`, `realized_requests_supported_by_core`, `code_plan_has_global_support_of_stable`
- 3 reading map (1): `JointFrame.ofModel`°
- 3 support lemma (3): `mem_map_image`†, `mem_map_preimage`†, `Compact.translate`†

**`Becoming.JoiningBridge`**

- 1 one-to-one reading (29): `Joining.Move.ofSide`°, `Joining.Move.toSide`°, `Joining.ofQuestion`°, `Joining.toQuestion`°, `Joining.holds_ofQuestion`, `Joining.holds_toQuestion`, `Joining.branchSame_iff`, `Joining.compatible_iff`, `Joining.ofQuestion_mapQuestion`, `Joining.treeOf`°, `Joining.treeOf_map`, `Joining.realizes_treeOf`, `Joining.courseOf`°, `Joining.realizes_iff_trace`, `Joining.contextFrom`°, `Joining.realizes_contextFrom`, `Joining.contextSame_iff_sameTests`, `Joining.roleOf`°, `Joining.roleTo`°, `Joining.roleOf_roleTo`, `Joining.occurrenceOf`°, `Joining.occurrenceTo`°, `Joining.occurrenceOf_at`, `Joining.occurrenceTo_at`, `Joining.tupleOccurrence`°, `Joining.tupleOccurrence_at`, `Joining.openMap_iff_incidence`, `Joining.roleTotal_iff`, `Joining.locallyFinite_iff`
- 3 instance of a core law (16): `Joining.kernel_iff`, `Joining.operation_lifts_iff`, `Joining.operation_lifts_of_em`, `Joining.common_multivalued_structure_of_em`, `Joining.questions_survive_encoding_of_em`, `Joining.tree_lifts_of_em`, `Joining.unique_common_operational_structure_by_core`, `Joining.openMap_keeps_role_tests`, `Joining.roleTotal_of_hasUnits`, `Joining.units_alike_in_roles`, `Joining.idle_neutral_by_core`, `Joining.joined_idle_right_by_core`, `Joining.trace_has_units_by_core`, `Joining.open_map_does_not_force_pair_lifting_by_core`, `Joining.single_step_roles_alike`, `Joining.every_exact_account_retains_real_difference_by_core`

**`Becoming.GranularityBridge`**

- 1 one-to-one reading (18): `blocks_ofModel`, `BranchingTest.holds_ofTest`, `BranchingTest.toTest_along`, `BranchingTest.toTest_finer`, `BranchingTest.holds_finer`, `answers_finer_iff`, `Recipe.ofProgram`°, `Recipe.toProgram`°, `Recipe.toProgram_ofProgram`, `Recipe.ofProgram_toProgram`, `Recipe.leads_ofProgram`, `Recipe.toTest_after`, `Recipe.holds_after_ofProgram`, `Recipe.exists_leads_ofProgram`, `Recipe.ofProgram_wordProgram`, `Recipe.advance_ofProgram`, `Recipe.Advance.toProgram`, `cut_iff_leaves`
- 3 instance of a core law (22): `compile_correct_by_core`, `blocks_trace_iff_by_core`, `finite_trace_endpoints_by_core`, `blocks_image_finite_by_core`, `cross_granularity_history_matches_of_em`, `singleton_coverage_recovers_questions_by_core`, `full_and_block_reduced_kernels_by_core`, `diamond_correct_of_decided`, `diamond_correct_of_em`, `program_compile_correct_of_em`, `word_program_exact_by_core`, `execution_has_native_trace_by_core`, `finite_program_endpoints_of_em`, `guarded_history_matches_of_em`, `branch_executes_by_core`, `guard_hoisting_sound_by_core`, `diamond_correct_iff_em`, `cut_resume_by_core`, `execution_iff_completed_cut_by_core`, `same_preserves_resumption_by_core`, `partial_history_matches_of_em`, `resumption_after_inserted_history_by_core`
- 3 support lemma (1): `encode_eq_flatMap`†

**`Becoming.RepairComparison`**

- 1 definitional (2): `SufficientMatching`°, `sufficientMatching_iff`
- 2 correspondence result (60): `Repair`°†, `Life`°†, `Claim`°†, `State`°†, `start`°†, `backboneAfter`°†, `advance`°†, `process`°†, `states`°†, `run`°†, `episodeTime`°†, `lifeOf`°†, `protects`°†, `frame`°†, `decidableRealized`°†, `outageAt`°†, `firstEpisodeOf`°†, `availableNow`°†, `supportedNow`°†, `decidableSupportedNow`°†, `finalState`°†, `common_start`†, `generated_trace`†, `separated_same_life`†, `support_between_episodes`†, `current_support_restored`†, `historical_claim_iff_support`†, `recovery_retains_loss`†, `sameEpisode`°†, `decidableSameEpisode`°†, `toB1`°†, `a_matches_b1`†, `toA`°†, `b3_matches_a`†, `swapB2`°†, `b2_loss_correspondence`†, `b2_correspondence_involutive`†, `fragile_b3_loses_backbone`†, `fragile_a_keeps_backbone`†, `fragile_b3_not_matching`†, `allClaims`°†, `allClaims_distinct`†, `allClaims_every`†, `listed`†, `lostCount`°†, `lost_not_backbone`†, `losses_alike`†, `matches_iff`†, `lost_counts`†, `a_matches_b1_by_count`†, `b3_matches_a_by_count`†, `b2_a_neither`†, `a_b1_not_extension`†, `fragile_b3_better_than_none`†, `states_succ`†, `realized_succ`†, `episode_le_four`†, `episodeTime_pos`†, `reads_at_episode`†, `p_losses_retained`†
- 3 instance of a core law (3): `conditional_lower_anchor`, `conditional_upper_anchor`, `conditional_outer_order`

**`Becoming.Instances`**

- 1 definitional (2): `routes_eq`, `process_eq`
- 1 one-to-one reading (9): `assured_iff_completes`, `chunks_eq`, `encode_eq`, `wordFirst`°, `wordRest`°, `spelled`, `evolve_eq_foldl`, `run_eq`, `trace_iff_run`
- 3 instance of a core law (11): `routes_assured_iff`, `regulation_assured_iff`, `two_word_iff`, `ideal_two_word`, `diagonal_no_decoder`, `dephase_no_restore`, `local_pair_no_update`, `local_pair_carries_no_law`, `rule_kept`, `rule_inherited`, `rule_change_located`
- 3 reading map (1): `adopts`°
- 3 support lemma (2): `flatten_eq_join`†, `ite_some`†

**`Becoming.RenewalBridge`**

- 2 correspondence result (10): `SupportGated.renewal`°†, `SupportGated.netGive`°†, `SupportGated.flow`°†, `SupportGated.web`°†, `SupportGated.level_succ_le`†, `SupportGated.balances`†, `SupportGated.renewal_supported`†, `SupportGated.netGive_active`†, `SupportGated.givers_supported`†, `SupportGated.netGive_step`†
- 3 instance of a core law (8): `SupportGated.repair_restores`†, `SupportGated.pulse_restores`, `SupportGated.below_for_good`†, `SupportGated.ends_for_good`†, `SupportGated.overdraw_ends`†, `SupportGated.jointly_ends`†, `SupportGated.overdraw_extension`, `SupportGated.contest_extensions`
- 3 support lemma (4): `SupportGated.add_sub_le`†, `SupportGated.sub_eq_zero_of_le`†, `SupportGated.sub_pos_of_lt`†, `SupportGated.add_sub_assoc_of_le`†

**`Becoming.CoursesBridge`**

- 2 correspondence result (2): `extension_classification_robust`, `extension_classification_robust_iff`
- 3 instance of a core law (1): `frame_classification_robust_iff_of_em`

**`Becoming.GuardHorizonProcesses`**

- 1 one-to-one reading (2): `dViable_iff`, `pathSafe_iff`
- 3 join (10): `viable_succ_iff`, `viable_guard`, `not_enabled_not_admissible`, `closed_viable`, `certificate_closed`, `certificate_viable`, `kernel_viable`, `safe_path_viable`, `uniform_viable`, `uniform_finer`
- 3 support lemma (5): `Kept`°†, `Kept.trace`†, `Kept.start`†, `moves`°†, `last`°†

**`Becoming.InstallationTraces`**

- 1 one-to-one reading (3): `protocol_iff`, `run_iff`, `passes_iff`
- 3 join (11): `chosen_completes`, `none_chosen`, `route_inquiry_completes_both`, `known_route_completes`, `statewise_not_uniform`, `omitted_route_fails`, `timely_trace`, `late_no_trace`, `shutdown_trace`, `replacement_trace`, `update_trace`
- 3 reading map (2): `installation`°, `planMoves`°
- 3 support lemma (12): `bind_eq_some`†, `map_eq_some`†, `some_of_isSome`†, `any_eq_true`†, `and_left`†, `and_right`†, `all_mem`†, `find_some`†, `find_none`†, `none_ne_some`†, `Move`°†, `protocolMoves`°†

**`Becoming.ReconfigurationProcesses`**

- 1 definitional (1): `step_iff`
- 1 one-to-one reading (1): `enabled_iff`
- 3 join (4): `shared_cause_no_step`, `separated_repair_steps`, `own_draw_alone_no_step`, `combined_draw_steps`
- 3 reading map (5): `process`°, `toMerged`°, `toRepaired`°, `lowReserve`°, `combinedReserve`°
- 3 support lemma (1): `Rearrangement`°†

**`Becoming.TreeSearchRuns`**

- 1 definitional (2): `advance_found`, `advance_empty`
- 1 one-to-one reading (1): `orbit_fixed`
- 3 join (7): `orbit_reads_scan_from`, `orbit_reads_scan`, `run_reads_scan`, `run_reads_discover`, `found_without_reading_rest`, `pending_then_found`, `example_found`
- 3 reading map (4): `advance`°, `verdict`°, `read`°, `start`°
- 3 support lemma (1): `Search`°†

**`Becoming.QueryTraces`**

- 1 one-to-one reading (3): `lesson_foldl`, `lesson_trace`, `trace_iff`
- 3 join (5): `course_records_follow_sender`, `basic_course_records`, `course_record_fits_departing_operation`, `extended_course_records`, `extended_course_separates_operations`
- 3 reading map (2): `deliver`°, `queryProcess`°

**`Becoming.DephasingRuns`**

- 1 definitional (1): `dephase_dephase`
- 1 one-to-one reading (1): `operations_trace_iff`†
- 3 join (23): `run_settles`, `settles`, `diagonal_invariant`, `mass_invariant`, `diagonal_along`, `mass_along`, `prepared_run_diagonal`, `coherent_run_diagonal`, `prepared_ne_coherent`, `merges`, `process_merges`, `not_lossless`, `runs_meet`, `no_restore_along`, `prepared_run`, `coherent_run`, `prepared_run_response`, `coherent_run_response`, `no_diagonal_decoder_along`, `returns`, `control_returns`, `prepared_reading`, `coherent_reading`
- 3 support lemma (1): `operations`°†

**`Becoming.DrawnAmountProcesses`**

- 1 definitional (1): `draw_step_iff`
- 3 join (3): `basis_after`, `rests_iff_free`, `idle_rests_left_changes`
- 3 reading map (1): `draw`°
- 3 support lemma (1): `eq_zero_of_sub_eq`†

**`Becoming.ProjectedLawTraces`**

- 1 one-to-one reading (2): `commuting_iff_factors`, `fibre_iff_goAlike`
- 3 join (7): `commuting_iff_traces`, `traces_compose`, `coupled_trace`, `wiring_recurrence`, `left_not_goAlike`, `left_carries_no_law`, `assembly_draws`

**`Becoming.RuleHandoffTraces`**

- 1 one-to-one reading (3): `handoff_step_eq`, `handoffs_trace_eq`, `integrate_enabled_iff`
- 3 join (17): `formation_trace`, `revision_trace`, `inherited_course_trace`, `successor_revision_trace`, `low_support_infeasible`, `review_step_keeps_roster`, `entry_without_review_disabled`, `proposal_step_keeps_rule`, `handoff_step_keeps`, `handoffs_trace_keeps`, `fork_step`, `branch_revises`, `repeated_votes_disabled`, `wait_and_objection`, `handoff_access`, `handoff_without_participation`, `integration_without_revision`
- 3 support lemma (1): `none_ne_some`

**`Becoming.ExactRecordRuns`**

- 3 join (9): `exact_sound`, `exact_resolves`, `sound_abstains`, `sound_within`, `finer_resolves`, `kept_exact`, `abstaining_sound`, `abstaining_not_exact`, `exact_iff_restsFrom`
- 3 support lemma (2): `recordBefore`°†, `valueAt`°†

**`Becoming.JoiningCodeFrames`**

- 1 one-to-one reading (3): `possible_iff_course`, `courseExact_iff`, `courseReduced_iff`
- 3 join (8): `descends_iff`, `lift_exact_iff`, `separating_blocks`, `readings_agree`, `canonical_course_exact`, `codes_apart`, `joinable_iff`, `identity_roles_open`
- 3 reading map (2): `CourseExact`°, `CourseReduced`°
- 3 support lemma (1): `sameTests_symm`

**`Becoming.JointPhaseTraces`**

- 1 definitional (1): `step_iff`
- 1 one-to-one reading (2): `trace_end`, `evolve_trace`
- 3 join (6): `interaction_forms_joined`, `phase_keeps_local_states`, `phase_keeps_masses`, `phase_changes_cross`, `interaction_tells_apart`, `no_local_update`
- 3 reading map (1): `process`°

**`Becoming.TestCodeFrames`**

- 1 one-to-one reading (1): `alike_one_code`
- 3 join (4): `kernel_iff`, `kernels_same`, `matches_iff`, `aligned_iff`

**`Becoming.UnitTraces`**

- 1 one-to-one reading (5): `merge_assoc`, `trace_cases`, `oneStep_reads_mp`, `oneStep_reads`, `neutral_of_iff`
- 3 join (13): `associative`, `units_unique`, `boundaries_unique`, `left_unit_of_joined`, `right_unit_of_joined`, `common_unit_joins`, `left_unit_transport`, `right_unit_transport`, `oneStep_reads_mpr`, `oneStep_functional`, `oneStep_associative`, `oneStep_has_units`, `oneStep_not_chain_complete`
- 3 reading map (4): `steps`°, `idleAt`°, `stepTrace`°, `oneStepImage`°
- 3 support lemma (1): `stepsWord`°†

**`Becoming.MoveOutcomeProcesses`**

- 1 definitional (2): `covers_iff_moves`, `steps_eq`
- 1 one-to-one reading (1): `canEnsure_iff`
- 3 join (14): `covers_iff`, `completes_mono`, `common_goal`, `no_strict_gain_everywhere`, `covers_along`, `summary_iff`, `common_completes`, `free_wider_not_covering`, `law_covers_free_and_loses`, `setting_covers_and_gains`, `setting_covers_and_opens`, `setting_separate_not_joint`, `halted_ensures_nothing`, `summary_hides_loss`
- 3 reading map (1): `Covers`°
- 3 support lemma (5): `Ensures`°†, `toFalse`°†, `free`°†, `setting`°†, `halted`°†

**`Becoming.RuleNarrowingProcesses`**

- 1 one-to-one reading (3): `after_congr`, `narrowed_congr`, `mem_learn_iff`
- 3 join (10): `answer_some`, `answer_none`, `answer_of_settles`, `settles_learn_iff`, `one_sample_settles_one`, `contrasting_settles_both`, `settled_differs_from_last`, `repeated_case_leaves_other`, `contradiction_settles_nothing`, `narrow_class_settles_wrongly`
- 3 reading map (4): `sense`°, `narrowed`°, `Settles`°, `onCons`°
- 3 support lemma (2): `all_true`†, `all_of`†

**`Becoming.SeedReachProcesses`**

- 1 definitional (1): `joined_iff_moves`
- 1 one-to-one reading (5): `reached_iff`, `cutReach_iff`, `admissible_iff`, `scoped_iff_moves`, `history_iff_moves`
- 3 join (15): `fromSeed_iff_invariant`, `covers_iff_invariant`, `unreached_has_invariant`, `substitute_seeds`, `scope_reach_in_atlas`, `glued_on_reach`, `alternating_beyond_scopes`, `unconnected_coverage_insufficient`, `history_reach_keeps`, `history_fromSeed_iff`, `history_sound_on_reach`, `cut_iff_not_fromSeed`, `noCut_iff_fromSeed_of_decidable`, `upgrade_iff_dne`, `reachable_living_significance`
- 3 reading map (3): `atlasProcess`°, `scopeProcess`°, `historyProcess`°
- 3 support lemma (2): `Moves`°†, `FromSeed`°†

**`Becoming.ExtendedClaimFrames`**

- 1 one-to-one reading (3): `extend_iff`, `included_iff`, `strictIncluded_iff`
- 3 join (6): `better_gain_iff`, `better_basic_iff`, `crossed_incomparable`, `gain_transfer_iff`, `fresh_gains_decide`, `fresh_basic_reverses`
- 3 support lemma (2): `old`°†, `fresh`°†

**`Becoming.ExtensionFrames`**

- 3 join (3): `extension_new_relevance`, `survives_iff_lifted`, `restricted_survives`

**`Becoming.InterfaceTraces`**

- 1 definitional (2): `run_none`, `run_some`
- 1 one-to-one reading (3): `run_iff_trace`, `passes_iff_completes`, `valid_iff`
- 3 reading map (3): `process`°, `moves`°, `Completes`°

**`Becoming.ReachableFrames`**

- 3 join (4): `carries_compose`, `complement_closed_no_extension`, `required_through_summary`, `common_relative_on_scope`

**`Becoming.StrictTransportRuns`**

- 3 join (3): `strict_above_along`, `strict_below_along`, `reachable_reason`

**`Becoming.ClassifiedBeliefProcesses`**

- 3 join (3): `after_empty_or_inhabited`†, `classified_of_decidable`†, `sufficiency_iff_implication_of_decidable`†

**`Becoming.ContextArrivalTraces`**

- 3 join (3): `step_arrives`, `empty_support_no_arrival`, `changed_context_arrives`

**`Becoming.CouplingHistoryFrames`**

- 1 one-to-one reading (2): `admissible_trace`, `trace_admissible`
- 3 join (3): `history_meaning`, `retained_left_only`, `joint_description_separates`
- 3 reading map (1): `frame`°

**`Becoming.CourseExtensionFrames`**

- 1 definitional (2): `broad_iff`, `preferOccurs_iff`
- 3 join (3): `living_significance_relational`, `contest_extensions`, `malignant_ranks`
- 3 support lemma (1): `broad`°†

**`Becoming.DerivationScopeProcesses`**

- 3 join (4): `relative_on_scope`, `discharged_on_scope`, `lemma_extension_on_scope`, `countermodel_on_scope`

**`Becoming.DescentRenewalRuns`**

- 1 one-to-one reading (2): `alternation_state`, `alternatingRank_eq`
- 3 join (10): `no_renewal_free_tail`, `renewal_arbitrarily_late`, `renewal_within_rank`, `actual_steps`, `period_two`, `restores_arbitrarily_late`, `restoration_raises_rank`, `unrenewed_first_step`, `no_new_configurations`, `every_score_bounded`
- 3 support lemma (2): `alternation`°†, `rank`°†

**`Becoming.FeasibleProfileTraces`**

- 3 join (6): `stable_of_same`, `stable_iff_letterwise`, `joint_obstruction_refutes_stability`, `obstruction_locates_changed_profile`, `same_future_extends`, `unrestricted_stable`
- 3 support lemma (1): `feasible_nil`†

**`Becoming.RuleRevisionTraces`**

- 1 definitional (2): `step_iff`, `revising_state`
- 3 join (3): `changed_form`, `outcome_not_fixed`, `generation_by_bound_on_runs`
- 3 reading map (3): `process`°, `frame`°, `revising`°

**`Becoming.SupportGatedWebs`**

- 3 join (9): `formation_does_not_decide`†, `own_trajectory_does_not_decide`†, `jointly_consuming`†, `escalation_consumes`†, `fluctuating_dependent`†, `fluctuating_neither`†, `pulse_levels`, `unsupported_pulse_ends`, `absent_dependent`
