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

end Generative.ConnectedModel

#print axioms Generative.ConnectedModel.permission_cut_step
#print axioms Generative.ConnectedModel.cut_excludes_trial_work
#print axioms Generative.ConnectedModel.cut_excludes_bank_work
#print axioms Generative.ConnectedModel.permission_cut_step_preserves_patient
#print axioms Generative.ConnectedModel.permission_cut_trace
#print axioms Generative.ConnectedModel.permission_cut_connected_accounts
