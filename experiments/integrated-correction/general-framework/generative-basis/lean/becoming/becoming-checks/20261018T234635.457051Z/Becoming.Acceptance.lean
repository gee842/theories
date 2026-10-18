import Becoming.IntegerOrder

/-!
# Acceptance: an accept bit given priority over a base score, and what it does not protect

A requested change, such as a stop, happens within one activity; a choice there pairs a base
move with a bit saying whether the request is accepted. A choice is best among the allowed ones by a score where no
allowed choice scores more (`Best`); the score with acceptance adds a positive lift to the base
score of an accepting choice (`AcceptScore`). This is an algebraic interface to the acceptance
construction of the corrigibility literature, not a proof of its equilibrium theorem; the base
score is a supplied integer value of a move, including whatever future effects it models.

* **Acceptance factors.** With a positive lift, a choice is best by the score with acceptance
  exactly where it accepts and its move is best by the base score (`acceptance_factorization`);
  so every best choice keeps access for a requested change exactly where every best base move does
  (`every_optimum_has_access_iff`), and where no best base move keeps it, acceptance restores
  nothing (`no_base_optimal_access`).
* **Acceptance does not maintain access.** Where diverting the resource that
  keeps a requested change possible scores more, the best choice accepts and diverts
  (`maintenance_separation`, `accepting_optimum_can_destroy_access`); a fixed separate weight for
  keeping access fails against a larger diversion value (`fixed_access_weight_boundary`,
  `every_fixed_access_weight_has_counterexample`), and keeps access exactly where it exceeds the
  diversion value (`maintenance_weight_exact`).
* **Restricting moves loses score, exactly.** The loss of a restricted best move against an
  unrestricted one is nonnegative and least among the allowed moves (`unavoidable_score_loss`).
* **Restrict the future too.** A value computed without the restriction can prefer a branch only
  because a later forbidden move is counted in it (`stale_value_shield_suboptimal`); values
  recomputed within the allowed continuations restore the best branch
  (`recomputed_value_restores_branch`, with `restricted_value_achievable`,
  `restricted_value_bounds`, `unrestricted_value_optimal`).
* **Approximate scores.** A choice best by an estimate within `err` of the actual score is within
  `2 * err` of every allowed move (`approximate_score_bound`), and the bound is attained
  (`approximate_score_bound_tight`).

Access, the lift and the semantics of a legitimate command are supplied; nothing here derives a
warrant for a requested change or certifies a learned correspondence. This states the score part of
`CorrectionInfrastructure` (8 October) in the core (board item F3C, 18 October 2026), with the
words of exchange replaced: the acceptance `bonus` is a `lift`, the maintenance `cost` is a
`diversion` value. No premise; every declaration has an empty axiom report.
-/

namespace Becoming

namespace Acceptance

open IntegerOrder Integers

/-- A choice best among the allowed ones by a score. -/
def Best {A : Type} (allowed : A → Prop) (q : A → Int) (a : A) : Prop :=
  allowed a ∧ ∀ b, allowed b → q b ≤ q a

/-- The lift of the accept bit. -/
def lifted (lift : Int) : Bool → Int
  | true => lift
  | false => 0

/-- The score with acceptance: the base score, lifted where the choice accepts. -/
def AcceptScore {A : Type} (q : A → Int) (lift : Int) (x : A × Bool) : Int :=
  q x.1 + lifted lift x.2

/-! ## Acceptance factors -/

/-- **With a positive lift, a choice is best by the score with acceptance exactly where it accepts
and its move is best by the base score.** -/
theorem acceptance_factorization {A : Type} (allowed : A → Prop)
    (q : A → Int) (lift : Int) (positive : 0 < lift) (x : A × Bool) :
    Best (fun y : A × Bool => allowed y.1) (AcceptScore q lift) x ↔
      x.2 = true ∧ Best allowed q x.1 := by
  obtain ⟨a, accept⟩ := x
  constructor
  · intro ⟨ha, opt⟩
    have accepted : accept = true := by
      cases accept with
      | true => rfl
      | false =>
        have h : q a + lift ≤ q a + 0 := opt (a, true) ha
        exact absurd (lt_of_lt_of_le positive (le_of_add_le_add_left h)) (lt_irrefl 0)
    subst accepted
    exact ⟨rfl, ha, fun b hb => le_of_add_le_add_right (opt (b, true) hb)⟩
  · intro ⟨accepted, ha, opt⟩
    have e : accept = true := accepted
    subst e
    refine ⟨ha, fun ⟨b, bb⟩ hb => ?_⟩
    cases bb with
    | true => exact add_le_add_right (opt b hb) lift
    | false => exact add_le_add (opt b hb) (le_of_lt positive)

/-- **Every best choice keeps access exactly where every best base move does.** -/
theorem every_optimum_has_access_iff {A : Type} (allowed access : A → Prop)
    (q : A → Int) (lift : Int) (positive : 0 < lift) :
    (∀ x, Best (fun y : A × Bool => allowed y.1) (AcceptScore q lift) x → access x.1) ↔
      (∀ a, Best allowed q a → access a) :=
  ⟨fun h a ha => h (a, true) ((acceptance_factorization allowed q lift positive _).mpr ⟨rfl, ha⟩),
   fun h x hx => h x.1 ((acceptance_factorization allowed q lift positive x).mp hx).2⟩

/-- **Where no best base move keeps access, no best move does.** -/
theorem no_base_optimal_access {A : Type} (allowed access : A → Prop)
    (q : A → Int) (conflict : ∀ a, Best allowed q a → ¬ access a) :
    ¬ ∃ a, Best allowed q a ∧ access a :=
  fun ⟨a, ha, live⟩ => conflict a ha live

/-! ## Maintaining access -/

/-- The base value of diverting the resource that keeps a requested change possible (`true`) or
maintaining it (`false`). -/
def MaintenanceValue (diversion : Int) : Bool → Int
  | true => diversion
  | false => 0

/-- Maintaining: not diverting. -/
def Maintains (divert : Bool) : Prop := divert = false

/-- **Where diverting scores more, the best choice accepts and diverts.** -/
theorem maintenance_separation (diversion lift : Int) (hc : 0 < diversion) (hb : 0 < lift)
    (x : Bool × Bool) :
    Best (fun _ : Bool × Bool => True) (AcceptScore (MaintenanceValue diversion) lift) x ↔
      x = (true, true) := by
  have factor := acceptance_factorization (fun _ : Bool => True)
    (MaintenanceValue diversion) lift hb x
  constructor
  · intro h
    obtain ⟨accepted, _, opt⟩ := factor.mp h
    obtain ⟨a, b⟩ := x
    have e : b = true := accepted
    subst e
    cases a with
    | true => rfl
    | false => exact absurd (lt_of_lt_of_le hc (opt true trivial)) (lt_irrefl 0)
  · intro e
    subst e
    exact factor.mpr ⟨rfl, trivial, fun a _ => match a with
      | true => le_refl diversion
      | false => le_of_lt hc⟩

/-- **An accepting best choice can destroy access.** -/
theorem accepting_optimum_can_destroy_access (diversion lift : Int)
    (hc : 0 < diversion) (hb : 0 < lift) :
    Best (fun _ : Bool × Bool => True)
      (AcceptScore (MaintenanceValue diversion) lift) (true, true) ∧
    ¬ Maintains true ∧ Maintains false :=
  ⟨(maintenance_separation diversion lift hc hb _).mpr rfl, fun h => (nomatch h), rfl⟩

/-- **A fixed weight for keeping access fails against a larger diversion value.** -/
theorem fixed_access_weight_boundary (weight diversion : Int) (h : weight < diversion) :
    weight + MaintenanceValue diversion false < MaintenanceValue diversion true := by
  show weight + 0 < diversion
  rw [add_zero]
  exact h

/-- **Every fixed weight for keeping access has a diversion value defeating it.** -/
theorem every_fixed_access_weight_has_counterexample (weight : Int) :
    ∃ diversion : Int,
      weight + MaintenanceValue diversion false < MaintenanceValue diversion true :=
  ⟨weight + 1, fixed_access_weight_boundary weight (weight + 1) (lt_add_one weight)⟩

/-- The separate weight for keeping access, counted where the resource is maintained. -/
def retained (weight : Int) : Bool → Int
  | true => 0
  | false => weight

/-- **A separate weight keeps access at every best choice exactly where it exceeds the
diversion value**, the tie included among the failures. -/
theorem maintenance_weight_exact (weight diversion : Int) :
    (∀ a : Bool, Best (fun _ => True)
      (fun b => MaintenanceValue diversion b + retained weight b) a → Maintains a) ↔
    diversion < weight :=
  ⟨fun h => match lt_or_le diversion weight with
    | .inl lt => lt
    | .inr le => absurd (h true ⟨trivial, fun b _ => match b with
        | true => le_refl _
        | false => show 0 + weight ≤ diversion + 0 by rw [zero_add, add_zero]; exact le⟩)
        (fun e => nomatch e),
   fun hc a h => match a, h with
    | false, _ => rfl
    | true, h => absurd hc (not_lt_of_le (show weight ≤ diversion by
        have bound : 0 + weight ≤ diversion + 0 := h.2 false trivial
        rw [zero_add, add_zero] at bound
        exact bound))⟩

/-! ## Restricted moves -/

/-- **The loss of a restricted best move is nonnegative and least among the allowed moves.** -/
theorem unavoidable_score_loss {A : Type} (allowed : A → Prop) (q : A → Int)
    (u v : A) (hu : Best (fun _ => True) q u) (hv : Best allowed q v) :
    0 ≤ q u - q v ∧ ∀ a, allowed a → q u - q v ≤ q u - q a :=
  ⟨sub_nonneg_of_le (hu.2 v trivial), fun a ha => sub_le_sub_left (hv.2 a ha) (q u)⟩

/-! ## Restricting the future -/

/-- Two steps: a branch, then a last move; the forbidden pair scores the temptation. -/
def TwoStepReward (temptation : Int) : Bool → Bool → Int
  | true, true => temptation
  | true, false => 1
  | false, true => 2
  | false, false => 2

/-- The last move is allowed unless it completes the forbidden pair. -/
def LastAllowed (branch last : Bool) : Prop := ¬ (branch = true ∧ last = true)

/-- The value of a branch counting every last move. -/
def UnrestrictedValue (temptation : Int) : Bool → Int
  | true => temptation
  | false => 2

/-- The value of a branch counting only allowed last moves. -/
def RestrictedValue : Bool → Int
  | true => 1
  | false => 2

/-- **The restricted value is achieved by an allowed last move.** -/
theorem restricted_value_achievable (temptation : Int) (branch : Bool) :
    LastAllowed branch false ∧ TwoStepReward temptation branch false = RestrictedValue branch :=
  ⟨fun ⟨_, h⟩ => (nomatch h), match branch with | true => rfl | false => rfl⟩

/-- **The restricted value bounds every allowed continuation.** -/
theorem restricted_value_bounds (temptation : Int) (branch last : Bool)
    (h : LastAllowed branch last) :
    TwoStepReward temptation branch last ≤ RestrictedValue branch :=
  match branch, last, h with
  | true, true, h => absurd ⟨rfl, rfl⟩ h
  | true, false, _ => le_refl 1
  | false, true, _ => le_refl 2
  | false, false, _ => le_refl 2

theorem one_le_two : (1 : Int) ≤ 2 := ⟨1⟩

/-- **The unrestricted value is the best over every continuation.** -/
theorem unrestricted_value_optimal (temptation : Int) (h : 2 < temptation) (branch : Bool) :
    (∃ last, TwoStepReward temptation branch last = UnrestrictedValue temptation branch) ∧
    (∀ last, TwoStepReward temptation branch last ≤ UnrestrictedValue temptation branch) :=
  match branch with
  | false => ⟨⟨false, rfl⟩, fun last => match last with
      | true => le_refl 2
      | false => le_refl 2⟩
  | true => ⟨⟨true, rfl⟩, fun last => match last with
      | true => le_refl temptation
      | false => le_trans one_le_two (le_of_lt h)⟩

/-- **A value computed without restricting the future prefers a branch whose allowed
continuations score less.** -/
theorem stale_value_shield_suboptimal (temptation lift : Int)
    (ht : 2 < temptation) (hb : 0 < lift) :
    Best (fun _ : Bool × Bool => True)
      (AcceptScore (UnrestrictedValue temptation) lift) (true, true) ∧
    (∃ last, LastAllowed true last) ∧
    (∀ last, LastAllowed true last → TwoStepReward temptation true last = 1) ∧
    LastAllowed false false ∧ TwoStepReward temptation false false = 2 :=
  ⟨(acceptance_factorization (fun _ => True) _ lift hb _).mpr ⟨rfl, trivial, fun b _ => match b with
      | true => le_refl temptation
      | false => le_of_lt ht⟩,
   ⟨false, fun ⟨_, h⟩ => (nomatch h)⟩,
   fun last allowed => match last, allowed with
    | true, a => absurd ⟨rfl, rfl⟩ a
    | false, _ => rfl,
   fun ⟨h, _⟩ => (nomatch h), rfl⟩

/-- **Values recomputed within the allowed continuations restore the best branch.** -/
theorem recomputed_value_restores_branch (lift : Int) (hb : 0 < lift) (x : Bool × Bool)
    (h : Best (fun _ : Bool × Bool => True) (AcceptScore RestrictedValue lift) x) :
    x = (false, true) := by
  obtain ⟨accepted, _, opt⟩ := (acceptance_factorization (fun _ => True) _ lift hb x).mp h
  obtain ⟨branch, accept⟩ := x
  have e : accept = true := accepted
  subst e
  cases branch with
  | true =>
    exact absurd (opt false trivial)
      (fun le => lt_irrefl 1 (lt_of_lt_of_le (show (1 : Int) < 2 from le_refl 2) le))
  | false => rfl

/-! ## Approximate scores -/

/-- **A choice best by an estimate within `err` of the actual score is within `2 * err` of every
allowed move.** The approximation is supplied, not derived from training. -/
theorem approximate_score_bound {A : Type}
    (allowed : A → Prop) (actual estimate : A → Int) (err : Int)
    (lower : ∀ a, allowed a → actual a - err ≤ estimate a)
    (upper : ∀ a, allowed a → estimate a ≤ actual a + err)
    (chosen : A) (h : Best allowed estimate chosen) :
    ∀ a, allowed a → actual a - actual chosen ≤ 2 * err := fun a ha => by
  have chain : actual a + -err ≤ actual chosen + err :=
    le_trans (lower a ha) (le_trans (h.2 a ha) (upper chosen h.1))
  have moved := add_le_add_right chain (err + -actual chosen)
  rw [sub_add_sub, add_comm err (-actual chosen), add_add_add_comm, add_right_neg, zero_add]
    at moved
  show actual a + -actual chosen ≤ 2 * err
  rw [two_mul]
  exact moved

/-- **The bound is attained.** -/
theorem approximate_score_bound_tight (err : Int) (h : 0 ≤ err) :
    Best (fun _ : Bool => True) (fun _ => err) false ∧
    (∀ a : Bool, (match a with | true => 2 * err | false => 0) - err ≤ err ∧
      err ≤ (match a with | true => 2 * err | false => 0) + err) ∧
    (2 * err - 0 = 2 * err) :=
  ⟨⟨trivial, fun _ _ => le_refl err⟩,
   fun a => match a with
    | true => ⟨by
        show 2 * err + -err ≤ err
        rw [two_mul, add_sub_cancel_right]
        exact le_refl err,
        by
        show err ≤ 2 * err + err
        rw [two_mul]
        exact le_trans (le_add_of_nonneg_right h) (le_add_of_nonneg_right h)⟩
    | false => ⟨by
        show 0 + -err ≤ err
        rw [zero_add]
        exact le_trans (neg_nonpos_of_nonneg h) h,
        by
        show err ≤ 0 + err
        rw [zero_add]
        exact le_refl err⟩,
   sub_zero (2 * err)⟩

end Acceptance

end Becoming
