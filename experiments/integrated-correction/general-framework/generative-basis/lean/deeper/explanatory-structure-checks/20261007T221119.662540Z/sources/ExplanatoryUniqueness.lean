import ExplanatoryStructure

/-! Relative uniqueness of reduced exact presentations, not unique ontology.
The query family is fixed independently of the presentation. Every summary
includes its interpretation; no varying decoder is hidden in a code. -/
namespace Generative.ExplanatoryUniqueness
universe u v w x
variable {M : Type u} {Q : Type v} {C : Type w} {D : Type x}

def SameAnswers (target : M → Q → Prop) (m n : M) : Prop :=
  ∀ q, target m q ↔ target n q

structure Presentation (M : Type u) (Q : Type v) (C : Type w) where
  encode : M → C
  read : C → Q → Prop

def Exact (target : M → Q → Prop) (p : Presentation M Q C) : Prop :=
  ∀ m q, p.read (p.encode m) q ↔ target m q

/-- No distinction among encoded models beyond the fixed answers. This is an
additional minimality demand, not part of Exact or of all explanation. -/
def Reduced (target : M → Q → Prop) (p : Presentation M Q C) : Prop :=
  ∀ m n, SameAnswers target m n → p.encode m = p.encode n

def Used (p : Presentation M Q C) (c : C) : Prop := ∃ m, p.encode m = c

def Matches (p : Presentation M Q C) (r : Presentation M Q D) (c : C) (d : D) : Prop :=
  ∃ m, p.encode m = c ∧ r.encode m = d

theorem equal_codes_same_answers {target : M → Q → Prop} {p : Presentation M Q C}
    (hp : Exact target p) {m n : M} (h : p.encode m = p.encode n) : SameAnswers target m n := by
  intro q
  exact (hp m q).symm.trans ((congrArg (fun c => p.read c q) h).to_iff.trans (hp n q))

theorem reduced_exact_kernel {target : M → Q → Prop} {p : Presentation M Q C}
    (hp : Exact target p) (rp : Reduced target p) (m n : M) :
    p.encode m = p.encode n ↔ SameAnswers target m n :=
  ⟨equal_codes_same_answers hp, rp m n⟩

theorem reduced_presentations_same_kernel {target : M → Q → Prop}
    {p : Presentation M Q C} {r : Presentation M Q D}
    (hp : Exact target p) (rp : Reduced target p)
    (hr : Exact target r) (rr : Reduced target r) (m n : M) :
    p.encode m = p.encode n ↔ r.encode m = r.encode n :=
  (reduced_exact_kernel hp rp m n).trans (reduced_exact_kernel hr rr m n).symm

theorem matches_total_on_used (p : Presentation M Q C) (r : Presentation M Q D)
    {c : C} (h : Used p c) : ∃ d, Used r d ∧ Matches p r c d := by
  obtain ⟨m, hm⟩ := h
  exact ⟨r.encode m, ⟨m, rfl⟩, ⟨m, hm, rfl⟩⟩

theorem matches_functional {target : M → Q → Prop}
    {p : Presentation M Q C} {r : Presentation M Q D}
    (hp : Exact target p) (rr : Reduced target r)
    {c : C} {d e : D} (hd : Matches p r c d) (he : Matches p r c e) : d = e := by
  obtain ⟨m, hm, hmd⟩ := hd
  obtain ⟨n, hn, hne⟩ := he
  exact hmd.symm.trans ((rr m n (equal_codes_same_answers hp (hm.trans hn.symm))).trans hne)

theorem matches_inverse_functional {target : M → Q → Prop}
    {p : Presentation M Q C} {r : Presentation M Q D}
    (hr : Exact target r) (rp : Reduced target p)
    {c e : C} {d : D} (hc : Matches p r c d) (he : Matches p r e d) : c = e := by
  obtain ⟨m, hmc, hm⟩ := hc
  obtain ⟨n, hne, hn⟩ := he
  exact hmc.symm.trans ((rp m n (equal_codes_same_answers hr (hm.trans hn.symm))).trans hne)

theorem matches_iff_equal_answers {target : M → Q → Prop}
    {p : Presentation M Q C} {r : Presentation M Q D}
    (hp : Exact target p) (hr : Exact target r) (rr : Reduced target r)
    (c : C) (d : D) : Matches p r c d ↔
      Used p c ∧ Used r d ∧ ∀ q, p.read c q ↔ r.read d q := by
  constructor
  · rintro ⟨m, hm, hn⟩
    subst c; subst d
    exact ⟨⟨m, rfl⟩, ⟨m, rfl⟩, fun q => (hp m q).trans (hr m q).symm⟩
  · rintro ⟨⟨m, hm⟩, ⟨n, hn⟩, he⟩
    subst c; subst d
    have hab : SameAnswers target m n := fun q => (hp m q).symm.trans ((he q).trans (hr n q))
    exact ⟨m, rfl, rr m n hab⟩

/-- Once the aligned encoded cases are fixed, there is only one functional
matching on used source codes. This is relational, with no choice of inverses. -/
theorem unique_matching (p : Presentation M Q C) (r : Presentation M Q D)
    (R : C → D → Prop) (aligned : ∀ m, R (p.encode m) (r.encode m))
    (functional : ∀ c d e, R c d → R c e → d = e)
    {c : C} {d : D} (used : Used p c) : R c d ↔ Matches p r c d := by
  constructor
  · intro h
    obtain ⟨m, hm⟩ := used
    subst c
    exact ⟨m, rfl, functional _ _ _ (aligned m) h⟩
  · rintro ⟨m, hm, hn⟩
    subst c; subst d
    exact aligned m

/-- Explicit exact presentations need not be reduced. -/
def firstTarget (m : Bool × Bool) (_ : Unit) : Prop := m.1 = true

def shortPresentation : Presentation (Bool × Bool) Unit Bool where
  encode := Prod.fst
  read c _ := c = true

def fullPresentation : Presentation (Bool × Bool) Unit (Bool × Bool) where
  encode m := m
  read c _ := c.1 = true

theorem short_exact : Exact firstTarget shortPresentation := fun _ _ => Iff.rfl

theorem full_exact : Exact firstTarget fullPresentation := fun _ _ => Iff.rfl

theorem short_reduced : Reduced firstTarget shortPresentation := by
  intro m n h
  have he := h ()
  cases m with
  | mk a b => cases n with
    | mk c d => cases a <;> cases c
                 · rfl
                 · have bad := he.mpr rfl; cases bad
                 · have bad := he.mp rfl; cases bad
                 · rfl

theorem full_not_reduced : ¬ Reduced firstTarget fullPresentation := by
  intro h
  have bad := h (false, false) (false, true) (fun _ => Iff.rfl)
  have hb : false = true := congrArg Prod.snd bad
  cases hb

/-- Enlarging the target can make previously irrelevant distinctions essential. -/
def bothTarget (m : Bool × Bool) (q : Bool) : Prop := (if q then m.2 else m.1) = true

theorem first_summary_cannot_answer_both :
    ¬ ∃ read : Bool → Bool → Prop, Exact bothTarget ⟨Prod.fst, read⟩ := by
  rintro ⟨read, h⟩
  have he := equal_codes_same_answers h (m := (false, false)) (n := (false, true)) rfl true
  have bad : false = true := he.mpr rfl
  cases bad

/-- A different question can isolate a useful invariant while losing dynamics. -/
open ExplanatoryStructure

theorem balance_does_not_determine_coverability :
    balance chessColor separated = balance chessColor ([] : List Square) ∧
    (∃ ts, Global adjacent [] ts []) ∧ ¬ ∃ ts, Global adjacent separated ts [] :=
  ⟨separated_balanced, ⟨[], True.intro, List.Perm.nil⟩, separated_not_coverable⟩

end Generative.ExplanatoryUniqueness

#print axioms Generative.ExplanatoryUniqueness.equal_codes_same_answers
#print axioms Generative.ExplanatoryUniqueness.reduced_exact_kernel
#print axioms Generative.ExplanatoryUniqueness.reduced_presentations_same_kernel
#print axioms Generative.ExplanatoryUniqueness.matches_total_on_used
#print axioms Generative.ExplanatoryUniqueness.matches_functional
#print axioms Generative.ExplanatoryUniqueness.matches_inverse_functional
#print axioms Generative.ExplanatoryUniqueness.matches_iff_equal_answers
#print axioms Generative.ExplanatoryUniqueness.unique_matching
#print axioms Generative.ExplanatoryUniqueness.short_exact
#print axioms Generative.ExplanatoryUniqueness.full_exact
#print axioms Generative.ExplanatoryUniqueness.short_reduced
#print axioms Generative.ExplanatoryUniqueness.full_not_reduced
#print axioms Generative.ExplanatoryUniqueness.first_summary_cannot_answer_both
#print axioms Generative.ExplanatoryUniqueness.balance_does_not_determine_coverability
