import OperativeCoherence
import SystemsOrganization

/-!
One joint activity can change while both of its reduced states remain fixed.
The same later controlled-X then reveals the changed relation. The operations,
real-amplitude fragment and physical interpretation are supplied, not derived.
The main phase-comparison witnesses have squared norm 2; amplitudes divide by
sqrt 2 and reduced density numerators divide by 2. The final omission witnesses
have norm 1. Arbitrary integer inputs
below support algebraic identities, not a claim of physical normalization.

The positive reduction retains a cross contribution in addition to the current
control density. Its exactness under arbitrary finite controlled-X/phase words
uses the existing SystemsOrganization theorem rather than a new history theory.
-/
namespace Generative.RelationalReduction

open OperativeCoherence

/-- Exchange coordinate roles solely to compute the other partial trace. -/
def exchangeCoordinates (v : Joint) : Joint :=
  ⟨⟨v.zero.zero, v.one.zero⟩, ⟨v.zero.one, v.one.one⟩⟩

def registerDensity (v : Joint) : Matrix := controlDensity (exchangeCoordinates v)
def localStates (v : Joint) : Matrix × Matrix := (controlDensity v, registerDensity v)

/-- Z on the first coordinate, applied to the same joint preparation. -/
def phase (v : Joint) : Joint := ⟨v.zero, negVec v.one⟩

def joined : Joint := recordBranch (withBlank ⟨1, 1⟩)
def changed : Joint := phase joined

theorem formation_from_blank :
    recordBranch (hControl (blankControl basisZero)) = joined := by decide

theorem actual_phase_preserves_both_local_states :
    localStates joined = (⟨1, 0, 0, 1⟩, ⟨1, 0, 0, 1⟩) ∧
    localStates changed = localStates joined := by decide

/-- Even the full computational-basis distribution misses this change. -/
def basisMasses (v : Joint) : Int × Int × Int × Int :=
  (v.zero.zero * v.zero.zero, v.zero.one * v.zero.one,
   v.one.zero * v.one.zero, v.one.one * v.one.one)

theorem actual_phase_preserves_basis_masses :
    basisMasses joined = (1, 0, 0, 1) ∧ basisMasses changed = basisMasses joined := by decide

/-- Responses use the same supplied gate and the same measurement in both cases. -/
theorem same_interaction_distinguishes_relation :
    response (controlDensity (recordBranch joined)) = (4, 0, 4) ∧
    response (controlDensity (recordBranch changed)) = (0, 4, 4) := by decide

theorem no_local_pair_update :
    ¬ ∃ update : (Matrix × Matrix) → Matrix,
      update (localStates joined) = controlDensity (recordBranch joined) ∧
      update (localStates changed) = controlDensity (recordBranch changed) := by
  rintro ⟨update, hj, hc⟩
  have same := actual_phase_preserves_both_local_states.2
  have unequal : controlDensity (recordBranch joined) ≠
      controlDensity (recordBranch changed) := by decide
  exact unequal (hj.symm.trans ((congrArg update same.symm).trans hc))

/-- The cross contribution that will enter the control density after CNOT. -/
def coupledCross (v : Joint) : Int :=
  v.zero.zero * v.one.one + v.zero.one * v.one.zero

structure Summary where
  zeroMass : Int
  oneMass : Int
  localCross : Int
  jointCross : Int
  deriving DecidableEq, Repr

def summarize (v : Joint) : Summary :=
  ⟨norm v.zero, norm v.one, inner v.zero v.one, coupledCross v⟩

def decodeControl (s : Summary) : Matrix :=
  ⟨s.zeroMass, s.localCross, s.localCross, s.oneMass⟩

theorem summary_recovers_control (v : Joint) :
    decodeControl (summarize v) = controlDensity v := by
  simp [decodeControl, summarize, controlDensity, norm, inner, Int.mul_comm]

inductive Event where
  | interact
  | shiftPhase
  deriving DecidableEq, Repr

def next (v : Joint) : Event → Joint
  | .interact => recordBranch v
  | .shiftPhase => phase v

/-- Interaction exchanges the two contributions; phase changes both signs. -/
def reducedNext (s : Summary) : Event → Summary
  | .interact => ⟨s.zeroMass, s.oneMass, s.jointCross, s.localCross⟩
  | .shiftPhase => ⟨s.zeroMass, s.oneMass, -s.localCross, -s.jointCross⟩

theorem summary_update_exact :
    SystemsOrganization.Commuting next reducedNext summarize := by
  intro v event
  cases event with
  | interact =>
      simp [next, reducedNext, summarize, recordBranch, xGate, norm, inner,
        coupledCross, Int.add_comm]
  | shiftPhase =>
      simp [next, reducedNext, summarize, phase, negVec, norm, inner,
        coupledCross, Int.mul_neg, Int.neg_mul, Int.neg_add]

/-- Formal application of the previously proved all-word composition theorem. -/
theorem every_finite_word_exact (v : Joint) (word : List Event) :
    summarize (SystemsOrganization.evolve next v word) =
      SystemsOrganization.evolve reducedNext (summarize v) word :=
  SystemsOrganization.evolve_semiconjugacy summary_update_exact v word

theorem every_finite_control_response_exact (v : Joint) (word : List Event) :
    response (decodeControl (SystemsOrganization.evolve reducedNext (summarize v) word)) =
      response (controlDensity (SystemsOrganization.evolve next v word)) := by
  rw [← every_finite_word_exact, summary_recovers_control]

theorem retained_cross_distinguishes_change :
    summarize joined = ⟨1, 1, 0, 1⟩ ∧
    summarize changed = ⟨1, 1, 0, -1⟩ := by decide

/-- The repair retains less than the whole joint state or both local states.
Its sufficiency is tied to the supplied operation and output family. -/
theorem summary_omits_other_relations :
    summarize (⟨⟨1, 0⟩, ⟨0, 0⟩⟩ : Joint) = summarize ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ ∧
    registerDensity (⟨⟨1, 0⟩, ⟨0, 0⟩⟩ : Joint) ≠
      registerDensity ⟨⟨0, 1⟩, ⟨0, 0⟩⟩ := by decide

end Generative.RelationalReduction
