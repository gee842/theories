import Becoming.HistoryIdeals

/-!
# What a finite stretch verifies, and what none can refute

`Becoming.Ideals` and `Becoming.HistoryIdeals` state what a finite stretch refutes: the closed
classes of histories, the hull of a reading, and the double negation between refutable and closed.
Here is the other side, what a finite stretch verifies, and the split of every reading into the part
a finite stretch can refute and a part none can.

**What a finite stretch verifies.** A reading of points, each read as the ideal of its stretches, is
verifiable where every point inside has a stretch through which only points inside pass
(`Ideals.VerifiableBy`); a point lies in the interior of a reading where one of its stretches is
such a stretch (`Ideals.InteriorBy`). The interior holds only points inside, is verifiable, and holds
every verifiable part of the reading (`InteriorBy.holds`, `interiorBy_verifiable`,
`interiorBy_largest`). With no premise:
* refuting is verifying the complement (`refutableBy_iff_compl`): a stretch through which no point
  inside passes is a stretch through which only points outside pass;
* a verifiable reading has a refutable complement where it is stable
  (`VerifiableBy.compl_refutable`); a point adhering to a reading lies outside the interior of its
  complement, and a point in the interior of a reading does not adhere to its complement
  (`AdheresBy.not_interior_compl`, `InteriorBy.not_adheres_compl`).

**Open classes.** A class of ideals is open where it holds every ideal above one it holds and, holding
the union of a directed family, holds a member of it (`Ideals.Open`). With no premise:
* a class is open exactly where it is the class of ideals meeting an upper set of stretches
  (`open_iff_upper`); the set is fixed, the stretches whose finite histories the class holds
  (`open_iff_meets_principal`, `upper_unique`);
* a class is open exactly where it is verifiable (`open_iff_verifiable`), with no premise either
  way: unlike refuting and closure, verifying and openness are one notion constructively;
* so a class is refutable exactly where its complement is open (`refutable_iff_compl_open`), and the
  complement of an open class is closed (`Open.compl_closed`). The step back, from a verifiable class
  to a refutable complement, is, asked of every order and class, exactly double-negation
  elimination, on the two-element chain (`verifiable_compl_refutable_iff`): a history only known not
  to lie outside a verifiable class does not thereby show the stretch that verifies it;
* the open classes hold every union and every finite meet of open classes, the class of every ideal
  and the empty class (`open_exists`, `open_and`, `open_true`, `open_false`); the interior is the
  largest open subclass (`interior_open`, `interior_largest`, `Open.interior_iff`).

**The split of a reading.** Every reading is its hull met with its remainder, the reading's holding
wherever it is adhered to (`Ideals.RemainderBy`, `splitBy`). The remainder is the largest part that
splits the reading so: for every split of a reading into a part holding every point adhering to it
and another part, the other part lies within the remainder (`remainderBy_largest`). Where a point
adheres to the reading, its remainder is the reading (`remainderBy_iff_of_adheres`). And no finite
stretch refutes the remainder (`remainderBy_not_refuted`): through every stretch of a point it is not
that only points outside the remainder pass. That the remainder is met through every stretch holds
up to double negation (`remainderBy_meets_not_not`) and outright where it is decided whether a
point of the reading passes through the stretch (`remainderBy_meets_of_decided`). The disjunctive
remainder, holding or not adhering, is the same split (`splitBy_or`); asked of every process, its
being met through every stretch is exactly excluded middle (`orNotAdheres_dense_iff_em`): separating
what a reading says that a finite stretch can find against from what no stretch can is deciding, at
each stretch, whether the reading can still hold there.

**On runs** (`Becoming`), each law is read on the runs of a process, the runs read as the ideals of
their stretches:
* Horizon's `Verifiable` is verifiability at stretches (`verifiable_iff_verifiableBy`); a run is
  verified in a reading where a stretch of it is a stretch only of runs inside (`Verified`,
  `verified_iff_interiorBy`), the largest verifiable part (`verified_verifiable`,
  `verified_largest`); refuting a reading is verifying its complement
  (`refutable_iff_compl_verifiable`); a run lies in an open class of histories exactly where one of
  its finite histories does (`Stretches.open_runs`), and a reading of runs is verifiable exactly
  where it is the reading of an open class (`Stretches.verifiable_iff_open`), its verifying class
  (`Stretches.verifyingClass`, `Stretches.verifiable_iff_class`); so verifiable readings hold every
  meet of two and every union, and refutable readings every join of two
  (`Stretches.verifiable_and`, `Stretches.verifiable_exists`, `Stretches.refutable_or`,
  `Stretches.verifiable_true_false`), and the runs outside an open class are closed
  (`Stretches.open_compl_adheres`); a class of histories is open exactly where it meets an upper
  set of stretches, its finite histories (`Stretches.open_iff_upper`), and a class whose
  complement is open is refutable at runs (`Stretches.refutable_of_compl_open`); a run verified in
  a reading does not adhere to its complement (`Verified.not_adheres_compl`);
* asked of every process, a verifiable reading has a refutable complement only under Markov's
  principle (`verifiable_compl_refutable_markov`): what a verification must find is a stretch it is
  only known not to miss, as for tests (`refutable_passes_iff_markov`);
* a reading both verifiable and refutable is decided by a finite stretch of each run at which it is
  decided (`decided_at_stretch`);
* the split on runs (`Remainder`, `split`, `remainder_largest`, `remainder_iff_of_adheres`,
  `remainder_not_refuted`, `remainder_meets_not_not`, `remainder_dense_of_decided`, `split_or`,
  `OrNotAdheres.remainder`); a reading is
  closed exactly where its remainder holds at every run (`Stretches.closed_iff_remainder`), and
  dense exactly where its hull does (`Dense`): wholly exposed to finite stretches a reading has an
  empty remainder, and refuted by none its hull is everything;
* **what a finite stretch finds against a reading is exactly what it finds against its hull**
  (`refutes_iff_refutes_hull`), so readings with one hull are refuted by the same stretches
  (`same_hull_same_refutations`): the remainder, added or taken away, changes nothing any finite
  stretch can find;
* a reading is dense where every run adheres to it (`Dense`); a dense reading is refuted by no
  stretch (`Dense.noStretchRefutes`); a refutable reading refuted by no stretch excludes nothing, up
  to double negation (`Refutable.noStretchRefutes_not_not`), and a reading whose remainder is
  refutable holds, up to double negation, wherever it is adhered to
  (`Refutable.remainder_not_not`);
* a practice keeping verdicts within a favoured reading, each verdict fixed by the record so far and
  met through the record's stretch, exists exactly where the favoured reading is dense
  (`insulates_iff_dense`); a refutable favoured reading so kept excludes nothing, up to double
  negation (`Insulates.refutable_not_not`);
* in the process of all Boolean sequences: some move being `true` is verifiable and dense
  (`Sequences.eventually_verifiable`, `Sequences.eventually_dense`); recurrence is dense and neither
  verifiable nor refutable (`Sequences.recurs_dense`, `Sequences.recurs_not_verifiable`): no finite
  record counts for or against it.

**Classical sources.** Open classes of ideals are the Scott-open sets, which are the open sets of the
topology of runs on the runs' histories; verifiable and refutable readings are the open and closed
classes of formal learning theory (Kelly 1996), the split is the decomposition of every property
into a safety and a liveness property (Alpern and Schneider 1985), and the largest liveness part is
the implication from the closure. Classically the hull's complement is open and every class
splits into a closed and a dense class; constructively the closed part and the split are given, and
the density of the remainder is the step of deciding, at each stretch, whether the reading can still
hold there.

No ethical predicate, ranking or axiom occurs; every declaration has an empty axiom report. Which
readings of an actual inquiry are verifiable, refutable or dense depends on the process they are read
on; the laws say what each gives.
-/

namespace Becoming

open Generative

universe u v w

namespace Ideals

variable {α : Type u}

/-! ## What a finite stretch verifies, for points read as ideals -/

section Points

variable {P : Preorder α} {X : Type v} {ι : X → Ideal P}

/-- A reading `K` of points, each read as the ideal `ι x` of its stretches, is verifiable where every
point inside has a stretch through which only points inside pass. -/
def VerifiableBy (ι : X → Ideal P) (K : X → Prop) : Prop :=
  ∀ x, K x → ∃ p, (ι x).mem p ∧ ∀ y, (ι y).mem p → K y

/-- A point lies in the interior of a reading where one of its stretches is a stretch only of points
inside. -/
def InteriorBy (ι : X → Ideal P) (K : X → Prop) (x : X) : Prop :=
  ∃ p, (ι x).mem p ∧ ∀ y, (ι y).mem p → K y

/-- **The interior holds only points inside.** -/
theorem InteriorBy.holds {K : X → Prop} {x : X} (interior : InteriorBy ι K x) : K x :=
  match interior with
  | ⟨_, hp, all⟩ => all x hp

/-- A reading is verifiable exactly where each of its points lies in its interior. -/
theorem verifiableBy_iff_interior {K : X → Prop} :
    VerifiableBy ι K ↔ ∀ x, K x → InteriorBy ι K x :=
  Iff.rfl

/-- **The interior is verifiable.** -/
theorem interiorBy_verifiable (K : X → Prop) : VerifiableBy ι (InteriorBy ι K) :=
  fun _ ⟨p, hp, all⟩ => ⟨p, hp, fun _ hy => ⟨p, hy, all⟩⟩

/-- **The interior holds every verifiable part of the reading.** -/
theorem interiorBy_largest {K L : X → Prop} (verifiable : VerifiableBy ι L)
    (sub : ∀ y, L y → K y) {x : X} (inside : L x) : InteriorBy ι K x :=
  match verifiable x inside with
  | ⟨p, hp, all⟩ => ⟨p, hp, fun y hy => sub y (all y hy)⟩

/-- For a verifiable reading, lying in the interior is holding. -/
theorem VerifiableBy.interior_iff {K : X → Prop} (verifiable : VerifiableBy ι K) {x : X} :
    InteriorBy ι K x ↔ K x :=
  ⟨InteriorBy.holds, verifiable x⟩

/-- **Refuting is verifying the complement**: a stretch through which no point inside passes is a
stretch through which only points outside pass. -/
theorem refutableBy_iff_compl {K : X → Prop} :
    RefutableBy ι K ↔ VerifiableBy ι (fun x => ¬ K x) :=
  ⟨fun refutable x outside => match refutable x outside with
    | ⟨p, hp, blocked⟩ => ⟨p, hp, fun y hy inside => blocked y inside hy⟩,
   fun verifiable x outside => match verifiable x outside with
    | ⟨p, hp, all⟩ => ⟨p, hp, fun y inside hy => all y hy inside⟩⟩

/-- **A stable verifiable reading has a refutable complement.** -/
theorem VerifiableBy.compl_refutable {K : X → Prop} (verifiable : VerifiableBy ι K)
    (stable : ∀ x, ¬ ¬ K x → K x) : RefutableBy ι (fun x => ¬ K x) :=
  fun x notOutside => match verifiable x (stable x notOutside) with
    | ⟨p, hp, all⟩ => ⟨p, hp, fun y outside hy => outside (all y hy)⟩

/-- **A point adhering to a reading lies outside the interior of its complement.** -/
theorem AdheresBy.not_interior_compl {K : X → Prop} {x : X} (adheres : AdheresBy ι K x) :
    ¬ InteriorBy ι (fun y => ¬ K y) x :=
  fun ⟨p, hp, all⟩ => match adheres p hp with
    | ⟨y, inside, hy⟩ => all y hy inside

/-- **A point in the interior of a reading does not adhere to its complement.** -/
theorem InteriorBy.not_adheres_compl {K : X → Prop} {x : X} (interior : InteriorBy ι K x) :
    ¬ AdheresBy ι (fun y => ¬ K y) x :=
  fun adheres => match interior with
    | ⟨p, hp, all⟩ => match adheres p hp with
      | ⟨y, outside, hy⟩ => outside (all y hy)

/-! ### The split of a reading -/

/-- The remainder of a reading: where a point adheres to the reading, the reading holds there. -/
def RemainderBy (ι : X → Ideal P) (K : X → Prop) (x : X) : Prop := AdheresBy ι K x → K x

/-- **Every reading is its hull met with its remainder.** -/
theorem splitBy {K : X → Prop} {x : X} : K x ↔ AdheresBy ι K x ∧ RemainderBy ι K x :=
  ⟨fun inside => ⟨AdheresBy.of inside, fun _ => inside⟩, fun ⟨adheres, rest⟩ => rest adheres⟩

/-- **The remainder is the largest part splitting the reading so**: where a reading is a part `C`
holding every point adhering to it, met with a part `L`, the part `L` lies within the remainder. -/
theorem remainderBy_largest {K C L : X → Prop} (closed : ∀ y, AdheresBy ι C y → C y)
    (split : ∀ y, K y ↔ C y ∧ L y) {x : X} (hL : L x) : RemainderBy ι K x :=
  fun adheres => (split x).mpr
    ⟨closed x (adheres.mono fun y inside => ((split y).mp inside).1), hL⟩

/-- **Where a point adheres to a reading, its remainder is the reading.** -/
theorem remainderBy_iff_of_adheres {K : X → Prop} {x : X} (adheres : AdheresBy ι K x) :
    RemainderBy ι K x ↔ K x :=
  ⟨fun rest => rest adheres, fun inside _ => inside⟩

/-- **No finite stretch refutes the remainder**: through every stretch of a point, it is not that
only points outside the remainder pass. -/
theorem remainderBy_not_refuted {K : X → Prop} {x : X} {p : α} (hp : (ι x).mem p) :
    ¬ ∀ y, (ι y).mem p → ¬ RemainderBy ι K y :=
  fun none_ =>
    have noK : ¬ ∃ y, K y ∧ (ι y).mem p := fun ⟨y, inside, hy⟩ => none_ y hy fun _ => inside
    none_ x hp fun adheres => absurd adheres (AdheresBy.closed noK x hp)

/-- **The remainder is met through every stretch, up to double negation.** -/
theorem remainderBy_meets_not_not {K : X → Prop} {x : X} {p : α} (hp : (ι x).mem p) :
    ¬ ¬ ∃ y, RemainderBy ι K y ∧ (ι y).mem p :=
  fun none_ => remainderBy_not_refuted hp fun y hy rest => none_ ⟨y, rest, hy⟩

/-- **The remainder is met through a stretch where it is decided whether a point of the reading
passes through it.** -/
theorem remainderBy_meets_of_decided {K : X → Prop} {x : X} {p : α} (hp : (ι x).mem p)
    (decided : (∃ y, K y ∧ (ι y).mem p) ∨ ¬ ∃ y, K y ∧ (ι y).mem p) :
    ∃ y, RemainderBy ι K y ∧ (ι y).mem p :=
  match decided with
  | .inl ⟨y, inside, hy⟩ => ⟨y, fun _ => inside, hy⟩
  | .inr noK => ⟨x, fun adheres => absurd adheres (AdheresBy.closed noK x hp), hp⟩

/-- The disjunctive remainder: the reading holds, or the point does not adhere to it. -/
def OrNotAdheresBy (ι : X → Ideal P) (K : X → Prop) (x : X) : Prop := K x ∨ ¬ AdheresBy ι K x

/-- **The disjunctive remainder splits the reading the same way**, and lies within the remainder. -/
theorem splitBy_or {K : X → Prop} {x : X} : K x ↔ AdheresBy ι K x ∧ OrNotAdheresBy ι K x :=
  ⟨fun inside => ⟨AdheresBy.of inside, .inl inside⟩,
   fun ⟨adheres, rest⟩ => match rest with
    | .inl inside => inside
    | .inr notAdheres => absurd adheres notAdheres⟩

theorem OrNotAdheresBy.remainder {K : X → Prop} {x : X} (rest : OrNotAdheresBy ι K x) :
    RemainderBy ι K x :=
  fun adheres => match rest with
    | .inl inside => inside
    | .inr notAdheres => absurd adheres notAdheres

/-- The disjunctive remainder is met through a stretch where it is decided whether a point of the
reading passes through it. -/
theorem orNotAdheresBy_meets_of_decided {K : X → Prop} {x : X} {p : α} (hp : (ι x).mem p)
    (decided : (∃ y, K y ∧ (ι y).mem p) ∨ ¬ ∃ y, K y ∧ (ι y).mem p) :
    ∃ y, OrNotAdheresBy ι K y ∧ (ι y).mem p :=
  match decided with
  | .inl ⟨y, inside, hy⟩ => ⟨y, .inl inside, hy⟩
  | .inr noK => ⟨x, .inr (AdheresBy.closed noK x hp), hp⟩

end Points

/-! ## Open classes of ideals -/

section Classes

variable {P : Preorder α}

/-- An upper set: it holds every element above one it holds. -/
def Upper (P : Preorder α) (U : α → Prop) : Prop := ∀ {p q}, P.le p q → U p → U q

/-- An ideal meets `U` where it holds an element of `U`. -/
def Meets (U : α → Prop) (I : Ideal P) : Prop := ∃ p, I.mem p ∧ U p

/-- An open class: it holds every ideal above one it holds, and, holding the union of a directed
family, holds a member of the family. -/
structure Open (C : Ideal P → Prop) : Prop where
  upper : ∀ {I J}, C I → Ideal.LE I J → C J
  inaccessible : ∀ (D : Ideal P → Prop) (hd : Directed (idealOrder P) D), C (union D hd) →
    ∃ I, D I ∧ C I

/-- A class of ideals is verifiable where every ideal of the class has an element that only ideals
of the class hold (`VerifiableBy`, each ideal read as itself). -/
def Verifiable (C : Ideal P → Prop) : Prop := VerifiableBy (fun I => I) C

/-- The interior of a class: the ideals with an element that only ideals of the class hold. -/
def Interior (C : Ideal P → Prop) : Ideal P → Prop := InteriorBy (fun I => I) C

theorem Open.same {C : Ideal P → Prop} (hc : Open C) {I J : Ideal P} (hI : C I)
    (h : Ideal.Same I J) : C J :=
  hc.upper hI h.le

theorem open_of_iff {C E : Ideal P → Prop} (hc : Open C) (h : ∀ I, C I ↔ E I) : Open E :=
  ⟨fun hI hIJ => (h _).mp (hc.upper ((h _).mpr hI) hIJ),
   fun D hd hE => match hc.inaccessible D hd ((h _).mpr hE) with
     | ⟨I, hI, hC⟩ => ⟨I, hI, (h I).mp hC⟩⟩

/-- **The ideals meeting any set are an open class.** -/
theorem meets_open (U : α → Prop) : Open (Meets (P := P) U) :=
  ⟨fun ⟨p, hp, hu⟩ hIJ => ⟨p, hIJ p hp, hu⟩,
   fun _ _ ⟨p, ⟨I, hI, hp⟩, hu⟩ => ⟨I, hI, p, hp, hu⟩⟩

/-- An open class holding an ideal holds the finite history of one of its elements. -/
theorem Open.principal_of_mem {C : Ideal P → Prop} (hc : Open C) {I : Ideal P} (hI : C I) :
    ∃ p, I.mem p ∧ C (principal P p) :=
  match hc.inaccessible (principalFamily I) (principalFamily_directed I)
      (hc.same hI (union_principalFamily I).symm) with
  | ⟨_, ⟨p, hp, hJ⟩, hC⟩ => ⟨p, hp, hc.same hC hJ⟩

/-- **An open class holds exactly the ideals one of whose finite histories it holds.** -/
theorem open_iff_meets_principal {C : Ideal P → Prop} (hc : Open C) (I : Ideal P) :
    C I ↔ Meets (fun p => C (principal P p)) I :=
  ⟨hc.principal_of_mem, fun ⟨_, hp, hC⟩ => hc.upper hC (principal_le_iff.mpr hp)⟩

/-- The stretches whose finite histories an open class holds are an upper set. -/
theorem principal_upper {C : Ideal P → Prop} (hc : Open C) :
    Upper P (fun p => C (principal P p)) :=
  fun hpq hp => hc.upper hp (Ideals.principal_le_iff.mpr hpq)

/-- **A class is open exactly where it is the class of ideals meeting an upper set.** -/
theorem open_iff_upper (C : Ideal P → Prop) :
    Open C ↔ ∃ U : α → Prop, Upper P U ∧ ∀ I, C I ↔ Meets U I :=
  ⟨fun hc => ⟨_, principal_upper hc, open_iff_meets_principal hc⟩,
   fun ⟨_, _, h⟩ => open_of_iff (meets_open _) fun I => (h I).symm⟩

theorem meets_principal_iff {U : α → Prop} (hu : Upper P U) {p : α} :
    Meets U (principal P p) ↔ U p :=
  ⟨fun ⟨_, hq, hU⟩ => hu hq hU, fun h => ⟨p, P.refl p, h⟩⟩

/-- **The upper set is fixed**: it holds exactly the stretches whose finite histories the class
holds. -/
theorem upper_unique {C : Ideal P → Prop} {U : α → Prop} (hu : Upper P U)
    (h : ∀ I, C I ↔ Meets U I) (p : α) : U p ↔ C (principal P p) :=
  (meets_principal_iff hu).symm.trans (h _).symm

/-- **An open class is verifiable.** -/
theorem Open.verifiable {C : Ideal P → Prop} (hc : Open C) : Verifiable C :=
  fun _ hI => match hc.principal_of_mem hI with
    | ⟨p, hp, hC⟩ => ⟨p, hp, fun _ hJ => hc.upper hC (principal_le_iff.mpr hJ)⟩

/-- **A verifiable class is open.** -/
theorem verifiable_open {C : Ideal P → Prop} (verifiable : Verifiable C) : Open C :=
  ⟨fun hI hIJ => match verifiable _ hI with
    | ⟨p, hp, all⟩ => all _ (hIJ p hp),
   fun _ _ hU => match verifiable _ hU with
    | ⟨_, ⟨I, hI, hpI⟩, all⟩ => ⟨I, hI, all I hpI⟩⟩

/-- **A class is open exactly where it is verifiable**, with no premise either way. -/
theorem open_iff_verifiable {C : Ideal P → Prop} : Open C ↔ Verifiable C :=
  ⟨Open.verifiable, verifiable_open⟩

/-- **A class is refutable exactly where its complement is open.** -/
theorem refutable_iff_compl_open {C : Ideal P → Prop} : Refutable C ↔ Open (fun I => ¬ C I) :=
  refutableBy_iff_compl.trans open_iff_verifiable.symm

/-- Avoiding a set is not meeting it. -/
theorem avoids_iff_not_meets (F : α → Prop) (I : Ideal P) : Avoids F I ↔ ¬ Meets F I :=
  ⟨fun h ⟨b, hb, hF⟩ => h b hF hb, fun h b hF hb => h ⟨b, hb, hF⟩⟩

/-- **The complement of an open class is closed.** -/
theorem Open.compl_closed {C : Ideal P → Prop} (hc : Open C) : ScottClosed (fun I => ¬ C I) :=
  closed_of_iff (avoids_closed fun p => C (principal P p)) fun I =>
    (avoids_iff_not_meets _ I).trans
      ⟨fun n hC => n ((open_iff_meets_principal hc I).mp hC),
       fun n m => n ((open_iff_meets_principal hc I).mpr m)⟩

/-- **Asked of every order and class, a verifiable class has a refutable complement exactly under
double-negation elimination.** The witness: on the two-element chain, the ideals holding `true`;
the ideal holding `true` where `φ` holds is not outside them once `¬ ¬ φ`, and the stretch that
would refute the complement must be `true`. -/
theorem verifiable_compl_refutable_iff :
    (∀ (α : Type) (P : Preorder α) (C : Ideal P → Prop),
      Verifiable C → Refutable (fun I => ¬ C I)) ↔ ∀ φ : Prop, ¬ ¬ φ → φ :=
  ⟨fun law φ notNot =>
    match law Bool chain (Meets fun b => b = true) (meets_open _).verifiable (chain.cut φ)
        (fun outside => notNot fun h => outside ⟨true, fun _ => h, rfl⟩) with
    | ⟨true, hp, _⟩ => hp rfl
    | ⟨false, _, blocked⟩ => absurd (Preorder.refl chain false)
        (blocked (principal chain false) fun ⟨_, hb, e⟩ => nomatch (hb e : false = true)),
   fun dne _ _ _ verifiable => VerifiableBy.compl_refutable verifiable fun _ => dne _⟩

/-! ### Unions and meets -/

/-- **Every union of open classes is open.** -/
theorem open_exists {β : Type w} (C : β → Ideal P → Prop) (hc : ∀ i, Open (C i)) :
    Open (fun I => ∃ i, C i I) :=
  ⟨fun ⟨i, hI⟩ hIJ => ⟨i, (hc i).upper hI hIJ⟩,
   fun D hd ⟨i, hU⟩ => match (hc i).inaccessible D hd hU with
     | ⟨I, hI, hC⟩ => ⟨I, hI, i, hC⟩⟩

/-- **The meet of two open classes is open.** -/
theorem open_and {C E : Ideal P → Prop} (hc : Open C) (he : Open E) :
    Open (fun I => C I ∧ E I) :=
  ⟨fun ⟨hC, hE⟩ hIJ => ⟨hc.upper hC hIJ, he.upper hE hIJ⟩,
   fun D hd ⟨hC, hE⟩ => match hc.inaccessible D hd hC, he.inaccessible D hd hE with
    | ⟨_, hI, hCI⟩, ⟨_, hJ, hEJ⟩ => match hd.directed hI hJ with
      | ⟨K, hK, hIK, hJK⟩ => ⟨K, hK, hc.upper hCI hIK, he.upper hEJ hJK⟩⟩

theorem open_true : Open (fun _ : Ideal P => True) :=
  ⟨fun _ _ => trivial, fun _ hd _ => match hd.nonempty with | ⟨I, hI⟩ => ⟨I, hI, trivial⟩⟩

theorem open_false : Open (fun _ : Ideal P => False) :=
  ⟨fun h _ => h, fun _ _ h => h.elim⟩

/-! ### The interior -/

/-- The interior is the class of ideals meeting the stretches that only ideals of the class hold. -/
theorem interior_iff_meets (C : Ideal P → Prop) (I : Ideal P) :
    Interior C I ↔ Meets (fun p => ∀ J : Ideal P, J.mem p → C J) I :=
  Iff.rfl

/-- **The interior is open.** -/
theorem interior_open (C : Ideal P → Prop) : Open (Interior C) :=
  verifiable_open (interiorBy_verifiable C)

/-- **The interior is the largest open subclass.** -/
theorem interior_largest {C E : Ideal P → Prop} (he : Open E) (sub : ∀ I, E I → C I)
    {I : Ideal P} (hI : E I) : Interior C I :=
  interiorBy_largest he.verifiable sub hI

/-- An open class is its own interior. -/
theorem Open.interior_iff {C : Ideal P → Prop} (hc : Open C) (I : Ideal P) :
    Interior C I ↔ C I :=
  VerifiableBy.interior_iff hc.verifiable

end Classes

end Ideals

/-! ## On runs -/

variable {S : Type u} {A : Type v} {P : Process S A}

/-- **A reading of runs is verifiable exactly where it is verifiable at a stretch.** -/
theorem verifiable_iff_verifiableBy {K : Run P → Prop} :
    Verifiable K ↔ Ideals.VerifiableBy Run.stretches K :=
  ⟨fun verifiable r inside => match verifiable r inside with
    | ⟨h, all⟩ => ⟨(r, h), Run.AgreeUpTo.refl r h, fun r' agree => all r' agree⟩,
   fun verifiable r inside => match verifiable r inside with
    | ⟨_, agree, all⟩ => ⟨_, fun r' agree' => all r' (agree.trans agree')⟩⟩

/-- A run is verified in a reading where a stretch of it is a stretch only of runs inside. -/
def Verified (K : Run P → Prop) (r : Run P) : Prop := ∃ h, ∀ r', r.AgreeUpTo h r' → K r'

/-- **Being verified is lying in the interior at the run's stretches.** -/
theorem verified_iff_interiorBy {K : Run P → Prop} {r : Run P} :
    Verified K r ↔ Ideals.InteriorBy Run.stretches K r :=
  ⟨fun ⟨h, all⟩ => ⟨(r, h), Run.AgreeUpTo.refl r h, fun r' agree => all r' agree⟩,
   fun ⟨_, agree, all⟩ => ⟨_, fun r' agree' => all r' (agree.trans agree')⟩⟩

/-- A run verified in a reading lies inside it. -/
theorem Verified.holds {K : Run P → Prop} {r : Run P} (verified : Verified K r) : K r :=
  Ideals.InteriorBy.holds (verified_iff_interiorBy.mp verified)

/-- A reading is verifiable exactly where each of its runs is verified in it. -/
theorem verifiable_iff_verified {K : Run P → Prop} : Verifiable K ↔ ∀ r, K r → Verified K r :=
  verifiable_iff_verifiableBy.trans (Ideals.verifiableBy_iff_interior.trans
    ⟨fun all r inside => verified_iff_interiorBy.mpr (all r inside),
     fun all r inside => verified_iff_interiorBy.mp (all r inside)⟩)

/-- **Being verified is verifiable.** -/
theorem verified_verifiable (K : Run P → Prop) : Verifiable (Verified K) :=
  verifiable_iff_verifiableBy.mpr fun r verified =>
    match Ideals.interiorBy_verifiable K r (verified_iff_interiorBy.mp verified) with
    | ⟨e, he, all⟩ => ⟨e, he, fun r' he' => verified_iff_interiorBy.mpr (all r' he')⟩

/-- **Being verified holds every verifiable part of the reading.** -/
theorem verified_largest {K L : Run P → Prop} (verifiable : Verifiable L) (sub : ∀ r, L r → K r)
    {r : Run P} (inside : L r) : Verified K r :=
  verified_iff_interiorBy.mpr
    (Ideals.interiorBy_largest (verifiable_iff_verifiableBy.mp verifiable) sub inside)

/-- **Refuting a reading of runs is verifying its complement.** -/
theorem refutable_iff_compl_verifiable {K : Run P → Prop} :
    Refutable K ↔ Verifiable (fun r => ¬ K r) :=
  refutable_iff_refutableBy.trans (Ideals.refutableBy_iff_compl.trans verifiable_iff_verifiableBy.symm)

/-- **A stable verifiable reading of runs has a refutable complement.** -/
theorem Verifiable.compl_refutable {K : Run P → Prop} (verifiable : Verifiable K)
    (stable : ∀ r, ¬ ¬ K r → K r) : Refutable (fun r => ¬ K r) :=
  refutable_iff_refutableBy.mpr
    (Ideals.VerifiableBy.compl_refutable (verifiable_iff_verifiableBy.mp verifiable) stable)

/-- **A run adhering to a reading is not verified in its complement.** -/
theorem Adheres.not_verified_compl {K : Run P → Prop} {r : Run P} (adheres : Adheres K r) :
    ¬ Verified (fun r' => ¬ K r') r :=
  fun verified => Ideals.AdheresBy.not_interior_compl (adheres_iff_adheresBy.mp adheres)
    (verified_iff_interiorBy.mp verified)

/-- **A run verified in a reading does not adhere to its complement.** -/
theorem Verified.not_adheres_compl {K : Run P → Prop} {r : Run P} (verified : Verified K r) :
    ¬ Adheres (fun r' => ¬ K r') r :=
  fun adheres => Ideals.InteriorBy.not_adheres_compl (verified_iff_interiorBy.mp verified)
    (adheres_iff_adheresBy.mp adheres)

/-- **A reading both verifiable and refutable is decided by a finite stretch of each run at which it
is decided**: a stretch through which only runs inside pass, or only runs outside. -/
theorem decided_at_stretch {K : Run P → Prop} (verifiable : Verifiable K) (refutable : Refutable K)
    {r : Run P} (decided : K r ∨ ¬ K r) :
    ∃ h, (∀ r', r.AgreeUpTo h r' → K r') ∨ ∀ r', r.AgreeUpTo h r' → ¬ K r' :=
  match decided with
  | .inl inside => match verifiable r inside with
    | ⟨h, all⟩ => ⟨h, .inl all⟩
  | .inr outside => match refutable r outside with
    | ⟨h, blocked⟩ => ⟨h, .inr blocked⟩

/-- **Asked of every process, a verifiable reading has a refutable complement only under Markov's
principle.** The witness: in the process of the Boolean sequences, some move being `true` is
verifiable; a refuting horizon for its complement at a sequence not false throughout bounds a
search for its `true`. -/
theorem verifiable_compl_refutable_markov
    (law : ∀ (S A : Type) (P : Process S A) (K : Run P → Prop),
      Verifiable K → Refutable (fun r => ¬ K r)) : Markov :=
  fun s notFalse =>
    match law Unit Bool (Sequences.process Bool) Sequences.Eventually
        (fun _ ⟨m, hm⟩ => ⟨m + 1, fun _ agree => ⟨m, (agree.2 m (Nat.lt_succ_self m)).symm.trans hm⟩⟩)
        (Sequences.run s)
        (fun never => notFalse fun n => match e : s n with
          | true => absurd ⟨n, e⟩ never
          | false => rfl) with
    | ⟨h, blocked⟩ =>
      match false_below_or_true s h with
      | .inr found => found
      | .inl below => absurd (fun ⟨t, atTrue⟩ =>
          match Nat.lt_or_ge t h with
          | .inl before => nomatch ((if_pos before).symm.trans atTrue).symm.trans (below t before)
          | .inr after => nomatch atTrue.symm.trans (Sequences.splice_after s false after))
          (blocked (Sequences.splice s h false) (Sequences.splice_agree s h false))

/-! ### The split on runs -/

/-- The remainder of a reading of runs: where a run adheres to the reading, the reading holds. -/
def Remainder (K : Run P → Prop) (r : Run P) : Prop := Adheres K r → K r

/-- The remainder is the remainder at the runs' stretches. -/
theorem remainder_iff_remainderBy {K : Run P → Prop} {r : Run P} :
    Remainder K r ↔ Ideals.RemainderBy Run.stretches K r :=
  ⟨fun rest adheres => rest (adheres_iff_adheresBy.mpr adheres),
   fun rest adheres => rest (adheres_iff_adheresBy.mp adheres)⟩

/-- **Every reading of runs is its hull met with its remainder.** -/
theorem split {K : Run P → Prop} {r : Run P} : K r ↔ Adheres K r ∧ Remainder K r :=
  Ideals.splitBy.trans
    ⟨fun ⟨adheres, rest⟩ => ⟨adheres_iff_adheresBy.mpr adheres, remainder_iff_remainderBy.mpr rest⟩,
     fun ⟨adheres, rest⟩ => ⟨adheres_iff_adheresBy.mp adheres, remainder_iff_remainderBy.mp rest⟩⟩

/-- **The remainder is the largest part splitting the reading so**: where a reading is a part
holding every run adhering to it met with another part, that part lies within the remainder. -/
theorem remainder_largest {K C L : Run P → Prop} (closed : ∀ r, Adheres C r → C r)
    (splitInto : ∀ r, K r ↔ C r ∧ L r) {r : Run P} (hL : L r) : Remainder K r :=
  remainder_iff_remainderBy.mpr
    (Ideals.remainderBy_largest (fun r adheres => closed r (adheres_iff_adheresBy.mpr adheres))
      splitInto hL)

/-- **Where a run adheres to a reading, its remainder is the reading.** -/
theorem remainder_iff_of_adheres {K : Run P → Prop} {r : Run P} (adheres : Adheres K r) :
    Remainder K r ↔ K r :=
  remainder_iff_remainderBy.trans
    (Ideals.remainderBy_iff_of_adheres (adheres_iff_adheresBy.mp adheres))

/-- **No finite stretch refutes the remainder.** -/
theorem remainder_not_refuted (K : Run P → Prop) (r : Run P) (h : Nat) :
    ¬ ∀ r', r.AgreeUpTo h r' → ¬ Remainder K r' :=
  fun none_ => Ideals.remainderBy_not_refuted (ι := Run.stretches) (K := K)
    (x := r) (p := (r, h)) (Run.AgreeUpTo.refl r h)
    fun r' agree rest => none_ r' agree (remainder_iff_remainderBy.mpr rest)

/-- **The remainder is met through every stretch, up to double negation.** -/
theorem remainder_meets_not_not (K : Run P → Prop) (r : Run P) (h : Nat) :
    ¬ ¬ ∃ r', Remainder K r' ∧ r.AgreeUpTo h r' :=
  fun none_ => Ideals.remainderBy_meets_not_not (ι := Run.stretches) (K := K) (x := r) (p := (r, h))
    (Run.AgreeUpTo.refl r h) fun ⟨r', rest, agree⟩ => none_ ⟨r', remainder_iff_remainderBy.mpr rest, agree⟩

/-- A reading is dense where every run adheres to it: every finite stretch is a stretch of a run of
the reading. -/
def Dense (K : Run P → Prop) : Prop := ∀ r, Adheres K r

/-- **The remainder is dense where it is decided, at each stretch, whether a run of the reading
passes through it.** -/
theorem remainder_dense_of_decided {K : Run P → Prop}
    (decided : ∀ (r : Run P) (h : Nat), (∃ r', K r' ∧ r.AgreeUpTo h r') ∨
      ¬ ∃ r', K r' ∧ r.AgreeUpTo h r') : Dense (Remainder K) :=
  fun r h =>
    have toStretch : ∀ {r'}, (∃ q, K q ∧ r'.AgreeUpTo h q) → ∃ y, K y ∧ y.stretches.mem (r', h) :=
      fun ⟨q, inside, agree⟩ => ⟨q, inside, agree⟩
    have ofStretch : ∀ {r'}, (∃ y, K y ∧ y.stretches.mem (r', h)) → ∃ q, K q ∧ r'.AgreeUpTo h q :=
      fun ⟨q, inside, agree⟩ => ⟨q, inside, agree⟩
    match Ideals.remainderBy_meets_of_decided (ι := Run.stretches) (K := K)
        (x := r) (p := (r, h)) (Run.AgreeUpTo.refl r h)
        (match decided r h with
          | .inl found => .inl (toStretch found)
          | .inr none_ => .inr fun found => none_ (ofStretch found)) with
    | ⟨r', rest, agree⟩ => ⟨r', remainder_iff_remainderBy.mpr rest, agree⟩

/-- The disjunctive remainder on runs: the reading holds, or the run does not adhere to it. -/
def OrNotAdheres (K : Run P → Prop) (r : Run P) : Prop := K r ∨ ¬ Adheres K r

/-- **The disjunctive remainder splits a reading of runs the same way.** -/
theorem split_or {K : Run P → Prop} {r : Run P} : K r ↔ Adheres K r ∧ OrNotAdheres K r :=
  Ideals.splitBy_or.trans
    ⟨fun ⟨adheres, rest⟩ => ⟨adheres_iff_adheresBy.mpr adheres, match rest with
       | .inl inside => .inl inside
       | .inr notAdheres => .inr fun adheres' => notAdheres (adheres_iff_adheresBy.mp adheres')⟩,
     fun ⟨adheres, rest⟩ => ⟨adheres_iff_adheresBy.mp adheres, match rest with
       | .inl inside => .inl inside
       | .inr notAdheres => .inr fun adheres' => notAdheres (adheres_iff_adheresBy.mpr adheres')⟩⟩

/-- The disjunctive remainder lies within the remainder. -/
theorem OrNotAdheres.remainder {K : Run P → Prop} {r : Run P} (rest : OrNotAdheres K r) :
    Remainder K r :=
  remainder_iff_remainderBy.mpr (Ideals.OrNotAdheresBy.remainder (match rest with
    | .inl inside => .inl inside
    | .inr notAdheres => .inr fun adheres => notAdheres (adheres_iff_adheresBy.mpr adheres)))

/-- **Asked of every process and reading, the disjunctive remainder is dense exactly under excluded
middle.** Separating what a reading says that a finite stretch can find against from what no
stretch can is deciding, at each stretch, whether the reading can still hold there. The witness,
on the process of `()`s: the reading of a proposition `φ` at every run; its disjunctive remainder
at the one run is `φ ∨ ¬ φ`. -/
theorem orNotAdheres_dense_iff_em :
    (∀ (S A : Type) (P : Process S A) (K : Run P → Prop), Dense (OrNotAdheres K)) ↔
      ∀ φ : Prop, φ ∨ ¬ φ :=
  ⟨fun law φ => match law Unit Unit (Sequences.process Unit) (fun _ => φ)
        Stretches.unitRun 0 with
    | ⟨_, .inl holds, _⟩ => .inl holds
    | ⟨_, .inr notAdheres, _⟩ => .inr fun holds => notAdheres (Adheres.of holds),
   fun em _ _ _ K r h => match em (∃ r', K r' ∧ r.AgreeUpTo h r') with
    | .inl ⟨r', inside, agree⟩ => ⟨r', .inl inside, agree⟩
    | .inr none_ =>
      match Ideals.orNotAdheresBy_meets_of_decided (ι := Run.stretches) (K := K)
          (x := r) (p := (r, h)) (Run.AgreeUpTo.refl r h)
          (.inr fun ⟨q, inside, agree⟩ => none_ ⟨q, inside, agree⟩) with
      | ⟨r', .inl inside, agree⟩ => ⟨r', .inl inside, agree⟩
      | ⟨r', .inr notAdheres, agree⟩ => ⟨r', .inr fun adheres =>
          notAdheres (adheres_iff_adheresBy.mp adheres), agree⟩⟩

/-! ### What a finite stretch finds against a reading -/

/-- **What a finite stretch finds against a reading is exactly what it finds against its hull**:
only runs outside the reading pass through it exactly where only runs not adhering to it do. -/
theorem refutes_iff_refutes_hull {K : Run P → Prop} {r : Run P} {h : Nat} :
    (∀ r', r.AgreeUpTo h r' → ¬ K r') ↔ ∀ r', r.AgreeUpTo h r' → ¬ Adheres K r' :=
  ⟨fun none_ => Adheres.closed fun ⟨r', inside, agree⟩ => none_ r' agree inside,
   fun none_ r' agree inside => none_ r' agree (Adheres.of inside)⟩

/-- **Readings with one hull are refuted by the same stretches.** -/
theorem same_hull_same_refutations {K K' : Run P → Prop} (same : ∀ r, Adheres K r ↔ Adheres K' r)
    {r : Run P} {h : Nat} :
    (∀ r', r.AgreeUpTo h r' → ¬ K r') ↔ ∀ r', r.AgreeUpTo h r' → ¬ K' r' :=
  refutes_iff_refutes_hull.trans
    ((Iff.intro (fun none_ r' agree adheres => none_ r' agree ((same r').mpr adheres))
      (fun none_ r' agree adheres => none_ r' agree ((same r').mp adheres))).trans
      refutes_iff_refutes_hull.symm)

/-- No finite stretch refutes a reading: through every stretch, it is not that only runs outside
pass. -/
def NoStretchRefutes (K : Run P → Prop) : Prop :=
  ∀ (r : Run P) (h : Nat), ¬ ∀ r', r.AgreeUpTo h r' → ¬ K r'

/-- **A dense reading is refuted by no stretch.** -/
theorem Dense.noStretchRefutes {K : Run P → Prop} (dense : Dense K) : NoStretchRefutes K :=
  fun r h none_ => match dense r h with
    | ⟨r', inside, agree⟩ => none_ r' agree inside

/-- **A refutable reading refuted by no stretch excludes nothing**, up to double negation. -/
theorem Refutable.noStretchRefutes_not_not {K : Run P → Prop} (refutable : Refutable K)
    (unrefuted : NoStretchRefutes K) (r : Run P) : ¬ ¬ K r :=
  fun outside => match refutable r outside with
    | ⟨h, blocked⟩ => unrefuted r h blocked

/-- **A reading whose remainder is refutable holds, up to double negation, wherever it is adhered
to.** -/
theorem Refutable.remainder_not_not {K : Run P → Prop} (refutable : Refutable (Remainder K))
    {r : Run P} (adheres : Adheres K r) : ¬ ¬ K r :=
  fun outside => refutable.noStretchRefutes_not_not (remainder_not_refuted K) r
    fun rest => outside (rest adheres)

/-! ### A practice that keeps a favoured verdict -/

/-- A practice of verdicts: at each horizon of each run, a verdict, a reading of runs. -/
abbrev Practice (P : Process S A) := Nat → Run P → Run P → Prop

/-- The verdict at each horizon is fixed by the record so far: runs agreeing up to the horizon get
verdicts holding the same runs. -/
def ByRecord (V : Practice P) : Prop :=
  ∀ h r r', r.AgreeUpTo h r' → ∀ q, V h r q ↔ V h r' q

/-- A practice insulates a favoured reading `F` where each verdict lies within `F` and is met through
the record's stretch: some run of the verdict agrees with the record so far. -/
def Insulates (V : Practice P) (F : Run P → Prop) : Prop :=
  ∀ r h, (∀ q, V h r q → F q) ∧ ∃ q, V h r q ∧ r.AgreeUpTo h q

/-- **A practice fixed by the record insulates a favoured reading exactly where the reading is
dense.** -/
theorem insulates_iff_dense {F : Run P → Prop} :
    (∃ V : Practice P, ByRecord V ∧ Insulates V F) ↔ Dense F :=
  ⟨fun ⟨_, _, insulates⟩ r h => match (insulates r h).2 with
    | ⟨q, verdict, agree⟩ => ⟨q, (insulates r h).1 q verdict, agree⟩,
   fun dense => ⟨fun _ _ q => F q, fun _ _ _ _ _ => Iff.rfl,
     fun r h => ⟨fun _ inside => inside, dense r h⟩⟩⟩

/-- **A refutable favoured reading kept by an insulating practice excludes nothing**, up to double
negation. -/
theorem Insulates.refutable_not_not {V : Practice P} {F : Run P → Prop} (insulates : Insulates V F)
    (refutable : Refutable F) (r : Run P) : ¬ ¬ F r :=
  refutable.noStretchRefutes_not_not
    (Dense.noStretchRefutes fun r h => match (insulates r h).2 with
      | ⟨q, verdict, agree⟩ => ⟨q, (insulates r h).1 q verdict, agree⟩) r

/-! ### Open classes of histories, at runs -/

namespace Stretches

/-- **A run lies in an open class of histories exactly where one of its finite histories does**:
verifying is finding. -/
theorem open_runs {C : Ideals.Ideal (stretchOrder P) → Prop} (hc : Ideals.Open C) (r : Run P) :
    C r.stretches ↔ ∃ e, r.stretches.mem e ∧ C (Ideals.principal _ e) :=
  Ideals.open_iff_meets_principal hc r.stretches

/-- **A class of histories of a process is open exactly where it is the class meeting an upper set
of stretches**, and that set is the stretches whose finite histories the class holds. -/
theorem open_iff_upper {C : Ideals.Ideal (stretchOrder P) → Prop} :
    Ideals.Open C ↔ ∃ U : Run P × Nat → Prop, Ideals.Upper (stretchOrder P) U ∧
      (∀ I, C I ↔ Ideals.Meets U I) ∧ ∀ e, U e ↔ C (Ideals.principal _ e) :=
  ⟨fun hc => match (Ideals.open_iff_upper C).mp hc with
    | ⟨U, hu, h⟩ => ⟨U, hu, h, Ideals.upper_unique hu h⟩,
   fun ⟨U, hu, h, _⟩ => (Ideals.open_iff_upper C).mpr ⟨U, hu, h⟩⟩

/-- **Where the histories outside a class are an open class, the class is refutable at runs.** -/
theorem refutable_of_compl_open {C : Ideals.Ideal (stretchOrder P) → Prop}
    (hc : Ideals.Open fun I => ¬ C I) : Refutable fun r : Run P => C r.stretches :=
  refutable_of_class (Ideals.refutable_iff_compl_open.mpr hc)

/-- **An open class of histories is verifiable at runs.** -/
theorem verifiable_of_class {C : Ideals.Ideal (stretchOrder P) → Prop} (hc : Ideals.Open C) :
    Verifiable fun r : Run P => C r.stretches :=
  verifiable_iff_verifiableBy.mpr fun r inside => match hc.verifiable r.stretches inside with
    | ⟨e, he, all⟩ => ⟨e, he, fun r' he' => all r'.stretches he'⟩

/-- **A reading of runs is verifiable exactly where it is the reading of an open class of
histories**: the class of histories meeting the stretches through which only runs inside pass. -/
theorem verifiable_iff_open {K : Run P → Prop} :
    Verifiable K ↔ ∃ C : Ideals.Ideal (stretchOrder P) → Prop, Ideals.Open C ∧
      ∀ r, K r ↔ C r.stretches :=
  ⟨fun verifiable => ⟨Ideals.Meets fun e : Run P × Nat => ∀ r' : Run P, r'.stretches.mem e → K r',
     Ideals.meets_open _, fun r =>
       ⟨fun inside => verified_iff_interiorBy.mp (verifiable r inside),
        fun meets => Ideals.InteriorBy.holds (ι := Run.stretches) meets⟩⟩,
   fun ⟨_, hc, h⟩ => verifiable_iff_verifiableBy.mpr fun r inside =>
     match verifiable_iff_verifiableBy.mp (verifiable_of_class hc) r ((h r).mp inside) with
     | ⟨e, he, all⟩ => ⟨e, he, fun r' he' => (h r').mpr (all r' he')⟩⟩

/-- **The runs outside an open class of histories are closed**: a run adhering to them lies
outside the class. -/
theorem open_compl_adheres {C : Ideals.Ideal (stretchOrder P) → Prop} (hc : Ideals.Open C)
    {r : Run P} (adheres : Adheres (fun r' : Run P => ¬ C r'.stretches) r) : ¬ C r.stretches :=
  adheres_iff_closed.mp adheres _ hc.compl_closed fun _ outside => outside

/-- The class of histories meeting the stretches through which only runs of a reading pass. -/
def verifyingClass (K : Run P → Prop) : Ideals.Ideal (stretchOrder P) → Prop :=
  Ideals.Meets fun e : Run P × Nat => ∀ r' : Run P, r'.stretches.mem e → K r'

/-- **A reading is verifiable exactly where it is the reading of its verifying class**, which is
open. -/
theorem verifiable_iff_class {K : Run P → Prop} :
    Verifiable K ↔ ∀ r, K r ↔ verifyingClass K r.stretches :=
  ⟨fun verifiable r => ⟨fun inside => verified_iff_interiorBy.mp (verifiable r inside),
     fun meets => (verified_iff_interiorBy.mpr meets).holds⟩,
   fun h => verifiable_iff_open.mpr ⟨_, Ideals.meets_open _, h⟩⟩

/-- **Verifiable readings are closed under meets**: verifying both is verifying each. -/
theorem verifiable_and {K L : Run P → Prop} (hK : Verifiable K) (hL : Verifiable L) :
    Verifiable fun r => K r ∧ L r :=
  verifiable_iff_open.mpr ⟨_, Ideals.open_and (Ideals.meets_open _) (Ideals.meets_open _),
    fun r => ⟨fun ⟨k, l⟩ => ⟨(verifiable_iff_class.mp hK r).mp k, (verifiable_iff_class.mp hL r).mp l⟩,
      fun ⟨k, l⟩ => ⟨(verifiable_iff_class.mp hK r).mpr k, (verifiable_iff_class.mp hL r).mpr l⟩⟩⟩

/-- **Verifiable readings are closed under every union**: verifying one is verifying the union. -/
theorem verifiable_exists {β : Type w} {K : β → Run P → Prop} (hK : ∀ i, Verifiable (K i)) :
    Verifiable fun r => ∃ i, K i r :=
  verifiable_iff_open.mpr ⟨_, Ideals.open_exists _ fun i => Ideals.meets_open
      (P := stretchOrder P) fun e : Run P × Nat => ∀ r' : Run P, r'.stretches.mem e → K i r',
    fun r => ⟨fun ⟨i, k⟩ => ⟨i, (verifiable_iff_class.mp (hK i) r).mp k⟩,
      fun ⟨i, k⟩ => ⟨i, (verifiable_iff_class.mp (hK i) r).mpr k⟩⟩⟩

/-- **Refutable readings are closed under joins**: a run outside both is refuted at the later of the
two horizons. -/
theorem refutable_or {K L : Run P → Prop} (hK : Refutable K) (hL : Refutable L) :
    Refutable fun r => K r ∨ L r :=
  refutable_iff_compl_verifiable.mpr
    (match verifiable_and (refutable_iff_compl_verifiable.mp hK)
        (refutable_iff_compl_verifiable.mp hL) with
     | verifiable => fun r outside =>
       match verifiable r ⟨fun k => outside (.inl k), fun l => outside (.inr l)⟩ with
       | ⟨h, all⟩ => ⟨h, fun r' agree inside => match inside with
         | .inl k => (all r' agree).1 k
         | .inr l => (all r' agree).2 l⟩)

/-- **The verifiable readings hold every run and no run.** -/
theorem verifiable_true_false :
    Verifiable (fun _ : Run P => True) ∧ Verifiable (fun _ : Run P => False) :=
  ⟨verifiable_iff_open.mpr ⟨_, Ideals.open_true, fun _ => Iff.rfl⟩,
   verifiable_iff_open.mpr ⟨_, Ideals.open_false, fun _ => Iff.rfl⟩⟩

/-- **A reading is closed exactly where its remainder holds at every run**, and dense exactly where
its hull does: wholly exposed to finite stretches, a reading has an empty remainder; refuted by no
stretch, its hull is everything. -/
theorem closed_iff_remainder {K : Run P → Prop} :
    (∀ r, Adheres K r → K r) ↔ ∀ r, Remainder K r :=
  Iff.rfl

end Stretches

/-! ### The sequences -/

namespace Sequences

/-- **Some move being `true` is verifiable.** -/
theorem eventually_verifiable : Verifiable Eventually :=
  fun _ ⟨m, hm⟩ => ⟨m + 1, fun _ agree => ⟨m, (agree.2 m (Nat.lt_succ_self m)).symm.trans hm⟩⟩

/-- **Some move being `true` is dense.** -/
theorem eventually_dense : Dense Eventually :=
  fun r h => ⟨splice r.act h true, ⟨h, splice_after _ true (Nat.le_refl h)⟩,
    ⟨fun _ _ => rfl, fun _ before => (if_pos before).symm⟩⟩

/-- **Recurrence is dense**: every finite record is a record of a recurring run. -/
theorem recurs_dense : Dense Recurs :=
  fun r h => ⟨splice r.act h true,
    fun n => ⟨n + h, Nat.le_add_right n h, splice_after _ true (Nat.le_add_left h n)⟩,
    ⟨fun _ _ => rfl, fun _ before => (if_pos before).symm⟩⟩

/-- **Recurrence is not verifiable**: the run of `true` throughout recurs and adheres to its
complement. -/
theorem recurs_not_verifiable : ¬ Verifiable Recurs :=
  not_verifiable_of_adheres (r := run fun _ => true)
    (fun h => ⟨splice (fun _ => true) h false, (fun recurs => match recurs h with
      | ⟨_, le, atTrue⟩ => nomatch atTrue.symm.trans (splice_after _ false le)),
      splice_agree _ h false⟩)
    (fun n => ⟨n, Nat.le_refl n, rfl⟩)

end Sequences

end Becoming
