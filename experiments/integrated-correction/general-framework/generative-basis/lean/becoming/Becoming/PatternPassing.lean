import Becoming.Wholes

/-!
# PatternPassing: a pattern that outlasts each of its carriers lasts only through passing

`Becoming.Wholes` proves that parts covering the steps from `T` on, none active at two steps `d`
apart, have a part arising within every `d` consecutive steps (`Web.Covered.arises_within`), and
that the bound `d` is attained (`Shifts.shifts`). This module reads a web's activity as carrying a
pattern and asks what a pattern lasting longer than each of its carriers needs, with no premise
beyond the hypotheses each statement names.

A pattern carried in a web `W` by `carries : Nat → F → Prop` is read through the web whose
activity is carrying while active (`Web.carrying`); where every carrier is active, its activity is
exactly carrying (`Web.carrying_iff`). Every law below is stated for any web `V`, its activity read
as carrying, so it holds of `W.carrying carries` for every pattern carried in every web. The
pattern is *present* at a step where some formation carries it (`Web.Present`). `passes t b a`
reads "across the step from `t`, `b` gives the pattern to `a`"; some carrier *passes it across the
step* where a formation carrying it at `t` gives it to a formation carrying it at `t + 1`
(`Web.PassesAt`). The *passing premise* (`Web.ByPassing`): a formation carrying the pattern at
`t + 1` carried it at `t` or was given it across the step from `t` by a formation carrying it at
`t`. Like transmission in `Becoming.Evolution` (`Flow.TransmitsWithin`), which
`Becoming.Transmission` shows independent of the core's other premises wherever it binds, the
passing premise is a reading of how carrying forms, supplied and not derived.

* **A lasting pattern of brief carriers needs carriers that begin.** Present at every step from
  `T` on, its carriers brief for `d` (none carries at two steps `d` apart, `Web.Brief`), some
  carrier begins within every `d` consecutive steps (`Web.begins_within`, an instance of
  `Web.Covered.arises_within` on the formations of the web as its parts; `PatternRelay.shifts`
  attains the bound). As there, "within" is the irrefutable form: no stretch of `d` steps is
  without a beginning.
* **Under the passing premise every beginning is a passing** (`Web.ByPassing.begins_passed`), and
  tracing a carrier back over `k` steps, it carried at the start or some carrier passed the pattern
  across one of those steps (`Web.ByPassing.trace`).
* **Under the passing premise the pattern lasts only through passing.** Present at every step from
  `T` on, its carriers brief for `d`, some carrier passes it across one of every `d` consecutive
  steps from `T` on (`Web.ByPassing.passes_within`). This one is positive: the step and both
  carriers are given. A carrier passes it within every two steps but not within every one in
  `PatternRelay.shifted` (`PatternRelay.shifts`), so the bound `d` is attained.
* **One empty step ends it.** Under the passing premise presence at a step gives presence at every
  earlier step (`Web.ByPassing.present_back`, `Web.ByPassing.present_of_le`), so a step at which
  no formation carries the pattern is followed by none at which any does
  (`Web.ByPassing.empty_stays`).
* **If passing stops, it ends within one span.** Under the passing premise, its carriers brief for
  `d`, and no carrier passing it across any step from `T` on, no formation carries it at any step
  from `T + d` on (`Web.ByPassing.ends_within`).
* **Witnesses.** In `PatternRelay` each carrier carries for two steps and gives the pattern to
  the next carrier across every step: every premise holds, the pattern is present at every step,
  and every carrier's carrying ends (`PatternRelay.relay`). With passing stopped from step `T` on,
  the pattern is present at every step up to `T + 1` and at none from `T + 2` on
  (`PatternRelay.stopped_relay`), so the bound `T + d` of `Web.ByPassing.ends_within` is attained
  at `d = 2`.

Passing carries whatever pattern it carries: nothing here says which patterns are worth passing,
or what carrying one does to the carriers or to anything else. What is not derived: whether
carrying forms by passing (`Web.ByPassing` is a hypothesis), which formations pass, when, or to
which formations, and whether a pattern changes as it is passed.
-/

namespace Becoming

variable {F C : Type}

namespace Web

/-! ## A pattern carried in a web -/

/-- The web read through a pattern: a formation is active where it carries the pattern and is
active in `W`. -/
def carrying (W : Web F C) (carries : Nat → F → Prop) : Web F C where
  level := W.level
  active t a := carries t a ∧ W.active t a
  requires := W.requires
  need := W.need
  draws := W.draws

/-- **Carrying is activity.** A formation active in the web read through a pattern is active in
the web. -/
theorem carrying_active (W : Web F C) (carries : Nat → F → Prop) {t : Nat} {a : F}
    (active : (W.carrying carries).active t a) : W.active t a :=
  active.2

/-- **Where every carrier is active, the web read through a pattern is active exactly where the
pattern is carried.** -/
theorem carrying_iff (W : Web F C) {carries : Nat → F → Prop}
    (carried : ∀ t a, carries t a → W.active t a) (t : Nat) (a : F) :
    (W.carrying carries).active t a ↔ carries t a :=
  ⟨And.left, fun carrying => ⟨carrying, carried t a carrying⟩⟩

variable (V : Web F C)

/-- The pattern is present at step `t`: some formation carries it. -/
def Present (t : Nat) : Prop :=
  ∃ a, V.active t a

/-- Some carrier passes the pattern across the step from `t`: a formation carrying it at `t`
gives it to a formation carrying it at `t + 1`. -/
def PassesAt (passes : Nat → F → F → Prop) (t : Nat) : Prop :=
  ∃ b a, V.active t b ∧ passes t b a ∧ V.active (t + 1) a

/-- The passing premise: a formation carrying the pattern at `t + 1` carried it at `t`, or was
given it across the step from `t` by a formation carrying it at `t`. -/
def ByPassing (passes : Nat → F → F → Prop) : Prop :=
  ∀ t a, V.active (t + 1) a → V.active t a ∨ ∃ b, V.active t b ∧ passes t b a

variable {V} {passes : Nat → F → F → Prop}

/-! ## A lasting pattern of brief carriers -/

/-- **A lasting pattern of brief carriers needs carriers that begin.** A pattern present at every
step from `T` on, no carrier carrying it at two steps `d` apart, has no `d` consecutive steps from
`T` on across which no carrier begins. An instance of `Web.Covered.arises_within`, every formation
of the web a part. -/
theorem begins_within {d T : Nat} (present : ∀ t, T ≤ t → V.Present t)
    (brief : ∀ a, V.Brief d a) {S : Nat} (after : T ≤ S) :
    ¬ ∀ j, j < d → ∀ a, ¬ V.Arises (S + j) a :=
  fun quiet => Covered.arises_within (parts := fun _ => True)
    (fun t later => match present t later with
      | ⟨a, active⟩ => ⟨a, trivial, active⟩)
    (fun a _ => brief a) after fun j below a _ => quiet j below a

/-! ## Under the passing premise -/

/-- **Under the passing premise every beginning is a passing.** A formation that begins to carry
the pattern across a step was given it there by a formation carrying it. -/
theorem ByPassing.begins_passed (by_passing : V.ByPassing passes) {t : Nat} {a : F}
    (begins : V.Arises t a) : ∃ b, V.active t b ∧ passes t b a :=
  match by_passing t a begins.2 with
  | .inl before => absurd before begins.1
  | .inr given => given

/-- **Tracing a carrier back.** Under the passing premise, a formation carrying the pattern `k`
steps after `S` carried it at `S`, or some carrier passed it across one of the `k` steps from
`S`. -/
theorem ByPassing.trace (by_passing : V.ByPassing passes) {S : Nat} :
    ∀ {k : Nat} {a : F}, V.active (S + k) a →
      V.active S a ∨ ∃ j, j < k ∧ V.PassesAt passes (S + j)
  | 0, _, active => .inl active
  | k + 1, a, active => match by_passing (S + k) a active with
    | .inl before => match trace by_passing before with
      | .inl start => .inl start
      | .inr ⟨j, below, passing⟩ => .inr ⟨j, Nat.lt_succ_of_lt below, passing⟩
    | .inr ⟨b, carrier, given⟩ => .inr ⟨k, Nat.lt_succ_self k, b, a, carrier, given, active⟩

/-- **Under the passing premise, the pattern lasts only through passing.** A pattern present at
every step from `T` on, no carrier carrying it at two steps `d` apart, is passed by some carrier
across one of every `d` consecutive steps from `T` on. -/
theorem ByPassing.passes_within (by_passing : V.ByPassing passes) {d T : Nat}
    (present : ∀ t, T ≤ t → V.Present t) (brief : ∀ a, V.Brief d a) {S : Nat}
    (after : T ≤ S) : ∃ j, j < d ∧ V.PassesAt passes (S + j) :=
  match present (S + d) (Nat.le_trans after (Nat.le_add_right S d)) with
  | ⟨a, active⟩ => match by_passing.trace active with
    | .inl start => absurd active (brief a S start)
    | .inr found => found

/-- **Presence goes back one step.** Under the passing premise, a pattern present at `t + 1` was
present at `t`. -/
theorem ByPassing.present_back (by_passing : V.ByPassing passes) {t : Nat}
    (present : V.Present (t + 1)) : V.Present t :=
  match present with
  | ⟨a, active⟩ => match by_passing t a active with
    | .inl before => ⟨a, before⟩
    | .inr ⟨b, carrier, _⟩ => ⟨b, carrier⟩

/-- Presence goes back any number of steps. -/
theorem ByPassing.present_earlier (by_passing : V.ByPassing passes) {t : Nat} :
    ∀ {k : Nat}, V.Present (t + k) → V.Present t
  | 0, present => present
  | _ + 1, present => present_earlier by_passing (by_passing.present_back present)

/-- **Under the passing premise, presence at a step gives presence at every earlier step.** -/
theorem ByPassing.present_of_le (by_passing : V.ByPassing passes) {t t' : Nat} (le : t ≤ t')
    (present : V.Present t') : V.Present t :=
  match le_dest le with
  | ⟨_, same⟩ =>
    by_passing.present_earlier (Eq.subst (motive := fun s => V.Present s) same present)

/-- **One empty step ends the pattern.** Under the passing premise, a step at which no formation
carries the pattern is followed by no step at which any does. -/
theorem ByPassing.empty_stays (by_passing : V.ByPassing passes) {t : Nat}
    (empty : ¬ V.Present t) {t' : Nat} (later : t ≤ t') : ¬ V.Present t' :=
  fun present => empty (by_passing.present_of_le later present)

/-- **If passing stops, the pattern ends within one span.** Under the passing premise, no carrier
carrying it at two steps `d` apart, and no carrier passing it across any step from `T` on, no
formation carries it at any step from `T + d` on. -/
theorem ByPassing.ends_within (by_passing : V.ByPassing passes) {d T : Nat}
    (brief : ∀ a, V.Brief d a) (stopped : ∀ t, T ≤ t → ¬ V.PassesAt passes t) {t : Nat}
    (later : T + d ≤ t) : ¬ V.Present t :=
  fun ⟨a, active⟩ => match le_dest later with
  | ⟨m, same⟩ =>
    have carried : V.active (T + m + d) a :=
      Eq.subst (motive := fun s => V.active s a) (same.trans (Nat.add_right_comm T d m)) active
    match by_passing.trace carried with
    | .inl start => brief a (T + m) start carried
    | .inr ⟨j, _, passing⟩ =>
      stopped (T + m + j) (Nat.le_trans (Nat.le_add_right T m) (Nat.le_add_right (T + m) j))
        passing

end Web

/-! ## Witnesses -/

namespace PatternRelay

/-- The `n`th carrier carries the pattern at steps `n` and `n + 1`. -/
def web : Web Nat Unit where
  level _ _ := 0
  active t n := t = n ∨ t = n + 1
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Across the step from `t`, the carrier `t` gives the pattern to the carrier `t + 1`. -/
def passes (t b a : Nat) : Prop :=
  b = t ∧ a = t + 1

/-- Every carrier carries for two steps, as a member of `Generations` is active. -/
theorem brief (n : Nat) : web.Brief 2 n :=
  Generations.brief (.member n) trivial

/-- **A relay of carriers each carrying for two steps, each giving the pattern to the next.** The
passing premise holds, no carrier carries at two steps two apart, every carrier's carrying ends,
the pattern is present at every step, and some carrier passes it across every step. -/
theorem relay : web.ByPassing passes ∧ (∀ n, web.Brief 2 n) ∧ (∀ n, web.Ends n) ∧
    (∀ t, web.Present t) ∧ ∀ t, web.PassesAt passes t :=
  ⟨fun t _ active => match active with
    | .inl begins => .inr ⟨t, .inl rfl, rfl, begins.symm⟩
    | .inr goes_on => .inl (.inl (Nat.succ.inj goes_on)),
   brief,
   fun n => Generations.ends (.member n) trivial,
   fun t => ⟨t, .inl rfl⟩,
   fun t => ⟨t, t + 1, .inl rfl, ⟨rfl, rfl⟩, .inl rfl⟩⟩

/-- The relay stopped at step `T`: the carriers up to `T`, each carrying at steps `n` and
`n + 1`. -/
def stopped (T : Nat) : Web Nat Unit where
  level _ _ := 0
  active t n := n ≤ T ∧ (t = n ∨ t = n + 1)
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Across each step before `T`, the carrier `t` gives the pattern to the carrier `t + 1`;
nothing is given from step `T` on. -/
def passesUntil (T t b a : Nat) : Prop :=
  t < T ∧ b = t ∧ a = t + 1

/-- The stopped relay meets the passing premise. -/
theorem stopped_by_passing (T : Nat) : (stopped T).ByPassing (passesUntil T) :=
  fun t _ ⟨within, active⟩ => match active with
  | .inl begins =>
    have before : t < T := Eq.subst (motive := (· ≤ T)) begins.symm within
    .inr ⟨t, ⟨Nat.le_of_lt before, .inl rfl⟩, before, rfl, begins.symm⟩
  | .inr goes_on => .inl ⟨within, .inl (Nat.succ.inj goes_on)⟩

/-- Every carrier of the stopped relay carries for two steps. -/
theorem stopped_brief (T n : Nat) : (stopped T).Brief 2 n :=
  fun t now later => brief n t now.2 later.2

/-- No carrier of the stopped relay passes the pattern across any step from `T` on. -/
theorem stopped_quiet (T : Nat) : ∀ t, T ≤ t → ¬ (stopped T).PassesAt (passesUntil T) t :=
  fun _ after ⟨_, _, _, ⟨before, _⟩, _⟩ => Nat.lt_irrefl T (Nat.lt_of_le_of_lt after before)

/-- **With passing stopped from step `T` on, the pattern ends exactly one span later.** The relay
stopped at `T` meets every premise of `Web.ByPassing.ends_within` with `d = 2`; the pattern is
present at every step up to `T + 1` and at none from `T + 2` on. So the bound `T + d` is
attained. -/
theorem stopped_relay (T : Nat) : (stopped T).ByPassing (passesUntil T) ∧
    (∀ n, (stopped T).Brief 2 n) ∧
    (∀ t, T ≤ t → ¬ (stopped T).PassesAt (passesUntil T) t) ∧
    (∀ t, t ≤ T + 1 → (stopped T).Present t) ∧
    ∀ t, T + 2 ≤ t → ¬ (stopped T).Present t :=
  ⟨stopped_by_passing T, stopped_brief T, stopped_quiet T,
   fun _ within => (stopped_by_passing T).present_of_le within ⟨T, Nat.le_refl T, .inr rfl⟩,
   fun _ later => (stopped_by_passing T).ends_within (stopped_brief T) (stopped_quiet T) later⟩

/-- Half of the step after an odd one is one more than half of it. -/
theorem half_odd : ∀ t, odd t = true → Shifts.half (t + 1) = Shifts.half t + 1
  | 0, odd' => (nomatch odd')
  | 1, _ => rfl
  | t + 2, odd' => congrArg (· + 1) (half_odd t ((Shifts.odd_two t).symm.trans odd'))

/-- Carriers in shifts: the `n`th carries the pattern at steps `2n` and `2n + 1`. -/
def shifted : Web Nat Unit where
  level _ _ := 0
  active t n := Shifts.half t = n
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Across each odd step, the carrier of that shift gives the pattern to the next. -/
def passesOdd (t b a : Nat) : Prop :=
  odd t = true ∧ b = Shifts.half t ∧ a = b + 1

/-- **The bounds of `Web.begins_within` and `Web.ByPassing.passes_within` are attained.**
Carriers in shifts of two steps, each giving the pattern to the next across an odd step: the
passing premise holds, no carrier carries at two steps two apart, the pattern is present at every
step, no carrier passes it across an even step, and no carrier begins across an even step. So a
carrier begins, and the pattern is passed, across one of every two consecutive steps, not of every
one. -/
theorem shifts : shifted.ByPassing passesOdd ∧ (∀ n, shifted.Brief 2 n) ∧
    (∀ t, shifted.Present t) ∧ (∀ t, odd t = false → ¬ shifted.PassesAt passesOdd t) ∧
    ∀ t, odd t = false → ∀ n, ¬ shifted.Arises t n :=
  ⟨fun t _ active => match parity : odd t with
    | true => .inr ⟨Shifts.half t, rfl, parity, rfl, active.symm.trans (half_odd t parity)⟩
    | false => .inl ((Shifts.half_even t parity).symm.trans active),
   fun _ t now later => Nat.succ_ne_self (Shifts.half t) (later.trans now.symm),
   fun t => ⟨Shifts.half t, rfl⟩,
   ⟨fun _ even ⟨_, _, _, ⟨odd', _⟩, _⟩ => (nomatch even.symm.trans odd'),
   fun t even _ arises => arises.1 ((Shifts.half_even t even).symm.trans arises.2)⟩⟩

end PatternRelay

end Becoming
