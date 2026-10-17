import Becoming.Frame
import GenerativeLossComparison

/-!
# Strict comparisons carried along runs and reachable configurations

`GenerativeLossComparison` states transport laws for a supplied comparison `Le` of continuations
(`b` at least as well supported as `a`) and its strict part `Strict Le`: a strict anchor carries
over to an alteration that is no worse in the matched sense `NoWorse` wherever every no-worse
alteration is weakly comparable (`Compatible NoWorse Le`) and `Le` is transitive, and a strict
comparison of feasible options' realizations supplies a reason (`PracticalBridge`).

This module reads them off the base. The continuations are a frame's configurations, and
`NoWorse` is read off the frame: `t` is no worse than `s` where `t` realizes every claim `s`
realizes, so no claim of `s` is lost. The feasible options are the configurations a process
reaches from where it is. The comparison `Le` and the reason stay supplied, as in the source.

* **A strict anchor holds along a run that loses no claim.** If a configuration is strictly
  better supported than a baseline, it stays so at every configuration of a run from it that
  keeps every claim at every step (`strict_above_along`).
* **A strict rejection holds along a run that gains no claim.** If the first configuration of a
  run is strictly worse supported than a baseline, so is every later one where no step realizes
  a claim the step before did not (`strict_below_along`).
* **Strict comparison among reachable configurations supplies a reason.** Where strict
  comparison between configurations reachable from `s` supplies a reason to move from the first
  to the second, a strict anchor followed by a weak improvement does (`reachable_reason`).

No ethical predicate, ranking or axiom occurs: `Le` and the reason are supplied.
-/

namespace Becoming

open Generative GenerativeLossComparison

universe u v w

namespace StrictTransportRuns

variable {S : Type u} {A : Type v} {C : Type w}

/-- **A strict anchor holds along a run that loses no claim.** With a transitive comparison of
a frame's configurations under which keeping every claim is weakly comparable, a configuration
strictly better supported than a baseline at the start of a run stays strictly better supported
at every later configuration, where each step keeps every claim realized before it. -/
theorem strict_above_along {F : Frame S A C} {Le : S → S → Prop} (trans : Transitive Le)
    (compatible : Compatible (fun s t => ∀ c, F.realized s c → F.realized t c) Le)
    (r : Run F.P) {baseline : S} (anchor : Strict Le baseline (r.state 0))
    (keeps : ∀ n c, F.realized (r.state n) c → F.realized (r.state (n + 1)) c) :
    ∀ n, Strict Le baseline (r.state n)
  | 0 => anchor
  | n + 1 => matched_loss_reduction_preserves_priority trans compatible
      (strict_above_along trans compatible r anchor keeps n) (keeps n)

/-- **A strict rejection holds along a run that gains no claim.** With a transitive comparison
of a frame's configurations under which keeping every claim is weakly comparable, a run whose
first configuration is strictly worse supported than a baseline stays strictly worse supported
at every later configuration, where no step realizes a claim the configuration before it did not
realize. -/
theorem strict_below_along {F : Frame S A C} {Le : S → S → Prop} (trans : Transitive Le)
    (compatible : Compatible (fun s t => ∀ c, F.realized s c → F.realized t c) Le)
    (r : Run F.P) {baseline : S} (anchor : Strict Le (r.state 0) baseline)
    (gainsNone : ∀ n c, F.realized (r.state (n + 1)) c → F.realized (r.state n) c) :
    ∀ n, Strict Le (r.state n) baseline
  | 0 => anchor
  | n + 1 => matched_loss_increase_preserves_rejection trans compatible
      (strict_below_along trans compatible r anchor gainsNone n) (gainsNone n)

/-- **Strict comparison among reachable configurations supplies a reason.** Where a strict
comparison between configurations reachable from `s` supplies a reason to move from the first
to the second, a baseline and an improved configuration both reachable from `s`, with the
baseline strictly below some configuration that the improved one is weakly above, supply that
reason. -/
theorem reachable_reason {P : Process S A} {s : S} {Le : S → S → Prop} {Reason : S → S → Prop}
    (trans : Transitive Le) (bridge : PracticalBridge Le (Reach P s) (fun t => t) Reason)
    {baseline original improved : S} (reachedBaseline : Reach P s baseline)
    (reachedImproved : Reach P s improved) (anchor : Strict Le baseline original)
    (improvement : Le original improved) : Reason baseline improved :=
  transported_comparison_supplies_reason trans bridge reachedBaseline reachedImproved anchor
    improvement

end StrictTransportRuns

end Becoming
