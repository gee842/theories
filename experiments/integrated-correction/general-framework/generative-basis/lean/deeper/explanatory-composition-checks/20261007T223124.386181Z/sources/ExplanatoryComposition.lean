import ExplanatoryUniqueness

/-! Contextual answers force a composition structure on reduced presentations.
Concatenation and the target language are supplied independently. This does not
claim that arbitrary physical processes are words or that all tests are acquired. -/
namespace Generative.ExplanatoryComposition
open ExplanatoryUniqueness
universe u v w
variable {A : Type u} {C : Type v} {D : Type w}

abbrev Context (A : Type u) := List A × List A

def target (L : List A → Prop) (word : List A) (q : Context A) : Prop :=
  L (q.1 ++ word ++ q.2)

abbrev ContextEq (L : List A → Prop) (x y : List A) := SameAnswers (target L) x y

abbrev Summary (A : Type u) (C : Type v) := Presentation (List A) (Context A) C

theorem context_refl (L : List A → Prop) (x : List A) : ContextEq L x x :=
  fun _ => Iff.rfl

theorem context_symm {L : List A → Prop} {x y : List A} (h : ContextEq L x y) :
    ContextEq L y x := fun q => (h q).symm

theorem context_trans {L : List A → Prop} {x y z : List A}
    (hxy : ContextEq L x y) (hyz : ContextEq L y z) : ContextEq L x z :=
  fun q => (hxy q).trans (hyz q)

theorem context_agrees_here {L : List A → Prop} {x y : List A} (h : ContextEq L x y) :
    L x ↔ L y := by
  have he := h ([], [])
  simpa only [target, List.nil_append, List.append_nil] using he

theorem context_append {L : List A → Prop} {x x' y y' : List A}
    (hx : ContextEq L x x') (hy : ContextEq L y y') : ContextEq L (x ++ y) (x' ++ y') := by
  intro q
  have hl := hx (q.1, y ++ q.2)
  have hr := hy (q.1 ++ x', q.2)
  simp only [target, List.append_assoc] at hl hr ⊢
  exact hl.trans hr

theorem context_stable {L : List A → Prop} {x y : List A} (h : ContextEq L x y)
    (left right : List A) : ContextEq L (left ++ x ++ right) (left ++ y ++ right) :=
  context_append (context_append (context_refl L left) h) (context_refl L right)

/-- Every substitution-stable relation respecting the target refines ContextEq.
Thus the closure is characterized rather than selected to favor a code. -/
theorem stable_relation_refines_context (L : List A → Prop) (R : List A → List A → Prop)
    (stable : ∀ x y, R x y → ∀ l r, R (l ++ x ++ r) (l ++ y ++ r))
    (respects : ∀ x y, R x y → (L x ↔ L y))
    {x y : List A} (h : R x y) : ContextEq L x y :=
  fun q => respects _ _ (stable x y h q.1 q.2)

theorem encoded_append_congr {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    {x x' y y' : List A} (hx : p.encode x = p.encode x') (hy : p.encode y = p.encode y') :
    p.encode (x ++ y) = p.encode (x' ++ y') :=
  rp _ _ (context_append (equal_codes_same_answers hp hx) (equal_codes_same_answers hp hy))

/-- The operation is induced from actual word composition, not stored as an
extra homomorphism requirement in Exact or Reduced. -/
def Compose (p : Summary A C) (a b c : C) : Prop :=
  ∃ x y, p.encode x = a ∧ p.encode y = b ∧ p.encode (x ++ y) = c

theorem compose_encoded_iff {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    (x y : List A) (c : C) : Compose p (p.encode x) (p.encode y) c ↔ p.encode (x ++ y) = c := by
  constructor
  · rintro ⟨u, v, hu, hv, huv⟩
    exact (encoded_append_congr hp rp hu hv).symm.trans huv
  · intro h
    exact ⟨x, y, rfl, rfl, h⟩

theorem compose_total (p : Summary A C) {a b : C} (ha : Used p a) (hb : Used p b) :
    ∃ c, Used p c ∧ Compose p a b c := by
  obtain ⟨x, hx⟩ := ha
  obtain ⟨y, hy⟩ := hb
  exact ⟨p.encode (x ++ y), ⟨x ++ y, rfl⟩, ⟨x, y, hx, hy, rfl⟩⟩

theorem compose_functional {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    {a b c d : C} (hc : Compose p a b c) (hd : Compose p a b d) : c = d := by
  obtain ⟨x, y, hx, hy, hxy⟩ := hc
  obtain ⟨u, v, hu, hv, huv⟩ := hd
  exact hxy.symm.trans ((encoded_append_congr hp rp (hx.trans hu.symm) (hy.trans hv.symm)).trans huv)

theorem compose_associative {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) (rp : Reduced (target L) p) (a b c d : C) :
    (∃ m, Compose p a b m ∧ Compose p m c d) ↔
      (∃ n, Compose p b c n ∧ Compose p a n d) := by
  constructor
  · rintro ⟨m, ⟨x, y, hx, hy, hxy⟩, ⟨u, v, hu, hv, huv⟩⟩
    have he := encoded_append_congr hp rp (hxy.trans hu.symm) (rfl : p.encode v = p.encode v)
    refine ⟨p.encode (y ++ v), ⟨y, v, hy, hv, rfl⟩, ⟨x, y ++ v, hx, rfl, ?_⟩⟩
    exact (congrArg p.encode (List.append_assoc x y v)).symm.trans (he.trans huv)
  · rintro ⟨n, ⟨y, z, hy, hz, hyz⟩, ⟨x, u, hx, hu, hxu⟩⟩
    have he := encoded_append_congr hp rp (rfl : p.encode x = p.encode x) (hyz.trans hu.symm)
    refine ⟨p.encode (x ++ y), ⟨x, y, hx, hy, rfl⟩, ⟨x ++ y, z, rfl, hz, ?_⟩⟩
    exact (congrArg p.encode (List.append_assoc x y z)).trans (he.trans hxu)

theorem compose_left_identity {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    {c d : C} (hc : Used p c) : Compose p (p.encode []) c d ↔ c = d := by
  obtain ⟨x, hx⟩ := hc
  subst c
  exact compose_encoded_iff hp rp [] x d

theorem compose_right_identity {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    {c d : C} (hc : Used p c) : Compose p c (p.encode []) d ↔ c = d := by
  obtain ⟨x, hx⟩ := hc
  subst c
  have he := compose_encoded_iff hp rp x [] d
  simpa only [List.append_nil] using he

theorem matching_composes {L : List A → Prop} {p : Summary A C} {r : Summary A D}
    (hp : Exact (target L) p) (rr : Reduced (target L) r)
    {a b c : C} {a' b' c' : D}
    (ha : Matches p r a a') (hb : Matches p r b b') (hc : Matches p r c c')
    (h : Compose p a b c) : Compose r a' b' c' := by
  obtain ⟨x, y, hx, hy, hxy⟩ := h
  have hxa : r.encode x = a' := matches_functional hp rr ⟨x, hx, rfl⟩ ha
  have hyb : r.encode y = b' := matches_functional hp rr ⟨y, hy, rfl⟩ hb
  have hxyc : r.encode (x ++ y) = c' := matches_functional hp rr ⟨x ++ y, hxy, rfl⟩ hc
  exact ⟨x, y, hxa, hyb, hxyc⟩

theorem matches_swap {p : Summary A C} {r : Summary A D} {a : C} {b : D}
    (h : Matches p r a b) : Matches r p b a := by
  obtain ⟨x, hx, hy⟩ := h
  exact ⟨x, hy, hx⟩

theorem matching_preserves_composition {L : List A → Prop} {p : Summary A C} {r : Summary A D}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    (hr : Exact (target L) r) (rr : Reduced (target L) r)
    {a b c : C} {a' b' c' : D}
    (ha : Matches p r a a') (hb : Matches p r b b') (hc : Matches p r c c') :
    Compose p a b c ↔ Compose r a' b' c' :=
  ⟨matching_composes hp rr ha hb hc,
    matching_composes hr rp (matches_swap ha) (matches_swap hb) (matches_swap hc)⟩

theorem matching_preserves_identity (p : Summary A C) (r : Summary A D) :
    Matches p r (p.encode []) (r.encode []) := ⟨[], rfl, rfl⟩

/-- The earlier unique answer correspondence now also preserves composition
and the empty context. No preservation field is assumed on the correspondence. -/
theorem structural_unique_correspondence {L : List A → Prop} {p : Summary A C} {r : Summary A D}
    (hp : Exact (target L) p) (rp : Reduced (target L) p)
    (hr : Exact (target L) r) (rr : Reduced (target L) r) :
    (∀ a, Used p a → ∃ b, Matches p r a b ∧ ∀ c, Matches p r a c → c = b) ∧
    (∀ b, Used r b → ∃ a, Matches p r a b ∧ ∀ c, Matches p r c b → c = a) ∧
    Matches p r (p.encode []) (r.encode []) ∧
    (∀ a b c a' b' c', Matches p r a a' → Matches p r b b' → Matches p r c c' →
      (Compose p a b c ↔ Compose r a' b' c')) := by
  have h := relative_unique_correspondence hp rp hr rr
  exact ⟨h.1, h.2, matching_preserves_identity p r,
    fun _ _ _ _ _ _ ha hb hc => matching_preserves_composition hp rp hr rr ha hb hc⟩

/-- A general existence witness, not an effective finite encoding or an account
of how answers are acquired. Function and proposition extensionality are used
in reduction; their standard Lean dependencies are audited explicitly. -/
def canonicalSummary (L : List A → Prop) : Summary A (Context A → Prop) where
  encode := target L
  read code q := code q

theorem canonical_exact (L : List A → Prop) : Exact (target L) (canonicalSummary L) :=
  fun _ _ => Iff.rfl

theorem canonical_reduced (L : List A → Prop) : Reduced (target L) (canonicalSummary L) := by
  intro x y h
  funext q
  exact propext (h q)

theorem reduced_presentation_exists (L : List A → Prop) :
    ∃ p : Summary A (Context A → Prop), Exact (target L) p ∧ Reduced (target L) p :=
  ⟨canonicalSummary L, canonical_exact L, canonical_reduced L⟩

/-- Even a redundant exact presentation has a canonical surjective functional
matching to the minimal contextual structure. Its induced Compose relation need
not itself be functional, so this is stated as a relation-preserving factor. -/
theorem canonical_factorization {L : List A → Prop} {p : Summary A C}
    (hp : Exact (target L) p) :
    (∀ c, Used p c → ∃ d, Used (canonicalSummary L) d ∧
      Matches p (canonicalSummary L) c d ∧
      ∀ e, Matches p (canonicalSummary L) c e → e = d) ∧
    (∀ d, Used (canonicalSummary L) d → ∃ c, Used p c ∧ Matches p (canonicalSummary L) c d) ∧
    (∀ a b c a' b' c', Matches p (canonicalSummary L) a a' →
      Matches p (canonicalSummary L) b b' → Matches p (canonicalSummary L) c c' →
      Compose p a b c → Compose (canonicalSummary L) a' b' c') := by
  refine ⟨?_, ?_, ?_⟩
  · intro c hc
    obtain ⟨d, hd, hm⟩ := matches_total_on_used p (canonicalSummary L) hc
    exact ⟨d, hd, hm, fun _ he => matches_functional hp (canonical_reduced L) he hm⟩
  · intro d hd
    obtain ⟨x, hx⟩ := hd
    exact ⟨p.encode x, ⟨x, rfl⟩, ⟨x, rfl, hx⟩⟩
  · intro a b c a' b' c' ha hb hc h
    exact matching_composes hp (canonical_reduced L) ha hb hc h

/-- A counterexample to replacing two-sided context tests by suffix tests. -/
def exactPattern (word : List Bool) : Prop := word = [true, false]

theorem suffix_tests_can_miss_left_context :
    (∀ suffix, exactPattern ([false] ++ suffix) ↔ exactPattern ([true, true] ++ suffix)) ∧
    ¬ ContextEq exactPattern [false] [true, true] := by
  constructor
  · intro suffix
    constructor <;> intro h <;> cases h
  · intro h
    have bad := (h ([true], [])).mp rfl
    cases bad

theorem current_answer_can_miss_composition :
    (exactPattern [] ↔ exactPattern [true]) ∧
    ¬ (exactPattern ([] ++ [false]) ↔ exactPattern ([true] ++ [false])) := by
  constructor
  · constructor <;> intro h <;> cases h
  · intro h
    have bad := h.mpr rfl
    cases bad

/-- An explicit finite realization of the earlier one-event budget language. -/
inductive Bucket where
  | empty | single | overflow
  deriving DecidableEq

def classify : List Unit → Bucket
  | [] => .empty
  | [_] => .single
  | _ :: _ :: _ => .overflow

def multiply : Bucket → Bucket → Bucket
  | .empty, b => b
  | .single, .empty => .single
  | .single, _ => .overflow
  | .overflow, _ => .overflow

def accepted : Bucket → Prop
  | .empty | .single => True
  | .overflow => False

def representative : Bucket → List Unit
  | .empty => []
  | .single => [()]
  | .overflow => [(), ()]

theorem classify_representative (b : Bucket) : classify (representative b) = b := by
  cases b <;> rfl

theorem classify_append (x y : List Unit) : classify (x ++ y) = multiply (classify x) (classify y) := by
  cases x with
  | nil => rfl
  | cons a xs =>
    cases xs with
    | nil =>
      cases y with
      | nil => rfl
      | cons b ys => cases ys <;> rfl
    | cons b xs => rfl

theorem accepted_classify (x : List Unit) : accepted (classify x) ↔ ExplanatoryNecessity.bounded x := by
  cases x with
  | nil => exact ⟨fun _ => Or.inl rfl, fun _ => True.intro⟩
  | cons a xs =>
    cases xs with
    | nil => exact ⟨fun _ => Or.inr ⟨a, rfl⟩, fun _ => True.intro⟩
    | cons b xs =>
      constructor
      · intro h; cases h
      · intro h
        rcases h with h | ⟨c, h⟩ <;> cases h

def budgetSummary : Summary Unit Bucket where
  encode := classify
  read c q := accepted (multiply (multiply (classify q.1) c) (classify q.2))

theorem budget_exact : Exact (target ExplanatoryNecessity.bounded) budgetSummary := by
  intro x q
  change accepted (multiply (multiply (classify q.1) (classify x)) (classify q.2)) ↔ _
  rw [← classify_append, ← classify_append]
  exact accepted_classify _

theorem bucket_separated (a b : Bucket)
    (h : ∀ l r, accepted (multiply (multiply l a) r) ↔ accepted (multiply (multiply l b) r)) : a = b := by
  have h0 := h .empty .empty
  have h1 := h .single .empty
  cases a <;> cases b <;> first
    | rfl
    | exact False.elim (h0.mp True.intro)
    | exact False.elim (h0.mpr True.intro)
    | exact False.elim (h1.mp True.intro)
    | exact False.elim (h1.mpr True.intro)

theorem budget_reduced : Reduced (target ExplanatoryNecessity.bounded) budgetSummary := by
  intro x y h
  apply bucket_separated
  intro l r
  have he := (budget_exact x (representative l, representative r)).trans
    ((h (representative l, representative r)).trans (budget_exact y (representative l, representative r)).symm)
  change accepted (multiply (multiply (classify (representative l)) (classify x)) (classify (representative r))) ↔
    accepted (multiply (multiply (classify (representative l)) (classify y)) (classify (representative r))) at he
  rw [classify_representative, classify_representative] at he
  exact he

theorem every_bucket_used (b : Bucket) : Used budgetSummary b :=
  ⟨representative b, classify_representative b⟩

theorem budget_composition (a b c : Bucket) : Compose budgetSummary a b c ↔ multiply a b = c := by
  have he := compose_encoded_iff budget_exact budget_reduced (representative a) (representative b) c
  change Compose budgetSummary (classify (representative a)) (classify (representative b)) c ↔
    classify (representative a ++ representative b) = c at he
  rw [classify_append, classify_representative, classify_representative] at he
  exact he

theorem any_exact_summary_retains_buckets {p : Summary Unit C}
    (hp : Exact (target ExplanatoryNecessity.bounded) p) {x y : List Unit}
    (h : p.encode x = p.encode y) : classify x = classify y :=
  budget_reduced x y (equal_codes_same_answers hp h)

theorem three_distinctions_required {p : Summary Unit C}
    (hp : Exact (target ExplanatoryNecessity.bounded) p) :
    p.encode [] ≠ p.encode [()] ∧ p.encode [] ≠ p.encode [(), ()] ∧
    p.encode [()] ≠ p.encode [(), ()] := by
  constructor
  · intro h; have bad := any_exact_summary_retains_buckets hp h; cases bad
  · constructor
    · intro h; have bad := any_exact_summary_retains_buckets hp h; cases bad
    · intro h; have bad := any_exact_summary_retains_buckets hp h; cases bad

theorem budget_kernel_characterization {p : Summary Unit C}
    (hp : Exact (target ExplanatoryNecessity.bounded) p)
    (rp : Reduced (target ExplanatoryNecessity.bounded) p) (x y : List Unit) :
    p.encode x = p.encode y ↔ classify x = classify y :=
  reduced_presentations_same_kernel hp rp budget_exact budget_reduced x y

end Generative.ExplanatoryComposition

#print axioms Generative.ExplanatoryComposition.context_refl
#print axioms Generative.ExplanatoryComposition.context_symm
#print axioms Generative.ExplanatoryComposition.context_trans
#print axioms Generative.ExplanatoryComposition.context_agrees_here
#print axioms Generative.ExplanatoryComposition.context_append
#print axioms Generative.ExplanatoryComposition.context_stable
#print axioms Generative.ExplanatoryComposition.stable_relation_refines_context
#print axioms Generative.ExplanatoryComposition.encoded_append_congr
#print axioms Generative.ExplanatoryComposition.compose_encoded_iff
#print axioms Generative.ExplanatoryComposition.compose_total
#print axioms Generative.ExplanatoryComposition.compose_functional
#print axioms Generative.ExplanatoryComposition.compose_associative
#print axioms Generative.ExplanatoryComposition.compose_left_identity
#print axioms Generative.ExplanatoryComposition.compose_right_identity
#print axioms Generative.ExplanatoryComposition.matching_composes
#print axioms Generative.ExplanatoryComposition.matches_swap
#print axioms Generative.ExplanatoryComposition.matching_preserves_composition
#print axioms Generative.ExplanatoryComposition.matching_preserves_identity
#print axioms Generative.ExplanatoryComposition.structural_unique_correspondence
#print axioms Generative.ExplanatoryComposition.canonical_exact
#print axioms Generative.ExplanatoryComposition.canonical_reduced
#print axioms Generative.ExplanatoryComposition.reduced_presentation_exists
#print axioms Generative.ExplanatoryComposition.canonical_factorization
#print axioms Generative.ExplanatoryComposition.suffix_tests_can_miss_left_context
#print axioms Generative.ExplanatoryComposition.current_answer_can_miss_composition
#print axioms Generative.ExplanatoryComposition.classify_representative
#print axioms Generative.ExplanatoryComposition.classify_append
#print axioms Generative.ExplanatoryComposition.accepted_classify
#print axioms Generative.ExplanatoryComposition.budget_exact
#print axioms Generative.ExplanatoryComposition.bucket_separated
#print axioms Generative.ExplanatoryComposition.budget_reduced
#print axioms Generative.ExplanatoryComposition.every_bucket_used
#print axioms Generative.ExplanatoryComposition.budget_composition
#print axioms Generative.ExplanatoryComposition.any_exact_summary_retains_buckets
#print axioms Generative.ExplanatoryComposition.three_distinctions_required
#print axioms Generative.ExplanatoryComposition.budget_kernel_characterization
