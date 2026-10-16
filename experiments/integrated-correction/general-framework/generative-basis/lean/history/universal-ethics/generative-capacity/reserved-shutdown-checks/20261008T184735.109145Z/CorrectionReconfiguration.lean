import FaultTolerantCorrection

/-! Causal fault formulas and atomic, funded reviewer reconfiguration.
Formulas are supplied engineering upper bounds, not discovered causal laws.
The protected monitor, authority to reorganize, and correspondence remain
premises. No network consensus, physical migration or ethical legitimacy
is derived from a passing check. -/
namespace CorrectionReconfiguration
open FaultTolerantCorrection

inductive FaultExpr where
  | cause : Nat → FaultExpr
  | any : FaultExpr → FaultExpr → FaultExpr
  | all : FaultExpr → FaultExpr → FaultExpr
  deriving DecidableEq, Repr

def fails : FaultExpr → List Nat → Bool
  | .cause r, roots => roots.contains r
  | .any a b, roots => fails a roots || fails b roots
  | .all a b, roots => fails a roots && fails b roots

def Subset (a b : List Nat) : Prop := ∀ r ∈ a, r ∈ b

theorem failure_monotone (e : FaultExpr) (a b : List Nat) (included : Subset a b)
    (failed : fails e a = true) : fails e b = true := by
  induction e with
  | cause r => simpa [fails] using included r (by simpa [fails] using failed)
  | any x y ihx ihy =>
      simp only [fails, Bool.or_eq_true] at failed ⊢
      exact failed.elim (fun h => Or.inl (ihx h)) (fun h => Or.inr (ihy h))
  | all x y ihx ihy =>
      simp only [fails, Bool.and_eq_true] at failed ⊢
      exact ⟨ihx failed.1, ihy failed.2⟩

theorem survives_subset (e : FaultExpr) (a b : List Nat) (included : Subset a b)
    (safe : fails e b = false) : fails e a = false := by
  cases h : fails e a
  · rfl
  · have := failure_monotone e a b included h
    simp [safe] at this

structure Arrangement where
  roster : List Domain
  vulnerability : Domain → FaultExpr
  rootFaults : List (List Nat)

def induced (a : Arrangement) (roots : List Nat) : List Domain :=
  a.roster.filter (fun d => fails (a.vulnerability d) roots)

def envelope (a : Arrangement) : Envelope := a.rootFaults.map (induced a)

def Covered (a : Arrangement) (actual : List Nat) : Prop :=
  ∃ bound, bound ∈ a.rootFaults ∧ Subset actual bound

theorem induced_membership (a : Arrangement) (roots : List Nat) (d : Domain) :
    d ∈ induced a roots ↔ d ∈ a.roster ∧ fails (a.vulnerability d) roots = true := by
  simp [induced]

theorem induced_monotone (a : Arrangement) (x y : List Nat) (h : Subset x y) :
    Subset (induced a x) (induced a y) := by
  intro d hd
  obtain ⟨member,failed⟩ := (induced_membership a x d).mp hd
  exact (induced_membership a y d).mpr ⟨member,failure_monotone _ x y h failed⟩

theorem outside_bound_survives (a : Arrangement) (actual bound : List Nat)
    (included : Subset actual bound) (d : Domain) (member : d ∈ a.roster)
    (outside : d ∉ induced a bound) : fails (a.vulnerability d) actual = false := by
  have h : fails (a.vulnerability d) bound = false := by
    cases hf : fails (a.vulnerability d) bound
    · rfl
    · exact False.elim (outside ((induced_membership a bound d).mpr ⟨member,hf⟩))
  exact survives_subset _ actual bound included h

theorem derived_certificate_sound (a : Arrangement) (actual : List Nat)
    (covered : Covered a actual) (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d ∈ a.roster, fails (a.vulnerability d) actual = false → supports d = true → P)
    (accepted : certificate a.roster (envelope a) supports = true) : P := by
  obtain ⟨bound,member,included⟩ := covered
  apply certificate_sound a.roster (envelope a) supports (induced a bound)
    (List.mem_map.mpr ⟨bound,member,rfl⟩) P _ accepted
  intro d hd outside supported
  exact faithful d hd (outside_bound_survives a actual bound included d hd outside) supported

def ready (a : Arrangement) : Bool :=
  !a.rootFaults.isEmpty && a.rootFaults.all (fun x => a.rootFaults.all (fun y =>
    a.roster.any (fun d => !(fails (a.vulnerability d) x) && !(fails (a.vulnerability d) y))))

theorem ready_separates (a : Arrangement) (h : ready a = true) :
    separated a.roster (envelope a) := by
  intro x hx y hy
  obtain ⟨rx,hrx,rfl⟩ := List.mem_map.mp hx
  obtain ⟨ry,hry,rfl⟩ := List.mem_map.mp hy
  have outer := (Bool.and_eq_true_iff.mp h).2
  have inner := List.all_eq_true.mp outer rx hrx
  have found := List.all_eq_true.mp inner ry hry
  obtain ⟨d,member,good⟩ := List.any_eq_true.mp found
  have good' : fails (a.vulnerability d) rx = false ∧ fails (a.vulnerability d) ry = false := by
    simpa using good
  exact ⟨d,member,by simp [induced,good'.1],by simp [induced,good'.2]⟩

theorem ready_iff_nonempty_separated (a : Arrangement) :
    ready a = true ↔ a.rootFaults ≠ [] ∧ separated a.roster (envelope a) := by
  constructor
  · intro h
    exact ⟨by simpa using (Bool.and_eq_true_iff.mp h).1,ready_separates a h⟩
  · rintro ⟨hne,sep⟩
    apply Bool.and_eq_true_iff.mpr
    constructor
    · simpa using hne
    · apply List.all_eq_true.mpr
      intro x hx
      apply List.all_eq_true.mpr
      intro y hy
      obtain ⟨d,hd,nx,ny⟩ := sep (induced a x) (List.mem_map.mpr ⟨x,hx,rfl⟩)
        (induced a y) (List.mem_map.mpr ⟨y,hy,rfl⟩)
      have fx := outside_bound_survives a x x (by intro r h; exact h) d hd nx
      have fy := outside_bound_survives a y y (by intro r h; exact h) d hd ny
      exact List.any_eq_true.mpr ⟨d,hd,by simp [fx,fy]⟩

theorem derived_certificate_available (a : Arrangement) (actual : List Nat)
    (covered : Covered a actual) (checked : ready a = true) (supports : Domain → Bool)
    (responsive : ∀ d ∈ a.roster, fails (a.vulnerability d) actual = false → supports d = true) :
    certificate a.roster (envelope a) supports = true := by
  obtain ⟨bound,member,included⟩ := covered
  apply certificate_available a.roster (envelope a) (induced a bound)
    (List.mem_map.mpr ⟨bound,member,rfl⟩) (ready_separates a checked) supports
  intro d hd outside
  exact responsive d hd (outside_bound_survives a actual bound included d hd outside)

theorem derived_actual_correction (a : Arrangement) (actual : List Nat)
    (covered : Covered a actual) (checked : ready a = true)
    (w : Installation) (p : Request) (reads : Readings) (approvals : Approvals)
    (current : fresh w p = true)
    (readResponses : ∀ d ∈ a.roster, fails (a.vulnerability d) actual = false → reads d = some (expected p))
    (issueResponses : ∀ d ∈ a.roster, fails (a.vulnerability d) actual = false → approvals d = some p)
    (readFaithful : ∀ d ∈ a.roster, fails (a.vulnerability d) actual = false →
      ∀ o, reads d = some o → o = observed w p.address)
    (issueFaithful : ∀ d ∈ a.roster, fails (a.vulnerability d) actual = false →
      approvals d = some p → withinMandate w p = true)
    (funded : a.roster.length*(p.address.length+2)+3 ≤ w.state.reserve)
    (timely : w.state.time+a.roster.length*(p.address.length+2)+3 ≤ w.state.deadline) :
    (guardedExecute a.roster (envelope a) (envelope a) w p reads approvals).succeeded = true ∧
    (guardedExecute a.roster (envelope a) (envelope a) w p reads approvals).installation.state.completed = true ∧
    withinMandate w p = true := by
  obtain ⟨bound,member,included⟩ := covered
  have admitted : induced a bound ∈ envelope a := List.mem_map.mpr ⟨bound,member,rfl⟩
  have safe := outside_bound_survives a actual bound included
  have h := quorum_to_actual_correction a.roster (envelope a) (envelope a) w p reads approvals
    (induced a bound) (induced a bound) admitted admitted (ready_separates a checked) (ready_separates a checked)
    current (fun d hd hn => readResponses d hd (safe d hd hn))
    (fun d hd hn => issueResponses d hd (safe d hd hn))
    (fun d hd hn => readFaithful d hd (safe d hd hn))
    (fun d hd hn => issueFaithful d hd (safe d hd hn)) funded timely
  have g := within_mandate_completion_survives_direct_guard a.roster (envelope a) (envelope a)
    w p reads approvals h.2.2 ⟨h.1,h.2.1⟩
  exact ⟨g.1,g.2,h.2.2⟩

structure Managed where
  arrangement : Arrangement
  installation : Installation

def responseCost (a : Arrangement) (depth : Nat) : Nat := a.roster.length*(depth+2)+3

-- Admission computation has no hidden claim of zero physical cost: cost is a
-- supplied reservation for review/installation; this is an atomic local model.
def reconfigure (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old : Managed) : Option Managed :=
  if authorized && ready candidate &&
      decide (cost+responseCost candidate depth ≤ old.installation.state.reserve) &&
      decide (old.installation.state.time+cost+responseCost candidate depth ≤ old.installation.state.deadline)
  then some ⟨candidate, { old.installation with
    state := { old.installation.state with
      authority := old.installation.state.authority+1
      signed := false
      issued := false
      delivered := false
      completed := false
      reserve := old.installation.state.reserve-cost
      time := old.installation.state.time+cost
      spent := old.installation.state.spent+cost }
    serial := old.installation.serial+1 }⟩
  else none

theorem admitted_configuration (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old next : Managed) (h : reconfigure authorized cost depth candidate old = some next) :
    authorized = true ∧ ready candidate = true ∧ next.arrangement = candidate ∧
    next.installation.mandate = old.installation.mandate ∧
    next.installation.root = old.installation.root ∧
    next.installation.state.authority = old.installation.state.authority+1 ∧
    next.installation.serial = old.installation.serial+1 ∧
    next.installation.state.signed = false ∧
    next.installation.state.spent = old.installation.state.spent+cost ∧
    next.installation.state.reserve+cost = old.installation.state.reserve ∧
    responseCost candidate depth ≤ next.installation.state.reserve ∧
    next.installation.state.time+responseCost candidate depth ≤ next.installation.state.deadline := by
  unfold reconfigure at h
  split at h
  · rename_i gate
    simp only [Bool.and_eq_true, decide_eq_true_eq] at gate
    have hcost : cost ≤ old.installation.state.reserve := by omega
    cases h
    exact ⟨gate.1.1.1,gate.1.1.2,rfl,rfl,rfl,rfl,rfl,rfl,rfl,by dsimp; omega,by dsimp; omega,gate.2⟩
  · simp at h

theorem reform_does_not_expand_mandate (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old next : Managed) (h : reconfigure authorized cost depth candidate old = some next)
    (command : EffectiveCommand.Command) :
    permits next.installation.mandate command = permits old.installation.mandate command := by
  rw [(admitted_configuration authorized cost depth candidate old next h).2.2.2.1]

theorem old_request_rejected_after_reform (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old next : Managed) (h : reconfigure authorized cost depth candidate old = some next)
    (p : Request) (oldEpoch : p.epoch = old.installation.state.authority) :
    fresh next.installation p = false := by
  have epoch := (admitted_configuration authorized cost depth candidate old next h).2.2.2.2.2.1
  have neq : p.epoch ≠ next.installation.state.authority := by omega
  simp [fresh,neq]

theorem admitted_budget_for_shorter_route (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old next : Managed) (h : reconfigure authorized cost depth candidate old = some next)
    (actualDepth : Nat) (within : actualDepth ≤ depth) :
    responseCost candidate actualDepth ≤ next.installation.state.reserve ∧
    next.installation.state.time+responseCost candidate actualDepth ≤ next.installation.state.deadline := by
  have admitted := admitted_configuration authorized cost depth candidate old next h
  have small : responseCost candidate actualDepth ≤ responseCost candidate depth := by
    unfold responseCost
    exact Nat.add_le_add_right (Nat.mul_le_mul_left _ (by omega)) _
  constructor <;> omega

theorem admitted_reform_completes (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old next : Managed) (installed : reconfigure authorized cost depth candidate old = some next)
    (actual : List Nat) (covered : Covered candidate actual)
    (p : Request) (reads : Readings) (approvals : Approvals)
    (depthBound : p.address.length ≤ depth) (current : fresh next.installation p = true)
    (readResponses : ∀ d ∈ candidate.roster, fails (candidate.vulnerability d) actual = false →
      reads d = some (expected p))
    (issueResponses : ∀ d ∈ candidate.roster, fails (candidate.vulnerability d) actual = false →
      approvals d = some p)
    (readFaithful : ∀ d ∈ candidate.roster, fails (candidate.vulnerability d) actual = false →
      ∀ o, reads d = some o → o = observed next.installation p.address)
    (issueFaithful : ∀ d ∈ candidate.roster, fails (candidate.vulnerability d) actual = false →
      approvals d = some p → withinMandate next.installation p = true) :
    (guardedExecute next.arrangement.roster (envelope next.arrangement) (envelope next.arrangement)
      next.installation p reads approvals).succeeded = true ∧
    (guardedExecute next.arrangement.roster (envelope next.arrangement) (envelope next.arrangement)
      next.installation p reads approvals).installation.state.completed = true ∧
    withinMandate next.installation p = true := by
  have admitted := admitted_configuration authorized cost depth candidate old next installed
  have funds := admitted_budget_for_shorter_route authorized cost depth candidate old next installed
    p.address.length depthBound
  rw [admitted.2.2.1]
  exact derived_actual_correction candidate actual covered admitted.2.1 next.installation p reads approvals
    current readResponses issueResponses readFaithful issueFaithful funds.1 funds.2

theorem unavailable_candidate_rejected (authorized : Bool) (cost depth : Nat) (candidate : Arrangement)
    (old : Managed) (unready : ready candidate = false) :
    reconfigure authorized cost depth candidate old = none := by simp [reconfigure,unready]

theorem unauthorized_reform_rejected (cost depth : Nat) (candidate : Arrangement) (old : Managed) :
    reconfigure false cost depth candidate old = none := by simp [reconfigure]

def separate3 : Arrangement := ⟨[0,1,2],FaultExpr.cause,[[0],[1],[2]]⟩
def merged3 : Arrangement := ⟨[0,1,2],fun d => .cause (if d < 2 then 0 else 2),[[0],[1],[2]]⟩
def repaired4 : Arrangement := ⟨[0,1,2,3],fun d => .cause (if d < 2 then 0 else d),[[0],[1],[2],[3]]⟩
def duplicated4 : Arrangement := ⟨[0,1,2,3],fun d => .cause (if d < 2 then 0 else 2),[[0],[2]]⟩
def original : Managed := ⟨separate3,initial⟩

theorem causal_envelopes_compute :
    envelope separate3 = [[0],[1],[2]] ∧
    envelope merged3 = [[0,1],[],[2]] ∧
    envelope repaired4 = [[0,1],[],[2],[3]] := by decide

theorem causal_readiness_changes :
    ready separate3 = true ∧ ready merged3 = false ∧
    ready repaired4 = true ∧ ready duplicated4 = false := by decide

theorem renamed_support_is_not_redundancy :
    fails (.all (.cause 0) (.cause 0)) [0] = true ∧
    fails (.all (.cause 0) (.cause 1)) [0] = false ∧
    fails (.any (.cause 0) (.cause 1)) [0] = true := by decide

theorem stale_envelope_accepts_captured_support :
    certificate merged3.roster (envelope separate3) (fun d => d < 2) = true ∧
    certificate merged3.roster (envelope merged3) (fun d => d < 2) = false := by decide

theorem reform_rejects_shared_control : reconfigure true 2 0 merged3 original = none := by decide

def renewed : Managed :=
  (reconfigure true 2 0 repaired4 original).getD original

def renewedRequest : Request := ⟨8,1,[],true,.shutdown⟩
def survivingReads : Readings := fun d => if d < 2 then none else some (observed renewed.installation [])
def survivingApprovals : Approvals := fun d => if d < 2 then none else some renewedRequest

theorem repaired_reform_installs :
    (reconfigure true 2 0 repaired4 original).isSome = true ∧
    renewed.installation.state.reserve = 18 ∧ renewed.installation.state.spent = 2 ∧
    renewed.installation.state.authority = 8 ∧ renewed.installation.serial = 1 := by decide

theorem repaired_reform_completes_correction :
    let result := guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
      renewed.installation renewedRequest survivingReads survivingApprovals
    result.succeeded = true ∧ result.installation.state.running = false ∧
    result.installation.state.spent = 13 ∧ result.installation.state.reserve = 7 ∧
    result.installation.serial = 2 := by decide

theorem old_approvals_fail_after_reform :
    gate repaired4.roster (envelope repaired4) (envelope repaired4) renewed.installation request
      (correctReads initial request) (correctApprovals initial request) = false := by decide

theorem review_alone_funded_is_not_enough :
    let limited : Managed := ⟨separate3,{initial with state := {initial.state with reserve := 12}}⟩
    (2 ≤ limited.installation.state.reserve) ∧ reconfigure true 2 0 repaired4 limited = none := by decide

theorem exact_combined_budget_suffices :
    let limited : Managed := ⟨separate3,{initial with state := {initial.state with reserve := 13,deadline := 13}}⟩
    (reconfigure true 2 0 repaired4 limited).isSome = true := by decide

theorem omitted_shared_cause_still_breaks_model :
    let omitted : Arrangement := ⟨[0,1,2],fun d => .any (.cause d) (.cause 9),[[0],[1],[2]]⟩
    ready omitted = true ∧ induced omitted [9] = [0,1,2] := by decide

end CorrectionReconfiguration
