import AcquiredContact
import PhaseCycleDerivation

/-!
# Phase recovery followed by contact inquiry and formation, without reset

The selected native law remains explicit. Three actual sensor readings,
interleaved with advances, determine the present phase despite unknown reading
inversion. Only those readings choose the alignment commands. Two probes then
read both transfer outcomes and calibrate the receipt. Neither an intact reset
nor phase, transfer inversion, or receipt calibration is an input to the policy.
The retained output table and the comparison/decoder mechanism remain supplied.
-/

namespace Generative.InquirySufficiency.PhaseRecoveredContact

open Generative NativePacketProcess PacketLawDerivation AcquiredContact FormationClosure

/-- A completed sensor command leaves its actual reading. -/
theorem read_shape {s t : NativePacketProcess.State} {r : Bool}
    (actual : execute s .read = .complete t (.reading r)) :
    Supportable s ∧ t = enact s ∧ r = readBit s := by
  unfold execute at actual
  generalize interface : support s = outcome at actual
  cases outcome with
  | capacity => cases actual
  | insufficient => cases actual
  | sustained ready =>
    obtain ⟨supported, rfl⟩ := (support_sustained_iff s ready).mp interface
    cases actual
    exact ⟨supported, rfl, rfl⟩

structure ProfileRun (s : NativePacketProcess.State) where
  s1 : NativePacketProcess.State
  s2 : NativePacketProcess.State
  s3 : NativePacketProcess.State
  s4 : NativePacketProcess.State
  s5 : NativePacketProcess.State
  r0 : Bool
  r1 : Bool
  r2 : Bool
  o2 : Observation
  o4 : Observation
  h1 : execute s .read = .complete s1 (.reading r0)
  h2 : execute s1 .a = .complete s2 o2
  h3 : execute s2 .read = .complete s3 (.reading r1)
  h4 : execute s3 .a = .complete s4 o4
  h5 : execute s4 .read = .complete s5 (.reading r2)

/-- Decodes the phase at the final reading, using equality of the bits only. -/
def decodedPhase (r0 r1 r2 : Bool) : Phase :=
  if r0 == r1 then .p2 else if r0 == r2 then .p0 else .p1

theorem decoded_native_profile (phase : Phase) (tau sigma : Bool) :
    decodedPhase ((output phase != tau) != sigma)
      ((output (nextPhase phase) != tau) != sigma)
      ((output (nextPhase (nextPhase phase)) != tau) != sigma) = nextPhase (nextPhase phase) := by
  cases phase <;> cases tau <;> cases sigma <;> rfl

def profileCommands : List NativePacketProcess.Command := [.read, .a, .read, .a, .read]

theorem profile_trace {s : NativePacketProcess.State} (q : ProfileRun s) :
    Trace NativePacketProcess.process s profileCommands q.s5 :=
  .cons ⟨_, q.h1⟩ (.cons ⟨_, q.h2⟩ (.cons ⟨_, q.h3⟩ (.cons ⟨_, q.h4⟩
    (.cons ⟨_, q.h5⟩ (.nil _)))))

/-- The decoded phase is acquired from the executed readings for every phase,
transfer inversion, sensor inversion and reset condition. -/
theorem profile_recovers_phase {s : NativePacketProcess.State} (q : ProfileRun s) :
    decodedPhase q.r0 q.r1 q.r2 = q.s5.phase ∧ q.s5.tau = s.tau ∧
      q.s5.blocked = s.blocked ∧ q.s5.receiptFlip = s.receiptFlip := by
  obtain ⟨s1,s2,s3,s4,s5,r0,r1,r2,o2,o4,h1,h2,h3,h4,h5⟩ := q
  obtain ⟨_, rfl, rfl⟩ := read_shape h1
  obtain ⟨_, rfl, rfl⟩ := a_shape h2
  obtain ⟨_, rfl, rfl⟩ := read_shape h3
  obtain ⟨_, rfl, rfl⟩ := a_shape h4
  obtain ⟨_, rfl, rfl⟩ := read_shape h5
  refine ⟨?_, rfl, rfl, rfl⟩
  exact decoded_native_profile s.phase s.tau s.sigma

/-- Advance count to the named zero phase after decoding. -/
def toZero : Phase → Nat
  | .p0 => 0
  | .p1 => 2
  | .p2 => 1

theorem toZero_correct (phase : Phase) : phaseAfter (toZero phase) phase = .p0 := by
  cases phase <;> rfl

def profileAligned {s : NativePacketProcess.State} (q : ProfileRun s) : NativePacketProcess.State :=
  rotations (toZero (decodedPhase q.r0 q.r1 q.r2)) q.s5

theorem profile_aligned {s : NativePacketProcess.State} (q : ProfileRun s) :
    (profileAligned q).phase = .p0 ∧ (profileAligned q).tau = s.tau ∧
      (profileAligned q).blocked = s.blocked ∧ (profileAligned q).receiptFlip = s.receiptFlip := by
  obtain ⟨phase, tau, blocked, flip⟩ := profile_recovers_phase q
  have fields := rotation_fields (toZero (decodedPhase q.r0 q.r1 q.r2)) q.s5
  refine ⟨?_, fields.2.1.trans tau, fields.2.2.1.trans blocked, fields.2.2.2.1.trans flip⟩
  change (rotations _ q.s5).phase = .p0
  rw [fields.1, phase]
  exact toZero_correct _

/-- Readings, their computed alignment, then probes at the two output values. -/
structure RecoveredInquiry (s : NativePacketProcess.State) where
  observed : ProfileRun s
  alignmentReady : RotationsReady (toZero (decodedPhase observed.r0 observed.r1 observed.r2)) observed.s5
  s1 : NativePacketProcess.State
  s2 : NativePacketProcess.State
  s3 : NativePacketProcess.State
  s4 : NativePacketProcess.State
  r0 : Bool
  r1 : Bool
  o2 : Observation
  o3 : Observation
  h1 : execute (profileAligned observed) .probe = .complete s1 (.receipt r0)
  h2 : execute s1 .a = .complete s2 o2
  h3 : execute s2 .a = .complete s3 o3
  h4 : execute s3 .probe = .complete s4 (.receipt r1)

def recoveredReading {s : NativePacketProcess.State} (q : RecoveredInquiry s) : Reading :=
  ⟨q.r0, q.r1, recordBit (profileAligned q.observed).transferred q.s1.transferred,
    recordBit q.s3.transferred q.s4.transferred⟩

def recoveredCommands {s : NativePacketProcess.State} (q : RecoveredInquiry s) :
    List NativePacketProcess.Command :=
  profileCommands ++ rotationEvents (toZero (decodedPhase q.observed.r0 q.observed.r1 q.observed.r2)) ++
    [.probe, .a, .a, .probe]

theorem recovered_trace {s : NativePacketProcess.State} (q : RecoveredInquiry s) :
    Trace NativePacketProcess.process s (recoveredCommands q) q.s4 := by
  apply trace_append_iff.mpr
  refine ⟨profileAligned q.observed, ?_, ?_⟩
  · exact trace_append_iff.mpr ⟨q.observed.s5, profile_trace q.observed,
      rotations_have_native_trace _ _ q.alignmentReady⟩
  · exact .cons ⟨_, q.h1⟩ (.cons ⟨_, q.h2⟩ (.cons ⟨_, q.h3⟩
      (.cons ⟨_, q.h4⟩ (.nil _))))

/-- The two probes record the two outputs once actual alignment is established. -/
theorem two_probe_reveals {s s1 s2 s3 s4 : NativePacketProcess.State}
    {r0 r1 : Bool} {o2 o3 : Observation}
    (h1 : execute s .probe = .complete s1 (.receipt r0))
    (h2 : execute s1 .a = .complete s2 o2)
    (h3 : execute s2 .a = .complete s3 o3)
    (h4 : execute s3 .probe = .complete s4 (.receipt r1)) (phase : s.phase = .p0) :
    recordBit s.transferred s1.transferred = arrivalAt false s.tau s.blocked ∧
      recordBit s3.transferred s4.transferred = arrivalAt true s.tau s.blocked ∧
      r0 = (arrivalAt false s.tau s.blocked != s.receiptFlip) ∧
      r1 = (arrivalAt true s.tau s.blocked != s.receiptFlip) ∧
      s4.tau = s.tau ∧ s4.blocked = s.blocked ∧ s4.receiptFlip = s.receiptFlip := by
  obtain ⟨_, rfl, e1⟩ := (probe_complete_iff _ _ _).mp h1
  obtain ⟨_, rfl, rfl⟩ := a_shape h2
  obtain ⟨_, rfl, rfl⟩ := a_shape h3
  obtain ⟨_, rfl, e4⟩ := (probe_complete_iff _ _ _).mp h4
  cases e1
  cases e4
  cases s with
  | mk phase tau sigma broken blocked flip source held live workspace capacity enacted arrived transferred dissipated =>
    subst phase
    refine ⟨?_,?_,rfl,rfl,rfl,rfl,rfl⟩
    · exact record_reads_arrival transferred (arrivalAt false tau blocked)
    · exact record_reads_arrival (transferred + if arrivalAt false tau blocked then 10 else 0)
        (arrivalAt true tau blocked)

/-- Reveals the same transfer profile as the old reset-based inquiry, with no
assumption that reset works and no given phase or inversion. -/
theorem reset_free_inquiry_reveals {s : NativePacketProcess.State} (q : RecoveredInquiry s) :
    (recoveredReading q).arrived0 = arrivalAt false s.tau s.blocked ∧
      (recoveredReading q).arrived1 = arrivalAt true s.tau s.blocked ∧
      (recoveredReading q).receipt0 = (arrivalAt false s.tau s.blocked != s.receiptFlip) ∧
      (recoveredReading q).receipt1 = (arrivalAt true s.tau s.blocked != s.receiptFlip) ∧
      q.s4.tau = s.tau ∧ q.s4.blocked = s.blocked ∧ q.s4.receiptFlip = s.receiptFlip := by
  have aligned := profile_aligned q.observed
  have revealed := two_probe_reveals q.h1 q.h2 q.h3 q.h4 aligned.1
  rw [aligned.2.1, aligned.2.2.1, aligned.2.2.2] at revealed
  exact revealed

theorem reset_free_decision_identifies_contact {s : NativePacketProcess.State} (q : RecoveredInquiry s) :
    formDecision (recoveredReading q) = s.blocked := by
  obtain ⟨a0,a1,_⟩ := reset_free_inquiry_reveals q
  unfold formDecision
  rw [a0,a1]
  cases s.tau <;> cases s.blocked <;> rfl

theorem reset_free_receipt_calibration {s : NativePacketProcess.State} (q : RecoveredInquiry s) :
    ((recoveredReading q).receipt0 != (recoveredReading q).arrived0) = s.receiptFlip ∧
      ((recoveredReading q).receipt1 != (recoveredReading q).arrived1) = s.receiptFlip := by
  obtain ⟨a0,a1,r0,r1,_⟩ := reset_free_inquiry_reveals q
  rw [a0,a1,r0,r1]
  constructor <;> cases arrivalAt _ s.tau s.blocked <;> cases s.receiptFlip <;> rfl

theorem reset_free_open_reveals_inversion {s : NativePacketProcess.State} (q : RecoveredInquiry s)
    (opened : s.blocked = false) :
    (recoveredReading q).arrived0 = s.tau ∧ (recoveredReading q).arrived1 = !s.tau := by
  obtain ⟨a0,a1,_⟩ := reset_free_inquiry_reveals q
  rw [a0,a1,opened]
  cases s.tau <;> exact ⟨rfl,rfl⟩

/-- The old information limit persists: a blocked contact hides transfer inversion. -/
theorem reset_free_blocked_hides_inversion {s : NativePacketProcess.State} (q : RecoveredInquiry s)
    (blocked : s.blocked = true) :
    (recoveredReading q).arrived0 = false ∧ (recoveredReading q).arrived1 = false := by
  obtain ⟨a0,a1,_⟩ := reset_free_inquiry_reveals q
  rw [a0,a1,blocked]
  cases s.tau <;> exact ⟨rfl,rfl⟩

/-- Native control, returning only completed commands with their witnesses. -/
def controlOf (s : NativePacketProcess.State) (command : NativePacketProcess.Command) :
    (r : Result) → execute s command = r → Option (Σ' t o, execute s command = .complete t o)
  | .complete t o, h => some ⟨t,o,h⟩
  | .stopped _ _, _ => none

def controlStep (s : NativePacketProcess.State) (command : NativePacketProcess.Command) :
    Option (Σ' t o, execute s command = .complete t o) :=
  controlOf s command (execute s command) rfl

def probeOf (s : NativePacketProcess.State) :
    (r : Result) → execute s .probe = r → Option (Σ' t r, execute s .probe = .complete t (.receipt r))
  | .complete t (.receipt r), h => some ⟨t,r,h⟩
  | .complete _ .silent, _ => none
  | .complete _ (.reading _), _ => none
  | .stopped _ _, _ => none

def probeStep (s : NativePacketProcess.State) :
    Option (Σ' t r, execute s .probe = .complete t (.receipt r)) :=
  probeOf s (execute s .probe) rfl

/-- A reading call retaining its certificate of actual completion. -/
def sensorOf (s : NativePacketProcess.State) :
    (r : Result) → execute s .read = r → Option (Σ' t r, execute s .read = .complete t (.reading r))
  | .complete t (.reading r), h => some ⟨t,r,h⟩
  | .complete _ .silent, _ => none
  | .complete _ (.receipt _), _ => none
  | .stopped _ _, _ => none

def sensorStep (s : NativePacketProcess.State) :
    Option (Σ' t r, execute s .read = .complete t (.reading r)) :=
  sensorOf s (execute s .read) rfl

def runProfile (s : NativePacketProcess.State) : Option (ProfileRun s) := do
  let ⟨s1,r0,h1⟩ ← sensorStep s
  let ⟨s2,o2,h2⟩ ← controlStep s1 .a
  let ⟨s3,r1,h3⟩ ← sensorStep s2
  let ⟨s4,o4,h4⟩ ← controlStep s3 .a
  let ⟨s5,r2,h5⟩ ← sensorStep s4
  pure ⟨s1,s2,s3,s4,s5,r0,r1,r2,o2,o4,h1,h2,h3,h4,h5⟩

/-- Tests only the actual support guards of the chosen advances. -/
def checkRotations : (count : Nat) → (s : NativePacketProcess.State) → Option (PLift (RotationsReady count s))
  | 0, _ => some ⟨True.intro⟩
  | count + 1, s =>
    if h : peak s ≤ s.capacity ∧ draw s ≤ s.held then
      match checkRotations count (rotateOnce s) with
      | some ⟨later⟩ => some ⟨⟨h,later⟩⟩
      | none => none
    else none

/-- The executable policy reads, decodes, aligns and probes. It never calls reset. -/
def inquireRecovered (s : NativePacketProcess.State) : Option (RecoveredInquiry s) := do
  let observed ← runProfile s
  let ready ← checkRotations (toZero (decodedPhase observed.r0 observed.r1 observed.r2)) observed.s5
  let ⟨s1,r0,h1⟩ ← probeStep (profileAligned observed)
  let ⟨s2,o2,h2⟩ ← controlStep s1 .a
  let ⟨s3,o3,h3⟩ ← controlStep s2 .a
  let ⟨s4,r1,h4⟩ ← probeStep s3
  pure ⟨observed,ready.down,s1,s2,s3,s4,r0,r1,o2,o3,h1,h2,h3,h4⟩

/-- Carry a native history into the same extended port, retaining spare counts. -/
theorem lift_native_trace (x : Port) {s t : NativePacketProcess.State} {commands : List NativePacketProcess.Command}
    (history : Trace NativePacketProcess.process s commands t) :
    Trace FormationClosure.process ⟨s,x.spare,x.recovered⟩ (nativeRun commands) ⟨t,x.spare,x.recovered⟩ := by
  induction history with
  | nil => exact .nil _
  | @cons s m t command rest step _ ih =>
    have first : FormationClosure.process.step ⟨s,x.spare,x.recovered⟩ (nativeE command)
        ⟨m,x.spare,x.recovered⟩ := ⟨step,rfl,rfl⟩
    exact .cons first ih

def afterInquiry (x : Port) (q : RecoveredInquiry x.native) : Port :=
  ⟨q.s4,x.spare,x.recovered⟩

/-- Only the acquired pair chooses whether recovery and formation occur. -/
def chosenFormation {s : NativePacketProcess.State} (q : RecoveredInquiry s) : List Event :=
  if formDecision (recoveredReading q) then [recoverE,formE] else []

structure RecoveredLoop (x : Port) where
  first : RecoveredInquiry x.native
  middle : Port
  formationRun : run (afterInquiry x first) (chosenFormation first) = some middle
  second : RecoveredInquiry middle.native

def loopEnd {x : Port} (q : RecoveredLoop x) : Port := afterInquiry q.middle q.second

def loopEvents {x : Port} (q : RecoveredLoop x) : List Event :=
  nativeRun (recoveredCommands q.first) ++ chosenFormation q.first ++ nativeRun (recoveredCommands q.second)

/-- The adaptive history is genuinely a trace of FormationClosure.process;
whole-port conservation and depletion results can apply directly. -/
theorem recovered_loop_trace {x : Port} (q : RecoveredLoop x) :
    Trace FormationClosure.process x (loopEvents q) (loopEnd q) := by
  apply trace_append_iff.mpr
  refine ⟨q.middle, ?_, lift_native_trace q.middle (recovered_trace q.second)⟩
  exact trace_append_iff.mpr ⟨afterInquiry x q.first,
    lift_native_trace x (recovered_trace q.first), run_sound q.formationRun⟩

/-- An actual recovery then formation opens the contact and retains inversion. -/
theorem recovery_formation_effects {x y : Port}
    (trace : Trace FormationClosure.process x [recoverE,formE] y) :
    y.native.blocked = false ∧ y.native.tau = x.native.tau := by
  obtain ⟨m, recovery, tail⟩ := trace_cons_iff.mp trace
  have formation := trace_singleton_iff.mp tail
  obtain ⟨_,_,rfl⟩ := (recover_complete_iff x m).mp recovery
  obtain ⟨_,_,rfl⟩ := (formPort_complete_iff _ y).mp formation
  exact ⟨rfl,rfl⟩

/-- Every completed loop ends open, and the second actual inquiry identifies the
original transfer inversion. Recovery and formation occur precisely when the
first recorded pair identifies blockage. -/
theorem acquired_reset_free_loop {x : Port} (q : RecoveredLoop x) :
    (loopEnd q).native.blocked = false ∧
      (recoveredReading q.second).arrived0 = x.native.tau ∧
      (recoveredReading q.second).arrived1 = !x.native.tau ∧
      formDecision (recoveredReading q.first) = x.native.blocked := by
  have first := reset_free_inquiry_reveals q.first
  have decision := reset_free_decision_identifies_contact q.first
  have actual := run_sound q.formationRun
  have mid : q.middle.native.blocked = false ∧ q.middle.native.tau = x.native.tau := by
    unfold chosenFormation at actual
    rw [decision] at actual
    cases blocked : x.native.blocked with
    | false =>
      rw [blocked] at actual
      have same := trace_nil_iff.mp actual
      rw [← same]
      exact ⟨first.2.2.2.2.2.1.trans blocked, first.2.2.2.2.1⟩
    | true =>
      rw [blocked] at actual
      have formed := recovery_formation_effects actual
      exact ⟨formed.1, formed.2.trans first.2.2.2.2.1⟩
  have last := reset_free_inquiry_reveals q.second
  have inversion := reset_free_open_reveals_inversion q.second mid.1
  refine ⟨last.2.2.2.2.2.1.trans mid.1, ?_, ?_, decision⟩
  · exact inversion.1.trans mid.2
  · rw [inversion.2, mid.2]

def runOf (x : Port) (events : List Event) : (outcome : Option Port) → run x events = outcome →
    Option (Σ' y, run x events = some y)
  | some y, h => some ⟨y,h⟩
  | none, _ => none

/-- The loop follows only acquired evidence; no hidden contact or phase chooses
its commands. None reports absence of a completed certificate, not rollback. -/
def runRecoveredLoop (x : Port) : Option (RecoveredLoop x) := do
  let first ← inquireRecovered x.native
  let ⟨middle,formed⟩ ← runOf (afterInquiry x first) (chosenFormation first)
    (run (afterInquiry x first) (chosenFormation first)) rfl
  let second ← inquireRecovered middle.native
  pure ⟨first,middle,formed,second⟩

/-- Same material endowment across every phase, inversion and reset condition. -/
def testStart (phase : Phase) (tau sigma broken blocked flip : Bool) : Port :=
  ⟨{ phase := phase, tau := tau, sigma := sigma, broken := broken, blocked := blocked,
      receiptFlip := flip, source := 40, held := 600000, live := 0, workspace := 0,
      capacity := 10, enacted := 0, arrived := 0, transferred := 0, dissipated := 0 }, 0, 0⟩

/-- All 96 phase/parameter combinations complete; this includes broken reset. -/
theorem all_native_cases_complete (phase : Phase) (tau sigma broken blocked flip : Bool) :
    (runRecoveredLoop (testStart phase tau sigma broken blocked flip)).isSome = true := by
  cases phase <;> cases tau <;> cases sigma <;> cases broken <;> cases blocked <;> cases flip <;> rfl

/-- A concrete initially blocked configuration with a broken reset. -/
def brokenStart : Port := testStart .p1 true false true true true

def brokenLoop : RecoveredLoop brokenStart :=
  (runRecoveredLoop brokenStart).get (all_native_cases_complete .p1 true false true true true)

/-- The old reset failure is overcome by an actual record-driven history. -/
theorem broken_reset_formed_history :
    Trace FormationClosure.process brokenStart (loopEvents brokenLoop) (loopEnd brokenLoop) ∧
      (loopEnd brokenLoop).native.blocked = false ∧
      (recoveredReading brokenLoop.second).arrived0 = true ∧
      (recoveredReading brokenLoop.second).arrived1 = false ∧
      (loopEnd brokenLoop).native.source = 0 ∧
      (loopEnd brokenLoop).native.transferred = 10 ∧
      (loopEnd brokenLoop).native.dissipated = 30 ∧
      (loopEnd brokenLoop).spare = 0 ∧ (loopEnd brokenLoop).recovered = 1 := by
  exact ⟨recovered_loop_trace brokenLoop,rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩

/-- Native lack of sustaining material still prevents a complete inquiry. -/
theorem insufficient_store_no_certificate :
    (inquireRecovered { brokenStart.native with held := 0 }).isNone = true := rfl

/-- Two probes consume two packets even when phase is recovered successfully. -/
theorem single_packet_no_certificate :
    (inquireRecovered { brokenStart.native with source := 10 }).isNone = true := rfl

/-- The first inquiry can complete while the formation loop cannot. -/
theorem two_packets_inquiry_but_no_loop :
    (inquireRecovered { brokenStart.native with source := 20 }).isSome = true ∧
      (runRecoveredLoop { brokenStart with native := { brokenStart.native with source := 20 } }).isNone = true :=
  ⟨rfl,rfl⟩

/-- Exactly the native draw stages of the inquiry: each probe has two. -/
def inquiryStages {s : NativePacketProcess.State} (q : RecoveredInquiry s) : Nat :=
  11 + toZero (decodedPhase q.observed.r0 q.observed.r1 q.observed.r2)

def avoidsReset : NativePacketProcess.Command → Bool
  | .reset => false
  | .a => true
  | .read => true
  | .probe => true

theorem recovered_commands_avoid_reset {s : NativePacketProcess.State} (q : RecoveredInquiry s) :
    (recoveredCommands q).all avoidsReset = true := by
  change (profileCommands ++ rotationEvents (toZero (decodedPhase q.observed.r0 q.observed.r1 q.observed.r2)) ++
    ([.probe,.a,.a,.probe] : List NativePacketProcess.Command)).all avoidsReset = true
  cases h : decodedPhase q.observed.r0 q.observed.r1 q.observed.r2 <;> rfl

/-- A transparent numerical readout for independent reconstruction. -/
def metrics (phase : Phase) (tau sigma broken blocked flip : Bool) : List Nat :=
  match runRecoveredLoop (testStart phase tau sigma broken blocked flip) with
  | none => []
  | some q =>
    [q.first.observed.r0.toNat, q.first.observed.r1.toNat, q.first.observed.r2.toNat,
      toZero (decodedPhase q.first.observed.r0 q.first.observed.r1 q.first.observed.r2),
      (recoveredReading q.first).arrived0.toNat, (recoveredReading q.first).arrived1.toNat,
      (formDecision (recoveredReading q.first)).toNat,
      (recoveredReading q.second).arrived0.toNat, (recoveredReading q.second).arrived1.toNat,
      ((recoveredReading q.first).receipt0 != (recoveredReading q.first).arrived0).toNat,
      (loopEnd q).native.held, (loopEnd q).native.enacted, (loopEnd q).native.arrived,
      (loopEnd q).native.source, (loopEnd q).native.transferred, (loopEnd q).native.dissipated,
      (loopEnd q).spare, (loopEnd q).recovered, (loopEvents q).length]

end Generative.InquirySufficiency.PhaseRecoveredContact

#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.read_shape
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.ProfileRun
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.decodedPhase
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.decoded_native_profile
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.profileCommands
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.profile_trace
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.profile_recovers_phase
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.toZero
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.toZero_correct
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.profileAligned
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.profile_aligned
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.RecoveredInquiry
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.recoveredReading
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.recoveredCommands
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.recovered_trace
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.two_probe_reveals
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.reset_free_inquiry_reveals
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.reset_free_decision_identifies_contact
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.reset_free_receipt_calibration
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.reset_free_open_reveals_inversion
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.reset_free_blocked_hides_inversion
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.controlOf
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.controlStep
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.probeOf
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.probeStep
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.sensorOf
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.sensorStep
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.runProfile
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.checkRotations
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.inquireRecovered
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.lift_native_trace
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.afterInquiry
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.chosenFormation
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.RecoveredLoop
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.loopEnd
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.loopEvents
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.recovered_loop_trace
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.recovery_formation_effects
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.acquired_reset_free_loop
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.runOf
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.runRecoveredLoop
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.testStart
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.all_native_cases_complete
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.brokenStart
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.brokenLoop
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.broken_reset_formed_history
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.insufficient_store_no_certificate
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.single_packet_no_certificate
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.two_packets_inquiry_but_no_loop
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.inquiryStages
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.avoidsReset
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.recovered_commands_avoid_reset
#print axioms Generative.InquirySufficiency.PhaseRecoveredContact.metrics
