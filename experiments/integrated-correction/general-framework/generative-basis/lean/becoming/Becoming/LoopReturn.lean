import Becoming.Frequency
import Becoming.Lasting
import Becoming.Prelude

/-!
# LoopReturn: whether a loop closes, keeps or widens a difference

`Becoming.Rejoining` (M4) shows that a difference between two courses closes only through a
response, and, citing `Becoming.PoolResponse`, where they are proved, that a response closing a
difference and one widening it share the structure of a loop through another's coupling and
response (`Loop.response_returns`); which of the two a loop does is left to the law followed
(`ExchangeLaw.response_not_fixed_by_coupling`). This module
states which return laws close, keep or widen a difference, with no premise beyond the hypotheses
each statement names.

A difference is a natural number. One turn around a loop sends a difference into the first link,
each link gives on what it receives to the next, and the last gives it back: a link is a map
`Nat → Nat`, and a loop of links `links` has the return map `LoopReturn.returnMap links`, the first
link applied first. The course of the difference is the run of the return map,
`(Law.run f d).state n`, a run of the spine whose states are the orbit `Law.orbit f d n`
(`Becoming.Recurrence`, `Law.run_state`), the difference after `n` turns from `d`. The difference
is one number, a simplification of Rejoining's levels at many conditions; no theorem here reads a
loop of Rejoining as a return map. A link's *factor* is what one turn makes of the difference it
receives; a *strength* is only a coupling strength of `Becoming.Propagation`, and around a cycle the
product of the coupling strengths (`Loops.product`). The last section joins the two.

* **A return map giving back what it receives keeps a difference.** Such a return map keeps
  `d` at every turn (`LoopReturn.kept_of_identity`), and so does a loop each of whose links gives on
  exactly what it receives (`LoopReturn.loop_kept`).
* **Closing needs a link that gives back less than it received.** Where every link gives on at
  least what it receives, the difference after every turn is at least `d`
  (`LoopReturn.never_closes_of_no_less`). So where the course falls below `d` at some turn, some link
  of the loop gives on, for some difference, less than it received (`LoopReturn.closing_needs_less`);
  the link and the difference are found, nothing being decided beyond the order of numbers.
* **A return map below what it receives closes within `d` turns.** Where `f 0 = 0` and `f x < x`
  for every positive `x`, the course is `0` at turn `d` and at every turn from then on
  (`LoopReturn.closes_within`), and the bound is exact: under `Nat.pred`, which meets both
  hypotheses, the course is positive before turn `d` (`LoopReturn.closes_within_exact`). This is an
  instance of the reaching law with a numeric variant (`Lasting.Variant.reaches`, read on the orbit
  by `Lasting.reaches_iff_orbit`): the difference itself is the variant for the target `0`. A
  loop that closes a positive difference merges two differences, a positive one and `0`, at the
  turn before it closes (`LoopReturn.closing_merges`, the turn found by searching the turns, where
  equality of numbers is decided), so its return map is not lossless
  (`LoopReturn.closing_not_lossless`): the two go on as one at every later turn (`Law.merged_stays`),
  and within finitely many differences the merge loses a possibility for good (`Law.Merges.loses`).
* **Taking a constant off closes, gradually where the constant is below the difference.** A return
  map giving back `c` less than it receives (`f x = x - c`) leaves `d - n * c` after `n` turns
  (`LoopReturn.orbit_sub_const`): the course is `0` once `n * c ≥ d` (`LoopReturn.sub_const_closes`)
  and positive while `n * c < d` (`LoopReturn.sub_const_open`), so the closing turn is the least `n`
  with `n * c ≥ d`. With `c = 0` nothing closes, and with `c ≥ d` the difference closes in one
  turn.
* **A cut closes at once, where what follows it gives nothing for nothing.** A link returning
  nothing makes the difference `0` from the first turn, whatever the links before it, where every
  link after it gives on no difference where it receives none (`LoopReturn.cut_closes`). The
  condition on the links after the cut is needed: in the loop of a cut followed by `Nat.succ`, the
  difference is `1` at every turn after the first, whatever it was (`LoopReturn.cut_reopened`).
* **Monotone return maps settle or rise.** Where `f` keeps order and `f d ≤ d`, the course never
  rises (`LoopReturn.never_rises`, from `Lasting.orbit_mono`: a monotone map keeps order along its
  orbits) and settles within `d` turns at a value `v` with `f v = v`, staying
  there (`LoopReturn.settles_within`); the bound `d` is exact, by `Nat.pred`
  (`LoopReturn.settles_within_exact`, `Nat.pred` meeting both hypotheses). Where `f` keeps order and
  `d ≤ f d`, the course never falls (`LoopReturn.never_falls`, again from `Lasting.orbit_mono`).
* **Doubling links run away.** Where a loop has at least one link and every link gives on at least
  twice what it receives, the difference after `n` turns is at least `2 ^ n * d`
  (`LoopReturn.runs_away`), exceeding every bound from a positive start
  (`LoopReturn.runs_away_unbounded`); the loop of one doubling link meets the hypothesis and attains
  `2 ^ n * d` exactly (`LoopReturn.doubling_exact`). An empty loop gives back what it receives, so
  the link is needed (`LoopReturn.empty_loop_kept`). This runs parallel to `Becoming.Frequency`'s
  doubling at every return, with no instance theorem between them (`carried_doubles_roundTrip`, `carried_roundTrip`): there a return doubles what had
  reached a condition because it arrives once held and once around the loop, and
  `runaway_of_roundTrip` turns doubling at returns that come often enough into outgrowing every
  polynomial in the steps. Here the doubling is a property of each link, and the count is of
  turns, not of steps; how many steps a turn takes is what `Becoming.Frequency` adds.
* **Whole-number factors have nothing between.** In a loop of links multiplying by whole-number
  factors (`LoopReturn.scaling`), the return map multiplies by the product of the factors
  (`LoopReturn.returnMap_scaling`, `LoopReturn.orbit_scaling`). With product `0` the difference closes
  at the first turn, with product `1` it is kept at every turn, and with product at least `2` it
  exceeds every bound from a positive start (`LoopReturn.whole_factors`). So no such loop closes a
  difference gradually: at every turn the course is `0` or no less than at the turn before
  (`LoopReturn.nothing_between`), while taking one off, from `2`, leaves `1` after one turn
  (`LoopReturn.gradual_needs_another_link`). With whole-number factors, a loop that closes
  gradually needs a link that is not a multiplication.
* **The return map is the carried amount of `Becoming.Loops`.** For one condition returning its
  current level to itself with coupling strength `M` (`Loops.SelfLoop.strengths`), the carried
  amount from a starting gap `D` is, at every step, the course from `D` of the loop of one link with
  factor `1 + M`, one turn a step (`LoopReturn.selfLoop_carried`, through
  `LoopReturn.geomBound_eq_course`). The carried amount is attained by the course the carrying law
  generates, against the quiet course (`carried_attained`), so where the actual response attains the
  carrying bound the gap itself is that course (`LoopReturn.selfLoop_gap`). Around every cycle of
  `m + 1` couplings holding at every step, the carried amount after `R` times around is at least the
  course after `R` turns of the loop of one link with factor one plus the product of the coupling
  strengths around the cycle (`LoopReturn.carried_around_course`, from `carried_runaway`). The one is
  the holding: the carrying law takes nothing, so a condition keeps what it had while the cycle
  returns more. A positive whole-number strength gives a factor of at least `2`, the doubling of
  `carried_doubles_around`.

What is not derived: which return law a loop follows, which the laws above take as given, as
`Becoming.Rejoining` leaves the response to the law followed; that a difference is one number,
rather than many differences at many conditions; how many steps a turn takes (`Becoming.Frequency`);
the carried amount around a cycle of more than one condition as a return map (intermediate
conditions hold and keep giving, so a turn is not a map of one number; the bound above is what
holds); and which of keeping, closing or widening a difference supports the generation of life in
the whole, which goes through the comparison and the condition of the chapter's §6.15.
-/

namespace Becoming

namespace LoopReturn

/-! ## Loops of links -/

/-- The return map of a loop of links: the difference that comes back after one turn for the
difference sent, the first link applied first. -/
def returnMap : List (Nat → Nat) → Nat → Nat
  | [], x => x
  | g :: gs, x => returnMap gs (g x)

/-- The links that multiply by whole-number factors. -/
def scaling (as : List Nat) : List (Nat → Nat) := as.map (fun a x => a * x)

/-- The product of the factors. -/
def factor : List Nat → Nat
  | [] => 1
  | a :: as => a * factor as

/-- A course at a value the return map keeps stays there. -/
theorem orbit_of_fixed {f : Nat → Nat} {v : Nat} (fixed : f v = v) : ∀ n, (Law.run f v).state n = v
  | 0 => rfl
  | n + 1 => (congrArg f (orbit_of_fixed fixed n)).trans fixed

/-- A course that reaches a value the return map keeps stays there. -/
theorem stays_from_fixed {f : Nat → Nat} {d k : Nat} (fixed : f ((Law.run f d).state k) = (Law.run f d).state k)
    {n : Nat} (le : k ≤ n) : (Law.run f d).state n = (Law.run f d).state k := by
  induction le with
  | refl => exact rfl
  | step _ ih => exact (congrArg f ih).trans fixed

/-- A number added to `b` and staying within `b` is `0`. -/
theorem eq_zero_of_add_le : ∀ {a b : Nat}, a + b ≤ b → a = 0
  | _, 0, le => Nat.eq_zero_of_le_zero le
  | _, _ + 1, le => eq_zero_of_add_le (Nat.le_of_succ_le_succ le)

/-- One raised to every exponent is one. -/
theorem one_pow : ∀ n, 1 ^ n = 1
  | 0 => rfl
  | n + 1 => (Nat.pow_succ 1 n).trans ((Nat.mul_one _).trans (one_pow n))

/-! ## Keeping -/

/-- **A return map giving back what it receives keeps a difference** at every turn. -/
theorem kept_of_identity {f : Nat → Nat} (same : ∀ x, f x = x) (d : Nat) :
    ∀ n, (Law.run f d).state n = d :=
  orbit_of_fixed (same d)

/-- A loop each of whose links gives on exactly what it receives gives back what it receives. -/
theorem returnMap_of_identity : ∀ {links : List (Nat → Nat)},
    (∀ g, g ∈ links → ∀ x, g x = x) → ∀ x, returnMap links x = x
  | [], _, _ => rfl
  | g :: gs, same, x =>
    (returnMap_of_identity (fun h m => same h (List.Mem.tail g m)) (g x)).trans
      (same g (List.Mem.head gs) x)

/-- **A loop each of whose links gives on what it receives keeps a difference.** -/
theorem loop_kept {links : List (Nat → Nat)} (same : ∀ g, g ∈ links → ∀ x, g x = x) (d : Nat) :
    ∀ n, (Law.run (returnMap links) d).state n = d :=
  kept_of_identity (returnMap_of_identity same) d

/-! ## Closing needs a link that gives back less -/

/-- A loop each of whose links gives on at least what it receives gives back at least what it
receives. -/
theorem returnMap_ge : ∀ {links : List (Nat → Nat)},
    (∀ g, g ∈ links → ∀ x, x ≤ g x) → ∀ x, x ≤ returnMap links x
  | [], _, x => Nat.le_refl x
  | g :: gs, up, x =>
    Nat.le_trans (up g (List.Mem.head gs) x)
      (returnMap_ge (fun h m => up h (List.Mem.tail g m)) (g x))

/-- A return map giving back at least what it receives never takes the course below its start:
`never_falls_over` (`Becoming.Recurrence`) read on the orbit, from turn `0`. -/
theorem orbit_ge_of_ge {f : Nat → Nat} (up : ∀ x, x ≤ f x) (d : Nat) (n : Nat) :
    d ≤ (Law.run f d).state n :=
  Nat.le_trans (never_falls_over (q := id) (g := (Law.run f d).state) (fun _ => up _) 0 n)
    (Nat.le_of_eq (congrArg ((Law.run f d).state) (Nat.zero_add n)))

/-- **Where every link gives on at least what it receives, no turn closes any of the difference.**
The difference after every turn is at least the difference sent. -/
theorem never_closes_of_no_less {links : List (Nat → Nat)}
    (up : ∀ g, g ∈ links → ∀ x, x ≤ g x) (d : Nat) :
    ∀ n, d ≤ (Law.run (returnMap links) d).state n :=
  orbit_ge_of_ge (returnMap_ge up) d

/-- A course that falls below its start passes a difference the return map gives back less of. -/
theorem below_of_falls {f : Nat → Nat} {d : Nat} :
    ∀ {n : Nat}, (Law.run f d).state n < d → ∃ y, f y < y
  | 0, lt => absurd lt (Nat.lt_irrefl d)
  | n + 1, lt =>
    match Nat.lt_or_ge (f ((Law.run f d).state n)) ((Law.run f d).state n) with
    | Or.inl less => ⟨_, less⟩
    | Or.inr ge => below_of_falls (Nat.lt_of_le_of_lt ge lt)

/-- A loop that gives back less than it received has a link that gives on less than it
received. -/
theorem link_below_of_below : ∀ {links : List (Nat → Nat)} {x : Nat},
    returnMap links x < x → ∃ g, g ∈ links ∧ ∃ y, g y < y
  | [], _, lt => absurd lt (Nat.lt_irrefl _)
  | g :: gs, x, lt =>
    match Nat.lt_or_ge (g x) x with
    | Or.inl less => ⟨g, List.Mem.head gs, x, less⟩
    | Or.inr ge =>
      match link_below_of_below (links := gs) (x := g x) (Nat.lt_of_lt_of_le lt ge) with
      | ⟨h, m, y, less⟩ => ⟨h, List.Mem.tail g m, y, less⟩

/-- **Closing needs a link that gives back less than it received.** Where the course of a loop
falls below the difference sent at some turn (in particular, where it closes a positive
difference), some link of the loop gives on, for some difference, less than it received. -/
theorem closing_needs_less {links : List (Nat → Nat)} {d n : Nat}
    (falls : (Law.run (returnMap links) d).state n < d) : ∃ g, g ∈ links ∧ ∃ x, g x < x :=
  match below_of_falls falls with
  | ⟨_, less⟩ => link_below_of_below less

/-! ## A return map below what it receives -/

/-- **The difference is a variant for closing.** Where `f x < x` for every positive `x`, the
difference itself is a numeric variant (`Lasting.Variant`) for reaching `0` within `d` turns. -/
theorem difference_variant {f : Nat → Nat} (below : ∀ x, 0 < x → f x < x) (d : Nat) :
    Lasting.Variant (Lasting.determined f) (fun _ => True) (fun x => x = 0) d id :=
  fun x _ => match x with
    | 0 => Or.inl rfl
    | x + 1 => Or.inr ⟨Nat.succ_pos x, fun _ _ => below (x + 1) (Nat.succ_pos x)⟩

/-- **A return map below what it receives closes within `d` turns.** Where `f 0 = 0` and `f x < x`
for every positive `x`, the course is `0` at turn `d` and at every turn from then on. This is an
instance of the reaching law with a numeric variant, `Lasting.Variant.reaches`, read on the orbit
by `Lasting.reaches_iff_orbit` (the variant is `difference_variant`); once `0` is met the course
stays there (`stays_from_fixed`). -/
theorem closes_within {f : Nat → Nat} (zero : f 0 = 0) (below : ∀ x, 0 < x → f x < x) (d : Nat) :
    (Law.run f d).state d = 0 ∧ ∀ n, d ≤ n → (Law.run f d).state n = 0 :=
  match Lasting.reaches_iff_orbit.mp
      (Lasting.Variant.reaches (difference_variant below d) (Nat.le_refl d)) with
  | ⟨k, le, met⟩ =>
    have closed : (Law.run f d).state k = 0 := met
    have fixed : f ((Law.run f d).state k) = (Law.run f d).state k :=
      (congrArg f closed).trans (zero.trans closed.symm)
    have after : ∀ n, d ≤ n → (Law.run f d).state n = 0 :=
      fun _ later => (stays_from_fixed fixed (Nat.le_trans le later)).trans closed
    ⟨after d (Nat.le_refl d), after⟩

/-! ## Taking a constant off -/

/-- **Taking a constant off.** A return map giving back `c` less than it receives leaves
`d - n * c` after `n` turns. -/
theorem orbit_sub_const {f : Nat → Nat} {c : Nat} (sub : ∀ x, f x = x - c) (d : Nat) :
    ∀ n, (Law.run f d).state n = d - n * c
  | 0 => (congrArg (d - ·) (Nat.zero_mul c)).symm
  | n + 1 =>
    (sub _).trans ((congrArg (· - c) (orbit_sub_const sub d n)).trans
      ((Naturals.sub_sub d (n * c) c).trans (congrArg (d - ·) (Nat.succ_mul n c).symm)))

/-- **Taking a constant off has closed once `n * c ≥ d`.** -/
theorem sub_const_closes {f : Nat → Nat} {c d n : Nat} (sub : ∀ x, f x = x - c)
    (enough : d ≤ n * c) : (Law.run f d).state n = 0 :=
  (orbit_sub_const sub d n).trans (sub_eq_zero_of_le enough)

/-- **Taking a constant off has not closed while `n * c < d`**: with `sub_const_closes`, the
closing turn is the least `n` with `n * c ≥ d`; with `c = 0` there is none for a positive `d`. -/
theorem sub_const_open {f : Nat → Nat} {c d n : Nat} (sub : ∀ x, f x = x - c)
    (short : n * c < d) : 0 < (Law.run f d).state n :=
  Nat.lt_of_lt_of_le (SupportGated.sub_pos_of_lt short) (Nat.le_of_eq (orbit_sub_const sub d n).symm)

/-- **The bound `d` is exact.** `Nat.pred` keeps no difference and is below every positive one, and
under it the course is positive at every turn before `d`. -/
theorem closes_within_exact :
    Nat.pred 0 = 0 ∧ (∀ x, 0 < x → Nat.pred x < x) ∧
      ∀ d n, n < d → 0 < (Law.run Nat.pred d).state n :=
  ⟨rfl, fun _ pos => Nat.pred_lt (Nat.ne_of_gt pos),
   fun d n lt =>
    match le_dest lt with
    | ⟨e, same⟩ =>
      have eq : (Law.run Nat.pred d).state n = e + 1 :=
        (congrArg (fun x => (Law.run Nat.pred x).state n)
            (same.trans ((Nat.add_comm (n + 1) e).trans (Nat.add_right_comm e 1 n).symm))).trans
          (Law.pred_orbit n (e + 1))
      Nat.lt_of_lt_of_le (Nat.succ_pos e) (Nat.le_of_eq eq.symm)⟩

/-- A course that starts positive and is `0` at some turn has a last positive turn before it: a
turn `k` with the course positive at `k` and `0` at `k + 1`. The turns are searched, equality of
numbers being decided. -/
theorem last_positive {f : Nat → Nat} {d : Nat} (pos : 0 < d) :
    ∀ {n : Nat}, (Law.run f d).state n = 0 → ∃ k, 0 < (Law.run f d).state k ∧ (Law.run f d).state (k + 1) = 0
  | 0, closed => absurd closed (Nat.ne_of_gt pos)
  | n + 1, closed =>
    match Nat.decEq ((Law.run f d).state n) 0 with
    | isTrue earlier => last_positive pos earlier
    | isFalse open_ => ⟨n, Nat.pos_of_ne_zero open_, closed⟩

/-- **A loop that closes a positive difference merges two differences.** Where the return map
keeps no difference and the course closes a positive `d`, the positive difference at the last turn
before closing and `0` go to one difference, `0` (`Law.Merges`). By `Law.merged_stays` no later
turn tells them apart, and within finitely many differences the merge loses a possibility for good
(`Law.Merges.loses`). -/
theorem closing_merges {f : Nat → Nat} {d n : Nat} (zero : f 0 = 0)
    (closed : (Law.run f d).state n = 0) (pos : 0 < d) : Law.Merges f :=
  match last_positive pos closed with
  | ⟨k, open_, next⟩ => Law.merges_iff.mpr ⟨(Law.run f d).state k, 0, Nat.ne_of_gt open_, next.trans zero.symm⟩

/-- **A loop that closes a positive difference is not lossless** (`Branching.Merges.not_lossless`). -/
theorem closing_not_lossless {f : Nat → Nat} {d n : Nat} (zero : f 0 = 0)
    (closed : (Law.run f d).state n = 0) (pos : 0 < d) : ¬ Law.Lossless f :=
  (closing_merges zero closed pos).not_lossless

/-! ## A cut -/

/-- A loop each of whose links gives on no difference where it receives none gives back none for
none. -/
theorem returnMap_zero : ∀ {links : List (Nat → Nat)},
    (∀ g, g ∈ links → g 0 = 0) → returnMap links 0 = 0
  | [], _ => rfl
  | g :: gs, keep =>
    (congrArg (returnMap gs) (keep g (List.Mem.head gs))).trans
      (returnMap_zero (fun h m => keep h (List.Mem.tail g m)))

/-- A loop with a link returning nothing, followed only by links giving nothing for nothing, gives
back nothing. -/
theorem returnMap_cut {c : Nat → Nat} (cut : ∀ x, c x = 0) :
    ∀ (pre : List (Nat → Nat)) {post : List (Nat → Nat)}, (∀ g, g ∈ post → g 0 = 0) →
      ∀ x, returnMap (pre ++ c :: post) x = 0
  | [], _, keep, x => (congrArg (returnMap _) (cut x)).trans (returnMap_zero keep)
  | g :: pre, _, keep, x => returnMap_cut cut pre keep (g x)

/-- **A cut closes at once.** A link returning nothing makes the difference `0` from the first
turn, whatever the links before it, where every link after it gives on no difference where it
receives none. -/
theorem cut_closes {c : Nat → Nat} (cut : ∀ x, c x = 0) (pre : List (Nat → Nat))
    {post : List (Nat → Nat)} (keep : ∀ g, g ∈ post → g 0 = 0) (d : Nat) :
    ∀ n, (Law.run (returnMap (pre ++ c :: post)) d).state (n + 1) = 0 :=
  fun _ => returnMap_cut cut pre keep _

/-- **What follows a cut can reopen the difference.** In the loop of a link returning nothing
followed by `Nat.succ`, the difference is `1` at every turn after the first, whatever it was: the
condition of `cut_closes` on the links after the cut is needed. -/
theorem cut_reopened (d : Nat) :
    ∀ n, (Law.run (returnMap [fun _ => 0, Nat.succ]) d).state (n + 1) = 1 :=
  fun _ => rfl

/-! ## Monotone return maps -/

/-- **A monotone return map that does not raise the start never raises the course.** This is
`Lasting.orbit_mono` (a monotone map keeps order along its orbits) for the orbits from `f d` and
from `d`, the first being the course one turn on (`Law.orbit_shift`). -/
theorem never_rises {f : Nat → Nat} (mono : ∀ x y, x ≤ y → f x ≤ f y) {d : Nat} (down : f d ≤ d)
    (n : Nat) : (Law.run f d).state (n + 1) ≤ (Law.run f d).state n :=
  Nat.le_trans (Nat.le_of_eq (Law.orbit_shift f d n))
    (Lasting.orbit_mono (rel := (· ≤ ·)) mono down n)

/-- **A monotone return map that does not lower the start never lowers the course**, by
`Lasting.orbit_mono` for the orbits from `d` and from `f d`. -/
theorem never_falls {f : Nat → Nat} (mono : ∀ x y, x ≤ y → f x ≤ f y) {d : Nat} (up : d ≤ f d)
    (n : Nat) : (Law.run f d).state n ≤ (Law.run f d).state (n + 1) :=
  Nat.le_trans (Lasting.orbit_mono (rel := (· ≤ ·)) mono up n)
    (Nat.le_of_eq (Law.orbit_shift f d n).symm)

/-- Under a monotone return map not raising the start, by turn `n` the course has met a kept value
or fallen by at least `n`. -/
theorem settled_or_fallen {f : Nat → Nat} (mono : ∀ x y, x ≤ y → f x ≤ f y) {d : Nat}
    (down : f d ≤ d) :
    ∀ n, (∃ k, k ≤ n ∧ f ((Law.run f d).state k) = (Law.run f d).state k) ∨ (Law.run f d).state n + n ≤ d
  | 0 => Or.inr (Nat.le_refl d)
  | n + 1 =>
    match settled_or_fallen mono down n with
    | Or.inl ⟨k, le, fixed⟩ => Or.inl ⟨k, Nat.le_succ_of_le le, fixed⟩
    | Or.inr fallen =>
      match Nat.decEq (f ((Law.run f d).state n)) ((Law.run f d).state n) with
      | isTrue fixed => Or.inl ⟨n, Nat.le_succ n, fixed⟩
      | isFalse moved =>
        Or.inr (Nat.le_trans
          (Nat.le_of_eq ((Nat.add_assoc ((Law.run f d).state (n + 1)) 1 n).trans
            (congrArg ((Law.run f d).state (n + 1) + ·) (Nat.add_comm 1 n))).symm)
          (Nat.le_trans (Nat.add_le_add_right
            (Nat.lt_of_le_of_ne (never_rises mono down n) moved) n) fallen))

/-- **A monotone return map that does not raise the start settles within `d` turns.** The course
meets, by turn `d`, a value `v` with `f v = v`, and stays there at every later turn. -/
theorem settles_within {f : Nat → Nat} (mono : ∀ x y, x ≤ y → f x ≤ f y) {d : Nat}
    (down : f d ≤ d) :
    ∃ k, k ≤ d ∧ f ((Law.run f d).state k) = (Law.run f d).state k ∧
      ∀ n, k ≤ n → (Law.run f d).state n = (Law.run f d).state k :=
  match settled_or_fallen mono down d with
  | Or.inl ⟨k, le, fixed⟩ => ⟨k, le, fixed, fun _ later => stays_from_fixed fixed later⟩
  | Or.inr fallen =>
    have closed : (Law.run f d).state d = 0 := eq_zero_of_add_le fallen
    have fixed : f ((Law.run f d).state d) = (Law.run f d).state d :=
      (Nat.eq_zero_of_le_zero (closed ▸ never_rises mono down d)).trans closed.symm
    ⟨d, Nat.le_refl d, fixed, fun _ later => stays_from_fixed fixed later⟩

/-- **The bound `d` of settling is exact.** `Nat.pred` keeps order and does not raise any start,
and under it the course meets no value it keeps before turn `d`. -/
theorem settles_within_exact :
    (∀ x y, x ≤ y → Nat.pred x ≤ Nat.pred y) ∧ (∀ d, Nat.pred d ≤ d) ∧
      ∀ d n, n < d → Nat.pred ((Law.run Nat.pred d).state n) ≠ (Law.run Nat.pred d).state n :=
  ⟨fun _ _ le => Nat.pred_le_pred le, fun _ => Nat.pred_le _,
   fun d n lt same =>
    Nat.ne_of_lt (Nat.pred_lt (Nat.ne_of_gt (closes_within_exact.2.2 d n lt))) same⟩

/-! ## Doubling links -/

/-- A loop with a link, each of whose links gives on at least twice what it receives, gives back at
least twice what it receives. -/
theorem returnMap_doubles {g : Nat → Nat} {gs : List (Nat → Nat)}
    (double : ∀ h, h ∈ g :: gs → ∀ x, x + x ≤ h x) (x : Nat) : x + x ≤ returnMap (g :: gs) x :=
  Nat.le_trans (double g (List.Mem.head gs) x)
    (returnMap_ge (fun h m y => Nat.le_trans (Nat.le_add_left y y) (double h (List.Mem.tail g m) y))
      (g x))

/-- Two to the next exponent, times a number, is twice two to the exponent times it. -/
theorem two_pow_succ_mul (n d : Nat) : 2 ^ (n + 1) * d = 2 ^ n * d + 2 ^ n * d :=
  (congrArg (· * d) (Nat.pow_succ 2 n)).trans
    ((mul_assoc_nat (2 ^ n) 2 d).trans
      ((congrArg (2 ^ n * ·) (Nat.two_mul d)).trans (Nat.left_distrib (2 ^ n) d d)))

/-- **Doubling links run away.** Where a loop has a link and every link gives on at least twice
what it receives, the difference after `n` turns is at least `2 ^ n * d`. -/
theorem runs_away {g : Nat → Nat} {gs : List (Nat → Nat)}
    (double : ∀ h, h ∈ g :: gs → ∀ x, x + x ≤ h x) (d : Nat) :
    ∀ n, 2 ^ n * d ≤ (Law.run (returnMap (g :: gs)) d).state n
  | 0 => Nat.le_of_eq (Nat.one_mul d)
  | n + 1 =>
    Nat.le_trans (Nat.le_of_eq (two_pow_succ_mul n d))
      (Nat.le_trans (Nat.add_le_add (runs_away double d n) (runs_away double d n))
        (returnMap_doubles double _))

/-- A positive number times two to an exponent exceeds the exponent. -/
theorem lt_two_pow_mul {d : Nat} (pos : 0 < d) (n : Nat) : n < 2 ^ n * d :=
  Nat.lt_of_lt_of_le (Loops.lt_two_pow n)
    (Nat.le_trans (Nat.le_of_eq (Nat.mul_one _).symm) (Nat.mul_le_mul_left _ pos))

/-- **From a positive start, doubling links exceed every bound.** -/
theorem runs_away_unbounded {g : Nat → Nat} {gs : List (Nat → Nat)}
    (double : ∀ h, h ∈ g :: gs → ∀ x, x + x ≤ h x) {d : Nat} (pos : 0 < d) :
    ∀ B, ∃ n, B < (Law.run (returnMap (g :: gs)) d).state n :=
  fun B => ⟨B, Nat.lt_of_lt_of_le (lt_two_pow_mul pos B) (runs_away double d B)⟩

/-- The loop of one link giving on twice what it receives leaves exactly `2 ^ n * d` after `n`
turns. -/
theorem orbit_doubling (d : Nat) :
    ∀ n, (Law.run (returnMap [fun x => x + x]) d).state n = 2 ^ n * d
  | 0 => (Nat.one_mul d).symm
  | n + 1 =>
    (congrArg (fun y => y + y) (orbit_doubling d n)).trans (two_pow_succ_mul n d).symm

/-- **The doubling bound is attained.** The loop of one link giving on twice what it receives meets
the hypothesis of `runs_away` and leaves exactly `2 ^ n * d` after `n` turns. -/
theorem doubling_exact :
    (∀ h, h ∈ [fun x : Nat => x + x] → ∀ x, x + x ≤ h x) ∧
      ∀ d n, (Law.run (returnMap [fun x => x + x]) d).state n = 2 ^ n * d :=
  ⟨fun h m x => (match h, m with
    | _, List.Mem.head _ => Nat.le_refl (x + x)
    | _, List.Mem.tail _ rest => nomatch rest),
   orbit_doubling⟩

/-- **An empty loop gives back what it receives**, so `runs_away` needs a link. -/
theorem empty_loop_kept (d : Nat) : ∀ n, (Law.run (returnMap []) d).state n = d :=
  kept_of_identity (fun _ => rfl) d

/-! ## Whole-number factors -/

/-- **A loop of multiplying links multiplies by the product of the factors.** -/
theorem returnMap_scaling : ∀ (as : List Nat) (x : Nat), returnMap (scaling as) x = factor as * x
  | [], x => (Nat.one_mul x).symm
  | a :: as, x =>
    (returnMap_scaling as (a * x)).trans
      ((mul_assoc_nat (factor as) a x).symm.trans
        (congrArg (· * x) (Nat.mul_comm (factor as) a)))

/-- **The course of a loop of multiplying links.** After `n` turns the difference is the product
of the factors to the `n` times the difference sent. -/
theorem orbit_scaling (as : List Nat) (d : Nat) :
    ∀ n, (Law.run (returnMap (scaling as)) d).state n = factor as ^ n * d
  | 0 => (Nat.one_mul d).symm
  | n + 1 =>
    (returnMap_scaling as _).trans
      ((congrArg (factor as * ·) (orbit_scaling as d n)).trans
        ((mul_assoc_nat (factor as) _ d).symm.trans
          (congrArg (· * d) ((Nat.mul_comm (factor as) _).trans (Nat.pow_succ _ n).symm))))

/-- **Whole-number factors have nothing between.** In a loop of links multiplying by
whole-number factors with product `P`: with `P = 0` the difference closes at the first turn, with
`P = 1` it is kept at every turn, and with `P ≥ 2` it exceeds every bound from a positive start. -/
theorem whole_factors (as : List Nat) (d : Nat) :
    (factor as = 0 → ∀ n, (Law.run (returnMap (scaling as)) d).state (n + 1) = 0) ∧
    (factor as = 1 → ∀ n, (Law.run (returnMap (scaling as)) d).state n = d) ∧
    (2 ≤ factor as → 0 < d → ∀ B, ∃ n, B < (Law.run (returnMap (scaling as)) d).state n) :=
  ⟨fun zero _ =>
    (returnMap_scaling as _).trans ((congrArg (· * _) zero).trans (Nat.zero_mul _)),
   fun one n =>
    (orbit_scaling as d n).trans
      ((congrArg (fun p => p ^ n * d) one).trans
        ((congrArg (· * d) (one_pow n)).trans (Nat.one_mul d))),
   fun two pos B =>
    ⟨B, Nat.lt_of_lt_of_le (lt_two_pow_mul pos B)
      (Nat.le_trans (Nat.mul_le_mul_right d (Loops.pow_le_pow_base two B))
        (Nat.le_of_eq (orbit_scaling as d B).symm))⟩⟩

/-- **No loop of multiplying links closes a difference gradually.** At every turn the course is
`0`, or no less than at the turn before. -/
theorem nothing_between (as : List Nat) (d n : Nat) :
    (Law.run (returnMap (scaling as)) d).state (n + 1) = 0 ∨
      (Law.run (returnMap (scaling as)) d).state n ≤ (Law.run (returnMap (scaling as)) d).state (n + 1) :=
  match h : factor as with
  | 0 => Or.inl ((whole_factors as d).1 h n)
  | k + 1 =>
    Or.inr (Nat.le_trans (Nat.le_of_eq (Nat.one_mul _).symm)
      (Nat.le_trans (Nat.mul_le_mul_right _ (h ▸ Nat.succ_pos k : 0 < factor as))
        (Nat.le_of_eq (returnMap_scaling as _).symm)))

/-- **A loop that closes gradually needs a link that is not a multiplication.** No loop of
multiplying links leaves, at any turn, a positive difference below the one before; taking one off,
from `2`, leaves `1` after one turn. -/
theorem gradual_needs_another_link :
    (∀ as d n, ¬ (0 < (Law.run (returnMap (scaling as)) d).state (n + 1) ∧
        (Law.run (returnMap (scaling as)) d).state (n + 1) < (Law.run (returnMap (scaling as)) d).state n)) ∧
      (0 < (Law.run (returnMap [fun x => x - 1]) 2).state 1 ∧
        (Law.run (returnMap [fun x => x - 1]) 2).state 1 < (Law.run (returnMap [fun x => x - 1]) 2).state 0) :=
  ⟨fun as d n ⟨pos, lt⟩ =>
    match nothing_between as d n with
    | Or.inl closed => Nat.ne_of_gt pos closed
    | Or.inr le => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le lt le),
   ⟨Nat.succ_pos 0, Nat.lt_succ_self 1⟩⟩

/-! ## The return map as the carried amount of `Becoming.Loops`

A link's factor is what one turn makes of the difference the link receives. Under the carrying law
of `Becoming.Propagation`, which gives what the coupling strengths make of the levels and takes
nothing, a condition holds what it had and receives what the strengths carry back to it, so one
turn multiplies by one plus the coupling strength, and around a cycle by at least one plus the
product of the coupling strengths around it. -/

/-- One link's factor is the factor of the loop of that one link. -/
theorem factor_single (a : Nat) : factor [a] = a :=
  Nat.mul_one a

/-- The self-loop's bound, step by step, is the course of the loop of one link with factor
`1 + M`. -/
theorem geomBound_eq_course (M D : Nat) :
    ∀ t, Loops.geomBound M D t = (Law.run (returnMap (scaling [1 + M])) D).state t
  | 0 => rfl
  | t + 1 =>
    show Loops.geomBound M D t + M * Loops.geomBound M D t =
        (1 + M) * (Law.run (returnMap (scaling [1 + M])) D).state t from
    (Loops.one_add_mul M _).symm.trans (congrArg ((1 + M) * ·) (geomBound_eq_course M D t))

/-- **A self-loop's carried amount is the course of a return map.** One condition returning its
current level to itself with coupling strength `M` (`Loops.SelfLoop.strengths`): from a starting gap
`D`, the carried amount at step `t` is the course from `D`, after `t` turns, of the loop of one link
with factor `1 + M`, one turn a step. -/
theorem selfLoop_carried (M D t : Nat) :
    carried [()] (fun _ => false) (fun _ _ _ => 0) (Loops.SelfLoop.strengths M) (fun _ => [()])
        (fun _ => D) t () =
      (Law.run (returnMap (scaling [1 + M])) D).state t :=
  (Loops.SelfLoop.carried_eq M D t).trans (geomBound_eq_course M D t)

/-- **Where the response attains the carrying bound, the gap is the course of the return map.** The
course the carrying law generates from `D` has, against the quiet course, exactly the carried
amount as its gap at every step (`carried_attained`); for the self-loop of coupling strength `M`
that gap is the course of the loop of one link with factor `1 + M`. -/
theorem selfLoop_gap (M D t : Nat) :
    gap (carried [()] (fun _ => false) (fun _ _ _ => 0) (Loops.SelfLoop.strengths M) (fun _ => [()])
          (fun _ => D) t ())
        (carried [()] (fun _ => false) (fun _ _ _ => 0) (Loops.SelfLoop.strengths M)
          (fun _ => [()]) (fun _ => 0) t ()) =
      (Law.run (returnMap (scaling [1 + M])) D).state t :=
  (carried_attained t ()).trans (selfLoop_carried M D t)

/-- **Around every cycle, at least the course of one plus the product of the coupling strengths.**
Where at every step each condition of a loop of `m + 1` couplings is coupled into the next with
strength at least `w` (`CoupledWith`), the carried amount at the loop after `R` times around is at
least the course, after `R` turns, of the loop of one link whose factor is one plus the product of
the coupling strengths around the cycle (`Loops.product`), from what had reached the loop
(`carried_runaway`). -/
theorem carried_around_course {F C : Type} {cs : List C} {part : F → Bool}
    {σ : Nat → F → C → Nat} {k : Nat → F → C → Nat → C → Nat} {present : Nat → List F}
    {δ : C → Nat} {v : Nat → C} {w : Nat → Nat} {m : Nat} {e : C} (start : v 0 = e)
    (back : v (m + 1) = e) (loop : CoupledWith cs part k present v w (m + 1)) (t R : Nat) :
    (Law.run (returnMap (scaling [1 + Loops.product w (m + 1)]))
        (carried cs part σ k present δ t e)).state R ≤
      carried cs part σ k present δ (t + (m + 1) * R) e :=
  Nat.le_trans
    (Nat.le_of_eq ((orbit_scaling _ _ R).trans
      (congrArg (fun x => x ^ R * carried cs part σ k present δ t e) (factor_single _))))
    (carried_runaway start back loop t R)

end LoopReturn

end Becoming
