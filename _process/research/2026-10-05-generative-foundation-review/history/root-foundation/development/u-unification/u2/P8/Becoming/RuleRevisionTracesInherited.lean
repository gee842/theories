import Becoming.RuleRevisionTraces

/-!
# The revising run never finishes, through the periphery's proofs

`OpenFutureRevision.revised_rules_can_fail_forever` states that every rule its revising sequence
executes finishes when retained and lowers its own remaining count, yet no outcome ever forms;
`revision_resets_remaining` states that each revision resets the remaining count from 1 to 2.
This module states both of the run `RuleRevisionTraces.revising` of the rule process.

* **Revised rules can fail for ever.** Along the revising run, the rule taken at every step, kept
  for two steps from the configuration there, reaches a formed outcome, and the step lowers that
  rule's remaining count; yet no configuration of the run is a formed outcome
  (`fails_forever`).
* **Each revision resets the remaining count**: after the step the rule just taken has 1
  remaining, and the rule taken next has 2 (`resets_remaining`).

This module inherits `propext` from `OpenFutureRevision.revised_rules_can_fail_forever` and
`OpenFutureRevision.revision_resets_remaining`, and adds no axiom of its own. No ethical predicate
or ranking occurs.
-/

namespace Becoming

namespace RuleRevisionTracesInherited

open Generative OpenFutureRevision RuleRevisionTraces

/-- **Revised rules can fail for ever along the revising run.** -/
theorem fails_forever :
    (∀ n, completed (advance (revising.act n) (advance (revising.act n) (revising.state n)))) ∧
    (∀ n, remaining (revising.act n) (revising.state (n + 1)) <
      remaining (revising.act n) (revising.state n)) ∧
    (∀ n, ¬ completed (revising.state n)) :=
  revised_rules_can_fail_forever

/-- **Each revision resets the remaining count along the revising run.** -/
theorem resets_remaining (n : Nat) :
    remaining (revising.act n) (revising.state (n + 1)) = 1 ∧
      remaining (revising.act (n + 1)) (revising.state (n + 1)) = 2 :=
  revision_resets_remaining n

end RuleRevisionTracesInherited

end Becoming
