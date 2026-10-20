# Batch B2 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

**What is in the batch folder**
- **Modules:** five in `.../u-unification/B2/Becoming/`: `TailRuns`, `SensitivityWebs`, `CensusWebs`, `DiagonalRuns`, `OrderWorlds`. Together they hold 46 theorems, and every one reaches the base. The build shows `"unclean": []` and `"with_axioms": {}` for each.
- **`classification.json`:** covers all 25 remaining roots: 7 model-witness, 9 support, 7 logical-strength, 2 restates.
- **`apart.json`:** the measurement output.

**REPORT.md content**

Apart count, before → after (roots in brackets):

| module | before | after |
|---|---|---|
| Tail | 35 (15) | 5 (5) |
| Sensitivity | 25 (10) | 8 (5) |
| Decidedness | 33 (9) | 9 (5) |
| Diagonal | 22 (6) | 0 |
| Listing | 17 (11) | 11 (7) |
| Refinement | 1 (0) | 1 (0) |
| Order | 3 (2) | 0 |
| OrderNormal | 22 (9) | 9 (3) |
| **total** | **158 (62)** | **43 (25)** |

Across the whole spine with this overlay there are 7,260 theorems, and apart falls from 1,019 to 904.

What each module covers:
- **`TailRuns`** (Tail, Sensitivity). The reading is that every sequence is a run (`Shown.run`), and anything registered along a run is a sequence. It adds rules and principles stated of every run of every process: `FalseRule`, `TrueRule`, `VanishRule`, `FalseDecided` (WLPO of every run) and `TrueDecided` (LPO of every run). Each comes with an exactness theorem (`falseRule_iff`, `trueRule_iff`, `vanishRule_iff`, `wlpo_iff_runs`, `lpo_iff_runs`).
  - The three `*_iff_rule` roots become `changedByNoCondition_iff_runs`, `insensitive_differs_iff_runs` and `not_through_sensitive_iff_runs`.
  - The two `wlpo_of_*` roots become `insensitive_differs_decides` and `not_through_sensitive_decides`.
  - `vanishDecision_iff_lpoRule` becomes `vanishRule_iff_trueRule`. This also brings in the `raisedFrom_*` and `Tail.*_eq_true` lemmas.
  - `lpo_of_vanish_decided` becomes `vanish_decides`, and `neverIndicator_add_vanishIndicator` becomes `indicators_sum`.
- **`SensitivityWebs`**:
  - `exchange_alike_of_insensitiveAt` and `exchange_alike_of_insensitive` state the source laws for two flows following one law (`Flow.Follows` along `W.level`).
  - `wholeLaw_not_through` is the web form of `wholeLaw_not_through_sensitive`.
  - `tailLaw_courseWorld_balanced_iff` comes through `tailLaw_nonanticipating`.
- **`CensusWebs`** reads a web's activity, through `Web.Arises`/`Web.Ceases`:
  - `listed_over_stretch`, `keep_pace`, `arisings_count`, `ceasings_count`
  - `census_identityDecided`
  - `stock_eq` and `stock_le`, from `ListsOnce.total_eq`/`total_le` on `Web.stock`
  - `indiscernible_numbers_unique`, from `NumbersBy.unique` on `World.Indiscernible`
- **`DiagonalRuns`** adds `Completion`, a process on registrations; `unfolds_iff` shows the unfoldings are exactly its runs.
  - On runs of `Completion`: `gap_new`, `incomplete`, `gaps_differ`, `never_returns`, `unheld` and `complete_iff_alike`.
  - `unfoldingRun` and `unfoldingRun_open` cover the two-valued unfolding.
  - Revision along runs: `revision_never_rests` and `negation_never_rests`, plus `negation_returns` (as `Branching.Returns`).
  - `frame_gap` covers `claims_gap`.
- **`OrderWorlds`** uses the joining relation of a world's footprint, `Footprinted.Joined`:
  - `rearranges_refl`, `rearranges_symm`, `rearranges_trans`, `normalForm_normal`, `normalForm_least`, `complete_iff`
  - `halving_premises_iff`, from `Halving.stutter`
  - `commuted_rise_count`, from `Exchanged.rise_count` (the one count `World.commute_counts` leaves out)

What you must decide:
1. **The `TailRuns` iff joins.** The right side is about every run, but the left side stays about exchange laws and level sequences, as in the source. This follows the brief's example of deciding something of every run's registration. You decide whether it meets standard 1. The new rules live in `Type 1`.
2. **`indicators_sum` changes what the index means.** In Tail, `α` is indexed by conditions; read along a run it is indexed by steps. The statement is still exact. If you drop it, `neverIndicator_add_vanishIndicator` becomes a model-witness.
3. **Some joins may look like padding.** These place a general law at the base object's own relation or quantity: `tailLaw_courseWorld_balanced_iff`, `halving_premises_iff`, `stock_eq`/`stock_le`, and the `OrderWorlds` arrangement theorems.
4. **New reading definitions** each come with an exactness theorem: the five `TailRuns` rules and principles, and `DiagonalRuns.Completion`.
5. **Refinement.** `not_not_within` is not a root. It stays apart only because its one user, `Law.sameFuture_classes_unrefuted` in Identification (another batch), is apart.

Problems in the source modules, which I did not edit:
- The docstrings of Tail and Sensitivity say "within Part I", a label AGENTS.md retires.
- Tail has no web form for `wholeLaw_not_through_sensitive`; `SensitivityWebs.wholeLaw_not_through` now supplies one.
- `tailLaw_not_through_sensitive` and `tailLaw_not_through` state the same law with separate proofs, so I classified the first as restates.

Also, `git status` shows `THEOREM-CONNECTIVITY.py` modified in the shared checkout. I didn't edit it; `apart_roots.py` only patches it in memory.
