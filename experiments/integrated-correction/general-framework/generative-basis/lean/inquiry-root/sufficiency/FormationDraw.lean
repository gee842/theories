import FormationClosure
import PhasePeriodSelection

/-!
# Formation and recovery draw what every native operation draws

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
FORMATION-DRAW.md.

`ContactFormation` and `FormationClosure` let formation and recovery draw the
native amount `bill` and list that choice as supplied. This module asks whether
it follows from the native activity.

1. **One draw per operation, natively.** `PhasePeriodSelection.sensing_command_draws`
   proves that a completed `a`, `read` or `reset` draws exactly `bill`. A
   completed probe makes two such draws, one before and one after its
   conversion (`native_operation_draw`). So the native activity already has one
   draw law: each operation draws `bill`, whatever the command, and `bill` stays
   fixed along every completed history.
2. **The closure process keeps that one law.** With formation and recovery drawing
   `bill`, every event of the closure process, native or not, draws its number
   of operations times `bill` (`closure_one_draw_law`, `closure_trace_draw`).
3. **Any other draw breaks it.** Formation and recovery are stated with an open
   draw (`formWith`, `recoverWith`; with `bill` they are the supplied ones,
   `formWith_native`, `recoverWith_native`). If the extended process has any single
   draw law at all, that law equals `bill` on every state where a native command
   completes (`one_law_is_native_draw`), and then formation and recovery must draw
   `bill` wherever they and a native command both complete
   (`one_law_forces_formation_draw`, `one_law_forces_recovery_draw`). A free
   formation has no single draw law (`free_formation_breaks_one_law`).

Scope. The claim that fixes the draw is that the extended process has one draw
law for all its operations, as the native activity already does for its four
commands. Under that claim the draw is derived; without it, the countercase
shows that a separately chosen formation draw is consistent with the port and
splits its draw into two laws. Why each native operation draws `16384 + peak`
is inherited from the port and not derived here.
-/

namespace Generative.InquirySufficiency.FormationDraw

open Generative NativePacketProcess PacketLawDerivation FormationClosure
open FormationLaw

/-! ## 1. The native draw law -/

/-- Left cancellation, proved without `propext`. -/
theorem cancel_left : ∀ (a : Nat) {b c : Nat}, a + b = a + c → b = c
  | 0, b, c, h => by
    rw [Nat.zero_add, Nat.zero_add] at h
    exact h
  | a + 1, b, c, h => by
    rw [Nat.succ_add, Nat.succ_add] at h
    exact cancel_left a (Nat.succ.inj h)

/-- Right distribution, proved without `propext`. -/
theorem add_mul_right (a b c : Nat) : (a + b) * c = a * c + b * c := by
  rw [Nat.mul_comm, Nat.mul_add, Nat.mul_comm c a, Nat.mul_comm c b]

/-- Draws a completed native command makes: one, or two for a probe. -/
def operations : NativePacketProcess.Command → Nat
  | .probe => 2
  | .a => 1
  | .reset => 1
  | .read => 1

theorem native_operation_draw {s t : NativePacketProcess.State}
    {command : NativePacketProcess.Command} {o : Observation}
    (actual : execute s command = .complete t o) :
    t.spent = s.spent + operations command * bill s ∧ bill t = bill s := by
  cases command with
  | probe =>
    obtain ⟨_, rfl, _⟩ := (probe_complete_iff s t o).mp actual
    refine ⟨?_, rfl⟩
    rw [(probe_final_effects s).2.2.2.1]
    change s.spent + bill s + bill s = s.spent + 2 * bill s
    rw [Nat.two_mul, Nat.add_assoc]
  | a =>
    obtain ⟨drawn, same, _, _⟩ :=
      PhasePeriodSelection.sensing_command_draws s t .a o rfl actual
    refine ⟨?_, same⟩
    rw [drawn]
    change s.spent + bill s = s.spent + 1 * bill s
    rw [Nat.one_mul]
  | reset =>
    obtain ⟨drawn, same, _, _⟩ :=
      PhasePeriodSelection.sensing_command_draws s t .reset o rfl actual
    refine ⟨?_, same⟩
    rw [drawn]
    change s.spent + bill s = s.spent + 1 * bill s
    rw [Nat.one_mul]
  | read =>
    obtain ⟨drawn, same, _, _⟩ :=
      PhasePeriodSelection.sensing_command_draws s t .read o rfl actual
    refine ⟨?_, same⟩
    rw [drawn]
    change s.spent + bill s = s.spent + 1 * bill s
    rw [Nat.one_mul]

/-! ## 2. Formation and recovery with an open draw -/

def drawWith (draw : NativePacketProcess.State → Nat) (s : NativePacketProcess.State) :
    NativePacketProcess.State :=
  { s with fuel := s.fuel - draw s, spent := s.spent + draw s }

def attemptDraw (draw : NativePacketProcess.State → Nat) (s : NativePacketProcess.State) :
    Payment :=
  if peak s ≤ s.capacity then
    if draw s ≤ s.fuel then .paid (drawWith draw s) else .funding
  else .capacity

theorem attemptDraw_native : attemptDraw bill = charge := rfl

theorem attemptDraw_held_iff (draw : NativePacketProcess.State → Nat)
    (s t : NativePacketProcess.State) :
    attemptDraw draw s = .paid t ↔
      (peak s ≤ s.capacity ∧ draw s ≤ s.fuel) ∧ t = drawWith draw s := by
  unfold attemptDraw
  by_cases capacity : peak s ≤ s.capacity
  · rw [if_pos capacity]
    by_cases funding : draw s ≤ s.fuel
    · rw [if_pos funding]
      constructor
      · intro h
        cases h
        exact ⟨⟨capacity, funding⟩, rfl⟩
      · rintro ⟨_, rfl⟩
        rfl
    · rw [if_neg funding]
      constructor
      · intro h
        cases h
      · intro h
        exact absurd h.1.2 funding
  · rw [if_neg capacity]
    constructor
    · intro h
      cases h
    · intro h
      exact absurd h.1.1 capacity

def formWith (draw : NativePacketProcess.State → Nat) (x : Port) : Outcome :=
  match attemptDraw draw x.native with
  | .capacity => .stopped x
  | .funding => .stopped x
  | .paid ready =>
    if 1 ≤ x.spare then .complete ⟨ContactFormation.openContact ready, x.spare - 1, x.recovered⟩
    else .stopped ⟨ready, x.spare, x.recovered⟩

def recoverWith (draw : NativePacketProcess.State → Nat) (x : Port) : Outcome :=
  match attemptDraw draw x.native with
  | .capacity => .stopped x
  | .funding => .stopped x
  | .paid ready => finishRecovery x ready

theorem recoverWith_native (x : Port) : recoverWith bill x = recover x := rfl

theorem formWith_native (x : Port) : formWith bill x = formPort x := by
  unfold formWith formPort ContactFormation.form
  rw [attemptDraw_native]
  cases charge x.native with
  | capacity => rfl
  | funding => rfl
  | paid ready =>
    dsimp only
    unfold ContactFormation.finishForm
    by_cases pair : 1 ≤ x.spare
    · rw [if_pos pair, if_pos pair]
    · rw [if_neg pair, if_neg pair]

theorem formWith_complete_iff (draw : NativePacketProcess.State → Nat) (x y : Port) :
    formWith draw x = .complete y ↔
      (peak x.native ≤ x.native.capacity ∧ draw x.native ≤ x.native.fuel) ∧ 1 ≤ x.spare ∧
        y = ⟨ContactFormation.openContact (drawWith draw x.native), x.spare - 1, x.recovered⟩ := by
  constructor
  · intro completed
    unfold formWith at completed
    generalize paid : attemptDraw draw x.native = payment at completed
    cases payment with
    | capacity => cases completed
    | funding => cases completed
    | paid ready =>
      obtain ⟨met, rfl⟩ := (attemptDraw_held_iff draw x.native ready).mp paid
      dsimp only at completed
      by_cases pair : 1 ≤ x.spare
      · rw [if_pos pair] at completed
        cases completed
        exact ⟨met, pair, rfl⟩
      · rw [if_neg pair] at completed
        cases completed
  · rintro ⟨met, pair, rfl⟩
    unfold formWith
    rw [(attemptDraw_held_iff draw x.native _).mpr ⟨met, rfl⟩]
    dsimp only
    rw [if_pos pair]

theorem recoverWith_complete_iff (draw : NativePacketProcess.State → Nat) (x y : Port) :
    recoverWith draw x = .complete y ↔
      (peak x.native ≤ x.native.capacity ∧ draw x.native ≤ x.native.fuel) ∧
        10 * (x.recovered + 1) ≤ x.native.wasted ∧
        y = ⟨drawWith draw x.native, x.spare + 1, x.recovered + 1⟩ := by
  constructor
  · intro completed
    unfold recoverWith at completed
    generalize paid : attemptDraw draw x.native = payment at completed
    cases payment with
    | capacity => cases completed
    | funding => cases completed
    | paid ready =>
      obtain ⟨met, rfl⟩ := (attemptDraw_held_iff draw x.native ready).mp paid
      dsimp only at completed
      unfold finishRecovery at completed
      by_cases backed : 10 * (x.recovered + 1) ≤ (drawWith draw x.native).wasted
      · rw [if_pos backed] at completed
        cases completed
        exact ⟨met, backed, rfl⟩
      · rw [if_neg backed] at completed
        cases completed
  · rintro ⟨met, backed, rfl⟩
    unfold recoverWith
    rw [(attemptDraw_held_iff draw x.native _).mpr ⟨met, rfl⟩]
    dsimp only
    unfold finishRecovery
    rw [if_pos (show 10 * (x.recovered + 1) ≤ (drawWith draw x.native).wasted from backed)]

/-- The closure process with formation and recovery drawing `formDraw` and
`recoverDraw`. With `bill` for both it has exactly the closure steps. -/
def processWith (formDraw recoverDraw : NativePacketProcess.State → Nat) :
    Process Port FormationClosure.Event where
  step x e y := match e with
    | .inl (.inl command) => (∃ o, execute x.native command = .complete y.native o) ∧
        y.spare = x.spare ∧ y.recovered = x.recovered
    | .inl (.inr _) => recoverWith recoverDraw x = .complete y
    | .inr _ => formWith formDraw x = .complete y

theorem processWith_native_step (x y : Port) (e : FormationClosure.Event) :
    (processWith bill bill).step x e y ↔ FormationClosure.process.step x e y := by
  cases e with
  | inl e =>
    cases e with
    | inl command => exact Iff.rfl
    | inr _ =>
      change recoverWith bill x = .complete y ↔ recover x = .complete y
      rw [recoverWith_native]
  | inr _ =>
    change formWith bill x = .complete y ↔ formPort x = .complete y
    rw [formWith_native]

/-- Operations an event of the extended process makes. -/
def eventOperations : FormationClosure.Event → Nat
  | .inl (.inl command) => operations command
  | .inl (.inr _) => 1
  | .inr _ => 1

/-- One draw law: every event draws its operations times one amount `amount`. -/
def OneDrawLaw (P : Process Port FormationClosure.Event)
    (amount : NativePacketProcess.State → Nat) : Prop :=
  ∀ x e y, P.step x e y →
    y.native.spent = x.native.spent + eventOperations e * amount x.native

/-! ## 3. The closure process has one draw law -/

theorem closure_one_draw_law : OneDrawLaw (processWith bill bill) bill := by
  intro x e y step
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨_, actual⟩, _, _⟩ := step
      exact (native_operation_draw actual).1
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (recoverWith_complete_iff bill x y).mp step
      change x.native.spent + bill x.native = x.native.spent + 1 * bill x.native
      rw [Nat.one_mul]
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formWith_complete_iff bill x y).mp step
    change x.native.spent + bill x.native = x.native.spent + 1 * bill x.native
    rw [Nat.one_mul]

def totalOperations : List FormationClosure.Event → Nat
  | [] => 0
  | e :: rest => eventOperations e + totalOperations rest

theorem closure_step_keeps_amount {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) : bill y.native = bill x.native := by
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨_, actual⟩, _, _⟩ := step
      exact (native_operation_draw actual).2
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
      rfl
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
    rfl

/-- A completed closure history draws its operations times the fixed amount. -/
theorem closure_trace_draw {x y : Port} {events : List FormationClosure.Event}
    (trace : Trace FormationClosure.process x events y) :
    y.native.spent = x.native.spent + totalOperations events * bill x.native ∧
      bill y.native = bill x.native := by
  induction trace with
  | nil =>
    refine ⟨?_, rfl⟩
    change _ = _ + 0 * _
    rw [Nat.zero_mul, Nat.add_zero]
  | @cons s m t e rest step _ ih =>
    have law := closure_one_draw_law s e m ((processWith_native_step s m e).mpr step)
    have same := closure_step_keeps_amount step
    refine ⟨?_, ih.2.trans same⟩
    rw [ih.1, law, same]
    change s.native.spent + eventOperations e * bill s.native +
        totalOperations rest * bill s.native =
      s.native.spent + (eventOperations e + totalOperations rest) * bill s.native
    rw [add_mul_right, Nat.add_assoc]

/-! ## 4. One draw law fixes the formation and recovery draw -/

/-- A single draw law for the extended process equals the native draw on every
state where a native advance completes. -/
theorem one_law_is_native_draw {formDraw recoverDraw amount : NativePacketProcess.State → Nat}
    (law : OneDrawLaw (processWith formDraw recoverDraw) amount)
    (s : NativePacketProcess.State) (ready : Payable s) : amount s = bill s := by
  have step : (processWith formDraw recoverDraw).step ⟨s, 0, 0⟩ (.inl (.inl .a))
      ⟨{ debit s with phase := nextPhase s.phase }, 0, 0⟩ :=
    ⟨⟨_, a_complete s ready⟩, rfl, rfl⟩
  have drawn := law _ _ _ step
  change s.spent + bill s = s.spent + 1 * amount s at drawn
  rw [Nat.one_mul] at drawn
  exact (cancel_left _ drawn).symm

theorem one_law_forces_formation_draw
    {formDraw recoverDraw amount : NativePacketProcess.State → Nat}
    (law : OneDrawLaw (processWith formDraw recoverDraw) amount)
    (x : Port) (ready : Payable x.native) (covered : formDraw x.native ≤ x.native.fuel)
    (pair : 1 ≤ x.spare) : formDraw x.native = bill x.native := by
  have step : (processWith formDraw recoverDraw).step x (.inr ()) _ :=
    (formWith_complete_iff formDraw x _).mpr ⟨⟨ready.1, covered⟩, pair, rfl⟩
  have drawn := law _ _ _ step
  change x.native.spent + formDraw x.native = x.native.spent + 1 * amount x.native at drawn
  rw [Nat.one_mul, one_law_is_native_draw law x.native ready] at drawn
  exact cancel_left _ drawn

theorem one_law_forces_recovery_draw
    {formDraw recoverDraw amount : NativePacketProcess.State → Nat}
    (law : OneDrawLaw (processWith formDraw recoverDraw) amount)
    (x : Port) (ready : Payable x.native) (covered : recoverDraw x.native ≤ x.native.fuel)
    (backed : 10 * (x.recovered + 1) ≤ x.native.wasted) :
    recoverDraw x.native = bill x.native := by
  have step : (processWith formDraw recoverDraw).step x (.inl (.inr ())) _ :=
    (recoverWith_complete_iff recoverDraw x _).mpr ⟨⟨ready.1, covered⟩, backed, rfl⟩
  have drawn := law _ _ _ step
  change x.native.spent + recoverDraw x.native = x.native.spent + 1 * amount x.native at drawn
  rw [Nat.one_mul, one_law_is_native_draw law x.native ready] at drawn
  exact cancel_left _ drawn

/-- A blocked port with one spare pair, enough held amount and no dissipation yet. -/
def onePairPort : Port :=
  ⟨{ phase := .p0, tau := false, sigma := false, broken := false, blocked := true,
     receiptFlip := false, source := 0, fuel := 100000, live := 0, workspace := 0,
     capacity := 10, spent := 0, income := 0, transferred := 0, wasted := 0 }, 1, 0⟩

/-- A formation that draws nothing leaves the extended process without any
single draw law. -/
theorem free_formation_breaks_one_law :
    ¬ ∃ amount, OneDrawLaw (processWith (fun _ => 0) bill) amount := by
  rintro ⟨amount, law⟩
  have forced := one_law_forces_formation_draw law onePairPort
    ⟨show 2 ≤ 10 by decide, show 16386 ≤ 100000 by decide⟩
    (show 0 ≤ 100000 by decide) (show 1 ≤ 1 by decide)
  exact absurd forced (by decide)

end Generative.InquirySufficiency.FormationDraw

#print axioms Generative.InquirySufficiency.FormationDraw.cancel_left
#print axioms Generative.InquirySufficiency.FormationDraw.add_mul_right
#print axioms Generative.InquirySufficiency.FormationDraw.operations
#print axioms Generative.InquirySufficiency.FormationDraw.native_operation_draw
#print axioms Generative.InquirySufficiency.FormationDraw.drawWith
#print axioms Generative.InquirySufficiency.FormationDraw.attemptDraw
#print axioms Generative.InquirySufficiency.FormationDraw.attemptDraw_native
#print axioms Generative.InquirySufficiency.FormationDraw.attemptDraw_held_iff
#print axioms Generative.InquirySufficiency.FormationDraw.formWith
#print axioms Generative.InquirySufficiency.FormationDraw.recoverWith
#print axioms Generative.InquirySufficiency.FormationDraw.recoverWith_native
#print axioms Generative.InquirySufficiency.FormationDraw.formWith_native
#print axioms Generative.InquirySufficiency.FormationDraw.formWith_complete_iff
#print axioms Generative.InquirySufficiency.FormationDraw.recoverWith_complete_iff
#print axioms Generative.InquirySufficiency.FormationDraw.processWith
#print axioms Generative.InquirySufficiency.FormationDraw.processWith_native_step
#print axioms Generative.InquirySufficiency.FormationDraw.eventOperations
#print axioms Generative.InquirySufficiency.FormationDraw.OneDrawLaw
#print axioms Generative.InquirySufficiency.FormationDraw.closure_one_draw_law
#print axioms Generative.InquirySufficiency.FormationDraw.totalOperations
#print axioms Generative.InquirySufficiency.FormationDraw.closure_step_keeps_amount
#print axioms Generative.InquirySufficiency.FormationDraw.closure_trace_draw
#print axioms Generative.InquirySufficiency.FormationDraw.one_law_is_native_draw
#print axioms Generative.InquirySufficiency.FormationDraw.one_law_forces_formation_draw
#print axioms Generative.InquirySufficiency.FormationDraw.one_law_forces_recovery_draw
#print axioms Generative.InquirySufficiency.FormationDraw.onePairPort
#print axioms Generative.InquirySufficiency.FormationDraw.free_formation_breaks_one_law
