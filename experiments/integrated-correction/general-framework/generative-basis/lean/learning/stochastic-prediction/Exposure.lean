import Std

namespace StochasticPrediction

inductive Arm where
  | variable | conventional | fixedFast | fixedSlow | directRecord
  | frozenRegister | invertedRecord | invertedAction
  deriving DecidableEq, Repr

structure Parameters where
  gateAssembly : Nat
  base : Nat
  retrofit : Nat
  rent : Nat
  trial : Nat
  writing : Nat
  renewal : Nat
  gateRenewal : Nat
  packet : Nat
  lifetime : Nat
  gateLifetime : Nat
  deriving DecidableEq, Repr

/-- Gate 2 represents absent; 0 slow and 1 fast. Stage 0 absent, 1 prototype,
2 predictive. The historical success flags of Python are observer-only. -/
structure State where
  fuel : Nat
  gate : Nat := 2
  gateLife : Nat := 0
  stage : Nat := 0
  life : Nat := 0
  q : Nat := 2
  last : Bool := false
  written : Bool := false
  deriving DecidableEq, Repr

structure Seed where
  gate : Bool
  prior : Bool
  available : Bool
  deriving DecidableEq, Repr

inductive Status where
  | inactive | rentFailed | noWork | workedUnpaid | workedPaid
  deriving DecidableEq, Repr

structure Result where
  state : State
  spent : Nat := 0
  waste : Nat := 0
  worked : Bool := false
  captured : Bool := false
  wrote : Bool := false
  status : Status := .inactive
  deriving DecidableEq, Repr

def maintenance (p : Parameters) := p.renewal+p.gateRenewal

def Admissible (p : Parameters) : Prop :=
  maintenance p ≤ p.packet ∧ 0 < p.lifetime ∧ 0 < p.gateLifetime

def Valid (p : Parameters) (s : State) : Prop :=
  s.q ≤ 4 ∧ s.gate ≤ 2 ∧ s.stage ≤ 2 ∧
  s.life ≤ p.lifetime ∧ s.gateLife ≤ p.gateLifetime

def command (s : State) : Bool := if s.q = 2 then s.last else 2 < s.q

def issued (a : Arm) (s : State) : Bool :=
  if a = .invertedAction then !(command s) else command s

def updated (fast : Bool) (q : Nat) (label : Bool) : Nat :=
  if fast then (if label then 4 else 0)
  else if label then min 4 (q+1) else q-1

def gateKind (a : Arm) (b : Bool) : Nat :=
  if a = .fixedFast ∨ a = .directRecord then 1
  else if a = .fixedSlow then 0 else if b then 1 else 0

def formGate (p : Parameters) (a : Arm) (b : Bool) (s : State) : State :=
  if s.gateLife = 0 ∧ p.gateAssembly ≤ s.fuel then
    {s with fuel := s.fuel-p.gateAssembly, gate := gateKind a b, gateLife := p.gateLifetime}
  else s

def gateCost (p : Parameters) (s : State) : Nat :=
  if s.gateLife = 0 ∧ p.gateAssembly ≤ s.fuel then p.gateAssembly else 0

def formBase (p : Parameters) (b : Bool) (s : State) : State :=
  if 0 < s.gateLife ∧ s.life = 0 ∧ s.stage ≠ 1 ∧ p.base ≤ s.fuel then
    {s with fuel := s.fuel-p.base, stage := 1, life := 0, q := 2, last := b, written := false}
  else s

def baseCost (p : Parameters) (s : State) : Nat :=
  if 0 < s.gateLife ∧ s.life = 0 ∧ s.stage ≠ 1 ∧ p.base ≤ s.fuel then p.base else 0

def retrofitPrice (p : Parameters) (a : Arm) : Nat :=
  if a = .directRecord then 1 else p.retrofit

def retrofit (p : Parameters) (a : Arm) (s : State) : State :=
  if 0 < s.gateLife ∧ s.stage = 1 ∧ retrofitPrice p a ≤ s.fuel then
    {s with fuel := s.fuel-retrofitPrice p a, stage := 2, life := p.lifetime, q := 2}
  else s

def retrofitCost (p : Parameters) (a : Arm) (s : State) : Nat :=
  if 0 < s.gateLife ∧ s.stage = 1 ∧ retrofitPrice p a ≤ s.fuel
  then retrofitPrice p a else 0

def prepared (p : Parameters) (a : Arm) (b : Seed) (s : State) : State :=
  retrofit p a (formBase p b.prior (formGate p a b.gate s))

def preparationCost (p : Parameters) (a : Arm) (b : Seed) (s : State) : Nat :=
  gateCost p s + baseCost p (formGate p a b.gate s) +
    retrofitCost p a (formBase p b.prior (formGate p a b.gate s))

/-- One actual worked trial, entered after rent has been paid. No write is
required to return its continuing successor. -/
def trial (p : Parameters) (a : Arm) (regime available : Bool) (s : State) : Result :=
  let action := issued a s
  let capture := (action == regime) && available
  let cash := s.fuel-p.trial + if capture then p.packet-maintenance p else 0
  let paid : Bool := p.writing ≤ cash
  let label := if capture then action else !action
  let label := if a = .invertedRecord then !label else label
  let q := if paid && (a != .frozenRegister) then updated (s.gate == 1) s.q label else s.q
  {state := {s with fuel := cash-(if paid then p.writing else 0), q := q, last := action, written := s.written || paid, gateLife := if capture then p.gateLifetime else s.gateLife-1, life := if capture then p.lifetime else s.life-1},
   spent := p.trial+(if capture then maintenance p else 0)+(if paid then p.writing else 0),
   waste := if capture then 0 else p.packet,
   worked := true, captured := capture, wrote := paid,
   status := if paid then .workedPaid else .workedUnpaid}

/-- Installed exposure after the possible formation stages. All non-work exits
still lose the scheduled packet. Failed rent destroys the operative predictor. -/
def operate (p : Parameters) (a : Arm) (regime available : Bool) (s : State) : Result :=
  if s.life = 0 ∨ s.stage ≠ 2 then
    {state := s, waste := p.packet}
  else if s.fuel < p.rent then
    {state := {s with stage := 0, life := 0, q := 2, last := false, written := false},
      waste := p.packet, status := .rentFailed}
  else
    let rented := {s with fuel := s.fuel-p.rent}
    if rented.gateLife = 0 ∨ rented.fuel < p.trial then
      {state := rented, spent := p.rent, waste := p.packet, status := .noWork}
    else
      let r := trial p a regime available rented
      {r with spent := p.rent+r.spent}

def exposure (p : Parameters) (a : Arm) (regime : Bool) (b : Seed) (s : State) : Result :=
  let r := operate p a regime b.available (prepared p a b s)
  {r with spent := preparationCost p a b s+r.spent}

theorem form_gate_account (p : Parameters) (a : Arm) (b : Bool) (s : State) :
    (formGate p a b s).fuel+gateCost p s = s.fuel := by
  simp only [formGate, gateCost]
  split <;> simp_all <;> omega

theorem form_base_account (p : Parameters) (b : Bool) (s : State) :
    (formBase p b s).fuel+baseCost p s = s.fuel := by
  simp only [formBase, baseCost]
  split <;> simp_all <;> omega

theorem retrofit_account (p : Parameters) (a : Arm) (s : State) :
    (retrofit p a s).fuel+retrofitCost p a s = s.fuel := by
  simp only [retrofit, retrofitCost]
  split <;> simp_all <;> omega

theorem preparation_account (p : Parameters) (a : Arm) (b : Seed) (s : State) :
    (prepared p a b s).fuel+preparationCost p a b s = s.fuel := by
  have h1 := form_gate_account p a b.gate s
  have h2 := form_base_account p b.prior (formGate p a b.gate s)
  have h3 := retrofit_account p a (formBase p b.prior (formGate p a b.gate s))
  simp only [prepared, preparationCost]
  omega

theorem trial_account (p : Parameters) (a : Arm) (regime available : Bool) (s : State)
    (hp : maintenance p ≤ p.packet) (hf : p.trial ≤ s.fuel) :
    (trial p a regime available s).state.fuel +
      (trial p a regime available s).spent + (trial p a regime available s).waste =
      s.fuel+p.packet := by
  unfold trial
  dsimp only
  split <;> split <;> simp_all <;> omega

theorem operate_account (p : Parameters) (a : Arm) (regime available : Bool) (s : State)
    (hp : maintenance p ≤ p.packet) :
    (operate p a regime available s).state.fuel +
      (operate p a regime available s).spent + (operate p a regime available s).waste =
      s.fuel+p.packet := by
  unfold operate
  split
  · simp
  · split
    · simp
    · dsimp only
      split
      · simp; omega
      · rename_i hl hr ht
        have h := trial_account p a regime available {s with fuel := s.fuel-p.rent} hp
          (by simp_all)
        dsimp only at h ⊢
        omega

theorem exposure_account (p : Parameters) (a : Arm) (regime : Bool) (b : Seed) (s : State)
    (hp : maintenance p ≤ p.packet) :
    (exposure p a regime b s).state.fuel + (exposure p a regime b s).spent +
      (exposure p a regime b s).waste = s.fuel+p.packet := by
  have h1 := preparation_account p a b s
  have h2 := operate_account p a regime b.available (prepared p a b s) hp
  simp only [exposure]
  omega

/-- Ordinary/conventional lookup tables give the same operational arithmetic
on the declared five-score domain. -/
def conventionalCommand (q : Nat) (last : Bool) : Bool :=
  match q with | 0 | 1 => false | 2 => last | _ => true

def conventionalUpdated (fast : Bool) (q : Nat) (label : Bool) : Nat :=
  if fast then (if label then 4 else 0)
  else if label then (match q with | 0 => 1 | 1 => 2 | 2 => 3 | _ => 4)
  else (match q with | 0 | 1 => 0 | 2 => 1 | 3 => 2 | _ => 3)

theorem conventional_command_agrees (s : State) (h : s.q ≤ 4) :
    conventionalCommand s.q s.last = command s := by
  obtain h | h | h | h | h : s.q=0 ∨ s.q=1 ∨ s.q=2 ∨ s.q=3 ∨ s.q=4 := by omega
  all_goals simp [conventionalCommand, command, h]

theorem conventional_update_agrees (fast label : Bool) (q : Nat) (h : q ≤ 4) :
    conventionalUpdated fast q label = updated fast q label := by
  obtain h | h | h | h | h : q=0 ∨ q=1 ∨ q=2 ∨ q=3 ∨ q=4 := by omega
  all_goals subst q; cases fast <;> cases label <;> decide

/-- The exact finite call list retains every actual successor, including
no-work, expired and skipped-write results. -/
def run (p : Parameters) (a : Arm) (s : State) : List (Bool × Seed) → List Result
  | [] => []
  | (regime,b)::xs => let r := exposure p a regime b s; r :: run p a r.state xs

def finalState (s : State) : List Result → State
  | [] => s
  | r::rs => finalState r.state rs

def charges (rs : List Result) : Nat := (rs.map (fun r => r.spent+r.waste)).sum

theorem final_cons (s : State) (r : Result) (rs : List Result) :
    finalState s (r::rs) = finalState r.state rs := by
  rfl

theorem run_account (p : Parameters) (a : Arm) (s : State) (xs : List (Bool × Seed))
    (hp : maintenance p ≤ p.packet) :
    (finalState s (run p a s xs)).fuel + charges (run p a s xs) =
      s.fuel + xs.length*p.packet := by
  induction xs generalizing s with
  | nil => simp [run, finalState, charges]
  | cons x xs ih =>
    obtain ⟨z,b⟩ := x
    have h1 := exposure_account p a z b s hp
    have h2 := ih (exposure p a z b s).state
    simp only [run, final_cons, charges, List.map_cons, List.sum_cons,
      List.length_cons, Nat.add_mul, Nat.one_mul] at *
    omega

theorem updated_bounded (fast label : Bool) (q : Nat) (h : q ≤ 4) :
    updated fast q label ≤ 4 := by
  cases fast <;> cases label <;> simp [updated] <;> omega

theorem preparation_preserves_bounds (p : Parameters) (a : Arm) (b : Seed) (s : State)
    (h : Valid p s) : Valid p (prepared p a b s) := by
  have hg : Valid p (formGate p a b.gate s) := by
    unfold formGate
    split
    · rcases h with ⟨hq,hg,hs,hl,hgl⟩
      refine ⟨hq,?_,hs,hl,Nat.le_refl _⟩
      unfold gateKind
      split <;> (try split) <;> (try split) <;> dsimp only <;> omega
    · exact h
  have hb : Valid p (formBase p b.prior (formGate p a b.gate s)) := by
    unfold formBase
    split
    · rcases hg with ⟨hq,hg,hs,hl,hgl⟩
      simp_all [Valid]
    · exact hg
  unfold prepared retrofit
  split
  · rcases hb with ⟨hq,hg,hs,hl,hgl⟩
    simp_all [Valid]
  · exact hb

theorem trial_preserves_bounds (p : Parameters) (a : Arm) (z available : Bool) (s : State)
    (h : Valid p s) : Valid p (trial p a z available s).state := by
  rcases h with ⟨hq,hg,hs,hl,hgl⟩
  simp only [trial, Valid]
  constructor
  · split <;> split <;> first | exact updated_bounded _ _ _ hq | exact hq
  · refine ⟨hg,hs,?_,?_⟩ <;> split <;> omega

theorem operate_preserves_bounds (p : Parameters) (a : Arm) (z available : Bool) (s : State)
    (h : Valid p s) : Valid p (operate p a z available s).state := by
  unfold operate
  split
  · exact h
  · split
    · rcases h with ⟨hq,hg,hs,hl,hgl⟩; simp_all [Valid]
    · dsimp only
      split
      · exact h
      · exact trial_preserves_bounds p a z available _ h

theorem exposure_preserves_bounds (p : Parameters) (a : Arm) (z : Bool) (b : Seed) (s : State)
    (h : Valid p s) : Valid p (exposure p a z b s).state :=
  operate_preserves_bounds p a z b.available _ (preparation_preserves_bounds p a b s h)

theorem command_ignores_fuel_and_leases (s : State) (fuel life gateLife : Nat) :
    command {s with fuel := fuel, life := life, gateLife := gateLife} = command s := rfl

end StochasticPrediction

#print axioms StochasticPrediction.form_gate_account
#print axioms StochasticPrediction.form_base_account
#print axioms StochasticPrediction.retrofit_account
#print axioms StochasticPrediction.preparation_account
#print axioms StochasticPrediction.trial_account
#print axioms StochasticPrediction.operate_account
#print axioms StochasticPrediction.exposure_account
#print axioms StochasticPrediction.conventional_command_agrees
#print axioms StochasticPrediction.conventional_update_agrees
#print axioms StochasticPrediction.final_cons
#print axioms StochasticPrediction.run_account
#print axioms StochasticPrediction.updated_bounded
#print axioms StochasticPrediction.preparation_preserves_bounds
#print axioms StochasticPrediction.trial_preserves_bounds
#print axioms StochasticPrediction.operate_preserves_bounds
#print axioms StochasticPrediction.exposure_preserves_bounds
#print axioms StochasticPrediction.command_ignores_fuel_and_leases
