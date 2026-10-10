import Becoming.Premises

/-!
# Openness: continued change needs exchange beyond what stands

`Becoming.Space` brings a finite, balanced, dissipative world whose arising is embodied to
rest, and in a finite world arising recurs exactly when ceasing does. This module states
what does the work. The world need not be finite: what brings it to rest is finitely many
standing at each step and enclosure around them from some step on, with a census of what
is active; for arising and ceasing to recur together, a bound on that census. In a world
that comes to rest so, not unboundedly many relata ever stand or are active
(`World.rest_few`): beyond finite worlds, the rest theorem adds relata that never stand
or act, and the flow too comes to rest (`World.exchange_stops`).
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
* **The exchange comes to rest.** Across such a step, a formation taking part that takes
  or gives anything lowers the total standing: the enclosing family holds what it
  exchanges, and giving to it needs taking from it (`Flow.exchange_lowers`). So where
  every step from some step on is enclosed around what stands, no formation takes or
  gives at arbitrarily late steps (`Flow.exchanges_finitely`, `World.exchange_stops`),
  with no census of activity and no embodiment. Each premise is needed, the exchange
  recurring without it (`World.exchange_needs`): without enclosure in `exposed`, which
  meets all eight premises; without dissipation in the cycle of `Becoming.Flow`, its one
  condition standing throughout and every step enclosed around it; without balance in
  `leaking`, finite and dissipative; and without the census of what stands in `throughput`,
  balanced, dissipative and enclosed at every step.
* **Ceasing needs arising.** In a world with a census whose activity is decided, ceasing
  recurs only where arising recurs (`World.arising_of_ceasing`, from
  `Web.arising_of_ceasing`). Not conversely: `accretion` has a census and arises without end
  while nothing ceases; `attrition` keeps ceasing while nothing arises, so it has no census
  (`World.census_one_way`).
* **A bounded count keeps them together.** Where at most `B` relata are active at each
  step (`World.CountedWithin`), arising recurs exactly when ceasing does
  (`World.CountedWithin.arising_iff_ceasing`, from `Web.unceasing_iff_bounded`). Every
  census of a finite world is bounded, with no decidability
  (`World.Finite.census_bounded`), so where activity is decided the law of finite worlds
  is a case (`World.Finite.countedWithin`, `World.Finite.arising_iff_ceasing`);
  `procession`, with one relatum active at a time among infinitely many, keeps arising and
  ceasing
  (`World.procession_world`); `accretion` has no bound (`World.accretion_unbounded`). The bound may
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
  `attrition` meets every other premise and keeps ceasing (`World.rest_needs_census`). Without
  the census of what stands, arising can go on: in `throughput` what is active is listed,
  whatever arises is embodied, the flow balances and dissipates and every step is
  enclosed around every relatum ever active, yet every unburnt fuel stands; in `embodiedThroughput`,
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
  every world that comes to rest under the rest theorem, not unboundedly many relata are
  ever active and not unboundedly many ever stand (`World.rest_few`); conversely, where
  some list holds every relatum ever active and activity is decided, a census exists
  (`World.counted_of_ever`). That stronger form, a list holding every member that ever
  holds, does not follow without omniscience: for a determination listed by at most one
  member and coming to hold at most once, it gives `LPO` (`Listed.lpo_of_few`, `Few`).
  Beyond finite worlds the rest theorem reaches only relata that never stand or act, as
  the idle ground of `hatch` (`World.hatch_idle`).
* **The premises decide neither enclosure nor openness.** The sides of `Shuttle`, also
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
* **Enclosure bounds change.** In a world with a census whose relata are embodied, with a
  balanced, dissipative flow and every step from `T` on enclosed, the relata active at any
  later step, with the steps since `T` at which something arose or ceased, number at most
  the total standing at `T`: that total bounds change (`World.enclosure_bounds_change`,
  `ChangeBound`). A bound from some step is one from the first step
  (`changeBound_iff_zero`). An enclosed queue, whose front exchanges only within the queue
  and whose standing falls by one at each step at which a member joins or leaves, has
  every step enclosed (`World.enclosedQueue_enclosed`), and meets all eight premises
  wherever a bound from the first step holds of its counts and nothing joins an empty
  queue (`World.enclosedQueue_premised`); activity needing support and bounded
  transmission hold there idly, nothing depending on anything. So under the eight, with
  every step from some step on enclosed, the laws of counting are the tally, that nothing
  arises across a step at which nothing is active, and a change bound from the first step
  (`World.enclosed_counting`). On the finitely many places its members ever take, the
  queue is a finite world meeting the eight (`World.finiteQueue_premised`), in which
  dissipation binds and the bound of `World.enclosure_bounds_change` is attained
  (`World.finite_dissipation_binds`, `World.replaced_attains`); so finite worlds have the
  same laws of counting (`World.finite_counting`, `World.enclosed_iff_finite_counting`).
  Change then does not recur (`ChangeBound.not_recurring`), but a step after which nothing
  arises in every finite world meeting the eight would give `LPO`
  (`World.lpo_of_finite_ends`).
* **Counting under each selection, with enclosure.** In worlds enclosed from some step on,
  the laws of counting under each selection of the premises add one condition to those of
  `World.counting_under`, exactly where balance, embodiment and dissipation are selected:
  from some step on change stays within a bound and nothing arises across a step at which
  nothing is active (`World.enclosed_counting_under`). Where neither only active relata
  giving nor only active relata taking is selected, the witness is an enclosed queue
  closing at that step, every relatum exchanging a unit each way with the front before it
  (`World.closingQueue_dissipative`). The enclosed queue takes only while active whatever
  its counts (`World.enclosedQueue_taking`) and dissipates step by step
  (`World.enclosedQueue_dissipatesOn`).
* **Counting under each selection, in finite worlds.** Every step of a finite world is
  enclosed (`World.Finite.enclosed`), so there dissipation with balance and embodiment
  binds counting by itself. Under each selection the laws of counting in finite worlds are
  those of a tally with at most some number active at each step, and two more where
  selected (`World.finite_counting_under`): nothing arising across a step at which nothing
  is active, exactly where balance and embodiment are selected with only active relata
  giving or with dissipation (`World.finite_counting_binds_iff`), and a change bound from
  the first step, exactly where balance, embodiment and dissipation are selected
  (`World.finite_change_bound_iff`). So the 256 selections give three kinds of law. Finite
  worlds and worlds enclosed from some step on have the same laws under a selection exactly
  when it bounds change and binds counting (`World.enclosed_iff_finite_counting_under`).
  The witnesses seat a queue round a ring of places, each member at the next place in turn
  (`Ring.slot`), so that those in the queue before or after any step hold distinct places
  and the ring counts what the queue counts (`Ring.slot_inj`, `Ring.counts`). With nothing
  standing, a ring meets every premise but embodiment (`World.ring_meets`); with each place
  standing while held, every premise but balance (`World.embodiedRing_meets`); with the
  front's place also taking what each place's standing loses and giving what it gains, every
  premise but dissipation, only active relata giving where nothing joins an empty queue
  (`World.balancedRing_meets`).

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

/-- What a mapped list holds is the value of some member. -/
theorem exists_of_mem_map {β : Type} {g : α → β} {b : β} :
    ∀ {l : List α}, b ∈ l.map g → ∃ a, a ∈ l ∧ g a = b
  | [], mem => nomatch mem
  | a :: _, mem => match mem_cons_cases mem with
    | .inl same => ⟨a, .head _, same.symm⟩
    | .inr mem => match exists_of_mem_map mem with
      | ⟨x, listed, same⟩ => ⟨x, .tail a listed, same⟩

/-- Mapping a list one to one on its members keeps it without repetition. -/
theorem distinct_map_on {β : Type} {g : α → β} :
    ∀ {l : List α}, (∀ a b, a ∈ l → b ∈ l → g a = g b → a = b) → Distinct l →
      Distinct (l.map g)
  | [], _, _ => trivial
  | a :: l, inj, ⟨fresh, distinct⟩ =>
    ⟨fun mem => match exists_of_mem_map mem with
      | ⟨b, listed, same⟩ => fresh (Eq.subst (motive := (· ∈ l))
          (inj b a (.tail a listed) (.head l) same) listed),
     distinct_map_on (fun x y first second => inj x y (.tail a first) (.tail a second))
       distinct⟩

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

/-- The flow exchanges at arbitrarily late steps: some formation taking part takes or gives
something. -/
def Flow.ExchangeRecurs (L : Flow F C) : Prop :=
  ∀ N, ∃ t f c, N ≤ t ∧ f ∈ L.present t ∧ (0 < L.take t f c ∨ 0 < L.give t f c)

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

/-- Across a step enclosed around what stands, a formation taking part that takes or gives
anything lowers the total standing: the enclosing family holds what it exchanges, and
under dissipation giving to it needs taking from it. -/
theorem exchange_lowers (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {t : Nat} (around : L.AroundStanding stand t) {f : F}
    {c : C} (present : f ∈ L.present t) (exchanges : 0 < L.take t f c ∨ 0 < L.give t f c) :
    W.stock (stand (t + 1)) (t + 1) < W.stock (stand t) t :=
  match around with
  | ⟨es, distinct, before, after, closed⟩ =>
    have dissipates := dissipative es t distinct closed
    have inside : ¬¬ c ∈ es := fun out => match closed f present c out with
      | ⟨noTake, noGive⟩ => match exchanges with
        | .inl takes => Nat.lt_irrefl 0 (Eq.subst (motive := fun k => 0 < k) noTake takes)
        | .inr gives => Nat.lt_irrefl 0 (Eq.subst (motive := fun k => 0 < k) noGive gives)
    have takes : 0 < total es (L.take t f) := Decidable.of_not_not fun idle => inside fun mem =>
      idle (match exchanges with
        | .inl takes => total_pos_of_mem mem takes
        | .inr gives => dissipates.takes_of_gives present (total_pos_of_mem mem gives))
    have lowers : W.stock es (t + 1) < W.stock es t :=
      Nat.lt_of_lt_of_le
        (Nat.lt_add_of_pos_right (total_pos_of_mem (q := fun f => sign (total es (L.take t f)))
          present (sign_pos takes)))
        (balances.runs_down dissipates)
    Nat.lt_of_le_of_lt (Nat.le_of_eq (census.stock_eq distinct after))
      (Nat.lt_of_lt_of_le lowers (Nat.le_of_eq (census.stock_eq distinct before).symm))

/-- The exchange comes to rest: where every step from some step on is not refuted to be
enclosed around what stands, no formation takes or gives at arbitrarily late steps. Each
such exchange lowers the total standing, which never rises across those steps. -/
theorem exchanges_finitely (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {T : Nat}
    (around : ∀ t, T ≤ t → ¬¬ L.AroundStanding stand t) : ¬ L.ExchangeRecurs :=
  fun exchanging => falls_finitely (fun t => W.stock (stand t) t) T
    (fun t later => Decidable.of_not_not fun rises => around t later fun enclosed =>
      rises (standing_never_rises balances dissipative census enclosed))
    fun N => match exchanging (N + T) with
    | ⟨t, _, _, later, present, exchanges⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
        Decidable.of_not_not fun stays =>
          around t (Nat.le_trans (Nat.le_add_left T N) later) fun enclosed =>
            stays (exchange_lowers balances dissipative census enclosed present exchanges)⟩

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

namespace Accretion

/-- The relata of `World.accretion` active at step `t`: the formations that arose before it. -/
def alive : Nat → List (Nat ⊕ Unit)
  | 0 => []
  | t + 1 => .inl t :: alive t

theorem mem_alive : ∀ {t : Nat} {x : Nat ⊕ Unit}, x ∈ alive t ↔ World.accretion.web.active t x
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

/-- At each step finitely many relata of `World.accretion` are active. -/
theorem census : World.accretion.web.Census alive :=
  fun t => ⟨alive_distinct t, fun _ => mem_alive.symm⟩

end Accretion

namespace World

/-- One way only. In `accretion`, which has a census, arising recurs while ceasing does not; in
`attrition` ceasing recurs while nothing arises, so by the census law it has no census. -/
theorem census_one_way :
    (accretion.Counted ∧ accretion.ArisingRecurs ∧ ¬ accretion.CeasingRecurs) ∧
    (attrition.CeasingRecurs ∧ ¬ attrition.ArisingRecurs ∧ ¬ attrition.Counted) :=
  match separate with
  | ⟨⟨arising, quiet, _⟩, ⟨ceasing, still, _⟩⟩ =>
    ⟨⟨⟨Accretion.alive, Accretion.census⟩, arising, quiet⟩,
     ⟨ceasing, still, fun counted => still (arising_of_ceasing counted ceasing)⟩⟩

/-- `accretion` has a census but no bound on it: arising recurs there while ceasing does not. -/
theorem accretion_unbounded (B : Nat) : ¬ accretion.CountedWithin B :=
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

end World

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

/-- The rest theorem needs its census of activity: in `attrition` nothing stands and nothing
takes part, so every other premise holds, every step is enclosed around what stands, and
ceasing recurs. -/
theorem rest_needs_census :
    attrition.web.StandingCensus (fun _ => []) ∧ attrition.ArisingEmbodied ∧ attrition.Balanced ∧
    attrition.Dissipative ∧ (∀ t, attrition.flow.AroundStanding (fun _ => []) t) ∧
    attrition.CeasingRecurs ∧ ¬ attrition.Counted :=
  ⟨fun _ => ⟨trivial, fun x => match x with
      | .inl _ => ⟨fun standing => absurd standing (Nat.lt_irrefl 0), fun mem => (nomatch mem)⟩
      | .inr _ => ⟨fun standing => absurd standing (Nat.lt_irrefl 0), fun mem => (nomatch mem)⟩⟩,
   fun t x arises => match x, arises with
      | .inl f, arises => absurd arises (Attrition.nothing_arises t f)
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

namespace Few

/-- `[t]` where `b`, and `l` otherwise. -/
def pick : Bool → Nat → List Nat → List Nat
  | true, t, _ => [t]
  | false, _, l => l

variable (s : Nat → Bool)

/-- The first `true` of `s`, once it has passed. -/
def found : Nat → List Nat
  | 0 => []
  | t + 1 => pick (clear s t && s t) t (found t)

/-- Holding at `t`: being the first `true` of `s`, before `t`. -/
abbrev passed (a t : Nat) : Prop :=
  a < t ∧ clear s a = true ∧ s a = true

theorem distinct_pick : ∀ (b : Bool) (t : Nat) {l : List Nat}, Distinct l →
    Distinct (pick b t l)
  | true, _, _, _ => ⟨fun no => (nomatch no), trivial⟩
  | false, _, _, distinct => distinct

theorem distinct_found : ∀ t, Distinct (found s t)
  | 0 => trivial
  | t + 1 => distinct_pick (clear s t && s t) t (distinct_found t)

theorem mem_pick (t a : Nat) : ∀ b : Bool, (clear s t && s t) = b →
    (passed s a t ↔ a ∈ found s t) → (passed s a (t + 1) ↔ a ∈ pick b t (found s t))
  | true, first, _ =>
    ⟨fun ⟨_, c, yes⟩ => Eq.subst (motive := fun x => x ∈ [t])
        (Clear.first_unique s (Clear.and_left first) (Clear.and_right first) c yes) (.head []),
     fun mem => match mem_cons_cases mem with
      | .inl same => Eq.subst (motive := fun x => passed s x (t + 1)) same.symm
          ⟨Nat.lt_succ_self t, Clear.and_left first, Clear.and_right first⟩
      | .inr no => nomatch no⟩
  | false, notFirst, before =>
    ⟨fun ⟨lt, c, yes⟩ => before.mp ⟨match Nat.lt_or_ge a t with
        | .inl earlier => earlier
        | .inr ge => (Clear.not_both notFirst
            (Eq.subst (motive := fun x => (clear s x && s x) = true)
              (Nat.le_antisymm (Nat.le_of_lt_succ lt) ge) (Clear.and_both _ _ c yes))).elim,
        c, yes⟩,
     fun mem => match before.mpr mem with
      | ⟨lt, c, yes⟩ => ⟨Nat.lt_succ_of_lt lt, c, yes⟩⟩

theorem mem_found : ∀ t a, passed s a t ↔ a ∈ found s t
  | 0, a => ⟨fun holds => absurd holds.1 (Nat.not_lt_zero a), fun no => nomatch no⟩
  | t + 1, a => mem_pick s t a (clear s t && s t) rfl (mem_found t a)

/-- Being the first `true`, once passed, is listed at each step by at most one member. -/
theorem listed : Listed (passed s) (found s) :=
  fun t => ⟨distinct_found s t, fun a => mem_found s t a⟩

/-- What comes to hold comes to hold at its own index. -/
theorem comes_at {a t : Nat} (comes : ComesToBe (passed s a) t) : a = t :=
  match comes with
  | ⟨fails, ⟨lt, c, yes⟩⟩ => match Nat.lt_or_ge a t with
    | .inl earlier => (fails ⟨earlier, c, yes⟩).elim
    | .inr ge => Nat.le_antisymm (Nat.le_of_lt_succ lt) ge

/-- Coming to hold happens at most once. -/
theorem quiet : ¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (passed s a) t :=
  fun all => match all 0 with
  | ⟨t₀, _, _, c₀⟩ => match all (t₀ + 1) with
    | ⟨_, _, later, c₁⟩ =>
      Nat.not_succ_le_self t₀ (Nat.le_trans later (Nat.le_of_eq
        (((comes_at s c₁).symm.trans
          (Clear.first_unique s c₁.2.2.1 c₁.2.2.2 c₀.2.2.1 c₀.2.2.2)).trans (comes_at s c₀))))

end Few

/-- `few_of_quiet` cannot be strengthened to a list holding every member that ever holds
without omniscience: if every determination decided and listed at each step, whose coming
to hold does not recur, had such a list, `LPO` would hold, even where at most one member is
listed at each step and coming to hold happens at most once (`Few`; the twelfth review's
probe). -/
theorem Listed.lpo_of_few
    (few : ∀ (p : Nat → Nat → Prop) (l : Nat → List Nat), (∀ a t, Decidable (p a t)) →
      Listed p l → (¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) →
      ∃ L : List Nat, ∀ t a, p a t → a ∈ L) :
    LPO := fun s =>
  match few (Few.passed s) (Few.found s) (fun _ _ => inferInstance) (Few.listed s)
      (Few.quiet s) with
  | ⟨L, covers⟩ => match Clear.or_first s (beyond L) with
    | .inr ⟨m, _, _, yes⟩ => .inl ⟨m, yes⟩
    | .inl c => .inr fun n => Clear.false_of_not (s n) fun yes =>
      match Clear.first_of_true s yes with
      | ⟨m, cm, ym⟩ => Clear.not_both
          (Clear.false_before s c (lt_beyond (covers (m + 1) m ⟨Nat.lt_succ_self m, cm, ym⟩))) ym

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

/-- In such a world the exchange comes to rest as well: no relatum takes or gives at
arbitrarily late steps (`Flow.exchanges_finitely`). This needs only the census of what
stands, balance, dissipation and enclosure, not a census of activity or embodiment. -/
theorem exchange_stops {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (around : ∀ t, T ≤ t → ¬¬ w.flow.AroundStanding stand t) : ¬ w.flow.ExchangeRecurs :=
  Flow.exchanges_finitely balanced dissipative standing around

end World

/-! ## Openness cannot be dropped -/

namespace Exposed

inductive Relatum where
  | side (b : Bool)
  | ground (n : Nat)

/-- The sides stand as in `Shuttle`; the ground relata stand at nothing. -/
def level (t : Nat) : Relatum → Nat
  | .side b => Shuttle.stands b t
  | .ground _ => 0

/-- Across every step the side holding the standing hands it to the other, as in
`Shuttle`, and takes a unit from each ground relatum and gives it back. -/
def flow : Flow Relatum Relatum where
  present t := [.side (Shuttle.holder t)]
  take t x y := match x, y with
    | .side b, .side c => Shuttle.flow.take t b c
    | .side _, .ground _ => 1
    | .ground _, .side _ => 0
    | .ground _, .ground _ => 0
  give t x y := match x, y with
    | .side b, .side c => Shuttle.flow.give t b c
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
    (closed (.side (Shuttle.holder t)) (.head _) _ (outside cs)).1.symm

/-- A side stands exactly when it holds the standing. -/
theorem stands_iff : ∀ (b : Bool) (t : Nat), 0 < Shuttle.stands b t ↔ b = Shuttle.holder t
  | true, 0 => ⟨fun _ => rfl, fun _ => Nat.zero_lt_one⟩
  | false, 0 => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => Bool.noConfusion no⟩
  | true, 1 => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => Bool.noConfusion no⟩
  | false, 1 => ⟨fun _ => rfl, fun _ => Nat.zero_lt_one⟩
  | true, t + 2 => stands_iff true t
  | false, t + 2 => stands_iff false t

/-- The side holding the standing is the one active relatum. -/
theorem census : web.Census fun t => [.side (Shuttle.holder t)] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side b => ⟨fun standing => Eq.subst
          (motive := fun c => Relatum.side c ∈ [Relatum.side (Shuttle.holder t)])
          ((stands_iff b t).mp standing).symm (.head _),
        fun mem => (stands_iff b t).mpr (match mem_cons_cases mem with
          | .inl same => congrArg sideOf same
          | .inr no => nomatch no)⟩
    | .ground n => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Relatum.ground n ∈ [Relatum.side (Shuttle.holder t)]) => match mem with
          | .tail _ no => (nomatch no)⟩⟩

/-- The holder stands at one. -/
theorem holder_one : ∀ t, Shuttle.stands (Shuttle.holder t) t = 1
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (Shuttle.stands_two (Shuttle.holder t) t).trans (holder_one t)

/-- And stands at nothing after the step. -/
theorem holder_after : ∀ t, Shuttle.stands (Shuttle.holder t) (t + 1) = 0
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (Shuttle.stands_two (Shuttle.holder t) (t + 1)).trans (holder_after t)

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

/-- The sides of `Shuttle` exchanging with an unbounded ground. -/
def exposed : World :=
  ⟨Exposed.Relatum, Exposed.flow, Exposed.web⟩

/-- `exposed` meets all eight premises and arising recurs in it: no step is enclosed, so
dissipation binds at none. -/
theorem exposed_world :
    exposed.Premised ∧ exposed.ArisingRecurs ∧ ∀ t, ¬ exposed.flow.Enclosed t :=
  ⟨.of (fun _ _ _ _ no => no.elim)
     (fun t c => match c with
      | .side c => Shuttle.balances t c
      | .ground _ => rfl)
     (fun t f _ present _ => match f, present with
      | _, .head _ => Shuttle.holder_stands t
      | _, .tail _ no => (nomatch no))
     (fun t f _ present _ => match f, present with
      | _, .head _ => ⟨Shuttle.holder_stands t, trivial⟩
      | _, .tail _ no => (nomatch no))
     (fun cs t distinct closed => absurd ⟨cs, distinct, closed⟩ (Exposed.open_at t))
     (fun _ _ => Iff.rfl) ⟨_, Exposed.census⟩ ⟨0, fun _ _ _ _ _ no => no.elim⟩,
   fun N => match Shuttle.recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩,
   Exposed.open_at⟩

/-- What stands in `exposed` is listed, the holder alone: the total standing is one at every
step, and the holder falls across every step. The world is not finite; what is unbounded
is the number of relata it exchanges with, each standing at nothing (the tenth review's
probe). -/
theorem exposed_standing :
    exposed.web.StandingCensus (fun t => [Exposed.Relatum.side (Shuttle.holder t)]) ∧
    (∀ t, exposed.web.stock [Exposed.Relatum.side (Shuttle.holder t)] t = 1) ∧
    (∀ t, exposed.web.Falls t (Exposed.Relatum.side (Shuttle.holder t))) ∧
    ¬ exposed.Finite :=
  ⟨standingCensus Exposed.census fun _ _ => Iff.rfl,
   fun t => show Shuttle.stands (Shuttle.holder t) t + 0 = 1 from Exposed.holder_one t,
   fun t => show Shuttle.stands (Shuttle.holder t) (t + 1) < Shuttle.stands (Shuttle.holder t) t
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
probe). Under a census, with every relatum embodied, balance and dissipation, openness is
necessary for arising without end (`arising_opens`), not sufficient. With only whatever
arises embodied it is not necessary: `throughput` is enclosed at every step and arises
without end (`rest_needs_standing`). -/
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

namespace Throughput

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
theorem census : web.Census fun t => [Relatum.side (Shuttle.holder t)] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side b => ⟨fun active => Eq.subst
          (motive := fun c => Relatum.side c ∈ [Relatum.side (Shuttle.holder t)])
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

end Throughput

namespace EmbodiedThroughput

/-- `Throughput`'s levels, each relatum active exactly while it stands, and no dependence. -/
def web : Web Throughput.Relatum Throughput.Relatum where
  level := Throughput.web.level
  active t c := 0 < Throughput.web.level t c
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end EmbodiedThroughput

namespace World

/-- `Throughput`'s flow with every relatum active while it stands (the tenth review's
probe). -/
def embodiedThroughput : World :=
  ⟨Throughput.Relatum, Throughput.flow, EmbodiedThroughput.web⟩

/-- The rest theorem needs its census of what stands. In `throughput` what is active is
listed, whatever arises is embodied, the flow balances and dissipates, and every step is
enclosed around both sides, every relatum ever active; arising recurs, and what stands
cannot be listed, since every unburnt fuel stands. In `embodiedThroughput`, the same flow with every
relatum embodied, every step is enclosed and arising recurs; nothing active can be
listed (the tenth review's probes). -/
theorem rest_needs_standing :
    (throughput.Counted ∧ throughput.ArisingEmbodied ∧ throughput.Balanced ∧
      throughput.Dissipative ∧
      (∀ t, throughput.flow.Around [Throughput.Relatum.side true, .side false] t) ∧
      throughput.ArisingRecurs ∧ ∀ stand, ¬ throughput.web.StandingCensus stand) ∧
    ((∀ t, embodiedThroughput.flow.Enclosed t) ∧ embodiedThroughput.Embodied ∧
      embodiedThroughput.Balanced ∧ embodiedThroughput.Dissipative ∧
      embodiedThroughput.ArisingRecurs ∧ ¬ embodiedThroughput.Counted) :=
  ⟨⟨⟨_, Throughput.census⟩, throughput_arising, throughput_world.1, throughput_world.2.1,
    Throughput.around, throughput_world.2.2.2.1,
    fun stand census => Throughput.unlisted (stand 0) (census 0).2 Throughput.fuel_stands⟩,
   ⟨fun t => match Throughput.around t with
     | ⟨es, distinct, _, closed⟩ => ⟨es, distinct, closed⟩,
    fun _ _ => Iff.rfl, Throughput.balances, Throughput.dissipative,
    fun N => match Throughput.throughput.2.2.2.2.2 true N with
     | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩,
    fun ⟨alive, census⟩ => Throughput.unlisted (alive 0) (census 0).2 Throughput.fuel_stands⟩⟩

end World

/-! ## The exchange needs each premise -/

namespace World

/-- The exchange comes to rest only with each of its premises: in each world below every
other premise holds and the flow exchanges at arbitrarily late steps. Without enclosure:
`exposed` meets all eight premises with what stands listed, and no step is enclosed.
Without dissipation: in the cycle of `Becoming.Flow` the one condition stands throughout,
the flow balances and every step is enclosed around it. Without balance: `leaking` is
dissipative, and every step is enclosed around the side holding the standing. Without the
census of what stands: `throughput` is balanced and dissipative and every step is enclosed,
but what stands cannot be listed, so enclosure around the empty list says nothing about
it. -/
theorem exchange_needs :
    (exposed.web.StandingCensus (fun t => [Exposed.Relatum.side (Shuttle.holder t)]) ∧
      exposed.Balanced ∧ exposed.Dissipative ∧
      (∀ t, ¬ exposed.flow.AroundStanding
        (fun t => [Exposed.Relatum.side (Shuttle.holder t)]) t) ∧
      exposed.flow.ExchangeRecurs) ∧
    (Cycle.web.StandingCensus (fun _ => [()]) ∧ Cycle.flow.Balances Cycle.web ∧
      ¬ Cycle.flow.Dissipative ∧ (∀ t, Cycle.flow.AroundStanding (fun _ => [()]) t) ∧
      Cycle.flow.ExchangeRecurs) ∧
    (leaking.web.StandingCensus (fun t => [Shuttle.holder t]) ∧ ¬ leaking.Balanced ∧
      leaking.Dissipative ∧ (∀ t, leaking.flow.AroundStanding (fun t => [Shuttle.holder t]) t) ∧
      leaking.flow.ExchangeRecurs) ∧
    ((∀ stand, ¬ throughput.web.StandingCensus stand) ∧ throughput.Balanced ∧
      throughput.Dissipative ∧ (∀ t, throughput.flow.AroundStanding (fun _ => []) t) ∧
      throughput.flow.ExchangeRecurs) :=
  have takes : ∀ t (b : Bool), 0 < Shuttle.flow.take t b b := fun _ b => match b with
    | true => Nat.zero_lt_one
    | false => Nat.zero_lt_one
  ⟨⟨exposed_standing.1, exposed_world.1 _ (.tail _ (.head _)),
     exposed_world.1 _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))),
     fun t ⟨es, distinct, _, _, closed⟩ => Exposed.open_at t ⟨es, distinct, closed⟩,
     fun N => ⟨N, .side (Shuttle.holder N), .ground 0, Nat.le_refl N, .head _,
       .inl Nat.zero_lt_one⟩⟩,
   ⟨fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun c => (match c with
      | () => ⟨fun _ => .head _, fun _ => Nat.zero_lt_one⟩)⟩,
    Cycle.closed_more.1, witnesses_not_dissipative.2.1,
    fun _ => ⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun c _ => (match c with | () => .head _),
      fun c _ => (match c with | () => .head _),
      fun _ _ c outside => (match c with | () => absurd (.head _) outside)⟩,
    fun N => ⟨N + 1, N, (), Nat.le_succ N, .head _, .inl Nat.zero_lt_one⟩⟩,
   ⟨fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun b =>
      ⟨fun standing => show b ∈ [Shuttle.holder t] from
        Eq.subst (motive := fun c => c ∈ [Shuttle.holder t])
          ((Exposed.stands_iff b t).mp standing).symm (.head _),
       fun (mem : b ∈ [Shuttle.holder t]) => (Exposed.stands_iff b t).mpr (match mem with
        | .head _ => rfl
        | .tail _ no => (nomatch no))⟩⟩,
    leaking_world.2.2.2.2.1, leaking_world.2.2.1,
    fun t => ⟨[true, false], Shuttle.distinct, fun c _ => Shuttle.every c,
      fun c _ => Shuttle.every c, (leaking_world.2.2.2.2.2 t).1⟩,
    fun N => ⟨N, Shuttle.holder N, Shuttle.holder N, Nat.le_refl N, .head _,
      .inl (takes N (Shuttle.holder N))⟩⟩,
   ⟨fun stand census => Throughput.unlisted (stand 0) (census 0).2 Throughput.fuel_stands,
    throughput_world.1, throughput_world.2.1,
    fun t => match Throughput.around t with
      | ⟨es, distinct, _, closed⟩ => ⟨es, distinct, fun _ no => (nomatch no),
          fun _ no => (nomatch no), closed⟩,
    fun N => ⟨N, .side (Shuttle.holder N), .fuel N, Nat.le_refl N, .head _,
      .inl (Nat.lt_of_lt_of_le Nat.zero_lt_two
        (Nat.le_of_eq (congrArg (2 * ·) (Frontier.burning_self N)).symm))⟩⟩⟩

end World

/-! ## Counting under enclosure -/

namespace World

variable {w : World}

/-- Under a census of embodied relata, each relatum active at a step stands there, so they
number at most the total standing. -/
theorem length_le_stock {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (t : Nat) : (alive t).length ≤ w.web.stock (alive t) t :=
  Nat.le_trans (Nat.le_of_eq (total_ones (alive t)).symm) (total_le (alive t) fun x mem =>
    (embodied x t).mp (((census t).2 x).mpr mem))

/-- Enclosure bounds change. In a world with a census whose relata are embodied, with a
balanced, dissipative flow, in which every step from `T` on is enclosed, the total standing
at `T` bounds the change of the census from `T`: the relata active at any
later step, with the steps since `T` at which something arose or ceased, number at most
that total. -/
theorem enclosure_bounds_change [∀ t x, Decidable (w.web.active t x)]
    {alive : Nat → List w.Relatum} (census : w.web.Census alive) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) :
    ChangeBound T (w.web.stock (alive T) T) (fun t => (alive t).length)
      (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
      (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t) :=
  have standing := standingCensus census embodied
  fun _ later => Nat.le_trans (Nat.add_le_add_right (length_le_stock census embodied _) _)
    (falls_by_occurrences (fun t => w.web.stock (alive t) t) _ (fun t later =>
      Decidable.of_not_not fun no => (enclosed t later).aroundStanding_not_not alive
        fun around => no (match Nat.eq_zero_or_pos (ceasings (alive t)
            (fun x s => w.web.active s x) t + comings (alive (t + 1))
            (fun x s => w.web.active s x) t) with
          | .inl quiet => Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) (mark_zero
              fun positive => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le positive
                (Nat.le_of_eq quiet)))))
              (Flow.standing_never_rises balanced dissipative standing around)
          | .inr changes =>
            have lowers : ∃ x, w.web.Rises t x ∨ w.web.Falls t x :=
              match Nat.eq_zero_or_pos (ceasings (alive t) (fun x s => w.web.active s x) t) with
              | .inr ceasing => match total_pos _ ceasing with
                | ⟨x, _, ceases⟩ => ⟨x, .inr (falls_of_ceases embodied (mark_pos.mp ceases))⟩
              | .inl still => match total_pos _ (Nat.lt_of_lt_of_le changes (Nat.le_of_eq
                  ((congrArg (· + _) still).trans (Nat.zero_add _)))) with
                | ⟨x, _, comes⟩ => ⟨x, .inl (rises_of_arises embodied (mark_pos.mp comes))⟩
            match lowers with
            | ⟨_, change⟩ => Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) (mark_one changes)))
                (Flow.change_lowers balanced dissipative standing around change)))
      later)

end World

namespace EnclosedQueue

variable (n c a : Nat → Nat) (B : Nat)

/-- What stands: `B`, less one for each step at which something ceased or arose. -/
def store (t : Nat) : Nat :=
  B - occurrences 0 (fun s => c s + a s) t

/-- Standing in a queue whose front is `g` and which holds `m`: one, and `s` more at the
front. -/
def place (g m s k : Nat) : Nat :=
  if g ≤ k ∧ k < g + m then 1 + (if k = g then s else 0) else 0

/-- Members stand by their place in the queue, the front holding what the store holds
beyond one for each member. -/
def level (t k : Nat) : Nat :=
  place (Queue.gone c t) (n t) (store c a B t - n t) k

/-- Members stand and are active exactly while in the queue. -/
def web : Web Nat Nat where
  level := level n c a B
  active t k := Queue.holds n c k t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The front takes part at every step. It takes from each member what that member's
standing loses across the step and gives each what it gains. -/
def flow : Flow Nat Nat where
  present t := [Queue.gone c t]
  take t _ k := level n c a B t k - level n c a B (t + 1) k
  give t _ k := level n c a B (t + 1) k - level n c a B t k

/-- The members in the queue before or after the step from `t`. -/
def span (t : Nat) : List Nat :=
  steps (Queue.gone c t) (n t + a t)

variable {n c a : Nat → Nat} {B : Nat}

theorem place_pos {g m s k : Nat} : (g ≤ k ∧ k < g + m) ↔ 0 < place g m s k :=
  if h : g ≤ k ∧ k < g + m then
    ⟨fun _ => Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_add_right 1 _))
      (Nat.le_of_eq (if_pos h).symm), fun _ => h⟩
  else
    ⟨fun holds => absurd holds h,
     fun pos => absurd (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (if_neg h))) (Nat.lt_irrefl 0)⟩

theorem place_zero {g m s k : Nat} (out : ¬ (g ≤ k ∧ k < g + m)) : place g m s k = 0 :=
  if_neg out

/-- A queue of `m + 1` stands at `m + 1`, and `s` more at its front. -/
theorem total_place (g m s : Nat) : total (steps g (m + 1)) (place g (m + 1) s) = m + 1 + s :=
  have front : place g (m + 1) s g = 1 + s :=
    (if_pos ⟨Nat.le_refl g, Nat.lt_add_of_pos_right (Nat.succ_pos m)⟩).trans
      (congrArg (1 + ·) (if_pos rfl))
  have rest : total (steps (g + 1) m) (place g (m + 1) s) = m :=
    (total_congr_on (g := fun _ => 1) fun _ mem =>
      (if_pos ⟨Nat.le_of_succ_le (steps_mem mem), Nat.lt_of_lt_of_le (steps_within mem)
        (Nat.le_of_eq (Nat.add_right_comm g 1 m))⟩).trans
        (congrArg (1 + ·) (if_neg fun same => Nat.lt_irrefl g (Nat.lt_of_lt_of_le
          (Nat.lt_succ_self g) (Nat.le_trans (steps_mem mem) (Nat.le_of_eq same)))))).trans
      ((total_ones _).trans (steps_length _ _))
  (congrArg (· + _) front).trans ((congrArg (1 + s + ·) rest).trans
    ((Nat.add_right_comm 1 s m).trans ((congrArg (· + s) (Nat.add_comm 1 m)))))

/-- Where a member's standing does not change, the front neither takes from nor gives to
it. -/
theorem still_flows {t k f : Nat} (same : level n c a B (t + 1) k = level n c a B t k) :
    (flow n c a B).take t f k = 0 ∧ (flow n c a B).give t f k = 0 :=
  ⟨(congrArg (level n c a B t k - ·) same).trans (Nat.sub_self _),
   (congrArg (· - level n c a B t k) same).trans (Nat.sub_self _)⟩

theorem still {t k f : Nat}
    (flows : (flow n c a B).take t f k = 0 ∧ (flow n c a B).give t f k = 0) :
    ¬ (0 < (flow n c a B).take t f k ∨ 0 < (flow n c a B).give t f k)
  | .inl takes => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le takes (Nat.le_of_eq flows.1))
  | .inr gives => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le gives (Nat.le_of_eq flows.2))

/-- An empty queue stays empty where nothing joins an empty queue. -/
theorem empty_stays (tally : Tally n c a) {t : Nat} (company : 0 < a t → 0 < n t)
    (empty : n t = 0) : n (t + 1) = 0 :=
  match tally t with
  | ⟨k, before, after⟩ =>
    have kept : k = 0 := Nat.eq_zero_of_le_zero
      (Nat.le_trans (Nat.le_add_right k (c t)) (Nat.le_of_eq (before.symm.trans empty)))
    have joined : a t = 0 := eq_zero_of_not_pos fun joins =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (company joins) (Nat.le_of_eq empty))
    after.trans ((congrArg (· + a t) kept).trans ((Nat.zero_add _).trans joined))

theorem outside_empty {k t : Nat} (empty : n t = 0) : ¬ Queue.holds n c k t :=
  fun holds => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (OpenQueue.occupied holds) (Nat.le_of_eq empty))

/-- Across a step from an empty queue nothing is taken or given. -/
theorem idle (tally : Tally n c a) {t : Nat} (company : 0 < a t → 0 < n t)
    (empty : n t = 0) (k f : Nat) :
    (flow n c a B).take t f k = 0 ∧ (flow n c a B).give t f k = 0 :=
  still_flows ((place_zero (outside_empty (empty_stays tally company empty))).trans
    (place_zero (outside_empty empty)).symm)

/-- Across a step at which nothing ceases or arises nothing changes. -/
theorem quiet_same (tally : Tally n c a) {t : Nat} (quiet : c t + a t = 0) (k : Nat) :
    level n c a B (t + 1) k = level n c a B t k :=
  have ceased : c t = 0 :=
    Nat.eq_zero_of_le_zero (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq quiet))
  have joined : a t = 0 :=
    Nat.eq_zero_of_le_zero (Nat.le_trans (Nat.le_add_left _ _) (Nat.le_of_eq quiet))
  have front : Queue.gone c (t + 1) = Queue.gone c t :=
    (Queue.gone_succ t).trans (congrArg (_ + ·) ceased)
  have size : n (t + 1) = n t := match tally t with
    | ⟨_, before, after⟩ => after.trans ((congrArg (_ + ·) joined).trans
        ((congrArg (_ + ·) ceased).symm.trans before.symm))
  have kept : store c a B (t + 1) = store c a B t :=
    congrArg (B - ·) ((occurrences_succ _ (Nat.zero_le t)).trans (congrArg (_ + ·)
      (mark_zero fun changes => Nat.lt_irrefl 0
        (Nat.lt_of_lt_of_le changes (Nat.le_of_eq quiet)))))
  (congrArg (fun g => place g (n (t + 1)) (store c a B (t + 1) - n (t + 1)) k) front).trans
    ((congrArg (fun m => place (Queue.gone c t) m (store c a B (t + 1) - m) k) size).trans
      (congrArg (fun s => place (Queue.gone c t) (n t) (s - n t) k) kept))

/-- What is in the queue before or after a step lies in its span. -/
theorem within_span (tally : Tally n c a) {t k : Nat}
    (holds : Queue.holds n c k t ∨ Queue.holds n c k (t + 1)) : k ∈ span n c a t :=
  match tally t, holds with
  | _, .inl now => steps_of_within now.1
      (Nat.lt_of_lt_of_le now.2 (Nat.add_le_add_left (Nat.le_add_right _ _) _))
  | ⟨_, before, after⟩, .inr next => steps_of_within
      (Nat.le_trans (Nat.le_trans (Nat.le_add_right _ (c t))
        (Nat.le_of_eq (Queue.gone_succ t).symm)) next.1)
      (Nat.lt_of_lt_of_le next.2 (Nat.le_of_eq ((congrArg (_ + ·) after).trans
        ((Nat.add_assoc _ _ _).symm.trans ((congrArg (· + a t) (Queue.kept_end before).symm).trans
          (Nat.add_assoc _ _ _))))))

/-- Whatever the front takes from or gives to lies in the span. -/
theorem moving_within (tally : Tally n c a) {t k f : Nat}
    (moves : 0 < (flow n c a B).take t f k ∨ 0 < (flow n c a B).give t f k) :
    k ∈ span n c a t :=
  if now : Queue.holds n c k t then within_span tally (.inl now)
  else if next : Queue.holds n c k (t + 1) then within_span tally (.inr next)
  else absurd moves (still (still_flows ((place_zero next).trans (place_zero now).symm)))

/-- Each step is enclosed by its span. -/
theorem closed (tally : Tally n c a) (t : Nat) : (flow n c a B).ClosedAt (span n c a t) t :=
  fun _ _ _ out => ⟨eq_zero_of_not_pos fun takes => out (moving_within tally (.inl takes)),
    eq_zero_of_not_pos fun gives => out (moving_within tally (.inr gives))⟩

theorem span_distinct (t : Nat) : Distinct (span n c a t) :=
  steps_distinct _ _

/-- Something taken or given means the queue is not empty. -/
theorem busy (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) {t k f : Nat}
    (moves : 0 < (flow n c a B).take t f k ∨ 0 < (flow n c a B).give t f k) : 0 < n t :=
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => absurd moves (still (idle tally (company t) empty k f))
  | .inr occupied => occupied

end EnclosedQueue

namespace World

/-- An enclosed queue: its front exchanges only within the queue, and what stands falls
by one at each step at which a member joins or leaves. -/
def enclosedQueue (n c a : Nat → Nat) (B : Nat) : World :=
  ⟨Nat, EnclosedQueue.flow n c a B, EnclosedQueue.web n c a B⟩

instance enclosedQueue_decided (n c a : Nat → Nat) (B : Nat) :
    ∀ t x, Decidable ((enclosedQueue n c a B).web.active t x) :=
  fun t k => inferInstanceAs (Decidable (Queue.holds n c k t))

/-- The census of an enclosed queue is the queue. -/
theorem enclosedQueue_census (n c a : Nat → Nat) (B : Nat) :
    (enclosedQueue n c a B).web.Census (Queue.line n c) :=
  Queue.listed

theorem enclosedQueue_embodied (n c a : Nat → Nat) (B : Nat) :
    (enclosedQueue n c a B).Embodied :=
  fun _ _ => EnclosedQueue.place_pos

theorem enclosedQueue_balanced (n c a : Nat → Nat) (B : Nat) :
    (enclosedQueue n c a B).Balanced :=
  fun t k => add_sub_turn (EnclosedQueue.level n c a B t k) (EnclosedQueue.level n c a B (t + 1) k)

variable {n c a : Nat → Nat} {B : Nat}

theorem enclosedQueue_acting (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (enclosedQueue n c a B).Acting :=
  fun _ f _ present gives => match f, present, gives with
    | _, .head _, gives => OpenQueue.front.mpr (EnclosedQueue.busy tally company (.inr gives))
    | _, .tail _ no, _ => (nomatch no)

/-- Only the front takes, and only from a member in the queue, so only while it is active,
whatever the counts. -/
theorem enclosedQueue_taking (n c a : Nat → Nat) (B : Nat) : (enclosedQueue n c a B).Taking :=
  fun _ f _ present takes => match f, present, takes with
    | _, .head _, takes => ⟨OpenQueue.front.mpr (OpenQueue.occupied (EnclosedQueue.place_pos.mpr
        (Nat.lt_of_lt_of_le takes (Nat.sub_le _ _)))), trivial⟩
    | _, .tail _ no, _ => (nomatch no)

/-- Where the queue fits its store, what stands is at most the store, and is the store
while the queue is not empty. -/
theorem enclosedQueue_stock {t : Nat} (fits : n t ≤ EnclosedQueue.store c a B t) :
    (enclosedQueue n c a B).web.stock (Queue.line n c t) t ≤ EnclosedQueue.store c a B t ∧
      (0 < n t → (enclosedQueue n c a B).web.stock (Queue.line n c t) t =
        EnclosedQueue.store c a B t) :=
  have whole : ∀ m, n t = m + 1 →
      (enclosedQueue n c a B).web.stock (Queue.line n c t) t = EnclosedQueue.store c a B t :=
    fun m size =>
      (congrArg (fun k => total (steps (Queue.gone c t) k)
        (EnclosedQueue.place (Queue.gone c t) k (EnclosedQueue.store c a B t - n t))) size).trans
        ((EnclosedQueue.total_place _ m _).trans ((congrArg (· + _) size.symm).trans
          (add_sub_of_le fits)))
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => ⟨Nat.le_trans (Nat.le_of_eq
      (congrArg (fun k => total (steps (Queue.gone c t) k)
        (EnclosedQueue.place (Queue.gone c t) k (EnclosedQueue.store c a B t - n t))) empty))
      (Nat.zero_le _), fun occupied => absurd (empty ▸ occupied) (Nat.lt_irrefl 0)⟩
  | .inr occupied => ⟨Nat.le_of_eq (whole _ (Nat.succ_pred_eq_of_pos occupied).symm),
      fun _ => whole _ (Nat.succ_pred_eq_of_pos occupied).symm⟩

/-- Across a step at which nothing joins an empty queue, with the queue within its store
before and after, the enclosed queue dissipates on every closed family: where something joins
or leaves, what stands falls by one, so the front takes more than it gives. -/
theorem enclosedQueue_dissipatesOn (tally : Tally n c a) {t : Nat}
    (company : 0 < a t → 0 < n t) (fits : n t ≤ EnclosedQueue.store c a B t)
    (fits' : n (t + 1) ≤ EnclosedQueue.store c a B (t + 1)) {cs : List Nat}
    (distinct : Distinct cs) (closed : (EnclosedQueue.flow n c a B).ClosedAt cs t) :
    (EnclosedQueue.flow n c a B).DissipatesOn cs t :=
  fun f present =>
    have still : (∀ k, (EnclosedQueue.flow n c a B).take t f k = 0 ∧
        (EnclosedQueue.flow n c a B).give t f k = 0) →
        total cs ((EnclosedQueue.flow n c a B).give t f) +
          sign (total cs ((EnclosedQueue.flow n c a B).take t f)) ≤
            total cs ((EnclosedQueue.flow n c a B).take t f) := fun flows =>
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_eq_zero fun k _ => (flows k).2)).trans
        ((Nat.zero_add _).trans (congrArg sign (total_eq_zero fun k _ => (flows k).1)))))
        (Nat.zero_le _)
    match Nat.eq_zero_or_pos (n t), Nat.eq_zero_or_pos (c t + a t) with
    | .inl empty, _ => still fun k => EnclosedQueue.idle tally company empty k f
    | .inr _, .inl quiet => still fun k =>
      EnclosedQueue.still_flows (EnclosedQueue.quiet_same tally quiet k)
    | .inr occupied, .inr changes =>
      have census := enclosedQueue_census n c a B
      have standing := standingCensus census (enclosedQueue_embodied n c a B)
      have before := standing.stock_eq (EnclosedQueue.span_distinct t) fun k mem =>
        EnclosedQueue.within_span tally (.inl (((census t).2 k).mpr mem))
      have after := standing.stock_eq (t := t + 1) (EnclosedQueue.span_distinct t) fun k mem =>
        EnclosedQueue.within_span tally (.inr (((census (t + 1)).2 k).mpr mem))
      have spent : EnclosedQueue.store c a B (t + 1) + 1 ≤ EnclosedQueue.store c a B t :=
        Nat.le_of_eq ((congrArg (fun u => B - u + 1) ((occurrences_succ _ (Nat.zero_le t)).trans
          (congrArg (_ + ·) (mark_one changes)))).trans (Nat.succ_pred_eq_of_pos
            (Nat.lt_of_lt_of_le occupied fits)))
      have lowered := Nat.le_trans (Nat.add_le_add_right (Nat.le_trans (Nat.le_of_eq after.symm)
          (enclosedQueue_stock fits').1) 1)
        (Nat.le_trans spent (Nat.le_of_eq (((enclosedQueue_stock fits).2
          occupied).symm.trans before)))
      have over := (enclosedQueue_balanced n c a B).over (EnclosedQueue.span n c a t) t
      have exceeds :
          total (EnclosedQueue.span n c a t) ((EnclosedQueue.flow n c a B).give t f) + 1 ≤
            total (EnclosedQueue.span n c a t) ((EnclosedQueue.flow n c a B).take t f) :=
        le_of_add_le_add_right _ (Nat.le_trans (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
          (congrArg (_ + ·) (Nat.add_comm _ _)))) (Nat.le_trans (Nat.add_le_add_left lowered _)
            (Nat.le_of_eq ((Nat.add_comm _ _).trans (over.symm.trans (Nat.add_comm _ _))))))
      Nat.le_trans (Nat.add_le_add (total_le_of_support distinct fun _ _ gives =>
          EnclosedQueue.moving_within tally (.inr gives)) (sign_le_one _))
        (Nat.le_trans exceeds (total_le_of_support (EnclosedQueue.span_distinct t) fun k _ takes =>
          match decideMem k cs with
          | .isTrue mem => mem
          | .isFalse out => absurd (Nat.lt_of_lt_of_le takes
              (Nat.le_of_eq (closed f present k out).1)) (Nat.lt_irrefl 0)))

/-- Under a change bound from the first step the enclosed queue dissipates. -/
theorem enclosedQueue_dissipative (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (bound : ChangeBound 0 B n c a) : (enclosedQueue n c a B).Dissipative :=
  fun _ t distinct closed => enclosedQueue_dissipatesOn tally (company t)
    (RelationalRenewal.le_sub_from_add (bound t (Nat.zero_le t)))
    (RelationalRenewal.le_sub_from_add (bound (t + 1) (Nat.zero_le _))) distinct closed

/-- Under a change bound from the first step, with nothing joining an empty queue, an
enclosed queue meets all eight premises. -/
theorem enclosedQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (bound : ChangeBound 0 B n c a) : (enclosedQueue n c a B).Premised :=
  .of (fun _ _ _ _ no => (nomatch no)) (enclosedQueue_balanced n c a B)
    (enclosedQueue_acting tally company) (enclosedQueue_taking n c a B)
    (enclosedQueue_dissipative tally company bound) (enclosedQueue_embodied n c a B)
    ⟨_, enclosedQueue_census n c a B⟩ ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- Every step of an enclosed queue is enclosed. -/
theorem enclosedQueue_enclosed (tally : Tally n c a) (t : Nat) :
    (enclosedQueue n c a B).flow.Enclosed t :=
  ⟨EnclosedQueue.span n c a t, EnclosedQueue.span_distinct t, EnclosedQueue.closed tally t⟩

/-- Under all eight premises, with every step from some step on enclosed, the laws of
counting are the tally, that nothing arises across a step at which nothing is active, and a
change bound from the first step: a property of the counts holds of every census of every such
world exactly when it holds of every tally of this kind. -/
theorem enclosed_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
        (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q :=
  ⟨fun law w _ premised ⟨_, enclosed⟩ alive census =>
    law _ _ _ census.tally
      (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        alive census)
      ⟨_, (enclosure_bounds_change census
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) enclosed).from_zero⟩,
   fun law _ _ _ tally company ⟨_, bound⟩ => pointwise (Queue.counts tally)
      (law (enclosedQueue _ _ _ _) (enclosedQueue_premised tally company bound)
        ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census _ _ _ _))⟩

end World

/-! ## Counting in finite worlds -/

/-- The numbers of a list that are below `K`, as places among `K`. -/
def placesBelow (K : Nat) : List Nat → List (Fin K)
  | [] => []
  | k :: l => if h : k < K then ⟨k, h⟩ :: placesBelow K l else placesBelow K l

theorem mem_placesBelow {K : Nat} {i : Fin K} :
    ∀ {l : List Nat}, i ∈ placesBelow K l ↔ i.val ∈ l
  | [] => ⟨fun no => (nomatch no), fun no => (nomatch no)⟩
  | k :: l =>
    if h : k < K then
      have unfold : placesBelow K (k :: l) = ⟨k, h⟩ :: placesBelow K l := dif_pos h
      ⟨fun mem => match mem_cons_cases (Eq.mp (congrArg (i ∈ ·) unfold) mem) with
        | .inl same => Eq.subst (motive := fun v => v ∈ k :: l) (congrArg Fin.val same).symm
            (.head l)
        | .inr mem => .tail k (mem_placesBelow.mp mem),
       fun mem => Eq.mpr (congrArg (i ∈ ·) unfold) (match mem_cons_cases mem with
        | .inl same => Eq.subst (motive := fun j => j ∈ (⟨k, h⟩ : Fin K) :: placesBelow K l)
            (Fin.eq_of_val_eq (i := ⟨k, h⟩) (j := i) same.symm) (.head _)
        | .inr mem => .tail _ (mem_placesBelow.mpr mem))⟩
    else
      have unfold : placesBelow K (k :: l) = placesBelow K l := dif_neg h
      ⟨fun mem => .tail k (mem_placesBelow.mp (Eq.mp (congrArg (i ∈ ·) unfold) mem)),
       fun mem => Eq.mpr (congrArg (i ∈ ·) unfold) (match mem_cons_cases mem with
        | .inl same => absurd (Eq.subst (motive := fun v => v < K) same i.isLt) h
        | .inr mem => mem_placesBelow.mpr mem)⟩

theorem placesBelow_distinct {K : Nat} :
    ∀ {l : List Nat}, Distinct l → Distinct (placesBelow K l)
  | [], _ => trivial
  | k :: _, ⟨fresh, distinct⟩ =>
    if h : k < K then
      Eq.mpr (congrArg Distinct (dif_pos h))
        ⟨fun mem => fresh (mem_placesBelow.mp mem), placesBelow_distinct distinct⟩
    else Eq.mpr (congrArg Distinct (dif_neg h)) (placesBelow_distinct distinct)

/-- Over a list of numbers below `K`, a quantity on places totals what it totals on the
numbers. -/
theorem total_placesBelow {K : Nat} {q : Fin K → Nat} {g : Nat → Nat}
    (same : ∀ i, q i = g i.val) :
    ∀ {l : List Nat}, (∀ k, k ∈ l → k < K) → total (placesBelow K l) q = total l g
  | [], _ => rfl
  | k :: l, within =>
    (congrArg (fun m => total m q) (dif_pos (within k (.head l)))).trans
      ((congrArg (· + total (placesBelow K l) q) (same ⟨k, within k (.head l)⟩)).trans
        (congrArg (g k + ·) (total_placesBelow same fun j mem => within j (.tail k mem))))

/-- The `K` places, each listed once. -/
theorem places_listed (K : Nat) : ∃ all : List (Fin K), Distinct all ∧ ∀ i, i ∈ all :=
  ⟨placesBelow _ (steps 0 K), placesBelow_distinct (steps_distinct _ _),
   fun i => mem_placesBelow.mpr (steps_of_within (Nat.zero_le _)
     (Nat.lt_of_lt_of_le i.isLt (Nat.le_of_eq (Nat.zero_add _).symm)))⟩

namespace FiniteQueue

variable (n c a : Nat → Nat) (B : Nat)

/-- Room for every member a queue counting a tally whose change `B` bounds ever holds
(`ChangeBound.reach`). -/
def size : Nat := B + B * B + 1

/-- The front of the queue where it lies within the room, the first place otherwise. -/
def front (t : Nat) : Fin (size B) :=
  if h : Queue.gone c t < size B then ⟨_, h⟩ else ⟨0, Nat.succ_pos _⟩

/-- The enclosed queue's web, on the places of the room. -/
def web : Web (Fin (size B)) (Fin (size B)) where
  level t i := EnclosedQueue.level n c a B t i.val
  active t i := Queue.holds n c i.val t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The enclosed queue's flow, on the places of the room. -/
def flow : Flow (Fin (size B)) (Fin (size B)) where
  present t := [front c B t]
  take t _ i := (EnclosedQueue.flow n c a B).take t (Queue.gone c t) i.val
  give t _ i := (EnclosedQueue.flow n c a B).give t (Queue.gone c t) i.val

/-- The members in the queue at each step, as places. -/
def alive (t : Nat) : List (Fin (size B)) :=
  placesBelow (size B) (Queue.line n c t)

variable {n c a : Nat → Nat} {B : Nat}

/-- Every member the queue holds has a place. -/
theorem placed (tally : Tally n c a) (bound : ChangeBound 0 B n c a) {k t : Nat}
    (holds : Queue.holds n c k t) : k < size B :=
  Nat.lt_of_lt_of_le holds.2 (Nat.le_succ_of_le (ChangeBound.reach tally bound t))

theorem front_val (tally : Tally n c a) (bound : ChangeBound 0 B n c a) (t : Nat) :
    (front c B t).val = Queue.gone c t :=
  congrArg Fin.val (dif_pos (Nat.lt_of_le_of_lt (Nat.le_add_right _ (n t))
    (Nat.lt_succ_of_le (ChangeBound.reach tally bound t))))

end FiniteQueue

namespace World

/-- An enclosed queue on the finitely many places its members ever take. -/
def finiteQueue (n c a : Nat → Nat) (B : Nat) : World :=
  ⟨Fin (FiniteQueue.size B), FiniteQueue.flow n c a B, FiniteQueue.web n c a B⟩

instance finiteQueue_decided (n c a : Nat → Nat) (B : Nat) :
    ∀ t x, Decidable ((finiteQueue n c a B).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Queue.holds n c i.val t))

theorem finiteQueue_finite (n c a : Nat → Nat) (B : Nat) : (finiteQueue n c a B).Finite :=
  places_listed _

theorem finiteQueue_census (n c a : Nat → Nat) (B : Nat) :
    (finiteQueue n c a B).web.Census (FiniteQueue.alive n c B) :=
  fun _ => ⟨placesBelow_distinct (steps_distinct _ _), fun _ =>
    ⟨fun holds => mem_placesBelow.mpr (steps_of_within holds.1 holds.2),
     fun mem => ⟨steps_mem (mem_placesBelow.mp mem), steps_within (mem_placesBelow.mp mem)⟩⟩⟩

variable {n c a : Nat → Nat} {B : Nat}

/-- Under a change bound from the first step, its census counts what the queue counts. -/
theorem finiteQueue_counts (tally : Tally n c a) (bound : ChangeBound 0 B n c a) (t : Nat) :
    (FiniteQueue.alive n c B t).length = n t ∧
      ceasings (FiniteQueue.alive n c B t)
        (fun x s => (finiteQueue n c a B).web.active s x) t = c t ∧
      comings (FiniteQueue.alive n c B (t + 1))
        (fun x s => (finiteQueue n c a B).web.active s x) t = a t :=
  have within : ∀ s k, k ∈ Queue.line n c s → k < FiniteQueue.size B := fun _ _ mem =>
    FiniteQueue.placed tally bound ⟨steps_mem mem, steps_within mem⟩
  ⟨(total_ones _).symm.trans ((total_placesBelow (g := fun _ => 1) (fun _ => rfl)
      (within t)).trans ((total_ones _).trans (steps_length _ _))),
   (total_placesBelow (fun _ => rfl) (within t)).trans (Queue.ceasings_eq tally t),
   (total_placesBelow (fun _ => rfl) (within (t + 1))).trans (Queue.comings_eq tally t)⟩

/-- Under a change bound from the first step, with nothing joining an empty queue, the
finite queue meets all eight premises: it dissipates as the enclosed queue does. -/
theorem finiteQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (bound : ChangeBound 0 B n c a) : (finiteQueue n c a B).Premised :=
  have active : ∀ {t : Nat}, 0 < n t →
      (finiteQueue n c a B).web.active t (FiniteQueue.front c B t) :=
    fun occupied => Eq.subst (motive := fun v => Queue.holds n c v _)
      (FiniteQueue.front_val tally bound _).symm (OpenQueue.front.mpr occupied)
  .of (fun _ _ _ _ no => (nomatch no))
    (fun t i => enclosedQueue_balanced n c a B t i.val)
    (fun _ f _ present gives => match f, present, gives with
      | _, .head _, gives => active (EnclosedQueue.busy (f := 0) tally company (.inr gives))
      | _, .tail _ no, _ => (nomatch no))
    (fun _ f _ present takes => match f, present, takes with
      | _, .head _, takes => ⟨active (EnclosedQueue.busy (f := 0) tally company (.inl takes)),
          trivial⟩
      | _, .tail _ no, _ => (nomatch no))
    (fun cs t distinct closed f present =>
      have dissipates := enclosedQueue_dissipative tally company bound
        (cs.map Fin.val) t (distinct_map (fun _ _ same => Fin.eq_of_val_eq same) distinct)
        (fun _ _ (k : Nat) out =>
          if h : k < FiniteQueue.size B then
            closed f present ⟨k, h⟩ fun mem => out (mem_map_of (g := Fin.val) mem)
          else EnclosedQueue.still_flows
            ((EnclosedQueue.place_zero fun holds => h (FiniteQueue.placed tally bound holds)).trans
              (EnclosedQueue.place_zero fun holds =>
                h (FiniteQueue.placed tally bound holds)).symm))
        (Queue.gone c t) (.head _)
      have gives : total (cs.map Fin.val) ((EnclosedQueue.flow n c a B).give t (Queue.gone c t)) =
          total cs ((FiniteQueue.flow n c a B).give t f) := total_map _ _ cs
      have takes : total (cs.map Fin.val) ((EnclosedQueue.flow n c a B).take t (Queue.gone c t)) =
          total cs ((FiniteQueue.flow n c a B).take t f) := total_map _ _ cs
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) gives.symm).trans
          (congrArg (fun k => _ + sign k) takes.symm)))
        (Nat.le_trans dissipates (Nat.le_of_eq takes)))
    (fun _ _ => EnclosedQueue.place_pos)
    ⟨_, finiteQueue_census _ _ _ _⟩
    ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- Under all eight premises, in a finite world, the laws of counting are those under
enclosure from some step on: the tally, that nothing arises across a step at which nothing
is active, and a change bound from the first step. -/
theorem finite_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
        w.CountsObey Q :=
  ⟨fun law w _ premised finite => (enclosed_counting pointwise).mp law w premised
      ⟨0, fun t _ => finite.enclosed t⟩,
   fun law _ _ _ tally company ⟨_, bound⟩ => pointwise (finiteQueue_counts tally bound)
      (law (finiteQueue _ _ _ _) (finiteQueue_premised tally company bound)
        (finiteQueue_finite _ _ _ _) _ (finiteQueue_census _ _ _ _))⟩

/-- So under the eight premises, worlds enclosed from some step on and finite worlds have
the same laws of counting (the thirteenth review's probe). -/
theorem enclosed_iff_finite_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
        w.CountsObey Q :=
  (enclosed_counting pointwise).symm.trans (finite_counting pointwise)

/-- One member replaced across the first step, in a finite queue. -/
abbrev replaced : World :=
  finiteQueue (fun _ => 1) (Swap.change fun _ => true) (Swap.change fun _ => true) 2

/-- In the finite queue dissipation binds: where one member is replaced across the first
step, the front takes two units from the family of all places. -/
theorem finite_dissipation_binds :
    ∃ cs t f, Distinct cs ∧ replaced.flow.ClosedAt cs t ∧ f ∈ replaced.flow.present t ∧
      0 < total cs (replaced.flow.take t f) :=
  have takes : replaced.flow.take 0 (FiniteQueue.front (Swap.change fun _ => true) 2 0)
      ⟨0, Nat.succ_pos _⟩ = 2 := rfl
  match finiteQueue_finite (fun _ => 1) (Swap.change fun _ => true)
      (Swap.change fun _ => true) 2 with
  | ⟨all, distinct, every⟩ =>
    ⟨all, 0, FiniteQueue.front (Swap.change fun _ => true) 2 0, distinct,
     fun _ _ x out => absurd (every x) out, .head _,
     Nat.lt_of_lt_of_le Nat.zero_lt_two (Nat.le_trans (Nat.le_of_eq takes.symm)
       (le_total_of_mem (every ⟨0, Nat.succ_pos _⟩)))⟩

/-- And the bound of `enclosure_bounds_change` is attained there: what stands at the first step
totals two, and from the next step on one member is active with one step of change behind
it. -/
theorem replaced_attains :
    replaced.web.stock (FiniteQueue.alive (fun _ => 1) (Swap.change fun _ => true) 2 0) 0 = 2 ∧
      ∀ t, (FiniteQueue.alive (fun _ => 1) (Swap.change fun _ => true) 2 (t + 1)).length +
        occurrences 0 (fun u => Swap.change (fun _ => true) u + Swap.change (fun _ => true) u)
          (t + 1) = 2 :=
  ⟨rfl, fun t => (congrArg (· + _) (finiteQueue_counts (Swap.tally fun _ => true)
      (Swap.change_bound fun _ => true) (t + 1)).1).trans (congrArg (1 + ·)
        ((congrArg (_ + ·) (mark_zero fun c => Bool.noConfusion (Clear.and_right c))).symm.trans
          (Swap.counted (fun _ => true) (t + 1))))⟩

/-- That arising does not recur in a finite world meeting the eight premises
(`premised_rests`) cannot be strengthened to a step after which nothing arises without
omniscience: if every such world whose activity is decided had one, `LPO` would hold, even
where one member is active throughout and replaced at most once (`Swap`; the thirteenth
review's probe). -/
theorem lpo_of_finite_ends
    (ends : ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
      ∃ E, ∀ t x, E ≤ t → ¬ w.web.Arises t x) : LPO := fun s =>
  match ends (finiteQueue (fun _ => 1) (Swap.change s) (Swap.change s) 2)
      (finiteQueue_premised (Swap.tally s) (fun _ _ => Nat.zero_lt_one) (Swap.change_bound s))
      (finiteQueue_finite _ _ _ _) with
  | ⟨E, quiet⟩ => Swap.decide_of_end s (E := E) fun m ge c yes =>
    match total_pos _ (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        ((Swap.at_first s c yes).symm.trans
          (finiteQueue_counts (Swap.tally s) (Swap.change_bound s) m).2.2.symm))) with
    | ⟨x, _, arises⟩ => quiet m x ge (mark_pos.mp arises)

end World

/-! ## Counting under each set of premises, with enclosure -/

/-- The enclosed queue's flow opened before step `T`: there every relatum also exchanges one
unit each way with the front, so no family is closed across a step before `T`. -/
def EnclosedQueue.closing (n c a : Nat → Nat) (B T : Nat) : Flow Nat Nat where
  present t := [Queue.gone c t]
  take t f k := (EnclosedQueue.flow n c a B).take t f k + mark (t < T)
  give t f k := (EnclosedQueue.flow n c a B).give t f k + mark (t < T)

namespace World

/-- An enclosed queue closing at step `T`: before `T` every relatum also exchanges one unit
each way with the front. -/
def closingQueue (n c a : Nat → Nat) (B T : Nat) : World :=
  ⟨Nat, EnclosedQueue.closing n c a B T, EnclosedQueue.web n c a B⟩

instance closingQueue_decided (n c a : Nat → Nat) (B T : Nat) :
    ∀ t x, Decidable ((closingQueue n c a B T).web.active t x) :=
  enclosedQueue_decided n c a B

variable {n c a : Nat → Nat} {B T : Nat}

theorem closingQueue_balanced (n c a : Nat → Nat) (B T : Nat) :
    (closingQueue n c a B T).Balanced :=
  fun t k =>
    show EnclosedQueue.level n c a B (t + 1) k + (EnclosedQueue.level n c a B t k -
        EnclosedQueue.level n c a B (t + 1) k + mark (t < T)) =
      EnclosedQueue.level n c a B t k + (EnclosedQueue.level n c a B (t + 1) k -
        EnclosedQueue.level n c a B t k + mark (t < T)) from
    (Nat.add_assoc _ _ _).symm.trans ((congrArg (· + mark (t < T))
      (add_sub_turn (EnclosedQueue.level n c a B t k)
        (EnclosedQueue.level n c a B (t + 1) k))).trans (Nat.add_assoc _ _ _))

/-- From step `T` on, the closing queue's flow is the enclosed queue's. -/
theorem closing_flows {t : Nat} (later : T ≤ t) (f k : Nat) :
    (EnclosedQueue.closing n c a B T).take t f k = (EnclosedQueue.flow n c a B).take t f k ∧
      (EnclosedQueue.closing n c a B T).give t f k = (EnclosedQueue.flow n c a B).give t f k :=
  have opened : mark (t < T) = 0 := mark_zero (Nat.not_lt_of_le later)
  ⟨congrArg (_ + ·) opened, congrArg (_ + ·) opened⟩

/-- Every step from `T` on is enclosed by its span. -/
theorem closingQueue_enclosed (tally : Tally n c a) {t : Nat} (later : T ≤ t) :
    (closingQueue n c a B T).flow.Enclosed t :=
  ⟨EnclosedQueue.span n c a t, EnclosedQueue.span_distinct t, fun f present k out =>
    match EnclosedQueue.closed (B := B) tally t f present k out with
    | ⟨takes, gives⟩ => ⟨(closing_flows later f k).1.trans takes,
        (closing_flows later f k).2.trans gives⟩⟩

/-- With a change bound from step `T`, nothing joining an empty queue from `T` on, the
closing queue dissipates: before `T` no family is closed, and from `T` on it dissipates as
the enclosed queue does, its store larger by `T`. -/
theorem closingQueue_dissipative (tally : Tally n c a) {K : Nat} (bound : ChangeBound T K n c a)
    (company : ∀ t, T ≤ t → 0 < a t → 0 < n t) : (closingQueue n c a (K + T) T).Dissipative :=
  fun cs t distinct closed f present => match Nat.lt_or_ge t T with
  | .inl early => absurd (closed f present (beyond cs) (beyond_not_mem cs)).2
      fun nothing => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
        (mark_pos.mpr early) (Nat.le_add_left _ _)) (Nat.le_of_eq nothing))
  | .inr later =>
    have fits : ∀ s, T ≤ s → n s ≤ EnclosedQueue.store c a (K + T) s := fun s later =>
      RelationalRenewal.le_sub_from_add (Nat.le_trans (Nat.add_le_add_left
        (occurrences_zero_le _ s) _) (Nat.le_trans (Nat.le_of_eq (Nat.add_assoc _ _ _).symm)
          (Nat.add_le_add_right (bound s later) T)))
    have takes : total cs ((EnclosedQueue.closing n c a (K + T) T).take t f) =
        total cs ((EnclosedQueue.flow n c a (K + T)).take t f) :=
      total_congr (fun k => (closing_flows later f k).1) cs
    have gives : total cs ((EnclosedQueue.closing n c a (K + T) T).give t f) =
        total cs ((EnclosedQueue.flow n c a (K + T)).give t f) :=
      total_congr (fun k => (closing_flows later f k).2) cs
    Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) gives).trans
        (congrArg (fun u => _ + sign u) takes)))
      (Nat.le_trans (enclosedQueue_dissipatesOn tally (company t later) (fits t later)
          (fits (t + 1) (Nat.le_succ_of_le later)) distinct
          (fun g present k out => match closed g present k out with
            | ⟨took, gave⟩ => ⟨(closing_flows later g k).1.symm.trans took,
                (closing_flows later g k).2.symm.trans gave⟩) f present)
        (Nat.le_of_eq takes.symm))

/-- A selection bounds change under enclosure when it selects balance, embodiment and
dissipation. -/
def BoundsChange (S : Premise → Bool) : Prop :=
  S .balanced = true ∧ S .embodied = true ∧ S .dissipative = true

/-- Where nothing takes part, every step is enclosed. -/
theorem still_enclosed (w : World) (still : ∀ t, w.flow.present t = []) (t : Nat) :
    w.flow.Enclosed t :=
  ⟨[], trivial, fun _ present => nomatch (still t) ▸ present⟩

/-- The laws of counting under each selection of the premises, in worlds enclosed from some
step on. A property of the counts holds of every census of every such world meeting the
selection exactly when it holds of every tally that meets two conditions: where the selection
binds counting, nothing arises across a step at which nothing is active; where it bounds
change, from some step `T` on change stays within a bound and nothing arises across a step at
which nothing is active. The second condition carries its step: that change does not recur
within the bound (`ChangeBound.not_recurring`) gives no such step by itself. -/
theorem enclosed_counting_under (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ T B, ChangeBound T B n c a ∧ ∀ t, T ≤ t → 0 < a t → 0 < n t) →
        Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
        (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q :=
  ⟨fun law w _ meets ⟨T, enclosed⟩ alive census => law _ _ _ census.tally
    (fun ⟨balanced, embodied, giving⟩ => match giving with
      | .inl acting => counting_binds_jointly.1 w (meets _ balanced) (meets _ acting)
          (Embodied.arising (meets _ embodied)) alive census
      | .inr ⟨taking, dissipative⟩ => taking_binds_counting w (meets _ balanced)
          (meets _ taking) (meets _ dissipative) (meets _ embodied) alive census)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨T, _, enclosure_bounds_change census
      (meets _ embodied) (meets _ balanced) (meets _ dissipative) enclosed,
      fun t later arising => enclosed_binds_counting w (meets _ balanced) (meets _ dissipative)
        (meets _ embodied) census (enclosed t later) arising⟩),
   fun law n c a tally quiet bounded =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => pointwise (Queue.counts tally) (law (embodiedQueue n c)
        (embodiedQueue_meets n c hb) ⟨0, fun t _ => still_enclosed _ (fun _ => rfl) t⟩ _
        Queue.listed)
    | true, false => pointwise (Queue.counts tally) (law (queue n c) (queue_meets n c he)
        ⟨0, fun t _ => still_enclosed _ (fun _ => rfl) t⟩ _ Queue.listed)
    | true, true => match hd : S .dissipative, ha : S .acting, ht : S .taking with
      | false, _, _ => pointwise (Queue.counts tally) (law (enclosedQueue n c a 0)
          (fun
            | .dependent, _ => fun _ _ _ _ no => (nomatch no)
            | .balanced, _ => enclosedQueue_balanced n c a 0
            | .acting, selected => enclosedQueue_acting tally (quiet ⟨hb, he, .inl selected⟩)
            | .taking, _ => enclosedQueue_taking n c a 0
            | .dissipative, selected => nomatch hd.symm.trans selected
            | .embodied, _ => enclosedQueue_embodied n c a 0
            | .counted, _ => ⟨_, enclosedQueue_census n c a 0⟩
            | .transmitting, _ => ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩)
          ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census n c a 0))
      | true, true, _ => match bounded ⟨hb, he, hd⟩ with
        | ⟨_, _, bound, _⟩ => pointwise (Queue.counts tally) (law (enclosedQueue n c a _)
            ((enclosedQueue_premised tally (quiet ⟨hb, he, .inl ha⟩) bound.from_zero).meets S)
            ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census n c a _))
      | true, false, true => match bounded ⟨hb, he, hd⟩ with
        | ⟨_, _, bound, _⟩ => pointwise (Queue.counts tally) (law (enclosedQueue n c a _)
            ((enclosedQueue_premised tally (quiet ⟨hb, he, .inr ⟨ht, hd⟩⟩)
              bound.from_zero).meets S)
            ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census n c a _))
      | true, false, false => match bounded ⟨hb, he, hd⟩ with
        | ⟨T, K, bound, company⟩ => pointwise (Queue.counts tally)
            (law (closingQueue n c a (K + T) T)
              (fun
                | .dependent, _ => fun _ _ _ _ no => (nomatch no)
                | .balanced, _ => closingQueue_balanced n c a (K + T) T
                | .acting, selected => nomatch ha.symm.trans selected
                | .taking, selected => nomatch ht.symm.trans selected
                | .dissipative, _ => closingQueue_dissipative tally bound company
                | .embodied, _ => enclosedQueue_embodied n c a (K + T)
                | .counted, _ => ⟨_, enclosedQueue_census n c a (K + T)⟩
                | .transmitting, _ => ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩)
              ⟨T, fun _ later => closingQueue_enclosed tally later⟩ _
              (enclosedQueue_census n c a (K + T)))⟩

end World

/-! ## Counting under each set of premises, in finite worlds -/

/-- Coming to be respects agreement at the step and after it. -/
theorem comesToBe_congr {p q : Nat → Prop} {t : Nat} (now : p t ↔ q t)
    (next : p (t + 1) ↔ q (t + 1)) : ComesToBe p t ↔ ComesToBe q t :=
  ⟨fun comes => ⟨fun holds => comes.1 (now.mpr holds), next.mp comes.2⟩,
   fun comes => ⟨fun holds => comes.1 (now.mp holds), next.mpr comes.2⟩⟩

/-- So does ceasing to be. -/
theorem ceasesToBe_congr {p q : Nat → Prop} {t : Nat} (now : p t ↔ q t)
    (next : p (t + 1) ↔ q (t + 1)) : CeasesToBe p t ↔ CeasesToBe q t :=
  ⟨fun ceases => ⟨now.mp ceases.1, fun holds => ceases.2 (next.mpr holds)⟩,
   fun ceases => ⟨now.mpr ceases.1, fun holds => ceases.2 (next.mp holds)⟩⟩

namespace Ring

/-- Members seated round a ring of `N` places in turn, the first at place `0`: the place of
the `k`th. -/
def slot (N : Nat) : Nat → Nat
  | 0 => 0
  | k + 1 => if slot N k + 1 < N then slot N k + 1 else 0

variable {N : Nat}

/-- The next member sits at the next place, or at the first once the ring is full. -/
theorem slot_step (N k : Nat) :
    (slot N (k + 1) = slot N k + 1 ∧ slot N k + 1 < N) ∨
      (slot N (k + 1) = 0 ∧ ¬ slot N k + 1 < N) :=
  if h : slot N k + 1 < N then .inl ⟨if_pos h, h⟩ else .inr ⟨if_neg h, h⟩

theorem slot_lt (pos : 0 < N) : ∀ k, slot N k < N
  | 0 => pos
  | k + 1 => match slot_step N k with
    | .inl ⟨same, below⟩ => Nat.lt_of_le_of_lt (Nat.le_of_eq same) below
    | .inr ⟨same, _⟩ => Nat.lt_of_le_of_lt (Nat.le_of_eq same) pos

/-- Fewer than `N` members on, the place is as many places on, or as many less a full
turn. -/
theorem slot_add (k : Nat) : ∀ {d : Nat}, d < N →
    slot N (k + d) = slot N k + d ∨ slot N (k + d) + N = slot N k + d
  | 0, _ => .inl rfl
  | d + 1, short =>
    have pos : 0 < N := Nat.lt_of_le_of_lt (Nat.zero_le _) short
    match slot_step N (k + d), slot_add k (Nat.lt_of_succ_lt short) with
    | .inl ⟨same, _⟩, .inl on => .inl (same.trans (congrArg (· + 1) on))
    | .inl ⟨same, _⟩, .inr round => .inr ((congrArg (· + N) same).trans
        ((Nat.add_right_comm _ 1 N).trans (congrArg (· + 1) round)))
    | .inr ⟨same, full⟩, on =>
      have turned : slot N (k + d) + 1 = N :=
        Nat.le_antisymm (slot_lt pos (k + d)) ((Nat.lt_or_ge _ _).resolve_left full)
      match on with
      | .inl on => .inr ((congrArg (· + N) same).trans ((Nat.zero_add N).trans
          (turned.symm.trans (congrArg (· + 1) on))))
      | .inr round => absurd (Nat.add_lt_add (slot_lt pos k) short)
          (Nat.not_lt_of_le (Nat.le_of_eq ((congrArg (· + N) turned).symm.trans
            ((Nat.add_right_comm _ 1 N).trans (congrArg (· + 1) round)))))

/-- Members fewer than a full turn apart sit at different places. -/
theorem slot_ne (k : Nat) {d : Nat} (pos : 0 < d) (short : d < N) :
    slot N (k + d) ≠ slot N k :=
  fun same => match slot_add k short with
  | .inl on => Nat.lt_irrefl (slot N k) (Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right pos)
      (Nat.le_of_eq (on.symm.trans same)))
  | .inr round => Nat.lt_irrefl (slot N k + d) (Nat.lt_of_lt_of_le
      (Nat.add_lt_add_left short _) (Nat.le_of_eq ((congrArg (· + N) same).symm.trans round)))

/-- A member later than another, both within `L ≤ N` members from `g`, sits apart from
it. -/
theorem slot_apart {g L j k : Nat} (fits : L ≤ N) (start : g ≤ j) (before : j < k)
    (within : k < g + L) : slot N k ≠ slot N j :=
  match le_dest (Nat.le_of_lt before) with
  | ⟨_, split⟩ =>
    have ahead : j + _ < j + L := Eq.subst (motive := (· < j + L)) split
      (Nat.lt_of_lt_of_le within (Nat.add_le_add_right start L))
    fun same => slot_ne j (Nat.lt_of_add_lt_add_left (n := j)
        (Eq.subst (motive := (j + 0 < ·)) split before))
      (Nat.lt_of_lt_of_le (Nat.lt_of_add_lt_add_left ahead) fits)
      (Eq.subst (motive := fun x => slot N x = slot N j) split same)

/-- Among at most `N` members in turn, members at one place are one. -/
theorem slot_inj {g L j k : Nat} (fits : L ≤ N) (first : g ≤ j ∧ j < g + L)
    (second : g ≤ k ∧ k < g + L) (same : slot N j = slot N k) : j = k :=
  match Nat.lt_or_ge j k with
  | .inl before => absurd same.symm (slot_apart fits first.1 before second.2)
  | .inr after => match Nat.lt_or_ge k j with
    | .inl before => absurd same (slot_apart fits second.1 before first.2)
    | .inr after' => Nat.le_antisymm after' after

/-- Room for the members in a queue before or after any step, where at most `M` are in it
at each. -/
def size (M : Nat) : Nat := M + M + 1

/-- The `k`th member's place on the ring. -/
def seat (M k : Nat) : Fin (size M) :=
  ⟨slot (size M) k, slot_lt (Nat.succ_pos _) k⟩

variable (n c : Nat → Nat) (M : Nat)

/-- The places held at step `t`: the queue's members, each at its place. -/
def seated (t : Nat) : List (Fin (size M)) :=
  (Queue.line n c t).map (seat M)

/-- Place `i` is held at step `t`. -/
def holds (i : Fin (size M)) (t : Nat) : Prop :=
  i ∈ seated n c M t

instance (i : Fin (size M)) (t : Nat) : Decidable (holds n c M i t) :=
  decideMem i _

/-- The queue seated round the ring, each place standing at `level` and active while
held. -/
def web (level : Nat → Fin (size M) → Nat) : Web (Fin (size M)) (Fin (size M)) where
  level := level
  active t i := holds n c M i t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- Each place stands exactly while it is held. -/
def stands (t : Nat) (i : Fin (size M)) : Nat :=
  mark (holds n c M i t)

/-- The front's place takes part at every step. It takes from each place what that place's
standing loses across the step and gives each what it gains. -/
def flow : Flow (Fin (size M)) (Fin (size M)) where
  present t := [seat M (Queue.gone c t)]
  take t _ i := stands n c M t i - stands n c M (t + 1) i
  give t _ i := stands n c M (t + 1) i - stands n c M t i

variable {n c M} {a : Nat → Nat}

/-- A place held means the queue is not empty. -/
theorem occupied {i : Fin (size M)} {t : Nat} (held : holds n c M i t) : 0 < n t :=
  match exists_of_mem_map held with
  | ⟨_, listed, _⟩ => OpenQueue.occupied ⟨steps_mem listed, steps_within listed⟩

/-- The front's place is held while the queue is not empty. -/
theorem front_holds {t : Nat} (pos : 0 < n t) : holds n c M (seat M (Queue.gone c t)) t :=
  mem_map_of (steps_of_within (OpenQueue.front.mpr pos).1 (OpenQueue.front.mpr pos).2)

/-- Where at most `M` are in the queue at each step, those in it before or after a step fit
on the ring. -/
theorem span_fits (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) (t : Nat) :
    n t + a t ≤ size M :=
  match tally t with
  | ⟨_, _, after⟩ => Nat.le_succ_of_le (Nat.add_le_add (bounded t) (Nat.le_trans
      (Nat.le_add_left _ _) (Nat.le_trans (Nat.le_of_eq after.symm) (bounded (t + 1)))))

/-- A member in the span of the step from `t` holds its place at a step whose queue lies in
the span exactly when it is in the queue then. -/
theorem holds_iff (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) {t k s : Nat}
    (spanned : k ∈ EnclosedQueue.span n c a t)
    (inside : ∀ j, Queue.holds n c j s → j ∈ EnclosedQueue.span n c a t) :
    holds n c M (seat M k) s ↔ Queue.holds n c k s :=
  ⟨fun held => match exists_of_mem_map held with
    | ⟨j, listed, same⟩ =>
      have member : Queue.holds n c j s := ⟨steps_mem listed, steps_within listed⟩
      have there := inside j member
      Eq.subst (motive := fun x => Queue.holds n c x s)
        (slot_inj (span_fits tally bounded t) ⟨steps_mem there, steps_within there⟩
          ⟨steps_mem spanned, steps_within spanned⟩ (congrArg Fin.val same)) member,
   fun holds => mem_map_of (steps_of_within holds.1 holds.2)⟩

/-- The ring lists the places held at each step, each once. -/
theorem census (bounded : ∀ t, n t ≤ M) (level : Nat → Fin (size M) → Nat) :
    (web n c M level).Census (seated n c M) :=
  fun t => ⟨distinct_map_on (fun _ _ first second same =>
      slot_inj (Nat.le_succ_of_le (Nat.le_trans (bounded t) (Nat.le_add_right M M)))
        ⟨steps_mem first, steps_within first⟩ ⟨steps_mem second, steps_within second⟩
        (congrArg Fin.val same)) (steps_distinct _ _), fun _ => Iff.rfl⟩

/-- Where at most `M` are in the queue at each step, the ring counts what the queue
counts. -/
theorem counts (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) (t : Nat) :
    (seated n c M t).length = n t ∧ ceasings (seated n c M t) (holds n c M) t = c t ∧
      comings (seated n c M (t + 1)) (holds n c M) t = a t :=
  have now : ∀ j, Queue.holds n c j t → j ∈ EnclosedQueue.span n c a t :=
    fun _ holds => EnclosedQueue.within_span tally (.inl holds)
  have next : ∀ j, Queue.holds n c j (t + 1) → j ∈ EnclosedQueue.span n c a t :=
    fun _ holds => EnclosedQueue.within_span tally (.inr holds)
  ⟨(total_ones _).symm.trans ((total_map _ _ _).trans ((total_ones _).trans (steps_length _ _))),
   (total_map _ _ _).trans ((total_congr_on fun k listed =>
      have spanned := now k ⟨steps_mem listed, steps_within listed⟩
      mark_iff (ceasesToBe_congr (holds_iff tally bounded spanned now)
        (holds_iff tally bounded spanned next))).trans (Queue.ceasings_eq tally t)),
   (total_map _ _ _).trans ((total_congr_on fun k listed =>
      have spanned := next k ⟨steps_mem listed, steps_within listed⟩
      mark_iff (comesToBe_congr (holds_iff tally bounded spanned now)
        (holds_iff tally bounded spanned next))).trans (Queue.comings_eq tally t))⟩

/-- What the front takes from a place, the place held before the step. -/
theorem taken_held {t : Nat} {f i : Fin (size M)} (takes : 0 < (flow n c M).take t f i) :
    holds n c M i t :=
  mark_pos.mp (Nat.lt_of_lt_of_le takes (Nat.sub_le _ _))

/-- What the front gives to a place, the place held after the step. -/
theorem given_held {t : Nat} {f i : Fin (size M)} (gives : 0 < (flow n c M).give t f i) :
    holds n c M i (t + 1) :=
  mark_pos.mp (Nat.lt_of_lt_of_le gives (Nat.sub_le _ _))

end Ring

/-- From the step after it arises, the lone relatum is all there is and nothing changes. -/
theorem Queue.lone_settles : ChangeBound 1 1 Queue.lone (fun _ => 0) Queue.joins :=
  have still : ∀ t, occurrences 1 (fun s => 0 + Queue.joins s) t = 0 := fun t =>
    Nat.rec (motive := fun t => occurrences 1 (fun s => 0 + Queue.joins s) t = 0) rfl
      (fun t same => (congrArg (· + _) same).trans ((Nat.zero_add _).trans
        (mark_zero (p := 1 ≤ t ∧ 0 < 0 + Queue.joins t) fun ⟨later, pos⟩ =>
          match t, later, pos with
          | 0, later, _ => Nat.not_succ_le_zero 0 later
          | _ + 1, _, pos => Nat.lt_irrefl 0 pos))) t
  fun t later => match t, later with
  | 0, later => absurd later (Nat.not_succ_le_zero 0)
  | t + 1, _ => Nat.le_of_eq (congrArg (1 + ·) (still (t + 1)))

namespace World

/-- A queue seated round a ring of places, with nothing standing or flowing. -/
def ring (n c : Nat → Nat) (M : Nat) : World :=
  ⟨Fin (Ring.size M), Flow.still, Ring.web n c M fun _ _ => 0⟩

/-- The same ring, each place standing exactly while it is held, with nothing flowing. -/
def embodiedRing (n c : Nat → Nat) (M : Nat) : World :=
  ⟨Fin (Ring.size M), Flow.still, Ring.web n c M (Ring.stands n c M)⟩

/-- The same ring, its front's place taking what each place's standing loses and giving what
it gains. -/
def balancedRing (n c : Nat → Nat) (M : Nat) : World :=
  ⟨Fin (Ring.size M), Ring.flow n c M, Ring.web n c M (Ring.stands n c M)⟩

instance ring_decided (n c : Nat → Nat) (M : Nat) :
    ∀ t x, Decidable ((ring n c M).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Ring.holds n c M i t))

instance embodiedRing_decided (n c : Nat → Nat) (M : Nat) :
    ∀ t x, Decidable ((embodiedRing n c M).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Ring.holds n c M i t))

instance balancedRing_decided (n c : Nat → Nat) (M : Nat) :
    ∀ t x, Decidable ((balancedRing n c M).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Ring.holds n c M i t))

variable {n c a : Nat → Nat} {M : Nat}

/-- Where at most `M` are in the queue at each step, the ring meets every premise but
embodiment. -/
theorem ring_premised (bounded : ∀ t, n t ≤ M) :
    (ring n c M).Dependent ∧ (ring n c M).Balanced ∧ (ring n c M).Acting ∧
      (ring n c M).Taking ∧ (ring n c M).Dissipative ∧ (ring n c M).Counted ∧
      (ring n c M).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), fun _ _ => rfl, (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, ⟨_, Ring.census bounded _⟩, (still_vacuous _).2.2.2⟩

/-- And the embodied ring every premise but balance. -/
theorem embodiedRing_premised (bounded : ∀ t, n t ≤ M) :
    (embodiedRing n c M).Dependent ∧ (embodiedRing n c M).Acting ∧
      (embodiedRing n c M).Taking ∧ (embodiedRing n c M).Dissipative ∧
      (embodiedRing n c M).Embodied ∧ (embodiedRing n c M).Counted ∧
      (embodiedRing n c M).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, fun _ _ => mark_pos.symm, ⟨_, Ring.census bounded _⟩,
   (still_vacuous _).2.2.2⟩

/-- The balanced ring meets every premise but dissipation and only active relata giving. -/
theorem balancedRing_holds (bounded : ∀ t, n t ≤ M) :
    (balancedRing n c M).Dependent ∧ (balancedRing n c M).Balanced ∧
      (balancedRing n c M).Taking ∧ (balancedRing n c M).Embodied ∧
      (balancedRing n c M).Counted ∧ (balancedRing n c M).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no),
   fun t i => add_sub_turn (Ring.stands n c M t i) (Ring.stands n c M (t + 1) i),
   fun _ f _ present takes => match f, present, takes with
    | _, .head _, takes => ⟨Ring.front_holds (Ring.occupied
        (Ring.taken_held takes)), trivial⟩
    | _, .tail _ no, _ => (nomatch no),
   fun _ _ => mark_pos.symm, ⟨_, Ring.census bounded _⟩,
   ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩⟩

/-- Where nothing joins an empty queue, only active relata give in the balanced ring. -/
theorem balancedRing_acting (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (balancedRing n c M).Acting :=
  fun t f _ present gives => match f, present, gives with
    | _, .head _, gives => Ring.front_holds (match Nat.eq_zero_or_pos (n t) with
      | .inl empty => absurd (Ring.occupied (Ring.given_held gives)) fun pos =>
          Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq
            (EnclosedQueue.empty_stays tally (company t) empty)))
      | .inr pos => pos)
    | _, .tail _ no, _ => (nomatch no)

/-- A ring meets every selection without embodiment. -/
theorem ring_meets (bounded : ∀ t, n t ≤ M) {S : Premise → Bool} (free : S .embodied = false) :
    (ring n c M).Meets S :=
  match ring_premised bounded with
  | ⟨dependent, balanced, acting, taking, dissipative, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, _ => acting
    | .taking, _ => taking
    | .dissipative, _ => dissipative
    | .embodied, selected => nomatch free.symm.trans selected
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- An embodied ring meets every selection without balance. -/
theorem embodiedRing_meets (bounded : ∀ t, n t ≤ M) {S : Premise → Bool}
    (free : S .balanced = false) : (embodiedRing n c M).Meets S :=
  match embodiedRing_premised bounded with
  | ⟨dependent, acting, taking, dissipative, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, selected => nomatch free.symm.trans selected
    | .acting, _ => acting
    | .taking, _ => taking
    | .dissipative, _ => dissipative
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- A balanced ring meets every selection without dissipation, where it selects only active
relata giving only if nothing joins an empty queue. -/
theorem balancedRing_meets (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) {S : Premise → Bool}
    (giving : S .acting = true → ∀ t, 0 < a t → 0 < n t) (free : S .dissipative = false) :
    (balancedRing n c M).Meets S :=
  match balancedRing_holds (c := c) bounded with
  | ⟨dependent, balanced, taking, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, selected => balancedRing_acting tally (giving selected)
    | .taking, _ => taking
    | .dissipative, selected => nomatch free.symm.trans selected
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- The laws of counting under each selection of the premises, in finite worlds. A property
of the counts holds of every census of every finite world meeting the selection exactly when
it holds of every tally that meets three conditions: at most some number are active at each
step; where the selection binds counting or bounds change, nothing arises across a step at
which nothing is active; where it bounds change, change stays within a bound from the first
step. Every step of a finite world is enclosed (`Finite.enclosed`), so dissipation with
balance and embodiment binds counting there by itself (`enclosed_binds_counting`). -/
theorem finite_counting_under (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∃ M, ∀ t, n t ≤ M) →
      (BindsCounting S ∨ BoundsChange S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ B, ChangeBound 0 B n c a) → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
        w.CountsObey Q :=
  ⟨fun law w _ meets finite alive census => law _ _ _ census.tally
    (match finite.census_bounded with
      | ⟨M, bounded⟩ => ⟨M, bounded alive census⟩)
    (fun
      | .inl ⟨balanced, embodied, .inl acting⟩ => counting_binds_jointly.1 w (meets _ balanced)
          (meets _ acting) (Embodied.arising (meets _ embodied)) alive census
      | .inl ⟨balanced, embodied, .inr ⟨_, dissipative⟩⟩ | .inr ⟨balanced, embodied, dissipative⟩ =>
          fun t arising => enclosed_binds_counting w (meets _ balanced) (meets _ dissipative)
            (meets _ embodied) census (finite.enclosed t) arising)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨_, enclosure_bounds_change census
      (meets _ embodied) (meets _ balanced) (meets _ dissipative) fun t _ => finite.enclosed t⟩),
   fun law n c _ tally ⟨M, bounded⟩ quiet bounds =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => pointwise (Ring.counts tally bounded) (law (embodiedRing n c M)
        (embodiedRing_meets bounded hb) (places_listed _) _ (Ring.census bounded _))
    | true, false => pointwise (Ring.counts tally bounded) (law (ring n c M)
        (ring_meets bounded he) (places_listed _) _ (Ring.census bounded _))
    | true, true => match hd : S .dissipative with
      | false => pointwise (Ring.counts tally bounded) (law (balancedRing n c M)
          (balancedRing_meets tally bounded (fun ha => quiet (.inl ⟨hb, he, .inl ha⟩)) hd)
          (places_listed _) _ (Ring.census bounded _))
      | true => match bounds ⟨hb, he, hd⟩ with
        | ⟨_, bound⟩ => pointwise (finiteQueue_counts tally bound) (law (finiteQueue _ _ _ _)
            ((finiteQueue_premised tally (quiet (.inr ⟨hb, he, hd⟩)) bound).meets S)
            (finiteQueue_finite _ _ _ _) _ (finiteQueue_census _ _ _ _))⟩

/-- So in finite worlds, nothing arising across a step at which nothing is active is a law of
counting under a selection exactly when the selection selects balance and embodiment, and
only active relata giving or dissipation. -/
theorem finite_counting_binds_iff (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
      w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t) ↔ BindsCounting S ∨ BoundsChange S :=
  have pointwise : Pointwise fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t :=
    fun same law t pos => Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos
      (Nat.le_of_eq (same t).2.2.symm))) (Nat.le_of_eq (same t).1)
  have unbound : ¬ (BindsCounting S ∨ BoundsChange S) → ¬ ∀ (w : World)
      [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
        w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t := fun free law =>
    Nat.lt_irrefl 0 ((finite_counting_under S pointwise).mpr law _ _ _ Queue.lone_tally
      ⟨1, fun | 0 => Nat.zero_le 1 | _ + 1 => Nat.le_refl 1⟩
      (fun binds => absurd binds free) (fun bounds => absurd (.inr bounds) free)
      0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, ha : S .acting,
      hd : S .dissipative with
    | true, true, true, _ => .inl ⟨hb, he, .inl ha⟩
    | true, true, false, true => .inr ⟨hb, he, hd⟩
    | false, _, _, _ => absurd law (unbound fun
        | .inl binds => nomatch hb.symm.trans binds.1
        | .inr bounds => nomatch hb.symm.trans bounds.1)
    | true, false, _, _ => absurd law (unbound fun
        | .inl binds => nomatch he.symm.trans binds.2.1
        | .inr bounds => nomatch he.symm.trans bounds.2.1)
    | true, true, false, false => absurd law (unbound fun
        | .inl ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | .inl ⟨_, _, .inr ⟨_, dissipative⟩⟩ => nomatch hd.symm.trans dissipative
        | .inr ⟨_, _, dissipative⟩ => nomatch hd.symm.trans dissipative),
   fun binds => (finite_counting_under S pointwise).mp fun _ _ _ _ _ quiet _ => quiet binds⟩

/-- And a change bound from the first step is a law of counting in finite worlds under a
selection exactly when the selection bounds change: one member replaced at every step is
counted by a finite world meeting any other selection. -/
theorem finite_change_bound_iff (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
      w.CountsObey fun n c a => ∃ B, ChangeBound 0 B n c a) ↔ BoundsChange S :=
  have replaced : Tally (fun _ => 1) (fun _ => 1) (fun _ => 1) := fun _ => ⟨0, rfl, rfl⟩
  have bounded : ∀ t, (fun _ => 1 : Nat → Nat) t ≤ 1 := fun _ => Nat.le_refl 1
  have recurring : ¬ ∃ B, ChangeBound 0 B
      (fun t => (Ring.seated (fun _ => 1) (fun _ => 1) 1 t).length)
      (fun t => ceasings (Ring.seated (fun _ => 1) (fun _ => 1) 1 t)
        (Ring.holds (fun _ => 1) (fun _ => 1) 1) t)
      (fun t => comings (Ring.seated (fun _ => 1) (fun _ => 1) 1 (t + 1))
        (Ring.holds (fun _ => 1) (fun _ => 1) 1) t) :=
    fun ⟨_, bound⟩ => bound.not_recurring fun N => ⟨N, Nat.le_refl N,
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_trans
        (Nat.le_of_eq (Ring.counts replaced bounded N).2.1.symm) (Nat.le_add_right _ _))⟩
  ⟨fun law => match hb : S .balanced, he : S .embodied, hd : S .dissipative with
    | true, true, true => ⟨hb, he, hd⟩
    | false, _, _ => absurd (law (embodiedRing _ _ 1) (embodiedRing_meets bounded hb)
        (places_listed _) _ (Ring.census bounded _)) recurring
    | true, false, _ => absurd (law (ring _ _ 1) (ring_meets bounded he)
        (places_listed _) _ (Ring.census bounded _)) recurring
    | true, true, false => absurd (law (balancedRing _ _ 1)
        (balancedRing_meets replaced bounded (fun _ _ _ => Nat.zero_lt_one) hd)
        (places_listed _) _ (Ring.census bounded _)) recurring,
   fun ⟨balanced, embodied, dissipative⟩ _ _ meets finite _ census =>
    ⟨_, enclosure_bounds_change census (meets _ embodied) (meets _ balanced)
      (meets _ dissipative) fun t _ => finite.enclosed t⟩⟩

/-- Finite worlds and worlds enclosed from some step on have the same laws of counting under a
selection exactly when it bounds change and binds counting: there a change bound from some
step is one from the first step (`ChangeBound.from_zero`) and bounds the count. Where the
selection does not bound change, a count growing without end is counted in a world enclosed
at every step and in no finite world; where it bounds change without binding counting, one
relatum arising from none before enclosure is counted in an enclosed world and in no finite
world. -/
theorem enclosed_iff_finite_counting_under (S : Premise → Bool) :
    (∀ Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop, Pointwise Q →
      ((∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
          (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
        ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
          w.CountsObey Q)) ↔
      BoundsChange S ∧ BindsCounting S :=
  have growing : ¬ BoundsChange S → ¬ ∀ Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop,
      Pointwise Q → ((∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
          (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
        ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
          w.CountsObey Q) := fun free law =>
    have pointwise : Pointwise fun n (_ _ : Nat → Nat) => ∃ M, ∀ t, n t ≤ M :=
      fun same ⟨M, bounded⟩ => ⟨M, fun t => Nat.le_trans (Nat.le_of_eq (same t).1.symm)
        (bounded t)⟩
    match (enclosed_counting_under S pointwise).mpr ((law _ pointwise).mpr
        fun _ _ _ finite alive census => match finite.census_bounded with
          | ⟨M, bounded⟩ => ⟨M, bounded alive census⟩)
        (fun t => t + 1) (fun _ => 0) (fun _ => 1) (fun t => ⟨t + 1, rfl, rfl⟩)
        (fun _ _ _ => Nat.succ_pos _) (fun bounds => absurd bounds free) with
    | ⟨M, bounded⟩ => Nat.lt_irrefl M (bounded M)
  have arising : BoundsChange S → ¬ BindsCounting S → ¬ ∀ Q : (Nat → Nat) → (Nat → Nat) →
      (Nat → Nat) → Prop, Pointwise Q →
      ((∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
          (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
        ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
          w.CountsObey Q) := fun bounds free law =>
    have pointwise : Pointwise fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t :=
      fun same law t pos => Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos
        (Nat.le_of_eq (same t).2.2.symm))) (Nat.le_of_eq (same t).1)
    Nat.lt_irrefl 0 ((enclosed_counting_under S pointwise).mpr ((law _ pointwise).mpr
        ((finite_counting_binds_iff S).mpr (.inr bounds))) _ _ _ Queue.lone_tally
      (fun binds => absurd binds free)
      (fun _ => ⟨1, 1, Queue.lone_settles, fun t later pos => match t, later, pos with
        | 0, later, _ => absurd later (Nat.not_succ_le_zero 0)
        | _ + 1, _, pos => absurd pos (Nat.lt_irrefl 0)⟩)
      0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, hd : S .dissipative, ha : S .acting,
      ht : S .taking with
    | true, true, true, true, _ => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inl ha⟩⟩
    | true, true, true, false, true => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inr ⟨ht, hd⟩⟩⟩
    | true, true, true, false, false => absurd law (arising ⟨hb, he, hd⟩ fun
        | ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | ⟨_, _, .inr ⟨taking, _⟩⟩ => nomatch ht.symm.trans taking)
    | false, _, _, _, _ => absurd law (growing fun bounds => nomatch hb.symm.trans bounds.1)
    | true, false, _, _, _ => absurd law (growing fun bounds => nomatch he.symm.trans bounds.2.1)
    | true, true, false, _, _ =>
      absurd law (growing fun bounds => nomatch hd.symm.trans bounds.2.2),
   fun ⟨bounds, binds⟩ _ pointwise => (enclosed_counting_under S pointwise).symm.trans
    (Iff.trans ⟨fun law n c a tally _ quiet bounded => law n c a tally (fun _ => quiet (.inl binds))
        fun _ => match bounded bounds with
          | ⟨_, bound⟩ => ⟨0, _, bound, fun t _ => quiet (.inl binds) t⟩,
      fun law n c a tally quiet bounded => match bounded bounds with
        | ⟨_, _, bound, _⟩ => law n c a tally ⟨_, fun t => Nat.le_trans (Nat.le_add_right _ _)
            (bound.from_zero t (Nat.zero_le t))⟩ (fun _ => quiet binds)
            (fun _ => ⟨_, bound.from_zero⟩)⟩
      (finite_counting_under S pointwise))⟩

end World

end Becoming
