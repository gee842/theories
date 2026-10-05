import ProtocolComposition

/-!
# Paid first-return blocks and an admitted infinite busy execution

Both examples use the same declared micro-event law. Entry spends usable fuel
before a later event converts a finite source unit into usable fuel. Optional
stalling gives the same internal tick a busy self-loop as well as a completing
outcome. Completed finite macro histories do not assert that completion occurs.
No probabilities, fairness, physical clock, identified chemistry or emerging
controller architecture are supplied by these discrete examples.
-/

namespace Generative.Learning.Protocols.Examples

inductive Phase where
  | ready | busy
  deriving DecidableEq

structure Inventory where
  phase : Phase
  fuel : Nat
  source : Nat
  deriving DecidableEq

def ready (fuel source : Nat) : Inventory := ⟨.ready, fuel, source⟩
def busy (fuel source : Nat) : Inventory := ⟨.busy, fuel, source⟩

inductive MicroEvent where
  | pay | tick
  deriving DecidableEq

inductive PaidStep (stall : Bool) : Inventory → MicroEvent → Inventory → Prop where
  | pay (fuel source : Nat) :
      PaidStep stall (ready (fuel + 1) source) .pay (busy fuel source)
  | replenish (fuel source : Nat) :
      PaidStep stall (busy fuel (source + 1)) .tick (ready (fuel + 1) source)
  | spin (fuel source : Nat) (allowed : stall = true) :
      PaidStep stall (busy fuel source) .tick (busy fuel source)

def world (stall : Bool) : Process Inventory MicroEvent := ⟨PaidStep stall⟩

def protocol (stall : Bool) : Protocol (world stall) Unit where
  boundary s := s.phase = .ready
  permits _ _ _ _ := True

def demand (_ : Inventory) (event : MicroEvent) (_ : Inventory) : Nat :=
  match event with
  | .pay => 1
  | .tick => 0

def credit (_ : Inventory) (event : MicroEvent) (t : Inventory) : Nat :=
  match event with
  | .pay => 0
  | .tick => if t.phase = .ready then 1 else 0

/-- Every replenishment debits the finite source; entry has no simultaneous credit. -/
theorem usable_account (stall : Bool) :
    Conditional.AccountLaw (world stall) Inventory.fuel demand credit := by
  intro s event t h
  cases h <;> simp [ready, busy, demand, credit]

theorem source_account (stall : Bool) :
    Conditional.AccountLaw (world stall) Inventory.source credit (fun _ _ _ => 0) := by
  intro s event t h
  cases h <;> simp [ready, busy, credit]

/-- Capturing source moves support; it does not create additional total stock. -/
theorem total_account (stall : Bool) :
    Conditional.AccountLaw (world stall) (fun s => s.fuel + s.source)
      demand (fun _ _ _ => 0) := by
  intro s event t h
  cases h <;> simp [ready, busy, demand] <;> omega

theorem zero_fuel_has_no_entry (stall : Bool) (source : Nat) :
    ¬ Enabled (world stall) (ready 0 source) .pay := by
  rintro ⟨t, h⟩
  cases h

/-- Terminal balance can hold although the first actual bill cannot be paid. -/
theorem empty_endpoint_balance :
    0 + 1 ≤ 0 + 1 ∧ ¬ Enabled (world false) (ready 0 1) .pay := by
  exact ⟨by omega, zero_fuel_has_no_entry false 1⟩

theorem paid_cycle_trace (stall : Bool) (fuel source : Nat) :
    Trace (world stall) (ready (fuel + 1) (source + 1)) [.pay, .tick]
      (ready (fuel + 1) source) := by
  exact .cons (.pay fuel (source + 1)) (.cons (.replenish fuel source) (.nil _))

/-- The entry bill is paid before the later source credit, on one actual path. -/
theorem paid_cycle_account (stall : Bool) (fuel source : Nat) :
    Conditional.SupportTrace (world stall) demand credit
      (ready (fuel + 1) (source + 1)) [.pay, .tick]
      (ready (fuel + 1) source) 1 1 1 := by
  simpa [demand, credit, ready, Conditional.credited] using
    (Conditional.SupportTrace.cons (P := world stall) (demand := demand) (credit := credit)
      (PaidStep.pay (stall := stall) fuel (source + 1))
      (Conditional.SupportTrace.cons (PaidStep.replenish (stall := stall) fuel source)
        (Conditional.SupportTrace.nil (ready (fuel + 1) source))))

theorem two_cycles_no_refill (stall : Bool) :
    Conditional.SupportTrace (world stall) demand credit
      (ready 1 2) [.pay, .tick, .pay, .tick] (ready 1 0) 2 2 2 := by
  exact Conditional.support_trace_append
    (paid_cycle_account stall 0 1) (paid_cycle_account stall 0 0)

theorem paid_block (stall : Bool) (command : Unit) (fuel source : Nat) :
    BlockPath (protocol stall) command (ready (fuel + 1) (source + 1))
      [.pay, .tick] (ready (fuel + 1) source) := by
  refine .next ⟨.pay fuel (source + 1), trivial⟩ ?_
    (.finish ⟨.replenish fuel source, trivial⟩ rfl)
  simp [protocol, busy]

def BlockOutcome (s t : Inventory) : Prop :=
  t.phase = .ready ∧ s.source = t.source + 1 ∧
    match s.phase with
    | .ready => t.fuel = s.fuel ∧ 0 < s.fuel
    | .busy => t.fuel = s.fuel + 1

/-- Arbitrarily many admitted busy ticks cannot change a completed block's
endpoint relation; they can still prevent reaching any endpoint. -/
theorem block_outcome {stall : Bool} {command : Unit} {s t : Inventory}
    {word : List MicroEvent} (h : BlockPath (protocol stall) command s word t) :
    BlockOutcome s t := by
  induction h with
  | finish hs hb =>
    cases hs.1 with
    | pay fuel source => simp [protocol, busy] at hb
    | replenish fuel source => simp [BlockOutcome, ready, busy]
    | spin fuel source allowed => simp [protocol, busy] at hb
  | next hs hn htail ih =>
    cases hs.1 with
    | pay fuel source =>
      obtain ⟨ht, hsource, hfuel⟩ := ih
      exact ⟨ht, hsource, hfuel, Nat.zero_lt_succ fuel⟩
    | replenish fuel source => simp [protocol, ready] at hn
    | spin fuel source allowed => exact ih

theorem boundary_inventory (stall : Bool) (s : BoundaryState (protocol stall)) :
    s.val = ready s.val.fuel s.val.source := by
  rcases s with ⟨⟨phase, fuel, source⟩, h⟩
  change phase = .ready at h
  subst phase
  rfl

theorem completed_step_iff (stall : Bool) (command : Unit)
    (s t : BoundaryState (protocol stall)) :
    (blockProcess (protocol stall)).step s command t ↔
      t.val.fuel = s.val.fuel ∧ s.val.source = t.val.source + 1 ∧ 0 < s.val.fuel := by
  constructor
  · rintro ⟨word, h⟩
    obtain ⟨_, hsource, hfuel⟩ := block_outcome h
    have phase : s.val.phase = .ready := s.property
    have amounts : t.val.fuel = s.val.fuel ∧ 0 < s.val.fuel := by
      simpa [phase] using hfuel
    exact ⟨amounts.1, hsource, amounts.2⟩
  · rintro ⟨hfuel, hsource, hpositive⟩
    have fuel_eq : s.val.fuel = (s.val.fuel - 1) + 1 := by omega
    refine ⟨[.pay, .tick], ?_⟩
    rw [boundary_inventory stall s, boundary_inventory stall t, hfuel, hsource, fuel_eq]
    exact paid_block stall command (s.val.fuel - 1) t.val.source

/-- Both implementations have exactly the same completed macro step relation. -/
theorem completed_steps_agree (command : Unit)
    (s t : BoundaryState (protocol false)) :
    (blockProcess (protocol false)).step s command t ↔
      (blockProcess (protocol true)).step s command t := by
  rw [completed_step_iff false, completed_step_iff true]

theorem completed_histories_agree (s t : BoundaryState (protocol false))
    (word : List Unit) :
    Trace (blockProcess (protocol false)) s word t ↔
      Trace (blockProcess (protocol true)) s word t := by
  constructor
  · exact trace_map (f := id) (fun s a t h => (completed_steps_agree a s t).mp h)
  · exact trace_map (f := id) (fun s a t h => (completed_steps_agree a s t).mpr h)

theorem no_completed_block_from_empty (stall : Bool) (source : Nat) :
    ¬ Enabled (blockProcess (protocol stall)) ⟨ready 0 source, rfl⟩ () := by
  rintro ⟨t, h⟩
  have hp := ((completed_step_iff stall () _ t).mp h).2.2
  simp [ready] at hp

theorem no_completed_block_after_two (stall : Bool) :
    ¬ Enabled (blockProcess (protocol stall)) ⟨ready 1 0, rfl⟩ () := by
  rintro ⟨t, h⟩
  have hs := ((completed_step_iff stall () _ t).mp h).2.1
  exact Nat.noConfusion hs

theorem two_completed_blocks (stall : Bool) :
    Trace (blockProcess (protocol stall)) ⟨ready 1 2, rfl⟩ [(), ()]
      ⟨ready 1 0, rfl⟩ := by
  exact .cons (m := ⟨ready 1 1, rfl⟩) ⟨[.pay, .tick], paid_block stall () 0 1⟩
    (.cons ⟨[.pay, .tick], paid_block stall () 0 0⟩ (.nil _))

/-- A failed incomplete attempt still spends the last inherited usable unit. -/
theorem paid_deadlock_prefix :
    Trace (world false) (ready 1 0) [.pay] (busy 0 0) := by
  exact .cons (.pay 0 0) (.nil _)

theorem nonstall_exhausted_deadlock (event : MicroEvent) :
    ¬ Enabled (world false) (busy 0 0) event := by
  rintro ⟨t, h⟩
  cases h with
  | spin _ _ h => cases h

def busyRun : Nat → Inventory
  | 0 => ready 1 1
  | _ + 1 => busy 0 1

def busyEvent : Nat → MicroEvent
  | 0 => .pay
  | _ + 1 => .tick

/-- An explicit infinite discrete execution of the committed permissive protocol.
The same tick could finish; no fairness or completion probability is asserted. -/
theorem infinite_committed_busy_run (n : Nat) :
    (committed (protocol true) ()).step (busyRun n) (busyEvent n) (busyRun (n + 1)) := by
  cases n with
  | zero => exact ⟨.pay 0 1, trivial⟩
  | succ n => exact ⟨.spin 0 1 rfl, trivial⟩

theorem busy_run_never_returns (n : Nat) :
    ¬ (protocol true).boundary (busyRun (n + 1)) := by
  simp [protocol, busyRun, busy]

/-- With stalling disabled, every admitted event from busy completes immediately. -/
theorem nonstall_busy_step_finishes {fuel source : Nat} {event : MicroEvent}
    {t : Inventory} (h : (world false).step (busy fuel source) event t) :
    t.phase = .ready := by
  cases h with
  | replenish => rfl
  | spin _ _ h => cases h

end Generative.Learning.Protocols.Examples

#print axioms Generative.Learning.Protocols.Examples.usable_account
#print axioms Generative.Learning.Protocols.Examples.source_account
#print axioms Generative.Learning.Protocols.Examples.total_account
#print axioms Generative.Learning.Protocols.Examples.zero_fuel_has_no_entry
#print axioms Generative.Learning.Protocols.Examples.empty_endpoint_balance
#print axioms Generative.Learning.Protocols.Examples.paid_cycle_trace
#print axioms Generative.Learning.Protocols.Examples.paid_cycle_account
#print axioms Generative.Learning.Protocols.Examples.two_cycles_no_refill
#print axioms Generative.Learning.Protocols.Examples.paid_block
#print axioms Generative.Learning.Protocols.Examples.block_outcome
#print axioms Generative.Learning.Protocols.Examples.boundary_inventory
#print axioms Generative.Learning.Protocols.Examples.completed_step_iff
#print axioms Generative.Learning.Protocols.Examples.completed_steps_agree
#print axioms Generative.Learning.Protocols.Examples.completed_histories_agree
#print axioms Generative.Learning.Protocols.Examples.no_completed_block_from_empty
#print axioms Generative.Learning.Protocols.Examples.no_completed_block_after_two
#print axioms Generative.Learning.Protocols.Examples.two_completed_blocks
#print axioms Generative.Learning.Protocols.Examples.paid_deadlock_prefix
#print axioms Generative.Learning.Protocols.Examples.nonstall_exhausted_deadlock
#print axioms Generative.Learning.Protocols.Examples.infinite_committed_busy_run
#print axioms Generative.Learning.Protocols.Examples.busy_run_never_returns
#print axioms Generative.Learning.Protocols.Examples.nonstall_busy_step_finishes
