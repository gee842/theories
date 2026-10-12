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

Reading (the AI's, pending Ren): for the laws of one step, the totals and counts over a stretch,
and recurrence, the step index carries nothing beyond the order of change; an idle step
registers nothing. What is counted per step, rates and how long a reserve carries, is relative
to the unit of the reading, as coarser steps were (`Becoming.Sampling`). Within the order, what
registers is the order of exchanges joined through a relatum or a dependence; exchanges joined by
neither may be taken in either order. The order the laws need would then be a partial order of
exchanges, not a sequence of steps; the converse that would make this exact is not shown (below).

Not shown: removing idle steps as a construction (only through the equivalences above, and a
census given a section); the converse, that any two sequences of the same exchanges with the same
order of dependence are related by `Reorders` (Foata normal form), and the partial order itself as
an object; activity needing support, only active relata giving, and the counts of arising and
ceasing along repeated commutation; invariance of the predicates of Part II; continuous time.
Commutation is of consecutive steps, each standing and activity changing across one of them; the
sides are given, not derived. No ethical predicate, ranking or axiom occurs.
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

end Becoming
