import Becoming.Continuation
import Becoming.Standpoints

/-! Independent review probes for commit 1f6f375f (W1–W5). Not part of the package. -/

namespace Becoming
namespace Review

/-! ## R1. The "transmission into each own region" conjunct of `center_not_derived`
follows from S0 at every position, in every valuation. -/
theorem own_transmission_of_selfGood {Pos C : Type} {V : Valuation Pos C}
    (self : ∀ p, V.SelfGood p) : Within (fun i => V.own i.1 i.2.2) V.transmits :=
  fun ⟨p, _, d⟩ own _ _ alive => self p d own alive

/-! ## R2. A second completion of S0: on a connected whole where every position holds a
living claim, S0 everywhere with N_rel gives G0, with no N_std premise. -/
theorem significant_of_selfGood_transmits {Pos C : Type} {V : Valuation Pos C}
    (connected : V.Connected) (holds : ∀ p, ∃ c, V.own p c ∧ V.living c)
    (self : ∀ p, V.SelfGood p) (transmit : Neutral V.transmits) : V.Significant :=
  fun q c alive => match holds q with
    | ⟨c₀, own, alive₀⟩ =>
      Valuation.reaches transmit (connected c₀ c alive₀ alive) (self q c₀ own alive₀)

/-- In `Apart` (connected: every two claims related) both completions are available:
Apart fails N_rel as well as N_std. -/
theorem apart_fails_transmission : ¬ Neutral Apart.valuation.transmits :=
  fun transmit => transmit (true, true, false) trivial trivial trivial

/-! ## R3. A sharing restricted to each position's own region (closer to "for anything,
its continuation has significance") already suffices on held lives. -/
theorem significant_iff_held_own {Pos C : Type} {V : Valuation Pos C} (held : V.Held) :
    V.Significant ↔ (∀ p, V.SelfGood p) ∧ Within (fun i => V.own i.1 i.2.2) V.shares :=
  ⟨fun all => ⟨fun p c _ alive => all p c alive, fun ⟨_, q, c⟩ _ alive _ => all q c alive⟩,
   fun ⟨self, share⟩ q c alive => match held c alive with
    | ⟨p, own⟩ => share (p, q, c) own alive (self p c own alive)⟩

/-! ## R4. Totalizer: the keeper's living event at step 0 is related, in `Web.valuation`'s
formed relations (co-participation), to the other formation's living event at step 0. -/
namespace Tot
open Totalizer

theorem keeper_alive : valuation.living (.keeper, 0) :=
  ⟨trivial, fun ⟨c, drawn, g, depends, _, fell⟩ => match c, drawn, g, depends, fell with
    | .supply, _, .keeper, _, fell => Nat.lt_irrefl 1 fell
    | .habitat, _, .other, _, fell => Nat.lt_irrefl 1 fell⟩

theorem other_alive : valuation.living (.other, 0) :=
  ⟨trivial, fun ⟨_, draws, _⟩ => draws⟩

theorem related_keeper_other : valuation.related (.keeper, 0) (.other, 0) :=
  ⟨.habitat, .inr trivial, .inl trivial⟩

/-- Transmission out of each own region along the formed relations fails in the witness. -/
theorem out_of_own_fails : ¬ Within (fun i => own i.1 i.2.1) valuation.transmits :=
  fun transmit => Formation.noConfusion
    (transmit (.keeper, (.keeper, 0), (.other, 0)) rfl rfl related_keeper_other other_alive)

/-! ## R5. A stronger witness of the center not being derived: the keeper also values
what feeds the condition its continuation requires (the sun), transmission along that
dependence holds from every own region, and still N_std fails. -/

/-- `e'` feeds a condition that `e`'s formation requires, at their common step. -/
def Feeds (e e' : Formation × Nat) : Prop :=
  e.2 = e'.2 ∧ ∃ c, web.requires e.2 e.1 c ∧ 0 < flow.give e'.2 e'.1 c

def sig2 : Formation → Formation × Nat → Prop
  | .keeper, e => e.1 = .keeper ∨ e.1 = .sun
  | .sun, e => e.1 = .sun
  | .other, e => e.1 = .other

def valuation2 : Valuation Formation (Formation × Nat) := web.valuation own sig2

theorem feeds_sun {e e' : Formation × Nat} (feeds : Feeds e e') : e'.1 = .sun :=
  match e, e', feeds with
  | (.keeper, _), (.sun, _), _ => rfl
  | (.keeper, _), (.keeper, _), ⟨_, .supply, _, gives⟩ => absurd gives (Nat.lt_irrefl 0)
  | (.keeper, _), (.other, _), ⟨_, .supply, _, gives⟩ => absurd gives (Nat.lt_irrefl 0)
  | (.other, _), (.sun, _), ⟨_, .habitat, _, gives⟩ => absurd gives (Nat.lt_irrefl 0)
  | (.other, _), (.keeper, _), ⟨_, .habitat, _, gives⟩ => absurd gives (Nat.lt_irrefl 0)
  | (.other, _), (.other, _), ⟨_, .habitat, _, gives⟩ => absurd gives (Nat.lt_irrefl 0)

theorem stronger :
    valuation2.Held ∧ (∀ f, valuation2.SelfGood f) ∧
      (∀ p e e', own p e → valuation2.sig p e → Feeds e e' → valuation2.sig p e') ∧
      valuation2.living (.other, 0) ∧ ¬ valuation2.sig .keeper (.other, 0) ∧
      ¬ Neutral valuation2.shares ∧ ¬ valuation2.Significant :=
  have apart : ¬ valuation2.sig .keeper (.other, 0) := fun
    | .inl same => Formation.noConfusion same
    | .inr same => Formation.noConfusion same
  ⟨web.held_by_formations sig2,
   fun f e owned _ => match f, e, owned with
    | .keeper, (.keeper, _), _ => .inl rfl
    | .sun, (.sun, _), _ => rfl
    | .other, (.other, _), _ => rfl,
   fun p e e' owned _ feeds => match p, e, e', owned, feeds_sun feeds, feeds with
    | .keeper, (.keeper, _), (.sun, _), _, _, _ => .inr rfl
    | .sun, (.sun, _), _, _, _, ⟨_, _, no, _⟩ => False.elim no
    | .other, (.other, _), (.sun, _), _, _, ⟨_, .habitat, _, gives⟩ =>
      absurd gives (Nat.lt_irrefl 0),
   other_alive, apart,
   fun share => apart (share (.other, .keeper, (.other, 0)) other_alive rfl),
   fun all => apart (all .keeper (.other, 0) other_alive)⟩

/-! ## R6. Under living on (`Web.sustenance`), read with one kind of relatum, the supply's
region is not a cut either: the keeper lives on the supply. -/
theorem supply_not_cut_living_on {Pos : Type} (own sig : Pos → (Formation ⊕ Place) × Nat → Prop) :
    ¬ Flow.Cut (web.roles.sustenance own sig) (fun e => e.1 ∈ [Sum.inr Place.supply]) :=
  fun cut => cut (.inr .supply, 0) (.inl .keeper, 0) (.head _)
    (fun mem => match mem with | .tail _ no => nomatch no)
    (.inr (.inr ⟨trivial, trivial, Nat.zero_lt_one⟩))

end Tot

/-! ## R7. Lone: every conveyance is by the sun; the one formation beyond the pool is the
same particular source at every step. -/
theorem lone_only_sun {t : Nat} {d : Frontier.Condition} {f : Lone.Formation}
    (gives : 0 < Lone.flow.give t f d) : f = .sun :=
  match f, gives with
  | .sun, _ => rfl
  | .eater, gives => absurd gives (Nat.lt_irrefl 0)

/-! ## R8. Mortal does not take jointly within what is given while it lives. -/
theorem mortal_joint_excess : ¬ Mortal.flow.WithinJoint 0 () ∧ ¬ Mortal.flow.WithinJoint 1 () :=
  ⟨fun within => Nat.not_succ_le_self 1 within, fun within => Nat.not_succ_le_self 1 within⟩

/-! ## R9. `Exceeding.all_end` is true of the stipulated activity without the law. -/
theorem exceeding_by_definition : ∀ n f, ¬ Exceeding.web.active (2 + n) f :=
  fun n _ dead => Eq.subst (motive := fun t => Exceeding.live t) (Nat.add_comm 2 n) dead

end Review
end Becoming

open Becoming.Review in
#print axioms own_transmission_of_selfGood
open Becoming.Review in
#print axioms significant_of_selfGood_transmits
open Becoming.Review in
#print axioms apart_fails_transmission
open Becoming.Review in
#print axioms significant_iff_held_own
#print axioms Becoming.Review.Tot.keeper_alive
#print axioms Becoming.Review.Tot.out_of_own_fails
#print axioms Becoming.Review.Tot.stronger
#print axioms Becoming.Review.Tot.supply_not_cut_living_on
#print axioms Becoming.Review.lone_only_sun
#print axioms Becoming.Review.mortal_joint_excess
#print axioms Becoming.Review.exceeding_by_definition
