import Becoming.Revision
import Becoming.Counterfactual

/-!
# Acquired consequences revise the next reference plan

An instance of the shared Process/Trace. Activity, return, retained method,
fresh reference contact, construction and later use are relations in one history.
The method is a finite list of addressed contacts, not a choice between two named
controllers. Acquired mismatch puts an address into the next executable plan.
Each planned contact acquires BOTH Boolean references; installation checks their
separation and consumes support. No generator reads the channel except through
the declared, charged contact. A repeated native history, matched frozen-method
control, erasure, exhaustion, failed separation and drift delimit the claim.

The local primitives, faithful return, two-reference binding, Boolean channel
family and revision policy are supplied. This is not their premise-free origin,
unbounded invention, a physical calibration experiment, or an attraction theorem.
-/

namespace Becoming.ReferencePlan

open Generative

def flip (key value : Bool) : Bool := if key then !value else value

theorem flip_twice (key value : Bool) : flip key (flip key value) = value := by
  cases key <;> cases value <;> rfl

structure Sample where
  address : Nat
  low : Bool
  high : Bool
  deriving DecidableEq

def valid : List Sample → Bool
  | [] => true
  | r :: rs => (r.low != r.high) && valid rs

def keyAt : List Sample → Nat → Bool
  | [], _ => false
  | r :: rs, i => if i = r.address then r.low else keyAt rs i

/-- A supplied two-point response law. The channel need not be invertible. -/
structure State where
  channel : Nat → Bool → Bool
  method : List Nat
  receipt : Option Nat
  pending : List Nat
  fresh : List Sample
  installed : List Sample
  building : Bool
  fuel : Nat
  spent : Nat
  response : Bool

inductive Act where
  | perform (address : Nat) (target : Bool)
  | revise
  | probe
  | install
  | frozen
  | erase
  | drift
  deriving DecidableEq

def cost : Act → Nat
  | .probe => 2
  | .perform _ _ => 1
  | .revise => 1
  | .install => 1
  | .frozen => 1
  | .erase => 1
  | .drift => 1

/-- A method is revised by acquired content; no current channel is consulted. -/
def propose (method : List Nat) (receipt : Option Nat) : List Nat :=
  match receipt with
  | none => method
  | some i => i :: method

/-- The uncharged part of an operation. Installation uses only fresh, bound
reference pairs; a failed separation blocks installation, not the contact cost. -/
def operate (s : State) : Act → Option State
  | .perform i target =>
    if s.building then none else
    let output := s.channel i (flip (keyAt s.installed i) target)
    some { s with response := output, receipt := if output = target then none else some i }
  | .revise =>
    match s.receipt with
    | none => none
    | some i =>
      let plan := propose s.method (some i)
      some { s with method := plan, pending := plan, fresh := [], building := true, receipt := none }
  | .probe =>
    if s.building then
      match s.pending with
      | [] => none
      | i :: tail => some { s with pending := tail, fresh := ⟨i, s.channel i false, s.channel i true⟩ :: s.fresh }
    else none
  | .install =>
    if s.building && s.pending.isEmpty && valid s.fresh then
      some { s with installed := s.fresh, building := false }
    else none
  | .frozen => some { s with pending := s.method, fresh := [], building := true, receipt := none }
  | .erase => some { s with receipt := none }
  | .drift => some { s with channel := fun i b => !(s.channel i b) }

/-- For every address, acquired content determines the next executable contact
sequence while leaving the old installed device in place until a checked commit. -/
theorem revision_binds_plan (s : State) (i : Nat) (h : s.receipt = some i) :
    (operate s .revise).map (fun t => (t.method, t.pending, t.installed)) =
      some (i :: s.method, i :: s.method, s.installed) := by
  unfold operate
  rw [h]
  rfl

theorem probe_binds_both_references (s : State) (i : Nat) (tail : List Nat)
    (active : s.building = true) (head : s.pending = i :: tail) :
    (operate s .probe).map (fun t => (t.pending, t.fresh)) =
      some (tail, ⟨i, s.channel i false, s.channel i true⟩ :: s.fresh) := by
  unfold operate
  rw [active, head]
  rfl

theorem install_binds_fresh (s : State) (active : s.building = true)
    (done : s.pending = []) (checked : valid s.fresh = true) :
    (operate s .install).map (fun t => (t.installed, t.building)) = some (s.fresh, false) := by
  unfold operate
  rw [active, done, checked]
  rfl

def execute (s : State) (a : Act) : Option State :=
  if cost a ≤ s.fuel then
    match operate s a with
    | none => none
    | some t => some { t with fuel := s.fuel - cost a, spent := s.spent + cost a }
  else none

def P : Process State Act := ⟨fun s a t => execute s a = some t⟩

theorem determined {s t u : State} {a : Act}
    (st : P.step s a t) (su : P.step s a u) : t = u :=
  Option.some.inj (st.symm.trans su)

theorem step_account {s t : State} {a : Act} (h : P.step s a t) :
    t.fuel + cost a = s.fuel ∧ t.spent = s.spent + cost a := by
  change execute s a = some t at h
  unfold execute at h
  split at h
  next enough =>
    cases eq : operate s a with
    | none => rw [eq] at h; contradiction
    | some u =>
      rw [eq] at h
      cases Option.some.inj h
      exact ⟨ExchangeLaw.sub_add_back enough, rfl⟩
  next => contradiction

theorem trace_account {s t : State} {as : List Act} (h : Trace P s as t) :
    t.fuel + t.spent = s.fuel + s.spent := by
  induction h with
  | nil => rfl
  | @cons s m t a as step tail ih =>
    obtain ⟨fuel, spent⟩ := step_account step
    rw [ih, spent, Nat.add_comm s.spent, ← Nat.add_assoc, fuel]

/-- A single policy consumes the retained method and receipt at every revision.
The sequence of ordinary undertakings is supplied separately. -/
def choose (s : State) : Option Act :=
  if s.building then
    if s.pending.isEmpty then some .install else some .probe
  else match s.receipt with
    | none => none
    | some _ => some .revise

def repair : Nat → State → Option State
  | 0, s => some s
  | n + 1, s =>
    match choose s with
    | none => none
    | some a => (execute s a).bind (repair n)

def run : State → List Act → Option State
  | s, [] => some s
  | s, a :: as => (execute s a).bind (fun t => run t as)

theorem run_trace {s t : State} {as : List Act} (h : run s as = some t) :
    Trace P s as t := by
  induction as generalizing s with
  | nil => exact (Option.some.inj h) ▸ Trace.nil s
  | cons a as ih =>
    cases eq : execute s a with
    | none => simp only [run, eq, Option.bind_none] at h; contradiction
    | some m =>
      simp only [run, eq, Option.bind_some] at h
      exact Trace.cons eq (ih h)

theorem repair_trace {n : Nat} {s t : State} (h : repair n s = some t) :
    ∃ as, Trace P s as t := by
  induction n generalizing s with
  | zero => exact ⟨[], (Option.some.inj h) ▸ Trace.nil s⟩
  | succ n ih =>
    cases chosen : choose s with
    | none => simp only [repair, chosen] at h; contradiction
    | some a =>
      cases executed : execute s a with
      | none => simp only [repair, chosen, executed, Option.bind_none] at h; contradiction
      | some m =>
        simp only [repair, chosen, executed, Option.bind_some] at h
        obtain ⟨as, path⟩ := ih h
        exact ⟨a :: as, Trace.cons executed path⟩

theorem propose_from_receipt (m : List Nat) (i : Nat) :
    propose m (some i) = i :: m := rfl

theorem propose_without_receipt (m : List Nat) : propose m none = m := rfl

/-- A two-reference candidate works at both targets precisely under the acquired
separation check. Applying this to later use also requires the channel to persist. -/
theorem checked_pair_correct (c : Bool → Bool) (separate : c false ≠ c true)
    (target : Bool) : c (flip (c false) target) = target := by
  cases lo : c false with
  | false =>
    cases hi : c true with
    | false => exact False.elim (separate (lo.trans hi.symm))
    | true => cases target <;> first | exact lo | exact hi
  | true =>
    cases hi : c true with
    | false => cases target <;> first | exact hi | exact lo
    | true => exact False.elim (separate (lo.trans hi.symm))

/-- The address domain of the installed registration. These are alternative
signals at its contacts, not claims that unseen channels were actually sampled. -/
def Alike (plan : List Nat) (x y : Nat → Bool) : Prop :=
  ∀ i, i ∈ plan → x i = y i

theorem added_keeps (m : List Nat) (i : Nat) :
    Registration.Keeps Alike m (i :: m) :=
  fun _ _ h j hj => h j (List.mem_cons_of_mem i hj)

/-- Direct reuse of P93, not a second definition of registration-based selection. -/
theorem old_selections_remain (m : List Nat) (i : Nat) :
    ∀ select, Learning.Training.Through (Alike m) select →
      Learning.Training.Through (Alike (i :: m)) select :=
  (Registration.keeps_iff
    (fun _ _ _ => rfl) (fun _ _ h j hj => (h j hj).symm)
    (fun _ _ _ h k j hj => (h j hj).trans (k j hj))).mp (added_keeps m i)

theorem choice_at_contact {m : List Nat} {i : Nat} (mem : i ∈ m) :
    Learning.Training.Through (Alike m) (fun x => x i = true) :=
  fun _ _ h => ⟨fun hx => (h i mem).symm.trans hx, fun hy => (h i mem).trans hy⟩

theorem new_contact_choice (m : List Nat) (i : Nat) (absent : i ∉ m) :
    Learning.Training.Through (Alike (i :: m)) (fun x => x i = true) ∧
      ¬ Learning.Training.Through (Alike m) (fun x => x i = true) := by
  refine ⟨choice_at_contact (List.mem_cons_self), ?_⟩
  intro through
  have same : Alike m (fun _ => false) (fun j => if j = i then true else false) := by
    intro j hj
    have ne : j ≠ i := fun eq => absent (eq ▸ hj)
    exact (if_neg ne).symm
  have bad := (through _ _ same).mpr (show (if i = i then true else false) = true from if_pos rfl)
  contradiction

/-! The native history has two repairs, no resource reset and no external
calibration labels. Both rounds use exactly `choose`. -/

def initial : State :=
  ⟨fun _ b => !b, [], none, [], [], [], false, 30, 0, false⟩

def failedFirst : State := { initial with fuel := 29, spent := 1, receipt := some 0 }

def repairedFirst : State := { failedFirst with method := [0], receipt := none, pending := [], fresh := [⟨0, true, false⟩], installed := [⟨0, true, false⟩], building := false, fuel := 25, spent := 5 }

def failedSecond : State := { repairedFirst with receipt := some 1, fuel := 23, spent := 7 }

def repairedSecond : State := { failedSecond with method := [1, 0], receipt := none, fresh := [⟨0, true, false⟩, ⟨1, true, false⟩], installed := [⟨0, true, false⟩, ⟨1, true, false⟩], fuel := 17, spent := 13 }

def finished : State := { repairedSecond with response := true, fuel := 15, spent := 15 }

theorem first_mismatch_acquired : execute initial (.perform 0 true) = some failedFirst := rfl

theorem first_policy_repair : repair 3 failedFirst = some repairedFirst := rfl

theorem first_repair_used_then_second_mismatch :
    run repairedFirst [.perform 0 true, .perform 1 true] = some failedSecond := rfl

theorem second_policy_repair : repair 4 failedSecond = some repairedSecond := rfl

theorem both_revised_contacts_used :
    run repairedSecond [.perform 1 true, .perform 0 true] = some finished := rfl

/-- The drift itself is an admitted, charged event, not an analyst replacing the
initial configuration of a failed test. The finite history starts after a checked repair. -/
theorem drift_has_actual_history :
    ∃ t, Trace P repairedFirst [.drift, .perform 0 true] t ∧ t.response = false ∧ t.receipt = some 0 :=
  ⟨{ repairedFirst with channel := fun i b => !(repairedFirst.channel i b), response := false, receipt := some 0, fuel := 23, spent := 7 }, run_trace rfl, rfl, rfl⟩

def actualWord : List Act :=
  [.perform 0 true, .revise, .probe, .install, .perform 0 true,
   .perform 1 true, .revise, .probe, .probe, .install,
   .perform 1 true, .perform 0 true]

theorem complete_history : Trace P initial actualWord finished := run_trace rfl

theorem actual_cost_without_reset : finished.fuel = 15 ∧ finished.spent = 15 := ⟨rfl, rfl⟩

theorem methods_change_twice :
    initial.method = [] ∧ repairedFirst.method = [0] ∧ repairedSecond.method = [1, 0] :=
  ⟨rfl, rfl, rfl⟩

theorem first_candidate_unavailable_before :
    keyAt initial.installed 0 = false ∧ keyAt repairedFirst.installed 0 = true ∧
    (0 ∉ initial.method) ∧ (0 ∈ repairedFirst.method) :=
  ⟨rfl, rfl, List.not_mem_nil, List.mem_cons_self⟩

theorem second_candidate_unavailable_before :
    keyAt repairedFirst.installed 1 = false ∧ keyAt repairedSecond.installed 1 = true ∧
    (1 ∉ repairedFirst.method) ∧ (1 ∈ repairedSecond.method) := by
  refine ⟨rfl, rfl, ?_, List.mem_cons_self⟩
  intro h
  cases h with
  | tail _ h => cases h

theorem first_new_selection :
    Learning.Training.Through (Alike repairedFirst.method) (fun x => x 0 = true) ∧
      ¬ Learning.Training.Through (Alike initial.method) (fun x => x 0 = true) :=
  new_contact_choice [] 0 (List.not_mem_nil)

theorem second_new_selection :
    Learning.Training.Through (Alike repairedSecond.method) (fun x => x 1 = true) ∧
      ¬ Learning.Training.Through (Alike repairedFirst.method) (fun x => x 1 = true) :=
  new_contact_choice [0] 1 second_candidate_unavailable_before.2.2.1

/-- Only constructed and installed contacts participate in this registration. -/
def registered (s : State) : (Nat → Bool) → (Nat → Bool) → Prop :=
  Alike (s.installed.map Sample.address)

theorem first_installed_choice :
    Learning.Training.Through (registered repairedFirst) (fun x => x 0 = true) ∧
      ¬ Learning.Training.Through (registered initial) (fun x => x 0 = true) :=
  first_new_selection

theorem second_installed_choice :
    Learning.Training.Through (registered repairedSecond) (fun x => x 1 = true) ∧
      ¬ Learning.Training.Through (registered repairedFirst) (fun x => x 1 = true) :=
  ⟨choice_at_contact (List.Mem.tail 0 (List.Mem.head [])), second_new_selection.2⟩

theorem installed_response_correct (target : Bool) :
    repairedFirst.channel 0 (flip (keyAt repairedFirst.installed 0) target) = target ∧
    repairedSecond.channel 0 (flip (keyAt repairedSecond.installed 0) target) = target ∧
    repairedSecond.channel 1 (flip (keyAt repairedSecond.installed 1) target) = target := by
  cases target <;> exact ⟨rfl, rfl, rfl⟩

theorem first_use_succeeds :
    (execute repairedFirst (.perform 0 true)).map (fun s => s.response) = some true := rfl

theorem second_use_succeeds :
    (execute repairedSecond (.perform 1 true)).map (fun s => s.response) = some true := rfl

/-! Controls keep genuine failures rather than declaring every revision successful. -/

def frozenEnd : State := { failedFirst with receipt := some 0, fuel := 26, spent := 4 }

theorem frozen_method_still_fails :
    run failedFirst [.frozen, .install, .perform 0 true] = some frozenEnd ∧
      frozenEnd.response = false ∧ frozenEnd.installed = [] := ⟨rfl, rfl, rfl⟩

def frozenSecondEnd : State := { failedSecond with fresh := [⟨0, true, false⟩], fuel := 18, spent := 12 }

/-- The frozen method really executes its old contact and retains the first
repair. It has MORE remaining support yet still misses the second address. -/
theorem frozen_second_method_still_fails :
    run failedSecond [.frozen, .probe, .install, .perform 1 true] = some frozenSecondEnd ∧
      frozenSecondEnd.response = false ∧ keyAt frozenSecondEnd.installed 0 = true ∧
      keyAt frozenSecondEnd.installed 1 = false := ⟨rfl, rfl, rfl, rfl⟩

theorem erased_receipt_cannot_activate :
    (execute failedFirst .erase).bind (repair 1) = none := rfl

theorem support_too_small_to_build :
    repair 3 { failedFirst with fuel := 3 } = none := rfl

theorem references_paid_before_exhaustion :
    (repair 2 { failedFirst with fuel := 3 }).map (fun s => (s.fuel, s.spent, s.installed)) =
      some (0, 4, []) := rfl

theorem no_action_after_exhaustion :
    execute { repairedFirst with fuel := 0 } (.perform 0 true) = none := rfl

theorem constant_channel_rejected :
    repair 3 { failedFirst with channel := fun _ _ => false } = none := rfl

theorem constant_channel_contacts_paid :
    (repair 2 { failedFirst with channel := fun _ _ => false }).map
      (fun s => (s.fuel, s.spent, valid s.fresh, s.installed)) =
      some (26, 4, false, []) := rfl

theorem drift_after_check_can_fail :
    (run repairedFirst [.drift, .perform 0 true]).map
      (fun s => (s.response, s.receipt, s.fuel, s.spent)) = some (false, some 0, 23, 7) := rfl

end Becoming.ReferencePlan
