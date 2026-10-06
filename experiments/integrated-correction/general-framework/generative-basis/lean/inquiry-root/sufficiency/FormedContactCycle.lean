import ContactFormation
import PhasePeriodSelection

/-!
# Formed contact supplies the two-valued arrival on the phase cycle

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
PHASE-PERIOD-SELECTION.md (joining section).

`PhaseCycleDerivation` states requirement R0 as: the probe needs a phase at which
arrival is possible, so both values of the arrival contact must occur around the
cycle. `ContactFormation` (imported unchanged from the contact-formation thread)
adds a formation event that clears `blocked`. This module joins the two where
their interfaces match: the arrival read around the three phases.

Joined: a blocked port has one-valued arrival on every phase, so R0 fails; a
completed formation makes it two-valued, equal to the native pattern `(0,0,1)`
up to the global inversion `tau`, keeps the phase, and so meets R0–R2; and in the
extended process every history that reaches two-valued arrival from a blocked
port contains a formation event.

Not joined: the phase-recovery results (R1 and knowing arrival under unknown
inversion) concern the sensor reading `readBit`, which never depends on
`blocked`. Formation neither supplies nor changes that reading, and the learned
output table `(0,0,1)` itself remains supplied.
-/

namespace Generative.InquirySufficiency.FormedContactCycle

open Generative
open Generative.NativePacketProcess (State Phase output arrivalAt)
open Generative.InquirySufficiency.PhaseCycleDerivation (bothValuesOccur supportsAlignment)
open Generative.InquirySufficiency.ContactFormation
  (Formed form formCount form_complete_iff opening_requires_formation)

/-- Actual arrival at each of the three phases, for the port's fixed inversion and contact. -/
def arrivalPattern (s : State) : List Bool :=
  [arrivalAt (output .p0) s.tau s.blocked, arrivalAt (output .p1) s.tau s.blocked,
    arrivalAt (output .p2) s.tau s.blocked]

theorem blocked_arrival_one_valued (s : State) (blocked : s.blocked = true) :
    arrivalPattern s = [false, false, false] ∧ bothValuesOccur (arrivalPattern s) = false := by
  unfold arrivalPattern
  rw [blocked]
  cases s.tau <;> exact ⟨rfl, rfl⟩

theorem open_arrival_is_native_pattern (s : State) (opened : s.blocked = false) :
    arrivalPattern s = [false, false, true].map (fun value => value != s.tau) := by
  unfold arrivalPattern
  rw [opened]
  cases s.tau <;> rfl

theorem native_pattern_inverted_supports_alignment (tau : Bool) :
    bothValuesOccur ([false, false, true].map (fun value => value != tau)) = true ∧
      supportsAlignment ([false, false, true].map (fun value => value != tau)) 3 2 = true := by
  cases tau <;> decide

/-- Formation turns one-valued arrival into the native two-valued pattern (up to
`tau`), on the same phase, so R0 and the rest of the alignment requirements hold. -/
theorem formation_supplies_two_valued_arrival (x y : Formed) (blocked : x.port.blocked = true)
    (completed : form x = .complete y) :
    bothValuesOccur (arrivalPattern x.port) = false ∧
      arrivalPattern y.port = [false, false, true].map (fun value => value != x.port.tau) ∧
      bothValuesOccur (arrivalPattern y.port) = true ∧
      supportsAlignment (arrivalPattern y.port) 3 2 = true ∧
      y.port.phase = x.port.phase := by
  obtain ⟨_, _, rfl⟩ := (form_complete_iff x y).mp completed
  have opened := open_arrival_is_native_pattern
    (ContactFormation.formedState x).port rfl
  have supported := native_pattern_inverted_supports_alignment x.port.tau
  refine ⟨(blocked_arrival_one_valued x.port blocked).2, opened, ?_, ?_, rfl⟩
  · rw [opened]; exact supported.1
  · rw [opened]; exact supported.2

/-- In the extended process, two-valued arrival from a blocked start requires formation. -/
theorem two_valued_arrival_requires_formation {x y : Formed}
    {events : List ContactFormation.Event}
    (trace : Trace ContactFormation.process x events y) (blocked : x.port.blocked = true)
    (twoValued : bothValuesOccur (arrivalPattern y.port) = true) : 1 ≤ formCount events := by
  cases ended : y.port.blocked with
  | false => exact opening_requires_formation trace blocked ended
  | true =>
    rw [(blocked_arrival_one_valued y.port ended).2] at twoValued
    cases twoValued

/-- The sensor reading never depends on the contact: formation leaves the readable
pattern, and so the phase-recovery results, exactly where they were. -/
theorem reading_independent_of_contact (s : State) (contact : Bool) :
    NativePacketProcess.readBit { s with blocked := contact } = NativePacketProcess.readBit s :=
  rfl

end Generative.InquirySufficiency.FormedContactCycle

#print axioms Generative.InquirySufficiency.FormedContactCycle.arrivalPattern
#print axioms Generative.InquirySufficiency.FormedContactCycle.blocked_arrival_one_valued
#print axioms Generative.InquirySufficiency.FormedContactCycle.open_arrival_is_native_pattern
#print axioms Generative.InquirySufficiency.FormedContactCycle.native_pattern_inverted_supports_alignment
#print axioms Generative.InquirySufficiency.FormedContactCycle.formation_supplies_two_valued_arrival
#print axioms Generative.InquirySufficiency.FormedContactCycle.two_valued_arrival_requires_formation
#print axioms Generative.InquirySufficiency.FormedContactCycle.reading_independent_of_contact
