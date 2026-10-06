import InquiryRevision
import PurposeCorrection

/- Native adapter to existing inquiry revision. The floor is a prospective
   application condition at the reached count-four boundary, not a reward or
   event-law parameter. Nothing here identifies stock with experience or proves
   autonomous formation of an ethical end. Earlier acquisition remains intact. -/
namespace PurposeCorrectionHistory
open PairedPlasticity
open Generative.PurposeCorrection
set_option maxHeartbeats 8000000
set_option maxRecDepth 32768

/-- What can remain true before the first new recipientPay. -/
def BeforeDebit (b : Nat) (s : PairedPlasticity.State) : Prop :=
  patient s=b ∧ (core s).phase=.ready ∧ s.count=4 ∧
  s.continuation=true ∧ s.portMode=.idle ∧
  (s.phase=.ready ∨ s.phase=.ownPaid ∨ s.phase=.ownReturned)

 theorem reason_core {laws : RecipientCorrection.Laws} {s : PairedPlasticity.State}
    {e : PaidRecipientReasons.Event} (h : Enabled s (.reason e)) :
    core (advance laws s (.reason e))=core s := by
  have hw:=PaidRecipientReasons.step_preserves_world
    (show PaidRecipientReasons.Step s.parent.parent.reasons e
      (PaidRecipientReasons.advance s.parent.parent.reasons e) from ⟨h,rfl⟩)
  exact congrArg (fun w => w.world.core) hw

 theorem beforeDebit_step {laws : RecipientCorrection.Laws} {s : PairedPlasticity.State}
    {e : PairedPlasticity.Event} {b : Nat}
    (hs : BeforeDebit b s) (he : Enabled s e) (hne : e≠.recipientPay) :
    BeforeDebit b (advance laws s e) := by
  rcases hs with ⟨hb,hp,hc,ht,hm,hphase⟩
  cases e with
  | recipientPay => exact False.elim (hne rfl)
  | ownPay => exact ⟨hb,hp,hc,ht,rfl,Or.inr (Or.inl rfl)⟩
  | ownReturn v => exact ⟨hb,hp,hc,ht,hm,Or.inr (Or.inr rfl)⟩
  | reason e =>
      have hk:=reason_core (laws:=laws) he
      refine ⟨?_,?_,hc,ht,?_,hphase⟩
      · exact (congrArg RecipientIdentification.State.patient hk).trans hb
      · exact (congrArg RecipientIdentification.State.phase hk).trans hp
      · simp [advance,hm]
  | scope v | permission v | delivery v =>
      simpa [BeforeDebit,advance,old,FreshRevision.actionAdvance,core,
        FreshRevision.core,RecipientAction.advance,RecipientAction.clear,
        RecipientAction.core,hm] using And.intro hb (And.intro hp (And.intro hc (And.intro ht (And.intro hm hphase))))
  | trial e =>
      have hsettle:=he.2
      have hp' : (RecipientAction.core s.parent.parent).phase=.ready := hp
      cases e <;> simp [RecipientAction.Settlement,hp',hm] at hsettle
  | close =>
      simp [Enabled,limit,hc,ht] at he
  | assess | attempt | abstain =>
      simp [Enabled,hm] at he
  | recipientReturn v | ownRead c | recipientRead c | skip | bind | replace | nativeWrite | read =>
      rcases hphase with hphase|hphase|hphase
      all_goals simp [Enabled,hphase] at he

 theorem first_debit {laws : RecipientCorrection.Laws} {s : PairedPlasticity.State} {b : Nat}
    (hs : BeforeDebit b s) : patient (advance laws s .recipientPay)=b-2 := by
  change patient s-2=b-2
  rw [hs.1]

/-- An arbitrary admitted old-law response history contains its first new debit.
    This is induction over all finite traces, not enumeration of selected words. -/
theorem every_response_has_debit_prefix {laws : RecipientCorrection.Laws}
    {s t : PairedPlasticity.State} {es : List PairedPlasticity.Event} {b : Nat}
    (h : Generative.Trace (PairedPlasticity.process laws) s es t)
    (hs : BeforeDebit b s) (ht : t.portMode≠.idle) :
    ∃ pre post v, es=pre++(.recipientPay::post) ∧
      Generative.Trace (PairedPlasticity.process laws) s pre v ∧
      BeforeDebit b v ∧ Enabled v .recipientPay ∧
      patient (advance laws v .recipientPay)=b-2 := by
  induction h with
  | nil => exact False.elim (ht hs.2.2.2.2.1)
  | @cons s m t e es he hh ih =>
      rcases he with ⟨hen,rfl⟩
      by_cases hdebit : e=.recipientPay
      · subst e
        exact ⟨[],es,s,rfl,.nil s,hs,hen,first_debit hs⟩
      · rcases ih (beforeDebit_step hs hen hdebit) ht with ⟨pre,post,v,hw,hv,hb,hpay,hstock⟩
        exact ⟨e::pre,post,v,by simp [hw],.cons ⟨hen,rfl⟩ hv,hb,hpay,hstock⟩

def boundary : PairedPlasticity.State := InquiryRevision.s4.parent

theorem boundary_before_debit : BeforeDebit 36 boundary := by unfold BeforeDebit; decide

theorem every_actual_old_response_hits_34
    {t : PairedPlasticity.State} {es : List PairedPlasticity.Event}
    (h : Generative.Trace (PairedPlasticity.process PlasticityWitness.laws) boundary es t)
    (ht : t.portMode≠.idle) :
    ∃ pre post v, es=pre++(.recipientPay::post) ∧
      Generative.Trace (PairedPlasticity.process PlasticityWitness.laws) boundary pre v ∧
      BeforeDebit 36 v ∧ Enabled v .recipientPay ∧
      patient (advance PlasticityWitness.laws v .recipientPay)=34 :=
  every_response_has_debit_prefix h boundary_before_debit ht

/-- Existing old law can finish both additional encounters and the response.
    The two return events restore the stock after each new debit. -/
def oldWord : List PairedPlasticity.Event :=
  PlasticityWitness.pair true false ++ PlasticityWitness.pair true false ++
  [.close,.read,.assess] ++ PlasticityWitness.actionWord
def oldFinal := PairedPlasticity.run PlasticityWitness.laws boundary oldWord

theorem old_target_is_completed :
    PairedPlasticity.Runnable PlasticityWitness.laws boundary oldWord ∧
    oldFinal.count=6 ∧ oldFinal.portMode=.consumed ∧
    (core oldFinal).packets=0 ∧ patient oldFinal=46 ∧ fuel oldFinal=6 := by decide

theorem old_actual_trace :
    Generative.Trace (PairedPlasticity.process PlasticityWitness.laws) boundary oldWord oldFinal :=
  PairedPlasticity.runnable_trace old_target_is_completed.1

/-- The formed extension starts with exactly the reached parent state. -/
def newWord := InquiryRevision.adaptation++InquiryRevision.assessment++InquiryRevision.action

theorem same_boundary_and_response :
    InquiryRevision.s4.parent=boundary ∧ boundary.continuation=true ∧
    patient boundary=36 ∧ fuel boundary=14 ∧
    PairedPlasticity.patient InquiryRevision.final.parent=46 ∧
    InquiryRevision.final.parent.portMode=.consumed ∧
    (core InquiryRevision.final.parent).packets=0 ∧
    fuel InquiryRevision.final.parent=1 ∧ InquiryRevision.material InquiryRevision.final=68 := by
  constructor
  · rfl
  · decide


def oldFloor (f : Nat) (s : PairedPlasticity.State) : Prop := f≤patient s
/-- The specified response endpoint includes actual restoration to stock 46. -/
def response (s : PairedPlasticity.State) : Prop :=
  s.portMode=.consumed ∧ (core s).packets=0 ∧ patient s=46

theorem guarded_old_trace_stays_before_debit {laws : RecipientCorrection.Laws}
    {s t : PairedPlasticity.State} {es : List PairedPlasticity.Event} {b f : Nat}
    (h : Generative.Trace (guarded (PairedPlasticity.process laws) (oldFloor f)) s es t)
    (hs : BeforeDebit b s) (hf : b-2<f) : BeforeDebit b t := by
  induction h with
  | nil => exact hs
  | @cons s m t e es he hh ih =>
      rcases he with ⟨⟨hen,rfl⟩,hks,hkt⟩
      by_cases hdebit : e=.recipientPay
      · subst e
        have hp:=first_debit (laws:=laws) hs
        change f≤patient (advance laws s .recipientPay) at hkt
        rw [hp] at hkt
        omega
      · exact ih (beforeDebit_step hs hen hdebit)

theorem old_response_not_viable (f : Nat) (hf : 34<f) :
    ¬Viable (PairedPlasticity.process PlasticityWitness.laws) (oldFloor f) response boundary := by
  rintro ⟨es,t,hk,htrace,hresponse⟩
  have hi:=guarded_old_trace_stays_before_debit htrace boundary_before_debit hf
  have hm:=hi.2.2.2.2.1
  have hc:=hresponse.1
  simp [hm] at hc

/-- Changing only a ranking/selection of old-law paths cannot remove the obstruction. -/
theorem old_restriction_cannot_repair (Q : Generative.Process PairedPlasticity.State PairedPlasticity.Event)
    (hQ : Extends Q (PairedPlasticity.process PlasticityWitness.laws))
    (f : Nat) (hf : 34<f) : ¬Viable Q (oldFloor f) response boundary :=
  no_restriction_creates_completion hQ (old_response_not_viable f hf)

def newFloor (f : Nat) (s : InquiryRevision.State) : Prop := f≤patient s.parent

def FloorRunnable (f : Nat) (s : InquiryRevision.State) : List InquiryRevision.Event → Prop
  | [] => newFloor f s
  | e::es => InquiryRevision.Enabled s e ∧ newFloor f s ∧
      FloorRunnable f (InquiryRevision.advance PlasticityWitness.laws s e) es
instance floorRunnableDecidable (f : Nat) (s : InquiryRevision.State) (es : List InquiryRevision.Event) :
    Decidable (FloorRunnable f s es) :=
  match es with
  | [] => inferInstanceAs (Decidable (f≤patient s.parent))
  | e::es => let _:=floorRunnableDecidable f (InquiryRevision.advance PlasticityWitness.laws s e) es
             inferInstanceAs (Decidable (InquiryRevision.Enabled s e ∧ (f≤patient s.parent) ∧
               FloorRunnable f (InquiryRevision.advance PlasticityWitness.laws s e) es))

theorem floorRunnable_start {f : Nat} {s : InquiryRevision.State} {es : List InquiryRevision.Event}
    (h : FloorRunnable f s es) : newFloor f s := by
  cases es with
  | nil => exact h
  | cons e es => exact h.2.1

theorem floorRunnable_trace {f : Nat} {s : InquiryRevision.State} {es : List InquiryRevision.Event}
    (h : FloorRunnable f s es) :
    Generative.Trace (guarded (InquiryRevision.process PlasticityWitness.laws) (newFloor f))
      s es (InquiryRevision.run PlasticityWitness.laws s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
      exact .cons ⟨⟨h.1,rfl⟩,h.2.1,floorRunnable_start h.2.2⟩ (ih h.2.2)

theorem new_actual_floor_run : FloorRunnable 36 InquiryRevision.s4 newWord := by decide

theorem inquiry_run_append (s : InquiryRevision.State)
    (xs ys : List InquiryRevision.Event) :
    InquiryRevision.run PlasticityWitness.laws s (xs++ys) =
      InquiryRevision.run PlasticityWitness.laws
        (InquiryRevision.run PlasticityWitness.laws s xs) ys := by
  induction xs generalizing s with
  | nil => rfl
  | cons e xs ih => exact ih _

theorem new_run_final : InquiryRevision.run PlasticityWitness.laws InquiryRevision.s4 newWord =
    InquiryRevision.final := by
  unfold newWord
  rw [inquiry_run_append,inquiry_run_append]
  rfl

theorem new_actual_floor_trace :
    Generative.Trace (guarded (InquiryRevision.process PlasticityWitness.laws) (newFloor 36))
      InquiryRevision.s4 newWord InquiryRevision.final :=
  by
    have h:=floorRunnable_trace new_actual_floor_run
    rw [new_run_final] at h
    exact h

theorem new_response_viable (f : Nat) (hf : f≤36) :
    Viable (InquiryRevision.process PlasticityWitness.laws) (newFloor f)
      (fun s => response s.parent) InquiryRevision.s4 := by
  refine ⟨newWord,InquiryRevision.final,?_,?_,?_⟩
  · change f≤patient boundary
    have hb:=boundary_before_debit.1
    omega
  · exact Generative.trace_map (P:=guarded (InquiryRevision.process PlasticityWitness.laws) (newFloor 36))
      (Q:=guarded (InquiryRevision.process PlasticityWitness.laws) (newFloor f)) (f:=id)
      (fun _ _ _ he => ⟨he.1,Nat.le_trans hf he.2.1,Nat.le_trans hf he.2.2⟩)
      new_actual_floor_trace
  · unfold response
    decide

/-- For each independently applicable floor in this interval, unchanged access
    fails while the actual admitted extension has a floor-preserving response. -/
theorem actual_access_correction (f : Nat) (hl : 34<f) (hu : f≤36) :
    ¬Viable (PairedPlasticity.process PlasticityWitness.laws) (oldFloor f) response boundary ∧
    Viable (InquiryRevision.process PlasticityWitness.laws) (newFloor f)
      (fun s => response s.parent) InquiryRevision.s4 :=
  ⟨old_response_not_viable f hl,new_response_viable f hu⟩

end PurposeCorrectionHistory

#print axioms PurposeCorrectionHistory.reason_core
#print axioms PurposeCorrectionHistory.beforeDebit_step
#print axioms PurposeCorrectionHistory.first_debit

#print axioms PurposeCorrectionHistory.every_response_has_debit_prefix
#print axioms PurposeCorrectionHistory.boundary_before_debit
#print axioms PurposeCorrectionHistory.every_actual_old_response_hits_34
#print axioms PurposeCorrectionHistory.old_target_is_completed
#print axioms PurposeCorrectionHistory.old_actual_trace
#print axioms PurposeCorrectionHistory.same_boundary_and_response

#print axioms PurposeCorrectionHistory.guarded_old_trace_stays_before_debit
#print axioms PurposeCorrectionHistory.old_response_not_viable
#print axioms PurposeCorrectionHistory.old_restriction_cannot_repair
#print axioms PurposeCorrectionHistory.floorRunnable_start
#print axioms PurposeCorrectionHistory.floorRunnable_trace
#print axioms PurposeCorrectionHistory.new_actual_floor_run
#print axioms PurposeCorrectionHistory.new_actual_floor_trace
#print axioms PurposeCorrectionHistory.new_response_viable
#print axioms PurposeCorrectionHistory.actual_access_correction

#print axioms PurposeCorrectionHistory.inquiry_run_append
#print axioms PurposeCorrectionHistory.new_run_final
