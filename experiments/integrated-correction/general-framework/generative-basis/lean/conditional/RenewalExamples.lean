import ResourceContinuation

/-!
# Realizations and boundary cases for conditional support necessity

These models witness compatibility and rule out stronger conclusions. They
do not identify which sustaining law any physical or social system satisfies.
-/

namespace Generative.Conditional.Examples

inductive Phase where
  | ready | depleted | terminal
  deriving DecidableEq

inductive Event where
  | use | restore | abandon
  deriving DecidableEq

inductive RenewalStep : Phase → Event → Phase → Prop where
  | use : RenewalStep .ready .use .depleted
  | restore : RenewalStep .depleted .restore .ready
  | abandon : RenewalStep .ready .abandon .terminal

/-- One law admits a supported cycle and terminal loss from the same start. -/
def renewalProcess : Process Phase Event := ⟨RenewalStep⟩

def held : Phase → Nat
  | .ready => 1
  | .depleted | .terminal => 0

def enacted (_ : Phase) (_ : Event) (_ : Phase) : Nat := 1

/-- Restoration brings two units, one of which the restoring event itself enacts.
    This is declared provision, not creation of support from nothing. -/
def arrived (_ : Phase) : Event → Phase → Nat
  | .restore, _ => 2
  | .use, _ | .abandon, _ => 0

theorem renewal_sustain_law : SustainLaw renewalProcess held enacted arrived := by
  intro s a t h
  cases h <;> decide

theorem renewal_unit_enactment : ∀ s a t, renewalProcess.step s a t → 1 ≤ enacted s a t := by
  intro s a t _
  exact Nat.le_refl 1

theorem renewal_arrival_cap : ∀ s a t, renewalProcess.step s a t → arrived s a t ≤ 2 := by
  intro s a t h
  cases h <;> decide

theorem renewal_cycle :
    SupportTrace renewalProcess enacted arrived .ready [.use, .restore] .ready 2 2 1 := by
  exact .cons RenewalStep.use (.cons RenewalStep.restore (.nil Phase.ready))

theorem terminal_branch : Trace renewalProcess .ready [.abandon] .terminal := by
  exact .cons RenewalStep.abandon (.nil Phase.terminal)

theorem terminal_has_no_continuation (a : Event) : ¬ Enabled renewalProcess .terminal a := by
  rintro ⟨t, h⟩
  cases h

def cycleStates (n : Nat) : Phase := if n % 2 = 0 then .ready else .depleted
def cycleActions (n : Nat) : Event := if n % 2 = 0 then .use else .restore

theorem cycle_is_lawful (n : Nat) :
    renewalProcess.step (cycleStates n) (cycleActions n) (cycleStates (n + 1)) := by
  by_cases even : n % 2 = 0
  · have odd : ¬ (n + 1) % 2 = 0 := by omega
    simpa [renewalProcess, cycleStates, cycleActions, even, odd] using RenewalStep.use
  · have next : (n + 1) % 2 = 0 := by omega
    simpa [renewalProcess, cycleStates, cycleActions, even, next] using RenewalStep.restore

theorem renewal_admits_infinite_execution :
    ∃ states : Nat → Phase, ∃ actions : Nat → Event,
      ∀ n, renewalProcess.step (states n) (actions n) (states (n + 1)) := by
  exact ⟨cycleStates, cycleActions, cycle_is_lawful⟩

theorem same_law_admits_continuation_and_loss :
    (∃ states : Nat → Phase, ∃ actions : Nat → Event,
      states 0 = .ready ∧
      ∀ n, renewalProcess.step (states n) (actions n) (states (n + 1))) ∧
      Trace renewalProcess .ready [.abandon] .terminal ∧
      (∀ a, ¬ Enabled renewalProcess .terminal a) := by
  exact ⟨⟨cycleStates, cycleActions, rfl, cycle_is_lawful⟩,
    terminal_branch, terminal_has_no_continuation⟩

/-- Arrival on every event is insufficient when every event enacts more. -/
def insufficientProcess : Process Nat Unit where
  step s _ t := t + 1 = s

def insufficientEnacted (_ : Nat) (_ : Unit) (_ : Nat) : Nat := 2
def insufficientArrived (_ : Nat) (_ : Unit) (_ : Nat) : Nat := 1

theorem insufficient_sustain_law :
    SustainLaw insufficientProcess id insufficientEnacted insufficientArrived := by
  intro s a t h
  change t + 1 = s at h
  simp only [id_eq, insufficientEnacted, insufficientArrived]
  omega

theorem insufficient_arrival_is_always_positive :
    ∀ s a t, insufficientProcess.step s a t → 0 < insufficientArrived s a t := by
  intro s a t _
  exact Nat.zero_lt_succ 0

theorem insufficient_finite_bound {s t : Nat} {events : List Unit}
    (h : Trace insufficientProcess s events t) : events.length + t ≤ s := by
  induction h with
  | nil s => simp
  | cons hs _ ih =>
    change _ + 1 = _ at hs
    simp only [List.length_cons]
    omega

theorem insufficient_has_no_infinite_execution :
    ¬ ∃ states : Nat → Nat, ∃ actions : Nat → Unit,
      ∀ n, insufficientProcess.step (states n) (actions n) (states (n + 1)) := by
  rintro ⟨states, actions, steps⟩
  have bound : ∀ n, n + states n ≤ states 0 := by
    intro n
    induction n with
    | zero => omega
    | succ n ih =>
      have h := steps n
      change states (n + 1) + 1 = states n at h
      omega
  have impossible := bound (states 0 + 1)
  omega

/-- Recurrence that enacts nothing falls within the general law but outside the
    positive-enactment corollaries. Nothing needs to arrive for these events. -/
def freeProcess : Process Unit Unit where
  step _ _ _ := True

theorem free_sustain_law :
    SustainLaw freeProcess (fun _ => 0) (fun _ _ _ => 0) (fun _ _ _ => 0) := by
  intro s a t _
  exact Nat.le_refl 0

theorem free_infinite_execution :
    ∃ states : Nat → Unit, ∃ actions : Nat → Unit,
      ∀ n, freeProcess.step (states n) (actions n) (states (n + 1)) := by
  exact ⟨fun _ => (), fun _ => (), fun _ => True.intro⟩

theorem free_process_has_no_unit_enactment :
    ¬ (∀ s a t, freeProcess.step s a t → 1 ≤ (fun _ _ _ => 0 : Unit → Unit → Unit → Nat) s a t) := by
  intro h
  have impossible := h () () () True.intro
  exact Nat.not_succ_le_zero 0 impossible

/-- One arbitrarily large delivery can support an arbitrarily long finite run;
    a uniform event-frequency bound needs a uniform cap on each arrival. -/
def bulkProcess : Process Nat Nat where
  step s a t := t + 1 = s + a

theorem bulk_sustain_law :
    SustainLaw bulkProcess id (fun _ _ _ => 1) (fun _ a _ => a) := by
  intro s a t h
  exact Nat.le_of_eq h

theorem bulk_has_no_uniform_arrival_cap :
    ¬ ∃ cap, ∀ s a t, bulkProcess.step s a t → a ≤ cap := by
  rintro ⟨cap, hcap⟩
  have edge : bulkProcess.step 0 (cap + 1) cap := by
    change cap + 1 = 0 + (cap + 1)
    omega
  have h := hcap 0 (cap + 1) cap edge
  omega

theorem bulk_single_delivery (amount : Nat) :
    SupportTrace bulkProcess (fun _ _ _ => 1) (fun _ a _ => a)
      0 [amount + 1] amount 1 (amount + 1) 1 := by
  have hs : bulkProcess.step 0 (amount + 1) amount := by
    change amount + 1 = 0 + (amount + 1)
    omega
  have ht : SupportTrace bulkProcess (fun _ _ _ => 1) (fun _ a _ => a)
      amount [] amount 0 0 0 := .nil amount
  simpa [arrivalEvent] using SupportTrace.cons hs ht

theorem bulk_consumes_held (amount : Nat) :
    SupportTrace bulkProcess (fun _ _ _ => 1) (fun _ a _ => a)
      amount (List.replicate amount 0) 0 amount 0 0 := by
  induction amount with
  | zero => exact .nil 0
  | succ amount ih =>
    have hs : bulkProcess.step (amount + 1) 0 amount := by
      change amount + 1 = amount + 1 + 0
      omega
    simpa [List.replicate_succ, arrivalEvent, Nat.add_comm] using SupportTrace.cons hs ih

theorem bulk_single_delivery_then_run (amount : Nat) :
    SupportTrace bulkProcess (fun _ _ _ => 1) (fun _ a _ => a)
      0 ((amount + 1) :: List.replicate amount 0) 0 (amount + 1) (amount + 1) 1 := by
  have hs : bulkProcess.step 0 (amount + 1) amount := by
    change amount + 1 = 0 + (amount + 1)
    omega
  simpa [arrivalEvent, Nat.add_comm] using SupportTrace.cons hs (bulk_consumes_held amount)

#print axioms renewal_sustain_law
#print axioms renewal_unit_enactment
#print axioms renewal_arrival_cap
#print axioms renewal_cycle
#print axioms terminal_branch
#print axioms terminal_has_no_continuation
#print axioms cycle_is_lawful
#print axioms renewal_admits_infinite_execution
#print axioms same_law_admits_continuation_and_loss
#print axioms insufficient_sustain_law
#print axioms insufficient_arrival_is_always_positive
#print axioms insufficient_finite_bound
#print axioms insufficient_has_no_infinite_execution
#print axioms free_sustain_law
#print axioms free_infinite_execution
#print axioms free_process_has_no_unit_enactment
#print axioms bulk_sustain_law
#print axioms bulk_has_no_uniform_arrival_cap
#print axioms bulk_single_delivery
#print axioms bulk_consumes_held
#print axioms bulk_single_delivery_then_run

end Generative.Conditional.Examples
