import Std -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Stock.covered_iff_prefix`, `Becoming.Stock.covered_append`, `Becoming.Stock.repeat_covered_iff` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md

/-!
Pathwise stock requirements and repeated renewal under an explicit block contract.
This module does not formalize or import the stochastic simulator. Signed event
increments must represent actual separately timed debits, transfers and returns;
non-resource guards and supplied source/component inventories remain premises.
-/

namespace RecipientRenewal

def required : List Int → Int
  | [] => 0
  | delta :: tail => max 0 (required tail - delta)

def feasible (floor stock : Int) : List Int → Prop
  | [] => floor ≤ stock
  | delta :: tail => floor ≤ stock ∧ feasible floor (stock + delta) tail

theorem required_nonnegative (events : List Int) : 0 ≤ required events := by
  cases events <;> simp only [required] <;> omega

theorem feasible_iff_required (floor stock : Int) (events : List Int) :
    feasible floor stock events ↔ floor + required events ≤ stock := by
  induction events generalizing stock with
  | nil => simp [feasible, required]
  | cons delta tail ih =>
    simp only [feasible, required, ih]
    omega

theorem required_append (first second : List Int) :
    required (first ++ second) = max (required first) (required second - first.sum) := by
  induction first with
  | nil =>
    simp only [List.nil_append, required, List.sum_nil]
    have h := required_nonnegative second
    omega
  | cons delta tail ih =>
    simp only [List.cons_append, required, List.sum_cons, ih]
    omega

theorem feasible_append (floor stock : Int) (first second : List Int) :
    feasible floor stock (first ++ second) ↔
      feasible floor stock first ∧ feasible floor (stock + first.sum) second := by
  simp only [feasible_iff_required, required_append]
  omega

theorem final_surplus_not_prefix_solvency :
    ([-12, 20] : List Int).sum = 8 ∧ ¬ feasible 1 10 [-12, 20] := by
  simp [feasible]

def correctProbe : List Int := [-1, -1, -3, 10, -1, -1]
def failedProbe : List Int := [-1, -1, -3, -1, -1]
/- The seed transfer is a recipient debit; the seeded child's matching work
   and actual return are supplied by the block contract, not credited early. -/
def correctCopy : List Int := [-1, -1, -1, -1, -1, -5, 10, -1]
def correctionAndCopy : List Int := failedProbe ++ correctProbe ++ correctCopy

theorem correct_probe_required : required correctProbe = 5 := by decide
theorem correct_probe_sum : correctProbe.sum = 3 := by decide
theorem failed_probe_required : required failedProbe = 7 := by decide
theorem failed_probe_sum : failedProbe.sum = -7 := by decide
theorem corrected_use_required : required (failedProbe ++ correctProbe) = 12 := by decide
theorem correct_copy_required : required correctCopy = 10 := by decide
theorem correct_copy_sum : correctCopy.sum = -1 := by decide
theorem correction_copy_required : required correctionAndCopy = 14 := by decide
theorem correction_copy_sum : correctionAndCopy.sum = -5 := by decide

def warmups : Nat → List Int
  | 0 => []
  | n + 1 => correctProbe ++ warmups n

theorem warmups_sum (n : Nat) : (warmups n).sum = 3 * (n : Int) := by
  induction n with
  | zero => simp [warmups]
  | succ n ih =>
    simp only [warmups, List.sum_append, correct_probe_sum, ih]
    omega

theorem warmups_required (n : Nat) : required (warmups (n + 1)) = 5 := by
  induction n with
  | zero => decide
  | succ n ih =>
    simp only [warmups, required_append, correct_probe_required,
      correct_probe_sum] at *
    omega

def block (n : Nat) : List Int := warmups n ++ correctionAndCopy

def guard (stock : Int) (n : Nat) : Prop :=
  (n = 0 ∨ 6 ≤ stock) ∧ 15 ≤ stock + 3 * (n : Int)

theorem block_sum (n : Nat) : (block n).sum = 3 * (n : Int) - 5 := by
  simp only [block, List.sum_append, warmups_sum, correction_copy_sum]
  omega

theorem block_feasible_iff_guard (stock : Int) (n : Nat) :
    feasible 1 stock (block n) ↔ guard stock n := by
  cases n with
  | zero => simp [block, warmups, feasible_iff_required, correction_copy_required, guard]
  | succ n =>
    simp only [block, feasible_iff_required, required_append, warmups_required,
      correction_copy_required, warmups_sum, guard]
    omega

def advance (stock : Int) (n : Nat) : Int := stock + 3 * (n : Int) - 5

theorem block_endpoint (stock : Int) (n : Nat) :
    stock + (block n).sum = advance stock n := by
  simp only [block_sum, advance]
  omega

theorem two_warmup_guard (stock : Int) : guard stock 2 ↔ 9 ≤ stock := by
  simp only [guard]
  omega

theorem one_warmup_guard (stock : Int) : guard stock 1 ↔ 12 ≤ stock := by
  simp only [guard]
  omega

theorem zero_warmup_guard (stock : Int) : guard stock 0 ↔ 15 ≤ stock := by
  simp [guard]

theorem two_warmup_advance (stock : Int) : advance stock 2 = stock + 1 := by
  simp [advance]
  omega

theorem two_warmup_invariant (stock : Int) (entry : 9 ≤ stock) :
    guard stock 2 ∧ 9 ≤ advance stock 2 := by
  rw [two_warmup_guard, two_warmup_advance]
  omega

def schedule : List Nat → List Int
  | [] => []
  | n :: tail => block n ++ schedule tail

def scheduleGuard (stock : Int) : List Nat → Prop
  | [] => 1 ≤ stock
  | n :: tail => guard stock n ∧ scheduleGuard (advance stock n) tail

theorem schedule_feasible_iff (stock : Int) (ns : List Nat) :
    feasible 1 stock (schedule ns) ↔ scheduleGuard stock ns := by
  induction ns generalizing stock with
  | nil => simp [schedule, scheduleGuard, feasible]
  | cons n tail ih =>
    simp only [schedule, feasible_append, block_feasible_iff_guard,
      block_endpoint, ih, scheduleGuard]

def repeated (n : Nat) : Nat → List Nat
  | 0 => []
  | k + 1 => n :: repeated n k

theorem arbitrarily_many_finite_two_warmup_blocks (stock : Int) (entry : 9 ≤ stock)
    (generations : Nat) : feasible 1 stock (schedule (repeated 2 generations)) := by
  rw [schedule_feasible_iff]
  induction generations generalizing stock with
  | zero => simp only [repeated, scheduleGuard]; omega
  | succ k ih =>
    simp only [repeated, scheduleGuard]
    have h := two_warmup_invariant stock entry
    exact ⟨h.1, ih (advance stock 2) h.2⟩

def reserveAfter (stock : Int) (n : Nat) : Nat → Int
  | 0 => stock
  | k + 1 => advance (reserveAfter stock n k) n

theorem two_warmup_reserve (stock : Int) (k : Nat) :
    reserveAfter stock 2 k = stock + (k : Int) := by
  induction k with
  | zero => simp [reserveAfter]
  | succ k ih =>
    simp only [reserveAfter, two_warmup_advance, ih]
    omega

theorem one_warmup_reserve (stock : Int) (k : Nat) :
    reserveAfter stock 1 k = stock - 2 * (k : Int) := by
  induction k with
  | zero => simp [reserveAfter]
  | succ k ih =>
    simp only [reserveAfter, advance, ih]
    omega

theorem zero_warmup_reserve (stock : Int) (k : Nat) :
    reserveAfter stock 0 k = stock - 5 * (k : Int) := by
  induction k with
  | zero => simp [reserveAfter]
  | succ k ih =>
    simp only [reserveAfter, advance, ih]
    omega

theorem one_warmup_next_block_exact (stock : Int) (k : Nat) :
    guard (reserveAfter stock 1 k) 1 ↔ 12 + 2 * (k : Int) ≤ stock := by
  rw [one_warmup_guard, one_warmup_reserve]
  omega

theorem zero_warmup_next_block_exact (stock : Int) (k : Nat) :
    guard (reserveAfter stock 0 k) 0 ↔ 15 + 5 * (k : Int) ≤ stock := by
  rw [zero_warmup_guard, zero_warmup_reserve]
  omega

theorem one_warmup_full_schedule_exact (stock : Int) (k : Nat) :
    scheduleGuard stock (repeated 1 (k + 1)) ↔ 12 + 2 * (k : Int) ≤ stock := by
  induction k generalizing stock with
  | zero =>
    simp only [repeated, scheduleGuard, one_warmup_guard, advance]
    omega
  | succ k ih =>
    change (guard stock 1 ∧ scheduleGuard (advance stock 1) (repeated 1 (k + 1))) ↔ _
    rw [ih, one_warmup_guard]
    simp only [advance]
    omega

theorem zero_warmup_full_schedule_exact (stock : Int) (k : Nat) :
    scheduleGuard stock (repeated 0 (k + 1)) ↔ 15 + 5 * (k : Int) ≤ stock := by
  induction k generalizing stock with
  | zero =>
    simp only [repeated, scheduleGuard, zero_warmup_guard, advance]
    omega
  | succ k ih =>
    change (guard stock 0 ∧ scheduleGuard (advance stock 0) (repeated 0 (k + 1))) ↔ _
    rw [ih, zero_warmup_guard]
    simp only [advance]
    omega

theorem one_warmup_full_event_schedule_exact (stock : Int) (k : Nat) :
    feasible 1 stock (schedule (repeated 1 (k + 1))) ↔
      12 + 2 * (k : Int) ≤ stock := by
  rw [schedule_feasible_iff, one_warmup_full_schedule_exact]

theorem zero_warmup_full_event_schedule_exact (stock : Int) (k : Nat) :
    feasible 1 stock (schedule (repeated 0 (k + 1))) ↔
      15 + 5 * (k : Int) ≤ stock := by
  rw [schedule_feasible_iff, zero_warmup_full_schedule_exact]

theorem primary_two_warmup_source_account (k : Nat) :
    50 * k = 39 * k + 10 * k + k := by omega

theorem false_large_warmup_bootstrap :
    15 ≤ (5 : Int) + 3 * 10 ∧ ¬ guard 5 10 := by simp [guard]

theorem primary_one_warmup_cannot_copy : ¬ guard 10 1 := by simp [guard]
theorem primary_two_warmup_can_copy : guard 10 2 := by simp [guard]

end RecipientRenewal

#print axioms RecipientRenewal.required_nonnegative
#print axioms RecipientRenewal.feasible_iff_required
#print axioms RecipientRenewal.required_append
#print axioms RecipientRenewal.feasible_append
#print axioms RecipientRenewal.final_surplus_not_prefix_solvency
#print axioms RecipientRenewal.correct_probe_required
#print axioms RecipientRenewal.correct_probe_sum
#print axioms RecipientRenewal.failed_probe_required
#print axioms RecipientRenewal.failed_probe_sum
#print axioms RecipientRenewal.corrected_use_required
#print axioms RecipientRenewal.correct_copy_required
#print axioms RecipientRenewal.correct_copy_sum
#print axioms RecipientRenewal.correction_copy_required
#print axioms RecipientRenewal.correction_copy_sum
#print axioms RecipientRenewal.warmups_sum
#print axioms RecipientRenewal.warmups_required
#print axioms RecipientRenewal.block_sum
#print axioms RecipientRenewal.block_feasible_iff_guard
#print axioms RecipientRenewal.block_endpoint
#print axioms RecipientRenewal.two_warmup_guard
#print axioms RecipientRenewal.one_warmup_guard
#print axioms RecipientRenewal.zero_warmup_guard
#print axioms RecipientRenewal.two_warmup_advance
#print axioms RecipientRenewal.two_warmup_invariant
#print axioms RecipientRenewal.schedule_feasible_iff
#print axioms RecipientRenewal.arbitrarily_many_finite_two_warmup_blocks
#print axioms RecipientRenewal.two_warmup_reserve
#print axioms RecipientRenewal.one_warmup_reserve
#print axioms RecipientRenewal.zero_warmup_reserve
#print axioms RecipientRenewal.one_warmup_next_block_exact
#print axioms RecipientRenewal.zero_warmup_next_block_exact
#print axioms RecipientRenewal.one_warmup_full_schedule_exact
#print axioms RecipientRenewal.zero_warmup_full_schedule_exact
#print axioms RecipientRenewal.one_warmup_full_event_schedule_exact
#print axioms RecipientRenewal.zero_warmup_full_event_schedule_exact
#print axioms RecipientRenewal.primary_two_warmup_source_account
#print axioms RecipientRenewal.false_large_warmup_bootstrap
#print axioms RecipientRenewal.primary_one_warmup_cannot_copy
#print axioms RecipientRenewal.primary_two_warmup_can_copy
