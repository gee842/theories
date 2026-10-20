import Becoming.DephasingRuns

/-!
# Dephasing, recording and gates as laws: the results with inherited axioms

`Becoming.DephasingRuns` reads `OperativeCoherence`'s dephasing and recording as determined laws
(`Law.process`) and its operations as the moves of a process applying one at each step
(`DephasingRuns.operations`). The fragment's remaining results have non-empty axiom reports from
their own proofs; this module states them of the runs of those laws and the courses of that
process, and proves them through those results.

* **The gates keep the norm.** The norm is an invariant of X and of Z as determined laws
  (`x_norm_invariant`, `z_norm_invariant`), so it is the same at every step of every run of them
  (`x_norm_along`, `z_norm_along`); the two orders of X and Z end at configurations that are
  negatives of each other (`orders_negate`).
* **Preparation and the switched order as a course.** From a control with a blank branch, the
  course of the unnormalised Hadamard reaches the prepared joint, whose control matrix has every
  entry the norm (`hadamard_prepares`); followed by the switched order of X and Z, the control
  matrix has the off-diagonal entries negated (`switched_course`).
* **Recording is dephasing of the control.** Along every run of the recording law from a control
  with a blank register, the control matrix read at the first step is the dephasing of the one
  read at the start (`recording_dephases`).
* **What dephasing does to the response.** Along every run of dephasing, from the first step on
  the response is that of the total weight it began with (`response_settles`); the plus response
  is kept exactly where the cross terms of the start sum to zero (`plus_kept_iff`); and the plus
  and minus responses sum to twice the total weight of the start at every step (`plus_minus_along`).

Axioms inherited: `propext` from `OperativeCoherence`'s `x_preserves_norm`, `z_preserves_norm`,
`xz_anticommute`, `preparation_from_blank`, `switched_density`, `recording_reduces_to_dephase` and
`dephase_response`; `propext` and `Quot.sound` from `dephase_keeps_response_iff` and
`response_mass_conserved`. No other axiom, and no ethical predicate or ranking, occurs.
-/

namespace Becoming

open Generative

namespace DephasingRunsInherited

open Generative.OperativeCoherence DephasingRuns

/-! ## The gates -/

/-- **The norm is an invariant of X.** -/
theorem x_norm_invariant (w : Int) : Invariant (Law.process xGate) (fun v => norm v = w) :=
  fun s _ _ step held => (congrArg norm step).trans ((x_preserves_norm s).trans held)

/-- **The norm is an invariant of Z.** -/
theorem z_norm_invariant (w : Int) : Invariant (Law.process zGate) (fun v => norm v = w) :=
  fun s _ _ step held => (congrArg norm step).trans ((z_preserves_norm s).trans held)

/-- **Along every run of X, the norm is the one it began with.** -/
theorem x_norm_along (r : Run (Law.process xGate)) (n : Nat) : norm (r.state n) = norm (r.state 0) :=
  (x_norm_invariant (norm (r.state 0))).run r rfl n

/-- **Along every run of Z, the norm is the one it began with.** -/
theorem z_norm_along (r : Run (Law.process zGate)) (n : Nat) : norm (r.state n) = norm (r.state 0) :=
  (z_norm_invariant (norm (r.state 0))).run r rfl n

/-- **The two orders of X and Z end at configurations that are negatives of each other.** -/
theorem orders_negate {v w w' : Vec} (first : Trace (operations Vec) v [xGate, zGate] w)
    (second : Trace (operations Vec) v [zGate, xGate] w') : w = negVec w' :=
  (operations_trace_iff.mp first).trans
    ((xz_anticommute v).trans (congrArg negVec (operations_trace_iff.mp second).symm))

/-! ## Preparation and the switched order -/

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

/-! ## Recording -/

/-- **Recording is dephasing of the control**: along every run of the recording law from a
control with a blank register, the control matrix read at the first step is the dephasing of the
one read at the start. -/
theorem recording_dephases {v : Vec} (r : Run (Law.process recordBranch))
    (start : r.state 0 = withBlank v) :
    controlDensity (r.state 1) = dephase (controlDensity (r.state 0)) :=
  (congrArg controlDensity (r.step 0)).trans
    (Eq.subst (motive := fun x => controlDensity (recordBranch x) = dephase (controlDensity x))
      start.symm (recording_reduces_to_dephase v))

/-! ## The response under dephasing -/

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
the start** at every step. -/
theorem plus_minus_along (r : Run (Law.process dephase)) (n : Nat) :
    plusMass (r.state n) + minusMass (r.state n) = 2 * mass (r.state 0) :=
  (response_mass_conserved (r.state n)).trans (congrArg (2 * ·) (mass_along r n))

end DephasingRunsInherited

end Becoming
