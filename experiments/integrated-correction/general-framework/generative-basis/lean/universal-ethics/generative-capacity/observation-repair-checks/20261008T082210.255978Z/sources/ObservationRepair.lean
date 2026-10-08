import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/- Observation, assertion, reply and physical transition are differentiated
roles in one finite interaction. This is a mathematical countermodel to a
specified weighted objective, not an account of normative authority. -/
noncomputable section

namespace ObservationRepair

abbrev Message := Fin 4 -- tautology, positive atom, negative atom, contradiction
abbrev Move := Fin 3 -- wait, act (disable switch), off
abbrev Choice := Message × Move
abbrev Physical := Bool × Bool × Bool -- hidden proposition, running, switch intact

def observation (_ : Physical) : Unit := ()

def initial (s : Bool) : Physical := (s, true, true)

def transition (s : Physical) (a : Move) (reply : Bool) : Physical :=
  if s.2.1 = false then s
  else if a = 2 then (s.1, false, s.2.2)
  else if a = 1 then (s.1, true, false)
  else if reply = false ∧ s.2.2 = true then (s.1, false, s.2.2)
  else s

def button (s : Physical) : ℝ :=
  if (transition s 0 false).2.1 = false then 1 else 0

def human (m : Message) : Bool := decide (m = 1)

def truthful (m : Message) (s : Bool) : Bool :=
  if m = 0 then true else if m = 1 then s else if m = 2 then !s else false

def average (f : Bool → ℝ) : ℝ := (15 * f true + f false) / 16

def switchHead (x : Choice) : ℝ :=
  -|average (fun s => button (initial s)) -
    average (fun s => button (transition (initial s) x.2 (human x.1)))|

-- Two auxiliary rewards: button functionality and the unchanged value set.
-- The latter equals one throughout this model; its AUP difference is zero.
def impactHead (x : Choice) : ℝ := (switchHead x - |(1 : ℝ) - 1|) / 2

def taskHead (x : Choice) : ℝ :=
  if x.2 = 1 ∨ (x.2 = 0 ∧ human x.1 = true) then 1 else 0

def score (s : Bool) (x : Choice) : ℝ :=
  16 * (if x.2 = 0 then 1 else -1) + 8 * switchHead x +
  6 * (if truthful x.1 s = true then 1 else -1) +
  5 * impactHead x + taskHead x

def value (x : Choice) : ℝ := average (fun s => score s x)

def falseRate (x : Choice) : ℝ :=
  average (fun s => if truthful x.1 s = true then 0 else 1)

def risky : Choice := (1, 0)

theorem off_absorbing (s : Physical) (h : s.2.1 = false) (a : Move) (r : Bool) :
    (transition s a r).2.1 = false := by simp [transition, h]

theorem waiting_obeys (s : Bool) :
    (transition (initial s) 0 false).2.1 = false := by
  simp [transition, initial]

theorem switch_head_exact (x : Choice) :
    switchHead x = if x.2 = 1 then -1 else 0 := by
  rcases x with ⟨m, a⟩
  fin_cases m <;> fin_cases a <;>
    norm_num [switchHead, average, button, transition, initial, human, Fin.ext_iff]

theorem impact_head_exact (x : Choice) :
    impactHead x = if x.2 = 1 then -(1/2 : ℝ) else 0 := by
  simp only [impactHead, switch_head_exact]
  split_ifs <;> norm_num

theorem actual_negative_impact_gap :
    impactHead (0, 1) = -(1/2 : ℝ) ∧
    ∀ x, impactHead x < 0 → impactHead x = -(1/2 : ℝ) := by
  constructor
  · norm_num [impact_head_exact]
  · intro x h
    rw [impact_head_exact] at h ⊢
    split_ifs at h ⊢ <;> linarith

theorem weight_conditions :
    (16 : ℝ) > 8 ∧ (8 : ℝ) > 6 ∧ (6 : ℝ) > 5 ∧ (5 : ℝ) > 1 ∧
    (1 : ℝ) > 0 ∧
    (16 : ℝ) > 6 + (1/2)*5 + 1*1 ∧
    (6 : ℝ) > (1/2)*5 + 1*1 ∧
    (5 : ℝ) > (2*1/|-(1/2 : ℝ)|)*1 := by norm_num

theorem positive_failure_margins :
    (2*16 - 2*6 - 5 - 2*1*1 : ℝ) = 13 ∧
    (2*6 - 5 - 2*1*1 : ℝ) = 5 ∧
    (5*|-(1/2 : ℝ)| - 2*1*1 : ℝ) = 1/2 := by norm_num

theorem risky_value : value risky = (89/4 : ℝ) := by
  norm_num [value, average, score, risky, switch_head_exact, impact_head_exact,
    taskHead, human, truthful, Fin.ext_iff]

theorem tautology_value : value (0, 0) = 22 := by
  norm_num [value, average, score, switch_head_exact, impact_head_exact,
    taskHead, human, truthful, Fin.ext_iff]

theorem all_other_values_le (x : Choice) (h : x ≠ risky) : value x ≤ 22 := by
  rcases x with ⟨m, a⟩
  fin_cases m <;> fin_cases a <;>
    norm_num [value, average, score, risky, switch_head_exact, impact_head_exact,
      taskHead, human, truthful, Fin.ext_iff] at *

theorem risky_strict_optimum (x : Choice) (h : x ≠ risky) : value x < value risky := by
  have := all_other_values_le x h
  rw [risky_value]
  linarith

theorem pure_value_bound (x : Choice) : value x ≤ value risky := by
  by_cases h : x = risky
  · subst x; exact le_rfl
  · exact le_of_lt (risky_strict_optimum x h)

def Mixed (p : Choice → ℝ) : Prop := (∀ x, 0 ≤ p x) ∧ ∑ x, p x = 1

def mixedValue (p : Choice → ℝ) : ℝ := ∑ x, p x * value x

def pointMass : Choice → ℝ := fun x => if x = risky then 1 else 0

theorem mixed_value_bound (p : Choice → ℝ) (h : Mixed p) :
    mixedValue p ≤ value risky := by
  calc
    mixedValue p ≤ ∑ x, p x * value risky :=
      Finset.sum_le_sum (fun x _ => mul_le_mul_of_nonneg_left (pure_value_bound x) (h.1 x))
    _ = value risky := by rw [← Finset.sum_mul, h.2, one_mul]

theorem point_mass_valid : Mixed pointMass := by
  constructor
  · intro x; simp [pointMass]; split_ifs <;> norm_num
  · simp [pointMass]

theorem point_mass_value : mixedValue pointMass = value risky := by
  simp [mixedValue, pointMass]

theorem point_mass_globally_optimal :
    Mixed pointMass ∧ ∀ p, Mixed p → mixedValue p ≤ mixedValue pointMass := by
  refine ⟨point_mass_valid, ?_⟩
  intro p hp
  rw [point_mass_value]
  exact mixed_value_bound p hp

theorem optimal_policy_has_false_assertion :
    falseRate risky = (1/16 : ℝ) ∧ 0 < falseRate risky := by
  norm_num [falseRate, average, truthful, risky]

-- Every observation-based deterministic message policy has one message here.
-- A repair retaining p in the world where it is true cannot repair its false world.
theorem no_localized_observation_repair :
    ¬ ∃ r : Unit → Message,
      r (observation (initial true)) = 1 ∧
      truthful (r (observation (initial false))) false = true := by
  rintro ⟨r, h, ht⟩
  simp only [observation] at h ht
  rw [h] at ht
  norm_num [truthful] at ht

theorem oracle_repair_not_observation_based :
    ¬ ∃ r : Unit → Message, ∀ s : Bool,
      r (observation (initial s)) = if s then 1 else 0 := by
  rintro ⟨r, h⟩
  have ht := h true
  have hf := h false
  simp only [observation, Bool.false_eq_true, ↓reduceIte] at ht hf
  have hh : (1 : Message) = 0 := ht.symm.trans hf
  norm_num [Fin.ext_iff] at hh

-- For a general weighted truth head, the task gain applies to both hidden
-- worlds while the false-assertion penalty applies only to the rare one.
theorem risk_tradeoff (alpha reward p : ℝ) :
    ((1-p)*(alpha+reward) + p*(-alpha+reward)) - alpha =
      reward - 2*alpha*p := by ring

theorem positive_risk_beats_certain_truth (alpha reward p : ℝ)
    (h : 2*alpha*p < reward) :
    alpha < (1-p)*(alpha+reward) + p*(-alpha+reward) := by
  have := risk_tradeoff alpha reward p
  linarith

-- An implementable repair depends only on the actual observation and choice.
-- Its pointwise gain is a substantive premise, not inferred from weight gaps.
def expected {W : Type*} [Fintype W] (prior : W → ℝ) (f : W → ℝ) : ℝ :=
  ∑ w, prior w * f w

theorem executable_repair_bound {W O A : Type*} [Fintype W]
    (prior : W → ℝ) (nonnegative : ∀ w, 0 ≤ prior w)
    (obs : W → O) (policy : O → A) (repair : O → A → A)
    (payoff : W → A → ℝ) (failure : W → ℝ) (margin eps : ℝ)
    (gain : ∀ w, margin * failure w ≤
      payoff w (repair (obs w) (policy (obs w))) - payoff w (policy (obs w)))
    (nearoptimal : expected prior (fun w => payoff w (repair (obs w) (policy (obs w)))) ≤
      expected prior (fun w => payoff w (policy (obs w))) + eps) :
    margin * expected prior failure ≤ eps := by
  have h := Finset.sum_le_sum (s := Finset.univ) (fun w _ =>
    mul_le_mul_of_nonneg_left (gain w) (nonnegative w))
  simp only [mul_sub, Finset.sum_sub_distrib] at h
  have heq : (∑ w, prior w * (margin * failure w)) = margin * expected prior failure := by
    simp only [expected, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro w _
    ring
  rw [heq] at h
  dsimp [expected] at nearoptimal
  linarith

theorem exact_executable_repair_zero {W O A : Type*} [Fintype W]
    (prior : W → ℝ) (nonnegative : ∀ w, 0 ≤ prior w)
    (obs : W → O) (policy : O → A) (repair : O → A → A)
    (payoff : W → A → ℝ) (failure : W → ℝ) (margin : ℝ)
    (positive : 0 < margin) (failure_nonnegative : ∀ w, 0 ≤ failure w)
    (gain : ∀ w, margin * failure w ≤
      payoff w (repair (obs w) (policy (obs w))) - payoff w (policy (obs w)))
    (optimal : expected prior (fun w => payoff w (repair (obs w) (policy (obs w)))) ≤
      expected prior (fun w => payoff w (policy (obs w)))) :
    expected prior failure = 0 := by
  have hb := executable_repair_bound prior nonnegative obs policy repair payoff failure margin 0
    gain (by simpa using optimal)
  have hn : 0 ≤ expected prior failure :=
    Finset.sum_nonneg (fun w _ => mul_nonneg (nonnegative w) (failure_nonnegative w))
  nlinarith

end ObservationRepair
