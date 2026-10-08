import LivingOrganization

/-!
Disjoint current provision and a prior increase of the selected functional pool.

An occurrence index is local to one reached inventory, not molecular identity
across time. An explicit assignment certifies different copies for coexisting
centers. Variable requirements and the correspondence of centers/copies to a
living phenotype remain supplied; assignment alone is not physiological success.

The result concerns the current provision frontier, never cumulative births.
No lifetime, use depletion, physical clock, growth rate or universal one-copy
requirement is imposed. A prior count increase can be activation, assembly or
import, and is not a genealogy or causal-use claim about current participants.
-/

namespace Generative.LivingExpansion

open LivingOrganization

universe u v w

variable {Center : Type w}

def requiredTotal (centers : List Center) (required : Center → Nat) : Nat :=
  (centers.map required).sum

/-- Distinct current centers are actually assigned distinct present occurrence
indices. This structure does not assume the total-requirement bound. -/
structure CurrentProvision (count : Nat) (centers : List Center)
    (required : Center → Nat) (assigned : Center → List Nat) : Prop where
  distinctCenters : centers.Nodup
  adequate : ∀ c ∈ centers, required c ≤ (assigned c).length
  distinctCopies : (centers.flatMap assigned).Nodup
  present : ∀ n ∈ centers.flatMap assigned, n < count

/-- The elementary finite allocation lemma derives a bound from distinct
actual occurrences rather than assuming a summed capacity inequality. -/
theorem distinct_subset_length {xs ys : List Nat} (distinct : xs.Nodup)
    (contained : ∀ n ∈ xs, n ∈ ys) : xs.length ≤ ys.length := by
  have remove : ∀ (x : Nat) (pool : List Nat), x ∈ pool →
      ∃ rest : List Nat, rest.length + 1 = pool.length ∧
        ∀ n, n ∈ pool → n ≠ x → n ∈ rest := by
    intro x pool
    induction pool with
    | nil => intro impossible; cases impossible
    | cons y pool ih =>
      intro member
      by_cases same : y = x
      · subst y
        refine ⟨pool, rfl, ?_⟩
        intro n present different
        rcases List.mem_cons.mp present with equal | later
        · exact False.elim (different equal)
        · exact later
      · have later : x ∈ pool := by
          rcases List.mem_cons.mp member with equal | later
          · exact False.elim (same equal.symm)
          · exact later
        obtain ⟨rest, size, kept⟩ := ih later
        refine ⟨y :: rest, ?_, ?_⟩
        · simp only [List.length_cons]
          omega
        · intro n present different
          rcases List.mem_cons.mp present with equal | later
          · exact List.mem_cons.mpr (Or.inl equal)
          · exact List.mem_cons.mpr (Or.inr (kept n later different))
  induction xs generalizing ys with
  | nil => simp
  | cons x xs ih =>
    obtain ⟨notAgain, restDistinct⟩ := List.nodup_cons.mp distinct
    obtain ⟨remaining, size, kept⟩ := remove x ys (contained x (by simp))
    have rest : ∀ n ∈ xs, n ∈ remaining := by
      intro n member
      have different : n ≠ x := by
        intro same
        subst n
        exact notAgain member
      exact kept n (contained n (by simp [member])) different
    have bounded := ih restDistinct rest
    simp only [List.length_cons]
    omega

theorem requirements_le_assigned (centers : List Center) (required : Center → Nat)
    (assigned : Center → List Nat)
    (adequate : ∀ c ∈ centers, required c ≤ (assigned c).length) :
    requiredTotal centers required ≤ (centers.flatMap assigned).length := by
  induction centers with
  | nil => simp [requiredTotal]
  | cons c centers ih =>
    have first := adequate c (by simp)
    have rest := ih (fun d member => adequate d (by simp [member]))
    simpa [requiredTotal, List.length_flatMap] using Nat.add_le_add first rest

theorem current_provision_bound {count : Nat} {centers : List Center}
    {required : Center → Nat} {assigned : Center → List Nat}
    (provision : CurrentProvision count centers required assigned) :
    requiredTotal centers required ≤ count := by
  have allocated := distinct_subset_length provision.distinctCopies
    (ys := List.range count) (fun n member => List.mem_range.mpr (provision.present n member))
  have needed := requirements_le_assigned centers required assigned provision.adequate
  simpa using Nat.le_trans needed allocated

theorem uniform_requirements_lower_bound (centers : List Center)
    (required : Center → Nat) (minimum : Nat)
    (each : ∀ c ∈ centers, minimum ≤ required c) :
    minimum * centers.length ≤ requiredTotal centers required := by
  induction centers with
  | nil => simp [requiredTotal]
  | cons c centers ih =>
    have first := each c (by simp)
    have rest := ih (fun d member => each d (by simp [member]))
    simp only [List.length_cons, Nat.mul_succ, requiredTotal, List.map_cons, List.sum_cons]
    unfold requiredTotal at rest
    omega

theorem uniform_current_provision_bound {count : Nat} {centers : List Center}
    {required : Center → Nat} {assigned : Center → List Nat}
    (provision : CurrentProvision count centers required assigned) (minimum : Nat)
    (each : ∀ c ∈ centers, minimum ≤ required c) :
    minimum * centers.length ≤ count :=
  Nat.le_trans (uniform_requirements_lower_bound centers required minimum each)
    (current_provision_bound provision)

variable {Species : Type u} {Reaction : Type v} [DecidableEq Species]

/-- This event really occurs in the supplied reaction history. Both its
reached-state increase and its excess recipe output are retained. -/
def IncreaseOccurs (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop)
    (participant : Species) (initial : Inventory Species) (word : List Reaction)
    (finalState : Inventory Species) : Prop :=
  ∃ preWord r postWord before after,
    word = preWord ++ r :: postWord ∧
    Trace (process recipes allowed) initial preWord before ∧
    (process recipes allowed).step before r after ∧
    Trace (process recipes allowed) after postWord finalState ∧
    before participant < after participant ∧
    (recipes r).inputs.count participant < (recipes r).outputs.count participant

theorem increase_prepend (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species)
    {initial middle finalState : Inventory Species} {r : Reaction} {word : List Reaction}
    (first : (process recipes allowed).step initial r middle)
    (later : IncreaseOccurs recipes allowed participant middle word finalState) :
    IncreaseOccurs recipes allowed participant initial (r :: word) finalState := by
  obtain ⟨preWord, source, postWord, before, after, decomposition,
    pre, step, post, increased, netOutput⟩ := later
  refine ⟨r :: preWord, source, postWord, before, after, ?_,
    .cons first pre, step, post, increased, netOutput⟩
  simp [decomposition]

/-- A net rise at the reached endpoint has an actual prior increasing event.
It does not identify which event supplied any particular final occurrence. -/
theorem reached_increase_has_actual_event (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species)
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    (increased : initial participant < finalState participant) :
    IncreaseOccurs recipes allowed participant initial word finalState := by
  induction history with
  | nil => exact False.elim (Nat.lt_irrefl _ increased)
  | @cons initial middle finalState r word first rest ih =>
    by_cases immediate : initial participant < middle participant
    · have balance := first.2.2 participant
      exact ⟨[], r, word, initial, middle, rfl, .nil _, first, rest, immediate, by omega⟩
    · have later : middle participant < finalState participant := by omega
      exact increase_prepend recipes allowed participant first (ih later)

/-- The antecedent asserts actual endpoint provision, with variable local
requirements and no double-counting. If these exceed inherited copies, a
selected-pool increase occurred; neither its particular route nor ancestry
of the current assignments is inferred. -/
theorem expanded_provision_requires_actual_increase
    (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop) (participant : Species)
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    {centers : List Center} {required : Center → Nat} {assigned : Center → List Nat}
    (provision : CurrentProvision (finalState participant) centers required assigned)
    (beyondInherited : initial participant < requiredTotal centers required) :
    IncreaseOccurs recipes allowed participant initial word finalState := by
  exact reached_increase_has_actual_event recipes allowed participant history
    (Nat.lt_of_lt_of_le beyondInherited (current_provision_bound provision))

/-- An audit of every admitted recipe can establish a no-increase regime.
This is a structural property of that repertoire, not universal chemistry. -/
theorem trace_bound_without_increasing_recipes
    (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop) (participant : Species)
    (noIncrease : ∀ r, allowed r →
      (recipes r).outputs.count participant ≤ (recipes r).inputs.count participant)
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState) :
    finalState participant ≤ initial participant := by
  induction history with
  | nil => exact Nat.le_refl _
  | cons first rest ih =>
    have balance := first.2.2 participant
    have recipe := noIncrease _ first.1
    omega

theorem inherited_provision_bound
    (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop) (participant : Species)
    (noIncrease : ∀ r, allowed r →
      (recipes r).outputs.count participant ≤ (recipes r).inputs.count participant)
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    {centers : List Center} {required : Center → Nat} {assigned : Center → List Nat}
    (provision : CurrentProvision (finalState participant) centers required assigned) :
    requiredTotal centers required ≤ initial participant :=
  Nat.le_trans (current_provision_bound provision)
    (trace_bound_without_increasing_recipes recipes allowed participant noIncrease history)

/-- An independently selected uniform requirement yields a frontier bound;
it is not a claim that all living centers require this participant. -/
theorem inherited_uniform_frontier_bound
    (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop) (participant : Species)
    (noIncrease : ∀ r, allowed r →
      (recipes r).outputs.count participant ≤ (recipes r).inputs.count participant)
    {initial finalState : Inventory Species} {word : List Reaction}
    (history : Trace (process recipes allowed) initial word finalState)
    {centers : List Center} {required : Center → Nat} {assigned : Center → List Nat}
    (provision : CurrentProvision (finalState participant) centers required assigned)
    (minimum : Nat) (each : ∀ c ∈ centers, minimum ≤ required c) :
    minimum * centers.length ≤ initial participant :=
  Nat.le_trans (uniform_requirements_lower_bound centers required minimum each)
    (inherited_provision_bound recipes allowed participant noIncrease history provision)

/- Small allocation checks: no expiry, fixed generation count or clock. -/

def unequalAssignment (center : Nat) : List Nat := if center = 0 then [0, 2] else [3]
def unequalRequirement (center : Nat) : Nat := if center = 0 then 2 else 1

/-- Unequal current allocations leave occurrence 1 unused and intact. -/
theorem finite_reserve_allows_unequal_provision :
    CurrentProvision 4 [0, 1] unequalRequirement unequalAssignment := by
  constructor
  · decide
  · intro c member
    simp at member
    rcases member with rfl | rfl <;> decide
  · decide
  · intro n member
    simp [unequalAssignment] at member
    omega

theorem three_required_centers_exceed_two_copies (assigned : Nat → List Nat) :
    ¬ CurrentProvision 2 [0, 1, 2] (fun _ => 1) assigned := by
  intro provision
  have bound := current_provision_bound provision
  simp [requiredTotal] at bound

/-- Different snapshots can assign the same occurrence to different centers.
This certifies the scope of a snapshot, not an unmodeled transfer mechanism. -/
theorem successive_snapshot_assignments_reuse_an_occurrence :
    CurrentProvision 1 [0] (fun _ : Nat => 1) (fun _ => [0]) ∧
    CurrentProvision 1 [1] (fun _ : Nat => 1) (fun _ => [0]) := by
  constructor <;> constructor
  all_goals first
    | decide
    | (intro c member; simp at *)
    | (intro n member; simp at member; omega)

end Generative.LivingExpansion
