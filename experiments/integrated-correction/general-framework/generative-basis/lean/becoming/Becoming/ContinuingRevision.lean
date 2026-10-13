import Becoming.ReferencePlan

/-!
# Successful activity supports its next revision across carriers

This extends ReferencePlan's actual operations, not a parallel account of observation.
A successful undertaking at the next address earns one consumable claim on production.
Realizing it pays for replacement, receives a declared return, and retains the acquired
reference for the successor. Obsolete contact records are retired: no monotonic growth of
all distinctions is assumed. A seven-operation policy history repeats at every carrier,
with new addressed method construction, unchanged budget units and cumulative accounts.

The production relation, succession/retirement rule, stable Boolean contacts, faithful
return and controller are supplied local laws. The return is not creation from nothing:
the counted installation is open to the productive relationship. No finite closed stock
or arbitrary physical world is claimed to support unending production. Cutting this
return closes the next inquiry despite a successful preceding repair.
-/

namespace Becoming.ContinuingRevision

open Generative
open ReferencePlan

structure State where
  work : ReferencePlan.State
  carrier : Nat
  received : Nat
  credit : Bool

inductive Act where
  | native (a : ReferencePlan.Act)
  | renew

/-- The right to receive production is earned by actual successful work, and consumed.
The retained sample is filtered from the installed device, never supplied as a correct key. -/
def execute (yield : Nat) (s : State) : Act → Option State
  | .native a =>
    match ReferencePlan.execute s.work a with
    | none => none
    | some t =>
      let credit := match a with
        | .perform i true => if i = s.carrier + 1 then t.response else false
        | .perform _ false => false
        | .revise => false
        | .probe => false
        | .install => false
        | .frozen => false
        | .erase => false
        | .drift => false
      some { s with work := t, credit := credit }
  | .renew =>
    if s.credit && !s.work.building then
      if 1 ≤ s.work.fuel then
        some { work := { s.work with method := [s.carrier + 1], receipt := none, pending := [], fresh := s.work.installed.filter (fun r => if r.address = s.carrier + 1 then true else false), installed := s.work.installed.filter (fun r => if r.address = s.carrier + 1 then true else false), fuel := s.work.fuel - 1 + yield, spent := s.work.spent + 1 }, carrier := s.carrier + 1, received := s.received + yield, credit := false }
      else none
    else none

def P (yield : Nat) : Process State Act := ⟨fun s a t => execute yield s a = some t⟩

def cost : Act → Nat
  | .native a => ReferencePlan.cost a
  | .renew => 1

def returned (yield : Nat) : Act → Nat
  | .native _ => 0
  | .renew => yield

theorem step_account {yield : Nat} {s t : State} {a : Act}
    (h : (P yield).step s a t) :
    t.work.fuel + cost a = s.work.fuel + returned yield a ∧
    t.work.spent = s.work.spent + cost a ∧
    t.received = s.received + returned yield a := by
  cases a with
  | native a =>
    change execute yield s (.native a) = some t at h
    dsimp only [execute] at h
    cases eq : ReferencePlan.execute s.work a with
    | none => rw [eq] at h; contradiction
    | some u =>
      rw [eq] at h
      cases Option.some.inj h
      obtain ⟨fuel, spent⟩ := ReferencePlan.step_account eq
      exact ⟨fuel, spent, (Nat.add_zero _).symm⟩
  | renew =>
    change execute yield s .renew = some t at h
    dsimp only [execute] at h
    split at h
    next =>
      split at h
      next enough =>
        cases Option.some.inj h
        refine ⟨?_, rfl, rfl⟩
        change (s.work.fuel - 1 + yield) + 1 = s.work.fuel + yield
        rw [Nat.add_right_comm, ExchangeLaw.sub_add_back enough]
      next => contradiction
    next => contradiction

/-- Includes production explicitly; no mid-history resource reset is permitted. -/
theorem trace_account {yield : Nat} {s t : State} {as : List Act}
    (h : Trace (P yield) s as t) :
    t.work.fuel + t.work.spent + s.received =
      s.work.fuel + s.work.spent + t.received := by
  induction h with
  | nil => rfl
  | @cons s m t a as step tail ih =>
    obtain ⟨fuel, spent, received⟩ := step_account step
    exact Becoming.add_right_cancel (returned yield a) (calc
      (t.work.fuel + t.work.spent + s.received) + returned yield a =
          t.work.fuel + t.work.spent + m.received := by rw [received, Nat.add_assoc]
      _ = m.work.fuel + m.work.spent + t.received := ih
      _ = (s.work.fuel + s.work.spent + t.received) + returned yield a := by
        rw [spent, ← Nat.add_assoc m.work.fuel s.work.spent (cost a),
          Nat.add_right_comm m.work.fuel s.work.spent (cost a), fuel,
          Nat.add_right_comm s.work.fuel (returned yield a) s.work.spent,
          Nat.add_right_comm (s.work.fuel + s.work.spent) (returned yield a) t.received])

def choose (s : State) : Act :=
  if s.credit then .renew else
    match ReferencePlan.choose s.work with
    | some a => .native a
    | none => .native (.perform (s.carrier + 1) true)

/-- Policy restriction of the SAME process; the policy is a disclosed premise. -/
def selected (yield : Nat) : Process State Act :=
  ⟨fun s a t => (P yield).step s a t ∧ a = choose s⟩

theorem forget_policy {yield : Nat} {s t : State} {as : List Act}
    (h : Trace (selected yield) s as t) : Trace (P yield) s as t := by
  induction h with
  | nil s => exact .nil s
  | cons step tail ih => exact .cons step.1 ih

def sample (n : Nat) : Sample := ⟨n, true, false⟩

/-- n counts actual replacement events. The support and return ledgers both retain history. -/
def ready (n : Nat) : State :=
  ⟨⟨fun _ b => !b, [n], none, [], [sample n], [sample n], false, 9, 9*n+6, true⟩,
   n, 9*n, false⟩

def failed (n : Nat) : State :=
  { ready n with work := { (ready n).work with receipt := some (n+1), response := false, fuel := 8, spent := 9*n+6+1 } }

def planned (n : Nat) : State :=
  { failed n with work := { (failed n).work with method := [n+1,n], pending := [n+1,n], fresh := [], receipt := none, building := true, fuel := 7, spent := 9*n+6+2 } }

def contacted (n : Nat) : State :=
  { planned n with work := { (planned n).work with pending := [n], fresh := [sample (n+1)], fuel := 5, spent := 9*n+6+4 } }

def acquired (n : Nat) : State :=
  { contacted n with work := { (contacted n).work with pending := [], fresh := [sample n, sample (n+1)], fuel := 3, spent := 9*n+6+6 } }

def installed (n : Nat) : State :=
  { acquired n with work := { (acquired n).work with installed := [sample n, sample (n+1)], building := false, fuel := 2, spent := 9*n+6+7 } }

def successful (n : Nat) : State :=
  { installed n with work := { (installed n).work with response := true, fuel := 1, spent := 9*n+6+8 }, credit := true }

theorem next_ne (n : Nat) : n+1 ≠ n := Nat.succ_ne_self n

theorem absent_key (n : Nat) : keyAt [sample n] (n+1) = false := by
  change (if n+1 = n then true else false) = false
  exact if_neg (next_ne n)

theorem acquired_key (n : Nat) : keyAt [sample n, sample (n+1)] (n+1) = true := by
  change (if n+1 = n then true else if n+1 = n+1 then true else false) = true
  rw [if_neg (next_ne n), if_pos rfl]

theorem retained_sample (n : Nat) :
    ([sample n, sample (n+1)].filter (fun r => if r.address = n+1 then true else false)) =
      [sample (n+1)] := by
  dsimp only [List.filter, sample]
  rw [if_neg (next_ne n).symm, if_pos rfl] <;> rfl

theorem fail_step (n : Nat) :
    (selected 9).step (ready n) (.native (.perform (n+1) true)) (failed n) := by
  constructor
  · change execute 9 (ready n) (.native (.perform (n+1) true)) = some (failed n)
    dsimp only [execute, ReferencePlan.execute, ReferencePlan.cost, ReferencePlan.operate, ready]
    rw [absent_key]
    dsimp
    rw [if_pos (rfl : n+1=n+1)] <;> rfl
  · rfl

theorem plan_step (n : Nat) : (selected 9).step (failed n) (.native .revise) (planned n) := ⟨rfl,rfl⟩

theorem first_contact (n : Nat) : (selected 9).step (planned n) (.native .probe) (contacted n) := ⟨rfl,rfl⟩

theorem second_contact (n : Nat) : (selected 9).step (contacted n) (.native .probe) (acquired n) := ⟨rfl,rfl⟩

theorem install_step (n : Nat) : (selected 9).step (acquired n) (.native .install) (installed n) := ⟨rfl,rfl⟩

theorem use_step (n : Nat) :
    (selected 9).step (installed n) (.native (.perform (n+1) true)) (successful n) := by
  constructor
  · change execute 9 (installed n) (.native (.perform (n+1) true)) = some (successful n)
    dsimp only [execute, ReferencePlan.execute, ReferencePlan.cost, ReferencePlan.operate,
      installed, acquired, contacted, planned, failed, ready]
    rw [acquired_key]
    dsimp
    rw [if_pos (rfl : n+1=n+1)] <;> rfl
  · rfl

theorem renew_step (n : Nat) : (selected 9).step (successful n) .renew (ready (n+1)) := by
  constructor
  · change execute 9 (successful n) .renew = some (ready (n+1))
    dsimp only [execute, successful, installed, acquired, contacted, planned, failed, ready]
    rw [retained_sample]
    have hr : 9*n+9 = 9*(n+1) := (Nat.mul_succ 9 n).symm
    have hs : 9*n+6+8+1 = 9*(n+1)+6 := calc
      9*n+6+8+1 = 9*n+6+9 := rfl
      _ = 9*n+9+6 := Nat.add_right_comm (9*n) 6 9
      _ = 9*(n+1)+6 := congrArg (fun k => k+6) hr
    rw [hs, hr] <;> rfl
  · rfl

def word (n : Nat) : List Act :=
  [.native (.perform (n+1) true), .native .revise, .native .probe, .native .probe,
   .native .install, .native (.perform (n+1) true), .renew]

/-- Every carrier, not just two chosen examples, executes the same revision policy. -/
theorem one_cycle (n : Nat) : Trace (selected 9) (ready n) (word n) (ready (n+1)) :=
  .cons (fail_step n) (.cons (plan_step n) (.cons (first_contact n)
    (.cons (second_contact n) (.cons (install_step n) (.cons (use_step n)
      (.cons (renew_step n) (.nil _)))))))

def history : Nat → List Act
  | 0 => []
  | n+1 => history n ++ word n

/-- Actual common boundary states compose; all consumed and received support survives. -/
theorem all_cycles : ∀ n, Trace (selected 9) (ready 0) (history n) (ready n)
  | 0 => .nil _
  | n+1 => trace_append_iff.mpr ⟨ready n, all_cycles n, one_cycle n⟩

theorem all_cycles_account (n : Nat) :
    (ready n).work.fuel = 9 ∧ (ready n).work.spent = 9*n+6 ∧
    (ready n).received = 9*n ∧ (ready n).carrier = n := ⟨rfl,rfl,rfl,rfl⟩

theorem method_changed (n : Nat) :
    (planned n).work.method = [n+1,n] ∧ (ready n).work.method = [n] := ⟨rfl,rfl⟩

theorem singleton_member {x y : Nat} (h : x ∈ [y]) : x = y := by
  cases h with
  | head => rfl
  | tail _ h => cases h

theorem next_absent (n : Nat) : n+1 ∉ [n] :=
  fun h => next_ne n (singleton_member h)

theorem new_available_choice (n : Nat) :
    Learning.Training.Through (ReferencePlan.registered (installed n).work)
      (fun x => x (n+1) = true) ∧
    ¬ Learning.Training.Through (ReferencePlan.registered (ready n).work)
      (fun x => x (n+1) = true) :=
  ⟨choice_at_contact (List.Mem.tail n (List.Mem.head [])),
   (new_contact_choice [n] (n+1) (next_absent n)).2⟩

theorem no_unearned_return (n : Nat) : execute 9 (ready n) .renew = none := rfl

theorem cut_return (n : Nat) :
    (execute 0 (successful n) .renew).map (fun s => (s.work.fuel, s.credit)) =
      some (0, false) := rfl

theorem cut_stops_next (n : Nat) :
    (execute 0 (successful n) .renew).bind
      (fun s => execute 0 s (.native (.perform (s.carrier+1) true))) = none := rfl

/-- Formation begins without a retained method or installed reference. The input stock
pays all five operations; there is no earned return before the recurrent regime starts. -/
def seed : State :=
  ⟨⟨fun _ b => !b, [], none, [], [], [], false, 15, 0, false⟩, 0, 0, false⟩

def run (yield : Nat) : State → List Act → Option State
  | s, [] => some s
  | s, a::as => (execute yield s a).bind (fun t => run yield t as)

theorem run_trace {yield : Nat} {s t : State} {as : List Act}
    (h : run yield s as = some t) : Trace (P yield) s as t := by
  induction as generalizing s with
  | nil => cases Option.some.inj h; exact .nil _
  | cons a as ih =>
    cases eq : execute yield s a with
    | none => change (execute yield s a).bind _ = some t at h; rw [eq] at h; contradiction
    | some m =>
      change (execute yield s a).bind _ = some t at h
      rw [eq] at h
      exact .cons eq (ih h)

def formation : List Act :=
  [.native (.perform 0 true), .native .revise, .native .probe,
   .native .install, .native (.perform 0 true)]

theorem formation_enters : Trace (P 9) seed formation (ready 0) := run_trace rfl

theorem formed_and_continues (n : Nat) :
    Trace (P 9) seed (formation ++ history n) (ready n) :=
  trace_append_iff.mpr ⟨ready 0, formation_enters, forget_policy (all_cycles n)⟩

/-- One actual extra expenditure destroys the tight reserve for replacement. -/
theorem reserve_consumed :
    run 9 (ready 0) (.native .erase :: word 0) = none := rfl

theorem frozen_plan_no_return :
    run 9 (failed 0) [.native .frozen, .native .probe, .native .install,
      .native (.perform 1 true), .renew] = none := rfl

theorem retired_choice (n : Nat) :
    Learning.Training.Through (ReferencePlan.registered (installed n).work)
      (fun x => x n = true) ∧
    ¬ Learning.Training.Through (ReferencePlan.registered (ready (n+1)).work)
      (fun x => x n = true) := by
  have absent : n ∉ [n+1] := fun h => next_ne n (singleton_member h).symm
  exact ⟨choice_at_contact (List.Mem.head _), (new_contact_choice [n+1] n absent).2⟩

/-- A clock only enumerates the already policy-checked seven operations; it adds no
action or support to the process. -/
inductive Phase where
  | ready | failed | planned | contacted | acquired | installed | successful

def clockNext : Nat × Phase → Nat × Phase
  | (n, .ready) => (n, .failed)
  | (n, .failed) => (n, .planned)
  | (n, .planned) => (n, .contacted)
  | (n, .contacted) => (n, .acquired)
  | (n, .acquired) => (n, .installed)
  | (n, .installed) => (n, .successful)
  | (n, .successful) => (n+1, .ready)

def expose : Nat × Phase → State
  | (n, .ready) => ready n
  | (n, .failed) => failed n
  | (n, .planned) => planned n
  | (n, .contacted) => contacted n
  | (n, .acquired) => acquired n
  | (n, .installed) => installed n
  | (n, .successful) => successful n

def action : Nat × Phase → Act
  | (n, .ready) => .native (.perform (n+1) true)
  | (_, .failed) => .native .revise
  | (_, .planned) => .native .probe
  | (_, .contacted) => .native .probe
  | (_, .acquired) => .native .install
  | (n, .installed) => .native (.perform (n+1) true)
  | (_, .successful) => .renew

theorem clock_step : ∀ q, (selected 9).step (expose q) (action q) (expose (clockNext q))
  | (n, .ready) => fail_step n
  | (n, .failed) => plan_step n
  | (n, .planned) => first_contact n
  | (n, .contacted) => second_contact n
  | (n, .acquired) => install_step n
  | (n, .installed) => use_step n
  | (n, .successful) => renew_step n

/-- One actual infinite Run under the supplied productive law and selected controller.
This is stronger than separately feasible finite paths selected by an existence axiom. -/
def continuing : Run (selected 9) :=
  ⟨fun t => expose (Law.orbit clockNext (0, .ready) t),
   fun t => action (Law.orbit clockNext (0, .ready) t),
   fun t => clock_step (Law.orbit clockNext (0, .ready) t)⟩

theorem clock_cycles : ∀ n, Law.orbit clockNext (0, .ready) (7*n) = (n, .ready)
  | 0 => rfl
  | n+1 => by
    rw [Nat.mul_succ, Law.orbit_add, clock_cycles n]
    rfl

theorem run_at_cycle (n : Nat) : continuing.state (7*n) = ready n :=
  congrArg expose (clock_cycles n)

theorem run_installs (n : Nat) : continuing.state (7*n+5) = installed n := by
  change expose (Law.orbit clockNext (0, .ready) (7*n+5)) = installed n
  rw [Law.orbit_add, clock_cycles]
  rfl

theorem unbounded_succession (n : Nat) : (continuing.state (7*n)).carrier = n :=
  congrArg State.carrier (run_at_cycle n)

theorem formation_to_run : Trace (P 9) seed formation (continuing.state 0) := formation_enters

end Becoming.ContinuingRevision
