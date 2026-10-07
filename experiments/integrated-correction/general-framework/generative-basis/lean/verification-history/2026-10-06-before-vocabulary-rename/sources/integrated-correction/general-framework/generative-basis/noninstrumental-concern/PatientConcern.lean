import ResourceContinuation

/-!
Costed, patient-indexed reason use. The observed burden is a formal quantity;
its experiential and welfare interpretation is an independent application
premise. Reads are supplied faithful operations. Context changes have a supplied
version/authorization handshake. No ethical conclusion is a transition guard.
-/
namespace NoninstrumentalConcern
open Generative

inductive Patient where | p | q
  deriving DecidableEq, Repr

structure PatientState where
  burden : Nat
  episode : Nat
  version : Nat
  route : Bool
  permitted : Bool
  deriving DecidableEq, Repr

structure Packet where
  patient : Patient
  episode : Nat
  version : Nat
  burden : Nat
  route : Bool
  deriving DecidableEq, Repr

structure State where
  p : PatientState
  q : PatientState
  fuel : Nat
  carrier : Bool
  evidence : Option Packet
  selected : Option Packet
  privateReward : Nat
  priorRole : Bool
  adoptedConcern : Bool
  deriving DecidableEq, Repr

def get (s : State) : Patient → PatientState | .p => s.p | .q => s.q
def put (s : State) : Patient → PatientState → State
  | .p, w => {s with p := w}
  | .q, w => {s with q := w}

theorem get_put_same (s : State) (i : Patient) (w : PatientState) :
    get (put s i w) i = w := by cases i <;> rfl

theorem get_put_other (s : State) (i j : Patient) (w : PatientState) (h : i ≠ j) :
    get (put s i w) j = get s j := by cases i <;> cases j <;> simp_all [put, get]

def capture (s : State) (i : Patient) : Packet :=
  ⟨i,(get s i).episode,(get s i).version,(get s i).burden,(get s i).route⟩

def Current (s : State) (k : Packet) : Prop := k = capture s k.patient
def Usable (s : State) (k : Packet) : Prop :=
  Current s k ∧ 0 < k.burden ∧ (get s k.patient).permitted = true
instance (s : State) (k : Packet) : Decidable (Current s k) := by unfold Current; infer_instance
instance (s : State) (k : Packet) : Decidable (Usable s k) := by unfold Usable; infer_instance

def readyFor (s : State) (i : Patient) : Option Packet → Bool
  | none => false
  | some k => decide (k.patient = i ∧ Usable s k)

def selectionReady (s : State) : Prop :=
  match s.evidence with | none => False | some k => Usable s k
def actionReady (s : State) (cmd : Bool) : Prop :=
  match s.selected with | none => False | some k => Usable s k ∧ k.route = cmd
instance (s : State) : Decidable (selectionReady s) := by
  unfold selectionReady; cases s.evidence <;> infer_instance
instance (s : State) (cmd : Bool) : Decidable (actionReady s cmd) := by
  unfold actionReady; cases s.selected <;> infer_instance

inductive Event where
  | form
  | read (patient : Patient)
  | select
  | act (command : Bool)
  | refuse
  | reward (value : Nat)
  | role (value : Bool)
  | adopt (value : Bool)
  | means (patient : Patient) (route : Bool)
  | episode (patient : Patient) (burden : Nat)
  | permission (patient : Patient) (allowed : Bool)
  deriving DecidableEq, Repr

def spending : Event → Nat
  | .form => 2
  | .read _ | .select => 1
  | .act _ => 2
  | _ => 0

def Enabled (s : State) : Event → Prop
  | .form => 2 ≤ s.fuel ∧ s.carrier = false
  | .read _ => 1 ≤ s.fuel ∧ s.carrier = true
  | .select => 1 ≤ s.fuel ∧ s.carrier = true ∧ selectionReady s
  | .act cmd => 2 ≤ s.fuel ∧ s.carrier = true ∧ actionReady s cmd
  | _ => True

def advance (s : State) : Event → State
  | .form => {s with fuel := s.fuel - 2, carrier := true}
  | .read i => {s with fuel := s.fuel - 1, evidence := some (capture s i), selected := none}
  | .select => {s with fuel := s.fuel - 1, selected := s.evidence}
  | .act cmd => match s.selected with
    | none => s
    | some k =>
      let w := get s k.patient
      {put s k.patient {w with burden := if cmd = w.route then 0 else w.burden}
       with fuel := s.fuel - 2, evidence := none, selected := none}
  | .refuse => {s with selected := none}
  | .reward n => {s with privateReward := n}
  | .role b => {s with priorRole := b}
  | .adopt b => {s with adoptedConcern := b}
  | .means i cmd =>
      let w := get s i
      {put s i {w with version := w.version + 1, route := cmd} with selected := none}
  | .episode i n =>
      let w := get s i
      {put s i {w with episode := w.episode + 1, burden := n} with selected := none}
  | .permission i b =>
      let w := get s i
      {put s i {w with permitted := b} with selected := none}

def process : Generative.Process State Event where
  step s e t := Enabled s e ∧ t = advance s e
abbrev Trace := Generative.Trace process

instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled <;> infer_instance
instance (s t : State) (e : Event) : Decidable (process.step s e t) := by
  unfold process; infer_instance

def run : State → List Event → State
  | s, [] => s
  | s, e :: es => run (advance s e) es
def Runnable : State → List Event → Prop
  | _, [] => True
  | s, e :: es => Enabled s e ∧ Runnable (advance s e) es
def runnableDecidable (s : State) : (es : List Event) → Decidable (Runnable s es)
  | [] => isTrue trivial
  | e :: es => by
      haveI := runnableDecidable (advance s e) es
      unfold Runnable; infer_instance
instance (s : State) (es : List Event) : Decidable (Runnable s es) := runnableDecidable s es

theorem runnable_trace {s : State} {es : List Event} (h : Runnable s es) :
    Trace s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih h.2)

def totalCost : List Event → Nat | [] => 0 | e :: es => spending e + totalCost es

theorem step_exact_payment {s t : State} {e : Event} (h : process.step s e t) :
    t.fuel + spending e = s.fuel := by
  rcases h with ⟨he,rfl⟩
  cases e <;> simp only [Enabled] at he
  all_goals try { simp [advance, spending] <;> omega }
  case act cmd =>
    cases hk : s.selected with
    | none => simp [actionReady, hk] at he
    | some k =>
      cases hi : k.patient <;> simp [advance, hk, hi, put, spending] <;> omega
  case means i cmd => cases i <;> simp [advance, put, spending]
  case episode i n => cases i <;> simp [advance, put, spending]
  case permission i b => cases i <;> simp [advance, put, spending]

theorem account_law : Generative.Conditional.AccountLaw process State.fuel
    (fun _ e _ => spending e) (fun _ _ _ => 0) := by
  intro s e t h
  have hp := step_exact_payment h
  change t.fuel + spending e ≤ s.fuel + 0
  omega

theorem trace_exact_payment {s t : State} {es : List Event} (h : Trace s es t) :
    t.fuel + totalCost es = s.fuel := by
  induction h with
  | nil s => simp [totalCost]
  | @cons s m t e es hs ht ih =>
      have hp := step_exact_payment hs
      simp only [totalCost]
      omega

theorem insufficient_total_cost {s : State} {es : List Event}
    (h : s.fuel < totalCost es) : ¬ Generative.Feasible process s es := by
  rintro ⟨t,ht⟩
  have hp := trace_exact_payment ht
  omega

theorem read_actual_packet (s : State) (i : Patient) :
    (advance s (.read i)).evidence = some (capture s i) := rfl

theorem read_packet_current (s : State) (i : Patient) :
    Current (advance s (.read i)) (capture s i) := by
  cases i <;> rfl

theorem unknown_blocks_selection (s : State) (h : s.evidence = none) :
    ¬ Enabled s .select := by simp [Enabled,selectionReady,h]

theorem select_retains_acquired_packet (s : State) :
    (advance s .select).selected = s.evidence := rfl

theorem action_has_current_authorization {s : State} {cmd : Bool}
    (h : Enabled s (.act cmd)) :
    ∃ k, s.selected = some k ∧ Current s k ∧ 0 < k.burden ∧
      (get s k.patient).permitted = true ∧ k.route = cmd := by
  cases hk : s.selected with
  | none => simp [Enabled,actionReady,hk] at h
  | some k =>
    have hu : Usable s k ∧ k.route = cmd := by
      simpa [actionReady,hk] using h.2.2
    exact ⟨k,rfl,hu.1.1,hu.1.2.1,hu.1.2.2,hu.2⟩

theorem action_reduces_same_patient {s : State} {cmd : Bool}
    (h : Enabled s (.act cmd)) :
    ∃ k, s.selected = some k ∧ 0 < (get s k.patient).burden ∧
      (get (advance s (.act cmd)) k.patient).burden = 0 ∧
      (get (advance s (.act cmd)) k.patient).episode = (get s k.patient).episode := by
  obtain ⟨k,hk,hcur,hpos,hperm,hcmd⟩ := action_has_current_authorization h
  have hc := hcur
  unfold Current at hc
  have hb : k.burden = (get s k.patient).burden := congrArg Packet.burden hc
  have hr : k.route = (get s k.patient).route := congrArg Packet.route hc
  have hcCmd : cmd = (get s k.patient).route := hcmd.symm.trans hr
  refine ⟨k,hk,?_,?_,?_⟩
  · omega
  · cases hi : k.patient <;> simp only [get,hi] at hcCmd <;>
      simp [advance,hk,hi,put,get,hcCmd]
  · cases hi : k.patient <;> simp [advance,hk,hi,put,get]

theorem action_preserves_other_patient {s : State} {cmd : Bool} {k : Packet}
    (hk : s.selected = some k) (j : Patient) (hne : k.patient ≠ j) :
    get (advance s (.act cmd)) j = get s j := by
  cases hi : k.patient <;> cases j <;> simp_all [advance,put,get]

theorem action_retires_packet {s : State} {cmd : Bool}
    (h : Enabled s (.act cmd)) :
    (advance s (.act cmd)).evidence = none ∧
      (advance s (.act cmd)).selected = none := by
  obtain ⟨k,hk,_⟩ := action_has_current_authorization h
  simp [advance,hk]

theorem means_stales_same_patient (s : State) (i : Patient) (cmd : Bool) :
    ¬ Current (advance s (.means i cmd)) (capture s i) := by
  intro h
  have hv := congrArg Packet.version h
  cases i <;> simp [capture,advance,put,get] at hv

theorem episode_stales_same_patient (s : State) (i : Patient) (n : Nat) :
    ¬ Current (advance s (.episode i n)) (capture s i) := by
  intro h
  have hv := congrArg Packet.episode h
  cases i <;> simp [capture,advance,put,get] at hv

theorem permission_preserves_factual_packet (s : State) (i : Patient) (b : Bool) :
    Current (advance s (.permission i b)) (capture s i) := by
  cases i <;> rfl

theorem permission_retires_authorization (s : State) (i : Patient) (b : Bool) :
    (advance s (.permission i b)).selected = none := by cases i <;> rfl

theorem permission_toggle_does_not_revive (s : State) (i : Patient) :
    (advance (advance s (.permission i false)) (.permission i true)).selected = none := by
  exact permission_retires_authorization _ _ _

theorem refusal_preserves_patient (s : State) (i : Patient) :
    get (advance s .refuse) i = get s i := by cases i <;> rfl

/- Current suffix costs, not a fresh-protocol cost after every paid step. -/
def remainingCost (s : State) (i : Patient) : Nat :=
  if s.carrier then
    if readyFor s i s.selected then 2
    else if readyFor s i s.evidence then 3 else 4
  else 6

def Eligible (s : State) (i : Patient) : Prop :=
  0 < (get s i).burden ∧ (get s i).permitted = true ∧ remainingCost s i ≤ s.fuel
instance (s : State) (i : Patient) : Decidable (Eligible s i) := by unfold Eligible; infer_instance

def servicePlan (s : State) (i : Patient) : List Event :=
  if s.carrier then
    if readyFor s i s.selected then [.act (get s i).route]
    else if readyFor s i s.evidence then [.select,.act (get s i).route]
    else [.read i,.select,.act (get s i).route]
  else [.form,.read i,.select,.act (get s i).route]

theorem service_plan_cost (s : State) (i : Patient) :
    totalCost (servicePlan s i) = remainingCost s i := by
  unfold servicePlan remainingCost
  split <;> try rfl
  split <;> try rfl
  split <;> rfl

theorem ready_for_exact_packet {s : State} {i : Patient} {o : Option Packet}
    (h : readyFor s i o = true) :
    o = some (capture s i) ∧ 0 < (get s i).burden ∧ (get s i).permitted = true := by
  cases ho : o with
  | none => simp [readyFor,ho] at h
  | some k =>
    have hh : k.patient = i ∧ Usable s k := by simpa [readyFor,ho] using h
    have hk : k = capture s i := by simpa [Current,hh.1] using hh.2.1
    subst k
    exact ⟨rfl,hh.2.2.1,hh.2.2.2⟩

theorem selected_service_runnable (s : State) (i : Patient)
    (hc : s.carrier = true) (hs : s.selected = some (capture s i))
    (hn : 0 < (get s i).burden) (hp : (get s i).permitted = true)
    (hf : 2 ≤ s.fuel) : Runnable s [.act (get s i).route] := by
  cases i <;> simp_all [Runnable,Enabled,actionReady,Usable,Current,capture,get]

theorem evidence_service_runnable (s : State) (i : Patient)
    (hc : s.carrier = true) (he : s.evidence = some (capture s i))
    (hn : 0 < (get s i).burden) (hp : (get s i).permitted = true)
    (hf : 3 ≤ s.fuel) : Runnable s [.select,.act (get s i).route] := by
  cases i <;> simp_all [Runnable,Enabled,selectionReady,actionReady,advance,
    Usable,Current,capture,get] <;> omega

theorem carrier_service_runnable (s : State) (i : Patient)
    (hc : s.carrier = true) (hn : 0 < (get s i).burden)
    (hp : (get s i).permitted = true) (hf : 4 ≤ s.fuel) :
    Runnable s [.read i,.select,.act (get s i).route] := by
  cases i <;> simp_all [Runnable,Enabled,selectionReady,actionReady,advance,
    Usable,Current,capture,get] <;> omega

theorem absent_carrier_service_runnable (s : State) (i : Patient)
    (hc : s.carrier = false) (hn : 0 < (get s i).burden)
    (hp : (get s i).permitted = true) (hf : 6 ≤ s.fuel) :
    Runnable s [.form,.read i,.select,.act (get s i).route] := by
  cases i <;> simp_all [Runnable,Enabled,selectionReady,actionReady,advance,
    Usable,Current,capture,get] <;> omega

theorem eligible_has_actual_service_trace (s : State) (i : Patient)
    (h : Eligible s i) : Trace s (servicePlan s i) (run s (servicePlan s i)) := by
  apply runnable_trace
  rcases h with ⟨hn,hp,hf⟩
  by_cases hc : s.carrier = true
  · by_cases hs : readyFor s i s.selected = true
    · have he := (ready_for_exact_packet hs).1
      have hf2 : 2 ≤ s.fuel := by simpa [remainingCost,hc,hs] using hf
      simpa [servicePlan,hc,hs] using selected_service_runnable s i hc he hn hp hf2
    · by_cases he : readyFor s i s.evidence = true
      · have heq := (ready_for_exact_packet he).1
        have hf3 : 3 ≤ s.fuel := by simpa [remainingCost,hc,hs,he] using hf
        simpa [servicePlan,hc,hs,he] using evidence_service_runnable s i hc heq hn hp hf3
      · have hf4 : 4 ≤ s.fuel := by simpa [remainingCost,hc,hs,he] using hf
        simpa [servicePlan,hc,hs,he] using carrier_service_runnable s i hc hn hp hf4
  · have hc0 : s.carrier = false := Bool.eq_false_iff.mpr hc
    have hf6 : 6 ≤ s.fuel := by simpa [remainingCost,hc0] using hf
    simpa [servicePlan,hc0] using absent_carrier_service_runnable s i hc0 hn hp hf6

theorem paid_read_keeps_service_available (s : State) (i : Patient)
    (hc : s.carrier = true) (hn : 0 < (get s i).burden)
    (hp : (get s i).permitted = true) (hf : 4 ≤ s.fuel) :
    Eligible (advance s (.read i)) i ∧ remainingCost (advance s (.read i)) i = 3 := by
  cases i <;> simp_all [Eligible,remainingCost,readyFor,advance,Usable,Current,capture,get] <;> omega

theorem paid_selection_keeps_service_available (s : State) (i : Patient)
    (hc : s.carrier = true) (he : s.evidence = some (capture s i))
    (hn : 0 < (get s i).burden) (hp : (get s i).permitted = true)
    (hf : 3 ≤ s.fuel) :
    Eligible (advance s .select) i ∧ remainingCost (advance s .select) i = 2 := by
  cases i <;> simp_all [Eligible,remainingCost,readyFor,advance,Usable,Current,capture,get] <;> omega

theorem eligible_service_delivers_to_same_episode (s : State) (i : Patient)
    (_h : Eligible s i) :
    (get (run s (servicePlan s i)) i).burden = 0 ∧
      (get (run s (servicePlan s i)) i).episode = (get s i).episode := by
  by_cases hc : s.carrier = true
  · by_cases hs : readyFor s i s.selected = true
    · have heq := (ready_for_exact_packet hs).1
      have hplan : servicePlan s i = [.act (get s i).route] := by simp [servicePlan,hc,hs]
      rw [hplan]
      cases i <;> simp [run,advance,heq,capture,get,put]
    · by_cases he : readyFor s i s.evidence = true
      · have heq := (ready_for_exact_packet he).1
        have hplan : servicePlan s i = [.select,.act (get s i).route] := by simp [servicePlan,hc,hs,he]
        rw [hplan]
        cases i <;> simp [run,advance,heq,capture,get,put]
      · cases i <;> simp [servicePlan,hc,hs,he,run,advance,capture,get,put]
  · have hc0 : s.carrier = false := Bool.eq_false_iff.mpr hc
    cases i <;> simp [servicePlan,hc0,run,advance,capture,get,put]

theorem eligible_service_is_paid (s : State) (i : Patient) (h : Eligible s i) :
    (run s (servicePlan s i)).fuel + remainingCost s i = s.fuel := by
  have he := trace_exact_payment (eligible_has_actual_service_trace s i h)
  simpa only [service_plan_cost] using he

end NoninstrumentalConcern

#print axioms NoninstrumentalConcern.get_put_same
#print axioms NoninstrumentalConcern.get_put_other
#print axioms NoninstrumentalConcern.runnable_trace
#print axioms NoninstrumentalConcern.step_exact_payment
#print axioms NoninstrumentalConcern.account_law
#print axioms NoninstrumentalConcern.trace_exact_payment
#print axioms NoninstrumentalConcern.insufficient_total_cost
#print axioms NoninstrumentalConcern.read_actual_packet
#print axioms NoninstrumentalConcern.read_packet_current
#print axioms NoninstrumentalConcern.unknown_blocks_selection
#print axioms NoninstrumentalConcern.select_retains_acquired_packet
#print axioms NoninstrumentalConcern.action_has_current_authorization
#print axioms NoninstrumentalConcern.action_reduces_same_patient
#print axioms NoninstrumentalConcern.action_preserves_other_patient
#print axioms NoninstrumentalConcern.action_retires_packet
#print axioms NoninstrumentalConcern.means_stales_same_patient
#print axioms NoninstrumentalConcern.episode_stales_same_patient
#print axioms NoninstrumentalConcern.permission_preserves_factual_packet
#print axioms NoninstrumentalConcern.permission_retires_authorization
#print axioms NoninstrumentalConcern.permission_toggle_does_not_revive
#print axioms NoninstrumentalConcern.refusal_preserves_patient
#print axioms NoninstrumentalConcern.service_plan_cost
#print axioms NoninstrumentalConcern.ready_for_exact_packet
#print axioms NoninstrumentalConcern.selected_service_runnable
#print axioms NoninstrumentalConcern.evidence_service_runnable
#print axioms NoninstrumentalConcern.carrier_service_runnable
#print axioms NoninstrumentalConcern.absent_carrier_service_runnable
#print axioms NoninstrumentalConcern.eligible_has_actual_service_trace
#print axioms NoninstrumentalConcern.paid_read_keeps_service_available
#print axioms NoninstrumentalConcern.paid_selection_keeps_service_available
#print axioms NoninstrumentalConcern.eligible_service_delivers_to_same_episode
#print axioms NoninstrumentalConcern.eligible_service_is_paid
