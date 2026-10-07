import NativePacketProcess
import ResourceContinuation
import Depletion

/-!
# The native port as an instance of the conditional continuation laws

The port's bookkeeping coordinates were named `fuel`, `spent` and `income` in
the Python source. Those names carry an exchange picture: an owner holding a
balance, paying out and earning. Nothing in the port's activity requires that
picture. Read through what the coordinates do, they are three aspects of one
continuing activity:

* `held` (存): what remains available to become further activity;
* `enacted` (化): what has already become activity;
* `arrived` (来): what has come in through actual contact.

No coordinate leaves the account. Every native call, completed or interrupted,
keeps `held + enacted` equal to its starting value plus what has `arrived`
(`execute_conserves`). This is the port's own structure. It does not depend on
the tariff numerals, which enter the proofs only as opaque amounts that one
stage moves from `held` to `enacted`, or that one arrival adds to `held` and
`arrived`.

The general law U1 (`Conditional.AccountLaw`) is the inequality shadow of this
equality. Its `reserve`, `demand` and `credit` are instantiated here as `held`,
the change in `enacted`, and the change in `arrived` (`port_account_law`).
Every result of the conditional package then applies to the port without a
further premise.

Counting the source as still-possible arrival gives the port's whole
`potential`. Every completed call strictly lowers it (`step_lowers_potential`),
so the port alone cannot continue indefinitely (`port_cannot_continue_indefinitely`).
This is a derived regime, not a defect: continuation beyond that bound needs a
contact the port does not represent. Nothing here renames the inherited fields
or changes the native executor.
-/

namespace Generative.NativePortContinuation

open Generative.NativePacketProcess

/-- What remains available to become further activity. -/
def held (s : State) : Nat := s.fuel

/-- What has already become activity. -/
def enacted (s : State) : Nat := s.spent

/-- What has come in through actual contact. -/
def arrived (s : State) : Nat := s.income

/-- One continuing activity between two configurations: nothing appears from
nowhere and nothing vanishes. `enacted` and `arrived` only accumulate. -/
def Continues (s t : State) : Prop :=
  held t + enacted t + arrived s = held s + enacted s + arrived t ∧
    enacted s ≤ enacted t ∧ arrived s ≤ arrived t

theorem continues_refl (s : State) : Continues s s :=
  ⟨rfl, Nat.le_refl _, Nat.le_refl _⟩

theorem continues_trans {s m t : State} (first : Continues s m)
    (second : Continues m t) : Continues s t := by
  obtain ⟨balance₁, enacted₁, arrived₁⟩ := first
  obtain ⟨balance₂, enacted₂, arrived₂⟩ := second
  refine ⟨?_, Nat.le_trans enacted₁ enacted₂, Nat.le_trans arrived₁ arrived₂⟩
  omega

/-- A charged stage moves its amount from `held` to `enacted`. -/
theorem debit_continues (s : State) (funded : bill s ≤ s.fuel) :
    Continues s (debit s) := by
  refine ⟨?_, Nat.le_add_right _ _, Nat.le_refl _⟩
  unfold held enacted arrived debit
  dsimp only
  omega

/-- An arrival adds the same amount to `held` and `arrived`. -/
theorem convert_continues (s : State) : Continues s (convert s) := by
  refine ⟨?_, Nat.le_refl _, Nat.le_add_right _ _⟩
  unfold held enacted arrived convert
  dsimp only
  omega

/-- Changing the phase leaves all three aspects unchanged. -/
theorem phase_continues (s : State) (p : Phase) :
    Continues s { s with phase := p } :=
  ⟨rfl, Nat.le_refl _, Nat.le_refl _⟩

theorem paid_continues {s t : State} (paid : charge s = .paid t) : Continues s t := by
  obtain ⟨⟨_, funded⟩, equality⟩ := (charge_paid_iff s t).mp paid
  subst equality
  exact debit_continues s funded

/-- Every native call conserves, including calls interrupted after a charge or
after a conversion whose receipt could not be acquired. -/
theorem execute_conserves (s : State) (command : Command) :
    Continues s (reached (execute s command)) := by
  unfold execute
  generalize interface : charge s = payment
  cases payment with
  | capacity => exact continues_refl s
  | funding => exact continues_refl s
  | paid ready =>
    have first := paid_continues interface
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
        generalize receipt : charge (convert ready) = second
        cases second with
        | capacity => exact arrival
        | funding => exact arrival
        | paid recorded => exact continues_trans arrival (paid_continues receipt)
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
def enactedBy (s : State) (_ : Command) (t : State) : Nat := enacted t - enacted s

/-- What arrives during an event. -/
def arrivedBy (s : State) (_ : Command) (t : State) : Nat := arrived t - arrived s

/-- The exact form of U1: equality, not only the inequality the law class asks. -/
theorem step_balance_exact {s t : State} {command : Command}
    (step : process.step s command t) :
    held t + enactedBy s command t = held s + arrivedBy s command t := by
  have c := step_continues step
  unfold Continues at c
  unfold enactedBy arrivedBy
  omega

/-- The native port belongs to the conditional law class U1. -/
theorem port_account_law :
    Conditional.AccountLaw process held enactedBy arrivedBy := by
  intro s command t step
  exact Nat.le_of_eq (step_balance_exact step)

/-- A completed call is either a paid control command, which only moves the
phase, or a completed probe. -/
theorem completed_shape {s t : State} {command : Command}
    (step : process.step s command t) :
    Payable s ∧ ((∃ p, t = { debit s with phase := p }) ∨
      (ProbeReady s ∧ t = probeFinal s)) := by
  obtain ⟨observation, completed⟩ := step
  cases command with
  | probe =>
    obtain ⟨ready, final, _⟩ := (probe_complete_iff s t observation).mp completed
    exact ⟨ready.1, Or.inr ⟨ready, final⟩⟩
  | a | reset | read =>
    unfold execute at completed
    generalize interface : charge s = payment at completed
    cases payment with
    | capacity => cases completed
    | funding => cases completed
    | paid ready =>
      obtain ⟨payable, equality⟩ := (charge_paid_iff s ready).mp interface
      subst equality
      cases completed
      exact ⟨payable, Or.inl ⟨_, rfl⟩⟩

theorem bill_positive (s : State) : 1 ≤ bill s := by
  unfold bill
  exact Nat.le_add_right_of_le (by decide)

/-- Every completed call makes something into activity. -/
theorem step_enacts {s t : State} {command : Command}
    (step : process.step s command t) : 1 ≤ enactedBy s command t := by
  have charged := bill_positive s
  obtain ⟨_, shape⟩ := completed_shape step
  unfold enactedBy
  rcases shape with ⟨p, rfl⟩ | ⟨ready, rfl⟩
  · have first : enacted { debit s with phase := p } = enacted s + bill s := rfl
    omega
  · have first : enacted (debit s) = enacted s + bill s := rfl
    have middle := (convert_continues (debit s)).2.1
    have last := (debit_continues (convert (debit s)) ready.2.2.2).2.1
    change 1 ≤ enacted (debit (convert (debit s))) - enacted s
    omega

/-- U2 for the port: on every history, what became activity plus what is still
held never exceeds what was held plus what arrived. -/
theorem port_history_bound {s t : State} {commands : List Command}
    {made gained count : Nat}
    (history : Conditional.SupportTrace process enactedBy arrivedBy s commands t
      made gained count) :
    made + held t ≤ held s + gained :=
  Conditional.support_trace_balance held port_account_law history

/-- An indefinitely continuing port would need arrivals at every later window
no longer than what it holds at that window's start. -/
theorem continuing_port_needs_arrivals (states : Nat → State)
    (commands : Nat → Command)
    (steps : ∀ n, process.step (states n) (commands n) (states (n + 1)))
    (start : Nat) :
    ∃ n, start ≤ n ∧ n ≤ start + held (states start) ∧
      0 < arrivedBy (states n) (commands n) (states (n + 1)) :=
  Conditional.infinite_unit_execution_credit_window held port_account_law
    (fun _ _ _ step => step_enacts step) states commands steps start

/-- Arrival per source unit in this port: ten units yield one arrival amount. -/
def yieldPerUnit : Nat := 65536

theorem arrival_amount : 655360 = 10 * yieldPerUnit := rfl

/-- What can still become activity: what is held, and what the source could
still bring if every remaining packet arrived. -/
def potential (s : State) : Nat := held s + yieldPerUnit * s.source

theorem debit_lowers_potential (s : State) (funded : bill s ≤ s.fuel) :
    potential (debit s) < potential s := by
  have charged : 1 ≤ bill s := by unfold bill; omega
  unfold potential held debit
  dsimp only
  omega

theorem convert_keeps_potential_bound (s : State) (available : 10 ≤ s.source) :
    potential (convert s) ≤ potential s := by
  unfold potential held convert gain yieldPerUnit
  dsimp only
  split <;> omega

theorem phase_keeps_potential (s : State) (p : Phase) :
    potential { s with phase := p } = potential s := rfl

/-- Every completed call strictly lowers the port's potential. -/
theorem step_lowers_potential {s t : State} {command : Command}
    (step : process.step s command t) : potential t < potential s := by
  obtain ⟨⟨_, funded⟩, shape⟩ := completed_shape step
  have first := debit_lowers_potential s funded
  rcases shape with ⟨p, rfl⟩ | ⟨ready, rfl⟩
  · exact first
  · have middle := convert_keeps_potential_bound (debit s) ready.2.1
    have last := debit_lowers_potential (convert (debit s)) ready.2.2.2
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

#print axioms continues_refl
#print axioms continues_trans
#print axioms debit_continues
#print axioms convert_continues
#print axioms phase_continues
#print axioms paid_continues
#print axioms execute_conserves
#print axioms step_continues
#print axioms trace_continues
#print axioms step_balance_exact
#print axioms port_account_law
#print axioms completed_shape
#print axioms bill_positive
#print axioms step_enacts
#print axioms port_history_bound
#print axioms continuing_port_needs_arrivals
#print axioms arrival_amount
#print axioms debit_lowers_potential
#print axioms convert_keeps_potential_bound
#print axioms phase_keeps_potential
#print axioms step_lowers_potential
#print axioms port_history_length
#print axioms port_cannot_continue_indefinitely

end Generative.NativePortContinuation
