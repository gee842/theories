import GenerativeComparison

/-!
# Self-good, formed relations and the reach of generative significance

One unfolding. An evaluating position is a formation within it, not a primitive
owner. `Gen` indexes occurrences of living and further generation in a
continuation; `Prof` describes the formed relations of an occurrence to this
evaluating (organizational continuity, formative contribution, dependence ...).
"Own" is therefore not a primitive index: it is a region of those formed
relations. The assignment `sig` is this standpoint's reason-giving positive
significance: contributory, not weight, permission or duty.

Supplied, and kept visible:
* `SelfGood` (S0): the evaluator's own living and further generation is
  reason-giving for it. S0 and `Tolerant` are the substantive normative
  premises. "Further generation" includes the evaluator's own learning and
  transformation; others formed through its activity are not part of S0's
  content (`ownOcc .formedOther` is false) and are reached, if at all, by step one.
* `Monotone`: for the same content, an occurrence at least as connected in the
  relations that ground the evaluator's self-good is at least as significant.
  It is unrestricted, ranging over own and other occurrences; a rival's own
  near-over-far principle ranges over own occurrences only. The unrestricted form
  amounts to supervenience, a profile-monotone valuation and boundary
  irrelevance (BI: the grounding profile has no own-region coordinate), a
  contested structural premise.
* `Supervenes`: significance of living content depends only on formed relations.
  This is a normative supervenience thesis, not entailed by the monist ontology;
  it allows profiles with a formed closure coordinate.
* `Tolerant`: an indiscernibly small relational step does not turn positive
  significance into none. A contested rationality premise; a threshold rival
  rejects it, and the countermodel below keeps that rival consistent. On a
  connected profile space, two-valued universal tolerance makes positive
  significance constant, including on zero-relation profiles, and it carries
  "none" backward as readily as "positive" forward.
* Differentiation and chain premises are correspondence claims about the
  actual unfolding. Differentiation is in scope for fission, copying, forking and
  successors and for evaluation led by formative contribution. `Chain` ranges
  over possible profiles, so tolerance is also a claim about valuing merely
  possible profiles.

No theorem here proves S0, `Tolerant`, BI or the correspondence premises. A
present-aim evaluator without S0 remains a consistent formation. The derived G0
is a standpoint-indexed, single-history instance of the G0 predicate; the
unindexed G0 over continuations needs a further bridge, stated as standpoint
neutrality in `becoming/MetaethicalCore.lean`.
-/

namespace EvaluatorGrounding

open GenerativeComparison

structure Standpoint (Gen Prof : Type) where
  prof : Gen → Prof
  own : Gen → Prop
  living : Gen → Prop
  reach : Gen → Prop
  sig : Gen → Prop

variable {Gen Prof : Type}

def SelfGood (s : Standpoint Gen Prof) : Prop :=
  ∀ g, s.own g → s.living g → s.sig g

def Monotone (s : Standpoint Gen Prof) (atLeast : Prof → Prof → Prop) : Prop :=
  ∀ g g', s.living g → s.living g' → atLeast (s.prof g) (s.prof g') → s.sig g → s.sig g'

def Supervenes (s : Standpoint Gen Prof) (val : Prof → Prop) : Prop :=
  ∀ g, s.living g → (s.sig g ↔ val (s.prof g))

def Tolerant (val : Prof → Prop) (step : Prof → Prof → Prop) : Prop :=
  ∀ p q, step p q → val p → val q

/-- Finite chains of small formed-relation differences. -/
inductive Chain (step : Prof → Prof → Prop) : Prof → Prof → Prop
  | refl (p : Prof) : Chain step p p
  | tail {p q r : Prof} : Chain step p q → step q r → Chain step p r

/-- Self-transcendence: self-good together with the rival's own monotonicity gives
significance to any living occurrence at least as connected as some valued
occurrence of the evaluator's own further generation. No tolerance is used. -/
theorem self_good_reaches_at_least_as_connected
    (s : Standpoint Gen Prof) (atLeast : Prof → Prof → Prop)
    (self : SelfGood s) (mono : Monotone s atLeast)
    {g g' : Gen} (ownG : s.own g) (livingG : s.living g) (livingG' : s.living g')
    (connected : atLeast (s.prof g) (s.prof g')) : s.sig g' :=
  mono g g' livingG livingG' connected (self g ownG livingG)

/-- The strictly indexed rival (significance only for its own occurrences) cannot
also hold self-good and monotonicity once its own further generation includes an
occurrence that another living occurrence is at least as connected as. -/
theorem strict_indexed_rival_inconsistent
    (s : Standpoint Gen Prof) (atLeast : Prof → Prof → Prop)
    (self : SelfGood s) (mono : Monotone s atLeast)
    (onlyOwn : ∀ g, s.sig g → s.own g)
    (differentiates : ∃ g g', s.own g ∧ s.living g ∧ s.living g' ∧ ¬ s.own g' ∧
      atLeast (s.prof g) (s.prof g')) : False := by
  obtain ⟨g, g', ownG, livingG, livingG', other, connected⟩ := differentiates
  exact other (onlyOwn g'
    (self_good_reaches_at_least_as_connected s atLeast self mono ownG livingG livingG' connected))

theorem chain_preserves (val : Prof → Prop) (step : Prof → Prof → Prop)
    (tol : Tolerant val step) {p q : Prof} (chain : Chain step p q) (start : val p) : val q := by
  induction chain with
  | refl => exact start
  | tail _ last ih => exact tol _ _ last ih

/-- Reach: with supervenience, tolerance and graded connection from valued own
generation, every reachable living occurrence has significance from this standpoint. -/
theorem tolerant_chain_reaches
    (s : Standpoint Gen Prof) (val : Prof → Prop) (step : Prof → Prof → Prop)
    (sup : Supervenes s val) (self : SelfGood s) (tol : Tolerant val step)
    (chain : ∀ g', s.reach g' → s.living g' →
      ∃ g, s.own g ∧ s.living g ∧ Chain step (s.prof g) (s.prof g')) :
    ∀ g', s.reach g' → s.living g' → s.sig g' := by
  intro g' reached living'
  obtain ⟨g, ownG, livingG, linked⟩ := chain g' reached living'
  have start : val (s.prof g) := (sup g livingG).1 (self g ownG livingG)
  exact (sup g' living').2 (chain_preserves val step tol linked start)

/-- The reachable generation of one continuation, read through the existing G0 interface. -/
def reachableInventory (s : Standpoint Gen Prof) : Inventory Unit Gen where
  realized := fun _ g => s.reach g
  generative := s.living

/-- The reached conclusion is exactly the existing G0 predicate for that inventory,
with this standpoint's significance as positive relevance. -/
theorem reach_is_g0 (s : Standpoint Gen Prof) :
    (∀ g', s.reach g' → s.living g' → s.sig g') ↔
      G0 (reachableInventory s) (fun _ g => s.sig g) := by
  constructor
  · intro reached _ g living realized
    exact reached g realized living
  · intro g0 g reached living
    exact g0 () g living reached

theorem self_good_derives_reachable_g0
    (s : Standpoint Gen Prof) (val : Prof → Prop) (step : Prof → Prof → Prop)
    (sup : Supervenes s val) (self : SelfGood s) (tol : Tolerant val step)
    (chain : ∀ g', s.reach g' → s.living g' →
      ∃ g, s.own g ∧ s.living g ∧ Chain step (s.prof g) (s.prof g')) :
    G0 (reachableInventory s) (fun _ g => s.sig g) :=
  (reach_is_g0 s).1 (tolerant_chain_reaches s val step sup self tol chain)

/-! ## A finite unfolding and its boundaries

Degrees of formed connection to this evaluating. `changedSelf` is the evaluator's
own transformed further generation; `formedOther` is another life formed through
this activity and at least as connected; `stranger` is reachable but weakly
connected; `beyond` is not reachable. Numbers are illustrative orderings only. -/

inductive Occ where
  | nearSelf | changedSelf | formedOther | stranger | beyond
  deriving DecidableEq

def degree : Occ → Nat
  | .nearSelf => 9
  | .changedSelf => 4
  | .formedOther => 5
  | .stranger => 1
  | .beyond => 0

def ownOcc : Occ → Prop
  | .nearSelf | .changedSelf => True
  | _ => False

def reachOcc : Occ → Prop
  | .beyond => False
  | _ => True

def adjacent (p q : Nat) : Prop := q + 1 = p ∨ p + 1 = q

def standpoint (val : Nat → Prop) : Standpoint Occ Nat where
  prof := degree
  own := ownOcc
  living := fun _ => True
  reach := reachOcc
  sig := fun g => val (degree g)

/-- Any monotone self-good standpoint in this unfolding gives the formed other significance. -/
theorem formed_other_has_significance (val : Nat → Prop)
    (self : SelfGood (standpoint val))
    (mono : Monotone (standpoint val) (· ≤ ·)) :
    (standpoint val).sig .formedOther :=
  self_good_reaches_at_least_as_connected (standpoint val) (· ≤ ·) self mono
    (g := .changedSelf) trivial trivial trivial (show 4 ≤ 5 by decide)

/-- Threshold rival: self-good, monotone and supervenient; it reaches the formed
other, not the stranger, and violates tolerance exactly at its cut. -/
theorem threshold_rival_is_consistent_without_tolerance :
    SelfGood (standpoint (4 ≤ ·)) ∧ Monotone (standpoint (4 ≤ ·)) (· ≤ ·) ∧
    Supervenes (standpoint (4 ≤ ·)) (4 ≤ ·) ∧
    (standpoint (4 ≤ ·)).sig .formedOther ∧ ¬ (standpoint (4 ≤ ·)).sig .stranger ∧
    ¬ Tolerant (4 ≤ ·) adjacent := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro g own _
    cases g <;> simp_all [standpoint, ownOcc, degree]
  · intro g g' _ _ le held
    exact Nat.le_trans held le
  · intro g _
    exact Iff.rfl
  · show 4 ≤ 5
    decide
  · show ¬ 4 ≤ 1
    decide
  · intro tol
    have := tol 4 3 (Or.inl rfl) (Nat.le_refl 4)
    omega

/-- With tolerance along adjacent degrees, the same self-good reaches every
reachable occurrence, including the stranger. The same premises also give
`sig .beyond`, since degree 0 is adjacent to 1: the `reach` field limits what
this theorem states, not what tolerance implies. -/
theorem tolerant_standpoint_reaches_stranger (val : Nat → Prop)
    (self : SelfGood (standpoint val)) (tol : Tolerant val adjacent) :
    (standpoint val).sig .stranger ∧ (standpoint val).sig .formedOther := by
  have four : val 4 := self .changedSelf trivial trivial
  have three : val 3 := tol 4 3 (Or.inl rfl) four
  have two : val 2 := tol 3 2 (Or.inl rfl) three
  have one : val 1 := tol 2 1 (Or.inl rfl) two
  have five : val 5 := tol 4 5 (Or.inr rfl) four
  exact ⟨one, five⟩

/-- Present-aim evaluator: no reason-giving self-good. It satisfies monotonicity,
supervenience and tolerance and assigns no significance anywhere. Universality
over every possible evaluator is therefore not derived. -/
theorem present_aim_evaluator_escapes :
    ¬ SelfGood (standpoint (fun _ => False)) ∧
    Monotone (standpoint (fun _ => False)) (· ≤ ·) ∧
    Supervenes (standpoint (fun _ => False)) (fun _ => False) ∧
    Tolerant (fun _ => False) adjacent ∧
    ¬ (standpoint (fun _ => False)).sig .formedOther := by
  refine ⟨fun self => self .nearSelf trivial trivial, ?_, ?_, ?_, id⟩
  · intro _ _ _ _ _ held; exact held
  · intro _ _; exact Iff.rfl
  · intro _ _ _ held; exact held

/-- Closed self: if no small step crosses between own and other, tolerance holds
yet nothing reaches the stranger. This is the threshold rival with its step
relation restricted to its own positive region: `Chain` carries weight for that
step relation. Parfitian continuity and autopoietic closure are monist formations
with exactly this closed structure; it is not a dualist picture. -/
def closedStep (p q : Nat) : Prop := 4 ≤ p ∧ 4 ≤ q ∧ adjacent p q

theorem closed_self_blocks_reach :
    SelfGood (standpoint (4 ≤ ·)) ∧ Tolerant (4 ≤ ·) closedStep ∧
    ¬ (standpoint (4 ≤ ·)).sig .stranger := by
  refine ⟨threshold_rival_is_consistent_without_tolerance.1, ?_, ?_⟩
  · intro p q step _
    exact step.2.1
  · show ¬ 4 ≤ 1
    decide

/-! ## Persistence-grounded rival

If self-good is grounded in organizational persistence alone, profiles have two
dimensions: (organizational continuity, formative contribution). The formed other
is more formed by this activity yet less organizationally continuous than the
changed self, so the product order does not make it at least as connected. In
this profile, the product order makes no other occurrence at least as connected
as any own occurrence, for every standpoint; under a weighted sum the formed other
is at least as connected only if formative contribution has at least 7/5 the
weight of organizational continuity. Step one therefore binds generative
self-good led by formative contribution, not generative self-good as such. -/

def profile2 : Occ → Nat × Nat
  | .nearSelf => (9, 9)
  | .changedSelf => (8, 2)
  | .formedOther => (1, 7)
  | .stranger => (0, 1)
  | .beyond => (0, 0)

def productLe (p q : Nat × Nat) : Prop := p.1 ≤ q.1 ∧ p.2 ≤ q.2

def persistence : Standpoint Occ (Nat × Nat) where
  prof := profile2
  own := ownOcc
  living := fun _ => True
  reach := reachOcc
  sig := fun g => 5 ≤ (profile2 g).1

theorem persistence_rival_escapes_self_transcendence :
    SelfGood persistence ∧ Monotone persistence productLe ∧
    ¬ productLe (profile2 .changedSelf) (profile2 .formedOther) ∧
    ¬ persistence.sig .formedOther := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro g own _
    cases g <;> simp_all [persistence, ownOcc, profile2]
  · intro g g' _ _ le held
    exact Nat.le_trans held le.1
  · intro le
    have := le.1
    simp [profile2] at this
  · show ¬ 5 ≤ 1
    decide

end EvaluatorGrounding
