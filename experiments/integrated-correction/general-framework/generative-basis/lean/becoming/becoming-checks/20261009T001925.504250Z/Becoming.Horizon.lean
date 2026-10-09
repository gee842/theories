import Becoming.Dependence

/-!
# What a finite history decides

`Becoming.Renewal` shows that the class of a formation belongs to the run, not to a
configuration: from one configuration, one run renews and another consumes. Here the
same holds for every finite stretch of a run. For every horizon `h`, two runs of the
commons agree on their configurations and actions up to `h`, the focal formation
drawing beyond renewal at each of those steps, while the condition still meets the
dependence on it. Afterwards one run draws within renewal and the focal formation
renews; the other keeps drawing beyond it, and the focal formation consumes. Every
event of the focal formation up to `h` is within renewal in both runs, so neither
stepwise reading withholds it.

So a reading decided by the first `h` steps of a run either withholds credit from a
run in which the focal formation renews, or credits one in which it consumes. The
stepwise readings, each decided by one step, credit depletion for as long as the
condition still meets the dependence. Classifying a stretch of drawing as consuming
requires knowing where the run goes, an account of its continuation, not only its
past.

No ethical predicate, ranking or axiom occurs. Whether an actual history continues
one way or the other is a question for inquiry into it.
-/

namespace Becoming

open Generative

universe u v

variable {S : Type u} {A : Type v}

/-- A run preceded by one admissible step into its start. -/
def Run.cons {P : Process S A} (s : S) (a : A) (r : Run P) (into : P.step s a (r.state 0)) :
    Run P :=
  ⟨fun | 0 => s | t + 1 => r.state t, fun | 0 => a | t + 1 => r.act t,
    fun | 0 => into | t + 1 => r.step t⟩

/-- Two runs agree up to `h`: the same configurations up to `h` and the same actions
before it. -/
def Run.AgreeUpTo {P : Process S A} (h : Nat) (r r' : Run P) : Prop :=
  (∀ t, t ≤ h → r.state t = r'.state t) ∧ ∀ t, t < h → r.act t = r'.act t

namespace Commons

/-- For every horizon `h`, two runs agree up to `h`, drawing beyond renewal at every
step before it, with every event of the focal formation there within renewal. Then one
renews and the other consumes. -/
theorem prefix_does_not_decide : ∀ h : Nat, ∃ renewing consuming : Run process,
    renewing.AgreeUpTo h consuming ∧ (∀ t, t < h → consuming.act t = 2) ∧
    (∀ t, t < h → (conditions.dependence.along renewing).RenewingAt t .focal ∧
      (conditions.dependence.along consuming).RenewingAt t .focal) ∧
    (conditions.dependence.along renewing).RenewingIn .focal ∧
    (conditions.dependence.along consuming).ConsumingIn .focal
  | 0 => ⟨sharing, winning, ⟨fun | 0, _ => rfl, fun _ before => absurd before (Nat.not_lt_zero _)⟩,
      fun _ before => absurd before (Nat.not_lt_zero _),
      fun _ before => absurd before (Nat.not_lt_zero _),
      fun _ _ _ _ g depends => match g, depends with
        | .sustaining, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩,
      ⟨0, (), trivial, .sustaining, 1, trivial, fun | _ + 2, _ => Nat.zero_lt_one⟩⟩
  | h + 1 =>
    match prefix_does_not_decide h with
    | ⟨r, c, ⟨states, acts⟩, over, within, renews, consumes⟩ =>
      have supported : 1 ≤ r.state 0 := (renews 0 () (Or.inr trivial) 0 .sustaining trivial).1
      have first : ∀ q : Run process, q.state 0 = r.state 0 → ∀ into,
          (conditions.dependence.along (Run.cons (r.state 0 + 1) 2 q into)).RenewingAt 0 .focal :=
        fun _ start _ => ⟨trivial, fun _ _ g depends => match g, depends with
          | .sustaining, _ => ⟨Nat.succ_le_succ (Nat.zero_le _),
              Nat.le_trans supported (Nat.le_of_eq start.symm)⟩⟩
      have start : c.state 0 = r.state 0 := (states 0 (Nat.zero_le h)).symm
      ⟨Run.cons (r.state 0 + 1) 2 r rfl, Run.cons (r.state 0 + 1) 2 c (start ▸ rfl),
       ⟨fun | 0, _ => rfl | t + 1, upTo => states t (Nat.le_of_succ_le_succ upTo),
        fun | 0, _ => rfl | t + 1, before => acts t (Nat.lt_of_succ_lt_succ before)⟩,
       fun | 0, _ => rfl | t + 1, before => over t (Nat.lt_of_succ_lt_succ before),
       fun | 0, _ => ⟨first r rfl rfl, first c start _⟩
           | t + 1, before => within t (Nat.lt_of_succ_lt_succ before),
       fun _ _ _ t g depends => match t, g, depends with
         | 0, .sustaining, _ => ⟨Nat.succ_le_succ (Nat.zero_le _), supported⟩
         | t + 1, .sustaining, _ => renews 0 () (Or.inr trivial) t .sustaining trivial,
       match consumes with
       | ⟨_, _, _, g, T, depends, below⟩ =>
         ⟨0, (), trivial, g, T + 1, depends, fun
           | t + 1, later => below t (Nat.lt_of_succ_lt_succ later)⟩⟩

/-- A reading decided by the first `h` steps of a run, crediting every run in which the
focal formation renews, credits a run in which it consumes. -/
theorem finite_reading_credits_consumption (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (credits : ∀ r, (conditions.dependence.along r).RenewingIn .focal → reading r) :
    ∃ r, (conditions.dependence.along r).ConsumingIn .focal ∧ reading r :=
  match prefix_does_not_decide h with
  | ⟨renewing, consuming, agree, _, _, renews, consumes⟩ =>
    ⟨consuming, consumes, decided renewing consuming agree (credits renewing renews)⟩

end Commons

end Becoming
