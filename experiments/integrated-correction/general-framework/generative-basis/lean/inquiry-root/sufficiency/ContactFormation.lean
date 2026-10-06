import PacketLawDerivation

/-!
# Supported contact formation changes the derived packet law

The native port holds its contact coordinate fixed: `execute_retains_parameters`
proves that no native command changes `blocked`. The derived A/B/C class, and
therefore the effective probe law, is consequently invariant under every native
history. This module adds one formation operation beside the unchanged port.

Formation follows the port's own ordering. It first meets the native interface
demand under the native capacity check, then requires one inherited spare
component pair. A completed formation consumes that pair and clears the
blocked contact. If no spare pair remains, the reserve drawn for the interface
is not restored and the contact stays blocked. No new material, free reset or favorable
replacement configuration is introduced.

Supplied here: the spare-pair stock, the use of the native interface demand for
formation, and the rule that a formed contact clears `blocked`. These follow the
pattern of the existing inquiry-revision contact (one inherited spare pair, one
supported operation), but that mechanism belongs to a different apparatus; its exact
parts are not claimed to compose with this port. Inversion `tau`, sensor parity
and receipt inversion remain fixed coordinates. Opening a contact changes which
transfer class the port has; it does not choose the favorable one, calibrate the
receipt, or establish that the change is good.
-/

namespace Generative.InquirySufficiency.ContactFormation

open Generative NativePacketProcess PacketLawDerivation OnePacketQuestions

/-- The native port together with its inherited stock of spare component pairs. -/
structure Formed where
  port : NativePacketProcess.State
  spare : Nat

inductive FormFailure where
  | interfaceCapacity | interfaceReserve | noSpare

inductive FormResult where
  | complete (state : Formed)
  | stopped (state : Formed) (reason : FormFailure)

def openContact (s : NativePacketProcess.State) : NativePacketProcess.State :=
  { s with blocked := false }

/-- Meet the native interface demand, then consume one spare pair to open the contact.
A missing pair is discovered after that demand is met, as the native source check is. -/
def finishForm (x : Formed) (ready : NativePacketProcess.State) : FormResult :=
  if 1 ≤ x.spare then .complete ⟨openContact ready, x.spare - 1⟩
  else .stopped ⟨ready, x.spare⟩ .noSpare

def form (x : Formed) : FormResult :=
  match charge x.port with
  | .capacity => .stopped x .interfaceCapacity
  | .funding => .stopped x .interfaceReserve
  | .paid ready => finishForm x ready

def formedState (x : Formed) : Formed := ⟨openContact (debit x.port), x.spare - 1⟩

inductive Event where
  | native (command : NativePacketProcess.Command)
  | form

/-- Completed native calls keep the spare stock; completed formations follow `form`. -/
def process : Process Formed Event where
  step x e y := match e with
    | .native command => (∃ o, execute x.port command = .complete y.port o) ∧ y.spare = x.spare
    | .form => form x = .complete y

def formCount : List Event → Nat
  | [] => 0
  | .form :: rest => formCount rest + 1
  | .native _ :: rest => formCount rest

theorem form_complete (x : Formed) (ready : Payable x.port) (pair : 1 ≤ x.spare) :
    form x = .complete (formedState x) := by
  unfold form
  rw [charge_paid x.port ready.1 ready.2]
  dsimp only
  unfold finishForm
  rw [if_pos pair]
  rfl

theorem form_complete_iff (x y : Formed) :
    form x = .complete y ↔ Payable x.port ∧ 1 ≤ x.spare ∧ y = formedState x := by
  constructor
  · intro completed
    unfold form at completed
    generalize interface : charge x.port = payment at completed
    cases payment with
    | capacity => cases completed
    | funding => cases completed
    | paid ready =>
      obtain ⟨sustained, equality⟩ := (charge_paid_iff x.port ready).mp interface
      cases equality
      dsimp only at completed
      unfold finishForm at completed
      by_cases pair : 1 ≤ x.spare
      · rw [if_pos pair] at completed
        cases completed
        exact ⟨sustained, pair, rfl⟩
      · rw [if_neg pair] at completed
        cases completed
  · rintro ⟨sustained, pair, rfl⟩
    exact form_complete x sustained pair

theorem form_capacity_stops (x : Formed) (capacity : ¬ peak x.port ≤ x.port.capacity) :
    form x = .stopped x .interfaceCapacity := by
  unfold form
  rw [charge_capacity x.port capacity]

theorem form_reserve_stops (x : Formed) (capacity : peak x.port ≤ x.port.capacity)
    (short : ¬ bill x.port ≤ x.port.fuel) :
    form x = .stopped x .interfaceReserve := by
  unfold form
  rw [charge_funding x.port capacity short]

/-- Without a spare pair the interface demand is still drawn and nothing opens. -/
theorem form_no_spare_still_draws (x : Formed) (ready : Payable x.port)
    (empty : x.spare = 0) :
    form x = .stopped ⟨debit x.port, x.spare⟩ .noSpare ∧
      (debit x.port).blocked = x.port.blocked ∧
      (debit x.port).fuel = x.port.fuel - bill x.port := by
  refine ⟨?_, rfl, rfl⟩
  unfold form
  have missing : ¬ 1 ≤ x.spare := by
    rw [empty]
    exact Nat.not_succ_le_zero 0
  rw [charge_paid x.port ready.1 ready.2]
  dsimp only
  unfold finishForm
  rw [if_neg missing]

/-- Exactly what a completed formation changes and retains. `fuel` and `spent`
are the inherited native names for the usable reserve and its cumulative draw. -/
theorem formed_effects (x : Formed) :
    (formedState x).port.blocked = false ∧
      (formedState x).port.tau = x.port.tau ∧
      (formedState x).port.sigma = x.port.sigma ∧
      (formedState x).port.receiptFlip = x.port.receiptFlip ∧
      (formedState x).port.broken = x.port.broken ∧
      (formedState x).port.phase = x.port.phase ∧
      (formedState x).port.source = x.port.source ∧
      (formedState x).port.live = x.port.live ∧
      (formedState x).port.workspace = x.port.workspace ∧
      (formedState x).port.capacity = x.port.capacity ∧
      (formedState x).port.fuel = x.port.fuel - bill x.port ∧
      (formedState x).port.spent = x.port.spent + bill x.port ∧
      (formedState x).spare = x.spare - 1 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- A failed formation leaves the contact, inversion and spare stock unchanged. -/
theorem failed_formation_retains_contact (x y : Formed) (reason : FormFailure)
    (stopped : form x = .stopped y reason) :
    y.port.blocked = x.port.blocked ∧ y.port.tau = x.port.tau ∧ y.spare = x.spare := by
  unfold form at stopped
  generalize interface : charge x.port = payment at stopped
  cases payment with
  | capacity => cases stopped; exact ⟨rfl, rfl, rfl⟩
  | funding => cases stopped; exact ⟨rfl, rfl, rfl⟩
  | paid ready =>
    obtain ⟨_, equality⟩ := (charge_paid_iff x.port ready).mp interface
    cases equality
    dsimp only at stopped
    unfold finishForm at stopped
    by_cases pair : 1 ≤ x.spare
    · rw [if_pos pair] at stopped
      cases stopped
    · rw [if_neg pair] at stopped
      cases stopped
      exact ⟨rfl, rfl, rfl⟩

/-- Completed formation moves the derived class to the open class fixed by `tau`. -/
theorem formation_sets_open_class (x y : Formed) (completed : form x = .complete y) :
    targetOf y.port.tau y.port.blocked = targetOf x.port.tau false := by
  obtain ⟨_, _, rfl⟩ := (form_complete_iff x y).mp completed
  rfl

theorem formation_leaves_class_C (x y : Formed) (blocked : x.port.blocked = true)
    (completed : form x = .complete y) :
    targetOf x.port.tau x.port.blocked = .C ∧ targetOf y.port.tau y.port.blocked ≠ .C := by
  rw [formation_sets_open_class x y completed, blocked]
  cases x.port.tau with
  | false => exact ⟨rfl, fun same => by cases same⟩
  | true => exact ⟨rfl, fun same => by cases same⟩

/-- The transfer-response profile changes from no arrival to exactly one arriving output. -/
theorem formation_changes_profile (x y : Formed) (blocked : x.port.blocked = true)
    (completed : form x = .complete y) :
    profile x.port.tau x.port.blocked = (false, false) ∧
      profile y.port.tau y.port.blocked = (x.port.tau, !x.port.tau) := by
  obtain ⟨_, _, rfl⟩ := (form_complete_iff x y).mp completed
  rw [blocked]
  change profile x.port.tau true = (false, false) ∧
    profile x.port.tau false = (x.port.tau, !x.port.tau)
  cases x.port.tau <;> exact ⟨rfl, rfl⟩

/-- Every native trace retains the contact and inversion coordinates. -/
theorem native_trace_retains_contact {s t : NativePacketProcess.State}
    {commands : List NativePacketProcess.Command}
    (trace : Trace NativePacketProcess.process s commands t) :
    t.blocked = s.blocked ∧ t.tau = s.tau := by
  induction trace with
  | nil => exact ⟨rfl, rfl⟩
  | cons step _ ih =>
    obtain ⟨_, actual⟩ := step
    have same := completed_retains_parameters actual
    exact ⟨ih.1.trans same.2.2.2.1, ih.2.trans same.1⟩

/-- Without formation, a blocked port remains in class C after any native history. -/
theorem native_history_cannot_leave_C {s t : NativePacketProcess.State}
    {commands : List NativePacketProcess.Command}
    (trace : Trace NativePacketProcess.process s commands t) (blocked : s.blocked = true) :
    targetOf t.tau t.blocked = .C := by
  rw [(native_trace_retains_contact trace).1, blocked]
  cases t.tau <;> rfl

/-- In the extended process, opening a blocked contact requires a formation event. -/
theorem opening_requires_formation {x y : Formed} {events : List Event}
    (trace : Trace process x events y) (blocked : x.port.blocked = true)
    (opened : y.port.blocked = false) : 1 ≤ formCount events := by
  induction trace with
  | nil =>
    rw [blocked] at opened
    cases opened
  | @cons s m t event rest step _ ih =>
    cases event with
    | native command =>
      obtain ⟨⟨_, actual⟩, _⟩ := step
      have same := completed_retains_parameters actual
      exact ih (same.2.2.2.1.trans blocked) opened
    | form =>
      exact Nat.succ_le_succ (Nat.zero_le _)

/-- Each completed formation consumes exactly one inherited spare pair. -/
theorem spare_accounting {x y : Formed} {events : List Event}
    (trace : Trace process x events y) : y.spare + formCount events = x.spare := by
  induction trace with
  | nil => rfl
  | @cons s m t event rest step _ ih =>
    cases event with
    | native command =>
      obtain ⟨_, kept⟩ := step
      change t.spare + formCount rest = s.spare
      rw [ih, kept]
    | form =>
      obtain ⟨_, pair, rfl⟩ := (form_complete_iff s m).mp step
      change t.spare + (formCount rest + 1) = s.spare
      rw [← Nat.add_assoc, ih]
      exact sub_add_cancel_constructive s.spare 1 pair

theorem formations_bounded_by_spares {x y : Formed} {events : List Event}
    (trace : Trace process x events y) : formCount events ≤ x.spare := by
  rw [← spare_accounting trace]
  exact Nat.le_add_left _ _

/-- Same alignment schedule, same phase, opposite transfer outcome: aligning
toward the output that differs from `tau` yields no arrival before formation
and an actual arrival after it. -/
theorem formation_changes_aligned_arrival (x y : Formed) (blocked : x.port.blocked = true)
    (completed : form x = .complete y) :
    alignedEvents (!x.port.tau) y.port = alignedEvents (!x.port.tau) x.port ∧
      arrival (alignedState (!x.port.tau) x.port) = false ∧
      arrival (alignedState (!x.port.tau) y.port) = true := by
  obtain ⟨_, _, rfl⟩ := (form_complete_iff x y).mp completed
  have before := rotation_fields (alignmentCount x.port.phase (!x.port.tau)) x.port
  have after := rotation_fields (alignmentCount (formedState x).port.phase (!x.port.tau))
    (formedState x).port
  have beforeOut := (aligned_state_properties (!x.port.tau) x.port).1
  have afterOut := (aligned_state_properties (!x.port.tau) (formedState x).port).1
  refine ⟨rfl, ?_, ?_⟩
  · unfold arrival
    rw [beforeOut]
    unfold alignedState
    rw [before.2.1, before.2.2.1, blocked]
    cases x.port.tau <;> rfl
  · unfold arrival
    rw [afterOut]
    unfold alignedState
    rw [after.2.1, after.2.2.1]
    change arrivalAt (!x.port.tau) x.port.tau false = true
    cases x.port.tau <;> rfl

end Generative.InquirySufficiency.ContactFormation

#print axioms Generative.InquirySufficiency.ContactFormation.Formed
#print axioms Generative.InquirySufficiency.ContactFormation.FormFailure
#print axioms Generative.InquirySufficiency.ContactFormation.FormResult
#print axioms Generative.InquirySufficiency.ContactFormation.openContact
#print axioms Generative.InquirySufficiency.ContactFormation.finishForm
#print axioms Generative.InquirySufficiency.ContactFormation.form
#print axioms Generative.InquirySufficiency.ContactFormation.formedState
#print axioms Generative.InquirySufficiency.ContactFormation.Event
#print axioms Generative.InquirySufficiency.ContactFormation.process
#print axioms Generative.InquirySufficiency.ContactFormation.formCount
#print axioms Generative.InquirySufficiency.ContactFormation.form_complete
#print axioms Generative.InquirySufficiency.ContactFormation.form_complete_iff
#print axioms Generative.InquirySufficiency.ContactFormation.form_capacity_stops
#print axioms Generative.InquirySufficiency.ContactFormation.form_reserve_stops
#print axioms Generative.InquirySufficiency.ContactFormation.form_no_spare_still_draws
#print axioms Generative.InquirySufficiency.ContactFormation.formed_effects
#print axioms Generative.InquirySufficiency.ContactFormation.failed_formation_retains_contact
#print axioms Generative.InquirySufficiency.ContactFormation.formation_sets_open_class
#print axioms Generative.InquirySufficiency.ContactFormation.formation_leaves_class_C
#print axioms Generative.InquirySufficiency.ContactFormation.formation_changes_profile
#print axioms Generative.InquirySufficiency.ContactFormation.native_trace_retains_contact
#print axioms Generative.InquirySufficiency.ContactFormation.native_history_cannot_leave_C
#print axioms Generative.InquirySufficiency.ContactFormation.opening_requires_formation
#print axioms Generative.InquirySufficiency.ContactFormation.spare_accounting
#print axioms Generative.InquirySufficiency.ContactFormation.formations_bounded_by_spares
#print axioms Generative.InquirySufficiency.ContactFormation.formation_changes_aligned_arrival
