import GenerativeCore
import GeneratedPaths

/-!
# Predication and finite prediction over the existing process core

An expository companion, not a new physical or ethical law. May is existential
endpoint satisfaction; Must is universal endpoint satisfaction for one fixed
finite event word. Must can hold when that word has no execution. Neither
predicate supplies a policy, probability, fairness or an infinite continuation.
-/

namespace Generative.CorePredication

universe u v
variable {State : Type u} {Event : Type v}

def May (P : Process State Event) (word : List Event)
    (Q : State → Prop) (s : State) : Prop :=
  ∃ t, Trace P s word t ∧ Q t

def Must (P : Process State Event) (word : List Event)
    (Q : State → Prop) (s : State) : Prop :=
  ∀ t, Trace P s word t → Q t

theorem may_append_iff (P : Process State Event) (xs ys : List Event)
    (Q : State → Prop) (s : State) :
    May P (xs ++ ys) Q s ↔ May P xs (May P ys Q) s := by
  constructor
  · rintro ⟨t, ht, hQ⟩
    obtain ⟨m, hx, hy⟩ := trace_append_iff.mp ht
    exact ⟨m, hx, t, hy, hQ⟩
  · rintro ⟨m, hx, t, hy, hQ⟩
    exact ⟨t, trace_append_iff.mpr ⟨m, hx, hy⟩, hQ⟩

theorem must_append_iff (P : Process State Event) (xs ys : List Event)
    (Q : State → Prop) (s : State) :
    Must P (xs ++ ys) Q s ↔ Must P xs (Must P ys Q) s := by
  constructor
  · intro h m hx t hy
    exact h t (trace_append_iff.mpr ⟨m, hx, hy⟩)
  · intro h t ht
    obtain ⟨m, hx, hy⟩ := trace_append_iff.mp ht
    exact h m hx t hy

theorem trace_invariant (P : Process State Event) (I : State → Prop)
    (preserved : ∀ s a t, I s → P.step s a t → I t)
    {s t : State} {word : List Event} : Trace P s word t → I s → I t := by
  intro h
  induction h with
  | nil => exact fun hs => hs
  | cons hstep _ ih =>
    intro hs
    exact ih (preserved _ _ _ hs hstep)

theorem reach_invariant (P : Process State Event) (I : State → Prop)
    (preserved : ∀ s a t, I s → P.step s a t → I t)
    {s t : State} (reachable : Deeper.Reach P s t) (initial : I s) : I t := by
  obtain ⟨word, h⟩ := reachable
  exact trace_invariant P I preserved h initial

theorem invariant_excludes_endpoint (P : Process State Event) (I : State → Prop)
    (preserved : ∀ s a t, I s → P.step s a t → I t)
    {s t : State} (initial : I s) (excluded : ¬ I t) : ¬ Deeper.Reach P s t := by
  intro h
  exact excluded (reach_invariant P I preserved h initial)

theorem feasible_and_must_implies_may (P : Process State Event)
    (word : List Event) (Q : State → Prop) (s : State)
    (feasible : Feasible P s word) (allEndpoints : Must P word Q s) :
    May P word Q s := by
  obtain ⟨t, ht⟩ := feasible
  exact ⟨t, ht, allEndpoints t ht⟩

theorem deterministic_trace_endpoint (P : Process State Event)
    (det : ∀ s a t r, P.step s a t → P.step s a r → t = r)
    {s t r : State} {word : List Event}
    (left : Trace P s word t) (right : Trace P s word r) : t = r := by
  induction left generalizing r with
  | nil => exact trace_nil_iff.mp right
  | cons hstep _ ih =>
    obtain ⟨m, hm, htail⟩ := trace_cons_iff.mp right
    have heq := det _ _ _ _ hstep hm
    cases heq
    exact ih htail

theorem deterministic_may_implies_must (P : Process State Event)
    (det : ∀ s a t r, P.step s a t → P.step s a r → t = r)
    (word : List Event) (Q : State → Prop) (s : State)
    (possible : May P word Q s) : Must P word Q s := by
  obtain ⟨t, ht, hQ⟩ := possible
  intro r hr
  have heq := deterministic_trace_endpoint P det ht hr
  exact heq ▸ hQ

def branching : Process Bool Unit where
  step _ _ _ := True

def blocked : Process Bool Unit where
  step _ _ _ := False

theorem possible_not_guaranteed :
    May branching [()] (fun t => t = true) false ∧
      ¬ Must branching [()] (fun t => t = true) false := by
  constructor
  · exact ⟨true, trace_singleton_iff.mpr True.intro, rfl⟩
  · intro h
    have impossible : false = true := h false (trace_singleton_iff.mpr True.intro)
    cases impossible

theorem blocked_word_not_feasible : ¬ Feasible blocked false [()] := by
  rintro ⟨t, ht⟩
  exact trace_singleton_iff.mp ht

theorem blocked_must_is_vacuous :
    Must blocked [()] (fun _ => False) false := by
  intro t ht
  exact trace_singleton_iff.mp ht

theorem blocked_may_is_false : ¬ May blocked [()] (fun _ => True) false := by
  rintro ⟨t, ht, _⟩
  exact blocked_word_not_feasible ⟨t, ht⟩

end Generative.CorePredication

#print axioms Generative.CorePredication.may_append_iff
#print axioms Generative.CorePredication.must_append_iff
#print axioms Generative.CorePredication.trace_invariant
#print axioms Generative.CorePredication.reach_invariant
#print axioms Generative.CorePredication.invariant_excludes_endpoint
#print axioms Generative.CorePredication.feasible_and_must_implies_may
#print axioms Generative.CorePredication.deterministic_trace_endpoint
#print axioms Generative.CorePredication.deterministic_may_implies_must
#print axioms Generative.CorePredication.possible_not_guaranteed
#print axioms Generative.CorePredication.blocked_word_not_feasible
#print axioms Generative.CorePredication.blocked_must_is_vacuous
#print axioms Generative.CorePredication.blocked_may_is_false
