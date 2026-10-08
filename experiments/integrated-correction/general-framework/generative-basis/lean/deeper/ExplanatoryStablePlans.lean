import ExplanatoryChangingSupport

/-! Interleaved changes and plan progress share the same physical change law.
Guards preserve this fixed target, not every possible target or ethical value. -/
namespace Generative.ExplanatoryStablePlans
open ExplanatoryChangingSupport ExplanatoryCoexistence ExplanatoryFootprints ExplanatoryJointness
universe u
variable {R : Type u} [DecidableEq R]

structure Position (R : Type u) where
  configuration : Configuration R
  done : List R
  remaining : List R
  deriving DecidableEq

inductive Event (R : Type u) where
  | change : Change R → Event R
  | advance : Event R
  deriving DecidableEq

def raw : Process (Position R) (Event R) where
  step s event t := match event with
    | .change c => enabled s.configuration c ∧
        t = ⟨after s.configuration c, s.done, s.remaining⟩
    | .advance => ∃ a rest, s.remaining = a :: rest ∧ enabled s.configuration (.take a) ∧
        t = ⟨after s.configuration (.take a), s.done ++ [a], rest⟩

def guarded : Process (Position R) (Event R) where
  step s event t := raw.step s event t ∧ match event with
    | .change c => Guard s.done s.remaining c
    | .advance => True

def Valid (s : Position R) : Prop := Certificate s.configuration s.done s.remaining

def native : Process (Configuration R) (Change R) where
  step s c t := enabled s c ∧ t = after s c

theorem raw_step_native {s t : Position R} {e : Event R} (h : raw.step s e t) :
    ∃ c, native.step s.configuration c t.configuration := by
  cases e with
  | change c => obtain ⟨en, rfl⟩ := h; exact ⟨c, en, rfl⟩
  | advance => obtain ⟨a, rest, _, en, rfl⟩ := h; exact ⟨.take a, en, rfl⟩

theorem guarded_iff_preserves {s t : Position R} {e : Event R}
    (valid : Valid s) (step : raw.step s e t) : guarded.step s e t ↔ Valid t := by
  have original := step
  cases e with
  | change c =>
    obtain ⟨_, rfl⟩ := step
    exact ⟨fun h => (change_preserves_iff_guard valid c).mpr h.2,
      fun h => ⟨original, (change_preserves_iff_guard valid c).mp h⟩⟩
  | advance =>
    obtain ⟨a, rest, eq, _, rfl⟩ := step
    have h : Certificate s.configuration s.done (a :: rest) := eq ▸ valid
    exact ⟨fun _ => advance_certificate h, fun _ => ⟨original, True.intro⟩⟩

theorem step_valid {s t : Position R} {e : Event R} (valid : Valid s)
    (h : guarded.step s e t) : Valid t := (guarded_iff_preserves valid h.1).mp h

theorem trace_valid {s t : Position R} {events : List (Event R)}
    (valid : Valid s) (h : Trace guarded s events t) : Valid t := by
  induction h with
  | nil => exact valid
  | cons step _ ih => exact ih (step_valid valid step)

theorem raw_step_goal {s t : Position R} {e : Event R} (h : raw.step s e t) :
    t.done ++ t.remaining = s.done ++ s.remaining := by
  cases e with
  | change c => obtain ⟨_, rfl⟩ := h; rfl
  | advance =>
    obtain ⟨a, rest, eq, _, rfl⟩ := h
    simp [eq, List.append_assoc]

theorem trace_goal {s t : Position R} {events : List (Event R)}
    (h : Trace guarded s events t) : t.done ++ t.remaining = s.done ++ s.remaining := by
  induction h with
  | nil => rfl
  | cons step _ ih => exact ih.trans (raw_step_goal step.1)

theorem trace_has_native_history {s t : Position R} {events : List (Event R)}
    (h : Trace guarded s events t) :
    ∃ changes : List (Change R), changes.length = events.length ∧
      Trace native s.configuration changes t.configuration := by
  induction h with
  | nil => exact ⟨[], rfl, Trace.nil _⟩
  | cons step _ ih =>
    obtain ⟨c, physical⟩ := raw_step_native step.1
    obtain ⟨cs, length, tail⟩ := ih
    exact ⟨c :: cs, by simp [length], Trace.cons physical tail⟩

theorem complete_by_advancing (rest : List R) : ∀ (s : Configuration R) (done : List R),
    Certificate s done rest → ∃ t : Position R,
      Trace guarded ⟨s, done, rest⟩ (List.replicate rest.length .advance) t ∧
      t.remaining = [] ∧ t.done = done ++ rest ∧ Valid t := by
  induction rest with
  | nil =>
    intro s done h
    exact ⟨⟨s, done, []⟩, Trace.nil _, rfl, by simp, h⟩
  | cons a rest ih =>
    intro s done h
    obtain ⟨t, trace, empty, final, good⟩ := ih (after s (.take a)) (done ++ [a]) (advance_certificate h)
    refine ⟨t, ?_, empty, ?_, good⟩
    · apply Trace.cons (m := ⟨after s (.take a), done ++ [a], rest⟩)
      · exact ⟨⟨a, rest, rfl, advance_enabled h, rfl⟩, True.intro⟩
      · exact trace
    · simpa [List.append_assoc] using final

theorem after_every_history_can_complete {s t : Position R} {events : List (Event R)}
    (valid : Valid s) (history : Trace guarded s events t) :
    ∃ final : Position R, Trace guarded t (List.replicate t.remaining.length .advance) final ∧
      final.remaining = [] ∧ final.done = s.done ++ s.remaining ∧
      ∀ a, a ∈ s.done ++ s.remaining → a ∈ final.configuration.busy := by
  obtain ⟨last, tail, empty, done, h⟩ := complete_by_advancing t.remaining t.configuration t.done
    (trace_valid valid history)
  have same : last.done = s.done ++ s.remaining := done.trans (trace_goal history)
  refine ⟨last, tail, empty, same, ?_⟩
  intro a ha
  exact h.2.1 a (same.symm ▸ ha)

theorem unbounded_schedule_certificate (states : Nat → Position R) (events : Nat → Event R)
    (initial : Valid (states 0))
    (steps : ∀ n, guarded.step (states n) (events n) (states (n + 1))) :
    ∀ n, Valid (states n) := by
  intro n
  induction n with
  | zero => exact initial
  | succ n ih => exact step_valid ih (steps n)

def advances : List (Event R) → Nat
  | [] => 0
  | .advance :: es => 1 + advances es
  | .change _ :: es => advances es

theorem trace_progress_count {s t : Position R} {events : List (Event R)}
    (h : Trace guarded s events t) : t.remaining.length + advances events = s.remaining.length := by
  induction h with
  | nil => simp [advances]
  | @cons s m t e es step _ ih =>
    cases e with
    | change c =>
      obtain ⟨_, rfl⟩ := step.1
      exact ih
    | advance =>
      obtain ⟨a, rest, eq, _, rfl⟩ := step.1
      simp only [advances, eq, List.length_cons] at *
      omega

theorem completion_iff_progress_count {s t : Position R} {events : List (Event R)}
    (h : Trace guarded s events t) : t.remaining = [] ↔ advances events = s.remaining.length := by
  have count := trace_progress_count h
  constructor
  · intro empty; simpa [empty] using count
  · intro all
    have zero : t.remaining.length = 0 := by omega
    exact List.length_eq_zero_iff.mp zero

omit [DecidableEq R] in
theorem native_plan_initial_certificate (available : List R) (p : Plan (List R))
    (h : Realizes joint (Supported support) available p) :
    Certificate ⟨available, []⟩ [] (Requests p) := by
  apply (initial_certificate_iff _ _).mpr
  obtain ⟨nodup, all⟩ := (realize_iff_supported p available).mp h
  exact ⟨nodup, fun a ha => ⟨all a ha, by simp⟩⟩

theorem native_trace_wellformed {s t : Configuration R} {changes : List (Change R)}
    (h : WellFormed s) (history : Trace native s changes t) : WellFormed t := by
  induction history with
  | nil => exact h
  | cons step _ ih =>
    obtain ⟨en, rfl⟩ := step
    exact ih (enabled_change_preserves_wellformed h _ en)

theorem guarded_trace_wellformed {s t : Position R} {events : List (Event R)}
    (h : WellFormed s.configuration) (history : Trace guarded s events t) : WellFormed t.configuration := by
  obtain ⟨_, _, physical⟩ := trace_has_native_history history
  exact native_trace_wellformed h physical

end Generative.ExplanatoryStablePlans

#print axioms Generative.ExplanatoryStablePlans.raw_step_native
#print axioms Generative.ExplanatoryStablePlans.guarded_iff_preserves
#print axioms Generative.ExplanatoryStablePlans.step_valid
#print axioms Generative.ExplanatoryStablePlans.trace_valid
#print axioms Generative.ExplanatoryStablePlans.raw_step_goal
#print axioms Generative.ExplanatoryStablePlans.trace_goal
#print axioms Generative.ExplanatoryStablePlans.trace_has_native_history
#print axioms Generative.ExplanatoryStablePlans.complete_by_advancing
#print axioms Generative.ExplanatoryStablePlans.after_every_history_can_complete
#print axioms Generative.ExplanatoryStablePlans.unbounded_schedule_certificate
#print axioms Generative.ExplanatoryStablePlans.trace_progress_count
#print axioms Generative.ExplanatoryStablePlans.completion_iff_progress_count
#print axioms Generative.ExplanatoryStablePlans.native_plan_initial_certificate
#print axioms Generative.ExplanatoryStablePlans.native_trace_wellformed
#print axioms Generative.ExplanatoryStablePlans.guarded_trace_wellformed
