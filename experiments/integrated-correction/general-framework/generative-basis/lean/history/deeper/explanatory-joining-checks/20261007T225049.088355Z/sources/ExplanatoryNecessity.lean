import HistoryRealization

/-!
Content recoverability is separated from explanatory or ontological priority.
Adequate below means exact answers to specified finite endpoint queries only.
It does not define philosophical explanation or a physically implemented decoder.
-/
namespace Generative.ExplanatoryNecessity

universe u v w
variable {S : Type u} {A : Type v} {E : Type w}

abbrev Answers (S : Type u) (A : Type v) := S → List A → S → Prop

def Adequate (P : Process S A) (decode : E → Answers S A) (e : E) : Prop :=
  ∀ s word t, decode e s word t ↔ Trace P s word t

theorem decode_singleton_recovers_step {P : Process S A}
    {decode : E → Answers S A} {e : E} (h : Adequate P decode e)
    (s : S) (a : A) (t : S) : decode e s [a] t ↔ P.step s a t :=
  (h s [a] t).trans trace_singleton_iff

theorem same_description_preserves_steps {P Q : Process S A}
    {decode : E → Answers S A} {e f : E}
    (hp : Adequate P decode e) (hq : Adequate Q decode f) (he : e = f)
    (s : S) (a : A) (t : S) : P.step s a t ↔ Q.step s a t := by
  subst f
  exact (decode_singleton_recovers_step hp s a t).symm.trans
    (decode_singleton_recovers_step hq s a t)

theorem different_steps_require_different_descriptions {P Q : Process S A}
    {decode : E → Answers S A} {e f : E}
    (hp : Adequate P decode e) (hq : Adequate Q decode f)
    {s t : S} {a : A} (hs : P.step s a t) (hn : ¬ Q.step s a t) : e ≠ f := by
  intro he
  exact hn ((same_description_preserves_steps hp hq he s a t).mp hs)

theorem step_equivalence_iff_trace_equivalence (P Q : Process S A) :
    (∀ s a t, P.step s a t ↔ Q.step s a t) ↔
      (∀ s word t, Trace P s word t ↔ Trace Q s word t) := by
  constructor
  · intro h s word t
    constructor
    · exact trace_map (f := fun x => x) (fun x a y hx => (h x a y).mp hx)
    · exact trace_map (f := fun x => x) (fun x a y hx => (h x a y).mpr hx)
  · intro h s a t
    exact trace_singleton_iff.symm.trans ((h s [a] t).trans trace_singleton_iff)

theorem static_profile_adequate (P : Process S A) :
    Adequate P (fun (profile : Answers S A) => profile) (Trace P) := by
  intro s word t
  exact Iff.rfl

theorem adequate_answers_agree {P : Process S A}
    {D : Type w} {decode : E → Answers S A} {other : D → Answers S A}
    {e : E} {d : D} (he : Adequate P decode e) (hd : Adequate P other d)
    (s : S) (word : List A) (t : S) : decode e s word t ↔ other d s word t :=
  (he s word t).trans (hd s word t).symm

def singletonProcess (H : Answers S A) : Process S A where
  step s a t := H s [a] t

/-- Exact local reconstruction requires empty-path identity and decomposition
through a common intermediate configuration; these are substantive conditions. -/
def LocallyDecomposable (H : Answers S A) : Prop :=
  (∀ s t, H s [] t ↔ s = t) ∧
  (∀ s a word t, H s (a :: word) t ↔ ∃ m, H s [a] m ∧ H m word t)

theorem local_decomposition_iff_trace_representation (H : Answers S A) :
    LocallyDecomposable H ↔
      (∀ s word t, H s word t ↔ Trace (singletonProcess H) s word t) := by
  constructor
  · rintro ⟨hnil, hcons⟩ s word t
    induction word generalizing s with
    | nil => exact (hnil s t).trans trace_nil_iff.symm
    | cons a word ih =>
      constructor
      · intro h
        obtain ⟨m, hm, ht⟩ := (hcons s a word t).mp h
        exact .cons hm ((ih m).mp ht)
      · intro h
        obtain ⟨m, hm, ht⟩ := trace_cons_iff.mp h
        exact (hcons s a word t).mpr ⟨m, hm, (ih m).mpr ht⟩
  · intro h
    constructor
    · intro s t
      exact (h s [] t).trans trace_nil_iff
    · intro s a word t
      constructor
      · intro hs
        obtain ⟨m, hm, ht⟩ := trace_cons_iff.mp ((h s (a :: word) t).mp hs)
        exact ⟨m, hm, (h m word t).mpr ht⟩
      · rintro ⟨m, hm, ht⟩
        exact (h s (a :: word) t).mpr (.cons hm ((h m word t).mp ht))

def idle : Process Bool Unit where
  step s _ t := t = s

def flip : Process Bool Unit where
  step s _ t := t = !s

theorem idle_feasible (s : Bool) (word : List Unit) : Feasible idle s word := by
  induction word generalizing s with
  | nil => exact ⟨s, .nil s⟩
  | cons a word ih =>
    obtain ⟨t, ht⟩ := ih s
    exact ⟨t, .cons rfl ht⟩

theorem flip_feasible (s : Bool) (word : List Unit) : Feasible flip s word := by
  induction word generalizing s with
  | nil => exact ⟨s, .nil s⟩
  | cons a word ih =>
    obtain ⟨t, ht⟩ := ih (!s)
    exact ⟨t, .cons rfl ht⟩

theorem feasibility_profiles_agree (s : Bool) (word : List Unit) :
    Feasible idle s word ↔ Feasible flip s word :=
  ⟨fun _ => flip_feasible s word, fun _ => idle_feasible s word⟩

theorem endpoint_profiles_differ :
    Trace flip false [()] true ∧ ¬ Trace idle false [()] true := by
  constructor
  · exact .cons rfl (.nil true)
  · intro h
    have bad : true = false := trace_singleton_iff.mp h
    cases bad

/-- A whole-history budget on a deliberately coarse one-point carrier. -/
def bounded (word : List Unit) : Prop := word = [] ∨ ∃ a, word = [a]

theorem bounded_empty : bounded [] := Or.inl rfl

theorem bounded_singleton (a : Unit) : bounded [a] := Or.inr ⟨a, rfl⟩

theorem bounded_rejects_double : ¬ bounded [(), ()] := by
  intro h
  rcases h with h | ⟨a, h⟩ <;> cases h

theorem bounded_prefix_closed : Deeper.PrefixClosed bounded := by
  intro pre suffix h
  cases pre with
  | nil => exact bounded_empty
  | cons a rest =>
    cases rest with
    | nil => exact bounded_singleton a
    | cons b tail =>
      rcases h with h | ⟨c, h⟩ <;> cases h

theorem bounded_no_one_point_realization :
    ¬ ∃ P : Process Unit Unit, ∀ word, Feasible P () word ↔ bounded word := by
  rintro ⟨P, h⟩
  obtain ⟨t, ht⟩ := (h [()]).mpr (bounded_singleton ())
  cases t
  have hs : P.step () () () := trace_singleton_iff.mp ht
  have twice : Feasible P () [(), ()] := ⟨(), .cons hs (.cons hs (.nil ()))⟩
  exact bounded_rejects_double ((h [(), ()]).mp twice)

theorem bounded_history_realization (word : List Unit) :
    Feasible (Deeper.historyProcess bounded) [] word ↔ bounded word :=
  Deeper.history_feasible_iff bounded_prefix_closed bounded_empty word

end Generative.ExplanatoryNecessity

#print axioms Generative.ExplanatoryNecessity.decode_singleton_recovers_step
#print axioms Generative.ExplanatoryNecessity.same_description_preserves_steps
#print axioms Generative.ExplanatoryNecessity.different_steps_require_different_descriptions
#print axioms Generative.ExplanatoryNecessity.step_equivalence_iff_trace_equivalence
#print axioms Generative.ExplanatoryNecessity.static_profile_adequate
#print axioms Generative.ExplanatoryNecessity.adequate_answers_agree
#print axioms Generative.ExplanatoryNecessity.local_decomposition_iff_trace_representation
#print axioms Generative.ExplanatoryNecessity.idle_feasible
#print axioms Generative.ExplanatoryNecessity.flip_feasible
#print axioms Generative.ExplanatoryNecessity.feasibility_profiles_agree
#print axioms Generative.ExplanatoryNecessity.endpoint_profiles_differ
#print axioms Generative.ExplanatoryNecessity.bounded_empty
#print axioms Generative.ExplanatoryNecessity.bounded_singleton
#print axioms Generative.ExplanatoryNecessity.bounded_rejects_double
#print axioms Generative.ExplanatoryNecessity.bounded_prefix_closed
#print axioms Generative.ExplanatoryNecessity.bounded_no_one_point_realization
#print axioms Generative.ExplanatoryNecessity.bounded_history_realization
