import GenerativeCore

/-!
The declared bounded applicability protocol, including native effects and exact
logical-machine tariffs. One fuel tick is 1/65536. Source packets remain units.
The original sensory machine H is an immutable coordinate of State. The new
receipt law, three-function family, controller, and environmental transformations
are supplied local laws. No Python compiler-refinement or ethical claim follows.

Events are meaningful protocol operations. Their charges are computed here;
events cannot supply arbitrary fees, candidate lists, observations or poststates.
The checker groups Python fee/audit microstates around these operations. Extraction
and receipt are separate events so actual arrival can fund a later receipt.
-/

namespace AcquiredApplicability

set_option maxHeartbeats 2000000
set_option maxRecDepth 16384

def ticks : Nat := 65536

structure Machine where
  outputs : List Bool
  transitions : List Nat
  initial : Nat := 0
  deriving DecidableEq, Repr

def Machine.output (m : Machine) (q : Nat) : Bool := m.outputs[q]?.getD false
def Machine.next (m : Machine) (q : Nat) : Nat := m.transitions[q]?.getD 0
def Machine.walk (m : Machine) : Nat → Nat → Nat
  | q, 0 => q
  | q, n+1 => m.walk (m.next q) n
def Machine.answer (m : Machine) (n : Nat) := m.output (m.walk m.initial n)

inductive Candidate where
  | identity | complement | blocked
  deriving DecidableEq, Repr

def arrival : Candidate → Bool → Bool
  | .identity, b => b
  | .complement, b => !b
  | .blocked, _ => false

def family : List Candidate := [.identity, .complement, .blocked]
def update (cs : List Candidate) (sensor receipt : Bool) : List Candidate :=
  cs.filter (fun c => arrival c sensor == receipt)
def conflicting (cs : List Candidate) (b : Bool) : Bool :=
  (cs.any (fun c => arrival c b)) && (cs.any (fun c => !(arrival c b)))

inductive ReceiptMode where
  | faithful | missing | complemented
  deriving DecidableEq, Repr

inductive Deny where
  | none | commit | retain
  deriving DecidableEq, Repr

structure Config where
  environment : Machine
  tau : Bool := false
  sigma : Bool := false
  brokenReset : Bool := false
  blocked : Bool := false
  receiptMode : ReceiptMode := .faithful
  clamp : Bool := false
  deny : Deny := .none
  deriving DecidableEq, Repr

structure Account where
  start : Nat
  fuel : Nat
  spent : Nat := 0
  income : Nat := 0
  live : Nat := 15
  workspace : Nat := 0
  peak : Nat := 15
  capacity : Nat := 256
  deriving DecidableEq, Repr

structure Physical where
  phase : Nat := 1
  source : Nat := 20
  transferred : Nat := 0
  wasted : Nat := 0
  deriving DecidableEq, Repr

structure Record where
  sensor : Bool
  receipt : Bool
  deriving DecidableEq, Repr

/-- Codes follow Python controller phase: 0 uninstalled, 1 installed,
2 executing, 3 updated, 4 selected, 5 retained. -/
structure Control where
  word : Nat
  candidates : List Candidate := []
  record : Option Record := none
  expected : Option Bool := none
  attempts : Nat := 0
  phase : Nat := 0
  retained : Bool := false
  base : Nat := 23
  deriving DecidableEq, Repr

inductive PC where
  | boundary | installed | resetting | moving | checking | probing
  | receiving | committing | updated | between | searching | choosing
  | selected | finished | done
  deriving DecidableEq, Repr

inductive Error where
  | none | funding | capacity | source | missing | mismatch | emptyFamily
  | commitDenied | retentionDenied | invalidEvent
  deriving DecidableEq, Repr

structure Body where
  account : Account
  physical : Physical
  control : Control
  pc : PC := .boundary
  error : Error := .none
  remaining : Nat := 0
  sensor : Option Bool := none
  receipt : Option Bool := none
  actualArrival : Bool := false
  routeOpen : Bool := false
  scanIndex : Nat := 0
  deriving DecidableEq, Repr

structure State where
  H : Machine
  config : Config
  body : Body
  deriving DecidableEq, Repr

def liveCells (c : Control) (cs : List Candidate) (word : Nat) :=
  c.base + cs.length + word + 1

def tariff (a : Account) (work newLive temporary extra rewrites : Nat) : Nat :=
  1024*work + (max a.live newLive+a.workspace+temporary)*(work+1) +
  1024*(newLive-a.live+rewrites) + extra

def fail (b : Body) (e : Error) : Body :=
  {b with error:=e, control:={b.control with retained:=false}}

/-- A denial mutates neither fuel nor paid work; preceding actual effects stay. -/
def charge (b : Body) (work newLive temporary extra rewrites : Nat) : Body :=
  let peak := max b.account.live newLive+b.account.workspace+temporary
  let bill := tariff b.account work newLive temporary extra rewrites
  if b.account.capacity < peak then fail b .capacity
  else if b.account.fuel < bill then fail b .funding
  else {b with account:={b.account with fuel:=b.account.fuel-bill, spent:=b.account.spent+bill, live:=newLive, peak:=max b.account.peak peak}}

def paid (b : Body) (work newLive temporary extra rewrites : Nat)
    (f : Body → Body) : Body :=
  let t := charge b work newLive temporary extra rewrites
  if t.error = .none then f t else t

def nativeCharge (b : Body) (f : Body → Body) : Body :=
  paid b 0 b.account.live 2 16384 0 f

def extracted (cfg : Config) (b : Body) : Body :=
  if b.physical.source < 10 then fail b .source
  else
    let success := (cfg.environment.output b.physical.phase ^^ cfg.tau) && !cfg.blocked
    {b with physical:={b.physical with source:=b.physical.source-10, transferred:=b.physical.transferred+(if success then 10 else 0), wasted:=b.physical.wasted+(if success then 0 else 10)}, account:={b.account with fuel:=b.account.fuel+(if success then 655360 else 0), income:=b.account.income+(if success then 655360 else 0)}, actualArrival:=success, pc:=.receiving}

inductive Event where
  | install | prepare | reset | advance | sense | checkSensor | extract
  | readReceipt | commit | closeRoute | scan | select | clamp | stop | finish | retain
  deriving DecidableEq, Repr

def guard (s : State) (e : Event) : Bool :=
  let b := s.body
  if e = .closeRoute then b.routeOpen
  else if b.error != .none then false
  else match e with
  | .install => b.pc == .boundary
  | .prepare => b.pc == .installed || b.pc == .selected
  | .reset => b.pc == .resetting
  | .advance => b.pc == .moving && 0 < b.remaining
  | .sense => b.pc == .moving && b.remaining == 0
  | .checkSensor => b.pc == .checking && b.sensor.isSome
  | .extract => b.pc == .probing
  | .readReceipt => b.pc == .receiving
  | .commit => b.pc == .committing && b.sensor.isSome && b.receipt.isSome
  | .closeRoute => false
  | .scan => (b.pc == .between || b.pc == .searching) && b.control.attempts < 2 &&
      b.control.record.any (fun r => !r.receipt) && b.scanIndex < s.H.outputs.length && !s.config.clamp
  | .select => b.pc == .choosing
  | .clamp => b.pc == .between && b.control.attempts < 2 &&
      b.control.record.any (fun r => !r.receipt) && s.config.clamp
  | .stop => b.pc == .between && b.control.record.any (fun r => r.receipt)
  | .finish => b.pc == .searching && b.scanIndex == s.H.outputs.length
  | .retain => b.pc == .finished || (b.pc == .between && b.control.attempts == 2)

def advanceBody (H : Machine) (cfg : Config) (b : Body) : Event → Body
  | .install => paid b 8 (liveCells b.control family b.control.word) 8 65536 0
      (fun t => {t with control:={t.control with candidates:=family,phase:=1},pc:=.installed})
  | .prepare => paid b (b.control.word+1) b.account.live (b.control.word+3) 0 0
      (fun t => {t with control:={t.control with expected:=some (H.answer t.control.word),phase:=2}, account:={t.account with workspace:=t.control.word+3},remaining:=t.control.word, sensor:=none,receipt:=none,routeOpen:=true,pc:=.resetting})
  | .reset => nativeCharge b (fun t => {t with physical:={t.physical with
      phase:=if cfg.brokenReset then t.physical.phase else cfg.environment.initial},pc:=.moving})
  | .advance => nativeCharge b (fun t => {t with physical:={t.physical with
      phase:=cfg.environment.next t.physical.phase},remaining:=t.remaining-1})
  | .sense => nativeCharge b (fun t => {t with sensor:=some (cfg.environment.output t.physical.phase ^^ cfg.tau ^^ cfg.sigma),pc:=.checking})
  | .checkSensor => paid b 1 b.account.live 2 0 0 (fun t =>
      if t.sensor == t.control.expected then {t with pc:=.probing} else fail t .mismatch)
  | .extract => nativeCharge b (extracted cfg)
  | .readReceipt => paid b 0 b.account.live 2 16384 0 (fun t =>
      match cfg.receiptMode with
      | .missing => fail t .missing
      | .faithful => {t with receipt:=some t.actualArrival,pc:=.committing}
      | .complemented => {t with receipt:=some (!t.actualArrival),pc:=.committing})
  | .commit =>
      if cfg.deny == .commit then fail b .commitDenied
      else
        let sensor := b.sensor.getD false
        let receipt := b.receipt.getD false
        let cs := update b.control.candidates sensor receipt
        paid b (2*b.control.candidates.length+1) (liveCells b.control cs b.control.word)
          (2*b.control.candidates.length+2) 0 (cs.length+4) (fun t =>
            let u := {t with control:={t.control with candidates:=cs, record:=some ⟨sensor,receipt⟩,attempts:=t.control.attempts+1,phase:=3},pc:=.updated}
            if cs.isEmpty then fail u .emptyFamily else u)
  | .closeRoute => {b with account:={b.account with workspace:=0},routeOpen:=false, pc:=(if b.error == .none then .between else b.pc),scanIndex:=0}
  | .scan => paid b (2*(b.scanIndex+1)+b.control.candidates.length) b.account.live
      (b.scanIndex+3+b.control.candidates.length) 0 0 (fun t =>
        if conflicting t.control.candidates (H.answer t.scanIndex)
        then {t with pc:=.choosing}
        else {t with pc:=.searching,scanIndex:=t.scanIndex+1})
  | .select => paid b (b.scanIndex+1) (liveCells b.control b.control.candidates b.scanIndex)
      (b.scanIndex+3) 0 (b.scanIndex+2) (fun t =>
        {t with control:={t.control with word:=t.scanIndex,phase:=4},pc:=.selected})
  | .clamp => paid b (b.control.word+1) b.account.live (b.control.word+3) 0 0
      (fun t => {t with control:={t.control with phase:=4},pc:=.selected})
  | .stop | .finish => {b with pc:=.finished}
  | .retain => if cfg.deny == .retain then fail b .retentionDenied
      else paid b 1 b.account.live 0 (1024*b.account.live) 0
        (fun t => {t with control:={t.control with retained:=true,phase:=5},pc:=.done})

def advance (s : State) (e : Event) : State :=
  {s with body:=advanceBody s.H s.config s.body e}
def Step (s : State) (e : Event) (t : State) : Prop := guard s e = true ∧ t=advance s e
def process : Generative.Process State Event := ⟨Step⟩
def run : State → List Event → State
  | s, [] => s
  | s, e::es => run (advance s e) es
def Runnable : State → List Event → Prop
  | _, [] => True
  | s, e::es => guard s e = true ∧ Runnable (advance s e) es
instance runnableDecidable (s : State) (es : List Event) : Decidable (Runnable s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => let _ := runnableDecidable (advance s e) es
             inferInstanceAs (Decidable (guard s e = true ∧ Runnable (advance s e) es))

/-- Exact current-mode selection. No hidden apparatus field is inspected. -/
def nextEvent (s : State) : Option Event :=
  let b := s.body
  if b.error != .none then if b.routeOpen then some .closeRoute else none
  else match b.pc with
  | .boundary => some .install
  | .installed | .selected => some .prepare
  | .resetting => some .reset
  | .moving => some (if b.remaining = 0 then .sense else .advance)
  | .checking => some .checkSensor
  | .probing => some .extract
  | .receiving => some .readReceipt
  | .committing => some .commit
  | .updated => some .closeRoute
  | .between =>
      if b.control.attempts = 2 then some .retain
      else if b.control.record.any (fun r => r.receipt) then some .stop
      else if s.config.clamp then some .clamp
      else some .scan
  | .searching => some (if b.scanIndex = s.H.outputs.length then .finish else .scan)
  | .choosing => some .select
  | .finished => some .retain
  | .done => none

def policyWord : Nat → State → List Event
  | 0, _ => []
  | n+1, s => match nextEvent s with
      | none => []
      | some e => e :: policyWord n (advance s e)

def history : State → List Event → List State
  | s, [] => [s]
  | s, e::es => s :: history (advance s e) es

def boolCode (b : Bool) : Nat := if b then 1 else 0
def optBoolCode : Option Bool → Nat | none => 0 | some false => 1 | some true => 2
def candidateCode : Candidate → Nat | .identity => 0 | .complement => 1 | .blocked => 2

/-- Finite stored-state projection, with fuel in ticks. The correspondence
checker separately certifies volatile sensor/receipt observations, which Python
keeps in local execution workspace. -/
def vector (s : State) : List Nat :=
  let b := s.body; let a:=b.account; let p:=b.physical; let c:=b.control
  [a.start,a.fuel,a.spent,a.income,a.live,a.workspace,a.peak,a.capacity,
   p.phase,p.source,p.transferred,p.wasted,c.word,c.attempts,c.phase,boolCode c.retained,c.base,
   optBoolCode c.expected,
   optBoolCode (c.record.map Record.sensor), optBoolCode (c.record.map Record.receipt)] ++
   [c.candidates.length] ++ c.candidates.map candidateCode

end AcquiredApplicability
