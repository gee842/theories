import GenerativeCore

/-!
Actual reaction participants and the origin of an organizing pool.

Finite input/output lists specify multiplicities over arbitrary species and
reaction types. A retained catalyst appears in BOTH lists. If another copy is
consumed, that additional copy must also occur in the input list: the guard
checks their summed multiplicity against the actual prestate.

The general result traces actual required participants to initial presence or
an actual prefix event that enters the selected pool without a pool input.
Closure is a checked property of the admitted recipes, not a law of all
chemistry. A slow uncatalyzed or other assembly route can invalidate closure.
Count-level origin does not identify individual molecules or their ages.
-/

namespace Generative.LivingOrganization

universe u v

structure Recipe (Species : Type u) where
  inputs : List Species
  outputs : List Species

abbrev Inventory (Species : Type u) := Species → Nat

variable {Species : Type u} {Reaction : Type v} [DecidableEq Species]

def process (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop) :
    Process (Inventory Species) Reaction where
  step before r after := allowed r ∧
    (∀ s, (recipes r).inputs.count s ≤ before s) ∧
    (∀ s, after s + (recipes r).inputs.count s = before s + (recipes r).outputs.count s)

def Touches (pool : Species → Prop) (xs : List Species) : Prop :=
  ∃ s, s ∈ xs ∧ pool s

instance touchesDecidable (pool : Species → Prop) [DecidablePred pool]
    (xs : List Species) : Decidable (Touches pool xs) :=
  inferInstanceAs (Decidable (∃ s, s ∈ xs ∧ pool s))

def Present (pool : Species → Prop) (state : Inventory Species) : Prop :=
  ∃ s, pool s ∧ 0 < state s

/-- Structural closure concerns every way a recipe produces a pool member. -/
def Closed (pool : Species → Prop) (recipe : Recipe Species) : Prop :=
  Touches pool recipe.outputs → Touches pool recipe.inputs

/-- Entry need not mean de novo material creation. Assembly from retained
subunits outside the selected pool is an honest entry into that pool. -/
def Entry (pool : Species → Prop) (recipe : Recipe Species) : Prop :=
  Touches pool recipe.outputs ∧ ¬ Touches pool recipe.inputs

theorem required_pool_is_present (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop)
    {before after : Inventory Species} {r : Reaction}
    (actual : (process recipes allowed).step before r after)
    (required : Touches pool (recipes r).inputs) : Present pool before := by
  obtain ⟨s, occurs, selected⟩ := required
  exact ⟨s, selected, Nat.lt_of_lt_of_le (List.count_pos_iff.mpr occurs) (actual.2.1 s)⟩

/-- A positive pool count after a closed reaction has prior pool support. -/
theorem closed_step_preserves_absence (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop)
    {before after : Inventory Species} {r : Reaction}
    (actual : (process recipes allowed).step before r after)
    (closed : Closed pool (recipes r)) :
    Present pool after → Present pool before := by
  rintro ⟨s, selected, positive⟩
  by_cases inherited : 0 < before s
  · exact ⟨s, selected, inherited⟩
  · have balance := actual.2.2 s
    have produced : 0 < (recipes r).outputs.count s := by omega
    exact required_pool_is_present recipes allowed pool actual
      (closed ⟨s, List.count_pos_iff.mp produced, selected⟩)

/-- This local alternative uses finite-list decisions, not a decision about
whether an arbitrary complete inventory contains any pool species. -/
theorem step_pool_origin (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop) [DecidablePred pool]
    {before after : Inventory Species} {r : Reaction}
    (actual : (process recipes allowed).step before r after) :
    Present pool after → Present pool before ∨ Entry pool (recipes r) := by
  rintro ⟨s, selected, positive⟩
  by_cases inherited : 0 < before s
  · exact Or.inl ⟨s, selected, inherited⟩
  · have balance := actual.2.2 s
    have produced : 0 < (recipes r).outputs.count s := by omega
    by_cases required : Touches pool (recipes r).inputs
    · exact Or.inl (required_pool_is_present recipes allowed pool actual required)
    · exact Or.inr ⟨⟨s, List.count_pos_iff.mp produced, selected⟩, required⟩

/-- All prefix and suffix states belong to the original actual history. -/
def EntryOccurs (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop)
    (pool : Species → Prop) (initial : Inventory Species) (word : List Reaction)
    (finalState : Inventory Species) : Prop :=
  ∃ preWord r postWord before after,
    word = preWord ++ r :: postWord ∧
    Trace (process recipes allowed) initial preWord before ∧
    (process recipes allowed).step before r after ∧
    Trace (process recipes allowed) after postWord finalState ∧
    Entry pool (recipes r)

theorem entry_prepend (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop)
    {initial middle finalState : Inventory Species} {r : Reaction} {word : List Reaction}
    (first : (process recipes allowed).step initial r middle)
    (later : EntryOccurs recipes allowed pool middle word finalState) :
    EntryOccurs recipes allowed pool initial (r :: word) finalState := by
  obtain ⟨preWord, source, postWord, before, after, decomposition, pre, step, post, entry⟩ := later
  refine ⟨r :: preWord, source, postWord, before, after, ?_,
    Trace.cons first pre, step, post, entry⟩
  simp [decomposition]

/-- Final pool presence entails initial presence or an actual entry event.
The first branch does not prove that an initial member survived, was used, or
was a causal ancestor of a later member. It is a pool-presence disjunction. -/
theorem trace_pool_origin (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop) [DecidablePred pool]
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    (present : Present pool finalState) :
    Present pool initial ∨ EntryOccurs recipes allowed pool initial word finalState := by
  induction history with
  | nil => exact Or.inl present
  | @cons initial middle finalState r word first rest ih =>
    cases ih present with
    | inr later => exact Or.inr (entry_prepend recipes allowed pool first later)
    | inl middlePresent =>
      cases step_pool_origin recipes allowed pool first middlePresent with
      | inl inherited => exact Or.inl inherited
      | inr entered =>
        exact Or.inr ⟨[], r, word, initial, middle, rfl, Trace.nil _, first, rest, entered⟩

/-- Closure must cover every admitted recipe; the conclusion is not inferred
from leaving an inconvenient formation route out of the audit. -/
theorem empty_pool_preserved (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop)
    (allClosed : ∀ r, allowed r → Closed pool (recipes r))
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    (absent : ¬ Present pool initial) : ¬ Present pool finalState := by
  induction history with
  | nil => exact absent
  | cons first rest ih =>
    apply ih
    intro present
    exact absent (closed_step_preserves_absence recipes allowed pool first
      (allClosed _ first.1) present)

/-- The origin concerns an actual required participant of an actual operation,
not a supplied label asserting that the final configuration is alive. -/
theorem actual_operation_origin (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop) [DecidablePred pool]
    {initial before after : Inventory Species} {word : List Reaction} {r : Reaction}
    (history : Trace (process recipes allowed) initial word before)
    (actual : (process recipes allowed).step before r after)
    (required : Touches pool (recipes r).inputs) :
    Present pool initial ∨ EntryOccurs recipes allowed pool initial word before :=
  trace_pool_origin recipes allowed pool history
    (required_pool_is_present recipes allowed pool actual required)

/-- Apply this to an actual suffix beginning at an established empty reached
state. Any later required operation needs entry AFTER that state, even if an
earlier part of the whole history once contained a pool member. -/
theorem operation_after_empty_state_requires_entry (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop) [DecidablePred pool]
    {emptyState before after : Inventory Species} {word : List Reaction} {r : Reaction}
    (absent : ¬ Present pool emptyState)
    (history : Trace (process recipes allowed) emptyState word before)
    (actual : (process recipes allowed).step before r after)
    (required : Touches pool (recipes r).inputs) :
    EntryOccurs recipes allowed pool emptyState word before := by
  cases actual_operation_origin recipes allowed pool history actual required with
  | inl present => exact False.elim (absent present)
  | inr entry => exact entry

theorem no_actual_operation_from_closed_empty_pool (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (pool : Species → Prop)
    (allClosed : ∀ r, allowed r → Closed pool (recipes r))
    {initial before after : Inventory Species} {word : List Reaction} {r : Reaction}
    (absent : ¬ Present pool initial)
    (history : Trace (process recipes allowed) initial word before)
    (actual : (process recipes allowed).step before r after)
    (required : Touches pool (recipes r).inputs) : False :=
  empty_pool_preserved recipes allowed pool allClosed history absent
    (required_pool_is_present recipes allowed pool actual required)

/-! Structural illustration only. The assembly and activation recipes below
are supplied. They are not a calibrated ribosome model or a claim that the
listed species suffice for translation, or that measured mutants are empty. -/

inductive Component where
  | active | protectedPair | left | right | substrate | product | support | spent
  deriving DecidableEq, Repr

inductive Operation where
  | protect | activate | assemble | separate | produce
  deriving DecidableEq, Repr

def exampleRecipes : Operation → Recipe Component
  | .protect => ⟨[.active, .active], [.protectedPair]⟩
  | .activate => ⟨[.protectedPair, .support], [.active, .active, .spent]⟩
  | .assemble => ⟨[.left, .right, .support], [.active, .spent]⟩
  | .separate => ⟨[.active], [.left, .right]⟩
  | .produce => ⟨[.active, .substrate, .support], [.active, .product, .spent]⟩

def organizingPool (c : Component) : Prop := c = .active ∨ c = .protectedPair

instance organizingPoolDecidable : DecidablePred organizingPool := fun c =>
  inferInstanceAs (Decidable (c = .active ∨ c = .protectedPair))

def retainedRoutes (r : Operation) : Prop := r ≠ .assemble
def allRoutes (_ : Operation) : Prop := True
def stocked (parts : List Component) : Inventory Component := fun c => parts.count c

def protectedStart := stocked [.protectedPair, .substrate, .support, .support]
def activeStart := stocked [.active, .active, .substrate, .support, .support]
def partsStart := stocked [.left, .left, .right, .right, .substrate, .support, .support]
def activated := stocked [.active, .active, .substrate, .support, .spent]
def protectedProduct := stocked [.active, .active, .product, .spent, .spent]
def assembled := stocked [.active, .left, .right, .substrate, .support, .spent]
def assembledProduct := stocked [.active, .left, .right, .product, .spent, .spent]

def material (s : Inventory Component) : Nat :=
  2 * s .active + 4 * s .protectedPair + s .left + s .right +
    s .substrate + s .product + s .support + s .spent

/-- This particular illustration preserves declared component weights.
Arbitrary input/output lists in the general theorem need not conserve them. -/
theorem example_step_preserves_material (allowed : Operation → Prop)
    {before after : Inventory Component} {r : Operation}
    (actual : (process exampleRecipes allowed).step before r after) :
    material after = material before := by
  have active := actual.2.2 Component.active
  have protectedCount := actual.2.2 Component.protectedPair
  have left := actual.2.2 Component.left
  have right := actual.2.2 Component.right
  have substrate := actual.2.2 Component.substrate
  have product := actual.2.2 Component.product
  have support := actual.2.2 Component.support
  have spent := actual.2.2 Component.spent
  cases r <;> simp [exampleRecipes] at active protectedCount left right substrate product support spent <;>
    simp only [material] <;> omega

theorem example_trace_preserves_material (allowed : Operation → Prop)
    {before after : Inventory Component} {word : List Operation}
    (history : Trace (process exampleRecipes allowed) before word after) :
    material after = material before := by
  induction history with
  | nil => rfl
  | cons first rest ih => exact ih.trans (example_step_preserves_material allowed first)

theorem retained_recipes_are_closed :
    ∀ r, retainedRoutes r → Closed organizingPool (exampleRecipes r) := by
  intro r allowed
  cases r <;> simp [retainedRoutes, Closed, Touches, exampleRecipes, organizingPool] at *

theorem assembly_is_pool_entry : Entry organizingPool (exampleRecipes .assemble) := by
  simp [Entry, Touches, exampleRecipes, organizingPool]

theorem parts_have_no_organizing_pool : ¬ Present organizingPool partsStart := by
  rintro ⟨c, (rfl | rfl), positive⟩ <;> simp [partsStart, stocked] at positive

theorem matched_material_and_support :
    material protectedStart = material partsStart ∧
      material activeStart = material partsStart ∧
      protectedStart .support = partsStart .support ∧
      activeStart .support = partsStart .support ∧
      protectedStart .substrate = partsStart .substrate := by
  decide

/-- The matched active organization supports an immediate actual operation. -/
theorem active_form_can_immediately_produce :
    Enabled (process exampleRecipes allRoutes) activeStart .produce := by
  refine ⟨stocked [.active, .active, .product, .support, .spent], trivial, ?_, ?_⟩ <;>
    intro c <;> cases c <;> decide

/-- Same bulk material and support do not entail the same immediate operation. -/
theorem dissociated_parts_do_not_enable_production :
    ¬ Enabled (process exampleRecipes allRoutes) partsStart .produce := by
  rintro ⟨after, actual⟩
  have requiresActive := actual.2.1 Component.active
  simp [exampleRecipes, partsStart, stocked] at requiresActive

theorem protected_form_does_not_immediately_produce :
    ¬ Enabled (process exampleRecipes allRoutes) protectedStart .produce := by
  rintro ⟨after, actual⟩
  have requiresActive := actual.2.1 Component.active
  simp [exampleRecipes, protectedStart, stocked] at requiresActive

/-- Actual retention and activation precede actual product formation. -/
theorem retained_activation_and_production :
    Trace (process exampleRecipes retainedRoutes) protectedStart [.activate, .produce] protectedProduct ∧
      protectedProduct .product = 1 ∧ protectedProduct .active = 2 := by
  have activation : (process exampleRecipes retainedRoutes).step protectedStart .activate activated := by
    refine ⟨by simp [retainedRoutes], ?_, ?_⟩ <;> intro c <;> cases c <;> decide
  have production : (process exampleRecipes retainedRoutes).step activated .produce protectedProduct := by
    refine ⟨by simp [retainedRoutes], ?_, ?_⟩ <;> intro c <;> cases c <;> decide
  exact ⟨Trace.cons activation (Trace.cons production (Trace.nil _)), by decide, by decide⟩

/-- Allowing actual assembly supplies a different, checked entry route. -/
theorem assembly_and_production :
    Trace (process exampleRecipes allRoutes) partsStart [.assemble, .produce] assembledProduct ∧
      assembledProduct .product = 1 ∧ assembledProduct .active = 1 := by
  have assembly : (process exampleRecipes allRoutes).step partsStart .assemble assembled := by
    refine ⟨trivial, ?_, ?_⟩ <;> intro c <;> cases c <;> decide
  have production : (process exampleRecipes allRoutes).step assembled .produce assembledProduct := by
    refine ⟨trivial, ?_, ?_⟩ <;> intro c <;> cases c <;> decide
  exact ⟨Trace.cons assembly (Trace.cons production (Trace.nil _)), by decide, by decide⟩

/-- Every actual productive continuation from these parts needs an actual
entry in its preceding history; no specific entry recipe is asserted necessary. -/
theorem production_from_parts_requires_entry
    {before after : Inventory Component} {word : List Operation}
    (history : Trace (process exampleRecipes allRoutes) partsStart word before)
    (production : (process exampleRecipes allRoutes).step before .produce after) :
    EntryOccurs exampleRecipes allRoutes organizingPool partsStart word before := by
  have required : Touches organizingPool (exampleRecipes .produce).inputs := by
    simp [Touches, exampleRecipes, organizingPool]
  exact operation_after_empty_state_requires_entry exampleRecipes allRoutes organizingPool
    parts_have_no_organizing_pool history production required

/-- The absence conclusion is explicitly restricted to the closed repertoire;
the preceding assembly witness prevents promoting it to physical impossibility. -/
theorem retained_routes_do_not_bootstrap_from_parts
    {before after : Inventory Component} {word : List Operation}
    (history : Trace (process exampleRecipes retainedRoutes) partsStart word before)
    (production : (process exampleRecipes retainedRoutes).step before .produce after) : False := by
  apply no_actual_operation_from_closed_empty_pool exampleRecipes retainedRoutes organizingPool
    retained_recipes_are_closed parts_have_no_organizing_pool history production
  simp [Touches, exampleRecipes, organizingPool]

end Generative.LivingOrganization
