import VaryingFeedback
import ResourceContinuation

/-!
# Acquired delayed-feedback gain revision with actual finite support

This is a newly supplied local realization, not a handoff from an existing
concern learner. Operate, acquire and update each cost one fuel unit. Operation
transfers one original three-unit source packet to fuel; it creates no energy.
The read acquires whether the old and new first coordinates have opposite signs.
That observation selects gain 1/4 after overshoot and 3/4 otherwise. The installed
readout, gain menu, update rule, return channel and event schedule are premises.

Total algebraic cycle functions are used to state the mathematics. Their values
are certified as executable only through the separately proved funding bounds.
An infinite safe mathematical schedule is not an infinite funded execution.
-/

namespace SystemsComplexity.SupportedRevision

noncomputable section

open Generative Generative.Conditional

inductive Phase where
  | ready | acquiring | updating
  deriving DecidableEq, Repr

inductive Event where
  | operate | acquire | update
  deriving DecidableEq, Repr

inductive Channel where
  | faithful | clamped
  deriving DecidableEq, Repr

structure State where
  plant : ℝ × ℝ
  prior : ℝ
  high : Bool
  observation : Option Bool
  phase : Phase
  fuel : ℕ
  packets : ℕ

def gain (high : Bool) : ℝ := if high then 3 / 4 else 1 / 4

def operated (s : State) : State :=
  { s with plant := RealFeedback.delayedStep (gain s.high) s.plant,
           prior := s.plant.1, observation := none, phase := .acquiring,
           fuel := s.fuel - 1 + 3, packets := s.packets - 1 }

def report (channel : Channel) (s : State) : Bool :=
  match channel with
  | .faithful => decide (s.prior * s.plant.1 < 0)
  | .clamped => false

def acquired (channel : Channel) (s : State) : State :=
  { s with observation := some (report channel s), phase := .updating,
           fuel := s.fuel - 1 }

def updated (s : State) (observation : Bool) : State :=
  { s with high := !observation, phase := .ready, fuel := s.fuel - 1 }

def process (channel : Channel) : Process State Event where
  step s a t := match a with
    | .operate => s.phase = .ready ∧ 0 < s.fuel ∧ 0 < s.packets ∧ t = operated s
    | .acquire => s.phase = .acquiring ∧ 0 < s.fuel ∧ t = acquired channel s
    | .update => s.phase = .updating ∧ 0 < s.fuel ∧
        ∃ bit, s.observation = some bit ∧ t = updated s bit

def cycle (channel : Channel) (s : State) : State :=
  updated (acquired channel (operated s)) (report channel (operated s))

def cycles (channel : Channel) (s : State) : ℕ → State
  | 0 => s
  | n + 1 => cycle channel (cycles channel s n)

def cycleWord : ℕ → List Event
  | 0 => []
  | n + 1 => cycleWord n ++ [.operate, .acquire, .update]

def demand (_ : State) (_ : Event) (_ : State) : ℕ := 1

def credit (_ : State) (a : Event) (_ : State) : ℕ :=
  match a with
  | .operate => 3
  | _ => 0

def totalSupport (s : State) : ℕ := s.fuel + 3 * s.packets

theorem gain_margin (b : Bool) : (1 : ℝ) / 4 ≤ gain b ∧ gain b ≤ 1 - 1 / 4 := by
  cases b <;> norm_num [gain]

theorem cycle_plant (channel : Channel) (s : State) :
    (cycle channel s).plant = RealFeedback.delayedStep (gain s.high) s.plant := by
  rfl

theorem cycle_phase (channel : Channel) (s : State) :
    (cycle channel s).phase = .ready := by
  rfl

theorem cycle_fuel (channel : Channel) (s : State) (hf : 0 < s.fuel) :
    (cycle channel s).fuel = s.fuel := by
  change s.fuel - 1 + 3 - 1 - 1 = s.fuel
  omega

theorem cycle_packets (channel : Channel) (s : State) :
    (cycle channel s).packets = s.packets - 1 := by
  rfl

/-- The observation changes the retained selector used by the NEXT operation. -/
theorem acquired_observation_controls_next_gain (channel : Channel) (s : State) :
    (cycle channel s).high = !(report channel (operated s)) ∧
    (cycle channel s).observation = some (report channel (operated s)) := by
  exact ⟨rfl, rfl⟩

theorem fuel_account (channel : Channel) :
    AccountLaw (process channel) State.fuel demand credit := by
  intro s a t hs
  cases a with
  | operate =>
      obtain ⟨_, hf, _, rfl⟩ := hs
      change s.fuel - 1 + 3 + 1 ≤ s.fuel + 3
      omega
  | acquire =>
      obtain ⟨_, hf, rfl⟩ := hs
      change s.fuel - 1 + 1 ≤ s.fuel + 0
      omega
  | update =>
      obtain ⟨_, hf, bit, _, rfl⟩ := hs
      change s.fuel - 1 + 1 ≤ s.fuel + 0
      omega

/-- The received fuel is subtracted from the original packet inventory. -/
theorem exact_total_support_step (channel : Channel) {s t : State} {a : Event}
    (hs : (process channel).step s a t) : totalSupport t + 1 = totalSupport s := by
  cases a with
  | operate =>
      obtain ⟨_, hf, hp, rfl⟩ := hs
      change (s.fuel - 1 + 3) + 3 * (s.packets - 1) + 1 = s.fuel + 3 * s.packets
      omega
  | acquire =>
      obtain ⟨_, hf, rfl⟩ := hs
      change s.fuel - 1 + 3 * s.packets + 1 = s.fuel + 3 * s.packets
      omega
  | update =>
      obtain ⟨_, hf, bit, _, rfl⟩ := hs
      change s.fuel - 1 + 3 * s.packets + 1 = s.fuel + 3 * s.packets
      omega

theorem total_support_account (channel : Channel) :
    AccountLaw (process channel) totalSupport demand (fun _ _ _ => 0) := by
  intro s a t hs
  have h := exact_total_support_step channel hs
  change totalSupport t + 1 ≤ totalSupport s + 0
  omega

theorem cycle_support_trace (channel : Channel) (s : State)
    (hr : s.phase = .ready) (hf : 0 < s.fuel) (hp : 0 < s.packets) :
    SupportTrace (process channel) demand credit s [.operate, .acquire, .update]
      (cycle channel s) 3 3 1 := by
  have ho : (process channel).step s .operate (operated s) := ⟨hr, hf, hp, rfl⟩
  have ha : (process channel).step (operated s) .acquire (acquired channel (operated s)) := by
    refine ⟨rfl, ?_, rfl⟩
    change 0 < s.fuel - 1 + 3
    omega
  have hu : (process channel).step (acquired channel (operated s)) .update (cycle channel s) := by
    refine ⟨rfl, ?_, report channel (operated s), rfl, rfl⟩
    change 0 < s.fuel - 1 + 3 - 1
    omega
  exact .cons ho (.cons ha (.cons hu (.nil _)))

theorem cycles_phase (channel : Channel) (s : State) (hr : s.phase = .ready) (n : ℕ) :
    (cycles channel s n).phase = .ready := by
  cases n with
  | zero => exact hr
  | succ n => exact cycle_phase channel _

theorem cycles_fuel (channel : Channel) (s : State) (hf : 0 < s.fuel) (n : ℕ) :
    (cycles channel s n).fuel = s.fuel := by
  induction n with
  | zero => rfl
  | succ n ih =>
      exact (cycle_fuel channel _ (by rw [ih]; exact hf)).trans ih

theorem cycles_packets (channel : Channel) (s : State) (n : ℕ) :
    (cycles channel s n).packets = s.packets - n := by
  induction n with
  | zero => simp [cycles]
  | succ n ih =>
      rw [cycles, cycle_packets, ih]
      omega

/-- These are actual paid histories for every funded prefix, with the original
source retained. The theorem does not execute the total cycle function after funding fails. -/
theorem funded_cycles (channel : Channel) (s : State)
    (hr : s.phase = .ready) (hf : 0 < s.fuel) (n : ℕ) (hn : n ≤ s.packets) :
    SupportTrace (process channel) demand credit s (cycleWord n) (cycles channel s n)
      (3 * n) (3 * n) n := by
  induction n with
  | zero => exact .nil s
  | succ n ih =>
      have priorTrace := ih (by omega)
      have hp : 0 < (cycles channel s n).packets := by
        rw [cycles_packets]
        omega
      have followingTrace := cycle_support_trace channel (cycles channel s n)
        (cycles_phase channel s hr n) (by rw [cycles_fuel channel s hf n]; exact hf) hp
      have joined := support_trace_append priorTrace followingTrace
      simpa [cycleWord, cycles, Nat.mul_add] using joined

theorem funded_cycles_generative_trace (channel : Channel) (s : State)
    (hr : s.phase = .ready) (hf : 0 < s.fuel) (n : ℕ) (hn : n ≤ s.packets) :
    Trace (process channel) s (cycleWord n) (cycles channel s n) := by
  exact support_trace_is_trace (funded_cycles channel s hr hf n hn)

theorem funded_cycles_exact_balance (channel : Channel) (s : State)
    (hf : 0 < s.fuel) (n : ℕ) (hn : n ≤ s.packets) :
    3 * n + totalSupport (cycles channel s n) = totalSupport s := by
  unfold totalSupport
  rw [cycles_fuel channel s hf n, cycles_packets]
  omega

def selectedGain (channel : Channel) (s : State) (n : ℕ) : ℝ :=
  gain (cycles channel s n).high

theorem selected_gain_margin (channel : Channel) (s : State) (n : ℕ) :
    (1 : ℝ) / 4 ≤ selectedGain channel s n ∧ selectedGain channel s n ≤ 1 - 1 / 4 := by
  exact gain_margin _

/-- Equality is mathematical for the total recurrences. Physical execution is
claimed only together with funded_cycles_generative_trace. -/
theorem cycle_trajectory (channel : Channel) (s : State) (n : ℕ) :
    (cycles channel s n).plant = AdaptiveCore.trajectory (selectedGain channel s) s.plant n := by
  induction n with
  | zero => rfl
  | succ n ih =>
      change RealFeedback.delayedStep (selectedGain channel s n) (cycles channel s n).plant =
        RealFeedback.delayedStep (selectedGain channel s n)
          (AdaptiveCore.trajectory (selectedGain channel s) s.plant n)
      exact congrArg (RealFeedback.delayedStep (selectedGain channel s n)) ih

theorem funded_regulation_bound (channel : Channel) (s : State)
    (hr : s.phase = .ready) (hf : 0 < s.fuel) (n : ℕ) (hn : n ≤ s.packets) :
    Trace (process channel) s (cycleWord n) (cycles channel s n) ∧
    AdaptiveCore.envelope (cycles channel s n).plant ≤
      ((3 : ℝ) / 4) ^ (n / 3) * AdaptiveCore.envelope s.plant := by
  refine ⟨funded_cycles_generative_trace channel s hr hf n hn, ?_⟩
  rw [cycle_trajectory]
  have h := VaryingFeedback.trajectory_geometric_bound_prefix (selectedGain channel s) s.plant
    (δ := (1 : ℝ) / 4) (by norm_num) (by norm_num) n
    (fun i _ => selected_gain_margin channel s i)
  norm_num at h ⊢
  exact h

theorem depleted_packets_block_operation (channel : Channel) (s : State)
    (hp : s.packets = 0) : ¬ Enabled (process channel) s .operate := by
  rintro ⟨t, _, _, positive, _⟩
  omega

theorem original_packets_exhaust (channel : Channel) (s : State) :
    ¬ Enabled (process channel) (cycles channel s s.packets) .operate := by
  apply depleted_packets_block_operation
  rw [cycles_packets]
  omega

theorem any_history_length_bound (channel : Channel) {s t : State} {word : List Event}
    (h : Trace (process channel) s word t) : word.length + totalSupport t ≤ totalSupport s := by
  obtain ⟨spent, received, count, accounted⟩ :=
    trace_has_support_account demand (fun _ _ _ => 0) h
  have bound := support_trace_length_bound totalSupport (total_support_account channel)
    (fun _ _ _ _ => Nat.le_refl 1) 0 (by intro _ _ _ _; exact Nat.le_refl 0) accounted
  simpa using bound

theorem no_infinite_execution (channel : Channel) (states : ℕ → State)
    (actions : ℕ → Event) :
    ¬ (∀ n, (process channel).step (states n) (actions n) (states (n + 1))) := by
  intro steps
  have h := infinite_unit_execution_unbounded_credit totalSupport (total_support_account channel)
    (fun _ _ _ _ => Nat.le_refl 1) states actions steps 0
  obtain ⟨length, positive⟩ := h
  have zero : intervalTotal (fun _ => 0) 0 length = 0 := by
    clear positive
    induction length with
    | zero => rfl
    | succ n ih => simpa [intervalTotal] using ih
  change 0 < intervalTotal (fun _ => 0) 0 length at positive
  rw [zero] at positive
  omega

def initial (packets : ℕ) : State :=
  ⟨(1, 1), 1, true, none, .ready, 1, packets⟩

/-- Two paid observations establish a changed gain; the third operation uses it. -/
theorem actual_revision_witness :
    (cycles .faithful (initial 3) 1).plant = ((1 : ℝ) / 4, 1) ∧
    (cycles .faithful (initial 3) 2).plant = (-(1 : ℝ) / 2, 1 / 4) ∧
    (cycles .faithful (initial 3) 2).observation = some true ∧
    (cycles .faithful (initial 3) 2).high = false ∧
    (cycles .faithful (initial 3) 3).plant = (-(9 : ℝ) / 16, -(1 : ℝ) / 2) ∧
    (cycles .faithful (initial 3) 3).high = true := by
  norm_num [cycles, cycle, acquired, operated, updated, report, initial,
    RealFeedback.delayedStep, gain]

/-- The clamped reader has the same timing and bills. Its different acquired
bit changes the retained gain and the next actual plant transition. -/
theorem clamped_reader_changes_later_operation :
    (cycles .clamped (initial 3) 2).plant = (cycles .faithful (initial 3) 2).plant ∧
    (cycles .clamped (initial 3) 2).high = true ∧
    (cycles .clamped (initial 3) 2).observation = some false ∧
    (cycles .clamped (initial 3) 3).plant = (-(11 : ℝ) / 16, -(1 : ℝ) / 2) ∧
    (cycles .clamped (initial 3) 3).plant ≠ (cycles .faithful (initial 3) 3).plant := by
  norm_num [cycles, cycle, acquired, operated, updated, report, initial,
    RealFeedback.delayedStep, gain]

theorem matched_reader_support (n packets : ℕ) :
    (cycles .faithful (initial packets) n).fuel = (cycles .clamped (initial packets) n).fuel ∧
    (cycles .faithful (initial packets) n).packets = (cycles .clamped (initial packets) n).packets := by
  constructor
  · rw [cycles_fuel _ _ (by exact Nat.zero_lt_one), cycles_fuel _ _ (by exact Nat.zero_lt_one)]
  · rw [cycles_packets, cycles_packets]

end
end SystemsComplexity.SupportedRevision

#print axioms SystemsComplexity.SupportedRevision.gain_margin
#print axioms SystemsComplexity.SupportedRevision.cycle_plant
#print axioms SystemsComplexity.SupportedRevision.cycle_phase
#print axioms SystemsComplexity.SupportedRevision.cycle_fuel
#print axioms SystemsComplexity.SupportedRevision.cycle_packets
#print axioms SystemsComplexity.SupportedRevision.acquired_observation_controls_next_gain
#print axioms SystemsComplexity.SupportedRevision.fuel_account
#print axioms SystemsComplexity.SupportedRevision.exact_total_support_step
#print axioms SystemsComplexity.SupportedRevision.total_support_account
#print axioms SystemsComplexity.SupportedRevision.cycle_support_trace
#print axioms SystemsComplexity.SupportedRevision.cycles_phase
#print axioms SystemsComplexity.SupportedRevision.cycles_fuel
#print axioms SystemsComplexity.SupportedRevision.cycles_packets
#print axioms SystemsComplexity.SupportedRevision.funded_cycles
#print axioms SystemsComplexity.SupportedRevision.funded_cycles_generative_trace
#print axioms SystemsComplexity.SupportedRevision.funded_cycles_exact_balance
#print axioms SystemsComplexity.SupportedRevision.selected_gain_margin
#print axioms SystemsComplexity.SupportedRevision.cycle_trajectory
#print axioms SystemsComplexity.SupportedRevision.funded_regulation_bound
#print axioms SystemsComplexity.SupportedRevision.depleted_packets_block_operation
#print axioms SystemsComplexity.SupportedRevision.original_packets_exhaust
#print axioms SystemsComplexity.SupportedRevision.any_history_length_bound
#print axioms SystemsComplexity.SupportedRevision.no_infinite_execution
#print axioms SystemsComplexity.SupportedRevision.actual_revision_witness
#print axioms SystemsComplexity.SupportedRevision.clamped_reader_changes_later_operation
#print axioms SystemsComplexity.SupportedRevision.matched_reader_support
