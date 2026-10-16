import FormationProfileGap

/-!
# Conditions defined by returning within the same unfolding

A return is a path whose endpoint is its starting configuration. This uses
the given equality of configurations, not a supplied coordinate readout.
Return questions distinguish all four states of the unchanged native process.
They are preserved by the stated faithful encodings, but are not definable
in the native atom-free modal interface. Neither structural definability nor
an empty axiom report establishes an implemented comparison or a foundation
without assumptions.
-/

namespace Generative.ReturnConditions
open SystemIndividuation FormationProfileGap

universe u v w

def Returns {S : Type u} {A : Type v} (P : Process S A)
    (s : S) (word : List A) : Prop := Trace P s word s

theorem returns_singleton_iff {S : Type u} {A : Type v}
    (P : Process S A) (s : S) (a : A) :
    Returns P s [a] ↔ P.step s a s := trace_singleton_iff

/-- Two transition-preserving maps with a left inverse suffice on encoded
states. Bijective recodings are included; no surjectivity is silently used. -/
theorem returns_transport {S : Type u} {T : Type w} {A : Type v}
    (P : Process S A) (Q : Process T A) (encode : S → T) (decode : T → S)
    (back : ∀ s, decode (encode s) = s)
    (forward : ∀ s a t, P.step s a t → Q.step (encode s) a (encode t))
    (reverse : ∀ s a t, Q.step s a t → P.step (decode s) a (decode t))
    (s : S) (word : List A) :
    Returns P s word ↔ Returns Q (encode s) word := by
  constructor
  · exact trace_map forward
  · intro h
    have restored := trace_map reverse h
    simpa only [back] using restored

theorem correlate_return_iff_diagonal (s : Bool × Bool) :
    Returns process s [.correlate] ↔ diagonal s := by
  constructor
  · intro h
    have step : s = (s.1, s.1) := trace_singleton_iff.mp h
    exact (congrArg Prod.snd step).symm
  · intro h
    apply trace_singleton_iff.mpr
    exact Prod.ext rfl h.symm

theorem pulse_return_iff_left (s : Bool × Bool) :
    Returns process s [.pulse] ↔ s.1 = true := by
  exact ⟨fun h => (trace_singleton_iff.mp h).1,
    fun h => trace_singleton_iff.mpr ⟨h, rfl⟩⟩

/-- Explicit separation, stronger than merely noting renaming invariance. -/
theorem two_returns_identify (s t : Bool × Bool)
    (pulse : Returns process s [.pulse] ↔ Returns process t [.pulse])
    (formed : Returns process s [.correlate] ↔ Returns process t [.correlate]) : s = t := by
  have pulse' := (pulse_return_iff_left s).symm.trans
    (pulse.trans (pulse_return_iff_left t))
  have formed' := (correlate_return_iff_diagonal s).symm.trans
    (formed.trans (correlate_return_iff_diagonal t))
  clear pulse formed
  cases s with
  | mk a b =>
    cases t with
    | mk c d =>
      cases a <;> cases b <;> cases c <;> cases d <;>
        simp_all [diagonal]

theorem same_returns_iff_same_state (s t : Bool × Bool) :
    (∀ word, Returns process s word ↔ Returns process t word) ↔ s = t := by
  constructor
  · intro h
    exact two_returns_identify s t (h [.pulse]) (h [.correlate])
  · intro h
    cases h
    exact fun _ => Iff.rfl

/-- This fixes the event labels and makes no claim of a unique physical
factorization or unique explanatory vocabulary. -/
theorem labelled_symmetry_fixes_states (encode decode : (Bool × Bool) → Bool × Bool)
    (back : ∀ s, decode (encode s) = s)
    (forward : ∀ s a t, process.step s a t → process.step (encode s) a (encode t))
    (reverse : ∀ s a t, process.step s a t → process.step (decode s) a (decode t))
    (s : Bool × Bool) : encode s = s := by
  apply (same_returns_iff_same_state (encode s) s).mp
  intro word
  exact (returns_transport process process encode decode back forward reverse s word).symm

theorem right_reading_from_returns (s : Bool × Bool) :
    s.2 = true ↔
      (Returns process s [.pulse] ∧ Returns process s [.correlate]) ∨
      (¬ Returns process s [.pulse] ∧ ¬ Returns process s [.correlate]) := by
  have raw : s.2 = true ↔ (s.1 = true ∧ diagonal s) ∨
      (¬ s.1 = true ∧ ¬ diagonal s) := by
    unfold diagonal
    cases s with
    | mk a b => cases a <;> cases b <;> decide
  have p := (pulse_return_iff_left s).symm
  have c := (correlate_return_iff_diagonal s).symm
  exact raw.trans (or_congr (and_congr p c) (and_congr (not_congr p) (not_congr c)))

theorem formation_changes_returns :
    ¬ Returns process (false, true) [.correlate] ∧
    process.step (false, true) .correlate (false, false) ∧
    Returns process (false, false) [.correlate] := by
  refine ⟨?_, rfl, (correlate_return_iff_diagonal _).mpr rfl⟩
  intro h
  exact Bool.noConfusion ((correlate_return_iff_diagonal _).mp h)

theorem formed_return_persists {s t : Bool × Bool} {word : List Event}
    (formed : Returns process s [.correlate]) (trace : Trace process s word t) :
    Returns process t [.correlate] :=
  (correlate_return_iff_diagonal t).mpr
    (diagonal_preserved_by_trace ((correlate_return_iff_diagonal s).mp formed) trace)

theorem feasible_words_do_not_determine_returns :
    ¬ (∀ s t : Bool × Bool,
      (∀ word, Feasible process s word ↔ Feasible process t word) →
      ∀ word, Returns process s word ↔ Returns process t word) := by
  intro h
  have same := h (false, true) (false, false)
    (same_left_same_feasible _ _ rfl) [.correlate]
  exact formation_changes_returns.1 (same.mpr formation_changes_returns.2.2)

/-- Query syntax with no supplied state predicates, names or equality tests.
It is a semantic query language, not an assertion of executable sensors. -/
inductive ActionQuery (A : Type v) where
  | truth
  | neg (p : ActionQuery A)
  | conj (p q : ActionQuery A)
  | possible (a : A) (p : ActionQuery A)

def Holds {S : Type u} {A : Type v} (P : Process S A) :
    ActionQuery A → S → Prop
  | .truth, _ => True
  | .neg p, s => ¬ Holds P p s
  | .conj p q, s => Holds P p s ∧ Holds P q s
  | .possible a p, s => ∃ t, P.step s a t ∧ Holds P p t

theorem same_left_same_queries (p : ActionQuery Event) (s t : Bool × Bool)
    (same : s.1 = t.1) : Holds process p s ↔ Holds process p t := by
  induction p generalizing s t with
  | truth => exact Iff.rfl
  | neg p ih => exact not_congr (ih s t same)
  | conj p q ihp ihq => exact and_congr (ihp s t same) (ihq s t same)
  | possible a p ih =>
    constructor
    · rintro ⟨next, step, answer⟩
      obtain ⟨other, lifted, retained⟩ := step_lift_same_left same step
      exact ⟨other, lifted, (ih next other retained).mp answer⟩
    · rintro ⟨next, step, answer⟩
      obtain ⟨other, lifted, retained⟩ := step_lift_same_left same.symm step
      exact ⟨other, lifted, (ih other next retained.symm).mpr answer⟩

theorem formed_return_not_query_definable :
    ¬ ∃ p : ActionQuery Event, ∀ s,
      Holds process p s ↔ Returns process s [.correlate] := by
  rintro ⟨p, exactAnswer⟩
  have atFormed := (exactAnswer (false, false)).mpr formation_changes_returns.2.2
  have atUnformed := (same_left_same_queries p (false, true) (false, false) rfl).mpr atFormed
  exact formation_changes_returns.1 ((exactAnswer (false, true)).mp atUnformed)

/-- Branching and negation do not repair the identity omission in this
specified interface, even when every query is retained. -/
theorem all_queries_do_not_determine_returns :
    ¬ (∀ s t : Bool × Bool,
      (∀ p : ActionQuery Event, Holds process p s ↔ Holds process p t) →
      ∀ word, Returns process s word ↔ Returns process t word) := by
  intro h
  have same := h (false, true) (false, false)
    (fun p => same_left_same_queries p _ _ rfl) [.correlate]
  exact formation_changes_returns.1 (same.mpr formation_changes_returns.2.2)

/-- A control against treating the native separation result as universal. -/
def holding : Process Bool Unit where
  step s _ t := t = s

theorem holding_returns (s : Bool) (word : List Unit) : Returns holding s word := by
  induction word with
  | nil => exact .nil _
  | cons a word ih => exact .cons rfl ih

theorem returns_not_universally_separating :
    false ≠ true ∧ ∀ word, Returns holding false word ↔ Returns holding true word := by
  exact ⟨Bool.noConfusion, fun word => ⟨fun _ => holding_returns true word,
    fun _ => holding_returns false word⟩⟩

end Generative.ReturnConditions

#print axioms Generative.ReturnConditions.Returns
#print axioms Generative.ReturnConditions.ActionQuery
#print axioms Generative.ReturnConditions.Holds
#print axioms Generative.ReturnConditions.holding
#print axioms Generative.ReturnConditions.returns_singleton_iff
#print axioms Generative.ReturnConditions.returns_transport
#print axioms Generative.ReturnConditions.correlate_return_iff_diagonal
#print axioms Generative.ReturnConditions.pulse_return_iff_left
#print axioms Generative.ReturnConditions.two_returns_identify
#print axioms Generative.ReturnConditions.same_returns_iff_same_state
#print axioms Generative.ReturnConditions.labelled_symmetry_fixes_states
#print axioms Generative.ReturnConditions.right_reading_from_returns
#print axioms Generative.ReturnConditions.formation_changes_returns
#print axioms Generative.ReturnConditions.formed_return_persists
#print axioms Generative.ReturnConditions.feasible_words_do_not_determine_returns
#print axioms Generative.ReturnConditions.same_left_same_queries
#print axioms Generative.ReturnConditions.formed_return_not_query_definable
#print axioms Generative.ReturnConditions.all_queries_do_not_determine_returns
#print axioms Generative.ReturnConditions.holding_returns
#print axioms Generative.ReturnConditions.returns_not_universally_separating
