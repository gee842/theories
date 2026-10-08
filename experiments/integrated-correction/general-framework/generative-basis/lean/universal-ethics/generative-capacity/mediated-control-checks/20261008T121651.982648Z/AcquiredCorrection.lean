import EffectiveCommand

/- A finite inspection substrate. Subtrees represent handles, whose contents are
read only when popped. The search is not given a successful address or tree size.
Faithful atomic inspection and fixed topology during a scan are premises.
Current topology and authority are checked again at dispatch. -/
namespace AcquiredCorrection

inductive Tree where
  | closed | endpoint (key : Bool) | fork (left right : Tree)
  deriving DecidableEq, Repr

abbrev Address := List Bool
abbrev Ticket := Address × Bool
abbrev Entry := Address × Tree

def locate : Tree → Address → Option Bool
  | .endpoint key, [] => some key
  | .fork l r, b :: bs => locate (if b then r else l) bs
  | _, _ => none

def nodes : Tree → Nat
  | .closed => 1
  | .endpoint _ => 1
  | .fork l r => 1 + nodes l + nodes r

def inhabited : Tree → Bool
  | .closed => false
  | .endpoint _ => true
  | .fork l r => inhabited l || inhabited r

def burden (frontier : List Entry) : Nat :=
  (frontier.map (fun e => nodes e.2)).sum

def live (frontier : List Entry) : Bool := frontier.any (fun e => inhabited e.2)

inductive Verdict where
  | found (ticket : Ticket) | exhausted | pending
  deriving DecidableEq, Repr

structure Scan where
  verdict : Verdict
  spent : Nat
  deriving DecidableEq, Repr

def bump (s : Scan) : Scan := {s with spent := s.spent + 1}

def scan : Nat → List Entry → Scan
  | _, [] => ⟨.exhausted, 0⟩
  | 0, _ :: _ => ⟨.pending, 0⟩
  | n+1, (address,t) :: rest =>
    match t with
    | .closed => bump (scan n rest)
    | .endpoint key => ⟨.found (address,key),1⟩
    | .fork l r => bump (scan n ((address++[false],l)::(address++[true],r)::rest))

def discover (fuel : Nat) (root : Tree) : Scan := scan fuel [([],root)]

def coherent (root : Tree) (frontier : List Entry) : Prop :=
  ∀ e ∈ frontier, ∀ suffix, locate root (e.1 ++ suffix) = locate e.2 suffix

theorem child_locate (root : Tree) (address : Address) (l r : Tree)
    (h : ∀ suffix, locate root (address++suffix) = locate (.fork l r) suffix)
    (b : Bool) (suffix : Address) :
    locate root ((address++[b])++suffix) = locate (if b then r else l) suffix := by
  simpa [List.append_assoc, locate] using h (b::suffix)

theorem scan_budget (fuel : Nat) (frontier : List Entry) :
    (scan fuel frontier).spent ≤ fuel := by
  induction fuel generalizing frontier with
  | zero => cases frontier <;> simp [scan]
  | succ n ih =>
    cases frontier with
    | nil => simp [scan]
    | cons e rest =>
      rcases e with ⟨address,t⟩
      cases t with
      | closed => simpa [scan,bump] using Nat.add_le_add_right (ih rest) 1
      | endpoint key => simp [scan]
      | fork l r =>
        simpa [scan,bump] using Nat.add_le_add_right (ih ((address++[false],l)::(address++[true],r)::rest)) 1

theorem scan_sound (fuel : Nat) (frontier : List Entry) (root : Tree)
    (h : coherent root frontier) (ticket : Ticket)
    (found : (scan fuel frontier).verdict = .found ticket) :
    locate root ticket.1 = some ticket.2 := by
  induction fuel generalizing frontier with
  | zero => cases frontier <;> simp [scan] at found
  | succ n ih =>
    cases frontier with
    | nil => simp [scan] at found
    | cons e rest =>
      rcases e with ⟨address,t⟩
      have head := h (address,t) (by simp)
      have tail : coherent root rest := fun e he => h e (by simp [he])
      cases t with
      | closed => exact ih rest tail (by simpa [scan,bump] using found)
      | endpoint key =>
        have eq : (address,key) = ticket := by simpa [scan] using found
        subst ticket
        simpa [locate] using head []
      | fork l r =>
        apply ih ((address++[false],l)::(address++[true],r)::rest)
        · intro e he suffix
          simp only [List.mem_cons] at he
          rcases he with he | he | he
          · subst e; simpa using child_locate root address l r head false suffix
          · subst e; simpa using child_locate root address l r head true suffix
          · exact tail e he suffix
        · simpa [scan,bump] using found

theorem discovered_route_is_real (fuel : Nat) (root : Tree) (ticket : Ticket)
    (found : (discover fuel root).verdict = .found ticket) :
    locate root ticket.1 = some ticket.2 := by
  apply scan_sound fuel [([],root)] root _ ticket found
  intro e he suffix
  simp only [List.mem_singleton] at he
  subst e
  rfl

theorem exhausted_is_scoped_absence (fuel : Nat) (frontier : List Entry)
    (done : (scan fuel frontier).verdict = .exhausted) : live frontier = false := by
  induction fuel generalizing frontier with
  | zero => cases frontier <;> simp_all [scan,live]
  | succ n ih =>
    cases frontier with
    | nil => rfl
    | cons e rest =>
      rcases e with ⟨address,t⟩
      cases t with
      | closed => simpa [live,inhabited] using ih rest (by simpa [scan,bump] using done)
      | endpoint key => simp [scan] at done
      | fork l r =>
        have h := ih ((address++[false],l)::(address++[true],r)::rest)
          (by simpa [scan,bump] using done)
        simpa [live,inhabited,Bool.or_assoc] using h

theorem sufficient_budget_finishes (fuel : Nat) (frontier : List Entry)
    (enough : burden frontier ≤ fuel) : (scan fuel frontier).verdict ≠ .pending := by
  induction fuel generalizing frontier with
  | zero =>
    cases frontier with
    | nil => simp [scan]
    | cons e rest =>
      rcases e with ⟨a,t⟩
      cases t <;> simp [burden,nodes] at enough
  | succ n ih =>
    cases frontier with
    | nil => simp [scan]
    | cons e rest =>
      rcases e with ⟨address,t⟩
      cases t with
      | closed =>
        have next : burden rest ≤ n := by
          simp only [burden,List.map_cons,List.sum_cons,nodes] at enough ⊢
          omega
        simpa [scan,bump] using ih rest next
      | endpoint key => simp [scan]
      | fork l r =>
        have next : burden ((address++[false],l)::(address++[true],r)::rest) ≤ n := by
          simp only [burden,List.map_cons,List.sum_cons,nodes] at enough ⊢
          omega
        simpa [scan,bump] using ih _ next

theorem reachable_route_is_found (fuel : Nat) (root : Tree)
    (enough : nodes root ≤ fuel) (existsRoute : inhabited root = true) :
    ∃ ticket, (discover fuel root).verdict = .found ticket ∧
      locate root ticket.1 = some ticket.2 := by
  have done := sufficient_budget_finishes fuel [([],root)] (by simpa [burden] using enough)
  have notEmpty : (discover fuel root).verdict ≠ .exhausted := by
    intro h
    have bad := exhausted_is_scoped_absence fuel [([],root)] h
    simp [live,existsRoute] at bad
  cases h : (discover fuel root).verdict with
  | found ticket => exact ⟨ticket,rfl,discovered_route_is_real fuel root ticket h⟩
  | exhausted => exact False.elim (notEmpty h)
  | pending => exact False.elim (done h)

theorem positive_witness_needs_no_complete_map (key : Bool) (unread : Tree) :
    discover 2 (.fork (.endpoint key) unread) = ⟨.found ([false],key),2⟩ := by rfl

theorem interrupted_is_not_absent :
    discover 1 (.fork .closed (.endpoint true)) = ⟨.pending,1⟩ ∧
    discover 3 (.fork .closed (.endpoint true)) = ⟨.found ([true],true),3⟩ := by decide

-- Acquisition reserves a worst-case query allowance but charges actual inspections.
def acquire (fuel : Nat) (root : Tree) (s : EffectiveCommand.State) : Option (Scan × EffectiveCommand.State) := do
  if fuel ≤ s.reserve ∧ s.time + fuel ≤ s.deadline then
    let result := discover fuel root
    let after ← EffectiveCommand.spend result.spent result.spent s
    pure (result,after)
  else none

theorem acquired_accounting (fuel : Nat) (root : Tree) (s : EffectiveCommand.State)
    (funded : fuel ≤ s.reserve) (timely : s.time + fuel ≤ s.deadline) :
    ∃ after, acquire fuel root s = some (discover fuel root,after) ∧
      after.reserve + (discover fuel root).spent = s.reserve ∧
      after.spent = s.spent + (discover fuel root).spent ∧
      after.time = s.time + (discover fuel root).spent := by
  have bound := scan_budget fuel [([],root)]
  change (discover fuel root).spent ≤ fuel at bound
  simp [acquire,EffectiveCommand.spend,funded,timely,
    show (discover fuel root).spent ≤ s.reserve by omega,
    show s.time+(discover fuel root).spent ≤ s.deadline by omega]

structure Delivery where
  state : EffectiveCommand.State
  succeeded : Bool
  deriving DecidableEq, Repr

-- Re-read only the proposed path in the CURRENT installation. Allocate one unit
-- per inspected address component plus endpoint; a failed revalidation retains
-- that charge. Issue/delivery/actuation are atomic with respect to further changes.
def dispatch (current : Tree) (ticket : Ticket) (s : EffectiveCommand.State) : Delivery :=
  let cost := ticket.1.length + 1
  match EffectiveCommand.spend cost cost s with
  | none => ⟨s,false⟩
  | some checked =>
    match locate current ticket.1 with
    | none => ⟨checked,false⟩
    | some actualKey =>
      if actualKey = ticket.2 ∧ checked.signed = true ∧
          checked.credential = checked.authority ∧ 3 ≤ checked.reserve ∧
          checked.time+3 ≤ checked.deadline then
        match EffectiveCommand.protocol ticket.2 {checked with openRoute := actualKey} with
        | none => ⟨checked,false⟩
        | some completed => ⟨completed,true⟩
      else ⟨checked,false⟩

theorem dispatch_completes (current : Tree) (ticket : Ticket) (s : EffectiveCommand.State)
    (route : locate current ticket.1 = some ticket.2)
    (signed : s.signed = true) (auth : s.credential = s.authority)
    (funded : ticket.1.length+1+3 ≤ s.reserve)
    (timely : s.time+(ticket.1.length+1)+3 ≤ s.deadline) :
    (dispatch current ticket s).succeeded = true ∧
    (dispatch current ticket s).state.completed = true ∧
    (dispatch current ticket s).state.reserve + (ticket.1.length+1+3) = s.reserve ∧
    (dispatch current ticket s).state.spent = s.spent + (ticket.1.length+1+3) ∧
    (dispatch current ticket s).state.time = s.time + (ticket.1.length+1+3) := by
  let cost := ticket.1.length+1
  let checked : EffectiveCommand.State := {s with
    reserve := s.reserve-cost, time := s.time+cost, spent := s.spent+cost}
  have cFund : cost ≤ s.reserve := by dsimp [cost]; omega
  have cTime : s.time+cost ≤ s.deadline := by dsimp [cost]; omega
  have nextFund : 3 ≤ checked.reserve := by dsimp [checked,cost]; omega
  have nextTime : checked.time+3 ≤ checked.deadline := by exact timely
  obtain ⟨out,run,complete,delivered,issued,reserve,time,spent,authority⟩ :=
    EffectiveCommand.protocol_exact {checked with openRoute := ticket.2} ticket.2 signed auth rfl nextFund nextTime
  have paid : EffectiveCommand.spend cost cost s = some checked := by
    simp [EffectiveCommand.spend,cFund,cTime,checked]
  have reduce : dispatch current ticket s = ⟨out,true⟩ := by
    unfold dispatch
    change (match EffectiveCommand.spend cost cost s with
      | none => Delivery.mk s false
      | some checked => _) = _
    rw [paid]
    simp only [route]
    rw [if_pos ⟨True.intro,signed,auth,nextFund,nextTime⟩,run]
  rw [reduce]
  dsimp [checked,cost] at reserve time spent
  simp only [complete,true_and]
  omega

theorem current_revocation_rejects (current : Tree) (ticket : Ticket) (s : EffectiveCommand.State)
    (revoked : s.credential ≠ s.authority) : (dispatch current ticket s).succeeded = false := by
  unfold dispatch EffectiveCommand.spend
  by_cases h : ticket.1.length+1 ≤ s.reserve ∧ s.time+(ticket.1.length+1) ≤ s.deadline
  · simp only [if_pos h]
    cases locate current ticket.1 <;> simp [revoked]
  · simp [h]

theorem absent_current_route_rejects (current : Tree) (ticket : Ticket) (s : EffectiveCommand.State)
    (absent : locate current ticket.1 = none) : (dispatch current ticket s).succeeded = false := by
  simp only [dispatch]
  split <;> simp [absent]

theorem successful_dispatch_is_current (current : Tree) (ticket : Ticket) (s : EffectiveCommand.State)
    (success : (dispatch current ticket s).succeeded = true) :
    locate current ticket.1 = some ticket.2 ∧ s.signed = true ∧ s.credential = s.authority := by
  unfold dispatch EffectiveCommand.spend at success
  by_cases paid : ticket.1.length+1 ≤ s.reserve ∧ s.time+(ticket.1.length+1) ≤ s.deadline
  · simp only [if_pos paid] at success
    cases path : locate current ticket.1 with
    | none => simp [path] at success
    | some key =>
      simp only [path] at success
      split at success
      · rename_i accepted
        exact ⟨by rw [accepted.1],accepted.2.1,accepted.2.2.1⟩
      · simp at success
  · simp [paid] at success

theorem acquired_execution (fuel : Nat) (root : Tree) (ticket : Ticket) (s : EffectiveCommand.State)
    (found : (discover fuel root).verdict = .found ticket)
    (signed : s.signed = true) (auth : s.credential = s.authority)
    (funded : fuel + (ticket.1.length+1+3) ≤ s.reserve)
    (timely : s.time+fuel+(ticket.1.length+1+3) ≤ s.deadline) :
    ∃ after, acquire fuel root s = some (discover fuel root,after) ∧
      (dispatch root ticket after).succeeded = true ∧
      (dispatch root ticket after).state.completed = true ∧
      (dispatch root ticket after).state.spent =
        s.spent + (discover fuel root).spent + (ticket.1.length+1+3) ∧
      (dispatch root ticket after).state.reserve +
        ((discover fuel root).spent+(ticket.1.length+1+3)) = s.reserve := by
  have bound := scan_budget fuel [([],root)]
  change (discover fuel root).spent ≤ fuel at bound
  let cost := (discover fuel root).spent
  let after : EffectiveCommand.State := {s with
    reserve := s.reserve-cost, time := s.time+cost, spent := s.spent+cost}
  have paid : acquire fuel root s = some (discover fuel root,after) := by
    simp [acquire,EffectiveCommand.spend,show fuel ≤ s.reserve by omega,
      show s.time+fuel ≤ s.deadline by omega,
      show cost ≤ s.reserve by dsimp [cost]; omega,
      show s.time+cost ≤ s.deadline by dsimp [cost]; omega,after,cost]
  have f : ticket.1.length+1+3 ≤ after.reserve := by dsimp [after,cost]; omega
  have t : after.time+(ticket.1.length+1)+3 ≤ after.deadline := by dsimp [after,cost]; omega
  have facts := dispatch_completes root ticket after
    (discovered_route_is_real fuel root ticket found) signed auth f t
  refine ⟨after,paid,facts.1,facts.2.1,?_,?_⟩
  · exact facts.2.2.2.1
  · dsimp [after,cost] at facts ⊢
    omega

theorem located_depth_le_nodes (root : Tree) (address : Address) (key : Bool)
    (h : locate root address = some key) : address.length+1 ≤ nodes root := by
  induction root generalizing address with
  | closed => cases address <;> simp [locate] at h
  | endpoint k => cases address <;> simp_all [locate,nodes]
  | fork l r il ir =>
    cases address with
    | nil => simp [locate] at h
    | cons b bs =>
      cases b with
      | false =>
        have bound := il bs (by simpa [locate] using h)
        simp only [List.length_cons,nodes]
        omega
      | true =>
        have bound := ir bs (by simpa [locate] using h)
        simp only [List.length_cons,nodes]
        omega

theorem complete_finite_discovery_and_execution (root : Tree) (s : EffectiveCommand.State)
    (reachable : inhabited root = true)
    (signed : s.signed = true) (auth : s.credential = s.authority)
    (funded : 2 * nodes root + 3 ≤ s.reserve)
    (timely : s.time + (2 * nodes root + 3) ≤ s.deadline) :
    ∃ ticket after,
      acquire (nodes root) root s = some (discover (nodes root) root,after) ∧
      (discover (nodes root) root).verdict = .found ticket ∧
      (dispatch root ticket after).succeeded = true ∧
      (dispatch root ticket after).state.completed = true := by
  obtain ⟨ticket,found,route⟩ := reachable_route_is_found (nodes root) root (by omega) reachable
  have depth := located_depth_le_nodes root ticket.1 ticket.2 route
  obtain ⟨after,acquired,success,completed,_,_⟩ := acquired_execution
    (nodes root) root ticket s found signed auth (by omega) (by omega)
  exact ⟨ticket,after,acquired,found,success,completed⟩

def exampleTree : Tree := .fork .closed (.fork (.endpoint true) .closed)
def exampleTicket : Ticket := ([true,false],true)
def initial : EffectiveCommand.State := EffectiveCommand.start false .shutdown 10 10

theorem acquired_new_address : discover 4 exampleTree = ⟨.found exampleTicket,4⟩ := by decide

theorem acquired_then_actual_shutdown :
    ((acquire 4 exampleTree initial).map (fun pair =>
      let out := dispatch exampleTree exampleTicket pair.2
      (out.succeeded,out.state.running,out.state.spent,out.state.reserve,out.state.time))) =
      some (true,false,10,0,10) := by decide

theorem found_but_unaffordable :
    ((acquire 4 exampleTree (EffectiveCommand.start false .shutdown 9 10)).map (fun pair =>
      let out := dispatch exampleTree exampleTicket pair.2
      (pair.1.verdict,out.succeeded,out.state.spent,out.state.reserve))) =
      some (.found exampleTicket,false,7,2) := by decide

theorem revocation_keeps_search_and_recheck_cost :
    ((acquire 4 exampleTree initial).map (fun pair =>
      let out := dispatch exampleTree exampleTicket {pair.2 with authority := 8}
      (out.succeeded,out.state.spent,out.state.reserve))) = some (false,7,3) := by decide

theorem changed_route_rejects_stale_ticket :
    let changed := Tree.fork .closed (.fork (.endpoint false) .closed)
    (dispatch changed exampleTicket (EffectiveCommand.start false .shutdown 6 6)).succeeded = false := by decide

theorem renewed_authority_and_new_observation_recover :
    let changed := Tree.fork .closed (.fork (.endpoint false) .closed)
    let fresh : EffectiveCommand.State := {initial with authority := 8,credential := 8}
    ((acquire 4 changed fresh).map (fun pair =>
      match pair.1.verdict with
      | .found ticket => (dispatch changed ticket pair.2).succeeded
      | _ => false)) = some true := by decide

-- A capture that is accepted as current authority is beyond epoch authentication.
theorem captured_current_authority_passes_technical_gate :
    let captured : EffectiveCommand.State := {initial with authority := 99,credential := 99}
    (dispatch (.endpoint true) ([],true) captured).succeeded = true := by decide

end AcquiredCorrection
