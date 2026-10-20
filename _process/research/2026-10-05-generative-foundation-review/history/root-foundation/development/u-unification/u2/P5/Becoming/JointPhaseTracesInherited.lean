import Becoming.JointPhaseTraces

/-!
# The phase and interaction steps of one joint configuration: the reduced summary

`RelationalReduction.every_finite_control_response_exact` states that a summary of the joint
configuration, holding the two masses, the local cross contribution and the cross contribution
the interaction will move into the control density, evolves by its own reduced law along every
finite word of interaction and phase steps, and gives the same response as the full joint
configuration. Its proof goes through `SystemsOrganization` and the periphery's commuting step,
proved with `simp`. Read on the traces of the process `Assurance.ofMap RelationalReduction.next`
(`JointPhaseTraces`):

* **The reduced summary gives the response at the end of every trace**: along every trace of the
  process, the response read from the summary evolved by the reduced law is the response of the
  configuration the trace ends at (`summary_response`).
* **The summary omits the register**: two configurations with one summary, `⟨⟨1, 0⟩, ⟨0, 0⟩⟩` and
  `⟨⟨0, 1⟩, ⟨0, 0⟩⟩`, keep one summary at the ends of their traces along every common word, yet
  their register densities differ (`summary_omits_register`). The summary is exact for this
  process and these responses, not for every reading of the configuration.

This module belongs to the periphery-join ring. No ethical predicate or ranking occurs. It
inherits `propext` from `RelationalReduction.every_finite_control_response_exact` and
`RelationalReduction.every_finite_word_exact` and adds no axiom of its own.
-/

namespace Becoming

open Generative

namespace JointPhaseTracesInherited

open Generative.OperativeCoherence Generative.RelationalReduction JointPhaseTraces

/-- **The reduced summary gives the response at the end of every trace of the process.** -/
theorem summary_response {v t : Joint} {word : List Event} (path : Trace process v word t) :
    response (decodeControl (SystemsOrganization.evolve reducedNext (summarize v) word)) =
      response (controlDensity t) :=
  (every_finite_control_response_exact v word).trans
    (congrArg (fun m => response (controlDensity m)) (trace_end path).symm)

/-- **The summary omits the register.** Two configurations with one summary keep one summary at the
ends of their traces along every common word, yet their register densities differ. -/
theorem summary_omits_register :
    registerDensity (⟨⟨1, 0⟩, ⟨0, 0⟩⟩ : Joint) ≠ registerDensity ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ ∧
    ∀ (word : List Event) (t t' : Joint), Trace process ⟨⟨1, 0⟩, ⟨0, 0⟩⟩ word t →
      Trace process ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ word t' → summarize t = summarize t' :=
  ⟨summary_omits_other_relations.2, fun word _ _ path path' =>
    (congrArg summarize (trace_end path)).trans
      ((every_finite_word_exact _ word).trans
        ((congrArg (fun q => SystemsOrganization.evolve reducedNext q word)
            summary_omits_other_relations.1).trans
          ((every_finite_word_exact _ word).symm.trans
            (congrArg summarize (trace_end path')).symm)))⟩

end JointPhaseTracesInherited

end Becoming
