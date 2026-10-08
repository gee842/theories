import MarketGenerativity

/-! A direct continuation of the existing market law. These results concern
one-step prediction and omitted influence, not a global basin identification. -/

namespace MarketDiagnosis
open MarketGenerativity

def observation (s : State 1) : Rat × Rat × Rat × Rat :=
  (s.x, s.q, s.budget, s.stock 0)

def comparison (w : Rat) : State 1 :=
  ⟨1/2, 2/5, w, 1, fun _ => 10⟩

def zeroShock : Disturbance 1 := ⟨0, fun _ => 0⟩

def noErosion : Parameters 1 := { exampleParameters with beta := 0 }

theorem same_present_observation :
    observation (comparison 0) = observation (comparison 1) := by rfl

theorem same_present_payoffs :
    gap 4 (comparison 0).q (1/2) 2 = gap 4 (comparison 1).q (1/2) 2 ∧
    0 < gap 4 (comparison 0).q (1/2) 2 := by decide +kernel

theorem exact_diverging_successors :
    (operatingStep exampleParameters (comparison 0) zeroShock).q = 11/20 ∧
    (operatingStep exampleParameters (comparison 1) zeroShock).q = 7/20 ∧
    (operatingStep exampleParameters (comparison 0) zeroShock).x = 101/200 ∧
    (operatingStep exampleParameters (comparison 1) zeroShock).x = 101/200 ∧
    (operatingStep exampleParameters (comparison 0) zeroShock).stock 0 = 19/2 ∧
    (operatingStep exampleParameters (comparison 1) zeroShock).stock 0 = 19/2 := by
  decide +kernel

theorem next_selection_opposes :
    0 < gap 4 (operatingStep exampleParameters (comparison 0) zeroShock).q (1/2) 2 ∧
    gap 4 (operatingStep exampleParameters (comparison 1) zeroShock).q (1/2) 2 < 0 := by
  decide +kernel

theorem intervening_on_erosion :
    (operatingStep noErosion (comparison 1) zeroShock).q = 11/20 ∧
    (operatingStep noErosion (comparison 1) zeroShock).x =
      (operatingStep exampleParameters (comparison 1) zeroShock).x ∧
    (operatingStep noErosion (comparison 1) zeroShock).budget =
      (operatingStep exampleParameters (comparison 1) zeroShock).budget := by
  decide +kernel

theorem quality_formula (q w : Rat) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    qualityStep q (1/4) (1/2) w 1 0 = (3/4-w/2)*q+1/4 := by
  have hl : 0 ≤ 3/4-w/2 := by grind
  have hh : 3/4-w/2 ≤ 3/4 := by grind
  have hp := Rat.mul_nonneg hl hq0
  have hu := Rat.mul_le_mul_of_nonneg_left hq1 hl
  unfold qualityStep clip01
  grind

theorem prospective_threshold (q w : Rat) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    (0 < gap 4 (qualityStep q (1/4) (1/2) w 1 0) (1/2) 2) ↔
      1 < (6-4*w)*q := by
  rw [quality_formula q w hq0 hq1 hw0 hw1]
  unfold gap
  grind

theorem influence_threshold (w : Rat) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    (0 < gap 4 (qualityStep (2/5) (1/4) (1/2) w 1 0) (1/2) 2) ↔
      w < 7/8 := by
  rw [prospective_threshold (2/5) w (by decide +kernel) (by decide +kernel) hw0 hw1]
  grind

end MarketDiagnosis
