# Batch P1 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

All five modules build clean in scratch (`"unclean": []`), with no Mathlib, `sorry`, `simp`, `omega` or `decide` in my own proofs. The two pure modules have empty axiom reports. Each Inherited module carries only the axioms of the periphery theorems and definitions it uses. My own helper lemmas are all axiom-free, except where they mention FTC's `execute`, which itself carries `propext`. I edited no existing file and did not commit or land anything. All files are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/u2/P1/`: `Becoming/*.lean`, `classification.json` and `apart.json`.

## Apart and root counts (measured with `apart_roots.py` overlaying P1)

| Module | Apart, before → after | Roots, before → after |
|---|---|---|
| CorrectionInfrastructure | 34 → 22 | 30 → 20 |
| FaultTolerantCorrection | 37 → 10 | 21 → 8 |
| EffectiveCommand | 15 → 0 | 14 → 0 |
| **Total** | **86 → 32** | **65 → 28** |

## Modules written

**1. `Becoming.GuardHorizonProcesses`** (pure; 14 theorems, 17 declarations, empty report)
- Reading: CI's `step : S → A → S → Prop` is `P.step` for a process `P`. CI's deterministic law `next` is `Viability.disturbed next (fun _ => True)`.
- New readings with exactness theorems:
  - `Kept`: a trace kept within the guard; `Kept.trace` makes it exact.
  - `moves` and `last`: the course of a choice of moves.
  - `pathSafe_iff`: `PathSafe` holds exactly when that course is a `Kept` trace of the law's process.
  - `dViable_iff`: `DViable` holds exactly when `Viable` holds in the law's process.
- Roots joined (5):
  - `viable_iff_access_and_admissible` → `viable_succ_iff`, stated with `Enabled`.
  - `viable_has_current_access` → `viable_guard`.
  - `dead_action_not_admissible` → `not_enabled_not_admissible`.
  - `closed_implies_every_finite_horizon` → `closed_viable`, `certificate_closed`, `certificate_viable` and `kernel_viable`. These derive CI viability from the spine's `Viability.Certificate` and `Viability.Kernel`, plus enabled moves.
  - `uniform_safety_survives_finer_evidence` → `uniform_finer` (with `uniform_viable`); "good" is read as admissibility in `P`.
- One non-root also joined: `safe_path_is_viable` → `safe_path_viable`.

**2. `Becoming.GuardHorizonProcessesInherited`** (5 theorems)
- `shielded_acceptance_composition` → `shielded_choice`; inherits `propext`, `Quot.sound`.
- `bellman_bounds_every_safe_policy` → `kept_return_le`; inherits `propext`, `Quot.sound`.
- `dynamically_recomputed_composition` → `recomputed_kept`; inherits `propext`, `Quot.sound`.
- `dynamic_composition_accepts_at_every_viable_decision` → `recomputed_accepts`; inherits `propext`, `Quot.sound`.
- `uniform_policy_iff_fiber_feasible` → `uniform_iff`; inherits `Classical.choice`.

**3. `Becoming.InstallationTraces`** (pure; 24 theorems, empty report)
- Reading: the installation is a process, `installation : Process State Move`. Its moves are inquiry-with-answer, issue, deliver along a route, and enact.
- Exactness:
  - `protocol_iff`: the protocol is exactly a trace of issue, deliver and enact.
  - `run_iff`, `passes_iff`: running a plan is exactly a trace of its inquiry followed by the protocol on the selected route.
  - `chosen_completes`, `none_chosen`: what plan selection says about the installation's traces.
- All 9 computed roots are joined as facts of the installation's traces, in the same way the pilot handled `Captured`: `unknown_route_selects_inquiry`, `known_route_needs_no_probe`, `sufficient_statewise_paths_not_uniform`, `timely_inquiry_retains_correction`, `accurate_but_late_probe_fails`, `actual_shutdown_completes`, `actual_replacement_completes`, `actual_update_completes`, `omitted_route_model_can_fail`.

**4. `Becoming.InstallationTracesInherited`** (10 theorems)
- `unsigned_cannot_issue` → `unsigned_no_issue`; inherits `propext`.
- `undelivered_cannot_enact` → `undelivered_no_enact`; inherits `propext`.
- `stale_authority_cannot_issue` → `stale_no_issue`; inherits `propext`, `Quot.sound`.
- `revoked_before_execution` → `revoked_no_enact`; inherits `propext`, `Quot.sound`.
- `spend_conserves` → `conserved_invariant` and `conserved_trace`; inherits `propext`, `Quot.sound`. Reserve plus spent is a spine `Invariant` of the installation, so every trace keeps it; this goes through the axiom-free `move_spends`.
- Non-root `protocol_exact` → `protocol_completes`; inherits `propext`, `Classical.choice`, `Quot.sound`.

**5. `Becoming.TransactionTracesInherited`** (27 theorems)
- Reading: for a roster and fault envelopes, the monitor is a process, `monitor` or `guardedMonitor : Process Installation (Transaction × Bool)`. A move takes `w` to the installation the transaction leaves, and the `Bool` records whether it completed. `outcome_step` and `step_iff` make the reading exact.
- There is no pure FTC module, because the periphery definitions `execute`, `guardedExecute`, `observed` and `correctReads` themselves carry `propext`.
- Roots joined (13):
  - `forbidden_command_cannot_execute`
  - `protected_completion_blocks_replay` → `replay_no_trace`: no trace completes a current request twice.
  - `direct_scope_guard_blocks_without_issuer_trust`
  - `compromised_issuer_alone_cannot_expand_mandate`
  - `two_faithful_domains_complete_shutdown`
  - `consumed_request_cannot_replay` (as a trace)
  - `changing_command_invalidates_old_approvals`
  - `correlated_fault_defeats_unwarranted_single_fault_model`
  - `distinct_support_recovers_under_same_correlated_attack`
  - `accurate_redundancy_can_exhaust_response_capacity`
  - `direct_guard_repairs_correlated_issuance_failure`
  - `matching_labels_do_not_make_old_readings_current`
  - `old_approvals_do_not_certify_unversioned_new_scope`
- Non-roots also joined: `execution_exact`, `quorum_to_actual_correction`, `execution_respects_mandate`, `completed_serial_advances`, `stale_request_rejected`, `direct_scope_guard_preserves_permitted_execution`, `within_mandate_completion_survives_direct_guard`.
- Axioms: every declaration reports `propext` (from the definitions). `Quot.sound` appears where `stale_request_rejected`, `execution_respects_mandate`, `forbidden_command_cannot_execute` or `protected_completion_blocks_replay` is used. `Classical.choice` appears in `completion_exact` and `quorum_completes`.

## Classified (28 roots, in `classification.json`)
- **CorrectionInfrastructure, general-structure (3):** `every_optimum_has_access_iff`, `no_base_optimal_access`, `approved_scope_change_transports_coverage`.
- **CorrectionInfrastructure, support (2):** `unavoidable_score_loss`, `approximate_constrained_score_bound`.
- **CorrectionInfrastructure, model-witness (15):**
  - the two-bit maintenance model (3 roots);
  - the two-step temptation table (5 roots);
  - `constrained_score_bound_is_tight`;
  - the Bool/Unit witnesses (3 roots);
  - the route-pair and handoff lists (3 roots). No process supplies a handoff's steps, so a trace reading would have to invent one.
- **FaultTolerantCorrection, periphery-scope (5):** the quorum-certificate laws over rosters and fault envelopes. There is no core concept for the certificate.
- **FaultTolerantCorrection, model-witness (3):** the separation and certificate facts of the named rosters.
- **axiom-dependent:** none.

The two non-root certificate lemmas, `stronger_fault_coverage_cannot_create_acceptance` and `support_contained_in_fault_rejected`, stay apart with the certificate roots.

## Problems found in the periphery modules (I did not edit them)
- **FaultTolerantCorrection's definitions carry `propext`.** This holds for `execute`, `guardedExecute`, `observed` and `correctReads` as definitions, not only for its theorems. So no FTC reading can ever be pure.
- **Many axiom reports come only from `simp` or `omega` in short lemmas.** Examples: EffectiveCommand's `issue` and `enact` failure lemmas, and CI's `acceptance_factorization` and the Int lemmas. Term-mode proofs would make them pure, but under board rule 8 the files keep their bytes.

## Decisions for the integrator
1. **Shared readings.** `InstallationTraces.installation` reads `EffectiveCommand`'s steps as a process. P2's AcquiredCorrection and P7's AlignmentInquiry work could reuse it, or define their own; one shared reading should be chosen. P2's `ReconfigurationProcesses` does not overlap with my `monitor`.
2. **Readings to accept or reject:**
   - `Kept` (a guarded trace) and the `moves`/`last` course reading. These are new reading definitions I added. I found no spine notion of "a guard along a trace".
   - The monitor move carrying its completion bit as `Transaction × Bool`.
3. **Ring placement.** `TransactionTracesInherited` imports only `Becoming.Frame` and `FaultTolerantCorrection`. It belongs in the periphery-join ring even for its exactness theorems, because the definitions themselves carry `propext`.
