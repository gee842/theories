import Std

/-
Practical judgment, 8 October 2026. Local analytical roles within one history.
The normative interpretation of protection priority, selection and allocation is
supplied explicitly in PRACTICAL-JUDGMENT.md, not proved by these definitions.
Predicates retain indexed claims; no additive welfare measure is assumed.
-/
namespace PracticalJudgment

def Included {I : Type} (a b : I → Prop) : Prop := ∀ i, a i → b i

def StrictIncluded {I : Type} (a b : I → Prop) : Prop :=
  Included a b ∧ ¬ Included b a

theorem included_trans {I : Type} {a b c : I → Prop}
    (hab : Included a b) (hbc : Included b c) : Included a c :=
  fun i hi => hbc i (hab i hi)

theorem strict_included_irrefl {I : Type} (a : I → Prop) :
    ¬ StrictIncluded a a := fun h => h.2 h.1

theorem strict_included_trans {I : Type} {a b c : I → Prop}
    (hab : StrictIncluded a b) (hbc : StrictIncluded b c) : StrictIncluded a c :=
  ⟨included_trans hab.1 hbc.1, fun hca => hab.2 (included_trans hbc.1 hca)⟩

/-- a is better than b. Protection improvement has priority over secondary gains;
the philosophical scope restriction is substantive, not certified by this type. -/
def Better {H C G : Type} (protect : H → C → Prop) (gain : H → G → Prop)
    (a b : H) : Prop :=
  StrictIncluded (protect b) (protect a) ∨
    (Included (protect b) (protect a) ∧ Included (protect a) (protect b) ∧
      StrictIncluded (gain b) (gain a))

theorem better_irrefl {H C G : Type} (p : H → C → Prop) (g : H → G → Prop)
    (a : H) : ¬ Better p g a a := by
  intro h
  rcases h with h | h
  · exact strict_included_irrefl _ h
  · exact strict_included_irrefl _ h.2.2

theorem better_trans {H C G : Type} (p : H → C → Prop) (g : H → G → Prop)
    {a b c : H} (hab : Better p g a b) (hbc : Better p g b c) : Better p g a c := by
  rcases hab with hab | hab <;> rcases hbc with hbc | hbc
  · exact Or.inl (strict_included_trans hbc hab)
  · exact Or.inl ⟨included_trans hbc.1 hab.1,
      fun hac => hab.2 (included_trans hac hbc.1)⟩
  · exact Or.inl ⟨included_trans hbc.1 hab.1,
      fun hac => hbc.2 (included_trans hab.1 hac)⟩
  · exact Or.inr ⟨included_trans hbc.1 hab.1,
      included_trans hab.2.1 hbc.2.1, strict_included_trans hbc.2.2 hab.2.2⟩

theorem protection_anchor {H C G : Type} {p : H → C → Prop} {g : H → G → Prop}
    {a b : H} (retain : Included (p b) (p a))
    (c : C) (restored : p a c) (lost : ¬ p b c) : Better p g a b :=
  Or.inl ⟨retain, fun reverse => lost (reverse c restored)⟩

theorem no_protection_trade_by_count {H C G : Type}
    {p : H → C → Prop} {g : H → G → Prop} {a b : H}
    (c : C) (hb : p b c) (ha : ¬ p a c) : ¬ Better p g a b := by
  intro h
  rcases h with h | h
  · exact ha (h.1 c hb)
  · exact ha (h.1 c hb)

def Frontier {H : Type} (eligible : H → Prop) (better : H → H → Prop)
    (a : H) : Prop := eligible a ∧ ∀ b, eligible b → ¬ better b a

theorem dominated_excluded {H : Type} {e : H → Prop} {r : H → H → Prop}
    {a b : H} (hb : e b) (hba : r b a) : ¬ Frontier e r a :=
  fun h => h.2 b hb hba

/-- Existence uses a finite nonempty actual menu, not an unlimited optimum. -/
theorem finite_frontier {H : Type} (r : H → H → Prop)
    (irr : ∀ a, ¬ r a a) (trans : ∀ {a b c}, r a b → r b c → r a c)
    (xs : List H) (hne : xs ≠ []) : ∃ a, a ∈ xs ∧ ∀ b, b ∈ xs → ¬ r b a := by
  classical
  induction xs with
  | nil => exact False.elim (hne rfl)
  | cons x xs ih =>
    by_cases empty : xs = []
    · subst xs
      refine ⟨x, by simp, ?_⟩
      intro b hb
      simp only [List.mem_cons, List.not_mem_nil, or_false] at hb
      subst b
      exact irr x
    · obtain ⟨a, ha, hmax⟩ := ih empty
      by_cases hxa : r x a
      · refine ⟨x, by simp, ?_⟩
        intro b hb hbx
        rcases List.mem_cons.mp hb with eq | hb
        · subst b
          exact irr x hbx
        · exact hmax b hb (trans hbx hxa)
      · refine ⟨a, List.mem_cons.mpr (Or.inr ha), ?_⟩
        intro b hb
        rcases List.mem_cons.mp hb with eq | hb
        · subst b
          exact hxa
        · exact hmax b hb

/-- Nonempty alternatives are necessary to avoid vacuous universal duties. -/
def Required {H : Type} (admissible : H → Prop) (task : H → Prop) : Prop :=
  (∃ a, admissible a) ∧ ∀ a, admissible a → task a

theorem required_performed {H : Type} {a : H} {ad task : H → Prop}
    (h : Required ad task) (chosen : ad a) : task a := h.2 a chosen

theorem alternative_defeats_specific_duty {H : Type} {ad task : H → Prop}
    {a : H} (ha : ad a) (hnot : ¬ task a) : ¬ Required ad task :=
  fun h => hnot (h.2 a ha)

theorem impossible_menu_no_duty {H : Type} {ad task : H → Prop}
    (empty : ∀ a, ¬ ad a) : ¬ Required ad task := by
  intro h
  obtain ⟨a, ha⟩ := h.1
  exact empty a ha

theorem necessary_means_required {H : Type} {ad target means : H → Prop}
    (h : Required ad target) (law : ∀ a, ad a → target a → means a) :
    Required ad means := ⟨h.1, fun a ha => law a ha (h.2 a ha)⟩

/-- Assignment is part of a jointly feasible plan, not inferred from causation. -/
def Assigned {P A T : Type} (allocation : P → T → A → Prop)
    (p : P) (a : A) (t : T) : Prop := allocation p t a

theorem unique_responder_required {P A T : Type} {ad : P → Prop}
    {allocation : P → T → A → Prop} {a : A} {t : T}
    (inhabited : ∃ p, ad p)
    (coverage : ∀ p, ad p → ∃ b, allocation p t b)
    (unique : ∀ p b, ad p → allocation p t b → b = a) :
    Required ad (fun p => Assigned allocation p a t) := by
  refine ⟨inhabited, ?_⟩
  intro p hp
  obtain ⟨b, hb⟩ := coverage p hp
  have h := unique p b hp hb
  subst b
  exact hb

theorem assignment_respects_capacity {P A T : Type}
    {ad : P → Prop} {allocation : P → T → A → Prop} {capable : P → A → T → Prop}
    (feasible : ∀ p a t, ad p → allocation p t a → capable p a t)
    {p : P} {a : A} {t : T} (hp : ad p) (ha : Assigned allocation p a t) :
    capable p a t := feasible p a t hp ha

/-- Coverage is demand-indexed: absence of a provider during a no-demand gap
does not alone imply failed continuation. -/
def Covered (demand oldSupport newSupport : Nat → Prop) : Prop :=
  ∀ t, demand t → oldSupport t ∨ newSupport t

theorem transfer_requires_actual_successor {d o n : Nat → Prop}
    (covered : Covered d o n) {t : Nat} (needed : d t) (withdrawn : ¬ o t) : n t :=
  (covered t needed).resolve_left withdrawn

theorem no_demand_gap_transfer {d o n : Nat → Prop} (handoff : Nat)
    (before : ∀ t, t < handoff → d t → o t)
    (after : ∀ t, handoff ≤ t → d t → n t) : Covered d o n := by
  intro t ht
  by_cases h : t < handoff
  · exact Or.inl (before t h ht)
  · exact Or.inr (after t (by omega) ht)

theorem uncovered_demand_is_failure {d o n : Nat → Prop} {t : Nat}
    (hd : d t) (ho : ¬ o t) (hn : ¬ n t) : ¬ Covered d o n := by
  intro h
  exact hn (transfer_requires_actual_successor h hd ho)

def Settled {T : Type} (due done released : T → Prop) : Prop :=
  ∀ t, due t → done t ∨ released t

def Residual {T : Type} (due done released : T → Prop) (t : T) : Prop :=
  due t ∧ ¬ done t ∧ ¬ released t

theorem settlement_removes_residual {T : Type} {d f r : T → Prop}
    (h : Settled d f r) (t : T) : ¬ Residual d f r t := by
  intro ht
  exact (h t ht.1).elim ht.2.1 ht.2.2

theorem unfulfilled_unreleased_remains {T : Type} {d f r : T → Prop}
    {t : T} (hd : d t) (hf : ¬ f t) (hr : ¬ r t) : Residual d f r t := ⟨hd,hf,hr⟩

def Robust {W H : Type} (live : W → Prop) (ad : W → H → Prop) (a : H) : Prop :=
  ∀ w, live w → ad w a

theorem robust_at_actual {W H : Type} {live : W → Prop} {ad : W → H → Prop}
    {w : W} {a : H} (truth : live w) (h : Robust live ad a) : ad w a := h w truth

theorem robust_under_refinement {W H : Type} {old new : W → Prop}
    {ad : W → H → Prop} {a : H} (subset : Included new old)
    (h : Robust old ad a) : Robust new ad a := fun w hw => h w (subset w hw)

theorem required_under_faithful_redescription {H K : Type}
    {ad : H → Prop} {ad' : K → Prop} {task : H → Prop} {task' : K → Prop}
    (f : H → K) (forward : ∀ a, ad a → ad' (f a))
    (cover : ∀ b, ad' b → ∃ a, ad a ∧ f a = b)
    (meaning : ∀ a, task a ↔ task' (f a)) (h : Required ad task) :
    Required ad' task' := by
  constructor
  · obtain ⟨a, ha⟩ := h.1
    exact ⟨f a, forward a ha⟩
  · intro b hb
    obtain ⟨a, ha, eq⟩ := cover b hb
    subst b
    exact (meaning a).mp (h.2 a ha)

/-- The ceiling is supplied. This proves no numerical bound from G0. -/
def withinCeiling (limit : Nat) (h : Nat × Nat) (_ : Unit) : Prop := h.1 ≤ limit
def optionalFormation (h : Nat × Nat) (i : Nat) : Prop := i < h.2

theorem supplied_ceiling_bounds_optional_gain (limit amount : Nat) :
    Better (withinCeiling limit) optionalFormation (0, 0) (limit + 1, amount) := by
  apply protection_anchor (c := ())
  · intro _ _
    exact Nat.zero_le limit
  · exact Nat.zero_le limit
  · simp [withinCeiling]

theorem independent_choices_not_joint_capacity :
    (1 ≤ 1 ∧ 1 ≤ 1) ∧ ¬ (1 + 1 ≤ (1 : Nat)) := by omega

/-- Concrete mixed anchor: repair preserves the living basis but loses an event;
celebration realizes that event but loses the basis. Neither loss is erased. -/
def basis (repair : Bool) (_ : Unit) : Prop := repair = true
def event (repair : Bool) (_ : Unit) : Prop := repair = false

theorem mixed_repair_anchor : Better basis event true false := by
  apply protection_anchor (c := ())
  · intro _ h
    cases h
  · rfl
  · intro h
    cases h

theorem repair_retains_real_loss : event false () ∧ ¬ event true () := by
  constructor
  · rfl
  · intro h
    cases h

/-- Competing distinct protected claims stay incomparable, even with equal gains. -/
def protectedOne (a : Bool) (c : Bool) : Prop := a = c
def noGain (_ : Bool) (_ : Unit) : Prop := False

theorem competing_claims_incomparable :
    ¬ Better protectedOne noGain true false ∧
    ¬ Better protectedOne noGain false true := by
  constructor
  · exact no_protection_trade_by_count false rfl (by simp [protectedOne])
  · exact no_protection_trade_by_count true rfl (by simp [protectedOne])

theorem collective_duty_without_individual_duty :
    Required (fun _ : Bool => True) (fun p => p = true ∨ p = false) ∧
    ¬ Required (fun _ : Bool => True) (fun p => p = true) ∧
    ¬ Required (fun _ : Bool => True) (fun p => p = false) := by
  refine ⟨⟨⟨true, True.intro⟩, ?_⟩, ?_, ?_⟩
  · intro p _
    cases p <;> simp
  · exact alternative_defeats_specific_duty (a := false) True.intro (by decide)
  · exact alternative_defeats_specific_duty (a := true) True.intro (by decide)

theorem uncertain_worlds_need_common_plan :
    (∀ w : Bool, ∃ a : Bool, a = w) ∧ ¬ (∃ a : Bool, ∀ w : Bool, a = w) := by
  refine ⟨fun w => ⟨w, rfl⟩, ?_⟩
  rintro ⟨a, h⟩
  have contra : (true : Bool) = false := (h true).symm.trans (h false)
  cases contra

end PracticalJudgment
