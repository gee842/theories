import GenerativeCore

/-!
# Native packet process reconstructed from the existing diagnosis port

Source: mathematical-abstraction/acquisition/access/diagnosis.py, Account.pay
(lines 44–59) and Port.command (83–114). This is the default scale-one tariff:
65536 integer fuel ticks represent one source unit; interface and receipt each
cost 16384 ticks plus one tick of rent for each live/workspace/temporary cell.
The two temporary cells are included in the capacity check before each payment.

The port call holds live, workspace and capacity fixed. External diagnostic
preparation, committed belief updates and retention are outside this executor.
Historical event-log metadata and maximum peak are not state coordinates here.
Every resource-changing stage and its ordering are retained, including source
conversion before a separately funded receipt. An interrupted result contains
the state actually reached. No rollback, restored packet or acquired receipt is
inserted. A stopped call is represented separately from a completed command.

The cycle, gate and default tariff are inherited apparatus laws, not claimed to
follow from logic or to be universal. This source imports no desired macro table.
-/

namespace Generative.NativePacketProcess

inductive Phase where
  | p0 | p1 | p2

inductive Command where
  | a | reset | read | probe

structure State where
  phase : Phase
  tau : Bool
  sigma : Bool
  broken : Bool
  blocked : Bool
  receiptFlip : Bool
  source : Nat
  fuel : Nat
  live : Nat
  workspace : Nat
  capacity : Nat
  spent : Nat
  income : Nat
  transferred : Nat
  wasted : Nat

inductive Observation where
  | silent
  | reading (value : Bool)
  | receipt (value : Bool)

inductive Failure where
  | interfaceCapacity | interfaceFunding | sourceUnavailable
  | receiptCapacity | receiptFunding

inductive Result where
  | complete (state : State) (observation : Observation)
  | stopped (state : State) (reason : Failure)

inductive Payment where
  | paid (state : State)
  | capacity | funding

def output : Phase → Bool
  | .p0 => false
  | .p1 => false
  | .p2 => true

def nextPhase : Phase → Phase
  | .p0 => .p1
  | .p1 => .p2
  | .p2 => .p0

/-- The actual native transfer gate, independently of any macro target class. -/
def arrivalAt (learnedOutput tau blocked : Bool) : Bool :=
  (learnedOutput != tau) && !blocked

def arrival (s : State) : Bool := arrivalAt (output s.phase) s.tau s.blocked

def readBit (s : State) : Bool := (output s.phase != s.tau) != s.sigma

def receiptBit (s : State) : Bool := arrival s != s.receiptFlip

def peak (s : State) : Nat := s.live + s.workspace + 2

def bill (s : State) : Nat := 16384 + peak s

def Payable (s : State) : Prop := peak s ≤ s.capacity ∧ bill s ≤ s.fuel

def debit (s : State) : State :=
  { s with fuel := s.fuel - bill s, spent := s.spent + bill s }

def charge (s : State) : Payment :=
  if peak s ≤ s.capacity then
    if bill s ≤ s.fuel then .paid (debit s) else .funding
  else .capacity

def gain (s : State) : Nat := if arrival s then 655360 else 0

/-- Applied only after the source guard in execute. It preserves the actual
arrival before the later receipt charge, even if that charge is denied. -/
def convert (s : State) : State :=
  { s with
    source := s.source - 10,
    fuel := s.fuel + gain s,
    income := s.income + gain s,
    transferred := s.transferred + (if arrival s then 10 else 0),
    wasted := s.wasted + (if arrival s then 0 else 10) }

/-- The second stage of the same command, after its interface charge. -/
def finishProbe (ready : State) : Result :=
  if 10 ≤ ready.source then
    match charge (convert ready) with
    | .capacity => .stopped (convert ready) .receiptCapacity
    | .funding => .stopped (convert ready) .receiptFunding
    | .paid recorded => .complete recorded (.receipt (receiptBit ready))
  else .stopped ready .sourceUnavailable

def execute (s : State) (command : Command) : Result :=
  match charge s with
  | .capacity => .stopped s .interfaceCapacity
  | .funding => .stopped s .interfaceFunding
  | .paid ready =>
      match command with
      | .a => .complete { ready with phase := nextPhase ready.phase } .silent
      | .reset =>
          .complete { ready with phase := if ready.broken then ready.phase else .p0 } .silent
      | .read => .complete ready (.reading (readBit ready))
      | .probe => finishProbe ready

def reached : Result → State
  | .complete s _ => s
  | .stopped s _ => s

/-- Only completed native calls count as these Process edges. Interrupted calls
remain fully represented by execute and their separate failure theorems. -/
def process : Process State Command where
  step s command t := ∃ o, execute s command = .complete t o

def probeFinal (s : State) : State := debit (convert (debit s))

def ProbeReady (s : State) : Prop :=
  Payable s ∧ 10 ≤ s.source ∧ Payable (convert (debit s))

theorem charge_paid (s : State) (capacity : peak s ≤ s.capacity)
    (funding : bill s ≤ s.fuel) : charge s = .paid (debit s) := by
  unfold charge
  rw [if_pos capacity, if_pos funding]

theorem charge_capacity (s : State) (capacity : ¬ peak s ≤ s.capacity) :
    charge s = .capacity := by
  unfold charge
  rw [if_neg capacity]

theorem charge_funding (s : State) (capacity : peak s ≤ s.capacity)
    (funding : ¬ bill s ≤ s.fuel) : charge s = .funding := by
  unfold charge
  rw [if_pos capacity, if_neg funding]

theorem charge_paid_iff (s t : State) :
    charge s = .paid t ↔ Payable s ∧ t = debit s := by
  unfold charge
  split
  next capacity =>
    split
    next funding =>
      constructor
      · intro h
        cases h
        exact ⟨⟨capacity, funding⟩, rfl⟩
      · rintro ⟨_, h⟩
        cases h
        rfl
    next funding =>
      constructor
      · intro h
        cases h
      · intro h
        exact False.elim (funding h.1.2)
  next capacity =>
    constructor
    · intro h
      cases h
    · intro h
      exact False.elim (capacity h.1.1)

theorem probeReady_exact (s : State) :
    ProbeReady s ↔ peak s ≤ s.capacity ∧ bill s ≤ s.fuel ∧ 10 ≤ s.source ∧
      bill s ≤ s.fuel - bill s + gain s := by
  constructor
  · intro h
    exact ⟨h.1.1, h.1.2, h.2.1, h.2.2.2⟩
  · rintro ⟨capacity, funding, source, receipt⟩
    exact ⟨⟨capacity, funding⟩, source, ⟨capacity, receipt⟩⟩

theorem probe_complete (s : State) (ready : ProbeReady s) :
    execute s .probe = .complete (probeFinal s) (.receipt (receiptBit s)) := by
  unfold execute
  rw [charge_paid s ready.1.1 ready.1.2]
  change (if 10 ≤ s.source then
    match charge (convert (debit s)) with
    | .capacity => Result.stopped (convert (debit s)) .receiptCapacity
    | .funding => Result.stopped (convert (debit s)) .receiptFunding
    | .paid recorded => Result.complete recorded (.receipt (receiptBit (debit s)))
    else Result.stopped (debit s) .sourceUnavailable) = _
  rw [if_pos ready.2.1, charge_paid (convert (debit s)) ready.2.2.1 ready.2.2.2]
  rfl


theorem a_complete (s : State) (ready : Payable s) :
    execute s .a = .complete { debit s with phase := nextPhase s.phase } .silent := by
  unfold execute
  rw [charge_paid s ready.1 ready.2]
  rfl

theorem reset_complete (s : State) (ready : Payable s) :
    execute s .reset =
      .complete { debit s with phase := if s.broken then s.phase else .p0 } .silent := by
  unfold execute
  rw [charge_paid s ready.1 ready.2]
  rfl

theorem read_complete (s : State) (ready : Payable s) :
    execute s .read = .complete (debit s) (.reading (readBit s)) := by
  unfold execute
  rw [charge_paid s ready.1 ready.2]
  rfl

/-- Exact completion criterion, including the reached state and the actual
receipt (which still permits the inherited receipt-flip countercase). -/
theorem probe_complete_iff (s t : State) (observation : Observation) :
    execute s .probe = .complete t observation ↔
      ProbeReady s ∧ t = probeFinal s ∧ observation = .receipt (receiptBit s) := by
  constructor
  · intro h
    unfold execute at h
    generalize interface : charge s = payment at h
    cases payment with
    | capacity => cases h
    | funding => cases h
    | paid ready =>
      obtain ⟨payable, equality⟩ := (charge_paid_iff s ready).mp interface
      cases equality
      change finishProbe (debit s) = .complete t observation at h
      unfold finishProbe at h
      split at h
      next source =>
        generalize receipt : charge (convert (debit s)) = second at h
        cases second with
        | capacity => cases h
        | funding => cases h
        | paid recorded =>
          obtain ⟨lastPayable, lastEquality⟩ :=
            (charge_paid_iff (convert (debit s)) recorded).mp receipt
          cases lastEquality
          cases h
          exact ⟨⟨payable, source, lastPayable⟩, rfl, rfl⟩
      next missing => cases h
  · rintro ⟨ready, rfl, rfl⟩
    exact probe_complete s ready

theorem interface_capacity_stops (s : State) (command : Command)
    (capacity : ¬ peak s ≤ s.capacity) :
    execute s command = .stopped s .interfaceCapacity := by
  unfold execute
  rw [charge_capacity s capacity]

theorem interface_funding_stops (s : State) (command : Command)
    (capacity : peak s ≤ s.capacity) (funding : ¬ bill s ≤ s.fuel) :
    execute s command = .stopped s .interfaceFunding := by
  unfold execute
  rw [charge_funding s capacity funding]

/-- Source denial occurs after the interface debit; no source conversion occurs. -/
theorem probe_source_stops (s : State) (ready : Payable s)
    (source : ¬ 10 ≤ s.source) :
    execute s .probe = .stopped (debit s) .sourceUnavailable := by
  unfold execute
  rw [charge_paid s ready.1 ready.2]
  change (if 10 ≤ s.source then _ else _) = _
  rw [if_neg source]

/-- A denied receipt retains the already converted source, actual arrival or
waste, credited income and interface charge. It delivers no receipt. -/
theorem probe_receipt_funding_stops (s : State) (ready : Payable s)
    (source : 10 ≤ s.source)
    (receipt : ¬ bill s ≤ s.fuel - bill s + gain s) :
    execute s .probe = .stopped (convert (debit s)) .receiptFunding := by
  unfold execute
  rw [charge_paid s ready.1 ready.2]
  change (if 10 ≤ s.source then _ else _) = _
  rw [if_pos source]
  rw [charge_funding (convert (debit s)) ready.1 receipt]

/-- Exact native resource effects, in source units and integer fuel ticks.
The two subtractions are ordered payments, not a credit before extraction. -/
theorem probe_final_effects (s : State) :
    (probeFinal s).phase = s.phase ∧
    (probeFinal s).source = s.source - 10 ∧
    (probeFinal s).fuel = (s.fuel - bill s + gain s) - bill s ∧
    (probeFinal s).spent = (s.spent + bill s) + bill s ∧
    (probeFinal s).income = s.income + gain s ∧
    (probeFinal s).transferred = s.transferred + (if arrival s then 10 else 0) ∧
    (probeFinal s).wasted = s.wasted + (if arrival s then 0 else 10) :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- Static port parameters are retained even by interrupted calls. The phase
is deliberately absent: native advance and reset may change it. -/
def SameParameters (before after : State) : Prop :=
  after.tau = before.tau ∧ after.sigma = before.sigma ∧
  after.broken = before.broken ∧ after.blocked = before.blocked ∧
  after.receiptFlip = before.receiptFlip ∧ after.live = before.live ∧
  after.workspace = before.workspace ∧ after.capacity = before.capacity

theorem execute_retains_parameters (s : State) (command : Command) :
    SameParameters s (reached (execute s command)) := by
  unfold execute
  generalize interface : charge s = payment
  cases payment with
  | capacity => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
  | funding => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
  | paid ready =>
    obtain ⟨_, equality⟩ := (charge_paid_iff s ready).mp interface
    cases equality
    cases command with
    | a => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
    | reset => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
    | read => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
    | probe =>
      change SameParameters s (reached (finishProbe (debit s)))
      unfold finishProbe
      split
      next source =>
        generalize receipt : charge (convert (debit s)) = second
        cases second with
        | capacity => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
        | funding => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
        | paid recorded =>
          obtain ⟨_, lastEquality⟩ :=
            (charge_paid_iff (convert (debit s)) recorded).mp receipt
          cases lastEquality
          exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
      next missing => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem completed_retains_parameters {s t : State} {command : Command}
    {observation : Observation} (actual : execute s command = .complete t observation) :
    SameParameters s t := by
  have retained := execute_retains_parameters s command
  rw [actual] at retained
  exact retained


/-- The second capacity check is faithfully present, but cannot newly fail:
this port call does not change live/workspace/capacity between its two charges. -/
theorem receipt_capacity_unreachable (s t : State) (command : Command) :
    execute s command ≠ .stopped t .receiptCapacity := by
  unfold execute
  generalize interface : charge s = payment
  cases payment with
  | capacity => intro h; cases h
  | funding => intro h; cases h
  | paid ready =>
    obtain ⟨payable, equality⟩ := (charge_paid_iff s ready).mp interface
    cases equality
    cases command with
    | a => intro h; cases h
    | reset => intro h; cases h
    | read => intro h; cases h
    | probe =>
      change finishProbe (debit s) ≠ .stopped t .receiptCapacity
      unfold finishProbe
      split
      next source =>
        by_cases enough : bill (convert (debit s)) ≤ (convert (debit s)).fuel
        · rw [charge_paid (convert (debit s)) payable.1 enough]
          intro h; cases h
        · rw [charge_funding (convert (debit s)) payable.1 enough]
          intro h; cases h
      next missing => intro h; cases h

end Generative.NativePacketProcess

#print axioms Generative.NativePacketProcess.Phase
#print axioms Generative.NativePacketProcess.Command
#print axioms Generative.NativePacketProcess.State
#print axioms Generative.NativePacketProcess.Observation
#print axioms Generative.NativePacketProcess.Failure
#print axioms Generative.NativePacketProcess.Result
#print axioms Generative.NativePacketProcess.Payment
#print axioms Generative.NativePacketProcess.output
#print axioms Generative.NativePacketProcess.nextPhase
#print axioms Generative.NativePacketProcess.arrivalAt
#print axioms Generative.NativePacketProcess.arrival
#print axioms Generative.NativePacketProcess.readBit
#print axioms Generative.NativePacketProcess.receiptBit
#print axioms Generative.NativePacketProcess.peak
#print axioms Generative.NativePacketProcess.bill
#print axioms Generative.NativePacketProcess.Payable
#print axioms Generative.NativePacketProcess.debit
#print axioms Generative.NativePacketProcess.charge
#print axioms Generative.NativePacketProcess.gain
#print axioms Generative.NativePacketProcess.convert
#print axioms Generative.NativePacketProcess.finishProbe
#print axioms Generative.NativePacketProcess.execute
#print axioms Generative.NativePacketProcess.reached
#print axioms Generative.NativePacketProcess.process
#print axioms Generative.NativePacketProcess.probeFinal
#print axioms Generative.NativePacketProcess.ProbeReady
#print axioms Generative.NativePacketProcess.charge_paid
#print axioms Generative.NativePacketProcess.charge_capacity
#print axioms Generative.NativePacketProcess.charge_funding
#print axioms Generative.NativePacketProcess.charge_paid_iff
#print axioms Generative.NativePacketProcess.probeReady_exact
#print axioms Generative.NativePacketProcess.probe_complete
#print axioms Generative.NativePacketProcess.a_complete
#print axioms Generative.NativePacketProcess.reset_complete
#print axioms Generative.NativePacketProcess.read_complete
#print axioms Generative.NativePacketProcess.probe_complete_iff
#print axioms Generative.NativePacketProcess.interface_capacity_stops
#print axioms Generative.NativePacketProcess.interface_funding_stops
#print axioms Generative.NativePacketProcess.probe_source_stops
#print axioms Generative.NativePacketProcess.probe_receipt_funding_stops
#print axioms Generative.NativePacketProcess.probe_final_effects
#print axioms Generative.NativePacketProcess.SameParameters
#print axioms Generative.NativePacketProcess.execute_retains_parameters
#print axioms Generative.NativePacketProcess.completed_retains_parameters
#print axioms Generative.NativePacketProcess.receipt_capacity_unreachable
