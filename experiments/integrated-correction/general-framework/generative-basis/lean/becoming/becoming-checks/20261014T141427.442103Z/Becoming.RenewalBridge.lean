import Becoming
import RenewalComparison
import RenewalRecovery

/-!
# The support-gated renewal law as an instance of the spine's general laws

`RelationalRenewal.Law` is one family of unfoldings: a shared condition renewed by a
sustaining formation while the condition supports it, drawn on and contributed to by a
focal formation while the condition supports that one. Three peripheral results were
proved for this family only: the classification of overdraw and joint drawing
(`RelationalRenewal`), recovery (`RenewalRecovery`) and the comparison of courses
(`RenewalComparison`). This module shows every law of the family to be a balanced flow on
its static web and derives the family results from laws that hold for every balanced flow
and every family of courses:

* Every law of the family is balanced by the flow in which the sustaining formation gives
  the renewal while supported and the focal formation gives what it contributes beyond its
  draw while active, and takes what it actually removes (`balances`). The focal take is
  defined as what the step removes, so balance holds by construction wherever the level does
  not exceed the level plus what is given (`level_succ_le`). The instance's content is that the
  given amounts are the family's renewal and net giving, given only where supported
  (`givers_supported`), and the family's arithmetic (`repair_restores`). Renewal gives only
  where the sustaining formation is supported, and the focal formation gives only where it
  is active.
* Restoration (`Flow.restores`): where the focal formation is active and contributes more
  than it draws at each of `needG - level` steps, the condition is back at the sustaining
  need (`repair_restores`), as in `RenewalRecovery.repair_restores_sustaining_support`; the
  supported pulse of `RenewalRecovery` is an instance (`pulse_restores`).
* Loss for good (`Flow.stays_below_at`, `Flow.ends_below_at`): once below a bound within
  the sustaining need, and with the focal formation contributing no more than it draws, the
  condition stays below the bound (`below_for_good`), and every formation depending on it
  at a need of at least the bound is inactive from then on (`ends_for_good`).
  `RelationalRenewal.Law.overdraw_crosses_support` gives the crossing, after which the
  sustaining formation is inactive for good (`overdraw_ends`). That a dependent overdrawing
  focal formation brings the level below its own need, and the bound on what it forms,
  remain the family's arithmetic (`RelationalRenewal.Law.dependent_overdraw_ends_itself`);
  from that step on its ending for good is `ends_for_good`.
* Joint drawing: two formations drawing together beyond renewal, read by the family as one
  focal formation with the summed draw, end with the renewing relation (`jointly_ends`).
  The family cannot represent each drawer's own share; `Becoming.Continuation`'s
  `WithinOwn`, `WithinJoint` and `Flow.joint_excess_ends` state that split for every flow.
* Comparison of courses (`Ranking.renewed_extends_iff`): `RenewalComparison`'s relational
  extension of the course without an overdrawing formation, and of sharing over winning by
  consumption, are instances of the law of comparison with a renewing course
  (`overdraw_extension`, `contest_extensions`).

Every declaration has an empty axiom report. The family's own arithmetic (the crossing,
`overdraw_consuming`, `within_renewal_sustains`) comes from the foundation module
`RelationalRenewal`; of the peripheral modules only definitions and
`RenewalComparison.undisturbed_sustains` are used.
-/

namespace Becoming

namespace SupportGated

open RelationalRenewal RelationalRenewal.Law

/-! ## Arithmetic -/

/-- Subtracting after adding is at most adding what remains after subtracting. -/
theorem add_sub_le : ∀ a c d : Nat, a + c - d ≤ a + (c - d)
  | _, _, 0 => Nat.le_refl _
  | a, 0, d + 1 => Nat.le_trans (Nat.sub_le a (d + 1)) (Nat.le_add_right a _)
  | a, c + 1, d + 1 => Nat.le_trans (Nat.le_of_eq (Nat.succ_sub_succ (a + c) d))
      (Nat.le_trans (add_sub_le a c d) (Nat.le_of_eq (congrArg (a + ·) (Nat.succ_sub_succ c d).symm)))

/-- Where nothing remains after subtracting, nothing does. -/
theorem sub_eq_zero_of_le : ∀ {c d : Nat}, c ≤ d → c - d = 0
  | 0, d, _ => Nat.zero_sub d
  | _ + 1, 0, le => absurd le (Nat.not_succ_le_zero _)
  | c + 1, d + 1, le => (Nat.succ_sub_succ c d).trans (sub_eq_zero_of_le (Nat.le_of_succ_le_succ le))

/-- What exceeds leaves a positive remainder. -/
theorem sub_pos_of_lt : ∀ {d c : Nat}, d < c → 0 < c - d
  | _, 0, less => absurd less (Nat.not_lt_zero _)
  | 0, c + 1, _ => Nat.succ_pos c
  | d + 1, c + 1, less => Nat.lt_of_lt_of_le (sub_pos_of_lt (Nat.lt_of_succ_lt_succ less))
      (Nat.le_of_eq (Nat.succ_sub_succ c d).symm)

/-- Within what is added, subtracting after adding is adding what remains. -/
theorem add_sub_assoc_of_le : ∀ (a : Nat) {c d : Nat}, d ≤ c → a + c - d = a + (c - d)
  | _, _, 0, _ => rfl
  | _, 0, _ + 1, le => absurd le (Nat.not_succ_le_zero _)
  | a, c + 1, d + 1, le => (Nat.succ_sub_succ (a + c) d).trans
      ((add_sub_assoc_of_le a (Nat.le_of_succ_le_succ le)).trans
        (congrArg (a + ·) (Nat.succ_sub_succ c d).symm))

/-! ## The law as a balanced flow -/

variable (L : Law)

/-- What the sustaining formation gives across the step: the renewal, while supported. -/
def renewal (t : Nat) : Nat :=
  if L.needG ≤ L.level t then L.renew else 0

/-- What the focal formation gives across the step: what it contributes beyond its draw,
while active. -/
def netGive (t : Nat) : Nat :=
  if L.needF ≤ L.level t then L.contrib t - L.draw t else 0

/-- The law as a flow: the sustaining formation gives the renewal while supported; the
focal formation gives its net giving while active and takes what the step removes, so the
flow balances by construction (`level_succ_le`). -/
def flow : Flow Part Unit where
  present _ := [.sustaining, .focal]
  give t p _ := match p with
    | .sustaining => renewal L t
    | .focal => netGive L t
  take t p _ := match p with
    | .sustaining => 0
    | .focal => L.level t + (renewal L t + netGive L t) - L.level (t + 1)

/-- The law's static web. -/
def web : Web Part Unit :=
  Web.static L.unfolding

/-- Across each step the level does not exceed the level before plus what is given. -/
theorem level_succ_le (t : Nat) : L.level (t + 1) ≤ L.level t + (renewal L t + netGive L t) := by
  show (if L.needG ≤ L.level t then
      if L.needF ≤ L.level t then L.level t + L.renew + L.contrib t - L.draw t
      else L.level t + L.renew
    else
      if L.needF ≤ L.level t then L.level t + L.contrib t - L.draw t
      else L.level t) ≤ L.level t + ((if L.needG ≤ L.level t then L.renew else 0) +
        (if L.needF ≤ L.level t then L.contrib t - L.draw t else 0))
  cases Nat.lt_or_ge (L.level t) L.needG with
  | inl gOff =>
    rw [if_neg (Nat.not_le_of_gt gOff), if_neg (Nat.not_le_of_gt gOff)]
    cases Nat.lt_or_ge (L.level t) L.needF with
    | inl fOff =>
      rw [if_neg (Nat.not_le_of_gt fOff), if_neg (Nat.not_le_of_gt fOff)]
      exact Nat.le_add_right _ _
    | inr fOn =>
      rw [if_pos fOn, if_pos fOn, Nat.zero_add]
      exact add_sub_le _ _ _
  | inr gOn =>
    rw [if_pos gOn, if_pos gOn]
    cases Nat.lt_or_ge (L.level t) L.needF with
    | inl fOff =>
      rw [if_neg (Nat.not_le_of_gt fOff), if_neg (Nat.not_le_of_gt fOff)]
      exact Nat.le_refl _
    | inr fOn =>
      rw [if_pos fOn, if_pos fOn, ← Nat.add_assoc]
      exact add_sub_le _ _ _

/-- Every law of the family is balanced by its flow. -/
theorem balances : (flow L).Balances (web L) :=
  fun t _ => (congrArg (L.level (t + 1) + ·) (Nat.zero_add _)).trans
    (add_sub_of_le (level_succ_le L t))

/-- Renewal gives only while the sustaining formation is supported. -/
theorem renewal_supported {t : Nat} (gives : 0 < renewal L t) : L.needG ≤ L.level t :=
  match Nat.lt_or_ge (L.level t) L.needG with
  | .inl gOff => absurd (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (if_neg (Nat.not_le_of_gt gOff))))
      (Nat.lt_irrefl 0)
  | .inr gOn => gOn

/-- The focal formation gives only while active, and only what it contributes beyond its
draw. -/
theorem netGive_active {t : Nat} (gives : 0 < netGive L t) :
    L.needF ≤ L.level t ∧ L.draw t < L.contrib t :=
  match Nat.lt_or_ge (L.level t) L.needF with
  | .inl fOff => absurd (Nat.lt_of_lt_of_le gives (Nat.le_of_eq (if_neg (Nat.not_le_of_gt fOff))))
      (Nat.lt_irrefl 0)
  | .inr fOn => ⟨fOn, match Nat.lt_or_ge (L.draw t) (L.contrib t) with
      | .inl less => less
      | .inr more => absurd (Nat.lt_of_lt_of_le gives (Nat.le_of_eq
          ((if_pos fOn).trans (sub_eq_zero_of_le more)))) (Nat.lt_irrefl 0)⟩

/-- Whatever gives to the condition is supported there. -/
theorem givers_supported (t : Nat) : (flow L).GiversSupported (web L) t () :=
  fun p _ gives _ _ => match p, gives with
    | .sustaining, gives => renewal_supported L gives
    | .focal, gives => (netGive_active L gives).1

/-! ## Restoration -/

/-- Where the focal formation is active and contributes more than it draws, the step is one
of joint net giving. -/
theorem netGive_step {t : Nat} (fOn : L.needF ≤ L.level t) (less : L.draw t < L.contrib t) :
    (flow L).taken t () < (flow L).given t () := by
  have raised : L.level (t + 1) = L.level t + (renewal L t + netGive L t) := by
    show (if L.needG ≤ L.level t then
        if L.needF ≤ L.level t then L.level t + L.renew + L.contrib t - L.draw t
        else L.level t + L.renew
      else
        if L.needF ≤ L.level t then L.level t + L.contrib t - L.draw t
        else L.level t) = L.level t + ((if L.needG ≤ L.level t then L.renew else 0) +
          (if L.needF ≤ L.level t then L.contrib t - L.draw t else 0))
    rw [if_pos fOn, if_pos fOn, if_pos fOn]
    cases Nat.lt_or_ge (L.level t) L.needG with
    | inl gOff =>
      rw [if_neg (Nat.not_le_of_gt gOff), if_neg (Nat.not_le_of_gt gOff), Nat.zero_add]
      exact add_sub_assoc_of_le _ (Nat.le_of_lt less)
    | inr gOn =>
      rw [if_pos gOn, if_pos gOn, ← Nat.add_assoc]
      exact add_sub_assoc_of_le _ (Nat.le_of_lt less)
  have positive : 0 < netGive L t := by
    show 0 < (if L.needF ≤ L.level t then L.contrib t - L.draw t else 0)
    rw [if_pos fOn]
    exact sub_pos_of_lt less
  show 0 + (L.level t + (renewal L t + netGive L t) - L.level (t + 1) + 0) <
    renewal L t + (netGive L t + 0)
  rw [raised, Nat.sub_self]
  exact Nat.lt_of_lt_of_le positive (Nat.le_add_left _ _)

/-- Restoration in the family, an instance of `Flow.restores`: where the focal formation
is active at `T` and contributes more than it draws at each of the `needG - level` steps
from `T`, the condition is back at the sustaining need. The statement is
`RenewalRecovery.repair_restores_sustaining_support`. -/
theorem repair_restores (T : Nat) (fOn : L.needF ≤ L.level T)
    (exceeds : ∀ d, d < L.needG - L.level T → L.draw (T + d) < L.contrib (T + d)) :
    L.needG ≤ L.level (T + (L.needG - L.level T)) :=
  Flow.restores (L := flow L) (W := web L) (balances L) (c := ()) (m := L.needG) (T := T)
    fun k below above => netGive_step L (Nat.le_trans fOn above) (exceeds k below)

/-- `RenewalRecovery`'s supported pulse, from step 1, where its level is 1: one step of
net giving restores the sustaining need. -/
theorem pulse_restores :
    (RenewalRecovery.pulse 2).needG ≤ (RenewalRecovery.pulse 2).level
      (1 + ((RenewalRecovery.pulse 2).needG - (RenewalRecovery.pulse 2).level 1)) :=
  repair_restores (RenewalRecovery.pulse 2) 1 (by decide) (by decide)

/-! ## Loss for good -/

/-- Once below a bound within the sustaining need, with the focal formation contributing
no more than it draws, the condition stays below the bound: an instance of
`Flow.stays_below_at`, the content of `RelationalRenewal.Law.permanently_below`. -/
theorem below_for_good {T : Nat} (noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t)
    {bound : Nat} (below : L.level T < bound) (within : bound ≤ L.needG) :
    ∀ n, L.level (T + n) < bound :=
  fun n => Flow.stays_below_at (L := flow L) (W := web L) (c := ()) below n
    (fun k _ => (balances L).on [()] (T + k))
    (fun k p _ _ gives => match p, gives with
      | .sustaining, _ => ⟨trivial, within⟩
      | .focal, gives => absurd (netGive_active L gives).2
          (Nat.not_lt_of_le (noRestore (T + k) (Nat.le_add_right T k))))
    fun k _ => givers_supported L (T + k)

/-- Every formation depending on the condition at a need of at least the bound is then
inactive from `T` on: an instance of `Flow.ends_below_at`. -/
theorem ends_for_good {T : Nat} (noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t)
    {bound : Nat} (below : L.level T < bound) (within : bound ≤ L.needG) (p : Part)
    (depends : L.requiresPart p) (high : bound ≤ L.need p) (n : Nat) :
    ¬ L.unfolding.active (T + n) p :=
  Flow.ends_below_at (W := web L) (c := ()) (fun active => (Web.static_dependent _).mpr
      (unfolding_dependent L) (T + n) p active)
    (below_for_good L noRestore below within n) depends high

/-- Drawing beyond renewal from `T0`, the sustaining formation is inactive for good after
the crossing that `RelationalRenewal.Law.overdraw_crosses_support` gives, and a focal
formation depending on the condition ends once the level is below its need: the endings
of the family are instances of `Flow.stays_below_at` and `Flow.ends_below_at`. -/
theorem overdraw_ends (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    ∃ T, T0 ≤ T ∧ ∀ n, ¬ L.unfolding.active (T + n) .sustaining :=
  match L.overdraw_crosses_support positive fWithin over with
  | ⟨T, after, _, low⟩ =>
    ⟨T, after, ends_for_good L (fun t later => Nat.le_of_lt (Nat.lt_of_le_of_lt
        (Nat.le_add_left _ _) (over t (Nat.le_trans after later))))
      low (Nat.le_refl _) .sustaining trivial (Nat.le_refl _)⟩

/-- Two formations drawing together beyond renewal, as `RelationalRenewal.Law.together`
reads them, end with the relation that renews their condition: the sustaining and the focal
formation are inactive for good after the crossing, an instance of `overdraw_ends` and
`Flow.ends_below_at`. Whether each draws within renewal alone is the family's arithmetic
(`RelationalRenewal.Law.jointly_consuming`). -/
theorem jointly_ends (start renew need : Nat) (d1 d2 : Nat → Nat)
    (joint : ∀ t, renew < d1 t + d2 t) (positive : 0 < need) :
    ∃ T, ∀ n, ¬ (together start renew need d1 d2).unfolding.active (T + n) .sustaining ∧
      ¬ (together start renew need d1 d2).unfolding.active (T + n) .focal :=
  have over : ∀ t, 0 ≤ t → renew + 0 < d1 t + d2 t := fun t _ => joint t
  match (together start renew need d1 d2).overdraw_crosses_support positive (Nat.le_refl _)
      over with
  | ⟨T, _, _, low⟩ =>
    have noRestore : ∀ t, T ≤ t → 0 ≤ d1 t + d2 t := fun _ _ => Nat.zero_le _
    ⟨T, fun n => ⟨ends_for_good _ noRestore low (Nat.le_refl _) .sustaining trivial
        (Nat.le_refl _) n,
      ends_for_good _ noRestore low (Nat.le_refl _) .focal positive (Nat.le_refl _) n⟩⟩

/-! ## Comparison of courses -/

/-- `RenewalComparison`'s relational extension of the course without an overdrawing
formation is an instance of `Ranking.renewed_extends_iff`: the course without it renews
every condition, is active at every event the course with it includes, and the sustaining
formation is active there after the loss. -/
theorem overdraw_extension (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG)
    (gStart : L.needG ≤ L.start) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    GenerativeComparison.GenerativeExtension
      (RenewalComparison.relationalInventory (RenewalComparison.course L)) .occurs .absent :=
  have sustains : ∀ t, L.needG ≤ RenewalComparison.undisturbed L t := fun t =>
    Nat.le_trans gStart (RenewalComparison.undisturbed_sustains L gStart t)
  match overdraw_consuming L positive fWithin over with
  | ⟨consuming, T, lost⟩ =>
    (Ranking.renewed_extends_iff (U := RenewalComparison.course L) (w := .occurs)
      (w' := .absent) fun _ t g _ => match g with
        | .focal => Nat.le_trans fWithin (sustains t)
        | .sustaining => sustains t).1.mpr
      ⟨fun
        | (.focal, _), ⟨_, notConsuming⟩ => absurd consuming notConsuming
        | (.sustaining, t), _ => sustains t,
       (.sustaining, T), sustains T, fun alive => lost T (Nat.le_refl T) alive.1⟩

/-- `RenewalComparison`'s extensions of winning by consumption by sharing, under both its
readings, are instances of the law of comparison with a renewing course in which every
formation is active at every step. -/
theorem contest_extensions :
    GenerativeComparison.GenerativeExtension
        (RenewalComparison.relationalInventory RenewalComparison.contest) .wins .shares ∧
      GenerativeComparison.GenerativeExtension
        (RenewalComparison.broadInventory RenewalComparison.contest) .wins .shares :=
  match overdraw_consuming winning (Nat.succ_pos 0) (Nat.zero_le 1) (T0 := 0)
      (fun _ _ => Nat.lt_succ_self 1) with
  | ⟨_, T, lost⟩ =>
    have kept := within_renewal_sustains sharing (fun _ => Nat.le_refl 1)
      (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
    have renews : ∀ c, Renewed (RenewalComparison.contest .shares) c :=
      fun _ t g depends => match g, depends with
        | .focal, depends => absurd depends (Nat.lt_irrefl 0)
        | .sustaining, _ => Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 1)) (kept t)
    have always : ∀ t p, (RenewalComparison.contest .shares).active t p := fun t p =>
      match p with
      | .focal => Nat.zero_le _
      | .sustaining => Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 1)) (kept t)
    ⟨(Ranking.renewed_active_extends_iff (U := RenewalComparison.contest) (w := .wins)
        (w' := .shares) renews always).1.mpr
        ⟨(.sustaining, T), fun alive => lost T (Nat.le_refl T) alive.1⟩,
     (Ranking.extendsUnder_iff_of_exact (reading := fun (w : RenewalComparison.Contest) (e : Part × Nat) =>
        (RenewalComparison.contest w).active e.2 e.1) (w := .wins) (w' := .shares)
        fun _ => Iff.rfl).mpr
        ⟨fun e _ => always e.2 e.1, ((Part.sustaining, T) : Part × Nat), always T .sustaining,
          lost T (Nat.le_refl T)⟩⟩

end SupportGated

end Becoming
