import Becoming.Gated
import LivingOrganization

/-!
# The origin of an organizing pool as an instance of the gate laws

`LivingOrganization` traces a pool present at the end of an actual reaction history to initial
presence or an actual entry event. Read with the gate `entryGate` (a recipe that outputs a pool
member while taking none in), every other step reflects pool presence (`presence_reflected`).
The origin then follows from the core's `Becoming.Gated.origin` (`trace_pool_origin_by_core`),
which adds that the pool is present right after the entry step and decides nothing about the
pool beyond the recipe lists. Where every admitted recipe is closed, the gate never opens and the
core's `reflected_along` keeps an empty pool empty (`empty_pool_preserved_by_core`).

Recipes, the admitted reactions and the selected pool keep `LivingOrganization`'s scope: closure
is a checked property of the admitted recipes, not a law of all chemistry.
-/

namespace Becoming.LivingOrganizationCorrespondence

open Generative Generative.LivingOrganization

universe u v

variable {Species : Type u} {Reaction : Type v} [DecidableEq Species]

/-- Whether a recipe enters the pool is decided from its two finite lists. -/
instance entryDecidable (pool : Species → Prop) [DecidablePred pool] (recipe : Recipe Species) :
    Decidable (Entry pool recipe) :=
  inferInstanceAs (Decidable (Touches pool recipe.outputs ∧ ¬ Touches pool recipe.inputs))

/-- A reaction passes the gate where its recipe enters the pool: it outputs a pool member and
takes none in. -/
def entryGate (recipes : Reaction → Recipe Species) (pool : Species → Prop) [DecidablePred pool]
    (r : Reaction) : Bool :=
  decide (Entry pool (recipes r))

/-- **Every step that is not an entry reflects pool presence.** -/
theorem presence_reflected (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop)
    (pool : Species → Prop) [DecidablePred pool] :
    Gated.ReflectedBy (process recipes allowed) (entryGate recipes pool) (Present pool) :=
  fun _ _ _ step ungated present =>
    (step_pool_origin recipes allowed pool step present).resolve_right (of_decide_eq_false ungated)

/-- **`trace_pool_origin` from the core's origin law.** A pool present at the end was present
initially, or an entry step occurs after which the pool is present. -/
theorem trace_pool_origin_by_core (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop) [DecidablePred pool]
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    (present : Present pool finalState) :
    Present pool initial ∨ EntryOccurs recipes allowed pool initial word finalState :=
  match Gated.origin (presence_reflected recipes allowed pool) history present with
  | .inl atStart => .inl atStart
  | .inr ⟨pre, r, post, before, after, split, path, step, gated, _, rest⟩ =>
    .inr ⟨pre, r, post, before, after, split, path, step, rest, of_decide_eq_true gated⟩

/-- The core's origin law gives more than `EntryOccurs`: the pool is present right after the
entry step. -/
theorem entry_then_present (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop) [DecidablePred pool]
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    (present : Present pool finalState) :
    Present pool initial ∨ ∃ pre r post before after, word = pre ++ r :: post ∧
      Trace (process recipes allowed) initial pre before ∧
      (process recipes allowed).step before r after ∧ Entry pool (recipes r) ∧
      Present pool after ∧ Trace (process recipes allowed) after post finalState :=
  match Gated.origin (presence_reflected recipes allowed pool) history present with
  | .inl atStart => .inl atStart
  | .inr ⟨pre, r, post, before, after, split, path, step, gated, holds, rest⟩ =>
    .inr ⟨pre, r, post, before, after, split, path, step, of_decide_eq_true gated, holds, rest⟩

/-- **`empty_pool_preserved` from the core.** Where every admitted recipe is closed, every step
reflects pool presence with no gate at all, so an empty pool stays empty along the history. -/
theorem empty_pool_preserved_by_core (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop)
    (allClosed : ∀ r, allowed r → Closed pool (recipes r))
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    (absent : ¬ Present pool initial) : ¬ Present pool finalState :=
  fun present => absent
    (Gated.reflected_along (gate := fun _ => false)
      (fun _ r _ step _ later =>
        closed_step_preserves_absence recipes allowed pool step (allClosed r step.1) later)
      history (fun _ _ => rfl) present)

end Becoming.LivingOrganizationCorrespondence
