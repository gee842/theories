import Becoming.LawAlongRun
import Becoming.Testing
import Becoming.Likeness

/-!
# A law through what a formation couples into, along one run

`Becoming.LawAlongRun` stated when one run's steps, read through a projection, admit a law at the
description. Chapter §8.2 left open its instance with `Becoming.Testing`'s registration, now
called coupling (`Web.AlikeThrough`), as the description. Coupling is a relation between level
histories, not a projection to a type of descriptions, and an equality of what is coupled would
need `propext`. So this module states the criterion up to a relation and takes coupling as one.
Ren, 18 October 2026: "Yes: claim G4 on the board — the criterion along one run with
Becoming.Testing's registration as the projection — and prove it in scratch while the queue
runs." No premise enters beyond what each theorem names.

* **Along one run, up to a relation.** A run's steps before `t` are consistent under a relation
  `E` when any two of them from configurations `E` relates, by the same move, reach configurations
  `E` relates (`Run.ConsistentUnder`). Where `E` is an equivalence, some process going alike under
  `E` (`GoAlikeUnder` of `Becoming.Likeness`, through the identity) admits the run's steps before
  `t` exactly where they are consistent (`Run.law_under_iff`). The witness is the record read under
  `E` (`Run.recordUnder`). The forward direction needs no equivalence. Consistency up to a step
  holds at every earlier step, so once failed the criterion fails from then on
  (`Run.ConsistentUnder.earlier`, `Run.no_law_under_later`). Where the process goes alike under
  `E`, every run is consistent (`Run.consistentUnder_of_goAlikeUnder`). Through equal projections
  this is `Run.ConsistentThrough` of `Becoming.LawAlongRun` (`Run.consistentUnder_eq_iff`).
* **Coupling as the relation.** With fixed conditions (`Conditions` of `Becoming.Renewal`), two
  configurations are alike in what a formation couples into when their levels admit it alike and
  the conditions it observes stand alike (`Conditions.AlikeAt`). This is an equivalence
  (`Conditions.alikeAt_equivalence`) and is exactly `Web.AlikeThrough` on the runs read through the
  conditions, between two runs at one step (`Conditions.alikeThrough_iff`) and, along one run,
  between two of its steps (`Conditions.alikeAt_iff_alikeThrough`). So some process going alike in
  what `g` couples into admits a run's steps up to `t` exactly where any two of them `g` couples
  alike, by the same move, lead to configurations `g` couples alike (`Run.law_through_coupling_iff`).
* **An uncoupled level can decide the next coupling.** In `Unseen` the process is determined, and a
  formation depending on one condition and observing nothing couples alike the first two steps of
  a run, which by the same move lead to configurations it couples apart: the level it does not
  couple into decides (`Unseen.determined`, `Unseen.inconsistent`, `Unseen.no_law`). Observing that
  level, the same run is consistent at every step (`Unseen.consistent_observing`).

**Reading (the AI's).** What a formation couples into carries a law along its course exactly as
far as the occasions it couples alike went alike; the record of those occasions is then the law.
Where a difference outside its coupling decides what it next couples into, no law at its coupling
holds along that course, however determined the unfolding is; coupling into the difference can
restore it. This is `Becoming.Testing`'s boundary, that a difference beyond what couples in is not
tested, read as the failure of a law along one course.

What is not derived: which formation's coupling carries a law along an actual unfolding; coupling
that changes along the run (`Dependence` rather than fixed `Conditions`); how many steps settle
whether it does. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

variable {S : Type u} {A : Type v}

namespace Run

variable {P : Process S A}

/-- The run's steps before `t` are consistent under `E`: two of them from configurations `E`
relates, by the same move, reach configurations `E` relates. -/
def ConsistentUnder (r : Run P) (E : S → S → Prop) (t : Nat) : Prop :=
  ∀ n m, n < t → m < t → E (r.state n) (r.state m) → r.act n = r.act m →
    E (r.state (n + 1)) (r.state (m + 1))

/-- The record read under `E` before `t`: a move goes from `x` to `y` where the run took it,
before `t`, from a configuration `E` relates to `x` to one `E` relates to `y`. -/
def recordUnder (r : Run P) (E : S → S → Prop) (t : Nat) : Process S A :=
  ⟨fun x a y => ∃ n, n < t ∧ E x (r.state n) ∧ r.act n = a ∧ E y (r.state (n + 1))⟩

/-- Where `E` is reflexive, the record admits the run's steps before `t`. -/
theorem recordUnder_steps (r : Run P) {E : S → S → Prop} (refl : ∀ x, E x x) (t : Nat) :
    ∀ n, n < t → (r.recordUnder E t).step (r.state n) (r.act n) (r.state (n + 1)) :=
  fun n before => ⟨n, before, refl _, rfl, refl _⟩

/-- Where `E` is an equivalence and the steps are consistent under it, the record goes alike
under `E`. -/
theorem recordUnder_goAlike (r : Run P) {E : S → S → Prop} (equivalence : Equivalence E)
    {t : Nat} (consistent : r.ConsistentUnder E t) :
    GoAlikeUnder (r.recordUnder E t) id E :=
  fun _ _ _ _ _ same ⟨n, before, at_x, by_a, to_y⟩ ⟨m, before', at_x', by_a', to_y'⟩ =>
    equivalence.trans to_y
      (equivalence.trans
        (consistent n m before before'
          (equivalence.trans (equivalence.symm at_x) (equivalence.trans same at_x'))
          (by_a.trans by_a'.symm))
        (equivalence.symm to_y'))

/-- **A law up to a relation along one run.** Where `E` is an equivalence, some process going
alike under `E` admits the run's steps before `t` exactly where those steps are consistent under
`E`. No premise: the witness is the record read under `E`. -/
theorem law_under_iff (r : Run P) {E : S → S → Prop} (equivalence : Equivalence E) (t : Nat) :
    (∃ Q : Process S A, GoAlikeUnder Q id E ∧
        ∀ n, n < t → Q.step (r.state n) (r.act n) (r.state (n + 1))) ↔
      r.ConsistentUnder E t :=
  ⟨fun ⟨Q, alike, steps⟩ n m before before' same same' =>
     alike _ _ _ _ _ same (steps n before)
       (Eq.subst (motive := fun b => Q.step (r.state m) b (r.state (m + 1))) same'.symm
         (steps m before')),
   fun consistent => ⟨r.recordUnder E t, r.recordUnder_goAlike equivalence consistent,
     r.recordUnder_steps equivalence.refl t⟩⟩

/-- Consistency up to a step holds at every earlier step. -/
theorem ConsistentUnder.earlier {r : Run P} {E : S → S → Prop} {t t' : Nat}
    (consistent : r.ConsistentUnder E t') (le : t ≤ t') : r.ConsistentUnder E t :=
  fun n m before before' => consistent n m (Nat.lt_of_lt_of_le before le)
    (Nat.lt_of_lt_of_le before' le)

/-- **Once failed, failed from then on.** Where no process going alike under `E` admits the run's
steps before `t`, none admits them before any later step. -/
theorem no_law_under_later (r : Run P) {E : S → S → Prop} (equivalence : Equivalence E)
    {t t' : Nat} (le : t ≤ t')
    (failed : ¬ ∃ Q : Process S A, GoAlikeUnder Q id E ∧
        ∀ n, n < t → Q.step (r.state n) (r.act n) (r.state (n + 1))) :
    ¬ ∃ Q : Process S A, GoAlikeUnder Q id E ∧
        ∀ n, n < t' → Q.step (r.state n) (r.act n) (r.state (n + 1)) :=
  fun law => failed ((r.law_under_iff equivalence t).mpr
    (((r.law_under_iff equivalence t').mp law).earlier le))

/-- Where the process goes alike under `E`, every run is consistent under `E` at every step. -/
theorem consistentUnder_of_goAlikeUnder (r : Run P) {E : S → S → Prop}
    (alike : GoAlikeUnder P id E) (t : Nat) : r.ConsistentUnder E t :=
  fun n m _ _ same same' => alike _ _ _ _ _ same (r.step n)
    (Eq.subst (motive := fun b => P.step (r.state m) b (r.state (m + 1))) same'.symm (r.step m))

/-- **`Becoming.LawAlongRun`'s criterion is the instance with equal projections.** -/
theorem consistentUnder_eq_iff {D : Type w} (r : Run P) (π : S → D) (t : Nat) :
    r.ConsistentUnder (fun x y => π x = π y) t ↔ r.ConsistentThrough π t :=
  Iff.rfl

end Run

/-! ## Coupling as the relation -/

namespace Conditions

variable {F C : Type} (K : Conditions S F C)

/-- The levels at `x` admit `g`: they meet every requirement `g` has. -/
def AdmitsAt (x : S) (g : F) : Prop :=
  ∀ c, K.requires g c → K.need g c ≤ K.level x c

/-- `x` and `y` are alike in what `g` couples into: their levels admit `g` alike, and the
conditions `g` observes stand alike. -/
def AlikeAt (obs : F → C → Prop) (g : F) (x y : S) : Prop :=
  (K.AdmitsAt x g ↔ K.AdmitsAt y g) ∧ ∀ c, obs g c → K.level x c = K.level y c

/-- Being alike in what `g` couples into is an equivalence. -/
theorem alikeAt_equivalence (obs : F → C → Prop) (g : F) : Equivalence (K.AlikeAt obs g) :=
  ⟨fun _ => ⟨Iff.rfl, fun _ _ => rfl⟩,
   fun alike => ⟨alike.1.symm, fun c observed => (alike.2 c observed).symm⟩,
   fun first second => ⟨first.1.trans second.1,
     fun c observed => (first.2 c observed).trans (second.2 c observed)⟩⟩

/-- **Coupling between two runs at one step is `Web.AlikeThrough`.** -/
theorem alikeThrough_iff {P : Process S A} (r r' : Run P) (obs : F → C → Prop) (g : F)
    (t : Nat) :
    (K.dependence.along r).AlikeThrough obs g (K.dependence.along r).level
        (K.dependence.along r').level t ↔
      K.AlikeAt obs g (r.state t) (r'.state t) :=
  Iff.rfl

/-- **Coupling between two steps of one run is `Web.AlikeThrough`** of the levels standing at those
steps, read at any step. -/
theorem alikeAt_iff_alikeThrough {P : Process S A} (r : Run P) (obs : F → C → Prop) (g : F)
    (n m t : Nat) :
    K.AlikeAt obs g (r.state n) (r.state m) ↔
      (K.dependence.along r).AlikeThrough obs g (fun _ => K.level (r.state n))
        (fun _ => K.level (r.state m)) t :=
  Iff.rfl

end Conditions

namespace Run

variable {P : Process S A} {F C : Type}

/-- **A law through what a formation couples into, along one run.** Some process going alike in
what `g` couples into admits a run's steps before `t` exactly where any two of them that `g`
couples alike, by the same move, lead to configurations `g` couples alike. -/
theorem law_through_coupling_iff (K : Conditions S F C) (r : Run P) (obs : F → C → Prop)
    (g : F) (t : Nat) :
    (∃ Q : Process S A, GoAlikeUnder Q id (K.AlikeAt obs g) ∧
        ∀ n, n < t → Q.step (r.state n) (r.act n) (r.state (n + 1))) ↔
      r.ConsistentUnder (K.AlikeAt obs g) t :=
  r.law_under_iff (K.alikeAt_equivalence obs g) t

end Run

/-! ## Witness: an uncoupled level decides the next coupling -/

namespace Unseen

/-- Two levels; each step moves the second into the first and empties the second. -/
def process : Process (Nat × Nat) Unit := ⟨fun x _ y => y = (x.2, 0)⟩

/-- The first level is condition `false`, the second `true`. -/
def level (x : Nat × Nat) : Bool → Nat
  | false => x.1
  | true => x.2

/-- One formation depending on condition `false` with need 1. -/
def conditions : Conditions (Nat × Nat) Unit Bool :=
  ⟨level, fun _ _ => True, fun _ c => c = false, fun _ _ => 1, fun _ _ => False⟩

/-- The run from `(1, 1)`: `(1, 1)`, `(1, 0)`, then `(0, 0)`. -/
def state : Nat → Nat × Nat
  | 0 => (1, 1)
  | 1 => (1, 0)
  | _ + 2 => (0, 0)

/-- The run. -/
def run : Run process :=
  ⟨state, fun _ => (), fun n => match n with
    | 0 => rfl
    | 1 => rfl
    | _ + 2 => rfl⟩

/-- The process is determined. -/
theorem determined : Determined process :=
  fun _ _ _ _ first second => first.trans second.symm

/-- A configuration whose first level is at least 1 admits the formation. -/
theorem admits {x : Nat × Nat} (one : 1 ≤ x.1) : conditions.AdmitsAt x () :=
  fun _ required => Eq.subst (motive := fun d => 1 ≤ level x d) required.symm one

/-- `(0, 0)` does not admit the formation. -/
theorem not_admits_zero : ¬ conditions.AdmitsAt (0, 0) () :=
  fun admitted => Nat.not_succ_le_zero 0 (admitted false rfl)

/-- **An uncoupled level decides.** Observing nothing, the formation couples the run's first two
steps alike, and by the same move they lead to configurations it couples apart. -/
theorem inconsistent : ¬ run.ConsistentUnder (conditions.AlikeAt thresholdOnly ()) 2 :=
  fun consistent =>
    not_admits_zero ((consistent 0 1 (Nat.zero_lt_succ 1) (Nat.lt_succ_self 1)
      ⟨⟨fun _ => admits (Nat.le_refl 1), fun _ => admits (Nat.le_refl 1)⟩, fun _ nothing => False.elim nothing⟩
      rfl).1.mp (admits (Nat.le_refl 1)))

/-- So no process going alike in what the formation couples into admits the run's first two
steps, though the process is determined. -/
theorem no_law {t : Nat} (two : 2 ≤ t) :
    ¬ ∃ Q : Process (Nat × Nat) Unit, GoAlikeUnder Q id (conditions.AlikeAt thresholdOnly ()) ∧
      ∀ n, n < t → Q.step (run.state n) (run.act n) (run.state (n + 1)) :=
  fun law => inconsistent
    (((run.law_through_coupling_iff conditions thresholdOnly () t).mp law).earlier two)

/-- The formation observes condition `true`. -/
def observing : Unit → Bool → Prop := fun _ c => c = true

/-- The first configuration is coupled apart from every later one when `true` is observed. -/
theorem first_apart (m : Nat) : ¬ conditions.AlikeAt observing () (1, 1) (state (m + 1)) :=
  match m with
  | 0 => fun alike => Nat.noConfusion (alike.2 true rfl)
  | _ + 1 => fun alike => Nat.noConfusion (alike.2 true rfl)

/-- **Coupling into the deciding level restores the law along the run**, at every step. -/
theorem consistent_observing (t : Nat) :
    run.ConsistentUnder (conditions.AlikeAt observing ()) t :=
  fun n m _ _ same _ => match n, m, same with
    | 0, 0, _ => (conditions.alikeAt_equivalence observing ()).refl _
    | 0, m + 1, same => (first_apart m same).elim
    | n + 1, 0, same => (first_apart n ((conditions.alikeAt_equivalence observing ()).symm same)).elim
    | _ + 1, _ + 1, _ => (conditions.alikeAt_equivalence observing ()).refl _

end Unseen

end Becoming
