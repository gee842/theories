import LivingOrganization

/-!
Joint participant allocation within untimed batches of actual reactions.

A batch is the aggregate recipe of its member reactions. All input copies,
including retained catalytic participants, must fit the same prestate. This
declared discipline applies to exclusively allocated participants, not every
shared enabling relationship. Serialization constructs an admissible ordering
under the existing positive-input guards, without unrepresented inhibitors or
spatial interference. It does not establish a molecular temporal observation,
physical simultaneous execution, or a clock: sequential reuse can be feasible
when joint allocation is not.

The horizon bound counts allocated participant uses over declared batches.
Actual positive changes of a selected count can expand later allocation;
activation or import counts as such a change, not necessarily new machinery.
-/

namespace Generative.LivingAllocation

open LivingOrganization

universe u v

variable {Species : Type u} {Reaction : Type v} [DecidableEq Species]

def aggregate (recipes : Reaction → Recipe Species) (word : List Reaction) :
    Recipe Species :=
  ⟨word.flatMap (fun r => (recipes r).inputs),
   word.flatMap (fun r => (recipes r).outputs)⟩

def batchProcess (recipes : Reaction → Recipe Species) (allowed : Reaction → Prop) :
    Process (Inventory Species) (List Reaction) :=
  process (aggregate recipes) (fun word => ∀ r ∈ word, allowed r)

/-- Construct an admissible serialization with every intermediate inventory;
no fresh support is inserted between jointly allocated members. An empirical
observation of the batch alone would not establish this temporal ordering. -/
theorem batch_serializes (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) {before after : Inventory Species}
    {word : List Reaction}
    (actual : (batchProcess recipes allowed).step before word after) :
    Trace (process recipes allowed) before word after := by
  induction word generalizing before with
  | nil =>
    have same : after = before := by
      funext s
      simpa [batchProcess, process, aggregate] using actual.2.2 s
    subst after
    exact .nil _
  | cons r word ih =>
    let middle : Inventory Species := fun s =>
      before s - (recipes r).inputs.count s + (recipes r).outputs.count s
    have first : (process recipes allowed).step before r middle := by
      refine ⟨actual.1 r (by simp), ?_, ?_⟩
      · intro s
        have allocated := actual.2.1 s
        simp only [aggregate, List.flatMap_cons, List.count_append] at allocated
        omega
      · intro s
        have allocated := actual.2.1 s
        simp only [aggregate, List.flatMap_cons, List.count_append] at allocated
        dsimp [middle]
        omega
    have rest : (batchProcess recipes allowed).step middle word after := by
      refine ⟨?_, ?_, ?_⟩
      · intro q member
        exact actual.1 q (by simp [member])
      · intro s
        have allocated := actual.2.1 s
        simp only [aggregate, List.flatMap_cons, List.count_append] at allocated
        dsimp [aggregate, middle]
        omega
      · intro s
        have allocated := actual.2.1 s
        have balanced := actual.2.2 s
        simp only [aggregate, List.flatMap_cons, List.count_append] at allocated balanced
        dsimp [aggregate, middle]
        omega
    exact .cons first (ih rest)

/-- Successive batches compose through their actual reached inventories. -/
theorem batches_serialize (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) {before after : Inventory Species}
    {batches : List (List Reaction)}
    (actual : Trace (batchProcess recipes allowed) before batches after) :
    Trace (process recipes allowed) before batches.flatten after := by
  induction actual with
  | nil => exact .nil _
  | cons first rest ih =>
    exact trace_append_iff.mpr ⟨_, batch_serializes recipes allowed first, ih⟩

def usesIn (uses : Reaction → Nat) (word : List Reaction) : Nat :=
  (word.map uses).sum

/-- The premise checks input multiplicity of each admitted recipe, not a
supplied state-level capacity inequality. Units are allocated uses. -/
theorem uses_le_aggregate_inputs (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species) (uses : Reaction → Nat)
    (requires : ∀ r, allowed r → uses r ≤ (recipes r).inputs.count participant)
    {word : List Reaction} (admitted : ∀ r ∈ word, allowed r) :
    usesIn uses word ≤ (aggregate recipes word).inputs.count participant := by
  induction word with
  | nil => simp [usesIn, aggregate]
  | cons r word ih =>
    have first := requires r (admitted r (by simp))
    have rest := ih (fun q member => admitted q (by simp [member]))
    simpa [usesIn, aggregate] using Nat.add_le_add first rest

theorem batch_uses_bound (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species) (uses : Reaction → Nat)
    (requires : ∀ r, allowed r → uses r ≤ (recipes r).inputs.count participant)
    {before after : Inventory Species} {word : List Reaction}
    (actual : (batchProcess recipes allowed).step before word after) :
    usesIn uses word ≤ before participant :=
  Nat.le_trans (uses_le_aggregate_inputs recipes allowed participant uses requires actual.1)
    (actual.2.1 participant)

/-- Retained catalytic copies appear on both sides and do not count as a
positive increase merely because they also occur in the output list. -/
def increase (recipes : Reaction → Recipe Species) (participant : Species)
    (word : List Reaction) : Nat :=
  (aggregate recipes word).outputs.count participant -
    (aggregate recipes word).inputs.count participant

theorem increase_eq_actual (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species)
    {before after : Inventory Species} {word : List Reaction}
    (actual : (batchProcess recipes allowed).step before word after) :
    increase recipes participant word = after participant - before participant := by
  have balance := actual.2.2 participant
  unfold increase
  omega

theorem count_after_le (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species)
    {before after : Inventory Species} {word : List Reaction}
    (actual : (batchProcess recipes allowed).step before word after) :
    after participant ≤ before participant + increase recipes participant word := by
  have balance := actual.2.2 participant
  unfold increase
  omega

def totalUses (uses : Reaction → Nat) : List (List Reaction) → Nat
  | [] => 0
  | word :: rest => usesIn uses word + totalUses uses rest

/-- An increase is credited only in the remaining batches, never within the
batch that forms it. Losses are permitted; this is an upper bound. -/
def laterCredit (recipes : Reaction → Recipe Species) (participant : Species) :
    List (List Reaction) → Nat
  | [] => 0
  | word :: rest => rest.length * increase recipes participant word +
      laterCredit recipes participant rest

theorem allocation_horizon_bound (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species) (uses : Reaction → Nat)
    (requires : ∀ r, allowed r → uses r ≤ (recipes r).inputs.count participant)
    {before after : Inventory Species} {batches : List (List Reaction)}
    (actual : Trace (batchProcess recipes allowed) before batches after) :
    totalUses uses batches ≤ batches.length * before participant +
      laterCredit recipes participant batches := by
  induction actual with
  | nil => simp [totalUses, laterCredit]
  | @cons before middle after word rest first history ih =>
    have allocated := batch_uses_bound recipes allowed participant uses requires first
    have retained := count_after_le recipes allowed participant first
    have scaled := Nat.mul_le_mul_left rest.length retained
    simp only [Nat.mul_add] at scaled
    simp only [totalUses, List.length_cons, laterCredit, Nat.succ_mul]
    omega

theorem credit_zero_without_increases (recipes : Reaction → Recipe Species)
    (participant : Species) {batches : List (List Reaction)}
    (noIncrease : ∀ word ∈ batches, increase recipes participant word = 0) :
    laterCredit recipes participant batches = 0 := by
  induction batches with
  | nil => rfl
  | cons word rest ih =>
    have first := noIncrease word (by simp)
    have later := ih (fun q member => noIncrease q (by simp [member]))
    simp [laterCredit, first, later]

theorem allocation_bound_without_increases (recipes : Reaction → Recipe Species)
    (allowed : Reaction → Prop) (participant : Species) (uses : Reaction → Nat)
    (requires : ∀ r, allowed r → uses r ≤ (recipes r).inputs.count participant)
    {before after : Inventory Species} {batches : List (List Reaction)}
    (actual : Trace (batchProcess recipes allowed) before batches after)
    (noIncrease : ∀ word ∈ batches, increase recipes participant word = 0) :
    totalUses uses batches ≤ batches.length * before participant := by
  have bound := allocation_horizon_bound recipes allowed participant uses requires actual
  simpa [credit_zero_without_increases recipes participant noIncrease] using bound

/- A structural illustration, not a fitted ribosome or growth-rate model. -/

inductive Participant where
  | active | inactive | substrate | product | support | spent
  deriving DecidableEq, Repr

inductive Activity where
  | activate | produce
  deriving DecidableEq, Repr

def exampleRecipes : Activity → Recipe Participant
  | .activate => ⟨[.active, .inactive, .support], [.active, .active, .spent]⟩
  | .produce => ⟨[.active, .substrate, .support], [.active, .product, .spent]⟩

def allActivities (_ : Activity) : Prop := True

def stock (active inactive substrate product support spent : Nat) : Inventory Participant
  | .active => active
  | .inactive => inactive
  | .substrate => substrate
  | .product => product
  | .support => support
  | .spent => spent

def productiveUses : Activity → Nat
  | .activate => 0
  | .produce => 1

theorem example_requires_participant : ∀ r, allActivities r →
    productiveUses r ≤ (exampleRecipes r).inputs.count .active := by
  intro r _
  cases r <;> decide

def partialStart := stock 1 1 4 0 5 0
def activatedStart := stock 2 0 4 0 4 1
def twoProducts := stock 2 0 2 2 2 3
def fourProducts := stock 2 0 0 4 0 5

/-- Both production and activation require the single available active copy;
checking the two recipes independently would incorrectly double-book it. -/
theorem activation_and_production_compete :
    Enabled (process exampleRecipes allActivities) partialStart .activate ∧
    Enabled (process exampleRecipes allActivities) partialStart .produce ∧
    ¬ Enabled (batchProcess exampleRecipes allActivities) partialStart [.activate, .produce] := by
  refine ⟨⟨activatedStart, trivial, ?_, ?_⟩,
    ⟨stock 1 1 3 1 4 1, trivial, ?_, ?_⟩, ?_⟩
  · intro s; cases s <;> decide
  · intro s; cases s <;> decide
  · intro s; cases s <;> decide
  · intro s; cases s <;> decide
  · rintro ⟨after, actual⟩
    have allocated := actual.2.1 Participant.active
    simp [aggregate, exampleRecipes, partialStart, stock] at allocated

/-- Support is also allocated jointly, even when enough active copies exist. -/
theorem shared_support_competes :
    ¬ Enabled (batchProcess exampleRecipes allActivities) (stock 2 1 1 0 1 0)
      [.activate, .produce] := by
  rintro ⟨after, actual⟩
  have allocated := actual.2.1 Participant.support
  simp [aggregate, exampleRecipes, stock] at allocated

theorem activation_then_four_products :
    Trace (batchProcess exampleRecipes allActivities) partialStart
      [[.activate], [.produce, .produce], [.produce, .produce]] fourProducts ∧
      fourProducts .product = 4 ∧ fourProducts .active = 2 := by
  have first : (batchProcess exampleRecipes allActivities).step partialStart
      [.activate] activatedStart := by
    refine ⟨by simp [allActivities], ?_, ?_⟩ <;>
      intro s <;> cases s <;> decide
  have second : (batchProcess exampleRecipes allActivities).step activatedStart
      [.produce, .produce] twoProducts := by
    refine ⟨by simp [allActivities], ?_, ?_⟩ <;>
      intro s <;> cases s <;> decide
  have third : (batchProcess exampleRecipes allActivities).step twoProducts
      [.produce, .produce] fourProducts := by
    refine ⟨by simp [allActivities], ?_, ?_⟩ <;>
      intro s <;> cases s <;> decide
  exact ⟨.cons first (.cons second (.cons third (.nil _))), rfl, rfl⟩

theorem production_only_has_no_increase {word : List Activity}
    (onlyProduction : ∀ r ∈ word, r = .produce) :
    increase exampleRecipes Participant.active word = 0 := by
  have same : (aggregate exampleRecipes word).outputs.count Participant.active =
      (aggregate exampleRecipes word).inputs.count Participant.active := by
    induction word with
    | nil => rfl
    | cons r word ih =>
      have first := onlyProduction r (by simp)
      have rest := ih (fun q member => onlyProduction q (by simp [member]))
      subst r
      simpa [aggregate, exampleRecipes] using rest
  simp [increase, same]

/-- A positive initial count supports work. Without actual increases, three
declared allocation batches permit at most three productive uses. -/
theorem three_batches_without_activation {after : Inventory Participant}
    {batches : List (List Activity)}
    (actual : Trace (batchProcess exampleRecipes allActivities) partialStart batches after)
    (three : batches.length = 3)
    (onlyProduction : ∀ word ∈ batches, ∀ r ∈ word, r = .produce) :
    totalUses productiveUses batches ≤ 3 := by
  have bound := allocation_bound_without_increases exampleRecipes allActivities
    Participant.active productiveUses example_requires_participant actual
    (fun word member => production_only_has_no_increase (onlyProduction word member))
  simpa [three, partialStart, stock] using bound

/-- Feasible serial reuse does not entail joint admission. In particular,
one batch must not be identified with an arbitrary elapsed-time interval. -/
theorem sequential_reuse_exceeds_joint_allocation :
    Trace (process exampleRecipes allActivities) (stock 1 0 2 0 2 0)
      [.produce, .produce] (stock 1 0 0 2 0 2) ∧
    ¬ Enabled (batchProcess exampleRecipes allActivities) (stock 1 0 2 0 2 0)
      [.produce, .produce] := by
  have first : (process exampleRecipes allActivities).step (stock 1 0 2 0 2 0)
      .produce (stock 1 0 1 1 1 1) := by
    refine ⟨trivial, ?_, ?_⟩ <;> intro s <;> cases s <;> decide
  have second : (process exampleRecipes allActivities).step (stock 1 0 1 1 1 1)
      .produce (stock 1 0 0 2 0 2) := by
    refine ⟨trivial, ?_, ?_⟩ <;> intro s <;> cases s <;> decide
  refine ⟨.cons first (.cons second (.nil _)), ?_⟩
  rintro ⟨after, actual⟩
  have allocated := actual.2.1 Participant.active
  simp [aggregate, exampleRecipes, stock] at allocated

end Generative.LivingAllocation
