import NativePortContinuation
import RevisingPort

/-!
# Support and finite continuation of the whole revising port

The native accounting coordinates remain coordinates of one process through
recovery, formation and encounters. Their exact conservation gives U1 and U2.
The native finite-source potential decreases at every completed extended event
and every encounter, without an intact-reset premise.

The native interface draw on formation is sufficient but not necessary for
conservation or finite continuation. An explicit rival omits that draw while
still consuming a spare pair. Its combined potential counts both remaining
native support and pairs. It still terminates; the native potential alone no
longer decreases on formation. This does not establish a physical zero-cost
formation law, or erase the original process's results.

These are implementation requirements relevant to learning and self-revision.
They do not identify persistence, contact opening or revision with ethical good.
-/

namespace Generative.InquirySufficiency.WholePortContinuation

open Generative NativePacketProcess NativePortContinuation
open FormationClosure AcquiredContact RevisingPort

theorem open_continues (s : State) : Continues s (ContactFormation.openContact s) :=
  ⟨rfl, Nat.le_refl _, Nat.le_refl _⟩

theorem recovery_continues {x y : Port} (step : recover x = .complete y) :
    Continues x.native y.native := by
  obtain ⟨ready, _, rfl⟩ := (recover_complete_iff x y).mp step
  exact enact_continues x.native ready.2

theorem formation_continues {x y : Port} (step : formPort x = .complete y) :
    Continues x.native y.native := by
  obtain ⟨ready, _, rfl⟩ := (formPort_complete_iff x y).mp step
  exact continues_trans (enact_continues x.native ready.2) (open_continues _)

theorem activity_continues {x y : Port} {e : Sum Command Unit}
    (step : activity.step x e y) : Continues x.native y.native := by
  cases e with
  | inl command => exact NativePortContinuation.step_continues step.1
  | inr _ => exact recovery_continues step

theorem extended_continues {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) : Continues x.native y.native := by
  cases e with
  | inl event => exact activity_continues step
  | inr _ => exact formation_continues step

theorem extended_trace_continues {x y : Port} {es : List FormationClosure.Event}
    (trace : Trace FormationClosure.process x es y) : Continues x.native y.native := by
  induction trace with
  | nil => exact continues_refl _
  | cons step _ ih => exact continues_trans (extended_continues step) ih

theorem acted_continues {b : Bool} {x z : Port} (act : acted b x z) :
    Continues x.native z.native := by
  cases b with
  | false => rw [act]; exact continues_refl _
  | true => exact formation_continues act

theorem inquiry_continues {s : State} (q : Inquiry s) : Continues s q.s5 :=
  NativePortContinuation.trace_continues q.trace

theorem revising_continues {a b : Revising} {e : RevisingEvent}
    (step : revising.step a e b) : Continues a.1.native b.1.native := by
  cases e with
  | inl event => exact activity_continues step.1
  | inr found =>
    obtain ⟨_, z, act, q, reached, _⟩ := step
    rw [reached]
    exact continues_trans (acted_continues act) (inquiry_continues q)

theorem revising_trace_continues {a b : Revising} {es : List RevisingEvent}
    (trace : Trace revising a es b) : Continues a.1.native b.1.native := by
  induction trace with
  | nil => exact continues_refl _
  | cons step _ ih => exact continues_trans (revising_continues step) ih

/-- Exact conservation expressed with the actual counter increments. -/
theorem continues_exact {s t : State} (continued : Continues s t) :
    t.held + (t.enacted - s.enacted) = s.held + (t.arrived - s.arrived) := by
  obtain ⟨balance, enactedGrew, arrivedGrew⟩ := continued
  apply cancel_right (c := s.enacted + s.arrived)
  calc t.held + (t.enacted - s.enacted) + (s.enacted + s.arrived)
      = t.held + ((t.enacted - s.enacted) + s.enacted) + s.arrived := by
        rw [Nat.add_assoc, Nat.add_assoc, Nat.add_assoc]
    _ = t.held + t.enacted + s.arrived := by rw [sub_add_restore _ _ enactedGrew]
    _ = s.held + s.enacted + t.arrived := balance
    _ = s.held + s.enacted + ((t.arrived - s.arrived) + s.arrived) := by
        rw [sub_add_restore _ _ arrivedGrew]
    _ = s.held + (t.arrived - s.arrived) + (s.enacted + s.arrived) := by
        rw [Nat.add_assoc, Nat.add_assoc, Nat.add_left_comm s.enacted]

def extendedEnacted (x : Port) (_ : FormationClosure.Event) (y : Port) : Nat :=
  y.native.enacted - x.native.enacted

def extendedArrived (x : Port) (_ : FormationClosure.Event) (y : Port) : Nat :=
  y.native.arrived - x.native.arrived

def revisingEnacted (a : Revising) (_ : RevisingEvent) (b : Revising) : Nat :=
  b.1.native.enacted - a.1.native.enacted

def revisingArrived (a : Revising) (_ : RevisingEvent) (b : Revising) : Nat :=
  b.1.native.arrived - a.1.native.arrived

theorem extended_sustain_law : Conditional.SustainLaw FormationClosure.process
    (fun x => x.native.held) extendedEnacted extendedArrived :=
  fun _ _ _ step => Nat.le_of_eq (continues_exact (extended_continues step))

theorem revising_sustain_law : Conditional.SustainLaw revising
    (fun a => a.1.native.held) revisingEnacted revisingArrived :=
  fun _ _ _ step => Nat.le_of_eq (continues_exact (revising_continues step))

theorem extended_history_bound {x y : Port} {es : List FormationClosure.Event}
    {made gained count : Nat}
    (history : Conditional.SupportTrace FormationClosure.process extendedEnacted extendedArrived
      x es y made gained count) : made + y.native.held ≤ x.native.held + gained :=
  Conditional.support_trace_bound (fun x => x.native.held) extended_sustain_law history

theorem revising_history_bound {a b : Revising} {es : List RevisingEvent}
    {made gained count : Nat}
    (history : Conditional.SupportTrace revising revisingEnacted revisingArrived
      a es b made gained count) : made + b.1.native.held ≤ a.1.native.held + gained :=
  Conditional.support_trace_bound (fun a => a.1.native.held) revising_sustain_law history

theorem recovery_lowers_potential {x y : Port} (step : recover x = .complete y) :
    potential y.native < potential x.native := by
  obtain ⟨ready, _, rfl⟩ := (recover_complete_iff x y).mp step
  exact enact_lowers_potential _ ready.2

theorem formation_lowers_potential {x y : Port} (step : formPort x = .complete y) :
    potential y.native < potential x.native := by
  obtain ⟨ready, _, rfl⟩ := (formPort_complete_iff x y).mp step
  exact enact_lowers_potential _ ready.2

theorem activity_lowers_potential {x y : Port} {e : Sum Command Unit}
    (step : activity.step x e y) : potential y.native < potential x.native := by
  cases e with
  | inl command => exact NativePortContinuation.step_lowers_potential step.1
  | inr _ => exact recovery_lowers_potential step

theorem extended_lowers_potential {x y : Port} {e : FormationClosure.Event}
    (step : FormationClosure.process.step x e y) : potential y.native < potential x.native := by
  cases e with
  | inl event => exact activity_lowers_potential step
  | inr _ => exact formation_lowers_potential step

theorem acted_bounds_potential {b : Bool} {x z : Port} (act : acted b x z) :
    potential z.native ≤ potential x.native := by
  cases b with
  | false => rw [act]; exact Nat.le_refl _
  | true => exact Nat.le_of_lt (formation_lowers_potential act)

theorem inquiry_lowers_potential {s : State} (q : Inquiry s) :
    potential q.s5 < potential s :=
  Nat.lt_trans (NativePortContinuation.step_lowers_potential ⟨_, q.step5⟩)
    (Nat.lt_trans (NativePortContinuation.step_lowers_potential ⟨_, q.step4⟩)
      (Nat.lt_trans (NativePortContinuation.step_lowers_potential ⟨_, q.step3⟩)
        (Nat.lt_trans (NativePortContinuation.step_lowers_potential ⟨_, q.step2⟩)
          (NativePortContinuation.step_lowers_potential ⟨_, q.step1⟩))))

theorem revising_lowers_potential {a b : Revising} {e : RevisingEvent}
    (step : revising.step a e b) : potential b.1.native < potential a.1.native := by
  cases e with
  | inl event => exact activity_lowers_potential step.1
  | inr found =>
    obtain ⟨_, z, act, q, reached, _⟩ := step
    rw [reached]
    exact Nat.lt_of_lt_of_le (inquiry_lowers_potential q) (acted_bounds_potential act)

theorem extended_history_length {x y : Port} {es : List FormationClosure.Event}
    (history : Trace FormationClosure.process x es y) :
    es.length + potential y.native ≤ potential x.native :=
  trace_reserve_bound (fun x => potential x.native)
    (fun _ _ _ step => extended_lowers_potential step) history

theorem revising_history_length {a b : Revising} {es : List RevisingEvent}
    (history : Trace revising a es b) : es.length + potential b.1.native ≤ potential a.1.native :=
  trace_reserve_bound (fun a => potential a.1.native)
    (fun _ _ _ step => revising_lowers_potential step) history

theorem extended_cannot_continue_indefinitely :
    ¬ ∃ states : Nat → Port, ∃ events : Nat → FormationClosure.Event,
      ∀ n, FormationClosure.process.step (states n) (events n) (states (n + 1)) :=
  no_infinite_execution_under_depletion (fun x => potential x.native)
    (fun _ _ _ step => extended_lowers_potential step)

theorem revising_cannot_continue_indefinitely :
    ¬ ∃ states : Nat → Revising, ∃ events : Nat → RevisingEvent,
      ∀ n, revising.step (states n) (events n) (states (n + 1)) :=
  no_infinite_execution_under_depletion (fun a => potential a.1.native)
    (fun _ _ _ step => revising_lowers_potential step)

/-! ## The formation draw is not necessary for these conclusions -/

/-- A rival retaining material consumption and contact opening, omitting only
the formation interface draw. Its capacity guard remains. -/
def undrawnFormation : Process Port Unit where
  step x _ y := peak x.native ≤ x.native.capacity ∧ 1 ≤ x.spare ∧
    y = ⟨ContactFormation.openContact x.native, x.spare - 1, x.recovered⟩

def undrawnProcess : Process Port FormationClosure.Event :=
  FormationLaw.extend activity undrawnFormation

theorem undrawn_continues {x y : Port} {e : FormationClosure.Event}
    (step : undrawnProcess.step x e y) : Continues x.native y.native := by
  cases e with
  | inl event => exact activity_continues step
  | inr _ =>
    obtain ⟨_, _, rfl⟩ := step
    exact open_continues _

theorem undrawn_sustain_law : Conditional.SustainLaw undrawnProcess
    (fun x => x.native.held) extendedEnacted extendedArrived :=
  fun _ _ _ step => Nat.le_of_eq (continues_exact (undrawn_continues step))

/-- Pair count is a termination coordinate, not a common value measure. Scaling
native potential by two absorbs the one pair that recovery can add. -/
def materialPotential (x : Port) : Nat := 2 * potential x.native + x.spare

theorem double_gap {m n : Nat} (lower : m < n) : 2 * m + 2 ≤ 2 * n := by
  have scaled := Nat.mul_le_mul_left 2 lower
  rw [Nat.mul_succ] at scaled
  exact scaled

theorem activity_lowers_material {x y : Port} {e : Sum Command Unit}
    (step : activity.step x e y) : materialPotential y < materialPotential x := by
  cases e with
  | inl command =>
    have gap := double_gap (NativePortContinuation.step_lowers_potential step.1)
    have strict : 2 * potential y.native < 2 * potential x.native :=
      Nat.le_trans (Nat.le_succ _) gap
    show 2 * potential y.native + y.spare < 2 * potential x.native + x.spare
    rw [step.2.1]
    exact Nat.add_lt_add_right strict _
  | inr _ =>
    have gap := double_gap (recovery_lowers_potential step)
    obtain ⟨_, _, rfl⟩ := (recover_complete_iff x y).mp step
    show 2 * potential (enact x.native) + (x.spare + 1) + 1 ≤
      2 * potential x.native + x.spare
    rw [← Nat.add_assoc, Nat.add_right_comm (2 * potential (enact x.native)) x.spare 1,
      Nat.add_right_comm (2 * potential (enact x.native) + 1) x.spare 1]
    exact Nat.add_le_add_right gap _

theorem undrawn_lowers_material {x y : Port} {e : FormationClosure.Event}
    (step : undrawnProcess.step x e y) : materialPotential y < materialPotential x := by
  cases e with
  | inl event => exact activity_lowers_material step
  | inr _ =>
    obtain ⟨_, pair, rfl⟩ := step
    show 2 * potential x.native + (x.spare - 1) < 2 * potential x.native + x.spare
    exact Nat.add_lt_add_left (Nat.sub_lt pair (Nat.zero_lt_succ 0)) _

theorem undrawn_history_length {x y : Port} {es : List FormationClosure.Event}
    (history : Trace undrawnProcess x es y) :
    es.length + materialPotential y ≤ materialPotential x :=
  trace_reserve_bound materialPotential (fun _ _ _ step => undrawn_lowers_material step) history

theorem undrawn_cannot_continue_indefinitely :
    ¬ ∃ states : Nat → Port, ∃ events : Nat → FormationClosure.Event,
      ∀ n, undrawnProcess.step (states n) (events n) (states (n + 1)) :=
  no_infinite_execution_under_depletion materialPotential
    (fun _ _ _ step => undrawn_lowers_material step)

/-- Removing the draw does not make material consumption disappear. It does
remove positive enactment and strict native-potential decrease on that event. -/
theorem undrawn_formation_preserves_native_potential (x : Port)
    (capacity : peak x.native ≤ x.native.capacity) (pair : 1 ≤ x.spare) :
    ∃ y, undrawnProcess.step x (.inr ()) y ∧
      potential y.native = potential x.native ∧ extendedEnacted x (.inr ()) y = 0 ∧
      y.spare + 1 = x.spare := by
  refine ⟨⟨ContactFormation.openContact x.native, x.spare - 1, x.recovered⟩,
    ⟨capacity, pair, rfl⟩, rfl, ?_, sub_add_restore _ _ pair⟩
  exact Nat.sub_self _

def undrawnActed : Bool → Port → Port → Prop
  | true, x, z => undrawnFormation.step x () z
  | false, x, z => z = x

/-- The same encounter order, decision rule and inquiry, with only the
formation's interface draw removed. -/
def undrawnRevising : Process Revising RevisingEvent where
  step a e b := match e with
    | .inl event => activity.step a.1 event b.1 ∧ b.2 = a.2
    | .inr found => contact a.1 = found ∧
        ∃ z, undrawnActed (PortValuation.portOrg.select a.2 found) a.1 z ∧
          ∃ q : Inquiry z.native, b.1 = ⟨q.s5, z.spare, z.recovered⟩ ∧
            b.2 = some (q.reading.arrived0, q.reading.arrived1)

theorem undrawn_acted_continues {b : Bool} {x z : Port} (act : undrawnActed b x z) :
    Continues x.native z.native := by
  cases b with
  | false => rw [act]; exact continues_refl _
  | true => exact undrawn_continues (e := .inr ()) act

theorem undrawn_revising_continues {a b : Revising} {e : RevisingEvent}
    (step : undrawnRevising.step a e b) : Continues a.1.native b.1.native := by
  cases e with
  | inl event => exact activity_continues step.1
  | inr found =>
    obtain ⟨_, z, act, q, reached, _⟩ := step
    rw [reached]
    exact continues_trans (undrawn_acted_continues act) (inquiry_continues q)

theorem undrawn_revising_sustain_law : Conditional.SustainLaw undrawnRevising
    (fun a => a.1.native.held) revisingEnacted revisingArrived :=
  fun _ _ _ step => Nat.le_of_eq (continues_exact (undrawn_revising_continues step))

theorem undrawn_acted_bounds_material {b : Bool} {x z : Port} (act : undrawnActed b x z) :
    materialPotential z ≤ materialPotential x := by
  cases b with
  | false => rw [act]; exact Nat.le_refl _
  | true => exact Nat.le_of_lt (undrawn_lowers_material (e := .inr ()) act)

theorem inquiry_lowers_material (x : Port) (q : Inquiry x.native) :
    materialPotential ⟨q.s5, x.spare, x.recovered⟩ < materialPotential x := by
  have gap := double_gap (inquiry_lowers_potential q)
  have strict : 2 * potential q.s5 < 2 * potential x.native :=
    Nat.le_trans (Nat.le_succ _) gap
  exact Nat.add_lt_add_right strict _

theorem undrawn_revising_lowers_material {a b : Revising} {e : RevisingEvent}
    (step : undrawnRevising.step a e b) : materialPotential b.1 < materialPotential a.1 := by
  cases e with
  | inl event => exact activity_lowers_material step.1
  | inr found =>
    obtain ⟨_, z, act, q, reached, _⟩ := step
    rw [reached]
    exact Nat.lt_of_lt_of_le (inquiry_lowers_material z q) (undrawn_acted_bounds_material act)

theorem undrawn_revising_history_length {a b : Revising} {es : List RevisingEvent}
    (history : Trace undrawnRevising a es b) :
    es.length + materialPotential b.1 ≤ materialPotential a.1 :=
  trace_reserve_bound (fun a => materialPotential a.1)
    (fun _ _ _ step => undrawn_revising_lowers_material step) history

theorem undrawn_revising_cannot_continue_indefinitely :
    ¬ ∃ states : Nat → Revising, ∃ events : Nat → RevisingEvent,
      ∀ n, undrawnRevising.step (states n) (events n) (states (n + 1)) :=
  no_infinite_execution_under_depletion (fun a => materialPotential a.1)
    (fun _ _ _ step => undrawn_revising_lowers_material step)

end Generative.InquirySufficiency.WholePortContinuation


#print axioms Generative.InquirySufficiency.WholePortContinuation.open_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.recovery_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.formation_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.activity_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_trace_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.acted_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.inquiry_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_trace_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.continues_exact
#print axioms Generative.InquirySufficiency.WholePortContinuation.extendedEnacted
#print axioms Generative.InquirySufficiency.WholePortContinuation.extendedArrived
#print axioms Generative.InquirySufficiency.WholePortContinuation.revisingEnacted
#print axioms Generative.InquirySufficiency.WholePortContinuation.revisingArrived
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_sustain_law
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_sustain_law
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_history_bound
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_history_bound
#print axioms Generative.InquirySufficiency.WholePortContinuation.recovery_lowers_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.formation_lowers_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.activity_lowers_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_lowers_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.acted_bounds_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.inquiry_lowers_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_lowers_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_history_length
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_history_length
#print axioms Generative.InquirySufficiency.WholePortContinuation.extended_cannot_continue_indefinitely
#print axioms Generative.InquirySufficiency.WholePortContinuation.revising_cannot_continue_indefinitely
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawnFormation
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawnProcess
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_sustain_law
#print axioms Generative.InquirySufficiency.WholePortContinuation.materialPotential
#print axioms Generative.InquirySufficiency.WholePortContinuation.double_gap
#print axioms Generative.InquirySufficiency.WholePortContinuation.activity_lowers_material
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_lowers_material
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_history_length
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_cannot_continue_indefinitely
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_formation_preserves_native_potential
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawnActed
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawnRevising
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_acted_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_revising_continues
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_revising_sustain_law
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_acted_bounds_material
#print axioms Generative.InquirySufficiency.WholePortContinuation.inquiry_lowers_material
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_revising_lowers_material
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_revising_history_length
#print axioms Generative.InquirySufficiency.WholePortContinuation.undrawn_revising_cannot_continue_indefinitely
