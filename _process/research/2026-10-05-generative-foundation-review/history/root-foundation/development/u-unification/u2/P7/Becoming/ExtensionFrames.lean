import Becoming.Bridge

/-!
# Generative extensions on frames: new relevant content and surviving responses

`GenerativeComparison` states its laws for an inventory of histories and a functional situation:
a generative extension's new realization is positively relevant under living significance
(`new_realization_has_positive_relevance`), and restricting the feasible options keeps a
response no feasible option generatively extends (`feasible_restriction_preserves_survivor`).
`Becoming.Bridge` reads the inventory off a frame (`Frame.inventory`, with `Extension` the
source's generative extension) and a functional situation as one step of a process at a
configuration (`situationProcess`), and states the lifted comparison, reason and selection laws
for every frame.

This module states the two laws of the base.

* **A generative extension realizes new relevant content.** Under the continuation condition, a
  generative extension of a frame's configuration realizes a claim the configuration lacks that
  is positively relevant read from significance (`Frame.relevance`) at the extension
  (`extension_new_relevance`).
* **A functional situation's survivors are the lifted survivors of its frame.** On the one-step
  frame of a functional situation, a response survives the generative-extension filter exactly
  when it is live and no live response liftedly extends it (`survives_iff_lifted`).
* **Restricting the responses keeps a survivor.** On that frame, restricting the enabled
  responses to a subfamily containing a surviving response keeps it surviving
  (`restricted_survives`). This needs the frame to be functional: on a frame where a response
  has several outcomes, removing outcomes can make a response liftedly extended.

No ethical predicate, ranking or axiom occurs; living significance holds here as a theorem of the
continuation condition, which is named.
-/

namespace Becoming

open Generative GenerativeComparison

namespace ExtensionFrames

/-- **A generative extension realizes new relevant content.** Under the continuation condition,
where `t` generatively extends `s` on a frame, `t` realizes a claim `s` lacks that is positively
relevant at `t`, read from significance. -/
theorem extension_new_relevance {S A Q F Pos : Type} (M : Frame S A Q) (living : Q → Prop)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) {s t : S} (extension : Extension M living s t) :
    ∃ c, M.relevance living sig formation step t c ∧ ¬ M.realized s c :=
  new_realization_of_unrestricted (inventory := M.inventory living) unrestricted formation step
    extension

variable {S A C : Type}

/-- **A functional situation's survivors are the lifted survivors of its frame.** On the
one-step frame of a functional situation at `s`, a response survives the generative-extension
filter of the frame's inventory exactly when it is live and no live response liftedly
extends it. -/
theorem survives_iff_lifted (situation : Situation S A) (s : S) (realized : S → C → Prop)
    (living : C → Prop) (a : A) :
    Survives (Frame.inventory ⟨situationProcess situation s, realized⟩ living) situation a ↔
      LiftSurvives ⟨situationProcess situation s, realized⟩ living s a :=
  ⟨fun ⟨feasibleA, unextended⟩ =>
    ⟨(situation_enabled_iff situation s a).mpr feasibleA, fun b liveB lifted =>
      let feasibleB := (situation_enabled_iff situation s b).mp liveB
      unextended b feasibleB
        ((situation_lift_iff situation s realized
          (Extension ⟨situationProcess situation s, realized⟩ living) feasibleA feasibleB).mp
          lifted)⟩,
   fun ⟨liveA, unextended⟩ =>
    let feasibleA := (situation_enabled_iff situation s a).mp liveA
    ⟨feasibleA, fun b feasibleB extension =>
      unextended b ((situation_enabled_iff situation s b).mpr feasibleB)
        ((situation_lift_iff situation s realized
          (Extension ⟨situationProcess situation s, realized⟩ living) feasibleA feasibleB).mpr
          extension)⟩⟩

/-- **Restricting the responses keeps a survivor.** On the one-step frame of a functional
situation, a response no live response liftedly extends still survives when the enabled
responses are restricted to a subfamily containing it. -/
theorem restricted_survives (situation : Situation S A) (s : S) (realized : S → C → Prop)
    (living : C → Prop) (restricted : A → Prop) {a : A}
    (survivor : LiftSurvives ⟨situationProcess situation s, realized⟩ living s a)
    (retained : restricted a) :
    LiftSurvives
      ⟨situationProcess
        { situation with feasible := fun option => situation.feasible option ∧ restricted option }
        s, realized⟩ living s a :=
  (survives_iff_lifted
      { situation with feasible := fun option => situation.feasible option ∧ restricted option }
      s realized living a).mp
    (feasible_restriction_preserves_survivor restricted
      ((survives_iff_lifted situation s realized living a).mpr survivor) retained)

end ExtensionFrames

end Becoming
