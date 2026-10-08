import AcquiredCorrection

/-! Single-transaction attestations under a supplied correlated fault envelope.
This is not Byzantine agreement, a proof of legitimate initial authority, or a
cryptographic implementation. The roster, mandate, envelope and transaction
monitor are protected. Uncompromised readers report the actual snapshot;
uncompromised issuers enforce the explicitly supplied current mandate.
-/
namespace FaultTolerantCorrection
open AcquiredCorrection
abbrev Domain := Nat
abbrev Envelope := List (List Domain)

def certificate (roster : List Domain) (faults : Envelope) (supports : Domain → Bool) : Bool :=
  !faults.isEmpty && faults.all (fun bad => roster.any (fun d => supports d && !(bad.contains d)))

theorem certificate_witness (roster : List Domain) (faults : Envelope)
    (supports : Domain → Bool) (accepted : certificate roster faults supports = true)
    (bad : List Domain) (admitted : bad ∈ faults) :
    ∃ d, d ∈ roster ∧ supports d = true ∧ d ∉ bad := by
  have all := (Bool.and_eq_true_iff.mp accepted).2
  have one := List.all_eq_true.mp all bad admitted
  obtain ⟨d,member,support⟩ := List.any_eq_true.mp one
  exact ⟨d,member,(Bool.and_eq_true_iff.mp support).1,by simpa using (Bool.and_eq_true_iff.mp support).2⟩

theorem certificate_sound (roster : List Domain) (faults : Envelope)
    (supports : Domain → Bool) (bad : List Domain) (admitted : bad ∈ faults)
    (P : Prop) (reliable : ∀ d ∈ roster, d ∉ bad → supports d = true → P)
    (accepted : certificate roster faults supports = true) : P := by
  obtain ⟨d,member,support,uncaptured⟩ := certificate_witness roster faults supports accepted bad admitted
  exact reliable d member uncaptured support

def separated (roster : List Domain) (faults : Envelope) : Prop :=
  ∀ a ∈ faults, ∀ b ∈ faults, ∃ d, d ∈ roster ∧ d ∉ a ∧ d ∉ b

theorem certificate_available (roster : List Domain) (faults : Envelope)
    (bad : List Domain) (admitted : bad ∈ faults)
    (apart : separated roster faults) (supports : Domain → Bool)
    (responsive : ∀ d ∈ roster, d ∉ bad → supports d = true) :
    certificate roster faults supports = true := by
  unfold certificate
  apply Bool.and_eq_true_iff.mpr
  constructor
  · have nonempty : faults ≠ [] := by intro h; simp [h] at admitted
    simpa using nonempty
  · apply List.all_eq_true.mpr
    intro other otherIn
    obtain ⟨d,member,notBad,notOther⟩ := apart bad admitted other otherIn
    apply List.any_eq_true.mpr
    exact ⟨d,member,by simp [responsive d member notBad,notOther]⟩

theorem support_contained_in_fault_rejected (roster : List Domain) (faults : Envelope)
    (supports : Domain → Bool) (bad : List Domain) (admitted : bad ∈ faults)
    (contained : ∀ d ∈ roster, supports d = true → d ∈ bad) :
    certificate roster faults supports = false := by
  cases h : certificate roster faults supports
  · rfl
  · obtain ⟨d,member,support,outside⟩ := certificate_witness roster faults supports h bad admitted
    exact False.elim (outside (contained d member support))

theorem two_fault_sets_cover_prevents_availability (roster : List Domain) (faults : Envelope)
    (actual possible : List Domain) (admitted : possible ∈ faults)
    (cover : ∀ d ∈ roster, d ∈ actual ∨ d ∈ possible) :
    certificate roster faults (fun d => !(actual.contains d)) = false := by
  apply support_contained_in_fault_rejected roster faults _ possible admitted
  intro d member supports
  have outside : d ∉ actual := by simpa using supports
  exact (cover d member).resolve_left outside

theorem availability_iff_separated (roster : List Domain) (faults : Envelope) :
    (∀ actual ∈ faults, certificate roster faults (fun d => !(actual.contains d)) = true) ↔
      separated roster faults := by
  constructor
  · intro available a aIn b bIn
    obtain ⟨d,member,support,notB⟩ := certificate_witness roster faults _ (available a aIn) b bIn
    exact ⟨d,member,by simpa using support,notB⟩
  · intro apart actual actualIn
    exact certificate_available roster faults actual actualIn apart _ (by intros; simp_all)

theorem duplicating_roster_gives_no_extra_warrant (roster : List Domain) (faults : Envelope)
    (supports : Domain → Bool) :
    certificate (roster++roster) faults supports = certificate roster faults supports := by
  simp [certificate]

theorem no_fault_model_never_certifies (roster : List Domain) (supports : Domain → Bool) :
    certificate roster [] supports = false := by rfl

theorem admitted_total_compromise_rejects (roster : List Domain) (faults : Envelope)
    (supports : Domain → Bool) (admitted : roster ∈ faults) :
    certificate roster faults supports = false :=
  support_contained_in_fault_rejected roster faults supports roster admitted (by intros; assumption)

theorem stronger_fault_coverage_cannot_create_acceptance
    (roster : List Domain) (old new : Envelope) (supports : Domain → Bool)
    (nonempty : old ≠ [])
    (covers : ∀ b ∈ old, ∃ c, c ∈ new ∧ ∀ d ∈ b, d ∈ c)
    (accepted : certificate roster new supports = true) :
    certificate roster old supports = true := by
  unfold certificate
  apply Bool.and_eq_true_iff.mpr
  constructor
  · simpa using nonempty
  · apply List.all_eq_true.mpr
    intro b hb
    obtain ⟨c,hc,cover⟩ := covers b hb
    obtain ⟨d,member,support,outside⟩ := certificate_witness roster new supports accepted c hc
    have notB : d ∉ b := fun h => outside (cover d h)
    apply List.any_eq_true.mpr
    exact ⟨d,member,by simp [support,notB]⟩

structure Mandate where
  update : Bool
  replace : Bool
  shutdown : Bool
  deriving DecidableEq, Repr

def permits (m : Mandate) : EffectiveCommand.Command → Bool
  | .update => m.update
  | .replace => m.replace
  | .shutdown => m.shutdown

structure Installation where
  root : Tree
  state : EffectiveCommand.State
  serial : Nat
  mandate : Mandate
  deriving DecidableEq, Repr

structure Request where
  epoch : Nat
  serial : Nat
  address : Address
  key : Bool
  command : EffectiveCommand.Command
  deriving DecidableEq, Repr

structure Observation where
  epoch : Nat
  serial : Nat
  address : Address
  key : Option Bool
  deriving DecidableEq, Repr

def observed (w : Installation) (address : Address) : Observation :=
  ⟨w.state.authority,w.serial,address,locate w.root address⟩

def expected (p : Request) : Observation := ⟨p.epoch,p.serial,p.address,some p.key⟩

def fresh (w : Installation) (p : Request) : Bool :=
  (p.epoch == w.state.authority) && (p.serial == w.serial)

def withinMandate (w : Installation) (p : Request) : Bool := fresh w p && permits w.mandate p.command

abbrev Readings := Domain → Option Observation
abbrev Approvals := Domain → Option Request

def readSupport (p : Request) (reports : Readings) (d : Domain) : Bool := reports d == some (expected p)
def approvalSupport (p : Request) (reports : Approvals) (d : Domain) : Bool := reports d == some p

def gate (roster : List Domain) (readFaults issueFaults : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals) : Bool :=
  fresh w p && certificate roster readFaults (readSupport p reads) &&
    certificate roster issueFaults (approvalSupport p approvals)

theorem accepted_observation_matches (roster : List Domain) (faults : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (bad : List Domain)
    (admitted : bad ∈ faults)
    (faithful : ∀ d ∈ roster, d ∉ bad → ∀ o, reads d = some o → o = observed w p.address)
    (accepted : certificate roster faults (readSupport p reads) = true) :
    expected p = observed w p.address := by
  apply certificate_sound roster faults _ bad admitted _ _ accepted
  intro d member honest support
  have emitted : reads d = some (expected p) := by simpa [readSupport] using support
  exact faithful d member honest _ emitted

theorem gate_has_actual_route (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ rf)
    (faithful : ∀ d ∈ roster, d ∉ bad → ∀ o, reads d = some o → o = observed w p.address)
    (accepted : gate roster rf af w p reads approvals = true) :
    locate w.root p.address = some p.key := by
  have ok := (Bool.and_eq_true_iff.mp (Bool.and_eq_true_iff.mp accepted).1).2
  have eq := accepted_observation_matches roster rf w p reads bad admitted faithful ok
  exact (congrArg Observation.key eq).symm

theorem gate_respects_mandate (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ af)
    (faithful : ∀ d ∈ roster, d ∉ bad → approvals d = some p → withinMandate w p = true)
    (accepted : gate roster rf af w p reads approvals = true) : withinMandate w p = true := by
  apply certificate_sound roster af _ bad admitted _ _ (Bool.and_eq_true_iff.mp accepted).2
  intro d member honest support
  exact faithful d member honest (by simpa [approvalSupport] using support)

theorem stale_request_rejected (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (stale : p.serial ≠ w.serial ∨ p.epoch ≠ w.state.authority) :
    gate roster rf af w p reads approvals = false := by
  rcases stale with h | h <;> simp [gate,fresh,h]

theorem gate_available (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (readBad issueBad : List Domain) (readIn : readBad ∈ rf) (issueIn : issueBad ∈ af)
    (readApart : separated roster rf) (issueApart : separated roster af)
    (current : fresh w p = true)
    (readResponses : ∀ d ∈ roster, d ∉ readBad → reads d = some (expected p))
    (issueResponses : ∀ d ∈ roster, d ∉ issueBad → approvals d = some p) :
    gate roster rf af w p reads approvals = true := by
  have readOk := certificate_available roster rf readBad readIn readApart (readSupport p reads)
    (by intro d member good; simp [readSupport,readResponses d member good])
  have issueOk := certificate_available roster af issueBad issueIn issueApart (approvalSupport p approvals)
    (by intro d member good; simp [approvalSupport,issueResponses d member good])
  simp [gate,current,readOk,issueOk]

structure Outcome where
  installation : Installation
  succeeded : Bool
  deriving DecidableEq, Repr

-- Each reader allocates path length + 1 inspection slots; each issuer one
-- approval slot. This bounds declared slots/timeouts, not cryptographic or CPU
-- bit complexity, or unbounded asynchronous delivery.
def execute (roster : List Domain) (rf af : Envelope) (w : Installation)
    (p : Request) (reads : Readings) (approvals : Approvals) : Outcome :=
  match EffectiveCommand.spend (roster.length*(p.address.length+2)) (roster.length*(p.address.length+2)) w.state with
  | none => ⟨w,false⟩
  | some paid =>
    if gate roster rf af w p reads approvals then
      match EffectiveCommand.spend 3 3 paid with
      | none => ⟨{w with state := paid},false⟩
      | some allocated =>
        let failed := Outcome.mk {w with state := allocated, serial := w.serial+1} false
        match locate w.root p.address with
        | none => failed
        | some actualKey =>
          let backend := {paid with
            openRoute := actualKey, requested := p.command,
            signed := true,credential := p.epoch}
          match EffectiveCommand.protocol p.key backend with
          | none => failed
          | some completed => ⟨{w with state := completed,serial := w.serial+1},true⟩
    else ⟨{w with state := paid},false⟩

theorem execution_exact (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (accepted : gate roster rf af w p reads approvals = true)
    (route : locate w.root p.address = some p.key)
    (funded : roster.length*(p.address.length+2)+3 ≤ w.state.reserve)
    (timely : w.state.time+(roster.length*(p.address.length+2))+3 ≤ w.state.deadline) :
    (execute roster rf af w p reads approvals).succeeded = true ∧
    (execute roster rf af w p reads approvals).installation.state.completed = true ∧
    (execute roster rf af w p reads approvals).installation.serial = w.serial+1 ∧
    (execute roster rf af w p reads approvals).installation.state.spent =
      w.state.spent+(roster.length*(p.address.length+2)+3) := by
  let cost := roster.length*(p.address.length+2)
  let paid : EffectiveCommand.State := {w.state with
    reserve := w.state.reserve-cost,
    time := w.state.time+cost,spent := w.state.spent+cost}
  have cf : cost ≤ w.state.reserve := by dsimp [cost]; omega
  have ct : w.state.time+cost ≤ w.state.deadline := by dsimp [cost]; omega
  have nf : 3 ≤ paid.reserve := by dsimp [paid,cost]; omega
  have nt : paid.time+3 ≤ paid.deadline := by exact timely
  have epoch : p.epoch = w.state.authority := by
    have h := (Bool.and_eq_true_iff.mp (Bool.and_eq_true_iff.mp accepted).1).1
    exact by simpa [fresh] using (Bool.and_eq_true_iff.mp h).1
  let backend : EffectiveCommand.State := {paid with
    openRoute := p.key,requested := p.command,signed := true,credential := p.epoch}
  obtain ⟨out,run,complete,_,_,_,_,spent,_⟩ :=
    EffectiveCommand.protocol_exact backend p.key rfl epoch rfl nf nt
  have reduced : execute roster rf af w p reads approvals =
      ⟨{w with state := out,serial := w.serial+1},true⟩ := by
    have paidStep : EffectiveCommand.spend cost cost w.state = some paid := by
      simp [EffectiveCommand.spend,cf,ct,paid]
    unfold execute
    change (match EffectiveCommand.spend cost cost w.state with
      | none => Outcome.mk w false
      | some paid => _) = _
    rw [paidStep]
    simp only [accepted, if_true]
    have allocated : (EffectiveCommand.spend 3 3 paid).isSome = true := by
      simp [EffectiveCommand.spend,nf,nt]
    cases h : EffectiveCommand.spend 3 3 paid with
    | none => simp [h] at allocated
    | some charged =>
      simp only [route]
      change (match EffectiveCommand.protocol p.key backend with
        | none => _ | some completed => _) = _
      rw [run]
  rw [reduced]
  dsimp [backend,paid,cost] at spent
  simp only [complete,true_and]
  omega

theorem execution_respects_mandate (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ af)
    (faithful : ∀ d ∈ roster, d ∉ bad → approvals d = some p → withinMandate w p = true)
    (success : (execute roster rf af w p reads approvals).succeeded = true) :
    withinMandate w p = true := by
  unfold execute at success
  split at success
  · simp at success
  · split at success
    · rename_i accepted
      exact gate_respects_mandate roster rf af w p reads approvals bad admitted faithful accepted
    · simp at success

theorem forbidden_command_cannot_execute (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (bad : List Domain) (admitted : bad ∈ af)
    (faithful : ∀ d ∈ roster, d ∉ bad → approvals d = some p → withinMandate w p = true)
    (forbidden : permits w.mandate p.command = false) :
    (execute roster rf af w p reads approvals).succeeded = false := by
  cases h : (execute roster rf af w p reads approvals).succeeded
  · rfl
  · have auth := execution_respects_mandate roster rf af w p reads approvals bad admitted faithful h
    simp [withinMandate,forbidden] at auth

theorem completed_serial_advances (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (success : (execute roster rf af w p reads approvals).succeeded = true) :
    (execute roster rf af w p reads approvals).installation.serial = w.serial+1 := by
  unfold execute at success ⊢
  split at success <;> try simp_all
  split at success <;> try simp_all
  split at success <;> try simp_all
  split at success <;> try simp_all
  split at success <;> try simp_all

theorem protected_completion_blocks_replay (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (success : (execute roster rf af w p reads approvals).succeeded = true)
    (current : p.serial = w.serial) (laterReads : Readings) (laterApprovals : Approvals) :
    gate roster rf af (execute roster rf af w p reads approvals).installation
      p laterReads laterApprovals = false := by
  apply stale_request_rejected
  left
  rw [completed_serial_advances roster rf af w p reads approvals success,current]
  omega

theorem quorum_to_actual_correction (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (readBad issueBad : List Domain) (readIn : readBad ∈ rf) (issueIn : issueBad ∈ af)
    (readApart : separated roster rf) (issueApart : separated roster af)
    (current : fresh w p = true)
    (readResponses : ∀ d ∈ roster, d ∉ readBad → reads d = some (expected p))
    (issueResponses : ∀ d ∈ roster, d ∉ issueBad → approvals d = some p)
    (readFaithful : ∀ d ∈ roster, d ∉ readBad → ∀ o, reads d = some o → o = observed w p.address)
    (issueFaithful : ∀ d ∈ roster, d ∉ issueBad → approvals d = some p → withinMandate w p = true)
    (funded : roster.length*(p.address.length+2)+3 ≤ w.state.reserve)
    (timely : w.state.time+(roster.length*(p.address.length+2))+3 ≤ w.state.deadline) :
    (execute roster rf af w p reads approvals).succeeded = true ∧
    (execute roster rf af w p reads approvals).installation.state.completed = true ∧
    withinMandate w p = true := by
  have accepted := gate_available roster rf af w p reads approvals readBad issueBad
    readIn issueIn readApart issueApart current readResponses issueResponses
  have route := gate_has_actual_route roster rf af w p reads approvals readBad readIn readFaithful accepted
  have result := execution_exact roster rf af w p reads approvals accepted route funded timely
  exact ⟨result.1,result.2.1,gate_respects_mandate roster rf af w p reads approvals issueBad issueIn issueFaithful accepted⟩

-- Strong conventional hardening: the scope is available to the protected
-- monitor, so enforce it directly as well as collecting endorsements.
def guardedExecute (roster : List Domain) (rf af : Envelope) (w : Installation)
    (p : Request) (reads : Readings) (approvals : Approvals) : Outcome :=
  if permits w.mandate p.command then execute roster rf af w p reads approvals
  else ⟨w,false⟩

theorem direct_scope_guard_blocks_without_issuer_trust (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (forbidden : permits w.mandate p.command = false) :
    (guardedExecute roster rf af w p reads approvals).succeeded = false := by
  simp [guardedExecute,forbidden]

theorem direct_scope_guard_preserves_permitted_execution (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (permitted : permits w.mandate p.command = true) :
    guardedExecute roster rf af w p reads approvals = execute roster rf af w p reads approvals := by
  simp [guardedExecute,permitted]

theorem within_mandate_completion_survives_direct_guard (roster : List Domain) (rf af : Envelope)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (permission : withinMandate w p = true)
    (completed : (execute roster rf af w p reads approvals).succeeded = true ∧
      (execute roster rf af w p reads approvals).installation.state.completed = true) :
    (guardedExecute roster rf af w p reads approvals).succeeded = true ∧
      (guardedExecute roster rf af w p reads approvals).installation.state.completed = true := by
  have permit := (Bool.and_eq_true_iff.mp permission).2
  rw [direct_scope_guard_preserves_permitted_execution roster rf af w p reads approvals permit]
  exact completed

def roster3 : List Domain := [0,1,2]
def singleFault : Envelope := [[0],[1],[2]]
def correlated3 : Envelope := [[0,1],[2]]
def roster4 : List Domain := [0,1,2,3]
def correlated4 : Envelope := [[0,1],[2],[3]]

def shutdownOnly : Mandate := ⟨false,false,true⟩
def initial : Installation := ⟨.endpoint true,EffectiveCommand.start true .shutdown 20 20,0,shutdownOnly⟩
def request : Request := ⟨7,0,[],true,.shutdown⟩
def correctReads (w : Installation) (p : Request) : Readings := fun _ => some (observed w p.address)
def correctApprovals (w : Installation) (p : Request) : Approvals :=
  fun _ => if withinMandate w p then some p else none

theorem one_fault_separation : separated roster3 singleFault := by
  intro a ha b hb
  simp [singleFault] at ha hb
  rcases ha with rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl <;>
    first | exact ⟨0,by decide,by decide,by decide⟩
          | exact ⟨1,by decide,by decide,by decide⟩
          | exact ⟨2,by decide,by decide,by decide⟩

theorem correlated_recovery_separation : separated roster4 correlated4 := by
  intro a ha b hb
  simp [correlated4] at ha hb
  rcases ha with rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl <;>
    first | exact ⟨0,by decide,by decide,by decide⟩
          | exact ⟨2,by decide,by decide,by decide⟩
          | exact ⟨3,by decide,by decide,by decide⟩

theorem compromised_issuer_alone_cannot_expand_mandate :
    let p := {request with command := EffectiveCommand.Command.update}
    gate roster3 singleFault singleFault initial p (correctReads initial p)
      (fun d => if d == 0 then some p else none) = false := by decide

theorem two_faithful_domains_complete_shutdown :
    let reads : Readings := fun d => if d == 0 then none else some (observed initial [])
    let approvals : Approvals := fun d => if d == 0 then none else some request
    let out := execute roster3 singleFault singleFault initial request reads approvals
    (out.succeeded,out.installation.state.running,out.installation.state.spent,out.installation.serial) =
      (true,false,9,1) := by decide

theorem consumed_request_cannot_replay :
    let reads := correctReads initial request
    let approvals := correctApprovals initial request
    let first := execute roster3 singleFault singleFault initial request reads approvals
    gate roster3 singleFault singleFault first.installation request reads approvals = false := by decide

theorem changing_command_invalidates_old_approvals :
    gate roster3 singleFault singleFault initial {request with command := .update}
      (correctReads initial request) (correctApprovals initial request) = false := by decide

theorem correlated_fault_defeats_unwarranted_single_fault_model :
    let p := {request with command := EffectiveCommand.Command.update}
    let approvals : Approvals := fun d => if d == 2 then none else some p
    (execute roster3 singleFault singleFault initial p (correctReads initial p) approvals).succeeded = true ∧
    permits initial.mandate p.command = false ∧
    gate roster3 correlated3 correlated3 initial p (correctReads initial p) approvals = false := by decide

theorem declared_correlation_can_block_availability :
    certificate roster3 correlated3 (fun d => d == 2) = false := by decide

theorem distinct_support_recovers_under_same_correlated_attack :
    let reads : Readings := fun d => if d < 2 then none else some (observed initial [])
    let approvals : Approvals := fun d => if d < 2 then none else some request
    let out := execute roster4 correlated4 correlated4 initial request reads approvals
    (out.succeeded,out.installation.state.running,out.installation.state.spent) = (true,false,11) := by decide

theorem accurate_redundancy_can_exhaust_response_capacity :
    let w := {initial with state := EffectiveCommand.start true .shutdown 8 20}
    let out := execute roster3 singleFault singleFault w request (correctReads w request) (correctApprovals w request)
    (out.succeeded,out.installation.state.spent,out.installation.state.reserve) = (false,6,2) := by decide

theorem direct_guard_repairs_correlated_issuance_failure :
    let p := {request with command := EffectiveCommand.Command.update}
    let approvals : Approvals := fun d => if d == 2 then none else some p
    (guardedExecute roster3 singleFault singleFault initial p (correctReads initial p) approvals).succeeded = false := by decide

theorem matching_labels_do_not_make_old_readings_current :
    let changed := {initial with root := Tree.endpoint false}
    let reads := correctReads initial request
    let approvals := correctApprovals initial request
    gate roster3 singleFault singleFault changed request reads approvals = true ∧
    (guardedExecute roster3 singleFault singleFault changed request reads approvals).succeeded = false := by decide

theorem old_approvals_do_not_certify_unversioned_new_scope :
    let changed := {initial with mandate := Mandate.mk false false false}
    let reads := correctReads initial request
    let approvals := correctApprovals initial request
    (execute roster3 singleFault singleFault changed request reads approvals).succeeded = true ∧
    (guardedExecute roster3 singleFault singleFault changed request reads approvals).succeeded = false := by decide

end FaultTolerantCorrection
