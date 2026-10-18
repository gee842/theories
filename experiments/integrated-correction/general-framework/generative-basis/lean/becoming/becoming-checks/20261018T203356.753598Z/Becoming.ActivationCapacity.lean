import Becoming.Bundles
import Becoming.Recurrence

/-!
# Activation capacity: what one preparation step changes in what can be realized together

`Becoming.Bundles` states the activation law (`Activation.law`): from the initial configuration a
coupling is retained or released, then one side, the other or (only where the coupling is
retained) both activate together; `Activation.realizedAt` reads the claims realized at a
configuration. `Becoming.Recurrence`'s `WithinMoves` says a bundle of claims is realized within
`n` moves. Board item F3R (18 October 2026) states here, on the core and constructively, what
`RelationalBecoming` (8 October) proved of that law: effective capacity (what is realizable
within a given number of moves) and eventual reachability are distinct within one process.

* **Joint content.** A configuration realizes both claims exactly when both are active
  (`joint_iff`).
* **Preparation.** The joint content is realizable within one move from the coupled
  configuration and not from the initial one, while it is realizable within two moves from the
  initial one, the preparation counted (`coupled_within_one`, `initial_not_within_one`,
  `preparation_changes_capacity`): a preparation step changes the current capacity and adds no
  eventually reachable bundle (`Becoming.together_after_reach`).
* **Release.** After the release no number of moves realizes the joint content
  (`released_not_joint`), so the actual release loses what was eventually reachable from the
  initial configuration (`release_loses_joint`).
* **Capacity is not realization.** The prepared configuration can still end with one side active
  and no move left (`prepared_can_end_one_sided`).

The law, the claim reading and the count of moves are supplied; a count of moves is not elapsed
time unless calibrated. No origin of the coupling and no ranking is derived. Every declaration has
an empty axiom report.
-/

namespace Becoming

open Generative Activation

namespace ActivationCapacity

/-- That both claims are realized. -/
def both (_ : Claim) : Prop := True

/-- **A configuration realizes both claims exactly when both sides are active.** -/
theorem joint_iff (s : Configuration) : (∀ c, both c → realizedAt s c) ↔ s = .bothActive :=
  ⟨fun content => joint_content_both fun c => content c trivial,
   fun h c _ => match c with
    | .leftRealized => .inr h
    | .rightRealized => .inr h⟩

/-- **From the coupled configuration the joint content is realizable within one move.** -/
theorem coupled_within_one : WithinMoves law realizedAt .coupled 1 both :=
  ⟨[.activateTogether], .bothActive, .cons Step.activateTogether (.nil _), Nat.le_refl _,
   (joint_iff .bothActive).mpr rfl⟩

/-- **From the initial configuration it is not.** -/
theorem initial_not_within_one : ¬ WithinMoves law realizedAt .initial 1 both
  | ⟨word, final, path, short, content⟩ =>
    have isBoth := (joint_iff final).mp content
    match word, path, short with
    | [], .nil _, _ => Configuration.noConfusion isBoth
    | [_], .cons step (.nil _), _ => match step, isBoth with
      | Step.retainCoupling, e => Configuration.noConfusion e
      | Step.releaseCoupling, e => Configuration.noConfusion e
    | _ :: _ :: _, _, short => absurd short (Nat.not_succ_le_zero _ ∘ Nat.le_of_succ_le_succ)

/-- **One preparation step changes the current capacity**; with the preparation counted, the
joint content was already realizable within two moves. -/
theorem preparation_changes_capacity :
    Trace law .initial [.retain] .coupled ∧ ¬ WithinMoves law realizedAt .initial 1 both ∧
      WithinMoves law realizedAt .coupled 1 both ∧ WithinMoves law realizedAt .initial 2 both :=
  have path : Trace law .initial [.retain] .coupled := .cons Step.retainCoupling (.nil _)
  ⟨path, initial_not_within_one, coupled_within_one, WithinMoves.after_course path coupled_within_one⟩

/-- **After the release no number of moves realizes the joint content.** -/
theorem released_not_joint : ¬ ∃ n, WithinMoves law realizedAt .released n both
  | ⟨_, _, _, path, _, content⟩ =>
    PastRelease.no_joint (.inl rfl) path fun c => content c trivial

/-- **The actual release loses what was eventually reachable.** -/
theorem release_loses_joint :
    Trace law .initial [.release] .released ∧ (∃ n, WithinMoves law realizedAt .initial n both) ∧
      ¬ ∃ n, WithinMoves law realizedAt .released n both :=
  ⟨.cons Step.releaseCoupling (.nil _), ⟨2, preparation_changes_capacity.2.2.2⟩, released_not_joint⟩

/-- **Capacity is not realization**: the prepared configuration can end with one side active, the
other claim unrealized and no move left. -/
theorem prepared_can_end_one_sided :
    Trace law .initial [.retain, .activateLeft] .leftActive ∧
      WithinMoves law realizedAt .coupled 1 both ∧ ¬ realizedAt .leftActive .rightRealized ∧
      ∀ a, ¬ Enabled law .leftActive a :=
  ⟨.cons Step.retainCoupling (.cons Step.activateLeftCoupled (.nil _)), coupled_within_one,
   fun r => match r with
    | .inl e => Configuration.noConfusion e
    | .inr e => Configuration.noConfusion e,
   fun _ ⟨_, step⟩ => nomatch step⟩

end ActivationCapacity

end Becoming
