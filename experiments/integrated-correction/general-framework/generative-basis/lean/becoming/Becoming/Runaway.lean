import Becoming.Testing

/-!
# Runaway: what a loop through its own registration cannot register

On 11 October 2026 Ren asked for "wisdoms to avoid run away feedbacks". `Becoming.Testing`
states threshold blindness for an exchange that follows a formation's registration
(`Flow.ExchangeFollows`), and reads a runaway as a loop running inside it. This module states,
with no premise beyond balance on the conditions registered, what that means for every
policy and how far the blindness reaches. Ren's reply to the proposal was "no extra review
needed, merge, then continue".

* **Every policy through registration.** A formation's policy goes through its registration
  when its own exchange on what it registers is alike wherever it has registered alike
  (`Flow.PolicyThrough`). With the rest of the exchange on what it registers fixed
  (`Flow.OthersFixed`), the exchange then follows its registration
  (`Flow.exchangeFollows_of_policy`). So for every such policy, a difference in a stock the
  formation depends on and does not observe is never used while the lower web supports it
  (`Flow.policy_keeps_difference`), and wherever the difference has been used, the lower web
  failed to support the formation at some earlier step (`Flow.policy_uses_after_failure`).
* **The distance to the break is not registered.** Raising a stock by `d` (`Web.raise`) keeps
  balance on every condition (`Flow.BalancesOn.raise`). At every step at which a web supports
  a formation that does not observe the stock, the raised web registers alike for it
  (`Web.alikeThrough_raise`). So before the break nothing the formation registers bounds how
  near the break is: for every horizon, where the stock is the only requirement that may be
  unmet up to it, some raised web registers alike at every step at which the actual web
  supports the formation, and supports it at every step up to the horizon
  (`Web.break_not_bounded`); the raised web is dependent where the web is
  (`Web.Dependent.raise`). `SupportDrawn.break_uncoupled` is an instance.
* **Observation registers it.** Observing the stock, a formation registers any raise at once
  (`Web.observed_raise_couples`).

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D26).**
- A runaway is a loop whose registration cannot register the distance to its break: before the
  break, its own registration is the same as in a world with as much more stock as one likes.
  Its policy, however clever, cannot use what it does not register.
- To avoid a runaway without forgoing what is there, a formation needs what registers the
  stock (measurement), or a model of it (理, a model answerable to registration), or another
  formation whose registration does (`Becoming.Testing`); experiment needs a return and a model
  of what is irrelevant (`Becoming.Experiment`).

What is not derived: that a formation draws more than is renewed, wants to keep its support,
or forms a policy; which formations respond to what. No ethical predicate, ranking or axiom
occurs.
-/

namespace Becoming

variable {F C : Type}

/-! ## Every policy through registration -/

namespace Flow

variable {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop} {g : F}

/-- `g`'s policy goes through its registration: wherever `g` has registered alike up to `t`,
its own take from and give to every condition it registers are alike across the step from
`t`. -/
def PolicyThrough (L : Flow F C) (W : Web F C) (L' : Flow F C) (W' : Web F C)
    (obs : F → C → Prop) (g : F) : Prop :=
  ∀ t, W.AlikeThroughUpTo obs g W.level W'.level t → ∀ c, W.CoupledInto obs g c →
    L.take t g c = L'.take t g c ∧ L.give t g c = L'.give t g c

/-- The rest of the exchange on what `g` registers is fixed: every other formation takes from
and gives to every condition `g` registers alike in the two flows, at every step. -/
def OthersFixed (L : Flow F C) (W : Web F C) (L' : Flow F C) (obs : F → C → Prop) (g : F) :
    Prop :=
  ∀ t h c, h ≠ g → W.CoupledInto obs g c → L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c

/-- **A policy through registration, with the rest fixed, is exchange following
registration.** -/
theorem exchangeFollows_of_policy [DecidableEq F] (present : ∀ t, L.present t = L'.present t)
    (policy : PolicyThrough L W L' W' obs g) (others : OthersFixed L W L' obs g) :
    L.ExchangeFollows W L' W' obs g :=
  fun t alike c registers =>
    have each : ∀ h, h ∈ L.present t → L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c :=
      fun h _ => match decEq h g with
        | isTrue same => same ▸ policy t alike c registers
        | isFalse other => others t h c other registers
    ⟨(total_congr_on fun h mem => (each h mem).1).trans
        (congrArg (fun as => total as fun h => L'.take t h c) (present t)),
     (total_congr_on fun h mem => (each h mem).2).trans
        (congrArg (fun as => total as fun h => L'.give t h c) (present t))⟩

/-- **A policy that keeps its support never uses a larger stock.** For every policy through
registration, with the rest fixed: where the starts differ only in a stock `g` depends on and
does not observe, `d` higher in the second, and the first web supports `g` at every step, the
stock stands `d` higher at every step and `g` registers alike. -/
theorem policy_keeps_difference [DecidableEq F] [DecidableEq C] {c : C} {d : Nat}
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (present : ∀ t, L.present t = L'.present t)
    (policy : PolicyThrough L W L' W' obs g) (others : OthersFixed L W L' obs g)
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.CoupledInto obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (supported : ∀ t, W.Supported t g) :
    ∀ t, W'.level t c = W.level t c + d ∧ W.AlikeThrough obs g W.level W'.level t :=
  subthreshold_alike_always balanced balanced' depends unobserved stock start
    (exchangeFollows_of_policy present policy others) supported

/-- **A larger stock is used only after a failure.** For every policy through registration,
with the rest fixed, starting at least as high on what `g` registers and alike on what it
observes: wherever a difference on a condition `g` registers has changed by a step, the first
web did not support `g` at every earlier step. -/
theorem policy_uses_after_failure [DecidableEq F]
    (balanced : ∀ t e, W.CoupledInto obs g e → L.BalancesOn W [e] t)
    (balanced' : ∀ t e, W.CoupledInto obs g e → L'.BalancesOn W' [e] t)
    (present : ∀ t, L.present t = L'.present t)
    (policy : PolicyThrough L W L' W' obs g) (others : OthersFixed L W L' obs g)
    (higher : ∀ e, W.CoupledInto obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e) {t : Nat} {e : C}
    (registers : W.CoupledInto obs g e)
    (changed : W'.level t e + W.level 0 e ≠ W.level t e + W'.level 0 e) :
    ¬ ∀ s, s < t → W.Supported s g :=
  fun supported => (difference_changes_after_divergence balanced balanced' higher observedAlike
    (exchangeFollows_of_policy present policy others) registers changed).1
    fun s before _ => supported s before

end Flow

/-! ## The distance to the break is not registered -/

namespace Web

variable (W : Web F C)

/-- The web with the stock `c` raised by `d` at every step, all else as it is. -/
def raise [DecidableEq C] (c : C) (d : Nat) : Web F C :=
  { W with level := fun t e => W.level t e + if e = c then d else 0 }

variable {W} {obs : F → C → Prop} {g : F}

/-- A raised web stands at least as high. -/
theorem le_raise [DecidableEq C] (c : C) (d t : Nat) (e : C) :
    W.level t e ≤ (W.raise c d).level t e :=
  Nat.le_add_right _ _

/-- A raised web supports whatever the web supports. -/
theorem Supported.raise [DecidableEq C] {t : Nat} (supported : W.Supported t g) (c : C)
    (d : Nat) : (W.raise c d).Supported t g :=
  fun e requires => Nat.le_trans (supported e requires) (le_raise c d t e)

/-- Away from the raised stock the levels stand as they are. -/
theorem raise_other [DecidableEq C] {c e : C} (other : e ≠ c) (d t : Nat) :
    (W.raise c d).level t e = W.level t e :=
  congrArg (W.level t e + ·) (if_neg other)

/-- **Before the break, a raise does not register.** At every step at which the web supports
`g`, a raise of a stock `g` does not observe registers alike for it. -/
theorem alikeThrough_raise [DecidableEq C] {c : C} (unobserved : ¬ obs g c) (d : Nat)
    {t : Nat} (supported : W.Supported t g) :
    W.AlikeThrough obs g W.level (W.raise c d).level t :=
  ⟨⟨fun _ e requires => Nat.le_trans (supported e requires) (le_raise c d t e),
    fun _ => supported⟩,
   fun e observed => (raise_other (W := W) (fun same : e = c => unobserved (same ▸ observed)) d t).symm⟩

/-- **Observation registers a raise at once.** Observing the stock, any positive raise is
registered at every step. -/
theorem observed_raise_couples [DecidableEq C] {c : C} (observed : obs g c) {d : Nat}
    (pos : 0 < d) (t : Nat) : ¬ W.AlikeThrough obs g W.level (W.raise c d).level t :=
  Web.observed_level_couples observed fun same =>
    Nat.ne_of_lt (Nat.lt_add_of_pos_right (n := W.level t c) (if_pos rfl ▸ pos))
      (same.trans rfl)

/-- The needs of `g` on `c` at the steps up to `u`, summed. -/
def needUpTo (g : F) (c : C) : Nat → Nat
  | 0 => W.need 0 g c
  | u + 1 => needUpTo g c u + W.need (u + 1) g c

/-- Each need up to `u` is at most their sum. -/
theorem need_le_needUpTo (g : F) (c : C) : ∀ {s u : Nat}, s ≤ u → W.need s g c ≤ W.needUpTo g c u
  | s, 0, le => match s, le with
    | 0, _ => Nat.le_refl _
  | s, _ + 1, le => match Nat.lt_or_eq_of_le le with
    | .inl before => Nat.le_trans (need_le_needUpTo g c (Nat.le_of_lt_succ before))
        (Nat.le_add_right _ _)
    | .inr same => match s, same with
      | _, rfl => Nat.le_add_left _ _

/-- A raised web is dependent where the web is: activity is unchanged and support only grows. -/
theorem Dependent.raise [DecidableEq C] (dependent : W.Dependent) (c : C) (d : Nat) :
    (W.raise c d).Dependent :=
  fun t f active => (dependent t f active).raise c d

/-- **No registered bound on the break.** Let `g` not observe a stock `c`, and let `c` be the
only requirement of `g` that may be unmet at the steps up to a horizon `u`. Then some raise of
`c` registers alike for `g` at every step at which the web supports `g`, and supports `g` at
every step up to `u`. So before the break nothing `g` registers bounds how far off it is. -/
theorem break_not_bounded [DecidableEq C] {c : C} (unobserved : ¬ obs g c) (u : Nat)
    (others : ∀ s, s ≤ u → ∀ e, e ≠ c → W.requires s g e → W.need s g e ≤ W.level s e) :
    ∃ d, (∀ s, s ≤ u → (W.raise c d).Supported s g) ∧
      ∀ t, W.Supported t g → W.AlikeThrough obs g W.level (W.raise c d).level t :=
  ⟨W.needUpTo g c u,
   fun s le e requires => match decEq e c with
    | isTrue same => match e, same, requires with
      | _, rfl, _ =>
        have raised : (W.raise c (W.needUpTo g c u)).level s c = W.level s c + W.needUpTo g c u :=
          congrArg (W.level s c + ·) (if_pos rfl)
        Nat.le_trans (Nat.le_trans (W.need_le_needUpTo g c le) (Nat.le_add_left _ (W.level s c)))
          (Nat.le_of_eq raised.symm)
    | isFalse other => Nat.le_trans (others s le e other requires) (le_raise c _ s e),
   fun _ supported => alikeThrough_raise unobserved _ supported⟩

end Web

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- **Raising a stock keeps balance.** Where a flow balances on a family across a step, it
balances there on the raised web. -/
theorem BalancesOn.raise [DecidableEq C] {cs : List C} {t : Nat} (balanced : L.BalancesOn W cs t)
    (c : C) (d : Nat) : L.BalancesOn (W.raise c d) cs t :=
  fun e mem =>
    (Nat.add_right_comm _ _ _).trans
      ((congrArg (· + _) (balanced e mem)).trans (Nat.add_right_comm _ _ _))

end Flow

/-! ## An instance -/

namespace SupportDrawn

/-- **The break, unregistered.** In the lower web the formation is unsupported at the third
step; a raise of its stock registers alike for it at every step at which the lower web
supports it, supports it at the third step, and keeps the flow balanced. -/
theorem break_uncoupled :
    ¬ (web lowerLevel).Supported 2 () ∧
      ∃ d, ((web lowerLevel).raise () d).Supported 2 () ∧
        (∀ t, (web lowerLevel).Supported t () →
          (web lowerLevel).AlikeThrough thresholdOnly () (web lowerLevel).level
            ((web lowerLevel).raise () d).level t) ∧
        ∀ t, (flow lowerDraw).BalancesOn ((web lowerLevel).raise () d) [()] t :=
  match (web lowerLevel).break_not_bounded (obs := thresholdOnly) (g := ()) (c := ())
      (fun no => no) 2 (fun _ _ () other => absurd rfl other) with
  | ⟨d, supports, alike⟩ =>
    ⟨fun supported => Nat.not_succ_le_zero 0 (supported () trivial), d,
     supports 2 (Nat.le_refl 2), alike, fun t => (lower_balances.on [()] t).raise () d⟩

end SupportDrawn

end Becoming
