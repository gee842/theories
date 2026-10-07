import PortRenewalLawClosure

/-!
Direct regeneration of a formation condition in the existing port process.
The inquiry's failed packet backs a new spare pair; its arriving packet can
cover inquiry and recovery. Contact does not age and source is not replenished.
-/

namespace Generative.InquirySufficiency.PortDirectRenewal

open Generative NativePacketProcess NativePortContinuation
open FormationClosure AcquiredContact PortRenewalLawClosure

/-- The two actual probes record ten failed units when open, twenty when blocked. -/
theorem inquiry_material {s : State} (q : Inquiry s) (intact : s.broken = false) :
    q.s5.dissipated = s.dissipated + (if s.blocked then 20 else 10) ∧
    q.s5.transferred = s.transferred + (if s.blocked then 0 else 10) := by
  obtain ⟨s1, s2, s3, s4, s5, r0, r1, o1, o3, o4, h1, h2, h3, h4, h5⟩ := q
  obtain ⟨_, rfl, rfl⟩ := reset_shape h1
  obtain ⟨_, rfl, _⟩ := (probe_complete_iff _ _ _).mp h2
  obtain ⟨_, rfl, rfl⟩ := a_shape h3
  obtain ⟨_, rfl, rfl⟩ := a_shape h4
  obtain ⟨_, rfl, _⟩ := (probe_complete_iff _ _ _).mp h5
  cases s with
  | mk phase tau sigma broken blocked flip source held live workspace capacity enacted
      arrived transferred dissipated =>
    subst intact
    cases tau <;> cases blocked
    · exact ⟨Nat.add_zero (dissipated + 10),
        congrArg (fun n => n + 10) (Nat.add_zero transferred)⟩
    · exact ⟨(Nat.add_assoc dissipated 10 10), Nat.add_zero (transferred + 0)⟩
    · exact ⟨congrArg (fun n => n + 10) (Nat.add_zero dissipated),
        Nat.add_zero (transferred + 10)⟩
    · exact ⟨(Nat.add_assoc dissipated 10 10), Nat.add_zero (transferred + 0)⟩

/-- Lift the native word while retaining exactly the same pair coordinates. -/
theorem native_word_lifts (spare recovered : Nat) {s t : State} {commands : List Command}
    (history : Trace NativePacketProcess.process s commands t) :
    Trace FormationClosure.process ⟨s, spare, recovered⟩ (nativeRun commands)
      ⟨t, spare, recovered⟩ := by
  induction history with
  | nil => exact .nil _
  | @cons s m t c cs step _ ih =>
    have first : FormationClosure.process.step ⟨s, spare, recovered⟩ (nativeE c)
        ⟨m, spare, recovered⟩ := ⟨step, rfl, rfl⟩
    exact .cons first ih

/-- Five native commands, then the actual pair-recovery event. -/
def renewalEvents : List FormationClosure.Event :=
  nativeRun inquiryCommands ++ [recoverE]

/-- Conditions retained by productive rounds, except for their finite source.
The held bound is sufficient transient funding, not a necessary threshold. -/
structure Ready (x : Port) : Prop where
  intact : x.native.broken = false
  opened : x.native.blocked = false
  backed : Backed x
  capacity : peak x.native ≤ x.native.capacity
  covered : 8 * draw x.native ≤ x.native.held
  adequate : 8 * draw x.native ≤ 655360

/-- Exact changes include material stock and the held costs of recovery. -/
structure Regenerates (x y : Port) : Prop where
  source : y.native.source + 20 = x.native.source
  held : y.native.held + 8 * draw x.native = x.native.held + 655360
  spare : y.spare = x.spare + 1
  recovered : y.recovered = x.recovered + 1
  dissipated : y.native.dissipated = x.native.dissipated + 10
  transferred : y.native.transferred = x.native.transferred + 10
  arrived : y.native.arrived = x.native.arrived + 655360
  enacted : y.native.enacted = x.native.enacted + 8 * draw x.native
  draw : draw y.native = draw x.native
  peak : peak y.native = peak x.native
  capacity : y.native.capacity = x.native.capacity
  intact : y.native.broken = x.native.broken
  opened : y.native.blocked = false

/-- A productive inquiry supplies its own new recovery backing. No existing
unrecovered failures or spare pair are required, only a consistent old record. -/
theorem inquiry_recovers_pair (x : Port) (intact : x.native.broken = false)
    (opened : x.native.blocked = false) (backed : Backed x)
    (capacity : peak x.native ≤ x.native.capacity)
    (source : 20 ≤ x.native.source) (covered : 8 * draw x.native ≤ x.native.held) :
    ∃ y, Trace FormationClosure.process x renewalEvents y ∧ Regenerates x y ∧ Backed y := by
  let q := fundedInquiry x.native capacity source (by omega)
  let middle : Port := ⟨q.s5, x.spare, x.recovered⟩
  let y : Port := ⟨enact q.s5, x.spare + 1, x.recovered + 1⟩
  have material := (inquiry_material q intact).1
  have transfer := (inquiry_material q intact).2
  have balance := inquiry_held_balance q intact
  have arrival := inquiry_arrival q intact
  rw [opened] at material transfer balance arrival
  change q.s5.dissipated = x.native.dissipated + 10 at material
  change q.s5.transferred = x.native.transferred + 10 at transfer
  change q.s5.held + 7 * draw x.native = x.native.held + 655360 at balance
  change q.s5.arrived = x.native.arrived + 655360 at arrival
  have drawQ : draw q.s5 = draw x.native := (inquiry_amounts q).2.2
  have supportQ : Supportable q.s5 := ⟨capacity, by rw [drawQ]; omega⟩
  have backing : 10 * (x.recovered + 1) ≤ q.s5.dissipated := by
    unfold Backed at backed
    omega
  have recovery : recover middle = .complete y :=
    (recover_complete_iff middle y).2 ⟨supportQ, backing, rfl⟩
  have history : Trace FormationClosure.process x renewalEvents y :=
    trace_append_iff.mpr ⟨middle, native_word_lifts x.spare x.recovered q.trace,
      .cons recovery (.nil _)⟩
  have paid : y.native.held + draw x.native = q.s5.held :=
    sub_add_restore _ _ supportQ.2
  refine ⟨y, history, ?_, trace_preserves_backing history backed⟩
  refine ⟨(inquiry_amounts q).1, by omega, rfl, rfl, material, transfer, arrival,
    ?_, drawQ, rfl, rfl, rfl, ?_⟩
  · have enacted := (inquiry_amounts q).2.1
    change q.s5.enacted + draw x.native = x.native.enacted + 8 * draw x.native
    omega
  · exact (inquiry_reveals q intact).2.2.2.2.2.1.trans opened

/-- The exact endpoint inequality includes recovery's eighth supported stage. -/
theorem regeneration_replenishes_iff {x y : Port} (r : Regenerates x y) :
    x.native.held ≤ y.native.held ↔ 8 * draw x.native ≤ 655360 := by
  have balance := r.held
  constructor <;> intro bound <;> omega

/-- Actual regeneration retains the conditions for another round, while its
source guard must be discharged anew from the reached source coordinate. -/
theorem regeneration_ready {x y : Port} (ready : Ready x)
    (r : Regenerates x y) (backed : Backed y) : Ready y := by
  have grows := (regeneration_replenishes_iff r).mpr ready.adequate
  refine ⟨r.intact.trans ready.intact, r.opened, backed, ?_, ?_, ?_⟩
  · rw [r.peak, r.capacity]; exact ready.capacity
  · rw [r.draw]; exact Nat.le_trans ready.covered grows
  · rw [r.draw]; exact ready.adequate

/-- Actual words concatenate at the reached state; no resource coordinate resets. -/
def renewalRounds : Nat → List FormationClosure.Event
  | 0 => []
  | n + 1 => renewalEvents ++ renewalRounds n

/-- Repeated rounds accumulate newly backed formation material and retain held
support. The initial finite source pays for every round. -/
theorem finite_material_regeneration (n : Nat) (x : Port) (ready : Ready x)
    (source : 20 * n ≤ x.native.source) :
    ∃ y, Trace FormationClosure.process x (renewalRounds n) y ∧ Ready y ∧
      y.native.source + 20 * n = x.native.source ∧
      y.spare = x.spare + n ∧ y.recovered = x.recovered + n ∧
      y.native.dissipated = x.native.dissipated + 10 * n ∧
      y.native.held + n * (8 * draw x.native) = x.native.held + n * 655360 ∧
      x.native.held ≤ y.native.held := by
  induction n generalizing x with
  | zero => exact ⟨x, .nil _, ready, rfl, rfl, rfl, rfl, by simp only [Nat.zero_mul, Nat.add_zero], Nat.le_refl _⟩
  | succ n ih =>
    obtain ⟨m, first, r, backed⟩ := inquiry_recovers_pair x ready.intact ready.opened
      ready.backed ready.capacity (by omega) ready.covered
    obtain ⟨y, rest, readyY, sourceY, spareY, recoveredY, materialY, balanceY, growsY⟩ :=
      ih m (regeneration_ready ready r backed) (by have h := r.source; omega)
    have grows := (regeneration_replenishes_iff r).mpr ready.adequate
    refine ⟨y, trace_append_iff.mpr ⟨m, first, rest⟩, readyY, ?_, ?_, ?_, ?_, ?_,
      Nat.le_trans grows growsY⟩
    · have h := r.source; omega
    · rw [spareY, r.spare]; omega
    · rw [recoveredY, r.recovered]; omega
    · rw [materialY, r.dissipated]; omega
    · rw [r.draw] at balanceY
      rw [Nat.succ_mul n (8 * draw x.native), Nat.succ_mul n 655360]
      have h := r.held
      omega

/-- An actual contact formation consumes one pair; the following productive
inquiry and recovery replace precisely that pair at nine draws total. This
does not claim contact aging, a second organization, or source regeneration. -/
theorem formation_regenerates_its_pair (x : Port) (intact : x.native.broken = false)
    (blocked : x.native.blocked = true) (backed : Backed x) (pair : 1 ≤ x.spare)
    (capacity : peak x.native ≤ x.native.capacity)
    (source : 20 ≤ x.native.source) (covered : 9 * draw x.native ≤ x.native.held) :
    ∃ y, Trace FormationClosure.process x (formE :: renewalEvents) y ∧
      y.native.blocked = false ∧ x.native.blocked ≠ y.native.blocked ∧
      y.spare = x.spare ∧ y.recovered = x.recovered + 1 ∧ Backed y ∧
      y.native.source + 20 = x.native.source ∧
      y.native.held + 9 * draw x.native = x.native.held + 655360 ∧
      (x.native.held ≤ y.native.held ↔ 9 * draw x.native ≤ 655360) := by
  let m : Port := ⟨ContactFormation.openContact (enact x.native), x.spare - 1, x.recovered⟩
  have funding : draw x.native ≤ x.native.held := by omega
  have formation : formPort x = .complete m :=
    (formPort_complete_iff x m).mpr ⟨⟨capacity, funding⟩, pair, rfl⟩
  have paid : m.native.held + draw x.native = x.native.held :=
    sub_add_restore _ _ funding
  obtain ⟨y, history, r, backedY⟩ := inquiry_recovers_pair m intact rfl backed capacity source
    (by change 8 * draw x.native ≤ m.native.held; omega)
  have held : y.native.held + 9 * draw x.native = x.native.held + 655360 := by
    have h := r.held
    change y.native.held + 8 * draw x.native = m.native.held + 655360 at h
    omega
  refine ⟨y, .cons formation history, r.opened, ?_, ?_, r.recovered, backedY,
    r.source, held, ?_⟩
  · rw [blocked, r.opened]; exact Bool.noConfusion
  · change y.spare = x.spare
    exact r.spare.trans (sub_add_restore _ _ pair)
  · constructor <;> intro bound <;> omega

/-- The earlier acquired history, extended by actual recovery, begins with
zero spares and ends with an open contact AND a newly available spare. -/
theorem acquired_condition_regeneration :
    ∃ y, run acquiredStart (acquiredHistory ++ [recoverE]) = some y ∧
      Trace FormationClosure.process acquiredStart (acquiredHistory ++ [recoverE]) y ∧
      acquiredStart.spare = 0 ∧ acquiredStart.recovered = 0 ∧
      y.native.blocked = false ∧ y.spare = 1 ∧ y.recovered = 2 ∧
      y.native.source = 0 ∧ y.native.dissipated = 30 ∧
      y.native.transferred = 10 ∧ y.native.arrived = 655360 ∧
      y.native.enacted = 278562 ∧ y.native.held = 776798 := by
  exact ⟨_, rfl, run_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- A supplied open port where inquiry alone is held-balanced but adding real
material recovery is not: the extra supported stage must not be omitted. -/
def highOverhead : Port :=
  ⟨{ acquiredStart.native with blocked := false, source := 20, held := 1000000, live := 73614, capacity := 73616 }, 0, 0⟩

theorem held_only_adequacy_does_not_cover_recovery :
    7 * draw highOverhead.native ≤ 655360 ∧
      655360 < 8 * draw highOverhead.native ∧
      ∃ y, run highOverhead renewalEvents = some y ∧
        Trace FormationClosure.process highOverhead renewalEvents y ∧
        y.spare = 1 ∧ y.native.held = 935360 ∧
        y.native.held < highOverhead.native.held ∧ y.native.source = 0 := by
  refine ⟨by decide, by decide, _, rfl, run_sound rfl, rfl, rfl, ?_, rfl⟩
  decide

end Generative.InquirySufficiency.PortDirectRenewal

#print axioms Generative.InquirySufficiency.PortDirectRenewal.inquiry_material
#print axioms Generative.InquirySufficiency.PortDirectRenewal.native_word_lifts
#print axioms Generative.InquirySufficiency.PortDirectRenewal.renewalEvents
#print axioms Generative.InquirySufficiency.PortDirectRenewal.Ready
#print axioms Generative.InquirySufficiency.PortDirectRenewal.Regenerates
#print axioms Generative.InquirySufficiency.PortDirectRenewal.inquiry_recovers_pair
#print axioms Generative.InquirySufficiency.PortDirectRenewal.regeneration_replenishes_iff
#print axioms Generative.InquirySufficiency.PortDirectRenewal.regeneration_ready
#print axioms Generative.InquirySufficiency.PortDirectRenewal.renewalRounds
#print axioms Generative.InquirySufficiency.PortDirectRenewal.finite_material_regeneration
#print axioms Generative.InquirySufficiency.PortDirectRenewal.formation_regenerates_its_pair
#print axioms Generative.InquirySufficiency.PortDirectRenewal.acquired_condition_regeneration
#print axioms Generative.InquirySufficiency.PortDirectRenewal.highOverhead
#print axioms Generative.InquirySufficiency.PortDirectRenewal.held_only_adequacy_does_not_cover_recovery
