import Becoming.Branching
import AcquiredCorrection

/-!
# Tree search as runs: the scan of `AcquiredCorrection` is the run of a determined law

`AcquiredCorrection` scans a finite tree from a frontier of entries, opening a fork into its two
children, passing a closed entry, and stopping at the first endpoint, with a budget of `fuel`
inspections (`AcquiredCorrection.scan`, `discover`). The scan is the run of one determined law
of the spine: a configuration of the search holds its frontier, the address and key found (if
any) and the inspections spent so far, and one step inspects the first entry of the frontier
(`advance`). A configuration with a key found, or with nothing left on the frontier, is left
unchanged by the law (`advance_found`, `advance_empty`). A determined law is a process of the
spine (`Law.process`), and every run of it is its orbit (`Branching.law_run_state`).

* **The scan is read off the run.** Along every run of the search law beginning at a tree, the
  verdict and the inspections spent at step `n` are the scan of that tree with budget `n`
  (`run_reads_discover`, from `orbit_reads_scan` and `run_reads_scan` for any frontier): a budget
  is a step of the run.
* **A positive witness needs no complete map.** Along every run beginning at a fork whose left
  child is an endpoint, step 2 has found that endpoint's address and key, whatever the right
  child is (`found_without_reading_rest`, through
  `AcquiredCorrection.positive_witness_needs_no_complete_map`).
* **An interrupted search is not an absence.** Along every run beginning at a fork with a closed
  left child and an endpoint right child, step 1 is pending and step 3 has found the endpoint
  (`pending_then_found`, through `AcquiredCorrection.interrupted_is_not_absent`).
* **A new address is found on the run.** Along every run beginning at the module's example tree,
  step 4 has found its endpoint at an address not given in advance (`example_found`, through
  `AcquiredCorrection.acquired_new_address`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative AcquiredCorrection

namespace TreeSearchRuns

/-- A configuration of the search: the frontier still to inspect, the address and key found, if
any, and the inspections spent. -/
structure Search where
  frontier : List Entry
  found : Option Ticket
  spent : Nat

/-- One step of the search: with a key found, or nothing left, the configuration is unchanged;
otherwise the first entry is inspected, at the cost of one inspection. A closed entry is passed,
an endpoint is found, and a fork is replaced by its two children. -/
def advance (s : Search) : Search :=
  match s.found, s.frontier with
  | some _, _ => s
  | none, [] => s
  | none, (_, .closed) :: rest => ⟨rest, none, s.spent + 1⟩
  | none, (a, .endpoint key) :: rest => ⟨rest, some (a, key), s.spent + 1⟩
  | none, (a, .fork l r) :: rest => ⟨(a ++ [false], l) :: (a ++ [true], r) :: rest, none, s.spent + 1⟩

/-- The verdict a configuration of the search shows: found, exhausted where nothing is left, and
pending otherwise. -/
def verdict (s : Search) : Verdict :=
  match s.found, s.frontier with
  | some t, _ => .found t
  | none, [] => .exhausted
  | none, _ :: _ => .pending

/-- What a configuration of the search reads as a scan: its verdict and the inspections spent. -/
def read (s : Search) : Scan := ⟨verdict s, s.spent⟩

/-- The search of a tree begins with the tree as the only entry, nothing found, nothing spent. -/
def start (root : Tree) : Search := ⟨[([], root)], none, 0⟩

/-- **A search that has found a key is left unchanged.** -/
theorem advance_found (f : List Entry) (t : Ticket) (k : Nat) :
    advance ⟨f, some t, k⟩ = ⟨f, some t, k⟩ := rfl

/-- **A search with nothing left is left unchanged.** -/
theorem advance_empty (k : Nat) : advance ⟨[], none, k⟩ = ⟨[], none, k⟩ := rfl

/-- A configuration the law leaves unchanged is its whole orbit. -/
theorem orbit_fixed {s : Search} (fixed : advance s = s) : ∀ n, Law.orbit advance s n = s
  | 0 => rfl
  | n + 1 => (congrArg advance (orbit_fixed fixed n)).trans fixed

/-- The orbit from a frontier, with `k` already spent, reads the scan of that frontier, with `k`
added to what it spends. -/
theorem orbit_reads_scan_from : ∀ (n : Nat) (f : List Entry) (k : Nat),
    verdict (Law.orbit advance ⟨f, none, k⟩ n) = (scan n f).verdict ∧
      (Law.orbit advance ⟨f, none, k⟩ n).spent = k + (scan n f).spent
  | 0, [], _ => ⟨rfl, rfl⟩
  | 0, _ :: _, _ => ⟨rfl, rfl⟩
  | n + 1, [], k =>
      have h := orbit_fixed (advance_empty k) (n + 1)
      ⟨congrArg verdict h, congrArg Search.spent h⟩
  | n + 1, (a, .closed) :: rest, k =>
      have shift := Law.orbit_shift advance ⟨(a, .closed) :: rest, none, k⟩ n
      have ih := orbit_reads_scan_from n rest (k + 1)
      ⟨(congrArg verdict shift).trans ih.1,
       (congrArg Search.spent shift).trans (ih.2.trans (Nat.succ_add k (scan n rest).spent))⟩
  | n + 1, (a, .endpoint key) :: rest, k =>
      have shift := Law.orbit_shift advance ⟨(a, .endpoint key) :: rest, none, k⟩ n
      have h := shift.trans (orbit_fixed (advance_found rest (a, key) (k + 1)) n)
      ⟨congrArg verdict h, congrArg Search.spent h⟩
  | n + 1, (a, .fork l r) :: rest, k =>
      have shift := Law.orbit_shift advance ⟨(a, .fork l r) :: rest, none, k⟩ n
      have ih := orbit_reads_scan_from n ((a ++ [false], l) :: (a ++ [true], r) :: rest) (k + 1)
      ⟨(congrArg verdict shift).trans ih.1,
       (congrArg Search.spent shift).trans (ih.2.trans (Nat.succ_add k
         (scan n ((a ++ [false], l) :: (a ++ [true], r) :: rest)).spent))⟩

/-- **The orbit of the search law reads the scan.** From a frontier with nothing spent, the
configuration `n` steps on reads as the scan of that frontier with budget `n`. -/
theorem orbit_reads_scan (n : Nat) (f : List Entry) :
    read (Law.orbit advance ⟨f, none, 0⟩ n) = scan n f :=
  have h := orbit_reads_scan_from n f 0
  congr (congrArg Scan.mk h.1) (h.2.trans (Nat.zero_add _))

/-- **The scan of a frontier is read off every run.** Along every run of the search law beginning
at a frontier with nothing found and nothing spent, the configuration at step `n` reads as the
scan of that frontier with budget `n`. -/
theorem run_reads_scan {f : List Entry} (r : Run (Law.process advance))
    (begins : r.state 0 = ⟨f, none, 0⟩) (n : Nat) : read (r.state n) = scan n f :=
  (congrArg read ((Branching.law_run_state r n).trans
    (congrArg (fun s => Law.orbit advance s n) begins))).trans (orbit_reads_scan n f)

/-- **The scan is read off every run.** Along every run of the search law beginning at a tree, the
configuration at step `n` reads as the scan of the tree with budget `n`. -/
theorem run_reads_discover {root : Tree} (r : Run (Law.process advance))
    (begins : r.state 0 = start root) (n : Nat) : read (r.state n) = discover n root :=
  run_reads_scan r begins n

/-- **A positive witness needs no complete map.** Along every run beginning at a fork whose left
child is an endpoint, step 2 has found the endpoint's address and key at the cost of two
inspections, whatever the right child is. -/
theorem found_without_reading_rest (key : Bool) (unread : Tree) (r : Run (Law.process advance))
    (begins : r.state 0 = start (.fork (.endpoint key) unread)) :
    read (r.state 2) = ⟨.found ([false], key), 2⟩ :=
  (run_reads_discover r begins 2).trans (positive_witness_needs_no_complete_map key unread)

/-- **An interrupted search is not an absence.** Along every run beginning at a fork with a closed
left child and an endpoint right child, step 1 is pending, not exhausted, and step 3 has found
the endpoint. -/
theorem pending_then_found (r : Run (Law.process advance))
    (begins : r.state 0 = start (.fork .closed (.endpoint true))) :
    read (r.state 1) = ⟨.pending, 1⟩ ∧ read (r.state 3) = ⟨.found ([true], true), 3⟩ :=
  ⟨(run_reads_discover r begins 1).trans interrupted_is_not_absent.1,
   (run_reads_discover r begins 3).trans interrupted_is_not_absent.2⟩

/-- **A new address is found on the run.** Along every run beginning at the example tree, step 4
has found its endpoint, at an address the search was not given, with four inspections. -/
theorem example_found (r : Run (Law.process advance)) (begins : r.state 0 = start exampleTree) :
    read (r.state 4) = ⟨.found exampleTicket, 4⟩ :=
  (run_reads_discover r begins 4).trans acquired_new_address

end TreeSearchRuns

end Becoming
