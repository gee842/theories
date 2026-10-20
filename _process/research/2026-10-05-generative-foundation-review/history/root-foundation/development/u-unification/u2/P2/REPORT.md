# Batch P2 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

# P2 report (second pass): CorrectionReconfiguration, EvidenceQualifiedCorrection, FallibleInspection, AcquiredCorrection

47 of the 71 roots are now joined. The other 24 are classified, and none of them is left as `axiom-dependent`. The full scratch build of my seven modules shows `"unclean": []`, with no warnings, no `sorry`, no Mathlib, and no `simp`, `omega` or `decide` in my own proofs. Where the Inherited proofs needed tactics, I used only `unfold`, `cases`, `rw` with plain equations, `dsimp only`, `show` and `rfl`; the audit shows that none of these added an axiom beyond those inherited.

## Counts

| Module | Apart before → after | Roots before → after |
|---|---|---|
| CorrectionReconfiguration | 28 → 7 | 20 → 7 |
| EvidenceQualifiedCorrection | 24 → 7 | 19 → 7 |
| FallibleInspection | 24 → 13 | 18 → 10 |
| AcquiredCorrection | 24 → 0 | 14 → 0 |
| **Total** | **100 → 27** | **71 → 24** |

With my tree overlaid, the whole measure reads 911 apart and 602 roots.

## Modules

All seven are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/u2/P2/Becoming/`.

**Pure (empty reports, from the first pass):**
- **`TreeSearchRuns`** (10 theorems): the scan is the run of a determined search law `advance`.
  - New this pass: `run_reads_scan`, the exactness theorem for a run starting from any frontier.
  - It joins 3 roots.
- **`ReconfigurationProcesses`** (6 theorems): `reconfigure` is the step relation of a process.
  - It joins 4 roots. You confirmed these one-step joins and the `opened` field.

**Inherited (periphery-join ring).** Each docstring ends by naming the axioms it inherits and the periphery theorems they come from.

| Module | Theorems | Inherits (`with_axioms`) | Readings and roots joined |
|---|---|---|---|
| `TreeSearchRunsInherited` | 8 | propext, Quot.sound, Classical.choice | Laws of the search runs: `scan_budget`, `scan_sound`, `discovered_route_is_real`, `exhausted_is_scoped_absence`, `sufficient_budget_finishes`, `reachable_route_is_found`, `acquired_accounting`, `complete_finite_discovery_and_execution`. Choice comes from the last one only. |
| `DispatchProcessesInherited` | 11 | propext, Quot.sound | New reading: dispatch is a process on deliveries with tickets as actions, `step_iff`. Roots: `absent_current_route_rejects`, `current_revocation_rejects`, `successful_dispatch_is_current`, and the 6 computed dispatch and acquire-then-dispatch cases, read as steps from the acquired state. |
| `ReconfigurationProcessesInherited` | 10 | propext, Quot.sound, Classical.choice | Laws of the reconfiguration step: `unauthorized_reform_rejected`, `unavailable_candidate_rejected`, `admitted_configuration`, `ready_iff_nonempty_separated` (every step installs a nonempty, separated envelope), `reform_does_not_expand_mandate`, `old_request_rejected_after_reform`, `derived_certificate_available`, `admitted_reform_completes`, `old_approvals_fail_after_reform`, `repaired_reform_completes_correction`. Choice comes from `admitted_reform_completes` only. |
| `ProbeRunsInherited` | 21 | propext, Quot.sound | See below. |
| `InspectionProcessesInherited` | 16 | propext, Quot.sound, Classical.choice | See below. |

**`ProbeRunsInherited`** reads `probe` and `respond` as steps of one process, `inquiry`, with queries and the response as actions.
- Along every run, the actual model stays a candidate (`inspected_actual_model_is_retained`) and the candidates only narrow (`retained_subset`). A separated pool stays separated (`refinement_preserves_separation`), and an accepted certificate stays accepted while the pool is nonempty (`refinement_preserves_certificate`).
- A chosen plan completes as a two-step trace (`selected_inquiry_actually_completes`).
- `trace_iff_run` makes a plan's run exactly the trace of its query and the response. That puts the 5 computed `final` cases and 2 of the 3 plan-selection cases on traces; the third, which finds no plan, is classified (see below).

**`InspectionProcessesInherited`** reads `inspect` and `respond` as steps of one process, `audit`.
- Candidates only narrow along every run (`joint_refinement_subset`).
- Faithful reports keep the actual model (`inspection_keeps_actual_under_admitted_faults`). After such a step, an accepted certificate is sound (`refined_pool_remains_sound`) and faithful responses complete (`jointly_inspected_completion`).
- A situation that allows no query has no inspection-then-response trace (`denied_inspection_does_not_collect_or_execute`).
- `trace_iff_run` puts the 3 computed `outcome` cases on traces. Choice comes from `jointly_inspected_completion` only.

## `classification.json` (24 roots)

- **18 `model-witness`:** the static computed facts about fixed arrangements, envelopes, certificates and posteriors. There is no run or world reading for these. One of them is the plan-selection case that finds no plan, which has no trace reading.
- **5 `periphery-scope`:**
  - `derived_certificate_sound` holds of every arrangement, so a reconfiguration step would play no role in it.
  - `induced_monotone`.
  - `empty_family_rejects`.
  - `missing_reports_preserve_each_nonempty_model`. A step reading of it would need filter congruence (`funext`), which the periphery theorem doesn't bring in.
  - `responsive_survivors_exclude_opposite`.
- **1 `bridge-interface`:** `complete_diagnosability_iff_cross_separation`. `Becoming.Bridge.complete_diagnosability_iff_by_core` already proves it with an empty report.

## For you to judge

1. **Possibly vacuous trace laws.** Several computed cases are stated as "every trace from `s` ends with …". Where the root implies that the final situation differs from the start, I also prove that the trace exists. Two cases are stated only as laws of every trace, because their facts don't rule out an empty trace: `empty_candidates_trace_fails` and the slow-query half of `slow_trace_misses_deadline`. Those two could be vacuous; please check whether that's acceptable.
2. **Dispatch reading.** Steps go to the delivery `dispatch` returns, and success is read off the target delivery. `dispatch` charges its cost even when it fails, so this total reading keeps that charge rather than making failure "no step".
3. **One axiom-free theorem in the Inherited ring.** `InspectionProcessesInherited.inspect_some` has an empty report. It could move to a pure module if you want the rings strictly separated.

`apart.json` and `.build/` in the batch folder are measurement and build output.
