import GenerativeCore

/-!
# Enacted evidence and the scope of a finite inquiry

This is an audit of two proposed grounding steps, not a premise-free derivation
of the generative ontology. The first step exposes the actual witness and the
interpretation required by a performative occurrence argument. The second
preserves any supplied finite process history in a bounded replay. At every
positive remaining count all original action labels are enabled exactly when
they were enabled in the original process; each step retains its original
state-to-state relation. The endpoint has no further transition.

The count is an explicit mathematical construction, not a discovered universal
clock, material stock or hidden assumption about actual inquiry. Replay does
not preserve unbounded futures or laws asserting their availability. It cannot
refute a richer account that independently warrants those laws. No new claim
about consciousness, universal ethics, or the impossibility of grounding is made.
-/

namespace Generative.EnactedFoundation

universe u v w

/-- Occurrence follows from an actual interpreted token, without assuming that
the propositional content of that token is true. Both inputs remain visible. -/
theorem occurrence_from_enactment {Token : Type w}
    (occurs denies : Token → Prop)
    (correspondence : ∀ x, denies x → occurs x)
    {x : Token} (enacted : denies x) : ∃ y, occurs y :=
  ⟨x, correspondence x enacted⟩

/-- The same inputs defeat a denial of all occurrence. This does not prove
that an actual token exists from logic alone. -/
theorem enacted_denial_excludes_no_occurrence {Token : Type w}
    (occurs denies : Token → Prop)
    (correspondence : ∀ x, denies x → occurs x)
    {x : Token} (enacted : denies x) : ¬ (∀ y, ¬ occurs y) := by
  intro none
  exact none x (correspondence x enacted)

variable {State : Type u} {Action : Type v}

/-- Restrict continuation by a finite count while retaining the original
configurations and labelled transition relation under projection. -/
def bounded (P : Process State Action) : Process (State × Nat) Action where
  step s a t := P.step s.1 a t.1 ∧ s.2 = t.2 + 1

theorem positive_count_preserves_enabled (P : Process State Action)
    (s : State) (n : Nat) (a : Action) :
    Enabled (bounded P) (s, n + 1) a ↔ Enabled P s a := by
  constructor
  · rintro ⟨t, ht⟩
    exact ⟨t.1, ht.1⟩
  · rintro ⟨t, ht⟩
    exact ⟨(t, n), ht, rfl⟩

theorem zero_count_has_no_step (P : Process State Action)
    (s : State) (a : Action) (t : State × Nat) :
    ¬ (bounded P).step (s, 0) a t := by
  intro h
  exact Nat.noConfusion h.2

theorem zero_count_has_no_enabled (P : Process State Action)
    (s : State) (a : Action) : ¬ Enabled (bounded P) (s, 0) a := by
  rintro ⟨t, ht⟩
  exact zero_count_has_no_step P s a t ht

theorem bounded_trace_projects {P : Process State Action}
    {s t : State × Nat} {as : List Action}
    (h : Trace (bounded P) s as t) : Trace P s.1 as t.1 := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs.1 ih

theorem bounded_trace_count {P : Process State Action}
    {s t : State × Nat} {as : List Action}
    (h : Trace (bounded P) s as t) : s.2 = t.2 + as.length := by
  induction h with
  | nil => exact (Nat.add_zero _).symm
  | @cons s m t a as hs _ ih =>
    calc
      s.2 = m.2 + 1 := hs.2
      _ = (t.2 + as.length) + 1 := congrArg (fun k => k + 1) ih
      _ = t.2 + (a :: as).length := Nat.add_assoc _ _ _

theorem finite_trace_lifts {P : Process State Action}
    {s t : State} {as : List Action} (h : Trace P s as t) (n : Nat) :
    Trace (bounded P) (s, n + as.length) as (t, n) := by
  induction h with
  | nil s0 =>
    simpa only [List.length_nil, Nat.add_zero] using
      (Trace.nil (P := bounded P) (s0, n))
  | @cons s m t a as hs _ ih =>
    exact .cons ⟨hs, (Nat.add_assoc n as.length 1).symm⟩ ih

/-- Exact characterization: the original history and its count relation are
jointly sufficient. There is no reset of original records or intermediate states. -/
theorem bounded_trace_iff (P : Process State Action)
    (s t : State) (n m : Nat) (as : List Action) :
    Trace (bounded P) (s, n) as (t, m) ↔
      Trace P s as t ∧ n = m + as.length := by
  constructor
  · intro h
    exact ⟨bounded_trace_projects h, bounded_trace_count h⟩
  · rintro ⟨h, rfl⟩
    exact finite_trace_lifts h m

/-- Any given finite inquiry can be retained with a terminal endpoint. This
only tests inferences whose grounds are that history and its projected relations. -/
theorem finite_trace_has_terminal_replay {P : Process State Action}
    {s t : State} {as : List Action} (h : Trace P s as t) :
    Trace (bounded P) (s, as.length) as (t, 0) ∧
      (∀ a, ¬ Enabled (bounded P) (t, 0) a) := by
  constructor
  · simpa only [Nat.zero_add] using finite_trace_lifts h 0
  · exact zero_count_has_no_enabled P t

theorem bounded_trace_length_le {P : Process State Action}
    {s t : State × Nat} {as : List Action}
    (h : Trace (bounded P) s as t) : as.length ≤ s.2 := by
  calc
    as.length ≤ t.2 + as.length := Nat.le_add_left _ _
    _ = s.2 := (bounded_trace_count h).symm

end Generative.EnactedFoundation

#print axioms Generative.EnactedFoundation.occurrence_from_enactment
#print axioms Generative.EnactedFoundation.enacted_denial_excludes_no_occurrence
#print axioms Generative.EnactedFoundation.positive_count_preserves_enabled
#print axioms Generative.EnactedFoundation.zero_count_has_no_step
#print axioms Generative.EnactedFoundation.zero_count_has_no_enabled
#print axioms Generative.EnactedFoundation.bounded_trace_projects
#print axioms Generative.EnactedFoundation.bounded_trace_count
#print axioms Generative.EnactedFoundation.finite_trace_lifts
#print axioms Generative.EnactedFoundation.bounded_trace_iff
#print axioms Generative.EnactedFoundation.finite_trace_has_terminal_replay
#print axioms Generative.EnactedFoundation.bounded_trace_length_le
