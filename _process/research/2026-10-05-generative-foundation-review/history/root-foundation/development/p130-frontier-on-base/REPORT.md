# P130：前沿与离群模块陈述在基上 / The frontier and the apart modules stated on the base

2026-10-16. A report by the P130 subagent (Claude Opus 5.5) for board item P130, claimed in ce808d6a from [the release-readiness review](../../../history/root-foundation/BECOMING-RELEASE-READINESS-REVIEW.md) §4. The lead saved it here, because the harness kept the subagent from writing report files. It is AI work, not Ren's words.

**Branch.** `p130-frontier-on-base`, from ce808d6a. Commits: 44be87ed (Runs, CourseWorlds), 0497eb66 (LearnableRuns), 11a868c9 (ParityReadings), b360ba49 (FinerTraces), d62bd5e5 (root imports, checker `CORE` and scope sentences), 73d2f2bd (FormedLoops), f5940006 (connectivity regenerated, with `connectivity_bases.py`). It is landed through `land-p130`.

**Scope.** Part I, with no premise beyond what each theorem names and no axiom. Only new modules were added: 6 modules with 98 theorems and 128 declarations, all with empty axiom reports. No existing statement or name changed.

## 1. The root, and why

The root is the run (`Generative.Process` with `Becoming.Run`). `Becoming.Runs` reads every base as runs, each by an exact correspondence theorem:

| Base | Read as a run | Declarations |
|---|---|---|
| `World` | A world is exactly a run of the law its webs-at-a-step and exchanges show (`Shown`). Every run on webs and exchanges is a world. Both directions hold by `rfl`. | `WebAt`, `World.webAt`, `World.law`, `World.run`, `Run.world`, `World.run_world`, `Run.world_webAt`, `Run.world_move`, `Run.world_run`, `Run.world_law_le`, `World.web_along` |
| Balance | A world balances exactly where it is a run of the law of exchange on webs. With the rest counted, every world's whole web is such a run, with no premise. | `exchangeAt`, `World.balanced_iff_run`, `World.balanced_iff_law`, `World.balancedRun`, `World.balanced_iff_exists_run`, `World.balancedRun_level`, `Run.world_balanced`, `World.balancedRun_world`, `World.restRun`, `World.restRun_web` |
| `ExchangeLaw` | A course is a world, with formations and conditions as roles of one relatum (`World.ofRoles`). It is balanced exactly where the law is feasible. Its generation is the one run of a determined law. | `ExchangeLaw.courseWorld`, `courseWorld_level`, `courseWorld_balanced_iff`, `courseRun`, `courseRun_state`, `generation`, `generation_runs`, `courseWorld_generation` |
| Coupling arrays | `carried` is the standing of a balanced world, and so of a run of the law of exchange, with no premise. | `carriedWorld`, `carriedWorld_level`, `carriedWorld_balanced`, `carriedRun`, `carriedRun_level` |
| `orbit` / `next` | An orbit is the run of the law's process. | Cited: `Law.run`, `Branching.law_run_state` |
| `Contextual`, `ParitySystem` | Readings in context form a world along every run. Gluing at a step is that world being context-free there. | Cited: `Contextual.world`. New: `Contextual.glues_iff_freeAt` |

**Why the run.** A run is the unfolding read step by step. A world is the same unfolding read as relata of one kind exchanging. The identification is exact in both directions, so these are one reading of one unfolding, not two things joined. The run is the root because every other reading is a run, while a process's configurations need not be webs. This follows the order of the nondual method and Ren's "there are no two realities" (12 October).

**What "one root" does not mean here.** The root is by correspondence, not by definition. `World` is still defined without `Process`, so the connectivity measure's `families_reach_each_other` stays false. Making the identification definitional would change existing statements, and that decision belongs to Ren. `ExchangeLaw.world` (P80b) covers one kind of relatum, and `courseWorld` covers two kinds through `ofRoles`. No theorem relates the two yet.

## 2. New modules and main statements

- **`Becoming.Runs`** (L3; 21 theorems, 35 declarations).
  - `World.run_world` and `Run.world_webAt`, both by `rfl`.
  - `World.balanced_iff_law`.
  - `Run.world_balanced`.
  - `ExchangeLaw.courseWorld_balanced_iff`: balanced exactly where feasible, for a law reading what has stood.
  - `ExchangeLaw.generation_runs`.
  - `carriedWorld_balanced` and `carriedRun_level`.
- **`Becoming.CourseWorlds`** (L4; 34 theorems, 38 declarations). The coupling-array frontier is stated on the worlds of two acts under one law (`TwoActs`):
  - Conditions of `TwoActs`: outside the part the law reads what has stood within the strengths `k`; each act reads what has stood and has a feasible course; the part's exchanges differ by at most `σ`, and the starts by at most `δ`.
  - Balance, and the rest following the law, come from the worlds' generation and are not assumed.
  - Results: `TwoActs.gap_le_carried`; `most_difference_worlds` (the bound is attained by the carrying law with the moves `giving σ` and `giving 0`); `gap_polynomial_iff_no_loop_worlds`; `gap_within_order_iff_worlds`; `most_difference_courses_worlds`; `runaway_worlds`; `apart_only_downstream_worlds`; `unread_carried_nowhere_worlds`; `break_carried_nowhere_worlds`; `formedWorld` together with `formedWorld_balanced`, `formedWorld_level` and `formedWorld_le_polynomial_before`; and the nonanticipation lemmas for `ofMoves`.
- **`Becoming.LearnableRuns`** (L4; 10 theorems, 13 declarations).
  - `restsFrom_iff`.
  - `learnable_iff`: learnable along every run of a determined law exactly where runs beginning alike in the registered frame have targets that agree from some step on.
  - `still_learnable_iff_lumped`.
  - Also `record_eq`, `rests_iff`, `course_same`, `records_same`, `agree_of_rests_both`, `not_rests_on_both`, `rests_through`.
- **`Becoming.ParityReadings`** (L4; 10 theorems, 13 declarations).
  - `Contextual.glues_iff_freeAt`.
  - `ParitySystem.world_free_iff`: a respecting world of readings is context-free at a step exactly where no selection of contexts contradicts.
  - `ParitySystem.world_met_le`.
  - `ParitySystem.freeFrame_iff`.
  - `Square.quantum_readings`: quantum registrations of the square leave the world of readings context-free at no step and fit no frame of context-free claims.
  - Also `met_congr`, `Square.QuantumAt` with `QuantumAt.not_glues`, `QuantumAt.not_freeAt`, `QuantumAt.no_free_frame`, and `Square.quantum`, `quantum_at`.
- **`Becoming.FinerTraces`** (L4; 16 theorems, 17 declarations).
  - `mem_finer_iff`: the finer courses of n steps are exactly the finer law's traces taking listed moves to listed configurations.
  - `trace_forget` and `trace_lift`, between the finer law and the law of positive weight.
  - `finer_exists_iff`.
  - `two_values_mem_iff`.
  - Membership lemmas at every universe, plus `supportLaw`, `nonzero_iff` and `two_listed`.
- **`Becoming.FormedLoops`** (L4; 7 theorems, 12 declarations).
  - `formedWorld_before`: up to a step, a world whose strengths are read off its own standing stands as the balanced world its couplings formed before that step carry.
  - `thresholdWorld_course`: the loop read off the world's own standing forms exactly at the threshold, not before.
  - `onsetWorld_course`, `scheduleWorld_course`, `sparseWorld_course`.
  - Each witness's own law is cited from Closing or Frequency. What this module adds is that each witness amount is the standing of a balanced world.

## 3. What stays apart, and why

Counts are under the original base set, with the extended base set in brackets. Every instance in §2 uses the base object's structure in its proof. Where no honest instance exists, none was written.

| Module | Apart | Why no instance was written |
|---|---|---|
| Gluing | 43 [43] | The Specker, CHSH, Square and Cycle instances, and the mixture bounds, would only add a name to `world_free_iff` / `world_met_le`. The cycle law has no base relation that is a cycle of equal-or-different relations unless one is supplied. |
| Quantum | 9 [9] | Integer-matrix algebra. |
| Typicality | 43 [43] | Counting identities over an enumeration. FinerTraces identifies the members with traces, but nothing proves that `finer` lists each trace once. |
| Situations | 32 [32] | Same as Typicality. |
| Frequency | 37 [37] | The settling calibrations quantify over every schedule. |
| Closing | 7 [7] | General formation laws for every array. They are stated on the base where the array is read off a world. |
| Remainder | 9 [9] | Array combinatorics and weight algebra. |
| Routes | 9 [9] | Array combinatorics and weight algebra. |
| Observation | 14 [11] | Array combinatorics and weight algebra. |
| Tail | 35 [10] | Mostly `ExchangeLaw` statements. The remainder are calibrations and arithmetic. |
| Sensitivity | 25 [3] | Same as Tail. |
| Propagation | 13 [3] | Same as Tail. |
| Thresholds | 22 [3] | Same as Tail. |
| Learnable | 7 [1] | Instantiation only. |
| Retrodiction | 6 [6] | Courses (P114) already states its laws on runs. |
| Loops | 2 [2] | Bound arithmetic. |
| Gain | 0 | — |

## 4. Connectivity, before and after, under both base sets

The measure was run on head 73d2f2bd, with core receipt 20261015T231055.702986Z: 215 modules, 29,151 constants.
- The committed JSON uses the original base set.
- The other columns come from `connectivity_bases.py`, which changes only the base lists. For "before" it drops the six new modules' constants, which reproduces the ce808d6a measurement exactly.
- The extended base set adds `Becoming.Law.orbit` to the Process family, and `Becoming.ExchangeLaw` and `Becoming.carried` to the World family.

| Class | Before, original | After, original | Before, extended | After, extended |
|---|---:|---:|---:|---:|
| Statement on both families | 124 | 145 | 132 | 154 |
| Statement on Process/Frame/Run/Trace | 1,300 | 1,318 | 1,470 | 1,487 |
| Statement on World/Flow/Web | 2,676 | 2,711 | 2,861 | 2,903 |
| Proof through a base family | 125 | 127 | 36 | 36 |
| Used by a theorem on the base | 1,771 | 1,888 | 1,744 | 1,836 |
| Apart: own vocabulary | 1,001 | 914 | 772 | 705 |
| Apart: prelude-only | 92 | 84 | 74 | 66 |
| **Apart, total** | **1,093** | **998** | **846** | **771** |
| Theorems | 7,089 | 7,187 | 7,089 | 7,187 |

- **New theorems.** None of the 98 is apart.
- **Existing theorems leaving apart.** 95 under the original base set and 75 under the extended one; extending the base alone moves 247.
- **By module, original base set.** Gluing 81 → 43, Quantum 37 → 9, Learnable 17 → 7, Situations 36 → 32, Context 23 → 18, Identification 48 → 44, Learning 42 → 40, Thresholds 24 → 22.
- **What is unchanged.** By definition the families still do not reach each other. There are 65 components, with 11 theorems outside the main one. Two records still rest only on apart theorems: `selection-through-a-model-of-the-options` and `typicality-by-counting`.

## 5. Builds

Each module was built with `scratch_build.py` and the shared cache, with warnings fatal. Every axiom report is empty, both for the six new modules and the root, and for the eight bridges. The new sources contain no `sorry`, `axiom`, `native_decide`, `unsafe`, `Classical`, `propext`, `Quot.sound`, `funext` or `simp`. The landing receipt is the integrator's run on `land-p130`.

## 6. Records

- **New: `worlds-are-runs`.** Laws: world ↔ run; balance ↔ a run of `exchangeAt`, with the rest-counted run; a course is a world, balanced where feasible and generated as one run; the carried amount is a balanced world's standing. Does not show: identity by definition; that every process is the law of some world; that readings glue.
- **New: `two-act-worlds-carry-the-difference`.** The worlds of two acts differ by at most the carried amount, and the bound is attained. The laws of loops, cuts, routes, closing, frequency, thresholds and observation hold of those worlds, and loops read off a world form within it.
- **Applications to existing records:**
  - `learnable-through-registration`
  - `gluing-under-parity`
  - `contextual-registration`
  - `weights-count-situations`
  - `how-loops-form`
  - `how-often-couplings-act`

## 7. Readings (the AI's, pending Ren)

1. A run is the unfolding read step by step, and a world is the same unfolding read as relata of one kind exchanging. The identification is exact, so it is one reading of one unfolding, not two things joined.
2. How much difference arrives is the difference between two worlds of one law: the actual one, and one generated by an act not taken.
3. When strengths are read off a world's own standing, which loops form, and when, is read off the world itself.

## 8. Possible next deltas

- The one-kind correspondence `ExchangeLaw.world` ↔ `courseWorld`.
- The CHSH, Specker and Square bounds as corollaries of `world_met_le`.
- A theorem that `finer` lists each trace once, so that the counts become counts of traces.
- Ren's judgment on whether to make the root definitional.
