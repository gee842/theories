import Becoming.ContinuingRevision

/-!
# Continuing runs: the witness of continuing revision at yield nine, read along its run

`Becoming.ContinuingRevision` states the general laws of revision supported by successful activity
(renewal and success recur along every run, no run exists with the return cut, the cycle repeats
exactly where the yield covers its use) and, at yield nine, a witness: the configurations of one
cycle at every carrier, with the amounts, methods and choices they hold, and finite controls in
which renewal without success, a cut return, an extra use of fuel or a frozen plan stops the
course. The witness has one infinite run (`ContinuingRevision.continuing`), at its cycle's start at
date `7 * n` (`ContinuingRevision.run_at_cycle`) and installed at `7 * n + 5`
(`ContinuingRevision.run_installs`). This module states the witness's facts of that run.

* **Along the run.** The configuration at every date of a cycle is that cycle's configuration
  (`run_at`). At each cycle's start the run holds fuel nine, has used `9 * n + 6`, received `9 * n`,
  and is at carrier `n` (`run_cycle_amounts`); the method changes within each cycle from `[n]` to
  `[n + 1, n]` (`run_method_changed`); the installed configuration of each cycle selects at the next
  address, which its start does not (`run_new_available_choice`), and the next cycle's start no
  longer selects at the retired address (`run_retired_choice`).
* **Controls on the run.** At each cycle's start renewal is no step: it needs a success first
  (`run_no_renewal_at_cycle`). From the configuration before each renewal, with the return cut to
  zero, renewal leaves no fuel and nothing enabled (`run_cut_renewal`), and from there the next
  undertaking is no step (`run_cut_stops`). Every course of the process ends where the executed
  moves end (`run_of_trace`); so from the run's start, one extra use of fuel before a cycle is no
  course (`run_reserve_consumed`), nor is a frozen plan from its second configuration
  (`run_frozen_no_return`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace ContinuingRuns

open ContinuingRevision (continuing clockNext expose Phase)

/-- Nothing is something. -/
theorem none_ne_some {α : Type} {a : α} (h : (none : Option α) = some a) : False := nomatch h

/-- **The configuration of the run at every date of a cycle is that cycle's configuration.** -/
theorem run_at (n k : Nat) :
    continuing.state (7 * n + k) = expose (Law.orbit clockNext (n, .ready) k) :=
  congrArg expose ((Law.orbit_add clockNext (0, .ready) (7 * n) k).trans
    (congrArg (fun q => Law.orbit clockNext q k) (ContinuingRevision.clock_cycles n)))

/-- **At each cycle's start the run holds fuel nine, has used `9 * n + 6`, received `9 * n`, and is
at carrier `n`.** -/
theorem run_cycle_amounts (n : Nat) :
    (continuing.state (7 * n)).work.fuel = 9 ∧ (continuing.state (7 * n)).work.used = 9 * n + 6 ∧
      (continuing.state (7 * n)).received = 9 * n ∧ (continuing.state (7 * n)).carrier = n :=
  Eq.subst (motive := fun s : ContinuingRevision.State =>
      s.work.fuel = 9 ∧ s.work.used = 9 * n + 6 ∧ s.received = 9 * n ∧ s.carrier = n)
    (ContinuingRevision.run_at_cycle n).symm (ContinuingRevision.all_cycles_amounts n)

/-- **The method changes within each cycle of the run**: from `[n]` at its start to `[n + 1, n]`
once planned. -/
theorem run_method_changed (n : Nat) :
    (continuing.state (7 * n + 2)).work.method = [n + 1, n] ∧
      (continuing.state (7 * n)).work.method = [n] :=
  match ContinuingRevision.method_changed n with
  | ⟨planned, ready⟩ =>
    ⟨(congrArg (fun s : ContinuingRevision.State => s.work.method) (run_at n 2)).trans planned,
     (congrArg (fun s : ContinuingRevision.State => s.work.method)
        (ContinuingRevision.run_at_cycle n)).trans ready⟩

/-- **The installed configuration of each cycle of the run selects at the next address, which the
cycle's start does not.** -/
theorem run_new_available_choice (n : Nat) :
    Learning.Training.Through (ReferencePlan.alikeOnInstalled (continuing.state (7 * n + 5)).work)
        (fun x => x (n + 1) = true) ∧
      ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled (continuing.state (7 * n)).work)
        (fun x => x (n + 1) = true) :=
  Eq.subst (motive := fun s : ContinuingRevision.State =>
      Learning.Training.Through (ReferencePlan.alikeOnInstalled s.work) (fun x => x (n + 1) = true) ∧
        ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled (continuing.state (7 * n)).work)
          (fun x => x (n + 1) = true))
    (ContinuingRevision.run_installs n).symm
    (Eq.subst (motive := fun s : ContinuingRevision.State =>
        Learning.Training.Through
            (ReferencePlan.alikeOnInstalled (ContinuingRevision.installed n).work)
            (fun x => x (n + 1) = true) ∧
          ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled s.work) (fun x => x (n + 1) = true))
      (ContinuingRevision.run_at_cycle n).symm (ContinuingRevision.new_available_choice n))

/-- **The next cycle's start no longer selects at the retired address**, which the installed
configuration of the cycle did. -/
theorem run_retired_choice (n : Nat) :
    Learning.Training.Through (ReferencePlan.alikeOnInstalled (continuing.state (7 * n + 5)).work)
        (fun x => x n = true) ∧
      ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled (continuing.state (7 * (n + 1))).work)
        (fun x => x n = true) :=
  Eq.subst (motive := fun s : ContinuingRevision.State =>
      Learning.Training.Through (ReferencePlan.alikeOnInstalled s.work) (fun x => x n = true) ∧
        ¬ Learning.Training.Through
          (ReferencePlan.alikeOnInstalled (continuing.state (7 * (n + 1))).work) (fun x => x n = true))
    (ContinuingRevision.run_installs n).symm
    (Eq.subst (motive := fun s : ContinuingRevision.State =>
        Learning.Training.Through
            (ReferencePlan.alikeOnInstalled (ContinuingRevision.installed n).work) (fun x => x n = true) ∧
          ¬ Learning.Training.Through (ReferencePlan.alikeOnInstalled s.work) (fun x => x n = true))
      (ContinuingRevision.run_at_cycle (n + 1)).symm (ContinuingRevision.retired_choice n))

/-- **At each cycle's start of the run, renewal is no step**: renewal needs a success first. -/
theorem run_no_renewal_at_cycle (n : Nat) :
    ¬ ∃ t, (ContinuingRevision.P 9).step (continuing.state (7 * n)) .renew t :=
  fun ⟨t, step⟩ => False.elim <| none_ne_some
    ((ContinuingRevision.no_return_without_success n).symm.trans
      (Eq.subst (motive := fun s => ContinuingRevision.execute 9 s .renew = some t)
        (ContinuingRevision.run_at_cycle n) step))

/-- **With the return cut to zero, renewal from the configuration before each renewal of the run
leaves no fuel and nothing enabled.** -/
theorem run_cut_renewal (n : Nat) :
    ∃ t, (ContinuingRevision.P 0).step (continuing.state (7 * n + 6)) .renew t ∧
      t.work.fuel = 0 ∧ t.enabled = false :=
  have at6 : continuing.state (7 * n + 6) = ContinuingRevision.successful n := run_at n 6
  match h : ContinuingRevision.execute 0 (ContinuingRevision.successful n) .renew with
  | some t =>
    have same : (t.work.fuel, t.enabled) = (0, false) := Option.some.inj
      ((congrArg (Option.map fun s : ContinuingRevision.State => (s.work.fuel, s.enabled)) h).symm.trans
        (ContinuingRevision.cut_return n))
    ⟨t, Eq.subst (motive := fun s => ContinuingRevision.execute 0 s .renew = some t) at6.symm h,
     congrArg Prod.fst same, congrArg Prod.snd same⟩
  | none => False.elim <| none_ne_some
      ((congrArg (Option.map fun s : ContinuingRevision.State => (s.work.fuel, s.enabled)) h).symm.trans
        (ContinuingRevision.cut_return n))

/-- **With the return cut to zero, the undertaking after renewal from the configuration before each
renewal of the run is no step.** -/
theorem run_cut_stops (n : Nat) (t : ContinuingRevision.State)
    (renewed : (ContinuingRevision.P 0).step (continuing.state (7 * n + 6)) .renew t) :
    ¬ ∃ u, (ContinuingRevision.P 0).step t (.native (.perform (t.carrier + 1) true)) u :=
  have at6 : continuing.state (7 * n + 6) = ContinuingRevision.successful n := run_at n 6
  have h : ContinuingRevision.execute 0 (ContinuingRevision.successful n) .renew = some t :=
    Eq.subst (motive := fun s => ContinuingRevision.execute 0 s .renew = some t) at6 renewed
  have stops : ContinuingRevision.execute 0 t (.native (.perform (t.carrier + 1) true)) = none :=
    (congrArg (fun o => o.bind fun s : ContinuingRevision.State =>
        ContinuingRevision.execute 0 s (.native (.perform (s.carrier + 1) true))) h).symm.trans
      (ContinuingRevision.cut_stops_next n)
  fun ⟨_, step⟩ => none_ne_some (stops.symm.trans step)

/-- **Every course of the process ends where the executed moves end.** -/
theorem run_of_trace {yield : Nat} :
    ∀ {s t : ContinuingRevision.State} {as : List ContinuingRevision.Act},
      Trace (ContinuingRevision.P yield) s as t → ContinuingRevision.run yield s as = some t
  | _, _, [], .nil _ => rfl
  | _, _, _ :: as, .cons step tail =>
    (congrArg (fun o => o.bind fun m => ContinuingRevision.run yield m as) step).trans
      (run_of_trace tail)

/-- **One extra use of fuel before a cycle is no course from the run's start.** -/
theorem run_reserve_consumed :
    ¬ ∃ t, Trace (ContinuingRevision.P 9) (continuing.state 0)
      (.native .erase :: ContinuingRevision.word 0) t :=
  fun ⟨_, path⟩ => False.elim <| none_ne_some
    (ContinuingRevision.reserve_consumed.symm.trans (run_of_trace path))

/-- **A frozen plan is no course from the run's second configuration** through use and renewal. -/
theorem run_frozen_no_return :
    ¬ ∃ t, Trace (ContinuingRevision.P 9) (continuing.state 1)
      [.native .frozen, .native .probe, .native .install, .native (.perform 1 true), .renew] t :=
  fun ⟨_, path⟩ => False.elim <| none_ne_some
    (ContinuingRevision.frozen_plan_no_return.symm.trans (run_of_trace path))

end ContinuingRuns

end Becoming
