import GenerativeCore

/-!
# Native packet process reconstructed from the existing diagnosis port

Source: mathematical-abstraction/acquisition/access/diagnosis.py, the original
`Account.pay` (lines 44–59) and `Port.command` (83–114), at its default scale
one. 65536 integer ticks of what is `held` represent one source unit. Each
interface stage and each receipt stage draws 16384 ticks plus one tick for each
live, workspace or temporary cell. The two temporary cells are included in the
capacity check before each stage is supported.

The port call holds live, workspace and capacity fixed. External diagnostic
preparation, committed belief updates and retention are outside this executor.
Historical event-log metadata and maximum peak are not state coordinates here.
Every stage that changes what is held, enacted or arrived is retained in order,
including source conversion before a separately supported receipt. An
interrupted result contains the state actually reached. No rollback, restored
packet or acquired receipt is inserted. A stopped call is represented
separately from a completed command.

Vocabulary renamed on 6 October 2026 at Ren's direction. The Python original
keeps its names; here `held`, `enacted`, `arrived` and `dissipated` replace
fuel, spent, income and wasted, and a stage's `draw`, `support` and `enact`
replace bill, charge and debit. Statements and proofs are unchanged.

The cycle, gate and draw schedule are inherited apparatus laws, not claimed to
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
  held : Nat
  live : Nat
  workspace : Nat
  capacity : Nat
  enacted : Nat
  arrived : Nat
  transferred : Nat
  dissipated : Nat

inductive Observation where
  | silent
  | reading (value : Bool)
  | receipt (value : Bool)

inductive Failure where
  | interfaceCapacity | interfaceInsufficient | sourceUnavailable
  | receiptCapacity | receiptInsufficient

inductive Result where
  | complete (state : State) (observation : Observation)
  | stopped (state : State) (reason : Failure)

inductive Support where
  | sustained (state : State)
  | capacity | insufficient

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

def draw (s : State) : Nat := 16384 + peak s

def Supportable (s : State) : Prop := peak s ≤ s.capacity ∧ draw s ≤ s.held

def enact (s : State) : State :=
  { s with held := s.held - draw s, enacted := s.enacted + draw s }

def support (s : State) : Support :=
  if peak s ≤ s.capacity then
    if draw s ≤ s.held then .sustained (enact s) else .insufficient
  else .capacity

def arrivalAmount (s : State) : Nat := if arrival s then 655360 else 0

/-- Applied only after the source guard in execute. It preserves the actual
arrival before the later receipt stage, even if that stage cannot be supported. -/
def convert (s : State) : State :=
  { s with
    source := s.source - 10,
    held := s.held + arrivalAmount s,
    arrived := s.arrived + arrivalAmount s,
    transferred := s.transferred + (if arrival s then 10 else 0),
    dissipated := s.dissipated + (if arrival s then 0 else 10) }

/-- The second stage of the same command, after its interface stage is supported. -/
def finishProbe (ready : State) : Result :=
  if 10 ≤ ready.source then
    match support (convert ready) with
    | .capacity => .stopped (convert ready) .receiptCapacity
    | .insufficient => .stopped (convert ready) .receiptInsufficient
    | .sustained recorded => .complete recorded (.receipt (receiptBit ready))
  else .stopped ready .sourceUnavailable

def execute (s : State) (command : Command) : Result :=
  match support s with
  | .capacity => .stopped s .interfaceCapacity
  | .insufficient => .stopped s .interfaceInsufficient
  | .sustained ready =>
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

def probeFinal (s : State) : State := enact (convert (enact s))

def ProbeReady (s : State) : Prop :=
  Supportable s ∧ 10 ≤ s.source ∧ Supportable (convert (enact s))

theorem support_sustained (s : State) (capacity : peak s ≤ s.capacity)
    (covered : draw s ≤ s.held) : support s = .sustained (enact s) := by
  unfold support
  rw [if_pos capacity, if_pos covered]

theorem support_capacity (s : State) (capacity : ¬ peak s ≤ s.capacity) :
    support s = .capacity := by
  unfold support
  rw [if_neg capacity]

theorem support_insufficient (s : State) (capacity : peak s ≤ s.capacity)
    (short : ¬ draw s ≤ s.held) : support s = .insufficient := by
  unfold support
  rw [if_pos capacity, if_neg short]

theorem support_sustained_iff (s t : State) :
    support s = .sustained t ↔ Supportable s ∧ t = enact s := by
  unfold support
  split
  next capacity =>
    split
    next covered =>
      constructor
      · intro h
        cases h
        exact ⟨⟨capacity, covered⟩, rfl⟩
      · rintro ⟨_, h⟩
        cases h
        rfl
    next short =>
      constructor
      · intro h
        cases h
      · intro h
        exact False.elim (short h.1.2)
  next capacity =>
    constructor
    · intro h
      cases h
    · intro h
      exact False.elim (capacity h.1.1)

theorem probeReady_exact (s : State) :
    ProbeReady s ↔ peak s ≤ s.capacity ∧ draw s ≤ s.held ∧ 10 ≤ s.source ∧
      draw s ≤ s.held - draw s + arrivalAmount s := by
  constructor
  · intro h
    exact ⟨h.1.1, h.1.2, h.2.1, h.2.2.2⟩
  · rintro ⟨capacity, covered, source, receipt⟩
    exact ⟨⟨capacity, covered⟩, source, ⟨capacity, receipt⟩⟩

theorem probe_complete (s : State) (ready : ProbeReady s) :
    execute s .probe = .complete (probeFinal s) (.receipt (receiptBit s)) := by
  unfold execute
  rw [support_sustained s ready.1.1 ready.1.2]
  change (if 10 ≤ s.source then
    match support (convert (enact s)) with
    | .capacity => Result.stopped (convert (enact s)) .receiptCapacity
    | .insufficient => Result.stopped (convert (enact s)) .receiptInsufficient
    | .sustained recorded => Result.complete recorded (.receipt (receiptBit (enact s)))
    else Result.stopped (enact s) .sourceUnavailable) = _
  rw [if_pos ready.2.1, support_sustained (convert (enact s)) ready.2.2.1 ready.2.2.2]
  rfl


theorem a_complete (s : State) (ready : Supportable s) :
    execute s .a = .complete { enact s with phase := nextPhase s.phase } .silent := by
  unfold execute
  rw [support_sustained s ready.1 ready.2]
  rfl

theorem reset_complete (s : State) (ready : Supportable s) :
    execute s .reset =
      .complete { enact s with phase := if s.broken then s.phase else .p0 } .silent := by
  unfold execute
  rw [support_sustained s ready.1 ready.2]
  rfl

theorem read_complete (s : State) (ready : Supportable s) :
    execute s .read = .complete (enact s) (.reading (readBit s)) := by
  unfold execute
  rw [support_sustained s ready.1 ready.2]
  rfl

/-- Exact completion criterion, including the reached state and the actual
receipt (which still permits the inherited receipt-flip countercase). -/
theorem probe_complete_iff (s t : State) (observation : Observation) :
    execute s .probe = .complete t observation ↔
      ProbeReady s ∧ t = probeFinal s ∧ observation = .receipt (receiptBit s) := by
  constructor
  · intro h
    unfold execute at h
    generalize interface : support s = outcome at h
    cases outcome with
    | capacity => cases h
    | insufficient => cases h
    | sustained ready =>
      obtain ⟨supportable, equality⟩ := (support_sustained_iff s ready).mp interface
      cases equality
      change finishProbe (enact s) = .complete t observation at h
      unfold finishProbe at h
      split at h
      next source =>
        generalize receipt : support (convert (enact s)) = second at h
        cases second with
        | capacity => cases h
        | insufficient => cases h
        | sustained recorded =>
          obtain ⟨lastSupportable, lastEquality⟩ :=
            (support_sustained_iff (convert (enact s)) recorded).mp receipt
          cases lastEquality
          cases h
          exact ⟨⟨supportable, source, lastSupportable⟩, rfl, rfl⟩
      next missing => cases h
  · rintro ⟨ready, rfl, rfl⟩
    exact probe_complete s ready

theorem interface_capacity_stops (s : State) (command : Command)
    (capacity : ¬ peak s ≤ s.capacity) :
    execute s command = .stopped s .interfaceCapacity := by
  unfold execute
  rw [support_capacity s capacity]

theorem interface_insufficient_stops (s : State) (command : Command)
    (capacity : peak s ≤ s.capacity) (short : ¬ draw s ≤ s.held) :
    execute s command = .stopped s .interfaceInsufficient := by
  unfold execute
  rw [support_insufficient s capacity short]

/-- Source denial occurs after the interface stage is enacted; no source conversion occurs. -/
theorem probe_source_stops (s : State) (ready : Supportable s)
    (source : ¬ 10 ≤ s.source) :
    execute s .probe = .stopped (enact s) .sourceUnavailable := by
  unfold execute
  rw [support_sustained s ready.1 ready.2]
  change (if 10 ≤ s.source then _ else _) = _
  rw [if_neg source]

/-- An unsupported receipt stage retains the already converted source, the actual
arrival or dissipation, what arrived, and the enacted interface stage. It delivers no receipt. -/
theorem probe_receipt_insufficient_stops (s : State) (ready : Supportable s)
    (source : 10 ≤ s.source)
    (receipt : ¬ draw s ≤ s.held - draw s + arrivalAmount s) :
    execute s .probe = .stopped (convert (enact s)) .receiptInsufficient := by
  unfold execute
  rw [support_sustained s ready.1 ready.2]
  change (if 10 ≤ s.source then _ else _) = _
  rw [if_pos source]
  rw [support_insufficient (convert (enact s)) ready.1 receipt]

/-- Exact native resource effects, in source units and integer held ticks.
The two subtractions are ordered draws; nothing arrives before conversion. -/
theorem probe_final_effects (s : State) :
    (probeFinal s).phase = s.phase ∧
    (probeFinal s).source = s.source - 10 ∧
    (probeFinal s).held = (s.held - draw s + arrivalAmount s) - draw s ∧
    (probeFinal s).enacted = (s.enacted + draw s) + draw s ∧
    (probeFinal s).arrived = s.arrived + arrivalAmount s ∧
    (probeFinal s).transferred = s.transferred + (if arrival s then 10 else 0) ∧
    (probeFinal s).dissipated = s.dissipated + (if arrival s then 0 else 10) :=
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
  generalize interface : support s = outcome
  cases outcome with
  | capacity => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
  | insufficient => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
  | sustained ready =>
    obtain ⟨_, equality⟩ := (support_sustained_iff s ready).mp interface
    cases equality
    cases command with
    | a => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
    | reset => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
    | read => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
    | probe =>
      change SameParameters s (reached (finishProbe (enact s)))
      unfold finishProbe
      split
      next source =>
        generalize receipt : support (convert (enact s)) = second
        cases second with
        | capacity => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
        | insufficient => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
        | sustained recorded =>
          obtain ⟨_, lastEquality⟩ :=
            (support_sustained_iff (convert (enact s)) recorded).mp receipt
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
this port call does not change live/workspace/capacity between its two stages. -/
theorem receipt_capacity_unreachable (s t : State) (command : Command) :
    execute s command ≠ .stopped t .receiptCapacity := by
  unfold execute
  generalize interface : support s = outcome
  cases outcome with
  | capacity => intro h; cases h
  | insufficient => intro h; cases h
  | sustained ready =>
    obtain ⟨supportable, equality⟩ := (support_sustained_iff s ready).mp interface
    cases equality
    cases command with
    | a => intro h; cases h
    | reset => intro h; cases h
    | read => intro h; cases h
    | probe =>
      change finishProbe (enact s) ≠ .stopped t .receiptCapacity
      unfold finishProbe
      split
      next source =>
        by_cases enough : draw (convert (enact s)) ≤ (convert (enact s)).held
        · rw [support_sustained (convert (enact s)) supportable.1 enough]
          intro h; cases h
        · rw [support_insufficient (convert (enact s)) supportable.1 enough]
          intro h; cases h
      next missing => intro h; cases h

end Generative.NativePacketProcess

#print axioms Generative.NativePacketProcess.Phase
#print axioms Generative.NativePacketProcess.Command
#print axioms Generative.NativePacketProcess.State
#print axioms Generative.NativePacketProcess.Observation
#print axioms Generative.NativePacketProcess.Failure
#print axioms Generative.NativePacketProcess.Result
#print axioms Generative.NativePacketProcess.Support
#print axioms Generative.NativePacketProcess.output
#print axioms Generative.NativePacketProcess.nextPhase
#print axioms Generative.NativePacketProcess.arrivalAt
#print axioms Generative.NativePacketProcess.arrival
#print axioms Generative.NativePacketProcess.readBit
#print axioms Generative.NativePacketProcess.receiptBit
#print axioms Generative.NativePacketProcess.peak
#print axioms Generative.NativePacketProcess.draw
#print axioms Generative.NativePacketProcess.Supportable
#print axioms Generative.NativePacketProcess.enact
#print axioms Generative.NativePacketProcess.support
#print axioms Generative.NativePacketProcess.arrivalAmount
#print axioms Generative.NativePacketProcess.convert
#print axioms Generative.NativePacketProcess.finishProbe
#print axioms Generative.NativePacketProcess.execute
#print axioms Generative.NativePacketProcess.reached
#print axioms Generative.NativePacketProcess.process
#print axioms Generative.NativePacketProcess.probeFinal
#print axioms Generative.NativePacketProcess.ProbeReady
#print axioms Generative.NativePacketProcess.support_sustained
#print axioms Generative.NativePacketProcess.support_capacity
#print axioms Generative.NativePacketProcess.support_insufficient
#print axioms Generative.NativePacketProcess.support_sustained_iff
#print axioms Generative.NativePacketProcess.probeReady_exact
#print axioms Generative.NativePacketProcess.probe_complete
#print axioms Generative.NativePacketProcess.a_complete
#print axioms Generative.NativePacketProcess.reset_complete
#print axioms Generative.NativePacketProcess.read_complete
#print axioms Generative.NativePacketProcess.probe_complete_iff
#print axioms Generative.NativePacketProcess.interface_capacity_stops
#print axioms Generative.NativePacketProcess.interface_insufficient_stops
#print axioms Generative.NativePacketProcess.probe_source_stops
#print axioms Generative.NativePacketProcess.probe_receipt_insufficient_stops
#print axioms Generative.NativePacketProcess.probe_final_effects
#print axioms Generative.NativePacketProcess.SameParameters
#print axioms Generative.NativePacketProcess.execute_retains_parameters
#print axioms Generative.NativePacketProcess.completed_retains_parameters
#print axioms Generative.NativePacketProcess.receipt_capacity_unreachable
