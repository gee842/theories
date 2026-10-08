import Std

/-!
Exact real-amplitude fragment of a controlled-order calculation.

Integers are unnormalised amplitudes and density numerators. No claim is made
that arbitrary integer matrices are physical states. For the three displayed
control matrices, trace = 2 and the physical density is the matrix / 2.
The plus/minus response numerators have the common denominator 2 * trace = 4.

The X and Z actions, coherent order control, partial trace, dephasing and
measurement interpretation are supplied quantum-mechanical operations. This
checks their algebra and an information-loss consequence, not quantum theory,
causal nonseparability, a laboratory implementation or axiom-free ontology.
-/
namespace Generative.OperativeCoherence

structure Vec where
  zero : Int
  one : Int
  deriving DecidableEq, Repr

structure Joint where
  zero : Vec
  one : Vec
  deriving DecidableEq, Repr

structure Matrix where
  zz : Int
  zo : Int
  oz : Int
  oo : Int
  deriving DecidableEq, Repr

def xGate (v : Vec) : Vec := ⟨v.one, v.zero⟩
def zGate (v : Vec) : Vec := ⟨v.zero, -v.one⟩
def negVec (v : Vec) : Vec := ⟨-v.zero, -v.one⟩
def norm (v : Vec) : Int := v.zero * v.zero + v.one * v.one
def inner (u v : Vec) : Int := u.zero * v.zero + u.one * v.one

/-- Control is prepared in plus; the common normalisation is kept outside. -/
def prepare (v : Vec) : Joint := ⟨v, v⟩

/-- Branch zero applies A then B; branch one applies B then A. -/
def switched (A B : Vec → Vec) (v : Joint) : Joint :=
  ⟨B (A v.zero), A (B v.one)⟩

/-- Partial trace over the target in the declared real-amplitude fragment. -/
def controlDensity (v : Joint) : Matrix :=
  ⟨inner v.zero v.zero, inner v.zero v.one,
   inner v.one v.zero, inner v.one v.one⟩

def dephase (m : Matrix) : Matrix := ⟨m.zz, 0, 0, m.oo⟩
def diagonal (m : Matrix) : Int × Int := (m.zz, m.oo)
def mass (m : Matrix) : Int := m.zz + m.oo
def plusMass (m : Matrix) : Int := m.zz + m.zo + m.oz + m.oo
def minusMass (m : Matrix) : Int := m.zz - m.zo - m.oz + m.oo

/-- Numerators for plus/minus and their common denominator. -/
def response (m : Matrix) : Int × Int × Int :=
  (plusMass m, minusMass m, 2 * mass m)

def basisZero : Vec := ⟨1, 0⟩
def prepared : Matrix := controlDensity (prepare basisZero)
def coherent : Matrix :=
  controlDensity (switched xGate zGate (prepare basisZero))
def degraded : Matrix := dephase coherent

theorem xz_anticommute (v : Vec) :
    zGate (xGate v) = negVec (xGate (zGate v)) := by
  cases v
  simp [xGate, zGate, negVec]

theorem x_preserves_norm (v : Vec) : norm (xGate v) = norm v := by
  simp [norm, xGate, Int.add_comm]

theorem z_preserves_norm (v : Vec) : norm (zGate v) = norm v := by
  simp [norm, zGate, Int.neg_mul, Int.mul_neg]

theorem prepared_density (v : Vec) :
    controlDensity (prepare v) = ⟨norm v, norm v, norm v, norm v⟩ := rfl

/-- The control sign is derived from the actual order composition. -/
theorem switched_density (v : Vec) :
    controlDensity (switched xGate zGate (prepare v)) =
      ⟨norm v, -norm v, -norm v, norm v⟩ := by
  simp [controlDensity, switched, xGate, zGate, prepare, inner, norm,
    Int.neg_mul, Int.mul_neg, Int.neg_add, Int.add_comm]

theorem dephase_preserves_diagonal (m : Matrix) :
    diagonal (dephase m) = diagonal m := rfl

theorem dephase_preserves_mass (m : Matrix) : mass (dephase m) = mass m := rfl

theorem response_mass_conserved (m : Matrix) :
    plusMass m + minusMass m = 2 * mass m := by
  simp only [plusMass, minusMass, mass]
  omega

theorem dephase_response (m : Matrix) :
    response (dephase m) = (mass m, mass m, 2 * mass m) := by
  simp [response, plusMass, minusMass, mass, dephase]

theorem prepared_matrix : prepared = ⟨1, 1, 1, 1⟩ := by decide
theorem coherent_matrix : coherent = ⟨1, -1, -1, 1⟩ := by decide
theorem degraded_matrix : degraded = ⟨1, 0, 0, 1⟩ := by decide

/-- Same branch weights, including both nonzero alternatives. -/
theorem branch_weights_unchanged :
    diagonal prepared = (1, 1) ∧ diagonal coherent = (1, 1) ∧
    diagonal degraded = (1, 1) := by decide

theorem prepared_response : response prepared = (4, 0, 4) := by decide
theorem coherent_response : response coherent = (0, 4, 4) := by decide
theorem degraded_response : response degraded = (2, 2, 4) := by decide

/-- A diagonal-only summary cannot recover this fixed measurement response. -/
theorem no_diagonal_response_decoder :
    ¬ ∃ decode : (Int × Int) → Int,
      decode (diagonal coherent) = plusMass coherent ∧
      decode (diagonal degraded) = plusMass degraded := by
  rintro ⟨decode, hc, hd⟩
  have same : diagonal coherent = diagonal degraded := by decide
  have unequal : plusMass coherent ≠ plusMass degraded := by decide
  exact unequal (hc.symm.trans ((congrArg decode same).trans hd))

theorem dephase_merges_preparations : dephase prepared = dephase coherent := by decide

/-- Uniform recovery from the reduced matrix alone fails for these two inputs.
This does not prohibit preparing a known target or using additional information. -/
theorem no_uniform_dephase_inverse :
    ¬ ∃ restore : Matrix → Matrix,
      restore (dephase prepared) = prepared ∧
      restore (dephase coherent) = coherent := by
  rintro ⟨restore, hp, hc⟩
  have unequal : prepared ≠ coherent := by decide
  exact unequal (hp.symm.trans ((congrArg restore dephase_merges_preparations).trans hc))

/-- Keeping the off-diagonal cross term is sufficient for this response.
It is not claimed sufficient for all measurements on general complex states. -/
def retained (m : Matrix) : (Int × Int) × Int := (diagonal m, m.zo + m.oz)

def decodePlus (r : (Int × Int) × Int) : Int := r.1.1 + r.2 + r.1.2

theorem retained_response_exact (m : Matrix) :
    decodePlus (retained m) = plusMass m := by
  simp only [decodePlus, retained, diagonal, plusMass]
  omega

/-- Loss of the measured contrast is exactly loss of this cross-term sum. -/
theorem dephase_keeps_response_iff (m : Matrix) :
    plusMass (dephase m) = plusMass m ↔ m.zo + m.oz = 0 := by
  simp only [plusMass, dephase]
  constructor
  · intro h
    omega
  · intro h
    omega

/-- The second index now denotes an initially blank environment register.
The roles of the two coordinates are stated locally, not primitive substances. -/
def withBlank (v : Vec) : Joint := ⟨⟨v.zero, 0⟩, ⟨v.one, 0⟩⟩

/-- Controlled X correlates the control with the environment register. -/
def recordBranch (v : Joint) : Joint := ⟨v.zero, xGate v.one⟩

theorem recordBranch_involution (v : Joint) :
    recordBranch (recordBranch v) = v := by
  cases v with
  | mk zero one =>
    cases one
    rfl

/-- Reduction after a reversible joint interaction gives exactly dephasing. -/
theorem recording_reduces_to_dephase (v : Vec) :
    controlDensity (recordBranch (withBlank v)) =
      dephase (controlDensity (withBlank v)) := by
  simp [controlDensity, recordBranch, withBlank, xGate, inner, dephase]

/-- Retaining and reversing the joint relation restores the original control. -/
theorem joint_reversal_restores_control (v : Vec) :
    controlDensity (recordBranch (recordBranch (withBlank v))) =
      controlDensity (withBlank v) := by
  exact congrArg controlDensity (recordBranch_involution (withBlank v))

theorem prepared_control_embedding :
    controlDensity (withBlank ⟨1, 1⟩) = prepared := by decide

theorem coherent_control_embedding :
    controlDensity (withBlank ⟨-1, 1⟩) = coherent := by decide

end Generative.OperativeCoherence
