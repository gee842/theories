import PracticalJudgment

/- Explicitly stipulated AI-service choices. Normative warrant is supplied by
G0/J1–J4 and actual correspondence, not established by the following predicates.
0 expands capability, 1 keeps service, 2 transfers service, 3 withdraws abruptly.
Bool indexes separate claims, not additive units of welfare. -/
namespace AlignmentDirection
open PracticalJudgment

def protection (plan : Nat) (claim : Bool) : Prop :=
  claim = true ∨ plan = 1 ∨ plan = 2

def realization (plan : Nat) (claim : Bool) : Prop :=
  (plan = 0 ∧ claim = false) ∨ (plan = 2 ∧ claim = true)

def eligible (plan : Nat) : Prop := plan < 4

theorem preserve_over_expansion : Better protection realization 1 0 := by
  apply protection_anchor (c := false)
  · intro c _
    exact Or.inr (Or.inl rfl)
  · exact Or.inr (Or.inl rfl)
  · simp [protection]

theorem expansion_has_real_gain_and_preservation_loses_it :
    realization 0 false ∧ ¬ realization 1 false := by
  simp [realization]

theorem transfer_over_preservation : Better protection realization 2 1 := by
  apply Or.inr
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro c _
    exact Or.inr (Or.inr rfl)
  · intro c _
    exact Or.inr (Or.inl rfl)
  · intro c h
    simp [realization] at h
  · intro h
    have bad := h true (Or.inr ⟨rfl, rfl⟩)
    simp [realization] at bad

theorem transfer_over_expansion : Better protection realization 2 0 :=
  better_trans protection realization transfer_over_preservation preserve_over_expansion

theorem expansion_excluded : ¬ Frontier eligible (Better protection realization) 0 :=
  dominated_excluded (a := 0) (b := 2) (by unfold eligible; decide) transfer_over_expansion

/-- Service can continue while this particular model stops. The actual demand
and reliable delivery times here are stipulated; the theorem does not certify them. -/
def demand (t : Nat) : Prop := t < 4
def oldService (t : Nat) : Prop := t < 2
def successorService (t : Nat) : Prop := 2 ≤ t ∧ t < 4

theorem covered_transfer_with_old_model_stopped :
    Covered demand oldService successorService ∧ ¬ oldService 2 := by
  constructor
  · apply no_demand_gap_transfer 2
    · intro t ht _
      exact ht
    · intro t ht needed
      exact ⟨ht, needed⟩
  · unfold oldService
    decide

theorem promised_successor_without_delivery_fails :
    ¬ Covered demand oldService (fun _ => False) :=
  uncovered_demand_is_failure (t := 2) (by unfold demand; decide) (by unfold oldService; decide) (fun h => h)

/-- When transfer harms a contributor's basic life, the old comparison no
longer applies: opposite basic protections remain unranked by this relation. -/
def conflictProtection (transfer : Bool) (claim : Bool) : Prop :=
  transfer = claim

theorem crossed_basic_losses_remain_unranked :
    ¬ Better conflictProtection noGain true false ∧
    ¬ Better conflictProtection noGain false true :=
  competing_claims_incomparable

/-- A change of vocabulary preserves the requirement only with faithful
coverage of admissible choices and unchanged task meaning. -/
theorem revision_preserves_requirement {H K : Type}
    {ad : H → Prop} {ad' : K → Prop} {task : H → Prop} {task' : K → Prop}
    (f : H → K) (forward : ∀ a, ad a → ad' (f a))
    (cover : ∀ b, ad' b → ∃ a, ad a ∧ f a = b)
    (meaning : ∀ a, task a ↔ task' (f a)) (required : Required ad task) :
    Required ad' task' :=
  required_under_faithful_redescription f forward cover meaning required

end AlignmentDirection
