import Becoming.Viability
import Becoming.Recurrence

/-!
# Lasting: a number of steps, exhaustion, and never reaching

`Becoming.Viability` states where no course ever leaves a guard. This module states the same for
a finite number of steps and reads it from both sides: what suffices for lasting `n` steps and
what lasting `n` steps requires. It then states when a guard is exhausted, and where a
determined law never reaches a target.

* **Lasting a horizon.** `Lasts f adm guard n s`: `s` is within the guard and, for `n` more
  steps, so is every configuration an admissible disturbance takes it to. A **ladder** is a
  family of levels within the guard in which every admissible step from level `k + 1` lands at
  level `k` (`Ladder`). A start lasts `n` steps exactly when some ladder holds it at level `n`
  (`lasts_iff_ladder`); `Lasts` is itself a ladder, the largest. A family is **necessary** when
  the guard gives level `0` and a configuration within the guard whose admissible successors are
  all at level `k` is at level `k + 1` (`Necessary`). A start lasts `n` steps exactly when every
  necessary family holds it at level `n` (`lasts_iff_necessary`); `Lasts` is the least. A family
  that is both is exactly `Lasts` (`lasts_iff_of_exact`). Given one admissible disturbance,
  lasting `n` steps is staying within the guard for the first `n` steps of every admissible
  history (`lasts_iff_histories`). With no premise, the kernel of `Becoming.Viability` is what
  lasts every horizon (`kernel_iff_lasts`). From within the guard, a guarded history agrees with
  the history at `n` exactly when the history stays within the guard up to `n`
  (`guarded_upto_iff`), and stops exactly when it does not (`guarded_none_iff`).
* **Exhaustion.** A family is **drained** when the guard gives level `0` and a configuration
  within the guard that one admissible step takes to level `k` was at level `k + 1` (`Drains`).
  Along every admissible history that stays within the guard for its first `n` steps, the start
  is at level `n` (`Drains.along`). So a start below level `n` leaves the guard within `n` steps
  on every admissible history (`Drains.leaves`). Being at level `n` does not suffice
  (`Collapse.level_not_lasting`). A sequence whose growth is bounded by a monotone map stays
  below the map's orbit (`below_orbit`), and the orbit is the worst such growth
  (`stays_below_iff`). Let a quantity grow at most by a monotone map, and let each step taken
  while the quantity's orbit stays at or below a threshold cost one level. Then every start
  whose orbit stays at or below the threshold for `n` steps and which is not at level `n`
  leaves the guard within `n` steps on every admissible history (`exhausts`).
* **Never reaching.** A determined law's orbit never reaches a target exactly when some set
  containing the start avoids the target and is closed under the law (`avoids_iff_closed`).
  This is the viability kernel of the target's complement (`avoids_iff_kernel`). Some seed
  never reaches the target exactly when such a set contains a seed (`some_avoids_iff`). No seed
  avoids the target exactly when no such set contains a seed (`none_avoid_iff`); read with
  excluded middle, which the core does not use, the left side says every seed reaches the
  target. A fixed configuration outside the target is such a set by itself (`fixed_avoids`).

Every condition named here is local: one step from each configuration. Which guard, levels,
quantity, threshold and target an application uses are supplied with it; nothing here says that
some ladder, drained family or closed set exists. No premise is added; every declaration has an
empty axiom report.
-/

namespace Becoming

open Generative

universe u v w

namespace Lasting

open Viability

variable {S : Type u} {A : Type v}

/-! ## Lasting a horizon -/

/-- `Lasts f adm guard n s`: `s` is within the guard and, for `n` more steps, so is every
configuration an admissible disturbance takes it to. -/
def Lasts (f : S → A → S) (adm : A → Prop) (guard : S → Prop) : Nat → S → Prop
  | 0, s => guard s
  | n + 1, s => guard s ∧ ∀ a, adm a → Lasts f adm guard n (f s a)

/-- A **ladder** for a guard: levels within the guard, every admissible step from level `k + 1`
landing at level `k`. -/
structure Ladder (f : S → A → S) (adm : A → Prop) (guard : S → Prop) (C : Nat → S → Prop) :
    Prop where
  within : ∀ k x, C k x → guard x
  descends : ∀ k x a, adm a → C (k + 1) x → C k (f x a)

/-- A family **necessary** for lasting: within the guard is level `0`, and a configuration
within the guard whose admissible successors are all at level `k` is at level `k + 1`. -/
structure Necessary (f : S → A → S) (adm : A → Prop) (guard : S → Prop) (L : Nat → S → Prop) :
    Prop where
  base : ∀ x, guard x → L 0 x
  rises : ∀ k x, guard x → (∀ a, adm a → L k (f x a)) → L (k + 1) x

/-- A family **drained** along every admissible step: within the guard is level `0`, and a
configuration within the guard that one admissible step takes to level `k` was at level
`k + 1`. -/
structure Drains (f : S → A → S) (adm : A → Prop) (guard : S → Prop) (L : Nat → S → Prop) :
    Prop where
  base : ∀ x, guard x → L 0 x
  rises : ∀ k x a, guard x → adm a → L k (f x a) → L (k + 1) x

variable {f : S → A → S} {adm : A → Prop} {guard : S → Prop}

/-- What lasts is within the guard. -/
theorem Lasts.within : ∀ {n : Nat} {s : S}, Lasts f adm guard n s → guard s
  | 0, _, lasts => lasts
  | _ + 1, _, lasts => And.left lasts

/-- **Every ladder lasts**: a start at level `n` of a ladder lasts `n` steps. -/
theorem Ladder.lasts {C : Nat → S → Prop} (ladder : Ladder f adm guard C) :
    ∀ (n : Nat) (s : S), C n s → Lasts f adm guard n s
  | 0, s, held => ladder.within 0 s held
  | n + 1, s, held => And.intro (ladder.within (n + 1) s held)
      (fun a admitted => Ladder.lasts ladder n (f s a) (ladder.descends n s a admitted held))

/-- **`Lasts` is a ladder.** -/
theorem lasts_ladder : Ladder f adm guard (Lasts f adm guard) :=
  ⟨fun _ _ lasts => Lasts.within lasts, fun _ _ a admitted lasts => And.right lasts a admitted⟩

/-- **A start lasts `n` steps exactly when some ladder holds it at level `n`.** -/
theorem lasts_iff_ladder {n : Nat} {s : S} :
    Lasts f adm guard n s ↔ ∃ C : Nat → S → Prop, C n s ∧ Ladder f adm guard C :=
  ⟨fun lasts => ⟨Lasts f adm guard, lasts, lasts_ladder⟩,
   fun ⟨_, held, ladder⟩ => Ladder.lasts ladder n s held⟩

/-- **Every necessary family holds what lasts.** -/
theorem Necessary.of_lasts {L : Nat → S → Prop} (necessary : Necessary f adm guard L) :
    ∀ (n : Nat) (s : S), Lasts f adm guard n s → L n s
  | 0, s, lasts => necessary.base s lasts
  | n + 1, s, lasts => necessary.rises n s (And.left lasts)
      (fun a admitted => Necessary.of_lasts necessary n (f s a) (And.right lasts a admitted))

/-- **`Lasts` is necessary.** -/
theorem lasts_necessary : Necessary f adm guard (Lasts f adm guard) :=
  ⟨fun _ held => held, fun _ _ held next => And.intro held next⟩

/-- **A start lasts `n` steps exactly when every necessary family holds it at level `n`.** -/
theorem lasts_iff_necessary {n : Nat} {s : S} :
    Lasts f adm guard n s ↔ ∀ L : Nat → S → Prop, Necessary f adm guard L → L n s :=
  ⟨fun lasts _ necessary => Necessary.of_lasts necessary n s lasts,
   fun every => every (Lasts f adm guard) lasts_necessary⟩

/-- **A family that is both a ladder and necessary is exactly lasting.** -/
theorem lasts_iff_of_exact {C : Nat → S → Prop} (ladder : Ladder f adm guard C)
    (necessary : Necessary f adm guard C) (n : Nat) (s : S) : Lasts f adm guard n s ↔ C n s :=
  ⟨Necessary.of_lasts necessary n s, Ladder.lasts ladder n s⟩

/-! ### Histories -/

/-- A disturbance put before a course of disturbances. -/
def prepend (a : A) (d : Nat → A) : Nat → A
  | 0 => a
  | k + 1 => d k

theorem prepend_admissible {a : A} {d : Nat → A} (admitted : adm a)
    (admissible : ∀ k, adm (d k)) : ∀ k, adm (prepend a d k)
  | 0 => admitted
  | k + 1 => admissible k

/-- **What lasts `n` steps stays within the guard for the first `n` steps of every admissible
history.** -/
theorem Lasts.histories : ∀ {n : Nat} {s : S}, Lasts f adm guard n s →
    ∀ d : Nat → A, (∀ k, adm (d k)) → ∀ k, k ≤ n → guard (history f s d k)
  | 0, _, lasts, _, _, 0, _ => lasts
  | 0, _, _, _, _, k + 1, bound => absurd bound (Nat.not_succ_le_zero k)
  | _ + 1, _, lasts, _, _, 0, _ => And.left lasts
  | _ + 1, s, lasts, d, admissible, k + 1, bound =>
      Eq.mpr (congrArg guard (history_shift f s d k))
        (Lasts.histories (And.right lasts (d 0) (admissible 0)) (fun j => d (j + 1))
          (fun j => admissible (j + 1)) k (Nat.le_of_succ_le_succ bound))

/-- **Given one admissible disturbance, what stays within the guard for the first `n` steps of
every admissible history lasts `n` steps.** -/
theorem lasts_of_histories {a₀ : A} (h₀ : adm a₀) : ∀ {n : Nat} {s : S},
    (∀ d : Nat → A, (∀ k, adm (d k)) → ∀ k, k ≤ n → guard (history f s d k)) →
      Lasts f adm guard n s
  | 0, _, every => every (fun _ => a₀) (fun _ => h₀) 0 (Nat.le_refl 0)
  | _ + 1, s, every => And.intro (every (fun _ => a₀) (fun _ => h₀) 0 (Nat.zero_le _))
      (fun a admitted => lasts_of_histories h₀ (fun d admissible k bound =>
        Eq.mp (congrArg guard (history_shift f s (prepend a d) k))
          (every (prepend a d) (prepend_admissible admitted admissible) (k + 1)
            (Nat.succ_le_succ bound))))

/-- **Given one admissible disturbance, a start lasts `n` steps exactly when every admissible
history from it stays within the guard for its first `n` steps.** -/
theorem lasts_iff_histories {a₀ : A} (h₀ : adm a₀) {n : Nat} {s : S} :
    Lasts f adm guard n s ↔
      ∀ d : Nat → A, (∀ k, adm (d k)) → ∀ k, k ≤ n → guard (history f s d k) :=
  ⟨fun lasts => Lasts.histories lasts, lasts_of_histories h₀⟩

/-- What lasts `n` steps keeps every course of at most `n` admissible steps within the guard. -/
theorem Lasts.trace : ∀ {plan : List A} {n : Nat} {s t : S}, Lasts f adm guard n s →
    Trace (disturbed f adm) s plan t → plan.length ≤ n → guard t
  | [], _, _, _, lasts, .nil _, _ => Lasts.within lasts
  | _ :: _, 0, _, _, _, _, bound => absurd bound (Nat.not_succ_le_zero _)
  | a :: _, n + 1, _, _, lasts, .cons ⟨admitted, moved⟩ tail, bound =>
      Lasts.trace (Eq.mpr (congrArg (Lasts f adm guard n) moved) (And.right lasts a admitted))
        tail (Nat.le_of_succ_le_succ bound)

/-- What no course leaves lasts every horizon. -/
theorem lasts_of_kernel : ∀ (n : Nat) {s : S}, Kernel (disturbed f adm) guard s →
    Lasts f adm guard n s
  | 0, s, kept => kept s (Reach.refl _ s)
  | n + 1, s, kept => And.intro (kept s (Reach.refl _ s))
      (fun a admitted => lasts_of_kernel n (fun t reach =>
        kept t (Reach.trans
          (Reach.of_step (show (disturbed f adm).step s a (f s a) from ⟨admitted, rfl⟩)) reach)))

/-- **What no course leaves is exactly what lasts every horizon**, with no premise. -/
theorem kernel_iff_lasts {s : S} :
    Kernel (disturbed f adm) guard s ↔ ∀ n, Lasts f adm guard n s :=
  ⟨fun kept n => lasts_of_kernel n kept,
   fun every _ ⟨plan, path⟩ => Lasts.trace (every plan.length) path (Nat.le_refl _)⟩

/-! ### Guarded histories up to a horizon -/

/-- A history within the guard up to `n` agrees with its guarded history at `n`. -/
theorem guarded_agrees [DecidablePred guard] {s : S} {d : Nat → A} : ∀ {n : Nat},
    (∀ k, k ≤ n → guard (history f s d k)) →
      guardedHistory f guard s d n = some (history f s d n)
  | 0, _ => rfl
  | n + 1, within => (congrArg (guardedStep f guard (d n))
      (guarded_agrees (fun k bound => within k (Nat.le_succ_of_le bound)))).trans
      (step_of_ready ⟨within n (Nat.le_succ n), within (n + 1) (Nat.le_refl _)⟩)

/-- A guarded history that goes on at `n + 1` is the history there, and the history stayed
within the guard up to `n + 1`. -/
theorem guarded_within [DecidablePred guard] {s : S} {d : Nat → A} : ∀ {n : Nat} {t : S},
    guardedHistory f guard s d (n + 1) = some t →
      t = history f s d (n + 1) ∧ ∀ k, k ≤ n + 1 → guard (history f s d k)
  | 0, t, moved => by
    have ready : guard s ∧ guard (f s (d 0)) := ready_of_step moved
    have next : t = f s (d 0) := by
      change (if guard s ∧ guard (f s (d 0)) then some (f s (d 0)) else none) = some t at moved
      rw [if_pos ready] at moved
      exact (Option.some.inj moved).symm
    exact ⟨next, fun k bound => match k, bound with
      | 0, _ => ready.1
      | 1, _ => ready.2
      | _ + 2, bound => absurd (Nat.le_of_succ_le_succ bound) (Nat.not_succ_le_zero _)⟩
  | n + 1, t, moved => by
    change guardedStep f guard (d (n + 1)) (guardedHistory f guard s d (n + 1)) = some t at moved
    cases prior : guardedHistory f guard s d (n + 1) with
    | none =>
      rw [prior] at moved
      exact absurd moved none_ne_some
    | some u =>
      rw [prior] at moved
      have earlier := guarded_within prior
      have ready : guard u ∧ guard (f u (d (n + 1))) := ready_of_step moved
      have next : t = f u (d (n + 1)) := by
        change (if guard u ∧ guard (f u (d (n + 1))) then some (f u (d (n + 1))) else none)
          = some t at moved
        rw [if_pos ready] at moved
        exact (Option.some.inj moved).symm
      have same : u = history f s d (n + 1) := earlier.1
      subst same
      exact ⟨next, fun k bound => match Nat.eq_or_lt_of_le bound with
        | .inl at_end => Eq.mpr (congrArg (fun j => guard (history f s d j)) at_end) ready.2
        | .inr before => earlier.2 k (Nat.le_of_lt_succ before)⟩

/-- **From within the guard, a guarded history agrees with the history at `n` exactly when the
history stays within the guard up to `n`.** -/
theorem guarded_upto_iff [DecidablePred guard] {s : S} {d : Nat → A} (start : guard s)
    {n : Nat} :
    guardedHistory f guard s d n = some (history f s d n) ↔
      ∀ k, k ≤ n → guard (history f s d k) :=
  ⟨fun agree => match n, agree with
    | 0, _ => fun k bound => match k, bound with
      | 0, _ => start
      | _ + 1, bound => absurd bound (Nat.not_succ_le_zero _)
    | _ + 1, agree => (guarded_within agree).2,
   guarded_agrees⟩

/-- **From within the guard, a guarded history stops by `n` exactly when the history leaves the
guard by `n`.** -/
theorem guarded_none_iff [DecidablePred guard] {s : S} {d : Nat → A} (start : guard s)
    {n : Nat} :
    guardedHistory f guard s d n = none ↔ ¬ ∀ k, k ≤ n → guard (history f s d k) :=
  ⟨fun stopped within => none_ne_some (stopped.symm.trans (guarded_agrees within)),
   fun leaves => by
    cases going : guardedHistory f guard s d n with
    | none => rfl
    | some t =>
      cases n with
      | zero => exact absurd (fun k bound => match k, bound with
          | 0, _ => start
          | _ + 1, bound => absurd bound (Nat.not_succ_le_zero _)) leaves
      | succ n => exact absurd (guarded_within going).2 leaves⟩

/-! ## Exhaustion -/

/-- **Along every admissible history within the guard for its first `n` steps, a drained family
holds the start at level `n`.** -/
theorem Drains.along {L : Nat → S → Prop} (drains : Drains f adm guard L) :
    ∀ (n : Nat) (s : S) (d : Nat → A), (∀ k, adm (d k)) →
      (∀ k, k ≤ n → guard (history f s d k)) → L n s
  | 0, s, _, _, within => drains.base s (within 0 (Nat.le_refl 0))
  | n + 1, s, d, admissible, within =>
      drains.rises n s (d 0) (within 0 (Nat.zero_le _)) (admissible 0)
        (Drains.along drains n (f s (d 0)) (fun k => d (k + 1)) (fun k => admissible (k + 1))
          (fun k bound => Eq.mp (congrArg guard (history_shift f s d k))
            (within (k + 1) (Nat.succ_le_succ bound))))

/-- **Exhaustion**: a start below level `n` of a drained family leaves the guard within `n`
steps on every admissible history. -/
theorem Drains.leaves {L : Nat → S → Prop} (drains : Drains f adm guard L) {n : Nat} {s : S}
    (below : ¬ L n s) (d : Nat → A) (admissible : ∀ k, adm (d k)) :
    ¬ ∀ k, k ≤ n → guard (history f s d k) :=
  fun within => below (Drains.along drains n s d admissible within)

/-- Given one admissible disturbance, a drained family is necessary. -/
theorem Drains.necessary {L : Nat → S → Prop} (drains : Drains f adm guard L) {a₀ : A}
    (h₀ : adm a₀) : Necessary f adm guard L :=
  ⟨drains.base, fun k x held next => drains.rises k x a₀ held h₀ (next a₀ h₀)⟩

/-! ### Being at a level does not suffice -/

namespace Collapse

/-- Every step goes to `false`. -/
def step (_ : Bool) (_ : Unit) : Bool := false

/-- The family "is `true`" is drained for the guard "is `true`" and holds `true` at level `1`,
yet `true` does not last one step. -/
theorem level_not_lasting :
    Drains step (fun _ => True) (fun b => b = true) (fun _ b => b = true) ∧
      (fun (_ : Nat) (b : Bool) => b = true) 1 true ∧
      ¬ Lasts step (fun _ => True) (fun b => b = true) 1 true :=
  ⟨⟨fun _ held => held, fun _ _ _ _ _ next => Bool.noConfusion next⟩, rfl,
   fun lasts => Bool.noConfusion (And.right lasts () trivial)⟩

end Collapse

/-! ### Growth bounded by a monotone map -/

section Growth

variable {V : Type w} {rel : V → V → Prop} {g : V → V}

/-- A monotone map keeps the order along its orbits. -/
theorem orbit_mono (mono : ∀ a b, rel a b → rel (g a) (g b)) {a b : V} (below : rel a b) :
    ∀ n, rel (Law.orbit g a n) (Law.orbit g b n)
  | 0 => below
  | n + 1 => mono _ _ (orbit_mono mono below n)

/-- **Growth bounded by a monotone map stays below the map's orbit.** -/
theorem below_orbit (trans : ∀ a b c, rel a b → rel b c → rel a c)
    (mono : ∀ a b, rel a b → rel (g a) (g b)) {x : Nat → V} {v : V} (start : rel (x 0) v)
    (grows : ∀ n, rel (x (n + 1)) (g (x n))) : ∀ n, rel (x n) (Law.orbit g v n)
  | 0 => start
  | n + 1 => trans _ _ _ (grows n) (mono _ _ (below_orbit trans mono start grows n))

/-- **The orbit is the worst growth**: every sequence starting at or below `v` whose growth `g`
bounds stays at or below `θ` for its first `n` steps exactly when the orbit of `v` does. -/
theorem stays_below_iff (refl : ∀ a, rel a a) (trans : ∀ a b c, rel a b → rel b c → rel a c)
    (mono : ∀ a b, rel a b → rel (g a) (g b)) {v θ : V} {n : Nat} :
    (∀ x : Nat → V, rel (x 0) v → (∀ k, rel (x (k + 1)) (g (x k))) →
        ∀ k, k ≤ n → rel (x k) θ) ↔
      ∀ k, k ≤ n → rel (Law.orbit g v k) θ :=
  ⟨fun every => every (Law.orbit g v) (refl v) (fun _ => refl _),
   fun bound _ start grows k before =>
    trans _ _ _ (below_orbit trans mono start grows k) (bound k before)⟩

/-- Where a quantity `q` grows at most by a monotone `g` on every admissible step from a region,
a configuration of the region whose quantity's orbit is at or below `θ` at `k + 1` steps goes,
after an admissible step, to one whose quantity's orbit is at or below `θ` at `k` steps. -/
theorem small_descends (trans : ∀ a b c, rel a b → rel b c → rel a c)
    (mono : ∀ a b, rel a b → rel (g a) (g b)) {R : S → Prop} {q : S → V}
    (grows : ∀ x a, adm a → R x → rel (q (f x a)) (g (q x))) {θ : V} {k : Nat} {x : S} {a : A}
    (admitted : adm a) (region : R x) (small : rel (Law.orbit g (q x) (k + 1)) θ) :
    rel (Law.orbit g (q (f x a)) k) θ :=
  trans _ _ _ (orbit_mono mono (grows x a admitted region) k)
    (Eq.mp (congrArg (fun y => rel y θ) (Law.orbit_shift g (q x) k)) small)

/-- **Exhaustion by bounded growth.** Let every admissible step keep a region, and bound the
growth of a quantity `q` there by a monotone `g`. Let within the guard be level `0`, and let an
admissible step from a configuration of the region within the guard, whose quantity's orbit is
at or below `θ` at `k + 1` steps, cost one level: reaching level `k` means having had level
`k + 1`. Then from a start in the region whose quantity's orbit is at or below `θ` at `n` steps
and which is not at level `n`, every admissible history leaves the guard within `n` steps. -/
theorem exhausts (trans : ∀ a b c, rel a b → rel b c → rel a c)
    (mono : ∀ a b, rel a b → rel (g a) (g b)) {R : S → Prop} {q : S → V} {θ : V}
    {level : Nat → S → Prop}
    (kept : ∀ x a, adm a → R x → R (f x a))
    (grows : ∀ x a, adm a → R x → rel (q (f x a)) (g (q x)))
    (base : ∀ x, guard x → level 0 x)
    (costs : ∀ k x a, R x → guard x → adm a → rel (Law.orbit g (q x) (k + 1)) θ →
      level k (f x a) → level (k + 1) x)
    {n : Nat} {s : S} (region : R s) (small : rel (Law.orbit g (q s) n) θ)
    (short : ¬ level n s) (d : Nat → A) (admissible : ∀ k, adm (d k)) :
    ¬ ∀ k, k ≤ n → guard (history f s d k) :=
  Drains.leaves (f := f) (adm := adm) (guard := guard)
    (L := fun k x => R x → rel (Law.orbit g (q x) k) θ → level k x)
    ⟨fun x held _ _ => base x held,
     fun k x a held admitted next region' small' =>
       costs k x a region' held admitted small'
         (next (kept x a admitted region')
           (small_descends trans mono grows admitted region' small'))⟩
    (fun at_level => short (at_level region small)) d admissible

end Growth

/-! ## Never reaching -/

section Reaching

variable {next : S → S} {target : S → Prop}

/-- Every configuration of the orbit of a member of a closed set is in the set. -/
theorem closed_orbit {K : S → Prop} (closed : ∀ x, K x → K (next x)) {s : S} (held : K s) :
    ∀ n, K (Law.orbit next s n)
  | 0 => held
  | n + 1 => closed _ (closed_orbit closed held n)

/-- **A determined law's orbit never reaches a target exactly when some set containing the start
avoids the target and is closed under the law.** -/
theorem avoids_iff_closed {s : S} :
    (∀ n, ¬ target (Law.orbit next s n)) ↔
      ∃ K : S → Prop, K s ∧ (∀ x, K x → ¬ target x) ∧ ∀ x, K x → K (next x) :=
  ⟨fun avoids => ⟨fun x => ∀ n, ¬ target (Law.orbit next x n), avoids, fun _ held => held 0,
    fun x held n =>
      Eq.mp (congrArg (fun y => ¬ target y) (Law.orbit_shift next x n)) (held (n + 1))⟩,
   fun ⟨_, held, avoid, closed⟩ n => avoid _ (closed_orbit closed held n)⟩

/-- A determined law as a law of change under one disturbance. -/
def determined (next : S → S) (x : S) (_ : Unit) : S := next x

theorem orbit_eq_history (next : S → S) (s : S) (d : Nat → Unit) :
    ∀ n, Law.orbit next s n = history (determined next) s d n
  | 0 => rfl
  | n + 1 => congrArg next (orbit_eq_history next s d n)

/-- **Never reaching a target is never leaving its complement**: the orbit never reaches the
target exactly when the start is in the viability kernel of the target's complement. -/
theorem avoids_iff_kernel {s : S} :
    (∀ n, ¬ target (Law.orbit next s n)) ↔
      Kernel (disturbed (determined next) (fun _ => True)) (fun x => ¬ target x) s :=
  (⟨fun avoids d _ n =>
      Eq.mp (congrArg (fun y => ¬ target y) (orbit_eq_history next s d n)) (avoids n),
    fun every n =>
      Eq.mpr (congrArg (fun y => ¬ target y) (orbit_eq_history next s (fun _ => ()) n))
        (every (fun _ => ()) (fun _ => trivial) n)⟩ :
      (∀ n, ¬ target (Law.orbit next s n)) ↔
        ∀ d : Nat → Unit, (∀ n, (fun _ : Unit => True) (d n)) →
          ∀ n, (fun x => ¬ target x) (history (determined next) s d n)).trans
    (never_leaves_iff_kernel (f := determined next) (adm := fun _ => True)
      (guard := fun x => ¬ target x) (s := s) (a₀ := ()) trivial)

/-- **Some seed never reaches the target exactly when some set closed under the law and avoiding
the target contains a seed.** -/
theorem some_avoids_iff {seed : S → Prop} :
    (∃ s, seed s ∧ ∀ n, ¬ target (Law.orbit next s n)) ↔
      ∃ K : S → Prop, (∃ s, seed s ∧ K s) ∧ (∀ x, K x → ¬ target x) ∧
        ∀ x, K x → K (next x) :=
  ⟨fun ⟨s, seeded, avoids⟩ => match avoids_iff_closed.mp avoids with
    | ⟨K, held, avoid, closed⟩ => ⟨K, ⟨s, seeded, held⟩, avoid, closed⟩,
   fun ⟨K, ⟨s, seeded, held⟩, avoid, closed⟩ =>
    ⟨s, seeded, avoids_iff_closed.mpr ⟨K, held, avoid, closed⟩⟩⟩

/-- **No seed avoids the target exactly when no set closed under the law and avoiding the target
contains a seed.** Read with excluded middle, the left side says every seed reaches the
target. -/
theorem none_avoid_iff {seed : S → Prop} :
    (∀ s, seed s → ¬ ∀ n, ¬ target (Law.orbit next s n)) ↔
      ¬ ∃ K : S → Prop, (∃ s, seed s ∧ K s) ∧ (∀ x, K x → ¬ target x) ∧
        ∀ x, K x → K (next x) :=
  ⟨fun none_avoid found => match some_avoids_iff.mpr found with
    | ⟨s, seeded, avoids⟩ => none_avoid s seeded avoids,
   fun none_found s seeded avoids => none_found (some_avoids_iff.mp ⟨s, seeded, avoids⟩)⟩

/-- Reaching the target from every seed rules out every set closed under the law and avoiding
the target that contains a seed. -/
theorem reaches_excludes {seed : S → Prop}
    (reaches : ∀ s, seed s → ∃ n, target (Law.orbit next s n)) :
    ¬ ∃ K : S → Prop, (∃ s, seed s ∧ K s) ∧ (∀ x, K x → ¬ target x) ∧
      ∀ x, K x → K (next x) :=
  none_avoid_iff.mp (fun s seeded avoids => match reaches s seeded with
    | ⟨n, reached⟩ => avoids n reached)

/-- **A fixed configuration outside the target never reaches it**: it is a closed set by
itself. -/
theorem fixed_avoids {x : S} (fixed : next x = x) (outside : ¬ target x) :
    ∀ n, ¬ target (Law.orbit next x n) :=
  avoids_iff_closed.mpr ⟨fun y => y = x, rfl,
    fun _ same => Eq.mpr (congrArg (fun z => ¬ target z) same) outside,
    fun _ same => Eq.mpr (congrArg (fun z => next z = x) same) fixed⟩

end Reaching

end Lasting

end Becoming
