import GenerativeComparison
import PracticalJudgment
import JointContinuationClassification
import StandardsBridge

/-!
# Certain positive ground with open future form

The target is a positive aspect/reason at a stated visible future scope, not an
all-things-considered strict comparison. C and Better are absent. G0 supplies
positive relevance for genuinely realized generation. Direct articulation into
a contributory reason is an explicit supplied premise, not permission or duty.

Histories describe one arrangement's response and subsequent formation. The
response is the same in every branch; its new realization can vary with the
branch. Two remaining hypotheses concern its formation magnitude, while two
future branches concern which form becomes actual. These are distinct sources
of openness. Query access is explicitly retained by the local response law.

The finite signed sum is a unit-measure integral over distinct represented
relational occurrences, including a joint occurrence formed through retained
prior activity. Units, addition and sign-to-living-meaning correspondence are
local inputs, not a definition or universal scalarization of ethical goodness.
An explicit burden remains in the full representation; positive ground does
not require its disappearance. No infinite horizon or complete theory of all
future life is an application gate.
-/

namespace PositiveGroundUncertainty

open GenerativeComparison
open JointContinuationClassification
open Generative.StandardsBridge

def finiteIntegral {R : Type} : List R → (R → Int) → Int
  | [], _ => 0
  | r :: rs, contribution => contribution r + finiteIntegral rs contribution

/-- A positive finite signed integral has some positively contributing occurrence.
Its ethical meaning is not inferred from the numerical sign alone. -/
theorem positive_integral_has_positive_occurrence {R : Type}
    (domain : List R) (contribution : R → Int)
    (positive : 0 < finiteIntegral domain contribution) :
    ∃ r ∈ domain, 0 < contribution r := by
  induction domain with
  | nil => simp [finiteIntegral] at positive
  | cons r rs ih =>
    by_cases here : 0 < contribution r
    · exact ⟨r, by simp, here⟩
    · have rest : 0 < finiteIntegral rs contribution := by
        simp only [finiteIntegral] at positive
        omega
      obtain ⟨s, member, good⟩ := ih rest
      exact ⟨s, by simp [member], good⟩

/-- Quantifier order matters: one fixed response can secure some new positive
realization in each continuation without securing one fixed realization in all.
The response is already represented in `inventory`; it is not chosen per history.
-/
theorem contingent_generation_has_positive_ground {H Q : Type}
    (admitted : H → Prop) (before : H → Q → Prop)
    (inventory : Inventory H Q) (positive : H → Q → Prop)
    (g0 : G0 inventory positive)
    (formed : ∀ h, admitted h → ∃ q, inventory.generative q ∧
      inventory.realized h q ∧ ¬ before h q) :
    ∀ h, admitted h → ∃ q, positive h q ∧ ¬ before h q := by
  intro h allowed
  obtain ⟨q, generated, actual, new⟩ := formed h allowed
  exact ⟨q, g0 h q generated actual, new⟩

/-- An explicit direct articulation yields a contributory reason, without C,
global no-loss, an ordering, permission or a duty. -/
theorem certified_integral_supplies_contributory_reason {H Q R : Type}
    (admitted : H → Prop) (before : H → Q → Prop)
    (inventory : Inventory H Q) (positive : H → Q → Prop)
    (reason : H → Prop) (g0 : G0 inventory positive)
    (articulate : ∀ h q, positive h q → reason h)
    (domain : List R) (contribution : H → R → Int) (meaning : R → Q)
    (correspondence : ∀ h, admitted h → ∀ r ∈ domain, 0 < contribution h r →
      inventory.generative (meaning r) ∧ inventory.realized h (meaning r) ∧
        ¬ before h (meaning r))
    (certificate : ∀ h, admitted h → 0 < finiteIntegral domain (contribution h)) :
    ∀ h, admitted h → (∃ q, positive h q ∧ ¬ before h q) ∧ reason h := by
  have formed : ∀ h, admitted h → ∃ q, inventory.generative q ∧
      inventory.realized h q ∧ ¬ before h q := by
    intro h allowed
    obtain ⟨r, member, positive⟩ :=
      positive_integral_has_positive_occurrence domain (contribution h) (certificate h allowed)
    exact ⟨meaning r, correspondence h allowed r member positive⟩
  intro h allowed
  obtain ⟨q, relevant, new⟩ :=
    contingent_generation_has_positive_ground admitted before inventory positive g0 formed h allowed
  exact ⟨⟨q, relevant, new⟩, articulate h q relevant⟩

inductive FormationModel where
  | barren | one | two
  deriving DecidableEq

def magnitude : FormationModel → Nat
  | .barren => 0
  | .one => 1
  | .two => 2

inductive LivingClaim where
  | priorLeft | priorRight | freshLeft | freshRight
  deriving DecidableEq

structure Arrangement where
  responded : Bool
  queryOpen : Bool
  deriving DecidableEq

def initial : Arrangement := ⟨false, true⟩

/-- One response retains the active query channel and changes the formation phase. -/
def respond (s : Arrangement) : Arrangement := {s with responded := true}

def prior (branch : Bool) : LivingClaim → Prop
  | .priorLeft => branch = false
  | .priorRight => branch = true
  | .freshLeft | .freshRight => False

/-- New formation requires the retained prior branch as well as the response.
The fresh occurrence is a relation formed through that prior activity. -/
def realizes (s : Arrangement) (m : FormationModel) (branch : Bool) : LivingClaim → Prop
  | .priorLeft => branch = false
  | .priorRight => branch = true
  | .freshLeft => s.responded = true ∧ 0 < magnitude m ∧ prior branch .priorLeft
  | .freshRight => s.responded = true ∧ 0 < magnitude m ∧ prior branch .priorRight

def future (s : Arrangement) (m : FormationModel) : Continuations Bool LivingClaim where
  feasible := fun _ => True
  realized := realizes s m

def generatedInventory (m : FormationModel) : Inventory Bool LivingClaim where
  realized := realizes (respond initial) m
  generative := fun q => q = .freshLeft ∨ q = .freshRight

def freshFor (branch : Bool) : LivingClaim := if branch then .freshRight else .freshLeft

theorem same_response_secures_generation_without_fixed_form
    (m : FormationModel) (productive : 0 < magnitude m) :
    (∀ branch, ∃ q, (generatedInventory m).generative q ∧
      (generatedInventory m).realized branch q ∧ ¬ prior branch q) ∧
    ¬ (∃ q, (generatedInventory m).generative q ∧
      ∀ branch, (generatedInventory m).realized branch q) := by
  constructor
  · intro branch
    refine ⟨freshFor branch, ?_⟩
    cases branch <;> simp [freshFor, generatedInventory, realizes, respond, initial, prior, productive]
  · rintro ⟨q, generated, all⟩
    rcases generated with rfl | rfl
    · have impossible := (all true).2.2
      cases impossible
    · have impossible := (all false).2.2
      cases impossible

inductive Occurrence where
  | freshLeft | freshRight | burden
  deriving DecidableEq

def positiveDomain : List Occurrence := [.freshLeft, .freshRight]
def fullDomain : List Occurrence := [.freshLeft, .freshRight, .burden]

def contribution (s : Arrangement) (m : FormationModel) (branch : Bool) : Occurrence → Int
  | .freshLeft => if s.responded && !branch then magnitude m else 0
  | .freshRight => if s.responded && branch then magnitude m else 0
  | .burden => if s.responded then -((magnitude m : Int) + 1) else 0

def occurrenceMeaning : Occurrence → LivingClaim
  | .freshLeft => .freshLeft
  | .freshRight => .freshRight
  | .burden => .priorLeft

/-- The meaningless burden fallback is never used: it lies outside positiveDomain.
Every strictly positive represented fresh occurrence has an actual new relation. -/
theorem positive_occurrence_has_actual_generative_correspondence
    (m : FormationModel) (branch : Bool) (r : Occurrence)
    (member : r ∈ positiveDomain)
    (good : 0 < contribution (respond initial) m branch r) :
    (generatedInventory m).generative (occurrenceMeaning r) ∧
    (generatedInventory m).realized branch (occurrenceMeaning r) ∧
    ¬ prior branch (occurrenceMeaning r) := by
  cases m <;> cases branch <;> cases r <;>
    simp_all [positiveDomain, contribution, respond, initial, magnitude,
      generatedInventory, occurrenceMeaning, realizes, prior]

/-- A positive new aspect coexists with an explicit adverse full signed change.
The coefficients are a local arithmetic illustration, not universal ethical units. -/
theorem positive_integral_and_adverse_full_change
    (m : FormationModel) (productive : 0 < magnitude m) (branch : Bool) :
    positiveDomain.Nodup ∧ fullDomain.Nodup ∧
    0 < finiteIntegral positiveDomain (contribution (respond initial) m branch) ∧
    finiteIntegral fullDomain (contribution (respond initial) m branch) = -1 ∧
    finiteIntegral fullDomain (contribution initial m branch) = 0 := by
  cases m <;> cases branch <;>
    simp_all [positiveDomain, fullDomain, finiteIntegral, contribution, magnitude,
      respond, initial]

/-- All old represented joint possibilities and the actual query-access field
are retained. This says nothing about unrepresented losses; burden stays above. -/
theorem response_preserves_joint_openness_and_query_access (m : FormationModel) :
    PreservesJointBundles (future initial m) (future (respond initial) m) ∧
    (respond initial).queryOpen = true := by
  constructor
  · apply faithful_history_transport_preserves_joint_bundles (transport := id)
    · intro _ _
      trivial
    · intro branch claim _ held
      cases claim <;> simp_all [future, realizes, initial, respond]
  · rfl

/-- First query sees productive coupling; second can refine its magnitude.
These are supplied physical reading laws within the same arrangement. -/
def rule (m : FormationModel) : Rule Bool :=
  fun query => if query then decide (0 < magnitude m) else decide (magnitude m = 1)

def repertoire : List (Rule Bool) := [rule .barren, rule .one, rule .two]
def firstEvidence : List (Observation Bool) := acquire (rule .one) 1 [true]
def live (m : FormationModel) : Prop := Fits (rule m) firstEvidence

theorem acquired_evidence_secures_good_and_leaves_both_opennesses :
    live .one ∧ live .two ∧ ¬ live .barren ∧
    (learn repertoire firstEvidence = [rule .one, rule .two]) ∧
    answer (learn repertoire firstEvidence) false = none ∧
    (∀ m, live m → ∀ branch,
      0 < finiteIntegral positiveDomain (contribution (respond initial) m branch)) ∧
    (∀ m, live m → ∀ branch,
      finiteIntegral positiveDomain (contribution initial m branch) = 0) ∧
    (revise (learn repertoire firstEvidence) (false, true) = [rule .one]) ∧
    (revise (learn repertoire firstEvidence) (false, false) = [rule .two]) ∧
    answer (revise (learn repertoire firstEvidence) (true, false)) true = none ∧
    learn repertoire (acquire (rule .barren) 1 [true]) = [rule .barren] := by
  refine ⟨?_, ?_, ?_, rfl, rfl, ?_, ?_, rfl, rfl, rfl, rfl⟩
  · simp [live, Fits, firstEvidence, acquire, rule, magnitude]
  · simp [live, Fits, firstEvidence, acquire, rule, magnitude]
  · simp [live, Fits, firstEvidence, acquire, rule, magnitude]
  · intro m admitted branch
    cases m <;> cases branch <;>
      simp_all [live, Fits, firstEvidence, acquire, rule, magnitude, positiveDomain,
        finiteIntegral, contribution, respond, initial]
  · intro m _ branch
    cases m <;> cases branch <;> rfl

/-- Widening the current admitted scope to include a nonproductive possibility
requires retracting the old positive certificate. The theorem does not license
that widening; actual new evidence or changed relations must warrant it. -/
theorem wider_scope_can_require_certificate_retraction :
    (∀ m, live m → live m ∨ m = .barren) ∧
    ¬ (∀ m, live m ∨ m = .barren → ∀ branch,
      0 < finiteIntegral positiveDomain (contribution (respond initial) m branch)) := by
  refine ⟨fun _ h => Or.inl h, ?_⟩
  intro claims
  have impossible := claims .barren (Or.inr rfl) false
  simp [positiveDomain, finiteIntegral, contribution, respond, initial, magnitude] at impossible

end PositiveGroundUncertainty
