import Becoming.Premises

/-!
# Openness: continued change needs exchange beyond what stands

`Becoming.Space` brings a finite, balanced, dissipative world whose arising is embodied to
rest, and in a finite world arising recurs exactly when ceasing does. This module states
what does the work. The world need not be finite: what brings it to rest is finitely many
standing at each step and enclosure around them from some step on, with a census of what
is active; for arising and ceasing to recur together, a bound on that census. In a world
that comes to rest so, only finitely many relata ever stand or are active
(`World.rest_few`): beyond finite worlds, the rest theorem adds relata that never stand
or act.
Under balance and dissipation, across a step whose exchange, together with whatever
stands before or after it, lies within finitely many conditions, the total standing does
not rise, and it falls whenever any condition's standing changes: a rise is given to, and
giving needs uptake there; a fall is taken from.

* **Total standing runs down.** Where what stands at each step is listed, each once
  (`Web.StandingCensus`), the total standing across a step enclosed around what stands
  (`Flow.AroundStanding`) does not rise (`Flow.standing_never_rises`), and any rise or
  fall of a condition's standing lowers it (`Flow.change_lowers`).
* **Standing comes to rest.** So where every step from some step on is enclosed around
  what stands, no condition's standing changes at arbitrarily late steps
  (`Flow.stills`).
* **Ceasing needs arising.** In a world with a census whose activity is decided, ceasing
  recurs only where arising recurs (`World.arising_of_ceasing`, from
  `Web.arising_of_ceasing`). Not conversely: `dawn` has a census and arises without end
  while nothing ceases; `dusk` keeps ceasing while nothing arises, so it has no census
  (`World.census_one_way`).
* **A bounded count keeps them together.** Where at most `B` relata are active at each
  step (`World.CountedWithin`), arising recurs exactly when ceasing does
  (`World.CountedWithin.arising_iff_ceasing`, from `Web.unceasing_iff_bounded`). Every
  census of a finite world is bounded, with no decidability
  (`World.Finite.census_bounded`), so where activity is decided the law of finite worlds
  is a case (`World.Finite.countedWithin`, `World.Finite.arising_iff_ceasing`); `procession`, with one
  relatum active at a time among infinitely many, keeps arising and ceasing
  (`World.procession_world`); `dawn` has no bound (`World.dawn_unbounded`). The bound may
  grow between: where at most `B t` relata are active at each step `t`
  (`World.CountedBy`) and `B` returns to at most `K` at arbitrarily late steps, the two
  still recur together (`World.CountedBy.arising_iff_ceasing`). A bound growing without
  end does not keep them together, however slowly it grows: in `slow B`, for any
  non-decreasing, unbounded `B`, the relata below `B t` are active at step `t`, arising
  recurs and nothing ceases (`World.slow_world`). So a non-decreasing bound keeps arising
  and ceasing together in every world it counts where it stays within some number, and
  not where it grows without end; there ceasing recurs exactly where the count falls
  short of what was there with what arose since (`Listed.ceasing_iff_shortfall`), as
  where arising outpaces the bound (`Listed.ceasing_of_outpacing`). Read of
  standing, the same law holds under a census of what stands: what stands at the end
  with what ceased to stand is what stood at the start with what came to stand
  (`Web.StandingCensus.over_stretch`), ceasing to stand recurring needs coming to stand
  recurring, and with a bound from some step on the two recur together
  (`Web.StandingCensus.coming_of_ceasing`, `Web.StandingCensus.coming_iff_ceasing`).
* **The rest theorem.** Where what stands is listed, whatever arises is embodied, the
  flow balances and dissipates, and every step from some step on is enclosed around what
  stands, arising stops, since standing stops changing (`World.arising_stops`). With a
  census of what is active as well, ceasing stops too, by the census law: the world comes
  to rest (`World.comes_to_rest`).
* **Each census does work.** Without the census of what is active, ceasing can go on:
  `dusk` meets every other premise and keeps ceasing (`World.rest_needs_census`). Without
  the census of what stands, arising can go on: in `kindling` what is active is listed,
  whatever arises is embodied, the flow balances and dissipates and every step is
  enclosed around every relatum ever active, yet every unburnt fuel stands; in `ember`,
  the same flow with every relatum embodied, every step is enclosed and nothing is listed
  (`World.rest_needs_standing`).
* **Its cases.** A finite world lists what stands and is enclosed around it at every step
  (`World.Finite.standing`), so the finite rest of `Becoming.Space` is a case
  (`World.Finite.comes_to_rest`). Where every relatum is embodied, the census of what is
  active lists what stands (`World.rests_around`), and enclosure from some step on
  suffices, with no decision of equality: an enclosed step is not not enclosed around
  what stands, and the totals compared are numbers (`World.rests_enclosed`). Read the
  other way, arising without end in such a world is incompatible with every step from
  some step on being enclosed: it exchanges beyond every finite family
  (`World.arising_opens`).
* **What comes to rest is few.** Where what holds is listed at each step and coming to be
  does not recur, not unboundedly many members ever hold (`Listed.few_of_quiet`). So in
  every world that comes to rest under the rest theorem, only finitely many relata are
  ever active and only finitely many ever stand (`World.rest_few`); conversely, where
  finitely many are ever active and activity is decided, a census exists
  (`World.counted_of_ever`). Beyond finite worlds the rest theorem reaches only relata
  that never stand or act, as the idle ground of `hatch` (`World.hatch_idle`).
* **The premises decide neither enclosure nor openness.** The sides of `Handing`, also
  taking a unit from each of infinitely many ground relata and giving it back at every
  step, meet all eight premises of `Becoming.Premises` and arise without end. No step is
  enclosed, so dissipation, which binds only at enclosed steps, binds at none
  (`World.exposed_world`); nothing depends on anything, so activity needing support and
  bounded transmission hold vacuously too. Their openness is exchange at zero net: the
  total standing stays at one, and the ground relata stand at nothing
  (`World.exposed_standing`). Nor does openness with the eight give arising without
  end: a holder taking a unit from each ground relatum and giving it back at every step
  meets the eight with no step enclosed, and nothing arises or ceases
  (`World.holding_world`). Mutualists meet the eight with every step enclosed and come
  to rest (`World.openness_contingent`). So does `hatch`, in which every premise binds:
  after the child arises and the parent ceases, every step is enclosed and nothing
  changes, though the world is not finite (`World.hatch_rests`).

What stands and what is active coincide only for embodied relata. The standing laws need
no embodiment; the rest theorem uses it only for what arises, turning arising into
rising, and reaches ceasing through the census law. Activity is supposed decidable where
a theorem needs it, a logical commitment of the representation. No ethical predicate,
ranking or axiom occurs.
-/

namespace Becoming

variable {α : Type} {F C : Type}

/-! ## Lists -/

theorem mem_append_left {a : α} {l : List α} (m : List α) : a ∈ l → a ∈ l ++ m
  | .head _ => .head _
  | .tail _ mem => .tail _ (mem_append_left m mem)

theorem mem_append_right {a : α} : ∀ (l : List α) {m : List α}, a ∈ m → a ∈ l ++ m
  | [], _, mem => mem
  | _ :: l, _, mem => .tail _ (mem_append_right l mem)

/-! ## Total standing -/

/-- What stands at each step is listed, each once: finitely many conditions stand at each
step. -/
def Web.StandingCensus (W : Web F C) (stand : Nat → List C) : Prop :=
  Listed (fun c t => 0 < W.level t c) stand

/-- The census law read of standing: under a census of what stands, conditions ceasing to
stand at arbitrarily late steps need conditions coming to stand at arbitrarily late
steps (`Listed.coming_of_ceasing`). -/
theorem Web.StandingCensus.coming_of_ceasing {W : Web F C} {stand : Nat → List C}
    (census : W.StandingCensus stand) (ceasing : ∀ N, ∃ t c, N ≤ t ∧ W.CeasesToStand t c) :
    ∀ N, ∃ t c, N ≤ t ∧ W.ComesToStand t c :=
  Listed.coming_of_ceasing census ceasing

/-- With at most `B` conditions standing at each step from some step on, coming to stand
recurs exactly when ceasing to stand does (`Listed.coming_iff_ceasing`). -/
theorem Web.StandingCensus.coming_iff_ceasing {W : Web F C} {stand : Nat → List C}
    (census : W.StandingCensus stand) {T B : Nat}
    (bounded : ∀ t, T ≤ t → (stand t).length ≤ B) :
    (∀ N, ∃ t c, N ≤ t ∧ W.ComesToStand t c) ↔ ∀ N, ∃ t c, N ≤ t ∧ W.CeasesToStand t c :=
  Listed.coming_iff_ceasing census bounded

instance Web.decideComesToStand (W : Web F C) (t : Nat) (c : C) :
    Decidable (W.ComesToStand t c) :=
  instDecidableAnd

instance Web.decideCeasesToStand (W : Web F C) (t : Nat) (c : C) :
    Decidable (W.CeasesToStand t c) :=
  instDecidableAnd

/-- The census balance read of standing: over any stretch, the conditions standing at the
end with those that ceased to stand are those standing at the start with those that came
to stand (`Listed.over_stretch`). -/
theorem Web.StandingCensus.over_stretch {W : Web F C} {stand : Nat → List C}
    (census : W.StandingCensus stand) (S n : Nat) :
    (stand (S + n)).length + total (steps S n) (fun t => total (stand t) fun c =>
      mark (W.CeasesToStand t c)) =
      (stand S).length + total (steps S n) (fun t => total (stand (t + 1)) fun c =>
        mark (W.ComesToStand t c)) :=
  Listed.over_stretch census S n

/-- The step from `t` is enclosed around what stands across it: some family without
repetition, closed across the step, holds whatever stands before or after it. -/
def Flow.AroundStanding (L : Flow F C) (stand : Nat → List C) (t : Nat) : Prop :=
  ∃ es, Distinct es ∧ (∀ c, c ∈ stand t → c ∈ es) ∧ (∀ c, c ∈ stand (t + 1) → c ∈ es) ∧
    L.ClosedAt es t

/-- The total standing over the list of what stands is the stock of any family without
repetition holding it. -/
theorem Web.StandingCensus.stock_eq {W : Web F C} {stand : Nat → List C}
    (census : W.StandingCensus stand) {es : List C} (distinct : Distinct es) {t : Nat}
    (within : ∀ c, c ∈ stand t → c ∈ es) : W.stock (stand t) t = W.stock es t :=
  Nat.le_antisymm (total_le_of_support (census t).1 fun c mem _ => within c mem)
    (total_le_of_support distinct fun c _ positive => ((census t).2 c).mp positive)

namespace Flow

variable {L : Flow F C} {W : Web F C} {stand : Nat → List C}

/-- With equality decided, a step enclosed by some family is enclosed around what
stands. -/
theorem Enclosed.aroundStanding [DecidableEq C] {t : Nat} (enclosed : L.Enclosed t)
    (stand : Nat → List C) : L.AroundStanding stand t :=
  match enclosed.around (stand t ++ stand (t + 1)) with
  | ⟨es, distinct, within, closed⟩ =>
    ⟨es, distinct, fun c mem => within c (mem_append_left _ mem),
     fun c mem => within c (mem_append_right _ mem), closed⟩

/-- Without decided equality, a step enclosed by some family is not not enclosed around
what stands (`Enclosed.around_not_not`). -/
theorem Enclosed.aroundStanding_not_not {t : Nat} (enclosed : L.Enclosed t)
    (stand : Nat → List C) : ¬¬ L.AroundStanding stand t :=
  fun no => enclosed.around_not_not (stand t ++ stand (t + 1))
    fun ⟨es, distinct, within, closed⟩ => no ⟨es, distinct,
      fun c mem => within c (mem_append_left _ mem),
      fun c mem => within c (mem_append_right _ mem), closed⟩

/-- A member of a family dissipated on across the step falling lowers the family's stock:
it is taken from. -/
theorem fall_lowers_on (balances : L.Balances W) {ds : List C} {t : Nat}
    (dissipates : L.DissipatesOn ds t) {c : C} (mem : c ∈ ds) (falls : W.Falls t c) :
    W.stock ds (t + 1) < W.stock ds t :=
  match total_pos (L.present t) (balances.fall_taken falls) with
  | ⟨_, present, takes⟩ => Nat.lt_of_lt_of_le
      (Nat.lt_add_of_pos_right (total_pos_of_mem (q := fun f => sign (total ds (L.take t f)))
        present (sign_pos (total_pos_of_mem mem takes))))
      (balances.runs_down dissipates)

/-- Under dissipation, across a step enclosed around what stands, the total standing falls
by at least the number of formations taking from the enclosing family. -/
theorem standing_runs_down (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} :
    L.AroundStanding stand t →
      ∃ es, W.stock (stand (t + 1)) (t + 1) + L.takers es t ≤ W.stock (stand t) t
  | ⟨es, distinct, before, after, closed⟩ =>
    ⟨es, Nat.le_trans (Nat.le_of_eq (congrArg (· + L.takers es t) (census.stock_eq distinct after)))
      (Nat.le_trans (balances.runs_down (dissipative es t distinct closed))
        (Nat.le_of_eq (census.stock_eq distinct before).symm))⟩

/-- So the total standing does not rise. -/
theorem standing_never_rises (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} (around : L.AroundStanding stand t) :
    W.stock (stand (t + 1)) (t + 1) ≤ W.stock (stand t) t :=
  match standing_runs_down balances dissipative census around with
  | ⟨_, runs⟩ => Nat.le_trans (Nat.le_add_right _ _) runs

/-- And any condition's standing rising or falling across the step lowers it. -/
theorem change_lowers (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} (around : L.AroundStanding stand t) {c : C}
    (changes : W.Rises t c ∨ W.Falls t c) :
    W.stock (stand (t + 1)) (t + 1) < W.stock (stand t) t :=
  match around with
  | ⟨es, distinct, before, after, closed⟩ =>
    have dissipates := dissipative es t distinct closed
    have lowers : W.stock es (t + 1) < W.stock es t := match changes with
      | .inl rises => rise_lowers_on balances dissipates
          (after c (((census (t + 1)).2 c).mp (Nat.lt_of_le_of_lt (Nat.zero_le _) rises))) rises
      | .inr falls => fall_lowers_on balances dissipates
          (before c (((census t).2 c).mp (Nat.lt_of_le_of_lt (Nat.zero_le _) falls))) falls
    Nat.lt_of_le_of_lt (Nat.le_of_eq (census.stock_eq distinct after))
      (Nat.lt_of_lt_of_le lowers (Nat.le_of_eq (census.stock_eq distinct before).symm))

/-- Standing comes to rest: where every step from some step on is enclosed around what
stands, no condition's standing changes at arbitrarily late steps. It is enough that each
of those enclosures is not refuted, since what the proof compares are numbers, whose order
is decided. -/
theorem stills (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {T : Nat}
    (around : ∀ t, T ≤ t → ¬¬ L.AroundStanding stand t) :
    ¬ ∀ N, ∃ t c, N ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  fun changing => falls_finitely (fun t => W.stock (stand t) t) T
    (fun t later => Decidable.of_not_not fun rises => around t later fun enclosed =>
      rises (standing_never_rises balances dissipative census enclosed))
    fun N => match changing (N + T) with
    | ⟨t, _, later, changes⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
        Decidable.of_not_not fun stays =>
          around t (Nat.le_trans (Nat.le_add_left T N) later) fun enclosed =>
            stays (change_lowers balances dissipative census enclosed changes)⟩

end Flow

/-! ## Arising and ceasing under a census -/

namespace World

/-- At most `B t` relata are active at each step `t`, listed each once (`Web.Census`). -/
def CountedBy (w : World) (B : Nat → Nat) : Prop :=
  ∃ alive, w.web.Census alive ∧ ∀ t, (alive t).length ≤ B t

/-- At most `B` relata are active at each step: counted by a bound that does not grow. -/
def CountedWithin (w : World) (B : Nat) : Prop :=
  w.CountedBy fun _ => B

variable {w : World}

/-- The census law: in a world with a census whose activity is decided, ceasing recurs
only where arising recurs (`Web.arising_of_ceasing`). -/
theorem arising_of_ceasing [∀ t x, Decidable (w.web.active t x)] (counted : w.Counted)
    (ceasing : w.CeasingRecurs) : w.ArisingRecurs :=
  match counted with
  | ⟨_, census⟩ => w.web.arising_of_ceasing census ceasing

/-- With at most `B` relata active at each step, arising recurs exactly when ceasing does
(`Web.unceasing_iff_bounded`). -/
theorem CountedWithin.arising_iff_ceasing [∀ t x, Decidable (w.web.active t x)] {B : Nat}
    (counted : w.CountedWithin B) : w.ArisingRecurs ↔ w.CeasingRecurs :=
  match counted with
  | ⟨_, census, bounded⟩ => w.web.unceasing_iff_bounded census (T := 0) fun t _ => bounded t

/-- Where the bound returns to at most `K` at arbitrarily late steps, however large it grows
between, arising recurs exactly when ceasing does (`Listed.ceasing_of_returning`). -/
theorem CountedBy.arising_iff_ceasing [∀ t x, Decidable (w.web.active t x)] {B : Nat → Nat}
    {K : Nat} (counted : w.CountedBy B) (returns : ∀ N, ∃ t, N ≤ t ∧ B t ≤ K) :
    w.ArisingRecurs ↔ w.CeasingRecurs :=
  match counted with
  | ⟨alive, census, bounded⟩ =>
    ⟨Listed.ceasing_of_returning census fun N => match returns N with
      | ⟨t, later, low⟩ => ⟨t, later, Nat.le_trans (bounded t) low⟩,
     arising_of_ceasing ⟨alive, census⟩⟩

/-- Every census of a finite world counts within the number of its relata; no
decidability is needed (the eleventh review's probe). -/
theorem Finite.census_bounded (finite : w.Finite) :
    ∃ B, ∀ alive, w.web.Census alive → ∀ t, (alive t).length ≤ B :=
  match finite with
  | ⟨all, _, every⟩ =>
    ⟨all.length, fun _ census t => length_le_of_sub (census t).1 fun x _ => every x⟩

/-- A finite world whose activity is decided has a census (`Finite.counted`), and it counts
within the number of its relata. -/
theorem Finite.countedWithin [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite) :
    ∃ B, w.CountedWithin B :=
  match finite.census_bounded, finite.counted with
  | ⟨B, bounded⟩, ⟨alive, census⟩ => ⟨B, alive, census, bounded alive census⟩

/-- So the law of finite worlds, `World.arising_iff_ceasing`, is a case of the bounded
law. -/
theorem Finite.arising_iff_ceasing [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite) :
    w.ArisingRecurs ↔ w.CeasingRecurs :=
  match finite.countedWithin with
  | ⟨_, counted⟩ => counted.arising_iff_ceasing

end World

namespace Dawn

/-- The relata of `World.dawn` active at step `t`: the formations that arose before it. -/
def alive : Nat → List (Nat ⊕ Unit)
  | 0 => []
  | t + 1 => .inl t :: alive t

theorem mem_alive : ∀ {t : Nat} {x : Nat ⊕ Unit}, x ∈ alive t ↔ World.dawn.web.active t x
  | 0, .inl f => ⟨fun mem => (nomatch mem), fun active => absurd active (Nat.not_lt_zero f)⟩
  | 0, .inr _ => ⟨fun mem => (nomatch mem), False.elim⟩
  | t + 1, .inl _ => ⟨fun mem => match mem with
      | .head _ => Nat.lt_succ_self _
      | .tail _ mem => Nat.lt_succ_of_lt ((mem_alive (t := t)).mp mem),
    fun active => match Nat.eq_or_lt_of_le (Nat.le_of_lt_succ active) with
      | .inl same => same ▸ .head _
      | .inr lower => .tail _ ((mem_alive (t := t)).mpr lower)⟩
  | t + 1, .inr _ => ⟨fun mem => match mem with
      | .tail _ mem => (mem_alive (t := t)).mp mem, False.elim⟩

theorem alive_distinct : ∀ t, Distinct (alive t)
  | 0 => trivial
  | t + 1 => ⟨fun mem => Nat.lt_irrefl t (mem_alive.mp mem), alive_distinct t⟩

/-- At each step finitely many relata of `World.dawn` are active. -/
theorem census : World.dawn.web.Census alive :=
  fun t => ⟨alive_distinct t, fun _ => mem_alive.symm⟩

end Dawn

namespace World

/-- One way only. In `dawn`, which has a census, arising recurs while ceasing does not; in
`dusk` ceasing recurs while nothing arises, so by the census law it has no census. -/
theorem census_one_way :
    (dawn.Counted ∧ dawn.ArisingRecurs ∧ ¬ dawn.CeasingRecurs) ∧
    (dusk.CeasingRecurs ∧ ¬ dusk.ArisingRecurs ∧ ¬ dusk.Counted) :=
  match separate with
  | ⟨⟨arising, quiet, _⟩, ⟨ceasing, still, _⟩⟩ =>
    ⟨⟨⟨Dawn.alive, Dawn.census⟩, arising, quiet⟩,
     ⟨ceasing, still, fun counted => still (arising_of_ceasing counted ceasing)⟩⟩

/-- `dawn` has a census but no bound on it: arising recurs there while ceasing does not. -/
theorem dawn_unbounded (B : Nat) : ¬ dawn.CountedWithin B :=
  fun counted => census_one_way.1.2.2 (counted.arising_iff_ceasing.mp census_one_way.1.2.1)

end World

namespace Procession

/-- Relatum `x` is active at step `x` alone. -/
def web : Web Nat Nat where
  level _ _ := 0
  active t x := x = t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- One relatum is active at each step, listed once. -/
theorem census : web.Census fun t => [t] :=
  fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun _ =>
    ⟨fun same => match same with | rfl => .head _, fun mem => match mem with
      | .head _ => rfl
      | .tail _ no => (nomatch no)⟩⟩

end Procession

namespace World

/-- Relatum `x` is active at step `x` alone: infinitely many relata, one active at a time.
-/
def procession : World :=
  ⟨Nat, Flow.still, Procession.web⟩

instance procession_decided : ∀ t x, Decidable (procession.web.active t x) :=
  fun t x => Nat.decEq x t

/-- The bounded law reaches beyond finite worlds: in `procession` one relatum is active at
each step, arising and ceasing both recur, and the relata are not finitely many. -/
theorem procession_world :
    procession.CountedWithin 1 ∧ procession.ArisingRecurs ∧ procession.CeasingRecurs ∧
    ¬ procession.Finite :=
  ⟨⟨fun t => [t], Procession.census, fun _ => Nat.le_refl 1⟩,
   fun N => ⟨N, N + 1, Nat.le_refl N, Nat.ne_of_gt (Nat.lt_succ_self N), rfl⟩,
   fun N => ⟨N, N, Nat.le_refl N, rfl, Nat.ne_of_lt (Nat.lt_succ_self N)⟩,
   fun ⟨all, _, every⟩ => beyond_not_mem all (every (beyond all))⟩

namespace Slow

/-- Relatum `x` is active at step `t` while below `B t`. -/
def web (B : Nat → Nat) : Web Nat Nat where
  level _ _ := 0
  active t x := x < B t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

theorem length : ∀ n, (Cycle.present n).length = n
  | 0 => rfl
  | n + 1 => congrArg Nat.succ (length n)

/-- The relata below `B t`, listed as the cycle lists its formations, each once. -/
theorem census (B : Nat → Nat) : (web B).Census fun t => Cycle.present (B t) :=
  fun t => ⟨Cycle.distinct (B t), fun x => ⟨Cycle.listed (B t) x, Cycle.present_lt (B t) x⟩⟩

theorem grows_between {B : Nat → Nat} (grows : ∀ t, B t ≤ B (t + 1)) :
    ∀ {s t}, s ≤ t → B s ≤ B t
  | _, _, .refl => Nat.le_refl _
  | _, _, .step within => Nat.le_trans (grows_between grows within) (grows _)

end Slow

namespace World

/-- Relatum `x` is active at step `t` while below `B t`. -/
def slow (B : Nat → Nat) : World :=
  ⟨Nat, Flow.still, Slow.web B⟩

instance slow_decided (B : Nat → Nat) : ∀ t x, Decidable ((slow B).web.active t x) :=
  fun t x => Nat.decLt x (B t)

/-- No bound growing without end keeps arising and ceasing together, however slowly it
grows. In `slow B`, counted by a non-decreasing, unbounded `B`, relatum `B t` arises across
each step at which the bound grows, and nothing ceases. -/
theorem slow_world {B : Nat → Nat} (grows : ∀ t, B t ≤ B (t + 1))
    (unbounded : ∀ n, ∃ t, n < B t) :
    (slow B).CountedBy B ∧ (slow B).ArisingRecurs ∧ ∀ t x, ¬ (slow B).web.Ceases t x :=
  ⟨⟨fun t => Cycle.present (B t), Slow.census B, fun t => Nat.le_of_eq (Slow.length (B t))⟩,
   fun N => match unbounded (B N) with
    | ⟨T, higher⟩ => match Nat.lt_or_ge T N with
      | .inl earlier => absurd higher
          (Nat.not_lt_of_ge (Slow.grows_between grows (Nat.le_of_lt earlier)))
      | .inr later => match rises_between (q := B) later higher with
        | ⟨t, from_, _, up⟩ => ⟨t, B t, from_, Nat.lt_irrefl (B t), up⟩,
   fun t _ ceases => ceases.2 (Nat.lt_of_lt_of_le ceases.1 (grows t))⟩

end World

/-! ## Worlds come to rest -/

variable {w : World}

/-- Arising stops where what stands is listed, whatever arises is embodied, the flow
balances and dissipates, and every step from some step on is enclosed around what stands:
no standing changes at arbitrarily late steps (`Flow.stills`), and an embodied relatum
arising comes to stand. Ceasing need not stop (`rest_needs_census`). -/
theorem arising_stops {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) : ¬ w.ArisingRecurs :=
  fun arising => Flow.stills balanced dissipative standing
    (fun t later => not_not_intro (around t later)) fun N => match arising N with
    | ⟨t, x, later, arises⟩ =>
      ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩

/-- The rest theorem. A world with a census of activity and of what stands, whose arising
is embodied, with a balanced, dissipative flow, in which every step from some step on is
enclosed around what stands, comes to rest. Arising stops (`arising_stops`), and by the
census law ceasing stops too. -/
theorem comes_to_rest [decided : ∀ t x, Decidable (w.web.active t x)] (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  have quiet := arising_stops standing embodied balanced dissipative around
  ⟨quiet, fun ceasing => quiet (arising_of_ceasing counted ceasing)⟩

/-- A finite world lists what stands at each step, and every step is enclosed around it,
so `World.rests` is the finite case of the rest theorem (`Finite.comes_to_rest`). -/
theorem Finite.standing (finite : w.Finite) :
    ∃ stand, w.web.StandingCensus stand ∧ ∀ t, w.flow.AroundStanding stand t :=
  match finite with
  | ⟨all, distinct, every⟩ =>
    ⟨fun t => keep (fun x => 0 < w.web.level t x) all,
     fun _ => ⟨keep_distinct distinct, fun x =>
       ⟨fun standing => mem_keep.mpr ⟨every x, standing⟩, fun mem => (mem_keep.mp mem).2⟩⟩,
     fun _ => ⟨all, distinct, fun c _ => every c, fun c _ => every c,
       fun _ _ c outside => absurd (every c) outside⟩⟩

/-- The finite case: `World.rests` follows from the rest theorem. -/
theorem Finite.comes_to_rest [∀ t x, Decidable (w.web.active t x)] (finite : w.Finite)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match finite.standing with
  | ⟨_, standing, around⟩ => World.comes_to_rest finite.counted standing embodied balanced
      dissipative (T := 0) fun t _ => around t

/-- The rest theorem needs its census of activity: in `dusk` nothing stands and nothing
takes part, so every other premise holds, every step is enclosed around what stands, and
ceasing recurs. -/
theorem rest_needs_census :
    dusk.web.StandingCensus (fun _ => []) ∧ dusk.ArisingEmbodied ∧ dusk.Balanced ∧
    dusk.Dissipative ∧ (∀ t, dusk.flow.AroundStanding (fun _ => []) t) ∧
    dusk.CeasingRecurs ∧ ¬ dusk.Counted :=
  ⟨fun _ => ⟨trivial, fun x => match x with
      | .inl _ => ⟨fun standing => absurd standing (Nat.lt_irrefl 0), fun mem => (nomatch mem)⟩
      | .inr _ => ⟨fun standing => absurd standing (Nat.lt_irrefl 0), fun mem => (nomatch mem)⟩⟩,
   fun t x arises => match x, arises with
      | .inl f, arises => absurd arises (Dusk.nothing_arises t f)
      | .inr _, arises => False.elim arises.2,
   fun _ x => match x with
      | .inl _ => rfl
      | .inr _ => rfl,
   fun _ _ _ _ _ present => (nomatch present),
   fun _ => ⟨[], trivial, fun _ mem => (nomatch mem), fun _ mem => (nomatch mem),
     fun _ present => (nomatch present)⟩,
   census_one_way.2.1, census_one_way.2.2.2⟩

/-- With a census of the active relata, every relatum embodied, what stands is listed. -/
theorem standingCensus {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) : w.web.StandingCensus alive :=
  fun t => ⟨(census t).1, fun x => (embodied x t).symm.trans ((census t).2 x)⟩

/-- An embodied relatum arising rises. -/
theorem rises_of_arises (embodied : w.Embodied) {t : Nat} {x : w.Relatum}
    (arises : w.web.Arises t x) : w.web.Rises t x :=
  Web.ComesToStand.rises (W := w.web)
    ⟨fun standing => arises.1 ((embodied x t).mpr standing), (embodied x (t + 1)).mp arises.2⟩

/-- An embodied relatum ceasing falls. -/
theorem falls_of_ceases (embodied : w.Embodied) {t : Nat} {x : w.Relatum}
    (ceases : w.web.Ceases t x) : w.web.Falls t x :=
  Nat.lt_of_le_of_lt
    (Nat.le_of_eq (eq_zero_of_not_pos fun standing => ceases.2 ((embodied x (t + 1)).mpr standing)))
    ((embodied x t).mp ceases.1)

/-- A world with a census whose relata are embodied, with a balanced, dissipative flow, in
which every step from some step on is enclosed around what stands, comes to rest: neither
arising nor ceasing recurs. -/
theorem rests_around {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (around : ∀ t, T ≤ t → w.flow.AroundStanding alive t) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  comes_to_rest (decided := fun t x => decidable_of_iff _ (embodied x t).symm) ⟨alive, census⟩
    (standingCensus census embodied) embodied.arising balanced dissipative around

/-- Enclosure from some step on suffices, with no decision of equality: each enclosed step
is not not enclosed around what stands, which is enough for standing to come to rest; an
embodied relatum arising rises, and one ceasing falls. -/
theorem rests_enclosed (counted : w.Counted) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) : ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match counted with
  | ⟨alive, census⟩ =>
    have still := Flow.stills balanced dissipative (standingCensus census embodied)
      fun t later => (enclosed t later).aroundStanding_not_not alive
    ⟨fun arising => still fun N => match arising N with
      | ⟨t, x, later, arises⟩ => ⟨t, x, later, .inl (rises_of_arises embodied arises)⟩,
     fun ceasing => still fun N => match ceasing N with
      | ⟨t, x, later, ceases⟩ => ⟨t, x, later, .inr (falls_of_ceases embodied ceases)⟩⟩

/-- So arising without end, in a world with a census whose relata are embodied and
whose flow balances and dissipates, is incompatible with every step from any point on
being enclosed: the world exchanges beyond every finite family. -/
theorem arising_opens (counted : w.Counted)
    (embodied : w.Embodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    (arising : w.ArisingRecurs) (T : Nat) : ¬ ∀ t, T ≤ t → w.flow.Enclosed t :=
  fun enclosed => (rests_enclosed counted embodied balanced dissipative enclosed).1 arising

end World

/-! ## What comes to rest is few -/

/-- The lists of the steps up to `n`, joined. -/
def gather (l : Nat → List α) : Nat → List α
  | 0 => l 0
  | n + 1 => l (n + 1) ++ gather l n

theorem gather_self {l : Nat → List α} {a : α} : ∀ {s : Nat}, a ∈ l s → a ∈ gather l s
  | 0, mem => mem
  | _ + 1, mem => mem_append_left _ mem

theorem mem_gather {l : Nat → List α} {a : α} {s : Nat} (mem : a ∈ l s) :
    ∀ {n}, s ≤ n → a ∈ gather l n
  | _, .refl => gather_self mem
  | m + 1, .step within => mem_append_right (l (m + 1)) (mem_gather mem within)

/-- A determination failing at `N` and holding at a later `T` came to be across a step
from `N` on. -/
theorem comes_after {p : Nat → Prop} [∀ t, Decidable (p t)] {N : Nat} (fails : ¬ p N) :
    ∀ {T}, N ≤ T → p T → ∃ t, N ≤ t ∧ ComesToBe p t
  | _, .refl, holds => absurd holds fails
  | m + 1, .step within, holds =>
    if h : p m then comes_after fails within h else ⟨m, within, h, holds⟩

/-- Where what holds is listed at each step and coming to be does not recur, not
unboundedly many members ever hold: not every finite list misses a member holding at some
step (the eleventh review's probe). -/
theorem Listed.few_of_quiet {p : α → Nat → Prop} [∀ a t, Decidable (p a t)]
    {l : Nat → List α} (listed : Listed p l)
    (quiet : ¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ¬ ∀ L : List α, ∃ t a, p a t ∧ ¬ a ∈ L :=
  fun many => quiet fun N => match many (gather l N) with
    | ⟨t, a, holds, out⟩ =>
      have fails : ¬ p a N := fun h => out (mem_gather (((listed N).2 a).mp h) (Nat.le_refl N))
      match Nat.decLe N t with
      | isTrue later => match comes_after fails later holds with
        | ⟨s, after, comes⟩ => ⟨s, a, after, comes⟩
      | isFalse early => absurd (mem_gather (((listed t).2 a).mp holds)
          (Nat.le_of_lt (Nat.gt_of_not_le early))) out

namespace World

variable {w : World}

/-- Read of activity: under a census, where arising does not recur, not unboundedly many
relata are ever active. -/
theorem few_active [∀ t x, Decidable (w.web.active t x)] {alive : Nat → List w.Relatum}
    (census : w.web.Census alive) (quiet : ¬ w.ArisingRecurs) :
    ¬ ∀ L : List w.Relatum, ∃ t x, w.web.active t x ∧ ¬ x ∈ L :=
  Listed.few_of_quiet (p := fun x t => w.web.active t x) census quiet

/-- In every world to which the rest theorem applies, with enclosure from some step on not
refuted, not unboundedly many relata are ever active and not unboundedly many ever stand
(the eleventh review's probe). So the worlds it covers beyond finite ones add only relata
that never stand or act. -/
theorem rest_few [∀ t x, Decidable (w.web.active t x)] (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → ¬¬ w.flow.AroundStanding stand t) :
    (¬ ∀ L : List w.Relatum, ∃ t x, w.web.active t x ∧ ¬ x ∈ L) ∧
    (¬ ∀ L : List w.Relatum, ∃ t x, 0 < w.web.level t x ∧ ¬ x ∈ L) :=
  have still := Flow.stills balanced dissipative standing around
  match counted with
  | ⟨_, census⟩ =>
    ⟨few_active census fun arising => still fun N => match arising N with
      | ⟨t, x, later, arises⟩ =>
        ⟨t, x, later, .inl ((embodied t x arises).comesToStand arises).rises⟩,
     Listed.few_of_quiet (p := fun x t => 0 < w.web.level t x) standing fun coming =>
       still fun N => match coming N with
       | ⟨t, x, later, comes⟩ => ⟨t, x, later, .inl (Web.ComesToStand.rises (W := w.web) comes)⟩⟩

end World

/-! ## Openness cannot be dropped -/

namespace Exposed

inductive Relatum where
  | side (b : Bool)
  | ground (n : Nat)

/-- The sides stand as in `Handing`; the ground relata stand at nothing. -/
def level (t : Nat) : Relatum → Nat
  | .side b => Handing.stands b t
  | .ground _ => 0

/-- Across every step the side holding the standing hands it to the other, as in
`Handing`, and takes a unit from each ground relatum and gives it back. -/
def flow : Flow Relatum Relatum where
  present t := [.side (Handing.holder t)]
  take t x y := match x, y with
    | .side b, .side c => Handing.flow.take t b c
    | .side _, .ground _ => 1
    | .ground _, .side _ => 0
    | .ground _, .ground _ => 0
  give t x y := match x, y with
    | .side b, .side c => Handing.flow.give t b c
    | .side _, .ground _ => 1
    | .ground _, .side _ => 0
    | .ground _, .ground _ => 0

/-- A relatum is active while it stands; nothing depends on anything, and the sides draw
on everything. -/
def web : Web Relatum Relatum where
  level := level
  active t x := 0 < level t x
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- Which side a side relatum is. -/
def sideOf : Relatum → Bool
  | .side b => b
  | .ground _ => false

/-- The index of a ground relatum. -/
def index : Relatum → Nat
  | .side _ => 0
  | .ground n => n

/-- No finite family holds every ground relatum. -/
theorem outside (cs : List Relatum) : ¬ Relatum.ground (beyond (cs.map index)) ∈ cs :=
  fun mem => beyond_not_mem _ (mem_map_of (g := index) mem)

/-- No step is enclosed: the side taking part takes from every ground relatum. -/
theorem open_at (t : Nat) : ¬ flow.Enclosed t :=
  fun ⟨cs, _, closed⟩ => Nat.zero_ne_one
    (closed (.side (Handing.holder t)) (.head _) _ (outside cs)).1.symm

/-- A side stands exactly when it holds the standing. -/
theorem stands_iff : ∀ (b : Bool) (t : Nat), 0 < Handing.stands b t ↔ b = Handing.holder t
  | true, 0 => ⟨fun _ => rfl, fun _ => Nat.zero_lt_one⟩
  | false, 0 => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => Bool.noConfusion no⟩
  | true, 1 => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => Bool.noConfusion no⟩
  | false, 1 => ⟨fun _ => rfl, fun _ => Nat.zero_lt_one⟩
  | true, t + 2 => stands_iff true t
  | false, t + 2 => stands_iff false t

/-- The side holding the standing is the one active relatum. -/
theorem census : web.Census fun t => [.side (Handing.holder t)] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side b => ⟨fun standing => Eq.subst
          (motive := fun c => Relatum.side c ∈ [Relatum.side (Handing.holder t)])
          ((stands_iff b t).mp standing).symm (.head _),
        fun mem => (stands_iff b t).mpr (match mem_cons_cases mem with
          | .inl same => congrArg sideOf same
          | .inr no => nomatch no)⟩
    | .ground n => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Relatum.ground n ∈ [Relatum.side (Handing.holder t)]) => match mem with
          | .tail _ no => (nomatch no)⟩⟩

/-- The holder stands at one. -/
theorem holder_one : ∀ t, Handing.stands (Handing.holder t) t = 1
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (Handing.stands_two (Handing.holder t) t).trans (holder_one t)

/-- And stands at nothing after the step. -/
theorem holder_after : ∀ t, Handing.stands (Handing.holder t) (t + 1) = 0
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (Handing.stands_two (Handing.holder t) (t + 1)).trans (holder_after t)

end Exposed

namespace Holding

/-- One side stands at one throughout; the other side and the ground stand at nothing. -/
def level (_ : Nat) : Exposed.Relatum → Nat
  | .side true => 1
  | .side false => 0
  | .ground _ => 0

/-- At every step the standing side takes a unit from each ground relatum and gives it
back. -/
def flow : Flow Exposed.Relatum Exposed.Relatum where
  present _ := [.side true]
  take _ x y := match x, y with
    | .side true, .ground _ => 1
    | .side true, .side _ => 0
    | .side false, _ => 0
    | .ground _, _ => 0
  give _ x y := match x, y with
    | .side true, .ground _ => 1
    | .side true, .side _ => 0
    | .side false, _ => 0
    | .ground _, _ => 0

/-- Every relatum is active while it stands, depends on nothing, and draws on everything. -/
def web : Web Exposed.Relatum Exposed.Relatum where
  level := level
  active t x := 0 < level t x
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

theorem open_at (t : Nat) : ¬ flow.Enclosed t :=
  fun ⟨cs, _, closed⟩ => Nat.zero_ne_one
    (closed (.side true) (.head _) _ (Exposed.outside cs)).1.symm

theorem census : web.Census fun _ => [.side true] :=
  fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side true => ⟨fun _ => .head _, fun _ => Nat.zero_lt_one⟩
    | .side false => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Exposed.Relatum.side false ∈ [Exposed.Relatum.side true]) => match mem with
          | .tail _ no => (nomatch no)⟩
    | .ground n => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Exposed.Relatum.ground n ∈ [Exposed.Relatum.side true]) => match mem with
          | .tail _ no => (nomatch no)⟩⟩

end Holding

namespace World

/-- The sides of `Handing` exchanging with an unbounded ground. -/
def exposed : World :=
  ⟨Exposed.Relatum, Exposed.flow, Exposed.web⟩

/-- `exposed` meets all eight premises and arising recurs in it: no step is enclosed, so
dissipation binds at none. -/
theorem exposed_world :
    exposed.Premised ∧ exposed.ArisingRecurs ∧ ∀ t, ¬ exposed.flow.Enclosed t :=
  ⟨.of (fun _ _ _ _ no => no.elim)
     (fun t c => match c with
      | .side c => Handing.balances t c
      | .ground _ => rfl)
     (fun t f _ present _ => match f, present with
      | _, .head _ => Handing.holder_stands t
      | _, .tail _ no => (nomatch no))
     (fun t f _ present _ => match f, present with
      | _, .head _ => ⟨Handing.holder_stands t, trivial⟩
      | _, .tail _ no => (nomatch no))
     (fun cs t distinct closed => absurd ⟨cs, distinct, closed⟩ (Exposed.open_at t))
     (fun _ _ => Iff.rfl) ⟨_, Exposed.census⟩ ⟨0, fun _ _ _ _ _ no => no.elim⟩,
   fun N => match Handing.recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩,
   Exposed.open_at⟩

/-- What stands in `exposed` is listed, the holder alone: the total standing is one at every
step, and the holder falls across every step. The world is not finite; what is unbounded
is the number of relata it exchanges with, each standing at nothing (the tenth review's
probe). -/
theorem exposed_standing :
    exposed.web.StandingCensus (fun t => [Exposed.Relatum.side (Handing.holder t)]) ∧
    (∀ t, exposed.web.stock [Exposed.Relatum.side (Handing.holder t)] t = 1) ∧
    (∀ t, exposed.web.Falls t (Exposed.Relatum.side (Handing.holder t))) ∧
    ¬ exposed.Finite :=
  ⟨standingCensus Exposed.census fun _ _ => Iff.rfl,
   fun t => show Handing.stands (Handing.holder t) t + 0 = 1 from Exposed.holder_one t,
   fun t => show Handing.stands (Handing.holder t) (t + 1) < Handing.stands (Handing.holder t) t
     from Nat.lt_of_lt_of_le (Nat.lt_of_le_of_lt (Nat.le_of_eq (Exposed.holder_after t))
       Nat.zero_lt_one) (Nat.le_of_eq (Exposed.holder_one t).symm),
   fun ⟨all, _, every⟩ => Exposed.outside all (every _)⟩

/-- The eight premises decide neither enclosure nor openness: `exposed` meets them with no
step enclosed and keeps arising, and mutualists meet them with every step enclosed and do
not keep arising (the tenth review's probe). -/
theorem openness_contingent :
    (exposed.Premised ∧ (∀ t, ¬ exposed.flow.Enclosed t) ∧ exposed.ArisingRecurs) ∧
    (mutualism.Premised ∧ (∀ t, mutualism.flow.Enclosed t) ∧ ¬ mutualism.ArisingRecurs) :=
  ⟨⟨exposed_world.1, exposed_world.2.2, exposed_world.2.1⟩,
   ⟨mutualism_premised, mutualism_finite.enclosed, mutualism_world.2.1⟩⟩

/-- One side holding its standing while exchanging at zero net with an unbounded ground. -/
def holding : World :=
  ⟨Exposed.Relatum, Holding.flow, Holding.web⟩

/-- Openness with the eight premises does not give arising without end: `holding` meets all
eight with no step enclosed, and nothing ever arises or ceases (the eleventh review's
probe). Under a census, with whatever arises embodied, balance and dissipation, openness is
necessary for arising without end (`arising_opens`), not sufficient. -/
theorem holding_world :
    holding.Premised ∧ (∀ t, ¬ holding.flow.Enclosed t) ∧ ¬ holding.ArisingRecurs ∧
    ¬ holding.CeasingRecurs ∧ ¬ holding.Finite :=
  ⟨.of (fun _ _ _ _ no => no.elim)
     (fun _ c => match c with
      | .side true => rfl
      | .side false => rfl
      | .ground _ => rfl)
     (fun _ f _ present _ => match f, present with
      | _, .head _ => Nat.zero_lt_one
      | _, .tail _ no => (nomatch no))
     (fun _ f _ present _ => match f, present with
      | _, .head _ => ⟨Nat.zero_lt_one, trivial⟩
      | _, .tail _ no => (nomatch no))
     (fun cs t distinct closed => absurd ⟨cs, distinct, closed⟩ (Holding.open_at t))
     (fun _ _ => Iff.rfl) ⟨_, Holding.census⟩ ⟨0, fun _ _ _ _ _ no => no.elim⟩,
   Holding.open_at,
   fun arising => match arising 0 with
    | ⟨_, x, _, arises⟩ => match x, arises with
      | .side true, arises => arises.1 Nat.zero_lt_one
      | .side false, arises => absurd arises.2 (Nat.lt_irrefl 0)
      | .ground _, arises => absurd arises.2 (Nat.lt_irrefl 0),
   fun ceasing => match ceasing 0 with
    | ⟨_, x, _, ceases⟩ => match x, ceases with
      | .side true, ceases => ceases.2 Nat.zero_lt_one
      | .side false, ceases => absurd ceases.1 (Nat.lt_irrefl 0)
      | .ground _, ceases => absurd ceases.1 (Nat.lt_irrefl 0),
   fun ⟨all, _, every⟩ => Exposed.outside all (every _)⟩

/-- A world meeting all eight premises with each binding comes to rest (`hatch_binds`).
Across the first step the child arises and the parent ceases; every step is enclosed
within the food, the parent and the child, and finitely many stand at each step, though
the world is not finite. -/
theorem hatch_rests : hatch.web.Arises 0 .child ∧ hatch.web.Ceases 0 .parent ∧
    ¬ hatch.ArisingRecurs ∧ ¬ hatch.CeasingRecurs :=
  ⟨⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, ⟨Nat.zero_lt_one, Nat.lt_irrefl 0⟩,
   rests_enclosed hatch_counted (fun _ _ => Iff.rfl) hatch_balanced hatch_dissipative
     (T := 0) fun t _ => ⟨Hatch.kin, Hatch.kin_distinct, Hatch.closed t⟩⟩

end World

/-! ## Finitely many standing cannot be dropped -/

namespace Kindling

/-- Which side a side relatum is. -/
def sideOf : Relatum → Bool
  | .side x => x
  | .fuel _ => false

/-- The index of a fuel. -/
def index : Relatum → Nat
  | .side _ => 0
  | .fuel n => n

/-- Every fuel stands at the first step. -/
theorem fuel_stands : ∀ n, 0 < web.level 0 (.fuel n)
  | 0 => Nat.zero_lt_two
  | _ + 1 => Nat.zero_lt_two

/-- The holder is the one active relatum. -/
theorem census : web.Census fun t => [Relatum.side (Handing.holder t)] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side b => ⟨fun active => Eq.subst
          (motive := fun c => Relatum.side c ∈ [Relatum.side (Handing.holder t)])
          ((Exposed.stands_iff b t).mp active).symm (.head _),
        fun mem => (Exposed.stands_iff b t).mpr (match mem_cons_cases mem with
          | .inl same => congrArg sideOf same
          | .inr no => nomatch no)⟩
    | .fuel _ => ⟨fun no => False.elim no, fun mem => match mem with
        | .tail _ no => (nomatch no)⟩⟩

/-- No list holds every fuel: a determination holding of every fuel lists none. -/
theorem unlisted {holds : Relatum → Prop} (l : List Relatum)
    (listed : ∀ x, holds x ↔ x ∈ l) (fuels : ∀ n, holds (.fuel n)) : False :=
  beyond_not_mem (l.map index)
    (mem_map_of (g := index) ((listed (.fuel (beyond (l.map index)))).mp (fuels _)))

end Kindling

namespace Ember

/-- `Kindling`'s levels, each relatum active exactly while it stands, and no dependence. -/
def web : Web Kindling.Relatum Kindling.Relatum where
  level := Kindling.web.level
  active t c := 0 < Kindling.web.level t c
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Ember

namespace World

/-- `Kindling`'s flow with every relatum active while it stands (the tenth review's
probe). -/
def ember : World :=
  ⟨Kindling.Relatum, Kindling.flow, Ember.web⟩

/-- The rest theorem needs its census of what stands. In `kindling` what is active is
listed, whatever arises is embodied, the flow balances and dissipates, and every step is
enclosed around both sides, every relatum ever active; arising recurs, and what stands
cannot be listed, since every unburnt fuel stands. In `ember`, the same flow with every
relatum embodied, every step is enclosed and arising recurs; nothing active can be
listed (the tenth review's probes). -/
theorem rest_needs_standing :
    (kindling.Counted ∧ kindling.ArisingEmbodied ∧ kindling.Balanced ∧
      kindling.Dissipative ∧
      (∀ t, kindling.flow.Around [Kindling.Relatum.side true, .side false] t) ∧
      kindling.ArisingRecurs ∧ ∀ stand, ¬ kindling.web.StandingCensus stand) ∧
    ((∀ t, ember.flow.Enclosed t) ∧ ember.Embodied ∧ ember.Balanced ∧ ember.Dissipative ∧
      ember.ArisingRecurs ∧ ¬ ember.Counted) :=
  ⟨⟨⟨_, Kindling.census⟩, kindling_arising, kindling_world.1, kindling_world.2.1,
    Kindling.around, kindling_world.2.2.2.1,
    fun stand census => Kindling.unlisted (stand 0) (census 0).2 Kindling.fuel_stands⟩,
   ⟨fun t => match Kindling.around t with
     | ⟨es, distinct, _, closed⟩ => ⟨es, distinct, closed⟩,
    fun _ _ => Iff.rfl, Kindling.balances, Kindling.dissipative,
    fun N => match Kindling.kindling.2.2.2.2.2 true N with
     | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩,
    fun ⟨alive, census⟩ => Kindling.unlisted (alive 0) (census 0).2 Kindling.fuel_stands⟩⟩

end World

end Becoming
