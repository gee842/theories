/-!
# Renewing and consuming as a relation to participated conditions

One unfolding is read through the levels of conditions of further formation and the
formations whose continuation depends on them. A formation is classified by its
relation to the conditions of the relations it participates in: those it depends on
and those it draws on. It is renewing when every such condition remains at the level
supporting every formation that depends on it. It is consuming when it draws on a
condition that some dependent formation permanently loses. The two are exclusive and
not exhaustive: fluctuating and merely undergoing cases fall under neither.

No ethical predicate, no ranking and no added axiom occurs. Definitions state what
the classification means; theorems hold for arbitrary unfoldings or for every
parameter of the law family below. The arithmetic helpers are proved here so that
the module depends on no Lean axiom.

The law family represents a condition renewed by a formation that itself depends on
it (an organism and its vitality, a community and its commons, an ecosystem and its
soil), while a focal formation draws on it and may contribute to it. Because renewal
depends on the renewed condition, drawing it below that formation's support ends the
renewal itself: the loss does not return within the law. The levels, units and the
single shared condition are local representations; their correspondence to an actual
history is an application duty, not proved here. `formed` counts units of new
organization formed at active steps. It is the predicate a per-claim reading of
generation would credit, and it is not a measure of complexity.

Results: the classification is exclusive and renewal keeps every dependent formation
supported; unrenewed drawdown admits only finitely many active steps; within renewal,
formation continues and forms without bound; beyond renewal, the renewing relation
loses its support permanently, and a dependent focal formation ends itself with
bounded formation. Formation of new organization at every active step does not decide
the class, nor does the focal formation's own activity and formation over the whole
unfolding. Formations each within renewal alone can consume jointly, and escalation
that begins within renewal can consume.

The narrower law-class result `universal-ethics/generative-capacity/RenewingFormation.lean`
(record `renewing-consuming-formation`) bounds total formation under a supplied wear law
and adds a G0 interface. This module is independent of it: no import, no adapter.
-/

namespace RelationalRenewal

/-! ## Arithmetic without axioms -/

theorem add_sub_self : ∀ (n m : Nat), n + m - m = n
  | _, 0 => rfl
  | n, m + 1 => by
    have shift : n + (m + 1) = (n + 1) + m := (Nat.succ_add n m).symm
    show Nat.pred (n + (m + 1) - m) = n
    rw [shift, add_sub_self (n + 1) m]
    rfl

theorem sub_le_from_add {a c d : Nat} (h : a ≤ c + d) : a - d ≤ c := by
  have bound := Nat.sub_le_sub_right h d
  rw [add_sub_self] at bound
  exact bound

theorem le_sub_from_add {a b c : Nat} (h : a + b ≤ c) : a ≤ c - b := by
  have bound := Nat.sub_le_sub_right h b
  rw [add_sub_self] at bound
  exact bound

/-- A draw within renewal and contribution does not lower the level. -/
theorem keeps_level (l r c d : Nat) (within : d ≤ r + c) : l ≤ l + r + c - d := by
  apply le_sub_from_add
  rw [Nat.add_assoc]
  exact Nat.add_le_add_left within l

/-- A contribution no larger than the draw cannot raise the level. -/
theorem no_gain (l c d : Nat) (h : c ≤ d) : l + c - d ≤ l :=
  sub_le_from_add (Nat.add_le_add_left h l)

/-- A draw exceeding renewal and contribution lowers a positive level by at least one. -/
theorem strict_loss (l r c d : Nat) (over : r + c + 1 ≤ d) (positive : 1 ≤ l) :
    l + r + c - d + 1 ≤ l := by
  cases l with
  | zero => exact absurd positive (Nat.not_succ_le_zero 0)
  | succ k =>
    apply Nat.succ_le_succ
    apply sub_le_from_add
    have shape : k + 1 + r + c = k + (r + c + 1) := by
      rw [Nat.succ_add k r, Nat.succ_add (k + r) c, Nat.add_assoc]
      rfl
    rw [shape]
    exact Nat.add_le_add_left over k

theorem add_le_cancel {a : Nat} : ∀ {b : Nat}, a + b ≤ b → a ≤ 0
  | 0, h => h
  | _ + 1, h => add_le_cancel (Nat.le_of_succ_le_succ h)

/-- A loss of at least one at a step accumulates with earlier losses. -/
theorem accumulate {a b k B : Nat} (step : a + 1 ≤ b) (bound : b + k ≤ B) :
    a + (k + 1) ≤ B := by
  have total : Nat.succ a + k ≤ b + k := Nat.add_le_add_right step k
  have shape : Nat.succ a + k = Nat.succ (a + k) := Nat.succ_add a k
  rw [shape] at total
  exact Nat.le_trans total bound

/-! ## Relational classification of one unfolding -/

/-- Levels of conditions of further formation, the formations active at each step,
which conditions a formation's continuation depends on and at what level, and which
conditions its activity draws on. -/
structure Unfolding (F C : Type) where
  level : Nat → C → Nat
  active : Nat → F → Prop
  requires : F → C → Prop
  need : F → C → Nat
  draws : F → C → Prop

variable {F C : Type}

def Supported (U : Unfolding F C) (t : Nat) (f : F) : Prop :=
  ∀ c, U.requires f c → U.need f c ≤ U.level t c

/-- Dependence: a formation is active only where the conditions it requires support it. -/
def Dependent (U : Unfolding F C) : Prop :=
  ∀ t f, U.active t f → Supported U t f

/-- The condition stays at the level supporting every formation that depends on it. -/
def Renewed (U : Unfolding F C) (c : C) : Prop :=
  ∀ t g, U.requires g c → U.need g c ≤ U.level t c

/-- Some formation depending on the condition loses its support from some step on. -/
def Consumed (U : Unfolding F C) (c : C) : Prop :=
  ∃ g T, U.requires g c ∧ ∀ t, T ≤ t → U.level t c < U.need g c

/-- The relations a formation participates in, through dependence or drawing. -/
def Participates (U : Unfolding F C) (f : F) (c : C) : Prop :=
  U.requires f c ∨ U.draws f c

def RenewingIn (U : Unfolding F C) (f : F) : Prop :=
  ∀ c, Participates U f c → Renewed U c

def ConsumingIn (U : Unfolding F C) (f : F) : Prop :=
  ∃ c, U.draws f c ∧ Consumed U c

theorem renewed_not_consumed {U : Unfolding F C} {c : C}
    (renewed : Renewed U c) : ¬ Consumed U c := by
  rintro ⟨g, T, depends, lost⟩
  exact Nat.not_le_of_gt (lost T (Nat.le_refl T)) (renewed T g depends)

theorem renewing_not_consuming {U : Unfolding F C} {f : F}
    (renewing : RenewingIn U f) : ¬ ConsumingIn U f := by
  rintro ⟨c, drawn, consumed⟩
  exact renewed_not_consumed (renewing c (Or.inr drawn)) consumed

/-- Renewal keeps the renewing formation's own conditions supporting it at every step. -/
theorem renewing_keeps_support {U : Unfolding F C} {f : F}
    (renewing : RenewingIn U f) : ∀ t, Supported U t f :=
  fun t c depends => renewing c (Or.inl depends) t f depends

/-- A consumed condition ends every dependent formation it no longer supports. -/
theorem lost_support_ends {U : Unfolding F C} (dependent : Dependent U)
    {g : F} {c : C} {T : Nat} (depends : U.requires g c)
    (lost : ∀ t, T ≤ t → U.level t c < U.need g c) :
    ∀ t, T ≤ t → ¬ U.active t g :=
  fun t after active => Nat.not_le_of_gt (lost t after) (dependent t g active c depends)

theorem unrenewed_monotone {U : Unfolding F C} {c : C} {T0 : Nat}
    (unrenewed : ∀ t, T0 ≤ t → U.level (t + 1) c ≤ U.level t c)
    {t : Nat} (after : T0 ≤ t) : ∀ d, U.level (t + d) c ≤ U.level t c
  | 0 => Nat.le_refl _
  | d + 1 =>
    Nat.le_trans (unrenewed (t + d) (Nat.le_trans after (Nat.le_add_right t d)))
      (unrenewed_monotone unrenewed after d)

/-- When nothing renews a condition and each active step of a formation lowers it,
the formation is active only finitely often. Unlike a strict decrease at every step,
inactive intervals are allowed; renewal, not rest alone, is what is missing. -/
theorem unrenewed_drawdown_finite (U : Unfolding F C) (f : F) (c : C) (T0 : Nat)
    (unrenewed : ∀ t, T0 ≤ t → U.level (t + 1) c ≤ U.level t c)
    (lowers : ∀ t, T0 ≤ t → U.active t f → U.level (t + 1) c < U.level t c) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ U.active t f := by
  intro recurring
  have descent : ∀ k, ∃ t, T0 ≤ t ∧ U.level t c + k ≤ U.level T0 c := by
    intro k
    induction k with
    | zero => exact ⟨T0, Nat.le_refl T0, Nat.le_refl _⟩
    | succ k ih =>
      obtain ⟨t, after, bound⟩ := ih
      obtain ⟨t', later, active⟩ := recurring t
      obtain ⟨d, rfl⟩ := Nat.le.dest later
      have afterT0 : T0 ≤ t + d := Nat.le_trans after (Nat.le_add_right t d)
      have drop : U.level (t + d + 1) c + 1 ≤ U.level t c :=
        Nat.le_trans (lowers (t + d) afterT0 active) (unrenewed_monotone unrenewed after d)
      exact ⟨t + d + 1, Nat.le_trans afterT0 (Nat.le_succ _), accumulate drop bound⟩
  obtain ⟨t, _, bound⟩ := descent (U.level T0 c + 1)
  exact Nat.not_succ_le_self _ (Nat.le_trans (Nat.le_add_left _ _) bound)

/-- A seasonal level: support recurs without lasting. -/
def alternating : Nat → Nat
  | 0 => 1
  | 1 => 0
  | n + 2 => alternating n

theorem alternating_even : ∀ n, alternating (n + n) = 1
  | 0 => rfl
  | n + 1 => by
    have shape : (n + 1) + (n + 1) = (n + n) + 2 := by
      rw [Nat.succ_add n (n + 1)]
      rfl
    rw [shape]
    exact alternating_even n

def fluctuating : Unfolding Unit Unit where
  level t _ := alternating t
  active t _ := 1 ≤ alternating t
  requires _ _ := True
  need _ _ := 1
  draws _ _ := True

theorem fluctuating_dependent : Dependent fluctuating :=
  fun _ _ active _ _ => active

/-- The classification is not a forced dichotomy. -/
theorem fluctuating_neither :
    ¬ RenewingIn fluctuating () ∧ ¬ ConsumingIn fluctuating () := by
  have notRenewed : ¬ Renewed fluctuating () :=
    fun renewed => Nat.not_succ_le_zero 0 (renewed 1 () trivial)
  have notConsumed : ¬ Consumed fluctuating () := by
    rintro ⟨_, T, _, lost⟩
    have low := lost (T + T) (Nat.le_add_right T T)
    change alternating (T + T) < 1 at low
    rw [alternating_even] at low
    exact Nat.lt_irrefl 1 low
  exact ⟨fun renewing => notRenewed (renewing () (Or.inl trivial)),
    fun ⟨_, _, consumed⟩ => notConsumed consumed⟩

/-! ## A condition renewed by a formation that depends on it -/

/-- `renew` is added while the condition supports the sustaining formation (`needG`).
The focal formation is active while the condition supports it (`needF`; zero means
it does not depend on this condition); while active it contributes `contrib t` and
draws `draw t`. -/
structure Law where
  start : Nat
  renew : Nat
  needG : Nat
  needF : Nat
  draw : Nat → Nat
  contrib : Nat → Nat

namespace Law

def level (L : Law) : Nat → Nat
  | 0 => L.start
  | t + 1 =>
    if L.needG ≤ level L t then
      if L.needF ≤ level L t then level L t + L.renew + L.contrib t - L.draw t
      else level L t + L.renew
    else
      if L.needF ≤ level L t then level L t + L.contrib t - L.draw t
      else level L t

theorem level_succ (L : Law) (t : Nat) : L.level (t + 1) =
    if L.needG ≤ L.level t then
      if L.needF ≤ L.level t then L.level t + L.renew + L.contrib t - L.draw t
      else L.level t + L.renew
    else
      if L.needF ≤ L.level t then L.level t + L.contrib t - L.draw t
      else L.level t := rfl

/-- Units of new organization formed by the focal formation, one per active step. -/
def formed (L : Law) : Nat → Nat
  | 0 => 0
  | t + 1 => if L.needF ≤ level L t then formed L t + 1 else formed L t

theorem formed_at_active (L : Law) {t : Nat} (active : L.needF ≤ L.level t) :
    L.formed (t + 1) = L.formed t + 1 := by
  show (if L.needF ≤ L.level t then L.formed t + 1 else L.formed t) = L.formed t + 1
  rw [if_pos active]

theorem formed_at_inactive (L : Law) {t : Nat} (inactive : ¬ L.needF ≤ L.level t) :
    L.formed (t + 1) = L.formed t := by
  show (if L.needF ≤ L.level t then L.formed t + 1 else L.formed t) = L.formed t
  rw [if_neg inactive]

theorem formed_le (L : Law) : ∀ t, L.formed t ≤ t
  | 0 => Nat.le_refl 0
  | t + 1 => by
    cases Nat.lt_or_ge (L.level t) L.needF with
    | inl low =>
      rw [formed_at_inactive L (Nat.not_le_of_gt low)]
      exact Nat.le_succ_of_le (formed_le L t)
    | inr high =>
      rw [formed_at_active L high]
      exact Nat.succ_le_succ (formed_le L t)

/-- If the focal formation is active at every step, it forms at every step. -/
theorem formed_of_always (L : Law) (always : ∀ t, L.needF ≤ L.level t) :
    ∀ t, L.formed t = t
  | 0 => rfl
  | t + 1 => by rw [formed_at_active L (always t), formed_of_always L always t]

inductive Part where
  | focal
  | sustaining

def need (L : Law) : Part → Nat
  | .focal => L.needF
  | .sustaining => L.needG

def requiresPart (L : Law) : Part → Prop
  | .focal => 0 < L.needF
  | .sustaining => True

def drawsPart (L : Law) : Part → Prop
  | .focal => ∃ t, 0 < L.draw t
  | .sustaining => False

/-- The law read as one unfolding with one shared condition. -/
def unfolding (L : Law) : Unfolding Part Unit where
  level t _ := L.level t
  active t p := L.need p ≤ L.level t
  requires p _ := L.requiresPart p
  need p _ := L.need p
  draws p _ := L.drawsPart p

theorem unfolding_dependent (L : Law) : Dependent L.unfolding :=
  fun _ _ active _ _ => active

/-! ### Within renewal -/

theorem within_renewal_sustains (L : Law)
    (within : ∀ t, L.draw t ≤ L.renew + L.contrib t)
    (gStart : L.needG ≤ L.start) (fStart : L.needF ≤ L.start) :
    ∀ t, L.start ≤ L.level t
  | 0 => Nat.le_refl _
  | t + 1 => by
    have ih := within_renewal_sustains L within gStart fStart t
    have g : L.needG ≤ L.level t := Nat.le_trans gStart ih
    have f : L.needF ≤ L.level t := Nat.le_trans fStart ih
    rw [level_succ, if_pos g, if_pos f]
    exact Nat.le_trans ih (keeps_level _ _ _ _ (within t))

/-- Within renewal the focal formation is renewing, active at every step and forms
without bound. Renewal is not stasis. -/
theorem within_renewal_renewing (L : Law)
    (within : ∀ t, L.draw t ≤ L.renew + L.contrib t)
    (gStart : L.needG ≤ L.start) (fStart : L.needF ≤ L.start) :
    RenewingIn L.unfolding .focal ∧ (∀ t, L.unfolding.active t .focal) ∧
      ∀ t, L.formed t = t := by
  have kept := within_renewal_sustains L within gStart fStart
  have always : ∀ t, L.needF ≤ L.level t := fun t => Nat.le_trans fStart (kept t)
  refine ⟨?_, always, formed_of_always L always⟩
  intro _ _ t p _
  cases p with
  | focal => exact always t
  | sustaining => exact Nat.le_trans gStart (kept t)

/-! ### Beyond renewal -/

/-- Once the condition falls below the sustaining formation's support, its renewal
has ended, and a focal formation that restores no more than it draws cannot raise it
again: the loss does not return within the law. -/
theorem no_return_below_support (L : Law) {T : Nat}
    (noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t)
    (below : L.level T < L.needG) : ∀ d, L.level (T + d) ≤ L.level T
  | 0 => Nat.le_refl _
  | d + 1 => by
    have ih := no_return_below_support L noRestore below d
    have off : ¬ L.needG ≤ L.level (T + d) :=
      fun on => Nat.not_le_of_gt below (Nat.le_trans on ih)
    show L.level (T + d + 1) ≤ L.level T
    rw [level_succ, if_neg off]
    cases Nat.lt_or_ge (L.level (T + d)) L.needF with
    | inl low =>
      rw [if_neg (Nat.not_le_of_gt low)]
      exact ih
    | inr high =>
      rw [if_pos high]
      exact Nat.le_trans
        (no_gain _ _ _ (noRestore (T + d) (Nat.le_add_right T d))) ih

theorem permanently_below (L : Law) {T : Nat}
    (noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t) {bound : Nat}
    (below : L.level T < bound) (within : bound ≤ L.needG) :
    ∀ t, T ≤ t → L.level t < bound := by
  intro t after
  obtain ⟨d, rfl⟩ := Nat.le.dest after
  exact Nat.lt_of_le_of_lt
    (no_return_below_support L noRestore (Nat.lt_of_lt_of_le below within) d) below

/-- Drawing beyond renewal and contribution takes the condition below the sustaining
formation's support within as many steps as the level it started from. -/
theorem overdraw_crosses_support (L : Law) (positive : 0 < L.needG)
    (fWithin : L.needF ≤ L.needG) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    ∃ T, T0 ≤ T ∧ T ≤ T0 + L.level T0 ∧ L.level T < L.needG := by
  have descent : ∀ k, (∃ T, T0 ≤ T ∧ T ≤ T0 + k ∧ L.level T < L.needG) ∨
      L.level (T0 + k) + k ≤ L.level T0 := by
    intro k
    induction k with
    | zero => exact Or.inr (Nat.le_refl _)
    | succ k ih =>
      cases ih with
      | inl found =>
        obtain ⟨T, after, before, low⟩ := found
        exact Or.inl ⟨T, after, Nat.le_succ_of_le before, low⟩
      | inr bound =>
        cases Nat.lt_or_ge (L.level (T0 + k)) L.needG with
        | inl low =>
          exact Or.inl ⟨T0 + k, Nat.le_add_right T0 k, Nat.le_succ _, low⟩
        | inr high =>
          refine Or.inr ?_
          have fOn : L.needF ≤ L.level (T0 + k) := Nat.le_trans fWithin high
          have step : L.level (T0 + k + 1) + 1 ≤ L.level (T0 + k) := by
            rw [level_succ, if_pos high, if_pos fOn]
            exact strict_loss _ _ _ _ (over (T0 + k) (Nat.le_add_right T0 k))
              (Nat.le_trans positive high)
          exact accumulate step bound
  cases descent (L.level T0) with
  | inl found => exact found
  | inr bound =>
    exact ⟨T0 + L.level T0, Nat.le_add_right _ _, Nat.le_refl _,
      Nat.lt_of_le_of_lt (add_le_cancel bound) positive⟩

/-- Drawing beyond renewal consumes: the sustaining formation loses its support for
ever, whether or not the focal formation depends on the condition. -/
theorem overdraw_consuming (L : Law) (positive : 0 < L.needG)
    (fWithin : L.needF ≤ L.needG) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    ConsumingIn L.unfolding .focal ∧
      ∃ T, ∀ t, T ≤ t → ¬ L.unfolding.active t .sustaining := by
  obtain ⟨T, after, _, low⟩ := overdraw_crosses_support L positive fWithin over
  have noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t := fun t later =>
    Nat.le_of_lt (Nat.lt_of_le_of_lt (Nat.le_add_left _ _)
      (over t (Nat.le_trans after later)))
  have lost := permanently_below L noRestore low (Nat.le_refl _)
  have draws : 0 < L.draw T0 :=
    Nat.lt_of_le_of_lt (Nat.zero_le _) (over T0 (Nat.le_refl T0))
  exact ⟨⟨(), ⟨T0, draws⟩, .sustaining, T, trivial, lost⟩,
    T, lost_support_ends (unfolding_dependent L) (g := .sustaining) (c := ()) trivial lost⟩

/-- A focal formation that depends on the condition and draws beyond its renewal ends
itself as well, and forms only boundedly much: it forms and then ceases. -/
theorem dependent_overdraw_ends_itself (L : Law) (fPositive : 0 < L.needF)
    (fWithin : L.needF ≤ L.needG) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    ∃ T, (∀ t, T ≤ t → ¬ L.unfolding.active t .focal) ∧ ∀ t, L.formed t ≤ T := by
  have descent : ∀ k, (∃ T, T0 ≤ T ∧ L.level T < L.needF) ∨
      L.level (T0 + k) + k ≤ L.level T0 := by
    intro k
    induction k with
    | zero => exact Or.inr (Nat.le_refl _)
    | succ k ih =>
      cases ih with
      | inl found => exact Or.inl found
      | inr bound =>
        cases Nat.lt_or_ge (L.level (T0 + k)) L.needF with
        | inl low => exact Or.inl ⟨T0 + k, Nat.le_add_right T0 k, low⟩
        | inr high =>
          refine Or.inr ?_
          have overHere := over (T0 + k) (Nat.le_add_right T0 k)
          have positiveHere : 1 ≤ L.level (T0 + k) := Nat.le_trans fPositive high
          have step : L.level (T0 + k + 1) + 1 ≤ L.level (T0 + k) := by
            rw [level_succ]
            cases Nat.lt_or_ge (L.level (T0 + k)) L.needG with
            | inl gOff =>
              rw [if_neg (Nat.not_le_of_gt gOff), if_pos high]
              have overAlone : 0 + L.contrib (T0 + k) + 1 ≤ L.draw (T0 + k) := by
                rw [Nat.zero_add]
                exact Nat.le_trans
                  (Nat.succ_le_succ (Nat.le_add_left _ _)) overHere
              exact strict_loss _ 0 _ _ overAlone positiveHere
            | inr gOn =>
              rw [if_pos gOn, if_pos high]
              exact strict_loss _ _ _ _ overHere positiveHere
          exact accumulate step bound
  have found : ∃ T, T0 ≤ T ∧ L.level T < L.needF := by
    cases descent (L.level T0) with
    | inl found => exact found
    | inr bound =>
      exact ⟨T0 + L.level T0, Nat.le_add_right _ _,
        Nat.lt_of_le_of_lt (add_le_cancel bound) fPositive⟩
  obtain ⟨T, after, low⟩ := found
  have noRestore : ∀ t, T ≤ t → L.contrib t ≤ L.draw t := fun t later =>
    Nat.le_of_lt (Nat.lt_of_le_of_lt (Nat.le_add_left _ _)
      (over t (Nat.le_trans after later)))
  have lost := permanently_below L noRestore low fWithin
  have ended : ∀ t, T ≤ t → ¬ L.unfolding.active t .focal :=
    fun t later active => Nat.not_le_of_gt (lost t later) active
  refine ⟨T, ended, ?_⟩
  have still : ∀ d, L.formed (T + d) = L.formed T := by
    intro d
    induction d with
    | zero => rfl
    | succ d ih =>
      show L.formed (T + d + 1) = L.formed T
      rw [formed_at_inactive L (ended (T + d) (Nat.le_add_right T d)), ih]
  intro t
  cases Nat.lt_or_ge t T with
  | inl early => exact Nat.le_trans (formed_le L t) (Nat.le_of_lt early)
  | inr late =>
    obtain ⟨d, rfl⟩ := Nat.le.dest late
    rw [still d]
    exact formed_le L T

/-- A focal formation independent of the condition can draw beyond its renewal,
continue at every step and form without bound, while the formation that depends on
the condition loses it for ever. Persistence and success do not certify renewal. -/
theorem independent_overdraw_persists (L : Law) (independent : L.needF = 0)
    (positive : 0 < L.needG) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    (∀ t, L.unfolding.active t .focal) ∧ (∀ t, L.formed t = t) ∧
      ConsumingIn L.unfolding .focal := by
  have always : ∀ t, L.needF ≤ L.level t := fun t => independent ▸ Nat.zero_le _
  exact ⟨always, formed_of_always L always,
    (overdraw_consuming L positive (independent ▸ Nat.zero_le _) over).1⟩

/-! ## Distinctions that formation of new organization cannot make -/

/-- Cultivation: draws and contributes, keeping its condition renewed. -/
def cultivation : Law := ⟨2, 1, 1, 1, fun _ => 2, fun _ => 1⟩
/-- Malignant growth: depends on a condition renewed by the organization it belongs to
and draws beyond that renewal. -/
def malignant : Law := ⟨4, 1, 2, 1, fun _ => 3, fun _ => 0⟩

/-- Both form one new unit of organization at every step at which they are active.
One continues and forms without bound; the other consumes the condition of the
relation it belongs to, ends itself and forms boundedly much. -/
theorem formation_does_not_decide :
    (∀ L : Law, ∀ t, L.needF ≤ L.level t → L.formed (t + 1) = L.formed t + 1) ∧
    (RenewingIn cultivation.unfolding .focal ∧ ∀ t, cultivation.formed t = t) ∧
    (malignant.formed 1 = 1 ∧ ConsumingIn malignant.unfolding .focal ∧
      ∃ T, (∀ t, T ≤ t → ¬ malignant.unfolding.active t .focal) ∧
        ∀ t, malignant.formed t ≤ T) := by
  have cult := within_renewal_renewing cultivation (fun _ => Nat.le_refl 2)
    (Nat.le_succ 1) (Nat.le_succ 1)
  have over : ∀ t, 0 ≤ t → malignant.renew + malignant.contrib t < malignant.draw t :=
    fun _ _ => Nat.lt_succ_of_le (Nat.le_succ 1)
  exact ⟨fun L _ active => formed_at_active L active, ⟨cult.1, cult.2.2⟩, rfl,
    (overdraw_consuming malignant (Nat.succ_pos 1) (Nat.le_succ 1) over).1,
    dependent_overdraw_ends_itself malignant (Nat.succ_pos 0) (Nat.le_succ 1) over⟩

/-- Use within renewal. -/
def sharing : Law := ⟨3, 1, 1, 0, fun _ => 1, fun _ => 0⟩
/-- The same formation drawing beyond renewal: the winner of a contest that removes the
other side's conditions, or an externality its source does not depend on. -/
def winning : Law := ⟨3, 1, 1, 0, fun _ => 2, fun _ => 0⟩

/-- The focal formation's own activity and formation are identical at every step of
the two unfoldings; one is renewing and the other consuming. No predicate of a
formation's own trajectory, including its persistence, success or growth, decides the
class: it is a relation to the conditions of the relations it participates in. -/
theorem own_trajectory_does_not_decide :
    (∀ t, sharing.unfolding.active t .focal ↔ winning.unfolding.active t .focal) ∧
    (∀ t, sharing.formed t = winning.formed t) ∧
    RenewingIn sharing.unfolding .focal ∧ ConsumingIn winning.unfolding .focal := by
  have share := within_renewal_renewing sharing (fun _ => Nat.le_refl 1)
    (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
  have win := independent_overdraw_persists winning rfl (Nat.succ_pos 0) (T0 := 0)
    (fun _ _ => Nat.lt_succ_self 1)
  refine ⟨fun t => ⟨fun _ => win.1 t, fun _ => share.2.1 t⟩, ?_, share.1, win.2.2⟩
  intro t
  rw [share.2.2 t, win.2.1 t]

/-- One formation drawing alone on a condition it shares. -/
def alone (start renew need : Nat) (d : Nat → Nat) : Law :=
  ⟨start, renew, need, need, d, fun _ => 0⟩

/-- Two formations sharing one condition at the same dependence level are active at the
same steps, so their joint drawing is one law with the summed draw. -/
def together (start renew need : Nat) (d1 d2 : Nat → Nat) : Law :=
  ⟨start, renew, need, need, fun t => d1 t + d2 t, fun _ => 0⟩

/-- Each alone stays within renewal; together they consume, and both end with the
relation that renews their condition. No single participant is the consumer: the class
belongs to their joint relation. -/
theorem jointly_consuming (start renew need : Nat) (d1 d2 : Nat → Nat)
    (within1 : ∀ t, d1 t ≤ renew) (within2 : ∀ t, d2 t ≤ renew)
    (joint : ∀ t, renew < d1 t + d2 t) (positive : 0 < need) (supported : need ≤ start) :
    RenewingIn (alone start renew need d1).unfolding .focal ∧
    RenewingIn (alone start renew need d2).unfolding .focal ∧
    ConsumingIn (together start renew need d1 d2).unfolding .focal ∧
    ∃ T, ∀ t, T ≤ t → ¬ (together start renew need d1 d2).unfolding.active t .focal ∧
      ¬ (together start renew need d1 d2).unfolding.active t .sustaining := by
  have over : ∀ t, 0 ≤ t → renew + 0 < d1 t + d2 t := fun t _ => joint t
  obtain ⟨T, ended, _⟩ := dependent_overdraw_ends_itself
    (together start renew need d1 d2) positive (Nat.le_refl _) over
  exact ⟨(within_renewal_renewing _ within1 supported supported).1,
    (within_renewal_renewing _ within2 supported supported).1,
    (overdraw_consuming _ positive (Nat.le_refl _) over).1,
    T, fun t later => ⟨ended t later, ended t later⟩⟩

/-- Escalation: each step's draw answers the last, forming more organization while the
draw stays within renewal at first. Once it exceeds renewal it consumes, and the
formation ends with the relation it depends on. -/
def escalation : Law := ⟨3, 2, 1, 1, fun t => t, fun _ => 0⟩

theorem escalation_consumes :
    (∀ t, t ≤ 2 → escalation.draw t ≤ escalation.renew + escalation.contrib t) ∧
    escalation.level 3 = 6 ∧ escalation.formed 3 = 3 ∧
    ConsumingIn escalation.unfolding .focal ∧
    ∃ T, (∀ t, T ≤ t → ¬ escalation.unfolding.active t .focal) ∧
      ∀ t, escalation.formed t ≤ T := by
  have over : ∀ t, 3 ≤ t → escalation.renew + escalation.contrib t < escalation.draw t :=
    fun _ later => later
  exact ⟨fun _ early => early, rfl, rfl,
    (overdraw_consuming escalation (Nat.succ_pos 0) (Nat.le_refl 1) over).1,
    dependent_overdraw_ends_itself escalation (Nat.succ_pos 0) (Nat.le_refl 1) over⟩

end Law

end RelationalRenewal
