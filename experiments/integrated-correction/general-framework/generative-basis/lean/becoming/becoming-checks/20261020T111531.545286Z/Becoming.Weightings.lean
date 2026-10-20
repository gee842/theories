import Becoming.Boundaries

/-!
# Weightings: what every standpoint's weighting ranks, and what the step across standpoints reaches

The ethics of the chapter rests on two premises: the continuation condition fixes scope (whose
losses count) and calling widening better (C) fixes order. `Becoming.Boundaries` decomposed the
condition into the self's presupposition and the step of invariance. This module states what the
step reaches when it is taken across standpoints rather than across drawings of a self, and what
order every standpoint shares when each weighs what can form in its own way.

* **Weighted counts.** Over a finite list of items (steps and formations), a course is the items it
  admits (a Bool-valued family), and a weighting gives each item a natural weight; the weighted
  count adds the weights of the admitted items (`Weighting.weighed`). A weighting is positive when
  it counts every listed item (`Weighting.Positive`).
* **Widening is what every positive weighting ranks higher.** Inclusion never lowers a weighted
  count (`Weighting.weighed_le_of_includes`); every positive weighting ranks a widening strictly
  higher (`Weighting.weighed_lt_of_widens`); where one course admits an item the other does not,
  some positive weighting ranks it higher (`Weighting.outweighs`), so a mixed comparison is decided
  both ways by positive weightings (`Weighting.mixed_either_way`); hence on the listed items one
  course widens another exactly when every positive weighting ranks it higher
  (`Weighting.widens_iff_every_positive`). On a web, where what either level path admits is listed
  and admission is decided, this is `Web.Widens` itself (`Web.widens_iff_every_weighting`).
* **A weight of zero ties.** Where every item a course admits beyond another weighs nothing, the
  two weigh the same (`Weighting.weighed_eq_of_unweighted`): a weighting that leaves an item out
  does not rank a widening that adds only that item.
* **The same weight for every item ranks by number.** Under one positive weight for all items, a
  course weighs more exactly when it admits more items (`Weighting.weighed_const`,
  `Weighting.neutral_ranks_by_number`).
* **Closing is never required.** Where the levels `l'` admit a formation at a step and `l` do not,
  `l` neither widens nor keeps `l'` (`Web.not_widens_of_closes`).
* **What the step across standpoints reaches.** Let each standpoint's presupposition about its own
  continuation hold (sub-true along the empty relation) and let significance be
  standpoint-invariant. Then the continuation of every standpoint's center has significance from
  every standpoint (`atCenters_least`), and the significance of the centers' continuation
  (`atCenters`) meets both premises (`atCenters_presupposed`, `atCenters_standpointInvariant`):
  what the two premises force is exactly that the centers count (`forced_iff_center`). It is the
  continuation condition exactly when every formation is some standpoint's center
  (`unrestricted_atCenters_iff`). Retaining under it is admitting every center the other path
  admits (`Web.retains_atCenters_iff`).
* **What a standpoint's own presupposition reaches.** Along a relation, what every significance
  making `p`'s presupposition sub-true at `f`'s closure gives significance to is exactly what lies
  within the closure (`forced_iff_within`).
* **Every relation one at a time, and being related at all.** The presupposition sub-true along
  every relation of a family is significance over the union of the closures
  (`subTrue_every_iff`); drawn along being related by some relation of the family (`Related`) it
  gives each of them (`subTrue_every_of_related`), and can say more: in `Chain` the third formation
  lies within the first's closure along being related at all and within no closure along a single
  relation (`Chain.third_related`, `Chain.third_not_within`, `Chain.every_not_related`).
* **Where the narrower scope and the condition part.** In `Clearing`, with the clearer the only
  standpoint's center, the clearer's part retains what has significance at the centers, while
  under the continuation condition it loses the dweller (`Clearing.centers_retain_yet_loses`).

**Reading (the AI's; the argument is in the chapter
`theories/becoming/chapters/THE-STEP-OF-INVARIANCE.md`).** Read a
positive weighting as one standpoint's order, partial in how much it weighs each formation's
possibility but counting all of them, and the order every such standpoint shares as the impartial
order. Then the impartial order is exactly C, the comparisons partiality may decide are exactly the
mixed ones, a weight of zero is a denial of scope, and a weighting the same for every formation
counts numbers. Read the centers as the formations that hold their own continuation significant
(what "wants its continuation"); then the step across standpoints, Gewirth's step, gives
significance to exactly them, and "anything" needs a further premise, that every formation is a
center or lies within some center's closure.

What is not derived: that a standpoint's order is a positive weighting (additivity and the sign of
the weights are supplied); which weighting a standpoint has; that the impartial order is what every
standpoint shares rather than one privileged weighting; which formations are centers; the step of
invariance itself. The representation commits to finite listings of steps and formations,
two-valued admission and natural-number weights. No ethical predicate or axiom occurs.
-/

namespace Becoming

/-! ## Weighted counts of what a course admits -/

namespace Weighting

variable {X : Type}

/-- The weighted count of the listed items a course admits: each admitted item counts its
weight. -/
def weighed (items : List X) (w : X → Nat) (a : X → Bool) : Nat :=
  total items fun x => cond (a x) (w x) 0

/-- A weighting is positive on the listed items: it counts every one of them. -/
def Positive (items : List X) (w : X → Nat) : Prop :=
  ∀ x, x ∈ items → 0 < w x

/-- On the listed items, `a` admits every item `b` admits. -/
def IncludesOn (items : List X) (a b : X → Bool) : Prop :=
  ∀ x, x ∈ items → b x = true → a x = true

/-- On the listed items, `a` admits an item `b` does not. -/
def ExceedsOn (items : List X) (a b : X → Bool) : Prop :=
  ∃ x, x ∈ items ∧ a x = true ∧ b x = false

/-- On the listed items, `a` widens `b`: it admits every item `b` admits, and one more. -/
def WidensOn (items : List X) (a b : X → Bool) : Prop :=
  IncludesOn items a b ∧ ExceedsOn items a b

/-- On the listed items, `a` and `b` are mixed: each admits an item the other does not. -/
def MixedOn (items : List X) (a b : X → Bool) : Prop :=
  ExceedsOn items a b ∧ ExceedsOn items b a

theorem term_le {w : Nat} : ∀ {a b : Bool}, (b = true → a = true) → cond b w 0 ≤ cond a w 0
  | _, false, _ => Nat.zero_le _
  | true, true, _ => Nat.le_refl w
  | false, true, kept => Bool.noConfusion (kept rfl)

theorem term_lt {w : Nat} (positive : 0 < w) :
    ∀ {a b : Bool}, a = true → b = false → cond b w 0 < cond a w 0
  | _, _, rfl, rfl => positive

theorem total_lt {p q : X → Nat} :
    ∀ {as : List X}, (∀ a, a ∈ as → p a ≤ q a) → (∃ a, a ∈ as ∧ p a < q a) →
      total as p < total as q
  | [], _, ⟨_, mem, _⟩ => nomatch mem
  | a :: as, le, ⟨b, mem, lt⟩ => match mem_cons_cases mem with
    | .inl same =>
      Nat.add_lt_add_of_lt_of_le (Eq.subst (motive := fun y => p y < q y) same lt)
        (total_le as fun c listed => le c (.tail a listed))
    | .inr rest =>
      Nat.add_lt_add_of_le_of_lt (le a (.head as))
        (total_lt (fun c listed => le c (.tail a listed)) ⟨b, rest, lt⟩)

theorem total_congr_on {p q : X → Nat} :
    ∀ {as : List X}, (∀ a, a ∈ as → p a = q a) → total as p = total as q
  | [], _ => rfl
  | a :: as, same =>
    (congrArg (· + total as p) (same a (.head as))).trans
      (congrArg (q a + ·) (total_congr_on fun c listed => same c (.tail a listed)))

/-- **Inclusion never lowers a weighted count**, whatever the weights. -/
theorem weighed_le_of_includes {items : List X} {a b : X → Bool} (w : X → Nat)
    (includes : IncludesOn items a b) : weighed items w b ≤ weighed items w a :=
  total_le items fun x listed => term_le (includes x listed)

/-- **Every positive weighting ranks a widening higher.** -/
theorem weighed_lt_of_widens {items : List X} {a b : X → Bool} {w : X → Nat}
    (positive : Positive items w) (widens : WidensOn items a b) :
    weighed items w b < weighed items w a :=
  match widens.2 with
  | ⟨x, listed, admits, not⟩ =>
    total_lt (fun y member => term_le (widens.1 y member))
      ⟨x, listed, term_lt (positive x listed) admits not⟩

/-- **A weight of zero on what a course adds ties it with the course it includes**: where every
item `a` admits beyond `b` weighs nothing, the weighted counts agree, so a widening that adds
only such items is not ranked. -/
theorem weighed_eq_of_unweighted {items : List X} {a b : X → Bool} {w : X → Nat}
    (includes : IncludesOn items a b)
    (unweighted : ∀ x, x ∈ items → a x = true → b x = false → w x = 0) :
    weighed items w a = weighed items w b :=
  total_congr_on fun x listed => match ha : a x, hb : b x with
    | true, true => rfl
    | true, false => unweighted x listed ha hb
    | false, false => rfl
    | false, true => Bool.noConfusion (ha.symm.trans (includes x listed hb))

/-- Comparing what two courses admit item by item: either `a` admits an item `b` does not, or
`b` admits every item `a` admits. -/
theorem exceeds_or_includes (a b : X → Bool) :
    ∀ items : List X, ExceedsOn items a b ∨ IncludesOn items b a
  | [] => .inr fun _ member => nomatch member
  | x :: rest => match exceeds_or_includes a b rest with
    | .inl ⟨y, listed, admits, not⟩ => .inl ⟨y, .tail x listed, admits, not⟩
    | .inr includes => match ha : a x, hb : b x with
      | true, false => .inl ⟨x, .head rest, ha, hb⟩
      | true, true => .inr fun y member admits => match mem_cons_cases member with
        | .inl same => Eq.subst (motive := fun z => b z = true) same.symm hb
        | .inr listed => includes y listed admits
      | false, _ => .inr fun y member admits => match mem_cons_cases member with
        | .inl same => Bool.noConfusion
            (ha.symm.trans (Eq.subst (motive := fun z => a z = true) same admits))
        | .inr listed => includes y listed admits

/-- The weighting that puts weight `M` on what `b` admits beyond `a` and one on every other
item. -/
def outweighing (M : Nat) (a b : X → Bool) : X → Nat :=
  fun x => cond (b x && !a x) M 1

theorem cond_pos (M : Nat) : ∀ v : Bool, 0 < cond v (M + 1) 1
  | true => Nat.succ_pos M
  | false => Nat.succ_pos 0

theorem outweighing_positive (M : Nat) (a b : X → Bool) (items : List X) :
    Positive items (outweighing (M + 1) a b) :=
  fun x _ => cond_pos M (b x && !a x)

theorem outweighing_term_le_one {M : Nat} : ∀ (ax bx : Bool),
    cond ax (cond (bx && !ax) M 1) 0 ≤ 1
  | true, true => Nat.le_refl 1
  | true, false => Nat.le_refl 1
  | false, _ => Nat.zero_le 1

theorem outweighing_term_at {M : Nat} : ∀ {ax bx : Bool}, bx = true → ax = false →
    M ≤ cond bx (cond (bx && !ax) M 1) 0
  | _, _, rfl, rfl => Nat.le_refl M

/-- **A course admitting an item the other does not is ranked higher by some positive
weighting.** -/
theorem outweighs {items : List X} {a b : X → Bool} (exceeds : ExceedsOn items b a) :
    ∃ w, Positive items w ∧ weighed items w a < weighed items w b :=
  ⟨outweighing (items.length + 1) a b, outweighing_positive items.length a b items,
   match exceeds with
   | ⟨_, listed, admits, not⟩ =>
     Nat.lt_of_le_of_lt
       (Nat.le_trans (total_le items fun y _ => outweighing_term_le_one (a y) (b y))
         (Nat.le_of_eq (total_ones items)))
       (Nat.lt_of_lt_of_le (Nat.lt_succ_self items.length)
         (Nat.le_trans (outweighing_term_at admits not)
           (le_total_of_mem (q := fun y => cond (b y) (outweighing (items.length + 1) a b y) 0)
             listed)))⟩

/-- **A mixed comparison is decided both ways by positive weightings**: some positive weighting
ranks the one higher, and some the other. -/
theorem mixed_either_way {items : List X} {a b : X → Bool} (mixed : MixedOn items a b) :
    (∃ w, Positive items w ∧ weighed items w b < weighed items w a) ∧
      ∃ w, Positive items w ∧ weighed items w a < weighed items w b :=
  ⟨outweighs mixed.1, outweighs mixed.2⟩

/-- **Widening is what every positive weighting ranks higher.** On the listed items, `a` widens
`b` exactly when every weighting positive on them weighs `a` above `b`. -/
theorem widens_iff_every_positive {items : List X} {a b : X → Bool} :
    WidensOn items a b ↔ ∀ w, Positive items w → weighed items w b < weighed items w a :=
  ⟨fun widens _ positive => weighed_lt_of_widens positive widens,
   fun every =>
    ⟨fun x listed admits => match h : a x with
      | true => rfl
      | false => match outweighs ⟨x, listed, admits, h⟩ with
        | ⟨w, positive, lt⟩ => absurd (every w positive) (Nat.lt_asymm lt),
     match exceeds_or_includes a b items with
     | .inl exceeds => exceeds
     | .inr includes =>
       absurd (every (fun _ => 1) fun _ _ => Nat.succ_pos 0)
         (Nat.not_lt_of_le (weighed_le_of_includes _ includes))⟩⟩

theorem cond_mul (k : Nat) : ∀ v : Bool, cond v k 0 = k * cond v 1 0
  | true => (Nat.mul_one k).symm
  | false => (Nat.mul_zero k).symm

/-- Under one weight `k` for every item, the weighted count is `k` times the number of listed
items admitted. -/
theorem weighed_const (k : Nat) (items : List X) (a : X → Bool) :
    weighed items (fun _ => k) a = k * weighed items (fun _ => 1) a :=
  (total_congr (fun x => cond_mul k (a x)) items).trans
    (total_mul k (fun x => cond (a x) 1 0) items)

theorem mul_lt_mul_pos {k m n : Nat} (positive : 0 < k) (lt : m < n) : k * m < k * n :=
  match k, positive with
  | j + 1, _ =>
    Eq.subst (motive := fun x => x < (j + 1) * n) (Nat.succ_mul j m).symm
      (Eq.subst (motive := fun y => j * m + m < y) (Nat.succ_mul j n).symm
        (Nat.add_lt_add_of_le_of_lt (Nat.mul_le_mul_left j (Nat.le_of_lt lt)) lt))

theorem lt_of_mul_lt {k m n : Nat} (lt : k * m < k * n) : m < n :=
  match Nat.lt_or_ge m n with
  | .inl less => less
  | .inr ge => absurd lt (Nat.not_lt_of_le (Nat.mul_le_mul_left k ge))

/-- **A weighting the same for every item ranks by number.** Under one positive weight for every
item, one course is weighed above another exactly when it admits more of the listed items. -/
theorem neutral_ranks_by_number {k : Nat} (positive : 0 < k) (items : List X) (a b : X → Bool) :
    weighed items (fun _ => k) b < weighed items (fun _ => k) a ↔
      weighed items (fun _ => 1) b < weighed items (fun _ => 1) a :=
  ⟨fun lt => lt_of_mul_lt
      (Eq.subst (motive := fun x => x < k * weighed items (fun _ => 1) a) (weighed_const k items b)
        (Eq.subst (motive := fun y => weighed items (fun _ => k) b < y) (weighed_const k items a)
          lt)),
   fun lt =>
    Eq.subst (motive := fun x => x < weighed items (fun _ => k) a) (weighed_const k items b).symm
      (Eq.subst (motive := fun y => k * weighed items (fun _ => 1) b < y)
        (weighed_const k items a).symm (mul_lt_mul_pos positive lt))⟩

end Weighting

/-! ## Weightings of what a web's levels admit -/

namespace Web

variable {F C : Type} {W : Web F C}

/-- A decision of admission at listed steps and formations: `admitted l (t, f)` is true exactly
when the levels `l` admit `f` at `t`. -/
def DecidesAdmission (W : Web F C) (admitted : (Nat → C → Nat) → Nat × F → Bool) : Prop :=
  ∀ l i, admitted l i = true ↔ W.Admits (l i.1) i.1 i.2

/-- Every step and formation the level path admits is listed. -/
def ListsAdmitted (W : Web F C) (items : List (Nat × F)) (l : Nat → C → Nat) : Prop :=
  ∀ t f, W.Admits (l t) t f → (t, f) ∈ items

/-- **Widening is what every positive weighting ranks higher.** Where what either level path
admits is listed, `l` widens `l'` exactly when every weighting positive on the listed steps and
formations weighs what `l` admits above what `l'` admits. -/
theorem widens_iff_every_weighting {admitted : (Nat → C → Nat) → Nat × F → Bool}
    (decides : DecidesAdmission W admitted) {items : List (Nat × F)} {l l' : Nat → C → Nat}
    (listed : ListsAdmitted W items l) (listed' : ListsAdmitted W items l') :
    W.Widens l l' ↔ ∀ w, Weighting.Positive items w →
      Weighting.weighed items w (admitted l') < Weighting.weighed items w (admitted l) :=
  Iff.trans
    ⟨fun widens =>
      ⟨fun x _ admits => (decides l x).mpr (widens.1 x.1 x.2 ((decides l' x).mp admits)),
       match widens.2 with
       | ⟨t, f, admits, not⟩ => ⟨(t, f), listed t f admits, (decides l (t, f)).mpr admits,
           match h : admitted l' (t, f) with
           | true => absurd ((decides l' (t, f)).mp h) not
           | false => rfl⟩⟩,
     fun widens =>
      ⟨fun t f admits => (decides l (t, f)).mp
         (widens.1 (t, f) (listed' t f admits) ((decides l' (t, f)).mpr admits)),
       match widens.2 with
       | ⟨x, _, admits, not⟩ => ⟨x.1, x.2, (decides l x).mp admits,
           fun admits' => Bool.noConfusion (not.symm.trans ((decides l' x).mpr admits'))⟩⟩⟩
    Weighting.widens_iff_every_positive

/-- **Closing is never required.** Where the levels `l'` admit a formation at a step and the
levels `l` do not, `l` neither widens `l'` nor keeps it the same: a comparison by widening never
ranks the course in which something is closed above the course in which it is not. -/
theorem not_widens_of_closes {l l' : Nat → C → Nat} {t : Nat} {f : F}
    (admits : W.Admits (l' t) t f) (closed : ¬ W.Admits (l t) t f) :
    ¬ W.Widens l l' ∧ ¬ W.Keeps l l' :=
  ⟨fun widens => closed (widens.1 t f admits), fun keeps => closed (keeps.1 t f admits)⟩

end Web

/-! ## What the step across standpoints reaches -/

variable {F Pos : Type}

/-- The significance of the continuation of what is some standpoint's center, from every
standpoint. -/
def atCenters (center : Pos → F) : Pos → Nat → F → Prop :=
  fun _ _ g => ∃ q, center q = g

/-- It is standpoint-invariant. -/
theorem atCenters_standpointInvariant (center : Pos → F) :
    StandpointInvariant (atCenters center) :=
  fun _ _ _ _ held => held

/-- It makes each standpoint's presupposition about its own continuation, along the empty
relation, sub-true. -/
theorem atCenters_presupposed (center : Pos → F) (p : Pos) :
    SubTrue (Boundary (fun _ _ => False) (center p)) (SignificantWithin (atCenters center) p) :=
  subTrue_empty_iff.mpr fun _ => ⟨p, rfl⟩

/-- **The least significance the step across standpoints gives.** Every significance under which
each standpoint's own continuation has significance from it, and which is standpoint-invariant,
gives significance from every standpoint to the continuation of every center. -/
theorem atCenters_least {center : Pos → F} {sig : Pos → Nat → F → Prop}
    (own : ∀ p, SubTrue (Boundary (fun _ _ => False) (center p)) (SignificantWithin sig p))
    (invariant : StandpointInvariant sig) : ∀ p t g, atCenters center p t g → sig p t g :=
  fun p t _ ⟨q, same⟩ =>
    Eq.subst (motive := fun g => sig p t g) same
      (invariant q p t (center q) (subTrue_empty_iff.mp (own q) t))

/-- **The step across standpoints reaches exactly the centers.** The continuation of `g` has
significance from `p` under every significance that gives each standpoint's own continuation
significance from it and is standpoint-invariant exactly when `g` is some standpoint's center. -/
theorem forced_iff_center (center : Pos → F) (p : Pos) (t : Nat) (g : F) :
    (∀ sig : Pos → Nat → F → Prop,
        (∀ q, SubTrue (Boundary (fun _ _ => False) (center q)) (SignificantWithin sig q)) →
          StandpointInvariant sig → sig p t g) ↔
      ∃ q, center q = g :=
  ⟨fun forced => forced (atCenters center) (atCenters_presupposed center)
      (atCenters_standpointInvariant center),
   fun centered _ own invariant => atCenters_least own invariant p t g centered⟩

/-- **The step across standpoints gives the continuation condition only where everything is a
center.** With some standpoint, the significance of the centers' continuation is unrestricted
exactly when every formation is some standpoint's center. -/
theorem unrestricted_atCenters_iff {center : Pos → F} (some : Pos) :
    Unrestricted (atCenters center) ↔ ∀ g, ∃ q, center q = g :=
  ⟨fun unrestricted g => unrestricted (some, 0, g), fun every i => every i.2.2⟩

/-- **What a standpoint's own presupposition reaches.** Along a relation, the continuation of `g`
has significance from `p` under every significance that makes `p`'s presupposition sub-true,
drawn at the closure of `f`, exactly when `g` lies within that closure. -/
theorem forced_iff_within (rel : F → F → Prop) (f : F) (p : Pos) (t : Nat) (g : F) :
    (∀ sig : Pos → Nat → F → Prop, SubTrue (Boundary rel f) (SignificantWithin sig p) →
        sig p t g) ↔ WithinClosure rel f g :=
  ⟨fun forced => forced (fun _ _ h => WithinClosure rel f h)
      (subTrue_significantWithin_iff.mpr fun _ _ within => within),
   fun within _ sub => subTrue_significantWithin_iff.mp sub t g within⟩

/-- Retaining what has significance at the centers is admitting, at every step, every center
the other path admits. -/
theorem Web.retains_atCenters_iff {C : Type} {W : Web F C} {center : Pos → F} {p : Pos}
    {l l' : Nat → C → Nat} :
    W.Retains (atCenters center) p l l' ↔
      ∀ t, W.AdmitsWithin (fun g => ∃ q, center q = g) (l t) (l' t) t :=
  Web.retains_bounded_iff

/-! ## The self drawn along every relation, and along being related at all -/

section Relations

variable {ι : Type}

/-- Being related by some relation of a family. -/
def Related (rel : ι → F → F → Prop) : F → F → Prop :=
  fun g h => ∃ i, rel i g h

/-- **The presupposition along every relation of a family** is significance over the union of
the closures: from `p`, the continuation of whatever lies within `f`'s closure along some
relation of the family has significance. -/
theorem subTrue_every_iff {rel : ι → F → F → Prop} {f : F} {sig : Pos → Nat → F → Prop}
    {p : Pos} :
    (∀ i, SubTrue (Boundary (rel i) f) (SignificantWithin sig p)) ↔
      ∀ t g, (∃ i, WithinClosure (rel i) f g) → sig p t g :=
  ⟨fun every t g ⟨i, within⟩ => subTrue_significantWithin_iff.mp (every i) t g within,
   fun union i => subTrue_significantWithin_iff.mpr fun t g within => union t g ⟨i, within⟩⟩

/-- Drawn along being related at all, the presupposition gives it along every relation of the
family. -/
theorem subTrue_every_of_related {rel : ι → F → F → Prop} {f : F} {sig : Pos → Nat → F → Prop}
    {p : Pos} (related : SubTrue (Boundary (Related rel) f) (SignificantWithin sig p)) :
    ∀ i, SubTrue (Boundary (rel i) f) (SignificantWithin sig p) :=
  fun i => subTrue_of_larger (fun _ _ holds => ⟨i, holds⟩) related

end Relations

/-! ## Witnesses -/

namespace Chain

/-- Three formations: the first bears one relation to the second, the second another to the
third. -/
inductive Formation where
  | first
  | second
  | third

/-- Relation `false` takes the first to the second, relation `true` the second to the third. -/
inductive rel : Bool → Formation → Formation → Prop where
  | one : rel false .first .second
  | two : rel true .second .third

/-- Along being related at all, the third lies within the first's closure. -/
theorem third_related : WithinClosure (Related rel) .first .third :=
  (WithinClosure.of_rel (rel := Related rel) ⟨false, .one⟩).trans
    (WithinClosure.of_rel (rel := Related rel) ⟨true, .two⟩)

/-- The first alone is closed under relation `true`. -/
def onlyFirst : Formation → Prop
  | .first => True
  | .second => False
  | .third => False

/-- The first and the second are closed under relation `false`. -/
def notThird : Formation → Prop
  | .first => True
  | .second => True
  | .third => False

/-- Along each relation alone, the third does not lie within the first's closure. -/
theorem third_not_within : ∀ i, ¬ WithinClosure (rel i) .first .third
  | false, within => within notThird (fun _ _ _ related => match related with
      | .one => trivial) trivial
  | true, within => within onlyFirst (fun _ _ inside related => match related, inside with
      | .two, no => no) trivial

/-- **Along every relation one at a time the self is smaller than along being related at all.**
Significance over the union of the first's closures makes its presupposition sub-true along
each relation, and not along being related at all. -/
theorem every_not_related :
    (∀ i, SubTrue (Boundary (rel i) .first)
        (SignificantWithin (fun (_ : Unit) _ g => ∃ i, WithinClosure (rel i) .first g) ())) ∧
      ¬ SubTrue (Boundary (Related rel) .first)
        (SignificantWithin (fun (_ : Unit) _ g => ∃ i, WithinClosure (rel i) .first g) ()) :=
  ⟨subTrue_every_iff.mpr fun _ _ union => union,
   fun related => match subTrue_significantWithin_iff.mp related 0 .third third_related with
     | ⟨i, within⟩ => third_not_within i within⟩

end Chain

namespace Clearing

/-- **Where only the clearer holds a standpoint, its part retains what has significance at the
centers, and under the continuation condition it loses the dweller.** The narrower scope and the
condition part exactly at a formation that is no standpoint's center. -/
theorem centers_retain_yet_loses {l : Nat → Place → Nat}
    (without : flow.WithheldLevels clearerPart web l)
    {sig : Unit → Nat → Formation → Prop} (unrestricted : Unrestricted sig) :
    web.Retains (atCenters fun (_ : Unit) => Formation.clearer) () web.level l ∧
      ¬ web.Retains sig () web.level l :=
  ⟨Web.retains_atCenters_iff.mpr fun t => ((loses_beyond without).1 t).2.2.narrow
      fun g ⟨_, same⟩ => match g, same with
        | .clearer, _ => trivial,
   (clearer_loses_dweller without unrestricted ()).2.1⟩

end Clearing

end Becoming
