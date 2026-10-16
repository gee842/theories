import Becoming
import D36

/-!
# Probes of the thirteenth independent review (P32–P34, drafts P35/P36)

Term mode throughout; no tactic blocks. The axiom audit is in `Review13Audit.lean`.

* Q1 `Balance`, `balance_not_tally`, `tally_iff`, `ceasing_bound_law`: the balance as an
  equation (`Listed.across`) is strictly weaker than a tally (`Listed.keeps`); the tally is
  the balance together with "no more cease across a step than are listed before it", which is
  a law of counting the equation does not give.
* Q2 `tally_congr`, `tally_iff_counted`: the counts listings can have are exactly the
  tallies, up to values at each step, stated with no `Pointwise` hypothesis.
* Q3 `since_le`, `since_zero_le`, `settles_zero`, `settles_iff_zero`, `same_laws`: settling
  from some step is settling from step 0 with a larger bound, so worlds enclosed from some step,
  worlds enclosed from step 0 and finite worlds have the same laws of counting under the eight
  premises (from the drafts' `enclosed_counting` and `finite_counting`).
* Q4 `tended_dissipation_idle`, `tended_not_binds`: in the tended queue dissipation never
  binds in the sense of `World.Binds` (nothing taking part ever takes from a closed family),
  and neither does activity needing support.
* Q5 `FirstChange.*`, `SettlesEnds`, `lpo_of_settlesEnds`, `FiniteEnds`, `lpo_of_finiteEnds`:
  a tally that settles from step 0, with nothing joining an empty queue, whose only change is at
  the first `true` of a Boolean sequence; an end step for change in every settling count, or an
  end step for arising in every finite world meeting the eight premises, implies LPO.
* Q6 `OneSwap.*`, `closed_dissipation_binds`: in the drafts' finite world, dissipation binds.
* Q7 `binds_arising`, `binds_adds`: where every premise binds (`World.Binds`), every census
  counts some arising, which is no law under the eight premises alone.
* Q8: the P30 names after P33b, and the drafts' arithmetic beside the core's.
-/

namespace Review13

open Becoming

/-! ## Q1. The balance equation is not the whole law of counting -/

/-- The census balance across each step, as `Listed.across` states it. -/
def Balance (n c a : Nat → Nat) : Prop :=
  ∀ t, n (t + 1) + c t = n t + a t

theorem tally_balance {n c a : Nat → Nat} (tally : Tally n c a) : Balance n c a := fun t =>
  match tally t with
  | ⟨k, before, after⟩ => (congrArg (· + c t) after).trans
      ((Nat.add_right_comm k (a t) (c t)).trans (congrArg (· + a t) before.symm))

theorem tally_le {n c a : Nat → Nat} (tally : Tally n c a) (t : Nat) : c t ≤ n t :=
  match tally t with
  | ⟨k, before, _⟩ => Nat.le_trans (Nat.le_add_left (c t) k) (Nat.le_of_eq before.symm)

theorem tally_of_balance {n c a : Nat → Nat} (balance : Balance n c a)
    (bounded : ∀ t, c t ≤ n t) : Tally n c a := fun t =>
  match le_dest (bounded t) with
  | ⟨k, same⟩ => ⟨k, same.trans (Nat.add_comm (c t) k),
      add_right_cancel (c t) ((balance t).trans ((congrArg (· + a t)
        (same.trans (Nat.add_comm (c t) k))).trans (Nat.add_right_comm k (c t) (a t))))⟩

/-- A tally is exactly the balance with no more ceasing across a step than were listed. -/
theorem tally_iff {n c a : Nat → Nat} : Tally n c a ↔ Balance n c a ∧ ∀ t, c t ≤ n t :=
  ⟨fun tally => ⟨tally_balance tally, tally_le tally⟩,
   fun ⟨balance, bounded⟩ => tally_of_balance balance bounded⟩

/-- None listed, one ceasing and one coming at every step: the equation holds, the tally
does not. -/
theorem balance_not_tally :
    Balance (fun _ => 0) (fun _ => 1) (fun _ => 1) ∧ ¬ Tally (fun _ => 0) (fun _ => 1) (fun _ => 1) :=
  ⟨fun _ => rfl, fun tally => Nat.not_succ_le_zero 0 (tally_le tally 0)⟩

/-- "No more cease than were listed" holds of every listing, and does not follow from the
balance equation. -/
theorem ceasing_bound_law :
    (∀ (α : Type) (p : α → Nat → Prop) [∀ x t, Decidable (p x t)] (l : Nat → List α),
      Listed p l → ∀ t, ceasings (l t) p t ≤ (l t).length) ∧
    ¬ ∀ n c a : Nat → Nat, Balance n c a → ∀ t, c t ≤ n t :=
  ⟨fun _ _ _ _ listed t => tally_le listed.tally t,
   fun law => Nat.not_succ_le_zero 0 (law _ _ _ balance_not_tally.1 0)⟩

/-! ## Q2. The characterization without `Pointwise` -/

/-- Tallies respect the counts' values at each step. -/
theorem tally_congr {n c a n' c' a' : Nat → Nat}
    (same : ∀ t, n t = n' t ∧ c t = c' t ∧ a t = a' t) (tally : Tally n c a) :
    Tally n' c' a' := fun t =>
  match tally t with
  | ⟨k, before, after⟩ =>
    ⟨k, (same t).1.symm.trans (before.trans (congrArg (k + ·) (same t).2.1)),
     (same (t + 1)).1.symm.trans (after.trans (congrArg (k + ·) (same t).2.2))⟩

/-- The counts some listing has are exactly the tallies: `counting_laws` without a
hypothesis on the property. -/
theorem tally_iff_counted (n c a : Nat → Nat) :
    Tally n c a ↔ ∃ (α : Type) (p : α → Nat → Prop) (_ : ∀ x t, Decidable (p x t))
      (l : Nat → List α), Listed p l ∧
        ∀ t, (l t).length = n t ∧ ceasings (l t) p t = c t ∧ comings (l (t + 1)) p t = a t :=
  ⟨fun tally => ⟨Nat, Queue.holds n c, fun _ _ => inferInstance, Queue.line n c, Queue.listed,
     Queue.counts tally⟩,
   fun ⟨_, _, _, _, listed, same⟩ => tally_congr same listed.tally⟩

/-! ## Q3. Settling from some step is settling from the first -/

theorem since_le {T : Nat} (q : Nat → Nat) : ∀ t, since T q t ≤ t
  | 0 => Nat.le_refl 0
  | t + 1 => Nat.add_le_add (since_le q t) (mark_le_one _)

theorem since_zero_le {T : Nat} (q : Nat → Nat) : ∀ t, since 0 q t ≤ since T q t + T
  | 0 => Nat.zero_le _
  | t + 1 => match Nat.lt_or_ge t T with
    | .inl early => Nat.le_trans (since_le q (t + 1)) (Nat.le_trans early (Nat.le_add_left T _))
    | .inr later => Nat.le_trans (Nat.le_of_eq (since_succ q (Nat.zero_le t)))
        (Nat.le_trans (Nat.add_le_add_right (since_zero_le q t) _)
          (Nat.le_of_eq ((Nat.add_right_comm _ T _).trans
            (congrArg (· + T) (since_succ q later).symm))))

/-- Counts settling from step `T` within `B` settle from step 0 within `B + T` and the counts
before `T`. -/
theorem settles_zero {n c a : Nat → Nat} {T B : Nat} (settles : Settles T B n c a) :
    Settles 0 (B + T + total (steps 0 T) n) n c a := fun t _ =>
  match Nat.lt_or_ge t T with
  | .inl early => Nat.le_trans
      (Nat.add_le_add (le_total_of_mem (q := n) (steps_of_within (Nat.zero_le t)
        (Nat.lt_of_lt_of_le early (Nat.le_of_eq (Nat.zero_add T).symm))))
        (Nat.le_trans (since_le _ t) (Nat.le_of_lt early)))
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _))
        (Nat.add_le_add_right (Nat.le_add_left T B) _))
  | .inr later => Nat.le_trans (Nat.add_le_add_left (since_zero_le _ t) _)
      (Nat.le_trans (Nat.le_of_eq (Nat.add_assoc _ _ _).symm)
        (Nat.le_trans (Nat.add_le_add_right (settles t later) T) (Nat.le_add_right _ _)))

theorem settles_iff_zero {n c a : Nat → Nat} :
    (∃ T B, Settles T B n c a) ↔ ∃ B, Settles 0 B n c a :=
  ⟨fun ⟨_, _, settles⟩ => ⟨_, settles_zero settles⟩, fun ⟨B, settles⟩ => ⟨0, B, settles⟩⟩

/-- Under the eight premises, worlds enclosed from some step and finite worlds have the same
laws of counting. -/
theorem same_laws {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
      w.CountsObey Q) :=
  ⟨fun law w _ premised finite => law w premised ⟨0, fun t _ => finite.enclosed t⟩,
   fun law => (World.enclosed_counting pointwise).mp fun n c a tally company settles =>
     (World.finite_counting pointwise).mpr law n c a tally company (settles_iff_zero.mp settles)⟩

/-! ## Q4. In the tended queue dissipation never binds -/

/-- Nothing taking part in the tended queue ever takes from a closed family: where something is
taken the front is active, and then it gives to a ground relatum beyond every finite family. -/
theorem tended_dissipation_idle {n c : Nat → Nat} :
    ¬ ∃ cs t f, Distinct cs ∧ (World.tendedQueue n c).flow.ClosedAt cs t ∧
      f ∈ (World.tendedQueue n c).flow.present t ∧
      0 < total cs ((World.tendedQueue n c).flow.take t f) :=
  fun ⟨cs, t, f, _, closed, present, takes⟩ =>
    match total_pos cs takes with
    | ⟨x, _, positive⟩ =>
      have occupied : 0 < n t := match x, positive with
        | .member _, positive => Tended.occupied (mark_pos.mp positive).1
        | .ground _, positive => Tended.front.mp (mark_pos.mp positive)
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        ((mark_one (Tended.front.mpr occupied)).symm.trans
          (closed f present _ (Tended.outside cs)).2)))

/-- So in the witness of `premised_counting` neither dissipation nor activity needing support
binds. -/
theorem tended_not_binds {n c : Nat → Nat} :
    (¬ ∃ cs t f, Distinct cs ∧ (World.tendedQueue n c).flow.ClosedAt cs t ∧
      f ∈ (World.tendedQueue n c).flow.present t ∧
      0 < total cs ((World.tendedQueue n c).flow.take t f)) ∧
    (¬ ∃ t f x, (World.tendedQueue n c).web.active t f ∧
      (World.tendedQueue n c).web.requires t f x ∧ 0 < (World.tendedQueue n c).web.need t f x) ∧
    ¬ (World.tendedQueue n c).Binds :=
  ⟨tended_dissipation_idle, fun ⟨_, _, _, _, no, _⟩ => no,
   fun binds => tended_dissipation_idle binds.dissipative⟩

/-! ## Q5. An end step for settling change is omniscience -/

def ind : Bool → Nat
  | true => 1
  | false => 0

theorem ind_split : ∀ b d : Bool, ind (b && d) + ind (b && !d) = ind b
  | true, true => rfl
  | true, false => rfl
  | false, _ => rfl

theorem mark_double : ∀ b : Bool, mark (0 < ind b + ind b) = ind b
  | true => rfl
  | false => rfl

namespace FirstChange

variable (s : Nat → Bool)

/-- One member leaves and one joins across the step at the first `true` of `s`, and nothing
changes at any other step. -/
def change (t : Nat) : Nat :=
  ind (clear s t && s t)

/-- The steps with a change before `t`, with whether no `true` has come yet, are one. -/
theorem since_clear : ∀ t, since 0 (fun u => change s u + change s u) t + ind (clear s t) = 1
  | 0 => rfl
  | t + 1 => (congrArg (· + ind (clear s (t + 1)))
      ((since_succ _ (Nat.zero_le t)).trans (congrArg (_ + ·) (mark_double _)))).trans
      ((Nat.add_assoc _ _ _).trans
        ((congrArg (since 0 (fun u => change s u + change s u) t + ·)
          (ind_split (clear s t) (s t))).trans (since_clear t)))

theorem tally : Tally (fun _ => 1) (change s) (change s) := fun t =>
  match Clear.cases (clear s t && s t) with
  | .inl no => ⟨1, (congrArg (1 + ·) (congrArg ind no)).symm,
      (congrArg (1 + ·) (congrArg ind no)).symm⟩
  | .inr yes => ⟨0, (congrArg (0 + ·) (congrArg ind yes)).symm,
      (congrArg (0 + ·) (congrArg ind yes)).symm⟩

theorem company : ∀ t, 0 < change s t → 0 < (fun _ => 1) t :=
  fun _ _ => Nat.zero_lt_one

theorem settles : Settles 0 2 (fun _ => 1) (change s) (change s) := fun t _ =>
  Nat.add_le_add_left (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq (since_clear s t))) 1

theorem at_first {m : Nat} (c : clear s m = true) (yes : s m = true) :
    change s m + change s m = 2 :=
  congrArg (fun b => ind b + ind b) (Clear.and_both _ _ c yes)

/-- From the step of an end, decide `s`. -/
theorem decide_of_end {E : Nat} (quiet : ∀ m, E ≤ m → clear s m = true → s m = true → False) :
    (∃ n, s n = true) ∨ ∀ n, s n = false :=
  match Clear.or_first s E with
  | .inr ⟨m, _, _, yes⟩ => .inl ⟨m, yes⟩
  | .inl c => .inr fun k => Clear.false_of_not (s k) fun yes =>
    match Clear.first_of_true s yes with
    | ⟨m, cm, ym⟩ => match Nat.lt_or_ge m E with
      | .inl lt => Clear.not_both (Clear.false_before s c lt) ym
      | .inr ge => quiet m ge cm ym

end FirstChange

/-- Every count that settles from the first step, with nothing joining an empty queue, has a
step after which nothing changes. -/
def SettlesEnds : Prop :=
  ∀ n c a : Nat → Nat, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, Settles 0 B n c a) →
    ∃ E, ∀ t, E ≤ t → c t + a t = 0

theorem lpo_of_settlesEnds (ends : SettlesEnds) : LPO := fun s =>
  match ends _ _ _ (FirstChange.tally s) (FirstChange.company s) ⟨2, FirstChange.settles s⟩ with
  | ⟨E, quiet⟩ => FirstChange.decide_of_end s (E := E) fun m ge c yes =>
    Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le Nat.zero_lt_two (Nat.le_of_eq
      ((FirstChange.at_first s c yes).symm.trans (quiet m ge))))

/-- Every finite world meeting the eight premises, whose activity is decided, has a step
after which nothing arises. -/
def FiniteEnds : Prop :=
  ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
    ∃ E, ∀ t x, E ≤ t → ¬ w.web.Arises t x

theorem lpo_of_finiteEnds (ends : FiniteEnds) : LPO := fun s =>
  match ends (World.closedQueue (fun _ => 1) (FirstChange.change s) (FirstChange.change s) 2)
      (World.closedQueue_premised (FirstChange.tally s) (FirstChange.company s)
        (FirstChange.settles s))
      (World.closedQueue_finite _ _ _ _) with
  | ⟨E, quiet⟩ => FirstChange.decide_of_end s (E := E) fun m ge c yes =>
    have comes : 0 < comings (Closed.alive (fun _ => 1) (FirstChange.change s) 2 (m + 1))
        (fun x u => (World.closedQueue (fun _ => 1) (FirstChange.change s)
          (FirstChange.change s) 2).web.active u x) m :=
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        ((congrArg ind (Clear.and_both _ _ c yes)).symm.trans
          ((World.closedQueue_counts (FirstChange.tally s) (FirstChange.settles s) m).2.2.symm)))
    match total_pos _ comes with
    | ⟨x, _, arises⟩ => quiet m x ge (mark_pos.mp arises)

/-! ## Q6. In the drafts' finite world dissipation binds -/

namespace OneSwap

/-- One member, replaced across the first step. -/
def change : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

theorem tally : Tally (fun _ => 1) change change
  | 0 => ⟨0, rfl, rfl⟩
  | _ + 1 => ⟨1, rfl, rfl⟩

theorem since_one : ∀ t, since 0 (fun u => change u + change u) (t + 1) = 1
  | 0 => rfl
  | t + 1 => (since_succ _ (Nat.zero_le (t + 1))).trans (congrArg (· + 0) (since_one t))

theorem settles : Settles 0 2 (fun _ => 1) change change
  | 0, _ => Nat.le_succ 1
  | t + 1, _ => Nat.le_of_eq (congrArg (1 + ·) (since_one t))

abbrev world : World := World.closedQueue (fun _ => 1) change change 2

/-- Place 0 holds the front at the first step. -/
def zero : Fin (Closed.size 2) := ⟨0, Nat.succ_pos _⟩

/-- At the first step the front, standing at two, leaves, and the new member stands at one. -/
theorem takes : world.flow.take 0 (Closed.front change 2 0) zero = 2 := rfl

/-- `change_within`'s bound is attained: the total standing at step 0 is two, and from step 1
on one member is active with one change step behind it. -/
theorem attained : world.web.stock (Closed.alive (fun _ => 1) change 2 0) 0 = 2 ∧
    ∀ t, (Closed.alive (fun _ => 1) change 2 (t + 1)).length +
      since 0 (fun u => change u + change u) (t + 1) = 2 :=
  ⟨rfl, fun t => (congrArg (· + _) ((World.closedQueue_counts tally settles (t + 1)).1)).trans
    (congrArg (1 + ·) (since_one t))⟩

end OneSwap

/-- In the drafts' finite world dissipation binds: something taking part takes from a closed
family. -/
theorem closed_dissipation_binds :
    ∃ cs t f, Distinct cs ∧ OneSwap.world.flow.ClosedAt cs t ∧ f ∈ OneSwap.world.flow.present t ∧
      0 < total cs (OneSwap.world.flow.take t f) :=
  match World.closedQueue_finite (fun _ => 1) OneSwap.change OneSwap.change 2 with
  | ⟨all, distinct, every⟩ =>
    ⟨all, 0, Closed.front OneSwap.change 2 0, distinct,
     fun _ _ x out => absurd (every x) out, .head _,
     Nat.lt_of_lt_of_le Nat.zero_lt_two (Nat.le_trans (Nat.le_of_eq OneSwap.takes.symm)
       (le_total_of_mem (every OneSwap.zero)))⟩

/-! ## Q7. Where every premise binds, counting has a further law -/

/-- In a world in which every premise binds (`World.Binds`), every census counts an arising:
embodiment binds only where something arises. -/
theorem binds_arising (w : World) [∀ t x, Decidable (w.web.active t x)] (binds : w.Binds) :
    w.CountsObey fun _ _ a => ∃ t, 0 < a t := fun alive census =>
  match binds.embodied with
  | ⟨t, x, arises⟩ =>
    have mem : x ∈ alive (t + 1) := ((census (t + 1)).2 x).mp arises.2
    have one : 0 < mark (ComesToBe (fun s => w.web.active s x) t) := mark_pos.mpr arises
    ⟨t, Nat.lt_of_lt_of_le one
      (le_total_of_mem (q := fun y => mark (ComesToBe (fun s => w.web.active s y) t)) mem)⟩

theorem arising_pointwise : Pointwise fun _ _ a => ∃ t, 0 < a t :=
  fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2)⟩

/-- Under the eight premises "something arises" is no law of counting (the empty tally), but
it is one where every premise binds: `premised_counting` ranges over worlds in which some
premises may hold idly. -/
theorem binds_adds :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Binds →
      w.CountsObey fun _ _ a => ∃ t, 0 < a t) ∧
    ¬ ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      w.CountsObey fun _ _ a => ∃ t, 0 < a t :=
  ⟨binds_arising, fun law =>
    match (World.premised_counting arising_pointwise).mpr law (fun _ => 0) (fun _ => 0)
        (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩) (fun _ no => no) with
    | ⟨_, no⟩ => Nat.lt_irrefl 0 no⟩

/-! ## Q8. Names -/

example := @Becoming.World.slow_world
example := @Becoming.World.slow
example := @Becoming.Slow.census
example := @Becoming.Web.Census.balanceFrom
example := @Becoming.World.premised_counting
-- The drafts' arithmetic beside what the core already has.
example : ∀ {a b c : Nat}, a + b ≤ c → a ≤ c - b := @RelationalRenewal.le_sub_from_add
example : ∀ {a b c : Nat}, a + b ≤ c → a ≤ c - b := @Becoming.le_sub_of_add_le
example : ∀ {a b : Nat} (k : Nat), a + k = b + k → a = b := @Becoming.add_right_cancel

end Review13
