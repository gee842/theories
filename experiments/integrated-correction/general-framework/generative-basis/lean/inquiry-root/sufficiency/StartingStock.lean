import RecoveryQuantum
import FormationDraw

/-!
# What the start of the closure history must hold

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
STARTING-STOCK.md.

`FormationClosure.start` begins with no spare pairs, no recovered pairs,
nothing dissipated, 200000 held units (`held`) and 20 source units. This module
asks which of these starting amounts follow from the activity that starts there.

1. **Spare pairs: zero is forced.** From a beginning with nothing dissipated and
   nothing recovered, every formation in every later history is backed by ten
   dissipated units of a failed conversion in that history exactly when the
   starting spare stock is zero (`backing_iff_empty_stock`). Any inherited pair
   can be formed with nothing dissipated (`inherited_pair_forms_unbacked`). A
   recovered count above zero with nothing dissipated contradicts the native
   backing invariant (`nothing_dissipated_nothing_recovered`).
2. **Held amount: a minimum is forced, and computed.** If the held amount is below
   the per-operation draw, no event of the closure process completes
   (`nothing_held_nothing_proceeds`). Along any completed history, the held amount
   plus the cumulative draw is conserved up to arrival
   (`held_amount_conserved`); so a history that receives no arrival
   started with at least its operations times the draw
   (`held_covers_draws_before_arrival`). Every completed history converts ten
   source units per probe (`source_accounting`).
3. **The closure history's least start.** The history of `failure_opens_contact`
   completes from held amount `f` and source `S` only if `114702 ≤ f` and
   `20 ≤ S`, that is seven draws of 16386 and two conversions; it completes at
   exactly that amount, and stops with one unit less of either
   (`least_starting_stock`). The 200000 and 20 of the supplied start are one
   admissible start above this minimum, not further inputs to the result.

Scope. Whether there is any held amount or source at all is not derived: the
results show that without them nothing proceeds, and how much a given history
needs. That the activity begins with nothing dissipated and nothing recovered is
the meaning of a beginning used in part 1, not derived from the port.
-/

namespace Generative.InquirySufficiency.StartingStock

open Generative NativePacketProcess PacketLawDerivation FormationClosure
open FormationLaw RecoveryQuantum FormationDraw

/-! ## 1. The spare-pair stock -/

theorem nothing_dissipated_nothing_recovered (x : Port) (backed : Backed x)
    (empty : x.native.dissipated = 0) : x.recovered = 0 := by
  unfold Backed at backed
  rw [empty] at backed
  cases r : x.recovered with
  | zero => rfl
  | succ n =>
    rw [r, Nat.mul_succ] at backed
    exact absurd (Nat.le_trans (Nat.le_add_left 10 (10 * n)) backed) (by decide)

/-- With an inherited pair, formation completes with nothing dissipated. -/
theorem inherited_pair_forms_unbacked (x : Port) (ready : Supportable x.native)
    (pair : 1 ≤ x.spare) :
    ∃ y, Trace FormationClosure.process x [formE] y ∧ formations [formE] = 1 ∧
      y.native.dissipated = x.native.dissipated := by
  refine ⟨_, trace_singleton_iff.mpr ((formPort_complete_iff x _).mpr ⟨ready, pair, rfl⟩),
    rfl, rfl⟩

/-- Every formation of every later history is backed by a recorded failed conversion. -/
def FormationsBackedFrom (x : Port) : Prop :=
  ∀ events y, Trace FormationClosure.process x events y →
    10 * formations events ≤ y.native.dissipated

theorem backing_iff_empty_stock (x : Port) (ready : Supportable x.native)
    (noDissipation : x.native.dissipated = 0) (noRecovery : x.recovered = 0) :
    FormationsBackedFrom x ↔ x.spare = 0 := by
  constructor
  · intro backed
    cases stock : x.spare with
    | zero => rfl
    | succ n =>
      have pair : 1 ≤ x.spare := by rw [stock]; exact Nat.succ_le_succ (Nat.zero_le n)
      obtain ⟨y, trace, _, same⟩ := inherited_pair_forms_unbacked x ready pair
      have bound := backed _ _ trace
      rw [same, noDissipation] at bound
      exact absurd bound (by decide)
  · intro empty events y trace
    obtain ⟨formed, recovered⟩ :=
      formations_backed_by_failures trace empty noRecovery noDissipation
    exact Nat.le_trans (Nat.mul_le_mul_left 10 formed) recovered

/-! ## 2. The held amount -/

theorem execute_complete_covered {s t : NativePacketProcess.State}
    {command : NativePacketProcess.Command} {o : Observation}
    (actual : execute s command = .complete t o) : Supportable s := by
  unfold execute at actual
  generalize interface : support s = result at actual
  cases result with
  | capacity => cases actual
  | insufficient => cases actual
  | sustained ready => exact ((support_sustained_iff s ready).mp interface).1

theorem step_covered {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) : Supportable x.native := by
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨_, actual⟩, _, _⟩ := step
      exact execute_complete_covered actual
    | inr _ => exact ((recover_complete_iff x y).mp step).1
  | inr _ => exact ((formPort_complete_iff x y).mp step).1

/-- Below one draw, no event of the closure process completes. -/
theorem nothing_held_nothing_proceeds (x : Port) (short : x.native.held < draw x.native)
    (e : FormationClosure.Event) (y : Port) : ¬ FormationClosure.process.step x e y :=
  fun step => Nat.lt_irrefl _ (Nat.lt_of_le_of_lt (step_covered step).2 short)

theorem sensing_shape {s t : NativePacketProcess.State} {command : NativePacketProcess.Command}
    {o : Observation} (actual : execute s command = .complete t o)
    (notProbe : command ≠ .probe) :
    t.held = (enact s).held ∧ t.enacted = (enact s).enacted ∧ t.arrived = s.arrived ∧
      t.source = s.source := by
  unfold execute at actual
  generalize interface : support s = result at actual
  cases result with
  | capacity => cases actual
  | insufficient => cases actual
  | sustained ready =>
    obtain ⟨_, rfl⟩ := (support_sustained_iff s ready).mp interface
    cases command with
    | a => cases actual; exact ⟨rfl, rfl, rfl, rfl⟩
    | reset => cases actual; exact ⟨rfl, rfl, rfl, rfl⟩
    | read => cases actual; exact ⟨rfl, rfl, rfl, rfl⟩
    | probe => exact absurd rfl notProbe

theorem draw_conserves (f sp b i : Nat) (covered : b ≤ f) :
    (f - b) + (sp + b) + i = f + sp + i := by
  rw [← Nat.add_assoc (f - b) sp b, Nat.add_right_comm (f - b) sp b,
    sub_add_cancel_constructive f b covered]

theorem probe_conserves (f sp b i g : Nat) (first : b ≤ f) (second : b ≤ f - b + g) :
    ((f - b + g) - b) + (sp + b + b) + i = f + sp + (i + g) := by
  rw [Nat.add_assoc sp b b, Nat.add_comm b b, ← Nat.add_assoc sp b b,
    Nat.add_comm (sp + b) b, ← Nat.add_assoc ((f - b + g) - b) b (sp + b),
    sub_add_cancel_constructive (f - b + g) b second,
    Nat.add_right_comm (f - b) g (sp + b), draw_conserves f sp b g first,
    Nat.add_assoc (f + sp) g i, Nat.add_comm g i]

theorem step_conserves {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) :
    y.native.held + y.native.enacted + x.native.arrived =
      x.native.held + x.native.enacted + y.native.arrived := by
  have ready := step_covered step
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨o, actual⟩, _, _⟩ := step
      cases command with
      | probe =>
        obtain ⟨probeReady, equal, _⟩ := (probe_complete_iff _ _ o).mp actual
        rw [equal]
        exact probe_conserves _ _ _ _ _ ready.2 probeReady.2.2.2
      | a =>
        obtain ⟨held, enacted, arrived, _⟩ := sensing_shape actual (fun h => by cases h)
        rw [held, enacted, arrived]
        exact draw_conserves _ _ _ _ ready.2
      | reset =>
        obtain ⟨held, enacted, arrived, _⟩ := sensing_shape actual (fun h => by cases h)
        rw [held, enacted, arrived]
        exact draw_conserves _ _ _ _ ready.2
      | read =>
        obtain ⟨held, enacted, arrived, _⟩ := sensing_shape actual (fun h => by cases h)
        rw [held, enacted, arrived]
        exact draw_conserves _ _ _ _ ready.2
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
      exact draw_conserves _ _ _ _ ready.2
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
    exact draw_conserves _ _ _ _ ready.2

theorem cancel_right (a b c : Nat) (h : a + c = b + c) : a = b := by
  rw [Nat.add_comm a c, Nat.add_comm b c] at h
  exact cancel_left c h

/-- Held amount plus cumulative draw is conserved up to arrival. -/
theorem held_amount_conserved {x y : Port} {events : List FormationClosure.Event}
    (trace : Trace FormationClosure.process x events y) :
    y.native.held + y.native.enacted + x.native.arrived =
      x.native.held + x.native.enacted + y.native.arrived := by
  induction trace with
  | nil => rfl
  | @cons s m t e rest step _ ih =>
    have first := step_conserves step
    apply cancel_right _ _ m.native.arrived
    calc t.native.held + t.native.enacted + s.native.arrived + m.native.arrived
        = (t.native.held + t.native.enacted + m.native.arrived) + s.native.arrived := by
          rw [Nat.add_right_comm]
      _ = (m.native.held + m.native.enacted + t.native.arrived) + s.native.arrived := by rw [ih]
      _ = (m.native.held + m.native.enacted + s.native.arrived) + t.native.arrived := by
          rw [Nat.add_right_comm]
      _ = (s.native.held + s.native.enacted + m.native.arrived) + t.native.arrived := by rw [first]
      _ = s.native.held + s.native.enacted + t.native.arrived + m.native.arrived := by
          rw [Nat.add_right_comm]

/-- A history without arrival started holding its draws and what remains. -/
theorem held_covers_draws_before_arrival {x y : Port} {events : List FormationClosure.Event}
    (trace : Trace FormationClosure.process x events y)
    (noArrival : y.native.arrived = x.native.arrived) :
    x.native.held = y.native.held + totalOperations events * draw x.native := by
  have conserved := held_amount_conserved trace
  rw [noArrival] at conserved
  have balance := cancel_right _ _ _ conserved
  rw [(closure_trace_draw trace).1, ← Nat.add_assoc, Nat.add_right_comm] at balance
  exact (cancel_right _ _ _ balance).symm

def conversions : List FormationClosure.Event → Nat
  | [] => 0
  | .inl (.inl .probe) :: rest => conversions rest + 1
  | .inl (.inl .a) :: rest => conversions rest
  | .inl (.inl .reset) :: rest => conversions rest
  | .inl (.inl .read) :: rest => conversions rest
  | .inl (.inr _) :: rest => conversions rest
  | .inr _ :: rest => conversions rest

theorem step_source {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) :
    y.native.source + 10 * conversions [e] = x.native.source := by
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨o, actual⟩, _, _⟩ := step
      cases command with
      | probe =>
        obtain ⟨probeReady, equal, _⟩ := (probe_complete_iff _ _ o).mp actual
        rw [equal]
        exact sub_add_cancel_constructive x.native.source 10 probeReady.2.1
      | a =>
        obtain ⟨_, _, _, source⟩ := sensing_shape actual (fun h => by cases h)
        rw [source]
        rfl
      | reset =>
        obtain ⟨_, _, _, source⟩ := sensing_shape actual (fun h => by cases h)
        rw [source]
        rfl
      | read =>
        obtain ⟨_, _, _, source⟩ := sensing_shape actual (fun h => by cases h)
        rw [source]
        rfl
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
      rfl
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
    rfl

theorem conversions_cons (e : FormationClosure.Event) (rest : List FormationClosure.Event) :
    conversions (e :: rest) = conversions [e] + conversions rest := by
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      cases command with
      | probe =>
        show conversions rest + 1 = (0 + 1) + conversions rest
        rw [Nat.zero_add, Nat.add_comm]
      | a => exact (Nat.zero_add _).symm
      | reset => exact (Nat.zero_add _).symm
      | read => exact (Nat.zero_add _).symm
    | inr _ => exact (Nat.zero_add _).symm
  | inr _ => exact (Nat.zero_add _).symm

/-- Every completed history converts ten source units per probe. -/
theorem source_accounting {x y : Port} {events : List FormationClosure.Event}
    (trace : Trace FormationClosure.process x events y) :
    y.native.source + 10 * conversions events = x.native.source := by
  induction trace with
  | nil => rfl
  | @cons s m t e rest step _ ih =>
    rw [conversions_cons, Nat.mul_add, Nat.add_comm (10 * conversions [e]),
      ← Nat.add_assoc, ih, step_source step]

/-! ## 3. The least start of the closure history -/

/-- The closure start with held amount `held` and source `source`. -/
def startWith (held source : Nat) : Port :=
  ⟨{ phase := .p0, tau := false, sigma := false, broken := false, blocked := true,
     receiptFlip := false, source := source, held := held, live := 0, workspace := 0,
     capacity := 10, enacted := 0, arrived := 0, transferred := 0, dissipated := 0 }, 0, 0⟩

theorem start_is_startWith : start = startWith 200000 20 := rfl

theorem blocked_step_no_arrival {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) (blocked : x.native.blocked = true) :
    y.native.arrived = x.native.arrived := by
  have closed := arrival_false_of_blocked x.native blocked
  cases e with
  | inl e =>
    cases e with
    | inl command =>
      obtain ⟨⟨o, actual⟩, _, _⟩ := step
      cases command with
      | probe =>
        obtain ⟨_, equal, _⟩ := (probe_complete_iff _ _ o).mp actual
        rw [equal, (probe_final_effects _).2.2.2.2.1]
        unfold arrivalAmount
        rw [closed]
        rfl
      | a =>
        obtain ⟨_, _, arrived, _⟩ := sensing_shape actual (fun h => by cases h)
        rw [arrived]
      | reset =>
        obtain ⟨_, _, arrived, _⟩ := sensing_shape actual (fun h => by cases h)
        rw [arrived]
      | read =>
        obtain ⟨_, _, arrived, _⟩ := sensing_shape actual (fun h => by cases h)
        rw [arrived]
    | inr _ =>
      obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
      rfl
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
    rfl

/-- Before any formation, a blocked start receives no arrival. -/
theorem blocked_history_no_arrival {x y : Port} {events : List FormationClosure.Event}
    (trace : Trace FormationClosure.process x events y) (none : formations events = 0)
    (blocked : x.native.blocked = true) :
    y.native.arrived = x.native.arrived ∧ y.native.blocked = true := by
  induction trace with
  | nil => exact ⟨rfl, blocked⟩
  | @cons s m t e rest step _ ih =>
    cases e with
    | inr _ => exact Nat.noConfusion none
    | inl a =>
      have kept := activity_retains_contact s a m step
      have mBlocked : m.native.blocked = true := by
        have := congrArg Prod.snd kept
        exact this.trans blocked
      obtain ⟨arrivedSame, final⟩ := ih none mBlocked
      exact ⟨arrivedSame.trans (blocked_step_no_arrival step blocked), final⟩

theorem history_split :
    history = ([nativeE .a, nativeE .a, nativeE .probe, recoverE] ++ [formE]) ++
      [nativeE .probe] := rfl

/-- The held amount and source the closure history needs, both attained. -/
theorem history_needs {held source : Nat} {y : Port}
    (trace : Trace FormationClosure.process (startWith held source) history y) :
    114702 ≤ held ∧ 20 ≤ source := by
  constructor
  · rw [history_split] at trace
    obtain ⟨m, before, last⟩ := trace_append_iff.mp trace
    obtain ⟨k, early, formed⟩ := trace_append_iff.mp before
    obtain ⟨noArrival, kBlocked⟩ := blocked_history_no_arrival early rfl rfl
    have formStep := trace_singleton_iff.mp formed
    have formArrived := blocked_step_no_arrival formStep kBlocked
    have held' := held_covers_draws_before_arrival before (formArrived.trans noArrival)
    have amount := (closure_trace_draw before).2
    have lastReady := step_covered (trace_singleton_iff.mp last)
    have covered : draw (startWith held source).native + 6 * draw (startWith held source).native
        ≤ (startWith held source).native.held := by
      rw [held']
      exact Nat.add_le_add_right (amount ▸ lastReady.2) _
    have amountIs : draw (startWith held source).native = 16386 := rfl
    rw [amountIs] at covered
    exact covered
  · have converted := source_accounting trace
    have : y.native.source + 20 = source := converted
    rw [← this]
    exact Nat.le_add_left 20 _

/-- The least start: needed by every completed run, attained, and one unit less
of either amount stops the history. -/
theorem least_starting_stock :
    (∀ held source y, run (startWith held source) history = some y →
      114702 ≤ held ∧ 20 ≤ source) ∧
      (∃ y, run (startWith 114702 20) history = some y ∧
        y.native.transferred = 10 ∧ y.native.held = 638974) ∧
      run (startWith 114701 20) history = none ∧
      run (startWith 114702 19) history = none :=
  ⟨fun _ _ _ ran => history_needs (run_sound ran), ⟨_, rfl, rfl, rfl⟩, rfl, rfl⟩

end Generative.InquirySufficiency.StartingStock

#print axioms Generative.InquirySufficiency.StartingStock.nothing_dissipated_nothing_recovered
#print axioms Generative.InquirySufficiency.StartingStock.inherited_pair_forms_unbacked
#print axioms Generative.InquirySufficiency.StartingStock.FormationsBackedFrom
#print axioms Generative.InquirySufficiency.StartingStock.backing_iff_empty_stock
#print axioms Generative.InquirySufficiency.StartingStock.execute_complete_covered
#print axioms Generative.InquirySufficiency.StartingStock.step_covered
#print axioms Generative.InquirySufficiency.StartingStock.nothing_held_nothing_proceeds
#print axioms Generative.InquirySufficiency.StartingStock.sensing_shape
#print axioms Generative.InquirySufficiency.StartingStock.draw_conserves
#print axioms Generative.InquirySufficiency.StartingStock.probe_conserves
#print axioms Generative.InquirySufficiency.StartingStock.step_conserves
#print axioms Generative.InquirySufficiency.StartingStock.cancel_right
#print axioms Generative.InquirySufficiency.StartingStock.held_amount_conserved
#print axioms Generative.InquirySufficiency.StartingStock.held_covers_draws_before_arrival
#print axioms Generative.InquirySufficiency.StartingStock.conversions
#print axioms Generative.InquirySufficiency.StartingStock.step_source
#print axioms Generative.InquirySufficiency.StartingStock.conversions_cons
#print axioms Generative.InquirySufficiency.StartingStock.source_accounting
#print axioms Generative.InquirySufficiency.StartingStock.startWith
#print axioms Generative.InquirySufficiency.StartingStock.start_is_startWith
#print axioms Generative.InquirySufficiency.StartingStock.blocked_step_no_arrival
#print axioms Generative.InquirySufficiency.StartingStock.blocked_history_no_arrival
#print axioms Generative.InquirySufficiency.StartingStock.history_split
#print axioms Generative.InquirySufficiency.StartingStock.history_needs
#print axioms Generative.InquirySufficiency.StartingStock.least_starting_stock
