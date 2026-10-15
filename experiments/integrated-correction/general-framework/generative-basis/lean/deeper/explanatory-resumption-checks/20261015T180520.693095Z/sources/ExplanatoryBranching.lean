import ExplanatoryUniqueness
import RelationalDynamics

/-! Finite branching tests force a relational correspondence; no state bijection,
determinism or native transition decoder is assumed. The converse is the
image-finite Hennessy-Milner route, with its classical dependencies audited.
Test availability and explanatory applicability remain substantive questions. -/
namespace Generative.ExplanatoryBranching
open ExplanatoryUniqueness
universe u v w x y

inductive Test (A : Type v) (O : Type w) where
  | top : Test A O
  | atom : O → Test A O
  | neg : Test A O → Test A O
  | conj : Test A O → Test A O → Test A O
  | after : A → Test A O → Test A O

structure Model (S : Type u) (A : Type v) (O : Type w) where
  process : Process S A
  condition : S → O → Prop

def Holds {S : Type u} {A : Type v} {O : Type w} (m : Model S A O) (s : S) : Test A O → Prop
  | .top => True
  | .atom o => m.condition s o
  | .neg f => ¬ Holds m s f
  | .conj f g => Holds m s f ∧ Holds m s g
  | .after a f => ∃ t, m.process.step s a t ∧ Holds m t f

def Same {S : Type u} {T : Type x} {A : Type v} {O : Type w}
    (m : Model S A O) (n : Model T A O) (s : S) (t : T) : Prop :=
  ∀ f, Holds m s f ↔ Holds n t f

def Bisimulation {S : Type u} {T : Type x} {A : Type v} {O : Type w}
    (m : Model S A O) (n : Model T A O) (R : S → T → Prop) : Prop :=
  Deeper.Bisimulation m.process n.process R ∧
    ∀ s t, R s t → ∀ o, m.condition s o ↔ n.condition t o

def ImageFinite {S : Type u} {A : Type v} {O : Type w} (m : Model S A O) : Prop :=
  ∀ s a, ∃ xs : List S, ∀ t, m.process.step s a t ↔ t ∈ xs

variable {S : Type u} {T : Type x} {U : Type y} {A : Type v} {O : Type w}
variable {m : Model S A O} {n : Model T A O} {p : Model U A O}

theorem same_refl (s : S) : Same m m s s := fun _ => Iff.rfl

theorem same_symm {s : S} {t : T} (h : Same m n s t) : Same n m t s := fun f => (h f).symm

theorem same_trans {s : S} {t : T} {z : U} (h : Same m n s t) (k : Same n p t z) :
    Same m p s z := fun f => (h f).trans (k f)

theorem bisimulation_preserves_tests {R : S → T → Prop} (h : Bisimulation m n R) :
    ∀ f s t, R s t → (Holds m s f ↔ Holds n t f) := by
  intro f
  induction f with
  | top => intro s t _; exact Iff.rfl
  | atom o => intro s t hr; exact h.2 s t hr o
  | neg f ih =>
    intro s t hr
    constructor
    · intro hn yes; exact hn ((ih s t hr).mpr yes)
    · intro hn yes; exact hn ((ih s t hr).mp yes)
  | conj f g ihf ihg =>
    intro s t hr
    exact ⟨fun hx => ⟨(ihf s t hr).mp hx.1, (ihg s t hr).mp hx.2⟩,
      fun hx => ⟨(ihf s t hr).mpr hx.1, (ihg s t hr).mpr hx.2⟩⟩
  | after a f ih =>
    intro s t hr
    constructor
    · rintro ⟨s', hs, hf⟩
      obtain ⟨t', ht, hr'⟩ := h.1.1 s t a s' hr hs
      exact ⟨t', ht, (ih s' t' hr').mp hf⟩
    · rintro ⟨t', ht, hf⟩
      obtain ⟨s', hs, hr'⟩ := h.1.2 s t a t' hr ht
      exact ⟨s', hs, (ih s' t' hr').mpr hf⟩

theorem bisimulation_implies_same {R : S → T → Prop} (h : Bisimulation m n R)
    {s : S} {t : T} (hr : R s t) : Same m n s t := fun f => bisimulation_preserves_tests h f s t hr

/-- Constructive finite conjunction step, given distinguishing witnesses. -/
theorem finite_separating_test (s : S) (xs : List T)
    (h : ∀ t, t ∈ xs → ∃ f, Holds m s f ∧ ¬ Holds n t f) :
    ∃ f, Holds m s f ∧ ∀ t, t ∈ xs → ¬ Holds n t f := by
  induction xs with
  | nil => exact ⟨.top, True.intro, fun _ ht => False.elim (List.not_mem_nil ht)⟩
  | cons t xs ih =>
    obtain ⟨f, hf, ht⟩ := h t (List.mem_cons_self)
    obtain ⟨g, hg, hx⟩ := ih (fun z hz => h z (List.mem_cons_of_mem t hz))
    refine ⟨.conj f g, ⟨hf, hg⟩, ?_⟩
    intro z hz both
    cases List.mem_cons.mp hz with
    | inl eq => subst z; exact ht both.1
    | inr mem => exact hx z mem both.2

/-- Classical orientation of a logical disagreement; kept separate from the
constructive finite conjunction lemma and finite concrete witnesses. -/
theorem not_same_has_separating_test {s : S} {t : T} (h : ¬ Same m n s t) :
    ∃ f, Holds m s f ∧ ¬ Holds n t f := by
  classical
  apply Classical.byContradiction
  intro no
  apply h
  intro f
  constructor
  · intro hm
    apply Classical.byContradiction
    intro hn
    exact no ⟨f, hm, hn⟩
  · intro hn
    apply Classical.byContradiction
    intro hm
    exact no ⟨.neg f, hm, fun hnot => hnot hn⟩

/-- Matching successors is derived from truthful finite tests, not stipulated
inside the explanation's representation. -/
theorem same_forces_successor_match (finite : ImageFinite n)
    {s : S} {t : T} (same : Same m n s t) {a : A} {s' : S}
    (step : m.process.step s a s') :
    ∃ t', n.process.step t a t' ∧ Same m n s' t' := by
  classical
  apply Classical.byContradiction
  intro no
  obtain ⟨xs, hx⟩ := finite t a
  have sep : ∀ z, z ∈ xs → ∃ f, Holds m s' f ∧ ¬ Holds n z f := by
    intro z hz
    apply not_same_has_separating_test
    intro same'
    exact no ⟨z, (hx z).mpr hz, same'⟩
  obtain ⟨f, hf, exclude⟩ := finite_separating_test s' xs sep
  have yes : Holds m s (.after a f) := ⟨s', step, hf⟩
  obtain ⟨t', ht, hf'⟩ := (same (.after a f)).mp yes
  exact exclude t' ((hx t').mp ht) hf'

theorem same_is_bisimulation (fm : ImageFinite m) (fn : ImageFinite n) :
    Bisimulation m n (Same m n) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · intro s t a s' same hs
    exact same_forces_successor_match fn same hs
  · intro s t a t' same ht
    obtain ⟨s', hs, he⟩ := same_forces_successor_match fm (same_symm same) ht
    exact ⟨s', hs, same_symm he⟩
  · intro s t same o
    exact same (.atom o)

theorem same_iff_bisimilar (fm : ImageFinite m) (fn : ImageFinite n) (s : S) (t : T) :
    Same m n s t ↔ ∃ R, Bisimulation m n R ∧ R s t :=
  ⟨fun h => ⟨Same m n, same_is_bisimulation fm fn, h⟩,
   fun ⟨_, h, hr⟩ => bisimulation_implies_same h hr⟩

/-- Generic answer correctness is enough: no transition decoder, homomorphism
or relation-preservation field is required in the presentation. -/
theorem exact_equal_codes_force_branch_matching {C : Type y}
    (fm : ImageFinite m) (account : Presentation S (Test A O) C)
    (exact : Exact (Holds m) account) {s t : S}
    (eq : account.encode s = account.encode t) :
    ∃ R, Bisimulation m m R ∧ R s t := by
  apply (same_iff_bisimilar fm fm s t).mp
  exact equal_codes_same_answers exact eq

/-- Each actual finite trace has a matched trace with related endpoint. -/
theorem bisimulation_lifts_trace {R : S → T → Prop} (h : Bisimulation m n R)
    {s : S} {t : T} (related : R s t) {word : List A} {s' : S}
    (trace : Trace m.process s word s') :
    ∃ t', Trace n.process t word t' ∧ R s' t' := by
  induction trace generalizing t with
  | nil s => exact ⟨t, .nil t, related⟩
  | @cons s middle finish a rest step tail ih =>
    obtain ⟨mid, qstep, rm⟩ := h.1.1 s t a middle related step
    obtain ⟨end', qt, re⟩ := ih rm
    exact ⟨end', .cons qstep qt, re⟩

def ReachableFrom (m : Model S A O) (root : S) : Prop :=
  ∀ s, ∃ word, Trace m.process root word s

def Separated (m : Model S A O) : Prop := ∀ s t, Same m m s t → s = t

theorem same_functional (sep : Separated n) {s : S} {t t' : T}
    (h : Same m n s t) (h' : Same m n s t') : t = t' :=
  sep t t' (same_trans (same_symm h) h')

theorem same_inverse_functional (sep : Separated m) {s s' : S} {t : T}
    (h : Same m n s t) (h' : Same m n s' t) : s = s' :=
  sep s s' (same_trans h (same_symm h'))

theorem same_total_on_reachable (fm : ImageFinite m) (fn : ImageFinite n)
    {root : S} {otherRoot : T} (h : Same m n root otherRoot)
    (reach : ReachableFrom m root) (s : S) : ∃ t, Same m n s t := by
  obtain ⟨word, trace⟩ := reach s
  obtain ⟨t, _, related⟩ := bisimulation_lifts_trace (same_is_bisimulation fm fn) h trace
  exact ⟨t, related⟩

theorem branching_structural_correspondence (fm : ImageFinite m) (fn : ImageFinite n)
    {root : S} {otherRoot : T} (h : Same m n root otherRoot)
    (rm : ReachableFrom m root) (rn : ReachableFrom n otherRoot)
    (sm : Separated m) (sn : Separated n) :
    (∀ s, ∃ t, Same m n s t ∧ ∀ t', Same m n s t' → t' = t) ∧
    (∀ t, ∃ s, Same m n s t ∧ ∀ s', Same m n s' t → s' = s) := by
  constructor
  · intro s
    obtain ⟨t, ht⟩ := same_total_on_reachable fm fn h rm s
    exact ⟨t, ht, fun _ ht' => same_functional sn ht' ht⟩
  · intro t
    obtain ⟨s, hs⟩ := same_total_on_reachable fn fm (same_symm h) rn t
    have hs' := same_symm hs
    exact ⟨s, hs', fun _ h' => same_inverse_functional sm h' hs'⟩

theorem correspondence_preserves_steps (fm : ImageFinite m) (fn : ImageFinite n)
    (sm : Separated m) (sn : Separated n) {s s' : S} {t t' : T}
    (h : Same m n s t) (h' : Same m n s' t') (a : A) :
    m.process.step s a s' ↔ n.process.step t a t' := by
  constructor
  · intro hs
    obtain ⟨z, hz, he⟩ := same_forces_successor_match fn h hs
    have eq := same_functional sn he h'
    exact eq ▸ hz
  · intro ht
    obtain ⟨z, hz, he⟩ := same_forces_successor_match fm (same_symm h) ht
    have eq := same_inverse_functional sm (same_symm he) h'
    exact eq ▸ hz

/-- Every adequate relational comparison is forced into the same correspondence
when target states are separated; this does not select an intrinsic state name. -/
theorem any_bisimulation_agrees (sep : Separated n) {R : S → T → Prop}
    (bis : Bisimulation m n R) {s : S} {t t' : T}
    (same : Same m n s t) (related : R s t') : t = t' :=
  same_functional sep same (bisimulation_implies_same bis related)

end Generative.ExplanatoryBranching

#print axioms Generative.ExplanatoryBranching.same_refl
#print axioms Generative.ExplanatoryBranching.same_symm
#print axioms Generative.ExplanatoryBranching.same_trans
#print axioms Generative.ExplanatoryBranching.bisimulation_preserves_tests
#print axioms Generative.ExplanatoryBranching.bisimulation_implies_same
#print axioms Generative.ExplanatoryBranching.finite_separating_test
#print axioms Generative.ExplanatoryBranching.not_same_has_separating_test
#print axioms Generative.ExplanatoryBranching.same_forces_successor_match
#print axioms Generative.ExplanatoryBranching.same_is_bisimulation
#print axioms Generative.ExplanatoryBranching.same_iff_bisimilar
#print axioms Generative.ExplanatoryBranching.exact_equal_codes_force_branch_matching
#print axioms Generative.ExplanatoryBranching.bisimulation_lifts_trace
#print axioms Generative.ExplanatoryBranching.same_functional
#print axioms Generative.ExplanatoryBranching.same_inverse_functional
#print axioms Generative.ExplanatoryBranching.same_total_on_reachable
#print axioms Generative.ExplanatoryBranching.branching_structural_correspondence
#print axioms Generative.ExplanatoryBranching.correspondence_preserves_steps
#print axioms Generative.ExplanatoryBranching.any_bisimulation_agrees
