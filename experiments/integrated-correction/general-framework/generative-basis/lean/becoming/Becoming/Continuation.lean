import Becoming.Roles

/-!
# Continuation: what a continuing formation must count

Ren's proposal of 10 October 2026 restates the metaethical core in two halves. Anything
that wants its continuation gives that continuation significance; following that want, it
must count what its continuation depends on, and the dynamics, with no ethical premise,
says how far that count reaches. This module states that half on flows and webs. The
center, whose continuation counts, is not settled here: `Becoming.Standpoints` states it.

* **Beyond the boundary.** Across a step, a formation taking part *conveys* from `c` to `d`
  when it takes from `c` and gives to `d` (`Flow.Conveys`); a family is *fed from beyond*
  across the step when something outside it is conveyed into one of its members
  (`Flow.FedFromBeyond`). A step at which the family is fed from beyond is not inward
  (`not_inward_of_fed`), and with equality decided a step at which it is not fed from
  beyond is inward (`inward_of_not_fed`), so the two are exact opposites
  (`inward_iff_not_fed`). Every draw-in law therefore reads as being fed: whatever refutes
  "inward from some step on" refutes "fed from nothing beyond from some step on"
  (`fed_of_not_inward`). Under balance and dissipation, a finite family without
  repetition, enclosed around from some step on, cannot from any step on be fed from
  nothing beyond it, whether taking from it recurs (`fed_from_beyond`), its members rise
  at arbitrarily late steps (`rising_fed_from_beyond`), or, read with one kind of
  relatum, embodied members arise at arbitrarily late steps
  (`Web.embodiedArising_fed_from_beyond`). Being fed is needed; no condition it is fed
  from need recur: in `Lone` the pool is fed at every step, and each fuel is conveyed from at one
  step only (`Lone.fed`, `Lone.each_fuel_once`). The one formation conveying, the source, is
  the same at every step.
* **Beyond one's own draw.** Each formation can take from a condition within what the
  step gives it (`WithinOwn`) while together they take more (`WithinJoint` fails;
  `Pair.own_not_joint`). Taking jointly within what is given keeps the level
  (`joint_keeps`); a step of joint excess lowers it by at least one (`excess_lowers`), so
  `n` consecutive steps of joint excess need a level of at least `n` at the start
  (`excess_bounded`), and in the pair no web balances the flow at all (`Pair.no_web`).
  Conversely a step of joint net giving raises the level by at least one (`net_give_raises_at`),
  and where the formations give jointly more than they take whenever the level is not below
  where it started, `m - level` steps bring it back to `m` (`restores`): the law of
  restoration. `RelationalRenewal.Law`'s recovery is an instance (`Becoming.RenewalFlow`).
* **Renewal that depends on what it renews.** Where every formation giving to a condition
  depends on it at a need of at least `m`, only active formations give and activity needs
  support, a level below `m` stays below `m` at every later step (`stays_below`), and
  every formation depending on the condition at a need of at least `m` is inactive from
  then on (`ends_below`). Joint excess that brings the level below `m` therefore ends the
  renewal and every formation depending on the condition at such a need, a taker among
  them where it so depends (`joint_excess_ends`). The joint count binds a want that
  outlasts what the condition holds: `n` steps of joint excess need only a level of `n`.
  In `Exceeding` a renewer and two takers, each taking within what the step gives, all end
  after two steps (`Exceeding.all_end`); with one taker the same renewer keeps the level
  and all continue (`Alone.all_continue`).
  `RelationalRenewal.Law`'s loss of renewal for good, and the ending for good of each
  formation depending on its condition once the level is below its need, are instances
  (`Becoming.RenewalFlow`).
* **What the derived extent does not reach.** Following the want counts what one's
  continuation depends on, and no more. In `Downstream` the self's continuation requires
  only its ground; a formation living on what the self gives ends when it stops giving,
  and the self continues (`Downstream.one_way`). In `Mortal` a formation active for two
  steps has every dependence met while it lives; its taking ends the renewal of a shared
  condition, and another formation depending on it ends after the first has ended
  (`Mortal.after_its_end`); without it, the renewer and the successor continue
  (`Mortal.without_continues`). In `Clearing`
  a clearer is active at every step, every condition it depends on is renewed and fed from
  beyond, and it takes jointly within what is given from each of them, while it draws
  down the habitat of a dweller, which ends (`Clearing.undermines_within_renewal`; the witness
  is stated in `Becoming.Clearing`, after `Becoming.Regions`). The endings in
  these witnesses are stipulated in their activity; each witness shows its ending
  consistent with balance, support and dependence, and the general theorems are where an
  ending is derived. The source of `Clearing`, like that of `Lone`, requires nothing.

The draw-in laws this module rereads are those of `Becoming.Dissipation` and
`Becoming.Roles`; the delta is the conveyance form, its exactness, the joint count, the
support-gated end, and the limits. Equality decided is a disclosed logical commitment, as
in `Flow.Enclosed.around`. No ethical predicate, ranking or axiom occurs.

Declarations moved here unchanged, with their names, from `Becoming.Standpoints` (board item W): see
the sections so headed.
-/

namespace Becoming

variable {F C : Type}

namespace Flow

/-! ## Conveying and being fed from beyond -/

section Conveying

variable (L : Flow F C)

/-- Across the step from `t`, some formation taking part takes from `c` and gives to `d`:
something is conveyed from `c` to `d`. -/
def Conveys (t : Nat) (c d : C) : Prop :=
  ∃ f, f ∈ L.present t ∧ 0 < L.take t f c ∧ 0 < L.give t f d

/-- Across the step from `t`, something beyond the family is conveyed into one of its
members. -/
def FedFromBeyond (ds : List C) (t : Nat) : Prop :=
  ∃ c d, ¬ c ∈ ds ∧ d ∈ ds ∧ L.Conveys t c d

variable {L}

/-- A step at which the family is fed from beyond is not inward. -/
theorem not_inward_of_fed {ds : List C} {t : Nat} (fed : L.FedFromBeyond ds t) :
    ¬ L.Inward ds t :=
  match fed with
  | ⟨c, _, outside, inside, f, present, takes, gives⟩ => fun inward =>
    outside (inward f present (total_pos_of_mem inside gives) c takes)

/-- With equality decided, a step at which nothing beyond the family is conveyed into it
is inward. -/
theorem inward_of_not_fed [DecidableEq C] {ds : List C} {t : Nat}
    (none : ¬ L.FedFromBeyond ds t) : L.Inward ds t :=
  fun f present gives c takes => match decideMem c ds with
    | .isTrue mem => mem
    | .isFalse outside => match total_pos ds gives with
      | ⟨d, inside, given⟩ => absurd ⟨c, d, outside, inside, f, present, takes, given⟩ none

/-- With equality decided, a step is inward exactly when the family is not fed from beyond
across it. -/
theorem inward_iff_not_fed [DecidableEq C] {ds : List C} {t : Nat} :
    L.Inward ds t ↔ ¬ L.FedFromBeyond ds t :=
  ⟨fun inward fed => not_inward_of_fed fed inward, inward_of_not_fed⟩

/-- Whatever refutes "inward from `N` on" refutes "fed from nothing beyond from `N` on". -/
theorem fed_of_not_inward [DecidableEq C] {ds : List C} {N : Nat}
    (opens : ¬ ∀ t, N ≤ t → L.Inward ds t) : ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fun never => opens fun t later => inward_of_not_fed (never t later)

variable {W : Web F C}

/-- A continuing family is fed from beyond, from a step on: where formations take from a
finite family without repetition at arbitrarily late steps, and from `T₀` on the family is
balanced on, enclosed around, and every family closed across each step is dissipated on,
it cannot from any step on be fed from nothing beyond it. -/
theorem fed_from_beyond_from [DecidableEq C] {ds : List C} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t) (balances : ∀ t, T₀ ≤ t → L.BalancesOn W ds t)
    (dissipative : ∀ t, T₀ ≤ t → ∀ es, Distinct es → L.ClosedAt es t → L.DissipatesOn es t)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fed_of_not_inward (taking_draws_in_from distinct around balances dissipative recurs N)

/-- So is a family whose members rise at arbitrarily late steps. -/
theorem rising_fed_from_beyond_from [DecidableEq C] {ds : List C} (distinct : Distinct ds)
    {T₀ : Nat} (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (balances : ∀ t, T₀ ≤ t → L.BalancesOn W ds t)
    (dissipative : ∀ t, T₀ ≤ t → ∀ es, Distinct es → L.ClosedAt es t → L.DissipatesOn es t)
    (rising : ∀ N, ∃ t c, N ≤ t ∧ c ∈ ds ∧ W.Rises t c) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fed_of_not_inward (rising_draws_in_from distinct around balances dissipative rising N)

/-- A continuing family is fed from beyond: under balance and dissipation, where formations
take from a finite family without repetition at arbitrarily late steps and the family is
enclosed around from some step on, it cannot from any step on be fed from nothing beyond
it. -/
theorem fed_from_beyond [DecidableEq C] (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List C} (distinct : Distinct ds) {T₀ : Nat} (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  fed_from_beyond_from distinct around (fun t _ => balances.on ds t)
    (fun t _ es => dissipative es t) recurs N

/-- So is a family whose members rise at arbitrarily late steps. -/
theorem rising_fed_from_beyond [DecidableEq C] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List C} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (rising : ∀ N, ∃ t c, N ≤ t ∧ c ∈ ds ∧ W.Rises t c) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  rising_fed_from_beyond_from distinct around (fun t _ => balances.on ds t)
    (fun t _ es => dissipative es t) rising N

end Conveying

/-! ## Counting one's own draw and the joint draw -/

section Joint

/-- Each formation taking part takes from the condition no more than the step gives it. -/
def WithinOwn (L : Flow F C) (t : Nat) (c : C) : Prop :=
  ∀ f, f ∈ L.present t → L.take t f c ≤ L.given t c

/-- Together the formations taking part take from the condition no more than the step
gives it. -/
def WithinJoint (L : Flow F C) (t : Nat) (c : C) : Prop :=
  L.taken t c ≤ L.given t c

variable {L : Flow F C} {W : Web F C}

/-- With balance at the condition across the step, taking jointly within what is given, the
level does not fall. -/
theorem joint_keeps_at {t : Nat} {c : C} (balances : L.BalancesOn W [c] t)
    (within : L.WithinJoint t c) : W.level t c ≤ W.level (t + 1) c :=
  le_of_add_le_add_right (L.taken t c)
    (Nat.le_trans (Nat.add_le_add_left within (W.level t c))
      (Nat.le_of_eq (balances c (.head [])).symm))

/-- Taking jointly within what is given, the level does not fall. -/
theorem joint_keeps (balances : L.Balances W) {t : Nat} {c : C}
    (within : L.WithinJoint t c) : W.level t c ≤ W.level (t + 1) c :=
  joint_keeps_at (balances.on [c] t) within

/-- With balance at the condition across the step, a step of joint excess lowers the level
by at least one. -/
theorem excess_lowers_at {t : Nat} {c : C} (balances : L.BalancesOn W [c] t)
    (excess : L.given t c < L.taken t c) : W.level (t + 1) c + 1 ≤ W.level t c :=
  le_of_add_le_add_right (L.given t c)
    (Nat.le_trans
      (Nat.le_of_eq ((Nat.add_assoc _ 1 _).trans
        (congrArg (W.level (t + 1) c + ·) (Nat.add_comm 1 (L.given t c)))))
      (Nat.le_trans
        (Nat.add_le_add_left (show L.given t c + 1 ≤ L.taken t c from excess) _)
        (Nat.le_of_eq (balances c (.head [])))))

/-- A step of joint excess lowers the level by at least one. -/
theorem excess_lowers (balances : L.Balances W) {t : Nat} {c : C}
    (excess : L.given t c < L.taken t c) : W.level (t + 1) c + 1 ≤ W.level t c :=
  excess_lowers_at (balances.on [c] t) excess

/-- With balance at the condition across each of the `n` steps, `n` consecutive steps of
joint excess lower the level by at least `n`. -/
theorem excess_bounded_at {c : C} {T : Nat} :
    ∀ n, (∀ k, k < n → L.BalancesOn W [c] (T + k)) →
      (∀ k, k < n → L.given (T + k) c < L.taken (T + k) c) →
      W.level (T + n) c + n ≤ W.level T c
  | 0, _, _ => Nat.le_refl _
  | n + 1, balances, excess =>
    Nat.le_trans (Nat.le_of_eq (Nat.add_right_comm (W.level (T + n + 1) c) n 1))
      (Nat.le_trans
        (Nat.add_le_add_right (excess_lowers_at (balances n (Nat.lt_succ_self n))
          (excess n (Nat.lt_succ_self n))) n)
        (excess_bounded_at n (fun k below => balances k (Nat.lt_succ_of_lt below))
          fun k below => excess k (Nat.lt_succ_of_lt below)))

/-- Joint excess cannot last: over `n` consecutive steps of joint excess from `T`, the
level falls by at least `n`. -/
theorem excess_bounded (balances : L.Balances W) {c : C} {T : Nat} :
    ∀ n, (∀ k, k < n → L.given (T + k) c < L.taken (T + k) c) →
      W.level (T + n) c + n ≤ W.level T c :=
  fun n => excess_bounded_at n fun k _ => balances.on [c] (T + k)

/-- With balance at the condition across the step, a step of joint net giving raises the level
by at least one. -/
theorem net_give_raises_at {t : Nat} {c : C} (balances : L.BalancesOn W [c] t)
    (netGive : L.taken t c < L.given t c) : W.level t c + 1 ≤ W.level (t + 1) c :=
  le_of_add_le_add_right (L.taken t c)
    (Nat.le_trans
      (Nat.le_of_eq ((Nat.add_assoc _ 1 _).trans
        (congrArg (W.level t c + ·) (Nat.add_comm 1 (L.taken t c)))))
      (Nat.le_trans
        (Nat.add_le_add_left (show L.taken t c + 1 ≤ L.given t c from netGive) _)
        (Nat.le_of_eq (balances c (.head [])).symm)))

/-- Restoration while the giving stays supported: with balance at the condition across each
of `n` steps from `T`, and joint net giving at each of them where the level is not below where
it was at `T`, the level rises by at least `n`. -/
theorem net_give_bounded_at {c : C} {T : Nat} :
    ∀ n, (∀ k, k < n → L.BalancesOn W [c] (T + k)) →
      (∀ k, k < n → W.level T c ≤ W.level (T + k) c → L.taken (T + k) c < L.given (T + k) c) →
      W.level T c + n ≤ W.level (T + n) c
  | 0, _, _ => Nat.le_refl _
  | n + 1, balances, netGive =>
    have before := net_give_bounded_at n (fun k below => balances k (Nat.lt_succ_of_lt below))
      fun k below => netGive k (Nat.lt_succ_of_lt below)
    Nat.le_trans (Nat.add_le_add_right before 1)
      (net_give_raises_at (balances n (Nat.lt_succ_self n))
        (netGive n (Nat.lt_succ_self n) (Nat.le_trans (Nat.le_add_right _ n) before)))

/-- The law of restoration: from level `W.level T c`, after `m - W.level T c` steps with
balance at the condition and joint net giving wherever the level is not below where it was at
`T`, the level is at least `m`. -/
theorem restores_at {c : C} {m T : Nat}
    (balances : ∀ k, k < m - W.level T c → L.BalancesOn W [c] (T + k))
    (netGive : ∀ k, k < m - W.level T c → W.level T c ≤ W.level (T + k) c →
      L.taken (T + k) c < L.given (T + k) c) :
    m ≤ W.level (T + (m - W.level T c)) c :=
  Nat.le_trans (Nat.le_trans (Nat.le_add_right m (W.level T c - m))
      (Nat.le_of_eq (add_sub_turn m (W.level T c)).symm))
    (net_give_bounded_at _ balances netGive)

/-- The law of restoration under balance. -/
theorem restores (balances : L.Balances W) {c : C} {m T : Nat}
    (netGive : ∀ k, k < m - W.level T c → W.level T c ≤ W.level (T + k) c →
      L.taken (T + k) c < L.given (T + k) c) :
    m ≤ W.level (T + (m - W.level T c)) c :=
  restores_at (fun k _ => balances.on [c] (T + k)) netGive

end Joint

/-! ## Renewal that depends on what it renews -/

section Gated

variable {L : Flow F C} {W : Web F C}

/-- Once below `m`, below `m` over the next `n` steps, where across each of them the
condition is balanced on and whatever gives to it depends on it at a need of at least `m`
and is supported. -/
theorem stays_below_at {c : C} {m T : Nat} (below : W.level T c < m) :
    ∀ n, (∀ k, k < n → L.BalancesOn W [c] (T + k)) →
      (∀ k f, k < n → f ∈ L.present (T + k) → 0 < L.give (T + k) f c →
        W.requires (T + k) f c ∧ m ≤ W.need (T + k) f c) →
      (∀ k, k < n → L.GiversSupported W (T + k) c) →
      W.level (T + n) c < m
  | 0, _, _, _ => below
  | n + 1, balances, gated, givers =>
    have before := stays_below_at below n (fun k lt => balances k (Nat.lt_succ_of_lt lt))
      (fun k f lt => gated k f (Nat.lt_succ_of_lt lt))
      fun k lt => givers k (Nat.lt_succ_of_lt lt)
    have none : L.given (T + n) c = 0 := total_eq_zero fun f present =>
      eq_zero_of_not_pos fun gives => match gated n f (Nat.lt_succ_self n) present gives with
        | ⟨depends, high⟩ =>
          Nat.lt_irrefl m (Nat.lt_of_le_of_lt (Nat.le_trans high
            (givers n (Nat.lt_succ_self n) f present gives c depends)) before)
    Nat.lt_of_le_of_lt
      (Nat.le_trans (Nat.le_add_right _ (L.taken (T + n) c))
        (Nat.le_of_eq (((balances n (Nat.lt_succ_self n)) c (.head [])).trans
          (congrArg (W.level (T + n) c + ·) none))))
      before

/-- Once below `m`, always below `m`: where every formation giving to the condition
depends on it at a need of at least `m`, only active formations give and activity needs
support, nothing gives to the condition while its level is below `m`, so the level stays
below `m`. -/
theorem stays_below (balances : L.Balances W) (acting : L.Acting W)
    (dependent : W.Dependent) {c : C} {m : Nat}
    (gated : ∀ t f, f ∈ L.present t → 0 < L.give t f c →
      W.requires t f c ∧ m ≤ W.need t f c)
    {T : Nat} (below : W.level T c < m) : ∀ n, W.level (T + n) c < m :=
  fun n => stays_below_at below n (fun k _ => balances.on [c] (T + k))
    (fun k f _ => gated (T + k) f) fun k _ => acting.giversSupported dependent (T + k) c

/-- At one step, a formation depending on a condition below its need is not active there,
where it is active only while supported. -/
theorem ends_below_at {c : C} {m t : Nat} {g : F}
    (dependent : W.active t g → W.Supported t g) (below : W.level t c < m)
    (depends : W.requires t g c) (high : m ≤ W.need t g c) : ¬ W.active t g :=
  fun active => Nat.lt_irrefl m (Nat.lt_of_le_of_lt
    (Nat.le_trans high (dependent active c depends)) below)

/-- Below `m` from `T` on, every formation depending on the condition at a need of at least
`m` is inactive. -/
theorem ends_below (dependent : W.Dependent) {c : C} {m T : Nat}
    (below : ∀ n, W.level (T + n) c < m) :
    ∀ n g, W.requires (T + n) g c → m ≤ W.need (T + n) g c → ¬ W.active (T + n) g :=
  fun n g => ends_below_at (dependent (T + n) g) (below n)

/-- Joint excess ends gated renewal, at the steps it uses: with balance at the condition
across the first `n + k` steps from `T`, whatever gives to it there depending on it at a need
of at least `m` and supported, `n` steps of joint excess from `T` starting below `n + m`
leave a formation depending on it at a need of at least `m` inactive at step `T + n + k`,
where it is active only while supported. -/
theorem joint_excess_ends_at {c : C} {m T n k : Nat} {g : F}
    (balances : ∀ j, j < n + k → L.BalancesOn W [c] (T + j))
    (gated : ∀ j f, j < n + k → f ∈ L.present (T + j) → 0 < L.give (T + j) f c →
      W.requires (T + j) f c ∧ m ≤ W.need (T + j) f c)
    (givers : ∀ j, j < n + k → L.GiversSupported W (T + j) c)
    (excess : ∀ j, j < n → L.given (T + j) c < L.taken (T + j) c)
    (start : W.level T c < n + m)
    (dependent : W.active (T + n + k) g → W.Supported (T + n + k) g) :
    W.requires (T + n + k) g c → m ≤ W.need (T + n + k) g c → ¬ W.active (T + n + k) g :=
  have early : ∀ j, j < n → j < n + k := fun _ below => Nat.lt_of_lt_of_le below (Nat.le_add_right n k)
  have shift : ∀ j, j < k → n + j < n + k := fun _ below => Nat.add_lt_add_left below n
  have low : W.level (T + n) c < m := Nat.lt_of_add_lt_add_left (n := n)
    (Nat.lt_of_le_of_lt
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm n _))
        (excess_bounded_at n (fun j below => balances j (early j below)) excess))
      start)
  ends_below_at dependent (stays_below_at (T := T + n) low k
    (fun j below => Eq.subst (motive := fun s => L.BalancesOn W [c] s) (Nat.add_assoc T n j).symm
      (balances (n + j) (shift j below)))
    (fun j f below => Eq.subst (motive := fun s => f ∈ L.present s → 0 < L.give s f c →
        W.requires s f c ∧ m ≤ W.need s f c) (Nat.add_assoc T n j).symm
      (gated (n + j) f (shift j below)))
    fun j below => Eq.subst (motive := fun s => L.GiversSupported W s c)
      (Nat.add_assoc T n j).symm (givers (n + j) (shift j below)))

/-- Joint excess ends gated renewal: if `n` consecutive steps of joint excess from `T`
start below `n + m`, the level is below `m` from `T + n` on, nothing gives to the
condition again, and every formation depending on it at a need of at least `m` is
inactive from then on, the takers included. -/
theorem joint_excess_ends (balances : L.Balances W) (acting : L.Acting W)
    (dependent : W.Dependent) {c : C} {m : Nat}
    (gated : ∀ t f, f ∈ L.present t → 0 < L.give t f c →
      W.requires t f c ∧ m ≤ W.need t f c)
    {T n : Nat} (excess : ∀ k, k < n → L.given (T + k) c < L.taken (T + k) c)
    (start : W.level T c < n + m) :
    ∀ k g, W.requires (T + n + k) g c → m ≤ W.need (T + n + k) g c →
      ¬ W.active (T + n + k) g :=
  fun k g => joint_excess_ends_at (fun j _ => balances.on [c] (T + j))
    (fun j f _ => gated (T + j) f) (fun j _ => acting.giversSupported dependent (T + j) c)
    excess start (dependent (T + n + k) g)

end Gated

end Flow

/-! ## Read with one kind of relatum: generation is fed from beyond -/

namespace Web

variable {X : Type} {W : Web X X} {L : Flow X X}

/-- Under dissipation, a finite family without repetition in which embodied members arise
at arbitrarily late steps, enclosed around from some step on, cannot from any step on be
fed from nothing beyond it. -/
theorem embodiedArising_fed_from_beyond [DecidableEq X] (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List X} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (arising : ∀ N, ∃ t x, N ≤ t ∧ x ∈ ds ∧ W.Embodied x ∧ W.Arises t x) (N : Nat) :
    ¬ ∀ t, N ≤ t → ¬ L.FedFromBeyond ds t :=
  Flow.fed_of_not_inward (embodiedArising_draws_in balances dissipative distinct around arising N)

end Web

/-! ## Being fed is needed; no condition it is fed from need recur -/

namespace Lone

open Frontier (Condition burning)

/-- The pool is fed from beyond at every step: the source conveys from the step's fuel. -/
theorem fed (t : Nat) : flow.FedFromBeyond [.pool] t :=
  ⟨.fuel t, .pool, (fun mem => match mem with | .tail _ no => nomatch no),
   .head _, .source, .head _,
   show 0 < 2 * burning t t from
     Eq.subst (motive := fun b => 0 < 2 * b) (Frontier.burning_self t).symm (Nat.succ_pos 1),
   Nat.zero_lt_one⟩

/-- Each fuel is conveyed from at one step only, its own. -/
theorem each_fuel_once {n t : Nat} {d : Condition} (conveys : flow.Conveys t (.fuel n) d) :
    n = t :=
  match conveys with
  | ⟨f, _, takes, _⟩ => match f, takes with
    | .source, takes => Frontier.burning_at n t (match h : burning n t with
      | 0 => absurd (Eq.subst (motive := fun b => 0 < 2 * b) h takes) (Nat.lt_irrefl 0)
      | k + 1 => Nat.succ_pos k)
    | .eater, takes => absurd takes (Nat.lt_irrefl 0)

/-- So in a balanced, dissipative flow whose takers recur, the pool is fed at every step,
while no fuel is conveyed from after its step. -/
theorem fed_not_recurring :
    flow.Balances web ∧ flow.Dissipative ∧ (∀ t, flow.FedFromBeyond [.pool] t) ∧
      ∀ n t, n < t → ∀ d, ¬ flow.Conveys t (.fuel n) d :=
  ⟨balances, dissipative, fed, fun _ _ before _ conveys =>
    Nat.lt_irrefl _ (Eq.subst (motive := fun m => m < _) (each_fuel_once conveys) before)⟩

end Lone

/-! ## Witnesses -/

namespace Pair

/-- Two formations each take one unit from one condition at every step; one of them gives
it one unit back. -/
def flow : Flow Bool Unit :=
  ⟨fun _ => [true, false], fun _ _ _ => 1, fun _ f _ => match f with
    | true => 1
    | false => 0⟩

/-- Each takes within what the step gives; together they take more. -/
theorem own_not_joint (t : Nat) : flow.WithinOwn t () ∧ ¬ flow.WithinJoint t () :=
  ⟨fun _ _ => Nat.le_refl 1, fun within => Nat.not_succ_le_self 1 within⟩

/-- So no web balances it: the joint excess cannot go on. -/
theorem no_web : ¬ ∃ W : Web Bool Unit, flow.Balances W :=
  fun ⟨W, balances⟩ =>
    Nat.not_succ_le_self (W.level 0 ())
      (Nat.le_trans (Nat.le_add_left _ (W.level (0 + (W.level 0 () + 1)) ()))
        (Flow.excess_bounded balances (W.level 0 () + 1) fun _ _ => Nat.lt_succ_self 1))

end Pair

namespace Exceeding

/-- A renewer and two takers share one condition. -/
inductive Member where
  | renewer
  | first
  | second

def level : Nat → Nat
  | 0 => 4
  | 1 => 2
  | _ + 2 => 0

def live : Nat → Prop
  | 0 => True
  | 1 => True
  | _ + 2 => False

def present : Nat → List Member
  | 0 => [.renewer, .first, .second]
  | 1 => [.renewer, .first, .second]
  | _ + 2 => []

/-- The renewer gives two units and each taker takes two, while they take part. -/
def flow : Flow Member Unit where
  present := present
  take _ f _ := match f with
    | .renewer => 0
    | .first => 2
    | .second => 2
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0

/-- Each depends on the condition at need one, the renewer included. -/
def web : Web Member Unit where
  level t _ := level t
  active t _ := live t
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => True

theorem balances : flow.Balances web
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem live_of_present : ∀ t f, f ∈ present t → live t
  | 0, _, _ => trivial
  | 1, _, _ => trivial
  | _ + 2, _, no => nomatch no

theorem acting : flow.Acting web :=
  fun t f _ present _ => live_of_present t f present

theorem dependent : web.Dependent
  | 0, _, _, _, _ => Nat.succ_le_succ (Nat.zero_le 3)
  | 1, _, _, _, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | _ + 2, _, dead, _, _ => nomatch dead

/-- Only the renewer gives, and it depends on the condition at need one. -/
theorem gated : ∀ t f, f ∈ flow.present t → 0 < flow.give t f () →
    web.requires t f () ∧ 1 ≤ web.need t f () :=
  fun _ _ _ _ => ⟨trivial, Nat.le_refl 1⟩

/-- While they take part, each taker takes within what the step gives, and together they
take more. -/
theorem own_not_joint : ∀ t, t < 2 → flow.WithinOwn t () ∧ ¬ flow.WithinJoint t ()
  | 0, _ => ⟨fun f _ => match f with
      | .renewer => Nat.zero_le 2
      | .first => Nat.le_refl 2
      | .second => Nat.le_refl 2,
    fun within => Nat.not_succ_le_self 2 (Nat.le_trans (Nat.le_succ 3) (show 4 ≤ 2 from within))⟩
  | 1, _ => ⟨fun f _ => match f with
      | .renewer => Nat.zero_le 2
      | .first => Nat.le_refl 2
      | .second => Nat.le_refl 2,
    fun within => Nat.not_succ_le_self 2 (Nat.le_trans (Nat.le_succ 3) (show 4 ≤ 2 from within))⟩
  | _ + 2, late => absurd late (Nat.not_lt_of_le (Nat.le_add_left 2 _))

/-- So the renewal ends and every member ends with it, the renewer and both takers: from
step two on nothing is active. The stipulated activity says so; derived here through the
law of gated renewal, the witness shows the law's hypotheses hold with that ending. -/
theorem all_end : ∀ n f, ¬ web.active (2 + n) f :=
  fun n f => Flow.ends_below (W := web) (c := ()) (m := 1) (T := 2) dependent
    (Flow.stays_below balances acting dependent gated (T := 2) Nat.zero_lt_one) n f
    trivial (Nat.le_refl 1)

end Exceeding

namespace Alone

/-- The same renewer with one taker. -/
def flow : Flow Exceeding.Member Unit where
  present _ := [.renewer, .first]
  take _ f _ := match f with
    | .renewer => 0
    | .first => 2
    | .second => 0
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0

def web : Web Exceeding.Member Unit where
  level _ _ := 4
  active _ f := match f with
    | .renewer => True
    | .first => True
    | .second => False
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => False

theorem balances : flow.Balances web := fun _ _ => rfl

theorem dependent : web.Dependent :=
  fun _ _ _ _ _ => Nat.succ_le_succ (Nat.zero_le 3)

/-- The taker takes jointly within what is given, and the renewer and the taker are active
at every step. -/
theorem all_continue :
    flow.Balances web ∧ web.Dependent ∧ (∀ t, flow.WithinJoint t ()) ∧
      ∀ t, web.active t .renewer ∧ web.active t .first :=
  ⟨balances, dependent, fun _ => Nat.le_refl 2, fun _ => ⟨trivial, trivial⟩⟩

end Alone

namespace Downstream

inductive Formation where
  | self
  | down

inductive Condition where
  | ground
  | output

def outputLevel : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 1
  | 3 => 1
  | _ + 4 => 0

def downLive : Nat → Prop
  | 0 => True
  | 1 => True
  | 2 => True
  | 3 => True
  | _ + 4 => False

/-- The self gives the output one unit for three steps; the downstream formation takes one
unit of it while it is active. -/
def present : Nat → List Formation
  | 0 => [.self, .down]
  | 1 => [.self, .down]
  | 2 => [.self, .down]
  | 3 => [.down]
  | _ + 4 => []

def flow : Flow Formation Condition where
  present := present
  take _ f c := match f, c with
    | .self, _ => 0
    | .down, .ground => 0
    | .down, .output => 1
  give _ f c := match f, c with
    | .self, .ground => 0
    | .self, .output => 1
    | .down, _ => 0

/-- The self depends on its ground, the downstream formation on the output. -/
def web : Web Formation Condition where
  level t c := match c with
    | .ground => 1
    | .output => outputLevel t
  active t f := match f with
    | .self => True
    | .down => downLive t
  requires _ f c := match f, c with
    | .self, .ground => True
    | .self, .output => False
    | .down, .ground => False
    | .down, .output => True
  need _ _ _ := 1
  draws _ f c := match f, c with
    | .self, _ => False
    | .down, .ground => False
    | .down, .output => True

theorem balances : flow.Balances web
  | 0, .ground => rfl
  | 0, .output => rfl
  | 1, .ground => rfl
  | 1, .output => rfl
  | 2, .ground => rfl
  | 2, .output => rfl
  | 3, .ground => rfl
  | 3, .output => rfl
  | _ + 4, .ground => rfl
  | _ + 4, .output => rfl

theorem dependent : web.Dependent
  | _, .self, _, .ground, _ => Nat.le_refl 1
  | _, .self, _, .output, no => nomatch no
  | _, .down, _, .ground, no => nomatch no
  | 0, .down, _, .output, _ => Nat.le_refl 1
  | 1, .down, _, .output, _ => Nat.le_refl 1
  | 2, .down, _, .output, _ => Nat.le_refl 1
  | 3, .down, _, .output, _ => Nat.le_refl 1
  | _ + 4, .down, dead, .output, _ => nomatch dead

/-- The derived extent runs one way. The self's continuation requires only its ground, and
the self is active and supported at every step; the formation living on what the self
gives ends once the self stops giving. -/
theorem one_way :
    flow.Balances web ∧ web.Dependent ∧ (∀ t c, web.requires t .self c → c = .ground) ∧
      (∀ t, web.active t .self ∧ web.Supported t .self) ∧
      ∀ n, ¬ web.active (n + 4) .down :=
  ⟨balances, dependent,
   fun _ c depends => match c, depends with | .ground, _ => rfl,
   fun t => ⟨trivial, dependent t .self trivial⟩,
   fun _ dead => dead⟩

end Downstream

namespace Mortal

/-- A renewer, a successor and a formation whose life is two steps. -/
inductive Member where
  | renewer
  | successor
  | mortal

def level : Nat → Nat
  | 0 => 3
  | 1 => 2
  | 2 => 1
  | _ + 3 => 0

def present : Nat → List Member
  | 0 => [.renewer, .successor, .mortal]
  | 1 => [.renewer, .successor, .mortal]
  | 2 => [.successor]
  | _ + 3 => []

/-- The renewer gives one unit; the successor and the mortal formation each take one. -/
def flow : Flow Member Unit where
  present := present
  take _ f _ := match f with
    | .renewer => 0
    | .successor => 1
    | .mortal => 1
  give _ f _ := match f with
    | .renewer => 1
    | .successor => 0
    | .mortal => 0

def live : Nat → Member → Prop
  | 0, _ => True
  | 1, _ => True
  | 2, .renewer => False
  | 2, .successor => True
  | 2, .mortal => False
  | _ + 3, _ => False

/-- The renewer depends on the condition at need two, the successor and the mortal formation at
need one. -/
def web : Web Member Unit where
  level t _ := level t
  active := live
  requires _ _ _ := True
  need _ f _ := match f with
    | .renewer => 2
    | .successor => 1
    | .mortal => 1
  draws _ f _ := match f with
    | .renewer => False
    | .successor => True
    | .mortal => True

theorem balances : flow.Balances web
  | 0, () => rfl
  | 1, () => rfl
  | 2, () => rfl
  | _ + 3, () => rfl

theorem dependent : web.Dependent
  | 0, .renewer, _, _, _ => Nat.succ_le_succ (Nat.succ_le_succ (Nat.zero_le 1))
  | 0, .successor, _, _, _ => Nat.succ_le_succ (Nat.zero_le 2)
  | 0, .mortal, _, _, _ => Nat.succ_le_succ (Nat.zero_le 2)
  | 1, .renewer, _, _, _ => Nat.le_refl 2
  | 1, .successor, _, _, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | 1, .mortal, _, _, _ => Nat.succ_le_succ (Nat.zero_le 1)
  | 2, .renewer, dead, _, _ => nomatch dead
  | 2, .successor, _, _, _ => Nat.le_refl 1
  | 2, .mortal, dead, _, _ => nomatch dead
  | _ + 3, _, dead, _, _ => nomatch dead

/-- The horizon of a want: the mortal formation's dependence is met at every step of its
life, and its taking ends the renewal of the condition; the successor, depending on the
condition, ends after the mortal formation has ended. -/
theorem after_its_end :
    flow.Balances web ∧ web.Dependent ∧
      (∀ t, web.active t .mortal → web.Supported t .mortal) ∧
      ¬ web.active 2 .mortal ∧ web.active 2 .successor ∧ ¬ web.active 2 .renewer ∧
      ∀ n f, ¬ web.active (n + 3) f :=
  ⟨balances, dependent, fun t active => dependent t .mortal active,
   fun dead => dead, trivial, fun dead => dead,
   fun _ _ dead => dead⟩

/-- Without the mortal formation the renewer and the successor continue at every step. -/
def without : Flow Member Unit where
  present _ := [.renewer, .successor]
  take _ f _ := match f with
    | .renewer => 0
    | .successor => 1
    | .mortal => 0
  give _ f _ := match f with
    | .renewer => 1
    | .successor => 0
    | .mortal => 0

def kept : Web Member Unit where
  level _ _ := 3
  active _ f := match f with
    | .renewer => True
    | .successor => True
    | .mortal => False
  requires _ _ _ := True
  need _ f _ := match f with
    | .renewer => 2
    | .successor => 1
    | .mortal => 1
  draws _ f _ := match f with
    | .renewer => False
    | .successor => True
    | .mortal => False

theorem without_continues :
    without.Balances kept ∧ kept.Dependent ∧
      ∀ t, kept.active t .renewer ∧ kept.active t .successor :=
  ⟨fun _ _ => rfl,
   fun _ f _ _ _ => match f with
    | .renewer => Nat.succ_le_succ (Nat.succ_le_succ (Nat.zero_le 1))
    | .successor => Nat.succ_le_succ (Nat.zero_le 2)
    | .mortal => Nat.succ_le_succ (Nat.zero_le 2),
   fun _ => ⟨trivial, trivial⟩⟩

end Mortal


end Becoming

/-! ## What feeds what (moved from `Becoming.Standpoints`) -/

namespace Becoming

namespace Flow

section Feeding

variable {F C : Type} (L : Flow F C) (W : Web F C)

/-- The continuation of `e`'s formation is fed by `e'`: at their common step, `e'`'s
formation takes part and gives to a condition `e`'s formation requires. -/
def FedBy (e e' : F × Nat) : Prop :=
  e.2 = e'.2 ∧ ∃ c, W.requires e.2 e.1 c ∧ e'.1 ∈ L.present e'.2 ∧ 0 < L.give e'.2 e'.1 c

end Feeding

end Flow

end Becoming
