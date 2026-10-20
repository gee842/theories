import Becoming.TreeSearchRuns

/-!
# Tree search as runs: the general laws of the scan, inherited

`Becoming.TreeSearchRuns` reads `AcquiredCorrection.scan` as the run of the determined search law
`advance`: along every run beginning at a frontier with nothing found and nothing spent, step `n`
reads as the scan of that frontier with budget `n` (`run_reads_scan`, `run_reads_discover`). The
general laws of the scan are proved in `AcquiredCorrection` with non-empty axiom reports; this
module states them as laws of the runs of the search law and proves them through those theorems,
in the periphery-join ring.

* **What is spent never exceeds the step.** Along every such run, the inspections spent at step
  `n` are at most `n` (`spent_le_step`, through `AcquiredCorrection.scan_budget`).
* **What is found is located.** Along every run beginning at a frontier coherent with a tree, a
  key found at any step is the key the tree holds at the address found (`found_located`, through
  `scan_sound`); from a tree, every key found is real (`found_real`, through
  `discovered_route_is_real`).
* **Exhausted is absence within the frontier.** A step that shows the search exhausted has a
  frontier with no inhabited entry (`exhausted_dead`, through `exhausted_is_scoped_absence`).
* **Enough steps settle the search.** At a step at least the number of nodes on the frontier the
  search is not pending (`steps_settle`, through `sufficient_budget_finishes`), and from an
  inhabited tree it has found a real key (`inhabited_found`, through `reachable_route_is_found`).
* **The search's cost is the run's.** Acquisition with budget `n` charges exactly the inspections
  the run has spent at step `n` (`acquire_charges_run`, through `acquired_accounting`), and with
  budget the tree's size the run has found a ticket that a dispatch then carries out
  (`search_then_dispatch`, through `complete_finite_discovery_and_execution`).

No ethical predicate or ranking occurs. The module adds no axiom of its own; it inherits
`propext` from every theorem of `AcquiredCorrection` it uses, `Quot.sound` from `scan_budget`,
`exhausted_is_scoped_absence`, `sufficient_budget_finishes`, `reachable_route_is_found`,
`acquired_accounting` and `complete_finite_discovery_and_execution`, and `Classical.choice` from
`complete_finite_discovery_and_execution`.
-/

namespace Becoming

open Generative AcquiredCorrection

namespace TreeSearchRunsInherited

open TreeSearchRuns

variable (r : Run (Law.process advance))

/-- **What is spent never exceeds the step.** Along every run of the search law beginning at a
frontier, the inspections spent at step `n` are at most `n`. -/
theorem spent_le_step {f : List Entry} (begins : r.state 0 = ⟨f, none, 0⟩) (n : Nat) :
    (r.state n).spent ≤ n :=
  Nat.le_trans (Nat.le_of_eq (congrArg Scan.spent (run_reads_scan r begins n)))
    (scan_budget n f)

/-- **What is found is located.** Along every run of the search law beginning at a frontier
coherent with a tree, a key found at step `n` is the key the tree holds at the address found. -/
theorem found_located {f : List Entry} {root : Tree} (begins : r.state 0 = ⟨f, none, 0⟩)
    (fits : coherent root f) {n : Nat} {t : Ticket} (found : verdict (r.state n) = .found t) :
    locate root t.1 = some t.2 :=
  scan_sound n f root fits t ((congrArg Scan.verdict (run_reads_scan r begins n)).symm.trans found)

/-- **What is found from a tree is real.** Along every run of the search law beginning at a tree,
a key found at any step is the key the tree holds at the address found. -/
theorem found_real {root : Tree} (begins : r.state 0 = start root) {n : Nat} {t : Ticket}
    (found : verdict (r.state n) = .found t) : locate root t.1 = some t.2 :=
  discovered_route_is_real n root t
    ((congrArg Scan.verdict (run_reads_discover r begins n)).symm.trans found)

/-- **Exhausted is absence within the frontier.** Along every run of the search law beginning at a
frontier, a step showing the search exhausted means no entry of that frontier is inhabited. -/
theorem exhausted_dead {f : List Entry} (begins : r.state 0 = ⟨f, none, 0⟩) {n : Nat}
    (done : verdict (r.state n) = .exhausted) : live f = false :=
  exhausted_is_scoped_absence n f
    ((congrArg Scan.verdict (run_reads_scan r begins n)).symm.trans done)

/-- **Enough steps settle the search.** Along every run of the search law beginning at a frontier,
at a step at least the number of nodes on the frontier the search is not pending. -/
theorem steps_settle {f : List Entry} (begins : r.state 0 = ⟨f, none, 0⟩) {n : Nat}
    (enough : burden f ≤ n) : verdict (r.state n) ≠ .pending :=
  fun pending => sufficient_budget_finishes n f enough
    ((congrArg Scan.verdict (run_reads_scan r begins n)).symm.trans pending)

/-- **An inhabited tree is found.** Along every run of the search law beginning at an inhabited
tree, at a step at least the tree's number of nodes the search has found a key the tree holds at
the address found. -/
theorem inhabited_found {root : Tree} (begins : r.state 0 = start root) {n : Nat}
    (enough : nodes root ≤ n) (inhabits : inhabited root = true) :
    ∃ t, verdict (r.state n) = .found t ∧ locate root t.1 = some t.2 :=
  match reachable_route_is_found n root enough inhabits with
  | ⟨t, found, located⟩ =>
      ⟨t, (congrArg Scan.verdict (run_reads_discover r begins n)).trans found, located⟩

/-- **The search's cost is the run's.** Along every run of the search law beginning at a tree,
acquisition with budget `n`, where reserve and time allow it, yields the scan read at step `n` and
charges exactly the inspections the run has spent by then, in reserve, spending and time. -/
theorem acquire_charges_run {root : Tree} (begins : r.state 0 = start root) (n : Nat)
    (s : EffectiveCommand.State) (funded : n ≤ s.reserve) (timely : s.time + n ≤ s.deadline) :
    ∃ after, acquire n root s = some (read (r.state n), after) ∧
      after.reserve + (r.state n).spent = s.reserve ∧
      after.spent = s.spent + (r.state n).spent ∧
      after.time = s.time + (r.state n).spent :=
  Eq.subst (motive := fun x : Scan => ∃ after, acquire n root s = some (x, after) ∧
      after.reserve + x.spent = s.reserve ∧ after.spent = s.spent + x.spent ∧
      after.time = s.time + x.spent)
    (run_reads_discover r begins n).symm (acquired_accounting n root s funded timely)

/-- **Search then dispatch.** Along every run of the search law beginning at an inhabited tree,
with a signed, current state whose reserve and time cover twice the tree's size and three more,
acquisition with budget the tree's size yields the scan read at that step, the run has found a
ticket there, and dispatching that ticket succeeds and completes. -/
theorem search_then_dispatch {root : Tree} (begins : r.state 0 = start root)
    (s : EffectiveCommand.State) (inhabits : inhabited root = true) (signed : s.signed = true)
    (current : s.credential = s.authority) (funded : 2 * nodes root + 3 ≤ s.reserve)
    (timely : s.time + (2 * nodes root + 3) ≤ s.deadline) :
    ∃ t after, acquire (nodes root) root s = some (read (r.state (nodes root)), after) ∧
      verdict (r.state (nodes root)) = .found t ∧
      (dispatch root t after).succeeded = true ∧ (dispatch root t after).state.completed = true :=
  Eq.subst (motive := fun x : Scan => ∃ t after, acquire (nodes root) root s = some (x, after) ∧
      x.verdict = .found t ∧ (dispatch root t after).succeeded = true ∧
      (dispatch root t after).state.completed = true)
    (run_reads_discover r begins (nodes root)).symm
    (complete_finite_discovery_and_execution root s inhabits signed current funded timely)

end TreeSearchRunsInherited

end Becoming
