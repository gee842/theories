import FormedRouteMonitor

/- A new finite head and guarded in-place swap, composed with the unchanged
monitor and learner. Parts, grants and copy packet are separately supplied.
Only the inherited plant's work event reads the hidden productive law. -/
namespace RouteRevision
open RecipientCorrection
open FormedRecipientRoute (Route Template)
set_option maxRecDepth 8192
set_option maxHeartbeats 3000000

inductive Phase where | waiting | released | assembled | inspected | changed | broken
  deriving DecidableEq, Repr

structure State where
  monitor : FormedRouteMonitor.State
  protectedFuel : Nat
  probeProvision : Nat
  copyPacket : Nat
  freeHeads : Nat
  head : Bool
  armed : Bool
  freeReplacement : Nat
  retiredRoutes : Nat
  childBlanks : Nat
  childRoutes : Nat
  phase : Phase
  probes : Nat
  deriving DecidableEq, Repr

def initial (monitor : FormedRouteMonitor.State) : State :=
  ⟨monitor,5,20,10,1,false,false,1,0,1,1,.waiting,0⟩

def firstBoundary (m : FormedRouteMonitor.State) : Prop :=
  m.phase=.ready ∧ m.quota=.one ∧ m.binding=true ∧ m.busValid=true ∧
  m.core.phase=.ready ∧ m.core.funded=none ∧ m.core.carrier=true ∧
  m.core.routing=true ∧ m.core.childFuel=0 ∧ m.core.template.q<4

instance (m : FormedRouteMonitor.State) : Decidable (firstBoundary m) := by
  unfold firstBoundary
  infer_instance

/-- Only the physically read class gates an attempt; not route identity or truth. -/
def requests : Option RouteDiagnostics.Class → Bool
  | some .unchanged | some .privateZero => true
  | _ => false

def energy (s : State) : Nat :=
  FormedRouteMonitor.energy s.monitor+s.protectedFuel+s.probeProvision+s.copyPacket

def heads (s : State) : Nat := s.freeHeads + if s.head then 1 else 0

def routeParts (s : State) : Nat :=
  s.freeReplacement+s.retiredRoutes+(if s.monitor.core.routing then 1 else 0)

def paidMonitor (s : State) : FormedRouteMonitor.State :=
  {s.monitor with core:=FormedRouteMonitor.fee s.monitor.core 1}

inductive Event where
  | release | assemble | read | keep | swap (route : Route)
  | learn (event : SuccessorLearning.Event) | breakBinding
  deriving DecidableEq, Repr

def Enabled (s : State) : Event → Prop
  | .release => s.phase=.waiting ∧ firstBoundary s.monitor
  | .assemble => s.phase=.released ∧ s.head=false ∧ 1≤s.freeHeads ∧
      FormedRouteMonitor.FeeEnabled s.monitor.core 1
  | .read => s.phase=.assembled ∧ s.head=true ∧ s.monitor.binding=true ∧
      FormedRouteMonitor.FeeEnabled s.monitor.core 1
  | .keep => s.phase=.inspected ∧ s.head=true ∧ s.armed=false ∧ s.monitor.binding=true
  | .swap _ => s.phase=.inspected ∧ s.head=true ∧ s.armed=true ∧
      s.monitor.binding=true ∧ s.monitor.core.routing=true ∧ 1≤s.freeReplacement ∧
      FormedRouteMonitor.FeeEnabled s.monitor.core 1
  | .learn e => s.phase=.changed ∧ (e=.reverse ∨ s.probes<3) ∧
      SuccessorLearning.Enabled SuccessorLearning.primary s.monitor.core e
  | .breakBinding => True

def advance (s : State) : Event → State
  | .release => {s with
      monitor:={s.monitor with core:={s.monitor.core with
        recipient:=s.monitor.core.recipient+s.protectedFuel,
        source:=s.monitor.core.source+s.probeProvision}},
      protectedFuel:=0,probeProvision:=0,phase:=.released}
  | .assemble => {s with monitor:=paidMonitor s,freeHeads:=s.freeHeads-1,head:=true,phase:=.assembled}
  | .read => {s with monitor:=paidMonitor s,armed:=requests (FormedRouteMonitor.diagnosis s.monitor),phase:=.inspected}
  | .keep => {s with phase:=.changed}
  | .swap route =>
      let old := FormedRouteMonitor.advance (some true) (paidMonitor s) .breakBinding
      { s with
        monitor := {old with core := {old.core with template := ⟨route,old.core.template.q⟩}}
        freeReplacement := s.freeReplacement-1
        retiredRoutes := s.retiredRoutes+1
        armed := false
        phase := .changed }
  | .learn e => { s with
      monitor := {s.monitor with core:=SuccessorLearning.advance SuccessorLearning.primary s.monitor.core e}
      probes := s.probes+(if e=.perform .write then 1 else 0) }
  | .breakBinding => { s with
      monitor := FormedRouteMonitor.advance (some true) s.monitor .breakBinding
      armed := false
      phase := .broken }

def Step (s : State) (e : Event) (t : State) : Prop := Enabled s e ∧ t=advance s e
inductive Trace : State → List Event → State → Prop where
  | nil (s : State) : Trace s [] s
  | cons {s m t : State} {e : Event} {es : List Event} :
      Step s e m → Trace m es t → Trace s (e::es) t

def run : State → List Event → State
  | s,[] => s
  | s,e::es => run (advance s e) es

def allEnabled : State → List Event → Prop
  | _,[] => True
  | s,e::es => Enabled s e ∧ allEnabled (advance s e) es

instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled firstBoundary FormedRouteMonitor.FeeEnabled <;> infer_instance
instance allEnabledDecidable (s : State) (es : List Event) : Decidable (allEnabled s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => @instDecidableAnd (Enabled s e) (allEnabled (advance s e) es)
      (inferInstance) (allEnabledDecidable (advance s e) es)

theorem enabled_list_is_trace (s : State) (es : List Event) (h : allEnabled s es) :
    Trace s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih _ h.2)

theorem run_append (s : State) (xs ys : List Event) : run s (xs++ys)=run (run s xs) ys := by
  induction xs generalizing s with
  | nil => rfl
  | cons x xs ih => exact ih _

theorem proposals_have_identical_guards (s : State) (a b : Route) :
    Enabled s (.swap a) ↔ Enabled s (.swap b) := Iff.rfl

theorem paid_read_uses_only_actual_diagnosis (s : State) :
    (advance s .read).armed=requests (FormedRouteMonitor.diagnosis s.monitor) := rfl

theorem read_requests_iff (s : State) :
    (advance s .read).armed=true ↔
      FormedRouteMonitor.diagnosis s.monitor=some .unchanged ∨
      FormedRouteMonitor.diagnosis s.monitor=some .privateZero := by
  cases h : FormedRouteMonitor.diagnosis s.monitor with
  | none => simp [advance,requests,h]
  | some c => cases c <;> simp [advance,requests,h]

theorem read_ignores_hidden_law (s : State) (law : Bool) :
    (advance {s with monitor:={s.monitor with core:={s.monitor.core with law:=law}}} .read).armed=
      (advance s .read).armed := rfl

theorem swap_preserves_actual_record_and_actor (s : State) (r : Route) :
    (advance s (.swap r)).monitor.core.template.q=s.monitor.core.template.q ∧
    (advance s (.swap r)).monitor.core.originalActor=s.monitor.core.originalActor ∧
    (advance s (.swap r)).monitor.core.template.route=r := ⟨rfl,rfl,rfl⟩

theorem swap_invalidates_old_evidence (s : State) (r : Route) :
    (advance s (.swap r)).armed=false ∧
    (advance s (.swap r)).monitor.binding=false ∧
    (advance s (.swap r)).monitor.success=.unseen ∧
    (advance s (.swap r)).monitor.failure=.unseen ∧
    FormedRouteMonitor.diagnosis (advance s (.swap r)).monitor=none := by
  exact ⟨rfl,rfl,rfl,rfl,rfl⟩

theorem binding_break_cancels_swap (s : State) (r : Route) :
    ¬ Enabled (advance s .breakBinding) (.swap r) := by simp [Enabled,advance]

theorem missing_part_blocks_swap (s : State) (r : Route) (h : s.freeReplacement=0) :
    ¬ Enabled s (.swap r) := by simp [Enabled,h]

theorem read_and_swap_do_not_refund (s : State) (r : Route) :
    (advance s .read).monitor.core.spent=s.monitor.core.spent+1 ∧
    (advance (advance s .read) (.swap r)).monitor.core.spent=s.monitor.core.spent+2 := by
  simp [advance,paidMonitor,FormedRouteMonitor.fee,FormedRouteMonitor.advance,Nat.add_assoc]

theorem step_accounts {s t : State} {e : Event} (h : Step s e t) :
    energy t=energy s ∧ heads t=heads s ∧ routeParts t=routeParts s ∧
    t.childBlanks=s.childBlanks ∧ t.childRoutes=s.childRoutes ∧
    FormedRouteMonitor.cells t.monitor=FormedRouteMonitor.cells s.monitor ∧
    FormedRouteMonitor.heads t.monitor=FormedRouteMonitor.heads s.monitor ∧
    t.monitor.core.originalActor=s.monitor.core.originalActor := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | release =>
      refine ⟨?_,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩
      simp only [advance,energy,FormedRouteMonitor.energy,SuccessorLearning.energy]
      omega
  | assemble =>
      have hf:=FormedRouteMonitor.fee_accounts s.monitor.core 1 he.2.2.2
      refine ⟨?_,?_,rfl,rfl,rfl,rfl,rfl,rfl⟩
      · exact congrArg (fun n => n+s.protectedFuel+s.probeProvision+s.copyPacket) hf.1
      · have hp:=he.2.2.1
        simp [heads,advance,he.2.1]
        omega
  | read =>
      have hf:=FormedRouteMonitor.fee_accounts s.monitor.core 1 he.2.2.2
      exact ⟨congrArg (fun n => n+s.protectedFuel+s.probeProvision+s.copyPacket) hf.1,
        rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩
  | swap r =>
      have hf:=FormedRouteMonitor.fee_accounts s.monitor.core 1 he.2.2.2.2.2.2
      refine ⟨?_,rfl,?_,rfl,rfl,rfl,rfl,rfl⟩
      · exact congrArg (fun n => n+s.protectedFuel+s.probeProvision+s.copyPacket) hf.1
      · have hp:=he.2.2.2.2.2.1
        cases hr : s.monitor.core.routing <;>
          simp [routeParts,advance,paidMonitor,FormedRouteMonitor.advance,FormedRouteMonitor.fee,hr] <;> omega
  | learn ev =>
      have hs : SuccessorLearning.Step SuccessorLearning.primary s.monitor.core ev _ := ⟨he.2.2,rfl⟩
      have hf:=SuccessorLearning.step_energy_account hs
      have hp:=SuccessorLearning.step_preserves_actor_route_and_carrier hs
      refine ⟨congrArg (fun n => n+s.protectedFuel+s.probeProvision+s.copyPacket) hf,
        rfl,?_,rfl,rfl,rfl,rfl,hp.1⟩
      simp [routeParts,advance,hp.2.2.2]
  | keep | breakBinding => exact ⟨rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem trace_accounts {s t : State} {es : List Event} (h : Trace s es t) :
    energy t=energy s ∧ heads t=heads s ∧ routeParts t=routeParts s ∧
    t.childBlanks=s.childBlanks ∧ t.childRoutes=s.childRoutes ∧
    FormedRouteMonitor.cells t.monitor=FormedRouteMonitor.cells s.monitor ∧
    FormedRouteMonitor.heads t.monitor=FormedRouteMonitor.heads s.monitor ∧
    t.monitor.core.originalActor=s.monitor.core.originalActor := by
  induction h with
  | nil => exact ⟨rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩
  | cons hs _ ih =>
      have hm:=step_accounts hs
      exact ⟨ih.1.trans hm.1,ih.2.1.trans hm.2.1,ih.2.2.1.trans hm.2.2.1,
        ih.2.2.2.1.trans hm.2.2.2.1,ih.2.2.2.2.1.trans hm.2.2.2.2.1,
        ih.2.2.2.2.2.1.trans hm.2.2.2.2.2.1,
        ih.2.2.2.2.2.2.1.trans hm.2.2.2.2.2.2.1,
        ih.2.2.2.2.2.2.2.trans hm.2.2.2.2.2.2.2⟩

theorem step_floor {s t : State} {e : Event} (h : Step s e t)
    (hr : 1≤s.monitor.core.recipient) : 1≤t.monitor.core.recipient := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | release => simp only [advance]; omega
  | assemble | read => exact (FormedRouteMonitor.fee_accounts _ _ he.2.2.2).2.1
  | swap r => exact (FormedRouteMonitor.fee_accounts _ _ he.2.2.2.2.2.2).2.1
  | learn ev => exact SuccessorLearning.step_preserves_recipient_floor ⟨he.2.2,rfl⟩ hr
  | keep | breakBinding => exact hr

theorem step_payload_bound {s t : State} {e : Event} (h : Step s e t)
    (hq : s.monitor.core.template.q<4) : t.monitor.core.template.q<4 := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | learn ev => exact SuccessorLearning.step_preserves_payload_bound ⟨he.2.2,rfl⟩ hq
  | release | assemble | read | keep | swap r | breakBinding => exact hq

theorem step_probe_bound {s t : State} {e : Event} (h : Step s e t)
    (hn : s.probes≤3) : t.probes≤3 := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | learn ev =>
      change s.probes+(if ev=.perform .write then 1 else 0)≤3
      by_cases hw : ev=.perform .write
      · have hh : s.probes<3 := by
          rcases he.2.1 with hh|hh
          · cases hh; contradiction
          · exact hh
        simp only [hw,ite_true]; omega
      · simp only [hw,ite_false,Nat.add_zero]; exact hn
  | release | assemble | read | keep | swap r | breakBinding => exact hn

def replacement (r : Route) : List Event := [.release,.assemble,.read,.swap r]
def trial : List Event := SuccessorLearning.trial.map Event.learn

def probes3 : List Event := trial++trial++trial

def ordinaryBoundary (r : Route) : FormedRouteMonitor.State := FormedRouteMonitor.afterFirst r

def proxyBoundary : FormedRouteMonitor.State :=
  FormedRouteMonitor.run (some true) (FormedRouteMonitor.assembled .privateZero 15 false) FormedRouteMonitor.frame

def repaired (r : Route) : State := run (initial (ordinaryBoundary .closed)) (replacement r)
def tested (r : Route) : State := run (repaired r) probes3

theorem actual_first_monitor_boundary :
    FormedRouteMonitor.allEnabled (some true) (FormedRouteMonitor.initial .closed 25 true)
      ([.assemble]++FormedRouteMonitor.frame) ∧
    firstBoundary (ordinaryBoundary .closed) ∧
    (ordinaryBoundary .closed).core.recipient=11 ∧
    (ordinaryBoundary .closed).core.source=10 ∧
    FormedRouteMonitor.diagnosis (ordinaryBoundary .closed)=some .unchanged := by decide

theorem actual_controlled_proxy_boundary :
    FormedRouteMonitor.allEnabled (some true) (FormedRouteMonitor.initial .privateZero 15 false)
      ([.assemble]++FormedRouteMonitor.frame) ∧
    firstBoundary proxyBoundary ∧ proxyBoundary.core.recipient=11 ∧
    proxyBoundary.core.source=10 ∧ FormedRouteMonitor.diagnosis proxyBoundary=some .privateZero := by decide

theorem every_proposal_is_paid (r : Route) :
    allEnabled (initial (ordinaryBoundary .closed)) (replacement r) ∧
    (repaired r).monitor.core.recipient=13 ∧ (repaired r).monitor.core.source=30 ∧
    (repaired r).copyPacket=10 ∧ (repaired r).monitor.core.template=⟨r,0⟩ ∧
    (repaired r).retiredRoutes=1 ∧ (repaired r).freeReplacement=0 := by cases r <;> decide

theorem target_three_probes_are_actual :
    allEnabled (repaired .target) probes3 ∧
    (tested .target).monitor.core.recipient=12 ∧ (tested .target).monitor.core.source=0 ∧
    (tested .target).monitor.core.template=⟨.target,2⟩ ∧ (tested .target).probes=3 := by decide

theorem proxy_three_probes_are_actual :
    allEnabled (repaired .privateZero) probes3 ∧
    (tested .privateZero).monitor.core.recipient=2 ∧ (tested .privateZero).monitor.core.source=0 ∧
    (tested .privateZero).monitor.core.template=⟨.privateZero,2⟩ := by decide

def twoWorkPrefix : List Event := trial ++
  [.learn (.fund .rent),.learn (.perform .rent),.learn (.fund .sense),.learn (.perform .sense),
   .learn (.fund .work),.learn (.perform .work)]

theorem nonwriters_stop_in_partial_probe (r : Route) (h : r=.closed ∨ r=.frozen) :
    allEnabled (repaired r) twoWorkPrefix ∧
    (run (repaired r) twoWorkPrefix).monitor.core.recipient=1 ∧
    (run (repaired r) twoWorkPrefix).monitor.core.source=10 ∧
    (run (repaired r) twoWorkPrefix).monitor.core.phase=.worked ∧
    ¬ Enabled (run (repaired r) twoWorkPrefix) (.learn (.fund .observe)) := by
  rcases h with rfl|rfl <;> decide

/-- No free class test can avoid either diagnostic access fee. -/
theorem unresolved_first_frame_pays_without_swap :
    let s:=run (initial (ordinaryBoundary .target)) [.release,.assemble,.read]
    allEnabled (initial (ordinaryBoundary .target)) [.release,.assemble,.read] ∧
    s.monitor.core.recipient=14 ∧ s.monitor.core.spent=16 ∧
    s.armed=false ∧ s.freeReplacement=1 ∧
    ∀ r, ¬ Enabled s (.swap r) := by
  dsimp only
  refine ⟨by decide,by decide,by decide,by decide,by decide,?_⟩
  intro r
  cases r <;> decide

theorem nonrequesting_read_cannot_swap (s : State) (r : Route)
    (h : requests (FormedRouteMonitor.diagnosis s.monitor)=false) :
    ¬ Enabled (advance s .read) (.swap r) := by simp [Enabled,advance,h]

theorem successful_swap_is_single_use (s : State) (a b : Route) :
    ¬ Enabled (advance s (.swap a)) (.swap b) := by simp [Enabled,advance]

theorem trace_floor_payload_and_probe_bounds {s t : State} {es : List Event}
    (h : Trace s es t) (hr : 1≤s.monitor.core.recipient)
    (hq : s.monitor.core.template.q<4) (hn : s.probes≤3) :
    1≤t.monitor.core.recipient ∧ t.monitor.core.template.q<4 ∧ t.probes≤3 := by
  induction h with
  | nil => exact ⟨hr,hq,hn⟩
  | cons hs _ ih => exact ih (step_floor hs hr) (step_payload_bound hs hq) (step_probe_bound hs hn)

/-- The paid read's no-replacement decision changes only the finite control
phase. It neither changes the inherited route nor refunds diagnostic access. -/
theorem keep_preserves_actual_state (s : State) :
    (advance s .keep).monitor=s.monitor ∧
    (advance s .keep).freeReplacement=s.freeReplacement ∧
    (advance s .keep).retiredRoutes=s.retiredRoutes ∧
    (advance s .keep).phase=.changed := ⟨rfl,rfl,rfl,rfl⟩

theorem armed_swap_request_cannot_keep (s : State) (h : s.armed=true) :
    ¬ Enabled s .keep := by simp [Enabled,h]

def keepDecision : List Event := [.release,.assemble,.read,.keep]
def keptTarget : State := run (initial (ordinaryBoundary .target)) keepDecision
def keptTargetTested : State := run keptTarget probes3

theorem unresolved_paid_decision_continues_actual_learner :
    allEnabled (initial (ordinaryBoundary .target)) keepDecision ∧
    keptTarget.monitor.core.recipient=14 ∧ keptTarget.monitor.core.spent=16 ∧
    keptTarget.monitor.core.template=⟨.target,2⟩ ∧ keptTarget.freeReplacement=1 ∧
    keptTarget.retiredRoutes=0 ∧ allEnabled keptTarget probes3 ∧
    keptTargetTested.monitor.core.recipient=23 ∧ keptTargetTested.monitor.core.source=0 ∧
    keptTargetTested.monitor.core.template=⟨.target,2⟩ := by decide

#print axioms RouteRevision.enabled_list_is_trace
#print axioms RouteRevision.run_append
#print axioms RouteRevision.proposals_have_identical_guards
#print axioms RouteRevision.paid_read_uses_only_actual_diagnosis
#print axioms RouteRevision.read_requests_iff
#print axioms RouteRevision.read_ignores_hidden_law
#print axioms RouteRevision.swap_preserves_actual_record_and_actor
#print axioms RouteRevision.swap_invalidates_old_evidence
#print axioms RouteRevision.binding_break_cancels_swap
#print axioms RouteRevision.missing_part_blocks_swap
#print axioms RouteRevision.read_and_swap_do_not_refund
#print axioms RouteRevision.step_accounts
#print axioms RouteRevision.trace_accounts
#print axioms RouteRevision.step_floor
#print axioms RouteRevision.step_payload_bound
#print axioms RouteRevision.step_probe_bound
#print axioms RouteRevision.actual_first_monitor_boundary
#print axioms RouteRevision.actual_controlled_proxy_boundary
#print axioms RouteRevision.every_proposal_is_paid
#print axioms RouteRevision.target_three_probes_are_actual
#print axioms RouteRevision.proxy_three_probes_are_actual
#print axioms RouteRevision.nonwriters_stop_in_partial_probe
#print axioms RouteRevision.unresolved_first_frame_pays_without_swap
#print axioms RouteRevision.nonrequesting_read_cannot_swap
#print axioms RouteRevision.successful_swap_is_single_use
#print axioms RouteRevision.trace_floor_payload_and_probe_bounds
#print axioms RouteRevision.keep_preserves_actual_state
#print axioms RouteRevision.armed_swap_request_cannot_keep
#print axioms RouteRevision.unresolved_paid_decision_continues_actual_learner

end RouteRevision
