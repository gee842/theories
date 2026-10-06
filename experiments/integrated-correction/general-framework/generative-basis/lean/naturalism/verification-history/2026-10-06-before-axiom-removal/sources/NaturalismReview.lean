import NaturalismIdentity

/-!
# Corrections after review

An independent review accepted the proofs of `WholeQualityNaturalism` and
`NaturalismIdentity` but found their descriptions overclaimed. This module
states the corrected forms. The earlier modules are unchanged.

* The structural credentials hold for **every** step relation, so they do not
  single out continuation inclusion or any orientation (`credentials_hold_for_every_relation`).
* `NonUndermining` constrains all state pairs, including pairs no transition joins.
  `TransitionNonUndermining` constrains only actual transitions. In `switching`, where
  moving between the two states actually occurs, every complete ranking, including every
  scalar welfare ranking, endorses an actual transition that removes a realizable activity
  (`total_orders_undermine_on_transitions`, `scalar_ranking_undermines_on_transitions`).
* The same objection reaches continuation inclusion itself: every actual exclusive choice
  registers as damage (`every_exclusive_choice_registers_as_damage`). Restraint is one
  instance of a general fact: choosing forecloses alternatives.
* The quality is binary non-loss. A fully recovered dip is condemned exactly as an
  unrecovered fall would be (`recovered_dip_still_condemned`).
-/

namespace Generative.Naturalism

open Generative.EthicalOrientation

universe u v

variable {State : Type u} {Action : Type v}

/-- Supervenience on visited states and composition hold for an arbitrary relation. -/
theorem credentials_hold_for_every_relation (P : Process State Action) :
    ∀ R : State → State → Prop,
      Supervenes (fun h : History P => Along R h.2.2) History.states ∧
      ∀ {s m t : State} (r : Run P s m) (r' : Run P m t),
        (Along R (r.append r') ↔ Along R r ∧ Along R r') :=
  fun R => ⟨along_supervenes_on_states P R, fun r r' => along_append R r r'⟩

/-- Following `R` along an actual transition never removes a realizable activity. -/
def TransitionNonUndermining (P : Process State Action) (R : State → State → Prop) : Prop :=
  ∀ s a t, P.step s a t → R s t → ∀ word, Feasible P s word → Feasible P t word

/-- Two states, each with its own activity, and an actual move between them. -/
def switching : Process Bool (Option Bool) where
  step s a t := match a with
    | none => t = !s
    | some b => b = s ∧ t = s

theorem switching_own (s : Bool) : Feasible switching s [some s] :=
  ⟨s, .cons (show s = s ∧ s = s from ⟨rfl, rfl⟩) (.nil s)⟩

theorem switching_not_other (s : Bool) : ¬ Feasible switching (!s) [some s] := by
  rintro ⟨t, h⟩
  cases h with
  | cons hs _ =>
    have e : s = !s := hs.1
    cases s <;> exact absurd e (by decide)

/-- Every complete ranking endorses an actual transition that removes an activity. -/
theorem total_orders_undermine_on_transitions (R : Bool → Bool → Prop)
    (htotal : ∀ x y, R x y ∨ R y x) : ¬ TransitionNonUndermining switching R := by
  intro h
  cases htotal true false with
  | inl hr =>
    exact switching_not_other true
      (h true none false (show false = !true from rfl) hr _ (switching_own true))
  | inr hr =>
    exact switching_not_other false
      (h false none true (show true = !false from rfl) hr _ (switching_own false))

theorem scalar_ranking_undermines_on_transitions (welfare : Bool → Nat) :
    ¬ TransitionNonUndermining switching (fun x y => welfare x ≤ welfare y) :=
  total_orders_undermine_on_transitions _ (fun x y => Nat.le_total (welfare x) (welfare y))

/-- Continuation inclusion avoids this only by endorsing neither actual move. -/
theorem generation_endorses_no_switch :
    ¬ ContinuationLe switching true false ∧ ¬ ContinuationLe switching false true :=
  ⟨witness_refutes_preservation ⟨switching_own true, switching_not_other true⟩,
    witness_refutes_preservation ⟨switching_own false, switching_not_other false⟩⟩

/-- From an open state, committing to either of two exclusive courses is an actual
transition, and each registers as damage. -/
def committing : Process (Option Bool) (Option Bool) where
  step s a t := match s, a with
    | none, none => t = some true ∨ t = some false
    | some b, some c => c = b ∧ t = some b
    | _, _ => False

theorem committing_open_can (b : Bool) : Feasible committing none [none, some b] :=
  ⟨some b, .cons (show some b = some true ∨ some b = some false by cases b <;> simp)
    (.cons (show b = b ∧ some b = some b from ⟨rfl, rfl⟩) (.nil _))⟩

theorem committing_lost (b : Bool) : ¬ Feasible committing (some b) [none, some (!b)] := by
  rintro ⟨t, h⟩
  cases h with
  | cons hs _ => exact hs

theorem every_exclusive_choice_registers_as_damage (b : Bool) :
    committing.step none none (some b) ∧ ¬ ContinuationLe committing none (some b) := by
  constructor
  · show some b = some true ∨ some b = some false
    cases b
    · exact Or.inr rfl
    · exact Or.inl rfl
  · intro h
    exact committing_lost b (h _ (committing_open_can (!b)))

/-- Recovery does not offset an intermediate loss in this binary quality. -/
theorem recovered_dip_still_condemned :
    ContinuationLe dip 2 2 ∧ ¬ Along (ContinuationLe dip) dipped :=
  ⟨fun _ h => h, quality_not_fixed_by_endpoints_and_word.2.2⟩

end Generative.Naturalism

#print axioms Generative.Naturalism.credentials_hold_for_every_relation
#print axioms Generative.Naturalism.switching_own
#print axioms Generative.Naturalism.switching_not_other
#print axioms Generative.Naturalism.total_orders_undermine_on_transitions
#print axioms Generative.Naturalism.scalar_ranking_undermines_on_transitions
#print axioms Generative.Naturalism.generation_endorses_no_switch
#print axioms Generative.Naturalism.committing_open_can
#print axioms Generative.Naturalism.committing_lost
#print axioms Generative.Naturalism.every_exclusive_choice_registers_as_damage
#print axioms Generative.Naturalism.recovered_dip_still_condemned
