# Batch D1 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

# U batch D1: report

## Apart count (apart_roots.py with D1 overlaid)

| module | before | after |
|---|---|---|
| Becoming.ReferencePlan | 47 (37 roots) | 3 (3 roots) |
| Becoming.Composition | 4 (3 roots) | 2 (2 roots) |
| Becoming.Joining | 1 | 1 |
| Becoming.Testing | 1 | 1 |
| **the four sources** | **53** | **7** |

- Eleven theorems of `Becoming.Contacts` and `Becoming.References` now feed the base too: `added_gains`, `answers_iff`, `blind_misses`, `nat_bound`, `nat_unlisted`, `retired_loses`, `through_at_iff`, `through_data_iff`, `bool_other`, `drives_iff`, `inverted_fails`.
- Across the spine, apart theorems fell from 1,019 to 962.
- Neither new module has an apart theorem.

## Readings used

**ReferencePlan's step was already a process of the spine.** `ReferencePlan.P` steps by `execute s a = some t`, so no new step reading was needed. These theorems make the reading exact:
- `step_iff`: a step is an operation together with the fuel it uses.
- `enabled_iff`.
- `run_iff`: `run s as = some t ↔ Trace P s as t`. Only the forward direction, `run_trace`, existed before.
- `trace_unique`.
- `repair_iff`: `repair n s = some t ↔ ∃ as, as.length = n ∧ Trace chosen s as t`.

**One new reading definition.** `chosen` is the repair policy read as a process: a step is the act `choose` picks, executed.

**The native history in rounds.** `firstRound`, `secondRound` and `lastUses` split the history, joined by `actualWord_rounds` and `history_rounds` (via `trace_append_iff`). Roots about the constructed states then become laws of the traces that end at those states, through `trace_unique`.

**Composition.** The plan law is read on a `JointFrame`, which extends `Frame`; the parts relation is `F.joint`.

## Roots covered (root → join theorem)

**Steps of `P`:**

| root | join theorem |
|---|---|
| revision_binds_plan | revise_binds_plan, revise_step |
| probe_binds_both_references | probe_binds |
| install_binds_fresh | install_binds |
| frozen_reads_method | frozen_plan |
| frozen_misses | frozen_leaves_unregistered |
| revise_registers_failure, propose_from_mismatch | revise_registers |
| old_selections_remain | revise_keeps_selections |
| added_keeps_of_law | revise_keeps |
| new_contact_choice_of_law | revise_gains_contact |
| checked_pair_correct | checked_drives (an iff; its converse uses checked_pair_iff) |
| drift_fails | drift_misses |
| no_action_after_exhaustion | exhausted_not_enabled |
| first_mismatch_acquired | first_mismatch_step |
| first_use_succeeds, second_use_succeeds | first_use_meets, second_use_meets |

**Traces of `P`:**

| root | join theorem |
|---|---|
| first_repair_used_then_second_mismatch | second_mismatch_trace |
| both_revised_contacts_used | finished_trace |
| frozen_method_still_fails | frozen_control_fails |
| frozen_second_method_still_fails | frozen_second_control_fails |
| drift_after_check_can_fail | drift_control_fails |
| fuel_used_without_reset | history_uses_fuel |
| methods_change_twice | rounds_change_method |
| first_candidate_unavailable_before | first_round_installs_contact |
| first_installed_choice | first_round_registers |
| second_installed_choice | second_round_registers |
| installed_response_correct | first_round_meets, second_round_meets |

**Traces of `chosen`:**

| root | join theorem |
|---|---|
| first_policy_repair | first_repair |
| second_policy_repair | second_repair |
| erased_mismatch_cannot_activate | erased_no_repair |
| support_too_small_to_build | small_support_no_repair |
| constant_channel_rejected | constant_channel_no_repair |
| references_use_fuel_before_exhaustion | small_support_uses_fuel |
| constant_channel_contacts_use_fuel | constant_channel_uses_fuel |

**Composition:**

| root | join theorems |
|---|---|
| JointPlan.plans_lift_iff | plans_lift_iff_of_kernel; plans_lift_of_jointAlike (no premise); plans_lift_of_sameJointTests (compact pairs, stable tests) |

## Roots left apart (classification.json)

- **support:** `ReferencePlan.flip_twice`, `ReferencePlan.alike_iff_agreeOn`, `ReferencePlan.propose_without_mismatch`, `nodup_iff_distinct`, `ownStanding_other`.
- **model-witness:** `Unjoined.supports_not_realizes`.
- **restates:** `Joining.openMap_id` restates `Becoming.openMap_id` on the role frame, through `Joining.openMap_iff`.

## For the integrator to decide

1. **`chosen` and the round definitions.** Is `chosen` acceptable as the evident reading of `repair`? `repair_iff` makes it exact. Should the rounds stay as named definitions (`firstRound`, `secondRound`, `lastUses`), or be stated as prefixes of `actualWord`?
2. **∃ form or ∀ form.** Some roots have the form `(…).map f = some v`, or a conjunction about one end state. Their joins read `∃ t, Trace … t ∧ …`. Ends are determined (`trace_unique`, `step_iff_of_execute`), so that `t` is unique. A ∀ form follows in one line if preferred. Roots of the form `= some x` are stated as `↔ t = x`.
3. **No plain restatement of `plans_lift_iff`.** I left out `plans_lift_iff` with `J := F.joint` on its own, because it would only restate the source law. The kernel form and its two cases carry the root instead.
4. **Notes on the sources.** No source theorem looked wrong. One naming clash is worth knowing about: with `open ReferencePlan`, `ReferencePlan.Alike` clashes with `Becoming.Alike` and `ReferencePlan.flip` clashes with core `flip`, so the join module uses qualified names. The source docstring already flags the first clash.
