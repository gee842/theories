import Becoming.Branching
import Becoming.Learnable
import Becoming.Parting
import Becoming.LimitVerification

/-!
# Learnable runs: what can be learned through a map along a run

`Becoming.Learnable` states what an extrapolation through a map can learn along the orbit of a
determined law. A determined law is a process of the spine (`Law.process`), and every run of it is
its orbit from where the run begins (`Branching.law_run_state`); configurations of a determined
law are alike in the frame by `reg` (`Law.frameBy`) exactly where their futures through the map
are the same (`Law.alike_iff_sameFuture`). This module states the laws of `Becoming.Learnable`
about the runs of the law and the likeness of the frame, and proves them through those laws.

* **A run's prefix is its orbit's.** The prefix through the map along a run is the prefix along
  the orbit from the run's first configuration (`prefix_eq`), so an extrapolation predicts on a run
  exactly where it predicts on that orbit (`predictsFrom_iff`, `predicts_iff`).
* **Alike in the frame, learned alike.** Two runs beginning at configurations alike in the frame
  by `reg` give every extrapolation the same prefix at every step (`prefixes_same`); an
  extrapolation predicting on both has features that agree from some step on
  (`agree_of_predicts_both`), and where their features differ at arbitrarily late steps no
  extrapolation predicts on both (`not_predicts_on_both`).
* **What is read off the map is learned along every run a list holds** (`predicts_through`), by
  elimination over the lasso candidates given nothing.
* **Exactly.** In a world a list holds, some extrapolation predicts the feature along
  every run of the law exactly where runs beginning alike in the frame have features that agree
  from some step on (`learnable_iff`); where the law leaves every configuration unchanged,
  exactly where the feature goes alike across the map's lumping (`still_learnable_iff_lumped`).
* **The case through a map of learning in the limit.** An extrapolation's guess along the runs
  (`guess`) is fixed by the record through the map (`FixedThrough`, `guess_fixedThrough`), and so
  by the record in the sense of `Becoming.LimitVerification` (`FixedThrough.byRecord`). It predicts
  the feature along every run exactly where it tracks the feature in the limit (`Limit.Tracks`,
  `predicts_iff_tracks`). Some guess fixed by the record through the map tracks the feature where
  the feature is learnable, with no premise (`tracks_of_learnable`); any such guess gives runs
  beginning alike in the frame features that agree from some step on (`agree_of_tracks`); so in a
  world a list holds, learnable through the map is exactly that some guess fixed by the record
  through the map tracks the feature (`learnable_iff_tracks`). Where the law leaves the feature
  unchanged (`val (next s) = val s`), tracking is identification of the feature at the run's start
  (`Limit.Identifies`, `learnable_iff_identifies`). Without that premise it is not: in `Merge`
  every configuration goes to `0` and the feature is whether a configuration is `1`; it is learned
  through the map that tells nothing apart, and no guess fixed by that record identifies it at the
  start (`Merge.learnable_not_identifies`).

Readings of this as learning along a course of the unfolding, rather than about a configuration
set apart from it, belong to the study, not to this module. No ethical predicate, ranking or axiom
occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace LearnableRuns

section Along

variable {S : Type u} {R : Type v} {V : Type w} {next : S → S}

/-- The course of a run through the map: the value of `reg` at each of its steps
(`Parting.course` on a run of the law's process). -/
def course (reg : S → R) (r : Run (Law.process next)) : Nat → R := Parting.course reg r

/-- The extrapolation `pred`, from the prefix of the run's course through the map, proposes the
feature's value at every step from `T` on. -/
def PredictsFrom (reg : S → R) (val : S → V) (pred : List R → Option V) (r : Run (Law.process next))
    (T : Nat) : Prop :=
  ∀ t, T ≤ t → pred (Learning.prefixOf (course reg r) t) = some (val (r.state t))

/-- The extrapolation predicts the feature along the run. -/
def Predicts (reg : S → R) (val : S → V) (pred : List R → Option V) (r : Run (Law.process next)) :
    Prop :=
  ∃ T, PredictsFrom reg val pred r T

/-- **A run's prefix through the map is the prefix along the orbit from where it begins.** -/
theorem prefix_eq (reg : S → R) (r : Run (Law.process next)) (t : Nat) :
    Learning.prefixOf (course reg r) t = Learning.prefixOf (Learnable.course next reg (r.state 0)) t :=
  Learning.prefix_congr fun n _ => congrArg reg (Branching.law_run_state r n)

/-- **An extrapolation predicts on a run from `T` exactly where it predicts from
`T` on the orbit from where the run begins.** -/
theorem predictsFrom_iff {reg : S → R} {val : S → V} {pred : List R → Option V}
    (r : Run (Law.process next)) (T : Nat) :
    PredictsFrom reg val pred r T ↔ Learnable.PredictsFrom next reg val pred (r.state 0) T :=
  ⟨fun rests t late =>
    (congrArg pred (prefix_eq reg r t)).symm.trans
      ((rests t late).trans (congrArg (fun x => some (val x)) (Branching.law_run_state r t))),
   fun rests t late =>
    (congrArg pred (prefix_eq reg r t)).trans
      ((rests t late).trans (congrArg (fun x => some (val x)) (Branching.law_run_state r t)).symm)⟩

theorem predicts_iff {reg : S → R} {val : S → V} {pred : List R → Option V}
    (r : Run (Law.process next)) :
    Predicts reg val pred r ↔ Learnable.Predicts next reg val pred (r.state 0) :=
  ⟨fun ⟨T, rests⟩ => ⟨T, (predictsFrom_iff r T).mp rests⟩,
   fun ⟨T, rests⟩ => ⟨T, (predictsFrom_iff r T).mpr rests⟩⟩

/-- Runs beginning alike in the frame by `reg` have the same future through the map along
the runs. -/
theorem course_same {reg : S → R} {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    (n : Nat) : reg (r.state n) = reg (r'.state n) :=
  (congrArg reg (Branching.law_run_state r n)).trans
    ((Law.alike_iff_sameFuture.mp alike n).trans
      (congrArg reg (Branching.law_run_state r' n)).symm)

/-- **Runs beginning alike in the frame give every extrapolation the same prefix.** -/
theorem prefixes_same {reg : S → R} {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    (t : Nat) : Learning.prefixOf (course reg r) t = Learning.prefixOf (course reg r') t :=
  Learning.prefix_congr fun n _ => course_same alike n

/-- **An extrapolation predicting on two runs beginning alike in the frame has features that agree
from some step on.** -/
theorem agree_of_predicts_both {reg : S → R} {val : S → V} {pred : List R → Option V}
    {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    {T T' : Nat} (rests : PredictsFrom reg val pred r T) (rests' : PredictsFrom reg val pred r' T') :
    ∀ t, T + T' ≤ t → val (r.state t) = val (r'.state t) :=
  fun t late =>
    (congrArg val (Branching.law_run_state r t)).trans
      ((Learnable.agree_of_predicts_both (Law.alike_iff_sameFuture.mp alike)
          ((predictsFrom_iff r T).mp rests) ((predictsFrom_iff r' T').mp rests') t late).trans
        (congrArg val (Branching.law_run_state r' t)).symm)

/-- **Where the features of two runs beginning alike in the frame differ at arbitrarily late
steps, no extrapolation predicts on both.** -/
theorem not_predicts_on_both {reg : S → R} {val : S → V} (pred : List R → Option V)
    {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0))
    (differ : ∀ T, ∃ t, T ≤ t ∧ val (r.state t) ≠ val (r'.state t)) :
    ¬ (Predicts reg val pred r ∧ Predicts reg val pred r') :=
  fun ⟨rests, rests'⟩ =>
    Learnable.not_predicts_on_both pred (Law.alike_iff_sameFuture.mp alike)
      (fun T => match differ T with
        | ⟨t, late, ne⟩ => ⟨t, late, fun same => ne
            ((congrArg val (Branching.law_run_state r t)).trans
              (same.trans (congrArg val (Branching.law_run_state r' t)).symm))⟩)
      ⟨(predicts_iff r).mp rests, (predicts_iff r').mp rests'⟩

end Along

section Through

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

/-- **What is read off the map is learned along every run a list holds**, by elimination
over the lasso candidates on the values through the map, given nothing, from
`Becoming.Identification`'s bound on. -/
theorem predicts_through (r : Run (Law.process next)) {l : List S} (held : ∀ n, r.state n ∈ l)
    {reg : S → R} {val : S → V} {g : R → V} (factors : ∀ s, val s = g (reg s)) :
    PredictsFrom reg val (fun x => (Learning.byElimination Learning.lassos x).map g) r
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  (predictsFrom_iff r _).mpr
    (Learnable.predicts_through
      (fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state r n) (held n))
      factors)

end Through

section Exactly

variable {S : Type} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

/-- **Exactly.** In a world a list holds, some extrapolation predicts the feature
along every run of the law exactly where runs beginning alike in the frame by `reg` have features
that agree from some step on. -/
theorem learnable_iff {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      ∀ r r' : Run (Law.process next),
        Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0) →
          ∃ T, ∀ t, T ≤ t → val (r.state t) = val (r'.state t) :=
  ⟨fun ⟨_, rests⟩ r r' alike =>
    match rests r, rests r' with
    | ⟨_, at_r⟩, ⟨_, at_r'⟩ => ⟨_, agree_of_predicts_both alike at_r at_r'⟩,
   fun agree =>
    match (Learnable.learnable_iff (next := next) (reg := reg) (val := val) world).mpr
        (fun s s' same => agree (Law.run next s) (Law.run next s')
          (Law.alike_iff_sameFuture.mpr same)) with
    | ⟨pred, rests⟩ => ⟨pred, fun r => (predicts_iff r).mpr (rests (r.state 0))⟩⟩

/-- **Where the law leaves every configuration unchanged, a feature is learnable along every run
exactly where it goes alike across the map's lumping.** -/
theorem still_learnable_iff_lumped (still : ∀ s, next s = s) {reg : S → R} {val : S → V}
    {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      Learning.Lumped reg val :=
  ⟨fun ⟨pred, rests⟩ => (Learnable.still_learnable_iff_lumped still world).mp
      ⟨pred, fun s => (predicts_iff (Law.run next s)).mp (rests (Law.run next s))⟩,
   fun lumped => match (Learnable.still_learnable_iff_lumped still world).mpr lumped with
    | ⟨pred, rests⟩ => ⟨pred, fun r => (predicts_iff r).mpr (rests (r.state 0))⟩⟩

end Exactly


/-! ## The case through a map of learning in the limit

`Becoming.LimitVerification` states learning in the limit over the runs of any process: a guess of
values tracks a target where, from some horizon on, it is the target's value at the horizon
(`Limit.Tracks`), and identifies a hypothesis where the target does not change with the horizon
(`Limit.Identifies`). An extrapolation through a map is the case of a guess fixed by the record
through the map. -/

section Limit

variable {S : Type u} {R : Type v} {V : Type w} {next : S → S}

/-- The guess of an extrapolation along the runs of the law: at horizon `k`, what it proposes from
the prefix before `k` of the run's course through the map. -/
def guess (reg : S → R) (pred : List R → Option V) : Nat → Run (Law.process next) → Option V :=
  fun k r => pred (Learning.prefixOf (course reg r) k)

/-- A guess of values is fixed by the record through `reg`: at horizon `k` it is the same on runs
whose courses through the map agree before `k`. -/
def FixedThrough {W : Type w} (reg : S → R) (g : Nat → Run (Law.process next) → W) : Prop :=
  ∀ k (r r' : Run (Law.process next)), (∀ n, n < k → reg (r.state n) = reg (r'.state n)) →
    g k r = g k r'

/-- **An extrapolation's guess is fixed by the record through the map.** -/
theorem guess_fixedThrough (reg : S → R) (pred : List R → Option V) :
    FixedThrough (next := next) reg (guess reg pred) :=
  fun _ _ _ agree => congrArg pred (Learning.prefix_congr agree)

/-- **A guess fixed by the record through the map is fixed by the record** in the sense of
`Becoming.LimitVerification`: on runs agreeing up to `k` it is the same at `k`. -/
theorem FixedThrough.byRecord {W : Type w} {reg : S → R} {g : Nat → Run (Law.process next) → W}
    (fixed : FixedThrough reg g) (k : Nat) (r r' : Run (Law.process next)) (agree : r.AgreeUpTo k r') :
    g k r = g k r' :=
  fixed k r r' fun n before => congrArg reg (agree.1 n (Nat.le_of_lt before))

/-- **An extrapolation predicts the feature along every run exactly where its guess tracks the
feature in the limit.** -/
theorem predicts_iff_tracks {reg : S → R} {val : S → V} {pred : List R → Option V} :
    (∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      Limit.Tracks (guess (next := next) reg pred) fun k r => some (val (r.state k)) :=
  Iff.rfl

/-- **Tracking through the map needs runs beginning alike in the frame to agree from some step
on.** A guess fixed by the record through the map that tracks the feature along every run gives
runs beginning alike in the frame by `reg` features that agree from some step on. -/
theorem agree_of_tracks {reg : S → R} {val : S → V} {g : Nat → Run (Law.process next) → Option V}
    (fixed : FixedThrough reg g) (tracks : Limit.Tracks g fun k r => some (val (r.state k)))
    {r r' : Run (Law.process next)}
    (alike : Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0)) :
    ∃ T, ∀ t, T ≤ t → val (r.state t) = val (r'.state t) :=
  match tracks r, tracks r' with
  | ⟨n, at_r⟩, ⟨n', at_r'⟩ => ⟨n + n', fun t le =>
    Option.some.inj ((at_r t (Nat.le_trans (Nat.le_add_right n n') le)).symm.trans
      ((fixed t r r' fun m _ => course_same alike m).trans
        (at_r' t (Nat.le_trans (Nat.le_add_left n' n) le))))⟩

/-- **Learnable through the map, then some guess fixed by its record tracks the feature**, with no
premise: the extrapolation's own guess. -/
theorem tracks_of_learnable {reg : S → R} {val : S → V}
    (learnable : ∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) :
    ∃ g : Nat → Run (Law.process next) → Option V,
      FixedThrough reg g ∧ Limit.Tracks g fun k r => some (val (r.state k)) :=
  match learnable with
  | ⟨pred, predicts⟩ => ⟨guess reg pred, guess_fixedThrough reg pred, predicts⟩

/-- Along a run of the law, a feature the law leaves unchanged stands at every step as at the
first. -/
theorem val_invariant {val : S → V} (invariant : ∀ s, val (next s) = val s)
    (r : Run (Law.process next)) : ∀ k, val (r.state k) = val (r.state 0)
  | 0 => rfl
  | k + 1 => (congrArg val (r.step k)).trans ((invariant _).trans (val_invariant invariant r k))

end Limit

section LimitExactly

variable {S : Type} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

/-- **Learnable through the map exactly where some guess fixed by the record through the map
tracks the feature in the limit**, in a world a list holds. The forward direction needs no list
(`tracks_of_learnable`); the converse goes through `learnable_iff`, which builds the extrapolation
from the law, the map, the feature and the list. -/
theorem learnable_iff_tracks {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      ∃ g : Nat → Run (Law.process next) → Option V,
        FixedThrough reg g ∧ Limit.Tracks g fun k r => some (val (r.state k)) :=
  ⟨tracks_of_learnable,
   fun ⟨_, fixed, tracks⟩ => (learnable_iff world).mpr fun _ _ alike =>
     agree_of_tracks fixed tracks alike⟩

/-- **Where the law leaves the feature unchanged, learnable through the map is identification in
the limit.** In a world a list holds, with `val (next s) = val s` for every `s`, some extrapolation
predicts the feature along every run exactly where some guess fixed by the record through the map
identifies, in the limit, the feature at the run's start. -/
theorem learnable_iff_identifies {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l)
    (invariant : ∀ s, val (next s) = val s) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      ∃ g : Nat → Run (Law.process next) → Option V,
        FixedThrough reg g ∧ Limit.Identifies g fun r => some (val (r.state 0)) :=
  have same : ∀ g : Nat → Run (Law.process next) → Option V,
      Limit.Tracks g (fun k r => some (val (r.state k))) ↔
        Limit.Identifies g fun r => some (val (r.state 0)) := fun _ =>
    ⟨fun tracks r => match tracks r with
      | ⟨n, at_r⟩ => ⟨n, fun k le => (at_r k le).trans
          (congrArg some (val_invariant invariant r k))⟩,
     fun identifies r => match identifies r with
      | ⟨n, at_r⟩ => ⟨n, fun k le => (at_r k le).trans
          (congrArg some (val_invariant invariant r k)).symm⟩⟩
  (learnable_iff_tracks world).trans
    ⟨fun ⟨g, fixed, tracks⟩ => ⟨g, fixed, (same g).mp tracks⟩,
     fun ⟨g, fixed, identifies⟩ => ⟨g, fixed, (same g).mpr identifies⟩⟩

end LimitExactly

/-! ## Witness: learnable, and the start not identified -/

namespace Merge

/-- Every configuration goes to `0`. -/
def next : Nat → Nat := fun _ => 0

/-- The feature: whether the configuration is `1`. -/
def val (s : Nat) : Bool := Nat.beq s 1

/-- From the first step on, every run of the law is at `0`. -/
theorem at_zero (r : Run (Law.process next)) (t : Nat) : r.state (t + 1) = 0 :=
  r.step t

/-- **Learnable through the map that tells nothing apart**: proposing `false` is right from step 1
on, along every run. -/
theorem learnable :
    ∃ pred : List Unit → Option Bool, ∀ r : Run (Law.process next), Predicts (fun _ => ()) val pred r :=
  ⟨fun _ => some false, fun r => ⟨1, fun t le =>
    match t, le with
    | t + 1, _ => congrArg (fun s => some (val s)) (at_zero r t).symm⟩⟩

/-- **The start is not identified.** No guess fixed by the record through the map identifies in the
limit the feature at the run's start: the runs from `0` and from `1` have the same record through
the map, and the feature at their starts differs. -/
theorem not_identifies :
    ¬ ∃ g : Nat → Run (Law.process next) → Option Bool,
        FixedThrough (fun _ => ()) g ∧ Limit.Identifies g fun r => some (val (r.state 0)) :=
  fun ⟨_, fixed, identifies⟩ =>
    match identifies (Law.run next 0), identifies (Law.run next 1) with
    | ⟨n, at_zero'⟩, ⟨n', at_one⟩ =>
      Bool.noConfusion (Option.some.inj
        ((at_zero' (n + n') (Nat.le_add_right n n')).symm.trans
          ((fixed (n + n') _ _ fun _ _ => rfl).trans (at_one (n + n') (Nat.le_add_left n' n)))))

/-- **So identification of the start is not the general case**: the feature is learnable through
the map, the law changes it (`val (next 1) ≠ val 1`), and no guess fixed by the record identifies
it at the start. -/
theorem learnable_not_identifies :
    (∃ pred : List Unit → Option Bool, ∀ r : Run (Law.process next), Predicts (fun _ => ()) val pred r) ∧
      val (next 1) ≠ val 1 ∧
      ¬ ∃ g : Nat → Run (Law.process next) → Option Bool,
        FixedThrough (fun _ => ()) g ∧ Limit.Identifies g fun r => some (val (r.state 0)) :=
  ⟨learnable, fun same => Bool.noConfusion same, not_identifies⟩

end Merge

end LearnableRuns

end Becoming
