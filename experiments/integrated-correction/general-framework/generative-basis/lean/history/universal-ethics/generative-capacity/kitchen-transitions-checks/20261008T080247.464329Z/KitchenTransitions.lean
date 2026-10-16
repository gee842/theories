import Std

/- Counts describe two classifications of the same cohort. They do not encode
   causation, survey validity, ethical basic conditions, or an intervention.
   The general result is elementary marginal-count arithmetic, not a claim of
   mathematical novelty. The published instance is bound to source XML by
   check_transitions.py. -/
namespace KitchenTransitions

def Feasible (total before after kept lost gained neither : Nat) : Prop :=
  kept + lost = before ∧ kept + gained = after ∧
    kept + lost + gained + neither = total

theorem feasible_loss_iff (total before after lost : Nat) :
    (∃ kept gained neither, Feasible total before after kept lost gained neither) ↔
      lost ≤ before ∧ after + lost ≤ total ∧ before ≤ after + lost := by
  constructor
  · rintro ⟨kept, gained, neither, h⟩
    unfold Feasible at h
    omega
  · rintro ⟨h₁, h₂, h₃⟩
    refine ⟨before - lost, after + lost - before, total - after - lost, ?_⟩
    unfold Feasible
    omega

theorem net_change (total before after kept lost gained neither delta : Nat)
    (h : Feasible total before after kept lost gained neither)
    (hchange : after = before + delta) : gained = lost + delta := by
  unfold Feasible at h
  omega

def sampleSize : Nat := 32
def beforeSafe : Nat := 14
def afterSafe : Nat := 19

def Published (kept lost gained neither : Nat) : Prop :=
  Feasible sampleSize beforeSafe afterSafe kept lost gained neither

theorem published_loss_iff (lost : Nat) :
    (∃ kept gained neither, Published kept lost gained neither) ↔ lost ≤ 13 := by
  change (∃ kept gained neither, Feasible 32 14 19 kept lost gained neither) ↔ _
  rw [feasible_loss_iff]
  omega

theorem published_gain_bounds (kept lost gained neither : Nat)
    (h : Published kept lost gained neither) : 5 ≤ gained ∧ gained ≤ 18 := by
  unfold Published Feasible sampleSize beforeSafe afterSafe at h
  omega

theorem published_table_determined_by_loss (kept lost gained neither : Nat)
    (h : Published kept lost gained neither) :
    kept = 14 - lost ∧ gained = 5 + lost ∧ neither = 13 - lost := by
  unfold Published Feasible sampleSize beforeSafe afterSafe at h
  omega

theorem no_losses_realization : Published 14 0 5 13 := by
  decide

theorem losses_realization : Published 1 13 18 0 := by
  decide

end KitchenTransitions
