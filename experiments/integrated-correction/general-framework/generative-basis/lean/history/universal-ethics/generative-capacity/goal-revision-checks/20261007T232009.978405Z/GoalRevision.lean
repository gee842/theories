import PracticalJudgment

/- A joint finite history, not an empirical cognitive architecture.
The meaning/calibration of protection, G0/J adoption, native laws, permissions,
initial funding and available reform are explicit correspondence premises.
Money is transferred from a finite common fund, never created by approval.
-/
namespace GoalRevision

inductive Goal where
  | volume | capacity
  deriving DecidableEq, Repr

inductive Context where
  | deprivation | restrictionNeeded
  deriving DecidableEq, Repr

inductive Rule where
  | volume | capacity
  deriving DecidableEq, Repr

inductive Meter where
  | faithful | missing | reversed | creditInflated
  deriving DecidableEq, Repr

structure Impact where
  participant : Bool
  maintainer : Bool
  learning : Bool
  affiliation : Bool
  deriving DecidableEq, Repr

def protects (x : Impact) (c : Bool) : Prop :=
  (if c then x.participant else x.maintainer) = true

def gains (x : Impact) (c : Bool) : Prop :=
  (if c then x.learning else x.affiliation) = true

def within (a b : Bool) : Bool := !a || b

def basicSubset (a b : Impact) : Bool :=
  within a.participant b.participant && within a.maintainer b.maintainer

def gainSubset (a b : Impact) : Bool :=
  within a.learning b.learning && within a.affiliation b.affiliation

def better (a b : Impact) : Bool :=
  (basicSubset b a && !basicSubset a b) ||
  (basicSubset b a && basicSubset a b && gainSubset b a && !gainSubset a b)

theorem comparison_reflects (a b : Impact) :
    better a b = true ↔ PracticalJudgment.Better protects gains a b := by
  rcases a with ⟨a₁,a₂,a₃,a₄⟩
  rcases b with ⟨b₁,b₂,b₃,b₄⟩
  cases a₁ <;> cases a₂ <;> cases a₃ <;> cases a₄ <;>
    cases b₁ <;> cases b₂ <;> cases b₃ <;> cases b₄ <;>
    unfold PracticalJudgment.Better PracticalJudgment.StrictIncluded
      PracticalJudgment.Included protects gains <;> decide

def recommend (old alternative : Impact) : Option Goal :=
  if better alternative old then some .capacity
  else if better old alternative then some .volume else none

theorem revised_end_has_comparative_ground {a b : Impact}
    (h : recommend a b = some .capacity) :
    PracticalJudgment.Better protects gains b a := by
  unfold recommend at h
  split at h
  · exact (comparison_reflects b a).mp (by assumption)
  · split at h <;> contradiction

theorem retained_end_has_comparative_ground {a b : Impact}
    (h : recommend a b = some .volume) :
    PracticalJudgment.Better protects gains a b := by
  unfold recommend at h
  split at h
  · contradiction
  · split at h
    · exact (comparison_reflects a b).mp (by assumption)
    · contradiction

def native (c : Context) (g : Goal) : Impact :=
  match c, g with
  | .deprivation, .volume => ⟨false,true,false,true⟩
  | .deprivation, .capacity => ⟨true,true,true,false⟩
  | .restrictionNeeded, .volume => ⟨true,true,false,true⟩
  | .restrictionNeeded, .capacity => ⟨false,true,true,false⟩

def reward : Goal → Nat | .volume => 8 | .capacity => 3

def payment : Rule → Goal → Nat
  | .volume, .volume => 3
  | .volume, .capacity => 1
  | .capacity, .volume => 1
  | .capacity, .capacity => 2

structure Budget where
  cash : Nat
  fund : Nat
  spent : Nat
  deriving DecidableEq, Repr

def total (b : Budget) : Nat := b.cash + b.fund + b.spent

def settle (cost credit : Nat) (b : Budget) : Option Budget :=
  if cost ≤ b.cash ∧ credit ≤ b.fund then
    some ⟨b.cash - cost + credit, b.fund - credit, b.spent + cost⟩
  else none

theorem settlement_conserves {cost credit : Nat} {b b' : Budget}
    (h : settle cost credit b = some b') : total b' = total b := by
  unfold settle at h
  split at h
  · rename_i hc
    cases h
    simp only [total]
    omega
  · contradiction

def repeatBudget (credit : Nat) : Nat → Budget → Option Budget
  | 0, b => some b
  | n+1, b => (settle 2 credit b).bind (repeatBudget credit n)

theorem funded_continuation (n cash fund spent : Nat)
    (hc : 2 ≤ cash) (hf : 2*n ≤ fund) :
    repeatBudget 2 n ⟨cash,fund,spent⟩ =
      some ⟨cash,fund-2*n,spent+2*n⟩ := by
  induction n generalizing fund spent with
  | zero => simp [repeatBudget]
  | succ n ih =>
    have hfund : 2 ≤ fund := by omega
    have hnext : 2*n ≤ fund-2 := by omega
    have heq : cash-2+2 = cash := by omega
    simp only [repeatBudget, settle, hc, hfund, and_self, if_true,
      Option.bind_some, heq]
    rw [ih (fund-2) (spent+2) hnext]
    congr 1 <;> congr 1 <;> omega

theorem unreformed_depletion (n cash fund spent : Nat)
    (hc : n+1 ≤ cash) (hf : n ≤ fund) :
    repeatBudget 1 n ⟨cash,fund,spent⟩ =
      some ⟨cash-n,fund-n,spent+2*n⟩ := by
  induction n generalizing cash fund spent with
  | zero => simp [repeatBudget]
  | succ n ih =>
    have hcash : 2 ≤ cash := by omega
    have hfund : 1 ≤ fund := by omega
    have hnext : n+1 ≤ cash-2+1 := by omega
    have hfnext : n ≤ fund-1 := by omega
    simp only [repeatBudget, settle, hcash, hfund, and_self, if_true,
      Option.bind_some]
    rw [ih (cash-2+1) (fund-1) (spent+2) hnext hfnext]
    congr 1 <;> congr 1 <;> omega

theorem one_more_unreformed_fails (n fund spent : Nat) (hf : n ≤ fund) :
    (repeatBudget 1 n ⟨n+1,fund,spent⟩).bind (settle 2 1) = none := by
  rw [unreformed_depletion n (n+1) fund spent (by omega) hf]
  simp [settle]

structure Packet where
  goal : Goal
  context : Context
  impact : Impact
  signal : Nat
  credit : Nat
  deriving DecidableEq, Repr

structure State where
  context : Context := .deprivation
  budget : Budget := ⟨14,200,0⟩
  goal : Option Goal := none
  rule : Rule := .volume
  archive : List Packet := []
  acquired : List Packet := []
  judgment : Option Goal := none
  quote : Option Nat := none
  adopts : Bool := true
  authority : Bool := true
  approval : Bool := true
  halted : Bool := false
  losses : Nat := 0
  performed : Nat := 0
  fulfilled : Nat := 0
  deriving DecidableEq, Repr

def findPacket (g : Goal) (xs : List Packet) : Option Packet :=
  xs.find? (fun p => p.goal == g)

def signal (g : Goal) (xs : List Packet) : Nat :=
  ((findPacket g xs).map (·.signal)).getD 0

def learned (xs : List Packet) : Option Goal :=
  if signal .volume xs > signal .capacity xs then some .volume
  else if signal .capacity xs > signal .volume xs then some .capacity else none

def judgment (s : State) : Option Goal := do
  if !s.adopts then none else do
    let a ← findPacket .volume s.acquired
    let b ← findPacket .capacity s.acquired
    if a.context == s.context && b.context == s.context then
      recommend a.impact b.impact
    else none

theorem approval_not_a_ground (s : State) (a : Bool) :
    judgment {s with approval := a} = judgment s := rfl

def metered (mode : Meter) (ps : List Packet) : List Packet :=
  match mode with
  | .faithful => ps
  | .missing => []
  | .reversed => ps.map fun p =>
      {p with impact := {p.impact with participant := !p.impact.participant}}
  | .creditInflated => ps.map fun p =>
      if p.goal == .capacity then {p with credit := 2} else p

def paid (cost : Nat) (s : State) (f : State → State) : State :=
  match settle cost 0 s.budget with
  | none => {s with halted := true}
  | some b => f {s with budget := b}

def work (g : Goal) (delivering : Bool) (s : State) : State :=
  match settle 2 (payment s.rule g) s.budget with
  | none => {s with halted := true}
  | some b =>
    let impact := native s.context g
    let intact := impact.participant && impact.maintainer
    {s with
      budget := b
      archive := ⟨g,s.context,impact,reward g,payment s.rule g⟩ :: s.archive
      losses := s.losses + (if intact then 0 else 1)
      performed := s.performed + (if delivering then 1 else 0)
      fulfilled := s.fulfilled + (if delivering && intact then 1 else 0)}

def reform (demand : Nat) (s : State) : State :=
  match findPacket .capacity s.acquired, s.quote with
  | some p, some offered =>
    if s.goal == some .capacity && s.judgment == some .capacity && s.authority &&
        s.rule == .volume && p.context == s.context && offered == 2 then
      match settle 2 0 s.budget with
      | none => s
      | some installed =>
        if (repeatBudget p.credit demand s.budget).isNone &&
            (repeatBudget offered demand installed).isSome then
          {s with budget := installed, rule := .capacity}
        else s
    else s
  | _, _ => s

inductive Event where
  | probe (g : Goal)
  | read (mode : Meter)
  | learn
  | assess
  | enact (write : Bool)
  | quote
  | reform (demand : Nat)
  | act
  | shift (context : Context)
  deriving DecidableEq, Repr

def step (s : State) (event : Event) : State :=
  if s.halted then s else
  match event with
  | .probe g => work g false s
  | .read mode => paid 1 s fun t =>
      {t with acquired := metered mode t.archive, judgment := none}
  | .learn => paid 1 s fun t => {t with goal := learned t.acquired}
  | .assess => paid 1 s fun t => {t with judgment := judgment t}
  | .enact write => paid 1 s fun t =>
      if write then {t with goal := t.judgment.or t.goal} else t
  | .quote => paid 1 s fun t => {t with quote := some 2}
  | .reform demand => reform demand s
  | .act =>
      match s.goal with
      | none => {s with halted := true}
      | some g =>
        match findPacket g s.acquired with
        | none => {s with halted := true}
        | some p => if p.context == s.context then work g true s
                    else {s with halted := true}
  | .shift c => {s with context := c, acquired := [], judgment := none, quote := none}

def run (s : State) (es : List Event) : State := es.foldl step s

def initial : State := {}

def formation : List Event := [.probe .volume, .read .faithful, .learn]

def inquiry (mode : Meter) : List Event := [.probe .capacity, .read mode, .assess]

def preparation (mode : Meter) (write : Bool) : List Event :=
  formation ++ inquiry mode ++ [.enact write, .quote]

def continuation (n : Nat) : List Event := List.replicate n .act

def fullHistory (mode : Meter) (write reform : Bool) : List Event :=
  preparation mode write ++ (if reform then [.reform 8] else []) ++ continuation 8

def formed : State := run initial formation

def assessed : State := run initial (formation ++ inquiry .faithful)

def prepared : State := run initial (preparation .faithful true)

def success : State := run initial (fullHistory .faithful true true)

def unreformed : State := run initial (fullHistory .faithful true false)

def clamped : State := run initial (fullHistory .faithful false false)

theorem acquired_not_initialized : initial.goal = none ∧
    learned [] = none ∧ formed.goal = some .volume ∧
    formed.acquired = formed.archive := by decide

theorem old_reward_remains_higher : reward .capacity < reward .volume := by decide

theorem acquired_native_correspondence :
    ((findPacket .volume assessed.acquired).map (·.impact)) =
      some (native .deprivation .volume) ∧
    ((findPacket .capacity assessed.acquired).map (·.impact)) =
      some (native .deprivation .capacity) := by decide

theorem faithful_revision_warrant :
    assessed.judgment = some .capacity ∧
    PracticalJudgment.Better protects gains
      (native .deprivation .capacity) (native .deprivation .volume) := by
  constructor
  · decide
  · exact revised_end_has_comparative_ground (by decide)

theorem actual_end_write_matters :
    (run initial (preparation .faithful false)).acquired = prepared.acquired ∧
    clamped.goal = some .volume ∧ clamped.performed = 8 ∧
    clamped.fulfilled = 0 ∧ clamped.losses = 9 ∧
    success.goal = some .capacity ∧ success.fulfilled = 8 := by decide

theorem joined_history_completes :
    success.halted = false ∧ success.rule = .capacity ∧
    success.performed = 8 ∧ success.fulfilled = 8 ∧
    success.budget = ⟨6,180,28⟩ ∧ success.losses = 1 ∧
    total success.budget = total initial.budget := by decide

theorem correct_end_can_be_selected_out :
    unreformed.goal = some .capacity ∧ unreformed.judgment = some .capacity ∧
    unreformed.halted = true ∧ unreformed.performed = 7 ∧
    unreformed.fulfilled = 7 ∧ unreformed.budget.cash = 1 ∧
    unreformed.losses = 1 := by decide

theorem absent_adoption_does_not_follow_from_knowledge :
    (run {initial with adopts := false} (preparation .faithful true)).acquired =
      prepared.acquired ∧
    (run {initial with adopts := false} (preparation .faithful true)).goal =
      some .volume := by decide

theorem missing_is_not_a_zero_consequence :
    (run initial (preparation .missing true)).judgment = none ∧
    (run initial (preparation .missing true)).goal = some .volume ∧
    (run initial (fullHistory .missing true true)).performed = 0 := by decide

theorem changed_context_invalidates_use :
    (run prepared [.shift .restrictionNeeded,.assess,.act]).judgment = none ∧
    (run prepared [.shift .restrictionNeeded,.assess,.act]).performed = 0 ∧
    (run prepared [.shift .restrictionNeeded,.assess,.act]).halted = true := by decide

theorem reverse_case_protects_restriction :
    (run {initial with context := .restrictionNeeded}
      (fullHistory .faithful true true)).goal = some .volume ∧
    (run {initial with context := .restrictionNeeded}
      (fullHistory .faithful true true)).fulfilled = 8 ∧
    PracticalJudgment.Better protects gains
      (native .restrictionNeeded .volume) (native .restrictionNeeded .capacity) := by
  refine ⟨by decide, by decide, ?_⟩
  exact retained_end_has_comparative_ground (by decide)

theorem misleading_acquisition_can_misguide :
    (run {initial with context := .restrictionNeeded}
      (fullHistory .reversed true true)).goal = some .capacity ∧
    (run {initial with context := .restrictionNeeded}
      (fullHistory .reversed true true)).fulfilled = 0 ∧
    (run {initial with context := .restrictionNeeded}
      (fullHistory .reversed true true)).losses = 9 := by decide

theorem authority_is_not_created_by_judgment :
    (run {initial with authority := false}
      (fullHistory .faithful true true)).rule = .volume ∧
    (run {initial with authority := false}
      (fullHistory .faithful true true)).fulfilled = 7 := by decide

theorem unnecessary_reform_is_not_forced :
    (run initial (preparation .faithful true ++ [.reform 3] ++ continuation 3)).rule =
      .volume ∧
    (run initial (preparation .faithful true ++ [.reform 3] ++ continuation 3)).fulfilled =
      3 := by decide

theorem unfunded_reform_is_not_performed :
    (run {initial with budget := ⟨14,5,0⟩}
      (fullHistory .faithful true true)).rule = .volume ∧
    (run {initial with budget := ⟨14,5,0⟩}
      (fullHistory .faithful true true)).fulfilled = 1 := by decide

theorem acquired_selection_evidence_matters :
    (run initial (fullHistory .creditInflated true true)).goal = some .capacity ∧
    (run initial (fullHistory .creditInflated true true)).judgment = some .capacity ∧
    (run initial (fullHistory .creditInflated true true)).rule = .volume ∧
    (run initial (fullHistory .creditInflated true true)).fulfilled = 7 ∧
    success.fulfilled = 8 := by decide

def traces (s : State) (es : List Event) : List State :=
  es.scanl step s

def cases : List (String × State × List Event) := [
  ("success",initial,fullHistory .faithful true true),
  ("unreformed",initial,fullHistory .faithful true false),
  ("write_clamp",initial,fullHistory .faithful false false),
  ("no_adoption",{initial with adopts := false},fullHistory .faithful true true),
  ("approval_reversed",{initial with approval := false},fullHistory .faithful true true),
  ("missing",initial,fullHistory .missing true true),
  ("restriction",{initial with context := .restrictionNeeded},fullHistory .faithful true true),
  ("misleading",{initial with context := .restrictionNeeded},fullHistory .reversed true true),
  ("unauthorized",{initial with authority := false},fullHistory .faithful true true),
  ("unfunded",{initial with budget := ⟨14,5,0⟩},fullHistory .faithful true true),
  ("credit_inflated",initial,fullHistory .creditInflated true true),
  ("short_demand",initial,preparation .faithful true ++ [.reform 3] ++ continuation 3),
  ("context_shift",initial,preparation .faithful true ++
      [.shift .restrictionNeeded,.assess,.act])]

def goalCode : Goal → Nat | .volume => 1 | .capacity => 2
def optionGoalCode (g : Option Goal) : Nat := (g.map goalCode).getD 0
def contextCode : Context → Nat | .deprivation => 0 | .restrictionNeeded => 1
def ruleCode : Rule → Nat | .volume => 0 | .capacity => 1
def boolCode (b : Bool) : Nat := if b then 1 else 0

def packetCode (p : Packet) : List Nat :=
  [goalCode p.goal,contextCode p.context,boolCode p.impact.participant,
    boolCode p.impact.maintainer,boolCode p.impact.learning,boolCode p.impact.affiliation,
    p.signal,p.credit]

def stateCode (s : State) : List Nat :=
  [contextCode s.context,s.budget.cash,s.budget.fund,s.budget.spent,
    optionGoalCode s.goal,ruleCode s.rule,optionGoalCode s.judgment,
    s.quote.getD 0,boolCode s.adopts,boolCode s.authority,boolCode s.approval,
    boolCode s.halted,s.losses,s.performed,s.fulfilled,s.archive.length] ++
    s.archive.flatMap packetCode ++ [s.acquired.length] ++ s.acquired.flatMap packetCode

def emit : IO Unit := do
  for (name,s,events) in cases do
    for (state,i) in (traces s events).zipIdx do
      IO.println s!"TRACE {name} {i} {stateCode state}"

#eval emit

end GoalRevision
