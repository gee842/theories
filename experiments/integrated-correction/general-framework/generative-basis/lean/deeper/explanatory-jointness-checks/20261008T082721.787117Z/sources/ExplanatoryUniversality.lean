import ExplanatoryUniqueness

/-! Testing the route from an independently fixed answer family to arbitrary
ternary relational content. No associativity, local units or total operation is
assumed. Saturation is a substantive recoverability condition, not a definition
of sufficient explanation. All-predicate tests expose the limiting case. -/
namespace Generative.ExplanatoryUniversality
open ExplanatoryUniqueness
universe u v w
variable {M : Type u} {Q : Type v} {C : Type w}

def Saturated (target : M → Q → Prop) (J : M → M → M → Prop) : Prop :=
  ∀ a a' b b' c c', SameAnswers target a a' → SameAnswers target b b' →
    SameAnswers target c c' → (J a b c ↔ J a' b' c')

def Lift (p : Presentation M Q C) (J : M → M → M → Prop) (x y z : C) : Prop :=
  ∃ a b c, p.encode a = x ∧ p.encode b = y ∧ p.encode c = z ∧ J a b c

def RelExact (p : Presentation M Q C) (J : M → M → M → Prop)
    (K : C → C → C → Prop) : Prop :=
  ∀ a b c, K (p.encode a) (p.encode b) (p.encode c) ↔ J a b c

theorem lift_contains (p : Presentation M Q C) (J : M → M → M → Prop)
    {a b c : M} (h : J a b c) : Lift p J (p.encode a) (p.encode b) (p.encode c) :=
  ⟨a, b, c, rfl, rfl, rfl, h⟩

theorem saturation_gives_exact_lift {target : M → Q → Prop}
    {p : Presentation M Q C} {J : M → M → M → Prop}
    (hp : Exact target p) (hJ : Saturated target J) : RelExact p J (Lift p J) := by
  intro a b c
  constructor
  · rintro ⟨a', b', c', ha, hb, hc, hj⟩
    exact (hJ a' a b' b c' c (equal_codes_same_answers hp ha)
      (equal_codes_same_answers hp hb) (equal_codes_same_answers hp hc)).mp hj
  · exact lift_contains p J

theorem exact_relation_forces_saturation {target : M → Q → Prop}
    {p : Presentation M Q C} {J : M → M → M → Prop} {K : C → C → C → Prop}
    (rp : Reduced target p) (hK : RelExact p J K) : Saturated target J := by
  intro a a' b b' c c' ha hb hc
  have ea := rp a a' ha
  have eb := rp b b' hb
  have ec := rp c c' hc
  exact (hK a b c).symm.trans ((by rw [ea, eb, ec] :
    K (p.encode a) (p.encode b) (p.encode c) ↔
    K (p.encode a') (p.encode b') (p.encode c')).trans (hK a' b' c'))

/-- Necessary and sufficient, for any relation, without categorical laws. -/
theorem relation_descends_iff_saturated {target : M → Q → Prop}
    {p : Presentation M Q C} {J : M → M → M → Prop}
    (hp : Exact target p) (rp : Reduced target p) :
    (∃ K, RelExact p J K) ↔ Saturated target J :=
  ⟨fun ⟨_, h⟩ => exact_relation_forces_saturation rp h,
   fun h => ⟨Lift p J, saturation_gives_exact_lift hp h⟩⟩

theorem lift_exact_iff_saturated {target : M → Q → Prop}
    {p : Presentation M Q C} {J : M → M → M → Prop}
    (hp : Exact target p) (rp : Reduced target p) :
    RelExact p J (Lift p J) ↔ Saturated target J :=
  ⟨exact_relation_forces_saturation rp, saturation_gives_exact_lift hp⟩

theorem relational_reading_unique_on_used {p : Presentation M Q C}
    {J : M → M → M → Prop} {K L : C → C → C → Prop}
    (hk : RelExact p J K) (hl : RelExact p J L)
    {x y z : C} (hx : Used p x) (hy : Used p y) (hz : Used p z) :
    K x y z ↔ L x y z := by
  obtain ⟨a, rfl⟩ := hx
  obtain ⟨b, rfl⟩ := hy
  obtain ⟨c, rfl⟩ := hz
  exact (hk a b c).trans (hl a b c).symm

/-- If an actual pair of cases disagrees on J, no reduced answer-only account
can exactly read J; this is not an arbitrary altered ethical predicate. -/
theorem separating_relation_blocks_descent {target : M → Q → Prop}
    {p : Presentation M Q C} {J : M → M → M → Prop}
    (rp : Reduced target p) {a a' b b' c c' : M}
    (ha : SameAnswers target a a') (hb : SameAnswers target b b')
    (hc : SameAnswers target c c') (yes : J a b c) (no : ¬ J a' b' c') :
    ¬ ∃ K, RelExact p J K := by
  rintro ⟨K, hk⟩
  exact no ((exact_relation_forces_saturation rp hk a a' b b' c c' ha hb hc).mp yes)

def AllPredicates (m : M) (q : M → Prop) : Prop := q m

theorem all_predicates_separate (a b : M) : SameAnswers AllPredicates a b ↔ a = b := by
  constructor
  · intro h
    exact (h (fun x => a = x)).mp rfl
  · intro h
    subst b
    exact fun _ => Iff.rfl

theorem all_predicates_force_injective {p : Presentation M (M → Prop) C}
    (hp : Exact AllPredicates p) : ∀ a b, p.encode a = p.encode b → a = b := by
  intro a b h
  exact (all_predicates_separate a b).mp (equal_codes_same_answers hp h)

theorem all_predicates_every_relation (J : M → M → M → Prop) : Saturated AllPredicates J := by
  intro a a' b b' c c' ha hb hc
  cases (all_predicates_separate a a').mp ha
  cases (all_predicates_separate b b').mp hb
  cases (all_predicates_separate c c').mp hc
  exact Iff.rfl

theorem all_predicates_relation_recoverable {p : Presentation M (M → Prop) C}
    (hp : Exact AllPredicates p) (J : M → M → M → Prop) : RelExact p J (Lift p J) :=
  saturation_gives_exact_lift hp (all_predicates_every_relation J)

theorem all_predicates_automatically_reduced (p : Presentation M (M → Prop) C) :
    Reduced AllPredicates p := by
  intro a b h
  exact congrArg p.encode ((all_predicates_separate a b).mp h)

/-- The maximal query family yields the prior uniqueness theorem, but preserves
all supplied case distinctions; it does not discover which cases describe reality. -/
theorem all_predicates_unique_correspondence {D : Type w}
    {p : Presentation M (M → Prop) C} {r : Presentation M (M → Prop) D}
    (hp : Exact AllPredicates p) (hr : Exact AllPredicates r) :
    (∀ c, Used p c → ∃ d, Matches p r c d ∧ ∀ e, Matches p r c e → e = d) ∧
    (∀ d, Used r d → ∃ c, Matches p r c d ∧ ∀ e, Matches p r e d → e = c) :=
  relative_unique_correspondence hp (all_predicates_automatically_reduced p)
    hr (all_predicates_automatically_reduced r)

end Generative.ExplanatoryUniversality

#print axioms Generative.ExplanatoryUniversality.lift_contains
#print axioms Generative.ExplanatoryUniversality.saturation_gives_exact_lift
#print axioms Generative.ExplanatoryUniversality.exact_relation_forces_saturation
#print axioms Generative.ExplanatoryUniversality.relation_descends_iff_saturated
#print axioms Generative.ExplanatoryUniversality.lift_exact_iff_saturated
#print axioms Generative.ExplanatoryUniversality.relational_reading_unique_on_used
#print axioms Generative.ExplanatoryUniversality.separating_relation_blocks_descent
#print axioms Generative.ExplanatoryUniversality.all_predicates_separate
#print axioms Generative.ExplanatoryUniversality.all_predicates_force_injective
#print axioms Generative.ExplanatoryUniversality.all_predicates_every_relation
#print axioms Generative.ExplanatoryUniversality.all_predicates_relation_recoverable
#print axioms Generative.ExplanatoryUniversality.all_predicates_automatically_reduced
#print axioms Generative.ExplanatoryUniversality.all_predicates_unique_correspondence
