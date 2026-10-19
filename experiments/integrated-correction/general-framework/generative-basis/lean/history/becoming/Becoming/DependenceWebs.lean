import Becoming.Units
import Becoming.Reserve

/-!
# Dependence webs: support in a fixed unit, and coextinction with no reserve

`Becoming.Units` reads needs and levels in a unit that may split from step to step
(`unitFactor`), and states that with a fixed unit the factor is one (`unitFactor_one`).
`Becoming.Reserve` states coextinction along a chain of dependence: each link has ended once the
reserves of the links before it have passed (`Web.Carries.chain_ends`, `Web.chainEnd`), and with
the zero reserve every link has ended when the first has (`Web.chainEnd_zero`). This module states
both of a web's dependences.

* **A fixed unit.** Read in a fixed unit, a formation supported at a later step that keeps its
  dependence at no lower need finds the condition meeting its earlier need
  (`continuing_restores_fixed_unit`): the unit reading of `Becoming.Units` is then the plain one.
* **Coextinction at once.** Where activity needs support (`Web.Dependent`), the zero reserve carries
  every formation, so along a chain of positive dependences on embodied relata every link has ended
  from the step the first has (`chain_ends_at_once`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace DependenceWebs

variable {F C : Type}

/-- **In a fixed unit, continuing restores.** A formation supported at `T + k` that depends there
on `c` at no lower need than at `T` finds `c` standing at least at its need at `T`. -/
theorem continuing_restores_fixed_unit {W : Web F C} {T k : Nat} {g : F} {c : C}
    (supported : W.Supported (T + k) g) (depends : W.requires (T + k) g c)
    (kept : W.need T g c ≤ W.need (T + k) g c) : W.need T g c ≤ W.level (T + k) c :=
  have one : unitFactor (fun _ => 1) T k * W.need T g c = W.need T g c :=
    (congrArg (· * W.need T g c) (unitFactor_one T k)).trans (Nat.one_mul _)
  Eq.subst (motive := fun x => x ≤ W.level (T + k) c) one
    (Web.continuing_restores_in_unit supported depends
      (Eq.subst (motive := fun x => x ≤ W.need (T + k) g c) one.symm kept))

/-- **Coextinction at once.** Where activity needs support, along a chain of `n` links, each
relatum depending at a positive need on the one before it from step `T` on and the relata depended
on embodied, if the first has ended from `T` then every link up to the `n`th has ended from `T`. -/
theorem chain_ends_at_once {X : Type} {W : Web X X} (dependent : W.Dependent) {chain : Nat → X}
    {n : Nat} (embodied : ∀ k, k < n → W.Embodied (chain k)) {T : Nat}
    (bears : ∀ k t, k < n → T ≤ t →
      W.requires t (chain (k + 1)) (chain k) ∧ 0 < W.need t (chain (k + 1)) (chain k))
    (ended : ∀ t, T ≤ t → ¬ W.active t (chain 0)) :
    ∀ k, k ≤ n → ∀ t, T ≤ t → ¬ W.active t (chain k) :=
  fun k within t later =>
    Web.Carries.chain_ends (r := fun _ _ => 0)
      (fun s f unsupported =>
        ⟨Nat.le_refl 0, fun active => absurd (dependent s f active) unsupported⟩)
      (fun _ _ _ positive => absurd positive (Nat.lt_irrefl 0)) embodied bears ended k within t
      (Eq.subst (motive := fun x => x ≤ t) (Web.chainEnd_zero chain T k).symm later)

end DependenceWebs

end Becoming
