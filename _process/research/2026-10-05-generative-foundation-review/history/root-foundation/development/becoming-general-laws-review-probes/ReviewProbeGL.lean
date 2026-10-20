import Becoming.Substitution
import Becoming.LossMatching
import Becoming.Countdown
import Becoming.Copying

/-!
# Probes of the seventeenth review (general laws of 13–14 October 2026)

Scratch only; not part of the package.

* `one_change_keeps` (finding G3): for one particular change of the consumer's own dependence,
  consumption is kept though no dependence the change leaves witnesses it, so the "exactly" of
  `Web.consumingIn_kept_iff` holds only for "kept under every change".
* `lost_side_is_worse` (finding G1): a configuration that loses the common support can be the
  worse side of a strict loss match; `not_strictLossMatch_of_base_lost` says it is never the
  better side.
* `longer_word_draws_more` (finding G2): among words of different lengths, the word with more
  unlike pairs can draw more although an unlike attachment draws less, so `use_lt_iff` needs
  words of one length.
* `done_before_without_apart` (finding G5): `Counts` does not make pending and finished apart,
  so "no shorter run finishes" needs `apart` (`not_done_before`), not `pending_before` alone.
-/

namespace Becoming.ReviewProbeGL

open Generative Becoming

/-! ## G3 -/

/-- The lone consumer with its dependence moved from step 0 to step 1. -/
def moved : Web Unit Unit := { Substitution.Lone.web with requires := fun t _ _ => t = 1 }

theorem one_change_keeps :
    Web.DependenceChanged Substitution.Lone.web moved () 0 ∧ moved.ConsumingIn () ∧
      ¬ (Substitution.Lone.web).ConsumingThrough () 0 :=
  ⟨⟨fun _ _ => rfl, fun _ _ => Iff.rfl, fun _ _ _ left => absurd (left rfl) (Nat.not_lt_zero _)⟩,
   ⟨0, (), trivial, (), 1, rfl, fun t lt => match t, lt with
     | 0, h => absurd h (Nat.not_lt_zero 1)
     | 1, h => absurd h (Nat.lt_irrefl 1)
     | _ + 2, _ => Nat.zero_lt_one⟩,
   Substitution.Lone.own_witness_lost.2.1⟩

/-! ## G1 -/

/-- Two configurations: `true` realizes every claim, `false` none. -/
def frame : Frame Bool Unit Bool := ⟨⟨fun _ _ _ => False⟩, fun s _ => s = true⟩

/-- Every claim rests on the claim `false`; the configuration `false` loses it, and is strictly
matched below `true`. -/
theorem lost_side_is_worse :
    (∀ s c, frame.realized s c → frame.realized s false) ∧ ¬ frame.realized false false ∧
      frame.StrictLossMatch (fun _ _ => True) true false :=
  ⟨fun _ _ realized => realized, fun h => Bool.noConfusion h,
   ⟨id, fun _ lost => absurd rfl lost, fun _ lost => absurd rfl lost,
    fun _ _ lost => absurd rfl lost, false, fun h => Bool.noConfusion h,
    fun _ lost => absurd rfl lost⟩⟩

/-! ## G2 -/

/-- First draw 1, 2 after a like token, 1 after an unlike one: ABAB (three unlike pairs) uses 4,
AA (none) uses 3. -/
theorem longer_word_draws_more :
    Copying.use (Copying.pairDraw 1 2 1) none [true, false, true, false] = 4 ∧
      Copying.use (Copying.pairDraw 1 2 1) none [true, true] = 3 ∧
      Copying.unlikeFrom true [false, true, false] = 3 ∧ Copying.unlikeFrom true [true] = 0 ∧
      (1 : Nat) < 2 :=
  ⟨rfl, rfl, rfl, rfl, Nat.lt_succ_self 1⟩

/-! ## G5 -/

def tick : Nat → Option Nat
  | 0 => none
  | n + 1 => some n

theorem counts : Countdown.Counts tick (fun _ => True) (fun _ => True) id id :=
  ⟨fun s _ _ pos => match s, pos with
    | n + 1, _ => ⟨n, rfl, trivial, rfl, rfl⟩,
   fun
     | 0, _, pos, _ => absurd pos (Nat.lt_irrefl 0)
     | _ + 1, _, _, zero => Nat.noConfusion zero,
   fun
     | 0, _, _ => rfl
     | _ + 1, _, zero => Nat.noConfusion zero⟩

/-- With pending and finished not apart, a run of `0 ≤ work` ticks is already finished. -/
theorem done_before_without_apart :
    Countdown.Counts tick (fun _ => True) (fun _ => True) id id ∧
      Countdown.ticks tick 0 3 = some 3 ∧ 0 ≤ id 3 ∧ (fun _ : Nat => True) 3 :=
  ⟨counts, rfl, Nat.zero_le _, trivial⟩

end Becoming.ReviewProbeGL
