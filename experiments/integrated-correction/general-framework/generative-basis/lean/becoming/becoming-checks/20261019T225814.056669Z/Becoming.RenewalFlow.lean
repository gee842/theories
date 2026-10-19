import Becoming.Continuation

/-!
# The support-gated renewal law as a balanced flow

`RelationalRenewal.Law` is one family of unfoldings: a shared condition renewed by a sustaining
formation while the condition supports it, drawn on and contributed to by a focal formation while
the condition supports that one. Every law of the family is a balanced flow on its static web, and
the family's recovery, its loss for good and its classification follow from laws that hold for
every balanced flow and every web.

* **Every law of the family is balanced** by the flow in which the sustaining formation gives the
  renewal while supported and the focal formation gives what it contributes beyond its draw while
  active, and takes what it actually removes (`SupportGated.balances`). The focal take is defined
  as what the step removes, so balance holds by construction wherever the level does not exceed
  the level plus what is given (`SupportGated.level_succ_le`). The content is that the given
  amounts are the family's renewal and net giving, given only where supported
  (`SupportGated.givers_supported`).
* **Restoration** (`Flow.restores`): where the focal formation is active and contributes more than
  it draws at each of `needG - level` steps, the condition is back at the sustaining need
  (`SupportGated.repair_restores`).
* **Loss for good** (`Flow.stays_below_at`, `Flow.ends_below_at`): once below a bound within the
  sustaining need, and with the focal formation contributing no more than it draws, the condition
  stays below the bound (`SupportGated.below_for_good`), and every formation depending on it at a
  need of at least the bound is inactive from then on (`SupportGated.ends_for_good`). After the
  crossing that `RelationalRenewal.Law.overdraw_crosses_support` gives, the sustaining formation is
  inactive for good (`SupportGated.overdraw_ends`), and two formations drawing together beyond
  renewal end with the renewing relation (`SupportGated.jointly_ends`). The family cannot represent
  each drawer's own share; `Becoming.Continuation`'s `WithinOwn`, `WithinJoint` and
  `Flow.joint_excess_ends` state that split for every flow.
* **The classification on the webs** (`Web.static`): formation does not decide the class
  (`SupportGatedWebs.formation_does_not_decide`), nor does the focal formation's own trajectory
  (`SupportGatedWebs.own_trajectory_does_not_decide`); formations each within renewal alone
  consume jointly (`SupportGatedWebs.jointly_consuming`); escalation consumes
  (`SupportGatedWebs.escalation_consumes`); and the seasonal web is dependent and neither renewing
  nor consuming (`SupportGatedWebs.fluctuating_dependent`, `SupportGatedWebs.fluctuating_neither`).

`Becoming.RenewalBridge` reads the pulses of `RenewalRecovery` and the comparison of courses of
`RenewalComparison` through these laws, and `Becoming.SupportGatedWebs` the pulses' webs and the
course without the focal formation. Every declaration has an empty axiom report.
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

end SupportGated

namespace SupportGatedWebs

open RelationalRenewal RelationalRenewal.Law

/-- **Formation does not decide the class, on the webs of the family.** -/
theorem formation_does_not_decide :
    (∀ L : Law, ∀ t, (SupportGated.web L).active t .focal → L.formed (t + 1) = L.formed t + 1) ∧
    ((SupportGated.web cultivation).RenewingIn .focal ∧ ∀ t, cultivation.formed t = t) ∧
    (malignant.formed 1 = 1 ∧ (SupportGated.web malignant).ConsumingIn .focal ∧
      ∃ T, (∀ t, T ≤ t → ¬ (SupportGated.web malignant).active t .focal) ∧
        ∀ t, malignant.formed t ≤ T) :=
  match Law.formation_does_not_decide with
  | ⟨forms, ⟨renewing, always⟩, ⟨one, consuming, ends⟩⟩ =>
    ⟨forms, ⟨(Web.static_renewingIn _ _).mpr renewing, always⟩,
     ⟨one, (Web.static_consumingIn _ _).mpr consuming, ends⟩⟩

/-- **The focal formation's own trajectory does not decide the class, on the webs of sharing
and winning.** -/
theorem own_trajectory_does_not_decide :
    (∀ t, (SupportGated.web sharing).active t .focal ↔
      (SupportGated.web winning).active t .focal) ∧
    (∀ t, sharing.formed t = winning.formed t) ∧
    (SupportGated.web sharing).RenewingIn .focal ∧
      (SupportGated.web winning).ConsumingIn .focal :=
  match Law.own_trajectory_does_not_decide with
  | ⟨same, formed, renewing, consuming⟩ =>
    ⟨same, formed, (Web.static_renewingIn _ _).mpr renewing,
     (Web.static_consumingIn _ _).mpr consuming⟩

/-- **Formations each within renewal alone consume jointly, on their webs**, and both end on the
joint web. -/
theorem jointly_consuming (start renew need : Nat) (d1 d2 : Nat → Nat)
    (within1 : ∀ t, d1 t ≤ renew) (within2 : ∀ t, d2 t ≤ renew)
    (joint : ∀ t, renew < d1 t + d2 t) (positive : 0 < need) (supported : need ≤ start) :
    (SupportGated.web (alone start renew need d1)).RenewingIn .focal ∧
    (SupportGated.web (alone start renew need d2)).RenewingIn .focal ∧
    (SupportGated.web (together start renew need d1 d2)).ConsumingIn .focal ∧
    ∃ T, ∀ t, T ≤ t → ¬ (SupportGated.web (together start renew need d1 d2)).active t .focal ∧
      ¬ (SupportGated.web (together start renew need d1 d2)).active t .sustaining :=
  match Law.jointly_consuming start renew need d1 d2 within1 within2 joint positive supported with
  | ⟨first, second, consuming, ends⟩ =>
    ⟨(Web.static_renewingIn _ _).mpr first, (Web.static_renewingIn _ _).mpr second,
     (Web.static_consumingIn _ _).mpr consuming, ends⟩

/-- **Escalation that begins within renewal consumes on its web**, and its focal formation ends
with bounded formation. -/
theorem escalation_consumes :
    (∀ t, t ≤ 2 → escalation.draw t ≤ escalation.renew + escalation.contrib t) ∧
    (SupportGated.web escalation).level 3 () = 6 ∧ escalation.formed 3 = 3 ∧
    (SupportGated.web escalation).ConsumingIn .focal ∧
    ∃ T, (∀ t, T ≤ t → ¬ (SupportGated.web escalation).active t .focal) ∧
      ∀ t, escalation.formed t ≤ T :=
  match Law.escalation_consumes with
  | ⟨within, level, formed, consuming, ends⟩ =>
    ⟨within, level, formed, (Web.static_consumingIn _ _).mpr consuming, ends⟩

/-- **The seasonal web is dependent.** -/
theorem fluctuating_dependent : (Web.static fluctuating).Dependent :=
  (Web.static_dependent _).mpr RelationalRenewal.fluctuating_dependent

/-- **The seasonal web is neither renewing nor consuming**: the classification is not a
dichotomy. -/
theorem fluctuating_neither :
    ¬ (Web.static fluctuating).RenewingIn () ∧ ¬ (Web.static fluctuating).ConsumingIn () :=
  match RelationalRenewal.fluctuating_neither with
  | ⟨notRenewing, notConsuming⟩ =>
    ⟨fun renewing => notRenewing ((Web.static_renewingIn _ _).mp renewing),
     fun consuming => notConsuming ((Web.static_consumingIn _ _).mp consuming)⟩

end SupportGatedWebs

end Becoming

section SupportRecovery

/-!
## Recovery in the support-gated renewal family: its window and its obstruction

`Becoming.RenewalFlow` reads every law of the support-gated family (`RelationalRenewal.Law`) as a
balanced flow and proves restoration (`SupportGated.repair_restores`) and loss for good
(`SupportGated.below_for_good`) as instances of laws of every flow. Board item F3R (18 October
2026) states here, on the core and constructively, what `RenewalRecovery` (8 October) proved of
the family's recovery window and its pulse histories, and what the joins `SupportGatedWebs` and
`SupportGatedWebsInherited` read of them on the webs.

* **No third route.** Where both formations have lost their support, the level stays where it is
  whatever is later drawn or contributed (`absorbs`).
* **The window.** A supported step of positive net repair raises the level by at least one even
  where the sustaining formation is inactive (`repair_step`), so a window of such steps raises it
  by at least its length (`window_progress`); restoration of the sustaining need is
  `SupportGated.repair_restores`.
* **Two pulses.** Two histories start at level 2 and differ only in their first draw; every later
  draw and contribution is the same (`same_later_inputs`). The supported pulse falls to 1 and
  returns to 2 (`pulse_levels`) and stays at the sustaining need from step 2 on
  (`supported_pulse_recovers`); the unsupported pulse falls to 0 and stays there with every
  formation inactive (`unsupported_pulse_ends`). The recovered history is neither renewing nor
  consuming in the family's whole-time classification, on its unfolding and its web
  (`recovered_neither`, `recovered_web_neither`): the classification has a scope, which this states.

The amounts, thresholds and contribution schedule are the family's inputs; no source of them and
no ethical direction is inferred. Every declaration has an empty axiom report.
-/

namespace Becoming

open RelationalRenewal RelationalRenewal.Law

namespace SupportRecovery

/-! ## No third route -/

/-- **Where both formations have lost their support, the level stays.** -/
theorem absorbs (L : Law) (T : Nat) (fOff : L.level T < L.needF) (gOff : L.level T < L.needG) :
    ∀ n, L.level (T + n) = L.level T
  | 0 => rfl
  | n + 1 => by
    have before := absorbs L T fOff gOff n
    show L.level (T + n + 1) = L.level T
    rw [L.level_succ, before, if_neg (Nat.not_le_of_gt gOff), if_neg (Nat.not_le_of_gt fOff)]

/-! ## The window -/

/-- **A supported step of positive net repair raises the level by at least one**, whether or not
the sustaining formation is active. -/
theorem repair_step (L : Law) (t : Nat) (fOn : L.needF ≤ L.level t)
    (surplus : L.draw t < L.contrib t) : L.level t + 1 ≤ L.level (t + 1) := by
  have one : 1 ≤ L.contrib t - L.draw t := SupportGated.sub_pos_of_lt surplus
  rw [L.level_succ, if_pos fOn, if_pos fOn]
  cases Nat.lt_or_ge (L.level t) L.needG with
  | inl gOff =>
    rw [if_neg (Nat.not_le_of_gt gOff),
      SupportGated.add_sub_assoc_of_le _ (Nat.le_of_lt surplus)]
    exact Nat.add_le_add_left one _
  | inr gOn =>
    rw [if_pos gOn, SupportGated.add_sub_assoc_of_le _ (Nat.le_of_lt surplus), Nat.add_assoc]
    exact Nat.add_le_add_left (Nat.le_trans one (Nat.le_add_left _ _)) _

/-- **A window of supported positive net repair raises the level by at least its length**; the
repairing formation stays supported because the level never falls within the window. -/
theorem window_progress (L : Law) (T N : Nat) (fOn : L.needF ≤ L.level T)
    (surplus : ∀ d, d < N → L.draw (T + d) < L.contrib (T + d)) :
    ∀ d, d ≤ N → L.level T + d ≤ L.level (T + d)
  | 0, _ => Nat.le_refl _
  | d + 1, bound =>
    have prior := window_progress L T N fOn surplus d (Nat.le_of_succ_le bound)
    have active : L.needF ≤ L.level (T + d) :=
      Nat.le_trans fOn (Nat.le_trans (Nat.le_add_right _ d) prior)
    Nat.le_trans (Nat.succ_le_succ prior)
      (repair_step L (T + d) active (surplus d (Nat.lt_of_succ_le bound)))

/-! ## Two pulses -/

/-- Two histories from level 2, sustaining need 2, focal need 1, renewal 1: only the first draw
differs, and one unit is contributed at every later step. -/
def pulse (firstDraw : Nat) : Law :=
  ⟨2, 1, 2, 1, (fun | 0 => firstDraw | _ + 1 => 0), (fun | 0 => 0 | _ + 1 => 1)⟩

/-- **The two pulses draw and contribute the same after the first step.** -/
theorem same_later_inputs (n : Nat) :
    (pulse 2).draw (n + 1) = (pulse 3).draw (n + 1) ∧
      (pulse 2).contrib (n + 1) = (pulse 3).contrib (n + 1) :=
  ⟨rfl, rfl⟩

/-- **The levels of the two pulses**: both start at 2; the supported pulse falls to 1 and returns
to 2, the unsupported one falls to 0. The web's level is the law's. -/
theorem pulse_levels :
    (SupportGated.web (pulse 2)).level 0 () = 2 ∧ (SupportGated.web (pulse 3)).level 0 () = 2 ∧
      (SupportGated.web (pulse 2)).level 1 () = 1 ∧ (SupportGated.web (pulse 3)).level 1 () = 0 ∧
      (SupportGated.web (pulse 2)).level 2 () = 2 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

/-- **The supported pulse stays at the sustaining need from step 2 on.** -/
theorem supported_pulse_recovers (n : Nat) : 2 ≤ (pulse 2).level (2 + n) := by
  have grow := window_progress (pulse 2) 1 (n + 1) (Nat.le_refl 1)
    (fun d _ => by rw [Nat.add_comm 1 d]; exact Nat.zero_lt_one) (n + 1) (Nat.le_refl _)
  have index : 1 + (n + 1) = 2 + n := Nat.add_right_comm 1 n 1
  rw [index] at grow
  exact Nat.le_trans (Nat.succ_le_succ (Nat.le_add_right 1 n)) grow

/-- **The unsupported pulse stays at 0 from step 1 on, with every formation inactive** on its
web. -/
theorem unsupported_pulse_ends (n : Nat) :
    (SupportGated.web (pulse 3)).level (1 + n) () = 0 ∧
      ∀ p, ¬ (SupportGated.web (pulse 3)).active (1 + n) p :=
  have zero : (pulse 3).level (1 + n) = 0 :=
    absorbs (pulse 3) 1 Nat.zero_lt_one Nat.zero_lt_two n
  ⟨zero, fun p => match p with
    | .focal => fun active => Nat.not_succ_le_zero 0 (Nat.le_trans active (Nat.le_of_eq zero))
    | .sustaining => fun active => Nat.not_succ_le_zero 1 (Nat.le_trans active (Nat.le_of_eq zero))⟩

/-- **The recovered history is neither class**: a temporary loss followed by lasting restoration
is neither renewing at all times nor consuming for good. -/
theorem recovered_neither :
    ¬ RenewingIn (pulse 2).unfolding .focal ∧ ¬ ConsumingIn (pulse 2).unfolding .focal :=
  ⟨fun renewing => Nat.not_succ_le_self 1
      (renewing () (Or.inl Nat.zero_lt_one) 1 .sustaining trivial),
   fun ⟨_, _, g, T, _, lost⟩ =>
    have high := supported_pulse_recovers T
    have low := lost (2 + T) (Nat.le_add_left T 2)
    match g, low with
    | .focal, low => Nat.not_le_of_gt low (Nat.le_trans (Nat.le_succ 1) high)
    | .sustaining, low => Nat.not_le_of_gt low high⟩

/-- The recovered history is neither class on its web. -/
theorem recovered_web_neither :
    ¬ (SupportGated.web (pulse 2)).RenewingIn .focal ∧
      ¬ (SupportGated.web (pulse 2)).ConsumingIn .focal :=
  ⟨fun renewing => recovered_neither.1 ((Web.static_renewingIn _ _).mp renewing),
   fun consuming => recovered_neither.2 ((Web.static_consumingIn _ _).mp consuming)⟩

end SupportRecovery

end Becoming

end SupportRecovery
