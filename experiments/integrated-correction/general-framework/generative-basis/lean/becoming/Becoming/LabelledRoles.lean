import Becoming.Horizon
import Becoming.Roles
import Becoming.Inquiry
import Becoming.Testing

/-!
# Runs read through roles and recurrence

The run readings of `Becoming.Roles` (a web's activity along a run, `Web.active_along`; what
bears on it, `Web.bearing`; ending together, `Web.coextinct`; the predation witness,
`Predation.fox_ends`) and of `Becoming.Dissipation` (a Boolean sequence recurs as a run exactly
where its one-member family recurs, `Sequences.recurs_iff`). The laws they read are stated over
the web and the flow in those modules, which do not import the frame.

Every declaration moved here unchanged, with its name (study section 180, board item W). Every
declaration has an empty axiom report.

It also holds the readings along runs of `Becoming.Testing` (judging a class, the finite readings of
renewal, and `sees_narrow`, which only they use), moved here unchanged with their names (board item
W, second batch).
-/

/-! ## Roles along a run (moved from `Becoming.Roles`) -/

open Generative

namespace Becoming

variable {F C X : Type}

namespace Web

variable (W : Web X X)

/-- Dependence at a positive need on embodied relata at a step, as a process on
relata. -/
def bearing (t : Nat) : Process X Unit :=
  ⟨fun g _ y => (W.requires t g y ∧ 0 < W.need t g y) ∧ W.Embodied y⟩

variable {W}

/-- Under `Dependent`, activity at a step passes along every chain of dependence on
embodied relata. -/
theorem active_along (dependent : W.Dependent) (t : Nat) :
    Invariant (W.bearing t) (W.active t) :=
  fun _ _ _ ⟨bearing, embodied⟩ active => embodied.active_of_bearing dependent active bearing

/-- Coextinction: under `Dependent`, a relatum that is not active at a step ends there
every formation whose chain of dependence on embodied relata reaches it. -/
theorem coextinct (dependent : W.Dependent) {t : Nat} {g y : X}
    (chain : Reach (W.bearing t) g y) (ended : ¬ W.active t y) : ¬ W.active t g :=
  fun active => ended ((active_along dependent t).reach chain active)

variable (W : Web F C)

end Web

namespace Predation

/-- The fox depends on the hare, so it ends with it. -/
theorem fox_ends : ∀ t, 2 < t → ¬ web.active t .fox :=
  fun t later => Web.coextinct dependent
    (Reach.of_step (a := ()) ⟨⟨.inr rfl, Nat.zero_lt_one⟩, embodied .hare⟩) (hare_ends t later)

end Predation

end Becoming

/-! ## A sequence's recurrence as a run (moved from `Becoming.Dissipation`) -/

namespace Becoming

variable {F C : Type}

/-- **Recurrence is one notion.** The moves of a run of sequences recur (`Sequences.Recurs` of
`Becoming.Horizon`) exactly where `true` is moved at arbitrarily late steps by the family of one
member (`Becoming.Recurs` of `Becoming.Change`). -/
theorem Sequences.recurs_iff (r : Run (Becoming.Sequences.process Bool)) :
    Becoming.Sequences.Recurs r ↔ Becoming.Recurs [()] (fun _ m => r.act m = true) :=
  ⟨fun recurs N => match recurs N with
    | ⟨m, later, yes⟩ => ⟨m, (), later, .head _, yes⟩,
   fun recurs n => match recurs n with
    | ⟨m, _, later, _, yes⟩ => ⟨m, later, yes⟩⟩

end Becoming

/-! ## Judging a class of webs along runs (moved from `Becoming.Testing`) -/

namespace Becoming

open Generative Generative.InquirySufficiency

variable {F C : Type}

/-- Belief narrows where the believed histories do. -/
theorem sees_narrow {X : Type} {B B' : X → Prop} (narrower : ∀ x, B' x → B x) :
    ∀ s, sees B' s → sees B s
  | _, ⟨x, believed, same⟩ => ⟨x, narrower x believed, same⟩

namespace Web

variable (W : Web F C)

variable {W} {obs obs' : F → C → Prop} {g : F} {l l' : Nat → C → Nat}

variable {H : Type} {admissible : (Nat → C → Nat) → H → Prop} {a : H}

/-- **The bridge to `Becoming.Inquiry`.** A judgment through a formation's couplings is a common
response over the class alike through it: admissible at every history alike with the actual
through its couplings. -/
theorem class_judge_iff {t : Nat} :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
        (sees (W.ClassThrough obs g l t)) a ↔ ∀ l', W.AlikeThroughUpTo obs g l l' t → admissible l' a :=
  commonResponse_judge_iff

/-- Later steps narrow the class and keep every common response. -/
theorem class_judge_later {t t' : Nat} (le : t ≤ t')
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (W.ClassThrough obs g l t)) a) :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
      (sees (W.ClassThrough obs g l t')) a :=
  commonResponse_antitone (sees_narrow fun _ alike => alike.earlier le) common

/-- More coupling by level narrows the class and keeps every common response. -/
theorem class_judge_widen (larger : ∀ g c, obs g c → obs' g c) {t : Nat}
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (W.ClassThrough obs g l t)) a) :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
      (sees (W.ClassThrough obs' g l t)) a :=
  commonResponse_antitone (sees_narrow fun _ alike => alike.of_obs larger) common

end Web

namespace Flow

variable (L : Flow F C) (W : Web F C)

variable {L W} {L' : Flow F C} {W' : Web F C} {obs obs' : F → C → Prop} {part : F → Bool}
  {g : F}

/-- A judgment from within the coupling closure holds with and without a part beyond it:
every response common to the class alike through the formation is admissible under both levels. -/
theorem class_judge_beyond {H : Type} {admissible : (Nat → C → Nat) → H → Prop} {a : H}
    {l₀ : Nat → C → Nat} (without : L.WithheldLevels part W l₀) {f : F}
    (balanced : ∀ t g c, L.WithinCoupling W obs f g → W.CoupledInto obs g c →
      L.BalancesOn W [c] t)
    (beyond : ∀ h, part h = true → ¬ L.WithinCoupling W obs f h)
    (within : L.WithinCoupling W obs f g) {t : Nat}
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (W.ClassThrough obs g W.level t)) a) :
    admissible W.level a ∧ admissible l₀ a :=
  ⟨Web.class_judge_iff.mp common W.level fun s _ => Web.AlikeThrough.refl s,
   Web.class_judge_iff.mp common l₀ fun s _ =>
     uncoupled_beyond_coupling without balanced beyond s g within⟩

end Flow

namespace Renewable

/-- A reading decided by the first `h` steps of a run, including no run in which the focal
formation consumes, excludes a run in which it renews. -/
theorem finite_reading_withholds_renewal (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (sound : ∀ r, reading r → ¬ (conditions.dependence.along r).ConsumingIn .focal) :
    ∃ r, (conditions.dependence.along r).RenewingIn .focal ∧ ¬ reading r :=
  match prefix_does_not_decide h with
  | ⟨renewing, consuming, agree, _, _, renews, consumes⟩ =>
    ⟨renewing, renews, fun reads => sound consuming (decided renewing consuming agree reads)
      consumes⟩

/-- **No finite reading is exact.** Where the continuation is open, no reading decided by the
first `h` steps of a run is the whole-run classification. -/
theorem no_exact_finite_reading (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r') :
    ¬ ∀ r, reading r ↔ (conditions.dependence.along r).RenewingIn .focal :=
  fun exact => match finite_reading_withholds_renewal h reading decided
      (fun r reads => Web.renewing_not_consuming ((exact r).mp reads)) with
    | ⟨r, renews, unread⟩ => unread ((exact r).mpr renews)

end Renewable

end Becoming
