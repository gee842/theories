import Becoming.Openness

/-!
# Resolution: what the unit of amounts carries

The spine counts amounts in natural numbers of one fixed unit. Read in that unit,
dissipation says that a formation taking from a closed family gives back at least one unit
less than it takes. So every exchange loses at least one unit, and the rest and openness
laws count those losses against the standing. This module separates what of those laws
belongs to the dynamics from what belongs to the fixed unit.

* **A unit that may refine.** Across the step from `t` the unit may split into `r t`
  finer units (`Flow.BalancesAt r`): the level before the step, counted in the finer
  unit, is `r t` times its count in the coarser one. With `r` constantly one this is
  `Balances` (`Flow.balancesAt_one`).
* **The loss law.** Whatever the refinement, where across each step from `T` on `q` times
  what remains together with `k` quanta of the unit of step `T` is within `q` times what
  was there, the quanta counted since `T` number at most `q` times the quantity at `T`
  (`losses_bound`). So the steps at which a family closed from `T` on loses at least `1/q`
  of the unit of step `T` number at most `q` times its stock at `T` (`Flow.quantum_bound`),
  and losing a quantum does not recur (`Flow.quantum_not_recurring`).
* **A fixed unit.** Where the unit is fixed from some step on, every taking step loses a
  whole unit, so taking from a closed family stops (`Flow.taking_stops`); with `r`
  constantly one this is the spine's `Flow.Balances.taking_ceases`.
* **Loss in proportion.** Where every formation gives a closed family at most `q` parts in
  `q + 1` of what it takes from it (`Flow.DissipativeBy q`), the share lost does not
  depend on the unit. Then, at every resolution that only refines:
  - the times a formation takes at least `1/p` of the unit from a closed family number at
    most `p (q + 1)` times the family's stock (the exchange law, `Flow.exchange_bound`), so
    such taking does not recur (`Flow.exchange_not_recurring`);
  - in a world with a census, embodied relata and every step from `T` on enclosed, the
    times a relatum gains at least `1/p` of the unit number at most `p q` times the total
    standing at `T` (the growth law, `World.growth_bound`), so such gains do not recur
    (`World.growth_not_recurring`) and nothing arises at that size at arbitrarily late
    steps (`World.arising_not_recurring`).
* **The frontier.** Each witness is balanced at a unit that splits without end, and its
  flow dissipates on every closed family.
  - In `Asymptote` a drawer takes from a closed pool without end and gives nothing back,
    so it is dissipative by every share; what it takes shrinks below every quantum
    (`rest_needs_quantum`).
  - In `Circulation` a drawer takes one whole unit of step 0 from a pool at every step,
    losing one unit of the step after; for no share is it dissipative in proportion
    (`exchange_needs_quantum`).
  - In `Emission` a pool gives back at most half of what it takes, every step is
    enclosed, and a new relatum arises at every step, standing at one unit of the step
    after, below every quantum (`arising_needs_quantum`).
  - In `Alternation` two sides hand one whole unit of step 0 back and forth inside an
    enclosure, each arising in turn; for no share is it dissipative in proportion
    (`arising_needs_proportion`).

So the rest of enclosed change is carried either by a least loss per exchange in a fixed
unit, as in the spine, or, at every resolution, by loss in proportion together with a
least size of what is exchanged or arises. Without the least size, change continues at
sizes shrinking without bound. Without the proportion, change of a whole unit continues
while its losses shrink without bound. What holds at every resolution without either is
the quantum law: an enclosed family cannot keep losing at a non-vanishing rate.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

/-! ## Products, regrouped without `propext` -/

theorem mul_regroup (a b : Nat) : ∀ c, a * b * c = a * (b * c)
  | 0 => rfl
  | c + 1 => (congrArg (· + a * b) (mul_regroup a b c)).trans (Nat.left_distrib a (b * c) b).symm

theorem mul_turn (a b c : Nat) : a * (b * c) = b * (a * c) :=
  (mul_regroup a b c).symm.trans ((congrArg (· * c) (Nat.mul_comm a b)).trans (mul_regroup b a c))

theorem add_mul_split (a b : Nat) : ∀ c, (a + b) * c = a * c + b * c
  | 0 => rfl
  | c + 1 => (congrArg (· + (a + b)) (add_mul_split a b c)).trans (Nat.add_add_add_comm _ _ _ _)

/-! ## A unit that may refine -/

namespace Flow

variable (L : Flow F C)

/-- The flow balances at resolution `r`: across the step from `t` the unit splits into
`r t` finer units, and the level before the step, counted in the finer unit, is `r t`
times its count in the coarser one. -/
def BalancesAt (r : Nat → Nat) (W : Web F C) : Prop :=
  ∀ t c, W.level (t + 1) c + L.taken t c = r t * W.level t c + L.given t c

variable {L} {W : Web F C}

/-- With a fixed unit, balance at resolution is the spine's balance. -/
theorem balancesAt_one : L.BalancesAt (fun _ => 1) W ↔ L.Balances W :=
  ⟨fun balances t c => (balances t c).trans (congrArg (· + L.given t c) (Nat.one_mul _)),
   fun balances t c => (balances t c).trans (congrArg (· + L.given t c) (Nat.one_mul _)).symm⟩

/-- Over a family, the stock after the step with its uptake is `r t` times the stock
before with its replenishment. -/
theorem BalancesAt.over {r : Nat → Nat} (balances : L.BalancesAt r W) :
    ∀ (cs : List C) (t : Nat),
      W.stock cs (t + 1) + L.uptake cs t = r t * W.stock cs t + L.replenishment cs t
  | [], _ => rfl
  | c :: cs, t =>
    (Nat.add_add_add_comm (W.level (t + 1) c) (W.stock cs (t + 1)) (L.taken t c)
      (L.uptake cs t)).trans
    ((congrArg (· + (W.stock cs (t + 1) + L.uptake cs t)) (balances t c)).trans
    ((congrArg (r t * W.level t c + L.given t c + ·) (balances.over cs t)).trans
    ((Nat.add_add_add_comm (r t * W.level t c) (L.given t c) (r t * W.stock cs t)
      (L.replenishment cs t)).trans
     (congrArg (· + (L.given t c + L.replenishment cs t))
       (Nat.left_distrib (r t) (W.level t c) (W.stock cs t)).symm))))

/-- Dissipated on, the family's stock after the step with its takers is at most `r t`
times its stock before. -/
theorem BalancesAt.lowers {r : Nat → Nat} (balances : L.BalancesAt r W) {cs : List C}
    {t : Nat} (dissipates : L.DissipatesOn cs t) :
    W.stock cs (t + 1) + L.takers cs t ≤ r t * W.stock cs t :=
  le_of_add_le_add_right (L.replenishment cs t) (Nat.le_trans
    (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
      (congrArg (W.stock cs (t + 1) + ·) (Nat.add_comm (L.takers cs t) (L.replenishment cs t)))))
    (Nat.le_trans (Nat.add_le_add_left dissipates.replenishment_takers _)
      (Nat.le_of_eq (balances.over cs t))))

end Flow

/-! ## The loss law -/

/-- Counted in a unit splitting into `r t` finer units across the step from `t`, a quantity
`s` loses across the step at least `1/q` of the unit in which `R` counts: in the unit of
step `t + 1`, `q` times the loss is at least `R (t + 1)`. -/
def LosesQuantum (r R s : Nat → Nat) (q t : Nat) : Prop :=
  R (t + 1) + q * s (t + 1) ≤ q * (r t * s t)

instance (r R s : Nat → Nat) (q t : Nat) : Decidable (LosesQuantum r R s q t) :=
  Nat.decLe _ _

/-- Units of each step from `T` on are positive where the unit only splits. -/
theorem units_pos {r R : Nat → Nat} {T : Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t) :
    ∀ {t}, T ≤ t → 0 < R t
  | _, .refl => Nat.lt_of_lt_of_le (Nat.succ_pos 0) (Nat.le_of_eq base.symm)
  | m + 1, .step later => Nat.le_trans
      (Nat.mul_le_mul (refining m later) (units_pos base unit refining later) :
        1 * 1 ≤ r m * R m)
      (Nat.le_of_eq (unit m later).symm)

/-- The invariant of the loss law. Counted in the unit of step `T`, with `R` counting
units of each later step per unit of step `T`: where across each step from `T` on, `q`
times what remains together with `k` quanta is within `q` times the quantity before, `q`
times what remains together with every quantum counted since `T` is within `q` times the
quantity at `T`. -/
theorem losses_invariant {r R s k : Nat → Nat} {q T : Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t)
    (step : ∀ t, T ≤ t → q * s (t + 1) + k t * R (t + 1) ≤ q * (r t * s t)) :
    ∀ n, q * s (T + n) + total (steps T n) k * R (T + n) ≤ q * s T * R (T + n)
  | 0 => Nat.le_of_eq ((congrArg (q * s T + ·) (Nat.zero_mul _)).trans
      ((Nat.add_zero _).trans ((Nat.mul_one _).symm.trans (congrArg (q * s T * ·) base.symm))))
  | n + 1 =>
    have before := losses_invariant base unit step n
    have later : T ≤ T + n := Nat.le_add_right T n
    calc q * s (T + n + 1) + total (steps T (n + 1)) k * R (T + n + 1)
        = q * s (T + n + 1) + k (T + n) * R (T + n + 1) +
            total (steps T n) k * R (T + n + 1) :=
          (congrArg (q * s (T + n + 1) + ·) ((congrArg (· * R (T + n + 1))
            (steps_last k T n)).trans ((add_mul_split _ _ _).trans (Nat.add_comm _ _)))).trans
            (Nat.add_assoc _ _ _).symm
      _ ≤ q * (r (T + n) * s (T + n)) + total (steps T n) k * R (T + n + 1) :=
          Nat.add_le_add_right (step (T + n) later) _
      _ = r (T + n) * (q * s (T + n) + total (steps T n) k * R (T + n)) :=
          (congrArg (q * (r (T + n) * s (T + n)) + ·) ((congrArg (total (steps T n) k * ·)
            (unit (T + n) later)).trans (mul_turn _ _ _))).trans
          ((congrArg (· + r (T + n) * (total (steps T n) k * R (T + n))) (mul_turn _ _ _)).trans
            (Nat.left_distrib _ _ _).symm)
      _ ≤ r (T + n) * (q * s T * R (T + n)) := Nat.mul_le_mul_left _ before
      _ = q * s T * R (T + n + 1) :=
          (mul_turn _ _ _).trans (congrArg (q * s T * ·) (unit (T + n) later).symm)

/-- The loss law: the quanta counted since `T` number at most `q` times the quantity at
`T`, whatever the refinement. -/
theorem losses_bound {r R s k : Nat → Nat} {q T : Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (step : ∀ t, T ≤ t → q * s (t + 1) + k t * R (t + 1) ≤ q * (r t * s t)) (n : Nat) :
    total (steps T n) k ≤ q * s T :=
  Nat.le_of_mul_le_mul_right
    (Nat.le_trans (Nat.le_add_left _ _) (losses_invariant base unit step n))
    (units_pos base unit refining (Nat.le_add_right T n))

/-- A count positive at arbitrarily late steps has totals over the steps from `T` beyond
every bound. -/
theorem unbounded_of_recurring {k : Nat → Nat} {T : Nat}
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < k t) : ∀ m, ∃ n, m ≤ total (steps T n) k
  | 0 => ⟨0, Nat.zero_le _⟩
  | m + 1 => match unbounded_of_recurring recurs m with
    | ⟨n, many⟩ => match recurs (T + n) with
      | ⟨_, after, positive⟩ => match Nat.le.dest after with
        | ⟨j, same⟩ => ⟨n + j + 1, Nat.le_trans (Nat.add_le_add many positive)
            (Nat.le_trans (Nat.add_le_add_right (steps_mono k T n j) _)
              (Nat.le_of_eq ((congrArg (fun u => total (steps T (n + j)) k + k u)
                ((Nat.add_assoc T n j).symm.trans same).symm).trans
                (steps_last k T (n + j)).symm)))⟩

/-- So a count whose totals over the steps from `T` stay within a bound is positive at
only finitely many steps. -/
theorem bounded_not_recurring {k : Nat → Nat} {T B : Nat}
    (bounded : ∀ n, total (steps T n) k ≤ B) : ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < k t :=
  fun recurs => match unbounded_of_recurring (T := T) recurs (B + 1) with
  | ⟨n, many⟩ => Nat.lt_irrefl B (Nat.lt_of_lt_of_le many (bounded n))

/-- Across one step: what remains, with one quantum for a step that lost one, is within
the quantity before the step, counted in the finer unit. -/
theorem quantum_step {r R s : Nat → Nat} {q t : Nat} (nonrising : s (t + 1) ≤ r t * s t) :
    q * s (t + 1) + mark (LosesQuantum r R s q t) * R (t + 1) ≤ q * (r t * s t) :=
  mark_cases (q := fun k => q * s (t + 1) + k * R (t + 1) ≤ q * (r t * s t))
    (fun loses => Nat.le_trans (Nat.le_of_eq ((congrArg (q * s (t + 1) + ·)
      (Nat.one_mul _)).trans (Nat.add_comm _ _))) loses)
    (fun _ => Nat.le_trans (Nat.le_of_eq ((congrArg (q * s (t + 1) + ·)
      (Nat.zero_mul _)).trans (Nat.add_zero _))) (Nat.mul_le_mul_left q nonrising))

/-- The quantum law: the steps since `T` at which a quantity that never rises in the finer
unit loses at least `1/q` of the unit of step `T` number at most `q` times the quantity at
`T`. -/
theorem quantum_bound {r R s : Nat → Nat} {q T : Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (nonrising : ∀ t, T ≤ t → s (t + 1) ≤ r t * s t) (n : Nat) :
    total (steps T n) (fun u => mark (LosesQuantum r R s q u)) ≤ q * s T :=
  losses_bound base unit refining (fun t later => quantum_step (nonrising t later)) n

/-- So losing a quantum does not recur. -/
theorem quantum_not_recurring {r R s : Nat → Nat} {q T : Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (nonrising : ∀ t, T ≤ t → s (t + 1) ≤ r t * s t) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ LosesQuantum r R s q t :=
  fun recurs => bounded_not_recurring (quantum_bound base unit refining nonrising)
    fun N => match recurs N with
    | ⟨t, after, loses⟩ => ⟨t, after, mark_pos.mpr loses⟩

/-! ## The quantum law on flows -/

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- The quantum law on a flow. Balanced at resolution `r` and dissipative, over a family
without repetition closed at every step from `T` on, the steps since `T` at which the
family loses at least `1/q` of the unit of step `T` number at most `q` times its stock at
`T`. -/
theorem quantum_bound {r R : Nat → Nat} (balances : L.BalancesAt r W)
    (dissipative : L.Dissipative) {cs : List C} (distinct : Distinct cs) {T : Nat}
    (closed : ∀ t, T ≤ t → L.ClosedAt cs t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (q n : Nat) :
    total (steps T n) (fun u => mark (LosesQuantum r R (W.stock cs) q u)) ≤ q * W.stock cs T :=
  Becoming.quantum_bound base unit refining (fun u after => Nat.le_trans (Nat.le_add_right _ _)
    (balances.lowers (dissipative cs u distinct (closed u after)))) n

/-- So a closed family's losing a quantum does not recur. -/
theorem quantum_not_recurring {r R : Nat → Nat} (balances : L.BalancesAt r W)
    (dissipative : L.Dissipative) {cs : List C} (distinct : Distinct cs) {T : Nat}
    (closed : ∀ t, T ≤ t → L.ClosedAt cs t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (q : Nat) : ¬ ∀ N, ∃ t, N ≤ t ∧ LosesQuantum r R (W.stock cs) q t :=
  Becoming.quantum_not_recurring base unit refining (fun u after =>
    Nat.le_trans (Nat.le_add_right _ _)
      (balances.lowers (dissipative cs u distinct (closed u after))))

/-- Dissipated on, a step at which some formation takes from the family loses at least one
unit of the step after it. -/
theorem takes_loses {r : Nat → Nat} (balances : L.BalancesAt r W) {cs : List C} {t : Nat}
    (dissipates : L.DissipatesOn cs t) (takes : 0 < L.takers cs t) :
    LosesQuantum r (fun _ => 1) (W.stock cs) 1 t :=
  Nat.le_trans (Nat.le_of_eq ((Nat.add_comm _ _).trans (congrArg (· + 1) (Nat.one_mul _))))
    (Nat.le_trans (Nat.add_le_add_left takes _)
      (Nat.le_trans (balances.lowers dissipates) (Nat.le_of_eq (Nat.one_mul _).symm)))

/-- With the unit fixed from some step on, taking from a closed family stops. -/
theorem taking_stops {r : Nat → Nat} (balances : L.BalancesAt r W)
    (dissipative : L.Dissipative) {cs : List C} (distinct : Distinct cs) {T : Nat}
    (closed : ∀ t, T ≤ t → L.ClosedAt cs t) (fixed : ∀ t, T ≤ t → r t = 1) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  fun recurs => quantum_not_recurring balances dissipative distinct closed (R := fun _ => 1) rfl
    (fun t later => ((Nat.mul_one _).trans (fixed t later)).symm)
    (fun t later => Nat.lt_of_lt_of_le (Nat.succ_pos 0) (Nat.le_of_eq (fixed t later).symm)) 1
    fun N => match recurs (N + T) with
      | ⟨t, after, takes⟩ =>
        ⟨t, Nat.le_trans (Nat.le_add_right N T) after,
         takes_loses balances (dissipative cs t distinct (closed t
           (Nat.le_trans (Nat.le_add_left T N) after))) takes⟩

end Flow

/-! ## Loss in proportion to what is taken -/

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- Across the step from `t`, every formation taking part gives the family at most `q`
parts in `q + 1` of what it takes from it: it loses at least a `(q + 1)`th of what it
takes, whatever the unit. -/
def DissipatesBy (q : Nat) (cs : List C) (t : Nat) : Prop :=
  ∀ f, f ∈ L.present t → (q + 1) * total cs (L.give t f) ≤ q * total cs (L.take t f)

/-- Dissipation in proportion: across every step, every family without repetition closed
across it is dissipated on by the share `q`. -/
def DissipativeBy (q : Nat) : Prop :=
  ∀ cs t, Distinct cs → L.ClosedAt cs t → L.DissipatesBy q cs t

/-- Summed over the formations taking part: `q + 1` times the family's replenishment is
within `q` times its uptake. -/
theorem DissipatesBy.over {q : Nat} {cs : List C} {t : Nat}
    (dissipates : L.DissipatesBy q cs t) :
    (q + 1) * L.replenishment cs t ≤ q * L.uptake cs t :=
  calc (q + 1) * L.replenishment cs t
      = total (L.present t) (fun f => (q + 1) * total cs (L.give t f)) :=
        (congrArg ((q + 1) * ·) (total_swap (fun f c => L.give t f c) cs (L.present t)).symm).trans
          (total_mul (q + 1) (fun f => total cs (L.give t f)) (L.present t)).symm
    _ ≤ total (L.present t) (fun f => q * total cs (L.take t f)) :=
        total_le (L.present t) dissipates
    _ = q * L.uptake cs t :=
        (total_mul q (fun f => total cs (L.take t f)) (L.present t)).trans
          (congrArg (q * ·) (total_swap (fun f c => L.take t f c) cs (L.present t)))

/-- So the family's replenishment is within its uptake. -/
theorem DissipatesBy.replenishment_le {q : Nat} {cs : List C} {t : Nat}
    (dissipates : L.DissipatesBy q cs t) : L.replenishment cs t ≤ L.uptake cs t :=
  Nat.le_of_mul_le_mul_left
    (Nat.le_trans dissipates.over (Nat.mul_le_mul_right _ (Nat.le_succ q))) (Nat.succ_pos q)

/-- Dissipated on by the share `q`, the family's stock never rises, counted in the finer
unit. -/
theorem BalancesAt.nonrisingBy {r : Nat → Nat} (balances : L.BalancesAt r W) {q : Nat}
    {cs : List C} {t : Nat} (dissipates : L.DissipatesBy q cs t) :
    W.stock cs (t + 1) ≤ r t * W.stock cs t :=
  le_of_add_le_add_right (L.replenishment cs t)
    (Nat.le_trans (Nat.add_le_add_left dissipates.replenishment_le _)
      (Nat.le_of_eq (balances.over cs t)))

/-- Dissipated on by the share `q`, `q` times the family's stock after the step, together
with its replenishment, is within `q` times its stock before, counted in the finer unit. -/
theorem BalancesAt.lowersBy {r : Nat → Nat} (balances : L.BalancesAt r W) {q : Nat}
    {cs : List C} {t : Nat} (dissipates : L.DissipatesBy q cs t) :
    q * W.stock cs (t + 1) + L.replenishment cs t ≤ q * (r t * W.stock cs t) :=
  le_of_add_le_add_right (q * L.replenishment cs t) (calc
    q * W.stock cs (t + 1) + L.replenishment cs t + q * L.replenishment cs t
        = q * W.stock cs (t + 1) + (q + 1) * L.replenishment cs t :=
          (Nat.add_assoc _ _ _).trans (congrArg (q * W.stock cs (t + 1) + ·)
            ((Nat.add_comm _ _).trans ((congrArg (q * L.replenishment cs t + ·)
              (Nat.one_mul _).symm).trans (add_mul_split q 1 _).symm)))
    _ ≤ q * W.stock cs (t + 1) + q * L.uptake cs t := Nat.add_le_add_left dissipates.over _
    _ = q * (r t * W.stock cs t) + q * L.replenishment cs t :=
          (Nat.left_distrib _ _ _).symm.trans ((congrArg (q * ·) (balances.over cs t)).trans
            (Nat.left_distrib _ _ _)))

end Flow

/-- Across the step from `t`, `c` gains at least `1/p` of the unit counted by `R`: counted
in the unit of step `t + 1`, `p` times its gain is at least `R (t + 1)`. -/
def Web.Gains (W : Web F C) (r R : Nat → Nat) (p t : Nat) (c : C) : Prop :=
  R (t + 1) + p * (r t * W.level t c) ≤ p * W.level (t + 1) c

instance (W : Web F C) (r R : Nat → Nat) (p t : Nat) (c : C) : Decidable (W.Gains r R p t c) :=
  Nat.decLe _ _

/-- The members of a list gaining at least `1/p` of the unit across the step from `t`. -/
def Web.gainers (W : Web F C) (r R : Nat → Nat) (p t : Nat) (gs : List C) : Nat :=
  total gs fun c => mark (W.Gains r R p t c)

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- Balanced at a resolution, what a condition gains across a step is given to it. -/
theorem BalancesAt.gain_given {r : Nat → Nat} (balances : L.BalancesAt r W) {R : Nat → Nat}
    {p t : Nat} {c : C} (gains : W.Gains r R p t c) : R (t + 1) ≤ p * L.given t c :=
  le_of_add_le_add_right (p * (r t * W.level t c)) (Nat.le_trans gains
    (Nat.le_trans (Nat.mul_le_mul_left p (Nat.le_trans (Nat.le_add_right _ (L.taken t c))
        (Nat.le_of_eq (balances t c))))
      (Nat.le_of_eq ((Nat.left_distrib _ _ _).trans (Nat.add_comm _ _)))))

/-- A total scaled after summing is the total of the scaled terms. -/
theorem total_mul_right {α : Type} (q : α → Nat) (g : Nat) (as : List α) :
    total as q * g = total as fun a => q a * g :=
  (Nat.mul_comm _ _).trans ((total_mul g q as).symm.trans
    (total_congr (fun a => Nat.mul_comm g (q a)) as))

/-- Dissipated on by the share `q`, the members of a list without repetition within the
family that gain at least `1/p` of the unit across a step make the family lose at least
`1/(p q)` of it each: `p q` times the stock after the step, together with one unit of
`R` for each of them, is within `p q` times the stock before. -/
theorem BalancesAt.gainers_lose {r : Nat → Nat} (balances : L.BalancesAt r W) {R : Nat → Nat}
    {p q : Nat} {cs gs : List C} {t : Nat} (dissipates : L.DissipatesBy q cs t)
    (distinct : Distinct gs) (within : ∀ c, c ∈ gs → c ∈ cs) :
    p * q * W.stock cs (t + 1) + W.gainers r R p t gs * R (t + 1) ≤
      p * q * (r t * W.stock cs t) :=
  calc p * q * W.stock cs (t + 1) + W.gainers r R p t gs * R (t + 1)
      ≤ p * q * W.stock cs (t + 1) + p * L.replenishment cs t :=
        Nat.add_le_add_left (Nat.le_trans (Nat.le_of_eq (total_mul_right _ _ gs))
          (Nat.le_trans (total_le gs fun c _ => mark_cases
              (q := fun m => m * R (t + 1) ≤ p * L.given t c)
              (fun gains => Nat.le_trans (Nat.le_of_eq (Nat.one_mul _))
                (balances.gain_given gains))
              (fun _ => Nat.le_trans (Nat.le_of_eq (Nat.zero_mul _)) (Nat.zero_le _)))
            (Nat.le_trans (Nat.le_of_eq (total_mul p (L.given t) gs))
              (Nat.mul_le_mul_left p (total_le_of_support distinct fun c mem _ =>
                within c mem))))) _
    _ = p * (q * W.stock cs (t + 1) + L.replenishment cs t) :=
        (congrArg (· + p * L.replenishment cs t) (mul_regroup p q _)).trans
          (Nat.left_distrib _ _ _).symm
    _ ≤ p * (q * (r t * W.stock cs t)) := Nat.mul_le_mul_left p (balances.lowersBy dissipates)
    _ = p * q * (r t * W.stock cs t) := (mul_regroup p q _).symm

/-- Dissipated on by the share `q`, `q + 1` times the family's stock after the step,
together with its uptake, is within `q + 1` times its stock before, counted in the finer
unit. -/
theorem BalancesAt.lowersTaking {r : Nat → Nat} (balances : L.BalancesAt r W) {q : Nat}
    {cs : List C} {t : Nat} (dissipates : L.DissipatesBy q cs t) :
    (q + 1) * W.stock cs (t + 1) + L.uptake cs t ≤ (q + 1) * (r t * W.stock cs t) :=
  le_of_add_le_add_right (q * L.uptake cs t) (calc
    (q + 1) * W.stock cs (t + 1) + L.uptake cs t + q * L.uptake cs t
        = (q + 1) * (W.stock cs (t + 1) + L.uptake cs t) :=
          (Nat.add_assoc _ _ _).trans ((congrArg ((q + 1) * W.stock cs (t + 1) + ·)
            ((Nat.add_comm _ _).trans ((congrArg (q * L.uptake cs t + ·)
              (Nat.one_mul _).symm).trans (add_mul_split q 1 _).symm))).trans
            (Nat.left_distrib _ _ _).symm)
    _ = (q + 1) * (r t * W.stock cs t) + (q + 1) * L.replenishment cs t :=
          (congrArg ((q + 1) * ·) (balances.over cs t)).trans (Nat.left_distrib _ _ _)
    _ ≤ (q + 1) * (r t * W.stock cs t) + q * L.uptake cs t :=
          Nat.add_le_add_left dissipates.over _)

/-- The formations taking part that take at least `1/p` of the unit counted by `R` from
the family across the step from `t`. -/
def takersAbove (R : Nat → Nat) (p : Nat) (cs : List C) (t : Nat) : Nat :=
  total (L.present t) fun f => mark (R (t + 1) ≤ p * total cs (L.take t f))

/-- Dissipated on by the share `q`, each formation taking at least `1/p` of the unit from
the family makes it lose at least `1/(p (q + 1))` of the unit. -/
theorem BalancesAt.takers_lose {r : Nat → Nat} (balances : L.BalancesAt r W) {R : Nat → Nat}
    {p q : Nat} {cs : List C} {t : Nat} (dissipates : L.DissipatesBy q cs t) :
    p * (q + 1) * W.stock cs (t + 1) + L.takersAbove R p cs t * R (t + 1) ≤
      p * (q + 1) * (r t * W.stock cs t) :=
  calc p * (q + 1) * W.stock cs (t + 1) + L.takersAbove R p cs t * R (t + 1)
      ≤ p * (q + 1) * W.stock cs (t + 1) + p * L.uptake cs t :=
        Nat.add_le_add_left (Nat.le_trans (Nat.le_of_eq (total_mul_right _ _ _))
          (Nat.le_trans (total_le (L.present t) fun f _ => mark_cases
              (q := fun m => m * R (t + 1) ≤ p * total cs (L.take t f))
              (fun takes => Nat.le_trans (Nat.le_of_eq (Nat.one_mul _)) takes)
              (fun _ => Nat.le_trans (Nat.le_of_eq (Nat.zero_mul _)) (Nat.zero_le _)))
            (Nat.le_of_eq ((total_mul p (fun f => total cs (L.take t f)) (L.present t)).trans
              (congrArg (p * ·) (total_swap (fun f c => L.take t f c) cs (L.present t))))))) _
    _ = p * ((q + 1) * W.stock cs (t + 1) + L.uptake cs t) :=
        (congrArg (· + p * L.uptake cs t) (mul_regroup p (q + 1) _)).trans
          (Nat.left_distrib _ _ _).symm
    _ ≤ p * ((q + 1) * (r t * W.stock cs t)) :=
        Nat.mul_le_mul_left p (balances.lowersTaking dissipates)
    _ = p * (q + 1) * (r t * W.stock cs t) := (mul_regroup p (q + 1) _).symm

/-- The exchange law. Balanced at a resolution that only refines and dissipative by the
share `q`, over a family without repetition closed at every step from `T` on, the times
since `T` that a formation takes at least `1/p` of the unit of step `T` from the family,
counted formation by formation, number at most `p (q + 1)` times its stock at `T`. -/
theorem exchange_bound {r : Nat → Nat} (balances : L.BalancesAt r W) {q : Nat}
    (dissipative : L.DissipativeBy q) {cs : List C} (distinct : Distinct cs) {T : Nat}
    (closed : ∀ t, T ≤ t → L.ClosedAt cs t) {R : Nat → Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (p n : Nat) : total (steps T n) (L.takersAbove R p cs) ≤ p * (q + 1) * W.stock cs T :=
  losses_bound base unit refining
    (fun t later => balances.takers_lose (dissipative cs t distinct (closed t later))) n

/-- So no formation takes at least `1/p` of the unit from the family at arbitrarily late
steps. -/
theorem exchange_not_recurring {r : Nat → Nat} (balances : L.BalancesAt r W) {q : Nat}
    (dissipative : L.DissipativeBy q) {cs : List C} (distinct : Distinct cs) {T : Nat}
    (closed : ∀ t, T ≤ t → L.ClosedAt cs t) {R : Nat → Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (p : Nat) :
    ¬ ∀ N, ∃ t f, N ≤ t ∧ f ∈ L.present t ∧ R (t + 1) ≤ p * total cs (L.take t f) :=
  fun recurs => bounded_not_recurring
    (exchange_bound balances dissipative distinct closed base unit refining p)
    fun N => match recurs N with
    | ⟨t, _, after, present, takes⟩ =>
      ⟨t, after, total_pos_of_mem (q := fun f => mark (R (t + 1) ≤ p * total cs (L.take t f)))
        present (mark_pos.mpr takes)⟩

end Flow

namespace World

variable {w : World}

/-- The growth law. In a world with a census whose relata are embodied, balanced at a
resolution that only refines and dissipative by the share `q`, with every step from `T`
on enclosed, the times since `T` that a relatum gains at least `1/p` of the unit of step
`T`, counted relatum by relatum, number at most `p q` times the total standing at `T`.
Each such gain is given within an enclosure, and the loss in proportion makes the
enclosure lose at least `1/(p q)` of the unit for each. -/
theorem growth_bound {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) {r : Nat → Nat} (balances : w.flow.BalancesAt r w.web) {q : Nat}
    (dissipative : w.flow.DissipativeBy q) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) {R : Nat → Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (p n : Nat) :
    total (steps T n) (fun t => w.web.gainers r R p t (alive (t + 1))) ≤
      p * q * w.web.stock (alive T) T :=
  have standing := standingCensus census embodied
  losses_bound (s := fun t => w.web.stock (alive t) t) base unit refining
    (fun t later => Decidable.of_not_not fun no =>
      (enclosed t later).aroundStanding_not_not alive fun ⟨es, distinct, before, after, closed⟩ =>
        no (Nat.le_trans (Nat.le_of_eq (congrArg (fun k => p * q * k + _)
            (standing.stock_eq distinct after)))
          (Nat.le_trans (balances.gainers_lose (dissipative es t distinct closed)
              (census (t + 1)).1 after)
            (Nat.le_of_eq (congrArg (fun k => p * q * (r t * k))
              (standing.stock_eq distinct before).symm))))) n

/-- So no relatum gains at least `1/p` of the unit at arbitrarily late steps. -/
theorem growth_not_recurring (counted : w.Counted) (embodied : w.Embodied) {r : Nat → Nat}
    (balances : w.flow.BalancesAt r w.web) {q : Nat} (dissipative : w.flow.DissipativeBy q)
    {T : Nat} (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) {R : Nat → Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (p : Nat) : ¬ ∀ N, ∃ t x, N ≤ t ∧ w.web.Gains r R p t x :=
  match counted with
  | ⟨_, census⟩ => fun recurs => bounded_not_recurring
    (growth_bound census embodied balances dissipative enclosed base unit refining p)
    fun N => match recurs (N + T) with
    | ⟨t, x, after, gains⟩ =>
      have later := Nat.le_trans (Nat.le_add_left T N) after
      have stands : 0 < w.web.level (t + 1) x := Nat.pos_of_ne_zero fun zero =>
        Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
          (units_pos base unit refining (Nat.le_succ_of_le later))
          (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_trans gains
            (Nat.le_of_eq ((congrArg (p * ·) zero).trans (Nat.mul_zero p))))))
      ⟨t, Nat.le_trans (Nat.le_add_right N T) after,
        total_pos_of_mem (q := fun c => mark (w.web.Gains r R p t c))
          (((standingCensus census embodied (t + 1)).2 x).mp stands) (mark_pos.mpr gains)⟩

/-- So arising at a size not vanishing does not recur: under the same premises, no relatum
arises standing at least `1/p` of the unit of step `T` at arbitrarily late steps. -/
theorem arising_not_recurring (counted : w.Counted) (embodied : w.Embodied) {r : Nat → Nat}
    (balances : w.flow.BalancesAt r w.web) {q : Nat} (dissipative : w.flow.DissipativeBy q)
    {T : Nat} (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) {R : Nat → Nat} (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (p : Nat) :
    ¬ ∀ N, ∃ t x, N ≤ t ∧ w.web.Arises t x ∧ R (t + 1) ≤ p * w.web.level (t + 1) x :=
  fun recurs => growth_not_recurring counted embodied balances dissipative enclosed base unit
    refining p fun N => match recurs N with
    | ⟨t, x, after, arises, size⟩ => ⟨t, x, after, Nat.le_trans (Nat.le_of_eq
        ((congrArg (fun k => R (t + 1) + p * (r t * k))
          (eq_zero_of_not_pos fun pos => arises.1 ((embodied x t).mpr pos))).trans
          ((congrArg (fun k => R (t + 1) + p * k) (Nat.mul_zero (r t))).trans
            ((congrArg (R (t + 1) + ·) (Nat.mul_zero p)).trans (Nat.add_zero _))))) size⟩

end World

/-- Units of step `t` per unit of step 0 where the unit halves at each step. -/
def halving : Nat → Nat
  | 0 => 1
  | t + 1 => 2 * halving t

/-! ## A unit refining without end -/

namespace Asymptote

variable (split : Nat → Nat)

/-- Across the step from `t` each unit splits into `split t + 1` finer units. -/
def refinement (t : Nat) : Nat :=
  split t + 1

/-- How many units of step `t` make one unit of step 0. -/
def units : Nat → Nat
  | 0 => 1
  | t + 1 => refinement split t * units t

/-- One drawer takes `split t` units of step `t + 1` from one pool and gives nothing back. -/
def flow : Flow Unit Unit :=
  ⟨fun _ => [()], fun t _ _ => split t, fun _ _ _ => 0⟩

/-- The pool stands one unit of step `t` above the drawer's need of one unit of step 0. -/
def web : Web Unit Unit :=
  ⟨fun t _ => units split t + 1, fun _ _ => True, fun _ _ _ => True,
    fun t _ _ => units split t, fun _ _ _ => True⟩

/-- The flow balances at the refining resolution. -/
theorem balances : (flow split).BalancesAt (refinement split) (web split) :=
  fun t c => match c with
  | () => show units split (t + 1) + 1 + (split t + 0) =
        refinement split t * (units split t + 1) + (0 + 0) from
      ((Nat.add_assoc _ _ _).trans (congrArg (refinement split t * units split t + ·)
        (Nat.add_comm 1 (split t)))).trans
      ((congrArg (refinement split t * units split t + ·)
        (Nat.mul_one (refinement split t)).symm).trans (Nat.left_distrib _ _ _).symm)

/-- The pool is closed at every step. -/
theorem closed (t : Nat) : (flow split).ClosedAt [()] t :=
  fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside

theorem distinct : Distinct [()] :=
  ⟨(fun mem => nomatch mem), trivial⟩

/-- Giving nothing back, the drawer dissipates on every family. -/
theorem dissipative : (flow split).Dissipative :=
  fun cs _ _ _ _ _ => Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_zero cs)).trans
    (Nat.zero_add _))) (sign_le _)

/-- Giving nothing back, the drawer loses all it takes: the flow is dissipative by every
share. -/
theorem dissipativeBy (q : Nat) : (flow split).DissipativeBy q :=
  fun cs _ _ _ _ _ => Nat.le_trans (Nat.le_of_eq ((congrArg ((q + 1) * ·) (total_zero cs)).trans
    (Nat.mul_zero _))) (Nat.zero_le _)

/-- The drawer is supported at every step. -/
theorem dependent : (web split).Dependent :=
  fun _ _ _ _ _ => Nat.le_add_right _ 1

/-- The pool stays above the drawer's need. -/
theorem above_need (t : Nat) : (web split).need t () () < (web split).level t () :=
  Nat.lt_succ_self _

/-- Only the drawer takes, and only from what it draws on; it gives nothing. -/
theorem taking : (flow split).Taking (web split) :=
  fun _ _ _ _ _ => ⟨trivial, trivial⟩

theorem acting : (flow split).Acting (web split) :=
  fun _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0)

/-- At each splitting step the pool falls, counted in the finer unit. -/
theorem falls {t : Nat} (splits : 0 < split t) :
    (web split).level (t + 1) () < refinement split t * (web split).level t () :=
  Nat.lt_of_lt_of_le (Nat.add_lt_add_left (Nat.succ_lt_succ splits) (units split (t + 1)))
    (Nat.le_of_eq ((congrArg (refinement split t * units split t + ·)
      (Nat.mul_one (refinement split t)).symm).trans (Nat.left_distrib _ _ _).symm))

/-- The flow exchanges at arbitrarily late steps exactly where the unit splits at
arbitrarily late steps. -/
theorem exchange_recurs_iff :
    (flow split).ExchangeRecurs ↔ ∀ N, ∃ t, N ≤ t ∧ 0 < split t :=
  ⟨fun recurs N => match recurs N with
    | ⟨t, _, _, later, _, .inl takes⟩ => ⟨t, later, takes⟩
    | ⟨_, _, _, _, _, .inr gives⟩ => absurd gives (Nat.lt_irrefl 0),
   fun splits N => match splits N with
    | ⟨t, later, positive⟩ => ⟨t, (), (), later, .head _, .inl positive⟩⟩

/-- Where the unit splits at arbitrarily late steps, the drawer takes from the closed pool
at arbitrarily late steps. -/
theorem taking_recurs (splits : ∀ N, ∃ t, N ≤ t ∧ 0 < split t) :
    ∀ N, ∃ t, N ≤ t ∧ 0 < (flow split).takers [()] t :=
  fun N => match splits N with
    | ⟨t, later, positive⟩ => ⟨t, later, match h : split t with
      | 0 => absurd (Nat.lt_of_lt_of_le positive (Nat.le_of_eq h)) (Nat.lt_irrefl 0)
      | _ + 1 => Nat.lt_of_lt_of_le (Nat.succ_pos 0) (Nat.le_of_eq
          (congrArg (fun k => sign (k + 0) + 0) h).symm)⟩

end Asymptote

/-! ## Exchange of a fixed size, with vanishing loss -/

namespace Circulation

/-- One less than the units of step `t` per unit of step 0; the unit halves at each step. -/
def spare : Nat → Nat
  | 0 => 0
  | t + 1 => 2 * spare t + 1

/-- Units of step `t` per unit of step 0. -/
def units (t : Nat) : Nat :=
  spare t + 1

/-- At each step the drawer takes one unit of step 0 from the pool, `units (t + 1)` units of
step `t + 1`, and gives all of it back but one unit of step `t + 1`. -/
def flow : Flow Unit Unit :=
  ⟨fun _ => [()], fun t _ _ => units (t + 1), fun t _ _ => spare (t + 1)⟩

/-- The pool stands one unit of step `t` above the drawer's need of one unit of step 0. -/
def web : Web Unit Unit :=
  ⟨fun t _ => spare t + 2, fun _ _ => True, fun _ _ _ => True, fun t _ _ => units t,
    fun _ _ _ => True⟩

theorem balances : flow.BalancesAt (fun _ => 2) web :=
  fun t c => match c with
  | () => show 2 * spare t + 1 + 2 + (2 * spare t + 1 + 1 + 0) =
        2 * (spare t + 2) + (2 * spare t + 1 + 0) from
      (Nat.succ_add (2 * spare t + 3) (2 * spare t + 1)).symm.trans
        (congrArg (· + (2 * spare t + 1)) (Nat.left_distrib 2 (spare t) 2).symm)

theorem closed (t : Nat) : flow.ClosedAt [()] t :=
  fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside

/-- Every take loses one unit of the step after it, so the flow dissipates. -/
theorem dissipative : flow.Dissipative :=
  fun cs t distinct _ f _ => match cs, distinct, f with
  | [], _, _ => Nat.le_refl 0
  | [()], _, () => Nat.le_refl (spare (t + 1) + 1)
  | () :: () :: _, ⟨fresh, _⟩, _ => absurd (List.Mem.head _) fresh

theorem dependent : web.Dependent :=
  fun _ _ _ _ _ => Nat.le_succ _

/-- The exchange never shrinks: at every step the drawer takes one unit of step 0. -/
theorem takes_a_unit (t : Nat) : flow.take t () () = units (t + 1) :=
  rfl

/-- What it gives back falls short of what it takes by one unit of the step after it. -/
theorem loses_one (t : Nat) : flow.give t () () + 1 = flow.take t () () :=
  rfl

/-- The units of `Circulation` are those of a unit halving at each step. -/
theorem units_eq : ∀ t, units t = halving t
  | 0 => rfl
  | t + 1 => (Nat.left_distrib 2 (spare t) 1).symm.trans (congrArg (2 * ·) (units_eq t))

/-- So at every step the drawer takes exactly one unit of step 0. -/
theorem takes_whole (t : Nat) : flow.take t () () = halving (t + 1) :=
  units_eq (t + 1)

theorem distinct : Distinct [()] :=
  ⟨(fun mem => nomatch mem), trivial⟩

/-- So no fixed share of what is taken is lost: by the exchange law, for no `q` is the flow
dissipative by the share `q`. -/
theorem not_dissipativeBy (q : Nat) : ¬ flow.DissipativeBy q :=
  fun dissipative => Flow.exchange_not_recurring balances dissipative distinct (T := 0)
    (fun t _ => closed t) (R := halving) rfl (fun _ _ => rfl) (fun _ _ => Nat.succ_pos 1) 1
    fun N => ⟨N, (), Nat.le_refl N, .head _, Nat.le_of_eq ((takes_whole N).symm.trans
      (Nat.one_mul _).symm)⟩

/-- The pool stands throughout and is listed. -/
theorem standing : web.StandingCensus fun _ => [()] :=
  fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun c => match c with
    | () => ⟨fun _ => .head _, fun _ => Nat.succ_pos _⟩⟩

/-- Every step is enclosed around what stands. -/
theorem around (t : Nat) : flow.AroundStanding (fun _ => [()]) t :=
  ⟨[()], ⟨fun no => (nomatch no), trivial⟩, (fun c _ => match c with | () => .head _),
    (fun c _ => match c with | () => .head _), closed t⟩

theorem exchange_recurs : flow.ExchangeRecurs :=
  fun N => ⟨N, (), (), Nat.le_refl N, .head _, .inl (Nat.succ_pos _)⟩

end Circulation

/-! ## Arising without end inside enclosure -/

namespace Emission

/-- The relatum emitted at step `s`: nothing through step `s`, then one unit of step
`s + 1`, kept as the unit halves. -/
def bud (s : Nat) : Nat → Nat
  | 0 => 0
  | t + 1 => 2 * bud s t + mark (s = t)

/-- What the pool takes across a step: two units of the step after it, from itself. -/
def drawn : Option Nat → Nat
  | none => 2
  | some _ => 0

/-- What the pool gives across the step from `t`: one unit to the relatum emitted then. -/
def emitted (t : Nat) : Option Nat → Nat
  | none => 0
  | some s => mark (s = t)

/-- The pool, `none`, stands at `halving t + 2` units of step `t`; the relatum emitted at `s`
at `bud s t`. -/
def level (t : Nat) : Option Nat → Nat
  | none => halving t + 2
  | some s => bud s t

def flow : Flow (Option Nat) (Option Nat) :=
  ⟨fun _ => [none], fun _ _ => drawn, fun t _ => emitted t⟩

/-- Each relatum is active exactly while it stands; the pool draws on itself. -/
def web : Web (Option Nat) (Option Nat) :=
  ⟨level, fun t x => 0 < level t x, fun _ _ _ => False, fun _ _ _ => 0,
    fun _ _ c => c = none⟩

def world : World :=
  ⟨Option Nat, flow, web⟩

theorem bud_before {s : Nat} : ∀ {t}, t ≤ s → bud s t = 0
  | 0, _ => rfl
  | t + 1, early =>
    (congrArg (fun k => 2 * k + mark (s = t)) (bud_before (Nat.le_of_succ_le early))).trans
      (congrArg (2 * 0 + ·) (mark_zero fun same =>
        Nat.lt_irrefl t (Nat.lt_of_lt_of_le early (Nat.le_of_eq same))))

theorem bud_after (s : Nat) : bud s (s + 1) = 1 :=
  (congrArg (fun k => 2 * k + mark (s = s)) (bud_before (Nat.le_refl s))).trans
    (congrArg (2 * 0 + ·) (mark_one rfl))

theorem bud_pos {s : Nat} : ∀ {t}, s + 1 ≤ t → 0 < bud s t
  | _, .refl => Nat.lt_of_lt_of_le (Nat.succ_pos 0) (Nat.le_of_eq (bud_after s).symm)
  | t + 1, .step later => Nat.lt_of_lt_of_le (bud_pos later)
      (Nat.le_trans (Nat.le_trans (Nat.le_of_eq (Nat.one_mul _).symm)
        (Nat.mul_le_mul_right (bud s t) (Nat.le_succ 1))) (Nat.le_add_right _ _))

theorem active_bud {s t : Nat} : web.active t (some s) ↔ s < t :=
  ⟨fun active => match Nat.lt_or_ge s t with
    | .inl before => before
    | .inr late => absurd (Nat.lt_of_lt_of_le active (Nat.le_of_eq (bud_before late)))
        (Nat.lt_irrefl 0),
   fun before => bud_pos before⟩

theorem none_not_mem : ∀ l : List Nat, ¬ (none : Option Nat) ∈ l.map some
  | [], mem => nomatch mem
  | _ :: l, mem => match mem with
    | .tail _ rest => none_not_mem l rest

theorem some_inj : ∀ a b : Nat, (some a : Option Nat) = some b → a = b :=
  fun _ _ same => congrArg (fun o => Option.getD o 0) same

/-- The pool and the relata emitted so far, each once. -/
def alive (t : Nat) : List (Option Nat) :=
  none :: (steps 0 t).map some

/-- A census: what is active at each step is listed, each once. -/
theorem census : web.Census alive :=
  fun t => ⟨⟨none_not_mem _, distinct_map some_inj (steps_distinct 0 t)⟩, fun x => match x with
    | none => ⟨fun _ => .head _, fun _ => Nat.succ_pos _⟩
    | some s => ⟨fun active => .tail _ (mem_map_of (steps_of_within (Nat.zero_le s)
          (Nat.lt_of_lt_of_le (active_bud.mp active) (Nat.le_of_eq (Nat.zero_add t).symm)))),
        fun mem => match mem with
          | .tail _ rest => active_bud.mpr (Nat.lt_of_lt_of_le
              (steps_within (mem_of_map some_inj rest)) (Nat.le_of_eq (Nat.zero_add t)))⟩⟩

theorem counted : world.Counted :=
  ⟨alive, census⟩

theorem embodied : world.Embodied :=
  fun _ _ => Iff.rfl

/-- The flow balances at a unit halving at each step. -/
theorem balances : flow.BalancesAt (fun _ => 2) web :=
  fun t c => match c with
  | none => show 2 * halving t + 2 + (2 + 0) = 2 * (halving t + 2) + (0 + 0) from
      (Nat.add_assoc (2 * halving t) 2 2).trans (Nat.left_distrib 2 (halving t) 2).symm
  | some _ => rfl

theorem emitted_absent {t : Nat} :
    ∀ {cs : List (Option Nat)}, ¬ some t ∈ cs → total cs (emitted t) = 0
  | [], _ => rfl
  | none :: _, absent => (Nat.zero_add _).trans (emitted_absent fun mem => absent (.tail _ mem))
  | some _ :: cs, absent =>
    (congrArg (· + total cs (emitted t)) (mark_zero fun same =>
      absent (Eq.subst (motive := fun k => some t ∈ some k :: cs) same.symm (.head cs)))).trans
    ((Nat.zero_add _).trans (emitted_absent fun mem => absent (.tail _ mem)))

theorem emitted_le_one {t : Nat} : ∀ {cs : List (Option Nat)}, Distinct cs → total cs (emitted t) ≤ 1
  | [], _ => Nat.zero_le 1
  | none :: _, ⟨_, distinct⟩ =>
    Nat.le_trans (Nat.le_of_eq (Nat.zero_add _)) (emitted_le_one distinct)
  | some s :: cs, ⟨fresh, distinct⟩ => match Nat.decEq s t with
    | isTrue same => Nat.add_le_add (mark_le_one _) (Nat.le_of_eq (emitted_absent fun mem =>
        fresh (Eq.subst (motive := fun k => some k ∈ cs) same.symm mem)))
    | isFalse other => Nat.le_trans (Nat.le_of_eq ((congrArg (· + total cs (emitted t))
        (mark_zero other)).trans (Nat.zero_add _))) (emitted_le_one distinct)

def decideNone (x : Option Nat) : Decidable (x = none) :=
  match x with
  | none => isTrue rfl
  | some _ => isFalse fun same => nomatch same

/-- A family closed across a step holds the pool, which takes from itself. -/
theorem pool_mem {cs : List (Option Nat)} {t : Nat} (closed : flow.ClosedAt cs t) :
    none ∈ cs :=
  match decideSome (decide := decideNone) cs with
  | isTrue ⟨_, mem, same⟩ => Eq.subst (motive := (· ∈ cs)) same mem
  | isFalse absent =>
    Nat.noConfusion (closed none (.head _) none fun mem => absent ⟨none, mem, rfl⟩).1

/-- The flow dissipates: on a family closed across a step, the pool gives at most one unit
and takes two. -/
theorem dissipative : flow.Dissipative :=
  fun _ _ distinct closed _ _ => Nat.le_trans
    (Nat.add_le_add (emitted_le_one distinct) (sign_le_one _))
    (le_total_of_mem (q := drawn) (pool_mem closed))

/-- Every step is enclosed: the pool and the relatum emitted then are closed. -/
theorem enclosed (t : Nat) : flow.Enclosed t :=
  ⟨[none, some t], ⟨(fun mem => match mem with | .tail _ rest => nomatch rest),
      ⟨(fun mem => nomatch mem), trivial⟩⟩,
   fun _ _ c outside => match c with
    | none => absurd (.head _) outside
    | some _ => ⟨rfl, mark_zero fun same => outside (Eq.subst
        (motive := fun k => some k ∈ [none, some t]) same.symm (.tail _ (.head _)))⟩⟩

/-- A new relatum arises at every step. -/
theorem arises (t : Nat) : web.Arises t (some t) :=
  ⟨fun active => absurd (Nat.lt_of_lt_of_le active (Nat.le_of_eq (bud_before (Nat.le_refl t))))
      (Nat.lt_irrefl 0),
   bud_pos (Nat.le_refl (t + 1))⟩

theorem arising_recurs : world.ArisingRecurs :=
  fun N => ⟨N, some N, Nat.le_refl N, arises N⟩

/-- Only the active pool gives and takes, and it takes only from itself. -/
theorem acting : flow.Acting web :=
  fun _ f _ present _ => match f, present with
  | none, _ => Nat.succ_pos _

theorem taking : flow.Taking web :=
  fun _ f c present takes => match f, present, c with
  | none, _, none => ⟨Nat.succ_pos _, rfl⟩
  | none, _, some _ => absurd takes (Nat.lt_irrefl 0)

/-- The flow dissipates in proportion: on a family closed across a step, the pool gives
back at most half of what it takes. -/
theorem dissipativeBy : flow.DissipativeBy 1 :=
  fun _ _ distinct closed _ _ => Nat.le_trans (Nat.mul_le_mul_left 2 (emitted_le_one distinct))
    (Nat.le_trans (le_total_of_mem (q := drawn) (pool_mem closed))
      (Nat.le_of_eq (Nat.one_mul _).symm))

/-- What arises at step `t` stands at one unit of step `t + 1`. -/
theorem arises_small (t : Nat) : web.level (t + 1) (some t) = 1 :=
  bud_after t

end Emission

/-! ## A whole unit handed back and forth -/

namespace Alternation

open Shuttle (holder stands)

/-- The side holding the standing at step `t` stands at `halving t + 1` units of step `t`,
one unit of step 0 and one of step `t`; the other side stands at nothing. -/
def level (t : Nat) (x : Bool) : Nat :=
  stands x t * (halving t + 1)

/-- Across each step the holder takes all it holds and gives the other side all of it but
one unit of the step after. -/
def flow : Flow Bool Bool :=
  ⟨fun t => [holder t], fun t _ x => stands x t * (2 * halving t + 2),
    fun t _ x => stands x (t + 1) * (2 * halving t + 1)⟩

/-- Each side is active exactly while it stands. -/
def web : Web Bool Bool :=
  ⟨level, fun t x => 0 < level t x, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩

def world : World :=
  ⟨Bool, flow, web⟩

/-- The flow balances at a unit halving at each step. -/
theorem balances : flow.BalancesAt (fun _ => 2) web :=
  fun t x => show stands x (t + 1) * (2 * halving t + 1) +
        (stands x t * (2 * halving t + 2) + 0) =
      2 * (stands x t * (halving t + 1)) + (stands x (t + 1) * (2 * halving t + 1) + 0) from
    (Nat.add_comm _ _).trans (congrArg (· + stands x (t + 1) * (2 * halving t + 1))
      ((congrArg (stands x t * ·) (Nat.left_distrib 2 (halving t) 1).symm).trans
        (mul_turn _ _ _)))

theorem stands_sum : ∀ t, stands true t + stands false t = 1
  | 0 => rfl
  | 1 => rfl
  | t + 2 => stands_sum t

theorem stands_one {x : Bool} {t : Nat} (standing : 0 < stands x t) : stands x t = 1 :=
  Eq.subst (motive := fun b => stands b t = 1) ((Exposed.stands_iff x t).mp standing).symm
    (Exposed.holder_one t)

theorem active_iff {t : Nat} {x : Bool} : web.active t x ↔ 0 < stands x t :=
  ⟨fun active => match Nat.eq_zero_or_pos (stands x t) with
    | .inl zero => absurd (Nat.lt_of_lt_of_le active (Nat.le_of_eq
        ((congrArg (· * (halving t + 1)) zero).trans (Nat.zero_mul _)))) (Nat.lt_irrefl 0)
    | .inr standing => standing,
   fun standing => (Nat.mul_le_mul standing (Nat.succ_pos (halving t)) : 1 * 1 ≤ _)⟩

/-- The holder is the one active relatum. -/
theorem census : web.Census fun t => [holder t] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x =>
    ⟨fun active => Eq.subst (motive := fun b => b ∈ [holder t])
        ((Exposed.stands_iff x t).mp (active_iff.mp active)).symm (.head _),
     fun mem => active_iff.mpr ((Exposed.stands_iff x t).mpr (match mem_cons_cases mem with
        | .inl same => same
        | .inr no => nomatch no))⟩⟩

theorem counted : world.Counted :=
  ⟨_, census⟩

theorem embodied : world.Embodied :=
  fun _ _ => Iff.rfl

/-- The two sides are all there is, so every step is enclosed. -/
theorem enclosed (t : Nat) : flow.Enclosed t :=
  Flow.enclosed_of_finite Shuttle.distinct Shuttle.every t

/-- The holder takes all it holds. -/
theorem holder_takes (t : Nat) : 2 * halving t + 2 = stands (holder t) t * (2 * halving t + 2) :=
  (Nat.one_mul _).symm.trans (congrArg (· * (2 * halving t + 2)) (Exposed.holder_one t).symm)

/-- A family closed across a step holds the holder. -/
theorem holder_mem {es : List Bool} {t : Nat} (closed : flow.ClosedAt es t) : holder t ∈ es :=
  match decideSome (decide := fun b => instDecidableEqBool b (holder t)) es with
  | isTrue ⟨_, mem, same⟩ => Eq.subst (motive := (· ∈ es)) same mem
  | isFalse absent => absurd (closed (holder t) (.head _) (holder t)
      fun mem => absent ⟨holder t, mem, rfl⟩).1 fun zero => Nat.lt_irrefl 0
        (Nat.lt_of_lt_of_le (Nat.succ_pos (2 * halving t + 1))
          (Nat.le_trans (Nat.le_of_eq (holder_takes t)) (Nat.le_of_eq zero)))

/-- What is given across a step totals at most all but one unit of the step after. -/
theorem given_total {es : List Bool} (distinct : Distinct es) (t : Nat) (f : Bool) :
    total es (flow.give t f) ≤ 2 * halving t + 1 :=
  Nat.le_trans (total_le_of_support distinct fun c _ _ => Shuttle.every c)
    (Nat.le_of_eq ((add_mul_split (stands true (t + 1)) (stands false (t + 1)) _).symm.trans
      ((congrArg (· * (2 * halving t + 1)) (stands_sum (t + 1))).trans (Nat.one_mul _))))

/-- Each step loses one unit of the step after it, so the flow dissipates. -/
theorem dissipative : flow.Dissipative :=
  fun _ t distinct closed f _ => Nat.le_trans
    (Nat.add_le_add (given_total distinct t f) (sign_le_one _))
    (Nat.le_trans (Nat.le_of_eq (holder_takes t)) (le_total_of_mem (q := flow.take t f)
      (holder_mem closed)))

/-- A whole unit of step 0 arises at arbitrarily late steps. -/
theorem arising_whole (N : Nat) :
    ∃ t x, N ≤ t ∧ web.Arises t x ∧ halving (t + 1) ≤ 1 * web.level (t + 1) x :=
  match Shuttle.recurs true N with
  | ⟨t, after, before, now⟩ => ⟨t, true, after,
      ⟨fun active => before (active_iff.mp active), active_iff.mpr now⟩,
      Nat.le_trans (Nat.le_succ _) (Nat.le_of_eq ((Nat.one_mul _).symm.trans
        ((congrArg (· * (halving (t + 1) + 1)) (stands_one now).symm).trans
          (Nat.one_mul _).symm)))⟩

theorem arising_recurs : world.ArisingRecurs :=
  fun N => match arising_whole N with
  | ⟨t, x, after, arises, _⟩ => ⟨t, x, after, arises⟩

/-- So no fixed share of what is taken is lost: by the growth law, for no `q` is the flow
dissipative by the share `q`. -/
theorem not_dissipativeBy (q : Nat) : ¬ flow.DissipativeBy q :=
  fun dissipative => World.arising_not_recurring (w := world) counted embodied balances
    dissipative (T := 0) (fun t _ => enclosed t) (R := halving) rfl (fun _ _ => rfl)
    (fun _ _ => Nat.succ_pos 1) 1 arising_whole

end Alternation


/-- Continued arising needs a quantum. With a fixed unit, a world with a census whose
relata are embodied, balanced and dissipative cannot arise without end with every step
from some step on enclosed (`World.arising_opens`). At a unit halving at each step, the
world of `Emission` has a census, embodied relata, a flow balanced at that resolution,
dissipative and even dissipative in proportion, every step enclosed, and arising at every
step. By the growth law what arises there shrinks below every quantum
(`Emission.arises_small`). -/
theorem arising_needs_quantum :
    Emission.world.Counted ∧ Emission.world.Embodied ∧
      Emission.flow.BalancesAt (fun _ => 2) Emission.web ∧ Emission.world.Dissipative ∧
      Emission.flow.DissipativeBy 1 ∧
      (∀ t, Emission.world.flow.Enclosed t) ∧ Emission.world.ArisingRecurs :=
  ⟨Emission.counted, Emission.embodied, Emission.balances, Emission.dissipative,
    Emission.dissipativeBy, Emission.enclosed, Emission.arising_recurs⟩

/-- Arising at a size not vanishing needs loss in proportion. With loss in proportion it
stops in every enclosed world at every resolution (`World.arising_not_recurring`). With
only the loss of one unit of the step after, the world of `Alternation` has a census,
embodied relata, a flow balanced at a unit halving at each step and dissipative, every
step enclosed, and a whole unit of step 0 arising at arbitrarily late steps; for no share
is it dissipative in proportion. -/
theorem arising_needs_proportion :
    Alternation.world.Counted ∧ Alternation.world.Embodied ∧
      Alternation.flow.BalancesAt (fun _ => 2) Alternation.web ∧ Alternation.world.Dissipative ∧
      (∀ t, Alternation.world.flow.Enclosed t) ∧
      (∀ N, ∃ t x, N ≤ t ∧ Alternation.web.Arises t x ∧
        halving (t + 1) ≤ 1 * Alternation.web.level (t + 1) x) ∧
      ∀ q, ¬ Alternation.flow.DissipativeBy q :=
  ⟨Alternation.counted, Alternation.embodied, Alternation.balances, Alternation.dissipative,
    Alternation.enclosed, Alternation.arising_whole, Alternation.not_dissipativeBy⟩

/-- Exchange of a fixed size needs a quantum. With a fixed unit, exchange enclosed around
what stands stops (`World.exchange_stops`). At a unit halving at each step, in
`Circulation` what stands is listed, the flow balances at that resolution and dissipates,
every step is enclosed around what stands, and the drawer takes one whole unit of step 0
at every step; for no share is it dissipative in proportion (`Flow.exchange_not_recurring`). -/
theorem exchange_needs_quantum :
    Circulation.web.StandingCensus (fun _ => [()]) ∧
      Circulation.flow.BalancesAt (fun _ => 2) Circulation.web ∧
      Circulation.flow.Dissipative ∧
      (∀ t, Circulation.flow.AroundStanding (fun _ => [()]) t) ∧
      (∀ t, Circulation.flow.take t () () = halving (t + 1)) ∧
      Circulation.flow.ExchangeRecurs ∧ ∀ q, ¬ Circulation.flow.DissipativeBy q :=
  ⟨Circulation.standing, Circulation.balances, Circulation.dissipative, Circulation.around,
    Circulation.takes_whole, Circulation.exchange_recurs, Circulation.not_dissipativeBy⟩

/-- Rest needs a quantum of loss. With the unit fixed from some step on, taking from a
closed family stops in every flow balanced at that resolution and dissipative; with the
unit splitting at arbitrarily late steps, the closed pool of `Asymptote` is taken from at
arbitrarily late steps, its flow balanced at that resolution and dissipative, even losing
all it takes, and its drawer supported throughout. By the exchange law what is taken
shrinks below every quantum. -/
theorem rest_needs_quantum (split : Nat → Nat) (splits : ∀ N, ∃ t, N ≤ t ∧ 0 < split t) :
    (Asymptote.flow split).BalancesAt (Asymptote.refinement split) (Asymptote.web split) ∧
      (Asymptote.flow split).Dissipative ∧ (∀ q, (Asymptote.flow split).DissipativeBy q) ∧
      (Asymptote.web split).Dependent ∧ (∀ t, (Asymptote.flow split).ClosedAt [()] t) ∧
      ∀ N, ∃ t, N ≤ t ∧ 0 < (Asymptote.flow split).takers [()] t :=
  ⟨Asymptote.balances split, Asymptote.dissipative split, Asymptote.dissipativeBy split,
    Asymptote.dependent split, Asymptote.closed split, Asymptote.taking_recurs split splits⟩

end Becoming
