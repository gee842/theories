import Init

/-!
# Actual witnesses and deductive necessity

This is an inference audit, not a model of the generative whole. `Case` and
`admits` describe an explicitly supplied range of comparisons. They assert
neither separate worlds nor a physical transition law. In particular, a return
edge below is modal accessibility, not an operation undoing physical history.

The equivalences quantify over ALL predicates on that range. Their converses
use equality with the starting case. They therefore characterize a uniform
inference policy, not a necessary condition on any one substantive claim.
No actual interpretation, modal frame property or generative law is postulated.
-/

namespace Generative.DeductiveNecessity

universe u

def Possible {Case : Type u} (admits : Case → Case → Prop)
    (claim : Case → Prop) (atCase : Case) : Prop :=
  ∃ witness, admits atCase witness ∧ claim witness

def Necessary {Case : Type u} (admits : Case → Case → Prop)
    (claim : Case → Prop) (atCase : Case) : Prop :=
  ∀ alternative, admits atCase alternative → claim alternative

theorem actual_gives_possible {Case : Type u} (admits : Case → Case → Prop)
    (claim : Case → Prop) (actual : Case)
    (selfAdmitted : admits actual actual) (holds : claim actual) :
    Possible admits claim actual :=
  ⟨actual, selfAdmitted, holds⟩

/-- Positive transfer: a single actual witness remains a possible witness at
every admitted alternative when each alternative admits that starting case. -/
theorem return_gives_necessary_possibility {Case : Type u}
    (admits : Case → Case → Prop) (claim : Case → Prop) (actual : Case)
    (returns : ∀ alternative, admits actual alternative → admits alternative actual)
    (holds : claim actual) : Necessary admits (Possible admits claim) actual :=
  fun alternative h => ⟨actual, returns alternative h, holds⟩

/-- Exact condition for the UNIFORM actual-to-necessarily-possible rule.
No symmetry law is assumed; the needed local return property is recovered. -/
theorem uniform_possibility_transfer_iff_return {Case : Type u}
    (admits : Case → Case → Prop) (actual : Case) :
    (∀ claim : Case → Prop,
      claim actual → Necessary admits (Possible admits claim) actual) ↔
      (∀ alternative, admits actual alternative → admits alternative actual) := by
  constructor
  · intro transfer alternative accessible
    obtain ⟨witness, step, same⟩ :=
      transfer (fun candidate => candidate = actual) rfl alternative accessible
    cases same
    exact step
  · intro returns claim holds
    exact return_gives_necessary_possibility admits claim actual returns holds

/-- Promoting every actual truth directly to necessity is stronger still.
With all predicates available, every admitted case must be the actual case. -/
theorem uniform_truth_transfer_iff_single_case {Case : Type u}
    (admits : Case → Case → Prop) (actual : Case) :
    (∀ claim : Case → Prop, claim actual → Necessary admits claim actual) ↔
      (∀ alternative, admits actual alternative → alternative = actual) := by
  constructor
  · intro transfer alternative accessible
    exact transfer (fun candidate => candidate = actual) rfl alternative accessible
  · intro same claim holds alternative accessible
    cases same alternative accessible
    exact holds

/-- A general separation witness for the proposed inference. It preserves the
actual claim and its present possibility; it is not a rival account of reality.
The supplied missing return is precisely the failed comparison condition. -/
theorem one_way_comparison_separates {Case : Type u}
    (admits : Case → Case → Prop) (actual alternative : Case)
    (selfAdmitted : admits actual actual) (accessible : admits actual alternative)
    (noReturn : ¬ admits alternative actual) :
    Possible admits (fun candidate => candidate = actual) actual ∧
      ¬ Necessary admits
        (Possible admits (fun candidate => candidate = actual)) actual := by
  constructor
  · exact actual_gives_possible admits _ actual selfAdmitted rfl
  · intro necessary
    obtain ⟨witness, step, same⟩ := necessary alternative accessible
    cases same
    exact noReturn step

end Generative.DeductiveNecessity

#print axioms Generative.DeductiveNecessity.Possible
#print axioms Generative.DeductiveNecessity.Necessary
#print axioms Generative.DeductiveNecessity.actual_gives_possible
#print axioms Generative.DeductiveNecessity.return_gives_necessary_possibility
#print axioms Generative.DeductiveNecessity.uniform_possibility_transfer_iff_return
#print axioms Generative.DeductiveNecessity.uniform_truth_transfer_iff_single_case
#print axioms Generative.DeductiveNecessity.one_way_comparison_separates
