import ConnectedGenerativeModel
import CompletionApplicability
import ClaimLedger

/-!
# Actual acquisition, selective certification and the unchanged assessment

This entry connects the existing root trace, actual acquired successor and
addressed-claim ledger. The ledger is verification state, not an installed
completion sensor, memory cell or controller. Episode binding, service meaning,
admission and old certificate soundness remain explicit inputs. No physical law
is changed and no missing runtime revision is supplied by defining a certificate.
-/

namespace Generative.Applicability

universe u v w

/-- Both existing trace interfaces describe exactly the same primitive events
and actual intermediate states when instantiated with the same process law. -/
theorem ledger_trace_iff {State : Type u} {Action : Type v}
    (P : Process State Action) (s t : State) (events : List Action) :
    ClaimLedger.Trace P.step s events t ↔ Trace P s events t := by
  constructor
  · intro history
    induction history with
    | nil s => exact .nil s
    | cons step _ ih => exact .cons step ih
  · intro history
    induction history with
    | nil s => exact .nil s
    | cons step _ ih => exact .cons step ih

/-- Proof-level certification of one addressed claim. Its truth is obtained
from the actual source history below; this definition creates no physical event. -/
def recordCompletion {Claim : Type w} (ledger : ClaimLedger.Ledger Claim)
    (Met : Claim → Prop) (completed : Claim) : ClaimLedger.Ledger Claim :=
  ClaimLedger.record ledger (fun claim => claim = completed ∧ Met completed)

/-- Actual acquired evidence can discharge one interpreted claim in the logical
ledger while the same physical learner retains its old help assessment through
every admitted finite continuation.
Other claims retain their ledger status, not necessarily ontic unmet need.
Old certificates require soundness at this same assessment horizon. -/
theorem actual_certificate_and_fixed_assessment
    {Claim : Type w} (ledger : ClaimLedger.Ledger Claim) (Met : Claim → Prop)
    (completed : Claim)
    {InEpisode : List PublicationBridge.ArchiveEvent → RecipientAction.Archive →
      RecipientArchive.World → Prop}
    (bound : ApplicationEvidence.EpisodeBound ApplicationEvidence.actualEntrance InEpisode)
    (meaning : ApplicationEvidence.ServiceMeaning InEpisode (Met completed))
    (admitted : ledger.admitted completed)
    (oldSound : ∀ claim, ledger.certified claim → Met claim) :
    let updated := recordCompletion ledger Met completed
    ClaimLedger.Trace (EvaluativeSuccession.process SuccessionWitness.changed).step
      SuccessionWitness.entry SuccessionWitness.prefixWord SuccessionWitness.consumed ∧
    Met completed ∧ updated.admitted = ledger.admitted ∧ updated.certified completed ∧
    (∀ claim, updated.certified claim → Met claim) ∧
    ¬ ClaimLedger.unresolved updated completed ∧
    (∀ other, other ≠ completed →
      (ClaimLedger.unresolved updated other ↔ ClaimLedger.unresolved ledger other)) ∧
    SuccessionWitness.consumed.core.hardware.q = 2 ∧
    SuccessionWitness.consumed.native.n = 7 ∧
    (∀ events endpoint,
      Trace (EvaluativeSuccession.process SuccessionWitness.changed)
        SuccessionWitness.consumed events endpoint → EvaluativeSuccession.help endpoint = true) := by
  have met : Met completed :=
    ApplicationEvidence.current_command_implies_interpreted_service_met
      ApplicationEvidence.actualEntrance bound meaning
  have certified : (recordCompletion ledger Met completed).certified completed :=
    Or.inr ⟨admitted, rfl, met⟩
  have factual := CompletionApplicability.Actual.actual_history_keeps_completed_query_and_recommends
  refine ⟨(ledger_trace_iff _ _ _ _).mpr SuccessionWitness.prefix_trace,
    met, rfl, certified, ?_, ?_, ?_, factual.2.2.2.2.1, factual.2.2.2.2.2, ?_⟩
  · apply ClaimLedger.recorded_certificates_sound ledger _ Met oldSound
    intro claim _ evidence
    exact evidence.1.symm ▸ evidence.2
  · intro pending
    exact pending.2 certified
  · intro other different
    exact ClaimLedger.no_new_certificate_preserves_unresolved ledger _ other
      (fun evidence => different evidence.1)
  · intro events endpoint continuation
    exact CompletionApplicability.Actual.all_reached_states_recommend
      (trace_append_iff.mpr ⟨SuccessionWitness.consumed,
        SuccessionWitness.prefix_trace, continuation⟩)

/-- The root outcome semantics observes the same invariant across all finite
continuations from the actual evidence-bearing endpoint. It grants no new sensor. -/
theorem actual_acquired_outcome_keeps_assessment
    (events : List EvaluativeSuccession.Event) (value : Bool)
    (outcome : OutcomeContinuation.OutcomeResidual
      (EvaluativeSuccession.process SuccessionWitness.changed)
      SuccessionWitness.consumed EvaluativeSuccession.help [] events value) :
    value = true := by
  rcases outcome with ⟨endpoint, history, observed⟩
  have reached : Trace (EvaluativeSuccession.process SuccessionWitness.changed)
      SuccessionWitness.entry (SuccessionWitness.prefixWord ++ events) endpoint :=
    trace_append_iff.mpr ⟨SuccessionWitness.consumed, SuccessionWitness.prefix_trace, history⟩
  exact observed.symm.trans (CompletionApplicability.Actual.all_reached_states_recommend reached)

end Generative.Applicability

#print axioms Generative.Applicability.ledger_trace_iff
#print axioms Generative.Applicability.recordCompletion
#print axioms Generative.Applicability.actual_certificate_and_fixed_assessment
#print axioms Generative.Applicability.actual_acquired_outcome_keeps_assessment
