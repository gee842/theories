import Becoming.OrderNormal

/-!
# Order worlds: the arrangements of a world's exchanges, and its readings in time

`Becoming.OrderNormal` states, for any symmetric relation joining the exchanges of a stretch,
that reaching one arrangement from another by commuting exchanges not joined is fixed by the
order of joined pairs, that a lexicographic normal form exists given a decision of apartness, and
that a complete invariant exists exactly where apartness is decided. A world with a footprint
(`Footprinted`) joins its exchanges by `Footprinted.Joined`, read off the relata its exchanges
touch and the dependences of its web, and that relation is symmetric (`Footprinted.Joined.symm`).
This module states those laws of a world's exchanges, together with two laws of
`Becoming.Order` read of a world and a web: the halving, and the steps at which a family's stock
rises in commuted webs.

* **Reaching is an equivalence of a world's arrangements.** Every arrangement of a stretch of a
  world's exchanges is reached from itself (`rearranges_refl`), reaching is symmetric
  (`rearranges_symm`) and transitive (`rearranges_trans`).
* **The normal form of a world's exchanges.** Given a decision of apartness of a world's
  exchanges over a stretch, the normal form is its own normal form (`normalForm_normal`) and is
  lexicographically least among the arrangements reached (`normalForm_least`). A complete
  invariant of the arrangements of the world's exchanges exists exactly where their apartness is
  decided (`complete_iff`).
* **Every step read twice.** A world read through the halving, every step taken twice, meets
  balance, dissipation, only active relata giving and taking, activity needing support,
  embodiment and bounded transmission exactly where the world meets them (`halving_premises_iff`).
* **Commuted webs rise at as many steps.** Over a stretch holding both commuted steps, the steps
  at which a family's stock rises number the same in two commuted webs (`commuted_rise_count`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace OrderWorlds

/-! ## Arrangements of a world's exchanges -/

section Arrangements

variable {X : Type} (r : Footprinted X) {S m : Nat}

/-- **Every arrangement of a stretch of a world's exchanges is reached from itself.** -/
theorem rearranges_refl {π σ : Nat → Nat} (reindex : Reindexes S m π σ) :
    Rearranges r.Joined S m π σ π :=
  (rearranges_iff (fun _ _ => Footprinted.Joined.symm) reindex reindex).mpr (Orients.refl π)

/-- **Reaching one arrangement of a world's exchanges from another is symmetric.** -/
theorem rearranges_symm {π σ π' σ' : Nat → Nat} (reindex : Reindexes S m π σ)
    (reindex' : Reindexes S m π' σ') (re : Rearranges r.Joined S m π σ π') :
    Rearranges r.Joined S m π' σ' π :=
  Rearranges.symm (fun _ _ => Footprinted.Joined.symm) reindex reindex' re

/-- **And transitive.** -/
theorem rearranges_trans {π σ π' σ' π'' σ'' : Nat → Nat} (reindex : Reindexes S m π σ)
    (reindex' : Reindexes S m π' σ') (reindex'' : Reindexes S m π'' σ'')
    (first : Rearranges r.Joined S m π σ π') (second : Rearranges r.Joined S m π' σ' π'') :
    Rearranges r.Joined S m π σ π'' :=
  Rearranges.trans (fun _ _ => Footprinted.Joined.symm) reindex reindex' reindex'' first second

variable {apart : Nat → Nat → Bool}

/-- **The normal form of a world's exchanges is its own normal form**, given a decision of their
apartness over the stretch. -/
theorem normalForm_normal {π σ : Nat → Nat} (decides : DecidesApart r.Joined S m apart)
    (reindex : Reindexes S m π σ) {i : Nat} (hi : S ≤ i) (hi' : i < S + m) :
    normalForm apart S m (normalForm apart S m π σ)
        (fun p => σ (origin (normalSteps apart S m π σ m) p)) i = normalForm apart S m π σ i :=
  Becoming.normalForm_normal (fun _ _ => Footprinted.Joined.symm) decides reindex hi hi'

/-- **The normal form of a world's exchanges is lexicographically least** among the arrangements
reached: where it and one reached hold the same exchanges before step `S + k`, its exchange there
is no greater. -/
theorem normalForm_least {π σ π' σ' : Nat → Nat} (decides : DecidesApart r.Joined S m apart)
    (reindex : Reindexes S m π σ) (reindex' : Reindexes S m π' σ')
    (re : Rearranges r.Joined S m π σ π') {k : Nat} (lt : k < m)
    (before : ∀ p, S ≤ p → p < S + k → σ (origin (normalSteps apart S m π σ m) p) = σ' p) :
    σ (origin (normalSteps apart S m π σ m) (S + k)) ≤ σ' (S + k) :=
  Becoming.normalForm_least (fun _ _ => Footprinted.Joined.symm) decides reindex reindex' re lt
    before

/-- **A complete invariant of the arrangements of a world's exchanges over a stretch exists
exactly where their apartness is decided.** -/
theorem complete_iff :
    (∃ N, CompleteInvariant r.Joined S m N) ↔ ∃ apart, DecidesApart r.Joined S m apart :=
  Becoming.complete_iff (fun _ _ => Footprinted.Joined.symm)

end Arrangements

/-! ## Readings in time -/

/-- **A world read with every step taken twice meets the premises exactly where it meets
them.** -/
theorem halving_premises_iff (w : World) [DecidableEq w.Relatum] (once : w.flow.Once) :
    ((w.sample Pulse.half).Balanced ↔ w.Balanced) ∧
      ((w.sample Pulse.half).Dissipative ↔ w.Dissipative) ∧
      ((w.sample Pulse.half).Acting ↔ w.Acting) ∧ ((w.sample Pulse.half).Taking ↔ w.Taking) ∧
      ((w.sample Pulse.half).Dependent ↔ w.Dependent) ∧
      ((w.sample Pulse.half).Embodied ↔ w.Embodied) ∧
      ((w.sample Pulse.half).Transmitting ↔ w.Transmitting) :=
  World.stutter_premises_iff Halving.stutter once

/-- **In two commuted webs, the steps at which a family's stock rises number the same** over a
stretch holding both commuted steps. -/
theorem commuted_rise_count {F C : Type} {W W' : Web F C} {t : Nat} (web : W.Commuted W' t)
    (cs : List C) {S m : Nat} (from_ : S ≤ t) (to : t + 2 ≤ S + m) :
    count (steps S m) (rise (W'.stock cs)) = count (steps S m) (rise (W.stock cs)) :=
  (web.stock cs).rise_count from_ to

end OrderWorlds

end Becoming
