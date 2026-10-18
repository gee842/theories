import Becoming.Horizon
import Becoming.Roles

/-!
# Runs read through roles and recurrence

The run readings of `Becoming.Roles` (a web's activity along a run, `Web.active_along`; what
bears on it, `Web.bearing`; ending together, `Web.coextinct`; the predation witness,
`Predation.fox_ends`) and of `Becoming.Dissipation` (a Boolean sequence recurs as a run exactly
where its one-member family recurs, `Sequences.recurs_iff`). The laws they read are stated over
the web and the flow in those modules, which do not import the frame.

Every declaration moved here unchanged, with its name (study section 180, board item W). Every
declaration has an empty axiom report.
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
