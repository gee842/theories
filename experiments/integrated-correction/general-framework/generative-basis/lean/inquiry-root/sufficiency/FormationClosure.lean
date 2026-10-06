import ContactFormation

/-!
# Closing the packet-law track: formation from the port's own failures

Three results close the contact-formation track.

1. **A general formation law.** For any process and any coordinate its steps
   retain, every law read from that coordinate is constant along histories.
   Adding a separate family of formation events, any history that changes the
   coordinate contains a formation event. This is the conditional-universality
   form: it holds for every process meeting the retention condition, not only
   for the packet port.

2. **Spare pairs from the port's own failures.** The contact-formation module
   supplied an inherited spare stock. Here the stock starts empty. A supported
   recovery step turns ten units of recorded failed conversion (`wasted`) into
   one spare pair. The native `wasted` counter itself is never decremented; a
   separate `recovered` count is bounded by it. Every formation is therefore
   backed by failed transfers recorded in the same history.

3. **What evidence can and cannot decide.** A failed transfer leaves the same
   receipt and the same ledger whether the contact is blocked or open but
   misaligned. Retained accounting alone cannot identify blockage, and forming
   an already open contact draws reserve and a spare pair for no change. When
   the port is aligned to the output that differs from `tau`, the transfer
   identifies the contact exactly. That alignment uses phase and inversion
   knowledge that is not acquired here.

A single executed history then takes a blocked port with no spares through a
failed probe, recover and formation to an actual transfer.

Supplied: the recovery rate (ten wasted units per pair), its native interface
demand, and the contact-opening rule. The decision to recover or form is not
derived; it is the reason the evidence results are stated separately.
-/

namespace Generative.FormationLaw

universe u v w x y

variable {S : Type u} {A : Type v} {F : Type w} {K : Type x} {L : Type y}

/-- Every step of `P` retains the coordinate `π`. -/
def Retains (P : Process S A) (π : S → K) : Prop :=
  ∀ s a t, P.step s a t → π t = π s

theorem trace_retains {P : Process S A} {π : S → K} (retains : Retains P π)
    {s t : S} {actions : List A} (trace : Trace P s actions t) : π t = π s := by
  induction trace with
  | nil => rfl
  | cons step _ ih => exact ih.trans (retains _ _ _ step)

/-- Any law read from a retained coordinate is constant along every history. -/
theorem law_constant {P : Process S A} {π : S → K} (retains : Retains P π) (law : K → L)
    {s t : S} {actions : List A} (trace : Trace P s actions t) : law (π t) = law (π s) :=
  congrArg law (trace_retains retains trace)

/-- Ordinary activity together with a separate family of formation events. -/
def extend (P : Process S A) (Q : Process S F) : Process S (Sum A F) where
  step s e t := match e with
    | .inl a => P.step s a t
    | .inr f => Q.step s f t

def formations : List (Sum A F) → Nat
  | [] => 0
  | .inl _ :: rest => formations rest
  | .inr _ :: rest => formations rest + 1

theorem no_formation_retains {P : Process S A} {Q : Process S F} {π : S → K}
    (retains : Retains P π) {s t : S} {events : List (Sum A F)}
    (trace : Trace (extend P Q) s events t) (none : formations events = 0) : π t = π s := by
  induction trace with
  | nil => rfl
  | @cons s m t event rest step _ ih =>
    cases event with
    | inl a => exact (ih none).trans (retains _ _ _ step)
    | inr f => exact Nat.noConfusion none

/-- Changing a coordinate that activity retains requires a formation event. -/
theorem change_requires_formation {P : Process S A} {Q : Process S F} {π : S → K}
    (retains : Retains P π) {s t : S} {events : List (Sum A F)}
    (trace : Trace (extend P Q) s events t) (changed : π t = π s → False) :
    1 ≤ formations events := by
  cases counted : formations events with
  | zero => exact absurd (no_formation_retains retains trace counted) changed
  | succ n => exact Nat.succ_le_succ (Nat.zero_le n)

theorem law_change_requires_formation {P : Process S A} {Q : Process S F} {π : S → K}
    (retains : Retains P π) (law : K → L) {s t : S} {events : List (Sum A F)}
    (trace : Trace (extend P Q) s events t) (changed : law (π t) = law (π s) → False) :
    1 ≤ formations events :=
  change_requires_formation retains trace (fun same => changed (congrArg law same))

end Generative.FormationLaw

namespace Generative.InquirySufficiency.FormationClosure

open Generative NativePacketProcess PacketLawDerivation OnePacketQuestions
open FormationLaw

/-- The native port with its spare pairs and the pairs already recovered. -/
structure Port where
  native : NativePacketProcess.State
  spare : Nat
  recovered : Nat

inductive Outcome where
  | complete (port : Port)
  | stopped (port : Port)

def finishRecovery (x : Port) (ready : NativePacketProcess.State) : Outcome :=
  if 10 * (x.recovered + 1) ≤ ready.wasted then .complete ⟨ready, x.spare + 1, x.recovered + 1⟩
  else .stopped ⟨ready, x.spare, x.recovered⟩

/-- Meet the native interface demand, then recover a pair from ten unrecovered wasted units. -/
def recover (x : Port) : Outcome :=
  match charge x.native with
  | .capacity => .stopped x
  | .funding => .stopped x
  | .paid ready => finishRecovery x ready

/-- Contact formation exactly as in `ContactFormation`, carrying the recover count. -/
def formPort (x : Port) : Outcome :=
  match ContactFormation.form ⟨x.native, x.spare⟩ with
  | .complete y => .complete ⟨y.port, y.spare, x.recovered⟩
  | .stopped y _ => .stopped ⟨y.port, y.spare, x.recovered⟩

def activity : Process Port (Sum NativePacketProcess.Command Unit) where
  step x e y := match e with
    | .inl command => (∃ o, execute x.native command = .complete y.native o) ∧
        y.spare = x.spare ∧ y.recovered = x.recovered
    | .inr _ => recover x = .complete y

def formation : Process Port Unit where
  step x _ y := formPort x = .complete y

abbrev Event := Sum (Sum NativePacketProcess.Command Unit) Unit

def process : Process Port Event := extend activity formation

def recoveries : List Event → Nat
  | [] => 0
  | .inl (.inl _) :: rest => recoveries rest
  | .inl (.inr _) :: rest => recoveries rest + 1
  | .inr _ :: rest => recoveries rest

def contact (x : Port) : Bool × Bool := (x.native.tau, x.native.blocked)

theorem recover_complete_iff (x y : Port) :
    recover x = .complete y ↔
      Payable x.native ∧ 10 * (x.recovered + 1) ≤ x.native.wasted ∧
        y = ⟨debit x.native, x.spare + 1, x.recovered + 1⟩ := by
  constructor
  · intro completed
    unfold recover at completed
    generalize interface : charge x.native = payment at completed
    cases payment with
    | capacity => cases completed
    | funding => cases completed
    | paid ready =>
      obtain ⟨sustained, equality⟩ := (charge_paid_iff x.native ready).mp interface
      cases equality
      dsimp only at completed
      unfold finishRecovery at completed
      by_cases backed : 10 * (x.recovered + 1) ≤ (debit x.native).wasted
      · rw [if_pos backed] at completed
        cases completed
        exact ⟨sustained, backed, rfl⟩
      · rw [if_neg backed] at completed
        cases completed
  · rintro ⟨sustained, backed, rfl⟩
    unfold recover
    rw [charge_paid x.native sustained.1 sustained.2]
    dsimp only
    unfold finishRecovery
    rw [if_pos (show 10 * (x.recovered + 1) ≤ (debit x.native).wasted from backed)]

theorem formPort_complete_iff (x y : Port) :
    formPort x = .complete y ↔
      Payable x.native ∧ 1 ≤ x.spare ∧
        y = ⟨ContactFormation.openContact (debit x.native), x.spare - 1, x.recovered⟩ := by
  constructor
  · intro completed
    unfold formPort at completed
    generalize formed : ContactFormation.form ⟨x.native, x.spare⟩ = result at completed
    cases result with
    | complete z =>
      obtain ⟨sustained, pair, rfl⟩ := (ContactFormation.form_complete_iff _ z).mp formed
      cases completed
      exact ⟨sustained, pair, rfl⟩
    | stopped z reason => cases completed
  · rintro ⟨sustained, pair, rfl⟩
    unfold formPort
    rw [ContactFormation.form_complete ⟨x.native, x.spare⟩ sustained pair]
    rfl

/-- Native calls and recover never change inversion or contact. -/
theorem activity_retains_contact : Retains activity contact := by
  intro x e y step
  cases e with
  | inl command =>
    obtain ⟨⟨_, actual⟩, _, _⟩ := step
    have same := completed_retains_parameters actual
    show (y.native.tau, y.native.blocked) = (x.native.tau, x.native.blocked)
    rw [same.1, same.2.2.2.1]
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
    rfl

/-- The A/B/C class changes in a history only if that history forms a contact. -/
theorem class_change_requires_formation {x y : Port} {events : List Event}
    (trace : Trace process x events y)
    (changed : targetOf y.native.tau y.native.blocked = targetOf x.native.tau x.native.blocked → False) :
    1 ≤ formations events :=
  law_change_requires_formation activity_retains_contact (fun c => targetOf c.1 c.2) trace changed

theorem completed_native_wasted_monotone {s t : NativePacketProcess.State}
    {command : NativePacketProcess.Command} {o : Observation}
    (actual : execute s command = .complete t o) : s.wasted ≤ t.wasted := by
  cases command with
  | probe =>
    obtain ⟨_, rfl, _⟩ := (probe_complete_iff s t o).mp actual
    rw [(probe_final_effects s).2.2.2.2.2.2]
    exact Nat.le_add_right _ _
  | a =>
    unfold execute at actual
    generalize interface : charge s = payment at actual
    cases payment with
    | capacity => cases actual
    | funding => cases actual
    | paid ready =>
      obtain ⟨_, rfl⟩ := (charge_paid_iff s ready).mp interface
      cases actual
      exact Nat.le_refl _
  | reset =>
    unfold execute at actual
    generalize interface : charge s = payment at actual
    cases payment with
    | capacity => cases actual
    | funding => cases actual
    | paid ready =>
      obtain ⟨_, rfl⟩ := (charge_paid_iff s ready).mp interface
      cases actual
      exact Nat.le_refl _
  | read =>
    unfold execute at actual
    generalize interface : charge s = payment at actual
    cases payment with
    | capacity => cases actual
    | funding => cases actual
    | paid ready =>
      obtain ⟨_, rfl⟩ := (charge_paid_iff s ready).mp interface
      cases actual
      exact Nat.le_refl _

/-- Recovered pairs never exceed a tenth of the recorded failed conversion. -/
def Backed (x : Port) : Prop := 10 * x.recovered ≤ x.native.wasted

theorem step_preserves_backing {x y : Port} {event : Event}
    (step : process.step x event y) (backed : Backed x) : Backed y := by
  cases event with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨_, actual⟩, _, kept⟩ := step
      unfold Backed
      rw [kept]
      exact Nat.le_trans backed (completed_native_wasted_monotone actual)
    | inr _ =>
      obtain ⟨_, enough, rfl⟩ := (recover_complete_iff x y).mp step
      exact enough
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
    exact backed

theorem trace_preserves_backing {x y : Port} {events : List Event}
    (trace : Trace process x events y) (backed : Backed x) : Backed y := by
  induction trace with
  | nil => exact backed
  | cons step _ ih => exact ih (step_preserves_backing step backed)

/-- Exact pair ledger: spares come only from recover and leave only by formation. -/
theorem pair_ledger {x y : Port} {events : List Event} (trace : Trace process x events y) :
    y.spare + formations events = x.spare + recoveries events ∧
      y.recovered = x.recovered + recoveries events := by
  induction trace with
  | nil => exact ⟨rfl, rfl⟩
  | @cons s m t event rest step _ ih =>
    cases event with
    | inl e =>
      cases e with
      | inl command =>
        obtain ⟨_, spare, kept⟩ := step
        change t.spare + formations rest = s.spare + recoveries rest ∧
          t.recovered = s.recovered + recoveries rest
        rw [← spare, ← kept]
        exact ih
      | inr _ =>
        obtain ⟨_, _, rfl⟩ := (recover_complete_iff s m).mp step
        change t.spare + formations rest = s.spare + (recoveries rest + 1) ∧
          t.recovered = s.recovered + (recoveries rest + 1)
        rw [ih.1, ih.2]
        exact ⟨Nat.add_right_comm _ _ _, Nat.add_right_comm _ _ _⟩
    | inr _ =>
      obtain ⟨_, pair, rfl⟩ := (formPort_complete_iff s m).mp step
      change t.spare + (formations rest + 1) = s.spare + recoveries rest ∧
        t.recovered = s.recovered + recoveries rest
      refine ⟨?_, ih.2⟩
      rw [← Nat.add_assoc, ih.1, Nat.add_right_comm]
      exact congrArg (· + recoveries rest) (sub_add_cancel_constructive s.spare 1 pair)

/-- From an empty stock, every formation is backed by ten units of failed
conversion recorded in the same history. -/
theorem formations_backed_by_failures {x y : Port} {events : List Event}
    (trace : Trace process x events y) (noSpare : x.spare = 0) (noRecovery : x.recovered = 0)
    (noWaste : x.native.wasted = 0) :
    formations events ≤ recoveries events ∧ 10 * recoveries events ≤ y.native.wasted := by
  have ledger := pair_ledger trace
  have backed := trace_preserves_backing trace (by
    unfold Backed
    rw [noRecovery, noWaste]
    exact Nat.le_refl 0)
  rw [noSpare, Nat.zero_add] at ledger
  refine ⟨?_, ?_⟩
  · rw [← ledger.1]
    exact Nat.le_add_left _ _
  · unfold Backed at backed
    rw [ledger.2, noRecovery, Nat.zero_add] at backed
    exact backed

theorem arrival_false_of_blocked (s : NativePacketProcess.State) (blocked : s.blocked = true) :
    arrival s = false := by
  unfold arrival arrivalAt
  rw [blocked]
  cases (output s.phase != s.tau) <;> rfl

theorem arrival_false_of_misaligned (s : NativePacketProcess.State)
    (misaligned : output s.phase = s.tau) : arrival s = false := by
  unfold arrival arrivalAt
  rw [misaligned]
  cases s.tau <;> rfl

/-- A blocked contact and an open but misaligned contact leave the same receipt
and the same ledger after a probe. Accounting cannot tell them apart. -/
theorem failed_transfer_indistinguishable (s : NativePacketProcess.State)
    (misaligned : output s.phase = s.tau) :
    let blockedPort := { s with blocked := true }
    let openPort := ContactFormation.openContact s
    receiptBit blockedPort = receiptBit openPort ∧
      (probeFinal blockedPort).wasted = (probeFinal openPort).wasted ∧
      (probeFinal blockedPort).transferred = (probeFinal openPort).transferred ∧
      (probeFinal blockedPort).fuel = (probeFinal openPort).fuel ∧
      (probeFinal blockedPort).income = (probeFinal openPort).income ∧
      (probeFinal blockedPort).source = (probeFinal openPort).source ∧
      targetOf blockedPort.tau blockedPort.blocked ≠ targetOf openPort.tau openPort.blocked := by
  have closed : arrival { s with blocked := true } = false :=
    arrival_false_of_blocked { s with blocked := true } rfl
  have missed : arrival (ContactFormation.openContact s) = false :=
    arrival_false_of_misaligned (ContactFormation.openContact s) misaligned
  refine ⟨?_, ?_, ?_, ?_, ?_, rfl, ?_⟩
  · unfold receiptBit
    rw [closed, missed]
    rfl
  · rw [(probe_final_effects _).2.2.2.2.2.2, (probe_final_effects _).2.2.2.2.2.2, closed, missed]
    rfl
  · rw [(probe_final_effects _).2.2.2.2.2.1, (probe_final_effects _).2.2.2.2.2.1, closed, missed]
    rfl
  · rw [(probe_final_effects _).2.2.1, (probe_final_effects _).2.2.1]
    unfold gain
    rw [closed, missed]
    rfl
  · rw [(probe_final_effects _).2.2.2.2.1, (probe_final_effects _).2.2.2.2.1]
    unfold gain
    rw [closed, missed]
    rfl
  · change targetOf s.tau true ≠ targetOf s.tau false
    cases s.tau <;> exact fun same => by cases same

/-- Forming an already open contact draws reserve and a pair and changes no class. -/
theorem redundant_formation_draws (x y : Port) (open_ : x.native.blocked = false)
    (formed : formPort x = .complete y) :
    targetOf y.native.tau y.native.blocked = targetOf x.native.tau x.native.blocked ∧
      y.native.fuel = x.native.fuel - bill x.native ∧ y.spare = x.spare - 1 := by
  obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp formed
  refine ⟨?_, rfl, rfl⟩
  change targetOf x.native.tau false = targetOf x.native.tau x.native.blocked
  rw [open_]

/-- Aligned to the output that differs from `tau`, a transfer identifies the contact. -/
theorem aligned_transfer_identifies_contact (s : NativePacketProcess.State)
    (aligned : output s.phase = !s.tau) :
    arrival s = !s.blocked ∧
      (probeFinal s).transferred = s.transferred + (if s.blocked then 0 else 10) := by
  have identifies : arrival s = !s.blocked := by
    unfold arrival arrivalAt
    rw [aligned]
    cases s.tau <;> cases s.blocked <;> rfl
  refine ⟨identifies, ?_⟩
  rw [(probe_final_effects s).2.2.2.2.2.1, identifies]
  cases s.blocked <;> rfl

def completeNative (x : Port) : Result → Option Port
  | .complete t _ => some ⟨t, x.spare, x.recovered⟩
  | .stopped _ _ => none

def completeOutcome : Outcome → Option Port
  | .complete y => some y
  | .stopped _ => none

/-- One executed step, returning the reached state only on completion. -/
def runEvent (x : Port) : Event → Option Port
  | .inl (.inl command) => completeNative x (execute x.native command)
  | .inl (.inr _) => completeOutcome (recover x)
  | .inr _ => completeOutcome (formPort x)

def run (x : Port) : List Event → Option Port
  | [] => some x
  | event :: rest => match runEvent x event with
    | some y => run y rest
    | none => none

theorem completeNative_some {x y : Port} {result : Result}
    (completed : completeNative x result = some y) :
    (∃ o, result = .complete y.native o) ∧ y.spare = x.spare ∧ y.recovered = x.recovered := by
  cases result with
  | complete t o =>
    cases completed
    exact ⟨⟨o, rfl⟩, rfl, rfl⟩
  | stopped t reason => cases completed

theorem completeOutcome_some {y : Port} {result : Outcome}
    (completed : completeOutcome result = some y) : result = .complete y := by
  cases result with
  | complete z =>
    cases completed
    rfl
  | stopped z => cases completed

theorem runEvent_sound {x y : Port} {event : Event} (ran : runEvent x event = some y) :
    process.step x event y := by
  cases event with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨o, actual⟩, spare, kept⟩ := completeNative_some (x := x) ran
      exact ⟨⟨o, actual⟩, spare, kept⟩
    | inr u => exact completeOutcome_some ran
  | inr u => exact completeOutcome_some ran

theorem run_sound {x y : Port} {events : List Event} (ran : run x events = some y) :
    Trace process x events y := by
  induction events generalizing x with
  | nil =>
    cases ran
    exact .nil _
  | cons event rest ih =>
    unfold run at ran
    split at ran
    next m stepped => exact .cons (runEvent_sound stepped) (ih ran)
    next => cases ran

def nativeE (command : NativePacketProcess.Command) : Event := .inl (.inl command)
def recoverE : Event := .inl (.inr ())
def formE : Event := .inr ()

/-- A blocked port with no spare pairs and an empty ledger. -/
def start : Port :=
  ⟨{ phase := .p0, tau := false, sigma := false, broken := false, blocked := true,
     receiptFlip := false, source := 20, fuel := 200000, live := 0, workspace := 0,
     capacity := 10, spent := 0, income := 0, transferred := 0, wasted := 0 }, 0, 0⟩

/-- Align to the arriving output, probe and fail, recover the waste, form, probe again. -/
def history : List Event :=
  [nativeE .a, nativeE .a, nativeE .probe, recoverE, formE, nativeE .probe]

/-- The blocked contact's own failed transfer supplies the pair that opens it,
and the same probe then transfers. -/
theorem failure_opens_contact :
    ∃ y, run start history = some y ∧ Trace process start history y ∧
      targetOf start.native.tau start.native.blocked = .C ∧
      targetOf y.native.tau y.native.blocked = .A ∧
      y.native.transferred = 10 ∧ y.native.wasted = 10 ∧ y.native.source = 0 ∧
      y.spare = 0 ∧ y.recovered = 1 ∧ formations history = 1 ∧ recoveries history = 1 := by
  refine ⟨_, rfl, run_sound rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

/-- Without formation the same port stays class C after any native history. -/
theorem start_native_history_stays_C {t : NativePacketProcess.State}
    {commands : List NativePacketProcess.Command}
    (trace : Trace NativePacketProcess.process start.native commands t) :
    targetOf t.tau t.blocked = .C :=
  ContactFormation.native_history_cannot_leave_C trace rfl

end Generative.InquirySufficiency.FormationClosure

#print axioms Generative.FormationLaw.Retains
#print axioms Generative.FormationLaw.trace_retains
#print axioms Generative.FormationLaw.law_constant
#print axioms Generative.FormationLaw.extend
#print axioms Generative.FormationLaw.formations
#print axioms Generative.FormationLaw.no_formation_retains
#print axioms Generative.FormationLaw.change_requires_formation
#print axioms Generative.FormationLaw.law_change_requires_formation
#print axioms Generative.InquirySufficiency.FormationClosure.Port
#print axioms Generative.InquirySufficiency.FormationClosure.Outcome
#print axioms Generative.InquirySufficiency.FormationClosure.finishRecovery
#print axioms Generative.InquirySufficiency.FormationClosure.recover
#print axioms Generative.InquirySufficiency.FormationClosure.formPort
#print axioms Generative.InquirySufficiency.FormationClosure.activity
#print axioms Generative.InquirySufficiency.FormationClosure.formation
#print axioms Generative.InquirySufficiency.FormationClosure.process
#print axioms Generative.InquirySufficiency.FormationClosure.recoveries
#print axioms Generative.InquirySufficiency.FormationClosure.contact
#print axioms Generative.InquirySufficiency.FormationClosure.recover_complete_iff
#print axioms Generative.InquirySufficiency.FormationClosure.formPort_complete_iff
#print axioms Generative.InquirySufficiency.FormationClosure.activity_retains_contact
#print axioms Generative.InquirySufficiency.FormationClosure.class_change_requires_formation
#print axioms Generative.InquirySufficiency.FormationClosure.completed_native_wasted_monotone
#print axioms Generative.InquirySufficiency.FormationClosure.Backed
#print axioms Generative.InquirySufficiency.FormationClosure.step_preserves_backing
#print axioms Generative.InquirySufficiency.FormationClosure.trace_preserves_backing
#print axioms Generative.InquirySufficiency.FormationClosure.pair_ledger
#print axioms Generative.InquirySufficiency.FormationClosure.formations_backed_by_failures
#print axioms Generative.InquirySufficiency.FormationClosure.arrival_false_of_blocked
#print axioms Generative.InquirySufficiency.FormationClosure.arrival_false_of_misaligned
#print axioms Generative.InquirySufficiency.FormationClosure.failed_transfer_indistinguishable
#print axioms Generative.InquirySufficiency.FormationClosure.redundant_formation_draws
#print axioms Generative.InquirySufficiency.FormationClosure.aligned_transfer_identifies_contact
#print axioms Generative.InquirySufficiency.FormationClosure.completeNative
#print axioms Generative.InquirySufficiency.FormationClosure.completeOutcome
#print axioms Generative.InquirySufficiency.FormationClosure.runEvent
#print axioms Generative.InquirySufficiency.FormationClosure.completeNative_some
#print axioms Generative.InquirySufficiency.FormationClosure.completeOutcome_some
#print axioms Generative.InquirySufficiency.FormationClosure.run
#print axioms Generative.InquirySufficiency.FormationClosure.runEvent_sound
#print axioms Generative.InquirySufficiency.FormationClosure.run_sound
#print axioms Generative.InquirySufficiency.FormationClosure.nativeE
#print axioms Generative.InquirySufficiency.FormationClosure.recoverE
#print axioms Generative.InquirySufficiency.FormationClosure.formE
#print axioms Generative.InquirySufficiency.FormationClosure.start
#print axioms Generative.InquirySufficiency.FormationClosure.history
#print axioms Generative.InquirySufficiency.FormationClosure.failure_opens_contact
#print axioms Generative.InquirySufficiency.FormationClosure.start_native_history_stays_C
