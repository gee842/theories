/-!
# Ideals: a history read off its finite stretches

The finite stretches of an unfolding are ordered by extension: `P.le p q` where the stretch `q`
extends `p`. The order is a relation given with the stretches (`Preorder`: reflexive and
transitive; two stretches extending each other are not thereby named equal). A history is read off
its stretches as an **ideal** (`Ideal`): a nonempty set of stretches that holds every stretch one of
its stretches extends, and in which any two stretches are extended by a third. The stretches one
stretch extends are a finite history (`principal`); the stretches of an unending run are an ideal
that no stretch bounds (`Becoming.HistoryIdeals`, where the runs of every process and the words
of moves are the cases). A **class** of ideals is a reading of histories. Ideals with the same
stretches are stated as such (`Ideal.Same`, two inclusions); no extensionality is used.

**What a finite stretch refutes.** Points `x` are read as the ideals `ι x` of their stretches. A
reading of points is refutable where every point outside it has a stretch through which no point
inside passes (`RefutableBy`); a point adheres to a reading where each of its stretches is a stretch
of a point inside (`AdheresBy`). With no premise:
* a refutable reading holds, up to double negation, at every point adhering to it
  (`RefutableBy.not_not`), and a refutable superset so holds at every point adhering to the subset
  (`RefutableBy.adheres_least`); for a stable reading, adhering is holding
  (`RefutableBy.adheres_iff`);
* what adheres is closed: where no point inside passes through a stretch, no point through it
  adheres (`AdheresBy.closed`), so adhering is refutable exactly where every failure to adhere has
  such a stretch (`refutableBy_adheres_iff`).
The laws of `Becoming.Horizon` are the case of the runs of a process read as the ideals of their
stretches (`Becoming.refutable_iff_refutableBy`, `Becoming.adheres_iff_adheresBy`).

**Classes of ideals.** A class is closed where it holds every ideal below one it holds and the union
of every directed family it holds (`ScottClosed`). With no premise:
* a class is closed exactly where it is the class of ideals within a lower set (`closed_iff_lower`);
  the set is then fixed: the stretches whose finite histories the class holds
  (`closed_iff_within_principal`, `lower_unique`), which are its content, the stretches of its
  ideals (`principal_iff_content`, `lower_iff_content`);
* a refutable class holds, up to double negation, every ideal below one it holds and the union of
  every directed family it holds (`Refutable.lower_not_not`, `Refutable.unions_not_not`), so a stable
  refutable class is closed (`Refutable.closed`);
* a closed class is refutable exactly where every ideal outside it has a stretch whose finite
  history the class does not hold (`ScottClosed.refutable_iff`).
Asked of every order and class, each of the two steps is exactly double-negation elimination,
witnessed on the two-element chain (`refutable_closed_iff`, `closed_refutable_iff`). Not being
refuted is not holding; and a history known not to lie within a closed class does not thereby show
the stretch at which it leaves. On the runs of the Boolean sequences, with tests fixed by
prefixes, the second step is Markov's principle (`Becoming.refutable_passes_iff_markov`).

**The hull.** The ideals all of whose stretches are stretches of a class's ideals (`Hull`) are a
closed class that holds the class, lies below every closed class holding it and has the class's
content (`hull_closed`, `Ideals.AdheresBy.of`, `hull_least`, `hull_content`); a closed class with the
first three properties holds exactly the hull's ideals (`hull_unique`). Any two stretches of an
ideal of the hull are extended by one stretch of an ideal of the class (`hull_joint`).

**Avoiding a set of stretches.** The ideals holding no stretch of a set `F` (`Avoids`) are the
ideals within the stretches that extend no stretch of `F` (`avoids_iff_within`): a closed class
(`avoids_closed`), the only closed class holding exactly those finite histories (`avoids_unique`),
and refutable wherever every ideal failing to avoid `F` holds a stretch of it
(`avoids_refutable_of_found`).

**A lower set's own order.** The ideals of the order a set inherits are the ideals within it, when
the set is lower (`Ideal.restrict`, `Ideal.lift`, `lift_within`, `lift_restrict`, `restrict_lift`,
`lift_le_iff`); the empty set has none (`restrict_false_none`).

**The completion.** Ideals ordered by inclusion are directed-complete, the union of a directed
family its supremum (`idealComplete`). A finite history is compact (`principal_compact`); every
ideal is the union of the finite histories below it (`union_principalFamily`); an ideal is compact
exactly where it is a finite history (`compact_iff_principal`). A monotone map of the stretches
into a directed-complete order extends to ideals continuously (`extend_continuous`), agreeing with
it on finite histories (`extend_principal`), and every continuous map agreeing with it there agrees
with the extension everywhere (`extend_unique`, `unique_continuous_extension`). A directed-complete
order with a basis of compact elements that generates it (`CompactBasis`) is the completion of the
basis, by an order equivalence the basis fixes (`CompactBasis.equivalence`,
`unique_basis_representation`); the ideals are their own case (`principal_basis`). Read into
propositions ordered by implication (`implication`), "extends `p`" extends to "holds `p`"
(`extend_above_iff`), and these readings separate ideals (`above_readings_separate`). Equalities
are stated up to the order's equivalence (`Preorder.Equiv`), as ideals are compared by their
stretches.

This module states in the core what `IdealWarrant` and `CompletionRole` (7 October 2026, the
completion package) proved with `Std` and classical reasoning; `Becoming.HistoryIdeals` states
`HistoryIdeals`, and `IdealsCorrespondence` in the completion package reads the three as
instances. No ethical predicate, ranking or axiom occurs; every declaration has an empty axiom
report.
-/

namespace Becoming

namespace Ideals

universe u v w

/-- An order of stretches: `le p q` where `q` extends `p`. Reflexive and transitive. -/
structure Preorder (α : Type u) where
  le : α → α → Prop
  refl : ∀ a, le a a
  trans : ∀ {a b c}, le a b → le b c → le a c

/-- Each below the other. -/
def Preorder.Equiv {α : Type u} (P : Preorder α) (a b : α) : Prop := P.le a b ∧ P.le b a

theorem Preorder.Equiv.refl {α : Type u} (P : Preorder α) (a : α) : P.Equiv a a :=
  ⟨P.refl a, P.refl a⟩

theorem Preorder.Equiv.symm {α : Type u} {P : Preorder α} {a b : α} (e : P.Equiv a b) :
    P.Equiv b a :=
  ⟨e.2, e.1⟩

theorem Preorder.Equiv.trans {α : Type u} {P : Preorder α} {a b c : α} (e : P.Equiv a b)
    (f : P.Equiv b c) : P.Equiv a c :=
  ⟨P.trans e.1 f.1, P.trans f.2 e.2⟩

variable {α : Type u}

/-- An ideal: a nonempty set, closed downward, in which any two elements lie below a third. Read on
stretches, a history read off its finite stretches. -/
structure Ideal (P : Preorder α) where
  mem : α → Prop
  nonempty : ∃ p, mem p
  lower : ∀ {p q}, P.le p q → mem q → mem p
  directed : ∀ {p q}, mem p → mem q → ∃ r, mem r ∧ P.le p r ∧ P.le q r

namespace Ideal

variable {P : Preorder α}

/-- `I` is below `J`: every element of `I` is an element of `J`. -/
def LE (I J : Ideal P) : Prop := ∀ p, I.mem p → J.mem p

/-- Two ideals with the same elements. -/
def Same (I J : Ideal P) : Prop := ∀ p, I.mem p ↔ J.mem p

theorem LE.refl (I : Ideal P) : LE I I := fun _ h => h

theorem LE.trans {I J K : Ideal P} (h : LE I J) (k : LE J K) : LE I K :=
  fun p hp => k p (h p hp)

theorem Same.refl (I : Ideal P) : Same I I := fun _ => Iff.rfl

theorem Same.symm {I J : Ideal P} (h : Same I J) : Same J I := fun p => (h p).symm

theorem Same.trans {I J K : Ideal P} (h : Same I J) (k : Same J K) : Same I K :=
  fun p => (h p).trans (k p)

theorem Same.le {I J : Ideal P} (h : Same I J) : LE I J := fun p => (h p).mp

theorem Same.ge {I J : Ideal P} (h : Same I J) : LE J I := fun p => (h p).mpr

/-- Ideals each below the other have the same elements. -/
theorem same_of_le {I J : Ideal P} (h : LE I J) (k : LE J I) : Same I J := fun p => ⟨h p, k p⟩

end Ideal

/-- Ideals ordered by inclusion; its equivalence is `Ideal.Same`. -/
def idealOrder (P : Preorder α) : Preorder (Ideal P) where
  le := Ideal.LE
  refl := Ideal.LE.refl
  trans := Ideal.LE.trans

theorem idealOrder_equiv_iff {P : Preorder α} {I J : Ideal P} :
    (idealOrder P).Equiv I J ↔ Ideal.Same I J :=
  ⟨fun e => Ideal.same_of_le e.1 e.2, fun h => ⟨h.le, h.ge⟩⟩

/-- The principal ideal of `p`: the elements below it. Read on stretches, a finite history. -/
def principal (P : Preorder α) (p : α) : Ideal P where
  mem q := P.le q p
  nonempty := ⟨p, P.refl p⟩
  lower h k := P.trans h k
  directed hp hq := ⟨p, P.refl p, hp, hq⟩

/-- **A finite history is below an ideal exactly where the ideal holds its last stretch.** -/
theorem principal_le_iff {P : Preorder α} {p : α} {I : Ideal P} :
    Ideal.LE (principal P p) I ↔ I.mem p :=
  ⟨fun h => h p (P.refl p), fun h _ hq => I.lower hq h⟩

/-- A directed set: nonempty, any two of its elements below a third of them. -/
structure Directed (P : Preorder α) (S : α → Prop) : Prop where
  nonempty : ∃ a, S a
  directed : ∀ {a b}, S a → S b → ∃ c, S c ∧ P.le a c ∧ P.le b c

theorem Ideal.directed_mem {P : Preorder α} (I : Ideal P) : Directed P I.mem :=
  ⟨I.nonempty, I.directed⟩

section Unions

variable {P : Preorder α}

/-- The union of a directed family of ideals. -/
def union (D : Ideal P → Prop) (hd : Directed (idealOrder P) D) : Ideal P where
  mem p := ∃ I, D I ∧ I.mem p
  nonempty := match hd.nonempty with
    | ⟨I, hI⟩ => match I.nonempty with
      | ⟨p, hp⟩ => ⟨p, I, hI, hp⟩
  lower hpq := fun ⟨I, hI, hq⟩ => ⟨I, hI, I.lower hpq hq⟩
  directed := fun ⟨_, hI, hp⟩ ⟨_, hJ, hq⟩ =>
    match hd.directed hI hJ with
    | ⟨K, hK, hIK, hJK⟩ => match K.directed (hIK _ hp) (hJK _ hq) with
      | ⟨r, hr, hpr, hqr⟩ => ⟨r, ⟨K, hK, hr⟩, hpr, hqr⟩

theorem le_union (D : Ideal P → Prop) (hd : Directed (idealOrder P) D) {I : Ideal P} (hI : D I) :
    Ideal.LE I (union D hd) :=
  fun _ hp => ⟨I, hI, hp⟩

theorem union_le (D : Ideal P → Prop) (hd : Directed (idealOrder P) D) (J : Ideal P)
    (hJ : ∀ I, D I → Ideal.LE I J) : Ideal.LE (union D hd) J :=
  fun p ⟨I, hI, hp⟩ => hJ I hI p hp

/-- The finite histories below an ideal: the principal ideals of its elements. -/
def principalFamily (I : Ideal P) (J : Ideal P) : Prop :=
  ∃ p, I.mem p ∧ Ideal.Same J (principal P p)

theorem principalFamily_directed (I : Ideal P) : Directed (idealOrder P) (principalFamily I) :=
  ⟨match I.nonempty with | ⟨p, hp⟩ => ⟨principal P p, p, hp, Ideal.Same.refl _⟩,
   fun ⟨_, hp, hJ⟩ ⟨_, hq, hK⟩ => match I.directed hp hq with
     | ⟨r, hr, hpr, hqr⟩ => ⟨principal P r, ⟨r, hr, Ideal.Same.refl _⟩,
         Ideal.LE.trans hJ.le (Ideals.principal_le_iff.mpr hpr),
         Ideal.LE.trans hK.le (Ideals.principal_le_iff.mpr hqr)⟩⟩

/-- **Every ideal is the union of the finite histories below it.** -/
theorem union_principalFamily (I : Ideal P) :
    Ideal.Same (union (principalFamily I) (principalFamily_directed I)) I :=
  fun p => ⟨fun ⟨_, ⟨_, hq, hJ⟩, hp⟩ => I.lower ((hJ p).mp hp) hq,
            fun hp => ⟨principal P p, ⟨p, hp, Ideal.Same.refl _⟩, P.refl p⟩⟩

end Unions

/-! ## What a finite stretch refutes, for points read as ideals -/

section Points

variable {P : Preorder α} {X : Type v} {ι : X → Ideal P}

/-- A reading `K` of points, each read as the ideal `ι x` of its stretches, is refutable where every
point outside it has a stretch through which no point inside passes. -/
def RefutableBy (ι : X → Ideal P) (K : X → Prop) : Prop :=
  ∀ x, ¬ K x → ∃ p, (ι x).mem p ∧ ∀ y, K y → ¬ (ι y).mem p

/-- A point adheres to a reading where each of its stretches is a stretch of a point inside. -/
def AdheresBy (ι : X → Ideal P) (K : X → Prop) (x : X) : Prop :=
  ∀ p, (ι x).mem p → ∃ y, K y ∧ (ι y).mem p

theorem AdheresBy.of {K : X → Prop} {x : X} (inside : K x) : AdheresBy ι K x :=
  fun _ hp => ⟨x, inside, hp⟩

theorem AdheresBy.mono {K L : X → Prop} {x : X} (sub : ∀ y, K y → L y)
    (adheres : AdheresBy ι K x) : AdheresBy ι L x :=
  fun p hp => match adheres p hp with
    | ⟨y, inside, hy⟩ => ⟨y, sub y inside, hy⟩

/-- Adhering to what adheres is adhering. -/
theorem AdheresBy.adheres {K : X → Prop} {x : X} (adheres : AdheresBy ι (AdheresBy ι K) x) :
    AdheresBy ι K x :=
  fun p hp => match adheres p hp with
    | ⟨_, adheres', hy⟩ => adheres' p hy

/-- **A refutable reading holds, up to double negation, at every point adhering to it.** -/
theorem RefutableBy.not_not {K : X → Prop} {x : X} (refutable : RefutableBy ι K)
    (adheres : AdheresBy ι K x) : ¬ ¬ K x :=
  fun outside => match refutable x outside with
    | ⟨p, hp, blocked⟩ => match adheres p hp with
      | ⟨y, inside, hy⟩ => blocked y inside hy

/-- **Refutable supersets hold where the subset is adhered to**, up to double negation. -/
theorem RefutableBy.adheres_least {K L : X → Prop} {x : X} (refutable : RefutableBy ι L)
    (sub : ∀ y, K y → L y) (adheres : AdheresBy ι K x) : ¬ ¬ L x :=
  refutable.not_not (adheres.mono sub)

/-- **For a stable refutable reading, adhering is holding.** -/
theorem RefutableBy.adheres_iff {K : X → Prop} {x : X} (refutable : RefutableBy ι K)
    (stable : ∀ y, ¬ ¬ K y → K y) : AdheresBy ι K x ↔ K x :=
  ⟨fun adheres => stable x (refutable.not_not adheres), AdheresBy.of⟩

/-- **A point adhering to a reading it lies outside shows the reading is not refutable.** -/
theorem not_refutableBy_of_adheres {K : X → Prop} {x : X} (adheres : AdheresBy ι K x)
    (outside : ¬ K x) : ¬ RefutableBy ι K :=
  fun refutable => refutable.not_not adheres outside

/-- **What adheres to a reading is closed**: where no point inside passes through `p`, no point
through `p` adheres. -/
theorem AdheresBy.closed {K : X → Prop} {p : α} (none_ : ¬ ∃ y, K y ∧ (ι y).mem p) :
    ∀ x, (ι x).mem p → ¬ AdheresBy ι K x :=
  fun _ hp adheres => none_ (adheres p hp)

/-- **Adhering is refutable exactly where every failure to adhere has a stretch** through which no
point inside passes. -/
theorem refutableBy_adheres_iff {K : X → Prop} :
    RefutableBy ι (AdheresBy ι K) ↔
      ∀ x, ¬ AdheresBy ι K x → ∃ p, (ι x).mem p ∧ ¬ ∃ y, K y ∧ (ι y).mem p :=
  ⟨fun refutable x outside => match refutable x outside with
    | ⟨p, hp, blocked⟩ => ⟨p, hp, fun ⟨y, inside, hy⟩ => blocked y (AdheresBy.of inside) hy⟩,
   fun witnessed x outside => match witnessed x outside with
    | ⟨_, hp, none_⟩ => ⟨_, hp, fun y adheres hy => AdheresBy.closed none_ y hy adheres⟩⟩

/-- Readings holding the same points are refutable alike. -/
theorem RefutableBy.congr {K L : X → Prop} (h : ∀ x, K x ↔ L x) :
    RefutableBy ι K ↔ RefutableBy ι L :=
  ⟨fun refutable x outside => match refutable x fun inside => outside ((h x).mp inside) with
    | ⟨p, hp, blocked⟩ => ⟨p, hp, fun y inside => blocked y ((h y).mpr inside)⟩,
   fun refutable x outside => match refutable x fun inside => outside ((h x).mpr inside) with
    | ⟨p, hp, blocked⟩ => ⟨p, hp, fun y inside => blocked y ((h y).mp inside)⟩⟩

end Points

/-! ## Classes of ideals -/

section Classes

variable {P : Preorder α}

/-- A class of ideals is refutable where every ideal outside it has an element that no ideal of the
class holds (`RefutableBy`, each ideal read as itself). -/
def Refutable (C : Ideal P → Prop) : Prop := RefutableBy (fun I => I) C

/-- The content of a class: the elements of its ideals. -/
def Content (C : Ideal P → Prop) (p : α) : Prop := ∃ I, C I ∧ I.mem p

/-- The hull of a class: the ideals each element of which is an element of an ideal of the class
(`AdheresBy`, each ideal read as itself). -/
def Hull (C : Ideal P → Prop) : Ideal P → Prop := AdheresBy (fun I => I) C

/-- A lower set: it holds every element below one it holds. -/
def Lower (P : Preorder α) (Q : α → Prop) : Prop := ∀ {p q}, P.le p q → Q q → Q p

/-- An ideal lies within `Q` where every element of it is in `Q`. -/
def Within (P : Preorder α) (Q : α → Prop) (I : Ideal P) : Prop := ∀ p, I.mem p → Q p

/-- A closed class: it holds every ideal below one it holds, and the union of every directed
family it holds. -/
structure ScottClosed (C : Ideal P → Prop) : Prop where
  lower : ∀ {I J}, C I → Ideal.LE J I → C J
  unions : ∀ (D : Ideal P → Prop) (hd : Directed (idealOrder P) D), (∀ I, D I → C I) →
    C (union D hd)

theorem ScottClosed.same {C : Ideal P → Prop} (hc : ScottClosed C) {I J : Ideal P} (hI : C I)
    (h : Ideal.Same I J) : C J :=
  hc.lower hI h.ge

theorem ScottClosed.principal_of_mem {C : Ideal P → Prop} (hc : ScottClosed C) {I : Ideal P} (hI : C I)
    {p : α} (hp : I.mem p) : C (principal P p) :=
  hc.lower hI (principal_le_iff.mpr hp)

theorem closed_of_iff {C E : Ideal P → Prop} (hc : ScottClosed C) (h : ∀ I, C I ↔ E I) : ScottClosed E :=
  ⟨fun hI hJI => (h _).mp (hc.lower ((h _).mpr hI) hJI),
   fun D hd hD => (h _).mp (hc.unions D hd fun I hI => (h I).mpr (hD I hI))⟩

/-- The ideals within any set are a closed class. -/
theorem within_closed (Q : α → Prop) : ScottClosed (Within P Q) :=
  ⟨fun hI hJI p hp => hI p (hJI p hp), fun _ _ hD p ⟨I, hI, hp⟩ => hD I hI p hp⟩

theorem within_principal_iff {Q : α → Prop} (hq : Lower P Q) {p : α} :
    Within P Q (principal P p) ↔ Q p :=
  ⟨fun h => h p (P.refl p), fun h _ hq' => hq hq' h⟩

/-- **A closed class holds exactly the ideals all of whose finite histories it holds.** -/
theorem closed_iff_within_principal {C : Ideal P → Prop} (hc : ScottClosed C) (I : Ideal P) :
    C I ↔ Within P (fun p => C (principal P p)) I :=
  ⟨fun hI _ hp => hc.principal_of_mem hI hp,
   fun h => hc.same (hc.unions (principalFamily I) (principalFamily_directed I)
       fun _ ⟨p, hp, hJ⟩ => hc.same (h p hp) hJ.symm)
     (union_principalFamily I)⟩

/-- The stretches whose finite histories a closed class holds are a lower set. -/
theorem principal_lower {C : Ideal P → Prop} (hc : ScottClosed C) : Lower P (fun p => C (principal P p)) :=
  fun hpq hq => hc.lower hq (Ideals.principal_le_iff.mpr hpq)

/-- **A class is closed exactly where it is the class of ideals within a lower set.** -/
theorem closed_iff_lower (C : Ideal P → Prop) :
    ScottClosed C ↔ ∃ Q : α → Prop, Lower P Q ∧ ∀ I, C I ↔ Within P Q I :=
  ⟨fun hc => ⟨_, principal_lower hc, closed_iff_within_principal hc⟩,
   fun ⟨_, _, h⟩ => closed_of_iff (within_closed _) fun I => (h I).symm⟩

/-- **The lower set is fixed**: it holds exactly the stretches whose finite histories the class
holds. -/
theorem lower_unique {C : Ideal P → Prop} {Q : α → Prop} (hq : Lower P Q)
    (h : ∀ I, C I ↔ Within P Q I) (p : α) : Q p ↔ C (principal P p) :=
  (within_principal_iff hq).symm.trans (h _).symm

/-- Two lower sets giving one class are the same set. -/
theorem lower_unique_of_two {C : Ideal P → Prop} {Q R : α → Prop} (hq : Lower P Q)
    (hr : Lower P R) (hQ : ∀ I, C I ↔ Within P Q I) (hR : ∀ I, C I ↔ Within P R I) (p : α) :
    Q p ↔ R p :=
  (lower_unique hq hQ p).trans (lower_unique hr hR p).symm

/-- **The finite histories a closed class holds are its content.** -/
theorem principal_iff_content {C : Ideal P → Prop} (hc : ScottClosed C) (p : α) :
    C (principal P p) ↔ Content C p :=
  ⟨fun h => ⟨_, h, P.refl p⟩, fun ⟨_, hI, hp⟩ => hc.principal_of_mem hI hp⟩

theorem lower_iff_content {C : Ideal P → Prop} {Q : α → Prop} (hq : Lower P Q)
    (h : ∀ I, C I ↔ Within P Q I) (p : α) : Q p ↔ Content C p :=
  (lower_unique hq h p).trans (principal_iff_content ((closed_iff_lower C).mpr ⟨Q, hq, h⟩) p)

theorem content_lower (C : Ideal P → Prop) : Lower P (Content C) :=
  fun hpq ⟨I, hI, hq⟩ => ⟨I, hI, I.lower hpq hq⟩

/-! ### Refutable and closed -/

/-- **A refutable class holds every ideal below one it holds, up to double negation.** -/
theorem Refutable.lower_not_not {C : Ideal P → Prop} (refutable : Refutable C) {I J : Ideal P}
    (hI : C I) (hJI : Ideal.LE J I) : ¬ ¬ C J :=
  RefutableBy.not_not refutable fun p hp => ⟨I, hI, hJI p hp⟩

/-- **A refutable class holds the union of a directed family it holds, up to double negation.** -/
theorem Refutable.unions_not_not {C : Ideal P → Prop} (refutable : Refutable C)
    (D : Ideal P → Prop) (hd : Directed (idealOrder P) D) (hD : ∀ I, D I → C I) :
    ¬ ¬ C (union D hd) :=
  RefutableBy.not_not refutable fun _ ⟨I, hI, hp⟩ => ⟨I, hD I hI, hp⟩

/-- **A stable refutable class is closed.** -/
theorem Refutable.closed {C : Ideal P → Prop} (refutable : Refutable C)
    (stable : ∀ I, ¬ ¬ C I → C I) : ScottClosed C :=
  ⟨fun hI hJI => stable _ (refutable.lower_not_not hI hJI),
   fun D hd hD => stable _ (refutable.unions_not_not D hd hD)⟩

/-- **A closed class is refutable exactly where every ideal outside it has an element whose
finite history it does not hold.** -/
theorem ScottClosed.refutable_iff {C : Ideal P → Prop} (hc : ScottClosed C) :
    Refutable C ↔ ∀ I, ¬ C I → ∃ p, I.mem p ∧ ¬ C (principal P p) :=
  ⟨fun refutable I outside => match refutable I outside with
     | ⟨p, hp, blocked⟩ => ⟨p, hp, fun h => blocked _ h (Preorder.refl P p)⟩,
   fun located I outside => match located I outside with
     | ⟨_, hp, notHeld⟩ => ⟨_, hp, fun _ hJ hpJ => notHeld (hc.principal_of_mem hJ hpJ)⟩⟩

/-- The ideals within a lower set are refutable exactly where every ideal not within it has an
element outside it. -/
theorem within_refutable_iff {Q : α → Prop} (hq : Lower P Q) :
    Refutable (Within P Q) ↔ ∀ I, ¬ Within P Q I → ∃ p, I.mem p ∧ ¬ Q p :=
  ((within_closed Q).refutable_iff).trans
    ⟨fun h I outside => match h I outside with
       | ⟨p, hp, n⟩ => ⟨p, hp, fun hQ => n ((within_principal_iff hq).mpr hQ)⟩,
     fun h I outside => match h I outside with
       | ⟨p, hp, n⟩ => ⟨p, hp, fun hW => n ((within_principal_iff hq).mp hW)⟩⟩

/-! ### The empty class -/

theorem within_false {I : Ideal P} : ¬ Within P (fun _ => False) I :=
  fun h => match I.nonempty with | ⟨p, hp⟩ => h p hp

theorem false_refutable : Refutable (fun _ : Ideal P => False) :=
  fun I _ => match I.nonempty with | ⟨p, hp⟩ => ⟨p, hp, fun _ h => h.elim⟩

theorem false_closed : ScottClosed (fun _ : Ideal P => False) :=
  ⟨fun h _ => h, fun _ hd hD => match hd.nonempty with | ⟨I, hI⟩ => hD I hI⟩

theorem content_false (p : α) : ¬ Content (fun _ : Ideal P => False) p :=
  fun ⟨_, h, _⟩ => h

/-! ### The hull -/

theorem hull_iff_within_content {C : Ideal P → Prop} {I : Ideal P} :
    Hull C I ↔ Within P (Content C) I :=
  Iff.rfl

theorem hull_closed (C : Ideal P → Prop) : ScottClosed (Hull C) :=
  closed_of_iff (within_closed (Content C)) fun _ => Iff.rfl

/-- **The hull lies below every closed class holding the class.** -/
theorem hull_least {C E : Ideal P → Prop} (he : ScottClosed E) (sub : ∀ I, C I → E I) {I : Ideal P}
    (hI : Hull C I) : E I :=
  (closed_iff_within_principal he I).mpr fun p hp => match hI p hp with
    | ⟨J, hJ, hpJ⟩ => he.principal_of_mem (sub J hJ) hpJ

/-- **The hull has the class's content.** -/
theorem hull_content (C : Ideal P → Prop) (p : α) : Content (Hull C) p ↔ Content C p :=
  ⟨fun ⟨_, hI, hp⟩ => hI p hp, fun ⟨I, hI, hp⟩ => ⟨I, AdheresBy.of hI, hp⟩⟩

/-- **A closed class holding the class and below every closed class holding it holds exactly the
hull's ideals.** -/
theorem hull_unique {C H : Ideal P → Prop} (hh : ScottClosed H) (contains : ∀ I, C I → H I)
    (least : ∀ E, ScottClosed E → (∀ I, C I → E I) → ∀ I, H I → E I) (I : Ideal P) :
    H I ↔ Hull C I :=
  ⟨least _ (hull_closed C) (fun _ => AdheresBy.of) I, hull_least hh contains⟩

/-- A closed class is its own hull. -/
theorem ScottClosed.hull_iff {C : Ideal P → Prop} (hc : ScottClosed C) (I : Ideal P) : Hull C I ↔ C I :=
  ⟨hull_least hc fun _ h => h, AdheresBy.of⟩

/-- **Any two stretches of an ideal of the hull are extended by one stretch of an ideal of the
class.** -/
theorem hull_joint {C : Ideal P → Prop} {I : Ideal P} (hI : Hull C I) {p q : α} (hp : I.mem p)
    (hq : I.mem q) : ∃ J, C J ∧ ∃ r, J.mem r ∧ P.le p r ∧ P.le q r :=
  match I.directed hp hq with
  | ⟨r, hr, hpr, hqr⟩ => match hI r hr with
    | ⟨J, hJ, hrJ⟩ => ⟨J, hJ, r, hrJ, hpr, hqr⟩

/-! ### Avoiding a set of stretches -/

/-- An ideal avoids `F` where it holds no element of `F`. -/
def Avoids (F : α → Prop) (I : Ideal P) : Prop := ∀ b, F b → ¬ I.mem b

/-- **Avoiding `F` is lying within the elements that are above no element of `F`.** -/
theorem avoids_iff_within (F : α → Prop) (I : Ideal P) :
    Avoids F I ↔ Within P (fun p => ∀ b, F b → ¬ P.le b p) I :=
  ⟨fun h _ hp b hb hbp => h b hb (I.lower hbp hp), fun h b hb hbI => h b hbI b hb (P.refl b)⟩

theorem avoids_closed (F : α → Prop) : ScottClosed (Avoids (P := P) F) :=
  closed_of_iff (within_closed _) fun I => (avoids_iff_within F I).symm

theorem avoids_principal_iff (F : α → Prop) (p : α) :
    Avoids F (principal P p) ↔ ∀ b, F b → ¬ P.le b p :=
  Iff.rfl

/-- **The only closed class holding exactly the finite histories that avoid `F`.** -/
theorem avoids_unique {C : Ideal P → Prop} (hc : ScottClosed C) {F : α → Prop}
    (h : ∀ p, C (principal P p) ↔ ∀ b, F b → ¬ P.le b p) (I : Ideal P) : C I ↔ Avoids F I :=
  (closed_iff_within_principal hc I).trans
    ((Iff.intro (fun hw p hp => (h p).mp (hw p hp)) (fun hw p hp => (h p).mpr (hw p hp))).trans
      (avoids_iff_within F I).symm)

/-- **Avoiding `F` is refutable wherever every ideal failing to avoid it holds an element of it.** -/
theorem avoids_refutable_of_found {F : α → Prop}
    (found : ∀ I : Ideal P, ¬ Avoids F I → ∃ b, F b ∧ I.mem b) : Refutable (Avoids (P := P) F) :=
  fun I outside => match found I outside with
    | ⟨b, hb, hbI⟩ => ⟨b, hbI, fun _ hJ hbJ => hJ b hb hbJ⟩

end Classes

/-! ## Double negation, on the two-element chain -/

/-- The two-element chain: `false` below `true`. -/
def chain : Preorder Bool where
  le a b := a = true → b = true
  refl _ h := h
  trans h k e := k (h e)

/-- The ideal holding `false`, and `true` where `φ` holds. -/
def chain.cut (φ : Prop) : Ideal chain where
  mem b := b = true → φ
  nonempty := ⟨false, fun e => nomatch e⟩
  lower hpq hq e := hq (hpq e)
  directed := fun {p q} hp hq => match p, hp with
    | true, hp => ⟨true, hp, fun _ => rfl, fun _ => rfl⟩
    | false, _ => ⟨q, hq, (fun e => nomatch e), fun e => e⟩

/-- **Asked of every order and class, refutability gives closure exactly under double-negation
elimination.** The witness: on the two-element chain, the class holding the ideals that hold
`true`, and every ideal where `φ` holds, is refutable once `¬ ¬ φ`; closed, it holds the finite
history of `false`, which is `φ`. -/
theorem refutable_closed_iff :
    (∀ (α : Type) (P : Preorder α) (C : Ideal P → Prop), Refutable C → ScottClosed C) ↔
      ∀ φ : Prop, ¬ ¬ φ → φ :=
  ⟨fun law φ notNot =>
    match (law Bool chain (fun J => J.mem true ∨ φ)
        fun _ outside => absurd (fun h => outside (.inr h)) notNot).lower
        (I := principal chain true) (J := principal chain false) (.inl (chain.refl true))
        (Ideals.principal_le_iff.mpr fun e => nomatch e) with
    | .inl atTrue => nomatch (atTrue rfl : false = true)
    | .inr holds => holds,
   fun dne _ _ _ refutable => refutable.closed fun _ => dne _⟩

/-- **Asked of every order and class, closure gives refutability exactly under double-negation
elimination.** The witness: on the two-element chain, the ideals within `false`; the ideal holding
`true` where `φ` holds lies outside them once `¬ ¬ φ`, and a refuting element must be `true`. -/
theorem closed_refutable_iff :
    (∀ (α : Type) (P : Preorder α) (C : Ideal P → Prop), ScottClosed C → Refutable C) ↔
      ∀ φ : Prop, ¬ ¬ φ → φ :=
  ⟨fun law φ notNot =>
    match law Bool chain (Within chain fun b => b = false) (within_closed _) (chain.cut φ)
        (fun within => notNot fun h => nomatch (within true fun _ => h : true = false)) with
    | ⟨true, hp, _⟩ => hp rfl
    | ⟨false, _, blocked⟩ => absurd (Preorder.refl chain false)
        (blocked (principal chain false) fun b hb => match b, hb with
          | false, _ => rfl
          | true, hb => nomatch (hb rfl : false = true)),
   fun dne _ _ _ hc => hc.refutable_iff.mpr fun I outside =>
     dne _ fun none_ => outside ((closed_iff_within_principal hc I).mpr fun p hp =>
       dne _ fun notHeld => none_ ⟨p, hp, notHeld⟩)⟩

/-! ## A lower set's own order -/

section Restrict

variable {P : Preorder α}

/-- The order a set inherits. -/
def Preorder.restrict (P : Preorder α) (Q : α → Prop) : Preorder {p // Q p} where
  le p q := P.le p.val q.val
  refl p := P.refl p.val
  trans h k := P.trans h k

/-- An ideal within `Q`, read in the order `Q` inherits. -/
def Ideal.restrict {Q : α → Prop} (I : Ideal P) (h : Within P Q I) : Ideal (P.restrict Q) where
  mem p := I.mem p.val
  nonempty := match I.nonempty with | ⟨p, hp⟩ => ⟨⟨p, h p hp⟩, hp⟩
  lower hpq hq := I.lower hpq hq
  directed := fun hp hq => match I.directed hp hq with
    | ⟨r, hr, hpr, hqr⟩ => ⟨⟨r, h r hr⟩, hr, hpr, hqr⟩

/-- An ideal of the order a lower set inherits, read in the whole order. -/
def Ideal.lift {Q : α → Prop} (hq : Lower P Q) (J : Ideal (P.restrict Q)) : Ideal P where
  mem p := ∃ hp : Q p, J.mem ⟨p, hp⟩
  nonempty := match J.nonempty with | ⟨p, hp⟩ => ⟨p.val, p.property, hp⟩
  lower := fun {p q} hpq ⟨hq', hj⟩ =>
    ⟨hq hpq hq', J.lower (p := ⟨p, hq hpq hq'⟩) (q := ⟨q, hq'⟩) hpq hj⟩
  directed := fun ⟨_, hjp⟩ ⟨_, hjq⟩ => match J.directed hjp hjq with
    | ⟨r, hr, hpr, hqr⟩ => ⟨r.val, ⟨r.property, hr⟩, hpr, hqr⟩

theorem lift_within {Q : α → Prop} (hq : Lower P Q) (J : Ideal (P.restrict Q)) :
    Within P Q (Ideal.lift hq J) :=
  fun _ ⟨h, _⟩ => h

theorem lift_restrict {Q : α → Prop} (hq : Lower P Q) (I : Ideal P) (h : Within P Q I) :
    Ideal.Same (Ideal.lift hq (I.restrict h)) I :=
  fun p => ⟨fun ⟨_, hp⟩ => hp, fun hp => ⟨h p hp, hp⟩⟩

theorem restrict_lift {Q : α → Prop} (hq : Lower P Q) (J : Ideal (P.restrict Q)) :
    Ideal.Same ((Ideal.lift hq J).restrict (lift_within hq J)) J :=
  fun p => ⟨fun ⟨_, hp⟩ => hp, fun hp => ⟨p.property, hp⟩⟩

theorem lift_le_iff {Q : α → Prop} (hq : Lower P Q) (J K : Ideal (P.restrict Q)) :
    Ideal.LE (Ideal.lift hq J) (Ideal.lift hq K) ↔ Ideal.LE J K :=
  ⟨fun h p hp => match h p.val ⟨p.property, hp⟩ with | ⟨_, hk⟩ => hk,
   fun h p ⟨hqp, hjp⟩ => ⟨hqp, h ⟨p, hqp⟩ hjp⟩⟩

/-- The empty set's order has no ideal. -/
theorem restrict_false_none (J : Ideal (P.restrict fun _ => False)) : False :=
  match J.nonempty with | ⟨p, _⟩ => p.property

end Restrict

/-! ## The completion -/

section Completion

variable {β : Type v} {γ : Type w}

/-- A directed-complete order: every directed set has a least upper bound, given as an operation. -/
structure DirectedComplete (Q : Preorder β) where
  sup : (S : β → Prop) → Directed Q S → β
  upper : ∀ S h a, S a → Q.le a (sup S h)
  least : ∀ S h b, (∀ a, S a → Q.le a b) → Q.le (sup S h) b

/-- A map keeping the order. -/
def Monotone (P : Preorder α) (Q : Preorder β) (f : α → β) : Prop :=
  ∀ a b, P.le a b → Q.le (f a) (f b)

/-- The image of a set under a map. -/
def Image (f : α → β) (S : α → Prop) : β → Prop := fun b => ∃ a, S a ∧ f a = b

/-- A compact element: below a directed supremum only where below a member of the set. -/
def Compact {Q : Preorder β} (D : DirectedComplete Q) (k : β) : Prop :=
  ∀ S h, Q.le k (D.sup S h) → ∃ a, S a ∧ Q.le k a

theorem image_directed {P : Preorder α} {Q : Preorder β} {f : α → β} (hf : Monotone P Q f)
    {S : α → Prop} (hS : Directed P S) : Directed Q (Image f S) := by
  refine ⟨match hS.nonempty with | ⟨a, ha⟩ => ⟨f a, a, ha, rfl⟩, ?_⟩
  intro a b ha hb
  obtain ⟨x, hx, rfl⟩ := ha
  obtain ⟨y, hy, rfl⟩ := hb
  obtain ⟨z, hz, hxz, hyz⟩ := hS.directed hx hy
  exact ⟨f z, ⟨z, hz, rfl⟩, hf x z hxz, hf y z hyz⟩

theorem sup_congr {Q : Preorder β} (D : DirectedComplete Q) {S T : β → Prop} (hS : Directed Q S)
    (hT : Directed Q T) (h : ∀ a, S a ↔ T a) : Q.Equiv (D.sup S hS) (D.sup T hT) :=
  ⟨D.least S hS _ fun a ha => D.upper T hT a ((h a).mp ha),
   D.least T hT _ fun a ha => D.upper S hS a ((h a).mpr ha)⟩

theorem sup_mono {Q : Preorder β} (D : DirectedComplete Q) {S T : β → Prop} (hS : Directed Q S)
    (hT : Directed Q T) (h : ∀ a, S a → T a) : Q.le (D.sup S hS) (D.sup T hT) :=
  D.least S hS _ fun a ha => D.upper T hT a (h a ha)

/-- A continuous map: monotone, and keeping directed suprema up to the order's equivalence. -/
structure Continuous {P : Preorder α} {Q : Preorder β} (D : DirectedComplete P)
    (E : DirectedComplete Q) (f : α → β) : Prop where
  monotone : Monotone P Q f
  preserves : ∀ S h, Q.Equiv (f (D.sup S h)) (E.sup (Image f S) (image_directed monotone h))

/-- **Ideals are directed-complete**: the union of a directed family is its supremum. -/
def idealComplete (P : Preorder α) : DirectedComplete (idealOrder P) where
  sup S h := union S h
  upper S h _ hI := le_union S h hI
  least S h J hJ := union_le S h J hJ

/-- **A finite history is compact.** -/
theorem principal_compact (P : Preorder α) (p : α) : Compact (idealComplete P) (principal P p) :=
  fun _ _ hp => match hp p (P.refl p) with
    | ⟨I, hI, hpI⟩ => ⟨I, hI, principal_le_iff.mpr hpI⟩

/-- **An ideal is compact exactly where it is a finite history.** -/
theorem compact_iff_principal {P : Preorder α} (I : Ideal P) :
    Compact (idealComplete P) I ↔ ∃ p, Ideal.Same I (principal P p) :=
  ⟨fun hI => match hI (principalFamily I) (principalFamily_directed I) (union_principalFamily I).ge with
    | ⟨_, ⟨p, hp, hJ⟩, hIJ⟩ => ⟨p, Ideal.same_of_le (Ideal.LE.trans hIJ hJ.le) (principal_le_iff.mpr hp)⟩,
   fun ⟨p, hp⟩ S h hI => match principal_compact P p S h (Ideal.LE.trans hp.ge hI) with
    | ⟨J, hJ, hpJ⟩ => ⟨J, hJ, Ideal.LE.trans hp.le hpJ⟩⟩

variable {P : Preorder α} {Q : Preorder β}

/-- The extension of a monotone map to ideals: the supremum of its values on an ideal. -/
def extend (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) (I : Ideal P) : β :=
  D.sup (Image f I.mem) (image_directed hf I.directed_mem)

theorem extend_upper (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) (I : Ideal P)
    (p : α) (hp : I.mem p) : Q.le (f p) (extend D f hf I) :=
  D.upper _ _ _ ⟨p, hp, rfl⟩

theorem extend_least (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) (I : Ideal P)
    (b : β) (hb : ∀ p, I.mem p → Q.le (f p) b) : Q.le (extend D f hf I) b := by
  apply D.least
  intro a ha
  obtain ⟨p, hp, rfl⟩ := ha
  exact hb p hp

theorem extend_monotone (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) :
    Monotone (idealOrder P) Q (extend D f hf) :=
  fun I J h => extend_least D f hf I _ fun p hp => extend_upper D f hf J p (h p hp)

/-- **The extension agrees with the map on finite histories.** -/
theorem extend_principal (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) (p : α) :
    Q.Equiv (extend D f hf (principal P p)) (f p) :=
  ⟨extend_least D f hf _ _ fun q hq => hf q p hq, extend_upper D f hf _ p (P.refl p)⟩

/-- **The extension is continuous.** -/
theorem extend_continuous (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) :
    Continuous (idealComplete P) D (extend D f hf) := by
  refine ⟨extend_monotone D f hf, fun S hS => ⟨?_, ?_⟩⟩
  · apply extend_least
    intro p hp
    obtain ⟨I, hI, hip⟩ := hp
    exact Q.trans (extend_upper D f hf I p hip) (D.upper _ _ _ ⟨I, hI, rfl⟩)
  · apply D.least
    intro b hb
    obtain ⟨I, hI, rfl⟩ := hb
    exact extend_monotone D f hf I _ ((idealComplete P).upper S hS I hI)

/-- **Every continuous map agreeing with the map on finite histories agrees with the extension.** -/
theorem extend_unique (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f)
    (g : Ideal P → β) (hg : Continuous (idealComplete P) D g)
    (he : ∀ p, Q.Equiv (g (principal P p)) (f p)) (I : Ideal P) :
    Q.Equiv (g I) (extend D f hf I) := by
  have hgen := hg.preserves (principalFamily I) (principalFamily_directed I)
  have hI : Q.le (g I) (g (union (principalFamily I) (principalFamily_directed I))) :=
    hg.monotone _ _ (union_principalFamily I).ge
  refine ⟨Q.trans hI (Q.trans hgen.1 ?_),
    extend_least D f hf I _ fun p hp =>
      Q.trans (he p).2 (hg.monotone _ _ (principal_le_iff.mpr hp))⟩
  apply D.least
  intro b hb
  obtain ⟨J, ⟨p, hp, hJ⟩, rfl⟩ := hb
  exact Q.trans (hg.monotone _ _ hJ.le) (Q.trans (he p).1 (extend_upper D f hf I p hp))

/-- **A monotone map extends uniquely to a continuous map of ideals**, up to the order's
equivalence. -/
theorem unique_continuous_extension (D : DirectedComplete Q) (f : α → β) (hf : Monotone P Q f) :
    ∃ g : Ideal P → β, Continuous (idealComplete P) D g ∧
      (∀ p, Q.Equiv (g (principal P p)) (f p)) ∧
      ∀ h, Continuous (idealComplete P) D h → (∀ p, Q.Equiv (h (principal P p)) (f p)) →
        ∀ I, Q.Equiv (h I) (g I) :=
  ⟨extend D f hf, extend_continuous D f hf, extend_principal D f hf,
   fun h hh he I => extend_unique D f hf h hh he I⟩

/-- A basis of compact elements: `e` embeds the order, each `e p` is compact, the elements of the
basis below each `x` are directed, and `x` is below their supremum. -/
structure CompactBasis (P : Preorder α) {Q : Preorder β} (D : DirectedComplete Q) (e : α → β) :
    Prop where
  embedding : ∀ p q, Q.le (e p) (e q) ↔ P.le p q
  compact : ∀ p, Compact D (e p)
  approximants : ∀ x, Directed P (fun p => Q.le (e p) x)
  generates : ∀ x, Q.le x (D.sup (Image e fun p => Q.le (e p) x)
    (image_directed (fun p q h => (embedding p q).mpr h) (approximants x)))

variable {D : DirectedComplete Q} {e : α → β}

theorem CompactBasis.monotone (R : CompactBasis P D e) : Monotone P Q e :=
  fun p q h => (R.embedding p q).mpr h

/-- The ideal of the basis elements below `x`. -/
def CompactBasis.below (R : CompactBasis P D e) (x : β) : Ideal P where
  mem p := Q.le (e p) x
  nonempty := (R.approximants x).nonempty
  lower hpq hqx := Q.trans (R.monotone _ _ hpq) hqx
  directed hp hq := (R.approximants x).directed hp hq

theorem CompactBasis.below_monotone (R : CompactBasis P D e) : Monotone Q (idealOrder P) R.below :=
  fun _ _ h _ hp => Q.trans hp h

theorem CompactBasis.below_extend (R : CompactBasis P D e) (I : Ideal P) :
    Ideal.Same (R.below (extend D e R.monotone I)) I := by
  intro p
  constructor
  · intro hp
    obtain ⟨b, ⟨q, hq, rfl⟩, hpq⟩ := R.compact p _ _ hp
    exact I.lower ((R.embedding p q).mp hpq) hq
  · intro hp
    exact extend_upper D e R.monotone I p hp

theorem CompactBasis.extend_below (R : CompactBasis P D e) (x : β) :
    Q.Equiv (extend D e R.monotone (R.below x)) x :=
  ⟨extend_least D e R.monotone _ x fun _ hp => hp, R.generates x⟩

/-- An equivalence of orders: monotone maps each way whose round trips are equivalent to the
identity. -/
structure OrderEquivalence (P : Preorder α) (Q : Preorder β) where
  forward : α → β
  backward : β → α
  forward_monotone : Monotone P Q forward
  backward_monotone : Monotone Q P backward
  backward_forward : ∀ x, P.Equiv (backward (forward x)) x
  forward_backward : ∀ y, Q.Equiv (forward (backward y)) y

/-- An equivalence of directed-complete orders is continuous. -/
theorem OrderEquivalence.continuous {P : Preorder α} {Q : Preorder β} (D : DirectedComplete P)
    (E : DirectedComplete Q) (F : OrderEquivalence P Q) : Continuous D E F.forward := by
  refine ⟨F.forward_monotone, fun S hS => ⟨?_, E.least _ _ _ ?_⟩⟩
  · have h : P.le (D.sup S hS)
        (F.backward (E.sup (Image F.forward S) (image_directed F.forward_monotone hS))) := by
      apply D.least
      intro a ha
      exact P.trans (F.backward_forward a).2
        (F.backward_monotone _ _ (E.upper _ _ _ ⟨a, ha, rfl⟩))
    exact Q.trans (F.forward_monotone _ _ h) (F.forward_backward _).1
  · intro b hb
    obtain ⟨a, ha, rfl⟩ := hb
    exact F.forward_monotone _ _ (D.upper S hS a ha)

/-- **The completion of a compact basis**: the ideals of the basis, by the extension of `e` and
the ideal of the basis elements below. -/
def CompactBasis.equivalence (R : CompactBasis P D e) : OrderEquivalence (idealOrder P) Q where
  forward := extend D e R.monotone
  backward := R.below
  forward_monotone := extend_monotone D e R.monotone
  backward_monotone := R.below_monotone
  backward_forward I := ⟨(R.below_extend I).le, (R.below_extend I).ge⟩
  forward_backward := R.extend_below

theorem CompactBasis.equivalence_principal (R : CompactBasis P D e) (p : α) :
    Q.Equiv (R.equivalence.forward (principal P p)) (e p) :=
  extend_principal D e R.monotone p

/-- **The basis fixes the equivalence**: every equivalence sending each finite history to its
basis element agrees with it. -/
theorem CompactBasis.equivalence_unique (R : CompactBasis P D e)
    (F : OrderEquivalence (idealOrder P) Q) (hF : ∀ p, Q.Equiv (F.forward (principal P p)) (e p))
    (I : Ideal P) : Q.Equiv (F.forward I) (R.equivalence.forward I) :=
  extend_unique D e R.monotone F.forward (F.continuous (idealComplete P) D) hF I

theorem CompactBasis.equivalence_backward_unique (R : CompactBasis P D e)
    (F : OrderEquivalence (idealOrder P) Q) (hF : ∀ p, Q.Equiv (F.forward (principal P p)) (e p))
    (y : β) : Ideal.Same (F.backward y) (R.equivalence.backward y) :=
  have unique := R.equivalence_unique F hF (F.backward y)
  Ideal.same_of_le
    (Ideal.LE.trans (R.equivalence.backward_forward (F.backward y)).2
      (R.equivalence.backward_monotone _ _ (Q.trans unique.2 (F.forward_backward y).1)))
    (Ideal.LE.trans
      (R.equivalence.backward_monotone _ _ (Q.trans (F.forward_backward y).2 unique.1))
      (R.equivalence.backward_forward (F.backward y)).1)

/-- **The ideals are their own case**: finite histories are a compact basis of the ideals. -/
theorem principal_basis (P : Preorder α) : CompactBasis P (idealComplete P) (principal P) :=
  ⟨fun _ _ => Ideals.principal_le_iff, principal_compact P,
   fun I => ⟨match I.nonempty with | ⟨p, hp⟩ => ⟨p, principal_le_iff.mpr hp⟩,
     fun hp hq => match I.directed (principal_le_iff.mp hp) (principal_le_iff.mp hq) with
       | ⟨r, hr, hpr, hqr⟩ => ⟨r, principal_le_iff.mpr hr, hpr, hqr⟩⟩,
   fun _ p hp => ⟨principal P p, ⟨p, principal_le_iff.mpr hp, rfl⟩, P.refl p⟩⟩

/-- **A directed-complete order with a compact basis that generates it is the completion of the
basis**, by an equivalence the basis fixes in both directions. -/
theorem unique_basis_representation (R : CompactBasis P D e) :
    ∃ F : OrderEquivalence (idealOrder P) Q, (∀ p, Q.Equiv (F.forward (principal P p)) (e p)) ∧
      ∀ G : OrderEquivalence (idealOrder P) Q, (∀ p, Q.Equiv (G.forward (principal P p)) (e p)) →
        (∀ I, Q.Equiv (G.forward I) (F.forward I)) ∧
          ∀ y, Ideal.Same (G.backward y) (F.backward y) :=
  ⟨R.equivalence, R.equivalence_principal,
   fun G hG => ⟨R.equivalence_unique G hG, R.equivalence_backward_unique G hG⟩⟩

end Completion

/-! ## Readings into propositions -/

/-- Propositions ordered by implication; its equivalence is `↔`. -/
def implication : Preorder Prop where
  le p q := p → q
  refl _ h := h
  trans h k x := k (h x)

/-- Propositions are directed-complete: the supremum of a set is that one of them holds. -/
def implicationComplete : DirectedComplete implication where
  sup S _ := ∃ p, S p ∧ p
  upper _ _ p hp ht := ⟨p, hp, ht⟩
  least _ _ _ hb := fun ⟨p, hp, ht⟩ => hb p hp ht

/-- The reading "extends `p`". -/
def above (P : Preorder α) (p : α) : α → Prop := fun q => P.le p q

theorem above_monotone (P : Preorder α) (p : α) : Monotone P implication (above P p) :=
  fun _ _ h hp => P.trans hp h

/-- **"Extends `p`" extends to ideals as "holds `p`".** -/
theorem extend_above_iff (P : Preorder α) (p : α) (I : Ideal P) :
    extend implicationComplete (above P p) (above_monotone P p) I ↔ I.mem p := by
  constructor
  · intro h
    obtain ⟨_, ⟨q, hq, rfl⟩, hpq⟩ := h
    exact I.lower hpq hq
  · intro hp
    exact ⟨above P p p, ⟨p, hp, rfl⟩, P.refl p⟩

/-- **These readings separate ideals.** -/
theorem above_readings_separate {P : Preorder α} (I J : Ideal P)
    (h : ∀ p, extend implicationComplete (above P p) (above_monotone P p) I ↔
      extend implicationComplete (above P p) (above_monotone P p) J) :
    Ideal.Same I J :=
  fun p => (extend_above_iff P p I).symm.trans ((h p).trans (extend_above_iff P p J))

end Ideals

end Becoming
