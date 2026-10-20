import Becoming.Branching
import Becoming.Assurance
import OperativeCoherence

/-!
# Dephasing and recording as determined laws

`OperativeCoherence` checks the algebra of an exact real-amplitude fragment: control matrices
of a two-branch preparation, dephasing (`dephase`, which keeps the diagonal and drops the cross
terms), the plus/minus response, and a reversible recording interaction (`recordBranch`, a
controlled X onto a blank register). Dephasing and recording are steps of change, so each is a
determined law of the spine (`Law.process`); every run of a determined law is its orbit from
where it begins (`Branching.law_run_state`). This module states the fragment's results of the
runs of those two laws and proves them through the module's theorems.

* **Operations as moves.** The fragment's operations are the moves of a process that applies
  one at each step (`operations`), whose courses reach exactly the configuration the operations
  give in order (`operations_trace_iff`); the inherited ring (`DephasingRunsInherited`) states the
  gate and preparation results of its courses.
* **What dephasing keeps.** The diagonal and the total weight are invariants of the dephasing
  law (`diagonal_invariant`, `mass_invariant`), so they are the same at every step of every run
  (`diagonal_along`, `mass_along`); on the runs from the prepared and the coherent control the
  diagonal is `(1, 1)` at every step (`prepared_run_diagonal`, `coherent_run_diagonal`).
* **What dephasing loses.** Every run of dephasing is, from its first step on, the dephased
  configuration it began with (`run_settles`, `settles`). The law merges the prepared and the
  coherent control (`merges`, `process_merges`), so its process is not lossless (`not_lossless`); their runs are equal from the first step on (`runs_meet`), and no
  reading of a later configuration recovers where both runs began (`no_restore_along`). Both
  runs go to `⟨1, 0, 0, 1⟩` and rest there (`prepared_run`, `coherent_run`), while their response
  changes from `(4, 0, 4)` and `(0, 4, 4)` to `(2, 2, 4)` (`prepared_run_response`,
  `coherent_run_response`): no decoder reading the diagonal along the coherent run gives its
  response at its start and at any later step (`no_diagonal_decoder_along`).
* **Recording is reversible.** Every configuration returns under the recording process, after two
  steps (`returns`); along every run of it from a control with a blank register the control
  matrix read at the second step is the one read at the start (`control_returns`), the prepared
  and the coherent control among them (`prepared_reading`, `coherent_reading`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace DephasingRuns

open Generative.OperativeCoherence

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

/-! ## What dephasing keeps -/

/-- Dephasing a dephased matrix changes nothing. -/
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

/-- **Along every run of dephasing, the diagonal is the one it began with.** -/
theorem diagonal_along (r : Run (Law.process dephase)) (n : Nat) :
    diagonal (r.state n) = diagonal (r.state 0) :=
  (diagonal_invariant (diagonal (r.state 0))).run r rfl n

/-- **Along every run of dephasing, the total weight is the one it began with.** -/
theorem mass_along (r : Run (Law.process dephase)) (n : Nat) :
    mass (r.state n) = mass (r.state 0) :=
  (mass_invariant (mass (r.state 0))).run r rfl n

/-- **On the run of dephasing from the prepared control, the diagonal is `(1, 1)` at every
step.** -/
theorem prepared_run_diagonal (n : Nat) : diagonal ((Law.run dephase prepared).state n) = (1, 1) :=
  (diagonal_along (Law.run dephase prepared) n).trans branch_weights_unchanged.1

/-- **On the run of dephasing from the coherent control, the diagonal is `(1, 1)` at every
step.** -/
theorem coherent_run_diagonal (n : Nat) : diagonal ((Law.run dephase coherent).state n) = (1, 1) :=
  (diagonal_along (Law.run dephase coherent) n).trans branch_weights_unchanged.2.1

/-! ## What dephasing loses -/

/-- The prepared and the coherent control differ. -/
theorem prepared_ne_coherent : prepared ≠ coherent :=
  fun same => no_uniform_dephase_inverse ⟨fun _ => prepared, rfl, same⟩

/-- **Dephasing merges the prepared and the coherent control.** -/
theorem merges : Law.Merges dephase :=
  ⟨prepared, coherent, prepared_ne_coherent, dephase_merges_preparations⟩

/-- The dephasing process merges two configurations. -/
theorem process_merges : Branching.Merges (Law.process dephase) :=
  Branching.law_merges_iff.mpr merges

/-- **The dephasing process is not lossless.** -/
theorem not_lossless : ¬ Branching.Lossless (Law.process dephase) :=
  fun lossless => merges.not_lossless (Branching.law_lossless_iff.mp lossless)

/-- **The runs from the prepared and the coherent control are equal from the first step on.** -/
theorem runs_meet (n : Nat) :
    (Law.run dephase prepared).state (n + 1) = (Law.run dephase coherent).state (n + 1) :=
  Law.merged_stays dephase_merges_preparations n

/-- **No reading of a later configuration recovers where both runs began**: no map takes the
configuration of each run at any step after the first to its configuration at the start. -/
theorem no_restore_along (n : Nat) :
    ¬ ∃ restore : Matrix → Matrix,
      restore ((Law.run dephase prepared).state (n + 1)) = (Law.run dephase prepared).state 0 ∧
      restore ((Law.run dephase coherent).state (n + 1)) = (Law.run dephase coherent).state 0 :=
  fun ⟨restore, back, back'⟩ =>
    prepared_ne_coherent (back.symm.trans ((congrArg restore (runs_meet n)).trans back'))

/-- **The run of dephasing from the prepared control** begins at `⟨1, 1, 1, 1⟩`, goes to
`⟨1, 0, 0, 1⟩` and rests there. -/
theorem prepared_run :
    (Law.run dephase prepared).state 0 = ⟨1, 1, 1, 1⟩ ∧
      ∀ n, (Law.run dephase prepared).state (n + 1) = ⟨1, 0, 0, 1⟩ :=
  ⟨prepared_matrix, fun n =>
    (run_settles prepared n).trans (dephase_merges_preparations.trans degraded_matrix)⟩

/-- **The run of dephasing from the coherent control** begins at `⟨1, -1, -1, 1⟩`, goes to
`⟨1, 0, 0, 1⟩` and rests there. -/
theorem coherent_run :
    (Law.run dephase coherent).state 0 = ⟨1, -1, -1, 1⟩ ∧
      ∀ n, (Law.run dephase coherent).state (n + 1) = ⟨1, 0, 0, 1⟩ :=
  ⟨coherent_matrix, fun n => (run_settles coherent n).trans degraded_matrix⟩

/-- **The response along the run from the prepared control** is `(4, 0, 4)` at the start and
`(2, 2, 4)` at every later step. -/
theorem prepared_run_response :
    response ((Law.run dephase prepared).state 0) = (4, 0, 4) ∧
      ∀ n, response ((Law.run dephase prepared).state (n + 1)) = (2, 2, 4) :=
  ⟨prepared_response, fun n =>
    (congrArg response ((run_settles prepared n).trans dephase_merges_preparations)).trans
      degraded_response⟩

/-- **The response along the run from the coherent control** is `(0, 4, 4)` at the start and
`(2, 2, 4)` at every later step. -/
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

/-! ## Recording is reversible -/

/-- **Every configuration returns under the recording process**, after two steps. -/
theorem returns (j : Joint) : Branching.Returns (Law.process recordBranch) j :=
  Branching.law_returns_iff.mpr ⟨2, Nat.zero_lt_succ 1, recordBranch_involution j⟩

/-- **Along every run of the recording law from a control with a blank register, the control
matrix read at the second step is the one read at the start.** -/
theorem control_returns {v : Vec} (r : Run (Law.process recordBranch))
    (start : r.state 0 = withBlank v) : controlDensity (r.state 2) = controlDensity (r.state 0) :=
  (congrArg controlDensity (Branching.law_run_state r 2)).trans
    (Eq.subst (motive := fun x =>
        controlDensity (Law.orbit recordBranch x 2) = controlDensity x)
      start.symm (joint_reversal_restores_control v))

/-- **The prepared control is read at the start and again at the second step** of every run of
the recording law from the blank-register embedding of `⟨1, 1⟩`. -/
theorem prepared_reading (r : Run (Law.process recordBranch)) (start : r.state 0 = withBlank ⟨1, 1⟩) :
    controlDensity (r.state 0) = prepared ∧ controlDensity (r.state 2) = prepared :=
  have first : controlDensity (r.state 0) = prepared :=
    (congrArg controlDensity start).trans prepared_control_embedding
  ⟨first, (control_returns r start).trans first⟩

/-- **The coherent control is read at the start and again at the second step** of every run of
the recording law from the blank-register embedding of `⟨-1, 1⟩`. -/
theorem coherent_reading (r : Run (Law.process recordBranch))
    (start : r.state 0 = withBlank ⟨-1, 1⟩) :
    controlDensity (r.state 0) = coherent ∧ controlDensity (r.state 2) = coherent :=
  have first : controlDensity (r.state 0) = coherent :=
    (congrArg controlDensity start).trans coherent_control_embedding
  ⟨first, (control_returns r start).trans first⟩

end DephasingRuns

end Becoming
