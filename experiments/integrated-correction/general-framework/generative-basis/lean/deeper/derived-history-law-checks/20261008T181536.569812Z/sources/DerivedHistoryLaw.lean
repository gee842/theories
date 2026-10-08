import ContinuationConditions

/-!
Derive a local relation from a supplied language and a summary of its histories.
Its exact finite continuation scope is characterized without supplying a second
update law, choosing representatives, or demanding endpoint-preserving lifting.
The language, its prefix closure, and its actual interpretation remain inputs.
-/
namespace Generative.DerivedHistoryLaw

open Deeper ContinuationConditions
universe u v
variable {A : Type u} {C : Type v}

/-- Each edge comes from one admitted extension in the same language. -/
def derivedProcess (L : List A → Prop) (q : List A → C) : Process C A where
  step s a t := ∃ h, L h ∧ q h = s ∧ L (h ++ [a]) ∧ q (h ++ [a]) = t

/-- Only admitted histories sharing a code need have the same finite futures. -/
def FiberFuture (L : List A → Prop) (q : List A → C) : Prop :=
  ∀ h k, L h → L k → q h = q k → SameFuture L h k

def ExactFuture (L : List A → Prop) (q : List A → C) : Prop :=
  ∀ h, L h → ∀ word, Feasible (derivedProcess L q) (q h) word ↔ L (h ++ word)

/-- Every admitted extension has its projected path, for every summary. -/
theorem admitted_extension_projects (L : List A → Prop) (closed : PrefixClosed L)
    (q : List A → C) {h word : List A} (hh : L h) (hw : L (h ++ word)) :
    Trace (derivedProcess L q) (q h) word (q (h ++ word)) := by
  have original : Trace (historyProcess L) h word (h ++ word) :=
    (history_trace_iff closed hh).mpr ⟨rfl, hw⟩
  apply trace_map (P := historyProcess L) (f := q) (h := original)
  intro before a after step
  obtain ⟨ha, hl⟩ := step
  subst after
  exact ⟨before, closed before [a] hl, rfl, hl, rfl⟩

/-- A summary cannot create false finite continuations if each used fiber has
one continuation profile. Endpoint lifting is not a premise or conclusion. -/
theorem derived_trace_sound (L : List A → Prop) (q : List A → C)
    (fibers : FiberFuture L q) {h word : List A} {t : C} (hh : L h)
    (path : Trace (derivedProcess L q) (q h) word t) : L (h ++ word) := by
  induction word generalizing h t with
  | nil => exact (append_nil_constructive h).symm ▸ hh
  | cons a word ih =>
    obtain ⟨m, edge, tail⟩ := trace_cons_iff.mp path
    obtain ⟨k, hk, hcode, hka, km⟩ := edge
    have ktail : Trace (derivedProcess L q) (q (k ++ [a])) word t := km.symm ▸ tail
    have klater : L ((k ++ [a]) ++ word) := ih hka ktail
    have kword : L (k ++ (a :: word)) :=
      (append_assoc_constructive k [a] word) ▸ klater
    exact (fibers k h hk hh hcode (a :: word)).mp kword

/-- Necessary and sufficient; local edges are constructed, not supplied. -/
theorem exact_iff_fiber_future (L : List A → Prop) (closed : PrefixClosed L)
    (q : List A → C) : ExactFuture L q ↔ FiberFuture L q := by
  constructor
  · intro hexact h k hh hk same word
    constructor
    · intro hw
      have path := (hexact h hh word).mpr hw
      exact (hexact k hk word).mp (same ▸ path)
    · intro hw
      have path := (hexact k hk word).mpr hw
      exact (hexact h hh word).mp (same.symm ▸ path)
  · intro fibers h hh word
    constructor
    · rintro ⟨t, path⟩
      exact derived_trace_sound L q fibers hh path
    · intro hw
      exact ⟨q (h ++ word), admitted_extension_projects L closed q hh hw⟩

/-- A witnessed bad merge yields a particular false continuation in the
derived local relation, not just failure of a sufficient certificate. -/
theorem distinguishing_merge_creates_false_continuation
    (L : List A → Prop) (closed : PrefixClosed L) (q : List A → C)
    {h k word : List A} (hh : L h) (hk : L k) (same : q h = q k)
    (yes : L (h ++ word)) (no : ¬ L (k ++ word)) :
    L k ∧ Feasible (derivedProcess L q) (q k) word ∧ ¬ L (k ++ word) := by
  have path := admitted_extension_projects L closed q hh yes
  exact ⟨hk, ⟨q (h ++ word), same ▸ path⟩, no⟩

def unrestricted : List Bool → Prop := fun _ => True

def singletonFalseCode : List Bool → Bool
  | [false] => true
  | _ => false

theorem unrestricted_summary_exact : ExactFuture unrestricted singletonFalseCode := by
  apply (exact_iff_fiber_future unrestricted (fun _ _ _ => True.intro)
    singletonFalseCode).mpr
  intro _ _ _ _ _ _
  exact ⟨fun _ => True.intro, fun _ => True.intro⟩

/-- Exact future words do not require exact encoded endpoints: the edge here
comes from [true] → [true,false], whose start shares the empty-history code. -/
theorem exact_futures_can_change_encoded_endpoint :
    ExactFuture unrestricted singletonFalseCode ∧
    Trace (derivedProcess unrestricted singletonFalseCode)
      (singletonFalseCode []) [false] false ∧
    singletonFalseCode ([] ++ [false]) ≠ false := by
  refine ⟨unrestricted_summary_exact, ?_, ?_⟩
  · exact .cons ⟨[true], True.intro, rfl, True.intro, rfl⟩ (.nil false)
  · intro bad
    cases bad

end Generative.DerivedHistoryLaw

#print axioms Generative.DerivedHistoryLaw.derivedProcess
#print axioms Generative.DerivedHistoryLaw.FiberFuture
#print axioms Generative.DerivedHistoryLaw.ExactFuture
#print axioms Generative.DerivedHistoryLaw.admitted_extension_projects
#print axioms Generative.DerivedHistoryLaw.derived_trace_sound
#print axioms Generative.DerivedHistoryLaw.exact_iff_fiber_future
#print axioms Generative.DerivedHistoryLaw.distinguishing_merge_creates_false_continuation
#print axioms Generative.DerivedHistoryLaw.unrestricted
#print axioms Generative.DerivedHistoryLaw.singletonFalseCode
#print axioms Generative.DerivedHistoryLaw.unrestricted_summary_exact
#print axioms Generative.DerivedHistoryLaw.exact_futures_can_change_encoded_endpoint
