import ExplanatoryJoiningContexts

/-! Exact answers to generated joining arrangements force an operational
factor. Reducedness is needed for unique codes, not for unavoidable content.
This reuses the earlier relative-uniqueness theorem rather than recounting it. -/
namespace Generative.ExplanatoryContextualStructure
open ExplanatoryUniqueness ExplanatoryLocalUnits ExplanatoryJoiningContexts
universe u v w
variable {F : Type u} {C : Type v} {D : Type w}

def target (J : Join F) (x : F) (c : Context F) : Prop := Possible J c x

abbrev Account (F : Type u) (C : Type v) := Presentation F (Context F) C

def Operation (J : Join F) (p : Account F C) (a b c : C) : Prop :=
  ∃ x y z, p.encode x = a ∧ p.encode y = b ∧ p.encode z = c ∧ J x y z

theorem exact_same_code {J : Join F} {p : Account F C}
    (hp : Exact (target J) p) {x y : F} (h : p.encode x = p.encode y) : Same J x y :=
  equal_codes_same_answers hp h

theorem different_realization_forces_distinction {J : Join F} {p : Account F C}
    (hp : Exact (target J) p) {x y : F} {c : Context F}
    (yes : Possible J c x) (no : ¬ Possible J c y) : p.encode x ≠ p.encode y :=
  fun eq => no ((exact_same_code hp eq c).mp yes)

theorem operation_domain_exact {J : Join F} {p : Account F C}
    (hp : Exact (target J) p) (x y : F) :
    (∃ c, Operation J p (p.encode x) (p.encode y) c) ↔ Composable J x y := by
  constructor
  · rintro ⟨c, a, b, z, ha, hb, _, hj⟩
    exact (same_preserves_joinability (exact_same_code hp ha) (exact_same_code hp hb)).mp ⟨z, hj⟩
  · rintro ⟨z, hz⟩
    exact ⟨p.encode z, x, y, z, rfl, rfl, rfl, hz⟩

theorem operation_on_realized_result {J : Join F} (hf : Functional J) {p : Account F C}
    (hp : Exact (target J) p) (rp : Reduced (target J) p)
    {x y z : F} (hz : J x y z) (c : C) :
    Operation J p (p.encode x) (p.encode y) c ↔ p.encode z = c := by
  constructor
  · rintro ⟨a, b, d, ha, hb, hd, hj⟩
    have h := same_join_results hf (exact_same_code hp ha) (exact_same_code hp hb) hj hz
    exact (rp d z h).symm.trans hd
  · intro eq
    exact ⟨x, y, z, rfl, rfl, eq, hz⟩

theorem operation_functional {J : Join F} (hf : Functional J) {p : Account F C}
    (hp : Exact (target J) p) (rp : Reduced (target J) p) : Functional (Operation J p) := by
  rintro a b c d ⟨x, y, z, hx, hy, hz, hj⟩ hd
  subst a; subst b
  exact hz.symm.trans ((operation_on_realized_result hf hp rp hj d).mp hd)

def canonical (J : Join F) : Account F (Context F → Prop) where
  encode := target J
  read c q := c q

theorem canonical_exact (J : Join F) : Exact (target J) (canonical J) := fun _ _ => Iff.rfl

theorem canonical_reduced (J : Join F) : Reduced (target J) (canonical J) := by
  intro x y h
  funext c
  exact propext (h c)

/-- No minimality requirement on the source account. No onto assumption on
its ambient code type; only codes of the very same activity are relevant. -/
theorem every_exact_account_has_canonical_factor {J : Join F} {p : Account F C}
    (hp : Exact (target J) p) :
    (∀ c, Used p c → ∃ d, Used (canonical J) d ∧ Matches p (canonical J) c d ∧
      ∀ e, Matches p (canonical J) c e → e = d) ∧
    (∀ d, Used (canonical J) d → ∃ c, Used p c ∧ Matches p (canonical J) c d) := by
  constructor
  · intro c hc
    obtain ⟨d, hd, hm⟩ := matches_total_on_used p (canonical J) hc
    exact ⟨d, hd, hm, fun e he => matches_functional hp (canonical_reduced J) he hm⟩
  · rintro d ⟨x, hx⟩
    exact ⟨p.encode x, ⟨x, rfl⟩, x, rfl, hx⟩

theorem aligned_matching_transports_operation {J : Join F}
    {p : Account F C} {r : Account F D}
    (hp : Exact (target J) p) (rr : Reduced (target J) r)
    {a b c : C} {a' b' c' : D}
    (ha : Matches p r a a') (hb : Matches p r b b') (hc : Matches p r c c')
    (h : Operation J p a b c) : Operation J r a' b' c' := by
  obtain ⟨x, y, z, hx, hy, hz, hj⟩ := h
  exact ⟨x, y, z, matches_functional hp rr ⟨x, hx, rfl⟩ ha,
    matches_functional hp rr ⟨y, hy, rfl⟩ hb,
    matches_functional hp rr ⟨z, hz, rfl⟩ hc, hj⟩

theorem aligned_matching_preserves_operation {J : Join F}
    {p : Account F C} {r : Account F D}
    (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (hr : Exact (target J) r) (rr : Reduced (target J) r)
    {a b c : C} {a' b' c' : D}
    (ha : Matches p r a a') (hb : Matches p r b b') (hc : Matches p r c c') :
    Operation J p a b c ↔ Operation J r a' b' c' := by
  have swap : ∀ {x : C} {y : D}, Matches p r x y → Matches r p y x := by
    rintro x y ⟨m, hx, hy⟩
    exact ⟨m, hy, hx⟩
  exact ⟨aligned_matching_transports_operation hp rr ha hb hc,
    aligned_matching_transports_operation hr rp (swap ha) (swap hb) (swap hc)⟩

/-- The operation is derived from the same J, and the comparison preserves it
without assuming a separately supplied homomorphism between the accounts. -/
theorem unique_common_operational_structure {J : Join F} (hf : Functional J)
    {p : Account F C} {r : Account F D}
    (hp : Exact (target J) p) (rp : Reduced (target J) p)
    (hr : Exact (target J) r) (rr : Reduced (target J) r) :
    Functional (Operation J p) ∧ Functional (Operation J r) ∧
    (∀ a, Used p a → ∃ b, Matches p r a b ∧ ∀ c, Matches p r a c → c = b) ∧
    (∀ b, Used r b → ∃ a, Matches p r a b ∧ ∀ c, Matches p r c b → c = a) ∧
    (∀ a b c a' b' c', Matches p r a a' → Matches p r b b' → Matches p r c c' →
      (Operation J p a b c ↔ Operation J r a' b' c')) := by
  have old := relative_unique_correspondence hp rp hr rr
  exact ⟨operation_functional hf hp rp, operation_functional hf hr rr,
    old.1, old.2, fun _ _ _ _ _ _ ha hb hc => aligned_matching_preserves_operation hp rp hr rr ha hb hc⟩

end Generative.ExplanatoryContextualStructure

#print axioms Generative.ExplanatoryContextualStructure.exact_same_code
#print axioms Generative.ExplanatoryContextualStructure.different_realization_forces_distinction
#print axioms Generative.ExplanatoryContextualStructure.operation_domain_exact
#print axioms Generative.ExplanatoryContextualStructure.operation_on_realized_result
#print axioms Generative.ExplanatoryContextualStructure.operation_functional
#print axioms Generative.ExplanatoryContextualStructure.canonical_exact
#print axioms Generative.ExplanatoryContextualStructure.canonical_reduced
#print axioms Generative.ExplanatoryContextualStructure.every_exact_account_has_canonical_factor
#print axioms Generative.ExplanatoryContextualStructure.aligned_matching_transports_operation
#print axioms Generative.ExplanatoryContextualStructure.aligned_matching_preserves_operation
#print axioms Generative.ExplanatoryContextualStructure.unique_common_operational_structure
