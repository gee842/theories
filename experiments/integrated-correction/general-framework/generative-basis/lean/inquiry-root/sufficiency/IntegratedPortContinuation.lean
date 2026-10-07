import PhaseRecoveredContact
import WholePortContinuation
import PortRenewalBoundary
import ActualRecovery

/-!
# Inquiry, support and retained contact history on one actual run

The reset-free inquiry's executed trace, the whole-port support law and the
naturalism study's actual-history profile can describe one and the same run.
The profile here follows whether contact is open. This is a coordinate of the
native process; it is not a claim that every open contact is useful or good.

The contact only stays fixed or opens in this law. A false-to-true profile entry
therefore need not restore a previously lost contact. The observation occasions
are completed native/extended edges; stopped attempts and elapsed time are not
represented by this profile.

The common-history interface does not select an ethical order. In particular,
finite source, an open contact, and adequate normative grounds remain distinct
questions within the unfolding represented here.
-/

namespace Generative.InquirySufficiency.IntegratedPortContinuation

open Generative Naturalism
open FormationClosure PhaseRecoveredContact WholePortContinuation

universe u v

/-- Existence in Prop suffices: no choice of hidden intermediate states is added. -/
theorem trace_has_actual_run {S : Type u} {A : Type v} {P : Process S A}
    {s t : S} {word : List A} (history : Trace P s word t) :
    ∃ r : Run P s t, r.word = word := by
  induction history with
  | nil s => exact ⟨.nil s, rfl⟩
  | @cons s m t a rest step _ ih =>
    obtain ⟨r, hr⟩ := ih
    exact ⟨.cons a step r, congrArg (List.cons a) hr⟩

def contactOpen (x : Port) : Bool := !x.native.blocked

/-- Conservation, a finite-source bound and the actual contact-profile balance refer
to exactly the same intermediate-state history. -/
theorem one_history_support_and_contact_profile {x y : Port}
    (r : Run FormationClosure.process x y) :
    y.native.held + (y.native.enacted - x.native.enacted) =
        x.native.held + (y.native.arrived - x.native.arrived) ∧
    r.word.length + NativePortContinuation.potential y.native ≤
        NativePortContinuation.potential x.native ∧
    ActualRecovery.losses contactOpen r + ActualRecovery.present (contactOpen y) =
        ActualRecovery.recoveries contactOpen r + ActualRecovery.present (contactOpen x) :=
  ⟨continues_exact (extended_trace_continues r.toTrace),
    extended_history_length r.toTrace, ActualRecovery.actual_balance contactOpen r⟩

/-- Appending later activity cannot delete earlier unavailable
contact occasions from this actual-history profile. No ethical weight is asserted. -/
theorem port_continuation_retains_interruption {x y z : Port}
    (r : Run FormationClosure.process x y) (later : Run FormationClosure.process y z) :
    ActualRecovery.interruptions contactOpen r ≤
      ActualRecovery.interruptions contactOpen (r.append later) :=
  ActualRecovery.continuation_keeps_interruption contactOpen r later

/-- The acquired phase inquiry has an actual run with its computed command word
and the native conservation relation, without a functioning-reset premise. -/
theorem acquired_inquiry_has_supported_run {s : NativePacketProcess.State}
    (q : RecoveredInquiry s) :
    ∃ r : Run NativePacketProcess.process s q.s4,
      r.word = recoveredCommands q ∧
      NativePortContinuation.Continues s q.s4 := by
  obtain ⟨r, word⟩ := trace_has_actual_run (recovered_trace q)
  exact ⟨r, word, NativePortContinuation.trace_continues r.toTrace⟩

/-- The adaptive inquiry/formation loop is one actual run carrying all three
interfaces. This joins existing conclusions without postulating a second history. -/
theorem acquired_loop_has_one_supported_history {x : Port} (q : RecoveredLoop x) :
    ∃ r : Run FormationClosure.process x (loopEnd q),
      r.word = loopEvents q ∧
      (loopEnd q).native.blocked = false ∧
      (loopEnd q).native.held + ((loopEnd q).native.enacted - x.native.enacted) =
          x.native.held + ((loopEnd q).native.arrived - x.native.arrived) ∧
      r.word.length + NativePortContinuation.potential (loopEnd q).native ≤
          NativePortContinuation.potential x.native ∧
      ActualRecovery.losses contactOpen r + ActualRecovery.present (contactOpen (loopEnd q)) =
          ActualRecovery.recoveries contactOpen r + ActualRecovery.present (contactOpen x) := by
  obtain ⟨r, word⟩ := trace_has_actual_run (recovered_loop_trace q)
  exact ⟨r, word, (acquired_reset_free_loop q).1, one_history_support_and_contact_profile r⟩

#print axioms Generative.InquirySufficiency.IntegratedPortContinuation.trace_has_actual_run
#print axioms Generative.InquirySufficiency.IntegratedPortContinuation.contactOpen
#print axioms Generative.InquirySufficiency.IntegratedPortContinuation.one_history_support_and_contact_profile
#print axioms Generative.InquirySufficiency.IntegratedPortContinuation.port_continuation_retains_interruption
#print axioms Generative.InquirySufficiency.IntegratedPortContinuation.acquired_inquiry_has_supported_run
#print axioms Generative.InquirySufficiency.IntegratedPortContinuation.acquired_loop_has_one_supported_history

end Generative.InquirySufficiency.IntegratedPortContinuation
