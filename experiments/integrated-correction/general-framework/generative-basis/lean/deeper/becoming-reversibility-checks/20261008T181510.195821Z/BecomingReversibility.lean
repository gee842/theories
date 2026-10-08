import GenerativeCore

/-!+Reachability and loss within one fixed relational process. Configuration
identity, the step law and finite traces remain supplied. Endpoint predicates
are mathematical tests, not an assertion of omniscient observation. Returning
to a configuration does not erase a history or its experienced losses.
-/
namespace BecomingReversibility
open Generative
universe u v

def Reach {S : Type u} {A : Type v} (P : Process S A) (s t : S) : Prop :=
  ∃ word, Trace P s word t

def Possible {S : Type u} {A : Type v} (P : Process S A)
    (s : S) (q : S → Prop) : Prop := ∃ t, Reach P s t ∧ q t

theorem reach_refl {S : Type u} {A : Type v} (P : Process S A) (s : S) :
    Reach P s s := ⟨[], .nil s⟩

theorem reach_trans {S : Type u} {A : Type v} {P : Process S A} {s t r : S}
    (h : Reach P s t) (k : Reach P t r) : Reach P s r := by
  obtain ⟨xs, hx⟩ := h
  obtain ⟨ys, hy⟩ := k
  exact ⟨xs ++ ys, trace_append_iff.mpr ⟨t, hx, hy⟩⟩

theorem possible_before_reached {S : Type u} {A : Type v}
    {P : Process S A} {s t : S} {q : S → Prop}
    (h : Reach P s t) (k : Possible P t q) : Possible P s q := by
  obtain ⟨r, hr, hq⟩ := k
  exact ⟨r, reach_trans h hr, hq⟩

/-- One exact endpoint test suffices for the converse. Its availability as
knowledge is not implied by this structural result. -/
theorem no_endpoint_loss_iff_return {S : Type u} {A : Type v}
    {P : Process S A} {s t : S} :
    (∀ q, Possible P s q → Possible P t q) ↔ Reach P t s := by
  constructor
  · intro h
    obtain ⟨r, hr, eq⟩ := h (fun r => r = s) ⟨s, reach_refl P s, rfl⟩
    subst r
    exact hr
  · intro h q hq
    exact possible_before_reached h hq

theorem same_endpoint_possibilities_iff_return {S : Type u} {A : Type v}
    {P : Process S A} {s t : S} (h : Reach P s t) :
    (∀ q, Possible P s q ↔ Possible P t q) ↔ Reach P t s := by
  constructor
  · intro eq
    exact no_endpoint_loss_iff_return.mp (fun q => (eq q).mp)
  · intro back q
    exact ⟨possible_before_reached back, possible_before_reached h⟩

/-- Constructive witness: the lost question is return to this configuration.
This is structural loss, not an ethical ranking or an entropy theorem. -/
theorem irreversible_iff_endpoint_loss {S : Type u} {A : Type v}
    {P : Process S A} {s t : S} :
    (¬ Reach P t s) ↔ ∃ q, Possible P s q ∧ ¬ Possible P t q := by
  constructor
  · intro noReturn
    refine ⟨(fun r => r = s), ⟨s, reach_refl P s, rfl⟩, ?_⟩
    rintro ⟨r, hr, eq⟩
    subst r
    exact noReturn hr
  · rintro ⟨q, before, after⟩ back
    exact after (possible_before_reached back before)

/-- Lost reachability cannot be repaired later under the same complete law:
any such repair would itself already have been a path from t. -/
theorem loss_persists_along_continuation {S : Type u} {A : Type v}
    {P : Process S A} {t r : S} {q : S → Prop}
    (lost : ¬ Possible P t q) (later : Reach P t r) : ¬ Possible P r q := by
  intro restored
  exact lost (possible_before_reached later restored)

/- A declared ordered pair records the before/after of one relation's change,
not independent agents. Either event forms the same visible activity; only
one law provides a restoring event. The observation deliberately omits which
stage was reached, and therefore cannot certify return. -/
def oneWay : Process Bool Unit where
  step s _ t := s = false ∧ t = true

def twoWay : Process Bool Unit where
  step s _ t := t = !s

theorem oneWay_no_return : ¬ Reach oneWay true false := by
  rintro ⟨word, h⟩
  cases h with
  | nil => contradiction
  | cons step _ => exact Bool.noConfusion step.1

theorem same_occurring_change_different_return :
    Trace oneWay false [()] true ∧ Trace twoWay false [()] true ∧
    ¬ Reach oneWay true false ∧ Reach twoWay true false := by
  exact ⟨trace_singleton_iff.mpr ⟨rfl, rfl⟩,
    trace_singleton_iff.mpr rfl, oneWay_no_return,
    ⟨[()], trace_singleton_iff.mpr rfl⟩⟩

/-- Every predicate on the supplied constant observation has the same answer.
This shows omitted information, not a counterexample to full relations. -/
theorem incomplete_questions_can_hide_irreversibility :
    (∀ q : Unit → Prop,
      Possible oneWay false (fun _ => q ()) ↔
      Possible oneWay true (fun _ => q ())) ∧ ¬ Reach oneWay true false := by
  refine ⟨?_, oneWay_no_return⟩
  intro q
  constructor
  · rintro ⟨_, _, hq⟩
    exact ⟨true, reach_refl oneWay true, hq⟩
  · rintro ⟨_, _, hq⟩
    exact ⟨false, reach_refl oneWay false, hq⟩

end BecomingReversibility
