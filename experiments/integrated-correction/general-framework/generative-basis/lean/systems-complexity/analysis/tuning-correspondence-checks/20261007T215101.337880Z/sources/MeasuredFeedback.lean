import EmbodiedChoiceScales

/-! A real-number abstraction of the published TCLab PI command, not a proof of
floating-point execution, sensor truth, thermal dynamics or ethical preference.
Readings, retained integral, actuator command and heat response are differentiated
relations of the same physical process. The measured records constrain this
abstraction through a separate archival replay. -/
namespace MeasuredFeedback
noncomputable section

structure Sample where
  target : ℝ
  reading : ℝ
  elapsed : ℝ

structure Gains where
  proportional : ℝ
  integral : ℝ

def increment (g : Gains) (o : Sample) : ℝ :=
  g.integral * (o.target - o.reading) * o.elapsed

def raw (g : Gains) (i : ℝ) (o : Sample) : ℝ :=
  g.proportional * (o.target - o.reading) + i + increment g o

def clip (u : ℝ) : ℝ := max 0 (min 100 u)

def command (g : Gains) (i : ℝ) (o : Sample) : ℝ := clip (raw g i o)

def retain (g : Gains) (i : ℝ) (o : Sample) : ℝ :=
  if raw g i o < 0 ∨ 100 < raw g i o then i else i + increment g o

structure Record where
  integral : ℝ
  issued : ℝ

def step (g : Gains) (s : Record) (o : Sample) : Record :=
  ⟨retain g s.integral o, command g s.integral o⟩

def history (g : Gains) (s : Record) (os : List Sample) : Record :=
  SystemsOrganization.evolve (step g) s os

theorem measured_history_is_trace (g : Gains) (s : Record) (os : List Sample) :
    Generative.Trace (SystemsOrganization.deterministic (step g)) s os (history g s os) :=
  (SystemsOrganization.deterministic_trace_iff _ _ _ _).mpr rfl

theorem command_bounds (g : Gains) (i : ℝ) (o : Sample) :
    0 ≤ command g i o ∧ command g i o ≤ 100 := by
  exact ⟨le_max_left _ _, max_le (by norm_num) (min_le_left _ _)⟩

theorem saturation_retains_integral (g : Gains) (i : ℝ) (o : Sample)
    (h : raw g i o < 0 ∨ 100 < raw g i o) : retain g i o = i := by
  simp [retain, h]

theorem interior_updates_integral (g : Gains) (i : ℝ) (o : Sample)
    (h : 0 ≤ raw g i o ∧ raw g i o ≤ 100) : retain g i o = i + increment g o := by
  simp [retain, not_lt.mpr h.1, not_lt.mpr h.2]

theorem clip_nonexpansive (u v : ℝ) : |clip u - clip v| ≤ |u-v| := by
  have hmin : |min 100 u - min 100 v| ≤ |u-v| := by
    simpa using abs_min_sub_min_le_max (100:ℝ) u 100 v
  have hmax : |clip u - clip v| ≤ |min 100 u - min 100 v| := by
    simpa [clip, max_comm] using abs_max_sub_max_le_abs (min 100 u) (min 100 v) 0
  exact hmax.trans hmin

/-- The command discrepancy is now derived from measurement and retained-memory
errors. Their actual bounds remain separately warranted inputs. -/
theorem command_error_bound (g : Gains) (i j r y z dt E M : ℝ)
    (measurement : |y-z| ≤ E) (memory : |i-j| ≤ M) :
    |command g i ⟨r,y,dt⟩ - command g j ⟨r,z,dt⟩| ≤
      |g.proportional + g.integral * dt| * E + M := by
  have algebra : raw g i ⟨r,y,dt⟩ - raw g j ⟨r,z,dt⟩ =
      -(g.proportional + g.integral*dt)*(y-z)+(i-j) := by
    simp [raw, increment]
    ring
  calc
    _ ≤ |raw g i ⟨r,y,dt⟩ - raw g j ⟨r,z,dt⟩| := clip_nonexpansive _ _
    _ = |-(g.proportional + g.integral*dt)*(y-z)+(i-j)| := congrArg abs algebra
    _ ≤ |-(g.proportional + g.integral*dt)*(y-z)| + |i-j| := abs_add_le _ _
    _ = |g.proportional + g.integral*dt| * |y-z| + |i-j| := by rw [abs_mul, abs_neg]
    _ ≤ |g.proportional + g.integral*dt| * E+M :=
      add_le_add (mul_le_mul_of_nonneg_left measurement (abs_nonneg _)) memory

/-- Directly discharges the previously supplied action-error term in the earlier
scale theorem, conditional on an explicit response sensitivity B. -/
theorem measured_feedback_one_step {X Y : Type} [PseudoMetricSpace Y]
    (p nextP : X → Y) (F : X → ℝ → X) (G : Y → ℝ → Y)
    (x : X) (y : Y) (g : Gains) (i j r measured represented dt E M L ε B : ℝ)
    (hB : 0 ≤ B)
    (measurement : |measured-represented| ≤ E) (memory : |i-j| ≤ M)
    (defect : dist (nextP (F x (command g i ⟨r,measured,dt⟩)))
      (G (p x) (command g i ⟨r,measured,dt⟩)) ≤ ε)
    (propagation : dist (G (p x) (command g i ⟨r,measured,dt⟩))
      (G y (command g i ⟨r,measured,dt⟩)) ≤ L * dist (p x) y)
    (response : ∀ a b, dist (G y a) (G y b) ≤ B * |a-b|) :
    dist (nextP (F x (command g i ⟨r,measured,dt⟩)))
      (G y (command g j ⟨r,represented,dt⟩)) ≤
      ε + L * dist (p x) y + B * (|g.proportional+g.integral*dt| * E+M) := by
  apply EmbodiedChoiceScales.controlled_one_step p nextP F G x y _ _ L ε _ defect propagation
  exact (response _ _).trans (mul_le_mul_of_nonneg_left
    (command_error_bound g i j r measured represented dt E M measurement memory) hB)

/-- Full finite-horizon composition. This does not turn a measured residual
maximum into any of the casewise hypotheses. -/
theorem measured_feedback_horizon {X Y : Type} [PseudoMetricSpace Y]
    (p : ℕ → X → Y) (F : ℕ → X → ℝ → X) (G : ℕ → Y → ℝ → Y)
    (act : ℕ → X → ℝ) (representedAct : ℕ → Y → ℝ)
    (x : ℕ → X) (y : ℕ → Y) (L ε B C : ℕ → ℝ) (initial : ℝ) (N : ℕ)
    (hx : ∀ t < N, x (t+1) = F t (x t) (act t (x t)))
    (hy : ∀ t < N, y (t+1) = G t (y t) (representedAct t (y t)))
    (h0 : dist (p 0 (x 0)) (y 0) ≤ initial)
    (hL : ∀ t < N, 0 ≤ L t) (hB : ∀ t < N, 0 ≤ B t)
    (hd : ∀ t < N, dist (p (t+1) (F t (x t) (act t (x t))))
      (G t (p t (x t)) (act t (x t))) ≤ ε t)
    (hp : ∀ t < N, dist (G t (p t (x t)) (act t (x t)))
      (G t (y t) (act t (x t))) ≤ L t * dist (p t (x t)) (y t))
    (hc : ∀ t < N, |act t (x t) - representedAct t (y t)| ≤ C t)
    (response : ∀ t < N, ∀ a b, dist (G t (y t) a) (G t (y t) b) ≤ B t * |a-b|) :
    ∀ n ≤ N, dist (p n (x n)) (y n) ≤
      RelationsAcrossScales.budget L (fun t => ε t + B t * C t) initial n := by
  apply EmbodiedChoiceScales.closed_loop_horizon p F G act representedAct x y L ε
    (fun t => B t*C t) initial N hx hy h0 hL hd hp
  intro t ht
  exact (response t ht _ _).trans (mul_le_mul_of_nonneg_left (hc t ht) (hB t ht))

def lastCommand : ℝ → List ℝ → ℝ
  | u, [] => u
  | _, v::rest => lastCommand v rest

def signedMotion : ℝ → List ℝ → ℝ
  | _, [] => 0
  | u, v::rest => v-u + signedMotion v rest

def absoluteMotion : ℝ → List ℝ → ℝ
  | _, [] => 0
  | u, v::rest => |v-u| + absoluteMotion v rest

theorem signed_motion_telescopes (u : ℝ) (us : List ℝ) :
    signedMotion u us = lastCommand u us - u := by
  induction us generalizing u with
  | nil => simp [signedMotion,lastCommand]
  | cons v rest ih => rw [signedMotion,lastCommand,ih]; ring

theorem absolute_motion_bounds_net (u : ℝ) (us : List ℝ) :
    |lastCommand u us-u| ≤ absoluteMotion u us := by
  induction us generalizing u with
  | nil => simp [lastCommand,absoluteMotion]
  | cons v rest ih =>
    calc
      _ = |(v-u)+(lastCommand v rest-v)| := by congr 1; simp only [lastCommand]; ring
      _ ≤ |v-u|+|lastCommand v rest-v| := abs_add_le _ _
      _ ≤ |v-u|+absoluteMotion v rest := add_le_add (le_refl _) (ih v)

/-- Physical actuation bounds do not repair the signed/absolute mismatch. -/
theorem bounded_round_trip_has_hidden_movement :
    signedMotion 0 [100,0] = 0 ∧ absoluteMotion 0 [100,0] = 200 ∧
    (∀ u ∈ ([100,0] : List ℝ), 0 ≤ u ∧ u ≤ 100) := by
  norm_num [signedMotion,absoluteMotion]

/-- Equal tracking loss can hide a changed candidate order under wrong movement
accounting. This is an engineering comparison, not an ethical priority claim. -/
theorem movement_objective_changes_comparison :
    signedMotion 0 [100,0] < signedMotion 0 [1] ∧
    absoluteMotion 0 [1] < absoluteMotion 0 [100,0] := by
  norm_num [signedMotion,absoluteMotion]

/-- No inference from one supplied model predicate to every future error is
encoded here. If candidate models share evidence but disagree at a later query,
that evidence alone does not resolve the query. -/
theorem shared_record_can_leave_prediction_unresolved {H E : Type}
    (record : H → E) (next : H → ℝ) (a b : H)
    (same : record a = record b) (different : next a ≠ next b) :
    ¬ ∃ prediction : E → ℝ, prediction (record a) = next a ∧ prediction (record b) = next b := by
  rintro ⟨f,ha,hb⟩
  apply different
  exact ha.symm.trans ((congrArg f same).trans hb)

end
end MeasuredFeedback
