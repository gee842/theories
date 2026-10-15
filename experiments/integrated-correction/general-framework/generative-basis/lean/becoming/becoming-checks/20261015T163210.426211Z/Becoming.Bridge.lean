import Becoming
import GenerativeComparison
import PositionedPositiveReason
import PracticalJudgment
import RenewalComparison
import JointContinuationClassification
import WholeGroundCoverage
import CutCoverageAudit
import EvaluatorGrounding
import PracticalReach
import StandardsBridge
import CorrectionInfrastructure
import ExplanatoryBranching
import OpenFutureRevision
import RelationalGrounding
import ProtectionPriorityRival
import ChanceAdequacy
import FallibleInspection
import BecomingReversibility
import DynamicConsequences
import DerivedHistoryLaw
import BecomingCompatibility
import RelationalBecoming
import ClassificationRobustJudgment
import JointInterpretation
import AlignmentDirection

/-!
# Existing interfaces as instances of the spine

Generic ethics modules are polymorphic over small interfaces. This module gives
each interface from the spine, or proves that a module's own combinator is the
spine's, so their theorems apply to one unfolding without copying them. The core
imports none of these modules; the dependency runs from them to the core.

* The core's G0, C, secured positive ground and positioned articulation D are, by
  definition, those of `GenerativeComparison` and `PositionedPositiveReason` on the
  frame's inventory; the relational reading of `living` is `RenewalComparison`'s, and
  so is the whole-run reading of courses in `Becoming.Ranking`, with the same
  undisturbed levels.
  J1/J2 on configurations, `BetterAt`, is `PracticalJudgment.Better`.
* Seed–edge closures (`WholeGroundCoverage.Reached`, `CutCoverageAudit.Reach`)
  and finite chains (`EvaluatorGrounding.Chain`) are reachability on the process
  whose steps are the edges. The core's closure under a relation (`WithinClosure`,
  `Becoming.Feedback`) is the seed–edge closure from one seed.
* Joint-continuation spaces are the configurations reachable in a frame; their
  faithful transports are the core's `trace_map` and `trace_lift`.
* `PracticalJudgment.Robust` is `CommonResponse`; `PracticalReach.Guarantees` is
  one-step `Completes`; `StandardsBridge.revise` is `After` on a pure
  observation; `CorrectionInfrastructure.LiveStep` is `Enabled`.
* `GenerativeComparison.Situation` realizes each option functionally. On a frame
  a response may have several outcomes, so comparing responses needs the lifting
  rule L. The functional articulation is exactly the deterministic case of the
  lifted one, and the lifted comparison, reason and selection results hold for
  every frame. Two countermodels show that the choice of lifting rule is
  substantive and that transitivity needs a live middle response.
* Under the axiom of `Becoming.Significance`, `GenerativeComparison.G0` holds for
  every inventory with positive relevance read from significance, which on a frame's
  inventory is the core's `Frame.relevance`. The periphery's theorems taking G0 as a
  hypothesis for an arbitrary positive relevance follow from the axiom with it: a new
  realization of a generative extension, contingent generation, and the universal
  address of positioned articulation with D read on it.
* `Deeper.Bisimulation` of `RelationalDynamics` and `ExplanatoryBranching.Bisimulation` are
  the core's `Bisimulation` (`Becoming.Unfolding`) on frames with no claims and with a model's
  conditions as claims (`deeper_bisimulation_iff`, `branching_bisimulation_iff`); in `static`
  and `toggle` every configuration of one is alike to every configuration of the other
  (`static_toggle_alike`); alike configurations pass every branching test (`Alike.same`).
  The core's branching tests (`Becoming.Likeness`) are the tests of `ExplanatoryBranching`, read
  one to one (`BranchingTest.toTest`, `BranchingTest.ofTest`), and hold at the same
  configurations (`BranchingTest.holds_toTest`), so passing the same tests is the same in both
  (`sameBranchingTests_iff_same`). On models with finitely many configurations whose steps and
  conditions are decided, configurations pass the same tests exactly where they are alike, with
  no classical reasoning (`same_iff_alike_of_finiteDecided`). For image-finite models the
  converse of `Alike.same` holds with excluded middle as a hypothesis, the moves and conditions
  unlisted (`same_iff_alike_of_imageFinite`), so `same_iff_bisimilar` is a theorem of the core
  with that hypothesis (`same_iff_bisimilar_of_em`). Tests separate a model exactly where the
  core's branching tests separate its frame (`separated_iff`), so `same_functional` is
  `SameBranchingTests.functional`.
* `EvaluatorGrounding`'s second step is N_rel on the valuation whose claims are a standpoint's
  profiles (`profileValuation`): tolerance is N_rel's neutrality there (`tolerant_iff_neutral`), a
  chain of small steps is reach along related profiles (`chain_iff_reach_profiles`) and S0 under
  supervenience is S0 there (`selfGood_profiles`), so `tolerant_chain_reaches` follows from the
  core's `Valuation.reaches` (`tolerant_chain_reaches_by_core`). Every profile is counted living,
  so the relation runs through merely possible profiles; the spine's readings of `related` relate
  events of one run.
* Three comparison results of the periphery are instances of core laws. An inventory is a frame
  with no moves (`Frame.ofInventory`). `RelationalGrounding`'s obstruction, that no strict
  comparison read off marginal possibilities satisfies C, is `Comparison.separates` at the
  retained coupling, which extends the released one with the same marginals
  (`strict_comparison_through_marginals_by_core`). In `ProtectionPriorityRival` the options with
  gains form an endless chain of extensions (`protection_successor_extension`), so
  `every_nat_score_trades` is `Comparison.outgrows` (`every_nat_score_trades_by_core`).
  `ChanceAdequacy`'s mass is the core's weighted mass (`chance_mass_eq`), so its
  characterization of inclusion by every weighting is `every_weighting_iff`
  (`all_weights_preserve_mass_iff_by_core`) and its chance floor is `mass_mono`
  (`fulfillment_floor_by_core`).
* Every protection-first comparison of `PracticalJudgment` is `BetterAt` on the frame of its
  options, realizing the protected claims as basic and the gains as living (`Judgment.frame`,
  `Judgment.better_iff_betterAt`), with the same frontier (`Judgment.frontier_iff`). So the
  alignment direction's comparison of plans and its frontier are the spine's
  (`alignment_better_iff_betterAt`, `alignment_frontier_iff`). `BetterAt` states J1/J2,
  commitments outside the core; G0 is neither used nor asserted here.
  On a listed menu the frontier is the undominated members (`Judgment.frontier_iff_undominated`),
  so `PracticalJudgment.finite_frontier` and `RelationalOrganization`'s requirement of formation
  hold with the comparison weakly decided and the task decided, with no classical reasoning
  (`Judgment.frontier_exists`, `Judgment.required_of_bettered`, from `exists_undominated` and
  `undominated_has` of `Becoming.Decidedness`).
* `FallibleInspection`'s Boolean explanation, on complete reports, is the core's explanation by
  fallible witnesses (`explains_complete_iff`, `compatible_complete_iff`), so its
  characterization of complete diagnosability by cross-separation is
  `Readout.no_common_report_envelopes_iff` (`complete_diagnosability_iff_by_core`). The list
  facts used are proved here with empty axiom reports, since the library's use `propext`.
* `BecomingReversibility`'s reachability is the core's, and a possibility is being at some
  reachable configuration (`keeps_possible_iff_keeps_reach`), so its return laws are the core's
  `same_reach_iff_returns` and `not_returns_iff_loses`
  (`same_endpoint_possibilities_iff_return_by_core`, `irreversible_iff_endpoint_loss_by_core`).
  `Deeper.same_steps_iff_endpoint_traces` is the core's `same_steps_iff_traces`
  (`same_steps_iff_endpoint_traces_by_core`).
* `DerivedHistoryLaw.derivedProcess` is the law of a language's admitted histories read
  through the summary (`admittedProcess`, `derived_same_steps`), so `exact_iff_fiber_future` is
  the core's `Readout.futures_through_iff` (`exact_iff_fiber_future_by_core`).
* `BecomingCompatibility`'s pooled, retained, evolving and erased laws are the core's laws in
  context (`Becoming.Context`), so `pooling_exact_iff_join_closed`, `retained_realizes_union`,
  `erasure_exact_iff_context_lifting`, `arrivals_append` and `arrivals_snoc` are
  `pooledLaw_exact_iff_joinClosed`, `retainedLaw_realizes_inOne`, `erasedLaw_exact_iff_lifts`,
  `arrives_append` and `arrives_snoc`, and its two witnesses are the core's `CrossingContexts`
  and `ChangingContext` (`pooling_exact_iff_join_closed_by_core` and the others); the core
  proves `changed_history_really_ends` without the `propext` the periphery's proof uses.
* `RelationalBecoming.Within` is the core's `WithinMoves`, so `within_after_prefix` and
  `eventual_after_prefix` are `WithinMoves.after_course` and `together_after_reach`
  (`within_after_prefix_by_core`, `eventual_after_prefix_by_core`). On the joint-activation law
  of `JointContinuationClassification`, one preparation step shortens the bound for joint
  activation from two moves to one, releasing the coupling loses it at every bound, and the
  prepared configuration can end one-sided (`actual_preparation_changes_effective_capacity_by_core`,
  `actual_release_loses_eventual_joint_by_core`,
  `prepared_capacity_can_end_without_joint_realization_by_core`), proved here without the
  `propext` and `Quot.sound` of the periphery's proofs.
* `ClassificationRobustJudgment.classification_robust_iff`, strict preference under every
  classification of fresh contents into basic and secondary exactly where the fresh contents of
  `b` are retained and `a` is better with all fresh contents secondary, holds with excluded
  middle as a named hypothesis (`classification_robust_iff_of_em`); the forward direction needs
  nothing (`compared_retains`, `compared_secondary`). Excluded middle is exactly what it needs:
  with one fresh content whose retention is a proposition `R`, strict preference under the
  classification making it basic is `R` or its failure (`classification_robust_iff_iff_em`).
* `GenerativeClosure` and `JointInterpretation` judge derivations against a supplied inquiry
  predicate. Read as the core's `Scope`, the configurations a policy's actual executions reach
  from a belief, the inquiry is fixed by the dynamics: a claim derived from a basis holding over
  the scope holds over it, and the whole closure does exactly where the basis does
  (`derivation_sound_on_scope`, `closure_over_scope_iff_basis`); every claim derived from a
  sound policy's goal holds over its scope (`sound_goal_closure`); and with a finite basis, each
  derived claim realized somewhere in the scope is one configuration of the scope realizing them
  all (`common_on_scope_iff`). Soundness itself is the periphery's theorem, compiled by the
  spine run with an empty axiom report.

Direction conventions differ and are kept: in `GenerativeComparison`,
`Better first second` says the second is better; in `PracticalJudgment` and
`LiftBetter`, `better x y` says `x` is better. Every declaration has an empty
axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

universe u v w

/-! ## Seed–edge closures are reachability -/

/-- A one-label process whose steps are the given edges. -/
def edgeProcess {X : Type u} (edge : X → X → Prop) : Process X Unit :=
  ⟨fun x _ y => edge x y⟩

/-- Everything reached from a seed along edges. -/
def Closure {X : Type u} (seed : X → Prop) (edge : X → X → Prop) (x : X) : Prop :=
  ∃ p, seed p ∧ Reach (edgeProcess edge) p x

namespace Closure

variable {X : Type u} {seed : X → Prop} {edge : X → X → Prop}

theorem base {x : X} (held : seed x) : Closure seed edge x :=
  ⟨x, held, Reach.refl _ _⟩

theorem step {x y : X} : Closure seed edge x → edge x y → Closure seed edge y
  | ⟨p, held, path⟩, e => ⟨p, held, path.trans (Reach.of_step (a := ()) e)⟩

/-- Any property holding at seeds and preserved along edges holds on the closure. -/
theorem induction {motive : X → Prop} (start : ∀ x, seed x → motive x)
    (carry : ∀ x y, motive x → edge x y → motive y) {x : X} :
    Closure seed edge x → motive x
  | ⟨p, held, path⟩ =>
    Invariant.reach (P := edgeProcess edge) (fun x _ y e m => carry x y m e) path (start p held)

end Closure

theorem reached_iff_closure {X : Type u} {seed : X → Prop} {edge : X → X → Prop} {x : X} :
    WholeGroundCoverage.Reached seed edge x ↔ Closure seed edge x := by
  constructor
  · intro h
    induction h with
    | seed held => exact Closure.base held
    | step _ e ih => exact ih.step e
  · exact Closure.induction (fun _ held => .seed held) (fun _ _ r e => .step r e)

theorem cutReach_iff_closure {X : Type u} {seed : X → Prop} {edge : X → X → Prop} {x : X} :
    UniversalEthics.CutCoverageAudit.Reach seed edge x ↔ Closure seed edge x := by
  constructor
  · intro h
    induction h with
    | root held => exact Closure.base held
    | step _ e ih => exact ih.step e
  · exact Closure.induction (fun _ held => .root held) (fun _ _ r e => .step r e)

/-- The core's closure under a relation, what lies in every region closed under it that holds a
formation (`Becoming.Feedback`), is the seed–edge closure from that formation alone. -/
theorem withinClosure_iff_closure {X : Type} {rel : X → X → Prop} {f g : X} :
    WithinClosure rel f g ↔ Closure (fun x => x = f) rel g :=
  ⟨fun within => within (Closure (fun x => x = f) rel) (fun _ _ held e => held.step e)
      (Closure.base rfl),
   Closure.induction (motive := WithinClosure rel f)
      (fun x (same : x = f) => same.symm ▸ WithinClosure.refl f)
      (fun _ _ within e => within.trans (WithinClosure.of_rel e))⟩

theorem chain_iff_reach {X : Type} {step : X → X → Prop} {p q : X} :
    EvaluatorGrounding.Chain step p q ↔ Reach (edgeProcess step) p q := by
  constructor
  · intro h
    induction h with
    | refl => exact Reach.refl _ _
    | tail _ last ih => exact ih.trans (Reach.of_step (a := ()) last)
  · intro path
    exact Invariant.reach (P := edgeProcess step) (I := EvaluatorGrounding.Chain step p)
      (fun _ _ _ e c => .tail c e) path (.refl p)

/-! ## Continuations of a frame -/

section Continuations

variable {S : Type u} {A : Type v} {C : Type w}

/-- The joint-continuation space of a frame from a root: reachable configurations
with their realized claims. -/
def Frame.continuations (F : Frame S A C) (root : S) :
    JointContinuationClassification.Continuations S C :=
  ⟨Reach F.P root, F.realized⟩

/-- A step- and claim-preserving map carries every jointly realizable bundle. -/
theorem Frame.map_preserves_bundles {S' : Type u} (F : Frame S A C) (G : Frame S' A C)
    (q : S → S') (step : ∀ s a t, F.P.step s a t → G.P.step (q s) a (q t))
    (claim : ∀ s c, F.realized s c → G.realized (q s) c) (root : S) :
    JointContinuationClassification.PreservesJointBundles
      (F.continuations root) (G.continuations (q root)) :=
  JointContinuationClassification.faithful_history_transport_preserves_joint_bundles q
    (fun _ reached => reached.map step) (fun s c _ held => claim s c held)

/-- A summary whose steps lift and whose claims reflect loses no bundle. -/
theorem Frame.lift_reflects_bundles {S' : Type u} (F : Frame S A C) (G : Frame S' A C)
    (q : S → S') (lift : ∀ s a r, G.P.step (q s) a r → ∃ t, F.P.step s a t ∧ q t = r)
    (claim : ∀ s c, G.realized (q s) c → F.realized s c) (root : S) :
    JointContinuationClassification.PreservesJointBundles
      (G.continuations (q root)) (F.continuations root)
  | _, ⟨_, reached, all⟩ => match Reach.lift lift reached with
    | ⟨t, path, same⟩ => ⟨t, path, fun c held => claim t c (same ▸ all c held)⟩

/-! ## Robust responses, guarantees, evidence narrowing and live steps -/

/-- A common response is a robust response whose admissibility is completion. -/
theorem commonResponse_is_robust {S R : Type} {A : Type v} (P : Process S A)
    (safe : S → A → S → Prop) (goal : S → Prop) (response : R → List A)
    (B : S → Prop) (r : R) :
    CommonResponse P safe goal response B r ↔
      PracticalJudgment.Robust B (fun s r => Completes P safe goal s (response r)) r :=
  Iff.rfl

/-- Every robust response is a common response of the judgment process. -/
theorem robust_iff_commonResponse {W H : Type} (live : W → Prop) (admissible : W → H → Prop)
    (a : H) :
    PracticalJudgment.Robust live admissible a ↔
      CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees live) a :=
  commonResponse_judge_iff.symm

/-- A guarantee is one-step completion. -/
theorem guarantees_iff_completes {S A : Type} (P : Process S A) (s : S) (a : A)
    (goal : S → Prop) :
    PracticalReach.Guarantees (fun a t => P.step s a t) a goal ↔
      Completes P (fun _ _ _ => True) goal s [a] :=
  ⟨fun ⟨live, all⟩ => ⟨live, fun t step => ⟨trivial, all t step⟩⟩,
   fun ⟨live, all⟩ => ⟨live, fun t step => (all t step).2⟩⟩

theorem liveStep_iff_enabled {S A : Type} (step : S → A → S → Prop) (s : S) (a : A) :
    CorrectionInfrastructure.LiveStep step s a ↔ Enabled (⟨step⟩ : Process S A) s a :=
  Iff.rfl

/-- A pure observation: the configuration is unchanged and the outcome is read. -/
def observe {Q : Type v} : Process S Q :=
  ⟨fun s _ t => t = s⟩

theorem after_observe_iff {Q : Type v} {k : Nat} (obs : S → Q → Fin k)
    (B : S → Prop) (q : Q) (o : Fin k) (t : S) :
    After observe (fun s q _ => obs s q) B q o t ↔ B t ∧ obs t q = o :=
  ⟨fun ⟨_, believed, same, read⟩ => by cases same; exact ⟨believed, read⟩,
   fun ⟨believed, read⟩ => ⟨t, believed, rfl, read⟩⟩

/-- Booleans as two observation outcomes, written without numeric literals. -/
def encode : Bool → Fin 2
  | false => ⟨0, Nat.zero_lt_succ 1⟩
  | true => ⟨1, Nat.succ_lt_succ (Nat.zero_lt_succ 0)⟩

theorem encode_inj : ∀ {a b : Bool}, encode a = encode b → a = b
  | false, false, _ => rfl
  | true, true, _ => rfl
  | false, true, h => Nat.noConfusion (congrArg Fin.val h)
  | true, false, h => Nat.noConfusion (congrArg Fin.val h)

theorem mem_filter {α : Type} (p : α → Bool) (x : α) :
    ∀ l : List α, x ∈ l.filter p ↔ x ∈ l ∧ p x = true
  | [] => ⟨fun h => (nomatch h), fun ⟨h, _⟩ => (nomatch h)⟩
  | a :: l => by
    have ih := mem_filter p x l
    unfold List.filter
    cases hp : p a with
    | true =>
      refine ⟨fun h => ?_, fun ⟨m, px⟩ => ?_⟩
      · cases h with
        | head => exact ⟨.head _, hp⟩
        | tail _ h => exact ⟨.tail _ (ih.mp h).1, (ih.mp h).2⟩
      · cases m with
        | head => exact .head _
        | tail _ m => exact .tail _ (ih.mpr ⟨m, px⟩)
    | false =>
      refine ⟨fun h => ⟨.tail _ (ih.mp h).1, (ih.mp h).2⟩, fun ⟨m, px⟩ => ?_⟩
      cases m with
      | head => exact absurd (hp.symm.trans px) Bool.false_ne_true
      | tail _ m => exact ih.mpr ⟨m, px⟩

theorem beq_true_iff : ∀ x b : Bool, (x == b) = true ↔ x = b
  | false, false => ⟨fun _ => rfl, fun _ => rfl⟩
  | true, true => ⟨fun _ => rfl, fun _ => rfl⟩
  | false, true => ⟨fun h => (nomatch h), fun h => (nomatch h)⟩
  | true, false => ⟨fun h => (nomatch h), fun h => (nomatch h)⟩

/-- Revising a list of rules by one observation is `After` on a pure observation. -/
theorem revise_is_after {Q : Type} (hs : List (StandardsBridge.Rule Q)) (q : Q) (b : Bool)
    (h : StandardsBridge.Rule Q) :
    h ∈ StandardsBridge.revise hs (q, b) ↔
      After observe (fun (g : StandardsBridge.Rule Q) q _ => encode (g q)) (· ∈ hs) q
        (encode b) h :=
  (mem_filter _ h hs).trans <|
    (Iff.intro (fun ⟨m, e⟩ => ⟨m, congrArg encode ((beq_true_iff _ _).mp e)⟩)
      (fun ⟨m, e⟩ => ⟨m, (beq_true_iff _ _).mpr (encode_inj e)⟩)).trans
    (after_observe_iff (fun (g : StandardsBridge.Rule Q) q => encode (g q)) _ q _ h).symm

end Continuations

/-! ## The core's definitions are those of the existing modules -/

section Definitions

variable {S A C Pos : Type}

/-- The frame's configurations as an inventory under a reading. -/
def Frame.inventory (F : Frame S A C) (reading : C → Prop) : GenerativeComparison.Inventory S C :=
  ⟨F.realized, reading⟩

theorem g0_iff (F : Frame S A C) (living : C → Prop) (positive : S → C → Prop) :
    G0 F living positive ↔ GenerativeComparison.G0 (F.inventory living) positive :=
  Iff.rfl

theorem extension_iff (F : Frame S A C) (living : C → Prop) (s t : S) :
    Extension F living s t ↔ GenerativeComparison.GenerativeExtension (F.inventory living) s t :=
  Iff.rfl

theorem comparison_iff (F : Frame S A C) (living : C → Prop) (Better : S → S → Prop) :
    Comparison F living Better ↔
      GenerativeComparison.ComparisonPrinciple (F.inventory living) Better :=
  Iff.rfl

theorem securesPositiveGround_iff {H R : Type} (admitted : R → H → Prop)
    (before : H → C → Prop) (positive : H → C → Prop) (r : R) :
    SecuresPositiveGround admitted before positive r ↔
      PositionedPositiveReason.SecuresPositiveGround admitted before positive r :=
  Iff.rfl

theorem positionedArticulation_iff {H R : Type} (access : Pos → R → Prop)
    (admitted : R → H → Prop) (before : H → C → Prop) (positive : H → C → Prop)
    (Reason : Pos → R → Prop) :
    PositionedArticulation access admitted before positive Reason ↔
      PositionedPositiveReason.PositionedArticulation access admitted before positive Reason :=
  Iff.rfl

/-- J1/J2 on configurations: basic conditions first, then living gains. -/
def BetterAt (F : Frame S A C) (basic living : C → Prop) : S → S → Prop :=
  PracticalJudgment.Better (fun s c => basic c ∧ F.realized s c)
    (fun s c => living c ∧ F.realized s c)

/-- The spine's `living` is the recorded relational reading. -/
theorem Conditions.living_iff_relational {F Cond : Type} {P : Process S A}
    (K : Conditions S F Cond) (r : Run P) (own sig : Pos → F × Nat → Prop) (e : F × Nat) :
    (K.valuation r own sig).living e ↔
      (RenewalComparison.relationalInventory (fun _ : Unit => K.along r)).realized () e :=
  Iff.rfl

/-- The core's whole-run reading of courses is `RenewalComparison`'s relational inventory. -/
theorem Ranking.wholeRun_iff {W F Cond : Type} (U : W → RelationalRenewal.Unfolding F Cond)
    (w : W) (e : F × Nat) :
    Ranking.wholeRun U w e ↔ (RenewalComparison.relationalInventory U).realized w e :=
  Iff.rfl

/-- The core's course without the focal formation has `RenewalComparison`'s levels. -/
theorem Ranking.undisturbed_eq (L : RelationalRenewal.Law) :
    ∀ t, Ranking.undisturbed L t = RenewalComparison.undisturbed L t
  | 0 => rfl
  | t + 1 =>
    congrArg (fun x => if L.needG ≤ x then x + L.renew else x) (Ranking.undisturbed_eq L t)

end Definitions

/-! ## The axiom discharges G0 in the existing modules -/

section Discharge

/-- Under the axiom `GenerativeComparison.G0` holds for every inventory, with positive relevance
read from significance: realized generative content whose continuation has significance from
every standpoint. Every theorem taking G0 as a hypothesis for an arbitrary positive relevance
holds with this one. -/
theorem inventory_g0_of_unrestricted {H Q F Pos : Type}
    (inventory : GenerativeComparison.Inventory H Q) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat) :
    GenerativeComparison.G0 inventory
      (fun h q => inventory.generative q ∧ inventory.realized h q ∧
        ∀ p, sig p (step q) (formation q)) :=
  fun _ q generative realized => ⟨generative, realized, fun p => unrestricted (p, step q, formation q)⟩

/-- On a frame's inventory it is the core's positive relevance read from significance. -/
theorem relevance_inventory_iff {S A Q F Pos : Type} (M : Frame S A Q) (living : Q → Prop)
    (sig : Pos → Nat → F → Prop) (formation : Q → F) (step : Q → Nat) (s : S) (c : Q) :
    M.relevance living sig formation step s c ↔
      (M.inventory living).generative c ∧ (M.inventory living).realized s c ∧
        ∀ p, sig p (step c) (formation c) :=
  Iff.rfl

/-- From the axiom, a new realization of a generative extension has positive relevance read from
significance (`GenerativeComparison.new_realization_has_positive_relevance`). -/
theorem new_realization_of_unrestricted {H Q F Pos : Type}
    {inventory : GenerativeComparison.Inventory H Q} {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat) {first second : H}
    (extension : GenerativeComparison.GenerativeExtension inventory first second) :
    ∃ q, (inventory.generative q ∧ inventory.realized second q ∧
        ∀ p, sig p (step q) (formation q)) ∧ ¬ inventory.realized first q :=
  GenerativeComparison.new_realization_has_positive_relevance
    (inventory_g0_of_unrestricted inventory unrestricted formation step) extension

/-- From the axiom, contingent generation secures positive ground read from significance
(`PositiveGroundUncertainty.contingent_generation_has_positive_ground`). -/
theorem contingent_generation_of_unrestricted {H Q F Pos : Type} (admitted : H → Prop)
    (before : H → Q → Prop) (inventory : GenerativeComparison.Inventory H Q)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat)
    (formed : ∀ h, admitted h → ∃ q, inventory.generative q ∧ inventory.realized h q ∧
      ¬ before h q) :
    ∀ h, admitted h → ∃ q, (inventory.generative q ∧ inventory.realized h q ∧
      ∀ p, sig p (step q) (formation q)) ∧ ¬ before h q :=
  PositiveGroundUncertainty.contingent_generation_has_positive_ground admitted before inventory _
    (inventory_g0_of_unrestricted inventory unrestricted formation step) formed

/-- Universal address from the axiom: with D read on positive relevance from significance,
formation correspondence gives every position with access the reason
(`PositionedPositiveReason.every_situated_position_has_reason`). -/
theorem every_situated_position_has_reason_of_unrestricted {Pos H Q R F : Type}
    (access : Pos → R → Prop) (admitted : R → H → Prop) (before : H → Q → Prop)
    (inventory : GenerativeComparison.Inventory H Q) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat)
    (Reason : Pos → R → Prop)
    (articulate : PositionedPositiveReason.PositionedArticulation access admitted before
      (fun h q => inventory.generative q ∧ inventory.realized h q ∧
        ∀ p, sig p (step q) (formation q)) Reason)
    (a : R)
    (formed : ∀ h, admitted a h → ∃ q, inventory.generative q ∧ inventory.realized h q ∧
      ¬ before h q) :
    ∀ p, access p a → Reason p a :=
  PositionedPositiveReason.every_situated_position_has_reason access admitted before inventory _
    Reason (inventory_g0_of_unrestricted inventory unrestricted formation step) articulate a formed

end Discharge

/-! ## Open-form revision on the shared frame (P89)

These are adapters for the existing result, not another model or an independent
ethical principle. The run supplies actual admissible steps. A completion event at
index `n` concerns the step to configuration `n + 1`; a bound `B` therefore allows
at most `B + 1` steps. The certificate is not a value measure. The significance
premise remains explicit, and no permission to replace an undertaking is inferred.
-/

section OpenFormRevision

/-- The inherited finite handoff argument supplies new realization on a run of the
shared frame. Completion-to-realization correspondence stays a visible premise. -/
theorem Run.novel_by_handoff {S A Q : Type} (M : Frame S A Q) (r : Run M.P)
    (living : Q → Prop) (before : S → Q → Prop)
    (rank : Nat → S → Nat) (completed : Nat → Prop) [DecidablePred completed]
    (bound : Nat) (initial : rank 0 (r.state 0) ≤ bound)
    (localStep : ∀ n, ¬ completed n → rank n (r.state (n + 1)) < rank n (r.state n))
    (handoff : ∀ n, ¬ completed n →
      rank (n + 1) (r.state (n + 1)) ≤ rank n (r.state (n + 1)))
    (correspondence : ∀ n, completed n → Novel M living before (r.state (n + 1))) :
    ∃ n, n ≤ bound ∧ Novel M living before (r.state (n + 1)) := by
  have decrease := OpenFutureRevision.handed_off_progress r.state rank completed localStep handoff
  obtain ⟨n, _, within, finished⟩ := ContinuationRenewal.renewal_within_rank_bound
    (fun n => rank n (r.state n)) completed decrease bound 0 initial
  exact ⟨n, by simpa using within, correspondence n finished⟩

/-- The same realized witness has the core's positive relevance under the named
significance condition. Its form is not fixed in advance or across runs. -/
theorem Run.relevance_by_handoff_of_unrestricted {S A Q F Pos : Type}
    (M : Frame S A Q) (r : Run M.P) (living : Q → Prop) (before : S → Q → Prop)
    (rank : Nat → S → Nat) (completed : Nat → Prop) [DecidablePred completed]
    (bound : Nat) (initial : rank 0 (r.state 0) ≤ bound)
    (localStep : ∀ n, ¬ completed n → rank n (r.state (n + 1)) < rank n (r.state n))
    (handoff : ∀ n, ¬ completed n →
      rank (n + 1) (r.state (n + 1)) ≤ rank n (r.state (n + 1)))
    (correspondence : ∀ n, completed n → Novel M living before (r.state (n + 1)))
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (formation : Q → F) (step : Q → Nat) :
    ∃ n, n ≤ bound ∧ ∃ q,
      M.relevance living sig formation step (r.state (n + 1)) q ∧
      ¬ before (r.state (n + 1)) q := by
  obtain ⟨n, within, q, alive, real, fresh⟩ :=
    r.novel_by_handoff M living before rank completed bound initial localStep handoff correspondence
  exact ⟨n, within, q,
    g0_of_unrestricted M living unrestricted formation step _ q alive real, fresh⟩

/-- The previously audited but unwritten instance of
`OpenFutureRevision.positive_ground_by_bound`, now checked in the bridge. -/
theorem positive_ground_by_bound_of_unrestricted {H Q F Pos : Type}
    (admitted : H → Prop) (appears : H → Nat → Q → Prop) (generative : Q → Prop)
    (before : H → Q → Prop) (bound : Nat) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat)
    (formed : ∀ h, admitted h → ∃ q,
      (OpenFutureRevision.boundedInventory appears generative bound).generative q ∧
      (OpenFutureRevision.boundedInventory appears generative bound).realized h q ∧
      ¬ before h q) :
    ∀ h, admitted h → ∃ q,
      (generative q ∧ (∃ n, n ≤ bound ∧ appears h n q) ∧
        ∀ p, sig p (step q) (formation q)) ∧ ¬ before h q :=
  OpenFutureRevision.positive_ground_by_bound admitted appears generative before bound _
    (inventory_g0_of_unrestricted (OpenFutureRevision.boundedInventory appears generative bound)
      unrestricted formation step) formed

/-- Complete producer-to-consumer instance, with every operational hypothesis of
the inherited generation theorem retained and G0 obtained from significance. -/
theorem revised_generation_by_bound_of_unrestricted {H S Q F Pos : Type}
    (admitted : H → Prop) (states : H → Nat → S) (rank : H → Nat → S → Nat)
    (completed : H → Nat → Prop) (decideEvent : ∀ h, DecidablePred (completed h))
    (appears : H → Nat → Q → Prop) (generative : Q → Prop) (before : H → Q → Prop)
    (bound : Nat) (initial : ∀ h, admitted h → rank h 0 (states h 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n (states h (n + 1)) < rank h n (states h n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n + 1) (states h (n + 1)) ≤ rank h n (states h (n + 1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, generative q ∧ appears h n q ∧ ¬ before h q)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (formation : Q → F) (step : Q → Nat) :
    ∀ h, admitted h → ∃ q,
      (generative q ∧ (∃ n, n ≤ bound ∧ appears h n q) ∧
        ∀ p, sig p (step q) (formation q)) ∧ ¬ before h q :=
  positive_ground_by_bound_of_unrestricted admitted appears generative before bound
    unrestricted formation step
    (OpenFutureRevision.generation_by_bound admitted states rank completed decideEvent
      appears generative before bound initial localStep handoff correspondence)

end OpenFormRevision

/-! ## Situations of a frame and the lifting rule -/

section Lifting

open GenerativeComparison

variable {S A C : Type}

/-- Every outcome of `b` generatively extends every outcome of `a`. -/
def LiftExtension (F : Frame S A C) (living : C → Prop) (s : S) (a b : A) : Prop :=
  ∀ t, F.P.step s a t → ∀ t', F.P.step s b t' → Extension F living t t'

/-- C lifts: a lifted extension is a conservative lifted comparison. `Better first
second` follows `GenerativeComparison`: the second is better. -/
theorem comparison_lifts {F : Frame S A C} {living : C → Prop} {Better : S → S → Prop}
    (comparison : Comparison F living Better) {s : S} {a b : A}
    (extension : LiftExtension F living s a b) : LiftBetter F (fun x y => Better y x) s b a :=
  fun t' ht' t ht => comparison t t' (extension t ht t' ht')

/-- P with L: a lifted comparison between live responses supplies a reason to move. -/
def LiftedArticulation (F : Frame S A C) (Better : S → S → Prop) (s : S)
    (Reason : A → A → Prop) : Prop :=
  ∀ a b, Enabled F.P s a → Enabled F.P s b → LiftBetter F (fun x y => Better y x) s b a →
    Reason a b

theorem lifted_comparison_supplies_reason {F : Frame S A C} {living : C → Prop}
    {Better : S → S → Prop} {s : S} {Reason : A → A → Prop}
    (comparison : Comparison F living Better) (practical : LiftedArticulation F Better s Reason)
    {a b : A} (liveA : Enabled F.P s a) (liveB : Enabled F.P s b)
    (extension : LiftExtension F living s a b) : Reason a b :=
  practical a b liveA liveB (comparison_lifts comparison extension)

/-- A live response no live response liftedly extends. -/
def LiftSurvives (F : Frame S A C) (living : C → Prop) (s : S) (a : A) : Prop :=
  Enabled F.P s a ∧ ∀ b, Enabled F.P s b → ¬ LiftExtension F living s a b

/-- N with L: a selected response is live and liftedly dominated by no live one. -/
def LiftCoherence (F : Frame S A C) (Better : S → S → Prop) (s : S)
    (Selected : A → Prop) : Prop :=
  ∀ a, Selected a → Enabled F.P s a ∧
    ∀ b, Enabled F.P s b → ¬ LiftBetter F (fun x y => Better y x) s b a

theorem lift_coherent_selection_survives {F : Frame S A C} {living : C → Prop}
    {Better : S → S → Prop} {s : S} {Selected : A → Prop}
    (comparison : Comparison F living Better) (coherence : LiftCoherence F Better s Selected)
    {a : A} (selected : Selected a) : LiftSurvives F living s a :=
  match coherence a selected with
  | ⟨live, undominated⟩ =>
    ⟨live, fun b liveB extension => undominated b liveB (comparison_lifts comparison extension)⟩

theorem lift_continual_improvement_has_no_survivor {F : Frame S A C} {living : C → Prop}
    {s : S} (improvement : ∀ a, Enabled F.P s a → ∃ b, Enabled F.P s b ∧ LiftExtension F living s a b)
    (a : A) : ¬ LiftSurvives F living s a
  | ⟨live, survives⟩ => match improvement a live with
    | ⟨b, liveB, extension⟩ => survives b liveB extension

/-- A functional situation as one frame step at a configuration. -/
def situationProcess (situation : Situation S A) (s : S) : Process S A :=
  ⟨fun x a t => x = s ∧ situation.feasible a ∧ t = situation.realize a⟩

theorem situation_enabled_iff (situation : Situation S A) (s : S) (a : A) :
    Enabled (situationProcess situation s) s a ↔ situation.feasible a :=
  ⟨fun ⟨_, _, feasible, _⟩ => feasible, fun feasible => ⟨_, rfl, feasible, rfl⟩⟩

theorem situation_lift_iff (situation : Situation S A) (s : S) (realized : S → C → Prop)
    (better : S → S → Prop) {a b : A} (feasibleA : situation.feasible a)
    (feasibleB : situation.feasible b) :
    LiftBetter ⟨situationProcess situation s, realized⟩ better s a b ↔
      better (situation.realize a) (situation.realize b) :=
  ⟨fun lifted => lifted _ ⟨rfl, feasibleA, rfl⟩ _ ⟨rfl, feasibleB, rfl⟩,
   fun held _ ⟨_, _, ha⟩ _ ⟨_, _, hb⟩ => by subst ha; subst hb; exact held⟩

/-- The functional articulation P is exactly the deterministic case of P with L. -/
theorem articulation_iff_lifted (situation : Situation S A) (s : S) (realized : S → C → Prop)
    (Better : S → S → Prop) (Reason : A → A → Prop) :
    PracticalArticulation situation Better Reason ↔
      LiftedArticulation ⟨situationProcess situation s, realized⟩ Better s Reason :=
  ⟨fun practical a b liveA liveB lifted =>
    let fa := (situation_enabled_iff situation s a).mp liveA
    let fb := (situation_enabled_iff situation s b).mp liveB
    practical a b fa fb ((situation_lift_iff situation s realized _ fb fa).mp lifted),
   fun lifted a b fa fb better =>
    lifted a b ((situation_enabled_iff situation s a).mpr fa)
      ((situation_enabled_iff situation s b).mpr fb)
      ((situation_lift_iff situation s realized (fun x y => Better y x) fb fa).mpr better)⟩

namespace LiftModel

inductive Act where
  | low | high | mixed | dead

/-- From configuration 0: `low` reaches 1, `high` 3, `mixed` 0 or 4, `dead` nothing.
A larger configuration is better. -/
def options : Nat → Act → Nat → Prop
  | s, .low, t => s = 0 ∧ t = 1
  | s, .high, t => s = 0 ∧ t = 3
  | s, .mixed, t => s = 0 ∧ (t = 0 ∨ t = 4)
  | _, .dead, _ => False

def frame : Frame Nat Act Unit := ⟨⟨options⟩, fun _ _ => True⟩

def larger (x y : Nat) : Prop := y < x

/-- The lifting rule is substantive: a response with one better and one worse
outcome is not comparable by the conservative rule, yet some outcome beats. -/
theorem some_outcome_does_not_lift :
    (∃ t t', frame.P.step 0 .mixed t ∧ frame.P.step 0 .high t' ∧ larger t t') ∧
    ¬ LiftBetter frame larger 0 .mixed .high ∧ ¬ LiftBetter frame larger 0 .high .mixed :=
  ⟨⟨4, 3, ⟨rfl, Or.inr rfl⟩, ⟨rfl, rfl⟩, Nat.lt_succ_self 3⟩,
    fun lifted => Nat.not_lt_zero 3 (lifted 0 ⟨rfl, Or.inl rfl⟩ 3 ⟨rfl, rfl⟩),
    fun lifted => Nat.lt_asymm (Nat.lt_succ_self 3) (lifted 3 ⟨rfl, rfl⟩ 4 ⟨rfl, Or.inr rfl⟩)⟩

/-- Transitivity needs a live middle response: through a response with no outcome
both lifted comparisons hold vacuously, while the composite fails. -/
theorem lift_needs_live_middle :
    LiftBetter frame larger 0 .low .dead ∧ LiftBetter frame larger 0 .dead .high ∧
    ¬ LiftBetter frame larger 0 .low .high :=
  ⟨fun _ _ _ never => (nomatch never), fun _ never => (nomatch never),
    fun lifted => Nat.lt_asymm (lifted 1 ⟨rfl, rfl⟩ 3 ⟨rfl, rfl⟩)
      (Nat.lt_trans (Nat.lt_succ_self 1) (Nat.lt_succ_self 2))⟩

end LiftModel

end Lifting

/-! ## Relational identity: the earlier bisimulations are the core's -/

section Likeness

variable {S : Type u} {T : Type w} {A : Type v}

/-- A process read with no claims. -/
def Frame.bare (P : Process S A) : Frame S A Empty :=
  ⟨P, fun _ c => nomatch c⟩

/-- **`Deeper.Bisimulation` is the core's bisimulation of frames with no claims.** -/
theorem deeper_bisimulation_iff {P : Process S A} {Q : Process T A} {B : S → T → Prop} :
    Deeper.Bisimulation P Q B ↔ Bisimulation (Frame.bare P) (Frame.bare Q) B :=
  ⟨fun ⟨forth, back⟩ s t related =>
    ⟨(fun c => nomatch c), fun a s' step => forth s t a s' related step,
     fun a t' step => back s t a t' related step⟩,
   fun bisim =>
    ⟨fun s t a s' related step => (bisim s t related).2.1 a s' step,
     fun s t a t' related step => (bisim s t related).2.2 a t' step⟩⟩

/-- **The relational reading of 6 October 2026 is an instance.** In `static` and `toggle`
every configuration of one is alike to every configuration of the other. -/
theorem static_toggle_alike (s t : Bool) :
    Alike (Frame.bare Deeper.static) (Frame.bare Deeper.toggle) s t :=
  ⟨_, deeper_bisimulation_iff.mp Deeper.static_toggle_one_dynamics, trivial⟩

variable {O : Type v}

/-- A model of `ExplanatoryBranching` is a frame whose claims are its conditions. -/
def Frame.ofModel (m : ExplanatoryBranching.Model S A O) : Frame S A O :=
  ⟨m.process, m.condition⟩

/-- **`ExplanatoryBranching.Bisimulation` is the core's bisimulation of frames.** -/
theorem branching_bisimulation_iff {m : ExplanatoryBranching.Model S A O}
    {n : ExplanatoryBranching.Model T A O} {R : S → T → Prop} :
    ExplanatoryBranching.Bisimulation m n R ↔
      Bisimulation (Frame.ofModel m) (Frame.ofModel n) R :=
  ⟨fun ⟨⟨forth, back⟩, conditions⟩ s t related =>
    ⟨conditions s t related, fun a s' step => forth s t a s' related step,
     fun a t' step => back s t a t' related step⟩,
   fun bisim =>
    ⟨⟨fun s t a s' related step => (bisim s t related).2.1 a s' step,
      fun s t a t' related step => (bisim s t related).2.2 a t' step⟩,
     fun s t related => (bisim s t related).1⟩⟩

/-- **Alike configurations pass every branching test** of `ExplanatoryBranching`, negation and
conjunction included (`bisimulation_implies_same`). -/
theorem Alike.same {m : ExplanatoryBranching.Model S A O} {n : ExplanatoryBranching.Model T A O}
    {s : S} {t : T} (alike : Alike (Frame.ofModel m) (Frame.ofModel n) s t) :
    ExplanatoryBranching.Same m n s t :=
  match alike with
  | ⟨_, bisim, related⟩ =>
    ExplanatoryBranching.bisimulation_implies_same (branching_bisimulation_iff.mpr bisim) related

/-- A branching test of the core read as a test of `ExplanatoryBranching`. -/
def BranchingTest.toTest : BranchingTest A O → ExplanatoryBranching.Test A O
  | .top => .top
  | .claim c => .atom c
  | .not φ => .neg φ.toTest
  | .both φ ψ => .conj φ.toTest ψ.toTest
  | .can a φ => .after a φ.toTest

/-- A test of `ExplanatoryBranching` read as a branching test of the core. -/
def BranchingTest.ofTest : ExplanatoryBranching.Test A O → BranchingTest A O
  | .top => .top
  | .atom o => .claim o
  | .neg f => .not (BranchingTest.ofTest f)
  | .conj f g => .both (BranchingTest.ofTest f) (BranchingTest.ofTest g)
  | .after a f => .can a (BranchingTest.ofTest f)

/-- Reading a test of `ExplanatoryBranching` into the core and back gives it again. -/
theorem BranchingTest.toTest_ofTest :
    ∀ f : ExplanatoryBranching.Test A O, (BranchingTest.ofTest f).toTest = f
  | .top => rfl
  | .atom _ => rfl
  | .neg f => congrArg ExplanatoryBranching.Test.neg (BranchingTest.toTest_ofTest f)
  | .conj f g => congr (congrArg ExplanatoryBranching.Test.conj (BranchingTest.toTest_ofTest f))
      (BranchingTest.toTest_ofTest g)
  | .after a f => congrArg (ExplanatoryBranching.Test.after a) (BranchingTest.toTest_ofTest f)

/-- Reading a branching test of the core into `ExplanatoryBranching` and back gives it again. -/
theorem BranchingTest.ofTest_toTest : ∀ φ : BranchingTest A O, BranchingTest.ofTest φ.toTest = φ
  | .top => rfl
  | .claim _ => rfl
  | .not φ => congrArg BranchingTest.not (BranchingTest.ofTest_toTest φ)
  | .both φ ψ => congr (congrArg BranchingTest.both (BranchingTest.ofTest_toTest φ))
      (BranchingTest.ofTest_toTest ψ)
  | .can a φ => congrArg (BranchingTest.can a) (BranchingTest.ofTest_toTest φ)

/-- **A branching test holds where its reading in `ExplanatoryBranching` holds**, in the frame
of a model. -/
theorem BranchingTest.holds_toTest {m : ExplanatoryBranching.Model S A O} :
    ∀ (φ : BranchingTest A O) (s : S),
      BranchingTest.Holds (Frame.ofModel m) s φ ↔ ExplanatoryBranching.Holds m s φ.toTest
  | .top, _ => Iff.rfl
  | .claim _, _ => Iff.rfl
  | .not φ, s => ⟨fun fails holds => fails ((BranchingTest.holds_toTest φ s).mpr holds),
      fun fails holds => fails ((BranchingTest.holds_toTest φ s).mp holds)⟩
  | .both φ ψ, s => ⟨fun ⟨first, second⟩ => ⟨(BranchingTest.holds_toTest φ s).mp first,
        (BranchingTest.holds_toTest ψ s).mp second⟩,
      fun ⟨first, second⟩ => ⟨(BranchingTest.holds_toTest φ s).mpr first,
        (BranchingTest.holds_toTest ψ s).mpr second⟩⟩
  | .can _ φ, _ => ⟨fun ⟨t, step, holds⟩ => ⟨t, step, (BranchingTest.holds_toTest φ t).mp holds⟩,
      fun ⟨t, step, holds⟩ => ⟨t, step, (BranchingTest.holds_toTest φ t).mpr holds⟩⟩

/-- **Passing the same branching tests of the core is passing the same tests of
`ExplanatoryBranching`.** -/
theorem sameBranchingTests_iff_same {m : ExplanatoryBranching.Model S A O}
    {n : ExplanatoryBranching.Model T A O} {s : S} {t : T} :
    SameBranchingTests (Frame.ofModel m) (Frame.ofModel n) s t ↔
      ExplanatoryBranching.Same m n s t :=
  ⟨fun same f => Eq.subst
      (motive := fun g => ExplanatoryBranching.Holds m s g ↔ ExplanatoryBranching.Holds n t g)
      (BranchingTest.toTest_ofTest f)
      ((BranchingTest.holds_toTest _ s).symm.trans
        ((same _).trans (BranchingTest.holds_toTest _ t))),
   fun same φ => (BranchingTest.holds_toTest φ s).trans
      ((same φ.toTest).trans (BranchingTest.holds_toTest φ t).symm)⟩

/-- **On finite decided models, passing the same tests of `ExplanatoryBranching` is likeness,
with no classical reasoning.** Where the moves and conditions are listed, some list holds the
configurations of each model, and whether a move takes one configuration to another and whether
a configuration meets a condition are decided, configurations pass the same tests exactly where
they are alike: on such models, `same_iff_bisimilar` with no classical reasoning. -/
theorem same_iff_alike_of_finiteDecided {m : ExplanatoryBranching.Model S A O}
    {n : ExplanatoryBranching.Model T A O} (moves : ∃ l : List A, ∀ a, a ∈ l)
    (conditions : ∃ l : List O, ∀ o, o ∈ l) (finite : FiniteDecided (Frame.ofModel m))
    (finite' : FiniteDecided (Frame.ofModel n)) {s : S} {t : T} :
    ExplanatoryBranching.Same m n s t ↔ Alike (Frame.ofModel m) (Frame.ofModel n) s t :=
  sameBranchingTests_iff_same.symm.trans
    (alike_iff_sameBranchingTests moves conditions finite finite').symm

/-- **On image-finite models, passing the same tests of `ExplanatoryBranching` is likeness, given
excluded middle**, with neither the moves nor the conditions listed. -/
theorem same_iff_alike_of_imageFinite (em : ∀ p : Prop, Decided p)
    {m : ExplanatoryBranching.Model S A O} {n : ExplanatoryBranching.Model T A O}
    (fm : ExplanatoryBranching.ImageFinite m) (fn : ExplanatoryBranching.ImageFinite n)
    {s : S} {t : T} :
    ExplanatoryBranching.Same m n s t ↔ Alike (Frame.ofModel m) (Frame.ofModel n) s t :=
  sameBranchingTests_iff_same.symm.trans
    (alike_iff_sameBranchingTests_of_em (F := Frame.ofModel m) (G := Frame.ofModel n) em fm fn).symm

/-- **`same_iff_bisimilar` is a theorem of the core with excluded middle a hypothesis**: on
image-finite models, positions pass the same tests exactly where a bisimulation relates them. -/
theorem same_iff_bisimilar_of_em (em : ∀ p : Prop, Decided p)
    {m : ExplanatoryBranching.Model S A O} {n : ExplanatoryBranching.Model T A O}
    (fm : ExplanatoryBranching.ImageFinite m) (fn : ExplanatoryBranching.ImageFinite n)
    (s : S) (t : T) :
    ExplanatoryBranching.Same m n s t ↔ ∃ R, ExplanatoryBranching.Bisimulation m n R ∧ R s t :=
  (same_iff_alike_of_imageFinite em fm fn).trans
    ⟨fun ⟨R, bisim, related⟩ => ⟨R, branching_bisimulation_iff.mpr bisim, related⟩,
     fun ⟨R, bisim, related⟩ => ⟨R, branching_bisimulation_iff.mp bisim, related⟩⟩

/-- **Tests separate a model exactly where the core's branching tests separate its frame**, so
`same_functional` is `SameBranchingTests.functional`. -/
theorem separated_iff {n : ExplanatoryBranching.Model T A O} :
    ExplanatoryBranching.Separated n ↔
      ∀ t t', SameBranchingTests (Frame.ofModel n) (Frame.ofModel n) t t' → t = t' :=
  ⟨fun sep t t' same => sep t t' (sameBranchingTests_iff_same.mp same),
   fun sep t t' same => sep t t' (sameBranchingTests_iff_same.mpr same)⟩

end Likeness

/-! ## Self-good along profiles is N_rel on profiles -/

section Profiles

variable {Gen Prof : Type}

/-- **A standpoint's valuation of profiles.** The claims are the profiles, each counted living; a
profile is related to those one small step from it, is the standpoint's own where an own living
occurrence has it, and is significant where `val` holds of it. -/
def profileValuation (s : EvaluatorGrounding.Standpoint Gen Prof) (val : Prof → Prop)
    (step : Prof → Prof → Prop) : Valuation Unit Prof :=
  ⟨fun _ => True, step, fun _ q => ∃ g, s.own g ∧ s.living g ∧ s.prof g = q, fun _ q => val q⟩

/-- **Tolerance is N_rel on profiles.** -/
theorem tolerant_iff_neutral {s : EvaluatorGrounding.Standpoint Gen Prof} {val : Prof → Prop}
    {step : Prof → Prof → Prop} :
    EvaluatorGrounding.Tolerant val step ↔ Neutral (profileValuation s val step).transmits :=
  ⟨fun tol ⟨_, p, q⟩ held related _ => tol p q related held,
   fun neutral p q related held => neutral ((), p, q) held related True.intro⟩

/-- **A chain of small steps is reach along related profiles.** -/
theorem chain_iff_reach_profiles {s : EvaluatorGrounding.Standpoint Gen Prof} {val : Prof → Prop}
    {step : Prof → Prof → Prop} {p q : Prof} :
    EvaluatorGrounding.Chain step p q ↔ Reach (profileValuation s val step).relations p q := by
  constructor
  · intro chain
    induction chain with
    | refl => exact Reach.refl _ _
    | tail _ last ih => exact ih.trans (Reach.of_step (a := ()) ⟨last, True.intro⟩)
  · intro path
    exact Invariant.reach (P := (profileValuation s val step).relations)
      (I := EvaluatorGrounding.Chain step p) (fun _ _ _ e c => .tail c e.1) path (.refl p)

/-- **S0 under supervenience is S0 on profiles.** -/
theorem selfGood_profiles {s : EvaluatorGrounding.Standpoint Gen Prof} {val : Prof → Prop}
    {step : Prof → Prof → Prop} (sup : EvaluatorGrounding.Supervenes s val)
    (self : EvaluatorGrounding.SelfGood s) : (profileValuation s val step).SelfGood () :=
  fun _ ⟨g, own, alive, same⟩ _ => same ▸ (sup g alive).1 (self g own alive)

/-- **`tolerant_chain_reaches` through the core**: under supervenience, S0 and tolerance, every
reachable living occurrence whose profile a chain of small steps links to an own living one has
significance, by the core's N_rel carrying significance along related profiles
(`Valuation.reaches`). -/
theorem tolerant_chain_reaches_by_core (s : EvaluatorGrounding.Standpoint Gen Prof)
    (val : Prof → Prop) (step : Prof → Prof → Prop) (sup : EvaluatorGrounding.Supervenes s val)
    (self : EvaluatorGrounding.SelfGood s) (tol : EvaluatorGrounding.Tolerant val step)
    (chain : ∀ g', s.reach g' → s.living g' →
      ∃ g, s.own g ∧ s.living g ∧ EvaluatorGrounding.Chain step (s.prof g) (s.prof g')) :
    ∀ g', s.reach g' → s.living g' → s.sig g' :=
  fun g' reached alive' => match chain g' reached alive' with
  | ⟨g, own, alive, linked⟩ => (sup g' alive').2
      (Valuation.reaches (tolerant_iff_neutral (s := s).mp tol)
        (chain_iff_reach_profiles (s := s) (val := val).mp linked)
        (selfGood_profiles (step := step) sup self (s.prof g) ⟨g, own, alive, rfl⟩ True.intro))

end Profiles

/-! ## The information C needs: joint bundles, not marginals -/

section JointBundles

/-- An inventory as a frame with no moves: its wholes are the configurations, realizing its
claims. -/
def Frame.ofInventory {H Q : Type} (I : GenerativeComparison.Inventory H Q) : Frame H Unit Q :=
  ⟨⟨fun _ _ _ => False⟩, I.realized⟩

/-- **`strict_comparison_cannot_factor_through_marginals` through the core**: retaining the
coupling extends releasing it with the same marginal possibilities, so by `Comparison.separates`
no comparison read off a summary that marginals determine, comparing no summary with itself,
satisfies C. -/
theorem strict_comparison_through_marginals_by_core {Summary : Type}
    (summary : RelationalGrounding.Regime → Summary)
    (marginalDetermines : ∀ a b, (∀ claim, RelationalGrounding.marginal a claim ↔
      RelationalGrounding.marginal b claim) → summary a = summary b)
    (compare : Summary → Summary → Prop) (irreflexive : ∀ s, ¬ compare s s) :
    ¬ GenerativeComparison.ComparisonPrinciple RelationalGrounding.jointInventory
      (fun a b => compare (summary a) (summary b)) :=
  fun comparison =>
    Comparison.separates (F := Frame.ofInventory RelationalGrounding.jointInventory)
      (living := RelationalGrounding.jointInventory.generative) irreflexive comparison
      RelationalGrounding.joint_bundle_extension
      (marginalDetermines _ _ RelationalGrounding.marginals_agree_but_joint_descriptions_differ.1)

end JointBundles

/-! ## A protected condition against counted gains -/

section ProtectionPriority

open ProtectionPriorityRival in
/-- Past the protected option, one more gain extends: option `i + 1` to option `i + 2`. -/
theorem protection_successor_extension (i : Nat) :
    Extension (Frame.ofInventory inventory) inventory.generative (i + 1) (i + 1 + 1) :=
  ⟨fun c held => match c, held with
    | .basic, (zero : i + 1 = 0) => Nat.noConfusion zero
    | .gain _, (lt : _ < i + 1) => Nat.lt_succ_of_lt lt,
   .gain (i + 1), True.intro, Nat.lt_succ_self (i + 1), Nat.lt_irrefl (i + 1)⟩

/-- **`every_nat_score_trades` through the core**: the options with gains form an endless chain
of extensions, so by `Comparison.outgrows` every natural-number score satisfying C ranks the
option with `score 0 + 2` gains above protection. -/
theorem every_nat_score_trades_by_core (score : Nat → Nat)
    (comparison : GenerativeComparison.ComparisonPrinciple ProtectionPriorityRival.inventory
      (fun first second => score first < score second)) :
    score 0 < score (score 0 + 2) :=
  Comparison.outgrows (F := Frame.ofInventory ProtectionPriorityRival.inventory)
    (living := ProtectionPriorityRival.inventory.generative) (next := fun i => i + 1)
    comparison protection_successor_extension 0

end ProtectionPriority

/-! ## Protection-first comparisons are comparisons of configurations -/

section JudgedFrames

namespace Judgment

variable {H Cl G : Type} {protect : H → Cl → Prop} {gain : H → G → Prop}

/-- The frame of a protection-first comparison: its options are the configurations, realizing the
protected claims on the left and the gains on the right; it has no moves. -/
def frame (protect : H → Cl → Prop) (gain : H → G → Prop) : Frame H Unit (Sum Cl G) :=
  ⟨⟨fun _ _ _ => False⟩, fun h c => match c with
    | .inl x => protect h x
    | .inr y => gain h y⟩

/-- The protected claims of a judged frame. -/
def protecting : Sum Cl G → Prop
  | .inl _ => True
  | .inr _ => False

/-- The gains of a judged frame. -/
def gaining : Sum Cl G → Prop
  | .inl _ => False
  | .inr _ => True

theorem included_protecting_iff {a b : H} :
    PracticalJudgment.Included (fun c => protecting c ∧ (frame protect gain).realized a c)
        (fun c => protecting c ∧ (frame protect gain).realized b c) ↔
      PracticalJudgment.Included (protect a) (protect b) :=
  ⟨fun included x held => (included (.inl x) ⟨True.intro, held⟩).2,
   fun included c => match c with
    | .inl x => fun ⟨_, held⟩ => ⟨True.intro, included x held⟩
    | .inr _ => fun ⟨no, _⟩ => False.elim no⟩

theorem included_gaining_iff {a b : H} :
    PracticalJudgment.Included (fun c => gaining c ∧ (frame protect gain).realized a c)
        (fun c => gaining c ∧ (frame protect gain).realized b c) ↔
      PracticalJudgment.Included (gain a) (gain b) :=
  ⟨fun included y held => (included (.inr y) ⟨True.intro, held⟩).2,
   fun included c => match c with
    | .inl _ => fun ⟨no, _⟩ => False.elim no
    | .inr y => fun ⟨_, held⟩ => ⟨True.intro, included y held⟩⟩

theorem strict_iff {p p' q q' : Prop} (first : p ↔ p') (second : q ↔ q') :
    (p ∧ ¬ q) ↔ (p' ∧ ¬ q') :=
  ⟨fun ⟨x, y⟩ => ⟨first.mp x, fun z => y (second.mpr z)⟩,
   fun ⟨x, y⟩ => ⟨first.mpr x, fun z => y (second.mp z)⟩⟩

/-- **Every protection-first comparison is `BetterAt` on its frame**: J1/J2 with protected claims
of one kind and gains of another compares options exactly as `BetterAt` compares the
configurations of the frame realizing both, the protected claims as basic and the gains as living. -/
theorem better_iff_betterAt {a b : H} :
    PracticalJudgment.Better protect gain a b ↔
      BetterAt (frame protect gain) protecting gaining a b :=
  have pba := (included_protecting_iff (protect := protect) (gain := gain) (a := b) (b := a)).symm
  have pab := (included_protecting_iff (protect := protect) (gain := gain) (a := a) (b := b)).symm
  have gba := (included_gaining_iff (protect := protect) (gain := gain) (a := b) (b := a)).symm
  have gab := (included_gaining_iff (protect := protect) (gain := gain) (a := a) (b := b)).symm
  ⟨fun better => match better with
    | .inl strict => .inl ((strict_iff pba pab).mp strict)
    | .inr ⟨back, forth, strict⟩ => .inr ⟨pba.mp back, pab.mp forth, (strict_iff gba gab).mp strict⟩,
   fun better => match better with
    | .inl strict => .inl ((strict_iff pba pab).mpr strict)
    | .inr ⟨back, forth, strict⟩ =>
      .inr ⟨pba.mpr back, pab.mpr forth, (strict_iff gba gab).mpr strict⟩⟩

/-- **Its frontier is the frontier of `BetterAt`.** -/
theorem frontier_iff {eligible : H → Prop} {a : H} :
    PracticalJudgment.Frontier eligible (PracticalJudgment.Better protect gain) a ↔
      PracticalJudgment.Frontier eligible (BetterAt (frame protect gain) protecting gaining) a :=
  ⟨fun ⟨admitted, unbeaten⟩ =>
    ⟨admitted, fun b other better => unbeaten b other (better_iff_betterAt.mpr better)⟩,
   fun ⟨admitted, unbeaten⟩ =>
    ⟨admitted, fun b other better => unbeaten b other (better_iff_betterAt.mp better)⟩⟩

/-- On an exact listed menu, the frontier is the undominated members. -/
theorem frontier_iff_undominated {eligible : H → Prop} {better : H → H → Prop} {menu : List H}
    (exact : ∀ a, eligible a ↔ a ∈ menu) {a : H} :
    PracticalJudgment.Frontier eligible better a ↔ Undominated menu better a :=
  ⟨fun ⟨admitted, unbeaten⟩ =>
    ⟨(exact a).mp admitted, fun b mem => unbeaten b ((exact b).mpr mem)⟩,
   fun ⟨mem, unbeaten⟩ =>
    ⟨(exact a).mpr mem, fun b admitted => unbeaten b ((exact b).mp admitted)⟩⟩

/-- **The frontier of a nonempty listed menu is not empty** where the comparison is irreflexive,
transitive and weakly decided on it (`exists_undominated`): `PracticalJudgment.finite_frontier`
with no classical reasoning. -/
theorem frontier_exists {eligible : H → Prop} {better : H → H → Prop} (x : H) (rest : List H)
    (exact : ∀ a, eligible a ↔ a ∈ x :: rest)
    (weakly : ∀ a b, eligible a → eligible b → WeaklyDecided (better a b))
    (irreflexive : ∀ a, ¬ better a a)
    (transitive : ∀ {a b c}, better a b → better b c → better a c) :
    ∃ a, PracticalJudgment.Frontier eligible better a :=
  match exists_undominated x rest (fun a b ma mb => weakly a b ((exact a).mpr ma) ((exact b).mpr mb))
      (fun a _ => irreflexive a) (fun _ _ _ _ _ _ first second => transitive first second) with
  | ⟨a, undominated⟩ => ⟨a, (frontier_iff_undominated exact).mpr undominated⟩

/-- **What every eligible option lacking it is bettered in is required of the frontier**: on a
nonempty listed menu with the comparison irreflexive, transitive and weakly decided, and the task
decided, the frontier is not empty and every member performs the task (`exists_undominated`,
`undominated_has`): `RelationalOrganization.formation_required_of_improvable_absence` with no
classical reasoning. -/
theorem required_of_bettered {eligible : H → Prop} {better : H → H → Prop} {task : H → Prop}
    (x : H) (rest : List H) (exact : ∀ a, eligible a ↔ a ∈ x :: rest)
    (weakly : ∀ a b, eligible a → eligible b → WeaklyDecided (better a b))
    (irreflexive : ∀ a, ¬ better a a)
    (transitive : ∀ {a b c}, better a b → better b c → better a c)
    (decided : ∀ a, eligible a → Decided (task a))
    (bettered : ∀ a, eligible a → ¬ task a → ∃ b, eligible b ∧ better b a) :
    PracticalJudgment.Required (PracticalJudgment.Frontier eligible better) task :=
  ⟨frontier_exists x rest exact weakly irreflexive transitive,
   fun a frontier => undominated_has (menu := x :: rest) (better := better)
     (fun a mem => decided a ((exact a).mpr mem))
     (fun a mem fails => match bettered a ((exact a).mpr mem) fails with
       | ⟨b, admitted, beats⟩ => ⟨b, (exact b).mp admitted, beats⟩)
     a ((frontier_iff_undominated exact).mp frontier)⟩

end Judgment

/-- **The alignment direction compares plans by `BetterAt`**: plans are the configurations of the
frame realizing each claim's protection and its realization, so `transfer_over_expansion` and the
other comparisons of `AlignmentDirection` are comparisons of the spine. -/
theorem alignment_better_iff_betterAt {a b : Nat} :
    PracticalJudgment.Better AlignmentDirection.protection AlignmentDirection.realization a b ↔
      BetterAt (Judgment.frame AlignmentDirection.protection AlignmentDirection.realization)
        Judgment.protecting Judgment.gaining a b :=
  Judgment.better_iff_betterAt

/-- **Its frontier of eligible plans is the frontier of `BetterAt`**, so `expansion_excluded`
excludes expansion from the frontier of the spine's comparison. -/
theorem alignment_frontier_iff {a : Nat} :
    PracticalJudgment.Frontier AlignmentDirection.eligible
        (PracticalJudgment.Better AlignmentDirection.protection AlignmentDirection.realization) a ↔
      PracticalJudgment.Frontier AlignmentDirection.eligible
        (BetterAt (Judgment.frame AlignmentDirection.protection AlignmentDirection.realization)
          Judgment.protecting Judgment.gaining) a :=
  Judgment.frontier_iff

end JudgedFrames

/-! ## Chance floors through the weighted mass -/

section ChanceFloor

/-- `ChanceAdequacy`'s mass is the core's. -/
theorem chance_mass_eq {Ω : Type} (weight : Ω → Nat) (event : Ω → Bool) :
    ∀ domain : List Ω, ChanceAdequacy.mass domain weight event = mass domain weight event
  | [] => rfl
  | h :: tail => congrArg (fun m => (if event h = true then weight h else 0) + m)
      (chance_mass_eq weight event tail)

theorem chance_includedOn_iff {Ω : Type} (domain : List Ω) (before after : Ω → Bool) :
    ChanceAdequacy.IncludedOn domain before after ↔ IncludedOn domain before after :=
  Iff.rfl

/-- **`all_weights_preserve_mass_iff` through the core**: it is `every_weighting_iff`. -/
theorem all_weights_preserve_mass_iff_by_core {Ω : Type} [DecidableEq Ω] (domain : List Ω)
    (before after : Ω → Bool) :
    (∀ weight : Ω → Nat,
      ChanceAdequacy.mass domain weight before ≤ ChanceAdequacy.mass domain weight after) ↔
      ChanceAdequacy.IncludedOn domain before after :=
  Iff.trans
    ⟨fun all weight => Nat.le_trans (Nat.le_of_eq (chance_mass_eq weight before domain).symm)
        (Nat.le_trans (all weight) (Nat.le_of_eq (chance_mass_eq weight after domain))),
     fun all weight => Nat.le_trans (Nat.le_of_eq (chance_mass_eq weight before domain))
        (Nat.le_trans (all weight) (Nat.le_of_eq (chance_mass_eq weight after domain).symm))⟩
    every_weighting_iff

/-- **`fulfillment_gives_chance_floor` through the core**: the floor is `mass_mono` twice. -/
theorem fulfillment_floor_by_core {Ω : Type} (domain : List Ω) (weight : Ω → Nat)
    (demand oldWorks newWorks : Ω → Bool)
    (fulfilled : ChanceAdequacy.Fulfilled domain demand oldWorks newWorks) :
    mass domain weight (ChanceAdequacy.target demand oldWorks) ≤ mass domain weight newWorks ∧
      mass domain weight newWorks ≤ mass domain weight (fun _ => true) :=
  ⟨mass_mono weight fulfilled, mass_mono weight fun _ _ _ => rfl⟩

end ChanceFloor

/-! ## Fallible inspection through the core's witnesses -/

section FallibleWitnesses

theorem list_contains_true_iff {d : Nat} : ∀ {l : List Nat}, l.contains d = true ↔ d ∈ l
  | [] => ⟨fun h => Bool.noConfusion h, fun h => nomatch h⟩
  | b :: l => by
    show (match d == b with | true => true | false => List.elem d l) = true ↔ d ∈ b :: l
    cases h : (d == b) with
    | true => exact ⟨fun _ => Eq.subst (motive := fun v => d ∈ v :: l) (of_decide_eq_true h)
        (.head l), fun _ => rfl⟩
    | false => exact ⟨fun e => .tail b (list_contains_true_iff.mp e), fun m =>
        match mem_cons_cases m with
        | .inl same => Bool.noConfusion (h.symm.trans (decide_eq_true same))
        | .inr m => list_contains_true_iff.mpr m⟩

theorem list_all_true_iff {α : Type} {p : α → Bool} :
    ∀ {l : List α}, l.all p = true ↔ ∀ d ∈ l, p d = true
  | [] => ⟨fun _ _ m => (nomatch m), fun _ => rfl⟩
  | a :: l => by
    show (p a && l.all p) = true ↔ _
    cases h : p a with
    | false => exact ⟨fun e => Bool.noConfusion e,
        fun all => Bool.noConfusion (h.symm.trans (all a (.head l)))⟩
    | true => exact ⟨fun e d m => (match mem_cons_cases m with
        | .inl same => Eq.subst (motive := fun v => p v = true) same.symm h
        | .inr m => list_all_true_iff.mp e d m),
        fun all => list_all_true_iff.mpr fun d m => all d (.tail a m)⟩

theorem list_any_true_iff {α : Type} {p : α → Bool} :
    ∀ {l : List α}, l.any p = true ↔ ∃ d, d ∈ l ∧ p d = true
  | [] => ⟨fun e => Bool.noConfusion e, fun ⟨_, m, _⟩ => nomatch m⟩
  | a :: l => by
    show (p a || l.any p) = true ↔ _
    cases h : p a with
    | true => exact ⟨fun _ => ⟨a, .head l, h⟩, fun _ => rfl⟩
    | false => exact ⟨fun e => let ⟨d, m, pd⟩ := list_any_true_iff.mp e; ⟨d, .tail a m, pd⟩,
        fun ⟨d, m, pd⟩ => match mem_cons_cases m with
        | .inl same => Bool.noConfusion
            (h.symm.trans (Eq.subst (motive := fun v => p v = true) same pd))
        | .inr m => list_any_true_iff.mpr ⟨d, m, pd⟩⟩

/-- One witness's term of `FallibleInspection.explains`, on a received report. -/
theorem witness_true_iff {bad : List Nat} {d : Nat} {v x : Bool} :
    ((bad.contains d || (some v).isNone) || (some v == some x)) = true ↔ (¬ d ∈ bad → v = x) := by
  cases hc : bad.contains d with
  | true => exact ⟨fun _ nb => absurd (list_contains_true_iff.mp hc) nb, fun _ => rfl⟩
  | false =>
    have out : ¬ d ∈ bad := fun m => Bool.noConfusion (hc.symm.trans (list_contains_true_iff.mpr m))
    cases v <;> cases x
    · exact ⟨fun _ _ => rfl, fun _ => rfl⟩
    · exact ⟨fun e => Bool.noConfusion e, fun f => Bool.noConfusion (f out)⟩
    · exact ⟨fun e => Bool.noConfusion e, fun f => Bool.noConfusion (f out)⟩
    · exact ⟨fun _ _ => rfl, fun _ => rfl⟩

theorem some_getD {o : Option Bool} (present : o ≠ none) : o = some (o.getD false) :=
  match o, present with
  | some _, _ => rfl
  | none, absent => absurd rfl absent

/-- On a complete report, `FallibleInspection.explains` is the core's `Readout.Explains`. -/
theorem explains_complete_iff {roster bad : List Nat} {x : Bool}
    {reports : FallibleInspection.Reports} (complete : ∀ d ∈ roster, reports d ≠ none) :
    FallibleInspection.explains roster bad x reports = true ↔
      Readout.Explains roster bad x fun d => (reports d).getD false :=
  list_all_true_iff.trans
    ⟨fun all d m => (Eq.subst (motive := fun o =>
        ((bad.contains d || o.isNone) || (o == some x)) = true →
          (¬ d ∈ bad → (reports d).getD false = x))
        (some_getD (complete d m)).symm witness_true_iff.mp) (all d m),
     fun e d m => (Eq.subst (motive := fun o =>
        (¬ d ∈ bad → (reports d).getD false = x) →
          ((bad.contains d || o.isNone) || (o == some x)) = true)
        (some_getD (complete d m)).symm witness_true_iff.mpr) (e d m)⟩

theorem compatible_complete_iff {roster : List Nat} {faults : List (List Nat)} {x : Bool}
    {reports : FallibleInspection.Reports} (complete : ∀ d ∈ roster, reports d ≠ none) :
    FallibleInspection.compatible roster faults x reports = true ↔
      ∃ bad, bad ∈ faults ∧ Readout.Explains roster bad x fun d => (reports d).getD false :=
  list_any_true_iff.trans
    ⟨fun ⟨b, m, e⟩ => ⟨b, m, (explains_complete_iff complete).mp e⟩,
     fun ⟨b, m, e⟩ => ⟨b, m, (explains_complete_iff complete).mpr e⟩⟩

/-- **`complete_diagnosability_iff_cross_separation` through the core**: on complete reports,
compatibility is the core's explanation under an admitted fault set, and cross-separation is a
common faithful witness for every two of them, so the theorem is
`Readout.no_common_report_envelopes_iff`. -/
theorem complete_diagnosability_iff_by_core (roster : List Nat) (fa fb : List (List Nat))
    (x y : Bool) (different : x ≠ y) :
    (∀ reports : FallibleInspection.Reports, (∀ d ∈ roster, reports d ≠ none) →
      FallibleInspection.compatible roster fa x reports = true →
        FallibleInspection.compatible roster fb y reports = false) ↔
      FallibleInspection.CrossSeparated roster fa fb :=
  Iff.trans
    ⟨fun apart (report : Nat → Bool) first second =>
      have complete : ∀ d ∈ roster, (fun d => some (report d)) d ≠ none :=
        fun d _ (h : some (report d) = none) => nomatch h
      Bool.noConfusion ((apart _ complete ((compatible_complete_iff complete).mpr first)).symm.trans
        ((compatible_complete_iff complete).mpr second)),
     fun apart reports complete first => match h : FallibleInspection.compatible roster fb y reports with
      | false => rfl
      | true => absurd ((compatible_complete_iff complete).mp h)
          (apart _ ((compatible_complete_iff complete).mp first))⟩
    (Readout.no_common_report_envelopes_iff different)

end FallibleWitnesses

/-! ## Return and traces -/

section ReturnAndTraces

variable {S : Type u} {A : Type v}

/-- Keeping every possibility is keeping every reachable configuration. -/
theorem keeps_possible_iff_keeps_reach {P : Process S A} {s t : S} :
    (∀ q, BecomingReversibility.Possible P s q → BecomingReversibility.Possible P t q) ↔
      ∀ u, Reach P s u → Reach P t u :=
  ⟨fun keeps u there => match keeps (fun r => r = u) ⟨u, there, rfl⟩ with
    | ⟨_, reach, same⟩ => Eq.subst (motive := fun v => Reach P t v) same reach,
   fun keeps _ ⟨r, there, holds⟩ => ⟨r, keeps r there, holds⟩⟩

/-- **`same_endpoint_possibilities_iff_return` through the core**: `same_reach_iff_returns`. -/
theorem same_endpoint_possibilities_iff_return_by_core {P : Process S A} {s t : S}
    (onward : Reach P s t) :
    (∀ q, BecomingReversibility.Possible P s q ↔ BecomingReversibility.Possible P t q) ↔
      Reach P t s :=
  Iff.trans
    ⟨fun same => keeps_possible_iff_keeps_reach.mp fun q => (same q).mp,
     fun back q => ⟨keeps_possible_iff_keeps_reach.mpr back q,
       fun ⟨r, there, holds⟩ => ⟨r, onward.trans there, holds⟩⟩⟩
    keeps_reach_iff_returns

/-- **`irreversible_iff_endpoint_loss` through the core**: `not_returns_iff_loses`, the lost
configuration read as the possibility of being there. -/
theorem irreversible_iff_endpoint_loss_by_core {P : Process S A} {s t : S} :
    ¬ Reach P t s ↔
      ∃ q, BecomingReversibility.Possible P s q ∧ ¬ BecomingReversibility.Possible P t q :=
  Iff.trans not_returns_iff_loses
    ⟨fun ⟨u, there, lost⟩ => ⟨fun r => r = u, ⟨u, there, rfl⟩, fun ⟨_, reach, same⟩ =>
        lost (Eq.subst (motive := fun v => Reach P t v) same reach)⟩,
     fun ⟨_, ⟨r, there, holds⟩, lost⟩ => ⟨r, there, fun reach => lost ⟨r, reach, holds⟩⟩⟩

/-- **`same_steps_iff_endpoint_traces` through the core**: `same_steps_iff_traces`. -/
theorem same_steps_iff_endpoint_traces_by_core (P Q : Process S A) :
    Generative.Deeper.SameSteps P Q ↔ ∀ s (word : List A) t, Trace P s word t ↔ Trace Q s word t :=
  same_steps_iff_traces

end ReturnAndTraces

/-! ## The derived history law through the core -/

section DerivedHistory

variable {A : Type u} {C : Type v}

/-- The admitted histories of a language, each step adding one move. -/
def admittedProcess (L : List A → Prop) : Process {h : List A // L h} A :=
  ⟨fun h a h' => h'.1 = h.1 ++ [a]⟩

theorem admitted_feasible_iff {L : List A → Prop} (closed : Generative.Deeper.PrefixClosed L) :
    ∀ {h : {h : List A // L h}} {word : List A},
      Feasible (admittedProcess L) h word ↔ L (h.1 ++ word)
  | h, [] => ⟨fun _ => Eq.subst (motive := L) (Generative.Deeper.append_nil_constructive h.1).symm h.2,
      fun _ => ⟨h, .nil h⟩⟩
  | h, a :: word =>
    ⟨fun ⟨_, .cons (step : _ = h.1 ++ [a]) rest⟩ =>
      Eq.subst (motive := L) (Generative.Deeper.append_assoc_constructive h.1 [a] word)
        (Eq.subst (motive := fun x => L (x ++ word)) step
          (admitted_feasible_iff closed |>.mp ⟨_, rest⟩)),
     fun holds =>
      have whole : L ((h.1 ++ [a]) ++ word) :=
        Eq.subst (motive := L) (Generative.Deeper.append_assoc_constructive h.1 [a] word).symm holds
      let ⟨t, rest⟩ := (admitted_feasible_iff closed (h := ⟨h.1 ++ [a], closed _ word whole⟩)).mpr whole
      ⟨t, .cons (show (admittedProcess L).step h a ⟨h.1 ++ [a], closed _ word whole⟩ from rfl) rest⟩⟩

/-- `derivedProcess` is the admitted histories' law read through the summary. -/
theorem derived_same_steps {L : List A → Prop} (q : List A → C) (k : C) (a : A) (k' : C) :
    (Generative.DerivedHistoryLaw.derivedProcess L q).step k a k' ↔
      (Readout.image (admittedProcess L) fun h => q h.1).step k a k' :=
  ⟨fun ⟨h, lh, here, la, there⟩ => ⟨⟨h, lh⟩, ⟨h ++ [a], la⟩, here, rfl, there⟩,
   fun ⟨h, t, here, (step : t.1 = h.1 ++ [a]), there⟩ =>
    ⟨h.1, h.2, here, Eq.subst (motive := L) step t.2,
      Eq.subst (motive := fun x => q x = k') step there⟩⟩

/-- **`exact_iff_fiber_future` through the core**: on the admitted histories the derived law is
the law read through the summary (`derived_same_steps`), so the theorem is
`Readout.futures_through_iff`. -/
theorem exact_iff_fiber_future_by_core (L : List A → Prop)
    (closed : Generative.Deeper.PrefixClosed L) (q : List A → C) :
    Generative.DerivedHistoryLaw.ExactFuture L q ↔ Generative.DerivedHistoryLaw.FiberFuture L q :=
  have traces := same_steps_iff_traces.mp (derived_same_steps q)
  have feasible : ∀ c word, Feasible (Generative.DerivedHistoryLaw.derivedProcess L q) c word ↔
      Feasible (Readout.image (admittedProcess L) fun h => q h.1) c word :=
    fun c word => ⟨fun ⟨t, path⟩ => ⟨t, (traces c word t).mp path⟩,
      fun ⟨t, path⟩ => ⟨t, (traces c word t).mpr path⟩⟩
  Iff.trans
    ⟨fun exact (h : {h : List A // L h}) word => (feasible _ word).symm.trans
        ((exact h.1 h.2 word).trans (admitted_feasible_iff closed).symm),
     fun exact h lh word => (feasible _ word).trans
        ((exact ⟨h, lh⟩ word).trans (admitted_feasible_iff closed (h := ⟨h, lh⟩)))⟩
    (Iff.trans Readout.futures_through_iff
      ⟨fun fibers (h k : List A) lh lk same word => (admitted_feasible_iff closed (h := ⟨h, lh⟩)).symm.trans
          ((fibers ⟨h, lh⟩ ⟨k, lk⟩ same word).trans (admitted_feasible_iff closed)),
       fun fibers (h k : {h : List A // L h}) same word => (admitted_feasible_iff closed).trans
          ((fibers h.1 k.1 h.2 k.2 same word).trans (admitted_feasible_iff closed).symm)⟩)

end DerivedHistory


/-! ## Laws in context -/

section ContextCoherence

/-- **`pooling_exact_iff_join_closed` through the core**: `pooledLaw_exact_iff_joinClosed`. -/
theorem pooling_exact_iff_join_closed_by_core {I : Type u} {S : Type v} {A : Type w}
    (family : I → Process S A) (seed : I) :
    (∀ s word t, Trace (BecomingCompatibility.pooled family) s word t ↔
        BecomingCompatibility.InOne family s word t) ↔
      BecomingCompatibility.JoinClosed family :=
  pooledLaw_exact_iff_joinClosed seed

/-- **`retained_realizes_union` through the core**: `retainedLaw_realizes_inOne`. -/
theorem retained_realizes_union_by_core {I : Type u} {S : Type v} {A : Type w}
    (family : I → Process S A) (s : S) (word : List A) (t : S) :
    (∃ i j, Trace (BecomingCompatibility.retained family) (i, s) word (j, t)) ↔
      BecomingCompatibility.InOne family s word t :=
  retainedLaw_realizes_inOne

/-- **`erasure_exact_iff_context_lifting` through the core**: `erasedLaw_exact_iff_lifts`, the
foundation's `projection_exact_iff` read along `Prod.snd`. -/
theorem erasure_exact_iff_context_lifting_by_core {I : Type u} {S : Type v} {A : Type w}
    (R : I → S → A → I → S → Prop) :
    (∀ i s a t, (∃ j k, R j s a k t) → ∃ k, R i s a k t) ↔
      (∀ i s word t, Trace (BecomingCompatibility.eraseContext R) s word t ↔
        ∃ j, Trace (BecomingCompatibility.evolving R) (i, s) word (j, t)) :=
  erasedLaw_exact_iff_lifts R

/-- **`arrivals_append` through the core**: `arrives_append`. -/
theorem arrivals_append_by_core {I : Type u} {S : Type v} {A : Type w}
    (R : I → S → A → I → S → Prop) (initial : I → Prop) (s : S) (xs ys : List A) (t : S)
    (k : I) :
    BecomingCompatibility.Arrives R initial s (xs ++ ys) t k ↔
      ∃ m, BecomingCompatibility.Arrives R
        (BecomingCompatibility.Arrives R initial s xs m) m ys t k :=
  arrives_append

/-- **`arrivals_snoc` through the core**: `arrives_snoc`. -/
theorem arrivals_snoc_by_core {I : Type u} {S : Type v} {A : Type w}
    (R : I → S → A → I → S → Prop) (initial : I → Prop) (s : S) (word : List A) (a : A) (t : S)
    (j : I) :
    BecomingCompatibility.Arrives R initial s (word ++ [a]) t j ↔
      ∃ m, BecomingCompatibility.Advance R
        (BecomingCompatibility.Arrives R initial s word m) m a t j :=
  arrives_snoc

/-- **`no_single_context_supports_crossing` through the core**: `CrossingContexts.not_inOne`. -/
theorem no_single_context_supports_crossing_by_core :
    ¬ BecomingCompatibility.InOne BecomingCompatibility.splitFamily 0 [(), ()] 2 :=
  CrossingContexts.not_inOne

/-- **`actual_context_change_joins_history` through the core**: `ChangingContext.joins`. -/
theorem actual_context_change_joins_history_by_core :
    Trace (BecomingCompatibility.evolving BecomingCompatibility.changingRelation) (false, 0)
      [(), ()] (true, 2) :=
  ChangingContext.joins

/-- **`changed_history_really_ends` through the core**: `ChangingContext.ends`, with an empty
axiom report. -/
theorem changed_history_really_ends_by_core (j : Bool) (t : Nat) :
    ¬ BecomingCompatibility.changingRelation true 2 () j t :=
  ChangingContext.ends j t

end ContextCoherence


/-! ## Realized together within a bound -/

section JointActivation

open JointContinuationClassification

/-- **`within_after_prefix` through the core**: `WithinMoves.after_course`. -/
theorem within_after_prefix_by_core {S : Type u} {A : Type v} {C : Type w} {P : Process S A}
    {realized : S → C → Prop} {s t : S} {earlierWord : List A} {n : Nat} {bundle : C → Prop}
    (path : Trace P s earlierWord t) (next : RelationalBecoming.Within P realized t n bundle) :
    RelationalBecoming.Within P realized s (earlierWord.length + n) bundle :=
  WithinMoves.after_course path next

/-- **`eventual_after_prefix` through the core**: `together_after_reach`. -/
theorem eventual_after_prefix_by_core {S : Type u} {A : Type v} {C : Type w} {P : Process S A}
    {realized : S → C → Prop} {s t : S} {earlierWord : List A} {bundle : C → Prop}
    (path : Trace P s earlierWord t) (next : RelationalBecoming.Eventually P realized t bundle) :
    RelationalBecoming.Eventually P realized s bundle :=
  together_after_reach ⟨earlierWord, path⟩ next

/-- The joint content of the activation law is the configuration with both active. -/
theorem joint_content_both {s : Configuration}
    (content : ∀ c, RelationalBecoming.both c → RelationalBecoming.realized s c) :
    s = .bothActive :=
  match content .leftRealized True.intro, content .rightRealized True.intro with
  | .inl left, .inl right => Configuration.noConfusion (left.symm.trans right)
  | _, .inr both => both
  | .inr both, _ => both

/-- Configurations past the release: released, or one side active. -/
def PastRelease (s : Configuration) : Prop :=
  s = .released ∨ s = .leftActive ∨ s = .rightActive

theorem PastRelease.step {s m : Configuration} {a : Event} (step : Step s a m)
    (past : PastRelease s) : PastRelease m :=
  match step, past with
  | .retainCoupling, .inl e => Configuration.noConfusion e
  | .retainCoupling, .inr (.inl e) => Configuration.noConfusion e
  | .retainCoupling, .inr (.inr e) => Configuration.noConfusion e
  | .releaseCoupling, .inl e => Configuration.noConfusion e
  | .releaseCoupling, .inr (.inl e) => Configuration.noConfusion e
  | .releaseCoupling, .inr (.inr e) => Configuration.noConfusion e
  | .activateLeftCoupled, .inl e => Configuration.noConfusion e
  | .activateLeftCoupled, .inr (.inl e) => Configuration.noConfusion e
  | .activateLeftCoupled, .inr (.inr e) => Configuration.noConfusion e
  | .activateRightCoupled, .inl e => Configuration.noConfusion e
  | .activateRightCoupled, .inr (.inl e) => Configuration.noConfusion e
  | .activateRightCoupled, .inr (.inr e) => Configuration.noConfusion e
  | .activateTogether, .inl e => Configuration.noConfusion e
  | .activateTogether, .inr (.inl e) => Configuration.noConfusion e
  | .activateTogether, .inr (.inr e) => Configuration.noConfusion e
  | .activateLeftReleased, _ => .inr (.inl rfl)
  | .activateRightReleased, _ => .inr (.inr rfl)

theorem PastRelease.trace : ∀ {s t : Configuration} {word : List Event},
    Trace RelationalBecoming.process s word t → PastRelease s → PastRelease t
  | _, _, _, .nil _, past => past
  | _, _, _, .cons step path, past => PastRelease.trace path (PastRelease.step step past)

theorem PastRelease.not_both : ¬ PastRelease .bothActive
  | .inl e => Configuration.noConfusion e
  | .inr (.inl e) => Configuration.noConfusion e
  | .inr (.inr e) => Configuration.noConfusion e

theorem prepared_joint_within_one_by_core :
    RelationalBecoming.Within RelationalBecoming.process RelationalBecoming.realized .coupled 1
      RelationalBecoming.both :=
  ⟨[.activateTogether], .bothActive, trace_singleton_iff.mpr Step.activateTogether, Nat.le_refl _,
   fun c _ => match c with
     | .leftRealized => Or.inr rfl
     | .rightRealized => Or.inr rfl⟩

theorem initial_not_joint_within_one_by_core :
    ¬ RelationalBecoming.Within RelationalBecoming.process RelationalBecoming.realized .initial 1
      RelationalBecoming.both
  | ⟨word, _, path, short, content⟩ =>
    have path : Trace RelationalBecoming.process .initial word .bothActive :=
      Eq.subst (motive := fun x => Trace RelationalBecoming.process .initial word x)
        (joint_content_both content) path
    match word, path, short with
    | [], path, _ => nomatch path
    | [_], .cons step (.nil _), _ => nomatch step
    | _ :: _ :: _, _, short => Nat.not_succ_le_zero _ (Nat.le_of_succ_le_succ short)

/-- **`actual_preparation_changes_effective_capacity` through the core.** -/
theorem actual_preparation_changes_effective_capacity_by_core :
    Trace RelationalBecoming.process .initial [.retain] .coupled ∧
    ¬ RelationalBecoming.Within RelationalBecoming.process RelationalBecoming.realized .initial 1
      RelationalBecoming.both ∧
    RelationalBecoming.Within RelationalBecoming.process RelationalBecoming.realized .coupled 1
      RelationalBecoming.both ∧
    RelationalBecoming.Within RelationalBecoming.process RelationalBecoming.realized .initial 2
      RelationalBecoming.both :=
  ⟨trace_singleton_iff.mpr Step.retainCoupling, initial_not_joint_within_one_by_core,
   prepared_joint_within_one_by_core,
   WithinMoves.after_course (trace_singleton_iff.mpr Step.retainCoupling)
     prepared_joint_within_one_by_core⟩

/-- **`released_cannot_reach_joint` through the core.** -/
theorem released_cannot_reach_joint_by_core :
    ¬ RelationalBecoming.Eventually RelationalBecoming.process RelationalBecoming.realized
      .released RelationalBecoming.both
  | ⟨_, _, _, path, _, content⟩ =>
    PastRelease.not_both (Eq.subst (motive := PastRelease) (joint_content_both content)
      (PastRelease.trace path (.inl rfl)))

/-- **`actual_release_loses_eventual_joint` through the core**: the core's
`lost_together_not_returns` reads it as a course with no way back. -/
theorem actual_release_loses_eventual_joint_by_core :
    Trace RelationalBecoming.process .initial [.release] .released ∧
    RelationalBecoming.Eventually RelationalBecoming.process RelationalBecoming.realized .initial
      RelationalBecoming.both ∧
    ¬ RelationalBecoming.Eventually RelationalBecoming.process RelationalBecoming.realized
      .released RelationalBecoming.both :=
  ⟨trace_singleton_iff.mpr Step.releaseCoupling,
   ⟨2, actual_preparation_changes_effective_capacity_by_core.2.2.2⟩,
   released_cannot_reach_joint_by_core⟩

/-- Releasing the coupling has no way back. -/
theorem release_not_returns :
    ¬ Reach RelationalBecoming.process .released .initial :=
  lost_together_not_returns (realized := RelationalBecoming.realized)
    (bundle := RelationalBecoming.both)
    actual_release_loses_eventual_joint_by_core.2.1 actual_release_loses_eventual_joint_by_core.2.2

/-- **`prepared_capacity_can_end_without_joint_realization` through the core.** -/
theorem prepared_capacity_can_end_without_joint_realization_by_core :
    Trace RelationalBecoming.process .initial [.retain, .activateLeft] .leftActive ∧
    RelationalBecoming.Within RelationalBecoming.process RelationalBecoming.realized .coupled 1
      RelationalBecoming.both ∧
    ¬ RelationalBecoming.realized .leftActive .rightRealized ∧
    (∀ a, ¬ Enabled RelationalBecoming.process .leftActive a) :=
  ⟨.cons Step.retainCoupling (.cons Step.activateLeftCoupled (.nil _)),
   prepared_joint_within_one_by_core,
   fun h => match h with
     | .inl e => Configuration.noConfusion e
     | .inr e => Configuration.noConfusion e,
   fun _ ⟨_, step⟩ => nomatch step⟩

end JointActivation


/-! ## Comparison under every classification of fresh contents -/

section ClassificationRobust

/-- Strict preference with every fresh content basic retains the fresh contents. -/
theorem compared_retains {H C G N : Type} {p : H → C → Prop} {g : H → G → Prop}
    {f : H → N → Prop} {a b : H}
    (h : ClassificationRobustJudgment.compared p g f (fun _ => True) a b) :
    PracticalJudgment.Included (f b) (f a) :=
  fun n fb => match h with
    | .inl strict => (strict.1 (.inr n) ⟨fb, True.intro⟩).1
    | .inr ⟨forward, _, _⟩ => (forward (.inr n) ⟨fb, True.intro⟩).1

/-- Strict preference with every fresh content secondary is preference with the fresh contents
added as gains. -/
theorem compared_secondary {H C G N : Type} {p : H → C → Prop} {g : H → G → Prop}
    {f : H → N → Prop} {a b : H}
    (h : ClassificationRobustJudgment.compared p g f (fun _ => False) a b) :
    PracticalJudgment.Better p (ConcernExtension.extend g f) a b :=
  match h with
  | .inl ⟨forward, notBack⟩ =>
    .inl ⟨fun c pb => forward (.inl c) pb,
      fun back => notBack fun i => match i with
        | .inl c => back c
        | .inr _ => fun held => held.2.elim⟩
  | .inr ⟨forward, back, gainForward, gainNotBack⟩ =>
    .inr ⟨fun c pb => forward (.inl c) pb, fun c pa => back (.inl c) pa,
      fun i => match i with
        | .inl x => gainForward (.inl x)
        | .inr n => fun fb => (gainForward (.inr n) ⟨fb, fun no => no⟩).1,
      fun gainBack => gainNotBack fun i => match i with
        | .inl x => gainBack (.inl x)
        | .inr n => fun held => ⟨gainBack (.inr n) held.1, held.2⟩⟩

/-- With excluded middle, retaining the fresh contents and being better with them secondary gives
strict preference under every classification. -/
theorem compared_of_em (em : ∀ p : Prop, Decided p) {H C G N : Type} {p : H → C → Prop}
    {g : H → G → Prop} {f : H → N → Prop} {a b : H}
    (fresh : PracticalJudgment.Included (f b) (f a))
    (old : PracticalJudgment.Better p (ConcernExtension.extend g f) a b) (q : N → Prop) :
    ClassificationRobustJudgment.compared p g f q a b :=
  match old with
  | .inl ⟨forward, notBack⟩ =>
    .inl ⟨fun i => match i with
        | .inl c => forward c
        | .inr n => fun held => ⟨fresh n held.1, held.2⟩,
      fun back => notBack fun c => back (.inl c)⟩
  | .inr ⟨pba, _, gainForward, gainNotBack⟩ =>
    have forward : PracticalJudgment.Included (ClassificationRobustJudgment.classifiedBasic p f q b)
        (ClassificationRobustJudgment.classifiedBasic p f q a) := fun i => match i with
      | .inl c => pba c
      | .inr n => fun held => ⟨fresh n held.1, held.2⟩
    match em (PracticalJudgment.Included (ClassificationRobustJudgment.classifiedBasic p f q a)
        (ClassificationRobustJudgment.classifiedBasic p f q b)) with
    | .inl back =>
      .inr ⟨forward, back,
        fun i => match i with
          | .inl x => gainForward (.inl x)
          | .inr n => fun held => ⟨fresh n held.1, held.2⟩,
        fun gainBack => gainNotBack fun i => match i with
          | .inl x => gainBack (.inl x)
          | .inr n => fun fa => match em (q n) with
            | .inl qn => (back (.inr n) ⟨fa, qn⟩).1
            | .inr nq => (gainBack (.inr n) ⟨fa, nq⟩).1⟩
    | .inr notBack => .inl ⟨forward, notBack⟩

/-- **`classification_robust_iff` with excluded middle as a named hypothesis.** -/
theorem classification_robust_iff_of_em (em : ∀ p : Prop, Decided p) {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H) :
    (∀ q, ClassificationRobustJudgment.compared p g f q a b) ↔
      PracticalJudgment.Included (f b) (f a) ∧
        PracticalJudgment.Better p (ConcernExtension.extend g f) a b :=
  ⟨fun robust => ⟨compared_retains (robust _), compared_secondary (robust _)⟩,
   fun ⟨fresh, old⟩ q => compared_of_em em fresh old q⟩

/-- **`two_extremes_suffice` with excluded middle as a named hypothesis.** -/
theorem two_extremes_suffice_of_em (em : ∀ p : Prop, Decided p) {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H) :
    (∀ q, ClassificationRobustJudgment.compared p g f q a b) ↔
      ClassificationRobustJudgment.compared p g f (fun _ => False) a b ∧
        ClassificationRobustJudgment.compared p g f (fun _ => True) a b :=
  ⟨fun robust => ⟨robust _, robust _⟩,
   fun ⟨secondary, basic⟩ q => compared_of_em em (compared_retains basic)
     (compared_secondary secondary) q⟩

/-- **Excluded middle is exactly what the robust comparison needs.** That strict preference under
every classification follows from retaining the fresh contents and being better with them
secondary, for all types, holds exactly where every proposition is decided: with `a = true`,
`b = false`, one fresh content held at `true` and, at `false`, exactly where `R` holds, and one
gain held only at `true`, the preference under the classification making the fresh content basic
is `R` or its failure. -/
theorem classification_robust_iff_iff_em :
    (∀ (H C G N : Type) (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H),
      (∀ q, ClassificationRobustJudgment.compared p g f q a b) ↔
        PracticalJudgment.Included (f b) (f a) ∧
          PracticalJudgment.Better p (ConcernExtension.extend g f) a b) ↔
      ∀ R : Prop, Decided R :=
  ⟨fun robust R =>
    match (robust Bool Unit Unit Unit (fun _ _ => True) (fun h _ => h = true)
        (fun h _ => h = true ∨ R) true false).mpr
        ⟨fun _ _ => Or.inl rfl,
         .inr ⟨fun _ _ => True.intro, fun _ _ => True.intro,
           ⟨fun i => match i with
              | .inl _ => fun no => Bool.noConfusion no
              | .inr _ => fun _ => Or.inl rfl,
            fun back => Bool.noConfusion (back (.inl ()) rfl)⟩⟩⟩
        (fun _ => True) with
    | .inl ⟨_, notBack⟩ =>
      .inr fun r => notBack fun i => match i with
        | .inl _ => fun _ => True.intro
        | .inr _ => fun _ => ⟨Or.inr r, True.intro⟩
    | .inr ⟨_, back, _⟩ =>
      match (back (.inr ()) ⟨Or.inl rfl, True.intro⟩).1 with
      | .inl no => Bool.noConfusion no
      | .inr r => .inl r,
   fun em _ _ _ _ p g f a b => classification_robust_iff_of_em em p g f a b⟩

end ClassificationRobust


/-! ## Derivation over the scope of an inquiry -/

section DerivationOverScope

variable {S A R Index : Type} {k : Nat} {P : Process S A} {sense : S → A → S → Fin k}
  {response : R → List A} {B : S → Prop} {policy : Policy A R k}
  {basis : Index → InquiryRoot.Formula S}

/-- **Derived claims hold over the scope where the basis does.** -/
theorem derivation_sound_on_scope
    (rootHolds : ∀ i, InquiryRoot.Necessary (Scope P sense response B policy) (basis i)) :
    ∀ q, InquiryRoot.Derives basis [] q → InquiryRoot.Necessary (Scope P sense response B policy) q :=
  InquiryRoot.all_closed_descendants_necessary rootHolds

/-- **The whole closure holds over the scope exactly where its basis does.** -/
theorem closure_over_scope_iff_basis :
    (∀ q, InquiryRoot.Derives basis [] q →
        InquiryRoot.Necessary (Scope P sense response B policy) q) ↔
      ∀ i, InquiryRoot.Necessary (Scope P sense response B policy) (basis i) :=
  InquiryRoot.entire_closure_necessary_iff_basis

/-- **Every claim derived from a sound policy's goal holds over its scope.** -/
theorem sound_goal_closure {safe : S → A → S → Prop} {goal : S → Prop}
    (sound : Sound P safe goal sense response policy B) :
    ∀ q, InquiryRoot.Derives (fun _ : Unit => goal) [] q →
      InquiryRoot.Necessary (Scope P sense response B policy) q :=
  derivation_sound_on_scope fun _ t inScope => Scope.secures sound t inScope

/-- **With a finite basis, each derived claim realized somewhere in the scope is one
configuration of the scope realizing them all.** -/
theorem common_on_scope_iff (indices : List Index) (covers : ∀ i, i ∈ indices) :
    (∀ q, InquiryRoot.Derives basis [] q → ∃ t, Scope P sense response B policy t ∧ q t) ↔
      ∃ t, Scope P sense response B policy t ∧ ∀ q, InquiryRoot.Derives basis [] q → q t :=
  InquiryRoot.JointInterpretation.pointwise_closure_iff_common basis indices covers _

end DerivationOverScope

end Becoming
