import Becoming.HexagramPlaces
import Becoming.HexagramCommuting

/-!
# Hexagram laws: the nuclear law, orbits, turning lines, symmetries, the counter

`Becoming.Hexagrams` states the six-line configurations of the 周易 as a world of the spine, with the
change of one line, the law of waxing and waning and the law that only wanes, and
`Becoming.HexagramPlaces` the relations of the places. This module states four more laws on the same
sixty-four configurations, the census of the law of waxing and waning, and what the spine's laws say
of each, with no premise beyond what each statement names. Where a passage of the text reads one of
them, the chapter on the 易传 maps it.

* **Counting over the received order.** The received order lists each configuration once
  (`order_nodup`), so a count over it is a count of configurations.
* **The nuclear law (互).** Lines 2 to 4 become the lower trigram and lines 3 to 5 the upper
  (`nuclear`). What it makes of a hexagram is fixed by the four inner lines (`nuclear_inner`), so
  two runs whose starts agree in them are one run from the first step (`run_inner`); two steps leave
  only lines 3 and 4, three times over (`nuclear_two`, `nuclear_two_lumped`, `run_two_middle`). It
  merges and loses a possibility for good (`nuclear_merges`, `nuclear_loses`). Where it draws
  everything is neither one configuration nor the whole: 乾 and 坤 stay and nothing else does, and 既濟
  and 未濟 take turns (`nuclear_fixed_iff`, `nuclear_rests_iff`, `nuclear_two_fixed_one_cycle`). Every
  configuration is in these four by the second step and never leaves (`nuclear_two_attractor`,
  `attractor_absorbing`, `run_in_attractor`), every other is drawn in (`outside_drawn`), and exactly
  these four return (`returns_iff_attractor`, `nuclear_process_returns_iff`, by
  `Law.Drawn.not_returns`): they are the first two and the last two of the received order
  (`process_returns_iff_ends`), four are in them, twelve enter at the first step and forty-eight at
  the second (`entry_counts`). Lines 3 and 4 fix where a course comes to rest: 16 configurations go
  to 乾, 16 to 坤 and 32 into the turns of 既濟 and 未濟 (`basin_iff`, `qian_basin`, `kun_basin`,
  `cycle_basin`, `basin_counts`, `run_rests_at`). Lines 3 and 4 are a lumping the law goes alike
  across, since they swap at every step (`innerPair_lumped`, `innerPair_goAlike`); the count of
  unbroken lines is not (`nuclear_yang_not_lumped`, `nuclear_yang_not_goAlike`). Beside the law of
  waxing and waning, which merges nothing so that everything returns, and the law that only wanes,
  which draws everything into 坤, this is a third shape: two configurations that stay and a cycle of
  two.
* **The four symmetries (錯, 綜).** Keeping a hexagram, changing every line, turning it over and both
  (`Symmetry`, `Symmetry.act`) compose as a group in which each is its own inverse and any two
  commute (`Symmetry.act_comp`, `Symmetry.comp_self`, `Symmetry.comp_comm`). The nuclear law
  commutes with each (`nuclear_complement`, `nuclear_reverse`, `nuclear_act`), so each takes every
  run of it to a run of it (`nuclear_run_act`, by `Law.Commutes.iterate`). Changing every line
  leaves nothing as it is (`complement_moves`), so the runs from a configuration and from its
  complement never meet (`run_complement_apart`), the instance of what a commuting law keeps apart
  (`Law.Commutes.apart`). A class is named by its member of least binary value (`classOf`), and
  two hexagrams are in one class exactly where a symmetry takes one to the other (`classOf_eq_iff`).
  There are twenty classes, eight of two and twelve of four (`classes`, `class_census`). They are a
  lumping the nuclear law goes alike across (`classes_lumped`, `classes_goAlike`); the law of waxing
  and waning does not go alike across them, since turning over runs it backward
  (`classes_not_lumped_waxWane`, `classes_not_goAlike_waxWane`). The configurations turning over
  leaves as they are are exactly those the received order pairs by changing every line
  (`turn_fixed_iff`); those that turning over and changing every line take to the same hexagram are
  exactly the pairs of the order in which the two agree (`both_fixed_iff`).
* **Turning and staying lines (老, 少) and the hexagram the lines go to (之卦).** A marked line is
  turning (老) or staying (少) (`Marked`); at the next step a turning line changes into its opposite
  and stays (`MarkedLines.settle`). The law merges (`MarkedLines.settle_merges`) and is settled in
  one step (`MarkedLines.settle_settle`, `MarkedLines.run_settled`, `MarkedLines.run_rests`): one
  with a turning line is drawn into those with none (`MarkedLines.drawn`), so a configuration
  returns exactly where no line turns (`MarkedLines.returns_iff`,
  `MarkedLines.process_returns_iff`). The hexagram shown (本卦, `MarkedLines.shown`) is not a lumping
  the law goes alike across (`MarkedLines.shown_not_lumped`, `MarkedLines.shown_not_goAlike`); the
  hexagram the lines go to is (`MarkedLines.onward`, `MarkedLines.onward_lumped`,
  `MarkedLines.onward_goAlike`). Six unbroken turning lines show 乾, and from the first step on the
  run shows 坤; six broken ones the other way (`MarkedLines.all_nines`, `MarkedLines.all_sixes`).
* **The counter adding one (加一).** Line 1 the lowest place, adding one turns the lowest broken line
  and every unbroken line below it (`addOne`, `carryAt`). It merges nothing and has one orbit of
  sixty-four: every configuration can be had from every other, and each first comes back at the
  sixty-fourth step (`addOne_lossless`, `addOne_reach`, `addOne_sixtyfour`, `addOne_first_return`,
  `addOne_one_orbit`). Line `k` turns every `2 ^ (k - 1)` steps, the lines below it then as they
  were (`period_pow`, `orbit_period`, `line_turns`).
* **The six orbits of the law of waxing and waning.** The rises and falls across the seams (承, 乘,
  `Becoming.HexagramPlaces`), with one more where the bottom and top lines agree, count the changes
  of line once round (`changesAround`); the law keeps them along every run (`changesAround_waxWane`,
  `changesAround_run`, `changesAround_invariant`). They are one, three or five at every step, on
  twelve, forty and twelve configurations (`changesAround_values`, `changesAround_counts`), so the
  law, though it merges nothing, does not reach 既濟 from 乾, as the counter reaches everything
  (`qian_not_reach_jiJi`, `waxWane_not_reach_every`). Every configuration is on the orbit of one of
  six starts, 乾, 屯, 蒙, 需, 隨 and 既濟 (`orbitStarts`, `on_an_orbit`), which first come back at the
  twelfth step, or the fourth for 隨 (`starts_return`). The orbit is a lumping the law goes alike
  across and is kept by what the law reaches (`orbitIndex`, `orbitIndex_goAlike`,
  `reach_keeps_orbit`); the six starts are on six orbits, of twelve, twelve, twelve, twelve, four
  and twelve configurations, with one, three, three, three, three and five changes around
  (`orbit_census`).

**Classical sources.** `nuclear` is the nuclear hexagram (互卦) of the commentarial tradition;
`addOne` reads the six lines as a binary numeral with line 1 the lowest digit, and with line 1 the
highest digit instead, 邵雍's 先天 sequence lists the sixty-four from 乾 down to 坤 in this count, the
arrangement Leibniz read as binary numerals; the four symmetries are the Klein four-group; `waxWane`
is the twisted ring counter, which carries its pattern round and so keeps the number of changes once
round. The statements are finite computations or instances of the spine's laws
(`Law.Drawn.not_returns`, `Learning.goAlike_iff_lumped`, `Branching.law_reach_iff`,
`Invariant.reach`), stated along the runs of the spine where they are laws of a course. What is the
spine's own is that each is an instance of a law stated for every world.

No ethical predicate, ranking or axiom occurs.
-/
namespace Becoming

open Generative

namespace Hexagram

/-! ## Counting over the received order -/

theorem not_mem_of_memb {s : Hexagram} : ∀ {l : List Hexagram}, memb s l = false → s ∉ l
  | [], _, mem => nomatch mem
  | _ :: _, h, .head _ => Bool.noConfusion ((eqb_self s).symm.trans (neither h).1)
  | _ :: _, h, .tail _ mem => not_mem_of_memb (neither h).2 mem

/-- No configuration occurs twice in a list, told line by line. -/
def distinctb : List Hexagram → Bool
  | [] => true
  | s :: l => !memb s l && distinctb l

theorem nodup_of_distinctb : ∀ {l : List Hexagram}, distinctb l = true → l.Nodup
  | [], _ => List.Pairwise.nil
  | _ :: l, h => List.Pairwise.cons
      (fun _ mem same => not_mem_of_memb (ListTests.false_of_not (bool_of_and_true h).1)
        (Eq.subst (motive := fun x => x ∈ l) same.symm mem))
      (nodup_of_distinctb (bool_of_and_true h).2)

/-- **The received order lists each configuration once**, so a count over it is a count of
configurations (with `mem_order`). -/
theorem order_nodup : order.Nodup := nodup_of_distinctb rfl

/-- All lines unbroken (乾). -/
def allUnbroken : Hexagram := ⟨true, true, true, true, true, true⟩

/-- A configuration a law leaves as it is stays along its run. -/
theorem orbit_still {next : Hexagram → Hexagram} {s : Hexagram} (still : next s = s) :
    ∀ n, Law.orbit next s n = s
  | 0 => rfl
  | n + 1 => (congrArg next (orbit_still still n)).trans still

/-! ## The nuclear law (互) -/

/-- The nuclear law (互): lines 2 to 4 become the lower trigram and lines 3 to 5 the upper; the
bottom and top lines pass out. -/
def nuclear : Hexagram → Hexagram
  | ⟨_, b, c, d, e, _⟩ => ⟨b, c, d, c, d, e⟩

/-- The four inner lines, 2 to 5 (中爻). -/
def inner (s : Hexagram) : Bool × Bool × Bool × Bool := (s.l2, s.l3, s.l4, s.l5)

/-- **What the nuclear law makes of a hexagram is fixed by its four inner lines.** -/
theorem nuclear_inner : Learning.Lumped inner nuclear := by
  intro ⟨_, b, c, d, e, _⟩ ⟨_, b', c', d', e', _⟩ same
  have lines : (b, c, d, e) = (b', c', d', e') := same
  cases lines
  rfl

/-- **So two runs whose starts agree in lines 2 to 5 are one run from the first step on**: the
bottom and top lines are lost at once. -/
theorem run_inner {s t : Hexagram} (same : inner s = inner t) (n : Nat) :
    (Law.run nuclear s).state (n + 1) = (Law.run nuclear t).state (n + 1) :=
  (Law.orbit_shift nuclear s n).trans
    ((congrArg (fun x => Law.orbit nuclear x n) (nuclear_inner s t same)).trans
      (Law.orbit_shift nuclear t n).symm)

/-- **The nuclear law merges**: 剝 and 坤 go on to 坤. -/
theorem nuclear_merges : Law.Merges nuclear :=
  Law.merges_iff.mpr ⟨falling 5, allBroken, ne_of_eqb rfl, rfl⟩

/-- The same merge, read on the law as a process of the spine. -/
theorem nuclear_process_merges : Branching.Merges (Law.process nuclear) :=
  Branching.law_merges_iff.mpr nuclear_merges

/-- **A possibility is lost for good**, by `Law.Merges.loses`, read on the law as a process. -/
theorem nuclear_loses : ¬ Branching.KeepsPossibilities (Law.process nuclear) :=
  fun keeps => nuclear_merges.loses mem_order
    (fun s => (Branching.law_keeps_iff.mp keeps) order.length s)

/-- The inner pair, lines 3 and 4. -/
def innerPair (s : Hexagram) : Bool × Bool := (s.l3, s.l4)

/-- A pair of lines three times over, from the bottom. -/
def thrice : Bool × Bool → Hexagram
  | (x, y) => ⟨x, y, x, y, x, y⟩

/-- **Two steps of the nuclear law leave lines 3 and 4, three times over.** -/
theorem nuclear_two : ∀ s : Hexagram, Law.orbit nuclear s 2 = thrice (innerPair s)
  | ⟨_, _, _, _, _, _⟩ => rfl

/-- **So two steps on are fixed by lines 3 and 4 alone.** -/
theorem nuclear_two_lumped : Learning.Lumped innerPair (fun s => Law.orbit nuclear s 2) :=
  fun s t same => (nuclear_two s).trans ((congrArg thrice same).trans (nuclear_two t).symm)

/-- **Two runs whose starts agree in lines 3 and 4 are one run from the second step on.** -/
theorem run_two_middle {s t : Hexagram} (same : innerPair s = innerPair t) (n : Nat) :
    (Law.run nuclear s).state (2 + n) = (Law.run nuclear t).state (2 + n) :=
  (Law.orbit_add nuclear s 2 n).trans
    ((congrArg (fun x => Law.orbit nuclear x n) (nuclear_two_lumped s t same)).trans
      (Law.orbit_add nuclear t 2 n).symm)

theorem thrice_inj : ∀ {p q : Bool × Bool}, thrice p = thrice q → p = q
  | (x, y), (x', y'), same => by
    have lines : (⟨x, y, x, y, x, y⟩ : Hexagram) = ⟨x', y', x', y', x', y'⟩ := same
    cases lines
    rfl

/-- Lines 3 and 4 swap at every step. -/
theorem innerPair_nuclear : ∀ s : Hexagram, innerPair (nuclear s) = (s.l4, s.l3)
  | ⟨_, _, _, _, _, _⟩ => rfl

theorem swap_eq {x y x' y' : Bool} (same : (x, y) = (x', y')) : (y, x) = (y', x') := by
  cases same
  rfl

/-- **Lines 3 and 4 are a lumping the nuclear law goes alike across**: they swap. -/
theorem innerPair_lumped : Learning.Lumped innerPair (fun s => innerPair (nuclear s)) :=
  fun s t same => (innerPair_nuclear s).trans ((swap_eq same).trans (innerPair_nuclear t).symm)

/-- The same, by `Learning.goAlike_iff_lumped`. -/
theorem innerPair_goAlike : GoAlike (Law.process nuclear) innerPair :=
  Learning.goAlike_iff_lumped.mpr innerPair_lumped

/-- **The count of unbroken lines is not**: 剝 and 比 have one each, and go on to none and to
one. -/
theorem nuclear_yang_not_lumped : ¬ Learning.Lumped yang (fun s => yang (nuclear s)) :=
  fun lumped =>
    absurd (lumped (falling 5) ⟨false, false, false, false, true, false⟩ rfl) (by decide)

theorem nuclear_yang_not_goAlike : ¬ GoAlike (Law.process nuclear) yang :=
  fun alike => nuclear_yang_not_lumped (Learning.goAlike_iff_lumped.mp alike)

/-- 乾, 坤, 既濟 and 未濟: the region the nuclear law draws every configuration into. -/
def NuclearAttractor (s : Hexagram) : Prop :=
  s = allUnbroken ∨ s = allBroken ∨ s = jiJi ∨ s = weiJi

/-- The same, told line by line. -/
def attractorb (s : Hexagram) : Bool :=
  eqb s allUnbroken || eqb s allBroken || eqb s jiJi || eqb s weiJi

theorem attractor_of_attractorb {s : Hexagram} (h : attractorb s = true) : NuclearAttractor s :=
  match ListTests.or_cases h with
  | .inr w => .inr (.inr (.inr (eq_of_eqb w)))
  | .inl h3 => match ListTests.or_cases h3 with
    | .inr j => .inr (.inr (.inl (eq_of_eqb j)))
    | .inl h2 => match ListTests.or_cases h2 with
      | .inr k => .inr (.inl (eq_of_eqb k))
      | .inl q => .inl (eq_of_eqb q)

theorem not_attractor_of_attractorb {s : Hexagram} (h : attractorb s = false) :
    ¬ NuclearAttractor s :=
  match neither h with
  | ⟨h3, w⟩ => match neither h3 with
    | ⟨h2, j⟩ => match neither h2 with
      | ⟨q, k⟩ => fun
        | .inl e => ne_of_eqb q e
        | .inr (.inl e) => ne_of_eqb k e
        | .inr (.inr (.inl e)) => ne_of_eqb j e
        | .inr (.inr (.inr e)) => ne_of_eqb w e

theorem thrice_attractor : ∀ p : Bool × Bool, NuclearAttractor (thrice p)
  | (true, true) => .inl rfl
  | (false, false) => .inr (.inl rfl)
  | (true, false) => .inr (.inr (.inl rfl))
  | (false, true) => .inr (.inr (.inr rfl))

/-- **Within two steps every configuration is in the attractor.** -/
theorem nuclear_two_attractor (s : Hexagram) : NuclearAttractor (Law.orbit nuclear s 2) :=
  Eq.subst (motive := NuclearAttractor) (nuclear_two s).symm (thrice_attractor (innerPair s))

theorem nuclear_allUnbroken : nuclear allUnbroken = allUnbroken := rfl

theorem nuclear_allBroken : nuclear allBroken = allBroken := rfl

theorem nuclear_jiJi : nuclear jiJi = weiJi := rfl

theorem nuclear_weiJi : nuclear weiJi = jiJi := rfl

/-- **Two configurations stay and two take turns**: along their runs, 乾 and 坤 are left as they
are at every step, and the run from 既濟 is at 既濟 at every even step and at 未濟 at every odd
one. -/
theorem nuclear_two_fixed_one_cycle (n : Nat) :
    (Law.run nuclear allUnbroken).state n = allUnbroken ∧
      (Law.run nuclear allBroken).state n = allBroken ∧
      (Law.run nuclear jiJi).state (2 * n) = jiJi ∧
      (Law.run nuclear jiJi).state (2 * n + 1) = weiJi ∧ jiJi ≠ weiJi :=
  have even : (Law.run nuclear jiJi).state (2 * n) = jiJi :=
    Law.orbit_mul (show Law.orbit nuclear jiJi 2 = jiJi from
      (congrArg nuclear nuclear_jiJi).trans nuclear_weiJi) n
  ⟨orbit_still nuclear_allUnbroken n, orbit_still nuclear_allBroken n, even,
   (congrArg nuclear even).trans nuclear_jiJi, ne_of_eqb rfl⟩

/-- **The nuclear law leaves 乾 and 坤 as they are, and nothing else.** -/
theorem nuclear_fixed_iff (s : Hexagram) : nuclear s = s ↔ s = allUnbroken ∨ s = allBroken := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
      first
      | exact ⟨fun _ => .inl rfl, fun _ => rfl⟩
      | exact ⟨fun _ => .inr rfl, fun _ => rfl⟩
      | exact ⟨fun h => absurd h (ne_of_eqb rfl),
          fun | .inl h => absurd h (ne_of_eqb rfl) | .inr h => absurd h (ne_of_eqb rfl)⟩

/-- **A run of the nuclear law stays where it starts exactly from 乾 and 坤.** -/
theorem nuclear_rests_iff (s : Hexagram) :
    (∀ n, (Law.run nuclear s).state n = s) ↔ s = allUnbroken ∨ s = allBroken :=
  ⟨fun stays => (nuclear_fixed_iff s).mp (stays 1),
   fun which => orbit_still ((nuclear_fixed_iff s).mpr which)⟩

/-- **The attractor is a region the law never leaves.** -/
theorem attractor_absorbing : Law.Absorbing nuclear NuclearAttractor
  | _, .inl e => .inl ((congrArg nuclear e).trans nuclear_allUnbroken)
  | _, .inr (.inl e) => .inr (.inl ((congrArg nuclear e).trans nuclear_allBroken))
  | _, .inr (.inr (.inl e)) => .inr (.inr (.inr ((congrArg nuclear e).trans nuclear_jiJi)))
  | _, .inr (.inr (.inr e)) => .inr (.inr (.inl ((congrArg nuclear e).trans nuclear_weiJi)))

/-- Each configuration of the attractor returns, 乾 and 坤 at once and 既濟 and 未濟 at the
second step. -/
theorem attractor_returns {s : Hexagram} : NuclearAttractor s → Law.Returns nuclear s
  | .inl e => Law.returns_iff.mpr ⟨1, Nat.succ_pos 0, by subst e; rfl⟩
  | .inr (.inl e) => Law.returns_iff.mpr ⟨1, Nat.succ_pos 0, by subst e; rfl⟩
  | .inr (.inr (.inl e)) => Law.returns_iff.mpr ⟨2, Nat.succ_pos 1, by subst e; rfl⟩
  | .inr (.inr (.inr e)) => Law.returns_iff.mpr ⟨2, Nat.succ_pos 1, by subst e; rfl⟩

/-- **Every other configuration is drawn into the attractor.** -/
theorem outside_drawn {s : Hexagram} (outside : ¬ NuclearAttractor s) :
    Law.DrawnInto nuclear NuclearAttractor s :=
  ⟨outside, 2, nuclear_two_attractor s⟩

/-- **And never returns**, by `Law.Drawn.not_returns`. -/
theorem outside_not_returns {s : Hexagram} (outside : ¬ NuclearAttractor s) :
    ¬ Law.Returns nuclear s :=
  Law.Drawn.not_returns ⟨_, attractor_absorbing, outside_drawn outside⟩

/-- **Exactly 乾, 坤, 既濟 and 未濟 return under the nuclear law.** -/
theorem returns_iff_attractor (s : Hexagram) : Law.Returns nuclear s ↔ NuclearAttractor s :=
  ⟨fun returns => match h : attractorb s with
    | true => attractor_of_attractorb h
    | false => absurd returns (outside_not_returns (not_attractor_of_attractorb h)),
   attractor_returns⟩

/-- The same, read on the law as a process of the spine. -/
theorem nuclear_process_returns_iff (s : Hexagram) :
    Branching.Returns (Law.process nuclear) s ↔ NuclearAttractor s :=
  Branching.law_returns_iff.trans (returns_iff_attractor s)

/-- **Exactly the first two and the last two configurations of the received order return under
the nuclear law**: 乾 and 坤 open the order, 既濟 and 未濟 close it. -/
theorem process_returns_iff_ends (s : Hexagram) :
    Branching.Returns (Law.process nuclear) s ↔ s ∈ order.take 2 ++ order.drop 62 :=
  have ends : order.take 2 ++ order.drop 62 = [allUnbroken, allBroken, jiJi, weiJi] := rfl
  (nuclear_process_returns_iff s).trans (ends ▸
    ⟨fun at_rest => by
      cases at_rest with
      | inl e => subst e; exact .head _
      | inr rest => cases rest with
        | inl e => subst e; exact .tail _ (.head _)
        | inr rest => cases rest with
          | inl e => subst e; exact .tail _ (.tail _ (.head _))
          | inr e => subst e; exact .tail _ (.tail _ (.tail _ (.head _))),
     fun mem => by
      cases mem with
      | head => exact .inl rfl
      | tail _ mem => cases mem with
        | head => exact .inr (.inl rfl)
        | tail _ mem => cases mem with
          | head => exact .inr (.inr (.inl rfl))
          | tail _ mem => cases mem with
            | head => exact .inr (.inr (.inr rfl))
            | tail _ mem => cases mem⟩)

/-- **Along every run of the nuclear law, from the second step on the run is in the
attractor.** -/
theorem run_in_attractor (s : Hexagram) (n : Nat) :
    NuclearAttractor ((Law.run nuclear s).state (2 + n)) :=
  attractor_absorbing.orbit (nuclear_two_attractor s) n

/-- **Four configurations are in the attractor, twelve enter it at the first step and forty-eight
at the second**, counted over the received order. -/
theorem entry_counts :
    (order.filter fun s => attractorb ((Law.run nuclear s).state 0)).length = 4 ∧
    (order.filter fun s => !attractorb ((Law.run nuclear s).state 0) &&
      attractorb ((Law.run nuclear s).state 1)).length = 12 ∧
    (order.filter fun s => !attractorb ((Law.run nuclear s).state 1)).length = 48 :=
  ⟨rfl, rfl, rfl⟩

theorem thrice_back : ∀ p : Bool × Bool, Law.orbit nuclear (thrice p) 2 = thrice p
  | (_, _) => rfl

/-- **Where a course comes to rest is fixed by lines 3 and 4**: at every even step from the second
on, the run is at lines 3 and 4 three times over. -/
theorem run_rests_at (s : Hexagram) (k : Nat) :
    (Law.run nuclear s).state (2 + 2 * k) = thrice (innerPair s) :=
  (Law.orbit_add nuclear s 2 (2 * k)).trans
    ((congrArg (fun x => Law.orbit nuclear x (2 * k)) (nuclear_two s)).trans
      (Law.orbit_mul (thrice_back (innerPair s)) k))

/-- **The basin of a course is told by lines 3 and 4.** -/
theorem basin_iff (s : Hexagram) (p : Bool × Bool) :
    (Law.run nuclear s).state 2 = thrice p ↔ innerPair s = p :=
  ⟨fun at_two => thrice_inj ((nuclear_two s).symm.trans at_two),
   fun same => (nuclear_two s).trans (congrArg thrice same)⟩

theorem and_of_both : ∀ {x y : Bool}, x = true ∧ y = true → (x && y) = true
  | true, true, _ => rfl
  | false, _, h => Bool.noConfusion h.1
  | true, false, h => Bool.noConfusion h.2

theorem or_of_neither : ∀ {x y : Bool}, x = false ∧ y = false → (x || y) = false
  | false, false, _ => rfl
  | true, _, h => Bool.noConfusion h.1
  | false, true, h => Bool.noConfusion h.2

/-- **A course goes to 乾 exactly where lines 3 and 4 are unbroken.** -/
theorem qian_basin (s : Hexagram) :
    (Law.run nuclear s).state 2 = allUnbroken ↔ s.l3 = true ∧ s.l4 = true := by
  cases s with
  | mk a b c d e f =>
    cases c <;> cases d <;>
      first
      | exact ⟨fun _ => ⟨rfl, rfl⟩, fun _ => rfl⟩
      | exact ⟨fun h => absurd h (ne_of_eqb rfl), fun h => Bool.noConfusion (and_of_both h)⟩

/-- **To 坤 exactly where both are broken.** -/
theorem kun_basin (s : Hexagram) :
    (Law.run nuclear s).state 2 = allBroken ↔ s.l3 = false ∧ s.l4 = false := by
  cases s with
  | mk a b c d e f =>
    cases c <;> cases d <;>
      first
      | exact ⟨fun _ => ⟨rfl, rfl⟩, fun _ => rfl⟩
      | exact ⟨fun h => absurd h (ne_of_eqb rfl), fun h => Bool.noConfusion (or_of_neither h)⟩

/-- **Into the turns of 既濟 and 未濟 exactly where they differ.** -/
theorem cycle_basin (s : Hexagram) :
    ((Law.run nuclear s).state 2 = jiJi ∨ (Law.run nuclear s).state 2 = weiJi) ↔
      s.l3 = !s.l4 := by
  cases s with
  | mk a b c d e f =>
    cases c <;> cases d <;>
      first
      | exact ⟨fun _ => rfl, fun _ => .inl rfl⟩
      | exact ⟨fun _ => rfl, fun _ => .inr rfl⟩
      | exact ⟨fun | .inl h => absurd h (ne_of_eqb rfl) | .inr h => absurd h (ne_of_eqb rfl),
          fun h => Bool.noConfusion h⟩

/-- **Sixteen configurations go to 乾, sixteen to 坤 and thirty-two into the turns of 既濟 and
未濟**, counted over the received order. -/
theorem basin_counts :
    (order.filter fun s => eqb ((Law.run nuclear s).state 2) allUnbroken).length = 16 ∧
    (order.filter fun s => eqb ((Law.run nuclear s).state 2) allBroken).length = 16 ∧
    (order.filter fun s => eqb ((Law.run nuclear s).state 2) jiJi ||
      eqb ((Law.run nuclear s).state 2) weiJi).length = 32 :=
  ⟨rfl, rfl, rfl⟩

/-! ## The four symmetries (錯, 綜) -/

/-- **The nuclear law commutes with changing every line.** -/
theorem nuclear_complement : ∀ s : Hexagram, nuclear (complement s) = complement (nuclear s)
  | ⟨_, _, _, _, _, _⟩ => rfl

/-- **And with turning over.** -/
theorem nuclear_reverse : ∀ s : Hexagram, nuclear (reverse s) = reverse (nuclear s)
  | ⟨_, _, _, _, _, _⟩ => rfl

theorem complement_reverse : ∀ s : Hexagram, complement (reverse s) = reverse (complement s)
  | ⟨_, _, _, _, _, _⟩ => rfl

theorem reverse_reverse : ∀ s : Hexagram, reverse (reverse s) = s
  | ⟨_, _, _, _, _, _⟩ => rfl

theorem reverse_complement_reverse : ∀ s : Hexagram, reverse (complement (reverse s)) = complement s
  | ⟨_, _, _, _, _, _⟩ => rfl

/-- The four symmetries of a hexagram: keeping it, changing every line (錯), turning it over (綜),
and both (錯綜). -/
inductive Symmetry where
  | keep
  | change
  | turn
  | both

namespace Symmetry

/-- What a symmetry does to a hexagram. -/
def act : Symmetry → Hexagram → Hexagram
  | keep, s => s
  | change, s => Hexagram.complement s
  | turn, s => Hexagram.reverse s
  | both, s => Hexagram.complement (Hexagram.reverse s)

/-- One symmetry after another. -/
def comp : Symmetry → Symmetry → Symmetry
  | keep, g => g
  | change, keep => change
  | change, change => keep
  | change, turn => both
  | change, both => turn
  | turn, keep => turn
  | turn, change => both
  | turn, turn => keep
  | turn, both => change
  | both, keep => both
  | both, change => turn
  | both, turn => change
  | both, both => keep

/-- **One symmetry after another is the symmetry they compose to.** -/
theorem act_comp : ∀ (g h : Symmetry) (s : Hexagram), (comp g h).act s = g.act (h.act s)
  | keep, _, _ => rfl
  | change, keep, _ => rfl
  | change, change, s => (complement_complement s).symm
  | change, turn, _ => rfl
  | change, both, s => (complement_complement (Hexagram.reverse s)).symm
  | turn, keep, _ => rfl
  | turn, change, s => complement_reverse s
  | turn, turn, s => (reverse_reverse s).symm
  | turn, both, s => (reverse_complement_reverse s).symm
  | both, keep, _ => rfl
  | both, change, s => ((congrArg Hexagram.complement (complement_reverse s).symm).trans
      (complement_complement (Hexagram.reverse s))).symm
  | both, turn, s => (congrArg Hexagram.complement (reverse_reverse s)).symm
  | both, both, s => ((congrArg Hexagram.complement (reverse_complement_reverse s)).trans
      (complement_complement s)).symm

/-- **Each symmetry is its own inverse.** -/
theorem comp_self : ∀ g : Symmetry, comp g g = keep
  | keep => rfl
  | change => rfl
  | turn => rfl
  | both => rfl

/-- **Any two commute.** -/
theorem comp_comm : ∀ g h : Symmetry, comp g h = comp h g := by
  intro g h
  cases g <;> cases h <;> rfl

theorem act_self (g : Symmetry) (s : Hexagram) : g.act (g.act s) = s :=
  (act_comp g g s).symm.trans (congrArg (fun x => act x s) (comp_self g))

end Symmetry

/-- **The nuclear law commutes with each of the four symmetries.** -/
theorem nuclear_act : ∀ (g : Symmetry) (s : Hexagram), nuclear (g.act s) = g.act (nuclear s)
  | .keep, _ => rfl
  | .change, s => nuclear_complement s
  | .turn, s => nuclear_reverse s
  | .both, s => (nuclear_complement (reverse s)).trans (congrArg complement (nuclear_reverse s))

/-- **So each takes every run of the nuclear law to a run of it** (`Law.Commutes.iterate`). -/
theorem nuclear_run_act (g : Symmetry) (s : Hexagram) (n : Nat) :
    (Law.run nuclear (g.act s)).state n = g.act ((Law.run nuclear s).state n) :=
  Law.Commutes.iterate (nuclear_act g) s n

/-- **The runs from a configuration and from its complement never meet**: the nuclear law commutes
with the complement, which moves every configuration, so this is what a commuting law keeps apart
(`Law.Commutes.apart`). -/
theorem run_complement_apart (s : Hexagram) (n : Nat) :
    (Law.run nuclear (complement s)).state n ≠ (Law.run nuclear s).state n :=
  Law.Commutes.apart nuclear_complement complement_moves s n

/-- The binary value of a hexagram, line 1 the lowest place. -/
def binaryValue (s : Hexagram) : Nat :=
  s.l1.toNat + 2 * s.l2.toNat + 4 * s.l3.toNat + 8 * s.l4.toNat + 16 * s.l5.toNat +
    32 * s.l6.toNat

/-- Of two hexagrams, the one of lesser binary value. -/
def leastOf (s t : Hexagram) : Hexagram :=
  match Nat.ble (binaryValue s) (binaryValue t) with
  | true => s
  | false => t

/-- The class of a hexagram under the four symmetries, named by its member of least binary
value. -/
def classOf (s : Hexagram) : Hexagram :=
  leastOf (leastOf s (complement s)) (leastOf (reverse s) (complement (reverse s)))

/-- **A symmetry keeps the class.** -/
theorem classOf_act (g : Symmetry) (s : Hexagram) : classOf (g.act s) = classOf s := by
  cases g
  · rfl
  all_goals
    cases s with
    | mk a b c d e f =>
      cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- The member naming a class is the hexagram under some symmetry. -/
theorem classOf_member (s : Hexagram) : ∃ g : Symmetry, classOf s = g.act s := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
      first
      | exact ⟨.keep, rfl⟩
      | exact ⟨.change, rfl⟩
      | exact ⟨.turn, rfl⟩
      | exact ⟨.both, rfl⟩

/-- **Two hexagrams are in one class exactly where a symmetry takes one to the other.** -/
theorem classOf_eq_iff (s t : Hexagram) : classOf s = classOf t ↔ ∃ g : Symmetry, t = g.act s :=
  ⟨fun same => match classOf_member s, classOf_member t with
    | ⟨g, hs⟩, ⟨h, ht⟩ =>
      ⟨h.comp g, (Symmetry.act_self h t).symm.trans
        ((congrArg h.act (ht.symm.trans (same.symm.trans hs))).trans
          (Symmetry.act_comp h g s).symm)⟩,
   fun ⟨g, e⟩ => ((congrArg classOf e).trans (classOf_act g s)).symm⟩

/-- The classes of two members, in increasing binary value, each named by its member of least
binary value: 坤 乾, 泰 否, 歸妹 漸, 小過 中孚, 坎 離, 既濟 未濟, 隨 蠱, 大過 頤. -/
def pairClasses : List Hexagram :=
  [⟨false, false, false, false, false, false⟩,
    ⟨true, true, true, false, false, false⟩,
    ⟨true, true, false, true, false, false⟩,
    ⟨false, false, true, true, false, false⟩,
    ⟨false, true, false, false, true, false⟩,
    ⟨true, false, true, false, true, false⟩,
    ⟨true, false, false, true, true, false⟩,
    ⟨false, true, true, true, true, false⟩]

/-- The classes of four members, in increasing binary value. -/
def fourClasses : List Hexagram :=
  [⟨true, false, false, false, false, false⟩,
    ⟨false, true, false, false, false, false⟩,
    ⟨true, true, false, false, false, false⟩,
    ⟨false, false, true, false, false, false⟩,
    ⟨true, false, true, false, false, false⟩,
    ⟨false, true, true, false, false, false⟩,
    ⟨true, false, false, true, false, false⟩,
    ⟨false, true, false, true, false, false⟩,
    ⟨true, false, true, true, false, false⟩,
    ⟨false, true, true, true, false, false⟩,
    ⟨true, false, false, false, true, false⟩,
    ⟨false, true, true, false, true, false⟩]

/-- The twenty classes. -/
def classes : List Hexagram := pairClasses ++ fourClasses

/-- The number of configurations in the class a hexagram names. -/
def classSize (r : Hexagram) : Nat := (order.filter fun s => eqb (classOf s) r).length

theorem classOf_mem (s : Hexagram) : classOf s ∈ classes := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
      exact mem_of_memb rfl

/-- **Twenty classes, eight of two members and twelve of four**: each listed hexagram names its
class, none twice, every hexagram's class is listed, and the counts are over the received
order. -/
theorem class_census :
    classes.length = 20 ∧ classes.Nodup ∧ classes.map classOf = classes ∧
      (∀ s, classOf s ∈ classes) ∧
      pairClasses.map classSize = [2, 2, 2, 2, 2, 2, 2, 2] ∧
      fourClasses.map classSize = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] :=
  ⟨rfl, nodup_of_distinctb rfl, rfl, classOf_mem, rfl, rfl⟩

/-- **The classes are a lumping the nuclear law goes alike across**, since it commutes with every
symmetry. -/
theorem classes_lumped : Learning.Lumped classOf (fun s => classOf (nuclear s)) :=
  fun s t same => match (classOf_eq_iff s t).mp same with
    | ⟨g, e⟩ => (classOf_eq_iff (nuclear s) (nuclear t)).mpr
        ⟨g, (congrArg nuclear e).trans (nuclear_act g s)⟩

/-- The same, by `Learning.goAlike_iff_lumped`. -/
theorem classes_goAlike : GoAlike (Law.process nuclear) classOf :=
  Learning.goAlike_iff_lumped.mpr classes_lumped

/-- **The law of waxing and waning does not go alike across them**: 剝 and 復 are one class,
turned over, and go on to 坤 and 臨. -/
theorem classes_not_lumped_waxWane : ¬ Learning.Lumped classOf (fun s => classOf (waxWane s)) :=
  fun lumped => absurd (lumped (falling 5) (rising 1) rfl) (ne_of_eqb rfl)

theorem classes_not_goAlike_waxWane : ¬ GoAlike (Law.process waxWane) classOf :=
  fun alike => classes_not_lumped_waxWane (Learning.goAlike_iff_lumped.mp alike)

theorem any_sound {p : Hexagram × Hexagram → Bool} :
    ∀ {l : List (Hexagram × Hexagram)}, l.any p = true → ∃ q, q ∈ l ∧ p q = true
  | [], h => Bool.noConfusion h
  | q :: _, h => match ListTests.or_cases h with
    | .inl here => ⟨q, .head _, here⟩
    | .inr there => match any_sound there with
      | ⟨q', mem, holds⟩ => ⟨q', .tail _ mem, holds⟩

/-- Some pair of the received order pairs by changing every line and holds `s`, told line by
line. -/
def pairedByChange (s : Hexagram) : Bool :=
  (pairs order).any fun q =>
    eqb (reverse q.1) q.1 && eqb q.2 (complement q.1) && (eqb s q.1 || eqb s q.2)

theorem pairedByChange_sound {s : Hexagram} (h : pairedByChange s = true) :
    ∃ q, q ∈ pairs order ∧ reverse q.1 = q.1 ∧ q.2 = complement q.1 ∧ (s = q.1 ∨ s = q.2) :=
  match any_sound h with
  | ⟨q, mem, holds⟩ => match bool_of_and_true holds with
    | ⟨rule, which⟩ => match bool_of_and_true rule with
      | ⟨fixed, changed⟩ =>
        ⟨q, mem, eq_of_eqb fixed, eq_of_eqb changed, match ListTests.or_cases which with
          | .inl first => .inl (eq_of_eqb first)
          | .inr second => .inr (eq_of_eqb second)⟩

/-- **The configurations turning over leaves as they are are exactly those the received order
pairs by changing every line**: 乾 坤, 頤 大過, 坎 離, 中孚 小過. -/
theorem turn_fixed_iff (s : Hexagram) : reverse s = s ↔
    ∃ q, q ∈ pairs order ∧ reverse q.1 = q.1 ∧ q.2 = complement q.1 ∧ (s = q.1 ∨ s = q.2) := by
  refine ⟨?_, fun ⟨q, _, fixed, changed, which⟩ => ?_⟩
  · cases s with
    | mk a b c d e f =>
      cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
        first
        | exact fun h => absurd h (ne_of_eqb rfl)
        | exact fun _ => pairedByChange_sound rfl
  · cases which with
    | inl e =>
      subst e
      exact fixed
    | inr e =>
      subst e
      exact (congrArg reverse changed).trans ((complement_reverse q.1).symm.trans
        ((congrArg complement fixed).trans changed.symm))

/-- Some pair of the received order is both turned over and changed in every line and holds
`s`, told line by line. -/
def pairedByBoth (s : Hexagram) : Bool :=
  (pairs order).any fun q =>
    eqb q.2 (reverse q.1) && eqb q.2 (complement q.1) && (eqb s q.1 || eqb s q.2)

theorem pairedByBoth_sound {s : Hexagram} (h : pairedByBoth s = true) :
    ∃ q, q ∈ pairs order ∧ q.2 = reverse q.1 ∧ q.2 = complement q.1 ∧ (s = q.1 ∨ s = q.2) :=
  match any_sound h with
  | ⟨q, mem, holds⟩ => match bool_of_and_true holds with
    | ⟨rule, which⟩ => match bool_of_and_true rule with
      | ⟨turned, changed⟩ =>
        ⟨q, mem, eq_of_eqb turned, eq_of_eqb changed, match ListTests.or_cases which with
          | .inl first => .inl (eq_of_eqb first)
          | .inr second => .inr (eq_of_eqb second)⟩

/-- **The configurations turning over and changing every line take to the same hexagram are
exactly the pairs of the received order in which turning over and changing every line agree**:
泰 否, 隨 蠱, 漸 歸妹, 既濟 未濟. -/
theorem both_fixed_iff (s : Hexagram) : complement (reverse s) = s ↔
    ∃ q, q ∈ pairs order ∧ q.2 = reverse q.1 ∧ q.2 = complement q.1 ∧ (s = q.1 ∨ s = q.2) := by
  refine ⟨?_, fun ⟨q, _, turned, changed, which⟩ => ?_⟩
  · cases s with
    | mk a b c d e f =>
      cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
        first
        | exact fun h => absurd h (ne_of_eqb rfl)
        | exact fun _ => pairedByBoth_sound rfl
  · cases which with
    | inl e =>
      subst e
      exact (congrArg complement (turned.symm.trans changed)).trans (complement_complement q.1)
    | inr e =>
      subst e
      exact (congrArg (fun x => complement (reverse x)) turned).trans
        ((congrArg complement (reverse_reverse q.1)).trans changed.symm)

/-! ## Turning and staying lines (老, 少) and the hexagram the lines go to (之卦) -/

/-- A line with its mark. A turning line (老: 老陽, nine, unbroken; 老陰, six, broken) changes into
its opposite at the next step; a staying line (少: 少陽, seven; 少陰, eight) is kept. -/
inductive Marked where
  | turning (b : Bool)
  | staying (b : Bool)

namespace Marked

/-- The line shown, unbroken (`true`) or broken. -/
def value : Marked → Bool
  | turning b => b
  | staying b => b

/-- The next step: a turning line changes into its opposite and stays; a staying line is kept
(老變少不變). -/
def settle : Marked → Marked
  | turning b => staying (!b)
  | staying b => staying b

/-- The line is staying. -/
def stays : Marked → Bool
  | turning _ => false
  | staying _ => true

theorem settle_settle : ∀ x : Marked, settle (settle x) = settle x
  | turning _ => rfl
  | staying _ => rfl

theorem stays_settle : ∀ x : Marked, stays (settle x) = true
  | turning _ => rfl
  | staying _ => rfl

theorem settle_of_stays : ∀ {x : Marked}, stays x = true → settle x = x
  | staying _, _ => rfl
  | turning _, h => Bool.noConfusion h

theorem turning_ne_staying {b c : Bool} : turning b ≠ staying c :=
  fun h => Marked.noConfusion h

theorem stays_of_settle : ∀ {x : Marked}, settle x = x → stays x = true
  | staying _, _ => rfl
  | turning _, h => absurd h.symm turning_ne_staying

end Marked

/-- Six marked lines, read from the bottom. -/
structure MarkedLines where
  m1 : Marked
  m2 : Marked
  m3 : Marked
  m4 : Marked
  m5 : Marked
  m6 : Marked

namespace MarkedLines

/-- The hexagram the lines show (本卦). -/
def shown : MarkedLines → Hexagram
  | ⟨a, b, c, d, e, f⟩ => ⟨a.value, b.value, c.value, d.value, e.value, f.value⟩

/-- The next step: every turning line changes into its opposite and stays. -/
def settle : MarkedLines → MarkedLines
  | ⟨a, b, c, d, e, f⟩ => ⟨a.settle, b.settle, c.settle, d.settle, e.settle, f.settle⟩

/-- The hexagram the lines go to (之卦): the hexagram shown one step on. -/
def onward (m : MarkedLines) : Hexagram := shown (settle m)

/-- Every line is staying. -/
def staysAll : MarkedLines → Bool
  | ⟨a, b, c, d, e, f⟩ => a.stays && b.stays && c.stays && d.stays && e.stays && f.stays

/-- **Settled in one step**: a second step changes nothing. -/
theorem settle_settle : ∀ m : MarkedLines, settle (settle m) = settle m
  | ⟨a, b, c, d, e, f⟩ => by
    show (⟨a.settle.settle, b.settle.settle, c.settle.settle, d.settle.settle, e.settle.settle,
      f.settle.settle⟩ : MarkedLines) =
        ⟨a.settle, b.settle, c.settle, d.settle, e.settle, f.settle⟩
    rw [Marked.settle_settle a, Marked.settle_settle b, Marked.settle_settle c,
      Marked.settle_settle d, Marked.settle_settle e, Marked.settle_settle f]

theorem staysAll_settle : ∀ m : MarkedLines, staysAll (settle m) = true
  | ⟨a, b, c, d, e, f⟩ => by
    show (a.settle.stays && b.settle.stays && c.settle.stays && d.settle.stays &&
      e.settle.stays && f.settle.stays) = true
    rw [Marked.stays_settle a, Marked.stays_settle b, Marked.stays_settle c,
      Marked.stays_settle d, Marked.stays_settle e, Marked.stays_settle f]
    rfl

/-- **A configuration is left as it is exactly where no line turns.** -/
theorem settle_fixed_iff : ∀ m : MarkedLines, settle m = m ↔ staysAll m = true
  | ⟨a, b, c, d, e, f⟩ =>
    ⟨fun fixed => by
      have ha : a.settle = a := congrArg MarkedLines.m1 fixed
      have hb : b.settle = b := congrArg MarkedLines.m2 fixed
      have hc : c.settle = c := congrArg MarkedLines.m3 fixed
      have hd : d.settle = d := congrArg MarkedLines.m4 fixed
      have he : e.settle = e := congrArg MarkedLines.m5 fixed
      have hf : f.settle = f := congrArg MarkedLines.m6 fixed
      show (a.stays && b.stays && c.stays && d.stays && e.stays && f.stays) = true
      rw [Marked.stays_of_settle ha, Marked.stays_of_settle hb, Marked.stays_of_settle hc,
        Marked.stays_of_settle hd, Marked.stays_of_settle he, Marked.stays_of_settle hf]
      rfl,
     fun all => by
      have ⟨h5, sf⟩ := bool_of_and_true all
      have ⟨h4, se⟩ := bool_of_and_true h5
      have ⟨h3, sd⟩ := bool_of_and_true h4
      have ⟨h2, sc⟩ := bool_of_and_true h3
      have ⟨sa, sb⟩ := bool_of_and_true h2
      show (⟨a.settle, b.settle, c.settle, d.settle, e.settle, f.settle⟩ : MarkedLines) =
        ⟨a, b, c, d, e, f⟩
      rw [Marked.settle_of_stays sa, Marked.settle_of_stays sb, Marked.settle_of_stays sc,
        Marked.settle_of_stays sd, Marked.settle_of_stays se, Marked.settle_of_stays sf]⟩

/-- **The law merges**: a turning unbroken line and a staying broken one go on to one. -/
theorem settle_merges : Law.Merges settle :=
  Law.merges_iff.mpr ⟨⟨.turning true, .staying false, .staying false, .staying false, .staying false, .staying false⟩,
   ⟨.staying false, .staying false, .staying false, .staying false, .staying false, .staying false⟩,
   fun same => Marked.turning_ne_staying (congrArg MarkedLines.m1 same), rfl⟩

/-- The same merge, read on the law as a process of the spine. -/
theorem settle_process_merges : Branching.Merges (Law.process settle) :=
  Branching.law_merges_iff.mpr settle_merges

/-- **Along every run, from the first step on the lines are settled.** -/
theorem run_settled (m : MarkedLines) : ∀ n, (Law.run settle m).state (n + 1) = settle m
  | 0 => rfl
  | n + 1 => (congrArg settle (run_settled m n)).trans (settle_settle m)

/-- **The run rests from the first step on.** -/
theorem run_rests (m : MarkedLines) (n : Nat) :
    (Law.run settle m).state (n + 2) = (Law.run settle m).state (n + 1) :=
  (run_settled m (n + 1)).trans (run_settled m n).symm

/-- **A configuration with a turning line is drawn into those with none.** -/
theorem drawn (m : MarkedLines) (turning : staysAll m = false) :
    Law.DrawnInto settle (fun x => staysAll x = true) m :=
  ⟨fun all => Bool.noConfusion (all.symm.trans turning), 1, staysAll_settle m⟩

/-- **A configuration returns exactly where no line turns**: one with a turning line is drawn
into those with none, which the law never leaves, and so never returns (`Law.Drawn.not_returns`). -/
theorem returns_iff (m : MarkedLines) : Law.Returns settle m ↔ staysAll m = true :=
  ⟨fun returns => match h : staysAll m with
    | true => rfl
    | false => absurd returns
        (Law.Drawn.not_returns ⟨_, fun x _ => staysAll_settle x, drawn m h⟩),
   fun all => Law.returns_iff.mpr ⟨1, Nat.succ_pos 0, (settle_fixed_iff m).mpr all⟩⟩

/-- The same, read on the law as a process of the spine. -/
theorem process_returns_iff (m : MarkedLines) :
    Branching.Returns (Law.process settle) m ↔ staysAll m = true :=
  Branching.law_returns_iff.trans (returns_iff m)

/-- **The hexagram shown is not a lumping the law goes alike across**: 乾 with every line staying,
and 乾 with its bottom line turning, go on to 乾 and to 姤. -/
theorem shown_not_lumped : ¬ Learning.Lumped shown (fun m => shown (settle m)) :=
  fun lumped => absurd
    (lumped ⟨.staying true, .staying true, .staying true, .staying true, .staying true,
        .staying true⟩
      ⟨.turning true, .staying true, .staying true, .staying true, .staying true, .staying true⟩
      rfl)
    (ne_of_eqb rfl)

theorem shown_not_goAlike : ¬ GoAlike (Law.process settle) shown :=
  fun alike => shown_not_lumped (Learning.goAlike_iff_lumped.mp alike)

/-- **The hexagram the lines go to is**: one step on, it is had again. -/
theorem onward_lumped : Learning.Lumped onward (fun m => onward (settle m)) :=
  fun s t same => (congrArg shown (settle_settle s)).trans
    (same.trans (congrArg shown (settle_settle t)).symm)

theorem onward_goAlike : GoAlike (Law.process settle) onward :=
  Learning.goAlike_iff_lumped.mpr onward_lumped

/-- Every line turning, unbroken (`true`: six nines) or broken (six sixes). -/
def allTurning (b : Bool) : MarkedLines :=
  ⟨.turning b, .turning b, .turning b, .turning b, .turning b, .turning b⟩

/-- **Six nines (用九)**: the lines show 乾, and from the first step on the run shows 坤. -/
theorem all_nines (n : Nat) : shown ((Law.run settle (allTurning true)).state 0) = allUnbroken ∧
    shown ((Law.run settle (allTurning true)).state (n + 1)) = allBroken :=
  ⟨rfl, congrArg shown (run_settled _ n)⟩

/-- **Six sixes (用六)**: the lines show 坤, and from the first step on the run shows 乾. -/
theorem all_sixes (n : Nat) : shown ((Law.run settle (allTurning false)).state 0) = allBroken ∧
    shown ((Law.run settle (allTurning false)).state (n + 1)) = allUnbroken :=
  ⟨rfl, congrArg shown (run_settled _ n)⟩

end MarkedLines

/-! ## The counter adding one (加一) -/

/-- One added at line 6: it turns. -/
def carry6 : Hexagram → Hexagram
  | ⟨a, b, c, d, e, f⟩ => ⟨a, b, c, d, e, !f⟩

/-- One added at line 5: a broken line becomes unbroken; an unbroken one becomes broken and one
is carried to line 6. -/
def carry5 : Hexagram → Hexagram
  | ⟨a, b, c, d, false, f⟩ => ⟨a, b, c, d, true, f⟩
  | ⟨a, b, c, d, true, f⟩ => carry6 ⟨a, b, c, d, false, f⟩

/-- One added at line 4. -/
def carry4 : Hexagram → Hexagram
  | ⟨a, b, c, false, e, f⟩ => ⟨a, b, c, true, e, f⟩
  | ⟨a, b, c, true, e, f⟩ => carry5 ⟨a, b, c, false, e, f⟩

/-- One added at line 3. -/
def carry3 : Hexagram → Hexagram
  | ⟨a, b, false, d, e, f⟩ => ⟨a, b, true, d, e, f⟩
  | ⟨a, b, true, d, e, f⟩ => carry4 ⟨a, b, false, d, e, f⟩

/-- One added at line 2. -/
def carry2 : Hexagram → Hexagram
  | ⟨a, false, c, d, e, f⟩ => ⟨a, true, c, d, e, f⟩
  | ⟨a, true, c, d, e, f⟩ => carry3 ⟨a, false, c, d, e, f⟩

/-- One added at line 1. -/
def carry1 : Hexagram → Hexagram
  | ⟨false, b, c, d, e, f⟩ => ⟨true, b, c, d, e, f⟩
  | ⟨true, b, c, d, e, f⟩ => carry2 ⟨false, b, c, d, e, f⟩

/-- One added at a place: the line there turns, and where it was unbroken one is carried to the
place above. -/
def carryAt : Place → Hexagram → Hexagram
  | .p1 => carry1
  | .p2 => carry2
  | .p3 => carry3
  | .p4 => carry4
  | .p5 => carry5
  | .p6 => carry6

/-- The counter adding one (加一), line 1 the lowest place. -/
def addOne : Hexagram → Hexagram := carry1

/-- One taken at line 6. -/
def borrow6 : Hexagram → Hexagram
  | ⟨a, b, c, d, e, f⟩ => ⟨a, b, c, d, e, !f⟩

def borrow5 : Hexagram → Hexagram
  | ⟨a, b, c, d, true, f⟩ => ⟨a, b, c, d, false, f⟩
  | ⟨a, b, c, d, false, f⟩ => borrow6 ⟨a, b, c, d, true, f⟩

def borrow4 : Hexagram → Hexagram
  | ⟨a, b, c, true, e, f⟩ => ⟨a, b, c, false, e, f⟩
  | ⟨a, b, c, false, e, f⟩ => borrow5 ⟨a, b, c, true, e, f⟩

def borrow3 : Hexagram → Hexagram
  | ⟨a, b, true, d, e, f⟩ => ⟨a, b, false, d, e, f⟩
  | ⟨a, b, false, d, e, f⟩ => borrow4 ⟨a, b, true, d, e, f⟩

def borrow2 : Hexagram → Hexagram
  | ⟨a, true, c, d, e, f⟩ => ⟨a, false, c, d, e, f⟩
  | ⟨a, false, c, d, e, f⟩ => borrow3 ⟨a, true, c, d, e, f⟩

def borrow1 : Hexagram → Hexagram
  | ⟨true, b, c, d, e, f⟩ => ⟨false, b, c, d, e, f⟩
  | ⟨false, b, c, d, e, f⟩ => borrow2 ⟨true, b, c, d, e, f⟩

/-- The counter run backward: taking one. -/
def subOne : Hexagram → Hexagram := borrow1

theorem subOne_addOne (s : Hexagram) : subOne (addOne s) = s := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **The counter merges nothing.** -/
theorem addOne_lossless : Law.Lossless addOne :=
  Law.lossless_iff.mpr fun x y same => (subOne_addOne x).symm.trans ((congrArg subOne same).trans (subOne_addOne y))

/-- From 坤, the counter comes to each configuration at the step of its binary value. -/
theorem from_allBroken (s : Hexagram) : Law.orbit addOne allBroken (binaryValue s) = s := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- And from each configuration it comes to 坤 at the step that completes sixty-four. -/
theorem to_allBroken (s : Hexagram) : Law.orbit addOne s (64 - binaryValue s) = allBroken := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **Every configuration can be had from every other.** -/
theorem addOne_reach (s t : Hexagram) : Reach (Law.process addOne) s t :=
  Reach.trans (Branching.law_reach_iff.mpr ⟨_, to_allBroken s⟩)
    (Branching.law_reach_iff.mpr ⟨_, from_allBroken t⟩)

/-- **Sixty-four steps on, every configuration is had again.** -/
theorem addOne_sixtyfour (s : Hexagram) : Law.orbit addOne s 64 = s := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- Whether a law brings `x` to `s` within `n` steps, told step by step. -/
def backWithin (next : Hexagram → Hexagram) (s : Hexagram) : Nat → Hexagram → Bool
  | 0, _ => false
  | n + 1, x => eqb (next x) s || backWithin next s n (next x)

theorem not_back {next : Hexagram → Hexagram} {s : Hexagram} :
    ∀ {n : Nat} {x : Hexagram}, backWithin next s n x = false →
      ∀ p, 0 < p → p ≤ n → Law.orbit next x p ≠ s
  | 0, _, _, _, pos, le => absurd (Nat.lt_of_lt_of_le pos le) (Nat.lt_irrefl 0)
  | _ + 1, _, _, 0, pos, _ => absurd pos (Nat.lt_irrefl 0)
  | _ + 1, _, h, 1, _, _ => ne_of_eqb (neither h).1
  | _ + 1, x, h, q + 2, _, le => fun same =>
    not_back (neither h).2 (q + 1) (Nat.succ_pos q) (Nat.le_of_succ_le_succ le)
      ((Law.orbit_shift next x (q + 1)).symm.trans same)

/-- What the step-by-step test finds: along the run from `s`, no step from the first to the
`n`-th is at `s`. -/
theorem first_return_of {next : Hexagram → Hexagram} {s : Hexagram} {n : Nat}
    (h : backWithin next s n s = false) : ∀ p, 0 < p → p < n + 1 → (Law.run next s).state p ≠ s :=
  fun p pos lt => not_back h p pos (Nat.le_of_lt_succ lt)

theorem backWithin_addOne (s : Hexagram) : backWithin addOne s 63 s = false := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **No configuration comes back before the sixty-fourth step.** -/
theorem addOne_first_return (s : Hexagram) (p : Nat) (pos : 0 < p) (lt : p < 64) :
    Law.orbit addOne s p ≠ s :=
  not_back (backWithin_addOne s) p pos (Nat.le_of_lt_succ lt)

/-- **One orbit of sixty-four**: the counter merges nothing, every configuration can be had from
every other, and along every run each configuration first comes back at the sixty-fourth step. -/
theorem addOne_one_orbit :
    Branching.Lossless (Law.process addOne) ∧ (∀ s t, Reach (Law.process addOne) s t) ∧
      ∀ s, (Law.run addOne s).state 64 = s ∧
        ∀ p, 0 < p → p < 64 → (Law.run addOne s).state p ≠ s :=
  ⟨Branching.law_lossless_iff.mpr addOne_lossless, addOne_reach,
   fun s => ⟨(congrArg (fun f => f 64) (Law.run_state addOne s)).trans (addOne_sixtyfour s),
     fun p pos lt same => addOne_first_return s p pos lt
       ((congrArg (fun f => f p) (Law.run_state addOne s)).symm.trans same)⟩⟩

/-- The place's exponent: line `k` is worth `2 ^ (k - 1)`. -/
def exponent : Place → Nat
  | .p1 => 0
  | .p2 => 1
  | .p3 => 2
  | .p4 => 3
  | .p5 => 4
  | .p6 => 5

/-- The steps after which the line at a place has turned. -/
def period : Place → Nat
  | .p1 => 1
  | .p2 => 2
  | .p3 => 4
  | .p4 => 8
  | .p5 => 16
  | .p6 => 32

theorem period_pow : ∀ k : Place, period k = 2 ^ exponent k
  | .p1 => rfl
  | .p2 => rfl
  | .p3 => rfl
  | .p4 => rfl
  | .p5 => rfl
  | .p6 => rfl

/-- The lines below a place, from the bottom. -/
def linesBelow : Place → Hexagram → List Bool
  | .p1, _ => []
  | .p2, s => [s.l1]
  | .p3, s => [s.l1, s.l2]
  | .p4, s => [s.l1, s.l2, s.l3]
  | .p5, s => [s.l1, s.l2, s.l3, s.l4]
  | .p6, s => [s.l1, s.l2, s.l3, s.l4, s.l5]

/-- **`2 ^ (k - 1)` steps of the counter add one at line `k`.** -/
theorem orbit_period (k : Place) (s : Hexagram) : Law.orbit addOne s (period k) = carryAt k s := by
  cases k <;>
    cases s with
    | mk a b c d e f =>
      cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

theorem carryAt_turns (k : Place) (s : Hexagram) : (carryAt k s).line k = !s.line k := by
  cases k <;>
    cases s with
    | mk a b c d e f =>
      cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

theorem carryAt_below (k : Place) (s : Hexagram) : linesBelow k (carryAt k s) = linesBelow k s := by
  cases k <;>
    cases s with
    | mk a b c d e f =>
      cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **Line `k` turns every `2 ^ (k - 1)` steps**: along every run of the counter,
`2 ^ exponent k` steps on, the line at `k` is turned and the lines below it are as they were. -/
theorem line_turns (k : Place) (s : Hexagram) (n : Nat) :
    ((Law.run addOne s).state (n + 2 ^ exponent k)).line k =
        !((Law.run addOne s).state n).line k ∧
      linesBelow k ((Law.run addOne s).state (n + 2 ^ exponent k)) =
        linesBelow k ((Law.run addOne s).state n) :=
  have at_k : (Law.run addOne s).state (n + 2 ^ exponent k) =
      carryAt k ((Law.run addOne s).state n) :=
    (congrArg (fun p => Law.orbit addOne s (n + p)) (period_pow k).symm).trans
      ((Law.orbit_add addOne s n (period k)).trans (orbit_period k _))
  ⟨(congrArg (fun x => x.line k) at_k).trans (carryAt_turns k _),
   (congrArg (linesBelow k) at_k).trans (carryAt_below k _)⟩

/-! ## The six orbits of the law of waxing and waning -/

/-- The changes of line going once round: across the five seams, a rise (承) or a fall (乘), and
from the top line round to the bottom, where it enters as its opposite, a change exactly where the
two agree. -/
def changesAround (s : Hexagram) : Nat := riseCount s + fallCount s + (same s.l1 s.l6).toNat

/-- **The law of waxing and waning keeps the changes around.** -/
theorem changesAround_waxWane (s : Hexagram) : changesAround (waxWane s) = changesAround s := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **Along every run they are those of the start.** -/
theorem changesAround_run (s : Hexagram) :
    ∀ n, changesAround ((Law.run waxWane s).state n) = changesAround s
  | 0 => rfl
  | n + 1 => (changesAround_waxWane _).trans (changesAround_run s n)

/-- **Every step of the law, read as a process, keeps them.** -/
theorem changesAround_invariant (v : Nat) :
    Invariant (Law.process waxWane) (fun x => changesAround x = v) :=
  fun s _ _ step held => (congrArg changesAround step).trans ((changesAround_waxWane s).trans held)

/-- **Along every run the changes around are one, three or five.** -/
theorem changesAround_values (s : Hexagram) (n : Nat) :
    changesAround ((Law.run waxWane s).state n) = 1 ∨
      changesAround ((Law.run waxWane s).state n) = 3 ∨
      changesAround ((Law.run waxWane s).state n) = 5 := by
  generalize (Law.run waxWane s).state n = x
  cases x with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
      first
      | exact .inl rfl
      | exact .inr (.inl rfl)
      | exact .inr (.inr rfl)

/-- **One on twelve configurations, three on forty, five on twelve**, counted over the received
order. -/
theorem changesAround_counts :
    (order.filter fun s => Nat.beq (changesAround s) 1).length = 12 ∧
    (order.filter fun s => Nat.beq (changesAround s) 3).length = 40 ∧
    (order.filter fun s => Nat.beq (changesAround s) 5).length = 12 :=
  ⟨rfl, rfl, rfl⟩

/-- **So the law does not reach 既濟 from 乾**: one change around against five. -/
theorem qian_not_reach_jiJi : ¬ Reach (Law.process waxWane) allUnbroken jiJi :=
  fun reach => absurd ((changesAround_invariant 1).reach reach rfl) (by decide)

/-- **Losing nothing, the law still does not reach every configuration from every other**, as the
counter adding one does (`addOne_reach`). -/
theorem waxWane_not_reach_every : ¬ ∀ s t, Reach (Law.process waxWane) s t :=
  fun every => qian_not_reach_jiJi (every _ _)

/-- 屯 (3). -/
def zhun : Hexagram := number 3

/-- 蒙 (4). -/
def meng : Hexagram := number 4

/-- The six orbits of the law of waxing and waning, each by a configuration on it and the number
of configurations on it: 乾, 屯, 蒙, 需 and 既濟 twelve, 隨 four. -/
def orbitStarts : List (Hexagram × Nat) :=
  [(allUnbroken, 12), (zhun, 12), (meng, 12), (xu, 12), (sui, 4), (jiJi, 12)]

/-- Some step before `n` of the law from `x` is at `s`, told step by step. -/
def visitsFrom (next : Hexagram → Hexagram) (s : Hexagram) : Nat → Hexagram → Bool
  | 0, _ => false
  | n + 1, x => eqb x s || visitsFrom next s n (next x)

theorem visits_sound {next : Hexagram → Hexagram} {s : Hexagram} :
    ∀ {n : Nat} {x : Hexagram}, visitsFrom next s n x = true → ∃ k, k < n ∧ Law.orbit next x k = s
  | 0, _, h => Bool.noConfusion h
  | _ + 1, x, h => match ListTests.or_cases h with
    | .inl here => ⟨0, Nat.succ_pos _, eq_of_eqb here⟩
    | .inr later => match visits_sound later with
      | ⟨k, lt, at_k⟩ => ⟨k + 1, Nat.succ_lt_succ lt, (Law.orbit_shift next x k).trans at_k⟩

/-- `s` is on the orbit of some listed start, told step by step. -/
def onOrbit (s : Hexagram) : List (Hexagram × Nat) → Bool
  | [] => false
  | q :: l => visitsFrom waxWane s q.2 q.1 || onOrbit s l

theorem onOrbit_sound {s : Hexagram} : ∀ {l : List (Hexagram × Nat)}, onOrbit s l = true →
    ∃ q, q ∈ l ∧ ∃ k, k < q.2 ∧ Law.orbit waxWane q.1 k = s
  | [], h => Bool.noConfusion h
  | q :: _, h => match ListTests.or_cases h with
    | .inl here => match visits_sound here with
      | ⟨k, lt, at_k⟩ => ⟨q, .head _, k, lt, at_k⟩
    | .inr there => match onOrbit_sound there with
      | ⟨q', mem, rest⟩ => ⟨q', .tail _ mem, rest⟩

theorem onOrbit_all (s : Hexagram) : onOrbit s orbitStarts = true := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **Every configuration is on one of the six orbits**: along the run from some listed start, it
is had before that start's number of steps. -/
theorem on_an_orbit (s : Hexagram) :
    ∃ q, q ∈ orbitStarts ∧ ∃ k, k < q.2 ∧ (Law.run waxWane q.1).state k = s :=
  onOrbit_sound (onOrbit_all s)

/-- **Each start first comes back at its number of steps**: five at the twelfth step, 隨 at the
fourth. -/
theorem starts_return : ∀ q, q ∈ orbitStarts →
    (Law.run waxWane q.1).state q.2 = q.1 ∧
      ∀ p, 0 < p → p < q.2 → (Law.run waxWane q.1).state p ≠ q.1
  | _, .head _ => ⟨rfl,
      first_return_of (next := waxWane) (s := allUnbroken) (n := 11) rfl⟩
  | _, .tail _ (.head _) => ⟨rfl,
      first_return_of (next := waxWane) (s := zhun) (n := 11) rfl⟩
  | _, .tail _ (.tail _ (.head _)) => ⟨rfl,
      first_return_of (next := waxWane) (s := meng) (n := 11) rfl⟩
  | _, .tail _ (.tail _ (.tail _ (.head _))) => ⟨rfl,
      first_return_of (next := waxWane) (s := xu) (n := 11) rfl⟩
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.head _)))) => ⟨rfl,
      first_return_of (next := waxWane) (s := sui) (n := 3) rfl⟩
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))) => ⟨rfl,
      first_return_of (next := waxWane) (s := jiJi) (n := 11) rfl⟩
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ mem))))) => nomatch mem

/-- The place in a list of the first start whose orbit holds `s`. -/
def indexIn (s : Hexagram) : List (Hexagram × Nat) → Nat
  | [] => 0
  | q :: l => match visitsFrom waxWane s q.2 q.1 with
    | true => 0
    | false => indexIn s l + 1

/-- The orbit a configuration is on, numbered by its start in `orbitStarts`. -/
def orbitIndex (s : Hexagram) : Nat := indexIn s orbitStarts

/-- **The law of waxing and waning keeps the orbit.** -/
theorem orbitIndex_waxWane (s : Hexagram) : orbitIndex (waxWane s) = orbitIndex s := by
  cases s with
  | mk a b c d e f =>
    cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;> rfl

/-- **The orbit is a lumping the law goes alike across.** -/
theorem orbitIndex_lumped : Learning.Lumped orbitIndex (fun s => orbitIndex (waxWane s)) :=
  fun s t same => (orbitIndex_waxWane s).trans (same.trans (orbitIndex_waxWane t).symm)

/-- The same, by `Learning.goAlike_iff_lumped`. -/
theorem orbitIndex_goAlike : GoAlike (Law.process waxWane) orbitIndex :=
  Learning.goAlike_iff_lumped.mpr orbitIndex_lumped

theorem orbitIndex_invariant (i : Nat) :
    Invariant (Law.process waxWane) (fun x => orbitIndex x = i) :=
  fun s _ _ step held => (congrArg orbitIndex step).trans ((orbitIndex_waxWane s).trans held)

/-- **What the law reaches is on the same orbit.** -/
theorem reach_keeps_orbit {s t : Hexagram} (reach : Reach (Law.process waxWane) s t) :
    orbitIndex t = orbitIndex s :=
  (orbitIndex_invariant (orbitIndex s)).reach reach rfl

/-- **The six orbits**: the starts are on six different orbits, so none reaches another; the
orbits hold twelve, twelve, twelve, twelve, four and twelve configurations, counted over the
received order; their changes around are one, three, three, three, three and five. -/
theorem orbit_census :
    orbitStarts.map (fun q => orbitIndex q.1) = [0, 1, 2, 3, 4, 5] ∧
    orbitStarts.map (fun q =>
      (order.filter fun s => Nat.beq (orbitIndex s) (orbitIndex q.1)).length) =
        [12, 12, 12, 12, 4, 12] ∧
    orbitStarts.map (fun q => changesAround q.1) = [1, 3, 3, 3, 3, 5] :=
  ⟨rfl, rfl, rfl⟩

end Hexagram

end Becoming
