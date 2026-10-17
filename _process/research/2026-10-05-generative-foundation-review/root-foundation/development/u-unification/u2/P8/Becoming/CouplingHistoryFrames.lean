import Becoming.Bridge

/-!
# The coupling law's histories as traces of its frame

`JointContinuationClassification` has one event law from an initial configuration: retaining
or releasing a coupling, then activating the left, the right or, only where retained, both
together. Its histories are two events through a middle configuration, admissible where both are
steps of the law, and they realize the claims of their final configuration. `RelationalBecoming`
reads the law as a process (`RelationalBecoming.process`) with its claims realized at
configurations (`RelationalBecoming.realized`); `RelationalGrounding` compares the retained and
released regimes by the joint bundles they make possible (`jointInventory`), which
`Becoming.Bridge` reads as a frame with no moves (`Frame.ofInventory`). This module reads the law
and its claims as one frame (`frame`), its admissible histories as two-step traces of it from the
initial configuration (`admissible_trace`, `trace_admissible`), and states the results there.

* **A history means its endpoint**: the claims a history realizes are those the frame realizes at
  its final configuration (`history_meaning`).
* **Retaining does not force joint activation.** Retaining the coupling keeps a trace from the
  initial configuration ending where both claims are realized, yet the same retained law has a
  trace ending where only the left claim is realized (`retained_left_only`).
* **The joint description separates the regimes**: on the frame of joint bundles, the released
  and the retained regimes realize different bundles (`joint_description_separates`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace CouplingHistoryFrames

open Generative JointContinuationClassification

/-- The coupling law with the claims realized at each configuration. -/
def frame : Frame Configuration Event Claim :=
  ⟨RelationalBecoming.process, RelationalBecoming.realized⟩

/-- An admissible history is a two-step trace of the frame's process from the initial
configuration. -/
theorem admissible_trace {h : History} (admissible : Admissible h) :
    Trace frame.P .initial [h.first, h.second] h.final :=
  .cons admissible.1 (.cons admissible.2 (.nil _))

/-- Every two-step trace of the frame's process from the initial configuration is an admissible
history through some middle configuration. -/
theorem trace_admissible {first second : Event} {final : Configuration}
    (trace : Trace frame.P .initial [first, second] final) :
    ∃ middle, Admissible ⟨first, middle, second, final⟩ :=
  match trace_cons_iff.mp trace with
  | ⟨middle, step, rest⟩ => ⟨middle, step, trace_singleton_iff.mp rest⟩

/-- **A history realizes exactly the claims the frame realizes at its final configuration.** -/
theorem history_meaning (h : History) (c : Claim) : Realized h c ↔ frame.realized h.final c :=
  RelationalBecoming.history_meaning h c

/-- **Retaining the coupling does not force joint activation.** Some trace from the initial
configuration beginning with retaining ends where every claim is realized, and the trace
retaining then activating the left ends where the left claim is realized and the right is
not. -/
theorem retained_left_only :
    (∃ second final, Trace frame.P .initial [.retain, second] final ∧
      ∀ c, frame.realized final c) ∧
    Trace frame.P .initial [.retain, .activateLeft] .leftActive ∧
    frame.realized .leftActive .leftRealized ∧ ¬ frame.realized .leftActive .rightRealized :=
  match RelationalGrounding.retained_possibility_does_not_force_joint_actualization with
  | ⟨⟨admissible, _⟩, left, notRight, ⟨h, ⟨jointly, first⟩, all⟩⟩ =>
    ⟨⟨h.second, h.final, Eq.subst (motive := fun e => Trace frame.P .initial [e, h.second] h.final)
        first (admissible_trace jointly),
      fun c => (history_meaning h c).mp (all c True.intro)⟩,
     admissible_trace admissible,
     (history_meaning RelationalGrounding.retainedLeft _).mp left,
     fun right => notRight ((history_meaning RelationalGrounding.retainedLeft _).mpr right)⟩

/-- **The joint description separates the regimes**: on the frame of joint bundles the released
and the retained regimes realize different bundles. -/
theorem joint_description_separates :
    (Frame.ofInventory RelationalGrounding.jointInventory).realized .released ≠
      (Frame.ofInventory RelationalGrounding.jointInventory).realized .retained :=
  RelationalGrounding.joint_description_separates

end CouplingHistoryFrames

end Becoming
