import Becoming.SeekingRuns

/-!
# Enough: where the runs of a process come to rest with a target met

`Becoming.Seeking` states the boundary of enough under a determined law: the orbit from a
configuration comes to rest with its target met exactly where it reaches a configuration the law
leaves unchanged that meets the target (`Law.rests_iff`), and `Becoming.SeekingRuns` states it on
the runs of the law. Under an undetermined law a configuration has many runs. This module states
the boundary of enough on the runs of any process, with no premise.

* **Possible enough.** Some run from a configuration comes to rest with its target met exactly
  where a configuration reachable from it meets the target and has a step that stays
  (`Enough.possibly_rests_iff`). The run reaches it and stays (`Enough.trace_then_stay`).
* **Assured enough needs every reachable stay to meet the target.** Where every run from a
  configuration comes to rest with its target met, every configuration reachable from it that has
  a step that stays meets the target (`Enough.assured_stays_meet`).
* **Exactly.** Every run from a configuration comes to rest with its target met exactly where
  every reachable configuration that has a step that stays meets the target and every run from it
  settles, its configuration unchanged from some step on (`Enough.assured_iff`). The second part
  is of the process alone.
* **And the first part is not enough.** Where every configuration can stay and meets the target, a run may
  still keep changing and never rest: in `Enough.Free`, two configurations with every step
  allowed, some run from a configuration rests and the alternating run from it does not settle
  (`Enough.Free.stays_meet_not_assured`).
* **Under a determined law the two are one.** Under a determined law some run from a
  configuration rests with its target met exactly where every run from it does
  (`Enough.law_possibly_iff_assured`), and exactly where the orbit reaches a configuration the law
  leaves unchanged that meets the target (`Enough.law_possibly_iff`): the instance of possible
  enough that is `Law.rests_iff`.

So under an undetermined law what can come to rest and what must come to rest part: the first is a
reachable configuration that stays and meets the target; the second is every such configuration
meeting it and every run settling. When the runs of a process settle is not stated here. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v

namespace Enough

section AnyProcess

variable {S : Type u} {A : Type v} {P : Process S A}

/-- A run comes to rest with the target met from step `T` on: from `T` on its configuration does
not change across a step and meets the target. -/
def RestsFrom (target : S → Prop) (r : Run P) (T : Nat) : Prop :=
  ∀ n, T ≤ n → r.state (n + 1) = r.state n ∧ target (r.state n)

/-- A run comes to rest with the target met. -/
def Rests (target : S → Prop) (r : Run P) : Prop := ∃ T, RestsFrom target r T

/-- A configuration has a step that stays: some action leaves it as it is. -/
def Stays (P : Process S A) (u : S) : Prop := ∃ a, P.step u a u

/-- The run that stays at `u` by a staying step. -/
def stayAt {u : S} {a : A} (stay : P.step u a u) : Run P :=
  ⟨fun _ => u, fun _ => a, fun _ => stay⟩

/-- The configurations of a step from `s` followed by a run. -/
def prependState (s : S) (r : Run P) : Nat → S
  | 0 => s
  | n + 1 => r.state n

/-- The actions of a step by `a` followed by a run. -/
def prependAct (a : A) (r : Run P) : Nat → A
  | 0 => a
  | n + 1 => r.act n

/-- A step from `s` to where a run begins, followed by the run: a run from `s`. -/
def prepend {s : S} {a : A} (r : Run P) (step : P.step s a (r.state 0)) : Run P :=
  ⟨prependState s r, prependAct a r, fun
    | 0 => step
    | n + 1 => r.step n⟩

/-- **Reaching, then staying.** Along a finite path from `s` to a configuration with a step that
stays, some run from `s` is at that configuration from the path's length on. -/
theorem trace_then_stay {u : S} {a : A} (stay : P.step u a u) {s : S} {as : List A}
    (path : Trace P s as u) :
    ∃ r : Run P, r.state 0 = s ∧ ∀ n, as.length ≤ n → r.state n = u := by
  induction path with
  | nil => exact ⟨stayAt stay, rfl, fun _ _ => rfl⟩
  | @cons s' m _ a' _ step _ ih =>
    exact match ih stay with
    | ⟨r, start, after⟩ =>
      ⟨prepend r (Eq.subst (motive := fun x => P.step s' a' x) start.symm step), rfl, fun
        | 0, late => absurd late (Nat.not_succ_le_zero _)
        | n + 1, late => after n (Nat.le_of_succ_le_succ late)⟩

/-- **Possible enough.** Some run from `s` comes to rest with its target met exactly where a
configuration reachable from `s` meets the target and has a step that stays. -/
theorem possibly_rests_iff {s : S} {target : S → Prop} :
    (∃ r : Run P, r.state 0 = s ∧ Rests target r) ↔ ∃ u, Reach P s u ∧ Stays P u ∧ target u :=
  ⟨fun ⟨r, start, T, rests⟩ =>
    ⟨r.state T,
     Eq.subst (motive := fun x => Reach P x (r.state T)) start
       (Eq.subst (motive := fun k => Reach P (r.state 0) (r.state k)) (Nat.zero_add T) (r.reach 0 T)),
     ⟨r.act T, Eq.subst (motive := fun x => P.step (r.state T) (r.act T) x)
       (rests T (Nat.le_refl T)).1 (r.step T)⟩,
     (rests T (Nat.le_refl T)).2⟩,
   fun ⟨_, ⟨as, path⟩, ⟨_, stay⟩, meets⟩ =>
    match trace_then_stay stay path with
    | ⟨r, start, after⟩ => ⟨r, start, as.length, fun n late =>
      ⟨(after (n + 1) (Nat.le_succ_of_le late)).trans (after n late).symm,
       (congrArg target (after n late)).mpr meets⟩⟩⟩

/-- **Assured enough needs every reachable stay to meet the target.** Where every run from `s`
comes to rest with its target met, every configuration reachable from `s` that has a step that
stays meets the target. -/
theorem assured_stays_meet {s : S} {target : S → Prop}
    (assured : ∀ r : Run P, r.state 0 = s → Rests target r) :
    ∀ u, Reach P s u → Stays P u → target u :=
  fun _ ⟨as, path⟩ ⟨_, stay⟩ =>
    match trace_then_stay stay path with
    | ⟨r, start, after⟩ =>
      match assured r start with
      | ⟨T, rests⟩ =>
        (congrArg target (after (as.length + T) (Nat.le_add_right _ _))).mp
          (rests (as.length + T) (Nat.le_add_left _ _)).2

/-- A run settles: from some step on its configuration does not change across a step. -/
def Settles (r : Run P) : Prop := ∃ T, ∀ n, T ≤ n → r.state (n + 1) = r.state n

/-- A run unchanged across every step from `T` on is at its configuration at `T` from `T` on. -/
theorem settled_at {r : Run P} {T : Nat} (stays : ∀ n, T ≤ n → r.state (n + 1) = r.state n) :
    ∀ k, r.state (T + k) = r.state T
  | 0 => rfl
  | k + 1 => (stays (T + k) (Nat.le_add_right T k)).trans (settled_at stays k)

/-- **Assured enough is every reachable stay meeting the target, and every run settling.** Every
run from `s` comes to rest with its target met exactly where every configuration reachable from
`s` that has a step that stays meets the target and every run from `s` settles. The second part
does not mention the target. -/
theorem assured_iff {s : S} {target : S → Prop} :
    (∀ r : Run P, r.state 0 = s → Rests target r) ↔
      (∀ u, Reach P s u → Stays P u → target u) ∧ ∀ r : Run P, r.state 0 = s → Settles r :=
  ⟨fun assured => ⟨assured_stays_meet assured, fun r start =>
      match assured r start with
      | ⟨T, rests⟩ => ⟨T, fun n late => (rests n late).1⟩⟩,
   fun ⟨meet, settle⟩ r start =>
    match settle r start with
    | ⟨T, stays⟩ =>
      have at_T := settled_at stays
      have meets : target (r.state T) :=
        meet _ (Eq.subst (motive := fun x => Reach P x (r.state T)) start
            (Eq.subst (motive := fun k => Reach P (r.state 0) (r.state k)) (Nat.zero_add T)
              (r.reach 0 T)))
          ⟨r.act T, Eq.subst (motive := fun x => P.step (r.state T) (r.act T) x)
            (stays T (Nat.le_refl T)) (r.step T)⟩
      ⟨T, fun n late =>
        match le_dest late with
        | ⟨d, gap⟩ => ⟨stays n late,
            (congrArg target ((congrArg r.state gap).trans (at_T d))).mpr meets⟩⟩⟩

end AnyProcess

/-! ## A run that keeps changing -/

namespace Free

/-- Two configurations, every step allowed: each configuration can stay or change. -/
def process : Process Bool Unit := everyStep Bool Unit

/-- The alternating configurations. -/
def alternate : Nat → Bool
  | 0 => false
  | n + 1 => !alternate n

/-- The run that changes at every step. -/
def alternating : Run process := ⟨alternate, fun _ => (), fun _ => trivial⟩

/-- **Every configuration can stay and meets the target, and still not every run rests.** In
`Free`, with the target met everywhere, every configuration has a step that stays and meets the
target, and some run from `false` rests with the target met; the alternating run from `false` does
not settle, so not every run from `false` rests. -/
theorem stays_meet_not_assured :
    (∀ u : Bool, Stays process u ∧ True) ∧
    (∃ r : Run process, r.state 0 = false ∧ Rests (fun _ => True) r) ∧
    ¬ Settles alternating ∧
    ¬ ∀ r : Run process, r.state 0 = false → Rests (fun _ => True) r :=
  have unsettled : ¬ Settles alternating := fun ⟨T, stays⟩ =>
    ListTests.not_ne_self (alternate T) (stays T (Nat.le_refl T))
  ⟨fun _ => ⟨⟨(), trivial⟩, trivial⟩,
   possibly_rests_iff.mpr ⟨false, Reach.refl process false, ⟨(), trivial⟩, trivial⟩,
   unsettled,
   fun assured => unsettled ((assured_iff.mp assured).2 alternating rfl)⟩

end Free

/-! ## Under a determined law -/

section Determined

variable {S : Type u} {next : S → S}

/-- **Under a determined law, possible enough is the boundary of enough.** Some run of a
determined law from `s` comes to rest with its target met exactly where the orbit from `s` reaches
a configuration the law leaves unchanged that meets the target: `Law.rests_iff`'s condition, here
as the instance of `possibly_rests_iff`. -/
theorem law_possibly_iff {s : S} {target : S → Prop} :
    (∃ r : Run (Law.process next), r.state 0 = s ∧ Rests target r) ↔
      ∃ T, next (Law.orbit next s T) = Law.orbit next s T ∧ target (Law.orbit next s T) :=
  possibly_rests_iff.trans
    ⟨fun ⟨_, reach, ⟨_, stay⟩, meets⟩ =>
      match Branching.law_reach_iff.mp reach with
      | ⟨T, to⟩ => ⟨T, (congrArg next to).trans (stay.symm.trans to.symm),
          (congrArg target to).mpr meets⟩,
     fun ⟨T, fixed, meets⟩ =>
      ⟨Law.orbit next s T, Branching.law_reach_iff.mpr ⟨T, rfl⟩, ⟨(), fixed.symm⟩, meets⟩⟩

/-- **Under a determined law, possible and assured enough are one.** Some run of a determined law
from `s` comes to rest with its target met exactly where every run from `s` does. -/
theorem law_possibly_iff_assured {s : S} {target : S → Prop} :
    (∃ r : Run (Law.process next), r.state 0 = s ∧ Rests target r) ↔
      ∀ r : Run (Law.process next), r.state 0 = s → Rests target r :=
  ⟨fun ⟨r, start, rests⟩ r' start' =>
    match (SeekingRuns.rests_iff r).mp rests with
    | ⟨T, fixed, meets⟩ =>
      have along : ∀ n, r.state n = r'.state n := fun n =>
        (Branching.law_run_state r n).trans ((congrArg (fun x => Law.orbit next x n)
          (start.trans start'.symm)).trans (Branching.law_run_state r' n).symm)
      (SeekingRuns.rests_iff r').mpr ⟨T, (congrArg next (along T)).symm.trans (fixed.trans (along T)),
        (congrArg target (along T)).mp meets⟩,
   fun assured => ⟨Law.run next s, rfl, assured (Law.run next s) rfl⟩⟩

end Determined

end Enough

end Becoming
