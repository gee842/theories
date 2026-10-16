import Std

/-!
# An explicit generative-premise inference audit

`Whole` denotes continuations within one unfolding. Claims describe differentiated
realizations and their relations within those histories, not independent owners.
The supplied inventory is a representation of proposed favoring grounds: it can
include actual life, support, repair and the absence of a particular loss. It must
include relevant intermediate histories, not just endpoint resources. Preserving
these grounds need not preserve their material carriers or old configurations.

The mathematical inclusion below only preserves the REPRESENTED claims. Its
correspondence to a whole no-loss comparison is an additional application duty.
No enumeration is certified ethically complete merely by inhabiting `Inventory`.
In particular, a new generative claim is not prefiltered through an independent
worthwhileness test; G0 is the positive-relevance premise for such realizations.
If further favorable grounds are admitted, their warrant is supplied, not derived
here. Relevant adverse effects must appear as losses of those grounds or in a
richer correspondence account; their omission never certifies absence of harm.
`Option` abbreviates differentiated feasible responses within one history. This
module does not derive their formation or assert a primitive independent chooser.
Comparisons require shared, stable claim meanings and truthful realization.
Adding descriptive labels to an unchanged continuation is not new generation.
The general `Better` parameter is intended as a strict ethical comparison; its
adequacy and strict-order properties are not established merely by the type.

G0, C, P and N remain separate, visible commitments:
* G0: actual generative realizations have positive ethical relevance;
* C: a fully covered no-loss generative extension warrants strict comparison;
* P: strict comparison among feasible situated alternatives supplies a reason;
* N: a selected option is feasible and is not strictly dominated.
P supplies a reason, not an obligation, authority or actual compliance. N is a
stronger selection-coherence premise. The conditional selection results use C
and N, not G0: there is no unused G0 parameter disguising a derivation of C.
The philosophical defense of C as an articulation of G0 is outside this audit.

The finite example has two actual generative dimensions and four joint profiles.
Two strictly positive appraisals respect every no-loss extension yet disagree
when one realization replaces another. This tests the force of the partial rule,
not the truth of the richer whole account. Its scores are illustration only.
-/

namespace GenerativeComparison

universe u v w

structure Inventory (Whole : Type u) (Claim : Type v) where
  realized : Whole → Claim → Prop
  generative : Claim → Prop

def G0 {Whole : Type u} {Claim : Type v} (inventory : Inventory Whole Claim)
    (PositiveRelevant : Whole → Claim → Prop) : Prop :=
  ∀ history claim, inventory.generative claim → inventory.realized history claim →
    PositiveRelevant history claim

def Extends {Whole : Type u} {Claim : Type v} (inventory : Inventory Whole Claim)
    (first second : Whole) : Prop :=
  ∀ claim, inventory.realized first claim → inventory.realized second claim

def GenerativeExtension {Whole : Type u} {Claim : Type v}
    (inventory : Inventory Whole Claim) (first second : Whole) : Prop :=
  Extends inventory first second ∧
    ∃ claim, inventory.generative claim ∧ inventory.realized second claim ∧
      ¬ inventory.realized first claim

/-- C: a normative comparison principle, not a conclusion from inclusion alone.
    `Better first second` means that the second continuation is strictly better. -/
def ComparisonPrinciple {Whole : Type u} {Claim : Type v}
    (inventory : Inventory Whole Claim) (Better : Whole → Whole → Prop) : Prop :=
  ∀ first second, GenerativeExtension inventory first second → Better first second

structure Situation (Whole : Type u) (Option : Type w) where
  feasible : Option → Prop
  realize : Option → Whole

/-- P: reason for moving from the first option to the second, within this
    differentiated situation. Feasibility/correspondence are supplied here. -/
def PracticalArticulation {Whole : Type u} {Option : Type w}
    (situation : Situation Whole Option) (Better : Whole → Whole → Prop)
    (Reason : Option → Option → Prop) : Prop :=
  ∀ first second, situation.feasible first → situation.feasible second →
    Better (situation.realize first) (situation.realize second) → Reason first second

/-- N is an optional stronger constraint, not the definition of all reasons. -/
def SelectionCoherence {Whole : Type u} {Option : Type w}
    (situation : Situation Whole Option) (Better : Whole → Whole → Prop)
    (Selected : Option → Prop) : Prop :=
  ∀ first, Selected first → situation.feasible first ∧
    ∀ second, situation.feasible second →
      ¬ Better (situation.realize first) (situation.realize second)

/-- Surviving this incomplete filter does not establish final permission or duty. -/
def Survives {Whole : Type u} {Claim : Type v} {Option : Type w}
    (inventory : Inventory Whole Claim) (situation : Situation Whole Option)
    (first : Option) : Prop :=
  situation.feasible first ∧ ∀ second, situation.feasible second →
    ¬ GenerativeExtension inventory (situation.realize first) (situation.realize second)

theorem new_realization_has_positive_relevance {Whole : Type u} {Claim : Type v}
    {inventory : Inventory Whole Claim} {PositiveRelevant : Whole → Claim → Prop}
    (positive : G0 inventory PositiveRelevant) {first second : Whole}
    (extension : GenerativeExtension inventory first second) :
    ∃ claim, PositiveRelevant second claim ∧ ¬ inventory.realized first claim := by
  obtain ⟨_, claim, generative, actual, newClaim⟩ := extension
  exact ⟨claim, positive second claim generative actual, newClaim⟩

theorem generative_extension_irreflexive {Whole : Type u} {Claim : Type v}
    (inventory : Inventory Whole Claim) (history : Whole) :
    ¬ GenerativeExtension inventory history history := by
  rintro ⟨_, claim, _, actual, absent⟩
  exact absent actual

theorem generative_extension_transitive {Whole : Type u} {Claim : Type v}
    {inventory : Inventory Whole Claim} {first second third : Whole}
    (left : GenerativeExtension inventory first second)
    (right : GenerativeExtension inventory second third) :
    GenerativeExtension inventory first third := by
  refine ⟨fun claim actual => right.1 claim (left.1 claim actual), ?_⟩
  obtain ⟨claim, generative, actual, absent⟩ := right.2
  exact ⟨claim, generative, actual, fun old => absent (left.1 claim old)⟩

theorem comparison_supplies_situated_reason {Whole : Type u} {Claim : Type v}
    {Option : Type w} {inventory : Inventory Whole Claim}
    {situation : Situation Whole Option} {Better : Whole → Whole → Prop}
    {Reason : Option → Option → Prop}
    (comparison : ComparisonPrinciple inventory Better)
    (practical : PracticalArticulation situation Better Reason)
    {first second : Option} (firstFeasible : situation.feasible first)
    (secondFeasible : situation.feasible second)
    (extension : GenerativeExtension inventory (situation.realize first)
      (situation.realize second)) : Reason first second :=
  practical first second firstFeasible secondFeasible
    (comparison _ _ extension)

theorem coherent_selection_survives_filter {Whole : Type u} {Claim : Type v}
    {Option : Type w} {inventory : Inventory Whole Claim}
    {situation : Situation Whole Option} {Better : Whole → Whole → Prop}
    {Selected : Option → Prop}
    (comparison : ComparisonPrinciple inventory Better)
    (coherence : SelectionCoherence situation Better Selected)
    {first : Option} (selected : Selected first) : Survives inventory situation first := by
  have coherent := coherence first selected
  exact ⟨coherent.1, fun second feasible extension =>
    coherent.2 second feasible (comparison _ _ extension)⟩

/-- Restricting options removes comparisons; it does not change whole realizations.
    This one-way filter fact is not an ethical improvement by deleting rivals,
    nor a guarantee of justified reasons after substantive self-modification. -/
theorem feasible_restriction_preserves_survivor {Whole : Type u} {Claim : Type v}
    {Option : Type w} {inventory : Inventory Whole Claim}
    {situation : Situation Whole Option} (restricted : Option → Prop)
    {first : Option} (survivor : Survives inventory situation first)
    (retained : restricted first) :
    Survives inventory
      { situation with feasible := fun option => situation.feasible option ∧ restricted option }
      first :=
  ⟨⟨survivor.1, retained⟩, fun second feasible => survivor.2 second feasible.1⟩

/-- The optional filter can be empty even when actions remain feasible. This is
    not a demand to attain a nonexistent final maximum of generative activity. -/
theorem continual_improvement_has_no_survivor {Whole : Type u} {Claim : Type v}
    {Option : Type w} {inventory : Inventory Whole Claim}
    {situation : Situation Whole Option}
    (improvement : ∀ first, situation.feasible first →
      ∃ second, situation.feasible second ∧
        GenerativeExtension inventory (situation.realize first) (situation.realize second)) :
    ∀ first, ¬ Survives inventory situation first := by
  intro first survivor
  obtain ⟨second, feasible, extension⟩ := improvement first survivor.1
  exact survivor.2 second feasible extension

/-! Two dimensions of actual generation, each either realized or absent. The
    representation is deliberately tiny. Neither dimension is an independent
    subject and neither is an external moral veto on generation. -/

abbrev Profile := Bool × Bool

def profileInventory : Inventory Profile Bool where
  realized := fun profile dimension =>
    if dimension then profile.2 = true else profile.1 = true
  generative := fun _ => True

def count (flag : Bool) : Nat := if flag then 1 else 0

def firstAppraisal (profile : Profile) : Nat := 2 * count profile.1 + count profile.2

def secondAppraisal (profile : Profile) : Nat := count profile.1 + 2 * count profile.2

def ScoreBetter (score : Profile → Nat) (first second : Profile) : Prop :=
  score first < score second

def tradeoffSituation : Situation Profile Profile where
  feasible := fun profile => profile = (true, false) ∨ profile = (false, true)
  realize := id

theorem both_appraisals_respect_all_extensions :
    ComparisonPrinciple profileInventory (ScoreBetter firstAppraisal) ∧
    ComparisonPrinciple profileInventory (ScoreBetter secondAppraisal) := by
  constructor <;> intro first second extension
  all_goals
    rcases first with ⟨firstA, firstB⟩
    rcases second with ⟨secondA, secondB⟩
    cases firstA <;> cases firstB <;> cases secondA <;> cases secondB <;>
      simp_all [GenerativeExtension, Extends, profileInventory, ScoreBetter,
        firstAppraisal, secondAppraisal, count, Bool.forall_bool]

theorem tradeoff_has_opposite_strict_appraisals :
    ScoreBetter firstAppraisal (false, true) (true, false) ∧
    ScoreBetter secondAppraisal (true, false) (false, true) := by
  simp [ScoreBetter, firstAppraisal, secondAppraisal, count]

theorem both_tradeoff_options_survive :
    Survives profileInventory tradeoffSituation (true, false) ∧
    Survives profileInventory tradeoffSituation (false, true) := by
  constructor
  · refine ⟨Or.inl rfl, ?_⟩
    intro second feasible
    rcases feasible with rfl | rfl
    · exact generative_extension_irreflexive _ _
    · intro extension
      have impossible := extension.1 false rfl
      cases impossible
  · refine ⟨Or.inr rfl, ?_⟩
    intro second feasible
    rcases feasible with rfl | rfl
    · intro extension
      have impossible := extension.1 true rfl
      cases impossible
    · exact generative_extension_irreflexive _ _

theorem each_appraisal_has_a_different_coherent_selection :
    SelectionCoherence tradeoffSituation (ScoreBetter firstAppraisal)
      (fun profile => profile = (true, false)) ∧
    SelectionCoherence tradeoffSituation (ScoreBetter secondAppraisal)
      (fun profile => profile = (false, true)) := by
  constructor
  · intro first selected
    subst first
    refine ⟨Or.inl rfl, ?_⟩
    intro second feasible
    rcases feasible with rfl | rfl <;>
      simp [ScoreBetter, firstAppraisal, count, tradeoffSituation]
  · intro first selected
    subst first
    refine ⟨Or.inr rfl, ?_⟩
    intro second feasible
    rcases feasible with rfl | rfl <;>
      simp [ScoreBetter, secondAppraisal, count, tradeoffSituation]

end GenerativeComparison
