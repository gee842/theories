import GenerativeComparison
import PositiveGroundUncertainty

/-!
# Positive ground addressed to every situated position

`PositiveGroundUncertainty` indexes a contributory reason only by history. This
module adds the position to which a reason is addressed. A `Position` is a
differentiated response position formed within the same unfolding: its access
to a response is a formed relation of capacity, standing and availability, not
a primitive independent agent standing outside the history. Histories already
include which response occurred; `admitted a` is the presently supported
visible scope of continuations following response `a`.

Supplied premises remain explicit:
* G0, unchanged from `GenerativeComparison`;
* E, formation correspondence: response `a` realizes some new generative
  content in every admitted continuation;
* D, positioned direct articulation: if a response available to a position
  secures positive new content in every admitted continuation, that position
  has a contributory reason for it. D mentions only access and the response's
  continuations; it does not mention endorsement, culture, identity or
  substrate.

Conclusions: every position with access has the reason (universal address);
the least reason satisfying D is fixed by access alone, so positions alike in
access are alike in this reason whatever else differs; a position without
access receives no reason from this route, which is not a proof that it has no
reason at all. The boundary theorem shows that endorsement independence is the
content of D, not a consequence of G0 and E: an endorsement-conditional
articulation is compatible with the same G0 and formation facts and withholds
the reason from a non-endorsing position with access.

A contributory reason is not permission, duty, an overall ranking or a
prediction that any position will recognize or act on it.

Every declaration in this module has an empty axiom report. The concrete
formation fact is computed directly from the `PositiveGroundUncertainty`
definitions instead of reusing its `simp`-based lemmas, whose `propext` and
`Quot.sound` reports are unchanged and remain outside this module.
-/

namespace PositionedPositiveReason

open GenerativeComparison
open PositiveGroundUncertainty

/-- Every admitted continuation of the response contains some positive content
that was not already present before it. -/
def SecuresPositiveGround {H Q A : Type}
    (admitted : A → H → Prop) (before : H → Q → Prop)
    (positive : H → Q → Prop) (a : A) : Prop :=
  ∀ h, admitted a h → ∃ q, positive h q ∧ ¬ before h q

/-- D: positioned direct articulation. Endorsement does not occur in it. -/
def PositionedArticulation {Pos H Q A : Type}
    (access : Pos → A → Prop) (admitted : A → H → Prop) (before : H → Q → Prop)
    (positive : H → Q → Prop) (Reason : Pos → A → Prop) : Prop :=
  ∀ p a, access p a → SecuresPositiveGround admitted before positive a → Reason p a

/-- The reason this route itself supplies: access plus secured positive ground. -/
def RouteReason {Pos H Q A : Type}
    (access : Pos → A → Prop) (admitted : A → H → Prop) (before : H → Q → Prop)
    (positive : H → Q → Prop) (p : Pos) (a : A) : Prop :=
  access p a ∧ SecuresPositiveGround admitted before positive a

/-- Universal address: under G0, formation correspondence E and positioned
articulation D, every position with access to the response has a contributory
reason for it. No endorsement, culture, identity or substrate hypothesis occurs.
This composes `contingent_generation_has_positive_ground`. -/
theorem every_situated_position_has_reason {Pos H Q A : Type}
    (access : Pos → A → Prop) (admitted : A → H → Prop)
    (before : H → Q → Prop) (inventory : Inventory H Q) (positive : H → Q → Prop)
    (Reason : Pos → A → Prop) (g0 : G0 inventory positive)
    (articulate : PositionedArticulation access admitted before positive Reason)
    (a : A)
    (formed : ∀ h, admitted a h → ∃ q, inventory.generative q ∧
      inventory.realized h q ∧ ¬ before h q) :
    ∀ p, access p a → Reason p a := by
  intro p available
  exact articulate p a available
    (contingent_generation_has_positive_ground (admitted a) before inventory positive g0 formed)

/-- The route reason satisfies D and is contained in every reason satisfying D. -/
theorem route_reason_is_least {Pos H Q A : Type}
    (access : Pos → A → Prop) (admitted : A → H → Prop) (before : H → Q → Prop)
    (positive : H → Q → Prop) :
    PositionedArticulation access admitted before positive
        (RouteReason access admitted before positive) ∧
      ∀ Reason, PositionedArticulation access admitted before positive Reason →
        ∀ p a, RouteReason access admitted before positive p a → Reason p a :=
  ⟨fun _ _ available secured => ⟨available, secured⟩,
   fun _ articulate p a route => articulate p a route.1 route.2⟩

/-- Positions alike in access are alike in the route reason, whatever else
about them differs. -/
theorem route_reason_depends_only_on_access {Pos H Q A : Type}
    (access : Pos → A → Prop) (admitted : A → H → Prop)
    (before : H → Q → Prop) (positive : H → Q → Prop) (p p' : Pos)
    (same : ∀ a, access p a ↔ access p' a) (a : A) :
    RouteReason access admitted before positive p a ↔
      RouteReason access admitted before positive p' a := by
  constructor
  · rintro ⟨available, secured⟩
    exact ⟨(same a).1 available, secured⟩
  · rintro ⟨available, secured⟩
    exact ⟨(same a).2 available, secured⟩

/-! ## Concrete witness on the positive-ground construction -/

inductive Act where
  | respond | abstain
  deriving DecidableEq

def arrangementOf : Act → Arrangement
  | .respond => PositiveGroundUncertainty.respond initial
  | .abstain => initial

/-- A continuation: which act occurred, a formation model, and a future branch. -/
abbrev Continuation := Act × FormationModel × Bool

/-- The presently supported visible scope: models still live after the acquired
evidence, either future branch. -/
def admittedAfter (a : Act) (h : Continuation) : Prop :=
  h.1 = a ∧ live h.2.1

def wholeInventory : Inventory Continuation LivingClaim where
  realized := fun h q => realizes (arrangementOf h.1) h.2.1 h.2.2 q
  generative := fun q => q = .freshLeft ∨ q = .freshRight

def priorIn (h : Continuation) (q : LivingClaim) : Prop := prior h.2.2 q

/-- A model of G0: positive relevance exactly where G0 requires it. -/
def g0Relevant (h : Continuation) (q : LivingClaim) : Prop :=
  wholeInventory.generative q ∧ wholeInventory.realized h q

theorem g0_holds : G0 wholeInventory g0Relevant :=
  fun _ _ generated actual => ⟨generated, actual⟩

inductive Substrate where
  | human | artificial
  deriving DecidableEq

/-- Analytical features of a formed position. `canRespond` stands for its formed
access to the response; `substrate` and `endorses` are included only to show
that they do not enter the reason. -/
structure Position where
  substrate : Substrate
  endorses : Bool
  canRespond : Bool
  deriving DecidableEq

def access (p : Position) : Act → Prop
  | .respond => p.canRespond = true
  | .abstain => True

/-- The acquired reading excludes the barren model. Proved by direct
computation, without propositional extensionality or quotient soundness. -/
theorem barren_not_live : ¬ live .barren :=
  fun alive => Bool.false_ne_true (alive (true, true) (List.Mem.head _))

theorem live_productive : ∀ m, live m → 0 < magnitude m
  | .barren, alive => absurd alive barren_not_live
  | .one, _ => Nat.succ_pos 0
  | .two, _ => Nat.succ_pos 1

/-- Formation correspondence E for the response, constructed directly from the
`PositiveGroundUncertainty` definitions: each admitted branch realizes its own
fresh relation. -/
theorem respond_formation :
    ∀ h, admittedAfter .respond h → ∃ q, wholeInventory.generative q ∧
      wholeInventory.realized h q ∧ ¬ priorIn h q := by
  intro h admitted
  obtain ⟨act, m, branch⟩ := h
  obtain ⟨same, alive⟩ := admitted
  have responded : act = .respond := same
  subst responded
  have productive := live_productive m alive
  cases branch with
  | false => exact ⟨.freshLeft, Or.inl rfl, And.intro rfl (And.intro productive rfl), id⟩
  | true => exact ⟨.freshRight, Or.inr rfl, And.intro rfl (And.intro productive rfl), id⟩

def nonEndorsingArtificial : Position := ⟨.artificial, false, true⟩
def endorsingHumanWithoutAccess : Position := ⟨.human, true, false⟩

/-- A non-endorsing artificial position with access has the reason, through the
same theorem that gives it to every other position with access. -/
theorem nonendorsing_position_with_access_has_reason :
    RouteReason access admittedAfter priorIn g0Relevant nonEndorsingArtificial .respond :=
  every_situated_position_has_reason access admittedAfter priorIn wholeInventory g0Relevant
    (RouteReason access admittedAfter priorIn g0Relevant) g0_holds
    (route_reason_is_least access admittedAfter priorIn g0Relevant).1
    .respond respond_formation nonEndorsingArtificial rfl

/-- Endorsement without access does not supply this route's reason. -/
theorem endorsement_without_access_gets_no_route_reason :
    ¬ RouteReason access admittedAfter priorIn g0Relevant endorsingHumanWithoutAccess .respond := by
  rintro ⟨available, _⟩
  cases available

/-- Endorsement independence is the content of D, not of G0 and E. An
endorsement-conditional articulation holds together with the same G0 and
formation facts, yet withholds the reason from a non-endorsing position with
access. -/
theorem endorsement_independence_is_supplied_by_articulation :
    G0 wholeInventory g0Relevant ∧
    (∀ h, admittedAfter .respond h → ∃ q, wholeInventory.generative q ∧
      wholeInventory.realized h q ∧ ¬ priorIn h q) ∧
    ∃ Reason : Position → Act → Prop,
      (∀ p a, access p a → p.endorses = true →
        SecuresPositiveGround admittedAfter priorIn g0Relevant a → Reason p a) ∧
      access nonEndorsingArtificial .respond ∧
      ¬ Reason nonEndorsingArtificial .respond := by
  refine ⟨g0_holds, respond_formation,
    fun p a => RouteReason access admittedAfter priorIn g0Relevant p a ∧ p.endorses = true,
    fun _ _ available endorsed secured => ⟨⟨available, secured⟩, endorsed⟩, rfl, ?_⟩
  rintro ⟨_, endorsed⟩
  cases endorsed

end PositionedPositiveReason
