import GenerativeOutcomeModel
import ReceiptRevisionBoundary

/-!
# Evidence scope and receipt revision in the existing generative model

This entry joins unknown-availability identification to the already implemented
paid predictor. The original event law supplies its own available-work and
phase conditions. Unknown-availability reasoning is not installed as a new
controller, and the separate stochastic outage implementation is not silently
identified with the deterministic paid-work process.
-/

namespace Generative.Model.Receipt

open PredictionAction

/-- A reported partial target is correct for every availability admitted by
the unchanged response relation. Abstention is a logical result, not a policy. -/
theorem partial_answer_matches_actual_receipt
    (action regime available target : Bool)
    (hanswer : ReceiptIdentification.partialDecode action
      (receiptOf action regime available) = some target) : target = regime :=
  (ReceiptIdentification.partial_decode_sound action _ target hanswer regime
    ⟨available, rfl⟩).symm

/-- The next event's kind and target freshness follow from the existing phase
law and actual edges. The theorem does not assert that a next event occurs;
an observed but unaffordable write may remain blocked. -/
theorem actual_next_step_uses_fresh_receipt
    {p : Parameters} {s observed written : State} {event : Event}
    (hwork : Step p s .work observed) (hnext : Step p observed event written) :
    event = .write ∧
      written.score = revisedScore s.physical.directed s.score s.physical.core.regime ∧
      written.physical.core.regime = s.physical.core.regime := by
  have hevent := ReceiptRevisionBoundary.enabled_after_work_must_be_write hwork hnext.1
  cases hevent
  have hfresh := ReceiptRevisionBoundary.available_work_write_update hwork hnext
  exact ⟨rfl, hfresh.1, hfresh.2.1⟩

end Generative.Model.Receipt

#print axioms Generative.Model.Receipt.partial_answer_matches_actual_receipt
#print axioms Generative.Model.Receipt.actual_next_step_uses_fresh_receipt
