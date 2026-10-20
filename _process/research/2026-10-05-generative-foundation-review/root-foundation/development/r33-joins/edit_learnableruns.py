import sys
p = sys.argv[1]
s = open(p).read()
s = s.replace('import Becoming.Parting\n', 'import Becoming.Parting\nimport Becoming.LimitVerification\n', 1)
block = '''
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
      Limit.Tracks (guess reg pred) fun k r => some (val (r.state k)) :=
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
        Limit.Identifies g fun r => some (val (r.state 0)) := fun g =>
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
  fun ⟨g, fixed, identifies⟩ =>
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
'''
anchor = '\nend LearnableRuns\n\nend Becoming'
assert s.count(anchor) == 1
s = s.replace(anchor, '\n' + block + anchor)
open(p, 'w').write(s)
