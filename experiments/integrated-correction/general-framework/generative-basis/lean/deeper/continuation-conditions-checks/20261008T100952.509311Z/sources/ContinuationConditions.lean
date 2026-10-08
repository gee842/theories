import HistoryRealization

/-!
Finite continuation conditions extracted from one supplied history language.
The update rule is derived from concatenation; the language and its actual
interpretation are not derived. Profiles preserve existential word feasibility,
not individual nondeterministic branches, probabilities or causal production.
-/

namespace Generative.ContinuationConditions

open Deeper
universe u v
variable {A : Type v}

def Future (L : List A → Prop) (past suffix : List A) : Prop :=
  L (past ++ suffix)

def SameFuture (L : List A → Prop) (h k : List A) : Prop :=
  ∀ suffix, Future L h suffix ↔ Future L k suffix

def Stable (L : List A → Prop) : Prop :=
  ∀ h, L h → SameFuture L h []

def Letterwise (L : List A → Prop) : List A → Prop
  | [] => True
  | a :: rest => L [a] ∧ Letterwise L rest

/-- A common update identity, with no independently supplied profile updater. -/
theorem future_update (L : List A → Prop) (h extension suffix : List A) :
    Future L (h ++ extension) suffix ↔ Future L h (extension ++ suffix) := by
  change L ((h ++ extension) ++ suffix) ↔ L (h ++ (extension ++ suffix))
  rw [append_assoc_constructive]

theorem same_future_extends (L : List A → Prop) {h k : List A}
    (same : SameFuture L h k) (extension : List A) :
    SameFuture L (h ++ extension) (k ++ extension) := by
  intro suffix
  exact (future_update L h extension suffix).trans
    ((same (extension ++ suffix)).trans (future_update L k extension suffix).symm)

/-- In a nondeterministic process this is a union over reachable endpoints. -/
theorem future_is_reachable_union {S : Type u} (P : Process S A)
    (s : S) (past suffix : List A) :
    Future (Feasible P s) past suffix ↔
      ∃ middle, Trace P s past middle ∧ Feasible P middle suffix :=
  feasible_append_iff

theorem letterwise_append (L : List A → Prop) (h k : List A) :
    Letterwise L (h ++ k) ↔ Letterwise L h ∧ Letterwise L k := by
  induction h with
  | nil =>
    constructor
    · intro hk; exact ⟨True.intro, hk⟩
    · intro hk; exact hk.2
  | cons a h ih =>
    constructor
    · intro hk
      have rest := ih.mp hk.2
      exact ⟨⟨hk.1, rest.1⟩, rest.2⟩
    · intro hk
      exact ⟨hk.1.1, ih.mpr ⟨hk.1.2, hk.2⟩⟩

/-- Stable profiles exclude every constraint beyond initially admitted letters. -/
theorem stable_implies_letterwise (L : List A → Prop)
    (closed : PrefixClosed L) (empty : L []) (stable : Stable L)
    (word : List A) : L word ↔ Letterwise L word := by
  induction word with
  | nil =>
    constructor
    · intro _; exact True.intro
    · intro _; exact empty
  | cons a word ih =>
    constructor
    · intro hw
      have ha : L [a] := closed [a] word hw
      have tail : L word := (stable [a] ha word).mp hw
      exact ⟨ha, ih.mp tail⟩
    · intro hw
      exact (stable [a] hw.1 word).mpr (ih.mpr hw.2)

theorem letterwise_implies_stable (L : List A → Prop)
    (exactLetters : ∀ word, L word ↔ Letterwise L word) : Stable L := by
  intro h hh suffix
  change L (h ++ suffix) ↔ L suffix
  constructor
  · intro hs
    exact (exactLetters suffix).mpr
      ((letterwise_append L h suffix).mp ((exactLetters (h ++ suffix)).mp hs)).2
  · intro hs
    exact (exactLetters (h ++ suffix)).mpr
      ((letterwise_append L h suffix).mpr
        ⟨(exactLetters h).mp hh, (exactLetters suffix).mp hs⟩)

/-- Exact boundary of unchanged finite existential continuation profiles. -/
theorem stable_iff_letterwise (L : List A → Prop)
    (closed : PrefixClosed L) (empty : L []) :
    Stable L ↔ ∀ word, L word ↔ Letterwise L word :=
  ⟨stable_implies_letterwise L closed empty, letterwise_implies_stable L⟩

theorem joint_obstruction_refutes_stability (L : List A → Prop)
    (closed : PrefixClosed L) (empty : L []) (word : List A)
    (letters : Letterwise L word) (blocked : ¬ L word) : ¬ Stable L := by
  intro stable
  exact blocked ((stable_implies_letterwise L closed empty stable word).mpr letters)

/-- A witnessed loss of one initially feasible continuation separates profiles. -/
theorem blocked_extension_separates (L : List A → Prop) (past suffix : List A)
    (initially : L suffix) (blocked : ¬ L (past ++ suffix)) :
    ¬ SameFuture L past [] := by
  intro same
  exact blocked ((same suffix).mpr initially)

/-- A finite decidable obstruction locates an admitted prefix before failure.
This is a formal feasibility witness, not a claim the prefix was enacted. -/
theorem locate_first_obstruction (L : List A → Prop) [DecidablePred L]
    (start word : List A) (admitted : L start)
    (letters : Letterwise L word) (blocked : ¬ L (start ++ word)) :
    ∃ pre a suffix, word = pre ++ (a :: suffix) ∧ L (start ++ pre) ∧
      L [a] ∧ ¬ L ((start ++ pre) ++ [a]) := by
  induction word generalizing start with
  | nil => exact False.elim (blocked ((append_nil_constructive start).symm ▸ admitted))
  | cons a word ih =>
    by_cases next : L (start ++ [a])
    · have laterBlocked : ¬ L ((start ++ [a]) ++ word) := by
        intro h
        exact blocked ((append_assoc_constructive start [a] word) ▸ h)
      obtain ⟨pre, b, suffix, heq, hp, hb, hn⟩ :=
        ih (start ++ [a]) next letters.2 laterBlocked
      refine ⟨a :: pre, b, suffix, congrArg (List.cons a) heq, ?_, hb, ?_⟩
      · exact (append_assoc_constructive start [a] pre) ▸ hp
      · intro h
        apply hn
        exact (congrArg (fun xs => xs ++ [b])
          (append_assoc_constructive start [a] pre)).symm ▸ h
    · refine ⟨[], a, word, rfl, ?_, letters.1, ?_⟩
      · exact (append_nil_constructive start).symm ▸ admitted
      · intro h
        exact next ((congrArg (fun xs => xs ++ [a]) (append_nil_constructive start)) ▸ h)

theorem obstruction_locates_changed_profile (L : List A → Prop) [DecidablePred L]
    (empty : L []) (word : List A) (letters : Letterwise L word)
    (blocked : ¬ L word) :
    ∃ pre a suffix, word = pre ++ (a :: suffix) ∧ L pre ∧
      L [a] ∧ ¬ L (pre ++ [a]) ∧ ¬ SameFuture L pre [] := by
  obtain ⟨pre, a, suffix, heq, hp, ha, hn⟩ :=
    locate_first_obstruction L [] word empty letters blocked
  exact ⟨pre, a, suffix, heq, hp, ha, hn,
    blocked_extension_separates L pre [a] ha hn⟩

def unrestricted : List Bool → Prop := fun _ => True

/-- Genuine finite histories of every length can have unchanged profiles. -/
theorem unrestricted_stable : Stable unrestricted := by
  intro _ _ _
  exact ⟨fun _ => True.intro, fun _ => True.intro⟩

theorem unrestricted_realized (word : List Bool) :
    Feasible (historyProcess unrestricted) [] word := by
  apply (history_feasible_iff (fun _ _ _ => True.intro) True.intro word).mpr
  exact True.intro

/-- One process with a formed latch: true closes the false route, while true
remains possible. The state/action roles belong to this local presentation. -/
def latch : Process Bool Bool where
  step before event after :=
    (before = false ∨ event = true) ∧ after = (before || event)

theorem latch_obstruction :
    Feasible latch false [true] ∧ Feasible latch false [false] ∧
    ¬ Feasible latch false [true, false] ∧
    Feasible latch false [true, true] := by
  refine ⟨⟨true, .cons ⟨Or.inl rfl, rfl⟩ (.nil true)⟩,
    ⟨false, .cons ⟨Or.inl rfl, rfl⟩ (.nil false)⟩, ?_,
    ⟨true, .cons ⟨Or.inl rfl, rfl⟩ (.cons ⟨Or.inr rfl, rfl⟩ (.nil true))⟩⟩
  rintro ⟨last, trace⟩
  obtain ⟨middle, first, rest⟩ := trace_cons_iff.mp trace
  have hm : middle = true := first.2
  subst middle
  obtain ⟨_, second, _⟩ := trace_cons_iff.mp rest
  cases second.1 with
  | inl bad => cases bad
  | inr bad => cases bad

theorem latch_changes_profile_and_continues :
    ¬ SameFuture (Feasible latch false) [true] [] ∧
      Feasible latch false [true, true] :=
  ⟨blocked_extension_separates _ [true] [false]
    latch_obstruction.2.1 latch_obstruction.2.2.1,
    latch_obstruction.2.2.2⟩

end Generative.ContinuationConditions

#print axioms Generative.ContinuationConditions.future_update
#print axioms Generative.ContinuationConditions.same_future_extends
#print axioms Generative.ContinuationConditions.future_is_reachable_union
#print axioms Generative.ContinuationConditions.letterwise_append
#print axioms Generative.ContinuationConditions.stable_implies_letterwise
#print axioms Generative.ContinuationConditions.letterwise_implies_stable
#print axioms Generative.ContinuationConditions.stable_iff_letterwise
#print axioms Generative.ContinuationConditions.joint_obstruction_refutes_stability
#print axioms Generative.ContinuationConditions.blocked_extension_separates
#print axioms Generative.ContinuationConditions.locate_first_obstruction
#print axioms Generative.ContinuationConditions.obstruction_locates_changed_profile
#print axioms Generative.ContinuationConditions.unrestricted_stable
#print axioms Generative.ContinuationConditions.unrestricted_realized
#print axioms Generative.ContinuationConditions.latch_obstruction
#print axioms Generative.ContinuationConditions.latch_changes_profile_and_continues
