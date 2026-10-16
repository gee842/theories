import RenewingFormation
import ProtectionPriorityRival
open RenewingFormation ProtectionPriorityRival GenerativeComparison

-- A concrete instance of the law class: consuming forms more first, then stops at its budget.
example : cumulative unitWear ⟨3, 2⟩ (fun _ => 2) 1 < cumulative unitWear ⟨3, 2⟩ (fun _ => 5) 1 ∧
    cumulative unitWear ⟨3, 2⟩ (fun _ => 5) 7 = 6 ∧
    cumulative unitWear ⟨3, 2⟩ (fun _ => 2) 7 = 14 := by decide

-- Joint consumption: two parts each at the full rate 2 jointly draw 4; together they form
-- only the budget 3 and then nothing, whereas either part alone forms 2 at every step.
example : cumulative unitWear ⟨0, 2⟩ (fun _ => 4) 5 = 3 ∧ formed unitWear ⟨0, 2⟩ (fun _ => 4) 5 = 0 ∧
    cumulative unitWear ⟨0, 2⟩ (fun _ => 2) 5 = 10 := by decide

-- Sign-neutrality control: any predicate in the G0 position covers both continuations'
-- events, and the Ceaseless distinction takes no valence argument. Which side a reading
-- favors is therefore not supplied by these theorems.
example (V : (Nat → Nat) → Nat × Nat → Prop)
    (anySign : G0 (eventInventory unitWear ⟨3, 2⟩) V) :
    V (fun _ => 5) (0, 2) ∧ V (fun _ => 2) (0, 1) ∧
    Ceaseless unitWear ⟨3, 2⟩ (fun _ => 2) ∧ ¬ Ceaseless unitWear ⟨3, 2⟩ (fun _ => 5) := by
  have beyond := beyond_initial_implies_current unitWear ⟨3, 2⟩ (fun _ => 5)
    (fun _ => show 2 < 5 by decide)
  refine ⟨(event_reading_recognizes_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).1,
    (event_reading_recognizes_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).2.2 0 1 (by decide),
    (ceaseless_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) beyond).1,
    (ceaseless_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) beyond).2⟩

-- A natural-number rival trades where basic-condition priority does not; the bounded
-- ratio score does not trade and ranks six gains above three.
example : weighted 5 0 < weighted 5 6 ∧ ¬ PracticalJudgment.Better protect gain 6 0 ∧
    ¬ (num 0 * den 6 < num 6 * den 0) ∧ (num 3 * den 6 < num 6 * den 3) :=
  ⟨weighted_trades 5, priority_never_trades 6 (by decide), by decide, by decide⟩
