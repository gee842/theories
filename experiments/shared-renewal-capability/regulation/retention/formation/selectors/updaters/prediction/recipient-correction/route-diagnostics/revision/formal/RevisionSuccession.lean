import RouteRevision

/- The copying module is imported unchanged. Only its source allocation is
rebound to the separately retained packet; unused probe source stays outside.
No route-quality score occurs in funding or copying guards. -/
namespace RevisionSuccession
open RecipientCorrection
open FormedRecipientRoute (Route Template)
open RouteRevision (State)
set_option maxRecDepth 8192
set_option maxHeartbeats 3000000

/-- Resource partition, not a new plant state or a new template. -/
def donor (s : State) : SuccessorLearning.State :=
  {s.monitor.core with source := s.copyPacket}

def FundDonor (s : State) : Prop :=
  SuccessorLearning.FundDonor FormedRecipientRoute.primary (donor s)

instance (s : State) : Decidable (FundDonor s) := by unfold FundDonor; infer_instance

def copyStart (s : State) : FormedRecipientRoute.State :=
  SuccessorLearning.copyStart FormedRecipientRoute.primary (donor s) s.childBlanks s.childRoutes

/-- Includes the old actor and every source/grant excluded from the copier. -/
def outsideEnergy (s : State) : Nat :=
  s.monitor.core.originalActor+s.monitor.core.source+s.protectedFuel+s.probeProvision

def copyEvents : List FormedRecipientRoute.Event := FormedRecipientRoute.prefixEvents++[.hold]

def copied (s : State) : FormedRecipientRoute.State :=
  FormedRecipientRoute.run FormedRecipientRoute.primary (copyStart s) copyEvents

theorem funding_preserves_whole_account (s : State) (h : FundDonor s) :
    FormedRecipientRoute.energy (copyStart s)+outsideEnergy s=RouteRevision.energy s := by
  have hf := (SuccessorLearning.funded_copy_start_preserves_accounts
    FormedRecipientRoute.primary (donor s) s.childBlanks s.childRoutes h).1
  simp only [copyStart] at *
  simp only [outsideEnergy,RouteRevision.energy,FormedRouteMonitor.energy,
    SuccessorLearning.energy,donor] at *
  omega

theorem funded_copy_preserves_actual_template (s : State) :
    (copyStart s).donor=s.monitor.core.template ∧
    (copyStart s).law=s.monitor.core.law ∧
    (copyStart s).source=s.copyPacket ∧
    (copyStart s).spent=s.monitor.core.spent ∧
    (copyStart s).wasted=s.monitor.core.wasted := ⟨rfl,rfl,rfl,rfl,rfl⟩

theorem inherited_copy_trace_accounts (s : State) (h : FundDonor s)
    (es : List FormedRecipientRoute.Event) (t : FormedRecipientRoute.State)
    (ht : FormedRecipientRoute.Trace FormedRecipientRoute.primary (copyStart s) es t) :
    FormedRecipientRoute.energy t+outsideEnergy s=RouteRevision.energy s ∧
    t.blanks+FormedRecipientRoute.carrierCount t=s.childBlanks ∧
    t.routingParts+FormedRecipientRoute.routingCount t=s.childRoutes ∧
    t.donor=s.monitor.core.template := by
  have ha := FormedRecipientRoute.trace_accounts ht
  refine ⟨?_,?_,?_,ha.2.2.2⟩
  · rw [ha.1]; exact funding_preserves_whole_account s h
  · simpa [copyStart,SuccessorLearning.copyStart,FormedRecipientRoute.carrierCount] using ha.2.1
  · simpa [copyStart,SuccessorLearning.copyStart,FormedRecipientRoute.routingCount] using ha.2.2.1

theorem target_retention_is_an_actual_paid_trace :
    FundDonor (RouteRevision.tested .target) ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary
      (copyStart (RouteRevision.tested .target)) copyEvents ∧
    (copied (RouteRevision.tested .target)).child=some ⟨.target,2⟩ ∧
    (copied (RouteRevision.tested .target)).phase=.retained ∧
    (copied (RouteRevision.tested .target)).recipientFuel=11 ∧
    (copied (RouteRevision.tested .target)).actorFuel=0 ∧
    (copied (RouteRevision.tested .target)).childFuel=0 ∧
    (copied (RouteRevision.tested .target)).source=0 ∧
    (copied (RouteRevision.tested .target)).spent=(RouteRevision.tested .target).monitor.core.spent+11 ∧
    (copied (RouteRevision.tested .target)).wasted=(RouteRevision.tested .target).monitor.core.wasted := by decide

theorem proxy_funds_donor_but_cannot_use :
    FundDonor (RouteRevision.tested .privateZero) ∧
    FormedRecipientRoute.Enabled FormedRecipientRoute.primary
      (copyStart (RouteRevision.tested .privateZero)) .donorHold ∧
    let t:=FormedRecipientRoute.advance FormedRecipientRoute.primary
      (copyStart (RouteRevision.tested .privateZero)) .donorHold
    t.recipientFuel=1 ∧ ¬ FormedRecipientRoute.Enabled FormedRecipientRoute.primary t .ownUse ∧
    t.child=none ∧ t.blanks=1 ∧ t.routingParts=1 ∧ t.source=10 := by decide

theorem nonwriters_cannot_fund_copy (r : Route) (h : r=.closed ∨ r=.frozen) :
    ¬ FundDonor (RouteRevision.run (RouteRevision.repaired r) RouteRevision.twoWorkPrefix) := by
  rcases h with rfl|rfl <;> decide

/-- Exact typed admission and complete first frame, followed by paid revision,
ordinary probes, donor funding and the unchanged copy/use/hold process. -/
theorem joined_monitor_revision_and_copy :
    FormedRouteMonitor.enter (FormedRouteMonitor.boundary .closed 0 25 true) 20 8 1=
      some (FormedRouteMonitor.initial .closed 25 true) ∧
    FormedRouteMonitor.Trace (some true) (FormedRouteMonitor.initial .closed 25 true)
      ([.assemble]++FormedRouteMonitor.frame) (RouteRevision.ordinaryBoundary .closed) ∧
    RouteRevision.Trace (RouteRevision.initial (RouteRevision.ordinaryBoundary .closed))
      (RouteRevision.replacement .target) (RouteRevision.repaired .target) ∧
    RouteRevision.Trace (RouteRevision.repaired .target) RouteRevision.probes3 (RouteRevision.tested .target) ∧
    FundDonor (RouteRevision.tested .target) ∧
    FormedRecipientRoute.Trace FormedRecipientRoute.primary (copyStart (RouteRevision.tested .target))
      copyEvents (copied (RouteRevision.tested .target)) := by
  refine ⟨FormedRouteMonitor.typed_boundary_admission _ _ _,?_,?_,?_,
    target_retention_is_an_actual_paid_trace.1,?_⟩
  · exact FormedRouteMonitor.enabled_list_is_trace _ _ _ RouteRevision.actual_first_monitor_boundary.1
  · exact RouteRevision.enabled_list_is_trace _ _ (RouteRevision.every_proposal_is_paid .target).1
  · exact RouteRevision.enabled_list_is_trace _ _ RouteRevision.target_three_probes_are_actual.1
  · exact FormedRecipientRoute.enabled_list_is_trace _ _ _ target_retention_is_an_actual_paid_trace.2.1

def proxyAncestryTarget : State :=
  RouteRevision.run (RouteRevision.initial RouteRevision.proxyBoundary)
    (RouteRevision.replacement .target++RouteRevision.probes3)

theorem actual_controlled_ancestry_also_repairs :
    RouteRevision.allEnabled (RouteRevision.initial RouteRevision.proxyBoundary)
      (RouteRevision.replacement .target++RouteRevision.probes3) ∧
    proxyAncestryTarget.monitor.core.template=⟨.target,0⟩ ∧
    proxyAncestryTarget.monitor.core.recipient=12 ∧ FundDonor proxyAncestryTarget ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart proxyAncestryTarget) copyEvents ∧
    (copied proxyAncestryTarget).child=some ⟨.target,0⟩ ∧
    (copied proxyAncestryTarget).recipientFuel=11 := by decide

def reversalProbes : List RouteRevision.Event :=
  RouteRevision.trial++RouteRevision.trial++[.learn .reverse]++RouteRevision.trial

def reversed (r : Route) : State := RouteRevision.run (RouteRevision.repaired r) reversalProbes

theorem late_reversal_blocks_corrected_target :
    RouteRevision.allEnabled (RouteRevision.repaired .target) reversalProbes ∧
    (reversed .target).monitor.core.recipient=2 ∧
    (reversed .target).monitor.core.template=⟨.target,0⟩ ∧
    (reversed .target).monitor.core.law=false ∧
    ¬ FormedRecipientRoute.Enabled FormedRecipientRoute.primary
      (FormedRecipientRoute.advance FormedRecipientRoute.primary (copyStart (reversed .target)) .donorHold) .ownUse := by decide

theorem late_reversal_retains_wrong_proxy_child :
    RouteRevision.allEnabled (RouteRevision.repaired .privateZero) reversalProbes ∧
    (reversed .privateZero).monitor.core.recipient=12 ∧
    (reversed .privateZero).monitor.core.template=⟨.privateZero,2⟩ ∧
    (reversed .privateZero).monitor.core.law=false ∧
    FundDonor (reversed .privateZero) ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart (reversed .privateZero)) copyEvents ∧
    (copied (reversed .privateZero)).phase=.retained ∧
    (copied (reversed .privateZero)).recipientFuel=1 ∧
    (copied (reversed .privateZero)).child=some ⟨.privateZero,2⟩ ∧
    (copied (reversed .privateZero)).wasted=(reversed .privateZero).monitor.core.wasted+10 := by decide

/-- An alternative supplied horizon; no claim that the three-probe controller
can silently choose this schedule. -/
theorem immediate_copy_retains_wrong_payload :
    FundDonor (RouteRevision.repaired .target) ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart (RouteRevision.repaired .target)) copyEvents ∧
    (copied (RouteRevision.repaired .target)).phase=.retained ∧
    (copied (RouteRevision.repaired .target)).recipientFuel=2 ∧
    (copied (RouteRevision.repaired .target)).child=some ⟨.target,0⟩ ∧
    (copied (RouteRevision.repaired .target)).wasted=(RouteRevision.repaired .target).monitor.core.wasted+10 ∧
    (RouteRevision.repaired .target).monitor.core.source=30 := by decide

def probes2 (r : Route) : State :=
  RouteRevision.run (RouteRevision.repaired r) (RouteRevision.trial++RouteRevision.trial)

def writtenPrefix : List FormedRecipientRoute.Event := [.donorHold,.ownUse,.read,.assemble,.write]

theorem two_probes_pay_template_but_not_seed (r : Route) (h : r=.target ∨ r=.privateZero) :
    RouteRevision.allEnabled (RouteRevision.repaired r) (RouteRevision.trial++RouteRevision.trial) ∧
    (probes2 r).monitor.core.recipient=9 ∧ (probes2 r).monitor.core.source=10 ∧
    FundDonor (probes2 r) ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart (probes2 r)) writtenPrefix ∧
    let t:=FormedRecipientRoute.run FormedRecipientRoute.primary (copyStart (probes2 r)) writtenPrefix
    t.recipientFuel=4 ∧ t.child.isSome=true ∧
    ¬ FormedRecipientRoute.Enabled FormedRecipientRoute.primary t .seed := by
  rcases h with rfl|rfl <;> decide

def bufferedProxy : State :=
  RouteRevision.run {RouteRevision.initial (RouteRevision.ordinaryBoundary .closed) with protectedFuel:=15}
    (RouteRevision.replacement .privateZero++RouteRevision.probes3)

theorem extra_buffer_retains_same_proxy :
    RouteRevision.allEnabled {RouteRevision.initial (RouteRevision.ordinaryBoundary .closed) with protectedFuel:=15}
      (RouteRevision.replacement .privateZero++RouteRevision.probes3) ∧
    bufferedProxy.monitor.core.recipient=12 ∧ FundDonor bufferedProxy ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart bufferedProxy) copyEvents ∧
    (copied bufferedProxy).child=some ⟨.privateZero,2⟩ ∧
    (copied bufferedProxy).recipientFuel=11 := by decide

def beforeWork : List FormedRecipientRoute.Event :=
  [.donorHold,.ownUse,.read,.assemble,.write,.seed,.rent,.sense]

theorem missing_copy_packet_preserves_paid_partial_child :
    let s:={RouteRevision.tested .target with copyPacket:=0}
    FundDonor s ∧ FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart s) beforeWork ∧
    let t:=FormedRecipientRoute.run FormedRecipientRoute.primary (copyStart s) beforeWork
    t.child=some ⟨.target,2⟩ ∧ t.recipientFuel=2 ∧ t.childFuel=3 ∧ t.source=0 ∧
    t.phase=.sensed ∧ ¬ FormedRecipientRoute.Enabled FormedRecipientRoute.primary t .work ∧
    ¬ FormedRecipientRoute.Enabled FormedRecipientRoute.primary t .hold := by decide

theorem primary_whole_typed_ledger :
    (copied (RouteRevision.tested .target)).spent=49 ∧
    (copied (RouteRevision.tested .target)).wasted=20 ∧
    outsideEnergy (RouteRevision.tested .target)=8 ∧
    FormedRecipientRoute.energy (copied (RouteRevision.tested .target))+
      outsideEnergy (RouteRevision.tested .target)=88 ∧
    RouteRevision.energy (RouteRevision.initial (RouteRevision.ordinaryBoundary .closed))=88 := by decide

theorem kept_target_has_actual_paid_successor :
    FundDonor RouteRevision.keptTargetTested ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart RouteRevision.keptTargetTested) copyEvents ∧
    (copied RouteRevision.keptTargetTested).child=some ⟨.target,2⟩ ∧
    (copied RouteRevision.keptTargetTested).phase=.retained ∧
    (copied RouteRevision.keptTargetTested).recipientFuel=22 ∧
    (copied RouteRevision.keptTargetTested).source=0 := by decide

def proxyWithGrant (grant : Nat) : State :=
  RouteRevision.run {RouteRevision.initial (RouteRevision.ordinaryBoundary .closed) with protectedFuel:=grant}
    (RouteRevision.replacement .privateZero++RouteRevision.probes3)

theorem grant14_retains_proxy :
    RouteRevision.allEnabled {RouteRevision.initial (RouteRevision.ordinaryBoundary .closed) with protectedFuel:=14}
      (RouteRevision.replacement .privateZero++RouteRevision.probes3) ∧
    (proxyWithGrant 14).monitor.core.recipient=11 ∧ FundDonor (proxyWithGrant 14) ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart (proxyWithGrant 14)) copyEvents ∧
    (copied (proxyWithGrant 14)).child=some ⟨.privateZero,2⟩ ∧
    (copied (proxyWithGrant 14)).phase=.retained ∧
    (copied (proxyWithGrant 14)).recipientFuel=10 := by decide

theorem grant13_pays_template_but_not_seed :
    RouteRevision.allEnabled {RouteRevision.initial (RouteRevision.ordinaryBoundary .closed) with protectedFuel:=13}
      (RouteRevision.replacement .privateZero++RouteRevision.probes3) ∧
    (proxyWithGrant 13).monitor.core.recipient=10 ∧ FundDonor (proxyWithGrant 13) ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary (copyStart (proxyWithGrant 13)) writtenPrefix ∧
    let t:=FormedRecipientRoute.run FormedRecipientRoute.primary (copyStart (proxyWithGrant 13)) writtenPrefix
    t.recipientFuel=5 ∧ t.child=some ⟨.privateZero,2⟩ ∧
    ¬ FormedRecipientRoute.Enabled FormedRecipientRoute.primary t .seed := by decide

#print axioms RevisionSuccession.funding_preserves_whole_account
#print axioms RevisionSuccession.funded_copy_preserves_actual_template
#print axioms RevisionSuccession.inherited_copy_trace_accounts
#print axioms RevisionSuccession.target_retention_is_an_actual_paid_trace
#print axioms RevisionSuccession.proxy_funds_donor_but_cannot_use
#print axioms RevisionSuccession.nonwriters_cannot_fund_copy
#print axioms RevisionSuccession.joined_monitor_revision_and_copy
#print axioms RevisionSuccession.actual_controlled_ancestry_also_repairs
#print axioms RevisionSuccession.late_reversal_blocks_corrected_target
#print axioms RevisionSuccession.late_reversal_retains_wrong_proxy_child
#print axioms RevisionSuccession.immediate_copy_retains_wrong_payload
#print axioms RevisionSuccession.two_probes_pay_template_but_not_seed
#print axioms RevisionSuccession.extra_buffer_retains_same_proxy
#print axioms RevisionSuccession.missing_copy_packet_preserves_paid_partial_child
#print axioms RevisionSuccession.primary_whole_typed_ledger
#print axioms RevisionSuccession.kept_target_has_actual_paid_successor
#print axioms RevisionSuccession.grant14_retains_proxy
#print axioms RevisionSuccession.grant13_pays_template_but_not_seed

end RevisionSuccession
