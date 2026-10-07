import AcquiredContact
import ClosedLoopValuation

/-!
# The port's formation disposition as a developing valuation

`ValuationDevelopment` states conditional universals for any organization with a
selection law, a retention law and a consequence law (`World`). There the
consequence law is a supplied local model input. This module instantiates that
framework on the native packet port and derives the consequence law from native
execution: what an inquiry records is the port's transfer-response profile
(`AcquiredContact.inquiry_reads_profile`).

The organization's retained condition is the last recorded pair of arrivals. Its
selective disposition is whether to form the contact. Presented conditions are
contact configurations. The disposition is history- and consequence-dependent,
becomes exactly right after one encounter, goes stale once formation changes the
contact, and recovers after the next encounter. Staleness here is the earlier
redundant-formation countercase seen from the side of valuation.

A second result compares two histories from the same blocked port: one revises
its contact on the strength of its own inquiry, the other inquires without
revising. The revising history ends holding far more and with an
actual transfer; the other ends with neither.

"Valuation" keeps the thin functional sense of `ValuationDevelopment`: a
selective disposition, not experience or ethical warrant.
-/

namespace Generative.InquirySufficiency.PortValuation

open Generative NativePacketProcess PacketLawDerivation OnePacketQuestions
open FormationClosure AcquiredContact ValuationDevelopment

/-- Retained: last recorded arrivals. Presented: contact configuration (tau, blocked).
Selected: whether to form. Consequence: recorded arrivals. -/
def portOrg : Org (Option (Bool × Bool)) (Bool × Bool) Bool (Bool × Bool) where
  select m _ := match m with
    | none => false
    | some r => !r.1 && !r.2
  retain _ _ _ c := some c

/-- The consequence law: what an inquiry records in each contact configuration. -/
def portWorld : World (Bool × Bool) Bool (Bool × Bool) := fun x _ => profile x.1 x.2

/-- The consequence law is not supplied: it is what native execution records. -/
theorem world_is_native {s : NativePacketProcess.State} (q : Inquiry s)
    (intact : s.broken = false) (a : Bool) :
    (q.reading.arrived0, q.reading.arrived1) = portWorld (s.tau, s.blocked) a :=
  inquiry_reads_profile q intact

/-- After one encounter the disposition forms exactly when that contact was blocked. -/
theorem disposition_after_encounter (m : Option (Bool × Bool)) (x x' : Bool × Bool) :
    portOrg.select (portOrg.next portWorld m x) x' = x.2 := by
  obtain ⟨tau, blocked⟩ := x
  cases tau <;> cases blocked <;> rfl

/-- The disposition changes with history. -/
theorem port_history_dependent : historyDependent portOrg portWorld :=
  ⟨none, [(false, true)], (false, true), fun same => Bool.noConfusion same⟩

/-- The disposition changes with consequences. -/
theorem port_consequence_dependent : consequenceDependent portOrg :=
  ⟨none, (false, false), false, (false, false), (false, true), fun same => by cases same⟩

/-- Inherited universal U1: a change of disposition requires a retained difference. -/
theorem port_change_needs_retained_difference (m : Option (Bool × Bool))
    (h₁ h₂ : List (Bool × Bool)) (x : Bool × Bool)
    (changed : portOrg.select (portOrg.run portWorld m h₁) x ≠
      portOrg.select (portOrg.run portWorld m h₂) x) :
    portOrg.run portWorld m h₁ ≠ portOrg.run portWorld m h₂ :=
  priority_change_needs_retained_difference portOrg portWorld m h₁ h₂ x changed

/-- After forming, the retained reading is stale: the disposition would form again
on the now open contact, which only draws on what is held. One further encounter with the
open contact restores a correct disposition. -/
theorem disposition_stale_then_recovers (tau : Bool) :
    portOrg.select (portOrg.run portWorld none [(tau, true)]) (tau, false) = true ∧
      portOrg.select (portOrg.run portWorld none [(tau, true), (tau, false)]) (tau, false) = false := by
  cases tau <;> exact ⟨rfl, rfl⟩

/-- Inquire twice without revising the contact. -/
def unrevisedHistory : List Event := nativeRun inquiryCommands ++ nativeRun inquiryCommands

/-- From the same blocked start, the history that revises its contact on the
strength of its own inquiry ends holding more and with an actual
transfer; the history that only inquires ends with neither and stays class C. -/
theorem revision_changes_continuation :
    ∃ y z, run acquiredStart acquiredHistory = some y ∧
      run acquiredStart unrevisedHistory = some z ∧
      Trace FormationClosure.process acquiredStart unrevisedHistory z ∧
      y.native.held = 793184 ∧ z.native.held = 170596 ∧
      y.native.transferred = 10 ∧ z.native.transferred = 0 ∧
      z.native.dissipated = 40 ∧ z.native.source = 0 ∧
      targetOf z.native.tau z.native.blocked = .C := by
  exact ⟨_, _, rfl, rfl, run_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem revised_holds_more : (170596 : Nat) < 793184 := by decide

end Generative.InquirySufficiency.PortValuation

#print axioms Generative.InquirySufficiency.PortValuation.portOrg
#print axioms Generative.InquirySufficiency.PortValuation.portWorld
#print axioms Generative.InquirySufficiency.PortValuation.world_is_native
#print axioms Generative.InquirySufficiency.PortValuation.disposition_after_encounter
#print axioms Generative.InquirySufficiency.PortValuation.port_history_dependent
#print axioms Generative.InquirySufficiency.PortValuation.port_consequence_dependent
#print axioms Generative.InquirySufficiency.PortValuation.port_change_needs_retained_difference
#print axioms Generative.InquirySufficiency.PortValuation.disposition_stale_then_recovers
#print axioms Generative.InquirySufficiency.PortValuation.unrevisedHistory
#print axioms Generative.InquirySufficiency.PortValuation.revision_changes_continuation
#print axioms Generative.InquirySufficiency.PortValuation.revised_holds_more
