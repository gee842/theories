import Becoming.Return

/-!
# What a finite history decides

`Becoming.Renewal` shows that the class of a formation belongs to the run, not to a
configuration: from one configuration, one run renews and another consumes. Here the
same holds for every finite stretch of a run. For every horizon `h`, two runs of
`Renewable` agree on their configurations and actions up to `h`, the focal formation
drawing beyond renewal at each of those steps, while the condition still meets the
dependence on it. Afterwards one run draws within renewal and the focal formation
renews; the other keeps drawing beyond it, and the focal formation consumes. Every
event of the focal formation before `h` is within renewal in both runs, so it is
neither breaking nor undermining.

So a reading decided by the first `h` steps of a run either withholds credit from a
run that the whole-run reading classifies as renewing, or credits one it classifies as
consuming. The work is done by crediting every renewing run: the renewing run itself
draws beyond renewal before `h`, from a stock that absorbs it, and the whole-run reading
credits those draws (`whole_run_credits_overdraw`). The result holds unchanged in the
support-gated law, whose renewal stops below support (`Feedback.prefix_does_not_decide`),
so it does not rest on the absence of feedback.

What a finite history decides depends on the reading:
* The event-level stepwise and cycle readings are fixed by the history up to the step
  after the event, or `p` steps after it. They credit depletion for as long as the
  condition still meets the dependence.
* The formation-level readings over cycles are not fixed by any finite prefix
  (`cycle_reading_not_finite`), nor is the whole-run classification.
* A reading of amounts, "draws no more than is renewed at this step", is fixed by the
  history through the step, credits every event of `withinRenewal` and withholds every draw
  beyond renewal before `h` in both runs (`amount_reading`). It escapes the theorem only
  by not crediting every run the whole-run reading classifies as renewing. It cannot be
  stated on `Web`, whose `draws` carries no amount and which has no renewal rate.

Classifying a stretch of drawing as the whole-run reading does requires knowing where
the run goes, an account of its continuation, not only its past. In `Renewable` the
dynamics are fixed by the actions, so what no prefix decides is the action still to be
taken.

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

namespace Renewable

/-- For every horizon `h`, two runs agree up to `h`, drawing beyond renewal at every
step before it, with every event of the focal formation there within renewal. Then one
renews and the other consumes. -/
theorem prefix_does_not_decide : ∀ h : Nat, ∃ renewing consuming : Run process,
    renewing.AgreeUpTo h consuming ∧ (∀ t, t < h → consuming.act t = 2) ∧
    (∀ t, t < h → (conditions.dependence.along renewing).RenewingAt t .focal ∧
      (conditions.dependence.along consuming).RenewingAt t .focal) ∧
    (conditions.dependence.along renewing).RenewingIn .focal ∧
    (conditions.dependence.along consuming).ConsumingIn .focal
  | 0 => ⟨withinRenewal, beyondRenewal,
      ⟨fun | 0, _ => rfl, fun _ before => absurd before (Nat.not_lt_zero _)⟩,
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

/-- The whole-run reading credits drawing beyond renewal. For every horizon, the
renewing run above draws two units, one beyond renewal, at every step before it, and
every event of its focal formation is active and not consuming. -/
theorem whole_run_credits_overdraw (h : Nat) : ∃ r : Run process,
    (∀ t, t < h → r.act t = 2) ∧ (conditions.dependence.along r).RenewingIn .focal ∧
      ∀ t, (conditions.along r).active t .focal ∧
        ¬ RelationalRenewal.ConsumingIn (conditions.along r) .focal :=
  match prefix_does_not_decide h with
  | ⟨r, _, ⟨_, acts⟩, over, _, renews, _⟩ =>
    ⟨r, fun t before => (acts t before).trans (over t before), renews, fun _ => ⟨trivial,
      RelationalRenewal.renewing_not_consuming ((Web.static_renewingIn _ _).mp renews)⟩⟩

/-- A reading of amounts escapes the horizon. "Draws no more than is renewed", at a step,
is fixed by the history through that step, credits every event of `withinRenewal`, and
withholds every draw before the horizon in both runs above. -/
theorem amount_reading (h : Nat) :
    (∀ t (r r' : Run process), r.AgreeUpTo (t + 1) r' → (r.act t ≤ 1 ↔ r'.act t ≤ 1)) ∧
    (∀ t, withinRenewal.act t ≤ 1) ∧
    ∃ r c : Run process, (conditions.dependence.along r).RenewingIn .focal ∧
      (conditions.dependence.along c).ConsumingIn .focal ∧
      ∀ t, t < h → ¬ r.act t ≤ 1 ∧ ¬ c.act t ≤ 1 :=
  ⟨fun t _ _ ⟨_, acts⟩ => acts t (Nat.lt_succ_self t) ▸ Iff.rfl, fun _ => Nat.le_refl 1,
   match prefix_does_not_decide h with
   | ⟨r, c, ⟨_, acts⟩, over, _, renews, consumes⟩ =>
     ⟨r, c, renews, consumes, fun t before =>
       ⟨fun le => Nat.not_succ_le_self 1
          (Nat.le_trans (Nat.le_of_eq ((acts t before).trans (over t before)).symm) le),
        fun le => Nat.not_succ_le_self 1 (Nat.le_trans (Nat.le_of_eq (over t before).symm) le)⟩⟩⟩

/-- The formation-level reading over cycles of any positive length is not fixed by any
finite prefix. -/
theorem cycle_reading_not_finite (h p : Nat) (positive : 0 < p) :
    ¬ ∀ r r' : Run process, r.AgreeUpTo h r' →
      (conditions.dependence.along r).RenewingInWithin p .focal →
      (conditions.dependence.along r').RenewingInWithin p .focal :=
  fun decided =>
    match finite_reading_credits_consumption h _ decided
      (fun _ renews => (Web.RenewingIn.within_one renews).mono positive) with
    | ⟨_, consumes, renews⟩ => renews.not_consuming consumes

end Renewable

/-! ## The horizon in the support-gated law -/

namespace Feedback

open RelationalRenewal RelationalRenewal.Law

/-- Start `h + 1`, renewal one unit, sustaining need one, focal need zero, no
contribution. Renewal stops below support. -/
def law (h : Nat) (d : Nat → Nat) : Law := ⟨h + 1, 1, 1, 0, d, fun _ => 0⟩

/-- Two units a step before `h`, then the renewal only. -/
def stopping (h t : Nat) : Nat := if t < h then 2 else 1

/-- Two units a step throughout. -/
def continuing (_ : Nat) : Nat := 2

theorem step_two {h t m : Nat} {d : Nat → Nat} (high : (law h d).level t = m + 2)
    (two : d t = 2) : (law h d).level (t + 1) = m + 1 := by
  rw [level_succ, high,
    if_pos (show (law h d).needG ≤ m + 2 from Nat.succ_le_succ (Nat.zero_le _)),
    if_pos (show (law h d).needF ≤ m + 2 from Nat.zero_le _)]
  show m + 1 + 1 + 1 + 0 - d t = m + 1
  rw [two]
  exact add_sub_self (m + 1) 2

theorem step_one {h t : Nat} {d : Nat → Nat} (one : (law h d).level t = 1) (same : d t = 1) :
    (law h d).level (t + 1) = 1 := by
  rw [level_succ, one, if_pos (show (law h d).needG ≤ 1 from Nat.le_refl 1),
    if_pos (show (law h d).needF ≤ 1 from Nat.zero_le _)]
  show 1 + 1 + 0 - d t = 1
  rw [same]

/-- Before the horizon, the level falls by one a step under either schedule. -/
theorem descending (h : Nat) (d : Nat → Nat) (two : ∀ t, t < h → d t = 2) :
    ∀ k, k ≤ h → (law h d).level k + k = h + 1
  | 0, _ => rfl
  | k + 1, le => by
    have ih := descending h d two k (Nat.le_of_succ_le le)
    have bound : 2 + k ≤ (law h d).level k + k := by
      rw [ih, Nat.add_comm 2 k]
      exact Nat.succ_le_succ le
    obtain ⟨m, hm⟩ := Nat.le.dest (le_of_add_le_add_right k bound)
    have high : (law h d).level k = m + 2 := by rw [← hm, Nat.add_comm]
    rw [step_two high (two k (Nat.lt_of_succ_le le))]
    rw [high] at ih
    rw [Nat.add_succ, ← Nat.succ_add]
    exact ih

theorem at_horizon (h : Nat) : (law h (stopping h)).level h = 1 :=
  add_right_cancel h ((descending h (stopping h) (fun _ before => if_pos before) h
    (Nat.le_refl h)).trans (Nat.add_comm h 1))

theorem after_horizon (h : Nat) : ∀ j, (law h (stopping h)).level (h + j) = 1
  | 0 => at_horizon h
  | j + 1 => step_one (after_horizon h j) (if_neg (Nat.not_lt_of_le (Nat.le_add_right h j)))

theorem supported (h t : Nat) : 1 ≤ (law h (stopping h)).level t :=
  match Nat.lt_or_ge t h with
  | .inl before =>
    le_of_add_le_add_right t (Nat.le_trans
      (show 1 + t ≤ h + 1 from (Nat.add_comm 1 t) ▸ Nat.succ_le_succ (Nat.le_of_lt before))
      (Nat.le_of_eq (descending h (stopping h) (fun _ b => if_pos b) t
        (Nat.le_of_lt before)).symm))
  | .inr after =>
    match Nat.le.dest after with
    | ⟨j, sum⟩ => sum ▸ Nat.le_of_eq (after_horizon h j).symm

/-- For every horizon, in the support-gated law, from the same start, under draws that
agree before the horizon (two units, one beyond renewal): stopping there renews,
continuing consumes. The renewing schedule never reaches the threshold below which
renewal stops, so the feedback does not change the horizon result. -/
theorem prefix_does_not_decide (h : Nat) :
    (law h (stopping h)).start = (law h continuing).start ∧
    (∀ t, t < h → stopping h t = continuing t) ∧
    RenewingIn (law h (stopping h)).unfolding .focal ∧
    ConsumingIn (law h continuing).unfolding .focal :=
  ⟨rfl, fun _ before => if_pos before,
   fun _ _ t g depends => match g, depends with
     | .sustaining, _ => supported h t,
   (overdraw_consuming (law h continuing) Nat.zero_lt_one (Nat.zero_le 1) (T0 := 0)
     fun _ _ => Nat.lt_succ_self 1).1⟩

end Feedback

end Becoming
