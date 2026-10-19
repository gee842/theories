import Becoming.Acceptance
import Becoming.FrontierFrames

/-!
# Scores over the options of a step: acceptance, restriction and estimates

`Becoming.Acceptance` states, for allowed choices of any type, what an accept bit given priority
over a base score does and does not protect, what restricting the choices costs, and how far a
choice best by an estimate can fall short. This module reads those laws on a frame of the spine,
the allowed choices at a configuration being its options: the configurations one move of the
frame's process reaches from it (`FrontierFrames.Options`). The scores are supplied integer
values of configurations, as in `Becoming.Acceptance`; nothing here derives a score or a warrant
for a requested change.

* **Acceptance protects only what the best options keep.** With a positive lift, every option best
  by the score with acceptance keeps access for a requested change exactly where every option best
  by the base score does (`access_iff`); where no best option keeps it, acceptance restores
  nothing (`no_access`).
* **Restricting to the options loses score, exactly.** Against a configuration best among all, the
  loss of an option best among the options is nonnegative and least among the options
  (`restriction_loss`).
* **Estimated scores.** An option best by an estimate within `err` of the actual score is within
  `2 * err` of every option (`estimate_bound`).

Each theorem is the law of `Becoming.Acceptance` it names, read on the options of a step; none is
a further result. No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative Acceptance FrontierFrames

namespace AcceptanceFrames

variable {S A C : Type} {F : Frame S A C}

/-- **Every option best by the score with acceptance keeps access exactly where every option best
by the base score does**, the lift positive. -/
theorem access_iff (s : S) (access : S → Prop) (q : S → Int) (lift : Int) (positive : 0 < lift) :
    (∀ x, Best (fun y : S × Bool => Options F s y.1) (AcceptScore q lift) x → access x.1) ↔
      (∀ t, Best (Options F s) q t → access t) :=
  every_optimum_has_access_iff (Options F s) access q lift positive

/-- **Where no option best by the base score keeps access, no best option does.** -/
theorem no_access (s : S) (access : S → Prop) (q : S → Int)
    (conflict : ∀ t, Best (Options F s) q t → ¬ access t) :
    ¬ ∃ t, Best (Options F s) q t ∧ access t :=
  no_base_optimal_access (Options F s) access q conflict

/-- **Restricting to the options loses score, exactly**: against a configuration best among all,
the loss of an option best among the options is nonnegative and least among them. -/
theorem restriction_loss {s : S} (q : S → Int) (u v : S) (best : Best (fun _ => True) q u)
    (bestOption : Best (Options F s) q v) :
    0 ≤ q u - q v ∧ ∀ t, Options F s t → q u - q v ≤ q u - q t :=
  unavoidable_score_loss (Options F s) q u v best bestOption

/-- **An option best by an estimate within `err` of the actual score is within `2 * err` of every
option.** -/
theorem estimate_bound {s : S} (actual estimate : S → Int) (err : Int)
    (lower : ∀ t, Options F s t → actual t - err ≤ estimate t)
    (upper : ∀ t, Options F s t → estimate t ≤ actual t + err) (chosen : S)
    (best : Best (Options F s) estimate chosen) :
    ∀ t, Options F s t → actual t - actual chosen ≤ 2 * err :=
  approximate_score_bound (Options F s) actual estimate err lower upper chosen best

end AcceptanceFrames

end Becoming
