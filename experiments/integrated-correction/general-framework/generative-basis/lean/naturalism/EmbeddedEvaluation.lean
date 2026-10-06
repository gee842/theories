import PremiseNecessity

/-!
# Evaluation as a relation inside the same process

The earlier modules compared a "quality" with a "natural base", as if they were two
kinds to be related. Here evaluation is not a second kind. It is a component of the
same process: a record that changes only with the process's own transitions, according
to a relation `E` between the states each transition joins.

* **Supervenience is derived, not assumed.** Along any history of the coupled process,
  the record says exactly whether `E` held across every transition of the same history
  (`record_tracks_whole_history`). The record is the whole-history relation, carried as
  part of the state; no further property is related to it.
* **Evaluation shares the conditions it evaluates.** Recording neither enables nor blocks
  any activity (`recording_enabled_iff`); it continues exactly as long as the process does.
  Under guidance that keeps continuation, every activity, the recording's own continuation
  included, stays realizable (`guided_recording_keeps_continuation`).
* **Which evaluation forms is part of the history.** The same law admits recording by
  continuation inclusion and recording by its converse; they read the same actual dip
  oppositely (`law_admits_opposite_recordings`). The orientation input proved necessary
  in `PremiseNecessity` is therefore the question of which recording relation forms and
  persists in the unfolding: a question about formation, as in the valuation-development
  study, and not a premise imported from outside the process.

This does not show which recording relation forms in any given history, nor that one
must. It removes the two-kinds framing; it does not answer the formation question.
-/

namespace Generative.Naturalism

open Generative.EthicalOrientation

universe u v

variable {State : Type u} {Action : Type v}

/-- The process with a record that changes only with its own transitions. -/
def recording (P : Process State Action) (E : State → State → Prop) :
    Process (State × Prop) Action where
  step x a y := P.step x.1 a y.1 ∧ (y.2 ↔ (x.2 ∧ E x.1 y.1))

/-- The same history, read without its record. -/
def Run.forget {P : Process State Action} {E : State → State → Prop} :
    {x y : State × Prop} → Run (recording P E) x y → Run P x.1 y.1
  | _, _, .nil x => .nil x.1
  | _, _, .cons a h r => .cons a h.1 (Run.forget r)

/-- The record is exactly the whole-history relation of the same history. -/
theorem record_tracks_whole_history {P : Process State Action} {E : State → State → Prop} :
    {x y : State × Prop} → (r : Run (recording P E) x y) →
    (y.2 ↔ (x.2 ∧ Along E r.forget))
  | _, _, .nil x => Iff.intro (fun h => ⟨h, True.intro⟩) (fun h => h.1)
  | _, _, .cons _ h r => by
    have ih := record_tracks_whole_history r
    constructor
    · intro hy
      have hm := ih.mp hy
      have hx := h.2.mp hm.1
      exact ⟨hx.1, hx.2, hm.2⟩
    · rintro ⟨hx, he, ha⟩
      exact ih.mpr ⟨h.2.mpr ⟨hx, he⟩, ha⟩

/-- Recording neither enables nor blocks an activity. -/
theorem recording_enabled_iff (P : Process State Action) (E : State → State → Prop)
    (x : State × Prop) (a : Action) :
    Enabled (recording P E) x a ↔ Enabled P x.1 a := by
  constructor
  · rintro ⟨y, hy⟩
    exact ⟨y.1, hy.1⟩
  · rintro ⟨t, ht⟩
    exact ⟨(t, x.2 ∧ E x.1 t), ht, Iff.rfl⟩

theorem recording_feasible_iff (P : Process State Action) (E : State → State → Prop) :
    (word : List Action) → (x : State × Prop) →
    (Feasible (recording P E) x word ↔ Feasible P x.1 word)
  | [], x => Iff.intro (fun _ => ⟨x.1, .nil _⟩) (fun _ => ⟨x, .nil _⟩)
  | a :: rest, x => by
    constructor
    · rintro ⟨y, h⟩
      obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
      obtain ⟨t, ht⟩ := (recording_feasible_iff P E rest m).mp ⟨y, hr⟩
      exact ⟨t, .cons hs.1 ht⟩
    · rintro ⟨t, h⟩
      obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
      obtain ⟨y, hy⟩ := (recording_feasible_iff P E rest (m, x.2 ∧ E x.1 m)).mpr ⟨t, hr⟩
      exact ⟨y, .cons (m := (m, x.2 ∧ E x.1 m))
        (show (recording P E).step x a (m, x.2 ∧ E x.1 m) from ⟨hs, Iff.rfl⟩) hy⟩

/-- Guided by continuation inclusion, the coupled process, recording included, keeps every
initially realizable activity at every visited state. -/
theorem guided_recording_keeps_continuation {P : Process State Action}
    {E : State → State → Prop} {x y : State × Prop} (r : Run (recording P E) x y)
    (hguided : Along (ContinuationLe P) r.forget) (word : List Action)
    (hw : Feasible (recording P E) x word) :
    ∀ z ∈ r.forget.states, Feasible (recording P E) (z, True) word := by
  intro z hz
  have := preserved_throughout word r.forget hguided ((recording_feasible_iff P E word x).mp hw) z hz
  exact (recording_feasible_iff P E word (z, True)).mpr this

/-- The fall from level 2 to level 1 in `dip`, carried with a record. -/
def fallRecorded (E : Nat → Nat → Prop) : Run (recording dip E) (2, True) (1, True ∧ E 2 1) :=
  .cons (m := (1, True ∧ E 2 1)) .go
    ⟨show dip.step 2 .go 1 from (show (1 : Nat) ≤ 2 ∧ (2 : Nat) ≤ 1 + 1 by decide), Iff.rfl⟩ (.nil _)

/-- One law, two recording relations that can form in it, opposite records of the same
actual transition. -/
theorem law_admits_opposite_recordings :
    ¬ (True ∧ ContinuationLe dip 2 1) ∧ (True ∧ converse (ContinuationLe dip) 2 1) :=
  ⟨fun h => witness_refutes_preservation ⟨dip_use_at_two, dip_no_use_at_one⟩ h.2,
    ⟨True.intro, dip_two_dominates_one⟩⟩

end Generative.Naturalism

#print axioms Generative.Naturalism.record_tracks_whole_history
#print axioms Generative.Naturalism.recording_enabled_iff
#print axioms Generative.Naturalism.recording_feasible_iff
#print axioms Generative.Naturalism.guided_recording_keeps_continuation
#print axioms Generative.Naturalism.law_admits_opposite_recordings
