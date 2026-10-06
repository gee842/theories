import FormationClosure

/-!
# Acquiring contact, inversion and receipt calibration within the port's history

The formation-closure study left one bridge open: deciding to form needs
knowledge of the contact that a single failed probe cannot give. This module
derives that knowledge from an inquiry the port runs on itself, using only
native operations: a reset, a probe, two rotations and a second probe.

The inquiry reads two retained traces of each probe: its receipt and the change
in the port's own record of transferred material. The record reports actual
arrival directly; the receipt reports arrival through the possibly inverted
receipt path. Comparing the two calibrates the receipt. The pair of recorded
arrivals is exactly the transfer-response profile, so it identifies the A/B/C
class, the contact, and, when the contact is open, the inversion.

What stays hidden is kept as results. A blocked contact hides the inversion,
and receipts alone cannot separate the inversion from receipt inversion.
The inquiry needs an intact reset (`broken = false`), two source packets and
the reserve for five native operations; those are the conditions of the
theorems, not assumed favorable outcomes. Reading the record and comparing
bits is described here, not built as a further mechanism in the port.
-/

namespace Generative.InquirySufficiency.AcquiredContact

open Generative NativePacketProcess PacketLawDerivation OnePacketQuestions
open FormationClosure

theorem reset_shape {s t : NativePacketProcess.State} {o : Observation}
    (actual : execute s .reset = .complete t o) :
    Payable s ∧ t = { debit s with phase := if s.broken then s.phase else .p0 } ∧ o = .silent := by
  unfold execute at actual
  generalize interface : charge s = payment at actual
  cases payment with
  | capacity => cases actual
  | funding => cases actual
  | paid ready =>
    obtain ⟨sustained, rfl⟩ := (charge_paid_iff s ready).mp interface
    cases actual
    exact ⟨sustained, rfl, rfl⟩

theorem a_shape {s t : NativePacketProcess.State} {o : Observation}
    (actual : execute s .a = .complete t o) :
    Payable s ∧ t = { debit s with phase := nextPhase s.phase } ∧ o = .silent := by
  unfold execute at actual
  generalize interface : charge s = payment at actual
  cases payment with
  | capacity => cases actual
  | funding => cases actual
  | paid ready =>
    obtain ⟨sustained, rfl⟩ := (charge_paid_iff s ready).mp interface
    cases actual
    exact ⟨sustained, rfl, rfl⟩

/-- Arrival as the port's own transfer record shows it: the record grew. -/
def recordBit (before after : Nat) : Bool := Nat.blt before after

theorem record_grew (n : Nat) : recordBit n (n + 10) = true := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

theorem record_unchanged (n : Nat) : recordBit n (n + 0) = false := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

theorem record_reads_arrival (n : Nat) (arrived : Bool) :
    recordBit n (n + (if arrived then 10 else 0)) = arrived := by
  cases arrived
  · exact record_unchanged n
  · exact record_grew n

/-- What one completed inquiry leaves: two receipts and two recorded arrivals. -/
structure Reading where
  receipt0 : Bool
  receipt1 : Bool
  arrived0 : Bool
  arrived1 : Bool

/-- The inquiry `reset, probe, a, a, probe` has completed through these states. -/
structure Inquiry (s : NativePacketProcess.State) where
  s1 : NativePacketProcess.State
  s2 : NativePacketProcess.State
  s3 : NativePacketProcess.State
  s4 : NativePacketProcess.State
  s5 : NativePacketProcess.State
  r0 : Bool
  r1 : Bool
  o1 : Observation
  o3 : Observation
  o4 : Observation
  step1 : execute s .reset = .complete s1 o1
  step2 : execute s1 .probe = .complete s2 (.receipt r0)
  step3 : execute s2 .a = .complete s3 o3
  step4 : execute s3 .a = .complete s4 o4
  step5 : execute s4 .probe = .complete s5 (.receipt r1)

def Inquiry.reading {s : NativePacketProcess.State} (q : Inquiry s) : Reading :=
  ⟨q.r0, q.r1, recordBit q.s1.transferred q.s2.transferred,
    recordBit q.s4.transferred q.s5.transferred⟩

def inquiryCommands : List NativePacketProcess.Command := [.reset, .probe, .a, .a, .probe]

/-- A completed inquiry is an actual native history. -/
theorem Inquiry.trace {s : NativePacketProcess.State} (q : Inquiry s) :
    Trace NativePacketProcess.process s inquiryCommands q.s5 :=
  .cons ⟨_, q.step1⟩ (.cons ⟨_, q.step2⟩ (.cons ⟨_, q.step3⟩ (.cons ⟨_, q.step4⟩
    (.cons ⟨_, q.step5⟩ (.nil _)))))

/-- Exactly what an inquiry from an intact port reveals. -/
theorem inquiry_reveals {s : NativePacketProcess.State} (q : Inquiry s) (intact : s.broken = false) :
    q.reading.arrived0 = arrivalAt false s.tau s.blocked ∧
      q.reading.arrived1 = arrivalAt true s.tau s.blocked ∧
      q.reading.receipt0 = (arrivalAt false s.tau s.blocked != s.receiptFlip) ∧
      q.reading.receipt1 = (arrivalAt true s.tau s.blocked != s.receiptFlip) ∧
      q.s5.tau = s.tau ∧ q.s5.blocked = s.blocked ∧ q.s5.receiptFlip = s.receiptFlip := by
  obtain ⟨s1, s2, s3, s4, s5, r0, r1, o1, o3, o4, h1, h2, h3, h4, h5⟩ := q
  obtain ⟨_, rfl, rfl⟩ := reset_shape h1
  obtain ⟨_, rfl, e2⟩ := (probe_complete_iff _ _ _).mp h2
  obtain ⟨_, rfl, rfl⟩ := a_shape h3
  obtain ⟨_, rfl, rfl⟩ := a_shape h4
  obtain ⟨_, rfl, e5⟩ := (probe_complete_iff _ _ _).mp h5
  cases e2
  cases e5
  cases s with
  | mk phase tau sigma broken blocked flip source reserve live workspace capacity drawn
      credit transferred wasted =>
    subst intact
    refine ⟨?_, ?_, ?_, ?_, rfl, rfl, rfl⟩
    · exact record_reads_arrival transferred (arrivalAt false tau blocked)
    · exact record_reads_arrival (transferred + if arrivalAt false tau blocked then 10 else 0)
        (arrivalAt true tau blocked)
    · rfl
    · rfl

/-- The recorded arrivals are exactly the transfer-response profile. -/
theorem inquiry_reads_profile {s : NativePacketProcess.State} (q : Inquiry s)
    (intact : s.broken = false) :
    (q.reading.arrived0, q.reading.arrived1) = profile s.tau s.blocked := by
  obtain ⟨a0, a1, _⟩ := inquiry_reveals q intact
  rw [a0, a1]
  rfl

/-- Receipt calibration acquired from the port's own record: each receipt
differs from the recorded arrival exactly by the receipt inversion. -/
theorem inquiry_calibrates_receipt {s : NativePacketProcess.State} (q : Inquiry s)
    (intact : s.broken = false) :
    (q.reading.receipt0 != q.reading.arrived0) = s.receiptFlip ∧
      (q.reading.receipt1 != q.reading.arrived1) = s.receiptFlip := by
  obtain ⟨a0, a1, r0, r1, _⟩ := inquiry_reveals q intact
  rw [a0, a1, r0, r1]
  constructor <;> cases arrivalAt _ s.tau s.blocked <;> cases s.receiptFlip <;> rfl

/-- Two inquiries agree on recorded arrivals exactly when their ports are in the same class. -/
theorem inquiry_identifies_class {s t : NativePacketProcess.State} (q : Inquiry s) (p : Inquiry t)
    (intactS : s.broken = false) (intactT : t.broken = false) :
    (q.reading.arrived0, q.reading.arrived1) = (p.reading.arrived0, p.reading.arrived1) ↔
      targetOf s.tau s.blocked = targetOf t.tau t.blocked := by
  rw [inquiry_reads_profile q intactS, inquiry_reads_profile p intactT]
  exact profile_equal_iff_target_equal _ _ _ _

/-- Decide to form exactly when neither output arrived. -/
def formDecision (r : Reading) : Bool := !r.arrived0 && !r.arrived1

/-- The decision is sound and complete: it forms exactly when the contact is blocked. -/
theorem decision_identifies_contact {s : NativePacketProcess.State} (q : Inquiry s)
    (intact : s.broken = false) : formDecision q.reading = s.blocked := by
  obtain ⟨a0, a1, _⟩ := inquiry_reveals q intact
  unfold formDecision
  rw [a0, a1]
  cases s.tau <;> cases s.blocked <;> rfl

/-- With an open contact the first recorded arrival is the inversion itself. -/
theorem open_inquiry_reveals_inversion {s : NativePacketProcess.State} (q : Inquiry s)
    (intact : s.broken = false) (opened : s.blocked = false) :
    q.reading.arrived0 = s.tau ∧ q.reading.arrived1 = !s.tau := by
  obtain ⟨a0, a1, _⟩ := inquiry_reveals q intact
  rw [a0, a1, opened]
  cases s.tau <;> exact ⟨rfl, rfl⟩

/-- A blocked contact hides the inversion: both inversions give the same reading. -/
theorem blocked_hides_inversion {s t : NativePacketProcess.State} (q : Inquiry s) (p : Inquiry t)
    (intactS : s.broken = false) (intactT : t.broken = false)
    (blockedS : s.blocked = true) (blockedT : t.blocked = true)
    (sameFlip : s.receiptFlip = t.receiptFlip) :
    q.reading = p.reading := by
  obtain ⟨a0, a1, r0, r1, _⟩ := inquiry_reveals q intactS
  obtain ⟨b0, b1, c0, c1, _⟩ := inquiry_reveals p intactT
  have same : ∀ x, arrivalAt x s.tau s.blocked = arrivalAt x t.tau t.blocked := by
    intro x
    rw [blockedS, blockedT]
    cases x <;> cases s.tau <;> cases t.tau <;> rfl
  cases hq : q.reading
  cases hp : p.reading
  rw [hq] at a0 a1 r0 r1
  rw [hp] at b0 b1 c0 c1
  simp only at a0 a1 r0 r1 b0 b1 c0 c1
  rw [a0, a1, r0, r1, b0, b1, c0, c1, same false, same true, sameFlip]

/-- Receipts alone cannot separate inversion from receipt inversion: flipping
both leaves both receipts unchanged on an open contact. -/
theorem receipts_confound_inversions (tau flip x : Bool) :
    (arrivalAt x tau false != flip) = (arrivalAt x (!tau) false != !flip) := by
  cases tau <;> cases flip <;> cases x <;> rfl

/-- Two packets and an intact reset are needed: an exhausted or single-packet
port cannot complete the inquiry. -/
theorem inquiry_needs_two_packets {s : NativePacketProcess.State} (q : Inquiry s) :
    20 ≤ s.source := by
  obtain ⟨s1, s2, s3, s4, s5, r0, r1, o1, o3, o4, h1, h2, h3, h4, h5⟩ := q
  obtain ⟨_, rfl, _⟩ := reset_shape h1
  obtain ⟨ready2, rfl, _⟩ := (probe_complete_iff _ _ _).mp h2
  obtain ⟨_, rfl, _⟩ := a_shape h3
  obtain ⟨_, rfl, _⟩ := a_shape h4
  obtain ⟨ready5, rfl, _⟩ := (probe_complete_iff _ _ _).mp h5
  have first := ready2.2.1
  have second := ready5.2.1
  change 10 ≤ s.source at first
  change 10 ≤ s.source - 10 at second
  exact sum_le_from_remainder 10 10 s.source first second

/-- The whole acquired loop as one executed history. -/
def nativeRun (commands : List NativePacketProcess.Command) : List Event :=
  commands.map nativeE

/-- Inquire, recover the wasted transfers, form, and inquire again. -/
def acquiredHistory : List Event :=
  nativeRun inquiryCommands ++ [recoverE, formE] ++ nativeRun inquiryCommands

/-- A blocked port with no spares, two inquiries' worth of source and an empty record. -/
def acquiredStart : Port :=
  ⟨{ phase := .p1, tau := true, sigma := false, broken := false, blocked := true,
     receiptFlip := true, source := 40, fuel := 400000, live := 0, workspace := 0,
     capacity := 10, spent := 0, income := 0, transferred := 0, wasted := 0 }, 0, 0⟩

/-- The executed loop: the first inquiry finds no arrival (decision: form), the
waste of its two failed probes is recovered into a pair, the contact is formed,
and the second inquiry records one arrival, revealing the inversion. -/
theorem acquired_loop :
    ∃ y, run acquiredStart acquiredHistory = some y ∧
      Trace FormationClosure.process acquiredStart acquiredHistory y ∧
      targetOf acquiredStart.native.tau acquiredStart.native.blocked = .C ∧
      targetOf y.native.tau y.native.blocked = .B ∧
      y.native.transferred = 10 ∧ y.native.wasted = 30 ∧ y.native.source = 0 ∧
      y.spare = 0 ∧ y.recovered = 1 := by
  exact ⟨_, rfl, run_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- From this start, any completed inquiry decides to form. -/
theorem acquired_start_decides_to_form (q : Inquiry acquiredStart.native) :
    formDecision q.reading = true :=
  decision_identifies_contact q rfl

end Generative.InquirySufficiency.AcquiredContact

#print axioms Generative.InquirySufficiency.AcquiredContact.reset_shape
#print axioms Generative.InquirySufficiency.AcquiredContact.a_shape
#print axioms Generative.InquirySufficiency.AcquiredContact.recordBit
#print axioms Generative.InquirySufficiency.AcquiredContact.record_grew
#print axioms Generative.InquirySufficiency.AcquiredContact.record_unchanged
#print axioms Generative.InquirySufficiency.AcquiredContact.record_reads_arrival
#print axioms Generative.InquirySufficiency.AcquiredContact.Reading
#print axioms Generative.InquirySufficiency.AcquiredContact.Inquiry
#print axioms Generative.InquirySufficiency.AcquiredContact.Inquiry.reading
#print axioms Generative.InquirySufficiency.AcquiredContact.inquiryCommands
#print axioms Generative.InquirySufficiency.AcquiredContact.Inquiry.trace
#print axioms Generative.InquirySufficiency.AcquiredContact.inquiry_reveals
#print axioms Generative.InquirySufficiency.AcquiredContact.inquiry_reads_profile
#print axioms Generative.InquirySufficiency.AcquiredContact.inquiry_calibrates_receipt
#print axioms Generative.InquirySufficiency.AcquiredContact.inquiry_identifies_class
#print axioms Generative.InquirySufficiency.AcquiredContact.formDecision
#print axioms Generative.InquirySufficiency.AcquiredContact.decision_identifies_contact
#print axioms Generative.InquirySufficiency.AcquiredContact.open_inquiry_reveals_inversion
#print axioms Generative.InquirySufficiency.AcquiredContact.blocked_hides_inversion
#print axioms Generative.InquirySufficiency.AcquiredContact.receipts_confound_inversions
#print axioms Generative.InquirySufficiency.AcquiredContact.inquiry_needs_two_packets
#print axioms Generative.InquirySufficiency.AcquiredContact.nativeRun
#print axioms Generative.InquirySufficiency.AcquiredContact.acquiredHistory
#print axioms Generative.InquirySufficiency.AcquiredContact.acquiredStart
#print axioms Generative.InquirySufficiency.AcquiredContact.acquired_loop
#print axioms Generative.InquirySufficiency.AcquiredContact.acquired_start_decides_to_form
