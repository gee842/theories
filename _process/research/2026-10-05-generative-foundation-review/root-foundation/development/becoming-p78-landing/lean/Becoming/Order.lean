import Becoming.Sampling

/-!
# Order: time read off change

The spine counts steps `0, 1, 2, …`. This module asks how much of what the laws state is carried
by the step numbers and how much by the order in which things change. It makes the two moves
converse to `Becoming.Sampling`'s strictly increasing reading: steps at which nothing happens are
inserted (a stuttering, read with the same `sample`), and two exchanges across consecutive steps
are taken in the other order.

* **Stutterings.** `Stutter ρ`: `ρ 0 = 0`, each step idle (`ρ (n + 1) = ρ n`) or moving by one,
  and every step reached. Read through `ρ`, an idle step holds no fine step (`span_idle`) and a
  moving step the one fine step read (`span_moves`).
  - At an idle step nothing takes part: balance, dissipation and closure hold on every family,
    and running down on a family holding what stands (`Flow.sample_idle_balancesOn`,
    `Flow.sample_idle_dissipatesOn`, `Flow.sample_idle_closedAt`, `Flow.sample_idle_runsDownOn`).
    At a moving step each holds exactly where it holds across the step read
    (`Flow.sample_moves_balancesOn_iff`, `Flow.sample_moves_dissipatesOn_iff`,
    `Flow.sample_moves_closedAt_iff`, `Flow.sample_moves_runsDownOn_iff`).
  - So a world read through a stuttering meets the premises exactly where it meets them
    (`World.stutter_premises_iff`): balance (each relatum listed once at each step), dissipation,
    only active relata giving, only active relata taking, activity needing support, embodiment
    and bounded transmission. Unlike a coarser reading (`Strobe.acting_taking_step_relative`,
    `Delay.transmitting_step_relative`), no condition on how activity is held is needed: each
    step of the reading holds at most one fine step.
  - Over any stretch the totals are those of the stretch read (`stutter_total`): what is taken
    and given (`Flow.stutter_taken`, `Flow.stutter_given`, each relatum listed once); the rises
    and falls of an amount and the steps at which it rises and falls (`stutter_risen`,
    `stutter_fallen`, `stutter_rise_count`, `stutter_fall_count`), so the terms of `over_stretch`;
    and, where it is decided, the members of a finite family coming to be and ceasing to be
    (`stutter_comings`, `stutter_ceasings`).
  - Arising, ceasing and change of standing recur read through a stuttering exactly where they
    recur (`World.stutter_arisingRecurs_iff`, `World.stutter_ceasingRecurs_iff`,
    `World.stutter_change_recurs_iff`, from `stutter_recurs_iff`). A census survives
    (`World.stutter_counted`) and returns where a step of the reading is given for each step
    (`World.stutter_counted_of_section`).
* **What a stuttering changes: what is counted per step.** With idle steps at arbitrarily late
  steps no flow is more without end (`Flow.sample_not_more`): the expansion is more without end
  and, every step read twice, it is not (`Expansion.more_step_relative`). A reserve carrying a
  relatum active beyond support falls at every step, so does not carry across an idle step
  (`Web.sample_idle_not_carries`): a world carried by a reserve of one needs a reserve of two
  when every step is read twice (`Lapse.reserve_step_relative`).
* **Independent exchanges commute.** `Flow.Commuted L L' t`: `L'` takes the exchanges of `L`
  across the steps from `t` and `t + 1` in the other order and every other exchange as `L` does.
  `Web.Commuted W W' t`: each standing, activity, dependence, need and drawing of `W` changes
  across at most one of the two steps, and `W'` makes that change across the other (`Moved`).
  Both relations are symmetric (`Flow.Commuted.symm`, `Web.Commuted.symm`). They are realized by
  `Flow.swap` and `Web.commute` wherever sides say which relata change across which step and
  split the two steps (`Web.Split`; `Flow.swap_commuted`, `Web.commute_commuted`); `World.commute`
  is the world with both.
  - Balance on a family across each of the two steps is balance across the other in the
    commuted world (`Flow.Commuted.balancesOn_first`, `Flow.Commuted.balancesOn_second`,
    `Flow.Commuted.balancesOn_away`): the standing amounts exchange (`Exchanged`,
    `Web.Commuted.stock`), their rises and falls changing places (`Exchanged.rise_first`,
    `Exchanged.fall_second`, …), balance being balance of change (`balance_iff_change`).
  - So balance, dissipation and embodiment hold of the commuted world exactly where they hold of
    the world (`World.commute_laws`, `Flow.Commuted.balances_iff`, `Flow.Commuted.dissipative_iff`,
    `Web.Commuted.embodied`), and running down across the two steps where the family holds what
    stands at the three times (`Flow.Commuted.runsDownOn_first`, `Flow.Commuted.runsDownOn_second`).
  - Over any stretch holding both steps, the counts and totals are those of the world
    (`World.commute_counts`, from `total_swapped`): the relata of a finite family arising and
    ceasing, the rises and falls of a family's total standing, and the steps at which it falls.
  - Repeated, the commutations generate `Reorders`, which keeps balance, dissipation and
    embodiment (`Reorders.laws`) and, over a stretch holding every commuted pair, the totals
    (`Reorders.totals`). This is the equivalence of Mazurkiewicz traces, with independence of two
    consecutive exchanges taken as the sides splitting them.
* **What the order carries: dependence.** Two further conditions are needed, and each is
  needed. Activity needing support holds after commuting where no dependence at the two outer
  steps crosses the sides (`Web.commute_dependent`); in `Crossing` the two exchanges share no
  relatum and the sides split them, yet a relatum depends on a condition the other exchange
  ends, and in the other order it is active without support (`Crossing.order_registers`). Only
  active relata giving holds after commuting where no relatum giving across one of the steps
  has its activity begun by the first or ended by the second (`Flow.Commuted.acting`); in
  `Arising` the relatum arising across the first step gives across the second, and in the other
  order it gives before it is active (`Arising.order_registers`).

* **The order of exchanges as an object (P78b).** `Footprinted X` is a world's flow and web with
  a footprint: at each step, the relata the exchange across it touches, decided relatum by
  relatum (`touch : Nat → X → Bool`). It `Contains` the exchanges where every relatum a step
  leaves untouched takes no part in its exchange and is unmoved across it (`Web.Unmoved`,
  `Web.SameAt`). Two exchanges are `Joined` where some relatum is touched by both, or a relatum
  touched by one depends, at the start or the end of its step, on a condition the other touches.
  `Precedes` is the order they generate: a strict partial order of the steps (`Precedes.lt`,
  `Precedes.irrefl`, `Precedes.asymm`), relative to the footprint (a footprint touching more
  joins and orders more, `Joined.mono`, `Precedes.mono`; every world has one containing it,
  `contains_everything`).
  - Two consecutive exchanges not joined are split by the first one's footprint, so commuting them
    (`Footprinted.commute`) is a step of `Reorders` (`Footprinted.split`). The moved footprint
    contains the commuted exchanges (`commute_contains`), each relatum a step touches is shown
    before and after it as it was across the step its exchange came from (`commute_shows`), and
    joining and the order are kept up to the renumbering (`commute_joined`,
    `commute_precedes`).
  - Commuting again and again (`reorder`, each commutation of two exchanges not joined:
    `Independent`), the exchange across step `n` comes to `place ts n` and step `m` holds the
    exchange from `origin ts m` (`reorder_exchange`, `reorder_touch`, `reorder_shows`,
    `reorder_joined`). **The order is kept**: one exchange precedes another in the reordering
    exactly where the exchanges they came from did (`reorder_precedes`, `precedes_place`), so the
    renumbering keeps the order of joined exchanges (`Independent.keeps`), and the reordering is
    one of `Reorders` (`reorder_reorders`).
  - **The converse.** For a renumbering of a stretch of steps among themselves (`Reindexes`) that
    keeps the order of joined exchanges (`Keeps`), commutations of exchanges not joined within
    the stretch take each exchange where the renumbering does (`sorts`: bubble sort, the exchange
    the renumbering puts first brought forward past exchanges it is not joined to, `lowering`,
    then the rest). So the renumberings reached are exactly those keeping the order
    (`sorts_iff`). And a world that takes the same exchanges, touches the same relata and shows
    them after each step as the world does, in an order keeping the order of joined exchanges and
    from the same start, agrees over the stretch with a reordering: the same exchange at each step
    and every relatum shown alike at every step (`converse`). This is Mazurkiewicz's theorem that
    a trace is determined by its order of dependence, with the footprint giving independence.
* **What carries along repeated commutation.** Commuting exchanges not joined keeps every
  premise exactly (`reorder_premises`): balance, dissipation and embodiment (through
  `Reorders.laws`), and only active relata giving, only active relata taking, activity needing
  support and bounded transmission (`reorder_acting_iff`, `reorder_taking_iff`,
  `reorder_dependent_iff`, `reorder_transmits_iff`). At one commutation: what takes part or comes
  to stand is touched, so is shown as across the step it came from (`acting_of_shows`,
  `taking_of_shows`, `transmits_of_shows`); between the two steps each active relatum's
  dependences and their conditions are shown as before them or as after them
  (`commute_dependent`), and commuting again restores the world (`commute_twice`). Along any
  `Reorders`, joined or not, the counts of arising and ceasing over a stretch holding every
  commuted pair are kept, with activity decided (`Reorders.counts`). `Reorders` itself keeps
  neither the order nor activity needing support nor only active relata giving: in `Crossing` and
  `Arising` every footprint containing the two exchanges joins them (`Crossing.joined`,
  `Arising.joined`), and taking them in the other order is a step of `Reorders` after which
  activity needing support, respectively only active relata giving, fails
  (`Crossing.reorders_joined`, `Arising.reorders_joined`).
* **Removing idle steps.** Given a stuttering `ρ` and its moving steps `σ` (`Stutter.Moves`; each
  exists by `Stutter.crosses` and is the only one, `Stutter.moving_unique`), a world idle at the
  idle steps of `ρ` (`World.IdleAt`) has them removed by keeping the exchanges of the moving steps
  and reading the web there (`World.withoutIdle`, `Flow.readAt`). Each step of the world shows
  every relatum as the step of the world without idle steps it is read at
  (`World.withoutIdle_sameAt`); the two meet balance, dissipation, only active relata giving and
  taking, activity needing support, embodiment and bounded transmission alike, with no condition
  on listing (`World.withoutIdle_premises`, `World.withoutIdle_transmits`), and either has a
  census exactly where the other does (`World.withoutIdle_counted`); and over any stretch
  what is taken and given, the rises and falls of a family's total standing with the steps at
  which it rises and falls, and the relata arising and ceasing, are those of the stretch of the
  world without idle steps it reads (`World.withoutIdle_totals`, `World.withoutIdle_counts`).

Reading (the AI's, pending Ren): for the laws of one step, the totals and counts over a stretch,
and recurrence, the step index carries nothing beyond the order of change; an idle step
registers nothing, and removing it changes nothing the laws state. What is counted per step,
rates and how long a reserve carries, is relative to the unit of the reading, as coarser steps
were (`Becoming.Sampling`). Within the order, what registers is the order of exchanges joined
through a relatum or a dependence: with a footprint, the order the laws need is the partial order
`Precedes`, not a sequence of steps. Commuting exchanges it does not order keeps every premise and
the order itself, and every arrangement of the same exchanges keeping it is reached so.

Not shown: a footprint derived from the world. The footprint is given and decided, and the order
is relative to it; the least footprint, each step touching exactly what takes part in it or moves
across it, would need being moved to be decided, which with activity and dependence as
propositions is not assumed. The sides of `Reorders` remain given. The moving steps of a
stuttering are given as a function: each exists and is unique, but choosing all of them at once is
an unbounded search, not done. Invariance of the predicates of Part II; continuous time.
Commutation is of consecutive steps. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

/-! ## Arithmetic -/

/-- One more than a number, less it, is one. -/
theorem succ_sub_self : ∀ a : Nat, a + 1 - a = 1
  | 0 => rfl
  | a + 1 => (Nat.succ_sub_succ (a + 1) a).trans (succ_sub_self a)

/-- A number exceeds itself by nothing. -/
theorem excess_self : ∀ a : Nat, excess a a = 0
  | 0 => rfl
  | a + 1 => excess_self a

/-- Adding the same to both sides leaves the excess. -/
theorem excess_add_right (x a : Nat) : ∀ k : Nat, excess (x + k) (a + k) = excess x a
  | 0 => rfl
  | k + 1 => excess_add_right x a k

/-- Where two sums agree, the excess of a part of one over a part of the other is the excess
of the other's remaining part over the first's: `x + y = a + b` gives `x - a = b - y`. -/
theorem excess_of_sum {x y a b : Nat} (sum : x + y = a + b) : excess x a = excess b y :=
  (excess_add_right x a y).symm.trans
    ((congrArg (fun k => excess k (a + y)) sum).trans
      ((congrArg (fun k => excess k (a + y)) (Nat.add_comm a b)).trans
        ((congrArg (fun k => excess (b + a) k) (Nat.add_comm a y)).trans
          (excess_add_right b y a))))

/-- The total over a stretch of `a + b` steps is the total over its first `a` steps with the
total over the `b` after them. -/
theorem total_steps_add (q : Nat → Nat) : ∀ (S a b : Nat),
    total (steps S (a + b)) q = total (steps S a) q + total (steps (S + a) b) q
  | S, 0, b => (congrArg (fun k => total (steps S k) q) (Nat.zero_add b)).trans
      (Nat.zero_add _).symm
  | S, a + 1, b =>
    (congrArg (fun k => total (steps S k) q) (Nat.succ_add a b)).trans
      ((congrArg (q S + ·) (total_steps_add q (S + 1) a b)).trans
        ((Nat.add_assoc _ _ _).symm.trans
          (congrArg (fun k => total (steps S (a + 1)) q + total (steps k b) q)
            (Nat.add_right_comm S 1 a))))

/-! ## Stutterings -/

/-- A stuttering: a reading of steps that starts at the first step, at each of its steps either
reads again the step it read, an *idle* step, or reads the next one, a *moving* step, and reads
every step. -/
def Stutter (ρ : Nat → Nat) : Prop :=
  ρ 0 = 0 ∧ (∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) ∧ ∀ s, ∃ n, ρ n = s

namespace Stutter

variable {ρ : Nat → Nat}

/-- A reading whose steps idle or move never reads an earlier step later. -/
theorem le_succ (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) (n : Nat) :
    ρ n ≤ ρ (n + 1) :=
  match moving n with
  | .inl idle => Nat.le_of_eq idle.symm
  | .inr moves => Nat.le_trans (Nat.le_succ _) (Nat.le_of_eq moves.symm)

theorem mono (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) :
    ∀ {n m : Nat}, n ≤ m → ρ n ≤ ρ m
  | _, _, .refl => Nat.le_refl _
  | _, m + 1, .step le => Nat.le_trans (mono moving le) (le_succ moving m)

/-- Where a reading's steps idle or move, it moves from below a step to above it across a moving
step reading it. -/
theorem crossing (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) {s : Nat}
    (start : ρ 0 ≤ s) : ∀ m, s < ρ m → ∃ n, n < m ∧ ρ n = s ∧ ρ (n + 1) = s + 1
  | 0, above => absurd start (Nat.not_le_of_gt above)
  | m + 1, above => match moving m with
    | .inl idle => match crossing moving start m (Nat.lt_of_lt_of_le above (Nat.le_of_eq idle)) with
      | ⟨n, below, here, next⟩ => ⟨n, Nat.lt_succ_of_lt below, here, next⟩
    | .inr moves => match Nat.lt_or_ge s (ρ m) with
      | .inl lt => match crossing moving start m lt with
        | ⟨n, below, here, next⟩ => ⟨n, Nat.lt_succ_of_lt below, here, next⟩
      | .inr ge =>
        have same : ρ m = s := Nat.le_antisymm ge
          (Nat.le_of_lt_succ (Nat.lt_of_lt_of_le above (Nat.le_of_eq moves)))
        ⟨m, Nat.lt_succ_self m, same, moves.trans (congrArg (· + 1) same)⟩

/-- A stuttering reads each step at a moving step. -/
theorem crosses (stutter : Stutter ρ) (s : Nat) : ∃ n, ρ n = s ∧ ρ (n + 1) = s + 1 :=
  match stutter.2.2 (s + 1) with
  | ⟨m, reads⟩ => match crossing stutter.2.1 (Nat.le_trans (Nat.le_of_eq stutter.1) (Nat.zero_le s)) m
      (Nat.lt_of_lt_of_le (Nat.lt_succ_self s) (Nat.le_of_eq reads.symm)) with
    | ⟨n, _, here, next⟩ => ⟨n, here, next⟩

/-- A moving step reading `t`. -/
theorem moving (stutter : Stutter ρ) (t : Nat) : ∃ n, ρ n = t ∧ ρ (n + 1) = ρ n + 1 :=
  match stutter.crosses t with
  | ⟨n, here, next⟩ => ⟨n, here, next.trans (congrArg (· + 1) here.symm)⟩

/-- A stuttering reads no step later than its own. -/
theorem le_self (stutter : Stutter ρ) : ∀ n, ρ n ≤ n
  | 0 => Nat.le_of_eq stutter.1
  | n + 1 => match stutter.2.1 n with
    | .inl idle => Nat.le_trans (Nat.le_of_eq idle) (Nat.le_trans (le_self stutter n) (Nat.le_succ n))
    | .inr moves => Nat.le_trans (Nat.le_of_eq moves) (Nat.succ_le_succ (le_self stutter n))

end Stutter

/-- At an idle step the coarse step holds no fine step. -/
theorem span_idle {ρ : Nat → Nat} {n : Nat} (idle : ρ (n + 1) = ρ n) : span ρ n = [] :=
  show steps (ρ n) (ρ (n + 1) - ρ n) = [] from
  (congrArg (fun k => steps (ρ n) (k - ρ n)) idle).trans
    (congrArg (steps (ρ n)) (Nat.sub_self (ρ n)))

/-- At a moving step the coarse step holds the one fine step read. -/
theorem span_moves {ρ : Nat → Nat} {n : Nat} (moves : ρ (n + 1) = ρ n + 1) :
    span ρ n = [ρ n] :=
  show steps (ρ n) (ρ (n + 1) - ρ n) = [ρ n] from
  (congrArg (fun k => steps (ρ n) (k - ρ n)) moves).trans
    (congrArg (steps (ρ n)) (succ_sub_self (ρ n)))

/-! ## One change read through a stuttering -/

section Change

variable {ρ : Nat → Nat} {n : Nat}

/-- Nothing comes to be across an idle step. -/
theorem not_comesToBe_idle {p : Nat → Prop} (idle : ρ (n + 1) = ρ n) :
    ¬ ComesToBe (fun k => p (ρ k)) n :=
  fun ⟨absent, held⟩ => absent (Eq.subst (motive := p) idle held)

/-- Nothing ceases to be across an idle step. -/
theorem not_ceasesToBe_idle {p : Nat → Prop} (idle : ρ (n + 1) = ρ n) :
    ¬ CeasesToBe (fun k => p (ρ k)) n :=
  fun ⟨held, absent⟩ => absent (Eq.subst (motive := p) idle.symm held)

/-- Across a moving step something comes to be exactly where it comes to be across the step
read. -/
theorem comesToBe_moves {p : Nat → Prop} (moves : ρ (n + 1) = ρ n + 1) :
    ComesToBe (fun k => p (ρ k)) n ↔ ComesToBe p (ρ n) :=
  ⟨fun ⟨absent, held⟩ => ⟨absent, Eq.subst (motive := p) moves held⟩,
   fun ⟨absent, held⟩ => ⟨absent, Eq.subst (motive := p) moves.symm held⟩⟩

/-- And ceases to be exactly where it ceases to be across the step read. -/
theorem ceasesToBe_moves {p : Nat → Prop} (moves : ρ (n + 1) = ρ n + 1) :
    CeasesToBe (fun k => p (ρ k)) n ↔ CeasesToBe p (ρ n) :=
  ⟨fun ⟨held, absent⟩ => ⟨held, fun yes => absent (Eq.subst (motive := p) moves.symm yes)⟩,
   fun ⟨held, absent⟩ => ⟨held, fun yes => absent (Eq.subst (motive := p) moves yes)⟩⟩

/-- An amount rises by nothing across an idle step. -/
theorem rise_idle (q : Nat → Nat) (idle : ρ (n + 1) = ρ n) : rise (fun k => q (ρ k)) n = 0 :=
  (congrArg (fun k => excess (q k) (q (ρ n))) idle).trans (excess_self _)

/-- And falls by nothing. -/
theorem fall_idle (q : Nat → Nat) (idle : ρ (n + 1) = ρ n) : fall (fun k => q (ρ k)) n = 0 :=
  (congrArg (fun k => excess (q (ρ n)) (q k)) idle).trans (excess_self _)

/-- Across a moving step it rises as across the step read. -/
theorem rise_moves (q : Nat → Nat) (moves : ρ (n + 1) = ρ n + 1) :
    rise (fun k => q (ρ k)) n = rise q (ρ n) :=
  congrArg (fun k => excess (q k) (q (ρ n))) moves

/-- And falls as across the step read. -/
theorem fall_moves (q : Nat → Nat) (moves : ρ (n + 1) = ρ n + 1) :
    fall (fun k => q (ρ k)) n = fall q (ρ n) :=
  congrArg (fun k => excess (q (ρ n)) (q k)) moves

end Change

/-! ## Totals over a stretch read through a stuttering -/

section Totals

variable {ρ : Nat → Nat}

/-- A quantity of each step, read through a reading whose steps idle or move: nothing at the
idle steps, the quantity of the step read at the moving ones. Over any stretch it totals what
the quantity totals over the stretch read. -/
theorem stutter_total (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) {g g' : Nat → Nat}
    (idle : ∀ n, ρ (n + 1) = ρ n → g' n = 0) (moves : ∀ n, ρ (n + 1) = ρ n + 1 → g' n = g (ρ n))
    (N : Nat) : ∀ m d, ρ N + d = ρ (N + m) →
      total (steps N m) g' = total (steps (ρ N) d) g
  | 0, 0, _ => rfl
  | 0, d + 1, reads => absurd (Nat.le_of_eq reads)
      (Nat.not_le_of_gt (Nat.lt_add_of_pos_right (Nat.succ_pos d)))
  | m + 1, d, reads => match moving (N + m) with
    | .inl still =>
      (steps_last g' N m).trans
        ((congrArg (total (steps N m) g' + ·) (idle (N + m) still)).trans
          (stutter_total moving idle moves N m d (reads.trans still)))
    | .inr next => match d, reads with
      | 0, reads => absurd (Nat.le_of_eq reads.symm)
          (Nat.not_le_of_gt (Nat.lt_of_le_of_lt (Stutter.mono moving (Nat.le_add_right N m))
            (Nat.lt_of_lt_of_le (Nat.lt_succ_self _) (Nat.le_of_eq next.symm))))
      | d + 1, reads =>
        have earlier : ρ N + d = ρ (N + m) := Nat.succ.inj (reads.trans next)
        (steps_last g' N m).trans
          ((congrArg (total (steps N m) g' + ·) (moves (N + m) next)).trans
            ((congrArg (· + g (ρ (N + m))) (stutter_total moving idle moves N m d earlier)).trans
              ((congrArg (fun k => total (steps (ρ N) d) g + g k) earlier).symm.trans
                (steps_last g (ρ N) d).symm)))

end Totals


/-! ## A flow and a web read through a stuttering

A stuttering read with `Becoming.Sampling`'s `sample`: at an idle step the coarse step holds no
fine step, so nothing takes part and the web shows the same step on both sides of it; at a
moving step it holds the one fine step read. -/

variable {F C : Type}

namespace Flow

section Nil

variable {L : Flow F C} {ρ : Nat → Nat} {n : Nat}

/-- Where nothing takes part, nothing is taken. -/
theorem taken_nil {t : Nat} (none : L.present t = []) (c : C) : L.taken t c = 0 :=
  congrArg (fun l => total l fun f => L.take t f c) none

/-- Where nothing takes part, nothing is given. -/
theorem given_nil {t : Nat} (none : L.present t = []) (c : C) : L.given t c = 0 :=
  congrArg (fun l => total l fun f => L.give t f c) none

/-- At a moving step the one fine step read is the only one, so listing once there is listing
once at every fine step of it. -/
theorem once_of_moves (moves : ρ (n + 1) = ρ n + 1) (once : Distinct (L.present (ρ n))) :
    ∀ j, j ∈ span ρ n → Distinct (L.present j) :=
  fun j mem => match mem_cons_cases (Eq.subst (motive := fun l => j ∈ l) (span_moves moves) mem) with
    | .inl same => Eq.subst (motive := fun k => Distinct (L.present k)) same.symm once
    | .inr no => nomatch no

end Nil

variable [DecidableEq F] {L : Flow F C} {W : Web F C} {ρ : Nat → Nat} {n : Nat}

/-- At an idle step nothing takes part. -/
theorem sample_idle_present (idle : ρ (n + 1) = ρ n) : (L.sample ρ).present n = [] :=
  congrArg L.unionPresent (span_idle idle)

/-- At an idle step nothing is taken. -/
theorem sample_idle_take (idle : ρ (n + 1) = ρ n) (f : F) (c : C) :
    (L.sample ρ).take n f c = 0 :=
  congrArg (fun l => total l fun j => gate f (L.present j) (L.take j f c)) (span_idle idle)

/-- At an idle step nothing is given. -/
theorem sample_idle_give (idle : ρ (n + 1) = ρ n) (f : F) (c : C) :
    (L.sample ρ).give n f c = 0 :=
  congrArg (fun l => total l fun j => gate f (L.present j) (L.give j f c)) (span_idle idle)

/-- At a moving step the relata taking part are those taking part in the step read. -/
theorem sample_moves_mem (moves : ρ (n + 1) = ρ n + 1) {f : F} :
    f ∈ (L.sample ρ).present n ↔ f ∈ L.present (ρ n) :=
  have same : (L.sample ρ).present n = L.unionPresent [ρ n] :=
    congrArg L.unionPresent (span_moves moves)
  ⟨fun mem => match (L.unionPresent_spec [ρ n]).2.2 f
      (Eq.subst (motive := fun l => f ∈ l) same mem) with
     | ⟨_, here, held⟩ => match mem_cons_cases here with
       | .inl same' => Eq.subst (motive := fun k => f ∈ L.present k) same' held
       | .inr no => (nomatch no),
   fun held => Eq.subst (motive := fun l => f ∈ l) same.symm
     ((L.unionPresent_spec [ρ n]).2.1 (ρ n) (.head []) f held)⟩

/-- And each takes what it takes across the step read. -/
theorem sample_moves_take (moves : ρ (n + 1) = ρ n + 1) {f : F} (held : f ∈ L.present (ρ n))
    (c : C) : (L.sample ρ).take n f c = L.take (ρ n) f c :=
  (congrArg (fun l => total l fun j => gate f (L.present j) (L.take j f c))
    (span_moves moves)).trans ((Nat.add_zero _).trans (gate_mem held _))

/-- And gives what it gives across the step read. -/
theorem sample_moves_give (moves : ρ (n + 1) = ρ n + 1) {f : F} (held : f ∈ L.present (ρ n))
    (c : C) : (L.sample ρ).give n f c = L.give (ρ n) f c :=
  (congrArg (fun l => total l fun j => gate f (L.present j) (L.give j f c))
    (span_moves moves)).trans ((Nat.add_zero _).trans (gate_mem held _))

/-- Each relatum listed once at the step read, what is taken from a condition across a moving
step is what is taken from it across the step read. -/
theorem sample_moves_taken (moves : ρ (n + 1) = ρ n + 1) (once : Distinct (L.present (ρ n)))
    (c : C) : (L.sample ρ).taken n c = L.taken (ρ n) c :=
  (sample_taken_on ρ (once_of_moves moves once) c).trans
    ((congrArg (fun l => total l fun j => L.taken j c) (span_moves moves)).trans (Nat.add_zero _))

/-- And what is given to it is what is given to it across the step read. -/
theorem sample_moves_given (moves : ρ (n + 1) = ρ n + 1) (once : Distinct (L.present (ρ n)))
    (c : C) : (L.sample ρ).given n c = L.given (ρ n) c :=
  (sample_given_on ρ (once_of_moves moves once) c).trans
    ((congrArg (fun l => total l fun j => L.given j c) (span_moves moves)).trans (Nat.add_zero _))

/-! ### The laws of one step at an idle step -/

/-- Balance holds on every family across an idle step. -/
theorem sample_idle_balancesOn (idle : ρ (n + 1) = ρ n) (cs : List C) :
    (L.sample ρ).BalancesOn (W.sample ρ) cs n :=
  fun c _ => (congrArg (· + (L.sample ρ).taken n c) (congrArg (fun k => W.level k c) idle)).trans
    (congrArg (W.level (ρ n) c + ·) ((taken_nil (sample_idle_present idle) c).trans
      (given_nil (sample_idle_present idle) c).symm))

/-- Every family is dissipated on across an idle step. -/
theorem sample_idle_dissipatesOn (idle : ρ (n + 1) = ρ n) (cs : List C) :
    (L.sample ρ).DissipatesOn cs n :=
  fun f mem => absurd (Eq.subst (motive := fun l => f ∈ l) (sample_idle_present idle) mem)
    fun no => nomatch no

/-- Every family is closed across an idle step. -/
theorem sample_idle_closedAt (idle : ρ (n + 1) = ρ n) (cs : List C) :
    (L.sample ρ).ClosedAt cs n :=
  fun f mem => absurd (Eq.subst (motive := fun l => f ∈ l) (sample_idle_present idle) mem)
    fun no => nomatch no

/-- So every idle step is enclosed. -/
theorem sample_idle_enclosed (idle : ρ (n + 1) = ρ n) : (L.sample ρ).Enclosed n :=
  ⟨[], trivial, sample_idle_closedAt idle []⟩

/-- A family without repetition holding what stands at the step read runs down across an idle
step. -/
theorem sample_idle_runsDownOn (idle : ρ (n + 1) = ρ n) {es : List C} (distinct : Distinct es)
    (holds : ∀ c, 0 < W.level (ρ n) c → c ∈ es) : (L.sample ρ).RunsDownOn (W.sample ρ) es n :=
  ⟨distinct, holds,
   fun c stands => holds c (Eq.subst (motive := fun k => 0 < W.level k c) idle stands),
   sample_idle_balancesOn idle es, sample_idle_dissipatesOn idle es⟩

/-! ### The laws of one step at a moving step -/

/-- Balance at a moving step is balance at the step read, each relatum listed once there. -/
theorem sample_moves_balancesOn_iff (moves : ρ (n + 1) = ρ n + 1)
    (once : Distinct (L.present (ρ n))) {cs : List C} :
    (L.sample ρ).BalancesOn (W.sample ρ) cs n ↔ L.BalancesOn W cs (ρ n) :=
  have ends : ∀ c, W.level (ρ (n + 1)) c + (L.sample ρ).taken n c =
      W.level (ρ n + 1) c + L.taken (ρ n) c := fun c =>
    congr (congrArg (· + ·) (congrArg (fun k => W.level k c) moves)) (sample_moves_taken moves once c)
  ⟨fun balances c mem => (ends c).symm.trans ((balances c mem).trans
      (congrArg (W.level (ρ n) c + ·) (sample_moves_given moves once c))),
   fun balances c mem => (ends c).trans ((balances c mem).trans
      (congrArg (W.level (ρ n) c + ·) (sample_moves_given moves once c)).symm)⟩

/-- Dissipation at a moving step is dissipation at the step read. -/
theorem sample_moves_dissipatesOn_iff (moves : ρ (n + 1) = ρ n + 1) {cs : List C} :
    (L.sample ρ).DissipatesOn cs n ↔ L.DissipatesOn cs (ρ n) :=
  have take : ∀ f, f ∈ L.present (ρ n) →
      total cs ((L.sample ρ).take n f) = total cs (L.take (ρ n) f) :=
    fun _ held => total_congr (fun c => sample_moves_take moves held c) cs
  have give : ∀ f, f ∈ L.present (ρ n) →
      total cs ((L.sample ρ).give n f) = total cs (L.give (ρ n) f) :=
    fun _ held => total_congr (fun c => sample_moves_give moves held c) cs
  ⟨fun dissipates f held => Nat.le_trans
      (Nat.le_of_eq (congr (congrArg (· + ·) (give f held)) (congrArg sign (take f held))).symm)
      (Nat.le_trans (dissipates f ((sample_moves_mem moves).mpr held))
        (Nat.le_of_eq (take f held))),
   fun dissipates f mem =>
     have held := (sample_moves_mem moves).mp mem
     Nat.le_trans
      (Nat.le_of_eq (congr (congrArg (· + ·) (give f held)) (congrArg sign (take f held))))
      (Nat.le_trans (dissipates f held) (Nat.le_of_eq (take f held).symm))⟩

/-- Closure at a moving step is closure at the step read. -/
theorem sample_moves_closedAt_iff (moves : ρ (n + 1) = ρ n + 1) {cs : List C} :
    (L.sample ρ).ClosedAt cs n ↔ L.ClosedAt cs (ρ n) :=
  (sample_closedAt_iff ρ).trans
    ⟨fun closed => closed (ρ n)
        (Eq.subst (motive := fun l => ρ n ∈ l) (span_moves moves).symm (.head [])),
     fun closed j mem =>
      match mem_cons_cases (Eq.subst (motive := fun l => j ∈ l) (span_moves moves) mem) with
      | .inl same => Eq.subst (motive := fun k => L.ClosedAt cs k) same.symm closed
      | .inr no => nomatch no⟩

/-- Running down at a moving step is running down at the step read, each relatum listed once
there. -/
theorem sample_moves_runsDownOn_iff (moves : ρ (n + 1) = ρ n + 1)
    (once : Distinct (L.present (ρ n))) {es : List C} :
    (L.sample ρ).RunsDownOn (W.sample ρ) es n ↔ L.RunsDownOn W es (ρ n) :=
  ⟨fun ⟨distinct, before, after, balances, dissipates⟩ => ⟨distinct, before,
     fun c stands => after c (Eq.subst (motive := fun k => 0 < W.level k c) moves.symm stands),
     (sample_moves_balancesOn_iff moves once).mp balances,
     (sample_moves_dissipatesOn_iff moves).mp dissipates⟩,
   fun ⟨distinct, before, after, balances, dissipates⟩ => ⟨distinct, before,
     fun c stands => after c (Eq.subst (motive := fun k => 0 < W.level k c) moves stands),
     (sample_moves_balancesOn_iff moves once).mpr balances,
     (sample_moves_dissipatesOn_iff moves).mpr dissipates⟩⟩

/-- Only active relata giving, at a moving step, is the same at the step read. -/
theorem sample_moves_acting_iff (moves : ρ (n + 1) = ρ n + 1) :
    (∀ f c, f ∈ (L.sample ρ).present n → 0 < (L.sample ρ).give n f c → W.active (ρ n) f) ↔
      ∀ f c, f ∈ L.present (ρ n) → 0 < L.give (ρ n) f c → W.active (ρ n) f :=
  ⟨fun acting f c held gives => acting f c ((sample_moves_mem moves).mpr held)
      (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (sample_moves_give moves held c).symm)),
   fun acting f c mem gives =>
     have held := (sample_moves_mem moves).mp mem
     acting f c held (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (sample_moves_give moves held c)))⟩

/-- Only active relata taking, and only from what they draw on, likewise. -/
theorem sample_moves_taking_iff (moves : ρ (n + 1) = ρ n + 1) :
    (∀ f c, f ∈ (L.sample ρ).present n → 0 < (L.sample ρ).take n f c →
        W.active (ρ n) f ∧ W.draws (ρ n) f c) ↔
      ∀ f c, f ∈ L.present (ρ n) → 0 < L.take (ρ n) f c → W.active (ρ n) f ∧ W.draws (ρ n) f c :=
  ⟨fun taking f c held takes => taking f c ((sample_moves_mem moves).mpr held)
      (Nat.lt_of_lt_of_le takes (Nat.le_of_eq (sample_moves_take moves held c).symm)),
   fun taking f c mem takes =>
     have held := (sample_moves_mem moves).mp mem
     taking f c held (Nat.lt_of_lt_of_le takes (Nat.le_of_eq (sample_moves_take moves held c)))⟩

/-! ### The laws of a flow read through a stuttering -/

/-- Balance survives a stuttering, and returns from it, each relatum listed once. -/
theorem stutter_balances_iff (stutter : Stutter ρ) (once : L.Once) :
    (L.sample ρ).Balances (W.sample ρ) ↔ L.Balances W :=
  ⟨fun balances => balances_iff_on.mpr fun cs t => match stutter.moving t with
     | ⟨n, here, moves⟩ => Eq.subst (motive := fun k => L.BalancesOn W cs k) here
        ((sample_moves_balancesOn_iff moves (once (ρ n))).mp (balances.on cs n)),
   fun balances => balances_iff_on.mpr fun cs n => match stutter.2.1 n with
     | .inl idle => sample_idle_balancesOn idle cs
     | .inr moves => (sample_moves_balancesOn_iff moves (once (ρ n))).mpr (balances.on cs (ρ n))⟩

/-- Dissipation survives a stuttering and returns from it. -/
theorem stutter_dissipative_iff (stutter : Stutter ρ) :
    (L.sample ρ).Dissipative ↔ L.Dissipative :=
  ⟨fun dissipative cs t distinct closed => match stutter.moving t with
     | ⟨n, here, moves⟩ => Eq.subst (motive := fun k => L.DissipatesOn cs k) here
        ((sample_moves_dissipatesOn_iff moves).mp (dissipative cs n distinct
          ((sample_moves_closedAt_iff moves).mpr
            (Eq.subst (motive := fun k => L.ClosedAt cs k) here.symm closed)))),
   sample_dissipative ρ⟩

/-- Only active relata giving survives a stuttering and returns from it: no condition on how
activity is held is needed, since every step of the reading holds at most one fine step. -/
theorem stutter_acting_iff (stutter : Stutter ρ) :
    (L.sample ρ).Acting (W.sample ρ) ↔ L.Acting W :=
  ⟨fun acting t f c held gives => match stutter.moving t with
     | ⟨n, here, moves⟩ => Eq.subst (motive := fun k => W.active k f) here
        ((sample_moves_acting_iff moves).mp (acting n) f c
          (Eq.subst (motive := fun k => f ∈ L.present k) here.symm held)
          (Eq.subst (motive := fun k => 0 < L.give k f c) here.symm gives)),
   fun acting n f c mem gives => match stutter.2.1 n with
     | .inl idle => absurd (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (sample_idle_give idle f c)))
        (Nat.lt_irrefl 0)
     | .inr moves => (sample_moves_acting_iff moves).mpr (acting (ρ n)) f c mem gives⟩

/-- Only active relata taking, and only from what they draw on, survives a stuttering and
returns from it. -/
theorem stutter_taking_iff (stutter : Stutter ρ) :
    (L.sample ρ).Taking (W.sample ρ) ↔ L.Taking W :=
  ⟨fun taking t f c held takes => match stutter.moving t with
     | ⟨n, here, moves⟩ => Eq.subst (motive := fun k => W.active k f ∧ W.draws k f c) here
        ((sample_moves_taking_iff moves).mp (taking n) f c
          (Eq.subst (motive := fun k => f ∈ L.present k) here.symm held)
          (Eq.subst (motive := fun k => 0 < L.take k f c) here.symm takes)),
   fun taking n f c mem takes => match stutter.2.1 n with
     | .inl idle => absurd (Nat.lt_of_lt_of_le takes (Nat.le_of_eq (sample_idle_take idle f c)))
        (Nat.lt_irrefl 0)
     | .inr moves => (sample_moves_taking_iff moves).mpr (taking (ρ n)) f c mem takes⟩

/-! ### What a stretch takes and gives -/

/-- Over any stretch, what is taken from a condition read through a stuttering totals what is
taken from it over the stretch read, each relatum listed once. -/
theorem stutter_taken (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) (once : L.Once)
    (c : C) (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (fun n => (L.sample ρ).taken n c) =
      total (steps (ρ N) d) (fun t => L.taken t c) :=
  stutter_total moving (fun _ idle => taken_nil (sample_idle_present idle) c)
    (fun n moves => sample_moves_taken moves (once (ρ n)) c) N m d reads

/-- And what is given to it totals what is given to it over the stretch read. -/
theorem stutter_given (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1) (once : L.Once)
    (c : C) (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (fun n => (L.sample ρ).given n c) =
      total (steps (ρ N) d) (fun t => L.given t c) :=
  stutter_total moving (fun _ idle => given_nil (sample_idle_present idle) c)
    (fun n moves => sample_moves_given moves (once (ρ n)) c) N m d reads

end Flow


/-! ## Recurrence, totals and counts read through a stuttering -/

section Stretches

variable {ρ : Nat → Nat}

/-- An event read through a stuttering, absent at the idle steps and occurring at a moving step
exactly where it occurs at the step read, recurs exactly where it recurs. -/
theorem stutter_recurs_iff (stutter : Stutter ρ) {E E' : Nat → Prop}
    (idle : ∀ n, ρ (n + 1) = ρ n → ¬ E' n) (moves : ∀ n, ρ (n + 1) = ρ n + 1 → (E' n ↔ E (ρ n))) :
    (∀ N, ∃ n, N ≤ n ∧ E' n) ↔ ∀ N, ∃ t, N ≤ t ∧ E t :=
  ⟨fun recurs N => match stutter.2.2 N with
     | ⟨m, reads⟩ => match recurs m with
       | ⟨n, later, event⟩ => match stutter.2.1 n with
         | .inl still => absurd event (idle n still)
         | .inr next => ⟨ρ n, Nat.le_trans (Nat.le_of_eq reads.symm) (Stutter.mono stutter.2.1 later),
             (moves n next).mp event⟩,
   fun recurs N => match recurs N with
     | ⟨t, later, event⟩ => match stutter.moving t with
       | ⟨n, here, next⟩ => ⟨n, Nat.le_trans later (Nat.le_trans (Nat.le_of_eq here.symm)
            (stutter.le_self n)),
          (moves n next).mpr (Eq.subst (motive := E) here.symm event)⟩⟩

variable (moving : ∀ n, ρ (n + 1) = ρ n ∨ ρ (n + 1) = ρ n + 1)
include moving

/-- Over any stretch, an amount read through a stuttering rises in all what it rises in all over
the stretch read. -/
theorem stutter_risen (q : Nat → Nat) (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (rise fun k => q (ρ k)) = total (steps (ρ N) d) (rise q) :=
  stutter_total moving (fun _ idle => rise_idle q idle) (fun _ moves => rise_moves q moves) N m d reads

/-- And falls in all what it falls in all over the stretch read. -/
theorem stutter_fallen (q : Nat → Nat) (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (fall fun k => q (ρ k)) = total (steps (ρ N) d) (fall q) :=
  stutter_total moving (fun _ idle => fall_idle q idle) (fun _ moves => fall_moves q moves) N m d reads

/-- The steps at which it rises number those of the stretch read. -/
theorem stutter_rise_count (q : Nat → Nat) (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    count (steps N m) (rise fun k => q (ρ k)) = count (steps (ρ N) d) (rise q) :=
  stutter_total (g := fun t => sign (rise q t)) (g' := fun k => sign (rise (fun k => q (ρ k)) k))
    moving (fun _ idle => congrArg sign (rise_idle q idle))
    (fun _ moves => congrArg sign (rise_moves q moves)) N m d reads

/-- And the steps at which it falls. -/
theorem stutter_fall_count (q : Nat → Nat) (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    count (steps N m) (fall fun k => q (ρ k)) = count (steps (ρ N) d) (fall q) :=
  stutter_total (g := fun t => sign (fall q t)) (g' := fun k => sign (fall (fun k => q (ρ k)) k))
    moving (fun _ idle => congrArg sign (fall_idle q idle))
    (fun _ moves => congrArg sign (fall_moves q moves)) N m d reads

variable {α : Type} {as : List α} {p : α → Nat → Prop} [∀ a t, Decidable (p a t)]

/-- Over any stretch, the members of a finite family coming to be, read through a stuttering,
number those coming to be over the stretch read. -/
theorem stutter_comings (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (comings as fun a k => p a (ρ k)) = total (steps (ρ N) d) (comings as p) :=
  stutter_total moving
    (fun _ idle => (total_congr (fun _ => mark_zero (not_comesToBe_idle idle)) as).trans
      (total_zero as))
    (fun _ moves => total_congr (fun _ => mark_iff (comesToBe_moves moves)) as) N m d reads

/-- And those ceasing to be number those ceasing to be over the stretch read. -/
theorem stutter_ceasings (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (ceasings as fun a k => p a (ρ k)) = total (steps (ρ N) d) (ceasings as p) :=
  stutter_total moving
    (fun _ idle => (total_congr (fun _ => mark_zero (not_ceasesToBe_idle idle)) as).trans
      (total_zero as))
    (fun _ moves => total_congr (fun _ => mark_iff (ceasesToBe_moves moves)) as) N m d reads

end Stretches

/-! ## A web read through a stuttering -/

namespace Web

variable {W : Web F C} {ρ : Nat → Nat}

/-- Activity needing support survives a stuttering and returns from it. -/
theorem stutter_dependent_iff (stutter : Stutter ρ) : (W.sample ρ).Dependent ↔ W.Dependent :=
  ⟨fun dependent t f active => match stutter.2.2 t with
     | ⟨n, here⟩ => Eq.subst (motive := fun k => W.Supported k f) here
        (dependent n f (Eq.subst (motive := fun k => W.active k f) here.symm active)),
   sample_dependent ρ⟩

/-- A relatum standing exactly while active does so read through a stuttering, and
conversely. -/
theorem stutter_embodied_iff {X : Type} {W : Web X X} (stutter : Stutter ρ) {x : X} :
    (W.sample ρ).Embodied x ↔ W.Embodied x :=
  ⟨fun embodied t => match stutter.2.2 t with
     | ⟨n, here⟩ => Eq.subst (motive := fun k => (W.active k x ↔ 0 < W.level k x)) here
        (embodied n),
   fun embodied n => embodied (ρ n)⟩

end Web

/-! ## Descent read through a stuttering -/

namespace Flow

variable {X : Type} [DecidableEq X] {L : Flow X X} {W : Web X X} {ρ : Nat → Nat} {n : Nat}

/-- Nothing descends across an idle step. -/
theorem sample_idle_not_descends (idle : ρ (n + 1) = ρ n) {x g : X} :
    ¬ (L.sample ρ).DescendsAt (W.sample ρ) n x g :=
  fun ⟨_, gives, _⟩ => absurd (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (sample_idle_give idle g x)))
    (Nat.lt_irrefl 0)

/-- Across a moving step a relatum descends exactly where it descends across the step read. -/
theorem sample_moves_descends_iff (moves : ρ (n + 1) = ρ n + 1) {x g : X} :
    (L.sample ρ).DescendsAt (W.sample ρ) n x g ↔ L.DescendsAt W (ρ n) x g :=
  ⟨fun ⟨mem, gives, comes⟩ =>
     have held := (sample_moves_mem moves).mp mem
     ⟨held, Nat.lt_of_lt_of_le gives (Nat.le_of_eq (sample_moves_give moves held x)),
      (comesToBe_moves (p := fun k => 0 < W.level k x) moves).mp comes⟩,
   fun ⟨held, gives, comes⟩ =>
     ⟨(sample_moves_mem moves).mpr held,
      Nat.lt_of_lt_of_le gives (Nat.le_of_eq (sample_moves_give moves held x).symm),
      (comesToBe_moves (p := fun k => 0 < W.level k x) moves).mpr comes⟩⟩

/-- Transmission within a bound survives a stuttering and returns from it, with the same
bound. The coarse steps of `Becoming.Sampling`'s `Delay` read a descent the fine steps lack
because one coarse step holds the gift and the coming to stand; a stuttering never puts two
fine steps in one. -/
theorem stutter_transmitsWithin_iff (stutter : Stutter ρ) {c : X} {δ : Nat} :
    (L.sample ρ).TransmitsWithin (W.sample ρ) c δ ↔ L.TransmitsWithin W c δ :=
  ⟨fun transmits t x g descends depends => match stutter.moving t with
     | ⟨n, here, moves⟩ =>
       have after : ρ (n + 1) = t + 1 := moves.trans (congrArg (· + 1) here)
       have inherited := transmits n x g
         ((sample_moves_descends_iff moves).mpr
           (Eq.subst (motive := fun k => L.DescendsAt W k x g) here.symm descends))
         (Eq.subst (motive := fun k => W.requires k x c) after.symm depends)
       ⟨Eq.subst (motive := fun k => W.requires k g c) here inherited.1,
        Eq.subst (motive := fun k => W.need k x c ≤ W.need t g c + δ) after
          (Eq.subst (motive := fun k => W.need (ρ (n + 1)) x c ≤ W.need k g c + δ) here
            inherited.2)⟩,
   fun transmits n x g descends depends => match stutter.2.1 n with
     | .inl idle => absurd descends (sample_idle_not_descends idle)
     | .inr moves =>
       have inherited := transmits (ρ n) x g ((sample_moves_descends_iff moves).mp descends)
         (Eq.subst (motive := fun k => W.requires k x c) moves depends)
       ⟨inherited.1, Eq.subst (motive := fun k => W.need k x c ≤ W.need (ρ n) g c + δ) moves.symm
          inherited.2⟩⟩

end Flow


/-! ## Worlds read through a stuttering -/

/-- Recurring at some relatum is recurring of there being one. -/
theorem recurs_shape {α : Type} {P : Nat → α → Prop} :
    (∀ N, ∃ t x, N ≤ t ∧ P t x) ↔ ∀ N, ∃ t, N ≤ t ∧ ∃ x, P t x :=
  ⟨fun recurs N => match recurs N with | ⟨t, x, later, p⟩ => ⟨t, later, x, p⟩,
   fun recurs N => match recurs N with | ⟨t, later, x, p⟩ => ⟨t, x, later, p⟩⟩

namespace World

variable {w : World} [DecidableEq w.Relatum] {ρ : Nat → Nat}

/-- Inserting idle steps leaves the premises as they were, and so does removing them: read
through a stuttering, a world meets balance (each relatum listed once at each step),
dissipation, only active relata giving, only active relata taking, activity needing support,
embodiment and bounded transmission exactly where it meets them. -/
theorem stutter_premises_iff (stutter : Stutter ρ) (once : w.flow.Once) :
    ((w.sample ρ).Balanced ↔ w.Balanced) ∧ ((w.sample ρ).Dissipative ↔ w.Dissipative) ∧
    ((w.sample ρ).Acting ↔ w.Acting) ∧ ((w.sample ρ).Taking ↔ w.Taking) ∧
    ((w.sample ρ).Dependent ↔ w.Dependent) ∧ ((w.sample ρ).Embodied ↔ w.Embodied) ∧
    ((w.sample ρ).Transmitting ↔ w.Transmitting) :=
  ⟨Flow.stutter_balances_iff (F := w.Relatum) stutter once,
   Flow.stutter_dissipative_iff (F := w.Relatum) stutter,
   Flow.stutter_acting_iff (F := w.Relatum) stutter, Flow.stutter_taking_iff (F := w.Relatum) stutter,
   Web.stutter_dependent_iff stutter,
   ⟨fun embodied x => (Web.stutter_embodied_iff stutter).mp (embodied x),
    fun embodied x => (Web.stutter_embodied_iff stutter).mpr (embodied x)⟩,
   ⟨fun ⟨δ, transmits⟩ => ⟨δ, fun c =>
      (Flow.stutter_transmitsWithin_iff (X := w.Relatum) stutter).mp (transmits c)⟩,
    fun ⟨δ, transmits⟩ => ⟨δ, fun c =>
      (Flow.stutter_transmitsWithin_iff (X := w.Relatum) stutter).mpr (transmits c)⟩⟩⟩

/-- A census survives a stuttering. -/
theorem stutter_counted (counted : w.Counted) : (w.sample ρ).Counted :=
  sample_counted (w := w) (σ := ρ) counted

/-- And returns from it where each step is read at a step given for it. -/
theorem stutter_counted_of_section {σ : Nat → Nat} (section_ : ∀ s, ρ (σ s) = s)
    (counted : (w.sample ρ).Counted) : w.Counted :=
  match counted with
  | ⟨alive, census⟩ => ⟨fun s => alive (σ s), fun s =>
      Eq.subst (motive := fun k => Distinct (alive (σ s)) ∧ ∀ x, w.web.active k x ↔ x ∈ alive (σ s))
        (section_ s) (census (σ s))⟩

/-- Arising recurs read through a stuttering exactly where it recurs. -/
theorem stutter_arisingRecurs_iff (stutter : Stutter ρ) :
    (w.sample ρ).ArisingRecurs ↔ w.ArisingRecurs :=
  recurs_shape.trans ((stutter_recurs_iff stutter (E := fun t => ∃ x, w.web.Arises t x)
    (fun _ idle ⟨x, arises⟩ => not_comesToBe_idle (p := fun k => w.web.active k x) idle arises)
    (fun _ moves => ⟨fun ⟨x, arises⟩ => ⟨x, (comesToBe_moves (p := fun k => w.web.active k x)
        moves).mp arises⟩,
      fun ⟨x, arises⟩ => ⟨x, (comesToBe_moves (p := fun k => w.web.active k x) moves).mpr
        arises⟩⟩)).trans recurs_shape.symm)

/-- Ceasing recurs read through a stuttering exactly where it recurs. -/
theorem stutter_ceasingRecurs_iff (stutter : Stutter ρ) :
    (w.sample ρ).CeasingRecurs ↔ w.CeasingRecurs :=
  recurs_shape.trans ((stutter_recurs_iff stutter (E := fun t => ∃ x, w.web.Ceases t x)
    (fun _ idle ⟨x, ceases⟩ => not_ceasesToBe_idle (p := fun k => w.web.active k x) idle ceases)
    (fun _ moves => ⟨fun ⟨x, ceases⟩ => ⟨x, (ceasesToBe_moves (p := fun k => w.web.active k x)
        moves).mp ceases⟩,
      fun ⟨x, ceases⟩ => ⟨x, (ceasesToBe_moves (p := fun k => w.web.active k x) moves).mpr
        ceases⟩⟩)).trans recurs_shape.symm)

/-- Some standing changes at arbitrarily late steps read through a stuttering exactly where it
does. -/
theorem stutter_change_recurs_iff (stutter : Stutter ρ) :
    (∀ N, ∃ t, N ≤ t ∧ ∃ c, (w.sample ρ).web.Rises t c ∨ (w.sample ρ).web.Falls t c) ↔
      ∀ N, ∃ t, N ≤ t ∧ ∃ c, w.web.Rises t c ∨ w.web.Falls t c :=
  have flat : ∀ n : Nat, ρ (n + 1) = ρ n → ∀ c : w.Relatum,
      ¬ ((w.sample ρ).web.Rises n c ∨ (w.sample ρ).web.Falls n c) := fun _ idle c changes =>
    match changes with
    | .inl rises => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (excess_pos.mpr rises)
        (Nat.le_of_eq (rise_idle (fun k => w.web.level k c) idle)))
    | .inr falls => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (excess_pos.mpr falls)
        (Nat.le_of_eq (fall_idle (fun k => w.web.level k c) idle)))
  have moved : ∀ n : Nat, ρ (n + 1) = ρ n + 1 → ∀ c : w.Relatum,
      (((w.sample ρ).web.Rises n c ∨ (w.sample ρ).web.Falls n c) ↔
        (w.web.Rises (ρ n) c ∨ w.web.Falls (ρ n) c)) := fun n moves c =>
    have up : (w.sample ρ).web.Rises n c ↔ w.web.Rises (ρ n) c :=
      excess_pos.symm.trans ((Iff.of_eq (congrArg (0 < ·)
        (rise_moves (fun k => w.web.level k c) moves))).trans excess_pos)
    have down : (w.sample ρ).web.Falls n c ↔ w.web.Falls (ρ n) c :=
      excess_pos.symm.trans ((Iff.of_eq (congrArg (0 < ·)
        (fall_moves (fun k => w.web.level k c) moves))).trans excess_pos)
    ⟨fun changes => match changes with
      | .inl rises => .inl (up.mp rises)
      | .inr falls => .inr (down.mp falls),
     fun changes => match changes with
      | .inl rises => .inl (up.mpr rises)
      | .inr falls => .inr (down.mpr falls)⟩
  stutter_recurs_iff stutter (fun n idle ⟨c, changes⟩ => flat n idle c changes)
    fun n moves => ⟨fun ⟨c, changes⟩ => ⟨c, (moved n moves c).mp changes⟩,
      fun ⟨c, changes⟩ => ⟨c, (moved n moves c).mpr changes⟩⟩

end World

/-! ## What a stuttering changes: rates and durations -/

namespace Flow

variable [DecidableEq F] {L : Flow F C} {ρ : Nat → Nat} {n : Nat}

/-- Nothing takes across an idle step. -/
theorem sample_idle_takers (idle : ρ (n + 1) = ρ n) (cs : List C) : (L.sample ρ).takers cs n = 0 :=
  congrArg (fun l => count l fun f => total cs ((L.sample ρ).take n f)) (sample_idle_present idle)

/-- Rates are counted per step. Read through a reading with idle steps at arbitrarily late
steps, no flow is more without end: at an idle step nothing takes. -/
theorem sample_not_more (idles : ∀ N, ∃ n, N ≤ n ∧ ρ (n + 1) = ρ n) (cs : List C) :
    ¬ (L.sample ρ).More cs :=
  fun more => match more 1 with
  | ⟨T, many⟩ => match idles T with
    | ⟨n, later, idle⟩ => Nat.not_succ_le_zero 0
        (Nat.le_trans (many n later) (Nat.le_of_eq (sample_idle_takers idle cs)))

end Flow

namespace Web

variable {W : Web F C} {ρ : Nat → Nat} {n : Nat}

/-- Durations are counted per step. A reserve read through a stuttering does not carry across
an idle step at which a relatum is active beyond support: nothing changes there, the reserve
included, while carrying asks it to fall. -/
theorem sample_idle_not_carries (idle : ρ (n + 1) = ρ n) {f : F}
    (unsupported : ¬ W.Supported (ρ n) f) (active : W.active (ρ n) f) (r : Nat → F → Nat) :
    ¬ (W.sample ρ).Carries fun k => r (ρ k) :=
  fun carries => Nat.lt_irrefl (r (ρ n) f)
    (Eq.subst (motive := fun k => r k f < r (ρ n) f) idle ((carries n f unsupported).2 active))

end Web

/-! ### The halving: every step read twice -/

namespace Halving

/-- `Pulse.half` reads every step twice, `0, 0, 1, 1, 2, 2, …`: a stuttering idle at every
even step. -/
theorem steps_ : ∀ n, Pulse.half (n + 1) = Pulse.half n ∨ Pulse.half (n + 1) = Pulse.half n + 1
  | 0 => .inl rfl
  | 1 => .inr rfl
  | n + 2 => match steps_ n with
    | .inl idle => .inl (congrArg (· + 1) idle)
    | .inr moves => .inr (congrArg (· + 1) moves)

theorem stutter : Stutter Pulse.half :=
  ⟨rfl, steps_, fun s => ⟨2 * s, Pulse.half_even s⟩⟩

/-- Idle at every even step, so at arbitrarily late steps. -/
theorem idles (N : Nat) : ∃ n, N ≤ n ∧ Pulse.half (n + 1) = Pulse.half n :=
  ⟨2 * N, Nat.le_trans (Nat.le_add_right N N) (Nat.le_of_eq (Nat.two_mul N).symm),
   (Pulse.half_odd N).trans (Pulse.half_even N).symm⟩

end Halving

namespace Expansion

instance kind_decided : DecidableEq Kind := fun a b => match a, b with
  | .renewer, .renewer => .isTrue rfl
  | .grower, .grower => .isTrue rfl
  | .renewer, .grower => .isFalse fun same => Kind.noConfusion same
  | .grower, .renewer => .isFalse fun same => Kind.noConfusion same

/-- More without end is not kept by inserting idle steps: the expansion is more without end,
and read with every step taken twice it is not. -/
theorem more_step_relative : flow.More [()] ∧ ¬ (flow.sample Pulse.half).More [()] :=
  ⟨more.2.2.2.2.2.2, Flow.sample_not_more Halving.idles [()]⟩

end Expansion

namespace Lapse

/-- One relatum active at the first step only, depending at need one on a condition standing
at nothing: never supported. -/
def web : Web Unit Unit where
  level _ _ := 0
  active t _ := t = 0
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := False

/-- A reserve of one at the first step, none after. -/
def reserve : Nat → Unit → Nat
  | 0, _ => 1
  | _ + 1, _ => 0

theorem unsupported (t : Nat) : ¬ web.Supported t () :=
  fun supported => Nat.not_succ_le_zero 0 (supported () trivial)

/-- A reserve of one carries it. -/
theorem carried : web.Carries reserve
  | 0, (), _ => ⟨Nat.zero_le 1, fun _ => Nat.zero_lt_one⟩
  | _ + 1, (), _ => ⟨Nat.le_refl 0, fun active => Nat.noConfusion active⟩

/-- Read with every step taken twice, it is active beyond support at two steps, so every reserve
carrying it stands at two or more at the start: how long a reserve carries is counted in
steps. -/
theorem stuttered_reserve (r : Nat → Unit → Nat) (carries : (web.sample Pulse.half).Carries r) :
    2 ≤ r 0 () :=
  have first : r 1 () < r 0 () := (carries 0 () (unsupported 0)).2 rfl
  have second : r 2 () < r 1 () := (carries 1 () (unsupported 0)).2 rfl
  Nat.succ_le_of_lt (Nat.lt_of_le_of_lt
    (Nat.succ_le_of_lt (Nat.lt_of_le_of_lt (Nat.zero_le _) second)) first)

/-- So the reserve law is step-relative: the world is carried by a reserve of one, the world read
with every step taken twice by none below two. -/
theorem reserve_step_relative :
    web.Carries reserve ∧ reserve 0 () = 1 ∧
      ∀ r, (web.sample Pulse.half).Carries r → 2 ≤ r 0 () :=
  ⟨carried, rfl, stuttered_reserve⟩

end Lapse


/-! ## Two exchanges taken in the other order -/

section Moving

/-- With the same added before, the rest is the same. -/
theorem add_left_cancel_of_eq {a x y : Nat} (same : a + x = a + y) : x = y :=
  add_right_cancel a ((Nat.add_comm x a).trans (same.trans (Nat.add_comm a y)))

theorem ne_succ_of_ne {n t : Nat} (other : n ≠ t) : n + 1 ≠ t + 1 :=
  fun same => other (Nat.succ.inj same)

theorem ne_first {t : Nat} : t ≠ t + 1 := Nat.ne_of_lt (Nat.lt_succ_self t)

theorem ne_last {t : Nat} : t + 2 ≠ t + 1 := Nat.ne_of_gt (Nat.lt_succ_self (t + 1))

variable {α : Type}

/-- `q'` is `q` with the change `q` makes across the steps from `t` and `t + 1` made across the
other of the two: it agrees with `q` away from the step between them, and there shows `q` at `t`
where `q` changes only across the first step, and `q` after both where `q` changes only across
the second. A change made across both steps is not moved. -/
def Moved (q q' : Nat → α) (t : Nat) : Prop :=
  (∀ n, n ≠ t + 1 → q' n = q n) ∧
    ((q (t + 1) = q (t + 2) ∧ q' (t + 1) = q t) ∨ (q t = q (t + 1) ∧ q' (t + 1) = q (t + 2)))

variable {q q' : Nat → α} {t : Nat}

theorem Moved.at_first (moved : Moved q q' t) : q' t = q t :=
  moved.1 t ne_first

theorem Moved.at_last (moved : Moved q q' t) : q' (t + 2) = q (t + 2) :=
  moved.1 (t + 2) ne_last

/-- Moving is symmetric: `q` is `q'` with its change moved back. -/
theorem Moved.symm (moved : Moved q q' t) : Moved q' q t :=
  ⟨fun n away => (moved.1 n away).symm,
   match moved.2 with
   | .inl ⟨still, shows⟩ => .inr ⟨moved.at_first.trans shows.symm, still.trans moved.at_last.symm⟩
   | .inr ⟨still, shows⟩ => .inl ⟨shows.trans moved.at_last.symm, still.symm.trans moved.at_first.symm⟩⟩

/-- Coming to be is moved with the change: across the first step it comes to be where it came to
be across the second. -/
theorem Moved.comesToBe_first {p p' : Nat → Prop} (moved : Moved p p' t) :
    ComesToBe p' t ↔ ComesToBe p (t + 1) :=
  match moved.2 with
  | .inl ⟨still, shows⟩ =>
    ⟨fun ⟨absent, held⟩ => absurd (cast (shows.trans moved.at_first.symm) held) absent,
     fun ⟨absent, held⟩ => absurd (cast still.symm held) absent⟩
  | .inr ⟨still, shows⟩ =>
    ⟨fun ⟨absent, held⟩ => ⟨fun yes => absent (cast moved.at_first.symm (cast still.symm yes)),
        cast shows held⟩,
     fun ⟨absent, held⟩ => ⟨fun yes => absent (cast still (cast moved.at_first yes)),
        cast shows.symm held⟩⟩

/-- Ceasing to be likewise. -/
theorem Moved.ceasesToBe_first {p p' : Nat → Prop} (moved : Moved p p' t) :
    CeasesToBe p' t ↔ CeasesToBe p (t + 1) :=
  match moved.2 with
  | .inl ⟨still, shows⟩ =>
    ⟨fun ⟨held, absent⟩ => absurd (cast (shows.trans moved.at_first.symm).symm held) absent,
     fun ⟨held, absent⟩ => absurd (cast still held) absent⟩
  | .inr ⟨still, shows⟩ =>
    ⟨fun ⟨held, absent⟩ => ⟨cast still (cast moved.at_first held),
        fun yes => absent (cast shows.symm yes)⟩,
     fun ⟨held, absent⟩ => ⟨cast moved.at_first.symm (cast still.symm held),
        fun yes => absent (cast shows yes)⟩⟩

/-- Across the second step it comes to be where it came to be across the first. -/
theorem Moved.comesToBe_second {p p' : Nat → Prop} (moved : Moved p p' t) :
    ComesToBe p' (t + 1) ↔ ComesToBe p t :=
  moved.symm.comesToBe_first.symm

theorem Moved.ceasesToBe_second {p p' : Nat → Prop} (moved : Moved p p' t) :
    CeasesToBe p' (t + 1) ↔ CeasesToBe p t :=
  moved.symm.ceasesToBe_first.symm

/-- Away from the two steps nothing is moved. -/
theorem Moved.away (moved : Moved q q' t) {n : Nat} (other : n ≠ t) (other' : n ≠ t + 1) :
    q' n = q n ∧ q' (n + 1) = q (n + 1) :=
  ⟨moved.1 n other', moved.1 (n + 1) (ne_succ_of_ne other)⟩

theorem Moved.comesToBe_away {p p' : Nat → Prop} (moved : Moved p p' t) {n : Nat} (other : n ≠ t)
    (other' : n ≠ t + 1) : ComesToBe p' n ↔ ComesToBe p n :=
  match moved.away other other' with
  | ⟨now, next⟩ => ⟨fun ⟨absent, held⟩ => ⟨fun yes => absent (cast now.symm yes), cast next held⟩,
      fun ⟨absent, held⟩ => ⟨fun yes => absent (cast now yes), cast next.symm held⟩⟩

theorem Moved.ceasesToBe_away {p p' : Nat → Prop} (moved : Moved p p' t) {n : Nat} (other : n ≠ t)
    (other' : n ≠ t + 1) : CeasesToBe p' n ↔ CeasesToBe p n :=
  match moved.away other other' with
  | ⟨now, next⟩ => ⟨fun ⟨held, absent⟩ => ⟨cast now held, fun yes => absent (cast next.symm yes)⟩,
      fun ⟨held, absent⟩ => ⟨cast now.symm held, fun yes => absent (cast next yes)⟩⟩

end Moving


/-! ### Amounts: the two orders add to the same -/

section Amounts

variable {t : Nat}

/-- The amounts `q'` take the two steps' changes of `q` in the other order: they agree with `q`
away from the step between, and there the amounts of the two orders add to the amounts at the
two ends. -/
def Exchanged (q q' : Nat → Nat) (t : Nat) : Prop :=
  (∀ n, n ≠ t + 1 → q' n = q n) ∧ q' (t + 1) + q (t + 1) = q t + q (t + 2)

/-- An amount whose change is moved exchanges the two steps' changes. -/
theorem Moved.exchanged {q q' : Nat → Nat} (moved : Moved q q' t) : Exchanged q q' t :=
  ⟨moved.1, match moved.2 with
    | .inl ⟨still, shows⟩ => congr (congrArg (· + ·) shows) still
    | .inr ⟨still, shows⟩ => (congr (congrArg (· + ·) shows) still.symm).trans (Nat.add_comm _ _)⟩

/-- So does the total of a finite family of such amounts, as a family's total standing. -/
theorem Exchanged.sum {β : Type} {as : List β} {q q' : β → Nat → Nat}
    (each : ∀ a, a ∈ as → Exchanged (q a) (q' a) t) :
    Exchanged (fun n => total as fun a => q a n) (fun n => total as fun a => q' a n) t :=
  ⟨fun n other => total_congr_on fun a mem => (each a mem).1 n other,
   (total_add (fun a => q' a (t + 1)) (fun a => q a (t + 1)) as).symm.trans
     ((total_congr_on fun a mem => (each a mem).2).trans
       (total_add (fun a => q a t) (fun a => q a (t + 2)) as))⟩

variable {q q' : Nat → Nat}

/-- Across the first step the amount rises as it rose across the second. -/
theorem Exchanged.rise_first (ex : Exchanged q q' t) : rise q' t = rise q (t + 1) :=
  (congrArg (excess (q' (t + 1))) (ex.1 t ne_first)).trans (excess_of_sum ex.2)

/-- Across the second step it rises as it rose across the first. -/
theorem Exchanged.rise_second (ex : Exchanged q q' t) : rise q' (t + 1) = rise q t :=
  (congrArg (fun k => excess k (q' (t + 1))) (ex.1 (t + 2) ne_last)).trans
    (excess_of_sum ((Nat.add_comm _ _).trans ex.2.symm))

/-- Across the first step it falls as it fell across the second. -/
theorem Exchanged.fall_first (ex : Exchanged q q' t) : fall q' t = fall q (t + 1) :=
  (congrArg (fun k => excess k (q' (t + 1))) (ex.1 t ne_first)).trans (excess_of_sum ex.2.symm)

/-- Across the second step it falls as it fell across the first. -/
theorem Exchanged.fall_second (ex : Exchanged q q' t) : fall q' (t + 1) = fall q t :=
  (congrArg (excess (q' (t + 1))) (ex.1 (t + 2) ne_last)).trans
    (excess_of_sum (ex.2.trans (Nat.add_comm _ _)))

/-- Away from the two steps it rises as it rose. -/
theorem Exchanged.rise_away (ex : Exchanged q q' t) {n : Nat} (other : n ≠ t) (other' : n ≠ t + 1) :
    rise q' n = rise q n :=
  show excess (q' (n + 1)) (q' n) = excess (q (n + 1)) (q n) from
  congr (congrArg excess (ex.1 (n + 1) (ne_succ_of_ne other))) (ex.1 n other')

/-- And falls as it fell. -/
theorem Exchanged.fall_away (ex : Exchanged q q' t) {n : Nat} (other : n ≠ t) (other' : n ≠ t + 1) :
    fall q' n = fall q n :=
  show excess (q' n) (q' (n + 1)) = excess (q n) (q (n + 1)) from
  congr (congrArg excess (ex.1 n other')) (ex.1 (n + 1) (ne_succ_of_ne other))

/-- Two equations of the same sides are one. -/
theorem eq_iff_of_sides {a b a' b' : Nat} (left : a = a') (right : b = b') : a = b ↔ a' = b' :=
  ⟨fun same => left.symm.trans (same.trans right), fun same => left.trans (same.trans right.symm)⟩

/-- Balance across a step is the balance of the change: the amount after the step with what is
taken is the amount before with what is given exactly when its rise with what is taken is its
fall with what is given. -/
theorem balance_iff_change {q : Nat → Nat} {n T G : Nat} :
    q (n + 1) + T = q n + G ↔ rise q n + T = fall q n + G :=
  have turn := across q n
  ⟨fun balance => add_left_cancel_of_eq (a := q n) (calc
      q n + (rise q n + T) = (q (n + 1) + fall q n) + T := (Nat.add_assoc _ _ _).symm.trans
          (congrArg (· + T) turn.symm)
      _ = (q (n + 1) + T) + fall q n := Nat.add_right_comm _ _ _
      _ = (q n + G) + fall q n := congrArg (· + fall q n) balance
      _ = q n + (fall q n + G) := (Nat.add_right_comm _ _ _).trans (Nat.add_assoc _ _ _)),
   fun change => add_right_cancel (fall q n) (calc
      (q (n + 1) + T) + fall q n = (q (n + 1) + fall q n) + T := Nat.add_right_comm _ _ _
      _ = q n + (rise q n + T) := (congrArg (· + T) turn).trans (Nat.add_assoc _ _ _)
      _ = q n + (fall q n + G) := congrArg (q n + ·) change
      _ = (q n + G) + fall q n := (Nat.add_assoc _ _ _).symm.trans (Nat.add_right_comm _ _ _))⟩

/-- Balance moves with the exchange: across the first step, with the second step's taking and
giving, an amount balances exactly where it balanced across the second step. -/
theorem Exchanged.balance_first (ex : Exchanged q q' t) {T G T' G' : Nat} (taken : T' = T)
    (given : G' = G) : q' (t + 1) + T' = q' t + G' ↔ q (t + 1 + 1) + T = q (t + 1) + G :=
  balance_iff_change.trans ((eq_iff_of_sides (congr (congrArg (· + ·) ex.rise_first) taken)
    (congr (congrArg (· + ·) ex.fall_first) given)).trans balance_iff_change.symm)

/-- And across the second step, with the first step's, exactly where it balanced across the
first. -/
theorem Exchanged.balance_second (ex : Exchanged q q' t) {T G T' G' : Nat} (taken : T' = T)
    (given : G' = G) : q' (t + 1 + 1) + T' = q' (t + 1) + G' ↔ q (t + 1) + T = q t + G :=
  balance_iff_change.trans ((eq_iff_of_sides (congr (congrArg (· + ·) ex.rise_second) taken)
    (congr (congrArg (· + ·) ex.fall_second) given)).trans balance_iff_change.symm)

end Amounts

/-! ### Totals over a stretch holding both steps -/

/-- A quantity of each step whose values at two adjacent steps are exchanged, and the same
elsewhere, totals the same over any stretch holding both steps. -/
theorem total_swapped {g g' : Nat → Nat} {t : Nat} (first : g' t = g (t + 1))
    (second : g' (t + 1) = g t) (away : ∀ n, n ≠ t → n ≠ t + 1 → g' n = g n) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) : total (steps S m) g' = total (steps S m) g :=
  match le_dest from_, le_dest to with
  | ⟨a, ta⟩, ⟨r, mr⟩ =>
    have length : m = a + (2 + r) := add_right_cancel S ((Nat.add_comm m S).trans (mr.trans
      ((congrArg (fun k => k + 2 + r) ta).trans ((Nat.add_assoc _ 2 r).trans
        ((Nat.add_assoc S a (2 + r)).trans (Nat.add_comm S _))))))
    have split : ∀ h : Nat → Nat, total (steps S m) h =
        total (steps S a) h + (total (steps (S + a) 2) h + total (steps (S + a + 2) r) h) :=
      fun h => (congrArg (fun k => total (steps S k) h) length).trans
        ((total_steps_add h S a (2 + r)).trans
          (congrArg (total (steps S a) h + ·) (total_steps_add h (S + a) 2 r)))
    have before : total (steps S a) g' = total (steps S a) g := total_congr_on fun k mem =>
      have below : k < t := Nat.lt_of_lt_of_le (steps_within mem) (Nat.le_of_eq ta.symm)
      away k (Nat.ne_of_lt below) (Nat.ne_of_lt (Nat.lt_succ_of_lt below))
    have middle : total (steps (S + a) 2) g' = total (steps (S + a) 2) g :=
      show g' (S + a) + (g' (S + a + 1) + 0) = g (S + a) + (g (S + a + 1) + 0) from
      Eq.subst (motive := fun k => g' k + (g' (k + 1) + 0) = g k + (g (k + 1) + 0)) ta
        ((congr (congrArg (· + ·) first) (congrArg (· + 0) second)).trans
          (Nat.add_left_comm _ _ _))
    have after : total (steps (S + a + 2) r) g' = total (steps (S + a + 2) r) g :=
      total_congr_on fun k mem =>
      have above : t + 2 ≤ k := Nat.le_trans (Nat.le_of_eq (congrArg (· + 2) ta)) (steps_mem mem)
      away k (Nat.ne_of_gt (Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right Nat.zero_lt_two) above))
        (Nat.ne_of_gt (Nat.lt_of_lt_of_le (Nat.lt_succ_self (t + 1)) above))
    (split g').trans ((congr (congrArg (· + ·) before)
      (congr (congrArg (· + ·) middle) after)).trans (split g).symm)

/-- So the amounts' rises over a stretch holding both steps total the same. -/
theorem Exchanged.risen {q q' : Nat → Nat} {t : Nat} (ex : Exchanged q q' t) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) : total (steps S m) (rise q') = total (steps S m) (rise q) :=
  total_swapped ex.rise_first ex.rise_second (fun _ other other' => ex.rise_away other other')
    from_ to

/-- And their falls. -/
theorem Exchanged.fallen {q q' : Nat → Nat} {t : Nat} (ex : Exchanged q q' t) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) : total (steps S m) (fall q') = total (steps S m) (fall q) :=
  total_swapped ex.fall_first ex.fall_second (fun _ other other' => ex.fall_away other other')
    from_ to

/-- And the steps at which they fall number the same. -/
theorem Exchanged.fall_count {q q' : Nat → Nat} {t : Nat} (ex : Exchanged q q' t) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) : count (steps S m) (fall q') = count (steps S m) (fall q) :=
  total_swapped (g := fun n => sign (fall q n)) (g' := fun n => sign (fall q' n))
    (congrArg sign ex.fall_first) (congrArg sign ex.fall_second)
    (fun _ other other' => congrArg sign (ex.fall_away other other')) from_ to

/-- And the steps at which they rise. -/
theorem Exchanged.rise_count {q q' : Nat → Nat} {t : Nat} (ex : Exchanged q q' t) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) : count (steps S m) (rise q') = count (steps S m) (rise q) :=
  total_swapped (g := fun n => sign (rise q n)) (g' := fun n => sign (rise q' n))
    (congrArg sign ex.rise_first) (congrArg sign ex.rise_second)
    (fun _ other other' => congrArg sign (ex.rise_away other other')) from_ to

/-- Over a stretch holding both steps, the members of a finite family coming to be number the
same where each member's change is moved. -/
theorem comings_moved {α : Type} {as : List α} {p p' : α → Nat → Prop} [∀ a n, Decidable (p a n)]
    [∀ a n, Decidable (p' a n)] {t : Nat} (moved : ∀ a, a ∈ as → Moved (p a) (p' a) t) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) :
    total (steps S m) (comings as p') = total (steps S m) (comings as p) :=
  total_swapped (total_congr_on fun a mem => mark_iff (moved a mem).comesToBe_first)
    (total_congr_on fun a mem => mark_iff (moved a mem).comesToBe_second)
    (fun _ other other' => total_congr_on fun a mem => mark_iff ((moved a mem).comesToBe_away other other'))
    from_ to

/-- And those ceasing to be. -/
theorem ceasings_moved {α : Type} {as : List α} {p p' : α → Nat → Prop} [∀ a n, Decidable (p a n)]
    [∀ a n, Decidable (p' a n)] {t : Nat} (moved : ∀ a, a ∈ as → Moved (p a) (p' a) t) {S m : Nat}
    (from_ : S ≤ t) (to : t + 2 ≤ S + m) :
    total (steps S m) (ceasings as p') = total (steps S m) (ceasings as p) :=
  total_swapped (total_congr_on fun a mem => mark_iff (moved a mem).ceasesToBe_first)
    (total_congr_on fun a mem => mark_iff (moved a mem).ceasesToBe_second)
    (fun _ other other' => total_congr_on fun a mem => mark_iff ((moved a mem).ceasesToBe_away other other'))
    from_ to


/-! ### Flows and webs taken in the other order -/

namespace Flow

/-- The exchange of `L` across the step from `n` is that of `L'` across the step from `m`: the
same relata take part, each taking and giving the same. -/
def SameExchange (L : Flow F C) (n : Nat) (L' : Flow F C) (m : Nat) : Prop :=
  L'.present m = L.present n ∧ ∀ f c, L'.take m f c = L.take n f c ∧ L'.give m f c = L.give n f c

/-- `L'` takes the exchanges of `L` across the steps from `t` and `t + 1` in the other order,
and every other exchange as `L` does. -/
def Commuted (L L' : Flow F C) (t : Nat) : Prop :=
  L.SameExchange (t + 1) L' t ∧ L.SameExchange t L' (t + 1) ∧
    ∀ n, n ≠ t → n ≠ t + 1 → L.SameExchange n L' n

variable {L L' : Flow F C} {n m t : Nat}

theorem SameExchange.symm (same : L.SameExchange n L' m) : L'.SameExchange m L n :=
  ⟨same.1.symm, fun f c => ⟨(same.2 f c).1.symm, (same.2 f c).2.symm⟩⟩

theorem Commuted.symm (flow : L.Commuted L' t) : L'.Commuted L t :=
  ⟨flow.2.1.symm, flow.1.symm, fun n other other' => (flow.2.2 n other other').symm⟩

theorem SameExchange.mem (same : L.SameExchange n L' m) {f : F} :
    f ∈ L'.present m ↔ f ∈ L.present n :=
  ⟨fun mem => Eq.subst (motive := fun l => f ∈ l) same.1 mem,
   fun mem => Eq.subst (motive := fun l => f ∈ l) same.1.symm mem⟩

theorem SameExchange.taken (same : L.SameExchange n L' m) (c : C) : L'.taken m c = L.taken n c :=
  (congrArg (fun l => total l fun f => L'.take m f c) same.1).trans
    (total_congr (fun f => (same.2 f c).1) (L.present n))

theorem SameExchange.given (same : L.SameExchange n L' m) (c : C) : L'.given m c = L.given n c :=
  (congrArg (fun l => total l fun f => L'.give m f c) same.1).trans
    (total_congr (fun f => (same.2 f c).2) (L.present n))

theorem SameExchange.takers (same : L.SameExchange n L' m) (cs : List C) :
    L'.takers cs m = L.takers cs n :=
  (congrArg (fun l => count l fun f => total cs (L'.take m f)) same.1).trans
    (total_congr (fun f => congrArg sign (total_congr (fun c => (same.2 f c).1) cs)) (L.present n))

theorem SameExchange.dissipatesOn_iff (same : L.SameExchange n L' m) {cs : List C} :
    L'.DissipatesOn cs m ↔ L.DissipatesOn cs n :=
  have take : ∀ f, total cs (L'.take m f) = total cs (L.take n f) :=
    fun f => total_congr (fun c => (same.2 f c).1) cs
  have give : ∀ f, total cs (L'.give m f) = total cs (L.give n f) :=
    fun f => total_congr (fun c => (same.2 f c).2) cs
  ⟨fun dissipates f mem => Nat.le_trans
      (Nat.le_of_eq (congr (congrArg (· + ·) (give f)) (congrArg sign (take f))).symm)
      (Nat.le_trans (dissipates f (same.mem.mpr mem)) (Nat.le_of_eq (take f))),
   fun dissipates f mem => Nat.le_trans
      (Nat.le_of_eq (congr (congrArg (· + ·) (give f)) (congrArg sign (take f))))
      (Nat.le_trans (dissipates f (same.mem.mp mem)) (Nat.le_of_eq (take f).symm))⟩

theorem SameExchange.closedAt_iff (same : L.SameExchange n L' m) {cs : List C} :
    L'.ClosedAt cs m ↔ L.ClosedAt cs n :=
  ⟨fun closed f mem c out => match closed f (same.mem.mpr mem) c out with
     | ⟨taken, given⟩ => ⟨(same.2 f c).1.symm.trans taken, (same.2 f c).2.symm.trans given⟩,
   fun closed f mem c out => match closed f (same.mem.mp mem) c out with
     | ⟨taken, given⟩ => ⟨(same.2 f c).1.trans taken, (same.2 f c).2.trans given⟩⟩

end Flow

namespace Web

/-- `W'` takes the changes of `W` across the steps from `t` and `t + 1` in the other order: each
standing, activity, dependence, need and drawing changes across one of the two steps at most,
and `W'` makes its change across the other. -/
def Commuted (W W' : Web F C) (t : Nat) : Prop :=
  (∀ c, Moved (W.level · c) (W'.level · c) t) ∧ (∀ f, Moved (W.active · f) (W'.active · f) t) ∧
    (∀ f c, Moved (W.requires · f c) (W'.requires · f c) t) ∧
    (∀ f c, Moved (W.need · f c) (W'.need · f c) t) ∧
    (∀ f c, Moved (W.draws · f c) (W'.draws · f c) t)

variable {W W' : Web F C} {t : Nat}

theorem Commuted.symm (web : W.Commuted W' t) : W'.Commuted W t :=
  ⟨fun c => (web.1 c).symm, fun f => (web.2.1 f).symm, fun f c => (web.2.2.1 f c).symm,
   fun f c => (web.2.2.2.1 f c).symm, fun f c => (web.2.2.2.2 f c).symm⟩

/-- A family's total standing exchanges the two steps' changes. -/
theorem Commuted.stock (web : W.Commuted W' t) (cs : List C) :
    Exchanged (W.stock cs) (W'.stock cs) t :=
  Exchanged.sum (q := fun c n => W.level n c) (q' := fun c n => W'.level n c)
    fun c _ => (web.1 c).exchanged

/-- What stands between the two steps of the other order stood before them or stands after
them. -/
theorem Commuted.stands_between (web : W.Commuted W' t) {c : C} (stands : 0 < W'.level (t + 1) c) :
    0 < W.level t c ∨ 0 < W.level (t + 2) c :=
  match (web.1 c).2 with
  | .inl ⟨_, shows⟩ => .inl (Eq.subst (motive := fun k => 0 < k) shows stands)
  | .inr ⟨_, shows⟩ => .inr (Eq.subst (motive := fun k => 0 < k) shows stands)

/-- Some standing changes across the first step of the other order exactly where some changed
across the second. -/
theorem Commuted.changes_first (web : W.Commuted W' t) :
    (∃ c, W'.Rises t c ∨ W'.Falls t c) ↔ ∃ c, W.Rises (t + 1) c ∨ W.Falls (t + 1) c :=
  have up : ∀ c, W'.Rises t c ↔ W.Rises (t + 1) c := fun c =>
    excess_pos.symm.trans ((Iff.of_eq (congrArg (0 < ·) (web.1 c).exchanged.rise_first)).trans
      excess_pos)
  have down : ∀ c, W'.Falls t c ↔ W.Falls (t + 1) c := fun c =>
    excess_pos.symm.trans ((Iff.of_eq (congrArg (0 < ·) (web.1 c).exchanged.fall_first)).trans
      excess_pos)
  ⟨fun ⟨c, changes⟩ => ⟨c, match changes with
      | .inl rises => .inl ((up c).mp rises)
      | .inr falls => .inr ((down c).mp falls)⟩,
   fun ⟨c, changes⟩ => ⟨c, match changes with
      | .inl rises => .inl ((up c).mpr rises)
      | .inr falls => .inr ((down c).mpr falls)⟩⟩

/-- And across the second exactly where some changed across the first. -/
theorem Commuted.changes_second (web : W.Commuted W' t) :
    (∃ c, W'.Rises (t + 1) c ∨ W'.Falls (t + 1) c) ↔ ∃ c, W.Rises t c ∨ W.Falls t c :=
  web.symm.changes_first.symm

/-- Embodiment is kept: a relatum standing exactly while active at the three steps does so at
the step between in the other order. -/
theorem Commuted.embodied {X : Type} {W W' : Web X X} (web : W.Commuted W' t) {x : X}
    (embodied : W.Embodied x) : W'.Embodied x :=
  fun n => match Nat.decEq n (t + 1) with
  | .isFalse other => Eq.subst (motive := fun P => P ↔ 0 < W'.level n x)
      ((web.2.1 x).1 n other).symm
      (Eq.subst (motive := fun k => W.active n x ↔ 0 < k) ((web.1 x).1 n other).symm (embodied n))
  | .isTrue here => Eq.subst (motive := fun k => W'.active k x ↔ 0 < W'.level k x) here.symm
      (match (web.2.1 x).2, (web.1 x).2 with
      | .inl ⟨_, act⟩, .inl ⟨_, lev⟩ =>
        Eq.subst (motive := fun P => P ↔ 0 < W'.level (t + 1) x) act.symm
          (Eq.subst (motive := fun k => W.active t x ↔ 0 < k) lev.symm (embodied t))
      | .inr ⟨_, act⟩, .inr ⟨_, lev⟩ =>
        Eq.subst (motive := fun P => P ↔ 0 < W'.level (t + 1) x) act.symm
          (Eq.subst (motive := fun k => W.active (t + 2) x ↔ 0 < k) lev.symm (embodied (t + 2)))
      | .inl ⟨still, act⟩, .inr ⟨flat, lev⟩ =>
        Eq.subst (motive := fun P => P ↔ 0 < W'.level (t + 1) x) act.symm
          (Eq.subst (motive := fun k => W.active t x ↔ 0 < k) lev.symm
            ((embodied t).trans ((Iff.of_eq (congrArg (0 < ·) flat)).trans
              ((embodied (t + 1)).symm.trans ((Iff.of_eq still).trans (embodied (t + 2)))))))
      | .inr ⟨still, act⟩, .inl ⟨flat, lev⟩ =>
        Eq.subst (motive := fun P => P ↔ 0 < W'.level (t + 1) x) act.symm
          (Eq.subst (motive := fun k => W.active (t + 2) x ↔ 0 < k) lev.symm
            ((embodied (t + 2)).trans ((Iff.of_eq (congrArg (0 < ·) flat)).symm.trans
              ((embodied (t + 1)).symm.trans ((Iff.of_eq still).symm.trans (embodied t)))))))

end Web

namespace Flow

variable {L L' : Flow F C} {W W' : Web F C} {t : Nat}

/-- Balance moves with the exchange: across the first step of the other order a family balances
exactly where it balanced across the second step. -/
theorem Commuted.balancesOn_first (flow : L.Commuted L' t) (web : W.Commuted W' t) {cs : List C} :
    L'.BalancesOn W' cs t ↔ L.BalancesOn W cs (t + 1) :=
  ⟨fun balances c mem => ((web.1 c).exchanged.balance_first (flow.1.taken c) (flow.1.given c)).mp
      (balances c mem),
   fun balances c mem => ((web.1 c).exchanged.balance_first (flow.1.taken c) (flow.1.given c)).mpr
      (balances c mem)⟩

/-- And across the second exactly where it balanced across the first. -/
theorem Commuted.balancesOn_second (flow : L.Commuted L' t) (web : W.Commuted W' t)
    {cs : List C} : L'.BalancesOn W' cs (t + 1) ↔ L.BalancesOn W cs t :=
  ⟨fun balances c mem => ((web.1 c).exchanged.balance_second (flow.2.1.taken c)
      (flow.2.1.given c)).mp (balances c mem),
   fun balances c mem => ((web.1 c).exchanged.balance_second (flow.2.1.taken c)
      (flow.2.1.given c)).mpr (balances c mem)⟩

/-- Away from the two steps, balance is as it was. -/
theorem Commuted.balancesOn_away (flow : L.Commuted L' t) (web : W.Commuted W' t) {cs : List C}
    {n : Nat} (other : n ≠ t) (other' : n ≠ t + 1) : L'.BalancesOn W' cs n ↔ L.BalancesOn W cs n :=
  have same := flow.2.2 n other other'
  have ends : ∀ c, W'.level (n + 1) c = W.level (n + 1) c ∧ W'.level n c = W.level n c :=
    fun c => ⟨((web.1 c).away other other').2, ((web.1 c).away other other').1⟩
  ⟨fun balances c mem => (eq_iff_of_sides (congr (congrArg (· + ·) (ends c).1) (same.taken c))
      (congr (congrArg (· + ·) (ends c).2) (same.given c))).mp (balances c mem),
   fun balances c mem => (eq_iff_of_sides (congr (congrArg (· + ·) (ends c).1) (same.taken c))
      (congr (congrArg (· + ·) (ends c).2) (same.given c))).mpr (balances c mem)⟩

/-- So a flow balances in the other order exactly where it balances. -/
theorem Commuted.balances_iff (flow : L.Commuted L' t) (web : W.Commuted W' t) :
    L'.Balances W' ↔ L.Balances W :=
  have forth : ∀ {A A' : Flow F C} {V V' : Web F C}, A.Commuted A' t → V.Commuted V' t →
      A.Balances V → A'.Balances V' := fun {_ A' _ V'} flow web balances =>
    balances_iff_on.mpr fun cs n => match Nat.decEq n t with
    | .isTrue here => Eq.subst (motive := fun k => A'.BalancesOn V' cs k) here.symm
        ((flow.balancesOn_first web).mpr (balances.on cs (t + 1)))
    | .isFalse other => match Nat.decEq n (t + 1) with
      | .isTrue here => Eq.subst (motive := fun k => A'.BalancesOn V' cs k) here.symm
          ((flow.balancesOn_second web).mpr (balances.on cs t))
      | .isFalse other' => (flow.balancesOn_away web other other').mpr (balances.on cs n)
  ⟨forth flow.symm web.symm, forth flow web⟩

/-- Dissipation moves with the exchange, and so is kept. -/
theorem Commuted.dissipative_iff (flow : L.Commuted L' t) : L'.Dissipative ↔ L.Dissipative :=
  have forth : ∀ {A A' : Flow F C}, A.Commuted A' t → A.Dissipative → A'.Dissipative :=
    fun {_ A'} flow dissipative cs n distinct closed => match Nat.decEq n t with
    | .isTrue here => Eq.subst (motive := fun k => A'.DissipatesOn cs k) here.symm
        (flow.1.dissipatesOn_iff.mpr (dissipative cs (t + 1) distinct
          (flow.1.closedAt_iff.mp (Eq.subst (motive := fun k => A'.ClosedAt cs k) here closed))))
    | .isFalse other => match Nat.decEq n (t + 1) with
      | .isTrue here => Eq.subst (motive := fun k => A'.DissipatesOn cs k) here.symm
          (flow.2.1.dissipatesOn_iff.mpr (dissipative cs t distinct
            (flow.2.1.closedAt_iff.mp (Eq.subst (motive := fun k => A'.ClosedAt cs k) here closed))))
      | .isFalse other' => (flow.2.2 n other other').dissipatesOn_iff.mpr
          (dissipative cs n distinct ((flow.2.2 n other other').closedAt_iff.mp closed))
  ⟨forth flow.symm, forth flow⟩

/-- Running down moves with the exchange, for a family without repetition holding what stands
at the three steps. -/
theorem Commuted.runsDownOn_first (flow : L.Commuted L' t) (web : W.Commuted W' t) {es : List C}
    (distinct : Distinct es) (before : ∀ c, 0 < W.level t c → c ∈ es)
    (between : ∀ c, 0 < W.level (t + 1) c → c ∈ es) (after : ∀ c, 0 < W.level (t + 2) c → c ∈ es) :
    L'.RunsDownOn W' es t ↔ L.RunsDownOn W es (t + 1) :=
  ⟨fun ⟨_, _, _, balances, dissipates⟩ => ⟨distinct, between, after,
      (flow.balancesOn_first web).mp balances, flow.1.dissipatesOn_iff.mp dissipates⟩,
   fun ⟨_, _, _, balances, dissipates⟩ => ⟨distinct,
      fun c stands => before c (Eq.subst (motive := fun k => 0 < k) (web.1 c).at_first stands),
      fun c stands => match web.stands_between stands with
        | .inl was => before c was
        | .inr will => after c will,
      (flow.balancesOn_first web).mpr balances, flow.1.dissipatesOn_iff.mpr dissipates⟩⟩

theorem Commuted.runsDownOn_second (flow : L.Commuted L' t) (web : W.Commuted W' t) {es : List C}
    (distinct : Distinct es) (before : ∀ c, 0 < W.level t c → c ∈ es)
    (between : ∀ c, 0 < W.level (t + 1) c → c ∈ es) (after : ∀ c, 0 < W.level (t + 2) c → c ∈ es) :
    L'.RunsDownOn W' es (t + 1) ↔ L.RunsDownOn W es t :=
  ⟨fun ⟨_, _, _, balances, dissipates⟩ => ⟨distinct, before, between,
      (flow.balancesOn_second web).mp balances, flow.2.1.dissipatesOn_iff.mp dissipates⟩,
   fun ⟨_, _, _, balances, dissipates⟩ => ⟨distinct,
      fun c stands => match web.stands_between stands with
        | .inl was => before c was
        | .inr will => after c will,
      fun c stands => after c (Eq.subst (motive := fun k => 0 < k) (web.1 c).at_last stands),
      (flow.balancesOn_second web).mpr balances, flow.2.1.dissipatesOn_iff.mpr dissipates⟩⟩

/-- Only active relata giving is kept where no relatum giving across one step has its activity
changed by the other: a giver across the second step was active before the first, and a giver
across the first is still active after the second. -/
theorem Commuted.acting (flow : L.Commuted L' t) (web : W.Commuted W' t) (acting : L.Acting W)
    (first : ∀ f c, f ∈ L.present (t + 1) → 0 < L.give (t + 1) f c → W.active (t + 1) f →
      W.active t f)
    (second : ∀ f c, f ∈ L.present t → 0 < L.give t f c → W.active (t + 1) f →
      W.active (t + 2) f) :
    L'.Acting W' :=
  fun n f c mem gives => match Nat.decEq n t with
  | .isTrue here =>
    have mem' := flow.1.mem.mp (Eq.subst (motive := fun k => f ∈ L'.present k) here mem)
    have gives' : 0 < L.give (t + 1) f c := Nat.lt_of_lt_of_le
      (Eq.subst (motive := fun k => 0 < L'.give k f c) here gives)
      (Nat.le_of_eq (flow.1.2 f c).2)
    Eq.subst (motive := fun k => W'.active k f) here.symm
      (cast (web.2.1 f).at_first.symm (first f c mem' gives' (acting (t + 1) f c mem' gives')))
  | .isFalse other => match Nat.decEq n (t + 1) with
    | .isTrue here =>
      have mem' := flow.2.1.mem.mp (Eq.subst (motive := fun k => f ∈ L'.present k) here mem)
      have gives' : 0 < L.give t f c := Nat.lt_of_lt_of_le
        (Eq.subst (motive := fun k => 0 < L'.give k f c) here gives)
        (Nat.le_of_eq (flow.2.1.2 f c).2)
      have was := acting t f c mem' gives'
      Eq.subst (motive := fun k => W'.active k f) here.symm (match (web.2.1 f).2 with
        | .inl ⟨_, shows⟩ => cast shows.symm was
        | .inr ⟨still, shows⟩ => cast shows.symm (second f c mem' gives' (cast still was)))
    | .isFalse other' =>
      have same := flow.2.2 n other other'
      cast ((web.2.1 f).1 n other').symm (acting n f c (same.mem.mp mem)
        (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (same.2 f c).2)))

end Flow


/-! ### Taking two exchanges in the other order: the construction -/

/-- The step numbers with `t` and `t + 1` exchanged. -/
def swapAt (t n : Nat) : Nat :=
  if n = t then t + 1 else if n = t + 1 then t else n

theorem swapAt_first (t : Nat) : swapAt t t = t + 1 :=
  if_pos rfl

theorem swapAt_second (t : Nat) : swapAt t (t + 1) = t :=
  (if_neg ne_first.symm).trans (if_pos rfl)

theorem swapAt_away {t n : Nat} (other : n ≠ t) (other' : n ≠ t + 1) : swapAt t n = n :=
  (if_neg other).trans (if_neg other')

theorem cond_of_true {α : Type} {b : Bool} {x y : α} (yes : b = true) : cond b x y = x :=
  Eq.subst (motive := fun b' => cond b' x y = x) yes.symm rfl

theorem cond_of_false {α : Type} {b : Bool} {x y : α} (no : b = false) : cond b x y = y :=
  Eq.subst (motive := fun b' => cond b' x y = y) no.symm rfl

/-- Between the two steps, a reading shows what was before them on the first side and what is
after them on the other; it moves the change of anything whose change is across the step of its
side. -/
theorem moved_of_side {α : Type} {q : Nat → α} {t : Nat} {b : Bool}
    (first : b = true → q (t + 1) = q (t + 2)) (second : b = false → q t = q (t + 1)) :
    Moved q (fun n => if n = t + 1 then cond b (q t) (q (t + 2)) else q n) t :=
  ⟨fun _ other => if_neg other,
   match b, first, second with
   | true, first, _ => .inl ⟨first rfl, if_pos rfl⟩
   | false, _, second => .inr ⟨second rfl, if_pos rfl⟩⟩

namespace Flow

/-- The flow with its exchanges across the steps from `t` and `t + 1` taken in the other
order. -/
def swap (L : Flow F C) (t : Nat) : Flow F C :=
  ⟨fun n => L.present (swapAt t n), fun n => L.take (swapAt t n), fun n => L.give (swapAt t n)⟩

theorem swap_commuted (L : Flow F C) (t : Nat) : L.Commuted (L.swap t) t :=
  have same : ∀ {n k : Nat}, swapAt t n = k → L.SameExchange k (L.swap t) n := fun same =>
    ⟨congrArg L.present same, fun f c =>
      ⟨congrArg (fun k => L.take k f c) same, congrArg (fun k => L.give k f c) same⟩⟩
  ⟨same (swapAt_first t), same (swapAt_second t),
   fun _ other other' => same (swapAt_away other other')⟩

end Flow

namespace Web

/-- The web with its changes across the steps from `t` and `t + 1` taken in the other order, as
the sides say: between the two steps a condition on the first side stands as before them and one
on the other side as after them, and a relatum on the first side is active, depends, needs and
draws as before them, one on the other side as after them. -/
def commute (W : Web F C) (t : Nat) (sideF : F → Bool) (sideC : C → Bool) : Web F C where
  level n c := if n = t + 1 then cond (sideC c) (W.level t c) (W.level (t + 2) c) else W.level n c
  active n f := if n = t + 1 then cond (sideF f) (W.active t f) (W.active (t + 2) f)
    else W.active n f
  requires n f c := if n = t + 1 then cond (sideF f) (W.requires t f c) (W.requires (t + 2) f c)
    else W.requires n f c
  need n f c := if n = t + 1 then cond (sideF f) (W.need t f c) (W.need (t + 2) f c)
    else W.need n f c
  draws n f c := if n = t + 1 then cond (sideF f) (W.draws t f c) (W.draws (t + 2) f c)
    else W.draws n f c

/-- The sides split the two steps: the second step leaves alone the conditions and relata on the
first side, with their dependences, needs and drawings, and the first step leaves alone those on
the other side. So no relatum's standing, activity or relations change across both steps. -/
def Split (W : Web F C) (t : Nat) (sideF : F → Bool) (sideC : C → Bool) : Prop :=
  (∀ c, sideC c = true → W.level (t + 1) c = W.level (t + 2) c) ∧
  (∀ c, sideC c = false → W.level t c = W.level (t + 1) c) ∧
  (∀ f, sideF f = true → W.active (t + 1) f = W.active (t + 2) f ∧
    ∀ c, W.requires (t + 1) f c = W.requires (t + 2) f c ∧ W.need (t + 1) f c = W.need (t + 2) f c ∧
      W.draws (t + 1) f c = W.draws (t + 2) f c) ∧
  (∀ f, sideF f = false → W.active t f = W.active (t + 1) f ∧
    ∀ c, W.requires t f c = W.requires (t + 1) f c ∧ W.need t f c = W.need (t + 1) f c ∧
      W.draws t f c = W.draws (t + 1) f c)

variable {W : Web F C} {t : Nat} {sideF : F → Bool} {sideC : C → Bool}

theorem commute_level_true {c : C} (yes : sideC c = true) :
    (W.commute t sideF sideC).level (t + 1) c = W.level t c :=
  show (if t + 1 = t + 1 then cond (sideC c) (W.level t c) (W.level (t + 2) c)
    else W.level (t + 1) c) = W.level t c from (if_pos rfl).trans (cond_of_true yes)

theorem commute_level_false {c : C} (no : sideC c = false) :
    (W.commute t sideF sideC).level (t + 1) c = W.level (t + 2) c :=
  show (if t + 1 = t + 1 then cond (sideC c) (W.level t c) (W.level (t + 2) c)
    else W.level (t + 1) c) = W.level (t + 2) c from (if_pos rfl).trans (cond_of_false no)

theorem commute_active_true {f : F} (yes : sideF f = true) :
    (W.commute t sideF sideC).active (t + 1) f = W.active t f :=
  show (if t + 1 = t + 1 then cond (sideF f) (W.active t f) (W.active (t + 2) f)
    else W.active (t + 1) f) = W.active t f from (if_pos rfl).trans (cond_of_true yes)

theorem commute_requires_true {f : F} {c : C} (yes : sideF f = true) :
    (W.commute t sideF sideC).requires (t + 1) f c = W.requires t f c :=
  show (if t + 1 = t + 1 then cond (sideF f) (W.requires t f c) (W.requires (t + 2) f c)
    else W.requires (t + 1) f c) = W.requires t f c from (if_pos rfl).trans (cond_of_true yes)

theorem commute_active_away {n : Nat} {f : F} (other : n ≠ t + 1) :
    (W.commute t sideF sideC).active n f = W.active n f :=
  show (if n = t + 1 then cond (sideF f) (W.active t f) (W.active (t + 2) f)
    else W.active n f) = W.active n f from if_neg other

/-- Split by sides, the web with its changes taken in the other order is a reordering. -/
theorem commute_commuted (split : W.Split t sideF sideC) : W.Commuted (W.commute t sideF sideC) t :=
  ⟨fun c => moved_of_side (q := (W.level · c)) (split.1 c) (split.2.1 c),
   fun f => moved_of_side (q := (W.active · f)) (fun yes => (split.2.2.1 f yes).1)
     (fun no => (split.2.2.2 f no).1),
   fun f c => moved_of_side (q := (W.requires · f c)) (fun yes => ((split.2.2.1 f yes).2 c).1)
     (fun no => ((split.2.2.2 f no).2 c).1),
   fun f c => moved_of_side (q := (W.need · f c)) (fun yes => ((split.2.2.1 f yes).2 c).2.1)
     (fun no => ((split.2.2.2 f no).2 c).2.1),
   fun f c => moved_of_side (q := (W.draws · f c)) (fun yes => ((split.2.2.1 f yes).2 c).2.2)
     (fun no => ((split.2.2.2 f no).2 c).2.2)⟩

/-- Activity needing support is kept where no dependence crosses the sides: every relatum
depending on a condition before or after the two steps is on the condition's side. Then between
the two steps each active relatum's dependences and their conditions are read at one step. -/
theorem commute_dependent (dependent : W.Dependent)
    (uncrossed : ∀ f c, (W.requires t f c ∨ W.requires (t + 2) f c) → sideF f = sideC c) :
    (W.commute t sideF sideC).Dependent :=
  have mid : ∀ f, (W.commute t sideF sideC).active (t + 1) f →
      (W.commute t sideF sideC).Supported (t + 1) f := fun f active =>
    match hf : sideF f with
    | true =>
      have act : W.active t f := cast ((if_pos rfl).trans (cond_of_true hf)) active
      fun c requires =>
        have req : W.requires t f c := cast ((if_pos rfl).trans (cond_of_true hf)) requires
        have hc : sideC c = true := (uncrossed f c (.inl req)).symm.trans hf
        Nat.le_trans (Nat.le_of_eq ((if_pos rfl).trans (cond_of_true hf)))
          (Nat.le_trans (dependent t f act c req)
            (Nat.le_of_eq ((if_pos rfl).trans (cond_of_true hc)).symm))
    | false =>
      have act : W.active (t + 2) f := cast ((if_pos rfl).trans (cond_of_false hf)) active
      fun c requires =>
        have req : W.requires (t + 2) f c := cast ((if_pos rfl).trans (cond_of_false hf)) requires
        have hc : sideC c = false := (uncrossed f c (.inr req)).symm.trans hf
        Nat.le_trans (Nat.le_of_eq ((if_pos rfl).trans (cond_of_false hf)))
          (Nat.le_trans (dependent (t + 2) f act c req)
            (Nat.le_of_eq ((if_pos rfl).trans (cond_of_false hc)).symm))
  fun n f active => match Nat.decEq n (t + 1) with
  | .isTrue here => Eq.subst (motive := fun k => (W.commute t sideF sideC).active k f →
        (W.commute t sideF sideC).Supported k f) here.symm (mid f) active
  | .isFalse other => fun c requires =>
    Nat.le_trans (Nat.le_of_eq (if_neg other))
      (Nat.le_trans (dependent n f (cast (if_neg other) active) c (cast (if_neg other) requires))
        (Nat.le_of_eq (if_neg other).symm))

end Web

/-! ### Worlds with two exchanges taken in the other order -/

namespace World

/-- A world with its exchanges across the steps from `t` and `t + 1` taken in the other order,
its changes moved as the side of each relatum says. -/
def commute (w : World) (t : Nat) (side : w.Relatum → Bool) : World :=
  ⟨w.Relatum, w.flow.swap t, w.web.commute t side side⟩

variable {w : World} {t : Nat} {side : w.Relatum → Bool}

/-- **Independent exchanges commute.** Where the sides split the two steps, taking the two
exchanges in the other order gives a world that balances, dissipates and is embodied exactly where
the world does; whose activity needs support where the world's does and no dependence crosses the
sides; and in which only active relata give where they do in the world and no relatum giving across
one step has its activity begun by the first step or ended by the second. -/
theorem commute_laws (split : w.web.Split t side side) :
    ((w.commute t side).Balanced ↔ w.Balanced) ∧
    ((w.commute t side).Dissipative ↔ w.Dissipative) ∧
    ((w.commute t side).Embodied ↔ w.Embodied) ∧
    (w.Dependent → (∀ f c, (w.web.requires t f c ∨ w.web.requires (t + 2) f c) → side f = side c) →
      (w.commute t side).Dependent) ∧
    (w.Acting →
      (∀ f c, f ∈ w.flow.present (t + 1) → 0 < w.flow.give (t + 1) f c →
        w.web.active (t + 1) f → w.web.active t f) →
      (∀ f c, f ∈ w.flow.present t → 0 < w.flow.give t f c →
        w.web.active (t + 1) f → w.web.active (t + 2) f) →
      (w.commute t side).Acting) :=
  have flow := Flow.swap_commuted w.flow t
  have web := Web.commute_commuted split
  ⟨flow.balances_iff web, flow.dissipative_iff,
   ⟨fun embodied x => web.symm.embodied (embodied x), fun embodied x => web.embodied (embodied x)⟩,
   fun dependent uncrossed => Web.commute_dependent dependent uncrossed,
   fun acting first second => flow.acting web acting first second⟩

/-- And the counts and totals are those of the world, over any stretch holding both steps: the
relata of a finite family arising and ceasing, with their activity decided in both, and the rises
and falls of a family's total standing, with the steps at which it falls. -/
theorem commute_counts (split : w.web.Split t side side)
    [∀ n x, Decidable (w.web.active n x)] [∀ n x, Decidable ((w.commute t side).web.active n x)]
    (xs : List w.Relatum) (cs : List w.Relatum) {S m : Nat} (from_ : S ≤ t) (to : t + 2 ≤ S + m) :
    total (steps S m) (comings xs fun x n => (w.commute t side).web.active n x) =
      total (steps S m) (comings xs fun x n => w.web.active n x) ∧
    total (steps S m) (ceasings xs fun x n => (w.commute t side).web.active n x) =
      total (steps S m) (ceasings xs fun x n => w.web.active n x) ∧
    total (steps S m) (rise ((w.commute t side).web.stock cs)) =
      total (steps S m) (rise (w.web.stock cs)) ∧
    total (steps S m) (fall ((w.commute t side).web.stock cs)) =
      total (steps S m) (fall (w.web.stock cs)) ∧
    count (steps S m) (fall ((w.commute t side).web.stock cs)) =
      count (steps S m) (fall (w.web.stock cs)) :=
  have web := Web.commute_commuted split
  ⟨comings_moved (p := fun x n => w.web.active n x)
     (p' := fun x n => (w.commute t side).web.active n x) (fun x _ => web.2.1 x) from_ to,
   ceasings_moved (p := fun x n => w.web.active n x)
     (p' := fun x n => (w.commute t side).web.active n x) (fun x _ => web.2.1 x) from_ to,
   (web.stock cs).risen from_ to, (web.stock cs).fallen from_ to,
   (web.stock cs).fall_count from_ to⟩

end World

/-! ### Reorderings: independent exchanges commuted again and again -/

/-- A law of change and a web reordered into another, each time commuting two exchanges the
sides split, at steps `within` admits: the closure of `World.commute` under repetition. -/
inductive Reorders {X : Type} (within : Nat → Prop) :
    Flow X X → Web X X → Flow X X → Web X X → Prop
  | refl (L : Flow X X) (W : Web X X) : Reorders within L W L W
  | swap {L : Flow X X} {W : Web X X} {L' : Flow X X} {W' : Web X X} (t : Nat) (side : X → Bool)
      (at_ : within t) (split : W.Split t side side)
      (more : Reorders within (L.swap t) (W.commute t side side) L' W') :
      Reorders within L W L' W'

/-- **Reordering keeps the laws.** However often exchanges the sides split are commuted, the
world balances, dissipates and is embodied exactly where it did. -/
theorem Reorders.laws {X : Type} {within : Nat → Prop} {L L' : Flow X X} {W W' : Web X X} :
    Reorders within L W L' W' →
      (((⟨X, L', W'⟩ : World).Balanced ↔ (⟨X, L, W⟩ : World).Balanced) ∧
       ((⟨X, L', W'⟩ : World).Dissipative ↔ (⟨X, L, W⟩ : World).Dissipative) ∧
       ((⟨X, L', W'⟩ : World).Embodied ↔ (⟨X, L, W⟩ : World).Embodied))
  | .refl _ _ => ⟨Iff.rfl, Iff.rfl, Iff.rfl⟩
  | .swap t side _ split more =>
    have laws := World.commute_laws (w := ⟨X, L, W⟩) (t := t) (side := side) split
    have next := Reorders.laws more
    ⟨next.1.trans laws.1, next.2.1.trans laws.2.1, next.2.2.trans laws.2.2.1⟩

/-- **And the totals over a stretch holding every commuted pair.** The rises and falls of a
family's total standing, and the steps at which it falls, are those of the world. -/
theorem Reorders.totals {X : Type} {S m : Nat} {L L' : Flow X X} {W W' : Web X X} (cs : List X) :
    Reorders (fun t => S ≤ t ∧ t + 2 ≤ S + m) L W L' W' →
      total (steps S m) (rise (W'.stock cs)) = total (steps S m) (rise (W.stock cs)) ∧
      total (steps S m) (fall (W'.stock cs)) = total (steps S m) (fall (W.stock cs)) ∧
      count (steps S m) (fall (W'.stock cs)) = count (steps S m) (fall (W.stock cs))
  | .refl _ _ => ⟨rfl, rfl, rfl⟩
  | .swap _ _ ⟨from_, to⟩ split more =>
    have stock := (Web.commute_commuted split).stock cs
    have next := Reorders.totals cs more
    ⟨next.1.trans (stock.risen from_ to), next.2.1.trans (stock.fallen from_ to),
     next.2.2.trans (stock.fall_count from_ to)⟩


/-! ### What the order of two exchanges carries -/

/-- The first relatum on one side, the others on the other. -/
def firstSide : Nat → Bool
  | 0 => true
  | _ + 1 => false

namespace Crossing

/-- The first relatum is active at the first step only; the third throughout. -/
def act : Nat → Nat → Bool
  | 0, 0 => true
  | _, 2 => true
  | _, _ => false

/-- The second relatum stands at two before the step from one, at nothing after it. -/
def standing : Nat → Nat → Nat
  | 0, 1 => 2
  | 1, 1 => 2
  | _, _ => 0

/-- The first relatum depends on the second at need two throughout; the third draws on the
second. -/
def web : Web Nat Nat where
  level := standing
  active n x := act n x = true
  requires _ x c := x = 0 ∧ c = 1
  need _ _ _ := 2
  draws _ x c := x = 2 ∧ c = 1

/-- Across the step from one, the third relatum takes the second's two units. -/
def take : Nat → Nat → Nat → Nat
  | 1, 2, 1 => 2
  | _, _, _ => 0

def present : Nat → List Nat
  | 1 => [2]
  | _ => []

def flow : Flow Nat Nat where
  present := present
  take := take
  give _ _ _ := 0

/-- The first relatum ceases across the step from zero; across the step from one the third
takes from the second, which ceases to stand. The two exchanges share no relatum, and the first
relatum depends on the second. -/
def world : World :=
  ⟨Nat, flow, web⟩

theorem balances : flow.Balances web
  | 0, 0 => rfl
  | 0, 1 => rfl
  | 0, _ + 2 => rfl
  | 1, 0 => rfl
  | 1, 1 => rfl
  | 1, _ + 2 => rfl
  | _ + 2, _ => rfl

theorem dependent : web.Dependent
  | 0, _, _, _, ⟨rfl, rfl⟩ => Nat.le_refl 2
  | _ + 1, _, active, _, ⟨rfl, rfl⟩ => Bool.noConfusion active

/-- The sides split the two steps: the first relatum changes across the first only, the others
across the second only. -/
theorem split : web.Split 0 firstSide firstSide :=
  ⟨fun c yes => match c, yes with
     | 0, _ => rfl
     | _ + 1, yes => Bool.noConfusion yes,
   fun c no => match c, no with
     | 0, no => Bool.noConfusion no
     | 1, _ => rfl
     | _ + 2, _ => rfl,
   fun f yes => match f, yes with
     | 0, _ => ⟨rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩
     | _ + 1, yes => Bool.noConfusion yes,
   fun f no => match f, no with
     | 0, no => Bool.noConfusion no
     | 1, _ => ⟨rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩
     | 2, _ => ⟨rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩
     | _ + 3, _ => ⟨rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩⟩

/-- **The order of exchanges joined by a dependence registers.** The two exchanges share no
relatum and the sides split them, so the world taken in the other order balances; but the first
relatum depends on the second across the sides, and in the other order the second ceases to stand
while the first is still active: activity needing support fails between the two steps. -/
theorem order_registers :
    world.Balanced ∧ world.Dependent ∧ world.web.Split 0 firstSide firstSide ∧
      (world.commute 0 firstSide).Balanced ∧ ¬ (world.commute 0 firstSide).Dependent :=
  ⟨balances, dependent, split, (World.commute_laws (w := world) split).1.mpr balances,
   fun dependent' =>
     have active : (web.commute 0 firstSide firstSide).active 1 0 :=
       cast (Web.commute_active_true (W := web) (t := 0) (sideC := firstSide) (f := 0)
         (rfl : firstSide 0 = true)).symm (rfl : act 0 0 = true)
     have requires : (web.commute 0 firstSide firstSide).requires 1 0 1 :=
       cast (Web.commute_requires_true (W := web) (t := 0) (sideC := firstSide) (f := 0) (c := 1)
         (rfl : firstSide 0 = true)).symm (⟨rfl, rfl⟩ : (0 : Nat) = 0 ∧ (1 : Nat) = 1)
     have level : (web.commute 0 firstSide firstSide).level 1 1 = 0 :=
       Web.commute_level_false (W := web) (t := 0) (sideF := firstSide) (c := 1)
         (rfl : firstSide 1 = false)
     Nat.not_succ_le_zero 1 (Nat.le_trans (dependent' 1 (0 : Nat) active (1 : Nat) requires)
       (Nat.le_of_eq level))⟩

end Crossing

namespace Arising

/-- The first relatum is active from the step after the first. -/
def act : Nat → Nat → Bool
  | 0, _ => false
  | _ + 1, 0 => true
  | _, _ => false

/-- The second relatum stands at one from the third step. -/
def standing : Nat → Nat → Nat
  | _ + 2, 1 => 1
  | _ + 2, 0 => 0
  | _ + 2, _ + 2 => 0
  | 0, _ => 0
  | 1, _ => 0

def web : Web Nat Nat where
  level := standing
  active n x := act n x = true
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Across the step from one, the first relatum gives the second a unit. -/
def give : Nat → Nat → Nat → Nat
  | 1, 0, 1 => 1
  | _, _, _ => 0

def present : Nat → List Nat
  | 1 => [0]
  | _ => []

def flow : Flow Nat Nat where
  present := present
  take _ _ _ := 0
  give := give

/-- The first relatum arises across the step from zero and gives across the step from one: the
two exchanges share it. -/
def world : World :=
  ⟨Nat, flow, web⟩

theorem balances : flow.Balances web
  | 0, _ => rfl
  | 1, 0 => rfl
  | 1, 1 => rfl
  | 1, _ + 2 => rfl
  | _ + 2, 0 => rfl
  | _ + 2, 1 => rfl
  | _ + 2, _ + 2 => rfl

theorem acting : flow.Acting web
  | 1, 0, 1, _, _ => rfl
  | 0, _, _, mem, _ => nomatch mem
  | 1, 0, 0, _, gives => absurd gives (Nat.lt_irrefl 0)
  | 1, 0, _ + 2, _, gives => absurd gives (Nat.lt_irrefl 0)
  | 1, _ + 1, _, mem, _ => match mem with
    | .tail _ no => nomatch no
  | _ + 2, _, _, mem, _ => nomatch mem

theorem split : web.Split 0 firstSide firstSide :=
  ⟨fun c yes => match c, yes with
     | 0, _ => rfl
     | _ + 1, yes => Bool.noConfusion yes,
   fun c no => match c, no with
     | 0, no => Bool.noConfusion no
     | 1, _ => rfl
     | _ + 2, _ => rfl,
   fun f yes => match f, yes with
     | 0, _ => ⟨rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩
     | _ + 1, yes => Bool.noConfusion yes,
   fun f no => match f, no with
     | 0, no => Bool.noConfusion no
     | _ + 1, _ => ⟨rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩⟩

/-- **The order of exchanges sharing a relatum registers.** Each standing and activity changes
across one of the two steps, so the world taken in the other order balances; but the relatum that
arises across the first step gives across the second, and in the other order it gives before it
is active. -/
theorem order_registers :
    world.Balanced ∧ world.Acting ∧ world.web.Split 0 firstSide firstSide ∧
      (world.commute 0 firstSide).Balanced ∧ ¬ (world.commute 0 firstSide).Acting :=
  ⟨balances, acting, split, (World.commute_laws (w := world) split).1.mpr balances,
   fun acting' =>
     have mem : (0 : Nat) ∈ (flow.swap 0).present 0 :=
       Eq.subst (motive := fun k => (0 : Nat) ∈ present k) (swapAt_first 0).symm (.head [])
     have gives : 0 < (flow.swap 0).give 0 0 1 :=
       Eq.subst (motive := fun k => 0 < give k 0 1) (swapAt_first 0).symm Nat.zero_lt_one
     Bool.noConfusion (cast (Web.commute_active_away (W := web) (t := 0) (sideF := firstSide)
       (sideC := firstSide) (n := 0) (f := 0) (Nat.succ_ne_self 0).symm)
       (acting' 0 (0 : Nat) (1 : Nat) mem gives) : act 0 0 = true)⟩

end Arising


/-! ## The order of exchanges as an object -/

/-! ### Exchanging two step numbers -/

section Swaps

/-- A number below another and not equal to it is below it. -/
theorem lt_of_le_ne {a b : Nat} (le : a ≤ b) (ne : a ≠ b) : a < b :=
  match Nat.lt_or_ge a b with
  | .inl lt => lt
  | .inr ge => absurd (Nat.le_antisymm le ge) ne

theorem swapAt_of_lt {t n : Nat} (lt : n < t) : swapAt t n = n :=
  swapAt_away (Nat.ne_of_lt lt) (Nat.ne_of_lt (Nat.lt_succ_of_lt lt))

theorem swapAt_of_gt {t n : Nat} (gt : t + 1 < n) : swapAt t n = n :=
  swapAt_away (Nat.ne_of_gt (Nat.lt_trans (Nat.lt_succ_self t) gt)) (Nat.ne_of_gt gt)

/-- Exchanging `t` and `t + 1` twice exchanges nothing. -/
theorem swapAt_swapAt (t : Nat) (n : Nat) : swapAt t (swapAt t n) = n :=
  match Nat.decEq n t with
  | .isTrue here => Eq.subst (motive := fun k => swapAt t (swapAt t k) = k) here.symm
      ((congrArg (swapAt t) (swapAt_first t)).trans (swapAt_second t))
  | .isFalse other => match Nat.decEq n (t + 1) with
    | .isTrue here => Eq.subst (motive := fun k => swapAt t (swapAt t k) = k) here.symm
        ((congrArg (swapAt t) (swapAt_second t)).trans (swapAt_first t))
    | .isFalse other' =>
      (congrArg (swapAt t) (swapAt_away other other')).trans (swapAt_away other other')

/-- Exchanging `t` and `t + 1` keeps the order of every pair but that one. -/
theorem swapAt_lt {t i j : Nat} (lt : i < j) (pair : i = t → j ≠ t + 1) :
    swapAt t i < swapAt t j :=
  match Nat.decEq i t with
  | .isTrue hi =>
    have later : t + 1 < j := lt_of_le_ne (Nat.succ_le_of_lt (Eq.subst (motive := (· < j)) hi lt))
      fun same => pair hi same.symm
    Eq.subst (motive := fun k => swapAt t k < swapAt t j) hi.symm
      (Eq.subst (motive := fun k => k < swapAt t j) (swapAt_first t).symm
        (Eq.subst (motive := fun k => t + 1 < k) (swapAt_of_gt later).symm later))
  | .isFalse oi => match Nat.decEq i (t + 1) with
    | .isTrue hi =>
      have later : t + 1 < j := Eq.subst (motive := (· < j)) hi lt
      Eq.subst (motive := fun k => swapAt t k < swapAt t j) hi.symm
        (Eq.subst (motive := fun k => k < swapAt t j) (swapAt_second t).symm
          (Eq.subst (motive := fun k => t < k) (swapAt_of_gt later).symm
            (Nat.lt_trans (Nat.lt_succ_self t) later)))
    | .isFalse oi' =>
      Eq.subst (motive := fun k => k < swapAt t j) (swapAt_away oi oi').symm
        (match Nat.decEq j t with
        | .isTrue hj => Eq.subst (motive := fun k => i < swapAt t k) hj.symm
            (Eq.subst (motive := fun k => i < k) (swapAt_first t).symm
              (Nat.lt_succ_of_lt (Eq.subst (motive := (i < ·)) hj lt)))
        | .isFalse oj => match Nat.decEq j (t + 1) with
          | .isTrue hj => Eq.subst (motive := fun k => i < swapAt t k) hj.symm
              (Eq.subst (motive := fun k => i < k) (swapAt_second t).symm
                (lt_of_le_ne (Nat.le_of_lt_succ (Eq.subst (motive := (i < ·)) hj lt)) oi))
          | .isFalse oj' => Eq.subst (motive := fun k => i < k) (swapAt_away oj oj').symm lt)

end Swaps

/-! ### What a web shows of a relatum -/

namespace Web

variable {X : Type}

/-- `W'` at step `k'` shows a relatum as `W` at step `k`: its standing, activity, dependences,
needs and drawings. -/
def SameAt (W : Web X X) (k : Nat) (W' : Web X X) (k' : Nat) (x : X) : Prop :=
  W'.level k' x = W.level k x ∧ W'.active k' x = W.active k x ∧
    ∀ c, W'.requires k' x c = W.requires k x c ∧ W'.need k' x c = W.need k x c ∧
      W'.draws k' x c = W.draws k x c

/-- A relatum is unmoved across the step from `n`: after it the web shows it as before. -/
def Unmoved (W : Web X X) (n : Nat) (x : X) : Prop :=
  W.SameAt n W (n + 1) x

variable {W W' W'' : Web X X} {k k' k'' : Nat} {x : X}

theorem SameAt.refl (W : Web X X) (k : Nat) (x : X) : W.SameAt k W k x :=
  ⟨rfl, rfl, fun _ => ⟨rfl, rfl, rfl⟩⟩

theorem SameAt.symm (same : W.SameAt k W' k' x) : W'.SameAt k' W k x :=
  ⟨same.1.symm, same.2.1.symm,
   fun c => ⟨(same.2.2 c).1.symm, (same.2.2 c).2.1.symm, (same.2.2 c).2.2.symm⟩⟩

theorem SameAt.trans (same : W.SameAt k W' k' x) (same' : W'.SameAt k' W'' k'' x) :
    W.SameAt k W'' k'' x :=
  ⟨same'.1.trans same.1, same'.2.1.trans same.2.1,
   fun c => ⟨(same'.2.2 c).1.trans (same.2.2 c).1, (same'.2.2 c).2.1.trans (same.2.2 c).2.1,
     (same'.2.2 c).2.2.trans (same.2.2 c).2.2⟩⟩

variable {t : Nat} {side : X → Bool}

/-- Away from the step between the two, the web with two steps' changes taken in the other
order shows every relatum as the web does. -/
theorem commute_sameAt_away (other : k ≠ t + 1) (x : X) :
    W.SameAt k (W.commute t side side) k x :=
  ⟨if_neg other, if_neg other, fun _ => ⟨if_neg other, if_neg other, if_neg other⟩⟩

/-- Between them it shows a relatum on the first side as the web before the two steps. -/
theorem commute_sameAt_true (yes : side x = true) :
    W.SameAt t (W.commute t side side) (t + 1) x :=
  ⟨(if_pos rfl).trans (cond_of_true yes), (if_pos rfl).trans (cond_of_true yes),
   fun _ => ⟨(if_pos rfl).trans (cond_of_true yes), (if_pos rfl).trans (cond_of_true yes),
     (if_pos rfl).trans (cond_of_true yes)⟩⟩

/-- And a relatum on the other side as the web after them. -/
theorem commute_sameAt_false (no : side x = false) :
    W.SameAt (t + 2) (W.commute t side side) (t + 1) x :=
  ⟨(if_pos rfl).trans (cond_of_false no), (if_pos rfl).trans (cond_of_false no),
   fun _ => ⟨(if_pos rfl).trans (cond_of_false no), (if_pos rfl).trans (cond_of_false no),
     (if_pos rfl).trans (cond_of_false no)⟩⟩

/-- Activity needing support is a matter of what the web shows: two webs showing every relatum
alike at every step need support alike. -/
theorem dependent_of_sameAt (same : ∀ k x, W.SameAt k W' k x) (dependent : W.Dependent) :
    W'.Dependent :=
  fun n f active c requires =>
    Nat.le_trans (Nat.le_of_eq ((same n f).2.2 c).2.1)
      (Nat.le_trans (dependent n f (cast (same n f).2.1 active) c
          (cast ((same n f).2.2 c).1 requires))
        (Nat.le_of_eq (same n c).1.symm))

end Web

/-! ### Footprints -/

/-- A world's flow and web over one kind of relatum, with a footprint: at each step, the relata
the exchange across it touches. -/
structure Footprinted (X : Type) where
  flow : Flow X X
  web : Web X X
  touch : Nat → X → Bool

namespace Footprinted

variable {X : Type}

/-- The world. -/
def world (r : Footprinted X) : World :=
  ⟨X, r.flow, r.web⟩

/-- The footprint contains each exchange: a relatum a step does not touch takes no part in its
exchange and is unmoved across it. -/
def Contains (r : Footprinted X) : Prop :=
  ∀ n x, r.touch n x = false → ¬ x ∈ r.flow.present n ∧ r.web.Unmoved n x

/-- The exchanges across steps `i` and `j` are joined: some relatum is touched by both, or a
relatum touched by one depends, at the start or the end of its step, on a condition the other
touches. -/
def Joined (r : Footprinted X) (i j : Nat) : Prop :=
  (∃ x, r.touch i x = true ∧ r.touch j x = true) ∨
  (∃ f c, r.touch i f = true ∧ r.touch j c = true ∧
    (r.web.requires i f c ∨ r.web.requires (i + 1) f c)) ∨
  (∃ f c, r.touch j f = true ∧ r.touch i c = true ∧
    (r.web.requires j f c ∨ r.web.requires (j + 1) f c))

/-- **The order of exchanges.** The exchange across step `i` comes before that across `j`: a chain
of joined exchanges leads from it to that one, each later than the last. -/
inductive Precedes (r : Footprinted X) : Nat → Nat → Prop
  | joined {i j : Nat} : i < j → r.Joined i j → Precedes r i j
  | trans {i j k : Nat} : Precedes r i j → Precedes r j k → Precedes r i k

variable {r : Footprinted X}

theorem Joined.symm {i j : Nat} : r.Joined i j → r.Joined j i
  | .inl ⟨x, a, b⟩ => .inl ⟨x, b, a⟩
  | .inr (.inl p) => .inr (.inr p)
  | .inr (.inr p) => .inr (.inl p)

/-- What comes before is earlier: the order is a strict partial order of the steps. -/
theorem Precedes.lt : ∀ {i j : Nat}, r.Precedes i j → i < j
  | _, _, .joined lt _ => lt
  | _, _, .trans a b => Nat.lt_trans a.lt b.lt

theorem Precedes.irrefl {i : Nat} : ¬ r.Precedes i i :=
  fun before => Nat.lt_irrefl i before.lt

theorem Precedes.asymm {i j : Nat} (before : r.Precedes i j) : ¬ r.Precedes j i :=
  fun after => Nat.lt_irrefl i (Nat.lt_trans before.lt after.lt)

/-! ### Two exchanges not joined, taken in the other order -/

/-- The exchanges across steps `t` and `t + 1` taken in the other order, each relatum's changes
moved as the first step's footprint says, the footprint moving with the exchanges. -/
def commute (r : Footprinted X) (t : Nat) : Footprinted X :=
  ⟨r.flow.swap t, r.web.commute t (r.touch t) (r.touch t), fun n => r.touch (swapAt t n)⟩

variable {t : Nat}

/-- Two exchanges not joined touch no relatum in common. -/
theorem disjoint (apart : ¬ r.Joined t (t + 1)) {x : X} (yes : r.touch t x = true) :
    r.touch (t + 1) x = false :=
  match h : r.touch (t + 1) x with
  | true => (apart (.inl ⟨x, yes, h⟩)).elim
  | false => rfl

/-- What a step touches, the commuted web shows across the step it is taken to. -/
theorem commute_shows_first (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {x : X}
    (touched : r.touch (t + 1) x = true) :
    r.web.SameAt (t + 1) (r.commute t).web t x ∧ r.web.SameAt (t + 1 + 1) (r.commute t).web (t + 1) x :=
  have side : r.touch t x = false := match h : r.touch t x with
    | true => Bool.noConfusion ((disjoint apart h).symm.trans touched)
    | false => rfl
  ⟨((contains t x side).2.symm).trans (Web.commute_sameAt_away ne_first x),
   Web.commute_sameAt_false side⟩

theorem commute_shows_second (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {x : X}
    (touched : r.touch t x = true) :
    r.web.SameAt t (r.commute t).web (t + 1) x ∧ r.web.SameAt (t + 1) (r.commute t).web (t + 1 + 1) x :=
  ⟨Web.commute_sameAt_true touched,
   (contains (t + 1) x (disjoint apart touched)).2.trans (Web.commute_sameAt_away ne_last x)⟩

/-- **What a commuted step touches it shows as the step it came from.** In the world with the two
exchanges taken in the other order, a relatum touched across step `m` is shown before and after
it as the world showed it before and after the step whose exchange came to `m`. -/
theorem commute_shows (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {m : Nat} {x : X}
    (touched : r.touch (swapAt t m) x = true) :
    r.web.SameAt (swapAt t m) (r.commute t).web m x ∧
      r.web.SameAt (swapAt t m + 1) (r.commute t).web (m + 1) x :=
  match Nat.decEq m t with
  | .isTrue here =>
    Eq.subst (motive := fun k => r.touch (swapAt t k) x = true →
        r.web.SameAt (swapAt t k) (r.commute t).web k x ∧
          r.web.SameAt (swapAt t k + 1) (r.commute t).web (k + 1) x) here.symm
      (Eq.subst (motive := fun k => r.touch k x = true →
          r.web.SameAt k (r.commute t).web t x ∧ r.web.SameAt (k + 1) (r.commute t).web (t + 1) x)
        (swapAt_first t).symm (commute_shows_first contains apart)) touched
  | .isFalse other => match Nat.decEq m (t + 1) with
    | .isTrue here =>
      Eq.subst (motive := fun k => r.touch (swapAt t k) x = true →
          r.web.SameAt (swapAt t k) (r.commute t).web k x ∧
            r.web.SameAt (swapAt t k + 1) (r.commute t).web (k + 1) x) here.symm
        (Eq.subst (motive := fun k => r.touch k x = true →
            r.web.SameAt k (r.commute t).web (t + 1) x ∧
              r.web.SameAt (k + 1) (r.commute t).web (t + 1 + 1) x)
          (swapAt_second t).symm (commute_shows_second contains apart)) touched
    | .isFalse other' =>
      Eq.subst (motive := fun k => r.web.SameAt k (r.commute t).web m x ∧
          r.web.SameAt (k + 1) (r.commute t).web (m + 1) x) (swapAt_away other other').symm
        ⟨Web.commute_sameAt_away other' x, Web.commute_sameAt_away (ne_succ_of_ne other) x⟩

/-- The footprint moved with the exchanges contains them. -/
theorem commute_contains (contains : r.Contains) : (r.commute t).Contains :=
  fun m x untouched => ⟨(contains (swapAt t m) x untouched).1,
    match Nat.decEq m t with
    | .isTrue here =>
      have second : r.touch (t + 1) x = false :=
        (congrArg (fun k => r.touch k x) (swapAt_first t)).symm.trans
          (Eq.subst (motive := fun k => r.touch (swapAt t k) x = false) here untouched)
      Eq.subst (motive := fun k => (r.commute t).web.Unmoved k x) here.symm
        (match h : r.touch t x with
        | true => ((Web.commute_sameAt_away ne_first x).symm).trans (Web.commute_sameAt_true h)
        | false => ((Web.commute_sameAt_away ne_first x).symm).trans
            ((contains t x h).2.trans ((contains (t + 1) x second).2.trans
              (Web.commute_sameAt_false h))))
    | .isFalse other => match Nat.decEq m (t + 1) with
      | .isTrue here =>
        have first : r.touch t x = false :=
          (congrArg (fun k => r.touch k x) (swapAt_second t)).symm.trans
            (Eq.subst (motive := fun k => r.touch (swapAt t k) x = false) here untouched)
        Eq.subst (motive := fun k => (r.commute t).web.Unmoved k x) here.symm
          (((Web.commute_sameAt_false first).symm).trans (Web.commute_sameAt_away ne_last x))
      | .isFalse other' =>
        ((Web.commute_sameAt_away other' x).symm).trans
          ((contains m x (Eq.subst (motive := fun k => r.touch k x = false)
              (swapAt_away other other') untouched)).2.trans
            (Web.commute_sameAt_away (ne_succ_of_ne other) x))⟩

/-- Joined in the commuted world is joined at the steps the exchanges came from. -/
theorem commute_joined (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {a b : Nat} :
    (r.commute t).Joined a b ↔ r.Joined (swapAt t a) (swapAt t b) :=
  have req : ∀ {m : Nat} {f c : X}, r.touch (swapAt t m) f = true →
      ((r.commute t).web.requires m f c ∨ (r.commute t).web.requires (m + 1) f c) =
        (r.web.requires (swapAt t m) f c ∨ r.web.requires (swapAt t m + 1) f c) :=
    fun touched =>
      have shows := commute_shows contains apart touched
      congr (congrArg Or (shows.1.2.2 _).1) (shows.2.2.2 _).1
  ⟨fun joined => match joined with
    | .inl ⟨x, ta, tb⟩ => .inl ⟨x, ta, tb⟩
    | .inr (.inl ⟨f, c, tf, tc, rq⟩) => .inr (.inl ⟨f, c, tf, tc, cast (req tf) rq⟩)
    | .inr (.inr ⟨f, c, tf, tc, rq⟩) => .inr (.inr ⟨f, c, tf, tc, cast (req tf) rq⟩),
   fun joined => match joined with
    | .inl ⟨x, ta, tb⟩ => .inl ⟨x, ta, tb⟩
    | .inr (.inl ⟨f, c, tf, tc, rq⟩) => .inr (.inl ⟨f, c, tf, tc, cast (req tf).symm rq⟩)
    | .inr (.inr ⟨f, c, tf, tc, rq⟩) => .inr (.inr ⟨f, c, tf, tc, cast (req tf).symm rq⟩)⟩

/-- The commuted world's exchanges at `t` and `t + 1` are not joined either. -/
theorem commute_apart (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    ¬ (r.commute t).Joined t (t + 1) :=
  fun joined => apart (cast (congr (congrArg r.Joined (swapAt_first t)) (swapAt_second t))
    ((commute_joined contains apart).mp joined)).symm

/-- Joined exchanges keep their order through the exchange of two not joined. -/
theorem commute_precedes_of (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    ∀ {i j : Nat}, r.Precedes i j → (r.commute t).Precedes (swapAt t i) (swapAt t j)
  | i, j, .joined lt joined =>
    .joined (swapAt_lt lt fun hi hj => apart (Eq.subst (motive := fun k => r.Joined t k) hj
        (Eq.subst (motive := fun k => r.Joined k j) hi joined)))
      ((commute_joined contains apart).mpr
        (cast (congr (congrArg r.Joined (swapAt_swapAt t i).symm) (swapAt_swapAt t j).symm) joined))
  | _, _, .trans a b => .trans (commute_precedes_of contains apart a) (commute_precedes_of contains apart b)

theorem precedes_of_commute (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    ∀ {a b : Nat}, (r.commute t).Precedes a b → r.Precedes (swapAt t a) (swapAt t b)
  | _, b, .joined lt joined =>
    .joined (swapAt_lt lt fun ha hb => commute_apart contains apart
        (Eq.subst (motive := fun k => (r.commute t).Joined t k) hb
          (Eq.subst (motive := fun k => (r.commute t).Joined k b) ha joined)))
      ((commute_joined contains apart).mp joined)
  | _, _, .trans a b => .trans (precedes_of_commute contains apart a) (precedes_of_commute contains apart b)

/-- **The order is kept through the exchange of two exchanges not joined**, up to the
renumbering of the two steps. -/
theorem commute_precedes (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {a b : Nat} :
    (r.commute t).Precedes a b ↔ r.Precedes (swapAt t a) (swapAt t b) :=
  ⟨precedes_of_commute contains apart,
   fun before => cast (congr (congrArg (r.commute t).Precedes (swapAt_swapAt t a))
     (swapAt_swapAt t b)) (commute_precedes_of contains apart before)⟩

/-- Exchanges not joined are split by the first one's footprint, so taking them in the other
order is a step of `Reorders`. -/
theorem split (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    r.web.Split t (r.touch t) (r.touch t) :=
  ⟨fun c yes => (contains (t + 1) c (disjoint apart yes)).2.1.symm,
   fun c no => (contains t c no).2.1.symm,
   fun f yes => have un := (contains (t + 1) f (disjoint apart yes)).2
     ⟨un.2.1.symm, fun c => ⟨(un.2.2 c).1.symm, (un.2.2 c).2.1.symm, (un.2.2 c).2.2.symm⟩⟩,
   fun f no => have un := (contains t f no).2
     ⟨un.2.1.symm, fun c => ⟨(un.2.2 c).1.symm, (un.2.2 c).2.1.symm, (un.2.2 c).2.2.symm⟩⟩⟩

end Footprinted


/-! ### Commuting again and again: where each exchange goes -/

/-- Where a reordering by a list of steps takes the exchange across step `n`: commuting at `t`
takes it to `swapAt t n`. -/
def place : List Nat → Nat → Nat
  | [], n => n
  | t :: ts, n => place ts (swapAt t n)

/-- Which exchange a reordering by a list of steps brings to step `m`. -/
def origin : List Nat → Nat → Nat
  | [], m => m
  | t :: ts, m => swapAt t (origin ts m)

theorem origin_place : ∀ (ts : List Nat) (n : Nat), origin ts (place ts n) = n
  | [], _ => rfl
  | t :: ts, n => (congrArg (swapAt t) (origin_place ts (swapAt t n))).trans (swapAt_swapAt t n)

theorem place_origin : ∀ (ts : List Nat) (m : Nat), place ts (origin ts m) = m
  | [], _ => rfl
  | t :: ts, m => (congrArg (place ts) (swapAt_swapAt t (origin ts m))).trans (place_origin ts m)

theorem place_append : ∀ (ts us : List Nat) (n : Nat), place (ts ++ us) n = place us (place ts n)
  | [], _, _ => rfl
  | t :: ts, us, n => place_append ts us (swapAt t n)

/-- Every step of a list meets a condition. -/
def EachStep (p : Nat → Prop) : List Nat → Prop
  | [] => True
  | t :: ts => p t ∧ EachStep p ts

theorem EachStep.mono {p q : Nat → Prop} (le : ∀ t, p t → q t) :
    ∀ {ts : List Nat}, EachStep p ts → EachStep q ts
  | [], _ => trivial
  | _ :: _, ⟨here, rest⟩ => ⟨le _ here, EachStep.mono le rest⟩

theorem EachStep.append {p : Nat → Prop} :
    ∀ {ts us : List Nat}, EachStep p ts → EachStep p us → EachStep p (ts ++ us)
  | [], _, _, each => each
  | _ :: _, _, ⟨here, rest⟩, each => ⟨here, EachStep.append rest each⟩

theorem EachStep.always : ∀ ts : List Nat, EachStep (fun _ => True) ts
  | [] => trivial
  | _ :: ts => ⟨trivial, EachStep.always ts⟩

/-- A step that no commutation of a list touches stays where it is. -/
theorem place_fixed {p : Nat → Prop} {n : Nat} (away : ∀ t, p t → n ≠ t ∧ n ≠ t + 1) :
    ∀ {ts : List Nat}, EachStep p ts → place ts n = n
  | [], _ => rfl
  | t :: ts, ⟨here, rest⟩ =>
    (congrArg (place ts) (swapAt_away (away t here).1 (away t here).2)).trans (place_fixed away rest)

namespace Flow

variable {F C : Type} {L L' L'' : Flow F C} {n m k : Nat}

theorem SameExchange.trans (same : L.SameExchange n L' m) (same' : L'.SameExchange m L'' k) :
    L.SameExchange n L'' k :=
  ⟨same'.1.trans same.1, fun f c => ⟨(same'.2 f c).1.trans (same.2 f c).1,
    (same'.2 f c).2.trans (same.2 f c).2⟩⟩

end Flow

namespace Footprinted

variable {X : Type}

/-- Commuting at each step of a list in turn. -/
def reorder : Footprinted X → List Nat → Footprinted X
  | r, [] => r
  | r, t :: ts => (r.commute t).reorder ts

/-- Each commutation of the list takes two exchanges not joined, in the world as it then
stands. -/
def Independent : Footprinted X → List Nat → Prop
  | _, [] => True
  | r, t :: ts => ¬ r.Joined t (t + 1) ∧ (r.commute t).Independent ts

theorem reorder_append : ∀ (r : Footprinted X) (ts us : List Nat),
    r.reorder (ts ++ us) = (r.reorder ts).reorder us
  | _, [], _ => rfl
  | r, t :: ts, us => reorder_append (r.commute t) ts us

theorem Independent.append : ∀ {r : Footprinted X} {ts us : List Nat},
    r.Independent ts → (r.reorder ts).Independent us → r.Independent (ts ++ us)
  | _, [], _, _, each => each
  | _, _ :: _, _, ⟨apart, rest⟩, each => ⟨apart, Independent.append rest each⟩

/-- The footprint of a reordering is the footprint of the steps its exchanges came from. -/
theorem reorder_touch : ∀ (r : Footprinted X) (ts : List Nat) (m : Nat) (x : X),
    (r.reorder ts).touch m x = r.touch (origin ts m) x
  | _, [], _, _ => rfl
  | r, t :: ts, m, x => reorder_touch (r.commute t) ts m x

/-- A reordering takes across each step the exchange of the step it came from. -/
theorem reorder_exchange : ∀ (r : Footprinted X) (ts : List Nat) (m : Nat),
    r.flow.SameExchange (origin ts m) (r.reorder ts).flow m
  | _, [], _ => ⟨rfl, fun _ _ => ⟨rfl, rfl⟩⟩
  | r, t :: ts, m => Flow.SameExchange.trans (L' := (r.commute t).flow)
      ⟨rfl, fun _ _ => ⟨rfl, rfl⟩⟩ (reorder_exchange (r.commute t) ts m)

variable {r : Footprinted X}

theorem reorder_contains : ∀ {r : Footprinted X} {ts : List Nat},
    r.Contains → r.Independent ts → (r.reorder ts).Contains
  | _, [], contains, _ => contains
  | r, t :: _, contains, ⟨_, rest⟩ => reorder_contains (r := r.commute t) (commute_contains contains) rest

/-- **A reordering shows what it moves as the world did.** A relatum touched across a step of
the reordering is shown, before and after it, as the world showed it before and after the step
whose exchange came there. -/
theorem reorder_shows : ∀ {r : Footprinted X} {ts : List Nat}, r.Contains → r.Independent ts →
    ∀ {m : Nat} {x : X}, r.touch (origin ts m) x = true →
      r.web.SameAt (origin ts m) (r.reorder ts).web m x ∧
        r.web.SameAt (origin ts m + 1) (r.reorder ts).web (m + 1) x
  | _, [], _, _, _, _, _ => ⟨Web.SameAt.refl _ _ _, Web.SameAt.refl _ _ _⟩
  | r, t :: ts, contains, ⟨apart, rest⟩, m, _, touched =>
    have later := reorder_shows (r := r.commute t) (commute_contains contains) rest (m := m) touched
    have here := commute_shows contains apart (m := origin ts m) touched
    ⟨here.1.trans later.1, here.2.trans later.2⟩

/-- Joined in a reordering is joined at the steps the exchanges came from. -/
theorem reorder_joined : ∀ {r : Footprinted X} {ts : List Nat}, r.Contains → r.Independent ts →
    ∀ {a b : Nat}, (r.reorder ts).Joined a b ↔ r.Joined (origin ts a) (origin ts b)
  | _, [], _, _, _, _ => Iff.rfl
  | r, t :: _, contains, ⟨apart, rest⟩, _, _ =>
    (reorder_joined (r := r.commute t) (commute_contains contains) rest).trans (commute_joined contains apart)

/-- **The order of exchanges is kept by commuting exchanges not joined**, up to the
renumbering: in a reordering one exchange precedes another exactly where the exchanges they
came from did. -/
theorem reorder_precedes : ∀ {r : Footprinted X} {ts : List Nat}, r.Contains → r.Independent ts →
    ∀ {a b : Nat}, (r.reorder ts).Precedes a b ↔ r.Precedes (origin ts a) (origin ts b)
  | _, [], _, _, _, _ => Iff.rfl
  | r, t :: _, contains, ⟨apart, rest⟩, _, _ =>
    (reorder_precedes (r := r.commute t) (commute_contains contains) rest).trans (commute_precedes contains apart)

/-- Read from the steps the exchanges leave. -/
theorem precedes_place {ts : List Nat} (contains : r.Contains) (independent : r.Independent ts)
    {i j : Nat} : r.Precedes i j ↔ (r.reorder ts).Precedes (place ts i) (place ts j) :=
  have same : r.Precedes i j = r.Precedes (origin ts (place ts i)) (origin ts (place ts j)) :=
    congr (congrArg r.Precedes (origin_place ts i).symm) (origin_place ts j).symm
  (Iff.of_eq same).trans (reorder_precedes contains independent).symm

/-- So a reordering by exchanges not joined keeps the order of joined exchanges. -/
theorem Independent.keeps {ts : List Nat} (contains : r.Contains) (independent : r.Independent ts)
    {i j : Nat} (lt : i < j) (joined : r.Joined i j) : place ts i < place ts j :=
  ((precedes_place contains independent).mp (.joined lt joined)).lt

/-- Commuting exchanges not joined is a reordering in the sense of `Reorders`. -/
theorem reorder_reorders {within : Nat → Prop} : ∀ {r : Footprinted X} {ts : List Nat},
    r.Contains → r.Independent ts → EachStep within ts →
      Reorders within r.flow r.web (r.reorder ts).flow (r.reorder ts).web
  | r, [], _, _, _ => .refl r.flow r.web
  | r, t :: _, contains, ⟨apart, rest⟩, ⟨at_, each⟩ =>
    .swap t (r.touch t) at_ (split contains apart)
      (reorder_reorders (r := r.commute t) (commute_contains contains) rest each)

end Footprinted


namespace Footprinted

variable {X : Type}

/-! ### What carries along commuting exchanges not joined -/

/-- A relatum taking part in an exchange is touched by it, where the footprint contains it. -/
theorem touched_of_mem {r : Footprinted X} (contains : r.Contains) {m : Nat} {x : X}
    (mem : x ∈ r.flow.present m) : r.touch m x = true :=
  match h : r.touch m x with
  | true => rfl
  | false => absurd mem (contains m x h).1

section Transfer

variable {r r' : Footprinted X}

/-- Where each step of `r'` takes the exchange of a step `back m` of `r`, and shows each relatum
it touches, before and after, as `r` shows it across that step, only active relata giving
carries from `r` to `r'`. -/
theorem acting_of_shows (back : Nat → Nat) (contains' : r'.Contains)
    (flows : ∀ m, r.flow.SameExchange (back m) r'.flow m)
    (shows : ∀ m x, r'.touch m x = true →
      r.web.SameAt (back m) r'.web m x ∧ r.web.SameAt (back m + 1) r'.web (m + 1) x)
    (acting : r.flow.Acting r.web) : r'.flow.Acting r'.web :=
  fun m f c mem gives =>
    cast (shows m f (touched_of_mem contains' mem)).1.2.1.symm
      (acting (back m) f c ((flows m).mem.mp mem)
        (Nat.lt_of_lt_of_le gives (Nat.le_of_eq ((flows m).2 f c).2)))

/-- So does only active relata taking, and only from what they draw on. -/
theorem taking_of_shows (back : Nat → Nat) (contains' : r'.Contains)
    (flows : ∀ m, r.flow.SameExchange (back m) r'.flow m)
    (shows : ∀ m x, r'.touch m x = true →
      r.web.SameAt (back m) r'.web m x ∧ r.web.SameAt (back m + 1) r'.web (m + 1) x)
    (taking : r.flow.Taking r.web) : r'.flow.Taking r'.web :=
  fun m f c mem takes =>
    have same := (shows m f (touched_of_mem contains' mem)).1
    have was := taking (back m) f c ((flows m).mem.mp mem)
      (Nat.lt_of_lt_of_le takes (Nat.le_of_eq ((flows m).2 f c).1))
    ⟨cast same.2.1.symm was.1, cast (same.2.2 c).2.2.symm was.2⟩

/-- And bounded transmission: the giver takes part and the receiver comes to stand, so both are
touched, and the descent is one of `r`. -/
theorem transmits_of_shows (back : Nat → Nat) (contains' : r'.Contains)
    (flows : ∀ m, r.flow.SameExchange (back m) r'.flow m)
    (shows : ∀ m x, r'.touch m x = true →
      r.web.SameAt (back m) r'.web m x ∧ r.web.SameAt (back m + 1) r'.web (m + 1) x)
    {c : X} {δ : Nat} (transmits : r.flow.TransmitsWithin r.web c δ) :
    r'.flow.TransmitsWithin r'.web c δ :=
  fun m x g ⟨mem, gives, comes⟩ requires =>
    have giver := (shows m g (touched_of_mem contains' mem)).1
    have moved : r'.touch m x = true := match h : r'.touch m x with
      | true => rfl
      | false => absurd (Eq.subst (motive := fun k => 0 < k) (contains' m x h).2.1 comes.2) comes.1
    have receiver := shows m x moved
    have descends : r.flow.DescendsAt r.web (back m) x g :=
      ⟨(flows m).mem.mp mem, Nat.lt_of_lt_of_le gives (Nat.le_of_eq ((flows m).2 g x).2),
       fun stood => comes.1 (Eq.subst (motive := fun k => 0 < k) receiver.1.1.symm stood),
       Eq.subst (motive := fun k => 0 < k) receiver.2.1 comes.2⟩
    have inherited := transmits (back m) x g descends (cast (receiver.2.2.2 c).1 requires)
    ⟨cast (giver.2.2 c).1.symm inherited.1,
     Nat.le_trans (Nat.le_of_eq (receiver.2.2.2 c).2.1)
       (Nat.le_trans inherited.2 (Nat.le_of_eq (congrArg (· + δ) (giver.2.2 c).2.1.symm)))⟩

end Transfer

variable {r : Footprinted X} {t : Nat}

theorem commute_flows (t m : Nat) : r.flow.SameExchange (swapAt t m) (r.commute t).flow m :=
  ⟨rfl, fun _ _ => ⟨rfl, rfl⟩⟩

theorem commute_back_flows (t m : Nat) : (r.commute t).flow.SameExchange (swapAt t m) r.flow m :=
  ⟨congrArg r.flow.present (swapAt_swapAt t m).symm, fun f c =>
    ⟨congrArg (fun k => r.flow.take k f c) (swapAt_swapAt t m).symm,
     congrArg (fun k => r.flow.give k f c) (swapAt_swapAt t m).symm⟩⟩

/-- And the world shows what a step touches as the commuted world shows it across the step the
exchange was taken to. -/
theorem commute_back_shows (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {m : Nat}
    {x : X} (touched : r.touch m x = true) :
    (r.commute t).web.SameAt (swapAt t m) r.web m x ∧
      (r.commute t).web.SameAt (swapAt t m + 1) r.web (m + 1) x :=
  have shows := commute_shows contains apart (m := swapAt t m)
    (Eq.subst (motive := fun k => r.touch k x = true) (swapAt_swapAt t m).symm touched)
  have shows' := Eq.subst (motive := fun k => r.web.SameAt k (r.commute t).web (swapAt t m) x ∧
      r.web.SameAt (k + 1) (r.commute t).web (swapAt t m + 1) x) (swapAt_swapAt t m) shows
  ⟨shows'.1.symm, shows'.2.symm⟩

theorem commute_acting_iff (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    (r.commute t).flow.Acting (r.commute t).web ↔ r.flow.Acting r.web :=
  ⟨acting_of_shows (r := r.commute t) (swapAt t) contains (commute_back_flows t)
      (fun _ _ touched => commute_back_shows contains apart touched),
   acting_of_shows (r' := r.commute t) (swapAt t) (commute_contains contains) (commute_flows t)
      (fun _ _ touched => commute_shows contains apart touched)⟩

theorem commute_taking_iff (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    (r.commute t).flow.Taking (r.commute t).web ↔ r.flow.Taking r.web :=
  ⟨taking_of_shows (r := r.commute t) (swapAt t) contains (commute_back_flows t)
      (fun _ _ touched => commute_back_shows contains apart touched),
   taking_of_shows (r' := r.commute t) (swapAt t) (commute_contains contains) (commute_flows t)
      (fun _ _ touched => commute_shows contains apart touched)⟩

theorem commute_transmits_iff (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) {c : X}
    {δ : Nat} :
    (r.commute t).flow.TransmitsWithin (r.commute t).web c δ ↔ r.flow.TransmitsWithin r.web c δ :=
  ⟨transmits_of_shows (r := r.commute t) (swapAt t) contains (commute_back_flows t)
      (fun _ _ touched => commute_back_shows contains apart touched),
   transmits_of_shows (r' := r.commute t) (swapAt t) (commute_contains contains) (commute_flows t)
      (fun _ _ touched => commute_shows contains apart touched)⟩

/-- **Activity needing support carries through two exchanges not joined.** Between the two
steps of the other order each active relatum's dependences and their conditions are shown as
before the two steps or as after them: a relatum one step touches does not depend on a condition
the other touches, and a relatum neither touches is the same at both. -/
theorem commute_dependent (contains : r.Contains) (apart : ¬ r.Joined t (t + 1))
    (dependent : r.web.Dependent) : (r.commute t).web.Dependent :=
  have mid : ∀ f, (r.commute t).web.active (t + 1) f → (r.commute t).web.Supported (t + 1) f :=
    fun f active c requires => match hf : r.touch t f with
    | true =>
      have sf := Web.commute_sameAt_true (W := r.web) (side := r.touch t) hf
      have needs := dependent t f (cast sf.2.1 active) c (cast (sf.2.2 c).1 requires)
      have level : (r.commute t).web.level (t + 1) c = r.web.level t c :=
        match hc : r.touch t c with
        | true => (Web.commute_sameAt_true (W := r.web) (side := r.touch t) hc).1
        | false => match hc' : r.touch (t + 1) c with
          | true => (apart (.inr (.inl ⟨f, c, hf, hc', .inl (cast (sf.2.2 c).1 requires)⟩))).elim
          | false => (Web.commute_sameAt_false (W := r.web) (side := r.touch t) hc).1.trans
              ((contains (t + 1) c hc').2.1.trans (contains t c hc).2.1)
      Nat.le_trans (Nat.le_of_eq (sf.2.2 c).2.1) (Nat.le_trans needs (Nat.le_of_eq level.symm))
    | false =>
      have sf := Web.commute_sameAt_false (W := r.web) (side := r.touch t) hf
      match hc : r.touch t c with
      | false =>
        have needs := dependent (t + 2) f (cast sf.2.1 active) c (cast (sf.2.2 c).1 requires)
        Nat.le_trans (Nat.le_of_eq (sf.2.2 c).2.1) (Nat.le_trans needs
          (Nat.le_of_eq (Web.commute_sameAt_false (W := r.web) (side := r.touch t) hc).1.symm))
      | true =>
        have level : (r.commute t).web.level (t + 1) c = r.web.level t c :=
          (Web.commute_sameAt_true (W := r.web) (side := r.touch t) hc).1
        match hf' : r.touch (t + 1) f with
        | true => (apart (.inr (.inr ⟨f, c, hf', hc, .inr (cast (sf.2.2 c).1 requires)⟩))).elim
        | false =>
          have still : r.web.SameAt t r.web (t + 1 + 1) f :=
            (contains t f hf).2.trans (contains (t + 1) f hf').2
          have sf0 : r.web.SameAt t (r.commute t).web (t + 1) f := still.trans sf
          have needs := dependent t f (cast sf0.2.1 active) c (cast (sf0.2.2 c).1 requires)
          Nat.le_trans (Nat.le_of_eq (sf0.2.2 c).2.1) (Nat.le_trans needs (Nat.le_of_eq level.symm))
  fun n f active => match Nat.decEq n (t + 1) with
  | .isTrue here => Eq.subst (motive := fun k => (r.commute t).web.active k f →
        (r.commute t).web.Supported k f) here.symm (mid f) active
  | .isFalse other =>
    have sf := Web.commute_sameAt_away (W := r.web) (side := r.touch t) other f
    fun c requires =>
      Nat.le_trans (Nat.le_of_eq (sf.2.2 c).2.1)
        (Nat.le_trans (dependent n f (cast sf.2.1 active) c (cast (sf.2.2 c).1 requires))
          (Nat.le_of_eq (Web.commute_sameAt_away (W := r.web) (side := r.touch t) other c).1.symm))

/-- Commuting the same two exchanges again shows every relatum as the world did. -/
theorem commute_twice (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) (k : Nat) (x : X) :
    r.web.SameAt k ((r.commute t).commute t).web k x :=
  match Nat.decEq k (t + 1) with
  | .isFalse other => (Web.commute_sameAt_away (W := r.web) (side := r.touch t) other x).trans
      (Web.commute_sameAt_away (W := (r.commute t).web) (side := (r.commute t).touch t) other x)
  | .isTrue here =>
    Eq.subst (motive := fun j => r.web.SameAt j ((r.commute t).commute t).web j x) here.symm
      (match h : r.touch (swapAt t t) x with
      | true =>
        have second : r.touch (t + 1) x = true :=
          (congrArg (fun j => r.touch j x) (swapAt_first t)).symm.trans h
        have first : r.touch t x = false := match h' : r.touch t x with
          | true => Bool.noConfusion ((disjoint apart h').symm.trans second)
          | false => rfl
        ((contains t x first).2.symm).trans
          ((Web.commute_sameAt_away (W := r.web) (side := r.touch t) ne_first x).trans
            (Web.commute_sameAt_true (W := (r.commute t).web) (side := (r.commute t).touch t) h))
      | false =>
        have second : r.touch (t + 1) x = false :=
          (congrArg (fun j => r.touch j x) (swapAt_first t)).symm.trans h
        (contains (t + 1) x second).2.trans
          ((Web.commute_sameAt_away (W := r.web) (side := r.touch t) ne_last x).trans
            (Web.commute_sameAt_false (W := (r.commute t).web) (side := (r.commute t).touch t) h)))

theorem commute_dependent_iff (contains : r.Contains) (apart : ¬ r.Joined t (t + 1)) :
    (r.commute t).web.Dependent ↔ r.web.Dependent :=
  ⟨fun dependent => Web.dependent_of_sameAt (fun k x => (commute_twice contains apart k x).symm)
      (commute_dependent (commute_contains contains) (commute_apart contains apart) dependent),
   commute_dependent contains apart⟩

/-! ### Along repeated commutation -/

theorem reorder_acting_iff : ∀ {r : Footprinted X} {ts : List Nat}, r.Contains → r.Independent ts →
    ((r.reorder ts).flow.Acting (r.reorder ts).web ↔ r.flow.Acting r.web)
  | _, [], _, _ => Iff.rfl
  | r, t :: _, contains, ⟨apart, rest⟩ =>
    (reorder_acting_iff (r := r.commute t) (commute_contains contains) rest).trans (commute_acting_iff contains apart)

theorem reorder_taking_iff : ∀ {r : Footprinted X} {ts : List Nat}, r.Contains → r.Independent ts →
    ((r.reorder ts).flow.Taking (r.reorder ts).web ↔ r.flow.Taking r.web)
  | _, [], _, _ => Iff.rfl
  | r, t :: _, contains, ⟨apart, rest⟩ =>
    (reorder_taking_iff (r := r.commute t) (commute_contains contains) rest).trans (commute_taking_iff contains apart)

theorem reorder_transmits_iff {c : X} {δ : Nat} : ∀ {r : Footprinted X} {ts : List Nat},
    r.Contains → r.Independent ts →
      ((r.reorder ts).flow.TransmitsWithin (r.reorder ts).web c δ ↔ r.flow.TransmitsWithin r.web c δ)
  | _, [], _, _ => Iff.rfl
  | r, t :: _, contains, ⟨apart, rest⟩ =>
    (reorder_transmits_iff (r := r.commute t) (commute_contains contains) rest).trans (commute_transmits_iff contains apart)

theorem reorder_dependent_iff : ∀ {r : Footprinted X} {ts : List Nat}, r.Contains →
    r.Independent ts → ((r.reorder ts).web.Dependent ↔ r.web.Dependent)
  | _, [], _, _ => Iff.rfl
  | r, t :: _, contains, ⟨apart, rest⟩ =>
    (reorder_dependent_iff (r := r.commute t) (commute_contains contains) rest).trans
      (commute_dependent_iff contains apart)

/-- **Commuting exchanges not joined keeps every premise.** However often two consecutive
exchanges not joined are taken in the other order, the world meets balance, dissipation, only
active relata giving, only active relata taking, activity needing support, embodiment and bounded
transmission exactly where it did. -/
theorem reorder_premises {ts : List Nat} (contains : r.Contains) (independent : r.Independent ts) :
    ((r.reorder ts).world.Balanced ↔ r.world.Balanced) ∧
    ((r.reorder ts).world.Dissipative ↔ r.world.Dissipative) ∧
    ((r.reorder ts).world.Acting ↔ r.world.Acting) ∧
    ((r.reorder ts).world.Taking ↔ r.world.Taking) ∧
    ((r.reorder ts).world.Dependent ↔ r.world.Dependent) ∧
    ((r.reorder ts).world.Embodied ↔ r.world.Embodied) ∧
    ((r.reorder ts).world.Transmitting ↔ r.world.Transmitting) :=
  have laws := Reorders.laws (reorder_reorders contains independent (EachStep.always ts))
  ⟨laws.1, laws.2.1, reorder_acting_iff contains independent,
   reorder_taking_iff contains independent, reorder_dependent_iff contains independent, laws.2.2,
   ⟨fun ⟨δ, transmits⟩ => ⟨δ, fun c => (reorder_transmits_iff contains independent).mp (transmits c)⟩,
    fun ⟨δ, transmits⟩ => ⟨δ, fun c => (reorder_transmits_iff contains independent).mpr (transmits c)⟩⟩⟩

end Footprinted

/-! ### Counts along any reordering -/

/-- Activity decided in a web is decided with two steps' changes taken in the other order. -/
def Web.commuteDecided {F C : Type} {W : Web F C} {t : Nat} {sideF : F → Bool} {sideC : C → Bool}
    (decided : ∀ n f, Decidable (W.active n f)) :
    ∀ n f, Decidable ((W.commute t sideF sideC).active n f) :=
  fun n f => match Nat.decEq n (t + 1) with
  | .isTrue here => match h : sideF f with
    | true => cast (congrArg Decidable (show (W.commute t sideF sideC).active n f = W.active t f from
        (if_pos here).trans (cond_of_true h)).symm) (decided t f)
    | false => cast (congrArg Decidable (show (W.commute t sideF sideC).active n f = W.active (t + 2) f from
        (if_pos here).trans (cond_of_false h)).symm) (decided (t + 2) f)
  | .isFalse other => cast (congrArg Decidable (show (W.commute t sideF sideC).active n f = W.active n f from
      if_neg other).symm) (decided n f)

/-- Members of a family coming to be number the same for two decisions of the same
determination. -/
theorem comings_of_iff {α : Type} {as : List α} {p q : α → Nat → Prop} [∀ a n, Decidable (p a n)]
    [∀ a n, Decidable (q a n)] (same : ∀ a n, p a n ↔ q a n) (t : Nat) :
    comings as p t = comings as q t :=
  total_congr (fun a => mark_iff
    ⟨fun ⟨no, yes⟩ => ⟨fun h => no ((same a t).mpr h), (same a (t + 1)).mp yes⟩,
     fun ⟨no, yes⟩ => ⟨fun h => no ((same a t).mp h), (same a (t + 1)).mpr yes⟩⟩) as

theorem ceasings_of_iff {α : Type} {as : List α} {p q : α → Nat → Prop} [∀ a n, Decidable (p a n)]
    [∀ a n, Decidable (q a n)] (same : ∀ a n, p a n ↔ q a n) (t : Nat) :
    ceasings as p t = ceasings as q t :=
  total_congr (fun a => mark_iff
    ⟨fun ⟨yes, no⟩ => ⟨(same a t).mp yes, fun h => no ((same a (t + 1)).mpr h)⟩,
     fun ⟨yes, no⟩ => ⟨(same a t).mpr yes, fun h => no ((same a (t + 1)).mp h)⟩⟩) as

/-- **Along any reordering, the counts of arising and ceasing.** Over a stretch holding every
commuted pair, the relata of a finite family arising, and those ceasing, number what they
number in the world, with activity decided in the two worlds; no condition on the commuted
exchanges is needed. -/
theorem Reorders.counts {X : Type} {S m : Nat} (xs : List X) :
    ∀ {L L' : Flow X X} {W W' : Web X X} [∀ n x, Decidable (W.active n x)]
      [∀ n x, Decidable (W'.active n x)],
      Reorders (fun t => S ≤ t ∧ t + 2 ≤ S + m) L W L' W' →
      total (steps S m) (comings xs fun x n => W'.active n x) =
        total (steps S m) (comings xs fun x n => W.active n x) ∧
      total (steps S m) (ceasings xs fun x n => W'.active n x) =
        total (steps S m) (ceasings xs fun x n => W.active n x)
  | _, _, W, _, decided, decided', .refl _ _ =>
    ⟨total_congr (fun n => @comings_of_iff X xs (fun x k => W.active k x) (fun x k => W.active k x)
        (fun a k => decided' k a) (fun a k => decided k a) (fun _ _ => Iff.rfl) n) (steps S m),
     total_congr (fun n => @ceasings_of_iff X xs (fun x k => W.active k x) (fun x k => W.active k x)
        (fun a k => decided' k a) (fun a k => decided k a) (fun _ _ => Iff.rfl) n) (steps S m)⟩
  | _, _, W, _, decided, _, .swap t side ⟨from_, to⟩ split more =>
    haveI : ∀ n x, Decidable ((W.commute t side side).active n x) := Web.commuteDecided decided
    have next := Reorders.counts xs more
    have web := Web.commute_commuted split
    ⟨next.1.trans (comings_moved (p := fun x n => W.active n x)
       (p' := fun x n => (W.commute t side side).active n x) (fun x _ => web.2.1 x) from_ to),
     next.2.trans (ceasings_moved (p := fun x n => W.active n x)
       (p' := fun x n => (W.commute t side side).active n x) (fun x _ => web.2.1 x) from_ to)⟩

/-! ### Where the order registers, every footprint joins the two exchanges -/

namespace Crossing

/-- **Every footprint containing the two exchanges joins them.** The first relatum, which the
first exchange touches (it ceases), depends on the second, which the second touches (it ceases to
stand). -/
theorem joined (touch : Nat → Nat → Bool)
    (contains : (⟨flow, web, touch⟩ : Footprinted Nat).Contains) :
    (⟨flow, web, touch⟩ : Footprinted Nat).Joined 0 1 :=
  have first : touch 0 0 = true := match h : touch 0 0 with
    | true => rfl
    | false => Bool.noConfusion
        (cast (contains 0 0 h).2.2.1.symm (rfl : act 0 0 = true) : act 1 0 = true)
  have second : touch 1 1 = true := match h : touch 1 1 with
    | true => rfl
    | false => Nat.noConfusion ((contains 1 1 h).2.1 : (0 : Nat) = 2)
  .inr (.inl ⟨0, 1, first, second, .inl ⟨rfl, rfl⟩⟩)

/-- So `Reorders` takes in the other order two exchanges every footprint joins, and activity
needing support fails: it carries only where the commuted exchanges are not joined. -/
theorem reorders_joined :
    Reorders (fun _ => True) flow web (flow.swap 0) (web.commute 0 firstSide firstSide) ∧
    (∀ touch, (⟨flow, web, touch⟩ : Footprinted Nat).Contains →
      (⟨flow, web, touch⟩ : Footprinted Nat).Joined 0 1) ∧
    web.Dependent ∧ ¬ (web.commute 0 firstSide firstSide).Dependent :=
  ⟨.swap 0 firstSide trivial split (.refl _ _), joined, dependent, order_registers.2.2.2.2⟩

end Crossing

namespace Arising

/-- Every footprint containing the two exchanges joins them: the first relatum arises across the
first step and gives across the second. -/
theorem joined (touch : Nat → Nat → Bool)
    (contains : (⟨flow, web, touch⟩ : Footprinted Nat).Contains) :
    (⟨flow, web, touch⟩ : Footprinted Nat).Joined 0 1 :=
  have first : touch 0 0 = true := match h : touch 0 0 with
    | true => rfl
    | false => Bool.noConfusion
        (cast (contains 0 0 h).2.2.1 (rfl : act 1 0 = true) : act 0 0 = true)
  have second : touch 1 0 = true := match h : touch 1 0 with
    | true => rfl
    | false => absurd (List.Mem.head [] : (0 : Nat) ∈ [0]) (contains 1 0 h).1
  .inl ⟨0, first, second⟩

/-- So `Reorders` takes in the other order two exchanges every footprint joins, and only active
relata giving fails. -/
theorem reorders_joined :
    Reorders (fun _ => True) flow web (flow.swap 0) (web.commute 0 firstSide firstSide) ∧
    (∀ touch, (⟨flow, web, touch⟩ : Footprinted Nat).Contains →
      (⟨flow, web, touch⟩ : Footprinted Nat).Joined 0 1) ∧
    flow.Acting web ∧ ¬ (flow.swap 0).Acting (web.commute 0 firstSide firstSide) :=
  ⟨.swap 0 firstSide trivial split (.refl _ _), joined, acting, order_registers.2.2.2.2⟩

end Arising


/-! ### Bringing one exchange forward -/

/-- Cancelling the same number added first. -/
theorem le_of_add_le_add_left_core {S a b : Nat} (le : S + a ≤ S + b) : a ≤ b :=
  le_of_add_le_add_right S (Nat.le_trans (Nat.le_of_eq (Nat.add_comm a S))
    (Nat.le_trans le (Nat.le_of_eq (Nat.add_comm S b))))

/-- The steps `S + d - 1`, …, `S + 1`, `S`: commuting at each in turn brings the exchange across
step `S + d` to step `S`, each exchange between them one step later. -/
def lowering (S : Nat) : Nat → List Nat
  | 0 => []
  | d + 1 => (S + d) :: lowering S d

theorem place_lowering_top (S : Nat) : ∀ d, place (lowering S d) (S + d) = S
  | 0 => rfl
  | d + 1 => (congrArg (place (lowering S d)) (swapAt_second (S + d))).trans (place_lowering_top S d)

theorem place_lowering_outside (S : Nat) :
    ∀ d {n : Nat}, (n < S ∨ S + d < n) → place (lowering S d) n = n
  | 0, _, _ => rfl
  | d + 1, n, out =>
    have away : n ≠ S + d ∧ n ≠ S + d + 1 := match out with
      | .inl below => And.intro (Nat.ne_of_lt (Nat.lt_of_lt_of_le below (Nat.le_add_right S d)))
          (Nat.ne_of_lt (Nat.lt_of_lt_of_le below (Nat.le_add_right S (d + 1))))
      | .inr above => And.intro (Nat.ne_of_gt (Nat.lt_trans (Nat.lt_succ_self (S + d)) above))
          (Nat.ne_of_gt above)
    (congrArg (place (lowering S d)) (swapAt_away away.1 away.2)).trans
      (place_lowering_outside S d (match out with
        | .inl below => .inl below
        | .inr above => .inr (Nat.lt_trans (Nat.lt_succ_self _) above)))

theorem place_lowering_below (S : Nat) :
    ∀ d {n : Nat}, S ≤ n → n < S + d → place (lowering S d) n = n + 1
  | 0, _, from_, below => absurd below (Nat.not_lt_of_le from_)
  | d + 1, n, from_, below => match Nat.decEq n (S + d) with
    | .isTrue here => Eq.subst (motive := fun k => place (lowering S (d + 1)) k = k + 1) here.symm
        ((congrArg (place (lowering S d)) (swapAt_first (S + d))).trans
          (place_lowering_outside S d (.inr (Nat.lt_succ_self _))))
    | .isFalse other =>
      have lt : n < S + d := lt_of_le_ne (Nat.le_of_lt_succ below) other
      (congrArg (place (lowering S d)) (swapAt_of_lt lt)).trans (place_lowering_below S d from_ lt)

theorem lowering_within (S M : Nat) :
    ∀ d, d < M → EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + M) (lowering S d)
  | 0, _ => trivial
  | d + 1, lt => ⟨⟨Nat.le_add_right S d,
      Nat.le_trans (Nat.le_of_eq (Nat.add_assoc S d 2)) (Nat.add_le_add_left lt S)⟩,
    lowering_within S M d (Nat.lt_of_succ_lt lt)⟩

namespace Footprinted

variable {X : Type}

/-- Where no exchange from step `S` up to step `S + d` is joined to the one across `S + d`,
bringing that one to `S` commutes exchanges not joined. -/
theorem lowering_independent {S : Nat} : ∀ {d : Nat} {r : Footprinted X}, r.Contains →
    (∀ p, S ≤ p → p < S + d → ¬ r.Joined p (S + d)) → r.Independent (lowering S d)
  | 0, _, _, _ => trivial
  | d + 1, r, contains, free =>
    have apart : ¬ r.Joined (S + d) (S + d + 1) :=
      free (S + d) (Nat.le_add_right S d) (Nat.lt_succ_self _)
    ⟨apart, lowering_independent (r := r.commute (S + d)) (commute_contains contains)
      fun p from_ below joined =>
      free p from_ (Nat.lt_succ_of_lt below)
        (cast (congr (congrArg r.Joined (swapAt_of_lt below)) (swapAt_first (S + d)))
          ((commute_joined contains apart).mp joined))⟩

end Footprinted

/-! ### The converse: every renumbering keeping the order is reached -/

/-- `π` renumbers the `m` steps from `S` among themselves, `σ` taking them back. -/
def Reindexes (S m : Nat) (π σ : Nat → Nat) : Prop :=
  ∀ i, S ≤ i → i < S + m →
    (S ≤ π i ∧ π i < S + m ∧ σ (π i) = i) ∧ (S ≤ σ i ∧ σ i < S + m ∧ π (σ i) = i)

namespace Footprinted

variable {X : Type}

/-- A renumbering keeps the order of joined exchanges within the stretch of `m` steps from
`S`. -/
def Keeps (r : Footprinted X) (S m : Nat) (π : Nat → Nat) : Prop :=
  ∀ i j, S ≤ i → j < S + m → i < j → r.Joined i j → π i < π j

/-- The exchange a renumbering keeping the order brings first is joined to none before it. -/
theorem first_free {r : Footprinted X} {S m : Nat} {π σ : Nat → Nat}
    (reindex : Reindexes S (m + 1) π σ) (keeps : r.Keeps S (m + 1) π) {p : Nat} (from_ : S ≤ p)
    (below : p < σ S) : ¬ r.Joined p (σ S) :=
  fun joined =>
    have hS := (reindex S (Nat.le_refl S) (Nat.lt_add_of_pos_right (Nat.succ_pos m))).2
    have hp := (reindex p from_ (Nat.lt_trans below hS.2.1)).1
    Nat.not_le_of_gt (Nat.lt_of_lt_of_le (keeps p (σ S) from_ hS.2.1 below joined)
      (Nat.le_of_eq hS.2.2)) hp.1

section Lowered

variable {S m d : Nat}

/-- Brought forward, the other exchanges of the stretch lie in the rest of it. -/
theorem lowered_place (dm : d ≤ m) {n : Nat} (from_ : S ≤ n) (below : n < S + (m + 1))
    (other : n ≠ S + d) : S + 1 ≤ place (lowering S d) n ∧ place (lowering S d) n < S + 1 + m :=
  match Nat.lt_or_ge n (S + d) with
  | .inl lt => Eq.subst (motive := fun k => S + 1 ≤ k ∧ k < S + 1 + m)
      (place_lowering_below S d from_ lt).symm
      ⟨Nat.succ_le_succ from_, Nat.lt_of_le_of_lt (Nat.succ_le_of_lt lt)
        (Nat.lt_of_le_of_lt (Nat.add_le_add_left dm S)
          (Nat.lt_of_lt_of_le (Nat.lt_succ_self _) (Nat.le_of_eq (Nat.add_right_comm S 1 m).symm)))⟩
  | .inr ge =>
    have gt : S + d < n := lt_of_le_ne ge (fun same => other same.symm)
    Eq.subst (motive := fun k => S + 1 ≤ k ∧ k < S + 1 + m)
      (place_lowering_outside S d (.inr gt)).symm
      ⟨Nat.le_trans (Nat.succ_le_succ (Nat.le_add_right S d)) gt,
       Nat.lt_of_lt_of_le below (Nat.le_of_eq (Nat.add_right_comm S 1 m).symm)⟩

/-- And each step of the rest holds one of them. -/
theorem lowered_origin (dm : d ≤ m) {a : Nat} (from_ : S + 1 ≤ a) (below : a < S + 1 + m) :
    S ≤ origin (lowering S d) a ∧ origin (lowering S d) a < S + (m + 1) ∧
      origin (lowering S d) a ≠ S + d :=
  have back := place_origin (lowering S d) a
  have low : S ≤ origin (lowering S d) a := match Nat.lt_or_ge (origin (lowering S d) a) S with
    | .inl lt => absurd (Nat.lt_trans (Nat.lt_of_lt_of_le (Nat.lt_succ_self S) from_)
        (Eq.subst (motive := (· < S)) ((place_lowering_outside S d (.inl lt)).symm.trans back) lt))
        (Nat.lt_irrefl S)
    | .inr ge => ge
  have high : origin (lowering S d) a < S + (m + 1) :=
    match Nat.lt_or_ge (origin (lowering S d) a) (S + (m + 1)) with
    | .inl lt => lt
    | .inr ge =>
      have gt : S + d < origin (lowering S d) a :=
        Nat.lt_of_lt_of_le (Nat.lt_succ_of_le (Nat.add_le_add_left dm S)) ge
      absurd (Nat.lt_of_lt_of_le below (Nat.le_trans
          (Nat.le_of_eq (Nat.add_right_comm S 1 m))
          (Nat.le_trans ge (Nat.le_of_eq ((place_lowering_outside S d (.inr gt)).symm.trans back)))))
        (Nat.lt_irrefl _)
  ⟨low, high, fun same => absurd (Nat.lt_of_lt_of_le (Nat.lt_succ_self S) (Nat.le_trans from_
      (Nat.le_of_eq (back.symm.trans ((congrArg (place (lowering S d)) same).trans
        (place_lowering_top S d))))))
    (Nat.lt_irrefl _)⟩

/-- Brought forward, the renumbering of the rest renumbers the rest among itself. -/
theorem lowered_reindexes {π σ : Nat → Nat} (reindex : Reindexes S (m + 1) π σ)
    (hk : σ S = S + d) (dm : d ≤ m) :
    Reindexes (S + 1) m (fun a => π (origin (lowering S d) a))
      (fun b => place (lowering S d) (σ b)) :=
  have hS := (reindex S (Nat.le_refl S) (Nat.lt_add_of_pos_right (Nat.succ_pos m))).2
  fun i from_ below =>
    have wide : S ≤ i ∧ i < S + (m + 1) := ⟨Nat.le_of_succ_le from_,
      Nat.lt_of_lt_of_le below (Nat.le_of_eq (Nat.add_right_comm S 1 m))⟩
    have n := lowered_origin dm from_ below
    have hn := (reindex (origin (lowering S d) i) n.1 n.2.1).1
    have moved : S < π (origin (lowering S d) i) := lt_of_le_ne hn.1 fun same =>
      n.2.2 (hn.2.2.symm.trans ((congrArg σ same.symm).trans hk))
    have hi := (reindex i wide.1 wide.2).2
    have other : σ i ≠ S + d := fun same => absurd
      (Nat.lt_of_lt_of_le (Nat.lt_succ_self S) (Nat.le_trans from_
        (Nat.le_of_eq (hi.2.2.symm.trans ((congrArg π (same.trans hk.symm)).trans hS.2.2)))))
      (Nat.lt_irrefl _)
    have placed := lowered_place dm hi.1 hi.2.1 other
    ⟨⟨moved, Nat.lt_of_lt_of_le hn.2.1 (Nat.le_of_eq (Nat.add_right_comm S 1 m).symm),
      (congrArg (place (lowering S d)) hn.2.2).trans (place_origin (lowering S d) i)⟩,
     ⟨placed.1, placed.2,
      (congrArg π (origin_place (lowering S d) (σ i))).trans hi.2.2⟩⟩

/-- And keeps the order of joined exchanges of the world brought forward. -/
theorem lowered_keeps {r : Footprinted X} {π : Nat → Nat} (contains : r.Contains)
    (independent : r.Independent (lowering S d)) (keeps : r.Keeps S (m + 1) π) (dm : d ≤ m) :
    (r.reorder (lowering S d)).Keeps (S + 1) m (fun a => π (origin (lowering S d) a)) :=
  fun a b from_ below lt joined =>
    have na := lowered_origin dm from_ (Nat.lt_trans lt below)
    have nb := lowered_origin dm (Nat.le_trans from_ (Nat.le_of_lt lt)) below
    have joined' := (reorder_joined contains independent).mp joined
    match Nat.lt_or_ge (origin (lowering S d) a) (origin (lowering S d) b) with
    | .inl before => keeps _ _ na.1 nb.2.1 before joined'
    | .inr ge => match Nat.lt_or_ge (origin (lowering S d) b) (origin (lowering S d) a) with
      | .inl after =>
        have back := ((precedes_place contains independent).mp (.joined after joined'.symm)).lt
        have ba : b < a := Eq.subst (motive := fun k => k < a) (place_origin (lowering S d) b)
          (Eq.subst (motive := fun k => place (lowering S d) (origin (lowering S d) b) < k)
            (place_origin (lowering S d) a) back)
        absurd (Nat.lt_trans lt ba) (Nat.lt_irrefl a)
      | .inr ge' =>
        have same : a = b := (place_origin (lowering S d) a).symm.trans
          ((congrArg (place (lowering S d)) (Nat.le_antisymm ge' ge)).trans
            (place_origin (lowering S d) b))
        absurd (Eq.subst (motive := (a < ·)) same.symm lt) (Nat.lt_irrefl a)

end Lowered

/-- One step of the sort: bring forward the exchange the renumbering puts first, then sort the
rest. -/
theorem sorts_step {m S d : Nat} {r : Footprinted X} {π σ : Nat → Nat} (contains : r.Contains)
    (reindex : Reindexes S (m + 1) π σ) (keeps : r.Keeps S (m + 1) π) (hk : σ S = S + d)
    (sub : ∀ {r' : Footprinted X} {π' σ' : Nat → Nat}, r'.Contains →
      Reindexes (S + 1) m π' σ' → r'.Keeps (S + 1) m π' →
      ∃ ts, EachStep (fun t => S + 1 ≤ t ∧ t + 2 ≤ S + 1 + m) ts ∧ r'.Independent ts ∧
        ∀ i, S + 1 ≤ i → i < S + 1 + m → place ts i = π' i) :
    ∃ ts, EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + (m + 1)) ts ∧ r.Independent ts ∧
      ∀ i, S ≤ i → i < S + (m + 1) → place ts i = π i :=
  have hS := (reindex S (Nat.le_refl S) (Nat.lt_add_of_pos_right (Nat.succ_pos m))).2
  have top : S + d < S + (m + 1) := Eq.subst (motive := (· < S + (m + 1))) hk hS.2.1
  have dm : d ≤ m :=
    Nat.le_of_lt_succ (le_of_add_le_add_left_core (S := S) (a := d + 1) (b := m + 1) top)
  have free : ∀ p, S ≤ p → p < S + d → ¬ r.Joined p (S + d) := fun p from_ below =>
    Eq.subst (motive := fun k => ¬ r.Joined p k) hk
      (first_free reindex keeps from_ (Eq.subst (motive := (p < ·)) hk.symm below))
  have independent := lowering_independent contains free
  match sub (reorder_contains contains independent) (lowered_reindexes reindex hk dm)
      (lowered_keeps contains independent keeps dm) with
  | ⟨rest, within, independent', places⟩ =>
    ⟨lowering S d ++ rest,
     EachStep.append (lowering_within S (m + 1) d (Nat.lt_succ_of_le dm))
       (EachStep.mono (fun _ bounds => ⟨Nat.le_of_succ_le bounds.1,
         Nat.le_trans bounds.2 (Nat.le_of_eq (Nat.add_right_comm S 1 m))⟩) within),
     independent.append independent',
     fun i from_ below => (place_append (lowering S d) rest i).trans
       (match Nat.decEq i (S + d) with
       | .isTrue here =>
         have first : place (lowering S d) i = S :=
           (congrArg (place (lowering S d)) here).trans (place_lowering_top S d)
         (congrArg (place rest) first).trans
           ((place_fixed (p := fun t => S + 1 ≤ t ∧ t + 2 ≤ S + 1 + m)
             (fun _ bounds => ⟨Nat.ne_of_lt bounds.1,
               Nat.ne_of_lt (Nat.lt_succ_of_lt bounds.1)⟩) within).trans
             (hS.2.2.symm.trans (congrArg π (hk.trans here.symm))))
       | .isFalse other =>
         have placed := lowered_place dm from_ below other
         (places (place (lowering S d) i) placed.1 placed.2).trans
           (congrArg π (origin_place (lowering S d) i)))⟩

/-- **Every renumbering keeping the order is reached by commuting exchanges not joined**
(bubble sort, one exchange brought forward at a time): for a renumbering of a stretch of steps
among themselves that keeps the order of joined exchanges, some list of commutations within the
stretch, each of two exchanges not joined, takes each exchange where the renumbering does. -/
theorem sorts : ∀ (m S : Nat) {r : Footprinted X} {π σ : Nat → Nat}, r.Contains →
    Reindexes S m π σ → r.Keeps S m π →
      ∃ ts, EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + m) ts ∧ r.Independent ts ∧
        ∀ i, S ≤ i → i < S + m → place ts i = π i
  | 0, _, _, _, _, _, _, _ =>
    ⟨[], trivial, trivial, fun _ from_ below => absurd below (Nat.not_lt_of_le from_)⟩
  | m + 1, S, _, _, _, contains, reindex, keeps =>
    match le_dest (reindex S (Nat.le_refl S) (Nat.lt_add_of_pos_right (Nat.succ_pos m))).2.1 with
    | ⟨_, hk⟩ => sorts_step contains reindex keeps hk
        (fun contains' reindex' keeps' => sorts m (S + 1) contains' reindex' keeps')

/-- So the renumberings reached by commuting exchanges not joined within a stretch are exactly
those keeping the order of joined exchanges. -/
theorem sorts_iff {S m : Nat} {r : Footprinted X} {π σ : Nat → Nat} (contains : r.Contains)
    (reindex : Reindexes S m π σ) :
    (∃ ts, EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + m) ts ∧ r.Independent ts ∧
        ∀ i, S ≤ i → i < S + m → place ts i = π i) ↔ r.Keeps S m π :=
  ⟨fun ⟨ts, _, independent, places⟩ i j from_ below lt joined =>
    Eq.subst (motive := fun k => k < π j) (places i from_ (Nat.lt_trans lt below))
      (Eq.subst (motive := fun k => place ts i < k)
        (places j (Nat.le_trans from_ (Nat.le_of_lt lt)) below)
        (Independent.keeps contains independent lt joined)),
   sorts m S contains reindex⟩

/-- A reordering within a stretch leaves the world before it as it was. -/
theorem reorder_before {S M : Nat} : ∀ {r : Footprinted X} {ts : List Nat},
    EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + M) ts → ∀ {k : Nat} (x : X), k ≤ S →
      r.web.SameAt k (r.reorder ts).web k x
  | r, [], _, _, x, _ => Web.SameAt.refl r.web _ x
  | r, t :: _, ⟨⟨from_, _⟩, rest⟩, _, x, le =>
    (Web.commute_sameAt_away (W := r.web) (side := r.touch t)
      (Nat.ne_of_lt (Nat.lt_succ_of_le (Nat.le_trans le from_))) x).trans
      (reorder_before (r := r.commute t) rest x le)

/-- The step of the converse's induction: the reordering's web and the other world's show every
relatum alike at each step of the stretch. -/
theorem converse_webs {S m : Nat} {r r₂ : Footprinted X} {π σ : Nat → Nat} {ts : List Nat}
    (contains : r.Contains) (contains₂ : r₂.Contains) (independent : r.Independent ts)
    (within : EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + m) ts) (reindex : Reindexes S m π σ)
    (came : ∀ a, S ≤ a → a < S + m → origin ts a = σ a)
    (footprints : ∀ i x, S ≤ i → i < S + m → r₂.touch (π i) x = r.touch i x)
    (changes : ∀ i x, S ≤ i → i < S + m → r.touch i x = true →
      r.web.SameAt (i + 1) r₂.web (π i + 1) x)
    (start : ∀ x, r.web.SameAt S r₂.web S x) :
    ∀ e, e ≤ m → ∀ x, (r.reorder ts).web.SameAt (S + e) r₂.web (S + e) x
  | 0, _, x => (reorder_before within x (Nat.le_refl S)).symm.trans (start x)
  | e + 1, le, x =>
    have below : S + e < S + m :=
      Nat.lt_of_lt_of_le (Nat.lt_succ_self _) (Nat.add_le_add_left le S)
    have hσ := (reindex (S + e) (Nat.le_add_right S e) below).2
    have hk := came (S + e) (Nat.le_add_right S e) below
    have earlier := converse_webs contains contains₂ independent within reindex came footprints
      changes start e (Nat.le_of_succ_le le) x
    match h : r.touch (origin ts (S + e)) x with
    | false =>
      have still := (reorder_contains contains independent (S + e) x
        ((reorder_touch r ts (S + e) x).trans h)).2
      have still₂ := (contains₂ (S + e) x
        ((congrArg (fun k => r₂.touch k x) hσ.2.2.symm).trans
          ((footprints (σ (S + e)) x hσ.1 hσ.2.1).trans
            ((congrArg (fun k => r.touch k x) hk).symm.trans h)))).2
      still.symm.trans (earlier.trans still₂)
    | true =>
      have shows := (reorder_shows contains independent h).2
      have changed := changes (σ (S + e)) x hσ.1 hσ.2.1
        ((congrArg (fun k => r.touch k x) hk).symm.trans h)
      shows.symm.trans (Eq.subst (motive := fun k => r.web.SameAt (k + 1) r₂.web (S + e + 1) x)
        hk.symm (Eq.subst (motive := fun k => r.web.SameAt (σ (S + e) + 1) r₂.web (k + 1) x)
          hσ.2.2 changed))

/-- **The converse: the same exchanges, footprints and changes, with the order of joined
exchanges kept, from the same start, are a reordering.** A world `r₂` that takes across step
`π i` the exchange `r` takes across step `i`, touches what it touches, shows what it touches after
the step as `r` does, keeps the order of joined exchanges and starts the stretch as `r` does, is
reached from `r` by commuting exchanges not joined: over the stretch, the reordering takes the
exchanges `r₂` takes, and its web shows every relatum at every step as `r₂`'s does. -/
theorem converse {S m : Nat} {r r₂ : Footprinted X} {π σ : Nat → Nat} (contains : r.Contains)
    (contains₂ : r₂.Contains) (reindex : Reindexes S m π σ) (keeps : r.Keeps S m π)
    (exchanges : ∀ i, S ≤ i → i < S + m → r.flow.SameExchange i r₂.flow (π i))
    (footprints : ∀ i x, S ≤ i → i < S + m → r₂.touch (π i) x = r.touch i x)
    (changes : ∀ i x, S ≤ i → i < S + m → r.touch i x = true →
      r.web.SameAt (i + 1) r₂.web (π i + 1) x)
    (start : ∀ x, r.web.SameAt S r₂.web S x) :
    ∃ ts, EachStep (fun t => S ≤ t ∧ t + 2 ≤ S + m) ts ∧ r.Independent ts ∧
      (∀ i, S ≤ i → i < S + m → place ts i = π i) ∧
      (∀ a, S ≤ a → a < S + m → (r.reorder ts).flow.SameExchange a r₂.flow a) ∧
      ∀ k x, S ≤ k → k ≤ S + m → (r.reorder ts).web.SameAt k r₂.web k x :=
  match sorts m S contains reindex keeps with
  | ⟨ts, within, independent, places⟩ =>
    have came : ∀ a, S ≤ a → a < S + m → origin ts a = σ a := fun a from_ below =>
      have ha := (reindex a from_ below).2
      (congrArg (origin ts) ((places (σ a) ha.1 ha.2.1).trans ha.2.2)).symm.trans
        (origin_place ts (σ a))
    ⟨ts, within, independent, places,
     fun a from_ below =>
       have ha := (reindex a from_ below).2
       Flow.SameExchange.trans
         (Eq.subst (motive := fun k => (r.reorder ts).flow.SameExchange a r.flow k)
           (came a from_ below) (reorder_exchange r ts a).symm)
         (Eq.subst (motive := fun k => r.flow.SameExchange (σ a) r₂.flow k) ha.2.2
           (exchanges (σ a) ha.1 ha.2.1)),
     fun _ x from_ upto => match le_dest from_ with
       | ⟨e, same⟩ => Eq.subst (motive := fun j => (r.reorder ts).web.SameAt j r₂.web j x)
           same.symm (converse_webs contains contains₂ independent within reindex came footprints
             changes start e (le_of_add_le_add_left_core
               (Eq.subst (motive := (· ≤ S + m)) same upto)) x)⟩

/-! ### The order is relative to the footprint -/

/-- A footprint touching more joins more. -/
theorem Joined.mono {r : Footprinted X} {touch : Nat → X → Bool}
    (more : ∀ n x, r.touch n x = true → touch n x = true) {i j : Nat} :
    r.Joined i j → (⟨r.flow, r.web, touch⟩ : Footprinted X).Joined i j
  | .inl ⟨x, a, b⟩ => .inl ⟨x, more i x a, more j x b⟩
  | .inr (.inl ⟨f, c, a, b, rq⟩) => .inr (.inl ⟨f, c, more i f a, more j c b, rq⟩)
  | .inr (.inr ⟨f, c, a, b, rq⟩) => .inr (.inr ⟨f, c, more j f a, more i c b, rq⟩)

/-- And orders more. -/
theorem Precedes.mono {r : Footprinted X} {touch : Nat → X → Bool}
    (more : ∀ n x, r.touch n x = true → touch n x = true) :
    ∀ {i j : Nat}, r.Precedes i j → (⟨r.flow, r.web, touch⟩ : Footprinted X).Precedes i j
  | _, _, .joined lt link => .joined lt (Joined.mono more link)
  | _, _, .trans a b => .trans (Precedes.mono more a) (Precedes.mono more b)

/-- A footprint touching more still contains the exchanges. -/
theorem Contains.mono {r : Footprinted X} {touch : Nat → X → Bool} (contains : r.Contains)
    (more : ∀ n x, r.touch n x = true → touch n x = true) :
    (⟨r.flow, r.web, touch⟩ : Footprinted X).Contains :=
  fun n x untouched => contains n x (match h : r.touch n x with
    | true => Bool.noConfusion ((more n x h).symm.trans untouched)
    | false => rfl)

/-- Every world has a footprint containing its exchanges: every step touching every relatum. -/
theorem contains_everything (L : Flow X X) (W : Web X X) :
    (⟨L, W, fun _ _ => true⟩ : Footprinted X).Contains :=
  fun _ _ untouched => Bool.noConfusion untouched

end Footprinted


/-! ## Removing idle steps -/

namespace Stutter

variable {ρ : Nat → Nat}

/-- The moving step reading a step is one: two steps at which a stuttering moves from `s` to
`s + 1` are the same step. -/
theorem moving_unique (stutter : Stutter ρ) {n n' s : Nat} (here : ρ n = s)
    (next : ρ (n + 1) = s + 1) (here' : ρ n' = s) (next' : ρ (n' + 1) = s + 1) : n = n' :=
  match Nat.lt_or_ge n n' with
  | .inl lt => absurd (Nat.le_trans (Nat.le_of_eq next.symm)
      (Nat.le_trans (mono stutter.2.1 lt) (Nat.le_of_eq here'))) (Nat.not_succ_le_self s)
  | .inr ge => match Nat.lt_or_ge n' n with
    | .inl lt => absurd (Nat.le_trans (Nat.le_of_eq next'.symm)
        (Nat.le_trans (mono stutter.2.1 lt) (Nat.le_of_eq here))) (Nat.not_succ_le_self s)
    | .inr ge' => Nat.le_antisymm ge' ge

/-- `σ` gives, for each step read, the moving step reading it. -/
def Moves (ρ σ : Nat → Nat) : Prop :=
  ∀ s, ρ (σ s) = s ∧ ρ (σ s + 1) = s + 1

variable {σ : Nat → Nat}

/-- A step comes no later than the moving step reading what it reads. -/
theorem le_moving (stutter : Stutter ρ) (moves : Moves ρ σ) (n : Nat) : n ≤ σ (ρ n) :=
  match Nat.lt_or_ge (σ (ρ n)) n with
  | .inl lt => absurd (Nat.le_trans (Nat.le_of_eq (moves (ρ n)).2.symm) (mono stutter.2.1 lt))
      (Nat.not_succ_le_self (ρ n))
  | .inr ge => ge

/-- And every step from it to that moving step is idle. -/
theorem idle_before_moving (stutter : Stutter ρ) (moves : Moves ρ σ) {n k : Nat} (from_ : n ≤ k)
    (below : k < σ (ρ n)) : ρ (k + 1) = ρ k :=
  have top : ρ (k + 1) ≤ ρ n := Nat.le_trans (mono stutter.2.1 below)
    (Nat.le_of_eq (moves (ρ n)).1)
  Nat.le_antisymm (Nat.le_trans top (mono stutter.2.1 from_))
    (le_succ stutter.2.1 k)

/-- Where a stuttering moves, its step is the moving step reading what it reads. -/
theorem moving_eq (stutter : Stutter ρ) (moves : Moves ρ σ) {n : Nat}
    (moved : ρ (n + 1) = ρ n + 1) : σ (ρ n) = n :=
  moving_unique stutter (moves (ρ n)).1 (moves (ρ n)).2 rfl moved

/-- What holds at every idle step and at each moving step holds at every step. -/
theorem every_step (stutter : Stutter ρ) (moves : Moves ρ σ) {P : Nat → Prop}
    (at_idle : ∀ n, ρ (n + 1) = ρ n → P n) (at_moving : ∀ s, P (σ s)) (n : Nat) : P n :=
  match stutter.2.1 n with
  | .inl still => at_idle n still
  | .inr moved => Eq.subst (motive := P) (moving_eq stutter moves moved) (at_moving (ρ n))

end Stutter

/-- A web unmoved at every step of a stretch shows every relatum at its end as at its start. -/
theorem Web.sameAt_of_unmoved {X : Type} {W : Web X X} :
    ∀ (d n : Nat), (∀ k, n ≤ k → k < n + d → ∀ x, W.Unmoved k x) → ∀ x, W.SameAt n W (n + d) x
  | 0, _, _, x => Web.SameAt.refl W _ x
  | d + 1, n, still, x =>
    (Web.sameAt_of_unmoved d n (fun k from_ below => still k from_ (Nat.lt_succ_of_lt below)) x).trans
      (still (n + d) (Nat.le_add_right n d) (Nat.lt_succ_self _) x)

/-- A flow read at the steps `σ`: across step `s` the exchange across step `σ s`. -/
def Flow.readAt {F C : Type} (L : Flow F C) (σ : Nat → Nat) : Flow F C :=
  ⟨fun s => L.present (σ s), fun s => L.take (σ s), fun s => L.give (σ s)⟩

namespace World

/-- The world is idle at the idle steps of a reading: nothing takes part and every relatum is
unmoved. -/
def IdleAt (v : World) (ρ : Nat → Nat) : Prop :=
  ∀ n, ρ (n + 1) = ρ n → v.flow.present n = [] ∧ ∀ x, v.web.Unmoved n x

/-- **The world with its idle steps removed.** Across step `s` the exchange across step `σ s`,
the web read at the times `σ`. Where `σ` gives the moving steps of a stuttering at whose idle
steps the world is idle, this removes them. -/
def withoutIdle (v : World) (σ : Nat → Nat) : World :=
  ⟨v.Relatum, v.flow.readAt σ, v.web.sample σ⟩

section Removal

variable {v : World} {ρ σ : Nat → Nat} (stutter : Stutter ρ) (moves : Stutter.Moves ρ σ)
  (idle : v.IdleAt ρ)
include stutter moves idle

/-- Each step of the world shows every relatum as the step of the world without idle steps it
is read at. -/
theorem withoutIdle_sameAt (n : Nat) (x : v.Relatum) :
    v.web.SameAt n v.web (σ (ρ n)) x :=
  match le_dest (Stutter.le_moving stutter moves n) with
  | ⟨d, same⟩ => Eq.subst (motive := fun k => v.web.SameAt n v.web k x) same.symm
      (Web.sameAt_of_unmoved d n (fun k from_ below => (idle k (Stutter.idle_before_moving
        stutter moves from_ (Nat.lt_of_lt_of_le below (Nat.le_of_eq same.symm)))).2) x)

/-- After a moving step the world shows every relatum as at the next moving step. -/
theorem withoutIdle_after (s : Nat) (x : v.Relatum) : v.web.SameAt (σ s + 1) v.web (σ (s + 1)) x :=
  Eq.subst (motive := fun k => v.web.SameAt (σ s + 1) v.web (σ k) x) (moves s).2
    (withoutIdle_sameAt stutter moves idle (σ s + 1) x)

/-- **Removing idle steps keeps every premise.** The world and the world with its idle steps
removed meet balance, dissipation, only active relata giving, only active relata taking,
activity needing support and embodiment exactly alike. Unlike a reading through a stuttering, no
condition on listing is needed: each step keeps its own exchange. -/
theorem withoutIdle_premises :
    ((v.withoutIdle σ).Balanced ↔ v.Balanced) ∧ ((v.withoutIdle σ).Dissipative ↔ v.Dissipative) ∧
    ((v.withoutIdle σ).Acting ↔ v.Acting) ∧ ((v.withoutIdle σ).Taking ↔ v.Taking) ∧
    ((v.withoutIdle σ).Dependent ↔ v.Dependent) ∧ ((v.withoutIdle σ).Embodied ↔ v.Embodied) :=
  have same := withoutIdle_sameAt stutter moves idle
  have after := withoutIdle_after stutter moves idle
  ⟨⟨fun balanced n c => Stutter.every_step stutter moves
      (P := fun n => ∀ c, v.web.level (n + 1) c + v.flow.taken n c = v.web.level n c + v.flow.given n c)
      (fun n still c => (congrArg (· + v.flow.taken n c) ((idle n still).2 c).1).trans
        (congrArg (v.web.level n c + ·) ((Flow.taken_nil (idle n still).1 c).trans
          (Flow.given_nil (idle n still).1 c).symm)))
      (fun s c => (congrArg (· + v.flow.taken (σ s) c) (after s c).1.symm).trans (balanced s c))
      n c,
    fun balanced s c => (congrArg (· + v.flow.taken (σ s) c) (after s c).1).trans (balanced (σ s) c)⟩,
   ⟨fun dissipative cs => Stutter.every_step stutter moves
      (P := fun n => Distinct cs → v.flow.ClosedAt cs n → v.flow.DissipatesOn cs n)
      (fun n still _ _ f mem => absurd (Eq.subst (motive := fun l => f ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s => dissipative cs s),
    fun dissipative cs s => dissipative cs (σ s)⟩,
   ⟨fun acting => Stutter.every_step stutter moves
      (P := fun n => ∀ f c, f ∈ v.flow.present n → 0 < v.flow.give n f c → v.web.active n f)
      (fun n still f _ mem _ => absurd (Eq.subst (motive := fun l => f ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s => acting s),
    fun acting s => acting (σ s)⟩,
   ⟨fun taking => Stutter.every_step stutter moves
      (P := fun n => ∀ f c, f ∈ v.flow.present n → 0 < v.flow.take n f c →
        v.web.active n f ∧ v.web.draws n f c)
      (fun n still f _ mem _ => absurd (Eq.subst (motive := fun l => f ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s => taking s),
    fun taking s => taking (σ s)⟩,
   ⟨fun dependent n f active c requires =>
      have sf := same n f
      Nat.le_trans (Nat.le_of_eq (sf.2.2 c).2.1.symm)
        (Nat.le_trans (dependent (ρ n) f (cast sf.2.1.symm active) c
            (cast (sf.2.2 c).1.symm requires))
          (Nat.le_of_eq (same n c).1)),
    Web.sample_dependent σ⟩,
   ⟨fun embodied x n => (Iff.of_eq (same n x).2.1).symm.trans ((embodied x (ρ n)).trans
      (Iff.of_eq (congrArg (0 < ·) (same n x).1))),
    fun embodied x => Web.sample_embodied σ (embodied x)⟩⟩

/-- And bounded transmission, with the same bound. -/
theorem withoutIdle_transmits {c : v.Relatum} {δ : Nat} :
    (v.withoutIdle σ).flow.TransmitsWithin (v.withoutIdle σ).web c δ ↔
      v.flow.TransmitsWithin v.web c δ :=
  have after := withoutIdle_after stutter moves idle
  ⟨fun transmits => Stutter.every_step stutter moves
      (P := fun n => ∀ x g, v.flow.DescendsAt v.web n x g → v.web.requires (n + 1) x c →
        v.web.requires n g c ∧ v.web.need (n + 1) x c ≤ v.web.need n g c + δ)
      (fun n still _ g ⟨mem, _, _⟩ => absurd (Eq.subst (motive := fun l => g ∈ l) (idle n still).1 mem)
        fun no => nomatch no)
      (fun s x g ⟨mem, gives, absent, stands⟩ requires =>
        have inherited := transmits s x g
          ⟨mem, gives, absent, Eq.subst (motive := (0 < ·)) (after s x).1.symm stands⟩
          (cast ((after s x).2.2 c).1.symm requires)
        ⟨inherited.1, Nat.le_trans (Nat.le_of_eq ((after s x).2.2 c).2.1.symm) inherited.2⟩),
   fun transmits s x g ⟨mem, gives, absent, stands⟩ requires =>
     have inherited := transmits (σ s) x g
       ⟨mem, gives, absent, Eq.subst (motive := (0 < ·)) (after s x).1 stands⟩
       (cast ((after s x).2.2 c).1 requires)
     ⟨inherited.1, Nat.le_trans (Nat.le_of_eq ((after s x).2.2 c).2.1) inherited.2⟩⟩

/-- And a census: the relata active at each step of the world are those active at the step it is
read at. -/
theorem withoutIdle_counted : (v.withoutIdle σ).Counted ↔ v.Counted :=
  ⟨fun ⟨alive, census⟩ => ⟨fun n => alive (ρ n), fun n => ⟨(census (ρ n)).1, fun x =>
      (Iff.of_eq (withoutIdle_sameAt stutter moves idle n x).2.1).symm.trans ((census (ρ n)).2 x)⟩⟩,
   fun ⟨alive, census⟩ => ⟨fun s => alive (σ s), fun s => census (σ s)⟩⟩

/-- **And the totals.** Over any stretch, what is taken from and given to a condition, the rises
and falls of a family's total standing and the steps at which it rises and falls are those of the
stretch of the world without idle steps it reads. -/
theorem withoutIdle_totals (cs : List v.Relatum) (c : v.Relatum) (N m d : Nat)
    (reads : ρ N + d = ρ (N + m)) :
    total (steps N m) (fun n => v.flow.taken n c) =
      total (steps (ρ N) d) (fun s => (v.withoutIdle σ).flow.taken s c) ∧
    total (steps N m) (fun n => v.flow.given n c) =
      total (steps (ρ N) d) (fun s => (v.withoutIdle σ).flow.given s c) ∧
    total (steps N m) (rise (v.web.stock cs)) =
      total (steps (ρ N) d) (rise ((v.withoutIdle σ).web.stock cs)) ∧
    total (steps N m) (fall (v.web.stock cs)) =
      total (steps (ρ N) d) (fall ((v.withoutIdle σ).web.stock cs)) ∧
    count (steps N m) (rise (v.web.stock cs)) =
      count (steps (ρ N) d) (rise ((v.withoutIdle σ).web.stock cs)) ∧
    count (steps N m) (fall (v.web.stock cs)) =
      count (steps (ρ N) d) (fall ((v.withoutIdle σ).web.stock cs)) :=
  have here : ∀ n, ρ (n + 1) = ρ n + 1 → σ (ρ n) = n := fun _ moved =>
    Stutter.moving_eq stutter moves moved
  have stock : ∀ n, v.web.stock cs n = (v.withoutIdle σ).web.stock cs (ρ n) := fun n =>
    total_congr_on fun c _ => (withoutIdle_sameAt stutter moves idle n c).1.symm
  have rises : ∀ n, rise (v.web.stock cs) n =
      rise (fun k => (v.withoutIdle σ).web.stock cs (ρ k)) n := fun n =>
    (congr (congrArg excess (stock (n + 1))) (stock n) :)
  have falls : ∀ n, fall (v.web.stock cs) n =
      fall (fun k => (v.withoutIdle σ).web.stock cs (ρ k)) n := fun n =>
    (congr (congrArg excess (stock n)) (stock (n + 1)) :)
  ⟨stutter_total stutter.2.1 (fun n still => Flow.taken_nil (idle n still).1 c)
     (fun n moved => congrArg (fun k => v.flow.taken k c) (here n moved).symm) N m d reads,
   stutter_total stutter.2.1 (fun n still => Flow.given_nil (idle n still).1 c)
     (fun n moved => congrArg (fun k => v.flow.given k c) (here n moved).symm) N m d reads,
   (total_congr rises (steps N m)).trans (stutter_risen stutter.2.1 _ N m d reads),
   (total_congr falls (steps N m)).trans (stutter_fallen stutter.2.1 _ N m d reads),
   (total_congr (fun n => congrArg sign (rises n)) (steps N m)).trans
     (stutter_rise_count stutter.2.1 _ N m d reads),
   (total_congr (fun n => congrArg sign (falls n)) (steps N m)).trans
     (stutter_fall_count stutter.2.1 _ N m d reads)⟩

/-- And the relata of a finite family arising and ceasing, with activity decided. -/
theorem withoutIdle_counts [decided : ∀ n x, Decidable (v.web.active n x)] (xs : List v.Relatum)
    (N m d : Nat) (reads : ρ N + d = ρ (N + m)) :
    haveI : ∀ s x, Decidable ((v.withoutIdle σ).web.active s x) := fun s x => decided (σ s) x
    total (steps N m) (comings xs fun x n => v.web.active n x) =
      total (steps (ρ N) d) (comings xs fun x s => (v.withoutIdle σ).web.active s x) ∧
    total (steps N m) (ceasings xs fun x n => v.web.active n x) =
      total (steps (ρ N) d) (ceasings xs fun x s => (v.withoutIdle σ).web.active s x) :=
  letI : ∀ s x, Decidable ((v.withoutIdle σ).web.active s x) := fun s x => decided (σ s) x
  have alike : ∀ x n, v.web.active n x ↔ (v.withoutIdle σ).web.active (ρ n) x := fun x n =>
    (Iff.of_eq (withoutIdle_sameAt stutter moves idle n x).2.1).symm
  ⟨(total_congr (fun n => comings_of_iff alike n) (steps N m)).trans
     (stutter_comings (as := xs) (p := fun x s => (v.withoutIdle σ).web.active s x) stutter.2.1
       N m d reads),
   (total_congr (fun n => ceasings_of_iff alike n) (steps N m)).trans
     (stutter_ceasings (as := xs) (p := fun x s => (v.withoutIdle σ).web.active s x) stutter.2.1
       N m d reads)⟩

end Removal

end World

end Becoming
