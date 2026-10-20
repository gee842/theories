import Becoming.Identification
import Becoming.Seeking

/-!
# Learnable: what can be learned through a map

An extrapolation proposes, from values through a map, a value of a feature the map need not
take: a map `reg : S → R` of configurations, a feature `val : S → V`, and an extrapolation
`pred : List R → Option V` that proposes at step `t` of the orbit from `s`, from the prefix
before `t` of the course through the map (`Becoming.Learning`'s `prefixOf`). It predicts the
feature from step `T` where it proposes the feature's value at every later step
(`PredictsFrom`, `Predicts`). `Becoming.Testing` shows that a claim is excluded at a formation only
through a difference that couples into it; `Becoming.Learning` that no prefix fixes the next
value; `Becoming.Identification` that in a world a list holds, elimination over the lasso
candidates predicts the course through the map within a bound. This module
states, with no premise, what a map lets an extrapolation predict.

* **Alike through the map, learned alike.** Two configurations with the same future through the
  map give every extrapolation the same prefix at every step (`prefixes_same`). So at a step
  where their features differ, a proposed value is right on at most one
  (`claim_not_right_on_both`); with the features decided it misses on one, while the two
  prefixes stay equal at every step (`missed_on_one`). An extrapolation predicting on both has
  features that agree from some step on (`agree_of_predicts_both`); where they differ at
  arbitrarily late steps, no extrapolation predicts on both (`not_predicts_on_both`), already for
  two
  configurations the law leaves unchanged (`still_not_predicts_on_both`).
* **What is read off the map is learned by an extrapolation given nothing.** Where the
  feature is read off the map (`val s = g (reg s)`), elimination over the lasso candidates on the
  values through the map, its proposals read by `g`, predicts the feature in every
  world a list holds, from `Becoming.Identification`'s bound on (`predicts_through`). It is given
  neither the configurations, nor their number, nor any value of the feature.
* **Exactly.** In a world a list holds, some extrapolation from prefixes through the map predicts
  the feature at every configuration exactly where configurations with the same
  future through the map have features that agree from some step on (`learnable_iff`). The
  extrapolation of the second direction is built from the law, the map, the feature and the list
  (`fromLaw`): no extrapolation does better, whatever it is given, since the first direction
  holds of every extrapolation. Features that go alike across the map's lumping
  (`Learning.Lumped`) are always learnable (`learnable_of_lumped`). Where the law leaves every
  configuration unchanged, they are exactly the learnable ones (`still_learnable_iff_lumped`):
  what can be learned through a map is what goes alike across its lumping, the lumping by which
  `Becoming.Learning` states generalization.
* **Two still configurations** (`Pair`). Through the map to the first of two coordinates, no
  extrapolation predicts the second at both `(true, false)` and `(true, true)`
  (`Pair.first_not_predicts`), the second not going alike across the first (`Pair.not_lumped`).
  Through the map to both, elimination over the lasso candidates predicts the second
  at every configuration from step 2 (`Pair.whole_predicts`).

Predicting the feature from some step on is learning in the limit (Gold 1967) through a map. In
the vocabulary of `Becoming.LimitVerification`, along the runs of the law, the extrapolation's
guess is fixed by the record through the map and tracks the feature (`Limit.Tracks`,
`LearnableRuns.predicts_iff_tracks`); it identifies a hypothesis (`Limit.Identifies`) where the law
leaves the feature unchanged (`LearnableRuns.learnable_iff_identifies`), and not in general
(`LearnableRuns.Merge.learnable_not_identifies`). `learnable_iff` is an observability condition in
that setting: its first direction holds of every extrapolation, while the extrapolation of its
second direction is built from the law, the map, the feature and the list, so that direction
shows existence, not an extrapolation given nothing.

Readings of this as the map bounding what is learned, as the limit of learning without a
coupling of the feature back into what is learned, or as a condition on cognition, belong to the
study, not to this module. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

universe u v w

namespace Learnable

section Rest

variable {S : Type u} {R : Type v} {V : Type w}

/-- The course from `s` through the map: the value of `reg` at each step of the orbit. -/
def course (next : S → S) (reg : S → R) (s : S) : Nat → R := fun n => reg (Law.orbit next s n)

/-- The extrapolation `pred`, from the prefix of the course through the map, proposes the
feature's value at every step from `T` on along the orbit from `s`. -/
def PredictsFrom (next : S → S) (reg : S → R) (val : S → V) (pred : List R → Option V) (s : S)
    (T : Nat) : Prop :=
  ∀ t, T ≤ t → pred (Learning.prefixOf (course next reg s) t) = some (val (Law.orbit next s t))

/-- The extrapolation predicts the feature along the orbit from `s`. -/
def Predicts (next : S → S) (reg : S → R) (val : S → V) (pred : List R → Option V) (s : S) : Prop :=
  ∃ T, PredictsFrom next reg val pred s T

end Rest

/-! ## Alike through the map, learned alike -/

section Alike

variable {S : Type u} {R : Type v} {V : Type w} {next : S → S} {reg : S → R} {val : S → V}

/-- **Configurations with the same future through the map give every extrapolation the same
prefix.** -/
theorem prefixes_same {s s' : S} (same : Law.SameFuture next reg s s') (t : Nat) :
    Learning.prefixOf (course next reg s) t = Learning.prefixOf (course next reg s') t :=
  Learning.prefix_congr fun n _ => same n

/-- **A proposal finer than the map is right on at most one.** At a step where the
features of two configurations with the same future through the map differ, a value an
extrapolation proposes is not right on both. No decision is used. -/
theorem claim_not_right_on_both (pred : List R → Option V) {s s' : S}
    (same : Law.SameFuture next reg s s') {t : Nat}
    (differ : val (Law.orbit next s t) ≠ val (Law.orbit next s' t)) :
    ¬ (pred (Learning.prefixOf (course next reg s) t) = some (val (Law.orbit next s t)) ∧
      pred (Learning.prefixOf (course next reg s') t) = some (val (Law.orbit next s' t))) :=
  fun ⟨right, right'⟩ =>
    differ (Option.some.inj
      ((right.symm.trans (congrArg pred (prefixes_same same t))).trans right'))

/-- **With the features decided, a proposed value there misses on one, and the prefixes stay
equal.** The prefix through the map is the same on both courses at every step, so it does not
show on which of them the proposal missed. -/
theorem missed_on_one [DecidableEq V] (pred : List R → Option V) {s s' : S}
    (same : Law.SameFuture next reg s s') {t : Nat}
    (differ : val (Law.orbit next s t) ≠ val (Law.orbit next s' t)) {w : V}
    (claims : pred (Learning.prefixOf (course next reg s) t) = some w) :
    (Learning.Misses (pred (Learning.prefixOf (course next reg s) t)) (val (Law.orbit next s t)) ∨
      Learning.Misses (pred (Learning.prefixOf (course next reg s') t))
        (val (Law.orbit next s' t))) ∧
    ∀ n, Learning.prefixOf (course next reg s) n = Learning.prefixOf (course next reg s') n :=
  ⟨match decEq w (val (Law.orbit next s t)) with
   | isTrue right => .inr ⟨w, (congrArg pred (prefixes_same same t)).symm.trans claims,
       fun at' => differ (right.symm.trans at')⟩
   | isFalse wrong => .inl ⟨w, claims, wrong⟩,
   prefixes_same same⟩

/-- **An extrapolation predicting on two configurations alike through the map has features that
agree from some step on.** -/
theorem agree_of_predicts_both {pred : List R → Option V} {s s' : S}
    (same : Law.SameFuture next reg s s') {T T' : Nat}
    (rests : PredictsFrom next reg val pred s T) (rests' : PredictsFrom next reg val pred s' T') :
    ∀ t, T + T' ≤ t → val (Law.orbit next s t) = val (Law.orbit next s' t) :=
  fun t late =>
    Option.some.inj (((rests t (Nat.le_trans (Nat.le_add_right T T') late)).symm.trans
      (congrArg pred (prefixes_same same t))).trans
      (rests' t (Nat.le_trans (Nat.le_add_left T' T) late)))

/-- **Where their features differ at arbitrarily late steps, no extrapolation predicts on both.** -/
theorem not_predicts_on_both (pred : List R → Option V) {s s' : S}
    (same : Law.SameFuture next reg s s')
    (differ : ∀ T, ∃ t, T ≤ t ∧ val (Law.orbit next s t) ≠ val (Law.orbit next s' t)) :
    ¬ (Predicts next reg val pred s ∧ Predicts next reg val pred s') :=
  fun ⟨⟨T, rests⟩, ⟨T', rests'⟩⟩ =>
    match differ (T + T') with
    | ⟨t, late, ne⟩ => ne (agree_of_predicts_both same rests rests' t late)

/-- A configuration the law leaves unchanged is its own orbit (`Law.fixed_rests`). -/
theorem orbit_of_still {s : S} (still : next s = s) (n : Nat) : Law.orbit next s n = s :=
  (Law.fixed_rests (target := fun _ => True) still trivial n).1

/-- **Already for two still configurations.** Where the law leaves `s` and `s'` unchanged, the
map does not tell them apart and their features differ, no extrapolation through the map predicts
the feature at both. -/
theorem still_not_predicts_on_both (pred : List R → Option V) {s s' : S} (still : next s = s)
    (still' : next s' = s') (alike : reg s = reg s') (differ : val s ≠ val s') :
    ¬ (Predicts next reg val pred s ∧ Predicts next reg val pred s') :=
  not_predicts_on_both pred
    (fun n => (congrArg reg (orbit_of_still still n)).trans
      (alike.trans (congrArg reg (orbit_of_still still' n)).symm))
    fun T => ⟨T, Nat.le_refl T, fun same =>
      differ ((congrArg val (orbit_of_still still T)).symm.trans
        (same.trans (congrArg val (orbit_of_still still' T))))⟩

/-- **Where the law leaves every configuration unchanged, a feature learned at every
configuration goes alike across the map's lumping.** -/
theorem still_lumped_of_predicts (still : ∀ s, next s = s) {pred : List R → Option V}
    (rests : ∀ s, Predicts next reg val pred s) : Learning.Lumped reg val :=
  fun s s' alike =>
    match rests s, rests s' with
    | ⟨T, at_s⟩, ⟨T', at_s'⟩ =>
      (congrArg val (orbit_of_still (still s) (T + T'))).symm.trans
        ((agree_of_predicts_both
            (fun n => (congrArg reg (orbit_of_still (still s) n)).trans
              (alike.trans (congrArg reg (orbit_of_still (still s') n)).symm))
            at_s at_s' (T + T') (Nat.le_refl _)).trans
          (congrArg val (orbit_of_still (still s') (T + T'))))

end Alike

/-! ## What is read off the map -/

section Through

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R]

/-- **What is read off the map is learned by an extrapolation given nothing.** In a world a
list holds, where the feature is read off the map, elimination over the lasso candidates on the
values through the map, its proposals read by `g`, predicts the feature from
`Becoming.Identification`'s bound on (`held_byElimination_rests`). It is given neither the
configurations, nor their number, nor any value of the feature. -/
theorem predicts_through {next : S → S} {s : S} {l : List S} (held : ∀ n, Law.orbit next s n ∈ l)
    {reg : S → R} {val : S → V} {g : R → V} (factors : ∀ s, val s = g (reg s)) :
    PredictsFrom next reg val (fun r => (Learning.byElimination Learning.lassos r).map g) s
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  fun t late =>
    (congrArg (Option.map g) (Identification.held_byElimination_rests held reg t late)).trans
      (congrArg some (factors (Law.orbit next s t)).symm)

end Through

/-! ## Exactly -/

section Exactly

/-- The first member meeting one decided condition is the first meeting another wherever the two
conditions agree on the list. -/
theorem firstFit_congr {α : Type} {p q : α → Prop} {dp : ∀ a, Decidable (p a)}
    {dq : ∀ a, Decidable (q a)} :
    ∀ {l : List α}, (∀ a, a ∈ l → (p a ↔ q a)) →
      Identification.firstFit p dp l = Identification.firstFit q dq l
  | [], _ => rfl
  | a :: l, same =>
    match Decidable.em (p a) with
    | .inl pa => (if_pos pa).trans (if_pos ((same a (List.Mem.head l)).mp pa)).symm
    | .inr npa =>
      (if_neg npa).trans ((firstFit_congr fun b mem => same b (List.Mem.tail a mem)).trans
        (if_neg fun qa => npa ((same a (List.Mem.head l)).mpr qa)).symm)

variable {S : Type} {R : Type v} {V : Type w} [DecidableEq R]

/-- The extrapolation built from the law at length `k`: among the configurations of `l`, the
first whose prefix through the map before `k` is the prefix given, and its feature `k` steps on. -/
def fromLawAt (next : S → S) (reg : S → R) (val : S → V) (l : List S) (k : Nat) (r : List R) :
    Option V :=
  (Identification.firstFit (fun x => Law.name next reg k x = r)
      (fun x => decEq (Law.name next reg k x) r) l).map
    fun x => val (Law.orbit next x k)

/-- **The extrapolation built from the law** (the law, the map, the feature and the list `l`):
from a prefix it proposes the feature of the first configuration of `l` with that prefix, as
many steps on as the prefix is long. -/
def fromLaw (next : S → S) (reg : S → R) (val : S → V) (l : List S) (r : List R) : Option V :=
  fromLawAt next reg val l r.length r

/-- **Exactly.** In a world a list holds, some extrapolation from prefixes through the map predicts
the feature at every configuration exactly where configurations with the same
future through the map have features that agree from some step on. The first direction holds of
every extrapolation, whatever it is given; the extrapolation of the second is built from the
law, the map, the feature and the list (`fromLaw`). -/
theorem learnable_iff {next : S → S} {reg : S → R} {val : S → V} {l : List S}
    (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ s, Predicts next reg val pred s) ↔
      ∀ s s', Law.SameFuture next reg s s' →
        ∃ T, ∀ t, T ≤ t → val (Law.orbit next s t) = val (Law.orbit next s' t) :=
  ⟨fun ⟨_, rests⟩ s s' same =>
    match rests s, rests s' with
    | ⟨_, at_s⟩, ⟨_, at_s'⟩ => ⟨_, agree_of_predicts_both same at_s at_s'⟩,
   fun agree => ⟨fromLaw next reg val l, fun s =>
    have closed : ∀ x, x ∈ l → next x ∈ l := fun x _ => world (next x)
    have iff_same : ∀ t, l.length + l.length - 1 ≤ t → ∀ x,
        (Law.name next reg t x = Learning.prefixOf (course next reg s) t ↔
          Law.SameFuture next reg x s) := fun _ late x =>
      ⟨fun named => (Law.sameFuture_iff_below closed (world x) (world s)).mpr fun n lt =>
          Identification.prefix_eq_iff.mp named n (Nat.lt_of_lt_of_le lt late),
       fun same => Identification.prefix_eq_iff.mpr fun n _ => same n⟩
    match Identification.firstFit_found
        (p := fun x => Law.name next reg (l.length + l.length - 1) x =
          Learning.prefixOf (course next reg s) (l.length + l.length - 1))
        (dec := fun _ => decEq _ _) (world s) rfl with
    | ⟨s₀, found⟩ =>
      have same₀ : Law.SameFuture next reg s₀ s :=
        (iff_same _ (Nat.le_refl _) s₀).mp (Identification.firstFit_sound found)
      match agree s₀ s same₀ with
      | ⟨T, agrees⟩ => ⟨l.length + l.length - 1 + T, fun t late =>
        have late_K : l.length + l.length - 1 ≤ t := Nat.le_trans (Nat.le_add_right _ T) late
        have first : Identification.firstFit
            (fun x => Law.name next reg t x = Learning.prefixOf (course next reg s) t)
            (fun x => decEq (Law.name next reg t x) (Learning.prefixOf (course next reg s) t)) l =
              some s₀ :=
          (firstFit_congr fun x _ =>
            (iff_same t late_K x).trans (iff_same _ (Nat.le_refl _) x).symm).trans found
        (congrArg (fun k => fromLawAt next reg val l k (Learning.prefixOf (course next reg s) t))
            (Learning.prefix_length _ t)).trans
          ((congrArg (Option.map fun x => val (Law.orbit next x t)) first).trans
            (congrArg some (agrees t (Nat.le_trans (Nat.le_add_left T _) late))))⟩⟩⟩

/-- **Features that go alike across the map's lumping are learnable**, under every law of a
world a list holds. -/
theorem learnable_of_lumped {next : S → S} {reg : S → R} {val : S → V} {l : List S}
    (world : ∀ s, s ∈ l) (lumped : Learning.Lumped reg val) :
    ∃ pred : List R → Option V, ∀ s, Predicts next reg val pred s :=
  (learnable_iff world).mpr fun _ _ same => ⟨0, fun t _ => lumped _ _ (same t)⟩

/-- **Where the law leaves every configuration unchanged, what can be learned through a
map is exactly what goes alike across its lumping.** -/
theorem still_learnable_iff_lumped {next : S → S} (still : ∀ s, next s = s) {reg : S → R}
    {val : S → V} {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ s, Predicts next reg val pred s) ↔ Learning.Lumped reg val :=
  ⟨fun ⟨_, rests⟩ => still_lumped_of_predicts still rests, learnable_of_lumped world⟩

end Exactly

/-! ## Two still configurations -/

namespace Pair

/-- Two coordinates, the law leaving each configuration unchanged. -/
def still : Bool × Bool → Bool × Bool := fun s => s

theorem stays (s : Bool × Bool) (n : Nat) : Law.orbit still s n = s :=
  orbit_of_still rfl n

/-- **Through the map to the first coordinate, no extrapolation predicts the second
at both `(true, false)` and `(true, true)`.** -/
theorem first_not_predicts (pred : List Bool → Option Bool) :
    ¬ (Predicts still Prod.fst Prod.snd pred (true, false) ∧
      Predicts still Prod.fst Prod.snd pred (true, true)) :=
  still_not_predicts_on_both pred rfl rfl rfl fun same => Bool.noConfusion same

/-- The second coordinate does not go alike across the first. -/
theorem not_lumped : ¬ Learning.Lumped (Prod.fst : Bool × Bool → Bool) Prod.snd :=
  fun lumped => Bool.noConfusion (lumped (true, false) (true, true) rfl)

/-- **Through the map to both, elimination over the lasso candidates predicts the
second at every configuration from step 2.** -/
theorem whole_predicts (s : Bool × Bool) :
    PredictsFrom still id Prod.snd (fun r => (Learning.byElimination Learning.lassos r).map Prod.snd) s 2 :=
  predicts_through (l := [s])
    (fun n => Eq.subst (motive := fun x => x ∈ [s]) (stays s n).symm (List.Mem.head []))
    fun _ => rfl

end Pair

end Learnable

end Becoming
