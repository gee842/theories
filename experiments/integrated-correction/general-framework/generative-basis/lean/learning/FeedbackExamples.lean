import ControllerRevision

/-!
A finite witness jointly instantiates actual consequence feedback and a resource
law. Its probe and update architecture are supplied. Every event spends one unit,
including the probe. No reward or success label enters the update. Both response
choices execute: the mismatched choice reaches a dead state. Three units fund
probe, matching response and use; a prepared flag without fuel is not capability.
-/

namespace Generative.Learning.Examples

inductive Action where
  | probe | left | right | use
  deriving DecidableEq

inductive Phase where
  | start | select | ready | dead | done
  deriving DecidableEq

structure World where
  mode : Bool
  phase : Phase
  fuel : Nat
  deriving DecidableEq

def response (b : Bool) : Action := if b then .right else .left

def world : Process World Action where
  step s a t := t.mode = s.mode ∧ s.fuel = t.fuel + 1 ∧
    match a with
    | .probe => s.phase = .start ∧ t.phase = .select
    | .left => s.phase = .select ∧ t.phase = if s.mode then .dead else .ready
    | .right => s.phase = .select ∧ t.phase = if s.mode then .ready else .dead
    | .use => s.phase = .ready ∧ t.phase = .done

inductive Memory where
  | unknown | learned (b : Bool) | prepared (b : Bool) | finished (b : Bool)
  deriving DecidableEq

def learner : Controller Memory Action (Option Bool) where
  choose m := match m with
    | .unknown => .probe
    | .learned b => response b
    | .prepared _ => .use
    | .finished _ => .use
  revise m o := match m, o with
    | .unknown, some b => .learned b
    | .learned b, _ => .prepared b
    | .prepared b, _ => .finished b
    | _, _ => m

/-- The supplied probe returns an actual property of its successor, not an
externally computed fitness or a successful-response label. -/
def feedback (_ : World) (a : Action) (t : World) : Option Bool :=
  if a = .probe then some t.mode else none

def misleading (_ : World) (a : Action) (t : World) : Option Bool :=
  if a = .probe then some (!t.mode) else none

theorem world_account : Conditional.AccountLaw world World.fuel
    (fun _ _ _ => 1) (fun _ _ _ => 0) := by
  intro s a t h
  have hc := h.2.1
  change t.fuel + 1 ≤ s.fuel + 0
  omega

theorem feedback_account : Conditional.AccountLaw (closedLoop learner world feedback)
    (fun p => p.1.fuel) (fun _ _ _ => 1) (fun _ _ _ => 0) :=
  closed_loop_account_law learner world feedback World.fuel
    (fun _ _ _ => 1) (fun _ _ _ => 0) world_account

theorem world_trace_exact_cost {s t : World} {word : List Action}
    (h : Trace world s word t) : word.length + t.fuel = s.fuel := by
  induction h with
  | nil s => simp
  | cons hs _ ih =>
    have hcost := hs.2.1
    simp only [List.length_cons]
    omega

theorem three_event_trace_needs_three {s t : World} {a b c : Action}
    (h : Trace world s [a, b, c] t) : 3 ≤ s.fuel := by
  have hc := world_trace_exact_cost h
  simp only [List.length_cons, List.length_nil] at hc
  omega

theorem accurate_feedback_completes (b : Bool) :
    Trace (closedLoop learner world feedback)
      (⟨b, .start, 3⟩, .unknown)
      [(.probe, some b), (response b, none), (.use, none)]
      (⟨b, .done, 0⟩, .finished b) := by
  refine .cons (m := (⟨b, .select, 2⟩, .learned b)) ?_
    (.cons (m := (⟨b, .ready, 1⟩, .prepared b)) ?_ (.cons ?_ (.nil _)))
  all_goals cases b <;> simp [closedLoop, world, learner, feedback, response]

theorem wrong_response_executes (b : Bool) :
    world.step ⟨b, .select, 2⟩ (response (!b)) ⟨b, .dead, 1⟩ := by
  cases b <;> simp [world, response]

theorem dead_no_event (b : Bool) (fuel : Nat) (a : Action) :
    ¬ Enabled world ⟨b, .dead, fuel⟩ a := by
  rintro ⟨t, ht⟩
  cases a <;> simp [world] at ht

theorem prepared_without_fuel_cannot_use (b : Bool) :
    ¬ Enabled world ⟨b, .ready, 0⟩ .use := by
  rintro ⟨t, ht⟩
  have hc := ht.2.1
  change 0 = t.fuel + 1 at hc
  omega

theorem misleading_feedback_reaches_dead (b : Bool) :
    Trace (closedLoop learner world misleading)
      (⟨b, .start, 3⟩, .unknown)
      [(.probe, some (!b)), (response (!b), none)]
      (⟨b, .dead, 1⟩, .prepared (!b)) := by
  refine .cons (m := (⟨b, .select, 2⟩, .learned (!b))) ?_
    (.cons ?_ (.nil _))
  all_goals cases b <;> simp [closedLoop, world, learner, misleading, response]

theorem misleading_feedback_cannot_use (b : Bool) :
    ¬ Enabled (closedLoop learner world misleading)
      (⟨b, .dead, 1⟩, .prepared (!b)) (.use, none) := by
  rintro ⟨t, ht⟩
  exact dead_no_event b 1 .use ⟨t.1, ht.1⟩

/-- From the response point, the command must match the mode if a subsequent
use is feasible. Both mismatching commands remain physically executable. -/
theorem response_then_use_requires_match {b : Bool} {fuel : Nat} {a : Action}
    (h : Feasible world ⟨b, .select, fuel⟩ [a, .use]) : a = response b := by
  obtain ⟨t, ht⟩ := h
  obtain ⟨mid, hfirst, hrest⟩ := trace_cons_iff.mp ht
  have huse := trace_singleton_iff.mp hrest
  have hready := huse.2.2.1
  cases b <;> cases a <;> simp_all [world, response]

theorem opposite_modes_incompatible (a : Action) :
    ¬ (Feasible world ⟨false, .select, 2⟩ [a, .use] ∧
       Feasible world ⟨true, .select, 2⟩ [a, .use]) := by
  intro h
  have hl := response_then_use_requires_match h.1
  have hr := response_then_use_requires_match h.2
  simp only [response, Bool.false_eq_true, ↓reduceIte] at hl
  simp only [response, ↓reduceIte] at hr
  rw [hl] at hr
  cases hr

/-- Arbitrary fixed deterministic controllers with a blind probe cannot choose
a response supporting later use in both modes, regardless of memory size. -/
theorem blind_probe_cannot_solve_both {M : Type}
    (C : Controller M Action Unit) (m : M) (hprobe : C.choose m = .probe) :
    ¬ (Feasible world ⟨false, .select, 2⟩ [C.choose (C.revise m ()), .use] ∧
       Feasible world ⟨true, .select, 2⟩ [C.choose (C.revise m ()), .use]) := by
  let sense : World → Action → World → Unit := fun _ _ _ => ()
  have hf : Trace (closedLoop C world sense)
      (⟨false, .start, 3⟩, m) [(.probe, ())]
      (⟨false, .select, 2⟩, C.revise m ()) := by
    exact trace_singleton_iff.mpr ⟨by simp [world], hprobe.symm, rfl, rfl⟩
  have ht : Trace (closedLoop C world sense)
      (⟨true, .start, 3⟩, m) [(.probe, ())]
      (⟨true, .select, 2⟩, C.revise m ()) := by
    exact trace_singleton_iff.mpr ⟨by simp [world], hprobe.symm, rfl, rfl⟩
  exact same_feedback_excludes_incompatible_futures C world world sense sense hf ht
    rfl rfl (fun a ha hb => opposite_modes_incompatible a ⟨ha, hb⟩)

theorem shared_current_signal_retains_mode (b : Bool) :
    learner.revise (.learned b) none = .prepared b := rfl

theorem different_retained_modes_after_same_signal :
    learner.revise (.learned false) none ≠ learner.revise (.learned true) none := by
  decide

end Generative.Learning.Examples

#print axioms Generative.Learning.Examples.world_account
#print axioms Generative.Learning.Examples.feedback_account
#print axioms Generative.Learning.Examples.world_trace_exact_cost
#print axioms Generative.Learning.Examples.three_event_trace_needs_three
#print axioms Generative.Learning.Examples.accurate_feedback_completes
#print axioms Generative.Learning.Examples.wrong_response_executes
#print axioms Generative.Learning.Examples.dead_no_event
#print axioms Generative.Learning.Examples.prepared_without_fuel_cannot_use
#print axioms Generative.Learning.Examples.misleading_feedback_reaches_dead
#print axioms Generative.Learning.Examples.misleading_feedback_cannot_use
#print axioms Generative.Learning.Examples.response_then_use_requires_match
#print axioms Generative.Learning.Examples.opposite_modes_incompatible
#print axioms Generative.Learning.Examples.blind_probe_cannot_solve_both
#print axioms Generative.Learning.Examples.shared_current_signal_retains_mode
#print axioms Generative.Learning.Examples.different_retained_modes_after_same_signal
