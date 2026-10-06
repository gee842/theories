import SuccessionWitness

/-!
Operational abstraction of the dormant Historical field under the unchanged law.
The field is unread even before retirement; the actual application below starts
after handoff. Arbitrary substituted snapshots need not share reachable ancestry.
This is not physical erasure, disappearance of the donor, or normative equivalence.
Live carriers, native influence, access, custody and support remain unchanged.
The result concerns the declared event law and available finite continuations;
an external scheduler newly permitted to read history is outside this interface.
-/
namespace SuccessionHistoryInterface
open EvaluativeSuccession

def withHistory (s : State) (h : Historical) : State := {s with history := h}

theorem withHistory_self (s : State) : withHistory s s.history = s := by cases s; rfl

theorem withHistory_overwrite (s : State) (h k : Historical) :
    withHistory (withHistory s h) k = withHistory s k := rfl

theorem live_data (s : State) (h : Historical) :
    (withHistory s h).core = s.core ∧ (withHistory s h).reader = s.reader ∧
    (withHistory s h).bank = s.bank ∧ (withHistory s h).native = s.native ∧
    (withHistory s h).commonCustody = s.commonCustody ∧
    (withHistory s h).sourceCustody = s.sourceCustody ∧
    (withHistory s h).nAccess = s.nAccess := ⟨rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem archive_withHistory (s : State) (h : Historical) :
    archive (withHistory s h) = archive s := rfl

theorem current_withHistory (s : State) (h : Historical) :
    Current (withHistory s h) ↔ Current s := Iff.rfl

theorem command_withHistory (s : State) (h : Historical) :
    command (withHistory s h) = command s := rfl

theorem known_withHistory (s : State) (h : Historical) :
    Known (withHistory s h) ↔ Known s := Iff.rfl

theorem help_withHistory (s : State) (h : Historical) :
    help (withHistory s h) = help s := rfl

theorem energy_withHistory (s : State) (h : Historical) :
    energy (withHistory s h) = energy s := rfl

theorem material_withHistory (s : State) (h : Historical) :
    material (withHistory s h) = material s := rfl

theorem enabled_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (e : Event) :
    Enabled laws (withHistory s h) e ↔ Enabled laws s e := by cases e <;> rfl

theorem advance_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (e : Event) :
    advance laws (withHistory s h) e = withHistory (advance laws s e) h := by
  cases e <;> try rfl
  case bank e => cases e with
    | bind i hd => rfl
    | write => rfl
    | core e w => cases e with
      | contextChange c => rfl
      | core e => cases e <;> rfl
  case attempt =>
    have he : (Known (withHistory s h) ∧ gates (withHistory s h) ∧
        (withHistory s h).core.phase = .ready ∧ 0 < (withHistory s h).core.packets) =
        (Known s ∧ gates s ∧ s.core.phase = .ready ∧ 0 < s.core.packets) := rfl
    simp only [advance,he]
    by_cases hc : Known s ∧ gates s ∧ s.core.phase = .ready ∧ 0 < s.core.packets
    · simp only [if_pos hc]; rfl
    · simp only [if_neg hc]; rfl

theorem charge_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (e : Event) :
    charge laws (withHistory s h) e = charge laws s e := by cases e <;> rfl

theorem run_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (es : List Event) :
    run laws (withHistory s h) es = withHistory (run laws s es) h := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
      simp only [run]
      rw [advance_withHistory]
      exact ih _

theorem runnable_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (es : List Event) :
    Runnable laws (withHistory s h) es ↔ Runnable laws s es := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
      simp only [Runnable,enabled_withHistory,advance_withHistory,ih]

theorem spent_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (es : List Event) :
    spent laws (withHistory s h) es = spent laws s es := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
      simp only [spent,charge_withHistory,advance_withHistory,ih]

theorem trace_withHistory {laws : RecipientCorrection.Laws} {s t : State}
    {es : List Event} (ht : Generative.Trace (process laws) s es t) (h : Historical) :
    Generative.Trace (process laws) (withHistory s h) es (withHistory t h) := by
  induction ht with
  | nil => exact .nil _
  | @cons s t u e es he ht ih =>
      apply Generative.Trace.cons (m := withHistory t h)
      · exact ⟨(enabled_withHistory laws s h e).mpr he.1,
          (congrArg (fun x => withHistory x h) he.2).trans
            (advance_withHistory laws s h e).symm⟩
      · exact ih

/-- Same admissible finite words, expenditure, and live outcome; no ancestry claim. -/
theorem continuation_interface (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (es : List Event) :
    (Runnable laws (withHistory s h) es ↔ Runnable laws s es) ∧
    spent laws (withHistory s h) es = spent laws s es ∧
    (run laws (withHistory s h) es).core = (run laws s es).core ∧
    (run laws (withHistory s h) es).reader = (run laws s es).reader ∧
    (run laws (withHistory s h) es).native = (run laws s es).native := by
  refine ⟨runnable_withHistory laws s h es,spent_withHistory laws s h es,?_,?_,?_⟩
  all_goals rw [run_withHistory]; rfl

/-- The existing state-dependent event generator also reads only retained live data. -/
theorem toOld_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (c : SuccessionWitness.Command) :
    SuccessionWitness.toOld laws (withHistory s h) c =
      SuccessionWitness.toOld laws s c := by cases c <;> rfl

theorem bankWord_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (cs : List SuccessionWitness.Command) :
    SuccessionWitness.bankWord laws (withHistory s h) cs =
      SuccessionWitness.bankWord laws s cs := by
  induction cs generalizing s with
  | nil => rfl
  | cons c cs ih =>
      simp only [SuccessionWitness.bankWord,toOld_withHistory,advance_withHistory,ih]

theorem runBank_withHistory (laws : RecipientCorrection.Laws) (s : State)
    (h : Historical) (cs : List SuccessionWitness.Command) :
    SuccessionWitness.runBank laws (withHistory s h) cs =
      withHistory (SuccessionWitness.runBank laws s cs) h := by
  induction cs generalizing s with
  | nil => rfl
  | cons c cs ih =>
      simp only [SuccessionWitness.runBank,toOld_withHistory,advance_withHistory,ih]

theorem actual_suffix_withHistory (h : Historical) :
    Generative.Trace (process SuccessionWitness.changed)
      (withHistory SuccessionWitness.consumed h) SuccessionWitness.suffix
      (withHistory SuccessionWitness.final h) :=
  trace_withHistory SuccessionWitness.suffix_trace h

theorem actual_suffix_accounting (h : Historical) :
    spent SuccessionWitness.changed (withHistory SuccessionWitness.consumed h)
      SuccessionWitness.suffix = 10 ∧
    energy (withHistory SuccessionWitness.consumed h) = 96 ∧
    energy (withHistory SuccessionWitness.final h) = 86 ∧
    material (withHistory SuccessionWitness.final h) = 78 := by
  have he := trace_energy SuccessionWitness.suffix_trace
  rcases SuccessionWitness.actual_new_publication with ⟨_,_,_,_,_,_,_,_,hi⟩
  rcases SuccessionWitness.actual_selected_action with ⟨_,_,_,_,_,_,_,_,_,_,_,hf,hm⟩
  simp only [spent_withHistory,energy_withHistory,material_withHistory]
  rw [hf,hi] at he
  exact ⟨Nat.add_left_cancel he,hi,hf,hm⟩

theorem actual_suffix_live_outcome (h : Historical) :
    (run SuccessionWitness.changed (withHistory SuccessionWitness.consumed h)
      SuccessionWitness.suffix).core.patient = 80 ∧
    (run SuccessionWitness.changed (withHistory SuccessionWitness.consumed h)
      SuccessionWitness.suffix).core.hardware.q = 2 ∧
    (run SuccessionWitness.changed (withHistory SuccessionWitness.consumed h)
      SuccessionWitness.suffix).native.n = 7 ∧
    (run SuccessionWitness.changed (withHistory SuccessionWitness.consumed h)
      SuccessionWitness.suffix).port = .consumed := by
  rw [run_withHistory,trace_run SuccessionWitness.suffix_trace]
  dsimp only [withHistory]
  rcases SuccessionWitness.actual_selected_action with ⟨_,_,hq,_,_,_,hp,hn,_,hport,_,_,_⟩
  exact ⟨hp,hq,hn,hport⟩

end SuccessionHistoryInterface

#print axioms SuccessionHistoryInterface.withHistory_self
#print axioms SuccessionHistoryInterface.withHistory_overwrite
#print axioms SuccessionHistoryInterface.live_data
#print axioms SuccessionHistoryInterface.archive_withHistory
#print axioms SuccessionHistoryInterface.current_withHistory
#print axioms SuccessionHistoryInterface.command_withHistory
#print axioms SuccessionHistoryInterface.known_withHistory
#print axioms SuccessionHistoryInterface.help_withHistory
#print axioms SuccessionHistoryInterface.energy_withHistory
#print axioms SuccessionHistoryInterface.material_withHistory
#print axioms SuccessionHistoryInterface.enabled_withHistory
#print axioms SuccessionHistoryInterface.advance_withHistory
#print axioms SuccessionHistoryInterface.charge_withHistory
#print axioms SuccessionHistoryInterface.run_withHistory
#print axioms SuccessionHistoryInterface.runnable_withHistory
#print axioms SuccessionHistoryInterface.spent_withHistory
#print axioms SuccessionHistoryInterface.trace_withHistory
#print axioms SuccessionHistoryInterface.continuation_interface
#print axioms SuccessionHistoryInterface.toOld_withHistory
#print axioms SuccessionHistoryInterface.bankWord_withHistory
#print axioms SuccessionHistoryInterface.runBank_withHistory
#print axioms SuccessionHistoryInterface.actual_suffix_withHistory
#print axioms SuccessionHistoryInterface.actual_suffix_accounting
#print axioms SuccessionHistoryInterface.actual_suffix_live_outcome
