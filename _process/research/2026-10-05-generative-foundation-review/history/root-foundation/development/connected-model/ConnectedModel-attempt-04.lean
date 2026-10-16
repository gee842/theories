import ApplicationEvidence

/-!
# Current authority through an actual learned successor history

These results analyze the existing EvaluativeSuccession law without changing
its state, event repertoire, decoder, controller, costs, or permission rules.
The cut concerns its technical permission bit, not the legitimacy of authority.
Patient credit is this law's resource transfer, not a definition of welfare.
All continuations are finite actual traces. No completion guarantee follows.
-/

namespace Generative.ConnectedModel

open EvaluativeSuccession
set_option maxRecDepth 32768
set_option maxHeartbeats 8000000

/-- A cut survives every admitted event, including copying and archive work. -/
theorem permission_cut_step {laws : RecipientCorrection.Laws}
    {s t : State} {e : Event} (h : Step laws s e t)
    (cut : s.permission = false) : t.permission = false := by
  rcases h with ⟨he, rfl⟩
  cases e with
  | copyWrite q sc pm dl => change (s.permission && pm) = false; rw [cut]; rfl
  | bank e => cases e with
    | bind i hd | write => exact cut
    | core e w => cases e with
      | contextChange c => exact cut
      | core e => cases e <;> exact cut
  | attempt => simp only [advance]; split <;> exact cut
  | permission v => exact he
  | _ => exact cut

/-- A current grant is needed for work, including fresh inquiry work. -/
theorem cut_excludes_trial_work {laws : RecipientCorrection.Laws}
    {s : State} (cut : s.permission = false) (available : Bool) :
    ¬ EvaluativeSuccession.Enabled laws s (.trial (.work available)) := by
  intro h
  rcases h.2.2.2.1 with settlement | authorized
  · exact settlement
  · have grant := authorized.2.2.1
    rw [cut] at grant
    cases grant

theorem cut_excludes_bank_work {laws : RecipientCorrection.Laws}
    {s : State} (cut : s.permission = false) (available : Bool)
    (successor : RecipientArchive.World) :
    ¬ EvaluativeSuccession.Enabled laws s (.bank (.core (.core (.work available)) successor)) := by
  intro h
  rcases h.2.2.2.1.2.2.1 with settlement | authorized
  · exact settlement
  · have grant := authorized.2.1
    rw [cut] at grant
    cases grant

/-- The two productive event sites are both excluded; settlement adds no credit. -/
theorem permission_cut_step_preserves_patient {laws : RecipientCorrection.Laws}
    {s t : State} {e : Event} (h : Step laws s e t)
    (cut : s.permission = false) : t.core.patient = s.core.patient := by
  rcases h with ⟨he, rfl⟩
  cases e with
  | trial e =>
    cases e with
    | work av => exact False.elim (cut_excludes_trial_work cut av he)
    | _ => rfl
  | bank e =>
    cases e with
    | bind i hd => rfl
    | write =>
      exact congrArg (fun w : RecipientArchive.World => w.core.patient)
        (EmissionArchive.write_preserves_world (producer laws) (archive s))
    | core e w =>
      cases e with
      | contextChange c => exact False.elim he.2.2.2.1
      | core e =>
        have hw : RecipientArchive.Step laws (archive s).world (.core e) w := he.2.2.2.2.1
        rcases hw with ⟨_, rfl⟩
        cases e with
        | work av => exact False.elim (cut_excludes_bank_work cut av _ he)
        | _ => rfl
  | attempt => simp only [advance]; split <;> rfl
  | _ => rfl

/-- Arbitrarily long admitted continuations cannot restore the cut or add a
recipient transfer. Neither stale learned knowledge nor a pending port bypasses it. -/
theorem permission_cut_trace {laws : RecipientCorrection.Laws}
    {s t : State} {events : List Event}
    (history : Trace (process laws) s events t) (cut : s.permission = false) :
    t.permission = false ∧ t.core.patient = s.core.patient := by
  induction history with
  | nil => exact ⟨cut, rfl⟩
  | cons hs _ ih =>
    have next := ih (permission_cut_step hs cut)
    exact ⟨next.1, next.2.trans (permission_cut_step_preserves_patient hs cut)⟩

/-- Both retained acquisition and all existing material/account laws survive
the same cut continuation; resources are not reconstructed at the interface. -/
theorem permission_cut_connected_accounts {laws : RecipientCorrection.Laws}
    {s t : State} {events : List Event}
    (history : Trace (process laws) s events t) (cut : s.permission = false) :
    t.permission = false ∧ t.core.patient = s.core.patient ∧
    t.native = s.native ∧ t.history = s.history ∧
    energy t + spent laws s events = energy s ∧ material t = material s := by
  have hcut := permission_cut_trace history cut
  have retained := trace_retains_native_and_history history
  exact ⟨hcut.1, hcut.2, retained.1, retained.2,
    trace_energy history, trace_material history⟩

namespace Actual

open SuccessionWitness

/-- These are prefixes of the accepted actual selected trial, not new states. -/
def beforeWorkWord : List Event :=
  [.trial .rent, .trial (.sense .recipient), .trial .reserve]
def beforeWork := run changed acting beforeWorkWord
def afterWork := advance changed beforeWork (.trial (.work true))
def cutBeforeWork := advance changed beforeWork (.permission false)
def cutAfterWork := advance changed afterWork (.permission false)
def settleWord : List Event := [.trial (.acquire true), .trial .write]
def settled := run changed cutAfterWork settleWord

theorem actual_prefix_to_work :
    Trace (process changed) entry
      (prefixWord ++ choiceWord ++ [.attempt] ++ beforeWorkWord) beforeWork := by
  have hc := trace_append_iff.mpr
    ⟨consumed, prefix_trace, runnable_trace acquired_assessment.1⟩
  have ha := trace_append_iff.mpr
    ⟨chosen, hc, trace_singleton_iff.mpr ⟨actual_selected_action.1, rfl⟩⟩
  exact trace_append_iff.mpr
    ⟨acting, ha, runnable_trace (show Runnable changed acting beforeWorkWord from by decide)⟩

theorem reached_work_is_informed_and_affordable :
    Known beforeWork ∧ beforeWork.native.n = 7 ∧
    beforeWork.core.hardware.q = 2 ∧ beforeWork.reader = consumed.reader ∧
    beforeWork.core.patient = 70 ∧ beforeWork.core.hardware.fuel = 3 ∧
    beforeWork.core.escrow = 3 ∧ beforeWork.core.packets = 1 ∧
    EvaluativeSuccession.Enabled changed beforeWork (.trial (.work true)) := by
  exact ⟨by decide, by decide, by decide, rfl, by decide, by decide,
    by decide, by decide, by decide⟩

/-- The actual cut removes neither the acquired data nor the means to perform work. -/
theorem actual_cut_before_work :
    Trace (process changed) beforeWork [.permission false] cutBeforeWork ∧
    Known cutBeforeWork ∧ cutBeforeWork.core = beforeWork.core ∧
    cutBeforeWork.reader = beforeWork.reader ∧ cutBeforeWork.native = beforeWork.native ∧
    cutBeforeWork.permission = false ∧
    ¬ EvaluativeSuccession.Enabled changed cutBeforeWork (.trial (.work true)) := by
  exact ⟨trace_singleton_iff.mpr ⟨rfl, rfl⟩, by decide, rfl, rfl, rfl, rfl,
    cut_excludes_trial_work rfl true⟩

/-- The same learned predecessor actually performs the productive event before
the second cut. No later revocation retrospectively erases that transfer. -/
theorem actual_work_then_cut :
    Trace (process changed) beforeWork [.trial (.work true), .permission false] cutAfterWork ∧
    cutAfterWork.core.patient = beforeWork.core.patient + 10 ∧
    cutAfterWork.core.escrow = 3 ∧ cutAfterWork.core.hardware.fuel = 0 ∧
    cutAfterWork.permission = false ∧ cutAfterWork.native = beforeWork.native := by
  exact ⟨.cons ⟨reached_work_is_informed_and_affordable.2.2.2.2.2.2.2.2, rfl⟩
      (.cons ⟨rfl, rfl⟩ (.nil _)), by decide, by decide, by decide, rfl, rfl⟩

/-- Prior escrow pays for acquisition and writing after the cut. Its original
record, permission and balance are continued; no new patient transfer occurs. -/
theorem actual_paid_settlement_after_cut :
    Trace (process changed) cutAfterWork settleWord settled ∧
    spent changed cutAfterWork settleWord = 3 ∧
    energy cutAfterWork = 89 ∧ energy settled = 86 ∧
    settled.core.patient = 80 ∧ settled.core.escrow = 0 ∧
    settled.core.hardware.q = 2 ∧ settled.native.n = 7 ∧
    settled.permission = false ∧ settled.port = .consumed ∧ settled.closed = true := by
  exact ⟨runnable_trace (show Runnable changed cutAfterWork settleWord from by decide),
    by decide, by decide, by decide, by decide, by decide, by decide, by decide,
    rfl, by decide, by decide⟩

theorem actual_joined_cut_settlement :
    Trace (process changed) entry
      ((prefixWord ++ choiceWord ++ [.attempt] ++ beforeWorkWord) ++
        [.trial (.work true), .permission false] ++ settleWord) settled ∧
    settled.native = entry.native ∧ settled.history = entry.history ∧
    energy settled + spent changed entry
      ((prefixWord ++ choiceWord ++ [.attempt] ++ beforeWorkWord) ++
        [.trial (.work true), .permission false] ++ settleWord) = energy entry ∧
    material settled = material entry := by
  have work := trace_append_iff.mpr ⟨beforeWork, actual_prefix_to_work, actual_work_then_cut.1⟩
  have complete := trace_append_iff.mpr ⟨cutAfterWork, work, actual_paid_settlement_after_cut.1⟩
  have retained := trace_retains_native_and_history complete
  exact ⟨complete, retained.1, retained.2, trace_energy complete, trace_material complete⟩

/-- All later admitted histories, not just the displayed settlement, preserve
the already accrued credit and the permission cut. -/
theorem actual_cut_all_continuations {t : State} {events : List Event}
    (history : Trace (process changed) cutAfterWork events t) :
    t.permission = false ∧ t.core.patient = 80 := by
  have h := permission_cut_trace history rfl
  exact ⟨h.1, h.2.trans (show cutAfterWork.core.patient = 80 from by decide)⟩

/-- Under the supplied one-service meaning, the original selector repeats work
after that service is already met. Its factual decoder and n remain operative.
This is a retained obstruction, not a newly installed withdrawal controller. -/
theorem interpreted_fulfillment_does_not_change_existing_selector
    {InEpisode : List PublicationBridge.ArchiveEvent → RecipientAction.Archive →
      RecipientArchive.World → Prop} {Met : Prop}
    (bound : ApplicationEvidence.EpisodeBound ApplicationEvidence.actualEntrance InEpisode)
    (meaning : ApplicationEvidence.ServiceMeaning InEpisode Met) :
    Met ∧ Trace (process changed) entry whole final ∧
    consumed.core.patient = firstEnd.core.patient + 10 ∧
    final.core.patient = consumed.core.patient + 10 ∧
    final.native.n = consumed.native.n := by
  exact ⟨ApplicationEvidence.current_command_implies_interpreted_service_met
      ApplicationEvidence.actualEntrance bound meaning,
    whole_actual_trace, by decide, by decide, rfl⟩

end Actual

end Generative.ConnectedModel

#print axioms Generative.ConnectedModel.permission_cut_step
#print axioms Generative.ConnectedModel.cut_excludes_trial_work
#print axioms Generative.ConnectedModel.cut_excludes_bank_work
#print axioms Generative.ConnectedModel.permission_cut_step_preserves_patient
#print axioms Generative.ConnectedModel.permission_cut_trace
#print axioms Generative.ConnectedModel.permission_cut_connected_accounts
#print axioms Generative.ConnectedModel.Actual.actual_prefix_to_work
#print axioms Generative.ConnectedModel.Actual.reached_work_is_informed_and_affordable
#print axioms Generative.ConnectedModel.Actual.actual_cut_before_work
#print axioms Generative.ConnectedModel.Actual.actual_work_then_cut
#print axioms Generative.ConnectedModel.Actual.actual_paid_settlement_after_cut
#print axioms Generative.ConnectedModel.Actual.actual_joined_cut_settlement
#print axioms Generative.ConnectedModel.Actual.actual_cut_all_continuations
#print axioms Generative.ConnectedModel.Actual.interpreted_fulfillment_does_not_change_existing_selector
