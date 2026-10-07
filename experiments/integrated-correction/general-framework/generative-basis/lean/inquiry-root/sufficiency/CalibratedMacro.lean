import AcquiredContact

/-!
# The macro probe law without a calibration premise

`PacketLawDerivation.aligned_probe_realizes_macro` derives the one-packet probe
law from native execution under the hypothesis `receiptFlip = false`: the
receipt path is assumed calibrated. `AcquiredContact.inquiry_calibrates_receipt`
shows that an inquiry the port runs on itself acquires the receipt inversion
from its own record of transferred material.

This module composes the two. For every receipt inversion, the receipt corrected
by the inversion the inquiry acquired reports the macro observation exactly. The
calibration hypothesis is removed: it is replaced by an inquiry on the same port,
whose existence and completion are themselves native activity.

Still required: the inquiry needs an intact reset and two packets, as
`AcquiredContact` proves; the probe itself needs one packet and the alignment
guard. "Same port" is stated as equality of the receipt inversion; native
execution never changes it (`execute_retains_parameters`).
-/

namespace Generative.InquirySufficiency.CalibratedMacro

open Generative NativePacketProcess PacketLawDerivation OnePacketQuestions
open AcquiredContact

/-- Correcting a receipt by the actual inversion recovers the arrival, and the
arrival is the macro receipt. No calibration premise. -/
theorem corrected_receipt_matches_macro (s : Native) :
    report (receiptBit s != s.receiptFlip) =
      receipt (start (targetOf s.tau s.blocked)) (test (output s.phase)) := by
  have recovered : (receiptBit s != s.receiptFlip) = arrival s := by
    unfold receiptBit
    cases arrival s <;> cases s.receiptFlip <;> rfl
  rw [recovered]
  exact native_gate_is_macro_receipt s.tau s.blocked (output s.phase)

/-- The inversion an inquiry acquires is the port's actual receipt inversion. -/
theorem acquired_inversion {u : Native} (q : Inquiry u) (intact : u.broken = false) :
    (q.reading.receipt0 != q.reading.arrived0) = u.receiptFlip :=
  (inquiry_calibrates_receipt q intact).1

/-- A completed one-packet probe projects onto the macro step, and its receipt,
corrected by the actual inversion, is the macro observation. -/
theorem completed_probe_projects_corrected (s t : Native) (bit : Bool)
    (source : s.source = 10)
    (completed : execute s .probe = .complete t (.receipt bit)) :
    ProbeReady s ∧
      OnePacketQuestions.process.step (onePacketProjection s) (test (output s.phase))
        (onePacketProjection t) ∧
      report (bit != s.receiptFlip) =
        sense (onePacketProjection s) (test (output s.phase)) (onePacketProjection t) ∧
      t.source = 0 ∧ targetOf t.tau t.blocked = targetOf s.tau s.blocked := by
  obtain ⟨ready, endpoint, observation⟩ := (probe_complete_iff s t (.receipt bit)).mp completed
  subst t
  have bitEq : bit = receiptBit s := Observation.receipt.inj observation
  have exhausted : (probeFinal s).source = 0 := by
    change s.source - 10 = 0
    rw [source]
  refine ⟨ready, ?_, ?_, exhausted, rfl⟩
  · rw [projection_at_one_packet s source, projection_at_exhaustion (probeFinal s) exhausted]
    change spent (targetOf s.tau s.blocked) =
      advance (start (targetOf s.tau s.blocked)) (test (output s.phase))
    cases output s.phase <;> rfl
  · rw [bitEq, projection_at_one_packet s source]
    exact corrected_receipt_matches_macro s

/-- The aligned macro probe law for every receipt inversion. The receipt is
corrected by the inversion acquired from an inquiry on the same port; no
`receiptFlip = false` hypothesis is used. -/
theorem acquired_calibration_realizes_macro (desired : Bool) (s : Native)
    (source : s.source = 10) (guard : AlignmentGuard desired s)
    {u : Native} (q : Inquiry u) (intact : u.broken = false)
    (samePort : u.receiptFlip = s.receiptFlip) :
    let prepared := alignedState desired s
    let final := probeFinal prepared
    let acquired := q.reading.receipt0 != q.reading.arrived0
    Generative.Trace NativePacketProcess.process s (alignedEvents desired s) final ∧
      execute prepared .probe = .complete final (.receipt (receiptBit prepared)) ∧
      OnePacketQuestions.process.step (onePacketProjection s) (test desired)
        (onePacketProjection final) ∧
      report (receiptBit prepared != acquired) =
        sense (onePacketProjection s) (test desired) (onePacketProjection final) ∧
      final.source = 0 ∧ targetOf final.tau final.blocked = targetOf s.tau s.blocked := by
  obtain ⟨rotationsReady, probeReady⟩ := alignment_guard_supplies_native_guards desired s guard
  have properties := aligned_state_properties desired s
  have actual := probe_complete (alignedState desired s) probeReady
  have projected := completed_probe_projects_corrected (alignedState desired s) _ _
    (properties.2.2.1.trans source) actual
  have nativeTrace : Generative.Trace NativePacketProcess.process s (alignedEvents desired s)
      (probeFinal (alignedState desired s)) := by
    apply Generative.trace_append_iff.mpr
    exact ⟨alignedState desired s,
      rotations_have_native_trace _ s rotationsReady,
      .cons ⟨_, actual⟩ (.nil _)⟩
  have acquiredEq : (q.reading.receipt0 != q.reading.arrived0) =
      (alignedState desired s).receiptFlip :=
    (acquired_inversion q intact).trans (samePort.trans properties.2.2.2.1.symm)
  refine ⟨nativeTrace, actual, ?_, ?_, projected.2.2.2.1,
    projected.2.2.2.2.trans properties.2.2.2.2⟩
  · rw [properties.1, properties.2.1] at projected
    exact projected.2.1
  · show report (receiptBit (alignedState desired s) != (q.reading.receipt0 != q.reading.arrived0)) = _
    rw [acquiredEq]
    rw [properties.1, properties.2.1] at projected
    exact projected.2.2.1

#print axioms Generative.InquirySufficiency.CalibratedMacro.corrected_receipt_matches_macro
#print axioms Generative.InquirySufficiency.CalibratedMacro.acquired_inversion
#print axioms Generative.InquirySufficiency.CalibratedMacro.completed_probe_projects_corrected
#print axioms Generative.InquirySufficiency.CalibratedMacro.acquired_calibration_realizes_macro

end Generative.InquirySufficiency.CalibratedMacro
