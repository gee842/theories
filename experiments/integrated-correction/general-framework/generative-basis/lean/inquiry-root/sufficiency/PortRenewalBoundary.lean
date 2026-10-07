import WholePortContinuation
import RelationalCut
import RenewalAccounting

/-!
# What the actual formed contact supplies to the renewal interface

Both the renewal configuration law and the revising port satisfy U1. The
contact-preserving and contact-changing parts inherit the law from their one
process. This derives an accounting interface across the relational cut; it
does not derive renewal's token-aging, span, support-edge or constant-rate law.

Actual formation followed by actual conversion can bring in more than the
formation draw, or less. One successful conversion brings 655360 held ticks
from ten source units. High overhead can exceed that arrival; without source,
an open contact brings no arrival. The counterexamples keep formation and the
native transfer law, rather than independently toggling a favorable predicate.
-/

namespace Generative.InquirySufficiency.PortRenewalBoundary

open Generative NativePacketProcess NativePortContinuation
open FormationClosure WholePortContinuation

universe u

/-- Renewal's declared resource update has exactly the common U1 form. This
does not supply its other two clauses (aging and actual support). -/
theorem renewal_sustain_law {Kind : Type u} (law : Conditional.Renewal.ChannelLaw Kind) :
    Conditional.SustainLaw (Conditional.Renewal.channelProcess law)
      Conditional.Renewal.Config.reserve
      (fun _ births _ => Conditional.Renewal.formation law births)
      (fun c _ _ => Conditional.Renewal.opened law.rate c.tokens) :=
  fun _ _ _ step => step.2.1

/-- The relation to the contact coordinate, not a prior division into kinds,
selects these steps. Their support account is inherited without new rates. -/
theorem contact_keeping_sustain_law : Conditional.SustainLaw
    (RelationalCut.keeps FormationClosure.process contact)
    (fun x => x.native.held) extendedEnacted extendedArrived :=
  fun _ _ _ step => extended_sustain_law _ _ _ step.1

theorem contact_changing_sustain_law : Conditional.SustainLaw
    (RelationalCut.changes FormationClosure.process contact)
    (fun x => x.native.held) extendedEnacted extendedArrived :=
  fun _ _ _ step => extended_sustain_law _ _ _ step.1

theorem contact_change_has_actual_draw {x y : Port} {e : FormationClosure.Event}
    (step : (RelationalCut.changes FormationClosure.process contact).step x e y) :
    extendedEnacted x e y = draw x.native ∧ extendedArrived x e y = 0 := by
  cases e with
  | inl event => exact False.elim (step.2 (activity_retains_contact _ _ _ step.1))
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step.1
    exact ⟨add_sub_self_left _ _, Nat.sub_self _⟩

/-- Source and held coordinates have different local units. A successful
packet converts ten source units to this many held ticks. -/
theorem successful_packet_units (s : State) (arrives : arrival s = true) :
    arrivalAmount s = 10 * yieldPerUnit := by
  unfold arrivalAmount
  rw [arrives]
  rfl

/-- Fixed contact/phase family for actual formation-and-probe comparisons.
Only the source, amount held, and live overhead vary. -/
def examplePort (held source live : Nat) : Port :=
  ⟨{ phase := .p2, tau := false, sigma := false, broken := false, blocked := true,
     receiptFlip := false, source := source, held := held, live := live, workspace := 0,
     capacity := live + 2, enacted := 0, arrived := 0, transferred := 0, dissipated := 0 },
    1, 0⟩

def formedExample (held source live : Nat) : Port :=
  ⟨ContactFormation.openContact (enact (examplePort held source live).native), 0, 0⟩

def probedExample (held source live : Nat) : Port :=
  ⟨probeFinal (formedExample held source live).native, 0, 0⟩

def formationProbe : List FormationClosure.Event := [.inr (), .inl (.inl .probe)]

theorem low_overhead_actual_trace :
    Trace FormationClosure.process (examplePort 100000 10 0) formationProbe
      (probedExample 100000 10 0) :=
  .cons (show formPort (examplePort 100000 10 0) = .complete (formedExample 100000 10 0) from rfl)
    (.cons (show FormationClosure.process.step (formedExample 100000 10 0)
      (.inl (.inl .probe)) (probedExample 100000 10 0) from
      ⟨⟨.receipt true, rfl⟩, rfl, rfl⟩) (.nil _))

/-- One packet covers not only formation but both native probe stages in this
actual low-overhead history. It still exhausts its finite source. -/
theorem low_overhead_covers_whole_segment :
    (formedExample 100000 10 0).native.enacted = 16386 ∧
    (probedExample 100000 10 0).native.enacted = 49158 ∧
    (probedExample 100000 10 0).native.arrived = 655360 ∧
    (probedExample 100000 10 0).native.transferred = 10 ∧
    (probedExample 100000 10 0).native.source = 0 ∧
    (probedExample 100000 10 0).native.enacted < (probedExample 100000 10 0).native.arrived :=
  ⟨rfl, rfl, rfl, rfl, rfl, by decide⟩

theorem high_overhead_actual_trace :
    Trace FormationClosure.process (examplePort 3000000 10 700000) formationProbe
      (probedExample 3000000 10 700000) :=
  .cons (show formPort (examplePort 3000000 10 700000) =
      .complete (formedExample 3000000 10 700000) from rfl)
    (.cons (show FormationClosure.process.step (formedExample 3000000 10 700000)
      (.inl (.inl .probe)) (probedExample 3000000 10 700000) from
      ⟨⟨.receipt true, rfl⟩, rfl, rfl⟩) (.nil _))

/-- Same contact change and successful transfer, but even formation alone
draws more than the packet arrives in the same held-tick units. -/
theorem high_overhead_shortfall :
    (formedExample 3000000 10 700000).native.enacted = 716386 ∧
    (probedExample 3000000 10 700000).native.arrived = 655360 ∧
    (probedExample 3000000 10 700000).native.transferred = 10 ∧
    (probedExample 3000000 10 700000).native.arrived <
      (formedExample 3000000 10 700000).native.enacted :=
  ⟨rfl, rfl, rfl, by decide⟩

/-- Opening still completes without any source; its following probe enacts
the interface stage and stops before conversion. -/
theorem empty_source_opens_without_arrival :
    formPort (examplePort 100000 0 0) = .complete (formedExample 100000 0 0) ∧
    (formedExample 100000 0 0).native.blocked = false ∧
    execute (formedExample 100000 0 0).native .probe =
      .stopped (enact (formedExample 100000 0 0).native) .sourceUnavailable ∧
    (enact (formedExample 100000 0 0).native).arrived = 0 :=
  ⟨rfl, rfl, rfl, rfl⟩

/-- Refutes the universal one-packet adequacy proposal while preserving a
completed formation and an actual successful probe. -/
theorem not_every_formed_contact_covers_formation :
    ¬ ∀ x z y : Port, formPort x = .complete z →
      NativePacketProcess.process.step z.native .probe y.native →
      z.native.enacted - x.native.enacted ≤ y.native.arrived - z.native.arrived := by
  intro covers
  have impossible := covers (examplePort 3000000 10 700000)
    (formedExample 3000000 10 700000) (probedExample 3000000 10 700000) rfl ⟨_, rfl⟩
  exact (by decide : ¬ 716386 ≤ 655360) impossible

/-- An actual favorable segment has the same finite-source bound as every
other segment. There is no inferred replenishment of its source. -/
theorem favorable_start_still_has_finite_bound {y : Port} {es : List FormationClosure.Event}
    (history : Trace FormationClosure.process (examplePort 100000 10 0) es y) :
    es.length + potential y.native ≤ 755360 :=
  extended_history_length history

/-- Empty spare stock and no earlier failure record; two source packets are
present so the first failed probe can supply the later formation. -/
def recoveredStart (held live : Nat) : Port :=
  { examplePort held 20 live with spare := 0 }

def recoveredHistory : List FormationClosure.Event :=
  [nativeE .probe, recoverE, formE, nativeE .probe]

/-- The favorable case can include the actual failure and recovery of its
forming pair. All six supported stages together remain below the arrival. -/
theorem recovery_backed_low_overhead :
    ∃ y, run (recoveredStart 200000 0) recoveredHistory = some y ∧
      Trace FormationClosure.process (recoveredStart 200000 0) recoveredHistory y ∧
      (recoveredStart 200000 0).spare = 0 ∧
      (recoveredStart 200000 0).native.dissipated = 0 ∧
      y.native.enacted = 98316 ∧ y.native.arrived = 655360 ∧
      y.native.transferred = 10 ∧ y.native.dissipated = 10 ∧
      y.native.source = 0 ∧ y.spare = 0 ∧ y.recovered = 1 ∧
      y.native.enacted < y.native.arrived := by
  refine ⟨_, rfl, run_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, ?_⟩
  decide

/-- The adverse case also starts without spares or a failure record. The
pair really is recovered in this history; successful transfer still fails to
cover even the one formation draw. -/
theorem recovery_backed_high_overhead_shortfall :
    ∃ y, run (recoveredStart 5000000 700000) recoveredHistory = some y ∧
      Trace FormationClosure.process (recoveredStart 5000000 700000) recoveredHistory y ∧
      (recoveredStart 5000000 700000).spare = 0 ∧
      (recoveredStart 5000000 700000).native.dissipated = 0 ∧
      y.native.arrived = 655360 ∧ y.native.transferred = 10 ∧ y.native.dissipated = 10 ∧
      y.native.source = 0 ∧ y.spare = 0 ∧ y.recovered = 1 ∧
      y.native.arrived < draw (recoveredStart 5000000 700000).native := by
  refine ⟨_, rfl, run_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, ?_⟩
  decide

end Generative.InquirySufficiency.PortRenewalBoundary


#print axioms Generative.InquirySufficiency.PortRenewalBoundary.renewal_sustain_law
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.contact_keeping_sustain_law
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.contact_changing_sustain_law
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.contact_change_has_actual_draw
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.successful_packet_units
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.examplePort
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.formedExample
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.probedExample
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.formationProbe
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.low_overhead_actual_trace
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.low_overhead_covers_whole_segment
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.high_overhead_actual_trace
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.high_overhead_shortfall
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.empty_source_opens_without_arrival
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.not_every_formed_contact_covers_formation
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.favorable_start_still_has_finite_bound
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.recoveredStart
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.recoveredHistory
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.recovery_backed_low_overhead
#print axioms Generative.InquirySufficiency.PortRenewalBoundary.recovery_backed_high_overhead_shortfall
