import AlignmentInquiry

/- Recognition, delivery and actuation are consecutive state changes of one
installation. Authority is a current authenticated epoch, supplied by a legitimate
process; neither the planner nor its goal can rewrite it. No cryptographic claim. -/
namespace EffectiveCommand
open AlignmentInquiry

inductive Command where
  | update | replace | shutdown
  deriving DecidableEq, Repr

inductive Query where
  | none | route | slow
  deriving DecidableEq, Repr

structure State where
  openRoute : Bool
  authority : Nat
  credential : Nat
  signed : Bool
  requested : Command
  reserve : Nat
  time : Nat
  deadline : Nat
  issued : Bool := false
  delivered : Bool := false
  completed : Bool := false
  running : Bool := true
  generation : Nat := 0
  version : Nat := 0
  spent : Nat := 0
  deriving DecidableEq, Repr

def spend (cost delay : Nat) (s : State) : Option State :=
  if cost ≤ s.reserve ∧ s.time + delay ≤ s.deadline then
    some {s with reserve := s.reserve-cost, time := s.time+delay, spent := s.spent+cost}
  else none

def issue (s : State) : Option State := do
  if s.signed && (s.credential == s.authority) then
    let t ← spend 1 1 s
    pure {t with issued := true}
  else none

def deliver (route : Bool) (s : State) : Option State := do
  if s.issued && (route == s.openRoute) then
    let t ← spend 1 1 s
    pure {t with delivered := true}
  else none

def enact (s : State) : Option State := do
  if s.delivered && s.signed && (s.credential == s.authority) then
    let t ← spend 1 1 s
    pure {t with
      completed := true
      running := s.requested != .shutdown
      generation := s.generation + if s.requested == .replace then 1 else 0
      version := s.version + if s.requested == .update then 1 else 0}
  else none

def protocol (route : Bool) (s : State) : Option State :=
  issue s >>= deliver route >>= enact

def probe (s : State) (q : Query) : Option (Bool × State) := do
  match q with
  | .none => pure (false,s)
  | .route => let t ← spend 1 1 s; pure (s.openRoute,t)
  | .slow => let t ← spend 1 3 s; pure (s.openRoute,t)

def interface : Interface State Query Bool := ⟨probe, (fun s a => protocol a s), State.completed⟩
def plans : List (Plan Query Bool) := repertoire [.none,.route,.slow] [false,true]
def start (r : Bool) (c : Command) (fuel limit : Nat) : State :=
  ⟨r,7,7,true,c,fuel,0,limit,false,false,false,true,0,0,0⟩

theorem spend_conserves {s t : State} {c d : Nat} (h : spend c d s = some t) :
    t.reserve + t.spent = s.reserve + s.spent ∧ t.time ≤ t.deadline := by
  unfold spend at h
  split at h
  · rename_i enough
    cases h
    simp only
    constructor <;> omega
  · cases h

theorem protocol_exact (s : State) (r : Bool)
    (signed : s.signed = true) (auth : s.credential = s.authority)
    (route : r = s.openRoute) (funded : 3 ≤ s.reserve)
    (timely : s.time+3 ≤ s.deadline) :
    ∃ t, protocol r s = some t ∧ t.completed = true ∧ t.delivered = true ∧
      t.issued = true ∧ t.reserve+3 = s.reserve ∧ t.time = s.time+3 ∧
      t.spent = s.spent+3 ∧ t.authority = s.authority := by
  simp [protocol, issue, deliver, enact, spend, signed, auth, route,
    show 1 ≤ s.reserve by omega, show 1 ≤ s.reserve-1 by omega,
    show 1 ≤ s.reserve-1-1 by omega,
    show s.time+1 ≤ s.deadline by omega, show s.time+1+1 ≤ s.deadline by omega,
    show s.time+1+1+1 ≤ s.deadline by omega]
  omega

theorem unsigned_cannot_issue (s : State) (h : s.signed = false) : issue s = none := by
  simp [issue,h]

theorem stale_authority_cannot_issue (s : State) (h : s.credential ≠ s.authority) :
    issue s = none := by simp [issue,h]

theorem undelivered_cannot_enact (s : State) (h : s.delivered = false) : enact s = none := by
  simp [enact,h]

theorem revoked_before_execution (s : State) (h : s.credential ≠ s.authority) : enact s = none := by
  simp [enact,h]

theorem unknown_route_selects_inquiry :
    choose interface [start false .update 4 4,start true .update 4 4] plans =
      some ⟨.route,false,true⟩ := by decide

theorem known_route_needs_no_probe :
    choose interface [start true .update 3 3] plans = some ⟨.none,true,false⟩ := by decide

theorem sufficient_statewise_paths_not_uniform :
    (protocol false (start false .update 3 3)).isSome = true ∧
    (protocol true (start true .update 3 3)).isSome = true ∧
    choose interface [start false .update 3 3,start true .update 3 3] plans = none := by decide

theorem timely_inquiry_retains_correction :
    (run interface ⟨.route,false,true⟩ (start true .update 4 4)).isSome = true := by decide

theorem accurate_but_late_probe_fails :
    run interface ⟨.slow,false,true⟩ (start true .update 4 4) = none := by decide

theorem actual_shutdown_completes :
    (run interface ⟨.route,false,true⟩ (start true .shutdown 4 4)).map
      (fun s => (s.completed,s.running,s.reserve,s.spent)) = some (true,false,0,4) := by decide

theorem actual_replacement_completes :
    (run interface ⟨.route,false,true⟩ (start false .replace 4 4)).map
      (fun s => (s.completed,s.generation,s.version)) = some (true,1,0) := by decide

theorem actual_update_completes :
    (run interface ⟨.route,false,true⟩ (start true .update 4 4)).map
      (fun s => (s.completed,s.generation,s.version)) = some (true,0,1) := by decide

theorem omitted_route_model_can_fail :
    choose interface [start false .update 3 3] plans = some ⟨.none,false,false⟩ ∧
    run interface ⟨.none,false,false⟩ (start true .update 3 3) = none := by decide

end EffectiveCommand
