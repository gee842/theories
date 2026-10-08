import ExplanatoryUniversality

/-! A repair, explicitly conditional on deterministic total realization,
reachability and separation by all finite marked continuations. The state spaces
and alphabet need not be finite. This is a checked familiar automata uniqueness
route, not a derivation of determinism or universal explanatory priority. -/
namespace Generative.ExplanatoryDeterminism
open ExplanatoryUniqueness
universe u v w

structure System (S : Type u) (A : Type v) where
  initial : S
  next : S → A → S
  marked : S → Prop

def run {S : Type u} {A : Type v} (d : System S A) (s : S) : List A → S
  | [] => s
  | a :: w => run d (d.next s a) w

def predicts {S : Type u} {A : Type v} (d : System S A) (s : S) (w : List A) : Prop :=
  d.marked (run d s w)

def language {S : Type u} {A : Type v} (d : System S A) (w : List A) : Prop :=
  predicts d d.initial w

def process {S : Type u} {A : Type v} (d : System S A) : Process S A where
  step s a t := d.next s a = t

def Reachable {S : Type u} {A : Type v} (d : System S A) : Prop :=
  ∀ s, ∃ w, run d d.initial w = s

def Separated {S : Type u} {A : Type v} (d : System S A) : Prop :=
  ∀ s t, (∀ w, predicts d s w ↔ predicts d t w) → s = t

def target {A : Type v} (L : List A → Prop) (w suffix : List A) : Prop := L (w ++ suffix)

def presentation {S : Type u} {A : Type v} (d : System S A) : Presentation (List A) (List A) S where
  encode := run d d.initial
  read := predicts d

variable {S : Type u} {T : Type w} {A : Type v}

theorem run_append (d : System S A) (s : S) (w suffix : List A) :
    run d s (w ++ suffix) = run d (run d s w) suffix := by
  induction w generalizing s with
  | nil => rfl
  | cons a w ih => exact ih (d.next s a)

theorem trace_iff_run (d : System S A) (s t : S) (w : List A) :
    Trace (process d) s w t ↔ run d s w = t := by
  induction w generalizing s with
  | nil => exact trace_nil_iff
  | cons a w ih =>
    constructor
    · intro h
      obtain ⟨m, hm, ht⟩ := trace_cons_iff.mp h
      change d.next s a = m at hm
      exact (congrArg (fun z => run d z w) hm).trans ((ih m).mp ht)
    · intro h
      exact .cons rfl ((ih (d.next s a)).mpr h)

theorem presentation_exact (d : System S A) : Exact (target (language d)) (presentation d) := by
  intro w suffix
  change d.marked (run d (run d d.initial w) suffix) ↔ d.marked (run d d.initial (w ++ suffix))
  rw [run_append]

theorem presentation_exact_common (d : System S A) (L : List A → Prop)
    (h : ∀ w, language d w ↔ L w) : Exact (target L) (presentation d) :=
  fun w suffix => (presentation_exact d w suffix).trans (h (w ++ suffix))

theorem presentation_reduced (d : System S A) (L : List A → Prop)
    (h : ∀ w, language d w ↔ L w) (sep : Separated d) :
    Reduced (target L) (presentation d) := by
  intro x y he
  apply sep
  intro suffix
  exact (presentation_exact_common d L h x suffix).trans
    ((he suffix).trans (presentation_exact_common d L h y suffix).symm)

theorem every_state_used (d : System S A) (reach : Reachable d) (s : S) :
    Used (presentation d) s := reach s

theorem matched_initials (d : System S A) (e : System T A) :
    Matches (presentation d) (presentation e) d.initial e.initial := ⟨[], rfl, rfl⟩

theorem matched_next (d : System S A) (e : System T A) {s : S} {t : T}
    (h : Matches (presentation d) (presentation e) s t) (a : A) :
    Matches (presentation d) (presentation e) (d.next s a) (e.next t a) := by
  obtain ⟨w, hs, ht⟩ := h
  refine ⟨w ++ [a], ?_, ?_⟩
  · change run d d.initial (w ++ [a]) = d.next s a
    rw [run_append]
    exact congrArg (fun z => d.next z a) hs
  · change run e e.initial (w ++ [a]) = e.next t a
    rw [run_append]
    exact congrArg (fun z => e.next z a) ht

theorem matched_marks (d : System S A) (e : System T A)
    (h : ∀ w, language d w ↔ language e w) {s : S} {t : T}
    (hm : Matches (presentation d) (presentation e) s t) : d.marked s ↔ e.marked t := by
  obtain ⟨w, hs, ht⟩ := hm
  have hw := h w
  change d.marked ((presentation d).encode w) ↔ e.marked ((presentation e).encode w) at hw
  rw [hs, ht] at hw
  exact hw

theorem matched_functional (d : System S A) (e : System T A)
    (h : ∀ w, language d w ↔ language e w) (sep : Separated e)
    {s : S} {t t' : T} (ht : Matches (presentation d) (presentation e) s t)
    (ht' : Matches (presentation d) (presentation e) s t') : t = t' :=
  matches_functional (presentation_exact_common d (language e) h)
    (presentation_reduced e (language e) (fun _ => Iff.rfl) sep) ht ht'

theorem matched_inverse_functional (d : System S A) (e : System T A)
    (h : ∀ w, language d w ↔ language e w) (sep : Separated d)
    {s s' : S} {t : T} (hs : Matches (presentation d) (presentation e) s t)
    (hs' : Matches (presentation d) (presentation e) s' t) : s = s' :=
  matches_inverse_functional (presentation_exact e)
    (presentation_reduced d (language e) h sep) hs hs'

/-- Relational isomorphism, avoiding an arbitrary choice of inverse function. -/
theorem reachable_separated_unique (d : System S A) (e : System T A)
    (h : ∀ w, language d w ↔ language e w)
    (rd : Reachable d) (re : Reachable e) (sd : Separated d) (se : Separated e) :
    (∀ s, ∃ t, Matches (presentation d) (presentation e) s t ∧
      ∀ t', Matches (presentation d) (presentation e) s t' → t' = t) ∧
    (∀ t, ∃ s, Matches (presentation d) (presentation e) s t ∧
      ∀ s', Matches (presentation d) (presentation e) s' t → s' = s) := by
  have result := relative_unique_correspondence
    (presentation_exact_common d (language e) h) (presentation_reduced d (language e) h sd)
    (presentation_exact e) (presentation_reduced e (language e) (fun _ => Iff.rfl) se)
  exact ⟨fun s => result.1 s (every_state_used d rd s),
    fun t => result.2 t (every_state_used e re t)⟩

theorem matching_preserves_and_reflects_steps (d : System S A) (e : System T A)
    (h : ∀ w, language d w ↔ language e w) (sd : Separated d) (se : Separated e)
    {s s' : S} {t t' : T} (hs : Matches (presentation d) (presentation e) s t)
    (ht : Matches (presentation d) (presentation e) s' t') (a : A) :
    (process d).step s a s' ↔ (process e).step t a t' := by
  have hn := matched_next d e hs a
  constructor
  · intro step
    change d.next s a = s' at step
    rw [step] at hn
    exact matched_functional d e h se hn ht
  · intro step
    change e.next t a = t' at step
    rw [step] at hn
    exact matched_inverse_functional d e h sd hn ht

/-- The correspondence is fixed by common executed words, not merely unique
among arbitrary automorphisms of an unrooted structure. -/
theorem unique_word_aligned_matching (d : System S A) (e : System T A)
    (rd : Reachable d) (R : S → T → Prop)
    (aligned : ∀ w, R (run d d.initial w) (run e e.initial w))
    (functional : ∀ s t t', R s t → R s t' → t = t') (s : S) (t : T) :
    R s t ↔ Matches (presentation d) (presentation e) s t :=
  unique_matching (presentation d) (presentation e) R aligned functional (every_state_used d rd s)

end Generative.ExplanatoryDeterminism

#print axioms Generative.ExplanatoryDeterminism.run_append
#print axioms Generative.ExplanatoryDeterminism.trace_iff_run
#print axioms Generative.ExplanatoryDeterminism.presentation_exact
#print axioms Generative.ExplanatoryDeterminism.presentation_exact_common
#print axioms Generative.ExplanatoryDeterminism.presentation_reduced
#print axioms Generative.ExplanatoryDeterminism.every_state_used
#print axioms Generative.ExplanatoryDeterminism.matched_initials
#print axioms Generative.ExplanatoryDeterminism.matched_next
#print axioms Generative.ExplanatoryDeterminism.matched_marks
#print axioms Generative.ExplanatoryDeterminism.matched_functional
#print axioms Generative.ExplanatoryDeterminism.matched_inverse_functional
#print axioms Generative.ExplanatoryDeterminism.reachable_separated_unique
#print axioms Generative.ExplanatoryDeterminism.matching_preserves_and_reflects_steps
#print axioms Generative.ExplanatoryDeterminism.unique_word_aligned_matching
