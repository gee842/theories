# Batch P3 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

## Report: U2 batch P3 (CompositionalFormation, CompositionalAcquisition, CompositionalTransmission)

Three roots now feed the base, through one new join module. Most of the rest can't be joined: 52 of the 63 roots have nonempty axiom reports in the periphery modules themselves.

**Module written:** `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/u2/P3/Becoming/QueryTraces.lean`, namespace `Becoming.QueryTraces`. It imports `Becoming.ReducedRuns` and `CompositionalTransmission`. The scratch build shows `"unclean": []` and `"with_axioms": {}` (8 theorems, 10 declarations).

**Reading used (an instance).** The transmission module's exchange is read as a process. Its configurations are exchanges and its moves are queries; a query takes `x` to `send e x`. This is `queryProcess := Assurance.ofMap deliver`.
- `lesson_foldl` shows a lesson is the fold of its queries.
- `trace_iff` makes the reading exact: a course of the process from `x` along `es` ends at `y` exactly when `y = lesson es x`. It goes through `ReducedRuns.trace_foldl`.
- The periphery's laws of records are then stated of what the receiver holds at the end of every course.

**Roots joined (3):**
- `CompositionalTransmission.teacher_program_changes_received_evidence` → `course_records_follow_sender`.
- `CompositionalFormation.old_record_can_admit_wrong_constructed_operation` → `course_record_fits_departing_operation`. Its record is read off the course by `basic_course_records`.
- `CompositionalFormation.asymmetric_composition_exposes_the_new_failure` → `extended_course_separates_operations`, via `extended_course_records`.

**Counts (apart / roots, before → after):**

| Module | Apart | Roots |
|---|---|---|
| CompositionalFormation | 37 → 35 | 25 → 23 |
| CompositionalAcquisition | 25 → 25 | 22 → 22 |
| CompositionalTransmission | 27 → 26 | 16 → 15 |

**Classification** (`classification.json`, covering all 60 remaining roots):
- **52 `axiom-dependent`**, of two kinds:
  - **40 are blocked by a definition.** Their statements name `readEvidence`, `interpretationFromRecords`, `train`, `develop`, `prepared`, `developed`, `reconsider`, `corrected`, `damaged`, `learn`, `successor`, `cohort`, `limitedCohort` or the named peers. All of these depend on `propext`. The cause is `readEvidence.match_1`: a list match with overlapping wildcard patterns.
  - **12 are blocked only by their proofs.** Their statements are axiom-free (I checked each statement as a `Prop` definition), but the proofs use `simp`, `simp_all`, `omega` or proof-level `decide`.
- **6 `model-witness`** (axiom-free): `changed_motivation_preserves_acquired_content`, `changed_order_invalidates_transfer`, `nonuniform_matches_training`, `nonuniform_fails_transfer`, `novel_expression_not_a_training_item`, `unresolved_order_can_preserve_a_novel_answer`.
- **2 `periphery-scope`**: `probe_readings` and `reencoding_preserves_content`. Both are about how the grammar evaluates expressions, which has no evident process; no core concept corresponds.

**What is wrong or misplaced in the periphery:**
- **The `propext` in the definitions can be removed.** I tested a version of `readEvidence` with exhaustive, non-overlapping patterns (`[] | [_] | [_,_] | [x,y,z] | _::_::_::_::_`, an `if` on derived equality of expressions, and a helper `single` matched the same way). It has an empty axiom report, and `readEvidence' (trialRecords c) = some (observe c)` holds by `rfl`. Even `single : | [a] => some a | _ => none` picks up `propext` under Lean 4.29.1 when the patterns overlap.
- With that fix, the definitions above would become axiom-free. The `decide` witnesses would very likely come out clean too, since `decide` over the clean definitions here was clean.
- **Strong join candidates waiting on the 12 proof-only roots.** Once reproved without `simp`/`omega`, these join directly:
  - `delivery_uses_actual_response` and `absent_response_does_not_fabricate_sample` are one-step laws of `queryProcess`.
  - `lesson_preserves_joint_support` is a conserved amount along every course.
  - `placing_accounts_parts` and `encounter_preserves_support` are conservation laws of the formation steps.
- **Naming.** `CompositionalFormation.Frame` shares a name with `Becoming.Frame`, and `Exchange` collides with a spine name under `namespace Becoming`. My module qualifies `CompositionalTransmission.Exchange` to avoid this.

**For the integrator to decide:**
1. Whether to rework these three periphery modules: the non-overlapping `readEvidence` plus axiom-free reproofs of the 12 proof-only roots. That needs edits to periphery files, which I wasn't allowed to make, and it interacts with board rule 8 (the original file keeps its path and bytes). It would unblock up to 52 roots for joins on `queryProcess` and on the formation steps.
2. Whether `QueryTraces` is an acceptable name, given the spine's other uses of "exchange" (`ExchangeLaw`, `ExchangeFlows`). I chose "query" for that reason.

Scratch probes are in my session scratchpad (`P3probe/`), not in the repository. The batch folder also holds `apart.json` and `.build` from the tools.
