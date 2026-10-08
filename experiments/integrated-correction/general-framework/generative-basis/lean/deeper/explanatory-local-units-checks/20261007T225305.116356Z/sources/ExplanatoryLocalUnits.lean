import ExplanatoryJoining

/-! Recover boundary roles from a partial ternary composition relation.
Local-unit existence, associativity, functionality and chain completion are
separate hypotheses. The finite budget counterexample separates the last one. -/
namespace Generative.ExplanatoryLocalUnits
universe u v
variable {F : Type u} {G : Type v}

abbrev Join (F : Type u) := F → F → F → Prop

def Composable (J : Join F) (a b : F) : Prop := ∃ c, J a b c

def Functional (J : Join F) : Prop := ∀ a b c d, J a b c → J a b d → c = d

def Associative (J : Join F) : Prop := ∀ a b c d,
  (∃ m, J a b m ∧ J m c d) ↔ (∃ n, J b c n ∧ J a n d)

/-- An element acts neutrally on either side wherever composition exists. -/
def Neutral (J : Join F) (e : F) : Prop :=
  (∀ a c, J e a c → c = a) ∧ (∀ a c, J a e c → c = a)

def LeftUnit (J : Join F) (e a : F) : Prop := Neutral J e ∧ J e a a

def RightUnit (J : Join F) (e a : F) : Prop := Neutral J e ∧ J a e a

def HasUnits (J : Join F) : Prop :=
  (∀ a, ∃ e, LeftUnit J e a) ∧ (∀ a, ∃ e, RightUnit J e a)

def CommonUnit (J : Join F) (a b : F) : Prop :=
  ∃ e, RightUnit J e a ∧ LeftUnit J e b

/-- Adjacent composable pairs extend to a whole three-fragment chain. -/
def ChainComplete (J : Join F) : Prop := ∀ a b c,
  Composable J a b → Composable J b c → ∃ m d, J a b m ∧ J m c d

theorem left_unit_unique {J : Join F} (ha : Associative J) {e f a : F}
    (he : LeftUnit J e a) (hf : LeftUnit J f a) : e = f := by
  obtain ⟨m, hef, _⟩ := (ha e f a a).mpr ⟨a, hf.2, he.2⟩
  exact (hf.1.2 _ _ hef).symm.trans (he.1.1 _ _ hef)

theorem right_unit_unique {J : Join F} (ha : Associative J) {e f a : F}
    (he : RightUnit J e a) (hf : RightUnit J f a) : e = f := by
  obtain ⟨m, hef, _⟩ := (ha a e f a).mp ⟨a, he.2, hf.2⟩
  exact (hf.1.2 _ _ hef).symm.trans (he.1.1 _ _ hef)

theorem neutral_self_composes {J : Join F} (hu : HasUnits J) {e : F}
    (he : Neutral J e) : J e e e := by
  obtain ⟨f, _, hfe⟩ := hu.1 e
  have h := he.2 f e hfe
  subst f
  exact hfe

theorem local_units_exist_uniquely {J : Join F} (ha : Associative J) (hu : HasUnits J) (a : F) :
    (∃ e, LeftUnit J e a ∧ ∀ f, LeftUnit J f a → f = e) ∧
    (∃ e, RightUnit J e a ∧ ∀ f, RightUnit J f a → f = e) := by
  obtain ⟨e, he⟩ := hu.1 a
  obtain ⟨f, hf⟩ := hu.2 a
  exact ⟨⟨e, he, fun _ h => left_unit_unique ha h he⟩,
    ⟨f, hf, fun _ h => right_unit_unique ha h hf⟩⟩

theorem joined_common_unit {J : Join F} (ha : Associative J) (hu : HasUnits J)
    {a b c : F} (h : J a b c) : CommonUnit J a b := by
  obtain ⟨e, he⟩ := hu.2 a
  obtain ⟨m, heb, _⟩ := (ha a e b c).mp ⟨a, he.2, h⟩
  have hm := he.1.1 b m heb
  subst m
  exact ⟨e, he, he.1, heb⟩

theorem composable_common_unit {J : Join F} (ha : Associative J) (hu : HasUnits J)
    {a b : F} (h : Composable J a b) : CommonUnit J a b := by
  obtain ⟨c, hc⟩ := h
  exact joined_common_unit ha hu hc

theorem left_unit_of_product {J : Join F} (ha : Associative J) (hf : Functional J)
    {a b c e : F} (hab : J a b c) (he : LeftUnit J e a) : LeftUnit J e c := by
  obtain ⟨n, habn, henc⟩ := (ha e a b c).mp ⟨a, he.2, hab⟩
  have hn := hf a b n c habn hab
  subst n
  exact ⟨he.1, henc⟩

theorem right_unit_of_product {J : Join F} (ha : Associative J) (hf : Functional J)
    {a b c e : F} (hab : J a b c) (he : RightUnit J e b) : RightUnit J e c := by
  obtain ⟨n, habn, hnec⟩ := (ha a b e c).mpr ⟨b, he.2, hab⟩
  have hn := hf a b n c habn hab
  subst n
  exact ⟨he.1, hnec⟩

theorem common_unit_suffices_when_complete {J : Join F} (hc : ChainComplete J)
    {a b : F} (h : CommonUnit J a b) : Composable J a b := by
  obtain ⟨e, he, hf⟩ := h
  obtain ⟨m, d, ham, hmb⟩ := hc a e b ⟨a, he.2⟩ ⟨b, hf.2⟩
  have hm := he.1.2 a m ham
  subst m
  exact ⟨d, hmb⟩

theorem composable_iff_common_unit {J : Join F} (ha : Associative J) (hu : HasUnits J)
    (hc : ChainComplete J) (a b : F) : Composable J a b ↔ CommonUnit J a b :=
  ⟨composable_common_unit ha hu, common_unit_suffices_when_complete hc⟩

/-- Exact characterization of the extra completion requirement. -/
theorem chain_complete_iff_unit_matching_suffices {J : Join F}
    (ha : Associative J) (hf : Functional J) (hu : HasUnits J) :
    ChainComplete J ↔ ∀ a b, CommonUnit J a b → Composable J a b := by
  constructor
  · intro h a b hab
    exact common_unit_suffices_when_complete h hab
  · intro h a b c hab hbc
    obtain ⟨m, hm⟩ := hab
    obtain ⟨e, heb, hec⟩ := composable_common_unit ha hu hbc
    obtain ⟨d, hd⟩ := h m c ⟨e, right_unit_of_product ha hf hm heb, hec⟩
    exact ⟨m, d, hm, hd⟩

theorem boundary_assignments_unique {J : Join F} (ha : Associative J)
    (left right left' right' : F → F)
    (hl : ∀ a, LeftUnit J (left a) a) (hr : ∀ a, RightUnit J (right a) a)
    (hl' : ∀ a, LeftUnit J (left' a) a) (hr' : ∀ a, RightUnit J (right' a) a) :
    ∀ a, left a = left' a ∧ right a = right' a :=
  fun a => ⟨left_unit_unique ha (hl a) (hl' a), right_unit_unique ha (hr a) (hr' a)⟩

/-- A faithful renaming of the composition graph also preserves its recovered
units; preservation of separately supplied boundary maps is not assumed. -/
theorem neutral_transport {J : Join F} {K : Join G} {f : F → G}
    (hi : ∀ a b, f a = f b → a = b) (hs : ∀ b, ∃ a, f a = b)
    (he : ∀ a b c, J a b c ↔ K (f a) (f b) (f c)) (e : F) :
    Neutral J e ↔ Neutral K (f e) := by
  constructor
  · intro hu
    constructor
    · intro a c h
      obtain ⟨x, rfl⟩ := hs a
      obtain ⟨y, rfl⟩ := hs c
      exact congrArg f (hu.1 x y ((he e x y).mpr h))
    · intro a c h
      obtain ⟨x, rfl⟩ := hs a
      obtain ⟨y, rfl⟩ := hs c
      exact congrArg f (hu.2 x y ((he x e y).mpr h))
  · intro hu
    exact ⟨fun a c h => hi c a (hu.1 _ _ ((he e a c).mp h)),
      fun a c h => hi c a (hu.2 _ _ ((he a e c).mp h))⟩

theorem left_unit_transport {J : Join F} {K : Join G} {f : F → G}
    (hi : ∀ a b, f a = f b → a = b) (hs : ∀ b, ∃ a, f a = b)
    (he : ∀ a b c, J a b c ↔ K (f a) (f b) (f c)) (e a : F) :
    LeftUnit J e a ↔ LeftUnit K (f e) (f a) :=
  ⟨fun h => ⟨(neutral_transport hi hs he e).mp h.1, (he e a a).mp h.2⟩,
   fun h => ⟨(neutral_transport hi hs he e).mpr h.1, (he e a a).mpr h.2⟩⟩

theorem right_unit_transport {J : Join F} {K : Join G} {f : F → G}
    (hi : ∀ a b, f a = f b → a = b) (hs : ∀ b, ∃ a, f a = b)
    (he : ∀ a b c, J a b c ↔ K (f a) (f b) (f c)) (e a : F) :
    RightUnit J e a ↔ RightUnit K (f e) (f a) :=
  ⟨fun h => ⟨(neutral_transport hi hs he e).mp h.1, (he a e a).mp h.2⟩,
   fun h => ⟨(neutral_transport hi hs he e).mpr h.1, (he a e a).mpr h.2⟩⟩

/-- The same one-event budget, now as a genuinely partial composition:
false is empty, true is one event; a second event has no admitted product. -/
def budgetJoin : Join Bool := fun a b c => (a = false ∨ b = false) ∧ c = (a || b)

theorem budget_functional : Functional budgetJoin := by
  intro a b c d hc hd
  exact hc.2.trans hd.2.symm

theorem budget_associative : Associative budgetJoin := by decide

theorem budget_has_units : HasUnits budgetJoin := by decide

theorem budget_matching_does_not_suffice :
    CommonUnit budgetJoin true true ∧ ¬ Composable budgetJoin true true := by decide

theorem budget_not_chain_complete : ¬ ChainComplete budgetJoin := by
  intro hc
  exact budget_matching_does_not_suffice.2
    (common_unit_suffices_when_complete hc budget_matching_does_not_suffice.1)

/-- Instantiation on the admitted finite fragments of the supplied process. -/
open ExplanatoryJoining
variable {S : Type u} {A : Type v}
abbrev Admitted (P : Process S A) := { f : Fragment S A // Valid P f }

def traceJoin (P : Process S A) : Join (Admitted P) := fun f g h => Joined P f.val g.val h.val

def traceIdle (P : Process S A) (s : S) : Admitted P := ⟨idle s, idle_valid P s⟩

theorem trace_join_functional (P : Process S A) : Functional (traceJoin P) := by
  intro a b c d hc hd
  exact Subtype.eq (joined_functional hc hd)

theorem trace_join_associative (P : Process S A) : Associative (traceJoin P) := by
  intro a b c d
  constructor
  · rintro ⟨m, ham, hmd⟩
    obtain ⟨n, hbn, hand⟩ := (joined_associative P a.val b.val c.val d.val).mp ⟨m.val, ham, hmd⟩
    exact ⟨⟨n, joined_valid hbn⟩, hbn, hand⟩
  · rintro ⟨n, hbn, hand⟩
    obtain ⟨m, ham, hmd⟩ := (joined_associative P a.val b.val c.val d.val).mpr ⟨n.val, hbn, hand⟩
    exact ⟨⟨m, joined_valid ham⟩, ham, hmd⟩

theorem trace_idle_neutral (P : Process S A) (s : S) : Neutral (traceJoin P) (traceIdle P s) := by
  constructor
  · intro a c h
    apply Subtype.eq
    have he := h.1.2.2
    change s = a.val.start at he
    have hid := (joined_idle_left a.property).2
    rw [← he] at hid
    exact h.2.symm.trans hid
  · intro a c h
    apply Subtype.eq
    have he := h.1.2.2
    change a.val.finish = s at he
    have hid := (joined_idle_right a.property).2
    rw [he] at hid
    exact h.2.symm.trans hid

theorem trace_has_units (P : Process S A) : HasUnits (traceJoin P) := by
  constructor
  · intro a
    exact ⟨traceIdle P a.val.start, trace_idle_neutral P _, joined_idle_left a.property⟩
  · intro a
    exact ⟨traceIdle P a.val.finish, trace_idle_neutral P _, joined_idle_right a.property⟩

theorem trace_chain_complete (P : Process S A) : ChainComplete (traceJoin P) := by
  intro a b c hab hbc
  obtain ⟨m, hm⟩ := hab
  obtain ⟨n, hn⟩ := hbc
  have hc : Joint P m.val c.val := by
    rw [← hm.2]
    exact joint_chain_left hm.1 hn.1
  exact ⟨m, ⟨merge m.val c.val, joint_merge_valid hc⟩, hm, hc, rfl⟩

theorem trace_left_unit_iff (P : Process S A) (e a : Admitted P) :
    LeftUnit (traceJoin P) e a ↔ e = traceIdle P a.val.start := by
  have hid : LeftUnit (traceJoin P) (traceIdle P a.val.start) a :=
    ⟨trace_idle_neutral P _, joined_idle_left a.property⟩
  exact ⟨fun h => left_unit_unique (trace_join_associative P) h hid, fun h => h ▸ hid⟩

theorem trace_right_unit_iff (P : Process S A) (e a : Admitted P) :
    RightUnit (traceJoin P) e a ↔ e = traceIdle P a.val.finish := by
  have hid : RightUnit (traceJoin P) (traceIdle P a.val.finish) a :=
    ⟨trace_idle_neutral P _, joined_idle_right a.property⟩
  exact ⟨fun h => right_unit_unique (trace_join_associative P) h hid, fun h => h ▸ hid⟩

theorem trace_composable_iff_common_unit (P : Process S A) (a b : Admitted P) :
    Composable (traceJoin P) a b ↔ CommonUnit (traceJoin P) a b :=
  composable_iff_common_unit (trace_join_associative P) (trace_has_units P) (trace_chain_complete P) a b

end Generative.ExplanatoryLocalUnits

#print axioms Generative.ExplanatoryLocalUnits.left_unit_unique
#print axioms Generative.ExplanatoryLocalUnits.right_unit_unique
#print axioms Generative.ExplanatoryLocalUnits.neutral_self_composes
#print axioms Generative.ExplanatoryLocalUnits.local_units_exist_uniquely
#print axioms Generative.ExplanatoryLocalUnits.joined_common_unit
#print axioms Generative.ExplanatoryLocalUnits.composable_common_unit
#print axioms Generative.ExplanatoryLocalUnits.left_unit_of_product
#print axioms Generative.ExplanatoryLocalUnits.right_unit_of_product
#print axioms Generative.ExplanatoryLocalUnits.common_unit_suffices_when_complete
#print axioms Generative.ExplanatoryLocalUnits.composable_iff_common_unit
#print axioms Generative.ExplanatoryLocalUnits.chain_complete_iff_unit_matching_suffices
#print axioms Generative.ExplanatoryLocalUnits.boundary_assignments_unique
#print axioms Generative.ExplanatoryLocalUnits.neutral_transport
#print axioms Generative.ExplanatoryLocalUnits.left_unit_transport
#print axioms Generative.ExplanatoryLocalUnits.right_unit_transport
#print axioms Generative.ExplanatoryLocalUnits.budget_functional
#print axioms Generative.ExplanatoryLocalUnits.budget_associative
#print axioms Generative.ExplanatoryLocalUnits.budget_has_units
#print axioms Generative.ExplanatoryLocalUnits.budget_matching_does_not_suffice
#print axioms Generative.ExplanatoryLocalUnits.budget_not_chain_complete
#print axioms Generative.ExplanatoryLocalUnits.trace_join_functional
#print axioms Generative.ExplanatoryLocalUnits.trace_join_associative
#print axioms Generative.ExplanatoryLocalUnits.trace_idle_neutral
#print axioms Generative.ExplanatoryLocalUnits.trace_has_units
#print axioms Generative.ExplanatoryLocalUnits.trace_chain_complete
#print axioms Generative.ExplanatoryLocalUnits.trace_left_unit_iff
#print axioms Generative.ExplanatoryLocalUnits.trace_right_unit_iff
#print axioms Generative.ExplanatoryLocalUnits.trace_composable_iff_common_unit
