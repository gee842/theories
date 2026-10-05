/-
# Foundation.R.CayleyKernel — parametric Cayley kernel + process algebra

This file is the **parametric / scale-invariant version** of the process
algebra previously hard-coded in `Foundation/Wen/Kernel.lean` Layers 1-12.

Where the old `Wen.Kernel` fixed `Field = R 7` (concretely
`Hexagram × YinBit`) and a specific `c_motion : R 7`, this file abstracts
over

* the **carrier type** `X : Type` with an `AddCommGroup` instance
  (any F_2 abelian group; characteristic 2 not strictly required for the
  structure but is the intended use);
* the "primer cell" `primer : X` with `primer ≠ 0` (any non-zero choice).

The resulting `CayleyKernel X` is an instance of "an abelian group under
addition-with-primer dynamics".  Specialises to:

* `R n + non-zero primer` — the parametric R-family case;
* `Hexagram × YinBit + c_motion` — the historical R_7 instance;
* any future abelian carrier with a chosen primer.

This realises the "tower 本身生生不息 = scale-invariant Cayley structure"
intuition: every abelian carrier admits Cayley kernels, every Cayley
kernel gives the same process algebra theorems.

## Design notes

* `motion s := s + K.primer` uses the AddCommGroup instance on the carrier.
  For F_2 carriers this is XOR-with-primer.  For general abelian carriers
  it is translation-by-primer.
* `terminus` is **vacuously uninhabited** for any Cayley kernel — this is
  the algebraic core of "post-Cayley center universal".  Proof uses
  `add_left_cancel`, valid in any AddCommGroup.
* `native_decide` is **not** used here.  All proofs are generic and
  follow from `K.primer_ne_zero` + `AddCommGroup` axioms.

## Doctrinal anchor

* `义理/W2_Lean形式化已撤回之命题索引.md` — the audit principle:
  math drives, culture names.  Scale-invariance from the math side.
* User dialogue 2026-05-21: "R tower 是一切 sayable 的基础，而这个
  基础本身是生生不息的" — this file is the formal expression.
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Group.Defs

namespace SSBX.Foundation.R

/-! ## §1 The CayleyKernel structure -/

/-- A **Cayley kernel** on an additive abelian carrier `X` is a non-zero
    primer element.

    The associated dynamics is `motion s := s + primer`.  Since the
    primer is non-zero, motion has no fixed points; every state is in
    "center" (= non-terminus).

    Different choices of `primer` give different Cayley kernels on the
    same carrier; conversely, the same algebraic identity `primer +
    primer = 0` (in characteristic-2 carriers) or `motion s ≠ s` (in
    general abelian carriers) holds for all of them. -/
structure CayleyKernel (X : Type*) [AddCommGroup X] where
  /-- The primer element — the addition target that drives motion. -/
  primer : X
  /-- Non-zero requirement: makes terminus uninhabited. -/
  primer_ne_zero : primer ≠ 0

namespace CayleyKernel

variable {X : Type*} [AddCommGroup X] (K : CayleyKernel X)

/-! ## §2 Field / motion / origin -/

/-- The field type carrying this kernel = `X`. -/
abbrev Field : Type _ := X

/-- The origin element = `0 : X`. -/
def origin : X := 0

/-- Motion: `s ↦ s + K.primer`.  The Cayley regular action of `K.primer`. -/
def motion (s : X) : X := s + K.primer

/-- Cayley grounding: motion is addition-with-primer, by definition. -/
@[simp] theorem motion_eq (s : X) : K.motion s = s + K.primer := rfl

/-- The first motion application to the origin = primer. -/
@[simp] theorem motion_origin : K.motion K.origin = K.primer := by
  show K.origin + K.primer = K.primer
  show (0 : X) + K.primer = K.primer
  exact zero_add _

/-! ## §3 Liveness — origin_alive, terminus uninhabited, center universal -/

/-- The origin is "alive": motion takes it off itself. -/
theorem origin_alive : K.motion K.origin ≠ K.origin := by
  rw [motion_origin]
  exact K.primer_ne_zero

/-- A state is a **terminus** iff motion fixes it. -/
def terminus (s : X) : Prop := K.motion s = s

/-- A state is in the **center** iff motion takes it elsewhere. -/
def center (s : X) : Prop := K.motion s ≠ s

/-- **Terminus is uninhabited**: no state is a fixed point of motion.

    Algebraic core: `motion s = s` would force `K.primer = 0` via
    `add_left_cancel`, contradicting `K.primer_ne_zero`. -/
theorem terminus_uninhabited (s : X) : ¬ K.terminus s := by
  intro h
  -- h : K.motion s = s, i.e., s + K.primer = s
  have h' : s + K.primer = s := h
  have hkey : K.primer = 0 := by
    have heq : s + K.primer = s + 0 := by rw [h', add_zero]
    exact add_left_cancel heq
  exact K.primer_ne_zero hkey

/-- **Center is universal**: every state is in center.

    Direct consequence of `terminus_uninhabited`. -/
theorem center_universal (s : X) : K.center s := K.terminus_uninhabited s

/-- Existence of a center state, constructively from `origin`. -/
theorem exists_middle : ∃ s : X, K.center s := ⟨K.origin, K.origin_alive⟩

/-- The origin specifically is in center. -/
theorem origin_is_middle : K.center K.origin := K.origin_alive

/-- Combined collapse summary: terminus empty + center universal. -/
theorem cayley_collapse_summary :
    (∀ s : X, ¬ K.terminus s) ∧ (∀ s : X, K.center s) :=
  ⟨K.terminus_uninhabited, K.center_universal⟩

/-! ## §4 Trace — n-fold iteration -/

/-- The k-fold trace of motion starting from `s`. -/
def trace : Nat → X → X
  | 0, s     => s
  | k+1, s   => K.motion (K.trace k s)

/-- Structural recursion: `trace (k+1)` = motion of `trace k`. -/
@[simp] theorem trace_succ (k : Nat) (s : X) :
    K.trace (k+1) s = K.motion (K.trace k s) := rfl

/-- Trace at zero is identity. -/
@[simp] theorem trace_zero (s : X) : K.trace 0 s = s := rfl

/-! ## §5 ZhongOrbit — center-preserving orbit -/

/-- A **ZhongOrbit** is a `Nat`-indexed sequence of states such that
    every state is in center and consecutive states are linked by motion.

    Existence is guaranteed: any starting state generates one via `trace`. -/
structure ZhongOrbit where
  /-- The state at step `k`. -/
  states   : Nat → X
  /-- Every step is in center (non-terminus). -/
  inMiddle : ∀ k, K.center (states k)
  /-- Each step is motion-of-previous. -/
  step     : ∀ k, K.motion (states k) = states (k+1)

namespace ZhongOrbit

variable {K}

/-- 生生不息: every state is in center.  Direct from `inMiddle`. -/
theorem shengsheng_buxi (o : K.ZhongOrbit) (k : Nat) : K.center (o.states k) :=
  o.inMiddle k

/-- 自指 (self-reference): each step references the previous via motion. -/
theorem self_reference (o : K.ZhongOrbit) (k : Nat) :
    K.motion (o.states k) = o.states (k+1) := o.step k

/-- 自洽 (self-consistency): consecutive states differ.

    Since `motion s ≠ s` (by `center`) and `motion (states k) = states (k+1)`
    (by `step`), we have `states k ≠ states (k+1)`. -/
theorem self_consistent (o : K.ZhongOrbit) (k : Nat) :
    o.states k ≠ o.states (k+1) := by
  intro heq
  apply o.inMiddle k
  rw [o.step k]
  exact heq.symm

/-- Combined: every step has center + step-link + non-collapse. -/
theorem motion_self_consistent (o : K.ZhongOrbit) (k : Nat) :
    K.center (o.states k)
    ∧ (K.motion (o.states k) = o.states (k+1))
    ∧ (o.states k ≠ o.states (k+1)) :=
  ⟨shengsheng_buxi o k, self_reference o k, self_consistent o k⟩

end ZhongOrbit

/-- The canonical orbit generated from any starting state. -/
def canonicalOrbit (s₀ : X) : K.ZhongOrbit where
  states := fun k => K.trace k s₀
  inMiddle := fun k => K.center_universal (K.trace k s₀)
  step := fun _ => rfl

/-- Existence of a ZhongOrbit (constructive, from origin). -/
theorem exists_zhongOrbit : Nonempty K.ZhongOrbit :=
  ⟨K.canonicalOrbit K.origin⟩

/-! ## §6 Layer 2 — momentumDirection (势) -/

/-- The momentum direction of an orbit at step `k`: the (state, next) pair. -/
def momentumDirection (o : K.ZhongOrbit) (k : Nat) : X × X :=
  (o.states k, o.states (k+1))

/-- Momentum direction is genuine: the two components differ. -/
theorem momentumDirection_genuine (o : K.ZhongOrbit) (k : Nat) :
    (K.momentumDirection o k).1 ≠ (K.momentumDirection o k).2 :=
  ZhongOrbit.self_consistent o k

/-- **No telos**: an orbit does not reach a fixed terminal state. -/
theorem momentumDirection_no_telos (o : K.ZhongOrbit) (target : X) (N : Nat) :
    ¬ (∀ k, k ≥ N → o.states k = target) := by
  intro h
  have h_N   : o.states N       = target := h N (Nat.le_refl _)
  have h_N1  : o.states (N + 1) = target := h (N + 1) (Nat.le_succ _)
  have : o.states N = o.states (N + 1) := h_N.trans h_N1.symm
  exact ZhongOrbit.self_consistent o N this

/-! ## §7 Layer 3 — pivotMoment (机) -/

/-- A step is a **pivotMoment** iff this state and the next differ. -/
def pivotMoment (o : K.ZhongOrbit) (k : Nat) : Prop :=
  o.states k ≠ o.states (k+1)

/-- Every step in a ZhongOrbit is a pivotMoment. -/
theorem orbit_is_pivotMoment (o : K.ZhongOrbit) (k : Nat) : K.pivotMoment o k :=
  ZhongOrbit.self_consistent o k

/-! ## §8 Layer 5 — ZhongField (multi-orbit plurality) -/

/-- A **ZhongField** is a non-trivial collection of ZhongOrbits with
    the invariant that at every time step, at least two orbits differ.

    `ever_differentiated` encodes "diversity persists" (反归一). -/
structure ZhongField where
  /-- Number of orbits (focal-processes). -/
  k : Nat
  /-- At least 2 orbits — non-trivial plurality. -/
  k_ge_two : 2 ≤ k
  /-- The orbits themselves. -/
  orbits : Fin k → K.ZhongOrbit
  /-- 反归一: at every time, two orbits disagree. -/
  ever_differentiated : ∀ m, ∃ i j : Fin k,
    i ≠ j ∧ (orbits i).states m ≠ (orbits j).states m

namespace ZhongField

variable {K}

/-- **Flowing**: each orbit in the field moves at every step (automatic
    from ZhongOrbit.self_consistent). -/
theorem flowing (f : K.ZhongField) (m : Nat) (i : Fin f.k) :
    (f.orbits i).states m ≠ (f.orbits i).states (m + 1) :=
  ZhongOrbit.self_consistent (f.orbits i) m

/-- **Harmony**: diversity persists at every time step. -/
theorem harmony_not_same (f : K.ZhongField) (m : Nat) :
    ¬ (∀ i j : Fin f.k, (f.orbits i).states m = (f.orbits j).states m) := by
  rcases f.ever_differentiated m with ⟨i, j, _, hij⟩
  intro hAll
  exact hij (hAll i j)

end ZhongField

/-! ## §9 Layer 6 — aestheticEncounter (美) -/

/-- An **aestheticEncounter**: heart's state at time `k` meets an event,
    and the meeting itself is non-terminus (in center). -/
def aestheticEncounter (heart : K.ZhongOrbit) (event : X) (k : Nat) : Prop :=
  K.center (heart.states k + event)

/-- Aesthetic encounter holds for every (heart, event, k) — directly from
    `center_universal` on the sum. -/
theorem aesthetic_universal (heart : K.ZhongOrbit) (event : X) (k : Nat) :
    K.aestheticEncounter heart event k :=
  K.center_universal _

/-! ## §10 Layer 7 — hasVirtue (德) + shiftOrbit -/

/-- An orbit "has virtue" iff every state is in center. -/
def hasVirtue (o : K.ZhongOrbit) : Prop := ∀ m, K.center (o.states m)

/-- Every ZhongOrbit has virtue (from `inMiddle`). -/
theorem center_orbit_has_virtue (o : K.ZhongOrbit) : K.hasVirtue o := o.inMiddle

/-- Shift an orbit forward by `k` steps. -/
def shiftOrbit (o : K.ZhongOrbit) (k : Nat) : K.ZhongOrbit where
  states   := fun m => o.states (m + k)
  inMiddle := fun m => o.inMiddle (m + k)
  step     := fun m => by
    have h := o.step (m + k)
    -- h : K.motion (o.states (m + k)) = o.states (m + k + 1)
    -- goal: K.motion (o.states (m + k)) = o.states (m + 1 + k)
    rw [show m + 1 + k = m + k + 1 from by omega]
    exact h

/-- Virtue is robust under shift. -/
theorem virtue_robust (o : K.ZhongOrbit) (k : Nat) : K.hasVirtue (K.shiftOrbit o k) :=
  fun m => o.inMiddle (m + k)

/-! ## §11 Layer 8 — principle (理) -/

/-- The **principle** of an orbit IS its state sequence: there is no
    hidden law beyond the trajectory itself. -/
def principle (o : K.ZhongOrbit) : Nat → X := o.states

/-- Principle is the state sequence — by definition. -/
@[simp] theorem principle_inseparable (o : K.ZhongOrbit) : K.principle o = o.states := rfl

/-- Principle is iterated motion from the initial state. -/
theorem principle_is_iterated_motion (o : K.ZhongOrbit) (m : Nat) :
    K.principle o m = K.trace m (o.states 0) := by
  induction m with
  | zero => rfl
  | succ m ih =>
    show o.states (m + 1) = K.trace (m + 1) (o.states 0)
    rw [trace_succ, ← ih]
    show o.states (m + 1) = K.motion (o.states m)
    exact (o.step m).symm

/-! ## §12 Layer 9 — selfSimilarity -/

/-- **Self-similarity**: an orbit shifted by `k` has the same form. -/
theorem selfSimilarity (o : K.ZhongOrbit) (k m : Nat) :
    (K.shiftOrbit o k).states m = o.states (m + k) := rfl

/-! ## §13 Layer 10 — Xin (心): perceiving focal-process -/

/-- **Xin** = an orbit equipped with a response function. -/
structure Xin where
  /-- The underlying orbit (process self-perception). -/
  process : K.ZhongOrbit
  /-- The response function (how this process reads other events). -/
  respond : X → X

namespace Xin

variable {K}

/-- Xin's state at any time is in center. -/
theorem heart_middle (x : K.Xin) (m : Nat) : K.center (x.process.states m) :=
  x.process.inMiddle m

end Xin

/-! ## §14 Layer 11 — feeling (情) -/

/-- **Feeling**: heart's perception of an event at step `k`. -/
def feeling (heart : K.ZhongOrbit) (event : X) (k : Nat) : X :=
  heart.states k + event

/-- A feeling is **well-directed** iff its result is in center. -/
def feelingWellDirected (heart : K.ZhongOrbit) (event : X) (k : Nat) : Prop :=
  K.center (K.feeling heart event k)

/-- Well-directed feeling is equivalent to aesthetic encounter (both
    say "the heart-event meeting lands in center"). -/
theorem feelingWellDirected_iff_aesthetic
    (heart : K.ZhongOrbit) (event : X) (k : Nat) :
    K.feelingWellDirected heart event k ↔ K.aestheticEncounter heart event k :=
  Iff.rfl

/-! ## §15 Layer 12 — traceAccumulation (积)

    Orbit history viewed as a finitely-indexed prefix.

    Note: the parameter `len` is the *length* (= max step index + 1)
    of the prefix.  The carrier type `X` is the (abstract) field type. -/

/-- The **trace accumulation** at length `len`: orbit's history at step `i ≤ len`. -/
def traceAccumulation (o : K.ZhongOrbit) (len : Nat) (i : Fin (len + 1)) : X :=
  o.states i.val

/-- Trace accumulation extends: history at `len + 1` includes history at `len`. -/
theorem traceAccumulation_extends
    (o : K.ZhongOrbit) (len : Nat) (i : Fin (len + 1)) :
    K.traceAccumulation o (len + 1) ⟨i.val, Nat.lt_succ_of_lt i.isLt⟩
      = K.traceAccumulation o len i := rfl

end CayleyKernel

end SSBX.Foundation.R
