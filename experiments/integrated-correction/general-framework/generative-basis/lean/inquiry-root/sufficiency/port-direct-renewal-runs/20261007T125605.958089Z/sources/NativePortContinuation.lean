import NativePacketProcess
import ResourceContinuation
import Depletion

/-!
# The native port as an instance of the conditional continuation laws

The port's three quantities are aspects of one continuing activity:

* `held` (存): what remains available to become further activity;
* `enacted` (化): what has already become activity;
* `arrived` (来): what has come in through actual contact.

Nothing appears from nowhere and nothing vanishes. Every native call, completed
or interrupted, keeps `held + enacted` equal to its starting value plus what has
`arrived` (`execute_conserves`). The proof never unfolds the draw schedule or
the arrival amount: a supported stage moves its draw from `held` to `enacted`,
and an arrival adds the same amount to `held` and `arrived`. The conservation
is therefore structural, not a property of these particular numbers.

The general law U1 (`Conditional.SustainLaw`) is the inequality form of this
equality, instantiated with what is held, the change in what is enacted, and
the change in what has arrived (`port_sustain_law`). Every consequence of the
conditional package then applies to the port without a further premise.

Counting the source as still-possible arrival gives the port's whole
`potential`. Every completed call strictly lowers it (`step_lowers_potential`),
so the port alone cannot continue indefinitely
(`port_cannot_continue_indefinitely`). This is a derived regime, not a defect:
continuation beyond that bound needs a contact the port does not represent.
-/

namespace Generative.NativePortContinuation

open Generative.NativePacketProcess

/-- One continuing activity between two configurations: nothing appears from
nowhere and nothing vanishes. `enacted` and `arrived` only accumulate. -/
def Continues (s t : State) : Prop :=
  t.held + t.enacted + s.arrived = s.held + s.enacted + t.arrived ∧
    s.enacted ≤ t.enacted ∧ s.arrived ≤ t.arrived

/-! Constructive arithmetic used below. The library versions of these facts
depend on `propext`; these proofs do not. -/

theorem cancel_right {a b c : Nat} (h : a + c = b + c) : a = b := by
  induction c with
  | zero => exact h
  | succ c ih => exact ih (Nat.succ.inj h)

theorem sub_add_restore (m k : Nat) (bound : k ≤ m) : (m - k) + k = m := by
  induction k generalizing m with
  | zero => rfl
  | succ k ih =>
    cases m with
    | zero => exact False.elim (Nat.not_succ_le_zero _ bound)
    | succ m =>
      rw [Nat.succ_sub_succ]
      exact congrArg Nat.succ (ih m (Nat.le_of_succ_le_succ bound))

theorem add_sub_self_left (a b : Nat) : (a + b) - a = b := by
  induction a with
  | zero => rw [Nat.zero_add]; rfl
  | succ a ih => rw [Nat.succ_add, Nat.succ_sub_succ]; exact ih

/-- Two conserving segments compose: the shared middle cancels. -/
theorem chain {T M S sA mA tA : Nat} (first : M + sA = S + mA)
    (second : T + mA = M + tA) : T + sA = S + tA :=
  cancel_right (c := mA) (calc (T + sA) + mA
      = (T + mA) + sA := Nat.add_right_comm T sA mA
    _ = (M + tA) + sA := by rw [second]
    _ = (M + sA) + tA := Nat.add_right_comm M tA sA
    _ = (S + mA) + tA := by rw [first]
    _ = (S + tA) + mA := Nat.add_right_comm S mA tA)

theorem continues_refl (s : State) : Continues s s :=
  ⟨rfl, Nat.le_refl _, Nat.le_refl _⟩

theorem continues_trans {s m t : State} (first : Continues s m)
    (second : Continues m t) : Continues s t := by
  obtain ⟨balance₁, enacted₁, arrived₁⟩ := first
  obtain ⟨balance₂, enacted₂, arrived₂⟩ := second
  exact ⟨chain balance₁ balance₂, Nat.le_trans enacted₁ enacted₂, Nat.le_trans arrived₁ arrived₂⟩

/-- A supported stage moves its draw from `held` to `enacted`. -/
theorem enact_continues (s : State) (covered : draw s ≤ s.held) :
    Continues s (enact s) := by
  refine ⟨?_, Nat.le_add_right _ _, Nat.le_refl _⟩
  show (s.held - draw s) + (s.enacted + draw s) + s.arrived = s.held + s.enacted + s.arrived
  rw [← Nat.add_assoc, Nat.add_right_comm (s.held - draw s) s.enacted (draw s),
    sub_add_restore s.held (draw s) covered]

/-- An arrival adds the same amount to `held` and `arrived`. -/
theorem convert_continues (s : State) : Continues s (convert s) := by
  refine ⟨?_, Nat.le_refl _, Nat.le_add_right _ _⟩
  show (s.held + arrivalAmount s) + s.enacted + s.arrived =
    s.held + s.enacted + (s.arrived + arrivalAmount s)
  rw [Nat.add_right_comm s.held, Nat.add_assoc (s.held + s.enacted), Nat.add_comm (arrivalAmount s)]

/-- Changing the phase leaves all three aspects unchanged. -/
theorem phase_continues (s : State) (p : Phase) :
    Continues s { s with phase := p } :=
  ⟨rfl, Nat.le_refl _, Nat.le_refl _⟩

theorem supported_continues {s t : State} (sustained : support s = .sustained t) : Continues s t := by
  obtain ⟨⟨_, covered⟩, equality⟩ := (support_sustained_iff s t).mp sustained
  subst equality
  exact enact_continues s covered

/-- Every native call conserves, including calls interrupted after a supported stage or
after a conversion whose receipt could not be acquired. -/
theorem execute_conserves (s : State) (command : Command) :
    Continues s (reached (execute s command)) := by
  unfold execute
  generalize interface : support s = outcome
  cases outcome with
  | capacity => exact continues_refl s
  | insufficient => exact continues_refl s
  | sustained ready =>
    have first := supported_continues interface
    cases command with
    | a => exact continues_trans first (phase_continues ready _)
    | reset => exact continues_trans first (phase_continues ready _)
    | read => exact first
    | probe =>
      change Continues s (reached (finishProbe ready))
      unfold finishProbe
      split
      next =>
        have arrival := continues_trans first (convert_continues ready)
        generalize receipt : support (convert ready) = second
        cases second with
        | capacity => exact arrival
        | insufficient => exact arrival
        | sustained recorded => exact continues_trans arrival (supported_continues receipt)
      next => exact first

theorem step_continues {s t : State} {command : Command}
    (step : process.step s command t) : Continues s t := by
  obtain ⟨observation, completed⟩ := step
  have conserved := execute_conserves s command
  rw [completed] at conserved
  exact conserved

/-- Whole histories conserve through their actual intermediate configurations. -/
theorem trace_continues {s t : State} {commands : List Command}
    (history : Trace process s commands t) : Continues s t := by
  induction history with
  | nil s => exact continues_refl s
  | cons step _ ih => exact continues_trans (step_continues step) ih

/-- What an event makes into activity. -/
def enactedBy (s : State) (_ : Command) (t : State) : Nat := t.enacted - s.enacted

/-- What arrives during an event. -/
def arrivedBy (s : State) (_ : Command) (t : State) : Nat := t.arrived - s.arrived

/-- The exact form of U1: equality, not only the inequality the law class asks. -/
theorem step_sustained_exact {s t : State} {command : Command}
    (step : process.step s command t) :
    t.held + enactedBy s command t = s.held + arrivedBy s command t := by
  obtain ⟨balance, enactedGrew, arrivedGrew⟩ := step_continues step
  unfold enactedBy arrivedBy
  apply cancel_right (c := s.enacted + s.arrived)
  calc t.held + (t.enacted - s.enacted) + (s.enacted + s.arrived)
      = t.held + ((t.enacted - s.enacted) + s.enacted) + s.arrived := by
        rw [Nat.add_assoc, Nat.add_assoc, Nat.add_assoc]
    _ = t.held + t.enacted + s.arrived := by rw [sub_add_restore _ _ enactedGrew]
    _ = s.held + s.enacted + t.arrived := balance
    _ = s.held + s.enacted + ((t.arrived - s.arrived) + s.arrived) := by
        rw [sub_add_restore _ _ arrivedGrew]
    _ = s.held + (t.arrived - s.arrived) + (s.enacted + s.arrived) := by
        rw [Nat.add_assoc, Nat.add_assoc, Nat.add_left_comm s.enacted]

/-- The native port belongs to the conditional law class U1. -/
theorem port_sustain_law :
    Conditional.SustainLaw process State.held enactedBy arrivedBy := by
  intro s command t step
  exact Nat.le_of_eq (step_sustained_exact step)

/-- A completed call is either a supported control command, which only moves the
phase, or a completed probe. -/
theorem completed_shape {s t : State} {command : Command}
    (step : process.step s command t) :
    Supportable s ∧ ((∃ p, t = { enact s with phase := p }) ∨
      (ProbeReady s ∧ t = probeFinal s)) := by
  obtain ⟨observation, completed⟩ := step
  cases command with
  | probe =>
    obtain ⟨ready, final, _⟩ := (probe_complete_iff s t observation).mp completed
    exact ⟨ready.1, Or.inr ⟨ready, final⟩⟩
  | a | reset | read =>
    unfold execute at completed
    generalize interface : support s = outcome at completed
    cases outcome with
    | capacity => cases completed
    | insufficient => cases completed
    | sustained ready =>
      obtain ⟨supportable, equality⟩ := (support_sustained_iff s ready).mp interface
      subst equality
      cases completed
      exact ⟨supportable, Or.inl ⟨_, rfl⟩⟩

theorem draw_positive (s : State) : 1 ≤ draw s := by
  unfold draw
  exact Nat.le_add_right_of_le (by decide)

/-- Every completed call makes something into activity. -/
theorem step_enacts {s t : State} {command : Command}
    (step : process.step s command t) : 1 ≤ enactedBy s command t := by
  have positive := draw_positive s
  obtain ⟨_, shape⟩ := completed_shape step
  unfold enactedBy
  rcases shape with ⟨p, rfl⟩ | ⟨ready, rfl⟩
  · show 1 ≤ (s.enacted + draw s) - s.enacted
    rw [add_sub_self_left]
    exact positive
  · show 1 ≤ ((s.enacted + draw s) + draw (convert (enact s))) - s.enacted
    rw [Nat.add_assoc, add_sub_self_left]
    exact Nat.le_trans positive (Nat.le_add_right _ _)

/-- U2 for the port: on every history, what became activity plus what is still
held never exceeds what was held plus what arrived. -/
theorem port_history_bound {s t : State} {commands : List Command}
    {made gained count : Nat}
    (history : Conditional.SupportTrace process enactedBy arrivedBy s commands t
      made gained count) :
    made + t.held ≤ s.held + gained :=
  Conditional.support_trace_bound State.held port_sustain_law history

/-- An indefinitely continuing port would need arrivals at every later window
no longer than what it holds at that window's start. -/
theorem continuing_port_needs_arrivals (states : Nat → State)
    (commands : Nat → Command)
    (steps : ∀ n, process.step (states n) (commands n) (states (n + 1)))
    (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + (states start).held ∧
      0 < arrivedBy (states n) (commands n) (states (n + 1)) :=
  Conditional.infinite_unit_execution_arrival_window State.held port_sustain_law
    (fun _ _ _ step => step_enacts step) states commands steps start

/-- Arrival per source unit in this port: ten units yield one arrival amount. -/
def yieldPerUnit : Nat := 65536

theorem arrival_amount : 655360 = 10 * yieldPerUnit := rfl

/-- What can still become activity: what is held, and what the source could
still bring if every remaining packet arrived. -/
def potential (s : State) : Nat := s.held + yieldPerUnit * s.source

theorem enact_lowers_potential (s : State) (covered : draw s ≤ s.held) :
    potential (enact s) < potential s := by
  have positive : 0 < draw s := draw_positive s
  show (s.held - draw s) + yieldPerUnit * s.source < s.held + yieldPerUnit * s.source
  exact Nat.add_lt_add_right
    (Nat.sub_lt (Nat.lt_of_lt_of_le positive covered) positive) _

theorem convert_keeps_potential_bound (s : State) (available : 10 ≤ s.source) :
    potential (convert s) ≤ potential s := by
  have bounded : arrivalAmount s ≤ yieldPerUnit * 10 := by
    unfold arrivalAmount
    cases arrival s with
    | true => exact Nat.le_refl _
    | false => exact Nat.zero_le _
  show (s.held + arrivalAmount s) + yieldPerUnit * (s.source - 10) ≤
    s.held + yieldPerUnit * s.source
  calc (s.held + arrivalAmount s) + yieldPerUnit * (s.source - 10)
      ≤ (s.held + yieldPerUnit * 10) + yieldPerUnit * (s.source - 10) :=
        Nat.add_le_add_right (Nat.add_le_add_left bounded _) _
    _ = s.held + yieldPerUnit * ((s.source - 10) + 10) := by
        rw [Nat.add_assoc, Nat.add_comm (yieldPerUnit * 10), ← Nat.mul_add]
    _ = s.held + yieldPerUnit * s.source := by rw [sub_add_restore _ _ available]

theorem phase_keeps_potential (s : State) (p : Phase) :
    potential { s with phase := p } = potential s := rfl

/-- Every completed call strictly lowers the port's potential. -/
theorem step_lowers_potential {s t : State} {command : Command}
    (step : process.step s command t) : potential t < potential s := by
  obtain ⟨⟨_, covered⟩, shape⟩ := completed_shape step
  have first := enact_lowers_potential s covered
  rcases shape with ⟨p, rfl⟩ | ⟨ready, rfl⟩
  · exact first
  · have middle := convert_keeps_potential_bound (enact s) ready.2.1
    have last := enact_lowers_potential (convert (enact s)) ready.2.2.2
    unfold probeFinal
    exact Nat.lt_trans last (Nat.lt_of_le_of_lt middle first)

/-- Every history of the port is no longer than its starting potential. -/
theorem port_history_length {s t : State} {commands : List Command}
    (history : Trace process s commands t) : commands.length ≤ potential s :=
  trace_length_bound potential (fun _ _ _ step => step_lowers_potential step) history

/-- With only its own source, the port cannot continue indefinitely. -/
theorem port_cannot_continue_indefinitely :
    ¬ ∃ states : Nat → State, ∃ commands : Nat → Command,
      ∀ n, process.step (states n) (commands n) (states (n + 1)) :=
  no_infinite_execution_under_depletion potential
    (fun _ _ _ step => step_lowers_potential step)

#print axioms cancel_right
#print axioms sub_add_restore
#print axioms add_sub_self_left
#print axioms chain
#print axioms continues_refl
#print axioms continues_trans
#print axioms enact_continues
#print axioms convert_continues
#print axioms phase_continues
#print axioms supported_continues
#print axioms execute_conserves
#print axioms step_continues
#print axioms trace_continues
#print axioms step_sustained_exact
#print axioms port_sustain_law
#print axioms completed_shape
#print axioms draw_positive
#print axioms step_enacts
#print axioms port_history_bound
#print axioms continuing_port_needs_arrivals
#print axioms arrival_amount
#print axioms enact_lowers_potential
#print axioms convert_keeps_potential_bound
#print axioms phase_keeps_potential
#print axioms step_lowers_potential
#print axioms port_history_length
#print axioms port_cannot_continue_indefinitely

end Generative.NativePortContinuation
