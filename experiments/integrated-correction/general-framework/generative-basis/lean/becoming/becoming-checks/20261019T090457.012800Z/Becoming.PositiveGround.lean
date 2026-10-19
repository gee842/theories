import Becoming.Bundles
import Becoming.Narrowing
import Becoming.Relevance

/-!
# Certain positive ground with open future form, addressed to every situated position

A response secures positive ground at a visible scope where every admitted continuation holds
positive content absent before it (`SecuresPositiveGround`, `Becoming.Metaethics`). This is a
positive aspect at a stated scope, not an all-things-considered comparison: C and every order
are absent. Living significance (`G0`) supplies relevance for realized living content (the
parameter is named `positive`, but the name carries no valence; read from significance it is
significance from every standpoint);
articulation into a contributory reason is a supplied premise, not permission or duty.

* **Quantifier order matters.** One fixed response can secure some new positive content in each
  continuation without securing one fixed content in all (`contingent_generation`,
  `same_response_without_fixed_form`). Which form becomes actual and how much forms are distinct
  sources of openness.
* **A finite signed integral certifies the ground** where each positively contributing occurrence
  means realized living content absent before (`positive_integral_has_positive_occurrence`,
  `certified_integral_reason`); a positive part coexists with an adverse full signed change
  (`positive_integral_and_adverse_full_change`). Units, addition and the sign's meaning are local
  inputs, not a scalarization of what is good.
* **Universal address.** With D (`PositionedArticulation`), every position with access to the
  response has the reason (`every_situated_position_has_reason`); the least reason satisfying D
  is fixed by access alone (`route_reason_is_least`, `route_reason_depends_only_on_access`). A
  position is a differentiated response position formed within the same unfolding, its access a
  formed relation of capacity, standing and availability. Endorsement independence is the content
  of D, not of living significance and formation: an endorsement-conditional articulation holds
  with the same facts and withholds the reason
  (`endorsement_independence_is_supplied_by_articulation`).
* **Under the continuation condition** the same holds with positive relevance read from
  significance (`contingent_generation_of_unrestricted`,
  `every_situated_position_has_reason_of_unrestricted`), and over a policy's visible scope
  (`certified_reason_on_scope`).

Ported from `PositiveGroundUncertainty` and `PositionedPositiveReason`, with the bridge's
`contingent_generation_of_unrestricted` and `every_situated_position_has_reason_of_unrestricted`
and the join `ReachableFramesInherited` (F3J, 18 October 2026). The periphery's `Inventory` is a
frame with `living` its generative claims (`Frame.ofInventory`). Its `simp`, `omega` and classical
proofs are constructive here; most of the prelude's `Int` order lemmas depend on `propext`, so
the signed sums are handled by cases on `Int`'s constructors (`pos_or_pos`). Every declaration has
an empty axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency Lexical

namespace PositiveGround

/-! ## Signed finite integrals -/

/-- The finite signed integral of contributions over listed occurrences. -/
def finiteIntegral {R : Type} : List R → (R → Int) → Int
  | [], _ => 0
  | r :: rs, contribution => contribution r + finiteIntegral rs contribution

theorem one_sub_succ (n : Nat) : 1 - (n + 1) = 0 := (Nat.succ_sub_succ 0 n).trans (Nat.zero_sub n)

theorem pos_succ (n : Nat) : (0 : Int) < Int.ofNat (n + 1) := by
  show Int.NonNeg (Int.subNatNat (n + 1) 1)
  rw [Int.subNatNat_of_sub_eq_zero (one_sub_succ n)]
  exact ⟨_⟩

theorem not_pos_negSucc (n : Nat) : ¬ (0 : Int) < Int.negSucc n :=
  fun pos => nomatch (pos : Int.NonNeg (Int.negSucc n + Int.negSucc 0))

/-- **A positive sum has a positive summand.** -/
theorem pos_or_pos : ∀ a b : Int, 0 < a + b → 0 < a ∨ 0 < b
  | .ofNat (n + 1), _, _ => .inl (pos_succ n)
  | .ofNat 0, .ofNat (n + 1), _ => .inr (pos_succ n)
  | .negSucc _, .ofNat (n + 1), _ => .inr (pos_succ n)
  | .ofNat 0, .ofNat 0, pos => nomatch (by decide : ¬ (0 : Int) < 0) pos
  | .ofNat 0, .negSucc n, pos => absurd (pos : (0 : Int) < Int.negSucc n) (not_pos_negSucc n)
  | .negSucc m, .ofNat 0, pos => absurd (pos : (0 : Int) < Int.negSucc m) (not_pos_negSucc m)
  | .negSucc m, .negSucc n, pos =>
    absurd (pos : (0 : Int) < Int.negSucc (m + n + 1)) (not_pos_negSucc _)

/-- **A positive finite signed integral has a positively contributing occurrence.** Its meaning
is not inferred from the sign alone. -/
theorem positive_integral_has_positive_occurrence {R : Type} :
    ∀ (domain : List R) (contribution : R → Int), 0 < finiteIntegral domain contribution →
      ∃ r, r ∈ domain ∧ 0 < contribution r
  | [], _, positive => nomatch (by decide : ¬ (0 : Int) < 0) positive
  | r :: rs, contribution, positive =>
    match pos_or_pos _ _ positive with
    | .inl here => ⟨r, .head _, here⟩
    | .inr rest => match positive_integral_has_positive_occurrence rs contribution rest with
      | ⟨s, m, good⟩ => ⟨s, .tail _ m, good⟩

/-! ## Positive ground on a frame -/

section Ground

variable {H A Q : Type}

/-- **Quantifier order matters**: where each admitted continuation realizes living content absent
before, living significance gives each some relevant content absent before, though no
one content need be realized in all. -/
theorem contingent_generation (F : Frame H A Q) (living : Q → Prop) (admitted : H → Prop)
    (before : H → Q → Prop) (positive : H → Q → Prop) (g0 : G0 F living positive)
    (formed : ∀ h, admitted h → ∃ q, living q ∧ F.realized h q ∧ ¬ before h q) :
    ∀ h, admitted h → ∃ q, positive h q ∧ ¬ before h q :=
  fun h allowed => match formed h allowed with
  | ⟨q, alive, actual, fresh⟩ => ⟨q, g0 h q alive actual, fresh⟩

/-- **A certified integral supplies a contributory reason**, with no comparison, order,
permission or duty: where every admitted continuation has a positive integral and each positive
occurrence means realized living content absent before, each holds positive content absent
before and has the reason articulated from positive relevance. -/
theorem certified_integral_reason {R : Type} (F : Frame H A Q) (living : Q → Prop)
    (admitted : H → Prop) (before : H → Q → Prop) (positive : H → Q → Prop) (reason : H → Prop)
    (g0 : G0 F living positive) (articulate : ∀ h q, positive h q → reason h) (domain : List R)
    (contribution : H → R → Int) (meaning : R → Q)
    (correspondence : ∀ h, admitted h → ∀ r, r ∈ domain → 0 < contribution h r →
      living (meaning r) ∧ F.realized h (meaning r) ∧ ¬ before h (meaning r))
    (certificate : ∀ h, admitted h → 0 < finiteIntegral domain (contribution h)) :
    ∀ h, admitted h → (∃ q, positive h q ∧ ¬ before h q) ∧ reason h :=
  fun h allowed =>
    match contingent_generation F living admitted before positive g0 (fun h allowed =>
        match positive_integral_has_positive_occurrence domain (contribution h)
            (certificate h allowed) with
        | ⟨r, m, good⟩ => ⟨meaning r, correspondence h allowed r m good⟩) h allowed with
    | ⟨q, relevant, fresh⟩ => ⟨⟨q, relevant, fresh⟩, articulate h q relevant⟩

/-- **Over a policy's visible scope**: the certified integral's reason holds at every
configuration the policy's executions reach. -/
theorem certified_reason_on_scope {C R O : Type} {k : Nat} (F : Frame H A C) (living : C → Prop)
    {sense : H → A → H → Fin k} {response : R → List A} {B : H → Prop} {policy : Policy A R k}
    (before : H → C → Prop) (positive : H → C → Prop) (reason : H → Prop)
    (g0 : G0 F living positive) (articulate : ∀ t c, positive t c → reason t) (domain : List O)
    (contribution : H → O → Int) (meaning : O → C)
    (correspondence : ∀ t, Scope F.P sense response B policy t → ∀ o, o ∈ domain →
      0 < contribution t o → living (meaning o) ∧ F.realized t (meaning o) ∧ ¬ before t (meaning o))
    (certificate : ∀ t, Scope F.P sense response B policy t →
      0 < finiteIntegral domain (contribution t)) :
    ∀ t, Scope F.P sense response B policy t → (∃ c, positive t c ∧ ¬ before t c) ∧ reason t :=
  certified_integral_reason F living (Scope F.P sense response B policy) before positive reason g0
    articulate domain contribution meaning correspondence certificate

/-- Under the continuation condition, formation gives content relevant as read from
significance, absent before, in every admitted continuation. -/
theorem contingent_generation_of_unrestricted {F' Pos : Type} (F : Frame H A Q)
    (living : Q → Prop) (admitted : H → Prop) (before : H → Q → Prop)
    {sig : Pos → Nat → F' → Prop} (unrestricted : Unrestricted sig) (formation : Q → F')
    (step : Q → Nat) (formed : ∀ h, admitted h → ∃ q, living q ∧ F.realized h q ∧ ¬ before h q) :
    ∀ h, admitted h → ∃ q, F.relevance living sig formation step h q ∧ ¬ before h q :=
  contingent_generation F living admitted before _
    (g0_of_unrestricted F living unrestricted formation step) formed

/-! ## Universal address -/

/-- The reason this route supplies: access plus secured positive ground. -/
def RouteReason {Pos R : Type} (access : Pos → R → Prop) (admitted : R → H → Prop)
    (before : H → Q → Prop) (positive : H → Q → Prop) (p : Pos) (r : R) : Prop :=
  access p r ∧ SecuresPositiveGround admitted before positive r

/-- **Universal address**: under living significance, formation and D, every position with
access to the response has a contributory reason for it. No endorsement, culture, identity or
substrate hypothesis occurs. -/
theorem every_situated_position_has_reason {Pos R : Type} (F : Frame H A Q) (living : Q → Prop)
    (access : Pos → R → Prop) (admitted : R → H → Prop) (before : H → Q → Prop)
    (positive : H → Q → Prop) (Reason : Pos → R → Prop) (g0 : G0 F living positive)
    (articulate : PositionedArticulation access admitted before positive Reason) (r : R)
    (formed : ∀ h, admitted r h → ∃ q, living q ∧ F.realized h q ∧ ¬ before h q) :
    ∀ p, access p r → Reason p r :=
  fun p available => articulate p r available
    (contingent_generation F living (admitted r) before positive g0 formed)

/-- Under the continuation condition, with D read on positive relevance from significance,
formation gives every position with access the reason. -/
theorem every_situated_position_has_reason_of_unrestricted {Pos R F' : Type} (F : Frame H A Q)
    (living : Q → Prop) (access : Pos → R → Prop) (admitted : R → H → Prop)
    (before : H → Q → Prop) {sig : Pos → Nat → F' → Prop} (unrestricted : Unrestricted sig)
    (formation : Q → F') (step : Q → Nat) (Reason : Pos → R → Prop)
    (articulate : PositionedArticulation access admitted before
      (F.relevance living sig formation step) Reason) (r : R)
    (formed : ∀ h, admitted r h → ∃ q, living q ∧ F.realized h q ∧ ¬ before h q) :
    ∀ p, access p r → Reason p r :=
  every_situated_position_has_reason F living access admitted before _ Reason
    (g0_of_unrestricted F living unrestricted formation step) articulate r formed

/-- **The route reason satisfies D and is contained in every reason satisfying D.** -/
theorem route_reason_is_least {Pos R : Type} (access : Pos → R → Prop) (admitted : R → H → Prop)
    (before : H → Q → Prop) (positive : H → Q → Prop) :
    PositionedArticulation access admitted before positive
        (RouteReason access admitted before positive) ∧
      ∀ Reason, PositionedArticulation access admitted before positive Reason →
        ∀ p r, RouteReason access admitted before positive p r → Reason p r :=
  ⟨fun _ _ available secured => ⟨available, secured⟩,
   fun _ articulate p r route => articulate p r route.1 route.2⟩

/-- **Positions alike in access are alike in the route reason**, whatever else differs. -/
theorem route_reason_depends_only_on_access {Pos R : Type} (access : Pos → R → Prop)
    (admitted : R → H → Prop) (before : H → Q → Prop) (positive : H → Q → Prop) (p p' : Pos)
    (same : ∀ r, access p r ↔ access p' r) (r : R) :
    RouteReason access admitted before positive p r ↔
      RouteReason access admitted before positive p' r :=
  ⟨fun ⟨available, secured⟩ => ⟨(same r).mp available, secured⟩,
   fun ⟨available, secured⟩ => ⟨(same r).mpr available, secured⟩⟩

end Ground

/-! ## One response, two future branches, three formation magnitudes -/

/-- Three hypotheses on how much a response forms. -/
inductive FormationModel where
  | barren | one | two

def magnitude : FormationModel → Nat
  | .barren => 0
  | .one => 1
  | .two => 2

inductive LivingClaim where
  | priorLeft | priorRight | freshLeft | freshRight

structure Arrangement where
  responded : Bool
  queryOpen : Bool

def initial : Arrangement := ⟨false, true⟩

/-- One response keeps the query channel open and changes the formation phase. -/
def respond (s : Arrangement) : Arrangement := ⟨true, s.queryOpen⟩

def prior (branch : Bool) : LivingClaim → Prop
  | .priorLeft => branch = false
  | .priorRight => branch = true
  | .freshLeft => False
  | .freshRight => False

/-- New formation needs the retained prior branch as well as the response: the fresh occurrence
is a relation formed through that prior activity. -/
def realizes (s : Arrangement) (m : FormationModel) (branch : Bool) : LivingClaim → Prop
  | .priorLeft => branch = false
  | .priorRight => branch = true
  | .freshLeft => s.responded = true ∧ 0 < magnitude m ∧ prior branch .priorLeft
  | .freshRight => s.responded = true ∧ 0 < magnitude m ∧ prior branch .priorRight

/-- The future branches of an arrangement as a frame with no moves. -/
def futureFrame (s : Arrangement) (m : FormationModel) : Frame Bool Unit LivingClaim :=
  ⟨⟨fun _ _ _ => False⟩, realizes s m⟩

/-- The fresh claims, the living ones. -/
def fresh (q : LivingClaim) : Prop := q = .freshLeft ∨ q = .freshRight

/-- **The same response secures generation without a fixed form**: each branch realizes a fresh
claim absent before, and no fresh claim is realized in both. -/
theorem same_response_without_fixed_form (m : FormationModel) (productive : 0 < magnitude m) :
    (∀ branch, ∃ q, fresh q ∧ (futureFrame (respond initial) m).realized branch q ∧
      ¬ prior branch q) ∧
    ¬ ∃ q, fresh q ∧ ∀ branch, (futureFrame (respond initial) m).realized branch q :=
  ⟨fun
    | false => ⟨.freshLeft, .inl rfl, ⟨rfl, productive, rfl⟩, id⟩
    | true => ⟨.freshRight, .inr rfl, ⟨rfl, productive, rfl⟩, id⟩,
   fun ⟨q, isFresh, all⟩ => match q, isFresh, all with
    | _, .inl rfl, all => Bool.noConfusion (all true).2.2
    | _, .inr rfl, all => Bool.noConfusion (all false).2.2⟩

inductive Occurrence where
  | freshLeft | freshRight | burden

def positiveDomain : List Occurrence := [.freshLeft, .freshRight]
def fullDomain : List Occurrence := [.freshLeft, .freshRight, .burden]

def contribution (s : Arrangement) (m : FormationModel) (branch : Bool) : Occurrence → Int
  | .freshLeft => if (s.responded && !branch) = true then magnitude m else 0
  | .freshRight => if (s.responded && branch) = true then magnitude m else 0
  | .burden => if s.responded = true then -((magnitude m : Int) + 1) else 0

def occurrenceMeaning : Occurrence → LivingClaim
  | .freshLeft => .freshLeft
  | .freshRight => .freshRight
  | .burden => .priorLeft

/-- **Every strictly positive represented fresh occurrence means an actual new relation**; the
burden lies outside the positive domain. -/
theorem positive_occurrence_correspondence (m : FormationModel) (branch : Bool) (r : Occurrence)
    (member : r ∈ positiveDomain) (good : 0 < contribution (respond initial) m branch r) :
    fresh (occurrenceMeaning r) ∧ (futureFrame (respond initial) m).realized branch
      (occurrenceMeaning r) ∧ ¬ prior branch (occurrenceMeaning r) :=
  match r, (member : r ∈ [Occurrence.freshLeft, .freshRight]), good with
  | _, .head _, good => by
    cases m <;> cases branch
    all_goals first
      | exact absurd good (by decide)
      | exact ⟨.inl rfl, ⟨rfl, by decide, rfl⟩, id⟩
  | _, .tail _ (.head _), good => by
    cases m <;> cases branch
    all_goals first
      | exact absurd good (by decide)
      | exact ⟨.inr rfl, ⟨rfl, by decide, rfl⟩, id⟩

theorem positiveDomain_nodup : positiveDomain.Nodup :=
  .cons (fun a n => match a, (n : a ∈ [Occurrence.freshRight]) with
      | _, .head _ => fun same => Occurrence.noConfusion same)
    (.cons (fun _ n => nomatch n) .nil)

theorem fullDomain_nodup : fullDomain.Nodup :=
  .cons (fun a n => match a, (n : a ∈ [Occurrence.freshRight, .burden]) with
      | _, .head _ => fun same => Occurrence.noConfusion same
      | _, .tail _ (.head _) => fun same => Occurrence.noConfusion same)
    (.cons (fun a n => match a, (n : a ∈ [Occurrence.burden]) with
        | _, .head _ => fun same => Occurrence.noConfusion same)
      (.cons (fun _ n => nomatch n) .nil))

/-- **A positive new aspect coexists with an adverse full signed change.** The coefficients are a
local illustration, not universal units. -/
theorem positive_integral_and_adverse_full_change (m : FormationModel)
    (productive : 0 < magnitude m) (branch : Bool) :
    positiveDomain.Nodup ∧ fullDomain.Nodup ∧
      0 < finiteIntegral positiveDomain (contribution (respond initial) m branch) ∧
      finiteIntegral fullDomain (contribution (respond initial) m branch) = -1 ∧
      finiteIntegral fullDomain (contribution initial m branch) = 0 :=
  ⟨positiveDomain_nodup, fullDomain_nodup, by
    cases m <;> cases branch
    all_goals first
      | exact absurd productive (by decide)
      | exact ⟨by decide, by decide, by decide⟩⟩

/-- **Every represented joint possibility and the query channel are kept by the response.** This
says nothing about unrepresented losses; the burden stays. -/
theorem response_preserves_joint_openness (m : FormationModel) :
    PreservesBundles (futureFrame initial m) (fun _ => True) (futureFrame (respond initial) m)
        (fun _ => True) ∧
      (respond initial).queryOpen = true :=
  ⟨preserves_of_transport (F := futureFrame initial m) (G := futureFrame (respond initial) m)
      id (fun _ _ => True.intro) (fun _ c _ held => match c, held with
        | .priorLeft, held => held
        | .priorRight, held => held
        | .freshLeft, held => Bool.noConfusion held.1
        | .freshRight, held => Bool.noConfusion held.1),
   rfl⟩

/-- The supplied reading law: the first query sees productive coupling, the second can refine
its magnitude. -/
def rule (m : FormationModel) : Narrowing.Rule Bool :=
  fun query => if query = true then decide (0 < magnitude m) else decide (magnitude m = 1)

def repertoire : List (Narrowing.Rule Bool) := [rule .barren, rule .one, rule .two]

def firstEvidence : List (Narrowing.Observation Bool) := Narrowing.acquire (rule .one) 1 [true]

/-- The magnitudes still live after the first observation. -/
def live (m : FormationModel) : Prop := Narrowing.Fits (rule m) firstEvidence

theorem live_one : live .one := fun o n =>
  match o, (n : o ∈ [(true, rule .one true)]) with
  | _, .head _ => rfl

theorem live_two : live .two := fun o n =>
  match o, (n : o ∈ [(true, rule .one true)]) with
  | _, .head _ => rfl

theorem barren_not_live : ¬ live .barren :=
  fun fits => absurd (fits (true, rule .one true) (.head _)) (by decide)

theorem live_productive : ∀ m, live m → 0 < magnitude m
  | .barren, alive => absurd alive barren_not_live
  | .one, _ => Nat.succ_pos 0
  | .two, _ => Nat.succ_pos 1

/-- **Acquired evidence secures the good and leaves both opennesses**: the first observation
rules out the barren magnitude, the response's positive integral is positive in every live model
and branch, and which magnitude holds stays open until a second query. -/
theorem acquired_evidence_secures_good_and_leaves_both_opennesses :
    live .one ∧ live .two ∧ ¬ live .barren ∧
    Narrowing.learn repertoire firstEvidence = [rule .one, rule .two] ∧
    Narrowing.answer (Narrowing.learn repertoire firstEvidence) false = none ∧
    (∀ m, live m → ∀ branch,
      0 < finiteIntegral positiveDomain (contribution (respond initial) m branch)) ∧
    (∀ m, live m → ∀ branch, finiteIntegral positiveDomain (contribution initial m branch) = 0) ∧
    Narrowing.revise (Narrowing.learn repertoire firstEvidence) (false, true) = [rule .one] ∧
    Narrowing.revise (Narrowing.learn repertoire firstEvidence) (false, false) = [rule .two] ∧
    Narrowing.answer (Narrowing.revise (Narrowing.learn repertoire firstEvidence) (true, false))
      true = none ∧
    Narrowing.learn repertoire (Narrowing.acquire (rule .barren) 1 [true]) = [rule .barren] :=
  ⟨live_one, live_two, barren_not_live, rfl, rfl,
   fun m alive branch => match m, branch with
    | .barren, _ => absurd alive barren_not_live
    | .one, false => by decide
    | .one, true => by decide
    | .two, false => by decide
    | .two, true => by decide,
   fun m _ branch => match m, branch with
    | .barren, false => rfl
    | .barren, true => rfl
    | .one, false => rfl
    | .one, true => rfl
    | .two, false => rfl
    | .two, true => rfl,
   rfl, rfl, rfl, rfl⟩

/-- **Widening the admitted scope to a nonproductive possibility retracts the certificate.** The
theorem does not license the widening; new evidence or changed relations must warrant it. -/
theorem wider_scope_can_require_certificate_retraction :
    (∀ m, live m → live m ∨ m = .barren) ∧
    ¬ (∀ m, live m ∨ m = .barren → ∀ branch,
      0 < finiteIntegral positiveDomain (contribution (respond initial) m branch)) :=
  ⟨fun _ alive => .inl alive, fun claims => absurd (claims .barren (.inr rfl) false) (by decide)⟩

/-! ## Positions addressed by the reason -/

inductive Act where
  | respond | abstain

def arrangementOf : Act → Arrangement
  | .respond => respond initial
  | .abstain => initial

/-- A continuation: which act occurred, a formation model, and a future branch. -/
abbrev Continuation := Act × FormationModel × Bool

/-- The presently supported visible scope: models still live after the acquired evidence, either
future branch. -/
def admittedAfter (a : Act) (h : Continuation) : Prop := h.1 = a ∧ live h.2.1

/-- The continuations as a frame with no moves. -/
def wholeFrame : Frame Continuation Unit LivingClaim :=
  ⟨⟨fun _ _ _ => False⟩, fun h q => realizes (arrangementOf h.1) h.2.1 h.2.2 q⟩

def priorIn (h : Continuation) (q : LivingClaim) : Prop := prior h.2.2 q

/-- A model of living significance: positive relevance exactly where it requires it. -/
def g0Relevant (h : Continuation) (q : LivingClaim) : Prop := fresh q ∧ wholeFrame.realized h q

theorem g0_holds : G0 wholeFrame fresh g0Relevant := fun _ _ alive actual => ⟨alive, actual⟩

inductive Substrate where
  | human | artificial

/-- Features of a formed position: `canRespond` is its formed access to the response;
`substrate` and `endorses` are included only to show that they do not enter the reason. -/
structure Position where
  substrate : Substrate
  endorses : Bool
  canRespond : Bool

def access (p : Position) : Act → Prop
  | .respond => p.canRespond = true
  | .abstain => True

/-- **Formation for the response**: each admitted continuation realizes its own fresh relation. -/
theorem respond_formation :
    ∀ h, admittedAfter .respond h → ∃ q, fresh q ∧ wholeFrame.realized h q ∧ ¬ priorIn h q
  | (.respond, m, false), ⟨_, alive⟩ => ⟨.freshLeft, .inl rfl, ⟨rfl, live_productive m alive, rfl⟩, id⟩
  | (.respond, m, true), ⟨_, alive⟩ => ⟨.freshRight, .inr rfl, ⟨rfl, live_productive m alive, rfl⟩, id⟩
  | (.abstain, _, _), ⟨same, _⟩ => Act.noConfusion same

def nonEndorsingArtificial : Position := ⟨.artificial, false, true⟩
def endorsingHumanWithoutAccess : Position := ⟨.human, true, false⟩

/-- **A non-endorsing artificial position with access has the reason**, through the same theorem
that gives it to every other position with access. -/
theorem nonendorsing_position_with_access_has_reason :
    RouteReason access admittedAfter priorIn g0Relevant nonEndorsingArtificial .respond :=
  every_situated_position_has_reason wholeFrame fresh access admittedAfter priorIn g0Relevant
    (RouteReason access admittedAfter priorIn g0Relevant) g0_holds
    (route_reason_is_least access admittedAfter priorIn g0Relevant).1 .respond respond_formation
    nonEndorsingArtificial rfl

/-- **Endorsement without access does not supply this route's reason.** -/
theorem endorsement_without_access_gets_no_route_reason :
    ¬ RouteReason access admittedAfter priorIn g0Relevant endorsingHumanWithoutAccess .respond :=
  fun ⟨available, _⟩ => Bool.noConfusion available

/-- **Endorsement independence is the content of D, not of living significance and formation.**
An endorsement-conditional articulation holds with the same facts, yet withholds the reason from
a non-endorsing position with access. -/
theorem endorsement_independence_is_supplied_by_articulation :
    G0 wholeFrame fresh g0Relevant ∧
    (∀ h, admittedAfter .respond h → ∃ q, fresh q ∧ wholeFrame.realized h q ∧ ¬ priorIn h q) ∧
    ∃ Reason : Position → Act → Prop,
      (∀ p a, access p a → p.endorses = true →
        SecuresPositiveGround admittedAfter priorIn g0Relevant a → Reason p a) ∧
      access nonEndorsingArtificial .respond ∧ ¬ Reason nonEndorsingArtificial .respond :=
  ⟨g0_holds, respond_formation,
   fun p a => RouteReason access admittedAfter priorIn g0Relevant p a ∧ p.endorses = true,
   fun _ _ available endorsed secured => ⟨⟨available, secured⟩, endorsed⟩, rfl,
   fun ⟨_, endorsed⟩ => Bool.noConfusion endorsed⟩

end PositiveGround

end Becoming
