import JointContinuationClassification
import GenerativeComparison

/-!
# Joint continuation and the information required by a strict comparison

This module composes two existing results rather than introducing a new ethical
axiom. Both descriptions concern the same initial configuration and event law in
`JointContinuationClassification`. Retaining or releasing its coupling changes
which realizations can occur together. Positions are differentiated within that
law, not independent owners supplied before their relations.

`jointInventory` records POSSIBLE joint realization, not actual realization.
Only the bundle including both represented claims is marked generative here.
The normative use of C therefore requires an EXPLICIT application premise:
this joint living possibility is positively significant, and all relevant
realized effects, costs and losses are covered by the comparison. This is not
proved by the event law, G0 alone, or the `generative` field. The small inventory
by itself does not certify that no ethically relevant loss has been omitted.

The new composition proves that, under this disclosed C application, no strict
comparison factoring through identical marginal descriptions can be adequate.
The full joint-bundle description distinguishes the case. Existence of that
richer possibility still does not force an actual history to realize it.

No practical obligation, preservation of every relation, independent value
ownership, general model of consciousness, or behavioral convergence is derived.
-/

namespace RelationalGrounding

open JointContinuationClassification
open GenerativeComparison

inductive Regime where
  | released | retained
  deriving DecidableEq

def continuations : Regime → Continuations History Claim
  | .released => released
  | .retained => retained

def marginal (regime : Regime) (claim : Claim) : Prop :=
  ∃ history, (continuations regime).feasible history ∧
    (continuations regime).realized history claim

def allBundle (_ : Claim) : Prop := True

def jointInventory : Inventory Regime (Claim → Prop) where
  realized := fun regime bundle => Jointly (continuations regime) bundle
  generative := fun bundle => ∀ claim, bundle claim

/-- Every released joint profile is realizable under the retained event law.
The proof uses the existing together history as one common witness, not a
different history for each marginal claim. -/
theorem released_profiles_are_carried :
    CarriesWholeProfiles released retained := by
  obtain ⟨history, feasible, joint⟩ :=
    same_marginal_realizations_can_lose_a_joint_bundle.2.1
  intro old _
  exact ⟨history, feasible, fun claim _ => joint claim True.intro⟩

/-- Producer-to-consumer adapter: whole-profile preservation supplies C's
represented no-loss input; the existing lost joint bundle supplies strictness. -/
theorem joint_bundle_extension :
    GenerativeExtension jointInventory Regime.released Regime.retained := by
  refine ⟨?_, allBundle, fun _ => True.intro, ?_, ?_⟩
  · exact (whole_profile_preservation_iff_joint_bundle_preservation
      released retained).mp released_profiles_are_carried
  · exact same_marginal_realizations_can_lose_a_joint_bundle.2.1
  · exact same_marginal_realizations_can_lose_a_joint_bundle.2.2

/-- The retained and released descriptions agree on every marginal possibility,
while the full represented joint-bundle description separates them. -/
theorem marginals_agree_but_joint_descriptions_differ :
    (∀ claim, marginal Regime.released claim ↔ marginal Regime.retained claim) ∧
    jointInventory.realized Regime.retained allBundle ∧
      ¬ jointInventory.realized Regime.released allBundle := by
  refine ⟨?_, same_marginal_realizations_can_lose_a_joint_bundle.2.1, ?_⟩
  · intro claim
    exact (same_marginal_realizations_can_lose_a_joint_bundle.1 claim).symm
  · exact same_marginal_realizations_can_lose_a_joint_bundle.2.2

/-- A summary can have any type. If identical marginals force identical summaries,
an irreflexive comparison on those summaries cannot satisfy this C application.
This is an information obstruction conditional on C, not a proof of C's warrant.
-/
theorem strict_comparison_cannot_factor_through_marginals
    {Summary : Type} (summary : Regime → Summary)
    (marginalDetermines : ∀ a b,
      (∀ claim, marginal a claim ↔ marginal b claim) → summary a = summary b)
    (compare : Summary → Summary → Prop)
    (irreflexive : ∀ s, ¬ compare s s) :
    ¬ ComparisonPrinciple jointInventory
      (fun a b => compare (summary a) (summary b)) := by
  intro comparison
  have strict := comparison _ _ joint_bundle_extension
  have same := marginalDetermines Regime.released Regime.retained
    marginals_agree_but_joint_descriptions_differ.1
  rw [same] at strict
  exact irreflexive _ strict

/-- Enriching the description with actual joint possibility repairs this specific
information obstruction: the full bundle already distinguishes the two regimes.
It does not certify full real-world descriptive or ethical adequacy. -/
theorem joint_description_separates :
    (fun bundle => jointInventory.realized Regime.released bundle) ≠
      (fun bundle => jointInventory.realized Regime.retained bundle) := by
  intro same
  have atBundle := congrFun same allBundle
  exact marginals_agree_but_joint_descriptions_differ.2.2
    (Eq.mp atBundle.symm marginals_agree_but_joint_descriptions_differ.2.1)

def retainedLeft : History :=
  ⟨.retain, .coupled, .activateLeft, .leftActive⟩

/-- The very same retained law has a complete admissible history realizing only
the left claim. Preserving a richer possibility is not behavioral convergence. -/
theorem retained_possibility_does_not_force_joint_actualization :
    retained.feasible retainedLeft ∧
    retained.realized retainedLeft Claim.leftRealized ∧
    ¬ retained.realized retainedLeft Claim.rightRealized ∧
    jointInventory.realized Regime.retained allBundle := by
  refine ⟨⟨⟨.retainCoupling, .activateLeftCoupled⟩, rfl⟩, Or.inl rfl, ?_, ?_⟩
  · rintro (impossible | impossible) <;> cases impossible
  · exact marginals_agree_but_joint_descriptions_differ.2.1

end RelationalGrounding
