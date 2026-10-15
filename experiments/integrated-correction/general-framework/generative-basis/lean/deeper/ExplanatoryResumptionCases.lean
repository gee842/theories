import ExplanatoryResiduals -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Midway.formation_changes_guard`, `Becoming.Midway.testing_before_formation_changes_results`, `Becoming.Midway.same_start_distinct_remainders` — 同一陈述 / the same statement; MODULE-CLASSIFICATION.md
import ExplanatoryGranularityBoundary

/-! All witnesses reuse the preceding single connected unfolding. The branch
guard is continuation availability from its actual position, not a freely
assigned predicate. Paused organization is supplied recipe semantics. -/
set_option autoImplicit false

namespace Generative.ExplanatoryResumptionCases
open ExplanatoryBranching ExplanatoryGuardedPrograms ExplanatoryResiduals
open ExplanatoryGranularityBoundary (Phase Event exists_phase)
open ExplanatoryGranularityBoundary.Phase ExplanatoryGranularityBoundary.Event
abbrev m := ExplanatoryGranularityBoundary.unfolding

def canFinish : Test Event Empty := .after .finish .top


theorem formation_changes_guard : m.process.step safe .begin ready ∧
    ¬ Holds m safe canFinish ∧ Holds m ready canFinish := by
  exact ⟨rfl, by simp [canFinish, Holds, m, ExplanatoryGranularityBoundary.unfolding],
    ⟨done, rfl, True.intro⟩⟩

def adaptive : Program Event Empty :=
  .seq (.action .begin) (branch canFinish (.action .finish) .skip)

/-- Relative to adaptive's reached-position branch, this alternative tests too early. -/
def earlyCheck : Program Event Empty :=
  branch canFinish (.seq (.action .begin) (.action .finish)) (.action .begin)

theorem adaptive_safe_exact (t : Phase) : Executes m adaptive safe t ↔ t = done := by
  simp [adaptive, Executes, branch_executes, canFinish, Holds, exists_phase, m,
    ExplanatoryGranularityBoundary.unfolding, eq_comm]

theorem early_check_safe_exact (t : Phase) : Executes m earlyCheck safe t ↔ t = ready := by
  simp [earlyCheck, branch_executes, Executes, canFinish, Holds, m,
    ExplanatoryGranularityBoundary.unfolding]

theorem testing_before_formation_changes_results :
    Executes m adaptive safe done ∧ ¬ Executes m earlyCheck safe done := by
  constructor
  · exact (adaptive_safe_exact done).mpr rfl
  · intro h; cases (early_check_safe_exact done).mp h

/-- The same recipe includes both completion and explicit early ending after
formation. The stopped branch is retained, not discarded as a failed sample. -/
theorem adaptive_risky_exact (t : Phase) :
    Executes m adaptive risky t ↔ t = done ∨ t = blocked := by
  simp [adaptive, Executes, branch_executes, canFinish, Holds, exists_phase, m,
    ExplanatoryGranularityBoundary.unfolding, eq_comm]

def pending : Program Event Empty :=
  .choice (.seq (.action .begin) (.action .finish)) (.action .begin)

theorem same_start_reaches_distinct_residuals :
    Cut m pending safe (.action .finish) ready ∧ Cut m pending safe .skip ready := by
  constructor
  · exact ⟨[(), (), ()], .cons (.left _ _ _) (.cons (.seq (.action rfl))
      (.cons (.seqSkip _ _) (.nil _)))⟩
  · exact ⟨[(), ()], .cons (.right _ _ _) (.cons (.action rfl) (.nil _))⟩

def answer (c : Program Event Empty × Phase) (q : Test Event Empty) : Prop :=
  ∃ t, Executes m c.1 c.2 t ∧ Holds m t q

theorem remaining_program_changes_continuation :
    answer (.action .finish, ready) (.neg canFinish) ∧
    ¬ answer (.skip, ready) (.neg canFinish) := by
  simp [answer, Executes, canFinish, Holds, exists_phase, m,
    ExplanatoryGranularityBoundary.unfolding]

theorem exact_paused_accounts_retain_remaining_program {C : Type}
    (p : ExplanatoryUniqueness.Presentation (Program Event Empty × Phase) (Test Event Empty) C)
    (hp : ExplanatoryUniqueness.Exact answer p) :
    p.encode (.action .finish, ready) ≠ p.encode (.skip, ready) := by
  intro eq
  exact remaining_program_changes_continuation.2
    ((ExplanatoryUniqueness.equal_codes_same_answers hp eq (.neg canFinish)).mp
      remaining_program_changes_continuation.1)

/-- Inserted activity belongs to the same native law. It consumes the very
continuation still pending; resuming at the old position would be fictitious. -/
theorem inserted_activity_can_disable_resumption :
    m.process.step ready .finish done ∧ Executes m (.action .finish) ready done ∧
      ¬ ∃ t, Executes m (.action .finish) done t := by
  exact ⟨rfl, rfl, by simp [Executes, m, ExplanatoryGranularityBoundary.unfolding]⟩

theorem inserted_activity_changes_native_answers : ¬ Same m m ready done := by
  intro same
  have yes : Holds m ready canFinish := ⟨done, rfl, True.intro⟩
  obtain ⟨t, impossible, _⟩ := (same canFinish).mp yes
  exact impossible

/-- The interrupted trace is still admitted; what fails is the stale pending
continuation, not the existence of the earlier formation. -/
theorem interrupted_history_retained :
    Trace m.process safe [.begin, .finish] done ∧
      ¬ ∃ t, Executes m (.action .finish) done t := by
  exact ⟨.cons rfl (.cons rfl (.nil _)), inserted_activity_can_disable_resumption.2.2⟩

end Generative.ExplanatoryResumptionCases

#print axioms Generative.ExplanatoryResumptionCases.adaptive_safe_exact
#print axioms Generative.ExplanatoryResumptionCases.early_check_safe_exact
#print axioms Generative.ExplanatoryResumptionCases.testing_before_formation_changes_results
#print axioms Generative.ExplanatoryResumptionCases.adaptive_risky_exact
#print axioms Generative.ExplanatoryResumptionCases.same_start_reaches_distinct_residuals
#print axioms Generative.ExplanatoryResumptionCases.remaining_program_changes_continuation
#print axioms Generative.ExplanatoryResumptionCases.exact_paused_accounts_retain_remaining_program
#print axioms Generative.ExplanatoryResumptionCases.inserted_activity_can_disable_resumption
#print axioms Generative.ExplanatoryResumptionCases.inserted_activity_changes_native_answers
#print axioms Generative.ExplanatoryResumptionCases.interrupted_history_retained

#print axioms Generative.ExplanatoryResumptionCases.formation_changes_guard
