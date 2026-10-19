import Becoming.Branching
import Becoming.Readout
import Becoming.Integers

/-!
# Dephasing: what a reduction of a two-branch control keeps, loses and can recover

An exact real-amplitude fragment of a controlled-order calculation, with integers for unnormalised
amplitudes and density numerators: a two-branch control (`Joint`), its control matrix
(`controlDensity`, the partial trace over the target), dephasing (`dephase`, which keeps the
diagonal and drops the cross terms), the plus/minus response, and a reversible recording
interaction (`recordBranch`, a controlled X onto a blank register). Dephasing and recording are
steps of change, so each is a determined law of the spine (`Law.process`), whose runs are its
orbits (`Branching.law_run_state`); the operations are the moves of a process that applies one
at each step (`operations`). Board item F3R (18 October 2026) states here, on the core's laws and
with constructive proofs (`Becoming.Integers`), what `OperativeCoherence` (8 October) checked and
what the joins `DephasingRuns` and `DephasingRunsInherited` (17 October) read of its runs.

* **The algebra.** X and Z keep the norm and anticommute (`x_preserves_norm`,
  `z_preserves_norm`, `xz_anticommute`); the Hadamard step on a control with a blank branch
  prepares the joint (`preparation_from_blank`); the switched order of X and Z negates the
  control's off-diagonal entries (`switched_density`); the plus and minus responses sum to twice
  the total weight (`response_mass_conserved`); dephasing keeps the diagonal and the weight
  (`dephase_preserves_diagonal`, `dephase_preserves_mass`), sets both responses to the weight
  (`dephase_response`), and keeps the plus response exactly where the cross terms sum to zero
  (`dephase_keeps_response_iff`). Keeping the cross term is enough for that response
  (`retained_response_exact`).
* **What dephasing loses, as instances of `Becoming.Readout`.** The diagonal merges the coherent
  and the degraded control, whose responses differ, so no decoder of the response reads the
  diagonal (`no_diagonal_response_decoder`); dephasing merges the prepared and the coherent
  control, so nothing restores them from its output (`no_uniform_dephase_inverse`).
* **Recording.** Reducing after the recording interaction is dephasing
  (`recording_reduces_to_dephase`); recording is an involution, so retaining and reversing the
  joint relation restores the control (`joint_reversal_restores_control`).
* **On the runs of the laws.** The diagonal, the weight and the norm are invariants
  (`diagonal_invariant`, `mass_invariant`, `x_norm_invariant`, `z_norm_invariant`); every run of
  dephasing rests from its first step on (`settles`), the runs from the prepared and the
  coherent control meet (`runs_meet`), the process is not lossless (`not_lossless`) and nothing
  read later restores where they began (`no_restore_along`); every configuration returns under
  recording after two steps (`returns`), and the control read at the second step is the one read
  at the start (`control_returns`).

The operations and their physical reading are supplied; this checks their algebra and a
consequence for what a reduction keeps, not quantum theory or a laboratory implementation. No
ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Integers

namespace Dephasing

/-! ## The fragment -/

/-- Two amplitudes. -/
structure Vec where
  zero : Int
  one : Int
  deriving DecidableEq

/-- A two-branch control: the target's amplitudes on each branch. -/
structure Joint where
  zero : Vec
  one : Vec
  deriving DecidableEq

/-- A two-by-two matrix of numerators. -/
structure Matrix where
  zz : Int
  zo : Int
  oz : Int
  oo : Int
  deriving DecidableEq

def xGate (v : Vec) : Vec := ⟨v.one, v.zero⟩
def zGate (v : Vec) : Vec := ⟨v.zero, -v.one⟩
def negVec (v : Vec) : Vec := ⟨-v.zero, -v.one⟩
def norm (v : Vec) : Int := v.zero * v.zero + v.one * v.one
def inner (u v : Vec) : Int := u.zero * v.zero + u.one * v.one

/-- The control prepared in plus; the common normalisation is kept outside. -/
def prepare (v : Vec) : Joint := ⟨v, v⟩

/-- A control with a blank second branch. -/
def blankControl (v : Vec) : Joint := ⟨v, ⟨0, 0⟩⟩

/-- The unnormalised Hadamard step on the control. -/
def hControl (v : Joint) : Joint :=
  ⟨⟨v.zero.zero + v.one.zero, v.zero.one + v.one.one⟩,
   ⟨v.zero.zero - v.one.zero, v.zero.one - v.one.one⟩⟩

/-- Branch zero applies `A` then `B`; branch one applies `B` then `A`. -/
def switched (A B : Vec → Vec) (v : Joint) : Joint := ⟨B (A v.zero), A (B v.one)⟩

/-- The control matrix: the partial trace over the target. -/
def controlDensity (v : Joint) : Matrix :=
  ⟨inner v.zero v.zero, inner v.zero v.one, inner v.one v.zero, inner v.one v.one⟩

/-- Dephasing: keep the diagonal, drop the cross terms. -/
def dephase (m : Matrix) : Matrix := ⟨m.zz, 0, 0, m.oo⟩
def diagonal (m : Matrix) : Int × Int := (m.zz, m.oo)
def mass (m : Matrix) : Int := m.zz + m.oo
def plusMass (m : Matrix) : Int := m.zz + m.zo + m.oz + m.oo
def minusMass (m : Matrix) : Int := m.zz - m.zo - m.oz + m.oo

/-- The plus and minus numerators and their common denominator. -/
def response (m : Matrix) : Int × Int × Int := (plusMass m, minusMass m, 2 * mass m)

def basisZero : Vec := ⟨1, 0⟩
def prepared : Matrix := controlDensity (prepare basisZero)
def coherent : Matrix := controlDensity (switched xGate zGate (prepare basisZero))
def degraded : Matrix := dephase coherent

/-- The diagonal and the cross-term sum. -/
def retained (m : Matrix) : (Int × Int) × Int := (diagonal m, m.zo + m.oz)
def decodePlus (r : (Int × Int) × Int) : Int := r.1.1 + r.2 + r.1.2

/-- A control with a blank register. -/
def withBlank (v : Vec) : Joint := ⟨⟨v.zero, 0⟩, ⟨v.one, 0⟩⟩

/-- The recording interaction: a controlled X onto the register. -/
def recordBranch (v : Joint) : Joint := ⟨v.zero, xGate v.one⟩

/-! ## The algebra -/

theorem preparation_from_blank : ∀ v : Vec, hControl (blankControl v) = prepare v
  | ⟨a, b⟩ => show (⟨⟨a + 0, b + 0⟩, ⟨a - 0, b - 0⟩⟩ : Joint) = ⟨⟨a, b⟩, ⟨a, b⟩⟩ by
      rw [add_zero a, add_zero b, sub_zero a, sub_zero b]

theorem xz_anticommute : ∀ v : Vec, zGate (xGate v) = negVec (xGate (zGate v))
  | ⟨a, b⟩ => show (⟨b, -a⟩ : Vec) = ⟨- -b, -a⟩ by rw [neg_neg b]

theorem x_preserves_norm : ∀ v : Vec, norm (xGate v) = norm v
  | ⟨a, b⟩ => add_comm (b * b) (a * a)

theorem z_preserves_norm : ∀ v : Vec, norm (zGate v) = norm v
  | ⟨a, b⟩ => show a * a + -b * -b = a * a + b * b by rw [neg_mul_neg b b]

theorem prepared_density (v : Vec) :
    controlDensity (prepare v) = ⟨norm v, norm v, norm v, norm v⟩ := rfl

/-- **The switched order of X and Z negates the control's off-diagonal entries.** -/
theorem switched_density : ∀ v : Vec,
    controlDensity (switched xGate zGate (prepare v)) = ⟨norm v, -norm v, -norm v, norm v⟩
  | ⟨a, b⟩ =>
    show (⟨b * b + -a * -a, b * -b + -a * a, -b * b + a * -a, -b * -b + a * a⟩ : Matrix) =
        ⟨a * a + b * b, -(a * a + b * b), -(a * a + b * b), a * a + b * b⟩ by
      rw [neg_mul_neg a a, neg_mul_neg b b, mul_neg b b, neg_mul a a, neg_mul b b, mul_neg a a,
        neg_add (a * a) (b * b), add_comm (b * b) (a * a), add_comm (-(b * b)) (-(a * a))]

theorem dephase_preserves_diagonal (m : Matrix) : diagonal (dephase m) = diagonal m := rfl

theorem dephase_preserves_mass (m : Matrix) : mass (dephase m) = mass m := rfl

/-- **The plus and minus responses sum to twice the total weight.** -/
theorem response_mass_conserved (m : Matrix) : plusMass m + minusMass m = 2 * mass m :=
  calc m.zz + m.zo + m.oz + m.oo + (m.zz + -m.zo + -m.oz + m.oo)
      = m.zz + m.oo + (m.zo + m.oz) + (m.zz + m.oo + (-m.zo + -m.oz)) := by
        rw [add_assoc m.zz m.zo m.oz, add_right_comm m.zz (m.zo + m.oz) m.oo,
          add_assoc m.zz (-m.zo) (-m.oz), add_right_comm m.zz (-m.zo + -m.oz) m.oo]
    _ = m.zz + m.oo + (m.zz + m.oo) + (m.zo + m.oz + (-m.zo + -m.oz)) :=
        add_add_add_comm _ _ _ _
    _ = m.zz + m.oo + (m.zz + m.oo) := by
        rw [← neg_add m.zo m.oz, add_right_neg, add_zero]
    _ = 2 * (m.zz + m.oo) := (two_mul _).symm

/-- **Dephasing sets both responses to the total weight.** -/
theorem dephase_response (m : Matrix) : response (dephase m) = (mass m, mass m, 2 * mass m) :=
  show ((m.zz + 0 + 0 + m.oo, m.zz - 0 - 0 + m.oo, 2 * (m.zz + m.oo)) : Int × Int × Int) =
      (m.zz + m.oo, m.zz + m.oo, 2 * (m.zz + m.oo)) by
    rw [add_zero m.zz, add_zero m.zz, sub_zero m.zz, sub_zero m.zz]

theorem prepared_matrix : prepared = ⟨1, 1, 1, 1⟩ := by decide
theorem coherent_matrix : coherent = ⟨1, -1, -1, 1⟩ := by decide
theorem degraded_matrix : degraded = ⟨1, 0, 0, 1⟩ := by decide

/-- The three controls have the same branch weights. -/
theorem branch_weights_unchanged :
    diagonal prepared = (1, 1) ∧ diagonal coherent = (1, 1) ∧ diagonal degraded = (1, 1) := by
  decide

theorem prepared_response : response prepared = (4, 0, 4) := by decide
theorem coherent_response : response coherent = (0, 4, 4) := by decide
theorem degraded_response : response degraded = (2, 2, 4) := by decide

/-- **No decoder of the response reads the diagonal**: the diagonal merges the coherent and the
degraded control, whose plus responses differ (`Readout.decoder_pair_iff`). -/
theorem no_diagonal_response_decoder :
    ¬ ∃ decode : (Int × Int) → Int,
      decode (diagonal coherent) = plusMass coherent ∧
      decode (diagonal degraded) = plusMass degraded :=
  fun found => (by decide : plusMass coherent ≠ plusMass degraded)
    ((Readout.decoder_pair_iff (by decide : diagonal coherent = diagonal degraded)).mp found)

theorem dephase_merges_preparations : dephase prepared = dephase coherent := by decide

/-- **Nothing restores the prepared and the coherent control from their dephasing**
(`Readout.no_restore`). -/
theorem no_uniform_dephase_inverse :
    ¬ ∃ restore : Matrix → Matrix,
      restore (dephase prepared) = prepared ∧ restore (dephase coherent) = coherent :=
  Readout.no_restore dephase_merges_preparations (by decide : prepared ≠ coherent)

/-- **Keeping the cross-term sum is enough for the plus response.** -/
theorem retained_response_exact (m : Matrix) : decodePlus (retained m) = plusMass m :=
  show m.zz + (m.zo + m.oz) + m.oo = m.zz + m.zo + m.oz + m.oo by
    rw [add_assoc m.zz m.zo m.oz]

/-- **Dephasing keeps the plus response exactly where the cross terms sum to zero.** -/
theorem dephase_keeps_response_iff (m : Matrix) :
    plusMass (dephase m) = plusMass m ↔ m.zo + m.oz = 0 :=
  have before : plusMass (dephase m) = m.zz + m.oo :=
    show m.zz + 0 + 0 + m.oo = m.zz + m.oo by rw [add_zero m.zz, add_zero m.zz]
  have after : plusMass m = m.zz + m.oo + (m.zo + m.oz) :=
    show m.zz + m.zo + m.oz + m.oo = m.zz + m.oo + (m.zo + m.oz) by
      rw [add_assoc m.zz m.zo m.oz, add_right_comm]
  ⟨fun kept => (add_left_cancel
      ((add_zero (m.zz + m.oo)).trans (before.symm.trans (kept.trans after)))).symm,
   fun none => before.trans (after.trans (by rw [none, add_zero])).symm⟩

theorem recordBranch_involution : ∀ v : Joint, recordBranch (recordBranch v) = v
  | ⟨_, ⟨_, _⟩⟩ => rfl

/-- **Reducing after the recording interaction is dephasing.** -/
theorem recording_reduces_to_dephase : ∀ v : Vec,
    controlDensity (recordBranch (withBlank v)) = dephase (controlDensity (withBlank v))
  | ⟨a, b⟩ =>
    show (⟨a * a + 0 * 0, a * 0 + 0 * b, 0 * a + b * 0, 0 * 0 + b * b⟩ : Matrix) =
        ⟨a * a + 0 * 0, 0, 0, b * b + 0 * 0⟩ by
      rw [mul_zero a, zero_mul b, zero_mul a, mul_zero b, zero_mul 0, add_zero 0,
        zero_add (b * b), add_zero (b * b)]

/-- **Retaining and reversing the joint relation restores the control.** -/
theorem joint_reversal_restores_control (v : Vec) :
    controlDensity (recordBranch (recordBranch (withBlank v))) = controlDensity (withBlank v) :=
  congrArg controlDensity (recordBranch_involution (withBlank v))

theorem prepared_control_embedding : controlDensity (withBlank ⟨1, 1⟩) = prepared := by decide

theorem coherent_control_embedding : controlDensity (withBlank ⟨-1, 1⟩) = coherent := by decide

/-! ## Operations as moves -/

/-- The declared operations on a configuration as moves: each step applies one operation. -/
def operations (S : Type) : Process S (S → S) := Assurance.ofMap fun s g => g s

/-- **A course of operations reaches exactly the configuration the operations give in order.** -/
theorem operations_trace_iff {S : Type} :
    ∀ {s t : S} {gs : List (S → S)}, Trace (operations S) s gs t ↔ t = gs.foldl (fun x g => g x) s
  | _, _, [] => ⟨fun path => (trace_nil_iff.mp path).symm, fun same => trace_nil_iff.mpr same.symm⟩
  | _, _, _ :: _ => ⟨fun path => match trace_cons_iff.mp path with
      | ⟨_, step, rest⟩ => (operations_trace_iff.mp rest).trans
          (congrArg (fun x => List.foldl (fun (y : S) (g : S → S) => g y) x _) step),
    fun same => .cons rfl (operations_trace_iff.mpr same)⟩

/-- **The two orders of X and Z end at configurations that are negatives of each other.** -/
theorem orders_negate {v w w' : Vec} (first : Trace (operations Vec) v [xGate, zGate] w)
    (second : Trace (operations Vec) v [zGate, xGate] w') : w = negVec w' :=
  (operations_trace_iff.mp first).trans
    ((xz_anticommute v).trans (congrArg negVec (operations_trace_iff.mp second).symm))

/-- **From a control with a blank branch, the Hadamard course reaches the prepared joint**, whose
control matrix has every entry the norm. -/
theorem hadamard_prepares {v : Vec} {t : Joint}
    (path : Trace (operations Joint) (blankControl v) [hControl] t) :
    t = prepare v ∧ controlDensity t = ⟨norm v, norm v, norm v, norm v⟩ :=
  have reached : t = prepare v := (operations_trace_iff.mp path).trans (preparation_from_blank v)
  ⟨reached, (congrArg controlDensity reached).trans (prepared_density v)⟩

/-- **Followed by the switched order of X and Z, the control matrix has its off-diagonal entries
negated.** -/
theorem switched_course {v : Vec} {t : Joint}
    (path : Trace (operations Joint) (blankControl v) [hControl, switched xGate zGate] t) :
    controlDensity t = ⟨norm v, -norm v, -norm v, norm v⟩ :=
  (congrArg controlDensity ((operations_trace_iff.mp path).trans
      (congrArg (switched xGate zGate) (preparation_from_blank v)))).trans (switched_density v)

/-! ## The gates as laws -/

/-- **The norm is an invariant of X.** -/
theorem x_norm_invariant (w : Int) : Invariant (Law.process xGate) (fun v => norm v = w) :=
  fun s _ _ step held => (congrArg norm step).trans ((x_preserves_norm s).trans held)

/-- **The norm is an invariant of Z.** -/
theorem z_norm_invariant (w : Int) : Invariant (Law.process zGate) (fun v => norm v = w) :=
  fun s _ _ step held => (congrArg norm step).trans ((z_preserves_norm s).trans held)

theorem x_norm_along (r : Run (Law.process xGate)) (n : Nat) : norm (r.state n) = norm (r.state 0) :=
  (x_norm_invariant (norm (r.state 0))).run r rfl n

theorem z_norm_along (r : Run (Law.process zGate)) (n : Nat) : norm (r.state n) = norm (r.state 0) :=
  (z_norm_invariant (norm (r.state 0))).run r rfl n

/-! ## What dephasing keeps along its runs -/

theorem dephase_dephase (m : Matrix) : dephase (dephase m) = dephase m := rfl

/-- **Every run of dephasing rests from its first step on.** -/
theorem run_settles (m : Matrix) : ∀ n, (Law.run dephase m).state (n + 1) = dephase m
  | 0 => rfl
  | n + 1 => (congrArg dephase (run_settles m n)).trans (dephase_dephase m)

/-- **Every run of dephasing is, from its first step on, the dephased configuration it began
with.** -/
theorem settles (r : Run (Law.process dephase)) (n : Nat) : r.state (n + 1) = dephase (r.state 0) :=
  (Branching.law_run_state r (n + 1)).trans (run_settles (r.state 0) n)

/-- **The diagonal is an invariant of the dephasing law.** -/
theorem diagonal_invariant (d : Int × Int) :
    Invariant (Law.process dephase) (fun m => diagonal m = d) :=
  fun s _ _ step held => (congrArg diagonal step).trans ((dephase_preserves_diagonal s).trans held)

/-- **The total weight is an invariant of the dephasing law.** -/
theorem mass_invariant (w : Int) : Invariant (Law.process dephase) (fun m => mass m = w) :=
  fun s _ _ step held => (congrArg mass step).trans ((dephase_preserves_mass s).trans held)

theorem diagonal_along (r : Run (Law.process dephase)) (n : Nat) :
    diagonal (r.state n) = diagonal (r.state 0) :=
  (diagonal_invariant (diagonal (r.state 0))).run r rfl n

theorem mass_along (r : Run (Law.process dephase)) (n : Nat) :
    mass (r.state n) = mass (r.state 0) :=
  (mass_invariant (mass (r.state 0))).run r rfl n

theorem prepared_run_diagonal (n : Nat) : diagonal ((Law.run dephase prepared).state n) = (1, 1) :=
  (diagonal_along (Law.run dephase prepared) n).trans branch_weights_unchanged.1

theorem coherent_run_diagonal (n : Nat) : diagonal ((Law.run dephase coherent).state n) = (1, 1) :=
  (diagonal_along (Law.run dephase coherent) n).trans branch_weights_unchanged.2.1

/-- **Along every run of dephasing, from the first step on the response is that of the total
weight it began with.** -/
theorem response_settles (r : Run (Law.process dephase)) (n : Nat) :
    response (r.state (n + 1)) = (mass (r.state 0), mass (r.state 0), 2 * mass (r.state 0)) :=
  (congrArg response (settles r n)).trans (dephase_response (r.state 0))

/-- **Along every run of dephasing, the plus response is kept exactly where the cross terms of
the start sum to zero.** -/
theorem plus_kept_iff (r : Run (Law.process dephase)) (n : Nat) :
    plusMass (r.state (n + 1)) = plusMass (r.state 0) ↔ (r.state 0).zo + (r.state 0).oz = 0 :=
  Eq.subst (motive := fun x => plusMass x = plusMass (r.state 0) ↔ (r.state 0).zo + (r.state 0).oz = 0)
    (settles r n).symm (dephase_keeps_response_iff (r.state 0))

/-- **Along every run of dephasing, the plus and minus responses sum to twice the total weight of
the start.** -/
theorem plus_minus_along (r : Run (Law.process dephase)) (n : Nat) :
    plusMass (r.state n) + minusMass (r.state n) = 2 * mass (r.state 0) :=
  (response_mass_conserved (r.state n)).trans (congrArg (2 * ·) (mass_along r n))

/-! ## What dephasing loses along its runs -/

theorem prepared_ne_coherent : prepared ≠ coherent := by decide

/-- **Dephasing merges the prepared and the coherent control.** -/
theorem merges : Law.Merges dephase :=
  Law.merges_iff.mpr ⟨prepared, coherent, prepared_ne_coherent, dephase_merges_preparations⟩

theorem process_merges : Branching.Merges (Law.process dephase) :=
  Branching.law_merges_iff.mpr merges

/-- **The dephasing process is not lossless.** -/
theorem not_lossless : ¬ Branching.Lossless (Law.process dephase) :=
  fun lossless => merges.not_lossless (Branching.law_lossless_iff.mp lossless)

/-- **The runs from the prepared and the coherent control are equal from the first step on.** -/
theorem runs_meet (n : Nat) :
    (Law.run dephase prepared).state (n + 1) = (Law.run dephase coherent).state (n + 1) :=
  Law.merged_stays dephase_merges_preparations n

/-- **No reading of a later configuration recovers where both runs began.** -/
theorem no_restore_along (n : Nat) :
    ¬ ∃ restore : Matrix → Matrix,
      restore ((Law.run dephase prepared).state (n + 1)) = (Law.run dephase prepared).state 0 ∧
      restore ((Law.run dephase coherent).state (n + 1)) = (Law.run dephase coherent).state 0 :=
  fun ⟨restore, back, back'⟩ =>
    prepared_ne_coherent (back.symm.trans ((congrArg restore (runs_meet n)).trans back'))

theorem prepared_run :
    (Law.run dephase prepared).state 0 = ⟨1, 1, 1, 1⟩ ∧
      ∀ n, (Law.run dephase prepared).state (n + 1) = ⟨1, 0, 0, 1⟩ :=
  ⟨prepared_matrix, fun n =>
    (run_settles prepared n).trans (dephase_merges_preparations.trans degraded_matrix)⟩

theorem coherent_run :
    (Law.run dephase coherent).state 0 = ⟨1, -1, -1, 1⟩ ∧
      ∀ n, (Law.run dephase coherent).state (n + 1) = ⟨1, 0, 0, 1⟩ :=
  ⟨coherent_matrix, fun n => (run_settles coherent n).trans degraded_matrix⟩

theorem prepared_run_response :
    response ((Law.run dephase prepared).state 0) = (4, 0, 4) ∧
      ∀ n, response ((Law.run dephase prepared).state (n + 1)) = (2, 2, 4) :=
  ⟨prepared_response, fun n =>
    (congrArg response ((run_settles prepared n).trans dephase_merges_preparations)).trans
      degraded_response⟩

theorem coherent_run_response :
    response ((Law.run dephase coherent).state 0) = (0, 4, 4) ∧
      ∀ n, response ((Law.run dephase coherent).state (n + 1)) = (2, 2, 4) :=
  ⟨coherent_response, fun n => (congrArg response (run_settles coherent n)).trans degraded_response⟩

/-- **No decoder reading the diagonal along the coherent run gives its response** at its start
and at any later step. -/
theorem no_diagonal_decoder_along (n : Nat) :
    ¬ ∃ decode : Int × Int → Int,
      decode (diagonal ((Law.run dephase coherent).state 0)) =
          plusMass ((Law.run dephase coherent).state 0) ∧
        decode (diagonal ((Law.run dephase coherent).state (n + 1))) =
          plusMass ((Law.run dephase coherent).state (n + 1)) :=
  fun ⟨decode, start, later⟩ => no_diagonal_response_decoder ⟨decode, start,
    Eq.subst (motive := fun m => decode (diagonal m) = plusMass m) (run_settles coherent n) later⟩

/-! ## Recording along its runs -/

/-- **Every configuration returns under the recording process**, after two steps. -/
theorem returns (j : Joint) : Branching.Returns (Law.process recordBranch) j :=
  Law.returns_iff.mpr ⟨2, Nat.zero_lt_succ 1, recordBranch_involution j⟩

/-- **Recording is dephasing of the control**: along every run of the recording law from a
control with a blank register, the control read at the first step is the dephasing of the one
read at the start. -/
theorem recording_dephases {v : Vec} (r : Run (Law.process recordBranch))
    (start : r.state 0 = withBlank v) :
    controlDensity (r.state 1) = dephase (controlDensity (r.state 0)) :=
  (congrArg controlDensity (r.step 0)).trans
    (Eq.subst (motive := fun x => controlDensity (recordBranch x) = dephase (controlDensity x))
      start.symm (recording_reduces_to_dephase v))

/-- **Along every run of the recording law from a control with a blank register, the control read
at the second step is the one read at the start.** -/
theorem control_returns {v : Vec} (r : Run (Law.process recordBranch))
    (start : r.state 0 = withBlank v) : controlDensity (r.state 2) = controlDensity (r.state 0) :=
  (congrArg controlDensity (Branching.law_run_state r 2)).trans
    (Eq.subst (motive := fun x =>
        controlDensity (Law.orbit recordBranch x 2) = controlDensity x)
      start.symm (joint_reversal_restores_control v))

theorem prepared_reading (r : Run (Law.process recordBranch)) (start : r.state 0 = withBlank ⟨1, 1⟩) :
    controlDensity (r.state 0) = prepared ∧ controlDensity (r.state 2) = prepared :=
  have first : controlDensity (r.state 0) = prepared :=
    (congrArg controlDensity start).trans prepared_control_embedding
  ⟨first, (control_returns r start).trans first⟩

theorem coherent_reading (r : Run (Law.process recordBranch))
    (start : r.state 0 = withBlank ⟨-1, 1⟩) :
    controlDensity (r.state 0) = coherent ∧ controlDensity (r.state 2) = coherent :=
  have first : controlDensity (r.state 0) = coherent :=
    (congrArg controlDensity start).trans coherent_control_embedding
  ⟨first, (control_returns r start).trans first⟩

end Dephasing

end Becoming
