import GenerativeCore

/-! A matched-target obstruction to unique minimal generating mechanisms.
Both recognizers realize exactly all nonempty Unit words, at the minimum of two
states; every state is reachable, coaccessible and right-language distinct.
They differ in branching. This refutes uniqueness from existential successful
word behavior, not an account already required to preserve branching facts. -/
namespace Generative.ExplanatoryMinimalModels
universe u

structure Machine (S : Type u) where
  process : Process S Unit
  initial : S → Prop
  final : S → Prop

def Right {S : Type u} (m : Machine S) (s : S) (w : List Unit) : Prop :=
  ∃ t, Trace m.process s w t ∧ m.final t

def Accepts {S : Type u} (m : Machine S) (w : List Unit) : Prop :=
  ∃ s, m.initial s ∧ Right m s w

def Reachable {S : Type u} (m : Machine S) (s : S) : Prop :=
  ∃ i w, m.initial i ∧ Trace m.process i w s

def Trim {S : Type u} (m : Machine S) : Prop :=
  ∀ s, Reachable m s ∧ ∃ w, Right m s w

def Separated {S : Type u} (m : Machine S) : Prop :=
  ∀ s t, (∀ w, Right m s w ↔ Right m t w) → s = t

def early : Machine Bool where
  process.step _ _ t := t = true
  initial s := s = false
  final s := s = true

def late : Machine Bool where
  process.step s _ _ := s = false
  initial s := s = false
  final s := s = true

theorem right_nil {S : Type u} (m : Machine S) (s : S) : Right m s [] ↔ m.final s := by
  constructor
  · rintro ⟨t, h, hf⟩
    cases h
    exact hf
  · intro h
    exact ⟨s, .nil s, h⟩

theorem accepts_nil {S : Type u} (m : Machine S) :
    Accepts m [] ↔ ∃ s, m.initial s ∧ m.final s := by
  constructor
  · rintro ⟨s, hi, hr⟩
    exact ⟨s, hi, (right_nil m s).mp hr⟩
  · rintro ⟨s, hi, hf⟩
    exact ⟨s, hi, (right_nil m s).mpr hf⟩

theorem early_nonempty_run (s : Bool) (a : Unit) (w : List Unit) :
    Trace early.process s (a :: w) true := by
  induction w generalizing s a with
  | nil => exact .cons rfl (.nil true)
  | cons b w ih => exact .cons rfl (ih true b)

theorem late_wait (w : List Unit) : Trace late.process false w false := by
  induction w with
  | nil => exact .nil false
  | cons a w ih => exact .cons rfl ih

theorem late_nonempty_run (a : Unit) (w : List Unit) :
    Trace late.process false (a :: w) true := by
  induction w generalizing a with
  | nil => exact .cons rfl (.nil true)
  | cons b w ih => exact .cons rfl (ih b)

theorem early_accepts (w : List Unit) : Accepts early w ↔ w ≠ [] := by
  cases w with
  | nil =>
    constructor
    · intro h
      obtain ⟨s, hi, hf⟩ := (accepts_nil early).mp h
      have bad : (false : Bool) = true := hi.symm.trans hf
      cases bad
    · intro h
      exact False.elim (h rfl)
  | cons a w =>
    constructor
    · intro _ h
      cases h
    · intro _
      exact ⟨false, rfl, true, early_nonempty_run false a w, rfl⟩

theorem late_accepts (w : List Unit) : Accepts late w ↔ w ≠ [] := by
  cases w with
  | nil =>
    constructor
    · intro h
      obtain ⟨s, hi, hf⟩ := (accepts_nil late).mp h
      have bad : (false : Bool) = true := hi.symm.trans hf
      cases bad
    · intro h
      exact False.elim (h rfl)
  | cons a w =>
    constructor
    · intro _ h
      cases h
    · intro _
      exact ⟨false, rfl, true, late_nonempty_run a w, rfl⟩

theorem same_complete_language : ∀ w, Accepts early w ↔ Accepts late w :=
  fun w => (early_accepts w).trans (late_accepts w).symm

/-- Any single- or multiple-initial-state recognizer for this language requires
at least two distinct states; this includes infinite carriers and no-state cases. -/
theorem any_realizer_needs_two_states {S : Type u} (m : Machine S)
    (h : ∀ w, Accepts m w ↔ w ≠ []) : ∃ s t : S, s ≠ t := by
  have yes : Accepts m [()] := (h [()]).mpr (by intro e; cases e)
  obtain ⟨s, hi, t, _, hf⟩ := yes
  refine ⟨s, t, ?_⟩
  intro eq
  subst t
  exact ((h []).mp ((accepts_nil m).mpr ⟨s, hi, hf⟩)) rfl

/-- Injection of the two-state carrier into every matching recognizer expresses
state-cardinality minimality without choosing inverses or a finite cardinal API. -/
theorem two_state_lower_bound {S : Type u} (m : Machine S)
    (h : ∀ w, Accepts m w ↔ w ≠ []) :
    ∃ f : Bool → S, ∀ a b, f a = f b → a = b := by
  obtain ⟨s, t, hne⟩ := any_realizer_needs_two_states m h
  refine ⟨fun b => if b then t else s, ?_⟩
  intro a b he
  cases a <;> cases b
  · rfl
  · exact False.elim (hne he)
  · exact False.elim (hne he.symm)
  · rfl

theorem early_trim : Trim early := by
  intro s
  cases s
  · exact ⟨⟨false, [], rfl, .nil false⟩, ⟨[()], true, early_nonempty_run false () [], rfl⟩⟩
  · exact ⟨⟨false, [()], rfl, early_nonempty_run false () []⟩, ⟨[], true, .nil true, rfl⟩⟩

theorem late_trim : Trim late := by
  intro s
  cases s
  · exact ⟨⟨false, [], rfl, .nil false⟩, ⟨[()], true, late_nonempty_run () [], rfl⟩⟩
  · exact ⟨⟨false, [()], rfl, late_nonempty_run () []⟩, ⟨[], true, .nil true, rfl⟩⟩

theorem final_distinguishes_bool_states (m : Machine Bool)
    (hf : ∀ s, m.final s ↔ s = true) : Separated m := by
  intro s t h
  have e : s = true ↔ t = true :=
    (hf s).symm.trans ((right_nil m s).symm.trans ((h []).trans ((right_nil m t).trans (hf t))))
  cases s <;> cases t
  · rfl
  · have bad := e.mpr rfl; cases bad
  · have bad := e.mp rfl; cases bad
  · rfl

theorem early_separated : Separated early := final_distinguishes_bool_states early (fun _ => Iff.rfl)

theorem late_separated : Separated late := final_distinguishes_bool_states late (fun _ => Iff.rfl)

def Deterministic {S : Type u} (m : Machine S) : Prop :=
  ∀ s a t v, m.process.step s a t → m.process.step s a v → t = v

theorem early_deterministic : Deterministic early := fun _ _ _ _ ht hv => ht.trans hv.symm

theorem late_branches : late.process.step false () false ∧ late.process.step false () true :=
  ⟨rfl, rfl⟩

theorem late_not_deterministic : ¬ Deterministic late := by
  intro h
  have bad := h false () false true late_branches.1 late_branches.2
  cases bad

/-- Even a relation-preserving injective renaming from late into early is
impossible, hence a fortiori there is no state isomorphism. -/
theorem no_injective_step_preserving_map :
    ¬ ∃ f : Bool → Bool, (∀ a b, f a = f b → a = b) ∧
      (∀ s a t, late.process.step s a t → early.process.step (f s) a (f t)) := by
  rintro ⟨f, hinj, hstep⟩
  have he := early_deterministic (f false) () (f false) (f true)
    (hstep false () false late_branches.1) (hstep false () true late_branches.2)
  have bad := hinj false true he
  cases bad

/-- All possible words with no terminal success question agree as well. -/
theorem same_possible_words (w : List Unit) :
    (∃ t, Trace early.process false w t) ∧ (∃ t, Trace late.process false w t) := by
  constructor
  · cases w with
    | nil => exact ⟨false, .nil false⟩
    | cons a w => exact ⟨true, early_nonempty_run false a w⟩
  · exact ⟨false, late_wait w⟩

/-- Strengthening the target to all realized branches immediately separates them. -/
def AllFinish {S : Type u} (m : Machine S) (w : List Unit) : Prop :=
  ∀ s t, m.initial s → Trace m.process s w t → m.final t

theorem early_all_finish_after_one : AllFinish early [()] := by
  intro s t _ h
  exact trace_singleton_iff.mp h

theorem late_not_all_finish_after_one : ¬ AllFinish late [()] := by
  intro h
  have bad : (false : Bool) = true := h false false rfl (late_wait [()])
  cases bad

/-- The successful endpoint also has different actual continuation potential. -/
theorem successful_continuation_differs :
    Enabled early.process true () ∧ ¬ Enabled late.process true () := by
  constructor
  · exact ⟨true, rfl⟩
  · rintro ⟨t, h⟩
    cases h

/-- Strong failure certificate: trim, separated, minimal, equal complete
existential languages, yet not even an injective step-preserving map. -/
theorem minimal_mechanism_uniqueness_fails :
    Trim early ∧ Trim late ∧ Separated early ∧ Separated late ∧
    (∀ w, Accepts early w ↔ Accepts late w) ∧
    (∀ (S : Type) (m : Machine S), (∀ w, Accepts m w ↔ w ≠ []) →
      ∃ f : Bool → S, ∀ a b, f a = f b → a = b) ∧
    ¬ ∃ f : Bool → Bool, (∀ a b, f a = f b → a = b) ∧
      (∀ s a t, late.process.step s a t → early.process.step (f s) a (f t)) :=
  ⟨early_trim, late_trim, early_separated, late_separated, same_complete_language,
   fun _ m h => two_state_lower_bound m h, no_injective_step_preserving_map⟩

/-- Two distinct edges are also necessary, so the example does not merely
trade state count against a larger transition table. -/
theorem any_realizer_needs_two_edges {S : Type u} (m : Machine S)
    (h : ∀ w, Accepts m w ↔ w ≠ []) :
    ∃ s middle t, m.process.step s () middle ∧ m.process.step middle () t ∧
      (s, middle) ≠ (middle, t) := by
  obtain ⟨s, hi, t, ht, hf⟩ := (h [(), ()]).mpr (by intro e; cases e)
  obtain ⟨middle, first, tail⟩ := trace_cons_iff.mp ht
  have second := trace_singleton_iff.mp tail
  refine ⟨s, middle, t, first, second, ?_⟩
  intro eq
  have st : s = t := (congrArg Prod.fst eq).trans (congrArg Prod.snd eq)
  subst t
  exact ((h []).mp ((accepts_nil m).mpr ⟨s, hi, hf⟩)) rfl

theorem early_edges_exact (s t : Bool) : early.process.step s () t ↔
    (s, t) = (false, true) ∨ (s, t) = (true, true) := by
  cases s <;> cases t <;> decide

theorem late_edges_exact (s t : Bool) : late.process.step s () t ↔
    (s, t) = (false, false) ∨ (s, t) = (false, true) := by
  cases s <;> cases t <;> decide

/-- Reachable collections, rather than individual nondeterministic states,
carry a complete continuation prediction after a common word. -/
def Collective {S : Type u} (m : Machine S) (past future : List Unit) : Prop :=
  ∃ s, ReachableAfter m past s ∧ Right m s future
where ReachableAfter (m : Machine S) (past : List Unit) (s : S) : Prop :=
  ∃ i, m.initial i ∧ Trace m.process i past s

theorem collective_iff_appended {S : Type u} (m : Machine S) (past future : List Unit) :
    Collective m past future ↔ Accepts m (past ++ future) := by
  constructor
  · rintro ⟨s, ⟨i, hi, hs⟩, t, ht, hf⟩
    exact ⟨i, hi, t, trace_append_iff.mpr ⟨s, hs, ht⟩, hf⟩
  · rintro ⟨i, hi, t, ht, hf⟩
    obtain ⟨s, hs, tail⟩ := trace_append_iff.mp ht
    exact ⟨s, ⟨i, hi, hs⟩, t, tail, hf⟩

theorem same_collective_predictions (past future : List Unit) :
    Collective early past future ↔ Collective late past future :=
  (collective_iff_appended early past future).trans
    ((same_complete_language (past ++ future)).trans (collective_iff_appended late past future).symm)

/-- Even though the collections predict identically, an individual early
successful state has no continuation-equivalent individual late state. -/
theorem no_late_state_matches_early_success (s : Bool) :
    ¬ (∀ w, Right early true w ↔ Right late s w) := by
  intro h
  cases s
  · have bad := (right_nil late false).mp ((h []).mp ⟨true, .nil true, rfl⟩)
    cases bad
  · obtain ⟨t, ht, _⟩ := (h [()]).mp ⟨true, early_nonempty_run true () [], rfl⟩
    have bad : (true : Bool) = false := trace_singleton_iff.mp ht
    cases bad

/-- Determinism cannot be inferred by any rule invariant under the complete
successful-word answers. Actual branches, not a freely toggled predicate,
provide the separating witness. -/
theorem determinism_not_language_invariant :
    ¬ (∀ m n : Machine Bool, (∀ w, Accepts m w ↔ Accepts n w) →
      (Deterministic m ↔ Deterministic n)) := by
  intro h
  exact late_not_deterministic ((h early late same_complete_language).mp early_deterministic)

end Generative.ExplanatoryMinimalModels

#print axioms Generative.ExplanatoryMinimalModels.right_nil
#print axioms Generative.ExplanatoryMinimalModels.accepts_nil
#print axioms Generative.ExplanatoryMinimalModels.early_nonempty_run
#print axioms Generative.ExplanatoryMinimalModels.late_wait
#print axioms Generative.ExplanatoryMinimalModels.late_nonempty_run
#print axioms Generative.ExplanatoryMinimalModels.early_accepts
#print axioms Generative.ExplanatoryMinimalModels.late_accepts
#print axioms Generative.ExplanatoryMinimalModels.same_complete_language
#print axioms Generative.ExplanatoryMinimalModels.any_realizer_needs_two_states
#print axioms Generative.ExplanatoryMinimalModels.two_state_lower_bound
#print axioms Generative.ExplanatoryMinimalModels.early_trim
#print axioms Generative.ExplanatoryMinimalModels.late_trim
#print axioms Generative.ExplanatoryMinimalModels.final_distinguishes_bool_states
#print axioms Generative.ExplanatoryMinimalModels.early_separated
#print axioms Generative.ExplanatoryMinimalModels.late_separated
#print axioms Generative.ExplanatoryMinimalModels.early_deterministic
#print axioms Generative.ExplanatoryMinimalModels.late_branches
#print axioms Generative.ExplanatoryMinimalModels.late_not_deterministic
#print axioms Generative.ExplanatoryMinimalModels.no_injective_step_preserving_map
#print axioms Generative.ExplanatoryMinimalModels.same_possible_words
#print axioms Generative.ExplanatoryMinimalModels.early_all_finish_after_one
#print axioms Generative.ExplanatoryMinimalModels.late_not_all_finish_after_one
#print axioms Generative.ExplanatoryMinimalModels.successful_continuation_differs
#print axioms Generative.ExplanatoryMinimalModels.minimal_mechanism_uniqueness_fails
#print axioms Generative.ExplanatoryMinimalModels.any_realizer_needs_two_edges
#print axioms Generative.ExplanatoryMinimalModels.early_edges_exact
#print axioms Generative.ExplanatoryMinimalModels.late_edges_exact
#print axioms Generative.ExplanatoryMinimalModels.collective_iff_appended
#print axioms Generative.ExplanatoryMinimalModels.same_collective_predictions
#print axioms Generative.ExplanatoryMinimalModels.no_late_state_matches_early_success
#print axioms Generative.ExplanatoryMinimalModels.determinism_not_language_invariant
