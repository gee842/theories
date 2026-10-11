import Becoming.Testing

/-!
# Probe F: own standing, registered as a gauge or through bearing on oneself

Sixteenth review of P47. The module counts a formation's own standing as observed in the
one-kind reading (`ownStanding`). The spine already has a structural relation of a relatum to its
own standing: bearing on itself (`Web.SelfBearing`, `Becoming.Roles`). This probe compares them.

* F1 `Gauged_own`: in `Gauged` (one formation, one condition, both `Unit`) the stock is the
  formation's own standing, so `ownStanding` is the gauge: a formation whose reserve is its own
  standing is never blind below its threshold there.
* F2 `Prey_omits`: in `Prey` the registered difference makes no difference to the prey: it is
  supported and active at every step with and without the bite; the prey does not bear on
  itself, and the predator is active with no standing (not embodied).
* F3 `SelfPrey`: let the prey bear on itself at need one. Then the predator lies within the prey's
  influence closure with support only; a bite of one unit (from two to one) registers neither
  through support (it is below the threshold) nor anywhere else under `supportOnly`, and registers
  under `ownStanding`; a bite of two units registers through support.
-/

namespace Becoming.Review47

open Becoming Generative

/-! ### F1 -/

theorem Gauged_own :
    (∀ g c, Gauged.stock g c ↔ ownStanding g c) ∧
      (Gauged.flow 1).RespondsThrough (Gauged.web 1) (Gauged.flow 2) (Gauged.web 2) ownStanding () ∧
      ¬ (Gauged.web 1).RegistersAlike ownStanding () (Gauged.web 1).level (Gauged.web 2).level 0 :=
  ⟨fun () () => ⟨fun _ => rfl, fun _ => trivial⟩,
   fun _ alike => absurd ((alike 0 (Nat.zero_le _)).2 () rfl) two_ne_three,
   fun alike => two_ne_three (alike.2 () rfl)⟩

/-! ### F2 -/

open Prey Prey.Relatum in
theorem Prey_omits :
    (∀ t, web.Supported t prey ∧ web.active t prey ∧ web.Admits (spared t) t prey) ∧
      ¬ web.SelfBearing prey ∧ ¬ web.Embodied predator :=
  ⟨fun _ => ⟨fun c requires => (match c, requires with
      | food, _ => Nat.le_refl 1
      | prey, no => nomatch no
      | predator, no => nomatch no),
    trivial,
    fun c requires => (match c, requires with
      | food, _ => Nat.le_refl 1
      | prey, no => nomatch no
      | predator, no => nomatch no)⟩,
   fun bearing => (nomatch (bearing 0 trivial).1),
   fun embodied => Nat.lt_irrefl 0 ((embodied 0).mp trivial)⟩

/-! ### F3 -/

namespace SelfPrey

open Prey.Relatum

/-- The predator takes `b` units of the prey's standing at the first step. -/
def flow (b : Nat) : Flow Prey.Relatum Prey.Relatum where
  present _ := [predator]
  take t f c := match f, c with
    | predator, prey => (match t with
      | 0 => b
      | _ + 1 => 0)
    | predator, food => 0
    | predator, predator => 0
    | food, _ => 0
    | prey, _ => 0
  give _ _ _ := 0

def standing (b : Nat) : Nat → Nat
  | 0 => 2
  | _ + 1 => 2 - b

/-- As `Prey.web`, except that the prey bears on its own standing at need one. -/
def web (b : Nat) : Web Prey.Relatum Prey.Relatum where
  level t c := match c with
    | food => 1
    | prey => standing b t
    | predator => 0
  active _ _ := True
  requires _ f c := match f, c with
    | prey, food => True
    | prey, prey => True
    | prey, predator => False
    | food, _ => False
    | predator, _ => False
  need _ _ _ := 1
  draws _ _ _ := True

theorem balances_one : (flow 1).Balances (web 1)
  | 0, food => rfl
  | 0, prey => rfl
  | 0, predator => rfl
  | _ + 1, food => rfl
  | _ + 1, prey => rfl
  | _ + 1, predator => rfl

theorem balances_two : (flow 2).Balances (web 2)
  | 0, food => rfl
  | 0, prey => rfl
  | 0, predator => rfl
  | _ + 1, food => rfl
  | _ + 1, prey => rfl
  | _ + 1, predator => rfl

theorem selfBearing (b : Nat) : (web b).SelfBearing prey :=
  fun _ _ => ⟨trivial, Nat.zero_lt_one⟩

/-- With bearing on itself, the predator lies within the prey's influence closure. -/
theorem within_influence (b : Nat) (pos : 0 < b) : (flow b).WithinInfluence (web b) prey predator :=
  WithinClosure.of_rel ⟨prey, ⟨0, trivial⟩, 0, .head _, .inl pos⟩

theorem admits_spared (b t : Nat) : (web b).Admits (Prey.spared t) t prey :=
  fun c requires => match c, requires with
  | food, _ => Nat.le_refl 1
  | prey, _ => Nat.le_succ 1
  | predator, no => nomatch no

/-- F3. A bite of one is below the prey's threshold on itself: through support it registers
alike with the spared levels at every step; under `ownStanding` it registers at step one. A bite
of two registers through support at step one. -/
theorem threshold_on_oneself :
    (∀ t, (web 1).RegistersAlike supportOnly prey (web 1).level Prey.spared t) ∧
      ¬ (web 1).RegistersAlike ownStanding prey (web 1).level Prey.spared 1 ∧
      ¬ (web 2).RegistersAlike supportOnly prey (web 2).level Prey.spared 1 :=
  ⟨fun t => ⟨⟨fun _ => admits_spared 1 t, fun _ c requires => match c, requires, t with
      | food, _, _ => Nat.le_refl 1
      | prey, _, 0 => Nat.le_succ 1
      | prey, _, _ + 1 => Nat.le_refl 1
      | predator, no, _ => nomatch no⟩, fun _ no => False.elim no⟩,
   fun alike => one_ne_two (alike.2 prey rfl),
   fun alike => Nat.not_succ_le_zero 0 ((alike.1.mpr (admits_spared 2 1)) prey trivial)⟩

end SelfPrey

end Becoming.Review47

open Becoming.Review47
#print axioms Gauged_own
#print axioms SelfPrey.flow
#print axioms Prey_omits
#print axioms SelfPrey.balances_one
#print axioms SelfPrey.balances_two
#print axioms SelfPrey.selfBearing
#print axioms SelfPrey.within_influence
#print axioms SelfPrey.threshold_on_oneself
