import RelationalDynamics

/-!
# Continuation read relationally: what remains of a dynamics without supplied identities

`RelationalDynamics` shows that for one kind of event, identifying configurations
by their relations leaves one dynamics that continues (the single recurrence) and
one that does not (`idle`). This module asks the same question for any process,
with any events.

* **Continuation is relational.** A configuration *continues* when it lies in a
  region each member of which has a further event leading back into the region
  (`Continues`, a definition). It is exactly what a step keeps
  (`continues_step`, `continues_of_step`), it is implied by every unending run
  (`continues_of_run`), it gives histories of every finite length
  (`continues_histories`), and related configurations agree on it
  (`bisimulation_continues`, `continuation_separates`). So the difference between
  continuing and not continuing is a difference of relations, not of supplied
  identities.
* **The continuing part is one recurrence.** Restrict any process to its
  continuing configurations (`coreProcess`) and do not supply which event is
  which (`erase`). The result is the single recurrence, whatever the carrier and
  the events (`core_erased_is_one_recurrence`).
* **Event identity is the remaining supplied distinction.** With event kinds kept
  as given, two processes can both continue from every configuration, have no
  configurations related at all, and still erase to the same single recurrence
  (`labels_carry_remaining_difference`). So continuation alone does not select
  among several-event dynamics; this counterexample is preserved.

Reading. Once neither carrier identity nor event identity is supplied, what a
dynamics says is where continuation is kept and where it is lost, that is, how
the unfolding keeps or loses the conditions for its own further unfolding. That
last sentence is a reading connecting this result to the research center, not a
theorem. Whether event kinds can themselves be identified by their relations,
and which labelled dynamics that would leave, is open.
-/

namespace Generative.Deeper

universe u v

/-- A configuration continues when it lies in a region each member of which has a
further event leading back into the region. -/
def Continues {S : Type u} {A : Type v} (P : Process S A) (s : S) : Prop :=
  ∃ C : S → Prop, C s ∧ ∀ x, C x → ∃ a y, P.step x a y ∧ C y

/-- A continuing configuration has a step to a continuing configuration. -/
theorem continues_step {S : Type u} {A : Type v} {P : Process S A} {s : S}
    (h : Continues P s) : ∃ a t, P.step s a t ∧ Continues P t := by
  obtain ⟨C, hs, closed⟩ := h
  obtain ⟨a, t, step, ht⟩ := closed s hs
  exact ⟨a, t, step, C, ht, closed⟩

/-- A step into a continuing configuration starts from a continuing one. -/
theorem continues_of_step {S : Type u} {A : Type v} {P : Process S A} {s t : S} {a : A}
    (step : P.step s a t) (h : Continues P t) : Continues P s := by
  obtain ⟨C, ht, closed⟩ := h
  refine ⟨fun x => x = s ∨ C x, Or.inl rfl, ?_⟩
  intro x hx
  cases hx with
  | inl e => subst e; exact ⟨a, t, step, Or.inr ht⟩
  | inr hc =>
    obtain ⟨b, y, step', hy⟩ := closed x hc
    exact ⟨b, y, step', Or.inr hy⟩

/-- Every unending run continues. -/
theorem continues_of_run {S : Type u} {A : Type v} {P : Process S A}
    (states : Nat → S) (events : Nat → A)
    (steps : ∀ n, P.step (states n) (events n) (states (n + 1))) (n : Nat) :
    Continues P (states n) := by
  refine ⟨fun x => ∃ k, states k = x, ⟨n, rfl⟩, ?_⟩
  intro x hx
  obtain ⟨k, e⟩ := hx
  subst e
  exact ⟨events k, states (k + 1), steps k, k + 1, rfl⟩

/-- A continuing configuration has histories of every finite length. -/
theorem continues_histories {S : Type u} {A : Type v} {P : Process S A} :
    ∀ (n : Nat) (s : S), Continues P s → ∃ word : List A, word.length = n ∧ Feasible P s word := by
  intro n
  induction n with
  | zero => intro s _; exact ⟨[], rfl, s, .nil s⟩
  | succ n ih =>
    intro s h
    obtain ⟨a, t, step, ht⟩ := continues_step h
    obtain ⟨word, len, final, trace⟩ := ih t ht
    exact ⟨a :: word, congrArg (· + 1) len, final, .cons step trace⟩

/-- Related configurations agree on continuation. -/
theorem bisimulation_continues {S : Type u} {T : Type u} {A : Type v}
    {P : Process S A} {Q : Process T A} {B : S → T → Prop}
    (bis : Bisimulation P Q B) {s : S} {t : T} (related : B s t)
    (h : Continues P s) : Continues Q t := by
  obtain ⟨C, hs, closed⟩ := h
  refine ⟨fun y => ∃ x, B x y ∧ C x, ⟨s, related, hs⟩, ?_⟩
  intro y hy
  obtain ⟨x, r, hx⟩ := hy
  obtain ⟨a, x', step, hx'⟩ := closed x hx
  obtain ⟨y', step', r'⟩ := bis.1 x y a x' r step
  exact ⟨a, y', step', x', r', hx'⟩

/-- No relational identity joins a continuing configuration to one that cannot
continue. -/
theorem continuation_separates {S : Type u} {T : Type u} {A : Type v}
    {P : Process S A} {Q : Process T A} {B : S → T → Prop}
    (bis : Bisimulation P Q B) {s : S} {t : T} (related : B s t) :
    Continues P s ↔ Continues Q t :=
  ⟨bisimulation_continues bis related,
    bisimulation_continues (bisimulation_converse bis) related⟩

/-- Do not supply which event is which: any event counts as the one event. -/
def erase {S : Type u} {A : Type v} (P : Process S A) : Process S Unit where
  step s _ t := ∃ a, P.step s a t

/-- The continuing configurations of a process with the events among them. -/
def coreProcess {S : Type u} {A : Type v} (P : Process S A) :
    Process {s : S // Continues P s} A where
  step s a t := P.step s.1 a t.1

/-- Every configuration of the continuing part has a further event within it. -/
theorem core_continues {S : Type u} {A : Type v} (P : Process S A)
    (s : {s : S // Continues P s}) : ∃ a t, (coreProcess P).step s a t := by
  obtain ⟨a, t, step, ht⟩ := continues_step s.2
  exact ⟨a, ⟨t, ht⟩, step⟩

/-- Without supplied carrier or event identities, the continuing part of any
process is the single recurrence. -/
theorem core_erased_is_one_recurrence {S : Type u} {A : Type v} (P : Process S A) :
    Bisimulation (erase (coreProcess P)) singletonLoop (fun _ _ => True) :=
  continuing_single_event_is_one_recurrence (erase (coreProcess P)) (fun s => by
    obtain ⟨a, t, step⟩ := core_continues P s
    exact ⟨t, a, step⟩)

/-- Two events, and only the first one ever happens. -/
def onlyFirst : Process Bool Bool where
  step _ a _ := a = false

/-- Two events, and they alternate with the configuration. -/
def alternating : Process Bool Bool where
  step s a t := a = s ∧ t = !s

theorem onlyFirst_continues (s : Bool) : Continues onlyFirst s :=
  ⟨fun _ => True, trivial, fun x _ => ⟨false, x, rfl, trivial⟩⟩

theorem alternating_continues (s : Bool) : Continues alternating s :=
  ⟨fun _ => True, trivial, fun x _ => ⟨x, !x, ⟨rfl, rfl⟩, trivial⟩⟩

/-- `[false, false]` happens in `onlyFirst` from every configuration and in
`alternating` from none. -/
theorem first_twice_separates (s t : Bool) :
    Feasible onlyFirst s [false, false] ∧ ¬ Feasible alternating t [false, false] := by
  refine ⟨⟨s, .cons (m := s) rfl (.cons (m := s) rfl (.nil s))⟩, ?_⟩
  rintro ⟨final, trace⟩
  cases trace with
  | cons step1 tail =>
    cases tail with
    | cons step2 _ =>
      obtain ⟨e1, m1⟩ := step1
      obtain ⟨e2, _⟩ := step2
      subst e1
      subst m1
      cases e2

/-- Continuation does not select among several-event dynamics: both processes
continue everywhere, no relation joins any of their configurations, and both
erase to the single recurrence. -/
theorem labels_carry_remaining_difference :
    (∀ s, Continues onlyFirst s) ∧ (∀ s, Continues alternating s) ∧
      (∀ (B : Bool → Bool → Prop) s t, B s t → ¬ Bisimulation onlyFirst alternating B) ∧
      Bisimulation (erase onlyFirst) singletonLoop (fun _ _ => True) ∧
      Bisimulation (erase alternating) singletonLoop (fun _ _ => True) := by
  refine ⟨onlyFirst_continues, alternating_continues, ?_, ?_, ?_⟩
  · intro B s t related bis
    exact (first_twice_separates s t).2
      ((bisimulation_same_histories bis related [false, false]).1 (first_twice_separates s t).1)
  · exact continuing_single_event_is_one_recurrence (erase onlyFirst)
      (fun s => ⟨s, false, rfl⟩)
  · exact continuing_single_event_is_one_recurrence (erase alternating)
      (fun s => ⟨!s, s, rfl, rfl⟩)

#print axioms Generative.Deeper.continues_step
#print axioms Generative.Deeper.continues_of_step
#print axioms Generative.Deeper.continues_of_run
#print axioms Generative.Deeper.continues_histories
#print axioms Generative.Deeper.bisimulation_continues
#print axioms Generative.Deeper.continuation_separates
#print axioms Generative.Deeper.core_continues
#print axioms Generative.Deeper.core_erased_is_one_recurrence
#print axioms Generative.Deeper.onlyFirst_continues
#print axioms Generative.Deeper.alternating_continues
#print axioms Generative.Deeper.first_twice_separates
#print axioms Generative.Deeper.labels_carry_remaining_difference

end Generative.Deeper
