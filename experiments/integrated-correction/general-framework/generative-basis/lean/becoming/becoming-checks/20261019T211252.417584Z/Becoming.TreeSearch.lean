import Becoming.Branching
import Becoming.Prelude

/-!
# Tree search: a finite inspection, read as the run of a determined law

A finite tree of handles is inspected entry by entry: a subtree's contents are read only when
it is opened (`Tree`, `locate`). The search keeps a frontier of entries, each an address and
the subtree there; it opens a fork into its two children, passes a closed entry and stops at the
first endpoint, within a fuel of inspections (`scan`, `discover`). It is not given a successful
address or the tree's size. Faithful inspection, and a topology that does not change during the
scan, are premises of the reading, not consequences.

* **What the search finds is there.** A frontier is coherent with a tree where each entry's
  subtree is what the tree holds below its address (`coherent`, `child_locate`); from a
  coherent frontier, a key found is the key the tree holds at the address found (`scan_sound`),
  and from a tree every key found is real (`discover_sound`).
* **Bounds.** The search inspects at most its fuel (`scan_fuel`); an address located in a tree is
  shorter than the tree's count of nodes (`located_depth_le`).
* **Exhausted is absence within the frontier, not absence.** A search that ends exhausted had no
  inhabited entry on its frontier (`exhausted_dead`); fuel at least the nodes of the frontier
  settles the search (`scan_settles`), so an inhabited tree is found with fuel its count of nodes
  (`inhabited_discovered`). A positive witness needs no complete map
  (`found_without_complete_map`), and an interrupted search is pending, not exhausted
  (`interrupted_pending`); a new address is found (`example_discovered`).
* **The search is a run.** One step of a determined law inspects the first entry (`advance`); a
  configuration with a key found or nothing left is fixed (`advance_found`, `advance_empty`).
  Along every run of the law from a frontier, step `n` reads as the scan with fuel `n`
  (`orbit_reads_scan`, `run_reads_scan`, `run_reads_discover`), so every law of the scan is a law
  of the runs: what is inspected never exceeds the step (`inspected_le_step`), what is found is located
  (`found_located`, `found_real`), exhausted is absence within the frontier
  (`exhausted_dead_run`), enough steps settle (`steps_settle`) and an inhabited tree is found
  (`inhabited_found`); the computed cases hold along every run (`found_without_reading_rest`,
  `pending_then_found`, `example_found`).

This states the search of `AcquiredCorrection` (8 October) and the joins `TreeSearchRuns` and
`TreeSearchRunsInherited` in the core (board item F3C, 18 October 2026); the dispatch is
`Becoming.Dispatch`. `locate`, `burden` and `live` are given by structural recursion, equal to
the periphery's at every argument. No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative ListTests Naturals

namespace TreeSearch

/-- A finite tree of handles: closed, an endpoint holding a key, or a fork. -/
inductive Tree where
  | closed | endpoint (key : Bool) | fork (left right : Tree)
  deriving DecidableEq

/-- An address: the turns from the root. -/
abbrev Address := List Bool
/-- A ticket: an address and the key found there. -/
abbrev Ticket := Address × Bool
/-- An entry of the frontier: an address and the subtree there. -/
abbrev Entry := Address × Tree

/-- The key at an address, if an endpoint is there. -/
def locate : Tree → Address → Option Bool
  | .closed, _ => none
  | .endpoint key, [] => some key
  | .endpoint _, _ :: _ => none
  | .fork _ _, [] => none
  | .fork l _, false :: bs => locate l bs
  | .fork _ r, true :: bs => locate r bs

/-- The count of nodes. -/
def nodes : Tree → Nat
  | .closed => 1
  | .endpoint _ => 1
  | .fork l r => 1 + nodes l + nodes r

/-- Whether some endpoint is held. -/
def inhabited : Tree → Bool
  | .closed => false
  | .endpoint _ => true
  | .fork l r => inhabited l || inhabited r

/-- The count of nodes on a frontier. -/
def burden : List Entry → Nat
  | [] => 0
  | e :: rest => nodes e.2 + burden rest

/-- Whether some entry of a frontier is inhabited. -/
def live : List Entry → Bool
  | [] => false
  | e :: rest => inhabited e.2 || live rest

/-- What a search shows: a ticket found, the frontier exhausted, or pending. -/
inductive Verdict where
  | found (ticket : Ticket) | exhausted | pending
  deriving DecidableEq

/-- A scan's verdict and the inspections it made. -/
structure Scan where
  verdict : Verdict
  inspected : Nat
  deriving DecidableEq

/-- One more inspection. -/
def bump (s : Scan) : Scan := {s with inspected := s.inspected + 1}

/-- The scan of a frontier with a fuel of inspections. -/
def scan : Nat → List Entry → Scan
  | _, [] => ⟨.exhausted, 0⟩
  | 0, _ :: _ => ⟨.pending, 0⟩
  | n + 1, (address, t) :: rest =>
    match t with
    | .closed => bump (scan n rest)
    | .endpoint key => ⟨.found (address, key), 1⟩
    | .fork l r => bump (scan n ((address ++ [false], l) :: (address ++ [true], r) :: rest))

/-- The scan of a tree. -/
def discover (fuel : Nat) (root : Tree) : Scan := scan fuel [([], root)]

/-- A frontier is coherent with a tree where each entry's subtree is what the tree holds below
its address. -/
def coherent (root : Tree) (frontier : List Entry) : Prop :=
  ∀ e, e ∈ frontier → ∀ suffix, locate root (e.1 ++ suffix) = locate e.2 suffix

/-! ## What the search finds is there -/

theorem append_assoc {α : Type} : ∀ (a b c : List α), a ++ b ++ c = a ++ (b ++ c)
  | [], _, _ => rfl
  | x :: a, b, c => congrArg (x :: ·) (append_assoc a b c)

theorem append_nil {α : Type} : ∀ (a : List α), a ++ [] = a
  | [] => rfl
  | x :: a => congrArg (x :: ·) (append_nil a)

/-- **A fork's children are what the tree holds one turn further.** -/
theorem child_locate (root : Tree) (address : Address) (l r : Tree)
    (h : ∀ suffix, locate root (address ++ suffix) = locate (.fork l r) suffix)
    (b : Bool) (suffix : Address) :
    locate root ((address ++ [b]) ++ suffix) = locate (if b then r else l) suffix :=
  match b with
  | false => (congrArg (locate root) (append_assoc address [false] suffix)).trans (h (false :: suffix))
  | true => (congrArg (locate root) (append_assoc address [true] suffix)).trans (h (true :: suffix))

/-- **The search inspects at most its fuel.** -/
theorem scan_fuel : ∀ (fuel : Nat) (frontier : List Entry), (scan fuel frontier).inspected ≤ fuel
  | 0, [] => Nat.zero_le _
  | _ + 1, [] => Nat.zero_le _
  | 0, _ :: _ => Nat.le_refl 0
  | n + 1, (_, .closed) :: rest => Nat.succ_le_succ (scan_fuel n rest)
  | _ + 1, (_, .endpoint _) :: _ => Nat.succ_le_succ (Nat.zero_le _)
  | n + 1, (a, .fork l r) :: rest =>
    Nat.succ_le_succ (scan_fuel n ((a ++ [false], l) :: (a ++ [true], r) :: rest))

theorem coherent_tail {root : Tree} {e : Entry} {rest : List Entry}
    (h : coherent root (e :: rest)) : coherent root rest :=
  fun e' m => h e' (.tail e m)

theorem coherent_fork {root : Tree} {a : Address} {l r : Tree} {rest : List Entry}
    (h : coherent root ((a, .fork l r) :: rest)) :
    coherent root ((a ++ [false], l) :: (a ++ [true], r) :: rest) := by
  intro e m suffix
  rcases mem_cons_iff.mp m with h1 | m
  · subst h1
    exact child_locate root a l r (h _ (.head _)) false suffix
  rcases mem_cons_iff.mp m with h2 | m
  · subst h2
    exact child_locate root a l r (h _ (.head _)) true suffix
  · exact h e (.tail _ m) suffix

/-- **From a coherent frontier, a key found is the key the tree holds at the address found.** -/
theorem scan_sound : ∀ (fuel : Nat) (frontier : List Entry) (root : Tree),
    coherent root frontier → ∀ (ticket : Ticket),
      (scan fuel frontier).verdict = .found ticket → locate root ticket.1 = some ticket.2
  | 0, [], _, _, _, found => nomatch found
  | _ + 1, [], _, _, _, found => nomatch found
  | 0, _ :: _, _, _, _, found => nomatch found
  | n + 1, (_, .closed) :: rest, root, h, ticket, found =>
    scan_sound n rest root (coherent_tail h) ticket found
  | _ + 1, (a, .endpoint key) :: _, root, h, ticket, found =>
    have same : (a, key) = ticket := Verdict.found.inj found
    same ▸ ((congrArg (locate root) (append_nil a).symm).trans (h _ (.head _) []))
  | n + 1, (_, .fork _ _) :: _, root, h, ticket, found =>
    scan_sound n _ root (coherent_fork h) ticket found

/-- **From a tree, every key found is real.** -/
theorem discover_sound (fuel : Nat) (root : Tree) (ticket : Ticket)
    (found : (discover fuel root).verdict = .found ticket) : locate root ticket.1 = some ticket.2 :=
  scan_sound fuel [([], root)] root
    (fun _ m _ => (mem_singleton_iff.mp m) ▸ rfl) ticket found

/-! ## Exhausted, settled, found -/

theorem or_false_iff {a b : Bool} : (a || b) = false ↔ a = false ∧ b = false :=
  false_iff_not.trans ⟨fun n => ⟨false_iff_not.mpr fun e => n (or_true_iff.mpr (.inl e)),
      false_iff_not.mpr fun e => n (or_true_iff.mpr (.inr e))⟩,
    fun ⟨x, y⟩ e => (or_true_iff.mp e).elim (fun e => Bool.noConfusion (x.symm.trans e))
      (fun e => Bool.noConfusion (y.symm.trans e))⟩

/-- **A search that ends exhausted had no inhabited entry on its frontier.** -/
theorem exhausted_dead : ∀ (fuel : Nat) (frontier : List Entry),
    (scan fuel frontier).verdict = .exhausted → live frontier = false
  | 0, [], _ => rfl
  | _ + 1, [], _ => rfl
  | 0, _ :: _, done => nomatch done
  | n + 1, (_, .closed) :: rest, done => exhausted_dead n rest done
  | _ + 1, (_, .endpoint _) :: _, done => nomatch done
  | n + 1, (_, .fork _ _) :: _, done =>
    match or_false_iff.mp (exhausted_dead n _ done) with
    | ⟨dl, rest'⟩ => match or_false_iff.mp rest' with
      | ⟨dr, dead⟩ => or_false_iff.mpr ⟨or_false_iff.mpr ⟨dl, dr⟩, dead⟩

theorem fork_burden (a : Address) (l r : Tree) (rest : List Entry) :
    burden ((a, .fork l r) :: rest) = burden ((a ++ [false], l) :: (a ++ [true], r) :: rest) + 1 :=
  show 1 + nodes l + nodes r + burden rest = nodes l + (nodes r + burden rest) + 1 from
  (Nat.add_assoc (1 + nodes l) (nodes r) (burden rest)).trans
    ((Nat.add_assoc 1 (nodes l) (nodes r + burden rest)).trans
      (Nat.add_comm 1 (nodes l + (nodes r + burden rest))))

theorem nodes_pos : ∀ t : Tree, 1 ≤ nodes t
  | .closed => Nat.le_refl 1
  | .endpoint _ => Nat.le_refl 1
  | .fork l r => Nat.le_trans (Nat.le_add_right 1 (nodes l)) (Nat.le_add_right _ (nodes r))

/-- **Fuel at least the nodes of the frontier settles the search.** -/
theorem scan_settles : ∀ (fuel : Nat) (frontier : List Entry),
    burden frontier ≤ fuel → (scan fuel frontier).verdict ≠ .pending
  | 0, [], _, e => nomatch e
  | _ + 1, [], _, e => nomatch e
  | 0, (_, t) :: rest, enough, _ => absurd (Nat.le_trans (Nat.le_trans (nodes_pos t)
      (Nat.le_add_right (nodes t) (burden rest))) enough) (Nat.not_succ_le_zero 0)
  | n + 1, (_, .closed) :: rest, enough, pending =>
    scan_settles n rest (Nat.le_of_succ_le_succ (Nat.le_trans
      (Nat.le_of_eq (Nat.add_comm (burden rest) 1)) enough)) pending
  | _ + 1, (_, .endpoint _) :: _, _, pending => nomatch pending
  | n + 1, (a, .fork l r) :: rest, enough, pending =>
    scan_settles n _ (Nat.le_of_succ_le_succ (Nat.le_trans
      (Nat.le_of_eq (fork_burden a l r rest).symm) enough)) pending

theorem live_single (root : Tree) : live [([], root)] = (inhabited root || false) := rfl

/-- **An inhabited tree is found with fuel its count of nodes, and the key found is real.** -/
theorem inhabited_discovered (fuel : Nat) (root : Tree) (enough : nodes root ≤ fuel)
    (inhabits : inhabited root = true) :
    ∃ ticket, (discover fuel root).verdict = .found ticket ∧ locate root ticket.1 = some ticket.2 :=
  match h : (discover fuel root).verdict with
  | .found ticket => ⟨ticket, rfl, discover_sound fuel root ticket h⟩
  | .exhausted =>
    absurd ((or_false_iff.mp (exhausted_dead fuel _ h)).1.symm.trans inhabits) (fun e => nomatch e)
  | .pending => absurd h (scan_settles fuel _ (show nodes root + 0 ≤ fuel from enough))

/-- **An address located in a tree is shorter than its count of nodes.** -/
theorem located_depth_le : ∀ (root : Tree) (address : Address) (key : Bool),
    locate root address = some key → address.length + 1 ≤ nodes root
  | .closed, [], _, h => nomatch h
  | .closed, _ :: _, _, h => nomatch h
  | .endpoint _, [], _, _ => Nat.le_refl 1
  | .endpoint _, _ :: _, _, h => nomatch h
  | .fork _ _, [], _, h => nomatch h
  | .fork l r, false :: bs, key, h =>
    Nat.le_trans (Nat.succ_le_succ (located_depth_le l bs key h))
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm (nodes l) 1))
        (Nat.le_add_right (1 + nodes l) (nodes r)))
  | .fork l r, true :: bs, key, h =>
    Nat.le_trans (Nat.succ_le_succ (located_depth_le r bs key h))
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm (nodes r) 1)) (Nat.add_le_add_right
        (Nat.le_add_right 1 (nodes l)) (nodes r)))

/-! ## Computed cases -/

/-- **A positive witness needs no complete map.** -/
theorem found_without_complete_map (key : Bool) (unread : Tree) :
    discover 2 (.fork (.endpoint key) unread) = ⟨.found ([false], key), 2⟩ := rfl

/-- **An interrupted search is pending, not exhausted.** -/
theorem interrupted_pending :
    discover 1 (.fork .closed (.endpoint true)) = ⟨.pending, 1⟩ ∧
    discover 3 (.fork .closed (.endpoint true)) = ⟨.found ([true], true), 3⟩ := by decide

/-- The example tree: the endpoint lies right, then left. -/
def exampleTree : Tree := .fork .closed (.fork (.endpoint true) .closed)
/-- The example's ticket. -/
def exampleTicket : Ticket := ([true, false], true)

/-- **A new address is found.** -/
theorem example_discovered : discover 4 exampleTree = ⟨.found exampleTicket, 4⟩ := by decide

/-! ## The search as the run of a determined law -/

/-- A configuration of the search: the frontier still to inspect, the ticket found, if any,
and the inspections made. -/
structure Search where
  frontier : List Entry
  found : Option Ticket
  inspected : Nat

/-- One step of the search. -/
def advance (s : Search) : Search :=
  match s.found, s.frontier with
  | some _, _ => s
  | none, [] => s
  | none, (_, .closed) :: rest => ⟨rest, none, s.inspected + 1⟩
  | none, (a, .endpoint key) :: rest => ⟨rest, some (a, key), s.inspected + 1⟩
  | none, (a, .fork l r) :: rest => ⟨(a ++ [false], l) :: (a ++ [true], r) :: rest, none, s.inspected + 1⟩

/-- The verdict a configuration shows. -/
def verdict (s : Search) : Verdict :=
  match s.found, s.frontier with
  | some t, _ => .found t
  | none, [] => .exhausted
  | none, _ :: _ => .pending

/-- What a configuration reads as a scan. -/
def read (s : Search) : Scan := ⟨verdict s, s.inspected⟩

/-- The search of a tree begins with the tree as the only entry. -/
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

/-- The orbit from a frontier, with `k` inspections already made, reads the scan of that
frontier, with `k` added to the inspections it makes. -/
theorem orbit_reads_scan_from : ∀ (n : Nat) (f : List Entry) (k : Nat),
    verdict (Law.orbit advance ⟨f, none, k⟩ n) = (scan n f).verdict ∧
      (Law.orbit advance ⟨f, none, k⟩ n).inspected = k + (scan n f).inspected
  | 0, [], _ => ⟨rfl, rfl⟩
  | 0, _ :: _, _ => ⟨rfl, rfl⟩
  | n + 1, [], k =>
      have h := orbit_fixed (advance_empty k) (n + 1)
      ⟨congrArg verdict h, congrArg Search.inspected h⟩
  | n + 1, (a, .closed) :: rest, k =>
      have shift := Law.orbit_shift advance ⟨(a, .closed) :: rest, none, k⟩ n
      have ih := orbit_reads_scan_from n rest (k + 1)
      ⟨(congrArg verdict shift).trans ih.1,
       (congrArg Search.inspected shift).trans (ih.2.trans (Nat.succ_add k (scan n rest).inspected))⟩
  | n + 1, (a, .endpoint key) :: rest, k =>
      have shift := Law.orbit_shift advance ⟨(a, .endpoint key) :: rest, none, k⟩ n
      have h := shift.trans (orbit_fixed (advance_found rest (a, key) (k + 1)) n)
      ⟨congrArg verdict h, congrArg Search.inspected h⟩
  | n + 1, (a, .fork l r) :: rest, k =>
      have shift := Law.orbit_shift advance ⟨(a, .fork l r) :: rest, none, k⟩ n
      have ih := orbit_reads_scan_from n ((a ++ [false], l) :: (a ++ [true], r) :: rest) (k + 1)
      ⟨(congrArg verdict shift).trans ih.1,
       (congrArg Search.inspected shift).trans (ih.2.trans (Nat.succ_add k
         (scan n ((a ++ [false], l) :: (a ++ [true], r) :: rest)).inspected))⟩

/-- **The orbit of the search law reads the scan.** -/
theorem orbit_reads_scan (n : Nat) (f : List Entry) :
    read (Law.orbit advance ⟨f, none, 0⟩ n) = scan n f :=
  have h := orbit_reads_scan_from n f 0
  congr (congrArg Scan.mk h.1) (h.2.trans (Nat.zero_add _))

/-- **The scan of a frontier is read off every run.** -/
theorem run_reads_scan {f : List Entry} (r : Run (Law.process advance))
    (begins : r.state 0 = ⟨f, none, 0⟩) (n : Nat) : read (r.state n) = scan n f :=
  (congrArg read ((Branching.law_run_state r n).trans
    (congrArg (fun s => Law.orbit advance s n) begins))).trans (orbit_reads_scan n f)

/-- **The scan of a tree is read off every run.** -/
theorem run_reads_discover {root : Tree} (r : Run (Law.process advance))
    (begins : r.state 0 = start root) (n : Nat) : read (r.state n) = discover n root :=
  run_reads_scan r begins n

/-- **A positive witness needs no complete map, along every run.** -/
theorem found_without_reading_rest (key : Bool) (unread : Tree) (r : Run (Law.process advance))
    (begins : r.state 0 = start (.fork (.endpoint key) unread)) :
    read (r.state 2) = ⟨.found ([false], key), 2⟩ :=
  (run_reads_discover r begins 2).trans (found_without_complete_map key unread)

/-- **An interrupted search is not an absence, along every run.** -/
theorem pending_then_found (r : Run (Law.process advance))
    (begins : r.state 0 = start (.fork .closed (.endpoint true))) :
    read (r.state 1) = ⟨.pending, 1⟩ ∧ read (r.state 3) = ⟨.found ([true], true), 3⟩ :=
  ⟨(run_reads_discover r begins 1).trans interrupted_pending.1,
   (run_reads_discover r begins 3).trans interrupted_pending.2⟩

/-- **A new address is found on every run.** -/
theorem example_found (r : Run (Law.process advance)) (begins : r.state 0 = start exampleTree) :
    read (r.state 4) = ⟨.found exampleTicket, 4⟩ :=
  (run_reads_discover r begins 4).trans example_discovered

/-! ## The laws of the scan as laws of the runs -/

section Runs

variable (r : Run (Law.process advance))

/-- **What is inspected never exceeds the step.** -/
theorem inspected_le_step {f : List Entry} (begins : r.state 0 = ⟨f, none, 0⟩) (n : Nat) :
    (r.state n).inspected ≤ n :=
  Nat.le_trans (Nat.le_of_eq (congrArg Scan.inspected (run_reads_scan r begins n))) (scan_fuel n f)

/-- **What is found is located.** -/
theorem found_located {f : List Entry} {root : Tree} (begins : r.state 0 = ⟨f, none, 0⟩)
    (fits : coherent root f) {n : Nat} {t : Ticket} (found : verdict (r.state n) = .found t) :
    locate root t.1 = some t.2 :=
  scan_sound n f root fits t ((congrArg Scan.verdict (run_reads_scan r begins n)).symm.trans found)

/-- **What is found from a tree is real.** -/
theorem found_real {root : Tree} (begins : r.state 0 = start root) {n : Nat} {t : Ticket}
    (found : verdict (r.state n) = .found t) : locate root t.1 = some t.2 :=
  discover_sound n root t ((congrArg Scan.verdict (run_reads_discover r begins n)).symm.trans found)

/-- **Exhausted is absence within the frontier.** -/
theorem exhausted_dead_run {f : List Entry} (begins : r.state 0 = ⟨f, none, 0⟩) {n : Nat}
    (done : verdict (r.state n) = .exhausted) : live f = false :=
  exhausted_dead n f ((congrArg Scan.verdict (run_reads_scan r begins n)).symm.trans done)

/-- **Enough steps settle the search.** -/
theorem steps_settle {f : List Entry} (begins : r.state 0 = ⟨f, none, 0⟩) {n : Nat}
    (enough : burden f ≤ n) : verdict (r.state n) ≠ .pending :=
  fun pending => scan_settles n f enough
    ((congrArg Scan.verdict (run_reads_scan r begins n)).symm.trans pending)

/-- **An inhabited tree is found.** -/
theorem inhabited_found {root : Tree} (begins : r.state 0 = start root) {n : Nat}
    (enough : nodes root ≤ n) (inhabits : inhabited root = true) :
    ∃ t, verdict (r.state n) = .found t ∧ locate root t.1 = some t.2 :=
  match inhabited_discovered n root enough inhabits with
  | ⟨t, found, located⟩ =>
      ⟨t, (congrArg Scan.verdict (run_reads_discover r begins n)).trans found, located⟩

end Runs

end TreeSearch

end Becoming
