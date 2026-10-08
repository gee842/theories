import RenewingFormation
import ProtectionPriorityRival
open RenewingFormation ProtectionPriorityRival GenerativeComparison

-- A concrete instance of the law class: consuming forms more first, then stops at its budget.
example : cumulative unitWear ⟨3, 2⟩ (fun _ => 2) 1 < cumulative unitWear ⟨3, 2⟩ (fun _ => 5) 1 ∧
    cumulative unitWear ⟨3, 2⟩ (fun _ => 5) 7 = 6 ∧
    cumulative unitWear ⟨3, 2⟩ (fun _ => 2) 7 = 14 := by decide

-- Valence control: any predicate in the G0 position covers both continuations' events;
-- the separation is the ceaseless/non-ceaseless dynamics, which takes no valence argument.
example (V : (Nat → Nat) → Nat × Nat → Prop)
    (anySign : G0 (eventInventory unitWear ⟨3, 2⟩) V) :
    V (fun _ => 5) (0, 2) ∧ V (fun _ => 2) (0, 1) ∧
    Ceaseless unitWear ⟨3, 2⟩ (fun _ => 2) ∧ ¬ Ceaseless unitWear ⟨3, 2⟩ (fun _ => 5) := by
  refine ⟨(event_reading_favors_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).1,
    (event_reading_favors_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).2.2 0 1 (by decide),
    (whole_direction_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) (fun _ => show 2 < 5 by decide)).1,
    (whole_direction_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) (fun _ => show 2 < 5 by decide)).2⟩

-- A concrete scalar rival trades where the basic-condition priority does not.
example : weighted 5 0 < weighted 5 6 ∧ ¬ PracticalJudgment.Better protect gain 6 0 :=
  ⟨weighted_trades 5, priority_never_trades 6 (by decide)⟩
