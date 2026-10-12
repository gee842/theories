import Becoming.Resolution

/-!
# Units: the laws of one step at a finer unit

The spine counts amounts in natural numbers of one unit. The zero-premise plan lists that unit
as a commitment of the representation and asks which laws survive amounts finer than it
(Ren's step 4). `Becoming.Resolution` reads a world at a unit that splits into `r t` finer
units across the step from `t` (`Flow.BalancesAt`); this module states the laws of one step
of `Becoming.Locality` at such a unit, with balance made local to a family and a step
(`Flow.BalancesAtOn`), and reads change in the unit: across the step a condition rises when
its level after it exceeds `r t` times its level before (`Web.RisesAt`), and falls when it is
below (`Web.FallsAt`). With `r` constantly one each is the spine's notion
(`Flow.balancesAtOn_one`, `Web.risesAt_one`, `Web.fallsAt_one`). This is a test of a
commitment of the representation, not a new premise.

* **Arising needs an active giver survives at every resolution.** Coming to stand and ceasing
  to stand do not depend on the unit: zero is zero in every unit. With balance at a condition
  at resolution `r`, it comes to stand exactly when it stood at nothing and was given more
  than was taken from it, and ceases to stand exactly when it stood and what was taken from it
  is all it had, counted in the finer unit, with all it was given
  (`Flow.BalancesAtOn.comesToStand_iff`, `Flow.BalancesAtOn.ceasesToStand_iff`). A rise in the
  unit is given to and a fall in the unit taken from (`Flow.BalancesAtOn.rise_given`,
  `Flow.BalancesAtOn.fall_taken`); where nothing is taken from a family balanced on, a member
  rises in the unit exactly when something taking part gives to it
  (`Flow.BalancesAtOn.rises_iff_gives`), which dissipation on the family excludes
  (`Flow.DissipatesOn.still_untaken_at`). An embodied relatum arises only as an active giver
  other than itself gives to it (`Flow.BalancesAtOn.arises_given`), and nothing comes to stand
  from nothing (`Flow.BalancesAtOn.comes_from_standing`). No condition on `r` is used.
* **The law of one exchange survives with change read in the unit.** Across a step at which a
  family holding what stands is balanced at resolution `r` and dissipated on
  (`Flow.RunsDownOnAt`), some condition rises or falls in the unit exactly when the family's
  total after the step is below `r t` times its total before (`Flow.RunsDownOnAt.changes_iff`).
* **Read in raw counts it fails.** A unit splitting in two with nothing exchanged doubles every
  level: every condition rises in raw counts, while nothing changes in the unit and the total
  does not fall (`Doubling.raw_reading_fails`). So the law of one exchange is a law of change
  in the unit.
* **What is cited, not reproved.** Ceasing needs arising (law 2) concerns what holds, not
  amounts, so it survives as stated. The recurrence of law 1 and the bound of law 3 use the
  least difference in a fixed unit: at a refining unit they fail where the refinement feeds
  the standing, and hold with the refinement counted as a giving (`Becoming.Resolution`:
  `World.rests_unrefuted_refinement_counted`, `World.arising_opens_refinement_counted`) or with the
  unit fixed from some step on (`Flow.taking_not_recurring`).

Not done here: the local laws of dependence, reserve and support at a finer unit, which need a
convention for the unit in which a need is counted.
-/

namespace Becoming

variable {F C : Type}

namespace Flow

variable (L : Flow F C)

/-- At resolution `r`, the flow balances on a family across the step from `t`: each
member's level after the step, with what is taken from it, is `r t` times its level before,
with what is given to it. -/
def BalancesAtOn (r : Nat → Nat) (W : Web F C) (cs : List C) (t : Nat) : Prop :=
  ∀ c, c ∈ cs → W.level (t + 1) c + L.taken t c = r t * W.level t c + L.given t c

variable {L} {W : Web F C} {r : Nat → Nat}

/-- Balance at a resolution is balance at it on every family across every step. -/
theorem BalancesAt.on (balances : L.BalancesAt r W) (cs : List C) (t : Nat) :
    L.BalancesAtOn r W cs t :=
  fun c _ => balances t c

/-- With a fixed unit, balance at a step at that resolution is the spine's balance at the
step. -/
theorem balancesAtOn_one {cs : List C} {t : Nat} :
    L.BalancesAtOn (fun _ => 1) W cs t ↔ L.BalancesOn W cs t :=
  ⟨fun on c mem => (on c mem).trans (congrArg (· + L.given t c) (Nat.one_mul _)),
   fun on c mem => (on c mem).trans (congrArg (· + L.given t c) (Nat.one_mul _)).symm⟩

/-- Balanced on a family at resolution `r`, the stock after the step with its uptake is `r t`
times the stock before with its replenishment. -/
theorem BalancesAtOn.over : ∀ {cs : List C} {t : Nat}, L.BalancesAtOn r W cs t →
    W.stock cs (t + 1) + L.uptake cs t = r t * W.stock cs t + L.replenishment cs t
  | [], _, _ => rfl
  | c :: cs, t, balances =>
    (Nat.add_add_add_comm (W.level (t + 1) c) (W.stock cs (t + 1)) (L.taken t c)
      (L.uptake cs t)).trans
    ((congrArg (· + (W.stock cs (t + 1) + L.uptake cs t)) (balances c (.head cs))).trans
    ((congrArg (r t * W.level t c + L.given t c + ·)
        (BalancesAtOn.over fun d mem => balances d (.tail c mem))).trans
    ((Nat.add_add_add_comm (r t * W.level t c) (L.given t c) (r t * W.stock cs t)
      (L.replenishment cs t)).trans
     (congrArg (· + (L.given t c + L.replenishment cs t))
       (Nat.left_distrib (r t) (W.level t c) (W.stock cs t)).symm))))

/-- Balanced and dissipated on at resolution `r`, the family's stock after the step with its
takers is at most `r t` times its stock before. -/
theorem BalancesAtOn.lowers {cs : List C} {t : Nat} (balances : L.BalancesAtOn r W cs t)
    (dissipates : L.DissipatesOn cs t) : W.stock cs (t + 1) + L.takers cs t ≤ r t * W.stock cs t :=
  le_of_add_le_add_right (L.replenishment cs t) (Nat.le_trans
    (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
      (congrArg (W.stock cs (t + 1) + ·) (Nat.add_comm (L.takers cs t) (L.replenishment cs t)))))
    (Nat.le_trans (Nat.add_le_add_left dissipates.replenishment_takers _)
      (Nat.le_of_eq balances.over)))

end Flow

namespace Web

variable (W : Web F C) (r : Nat → Nat)

/-- Read in a unit splitting into `r t` across the step from `t`, `c` rises: its level after
the step exceeds `r t` times its level before. -/
def RisesAt (t : Nat) (c : C) : Prop :=
  r t * W.level t c < W.level (t + 1) c

/-- And falls: its level after the step is below `r t` times its level before. -/
def FallsAt (t : Nat) (c : C) : Prop :=
  W.level (t + 1) c < r t * W.level t c

variable {W}

/-- With a fixed unit, a rise in the unit is a rise. -/
theorem risesAt_one {t : Nat} {c : C} : W.RisesAt (fun _ => 1) t c ↔ W.Rises t c :=
  ⟨fun rises => Nat.lt_of_le_of_lt (Nat.le_of_eq (Nat.one_mul _).symm) rises,
   fun rises => Nat.lt_of_le_of_lt (Nat.le_of_eq (Nat.one_mul _)) rises⟩

/-- And a fall in the unit is a fall. -/
theorem fallsAt_one {t : Nat} {c : C} : W.FallsAt (fun _ => 1) t c ↔ W.Falls t c :=
  ⟨fun falls => Nat.lt_of_lt_of_le falls (Nat.le_of_eq (Nat.one_mul _)),
   fun falls => Nat.lt_of_lt_of_le falls (Nat.le_of_eq (Nat.one_mul _).symm)⟩

end Web

/-! ## Arising needs an active giver, at every resolution -/

namespace Flow

variable {L : Flow F C} {W : Web F C} {r : Nat → Nat} {cs : List C} {t : Nat} {c : C}

/-- With balance at `c` at resolution `r`, `c` comes to stand across the step exactly when it
stood at nothing and was given more than was taken from it. -/
theorem BalancesAtOn.comesToStand_iff (balances : L.BalancesAtOn r W cs t) (mem : c ∈ cs) :
    W.ComesToStand t c ↔ W.level t c = 0 ∧ L.taken t c < L.given t c :=
  have fed : W.level t c = 0 → W.level (t + 1) c + L.taken t c = L.given t c := fun zero =>
    (balances c mem).trans ((congrArg (fun l => r t * l + L.given t c) zero).trans
      ((congrArg (· + L.given t c) (Nat.mul_zero (r t))).trans (Nat.zero_add _)))
  ⟨fun comes => ⟨eq_zero_of_not_pos comes.1,
      (pos_iff_lt (fed (eq_zero_of_not_pos comes.1))).mp comes.2⟩,
   fun ⟨zero, more⟩ => ⟨fun pos => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq zero)),
      (pos_iff_lt (fed zero)).mpr more⟩⟩

/-- With balance at `c` at resolution `r`, `c` ceases to stand across the step exactly when it
stood and what was taken from it is all it had, counted in the finer unit, with all it was
given. -/
theorem BalancesAtOn.ceasesToStand_iff (balances : L.BalancesAtOn r W cs t) (mem : c ∈ cs) :
    W.CeasesToStand t c ↔ 0 < W.level t c ∧ L.taken t c = r t * W.level t c + L.given t c :=
  ⟨fun ceases => ⟨ceases.1, (Nat.zero_add _).symm.trans
      ((congrArg (· + L.taken t c) (eq_zero_of_not_pos ceases.2)).symm.trans (balances c mem))⟩,
   fun ⟨stands, all⟩ => ⟨stands, fun pos => Nat.lt_irrefl (L.taken t c)
      (Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right pos)
        (Nat.le_of_eq ((Nat.add_comm _ _).trans ((balances c mem).trans all.symm))))⟩⟩

/-- With balance at `c` at resolution `r`, a rise of `c` in the unit is given to. -/
theorem BalancesAtOn.rise_given (balances : L.BalancesAtOn r W cs t) (mem : c ∈ cs)
    (rises : W.RisesAt r t c) : 0 < L.given t c :=
  Nat.pos_of_ne_zero fun nothing => Nat.not_le_of_gt rises
    (Nat.le_trans (Nat.le_add_right _ (L.taken t c))
      (Nat.le_of_eq ((balances c mem).trans (congrArg (r t * W.level t c + ·) nothing))))

/-- With balance at `c` at resolution `r`, a fall of `c` in the unit is taken from. -/
theorem BalancesAtOn.fall_taken (balances : L.BalancesAtOn r W cs t) (mem : c ∈ cs)
    (falls : W.FallsAt r t c) : 0 < L.taken t c :=
  Nat.pos_of_ne_zero fun nothing => Nat.not_le_of_gt falls
    (Nat.le_trans (Nat.le_add_right _ (L.given t c))
      (Nat.le_of_eq ((balances c mem).symm.trans (congrArg (W.level (t + 1) c + ·) nothing))))

/-- Across a step at which nothing is taken from a family balanced on at resolution `r`, a
member rises in the unit exactly when some formation taking part gives to the family. -/
theorem BalancesAtOn.rises_iff_gives (balances : L.BalancesAtOn r W cs t)
    (untaken : ∀ c, c ∈ cs → L.taken t c = 0) :
    (∃ c, c ∈ cs ∧ W.RisesAt r t c) ↔ ∃ f c, f ∈ L.present t ∧ c ∈ cs ∧ 0 < L.give t f c :=
  have up : ∀ c, c ∈ cs → W.level (t + 1) c = r t * W.level t c + L.given t c := fun c mem =>
    (congrArg (W.level (t + 1) c + ·) (untaken c mem)).symm.trans (balances c mem)
  ⟨fun ⟨c, mem, rises⟩ => match total_pos _ ((lt_iff_pos (up c mem)).mp rises) with
    | ⟨f, present, gives⟩ => ⟨f, c, present, mem, gives⟩,
   fun ⟨_, c, present, mem, gives⟩ => ⟨c, mem, (lt_iff_pos (up c mem)).mpr
      (Nat.lt_of_lt_of_le gives (le_total_of_mem (q := fun f => L.give t f c) present))⟩⟩

/-- So where nothing is taken from a family balanced on at resolution `r` and dissipated on,
no member rises in the unit. -/
theorem DissipatesOn.still_untaken_at (dissipates : L.DissipatesOn cs t)
    (balances : L.BalancesAtOn r W cs t) (untaken : ∀ c, c ∈ cs → L.taken t c = 0) :
    ¬ ∃ c, c ∈ cs ∧ W.RisesAt r t c :=
  fun rising => match (balances.rises_iff_gives untaken).mp rising with
  | ⟨f, _, present, mem, gives⟩ =>
    match total_pos cs (dissipates.takes_of_gives present
        (Nat.lt_of_lt_of_le gives (le_total_of_mem (q := L.give t f) mem))) with
    | ⟨d, inside, takes⟩ => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
        (Nat.lt_of_lt_of_le takes (le_total_of_mem (q := fun f => L.take t f d) present))
        (Nat.le_of_eq (untaken d inside)))

/-- Balanced at resolution `r` and dissipated on, a family a formation taking part takes from
falls in the unit across the step. -/
theorem BalancesAtOn.taking_lowers (balances : L.BalancesAtOn r W cs t)
    (dissipates : L.DissipatesOn cs t) {f : F} (present : f ∈ L.present t)
    (takes : 0 < total cs (L.take t f)) : W.stock cs (t + 1) < r t * W.stock cs t :=
  Nat.lt_of_lt_of_le
    (Nat.lt_add_of_pos_right (total_pos_of_mem (q := fun f => sign (total cs (L.take t f)))
      present (sign_pos takes)))
    (balances.lowers dissipates)

/-- Balanced at resolution `r` and dissipated on, a member's fall in the unit lowers the
family in the unit. -/
theorem BalancesAtOn.fall_lowers (balances : L.BalancesAtOn r W cs t)
    (dissipates : L.DissipatesOn cs t) (mem : c ∈ cs) (falls : W.FallsAt r t c) :
    W.stock cs (t + 1) < r t * W.stock cs t :=
  match total_pos (L.present t) (balances.fall_taken mem falls) with
  | ⟨_, present, takes⟩ => balances.taking_lowers dissipates present (total_pos_of_mem mem takes)

/-- And so does a member's rise in the unit: it is given to, and what gives to the family
takes from it. -/
theorem BalancesAtOn.rise_lowers (balances : L.BalancesAtOn r W cs t)
    (dissipates : L.DissipatesOn cs t) (mem : c ∈ cs) (rises : W.RisesAt r t c) :
    W.stock cs (t + 1) < r t * W.stock cs t :=
  match total_pos (L.present t) (balances.rise_given mem rises) with
  | ⟨_, present, gives⟩ => balances.taking_lowers dissipates present
      (dissipates.takes_of_gives present (total_pos_of_mem mem gives))

/-- Coming to stand is a rise in every unit: zero times the split is zero. -/
theorem risesAt_of_comesToStand (comes : W.ComesToStand t c) : W.RisesAt r t c :=
  Nat.lt_of_le_of_lt (Nat.le_of_eq ((congrArg (r t * ·) (eq_zero_of_not_pos comes.1)).trans
    (Nat.mul_zero (r t)))) comes.2

/-- Nothing comes to stand from nothing, at every resolution: across a step at which a family
is balanced at resolution `r` and dissipated on, a member comes to stand only where the family
stood at something before. -/
theorem BalancesAtOn.comes_from_standing (balances : L.BalancesAtOn r W cs t)
    (dissipates : L.DissipatesOn cs t) (mem : c ∈ cs) (comes : W.ComesToStand t c) :
    0 < W.stock cs t :=
  Nat.pos_of_ne_zero fun zero => Nat.lt_irrefl 0 (Nat.lt_of_le_of_lt (Nat.zero_le _)
    (Nat.lt_of_lt_of_le (balances.rise_lowers dissipates mem (risesAt_of_comesToStand comes))
      (Nat.le_of_eq ((congrArg (r t * ·) zero).trans (Nat.mul_zero (r t))))))

section Relata

variable {X : Type} {L : Flow X X} {W : Web X X} {r : Nat → Nat} {xs : List X} {t : Nat} {x : X}

/-- Arising needs an active giver, at every resolution: with balance at resolution `r` at a
relatum embodied at both ends of the step, where only active formations give to it, an arising
relatum is given to by an active formation taking part, another than itself. -/
theorem BalancesAtOn.arises_given (balances : L.BalancesAtOn r W xs t) (mem : x ∈ xs)
    (before : W.active t x ↔ 0 < W.level t x)
    (after : W.active (t + 1) x ↔ 0 < W.level (t + 1) x)
    (acting : ∀ f, f ∈ L.present t → 0 < L.give t f x → W.active t f) (arises : W.Arises t x) :
    ∃ f, W.active t f ∧ f ∈ L.present t ∧ 0 < L.give t f x ∧ f ≠ x :=
  have comes : W.ComesToStand t x :=
    ⟨fun stands => arises.1 (before.mpr stands), after.mp arises.2⟩
  match total_pos (L.present t) (Nat.lt_of_le_of_lt (Nat.zero_le _)
      ((balances.comesToStand_iff mem).mp comes).2) with
  | ⟨f, present, gives⟩ =>
    have active := acting f present gives
    ⟨f, active, present, gives, fun same => arises.1 (Eq.subst (motive := fun g => W.active t g)
      same active)⟩

end Relata

/-! ## The law of one exchange, with change read in the unit -/

/-- Across the step from `t` the family runs down at resolution `r`: without repetition it
holds whatever stands before or after the step, and the flow balances on it at resolution `r`
and dissipates on it. -/
def RunsDownOnAt (L : Flow F C) (r : Nat → Nat) (W : Web F C) (es : List C) (t : Nat) : Prop :=
  Distinct es ∧ (∀ c, 0 < W.level t c → c ∈ es) ∧ (∀ c, 0 < W.level (t + 1) c → c ∈ es) ∧
    L.BalancesAtOn r W es t ∧ L.DissipatesOn es t

/-- With a fixed unit, running down at that resolution is the spine's running down. -/
theorem runsDownOnAt_one {es : List C} :
    L.RunsDownOnAt (fun _ => 1) W es t ↔ L.RunsDownOn W es t :=
  ⟨fun ⟨distinct, before, after, balances, dissipates⟩ =>
    ⟨distinct, before, after, balancesAtOn_one.mp balances, dissipates⟩,
   fun ⟨distinct, before, after, balances, dissipates⟩ =>
    ⟨distinct, before, after, balancesAtOn_one.mpr balances, dissipates⟩⟩

/-- The law of one exchange at a finer unit: across a step at which the family runs down at
resolution `r`, some condition rises or falls in the unit exactly when the family's total
after the step is below `r t` times its total before. -/
theorem RunsDownOnAt.changes_iff {es : List C} (runs : L.RunsDownOnAt r W es t) :
    (∃ c, W.RisesAt r t c ∨ W.FallsAt r t c) ↔ W.stock es (t + 1) < r t * W.stock es t :=
  match runs with
  | ⟨_, before, after, balances, dissipates⟩ =>
    ⟨fun ⟨c, changes⟩ => match changes with
      | .inl rises => balances.rise_lowers dissipates
          (after c (Nat.lt_of_le_of_lt (Nat.zero_le _) rises)) rises
      | .inr falls => balances.fall_lowers dissipates
          (before c (Nat.pos_of_ne_zero fun zero => Nat.lt_irrefl 0 (Nat.lt_of_le_of_lt
            (Nat.zero_le _) (Nat.lt_of_lt_of_le falls (Nat.le_of_eq
              ((congrArg (r t * ·) zero).trans (Nat.mul_zero (r t)))))))) falls,
     fun lower => match exists_lt_of_total_lt (p := W.level (t + 1))
        (q := fun c => r t * W.level t c)
        (Nat.lt_of_lt_of_le lower (Nat.le_of_eq (total_mul (r t) (W.level t) es).symm)) with
      | ⟨c, _, less⟩ => ⟨c, .inr less⟩⟩

end Flow

/-! ## Read in raw counts, the law of one exchange fails -/

namespace Doubling

/-- One, doubled at each step. -/
def double : Nat → Nat
  | 0 => 1
  | n + 1 => double n + double n

theorem double_pos : ∀ n, 0 < double n
  | 0 => Nat.succ_pos 0
  | n + 1 => Nat.lt_of_lt_of_le (double_pos n) (Nat.le_add_right _ _)

theorem two_mul_eq (n : Nat) : 2 * n = n + n :=
  (Nat.succ_mul 1 n).trans (congrArg (· + n) (Nat.one_mul n))

/-- Nothing takes part. -/
def flow : Flow Unit Unit where
  present _ := []
  take _ _ _ := 0
  give _ _ _ := 0

/-- One condition, standing at one and doubling at each step, as the unit splits in two. -/
def web : Web Unit Unit where
  level t _ := double t
  active _ _ := False
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Across every step the unit splits in two and nothing is exchanged: the family of the one
condition runs down at that resolution. -/
theorem runsDown (t : Nat) : flow.RunsDownOnAt (fun _ => 2) web [()] t :=
  ⟨⟨fun mem => (nomatch mem), trivial⟩, fun _ _ => .head [], fun _ _ => .head [],
   fun _ _ => (two_mul_eq (double t)).symm, fun _ mem => nomatch mem⟩

/-- Read in raw counts the law of one exchange fails: across every step the condition rises
in raw counts, while nothing rises or falls in the unit and the total does not fall in it. -/
theorem raw_reading_fails (t : Nat) :
    web.Rises t () ∧ ¬ (∃ c, web.RisesAt (fun _ => 2) t c ∨ web.FallsAt (fun _ => 2) t c) ∧
      ¬ web.stock [()] (t + 1) < 2 * web.stock [()] t :=
  have even : double (t + 1) = 2 * double t := (two_mul_eq (double t)).symm
  ⟨Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right (double_pos t)) (Nat.le_refl _),
   fun ⟨_, changes⟩ => match changes with
    | .inl rises => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le rises (Nat.le_of_eq even))
    | .inr falls => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le falls (Nat.le_of_eq even.symm)),
   fun lower => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le lower (Nat.le_of_eq even.symm))⟩

end Doubling

/-! ## Need read in the unit -/

/-- The unit factor from step `T` over `k` steps: each step from `T` on splits the unit into
`r` finer units, so a count at `T` is read at `T + k` as this many times itself. -/
def unitFactor (r : Nat → Nat) (T : Nat) : Nat → Nat
  | 0 => 1
  | k + 1 => r (T + k) * unitFactor r T k

/-- With a fixed unit the factor is one. -/
theorem unitFactor_one (T : Nat) : ∀ k, unitFactor (fun _ => 1) T k = 1
  | 0 => rfl
  | k + 1 => (Nat.one_mul _).trans (unitFactor_one T k)

namespace Web

variable {W : Web F C}

/-- Support is unchanged by a pure split: across a step at which the unit splits into `r t > 0`
finer units, where a formation's requirements stay and each need and each required level is
read `r t` times over in the finer unit, it is supported after the step exactly when it was
before. Support compares a need with a level in one unit, so the grain of measurement does not
change it. -/
theorem supported_unchanged_by_split {r : Nat → Nat} {t : Nat} {g : F} (positive : 0 < r t)
    (requires : ∀ c, W.requires (t + 1) g c ↔ W.requires t g c)
    (need : ∀ c, W.requires t g c → W.need (t + 1) g c = r t * W.need t g c)
    (level : ∀ c, W.requires t g c → W.level (t + 1) c = r t * W.level t c) :
    W.Supported (t + 1) g ↔ W.Supported t g :=
  ⟨fun supported c depends => Nat.le_of_mul_le_mul_left
      (Nat.le_trans (Nat.le_of_eq (need c depends).symm) (Nat.le_trans
        (supported c ((requires c).mpr depends)) (Nat.le_of_eq (level c depends)))) positive,
   fun supported c depends =>
      have before := (requires c).mp depends
      Nat.le_trans (Nat.le_of_eq (need c before))
        (Nat.le_trans (Nat.mul_le_mul_left (r t) (supported c before))
          (Nat.le_of_eq (level c before).symm))⟩

/-- A formation supported at `T + k`, with a dependence at least as strong as an earlier one
read in the unit of `T + k`, finds the condition meeting the earlier need read in that unit. -/
theorem continuing_restores_in_unit {r : Nat → Nat} {T k : Nat} {g : F} {c : C}
    (supported : W.Supported (T + k) g) (depends : W.requires (T + k) g c)
    (kept : unitFactor r T k * W.need T g c ≤ W.need (T + k) g c) :
    unitFactor r T k * W.need T g c ≤ W.level (T + k) c :=
  Nat.le_trans kept (supported c depends)

/-- After a loss read in the unit, a formation supported at a later step has weakened or
dissolved its dependence, read in the unit. -/
theorem consumed_continues_transformed_in_unit {r : Nat → Nat} {T k : Nat} {g : F} {c : C}
    (below : W.level (T + k) c < unitFactor r T k * W.need T g c)
    (supported : W.Supported (T + k) g) :
    ¬ (W.requires (T + k) g c ∧ unitFactor r T k * W.need T g c ≤ W.need (T + k) g c) :=
  fun ⟨depends, kept⟩ => Nat.not_le_of_gt below (continuing_restores_in_unit supported depends kept)

/-- A dependence left below its need read in the unit across a step, persisting after it at no
lower need read in the unit, belongs to a formation not active after the step, where it is
active after the step only while supported then. -/
theorem inactive_below_in_unit {r : Nat → Nat} {t : Nat} {g : F} {c : C}
    (dependent : W.active (t + 1) g → W.Supported (t + 1) g)
    (below : W.level (t + 1) c < r t * W.need t g c) (persists : W.requires (t + 1) g c)
    (noLess : r t * W.need t g c ≤ W.need (t + 1) g c) : ¬ W.active (t + 1) g :=
  fun active => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le below
    (Nat.le_trans noLess (dependent active c persists)))

end Web

namespace Flow

variable {L : Flow F C} {W : Web F C} {r : Nat → Nat}

/-- Support is gained from the supported, at every resolution: with balance at the condition at
resolution `r` across the step, a rise in the unit is given by a formation taking part; where
whatever gives to it there is supported, by a supported one. -/
theorem BalancesAtOn.rise_given_by_supported {t : Nat} {c : C}
    (balances : L.BalancesAtOn r W [c] t) (givers : L.GiversSupported W t c)
    (rises : W.RisesAt r t c) : ∃ g, g ∈ L.present t ∧ 0 < L.give t g c ∧ W.Supported t g :=
  match total_pos (L.present t) (balances.rise_given (.head []) rises) with
  | ⟨g, mem, gives⟩ => ⟨g, mem, gives, givers g mem gives⟩

end Flow

/-! ## Counting a loss over a stretch needs a fixed unit -/

namespace Feeding

/-- One formation, taking one finer unit at every step. -/
def flow : Flow Unit Unit where
  present _ := [()]
  take _ _ _ := 1
  give _ _ _ := 0

/-- One condition standing at one, required at need one by the formation, which is always
active. -/
def web : Web Unit Unit where
  level _ _ := 1
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := True

/-- Consumption without a feeder need not end at a finer unit: the unit doubling at every step,
the formation takes one finer unit across every step, nothing gives to the condition, the flow
balances at that resolution and dissipates on the condition, and the formation is active and
supported at every step. With a fixed unit unfed consumption lasts at most as many steps as the
level (`Flow.Balances.unfed_consumption_ends`); here the refinement feeds it, as it feeds the
standing in `Becoming.Resolution`, and counted as a giving (`Flow.withRefinement`) it is the
feeder. -/
theorem endless :
    flow.BalancesAt (fun _ => 2) web ∧ (∀ t, flow.DissipatesOn [()] t) ∧
      (∀ t, web.active t () ∧ 0 < flow.take t () () ∧ flow.given t () = 0) ∧
      ∀ t, web.Supported t () :=
  ⟨fun _ _ => rfl, fun _ _ _ => Nat.le_refl _, fun _ => ⟨trivial, Nat.succ_pos 0, rfl⟩,
   fun _ _ _ => Nat.le_refl 1⟩

end Feeding

end Becoming
