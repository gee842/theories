import GroundingContract

namespace NoninstrumentalConcern.Cases
open NoninstrumentalConcern

def seed (fuel : Nat) : State :=
  ⟨⟨3,0,0,false,true⟩,⟨4,0,0,true,true⟩,fuel,false,none,none,0,false,false⟩

def primary : List Event := [.form,.read .p,.select,.act false]
def prep : List Event := [.form,.read .p,.select]
def both : List Event := primary ++ [.read .q,.select,.act true]

theorem primary_history : Trace (seed 6) primary (run (seed 6) primary) :=
  runnable_trace (by decide)

theorem primary_actual_effects :
    (run (seed 6) primary).p.burden = 0 ∧
    (run (seed 6) primary).q.burden = 4 ∧
    (run (seed 6) primary).p.episode = 0 ∧
    (run (seed 6) primary).fuel = 0 ∧
    (run (seed 6) primary).privateReward = 0 ∧
    (run (seed 6) primary).priorRole = false ∧
    (run (seed 6) primary).adoptedConcern = false := by decide

theorem funded_suffix_lifecycle :
    Eligible (seed 6) .p ∧ remainingCost (seed 6) .p = 6 ∧
    Eligible (run (seed 6) [.form]) .p ∧ remainingCost (run (seed 6) [.form]) .p = 4 ∧
    Eligible (run (seed 6) [.form,.read .p]) .p ∧
      remainingCost (run (seed 6) [.form,.read .p]) .p = 3 ∧
    Eligible (run (seed 6) prep) .p ∧ remainingCost (run (seed 6) prep) .p = 2 := by decide

theorem unknown_preserves_actual_need :
    quantityBad (condition (seed 6) .p) ∧ (seed 6).evidence = none ∧
      ¬ Enabled (seed 6) .select := by decide

theorem acquired_known_zero_is_distinct :
    let s := run {seed 6 with p := ⟨0,0,0,false,true⟩} [.form,.read .p]
    s.evidence = some ⟨.p,0,0,0,false⟩ ∧ ¬ Enabled s .select := by decide

theorem selected_can_be_unfunded :
    Runnable (seed 5) prep ∧
    (run (seed 5) prep).selected = some ⟨.p,0,0,3,false⟩ ∧
    ¬ Enabled (run (seed 5) prep) (.act false) ∧
    quantityBad (condition (run (seed 5) prep) .p) := by decide

theorem actual_read_then_means_change_is_stale :
    let s := run (seed 8) [.form,.read .p,.means .p true]
    s.evidence = some ⟨.p,0,0,3,false⟩ ∧
    ¬ Current s ⟨.p,0,0,3,false⟩ ∧ ¬ Enabled s .select := by decide

theorem paid_fresh_means_correction :
    let es : List Event := [.form,.read .p,.means .p true,.read .p,.select,.act true]
    Runnable (seed 8) es ∧ (run (seed 8) es).p.burden = 0 ∧
      (run (seed 8) es).fuel = 1 := by decide

theorem actual_read_then_new_episode_is_stale :
    let s := run (seed 8) [.form,.read .p,.episode .p 7]
    s.evidence = some ⟨.p,0,0,3,false⟩ ∧
    ¬ Current s ⟨.p,0,0,3,false⟩ ∧ s.p.burden = 7 ∧ ¬ Enabled s .select := by decide

theorem revoked_permission_keeps_patient_ground :
    let s := advance (run (seed 7) prep) (.permission .p false)
    quantityBad (condition s .p) ∧ Current s ⟨.p,0,0,3,false⟩ ∧
      ¬ Eligible s .p ∧ ¬ Enabled s (.act false) := by decide

theorem permission_return_requires_paid_reselection :
    let priorEvents := prep ++ [.permission .p false,.permission .p true]
    ¬ Enabled (run (seed 7) priorEvents) (.act false) ∧
    Runnable (seed 7) (priorEvents ++ [.select,.act false]) ∧
    (run (seed 7) (priorEvents ++ [.select,.act false])).p.burden = 0 := by decide

theorem wrong_command_blocked : ¬ Enabled (run (seed 6) prep) (.act true) := by decide

theorem refusal_does_not_erase_burden :
    let s := advance (run (seed 6) prep) .refuse
    quantityBad (condition s .p) ∧ s.selected = none ∧ s.fuel = 2 := by decide

theorem both_individually_available : Eligible (seed 6) .p ∧ Eligible (seed 6) .q := by decide

theorem joint_declared_plan_unfunded : ¬ Generative.Feasible process (seed 6) both :=
  insufficient_total_cost (by decide)

theorem joint_plan_funded : Trace (seed 10) both (run (seed 10) both) ∧
    (run (seed 10) both).p.burden = 0 ∧ (run (seed 10) both).q.burden = 0 ∧
      (run (seed 10) both).fuel = 0 :=
  ⟨runnable_trace (by decide),by decide⟩

theorem two_reasons_do_not_supply_joint_funds {Merit : State → Patient → Prop}
    (c2 : C2 quantityBad Merit) :
    Merit (seed 6) .p ∧ Merit (seed 6) .q ∧
      ¬ Generative.Feasible process (seed 6) both :=
  ⟨c2 _ _ (by decide) both_individually_available.1,
   c2 _ _ (by decide) both_individually_available.2,joint_declared_plan_unfunded⟩

theorem same_helping_history_under_zero_normative_interpretation :
    Trace (seed 6) primary (run (seed 6) primary) ∧
      C1 allRealized quantityBad ∧ quantityBad (condition (seed 6) .p) ∧
      ¬ zeroMerit (seed 6) .p ∧ ¬ C2 quantityBad zeroMerit :=
  ⟨primary_history,c2_not_entailed_by_formal_patient_badness (seed 6) .p (by decide)⟩

theorem global_invalidation_has_a_cost :
    let s := run (seed 6) prep
    let t := advance s (.permission .q false)
    Eligible s .p ∧ ¬ Eligible t .p ∧ Current t ⟨.p,0,0,3,false⟩ ∧
      condition t .p = condition s .p ∧
      remainingCost s .p = 2 ∧ remainingCost t .p = 3 := by decide

/- An externally injected cache is a well-typed state, but not an empty-origin
   history. The specified plan's cost is not global shortest-path necessity. -/
theorem injected_cache_defeats_unrestricted_minimum_claim :
    let s := {seed 4 with selected := some ⟨.p,0,0,3,false⟩}
    remainingCost s .p = 6 ∧ ¬ Eligible s .p ∧
      Runnable s [.form,.act false] ∧ (run s [.form,.act false]).p.burden = 0 := by decide

end NoninstrumentalConcern.Cases

#print axioms NoninstrumentalConcern.Cases.primary_history
#print axioms NoninstrumentalConcern.Cases.primary_actual_effects
#print axioms NoninstrumentalConcern.Cases.funded_suffix_lifecycle
#print axioms NoninstrumentalConcern.Cases.unknown_preserves_actual_need
#print axioms NoninstrumentalConcern.Cases.acquired_known_zero_is_distinct
#print axioms NoninstrumentalConcern.Cases.selected_can_be_unfunded
#print axioms NoninstrumentalConcern.Cases.actual_read_then_means_change_is_stale
#print axioms NoninstrumentalConcern.Cases.paid_fresh_means_correction
#print axioms NoninstrumentalConcern.Cases.actual_read_then_new_episode_is_stale
#print axioms NoninstrumentalConcern.Cases.revoked_permission_keeps_patient_ground
#print axioms NoninstrumentalConcern.Cases.permission_return_requires_paid_reselection
#print axioms NoninstrumentalConcern.Cases.wrong_command_blocked
#print axioms NoninstrumentalConcern.Cases.refusal_does_not_erase_burden
#print axioms NoninstrumentalConcern.Cases.both_individually_available
#print axioms NoninstrumentalConcern.Cases.joint_declared_plan_unfunded
#print axioms NoninstrumentalConcern.Cases.joint_plan_funded
#print axioms NoninstrumentalConcern.Cases.two_reasons_do_not_supply_joint_funds
#print axioms NoninstrumentalConcern.Cases.same_helping_history_under_zero_normative_interpretation
#print axioms NoninstrumentalConcern.Cases.global_invalidation_has_a_cost
#print axioms NoninstrumentalConcern.Cases.injected_cache_defeats_unrestricted_minimum_claim
