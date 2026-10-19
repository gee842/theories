import Becoming.LawThroughCoupling

/-!
# A law through coupling that changes along the run

`Becoming.LawThroughCoupling` stated, along one run, when some process going alike in what a
formation couples into admits the run's steps, with fixed conditions (`Conditions`). Chapter §8.2
left open the criterion through coupling that changes along the run. Here the dependences are an
observable of the configuration (`Dependence` of `Becoming.Dependence`): what a formation depends
on, and at what level, can form and dissolve as the run goes. Ren, 18 October 2026: "you have
permission now, please see what else is there to do - keep pushing the frontier till finishing";
the AI chose the item. No premise enters beyond what each theorem names.

* **Each occasion through its own dependence.** Two configurations are alike in what `g` couples
  into when the levels at each, read through the dependence `g` has there, admit it alike and the
  conditions it observes stand alike (`Dependence.AlikeAt`). This is an equivalence
  (`Dependence.alikeAt_equivalence`), so the criterion of `Becoming.LawThroughCoupling` holds
  through it: some process going alike in what `g` couples into admits a run's steps up to `t`
  exactly where they are consistent under it (`Run.law_through_dependence_iff`). Fixed conditions
  are the instance (`Dependence.conditions_alikeAt_iff`; along a run,
  `Run.consistent_conditions_iff`). Along a run it is the relation between two steps each read
  through the dependence of its own step (`Web.AlikeAcross`, `Dependence.alikeAt_iff_alikeAcross`).
* **Testing's coupling fixes the dependence of one step.** `Web.AlikeThrough` of `Becoming.Testing`,
  read at step `t` between the levels standing at two steps of the run, is the coupling with the
  dependence fixed at the configuration of step `t` (`Dependence.fixedAt`,
  `Dependence.alikeThrough_iff_fixedAt`). Where the dependence at the two steps compared is the one
  at `t`, it is the changing coupling (`Web.alikeAcross_iff_alikeThrough`).
* **Unchanged dependences give one criterion.** Consistency under two relations agreeing on the
  run's configurations up to `t` is the same (`Run.consistentUnder_congr`). So where `g`'s
  dependences up to `t` are those of one step (`Dependence.Unchanged`), the criterion through the
  changing coupling and the criterion through the coupling fixed at that step agree
  (`Run.consistent_unchanged_iff`).
* **Where dependences form or dissolve, neither gives the other.** On one determined process
  (`Changing.process`, a level rising by one each step), a dependence that dissolves across the
  first step leaves the run consistent at every step under the changing coupling, while the
  coupling fixed at the start is inconsistent at step 2 (`Changing.dissolving_consistent`,
  `Changing.dissolving_fixed_inconsistent`). A dependence that forms across the first step leaves
  the coupling fixed at the start consistent at every step and the changing coupling inconsistent
  at step 3 (`Changing.forming_fixed_consistent`, `Changing.forming_inconsistent`).

**Reading (the AI's).** What a formation couples into changes as what it depends on forms and
dissolves, and a law at its coupling along a course is a law at the coupling it has on each
occasion. Reading the course through the dependence of one moment can find a law the formation's
own coupling does not carry, or miss one it does; where nothing it depends on changes, the two are
one.

What is not derived: which dependences an actual formation forms along an unfolding; observation
that changes along the run (here what a formation observes is fixed, as in `Becoming.Testing`); how
many steps settle whether a law at the coupling holds. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v

variable {S : Type u} {A : Type v}

namespace Dependence

variable {F C : Type} (D : Dependence S F C)

/-- The levels at `x` admit `g` through the dependence `g` has at `x`. -/
def AdmitsAt (x : S) (g : F) : Prop :=
  ∀ c, D.requires x g c → D.need x g c ≤ D.level x c

/-- `x` and `y` are alike in what `g` couples into, each read through the dependence `g` has
there: their levels admit `g` alike, and the conditions `g` observes stand alike. -/
def AlikeAt (obs : F → C → Prop) (g : F) (x y : S) : Prop :=
  (D.AdmitsAt x g ↔ D.AdmitsAt y g) ∧ ∀ c, obs g c → D.level x c = D.level y c

/-- Being alike in what `g` couples into, through changing dependence, is an equivalence. -/
theorem alikeAt_equivalence (obs : F → C → Prop) (g : F) : Equivalence (D.AlikeAt obs g) :=
  ⟨fun _ => ⟨Iff.rfl, fun _ _ => rfl⟩,
   fun alike => ⟨alike.1.symm, fun c observed => (alike.2 c observed).symm⟩,
   fun first second => ⟨first.1.trans second.1,
     fun c observed => (first.2 c observed).trans (second.2 c observed)⟩⟩

/-- **Fixed conditions are the instance.** -/
theorem conditions_alikeAt_iff (K : Conditions S F C) (obs : F → C → Prop) (g : F) (x y : S) :
    K.dependence.AlikeAt obs g x y ↔ K.AlikeAt obs g x y :=
  Iff.rfl

/-- The dependences of `x₀` held fixed: the conditions read at `x₀`. -/
def fixedAt (x₀ : S) : Conditions S F C :=
  ⟨D.level, D.active, D.requires x₀, D.need x₀, D.draws x₀⟩

/-- `g` depends at `x` on the same conditions, at the same levels, as at `y`. -/
def SameFor (g : F) (x y : S) : Prop :=
  (∀ c, D.requires x g c ↔ D.requires y g c) ∧ ∀ c, D.need x g c = D.need y g c

/-- Where `g`'s dependence at `x` is the one at `x₀`, admitting through it is admitting through the
dependence fixed at `x₀`. -/
theorem admitsAt_fixedAt_iff {g : F} {x x₀ : S} (same : D.SameFor g x x₀) :
    D.AdmitsAt x g ↔ (D.fixedAt x₀).AdmitsAt x g :=
  ⟨fun admitted c required =>
     Eq.subst (motive := fun d => d ≤ D.level x c) (same.2 c)
       (admitted c ((same.1 c).mpr required)),
   fun admitted c required =>
     Eq.subst (motive := fun d => d ≤ D.level x c) (same.2 c).symm
       (admitted c ((same.1 c).mp required))⟩

/-- `g`'s dependences do not change along the run up to `t`: at every step up to `t` they are
those of step `k`. -/
def Unchanged {P : Process S A} (r : Run P) (g : F) (k t : Nat) : Prop :=
  ∀ n, n ≤ t → D.SameFor g (r.state n) (r.state k)

end Dependence

namespace Web

variable {F C : Type} (W : Web F C)

/-- Two steps `n` and `m` are alike in what `g` couples into, each read through the dependence
of its own step. -/
def AlikeAcross (obs : F → C → Prop) (g : F) (n m : Nat) : Prop :=
  (W.Admits (W.level n) n g ↔ W.Admits (W.level m) m g) ∧ ∀ c, obs g c → W.level n c = W.level m c

variable {W}

/-- Where `g`'s dependence at `n` is the one at `t`, the levels standing at `n` are admitted at `n`
exactly as at `t`. -/
theorem admits_own_iff {g : F} {n t : Nat}
    (requires : ∀ c, W.requires n g c ↔ W.requires t g c)
    (need : ∀ c, W.need n g c = W.need t g c) :
    W.Admits (W.level n) n g ↔ W.Admits (W.level n) t g :=
  ⟨fun admitted c required =>
     Eq.subst (motive := fun d => d ≤ W.level n c) (need c) (admitted c ((requires c).mpr required)),
   fun admitted c required =>
     Eq.subst (motive := fun d => d ≤ W.level n c) (need c).symm
       (admitted c ((requires c).mp required))⟩

/-- **Testing's coupling at one step is the changing coupling** where the dependence at the two
steps compared is the one at that step. -/
theorem alikeAcross_iff_alikeThrough {obs : F → C → Prop} {g : F} {n m t : Nat}
    (requires : ∀ c, W.requires n g c ↔ W.requires t g c)
    (need : ∀ c, W.need n g c = W.need t g c)
    (requires' : ∀ c, W.requires m g c ↔ W.requires t g c)
    (need' : ∀ c, W.need m g c = W.need t g c) :
    W.AlikeAcross obs g n m ↔
      W.AlikeThrough obs g (fun _ => W.level n) (fun _ => W.level m) t :=
  ⟨fun alike => ⟨(admits_own_iff requires need).symm.trans
       (alike.1.trans (admits_own_iff requires' need')), alike.2⟩,
   fun alike => ⟨(admits_own_iff requires need).trans
       (alike.1.trans (admits_own_iff requires' need').symm), alike.2⟩⟩

end Web

namespace Dependence

variable {F C : Type} (D : Dependence S F C)

/-- **Along a run, the changing coupling is `Web.AlikeAcross`** of the run read through its
dependences. -/
theorem alikeAt_iff_alikeAcross {P : Process S A} (r : Run P) (obs : F → C → Prop) (g : F)
    (n m : Nat) :
    D.AlikeAt obs g (r.state n) (r.state m) ↔ (D.along r).AlikeAcross obs g n m :=
  Iff.rfl

/-- **Testing's coupling read at step `t` fixes the dependence of step `t`.** Between the levels
standing at two steps of the run, `Web.AlikeThrough` at `t` is the coupling through the conditions
fixed at the configuration of step `t`. -/
theorem alikeThrough_iff_fixedAt {P : Process S A} (r : Run P) (obs : F → C → Prop) (g : F)
    (n m t : Nat) :
    (D.along r).AlikeThrough obs g (fun _ => D.level (r.state n)) (fun _ => D.level (r.state m)) t ↔
      (D.fixedAt (r.state t)).AlikeAt obs g (r.state n) (r.state m) :=
  Iff.rfl

end Dependence

namespace Run

variable {P : Process S A} {F C : Type}

/-- **A law through coupling that changes along the run.** Some process going alike in what `g`
couples into, each configuration read through the dependence `g` has there, admits a run's steps
before `t` exactly where any two of them `g` couples alike, by the same move, lead to configurations
`g` couples alike. -/
theorem law_through_dependence_iff (D : Dependence S F C) (r : Run P) (obs : F → C → Prop)
    (g : F) (t : Nat) :
    (∃ Q : Process S A, GoAlikeUnder Q id (D.AlikeAt obs g) ∧
        ∀ n, n < t → Q.step (r.state n) (r.act n) (r.state (n + 1))) ↔
      r.ConsistentUnder (D.AlikeAt obs g) t :=
  r.law_under_iff (D.alikeAt_equivalence obs g) t

/-- **Consistency reads a relation only on the run's configurations up to `t`.** -/
theorem consistentUnder_congr (r : Run P) {E E' : S → S → Prop} {t : Nat}
    (agree : ∀ n m, n ≤ t → m ≤ t → (E (r.state n) (r.state m) ↔ E' (r.state n) (r.state m))) :
    r.ConsistentUnder E t ↔ r.ConsistentUnder E' t :=
  ⟨fun consistent n m before before' same act =>
     (agree (n + 1) (m + 1) before before').mp (consistent n m before before'
       ((agree n m (Nat.le_of_lt before) (Nat.le_of_lt before')).mpr same) act),
   fun consistent n m before before' same act =>
     (agree (n + 1) (m + 1) before before').mpr (consistent n m before before'
       ((agree n m (Nat.le_of_lt before) (Nat.le_of_lt before')).mp same) act)⟩

/-- **Fixed conditions are the instance along a run**: through fixed conditions, consistency under
the changing coupling is consistency under the coupling of `Becoming.LawThroughCoupling`. -/
theorem consistent_conditions_iff (K : Conditions S F C) (r : Run P) (obs : F → C → Prop) (g : F)
    (t : Nat) :
    r.ConsistentUnder (K.dependence.AlikeAt obs g) t ↔ r.ConsistentUnder (K.AlikeAt obs g) t :=
  r.consistentUnder_congr fun _ _ _ _ => Dependence.conditions_alikeAt_iff K obs g _ _

/-- **Unchanged dependences give one criterion.** Where `g`'s dependences up to `t` are those of
step `k`, the run is consistent under the changing coupling exactly where it is consistent under
the coupling fixed at step `k`. -/
theorem consistent_unchanged_iff (D : Dependence S F C) (r : Run P) (obs : F → C → Prop)
    {g : F} {k t : Nat} (unchanged : D.Unchanged r g k t) :
    r.ConsistentUnder (D.AlikeAt obs g) t ↔
      r.ConsistentUnder ((D.fixedAt (r.state k)).AlikeAt obs g) t :=
  r.consistentUnder_congr fun n m le le' =>
    ⟨fun alike => ⟨(D.admitsAt_fixedAt_iff (unchanged n le)).symm.trans
        (alike.1.trans (D.admitsAt_fixedAt_iff (unchanged m le'))), alike.2⟩,
     fun alike => ⟨(D.admitsAt_fixedAt_iff (unchanged n le)).trans
        (alike.1.trans (D.admitsAt_fixedAt_iff (unchanged m le')).symm), alike.2⟩⟩

end Run

/-! ## Witnesses: dependences that dissolve and form along one run -/

namespace Changing

/-- One level, rising by one each step. -/
def process : Process Nat Unit := ⟨fun x _ y => y = x + 1⟩

/-- The run from 0: the level at step `n` is `n`. -/
def run : Run process := ⟨fun n => n, fun _ => (), fun _ => rfl⟩

/-- The process is determined. -/
theorem determined : Determined process :=
  fun _ _ _ _ first second => first.trans second.symm

/-- The formation depends on the one condition, with need 2, only at level 0. -/
def dissolving : Dependence Nat Unit Unit :=
  ⟨fun x _ => x, fun _ _ => True, fun x _ _ => x = 0, fun _ _ _ => 2, fun _ _ _ => False⟩

/-- The formation depends on the one condition, with need 2, from level 1 on. -/
def forming : Dependence Nat Unit Unit :=
  ⟨fun x _ => x, fun _ _ => True, fun x _ _ => 1 ≤ x, fun _ _ _ => 2, fun _ _ _ => False⟩

/-- The dependence dissolves across the first step. -/
theorem dissolves : (dissolving.along run).Dissolves 0 () () :=
  ⟨rfl, fun moved => Nat.noConfusion moved⟩

/-- The dependence forms across the first step. -/
theorem forms : (forming.along run).Forms 0 () () :=
  ⟨Nat.not_succ_le_zero 0, Nat.le_refl 1⟩

theorem dissolving_not_admits_zero : ¬ dissolving.AdmitsAt 0 () :=
  fun admitted => Nat.not_succ_le_zero 1 (admitted () rfl)

theorem dissolving_admits_succ (n : Nat) : dissolving.AdmitsAt (n + 1) () :=
  fun _ required => Nat.noConfusion required

/-- **A dissolving dependence carries a law at the changing coupling**, at every step. -/
theorem dissolving_consistent (t : Nat) :
    run.ConsistentUnder (dissolving.AlikeAt thresholdOnly ()) t :=
  fun n m _ _ same _ => match n, m, same with
    | 0, 0, _ => (dissolving.alikeAt_equivalence thresholdOnly ()).refl _
    | 0, m + 1, same => absurd (same.1.mpr (dissolving_admits_succ m)) dissolving_not_admits_zero
    | n + 1, 0, same => absurd (same.1.mp (dissolving_admits_succ n)) dissolving_not_admits_zero
    | n + 1, m + 1, _ =>
      ⟨⟨fun _ => dissolving_admits_succ (m + 1), fun _ => dissolving_admits_succ (n + 1)⟩,
       fun _ nothing => nothing.elim⟩

/-- **The coupling fixed at the start lacks it.** Through the dependence of level 0 held fixed, the
first two steps start alike (neither level admits) and lead to levels 1 and 2, coupled apart. -/
theorem dissolving_fixed_inconsistent :
    ¬ run.ConsistentUnder ((dissolving.fixedAt (run.state 0)).AlikeAt thresholdOnly ()) 2 :=
  fun consistent =>
    have below : ∀ x, x < 2 → ¬ (dissolving.fixedAt 0).AdmitsAt x () :=
      fun _ low admitted => Nat.not_le_of_lt low (admitted () rfl)
    have two : (dissolving.fixedAt 0).AdmitsAt 2 () := fun _ _ => Nat.le_refl 2
    below 1 (Nat.lt_succ_self 1)
      ((consistent 0 1 (Nat.zero_lt_succ 1) (Nat.lt_succ_self 1)
        ⟨⟨fun admitted => absurd admitted (below 0 (Nat.zero_lt_succ 1)),
          fun admitted => absurd admitted (below 1 (Nat.lt_succ_self 1))⟩,
         fun _ nothing => nothing.elim⟩ rfl).1.mpr two)

theorem forming_admits_zero : forming.AdmitsAt 0 () :=
  fun _ required => absurd required (Nat.not_succ_le_zero 0)

theorem forming_not_admits_one : ¬ forming.AdmitsAt 1 () :=
  fun admitted => Nat.not_succ_le_self 1 (admitted () (Nat.le_refl 1))

theorem forming_admits_three : forming.AdmitsAt 3 () :=
  fun _ _ => Nat.le_succ 2

/-- **A forming dependence breaks a law at the changing coupling.** Steps 0 and 2 start alike
(both levels admit) and lead to levels 1 and 3, coupled apart. -/
theorem forming_inconsistent : ¬ run.ConsistentUnder (forming.AlikeAt thresholdOnly ()) 3 :=
  fun consistent =>
    forming_not_admits_one
      ((consistent 0 2 (Nat.zero_lt_succ 2) (Nat.lt_succ_self 2)
        ⟨⟨fun _ => fun _ _ => Nat.le_refl 2, fun _ => forming_admits_zero⟩,
         fun _ nothing => nothing.elim⟩ rfl).1.mpr forming_admits_three)

/-- **The coupling fixed at the start has it**, at every step: through the dependence of level 0
held fixed, the formation depends on nothing, and every two configurations are coupled alike. -/
theorem forming_fixed_consistent (t : Nat) :
    run.ConsistentUnder ((forming.fixedAt (run.state 0)).AlikeAt thresholdOnly ()) t :=
  have every : ∀ x, (forming.fixedAt 0).AdmitsAt x () :=
    fun _ _ required => absurd required (Nat.not_succ_le_zero 0)
  fun _ _ _ _ _ _ => ⟨⟨fun _ => every _, fun _ => every _⟩, fun _ nothing => nothing.elim⟩

/-- So no process going alike at the changing coupling admits the forming run's steps before 3,
though the process is determined. -/
theorem forming_no_law {t : Nat} (three : 3 ≤ t) :
    ¬ ∃ Q : Process Nat Unit, GoAlikeUnder Q id (forming.AlikeAt thresholdOnly ()) ∧
      ∀ n, n < t → Q.step (run.state n) (run.act n) (run.state (n + 1)) :=
  fun law => forming_inconsistent
    (((run.law_through_dependence_iff forming thresholdOnly () t).mp law).earlier three)

/-- And no process going alike at the coupling fixed at the start admits the dissolving run's steps
before 2. -/
theorem dissolving_fixed_no_law {t : Nat} (two : 2 ≤ t) :
    ¬ ∃ Q : Process Nat Unit,
        GoAlikeUnder Q id ((dissolving.fixedAt (run.state 0)).AlikeAt thresholdOnly ()) ∧
      ∀ n, n < t → Q.step (run.state n) (run.act n) (run.state (n + 1)) :=
  fun law => dissolving_fixed_inconsistent
    (((run.law_through_coupling_iff (dissolving.fixedAt (run.state 0)) thresholdOnly () t).mp
      law).earlier two)

end Changing

end Becoming
