import Becoming.Labelled
import Becoming.ReferencePlan
import Becoming.Stock

/-!
# Successful activity supports its next revision across carriers

This extends ReferencePlan's actual operations, not a parallel account of observation.
A successful undertaking at the next address enables one renewal, used once. Renewal uses
fuel for replacement, receives a declared return (the yield), and retains the acquired
reference for the successor. Obsolete contact records are retired: no monotonic growth of
all distinctions is assumed. A seven-operation policy history repeats at every carrier,
with new addressed method construction and cumulative amounts used and received.

The general laws come first. The fuel is a stock of `Becoming.Stock`, balanced against what
each act uses and what renewal returns (`balanced`). So, along every run at every yield,
renewal recurs (`renew_recurs`) and so does successful activity (`success_recurs`); with the
return cut no unending run exists under any controller (`no_run_without_return`). The cycle
is stated with the fuel held in reserve and the yield as parameters (`readyAt`,
`one_cycle_at`): it repeats for every number of cycles from some configuration exactly where
the yield covers the nine units a cycle uses (`repeats_iff`), at every yield. The witnesses
at yield nine, with their infinite Run, are instances and controls of these laws.

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
  enabled : Bool

inductive Act where
  | native (a : ReferencePlan.Act)
  | renew

/-- Renewal is enabled by an actual success at the next address and used once.
The retained sample is filtered from the installed device, never supplied as a correct key. -/
def execute (yield : Nat) (s : State) : Act → Option State
  | .native a =>
    match ReferencePlan.execute s.work a with
    | none => none
    | some t =>
      let enabled := match a with
        | .perform i true => if i = s.carrier + 1 then t.response else false
        | .perform _ false => false
        | .revise => false
        | .probe => false
        | .install => false
        | .frozen => false
        | .erase => false
        | .drift => false
      some { s with work := t, enabled := enabled }
  | .renew =>
    if s.enabled && !s.work.building then
      if 1 ≤ s.work.fuel then
        some { work := { s.work with method := [s.carrier + 1], mismatch := none, pending := [], fresh := s.work.installed.filter (fun r => if r.address = s.carrier + 1 then true else false), installed := s.work.installed.filter (fun r => if r.address = s.carrier + 1 then true else false), fuel := s.work.fuel - 1 + yield, used := s.work.used + 1 }, carrier := s.carrier + 1, received := s.received + yield, enabled := false }
      else none
    else none

def P (yield : Nat) : Process State Act := ⟨fun s a t => execute yield s a = some t⟩

def use : Act → Nat
  | .native a => ReferencePlan.use a
  | .renew => 1

def returned (yield : Nat) : Act → Nat
  | .native _ => 0
  | .renew => yield

theorem step_conserves {yield : Nat} {s t : State} {a : Act}
    (h : (P yield).step s a t) :
    t.work.fuel + use a = s.work.fuel + returned yield a ∧
    t.work.used = s.work.used + use a ∧
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
      obtain ⟨fuel, used⟩ := ReferencePlan.step_conserves eq
      exact ⟨fuel, used, (Nat.add_zero _).symm⟩
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
        rw [Nat.add_right_comm, Naturals.sub_add_cancel enough]
      next => contradiction
    next => contradiction

/-- Includes production explicitly; no mid-history reset of fuel is permitted. -/
theorem trace_conserves {yield : Nat} {s t : State} {as : List Act}
    (h : Trace (P yield) s as t) :
    t.work.fuel + t.work.used + s.received =
      s.work.fuel + s.work.used + t.received := by
  induction h with
  | nil => rfl
  | @cons s m t a as step tail ih =>
    obtain ⟨fuel, used, received⟩ := step_conserves step
    exact Becoming.add_right_cancel (returned yield a) (calc
      (t.work.fuel + t.work.used + s.received) + returned yield a =
          t.work.fuel + t.work.used + m.received := by rw [received, Nat.add_assoc]
      _ = m.work.fuel + m.work.used + t.received := ih
      _ = (s.work.fuel + s.work.used + t.received) + returned yield a := by
        rw [used, ← Nat.add_assoc m.work.fuel s.work.used (use a),
          Nat.add_right_comm m.work.fuel s.work.used (use a), fuel,
          Nat.add_right_comm s.work.fuel (returned yield a) s.work.used,
          Nat.add_right_comm (s.work.fuel + s.work.used) (returned yield a) t.received])

def choose (s : State) : Act :=
  if s.enabled then .renew else
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

/-! ### The cycle, with the fuel held in reserve and the yield as parameters

At carrier `n` the configuration holds fuel `m + 9`, `m` being what is held beyond the nine
units a cycle uses, has used `u` and received `g`. -/

/-- The configuration ready at carrier `n`, holding `m` beyond a cycle's use, having used `u`
and received `g`. -/
def readyAt (m u g n : Nat) : State :=
  ⟨⟨fun _ b => !b, [n], none, [], [sample n], [sample n], false, m + 9, u, true⟩,
   n, g, false⟩

def failedAt (m u g n : Nat) : State :=
  { readyAt m u g n with work := { (readyAt m u g n).work with mismatch := some (n+1), response := false, fuel := m + 8, used := u+1 } }

def plannedAt (m u g n : Nat) : State :=
  { failedAt m u g n with work := { (failedAt m u g n).work with method := [n+1,n], pending := [n+1,n], fresh := [], mismatch := none, building := true, fuel := m + 7, used := u+2 } }

def contactedAt (m u g n : Nat) : State :=
  { plannedAt m u g n with work := { (plannedAt m u g n).work with pending := [n], fresh := [sample (n+1)], fuel := m + 5, used := u+4 } }

def acquiredAt (m u g n : Nat) : State :=
  { contactedAt m u g n with work := { (contactedAt m u g n).work with pending := [], fresh := [sample n, sample (n+1)], fuel := m + 3, used := u+6 } }

def installedAt (m u g n : Nat) : State :=
  { acquiredAt m u g n with work := { (acquiredAt m u g n).work with installed := [sample n, sample (n+1)], building := false, fuel := m + 2, used := u+7 } }

def successfulAt (m u g n : Nat) : State :=
  { installedAt m u g n with work := { (installedAt m u g n).work with response := true, fuel := m + 1, used := u+8 }, enabled := true }

theorem absent_key (n : Nat) : keyAt [sample n] (n+1) = false := by
  change (if n+1 = n then true else false) = false
  exact if_neg (Naturals.succ_ne_self n)

theorem acquired_key (n : Nat) : keyAt [sample n, sample (n+1)] (n+1) = true := by
  change (if n+1 = n then true else if n+1 = n+1 then true else false) = true
  rw [if_neg (Naturals.succ_ne_self n), if_pos rfl]

theorem retained_sample (n : Nat) :
    ([sample n, sample (n+1)].filter (fun r => if r.address = n+1 then true else false)) =
      [sample (n+1)] := by
  dsimp only [List.filter, sample]
  rw [if_neg (Naturals.succ_ne_self n).symm, if_pos rfl] <;> rfl

theorem fail_step_at (y m u g n : Nat) :
    (selected y).step (readyAt m u g n) (.native (.perform (n+1) true)) (failedAt m u g n) := by
  constructor
  · change execute y (readyAt m u g n) (.native (.perform (n+1) true)) = some (failedAt m u g n)
    dsimp only [execute, ReferencePlan.execute, ReferencePlan.use, ReferencePlan.operate, readyAt]
    rw [absent_key]
    dsimp
    rw [if_pos (rfl : n+1=n+1)] <;> rfl
  · rfl

theorem plan_step_at (y m u g n : Nat) :
    (selected y).step (failedAt m u g n) (.native .revise) (plannedAt m u g n) := ⟨rfl,rfl⟩

theorem first_contact_at (y m u g n : Nat) :
    (selected y).step (plannedAt m u g n) (.native .probe) (contactedAt m u g n) := ⟨rfl,rfl⟩

theorem second_contact_at (y m u g n : Nat) :
    (selected y).step (contactedAt m u g n) (.native .probe) (acquiredAt m u g n) := ⟨rfl,rfl⟩

theorem install_step_at (y m u g n : Nat) :
    (selected y).step (acquiredAt m u g n) (.native .install) (installedAt m u g n) := ⟨rfl,rfl⟩

theorem use_step_at (y m u g n : Nat) :
    (selected y).step (installedAt m u g n) (.native (.perform (n+1) true)) (successfulAt m u g n) := by
  constructor
  · change execute y (installedAt m u g n) (.native (.perform (n+1) true)) = some (successfulAt m u g n)
    dsimp only [execute, ReferencePlan.execute, ReferencePlan.use, ReferencePlan.operate,
      installedAt, acquiredAt, contactedAt, plannedAt, failedAt, readyAt]
    rw [acquired_key]
    dsimp
    rw [if_pos (rfl : n+1=n+1)] <;> rfl
  · rfl

/-- **Renewal at yield `e + 9`** leaves `m + e` beyond the next cycle's use. -/
theorem renew_step_at (e m u g n : Nat) :
    (selected (e + 9)).step (successfulAt m u g n) .renew (readyAt (m + e) (u + 9) (g + (e + 9)) (n+1)) := by
  constructor
  · change execute (e + 9) (successfulAt m u g n) .renew = some (readyAt (m + e) (u + 9) (g + (e + 9)) (n+1))
    dsimp only [execute, successfulAt, installedAt, acquiredAt, contactedAt, plannedAt, failedAt, readyAt]
    rw [retained_sample]
    rfl
  · rfl

def word (n : Nat) : List Act :=
  [.native (.perform (n+1) true), .native .revise, .native .probe, .native .probe,
   .native .install, .native (.perform (n+1) true), .renew]

/-- **One cycle at every yield covering its use**: from `readyAt m u g n`, at yield `e + 9`,
the same seven operations reach the next carrier with `e` more held in reserve. -/
theorem one_cycle_at (e m u g n : Nat) :
    Trace (selected (e + 9)) (readyAt m u g n) (word n) (readyAt (m + e) (u + 9) (g + (e + 9)) (n+1)) :=
  .cons (fail_step_at _ m u g n) (.cons (plan_step_at _ m u g n) (.cons (first_contact_at _ m u g n)
    (.cons (second_contact_at _ m u g n) (.cons (install_step_at _ m u g n) (.cons (use_step_at _ m u g n)
      (.cons (renew_step_at e m u g n) (.nil _)))))))

def history : Nat → List Act
  | 0 => []
  | n+1 => history n ++ word n

/-- **Every number of cycles at every yield covering its use**, from any reserve. -/
theorem cycles_at (e m u g : Nat) :
    ∀ k, ∃ m' u' g', Trace (selected (e + 9)) (readyAt m u g 0) (history k) (readyAt m' u' g' k)
  | 0 => ⟨m, u, g, .nil _⟩
  | k+1 => match cycles_at e m u g k with
    | ⟨m', u', g', path⟩ => ⟨m' + e, u' + 9, g' + (e + 9),
        trace_append_iff.mpr ⟨readyAt m' u' g' k, path, one_cycle_at e m' u' g' k⟩⟩

/-! ### The witness at yield nine with no reserve -/

/-- n counts actual replacement events. The amounts used and received both retain history. -/
def ready (n : Nat) : State := readyAt 0 (9*n+6) (9*n) n

def failed (n : Nat) : State := failedAt 0 (9*n+6) (9*n) n

def planned (n : Nat) : State := plannedAt 0 (9*n+6) (9*n) n

def contacted (n : Nat) : State := contactedAt 0 (9*n+6) (9*n) n

def acquired (n : Nat) : State := acquiredAt 0 (9*n+6) (9*n) n

def installed (n : Nat) : State := installedAt 0 (9*n+6) (9*n) n

def successful (n : Nat) : State := successfulAt 0 (9*n+6) (9*n) n

theorem fail_step (n : Nat) :
    (selected 9).step (ready n) (.native (.perform (n+1) true)) (failed n) :=
  fail_step_at 9 0 (9*n+6) (9*n) n

theorem plan_step (n : Nat) : (selected 9).step (failed n) (.native .revise) (planned n) := ⟨rfl,rfl⟩

theorem first_contact (n : Nat) : (selected 9).step (planned n) (.native .probe) (contacted n) := ⟨rfl,rfl⟩

theorem second_contact (n : Nat) : (selected 9).step (contacted n) (.native .probe) (acquired n) := ⟨rfl,rfl⟩

theorem install_step (n : Nat) : (selected 9).step (acquired n) (.native .install) (installed n) := ⟨rfl,rfl⟩

theorem use_step (n : Nat) :
    (selected 9).step (installed n) (.native (.perform (n+1) true)) (successful n) :=
  use_step_at 9 0 (9*n+6) (9*n) n

theorem renew_step (n : Nat) : (selected 9).step (successful n) .renew (ready (n+1)) :=
  renew_step_at 0 0 (9*n+6) (9*n) n

/-- Every carrier, not just two chosen examples, executes the same revision policy. -/
theorem one_cycle (n : Nat) : Trace (selected 9) (ready n) (word n) (ready (n+1)) :=
  one_cycle_at 0 0 (9*n+6) (9*n) n

/-- Actual common boundary states compose; all used and received amounts survive. -/
theorem all_cycles : ∀ n, Trace (selected 9) (ready 0) (history n) (ready n)
  | 0 => .nil _
  | n+1 => trace_append_iff.mpr ⟨ready n, all_cycles n, one_cycle n⟩

theorem all_cycles_amounts (n : Nat) :
    (ready n).work.fuel = 9 ∧ (ready n).work.used = 9*n+6 ∧
    (ready n).received = 9*n ∧ (ready n).carrier = n := ⟨rfl,rfl,rfl,rfl⟩

theorem method_changed (n : Nat) :
    (planned n).work.method = [n+1,n] ∧ (ready n).work.method = [n] := ⟨rfl,rfl⟩

theorem singleton_member {x y : Nat} (h : x ∈ [y]) : x = y := by
  cases h with
  | head => rfl
  | tail _ h => cases h

theorem next_absent (n : Nat) : n+1 ∉ [n] :=
  fun h => Naturals.succ_ne_self n (singleton_member h)

theorem new_available_choice (n : Nat) :
    Learning.Training.Through (ReferencePlan.alikeOnInstalled (installed n).work)
      (fun x => x (n+1) = true) ∧
    ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled (ready n).work)
      (fun x => x (n+1) = true) :=
  ⟨choice_at_contact (List.Mem.tail n (List.Mem.head [])),
   (new_contact_choice [n] (n+1) (next_absent n)).2⟩

theorem no_return_without_success (n : Nat) : execute 9 (ready n) .renew = none := rfl

theorem cut_return (n : Nat) :
    (execute 0 (successful n) .renew).map (fun s => (s.work.fuel, s.enabled)) =
      some (0, false) := rfl

theorem cut_stops_next (n : Nat) :
    (execute 0 (successful n) .renew).bind
      (fun s => execute 0 s (.native (.perform (s.carrier+1) true))) = none := rfl

/-- Formation begins without a retained method or installed reference. The input stock
covers all five operations; there is no return before the recurrent regime starts. -/
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

/-- One actual extra use of fuel destroys the tight reserve for replacement. -/
theorem reserve_consumed :
    run 9 (ready 0) (.native .erase :: word 0) = none := rfl

theorem frozen_plan_no_return :
    run 9 (failed 0) [.native .frozen, .native .probe, .native .install,
      .native (.perform 1 true), .renew] = none := rfl

theorem retired_choice (n : Nat) :
    Learning.Training.Through (ReferencePlan.alikeOnInstalled (installed n).work)
      (fun x => x n = true) ∧
    ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled (ready (n+1)).work)
      (fun x => x n = true) := by
  have absent : n ∉ [n+1] := fun h => Naturals.succ_ne_self n (singleton_member h).symm
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

/-! ## Through the general laws of stock -/

/-- The fuel is a stock: each act uses what it uses, and renewal returns the yield. -/
theorem balanced (yield : Nat) :
    Stock.Balanced (P yield) (fun s => s.work.fuel) use (returned yield) :=
  fun _ _ _ h => (step_conserves h).1

theorem use_pos : ∀ a, 0 < use a
  | .native (.perform _ _) => Nat.succ_pos 0
  | .native .revise => Nat.succ_pos 0
  | .native .probe => Nat.succ_pos 1
  | .native .install => Nat.succ_pos 0
  | .native .frozen => Nat.succ_pos 0
  | .native .erase => Nat.succ_pos 0
  | .native .drift => Nat.succ_pos 0
  | .renew => Nat.succ_pos 0

theorem renew_of_returned {yield : Nat} : ∀ {a : Act}, 0 < returned yield a → a = .renew
  | .native _, h => absurd h (Nat.lt_irrefl 0)
  | .renew, _ => rfl

theorem no_return : ∀ (s : State) (a : Act), s.work.fuel + returned 0 a = s.work.fuel
  | _, .native _ => rfl
  | _, .renew => rfl

/-- **Instance of `Run.not_of_depletion`.** With the return cut, no unending run exists at all,
whatever the controller; `cut_stops_next` is one finite control of this law. -/
theorem no_run_without_return (r : Run (P 0)) : False :=
  Run.not_of_depletion (fun s => s.work.fuel)
    (fun s a _ h => Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right (use_pos a))
      (Nat.le_of_eq ((step_conserves h).1.trans (no_return s a)))) r

/-- **Instance of `Run.replenishes_of_draws`.** Along every run of every yield, renewal recurs. -/
theorem renew_recurs {yield : Nat} (r : Run (P yield)) : ∀ N, ∃ n, N ≤ n ∧ r.act n = .renew :=
  fun N => match Run.replenishes_of_draws (balanced yield) r
      (fun M => ⟨M, Nat.le_refl M, use_pos _⟩) N with
  | ⟨n, le, pos⟩ => ⟨n, le, renew_of_returned pos⟩

/-- Renewal is taken only where it is enabled. -/
theorem renew_needs_enabled {yield : Nat} {s t : State} (h : (P yield).step s .renew t) :
    s.enabled = true := by
  change execute yield s .renew = some t at h
  dsimp only [execute] at h
  split at h
  next cond =>
    cases hc : s.enabled with
    | true => rfl
    | false =>
      rw [hc] at cond
      exact Bool.noConfusion cond
  next => contradiction

/-- Renewal is enabled only by a successful undertaking at the next address. -/
theorem enabled_by_success {yield : Nat} {s t : State} {a : Act} (h : (P yield).step s a t)
    (enabled : t.enabled = true) :
    ∃ i, a = .native (.perform i true) ∧ t.work.response = true := by
  cases a with
  | renew =>
    change execute yield s .renew = some t at h
    dsimp only [execute] at h
    split at h
    next =>
      split at h
      next =>
        cases Option.some.inj h
        exact Bool.noConfusion enabled
      next => contradiction
    next => contradiction
  | native a =>
    change execute yield s (.native a) = some t at h
    dsimp only [execute] at h
    cases eq : ReferencePlan.execute s.work a with
    | none => rw [eq] at h; contradiction
    | some u =>
      rw [eq] at h
      cases Option.some.inj h
      cases a with
      | perform i b =>
        cases b with
        | false => exact Bool.noConfusion enabled
        | true =>
          refine ⟨i, rfl, ?_⟩
          revert enabled
          show (if i = s.carrier + 1 then u.response else false) = true → u.response = true
          split
          next => exact id
          next => exact fun c => Bool.noConfusion c
      | revise => exact Bool.noConfusion enabled
      | probe => exact Bool.noConfusion enabled
      | install => exact Bool.noConfusion enabled
      | frozen => exact Bool.noConfusion enabled
      | erase => exact Bool.noConfusion enabled
      | drift => exact Bool.noConfusion enabled

/-- **Successful activity recurs along every run of every yield.** Renewal recurs (the law of
stock), renewal needs to be enabled, and only a successful undertaking enables it. -/
theorem success_recurs {yield : Nat} (r : Run (P yield)) :
    ∀ N, ∃ n i, N ≤ n ∧ r.act n = .native (.perform i true) ∧
      (r.state (n + 1)).work.response = true :=
  fun N => match renew_recurs r (N + 1) with
  | ⟨0, le, _⟩ => absurd le (Nat.not_succ_le_zero N)
  | ⟨n + 1, le, renew⟩ =>
    have step : (P yield).step (r.state (n + 1)) .renew (r.state (n + 1 + 1)) :=
      Eq.mp (congrArg (fun a => (P yield).step (r.state (n + 1)) a (r.state (n + 1 + 1))) renew)
        (r.step (n + 1))
    match enabled_by_success (r.step n) (renew_needs_enabled step) with
    | ⟨i, act, response⟩ => ⟨n, i, Nat.le_of_succ_le_succ le, act, response⟩

theorem history_cycles : ∀ k, history k = Stock.cycles word k
  | 0 => rfl
  | k + 1 => congrArg (· ++ word k) (history_cycles k)

theorem word_use (n : Nat) : total (word n) use = 9 := rfl

theorem word_return (yield n : Nat) : total (word n) (returned yield) = yield := by
  show 0 + (0 + (0 + (0 + (0 + (0 + yield))))) = yield
  rw [Nat.zero_add, Nat.zero_add, Nat.zero_add, Nat.zero_add, Nat.zero_add, Nat.zero_add]

/-- **Instance of `Stock.cycles_need`.** The revision cycle can be repeated for every number
of cycles, from any configuration, only where the yield covers its use of nine. -/
theorem cycles_need_yield {yield : Nat} {s : State}
    (each : ∀ k, Feasible (P yield) s (history k)) : 9 ≤ yield :=
  Stock.cycles_need (balanced yield) (w := word) word_use (word_return yield)
    (fun k => history_cycles k ▸ each k)

/-- **The cycle repeats without end exactly where the yield covers its use**, at every yield:
for every number of cycles from some configuration exactly where `9 ≤ yield`. -/
theorem repeats_iff (yield : Nat) :
    (∃ s, ∀ k, Feasible (P yield) s (history k)) ↔ 9 ≤ yield :=
  ⟨fun ⟨_, each⟩ => cycles_need_yield each,
   fun le => match le_dest le with
    | ⟨e, same⟩ =>
      have shape : yield = e + 9 := same.trans (Nat.add_comm 9 e)
      ⟨readyAt 0 0 0 0, fun k => match cycles_at e 0 0 0 k with
        | ⟨m, u, g, path⟩ => ⟨readyAt m u g k,
            Eq.subst (motive := fun y => Trace (P y) (readyAt 0 0 0 0) (history k) (readyAt m u g k))
              shape.symm (forget_policy path)⟩⟩⟩

end Becoming.ContinuingRevision
