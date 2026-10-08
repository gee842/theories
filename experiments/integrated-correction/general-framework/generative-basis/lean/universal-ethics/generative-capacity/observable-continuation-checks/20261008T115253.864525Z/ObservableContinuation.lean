import AlignmentInquiry
import ChanceAdequacy

/-
Observable realization of a specified continuation profile, 8 October 2026.
The finite contingent selector, search soundness and observation restriction
are imported unchanged. The first theorem connects actual selected execution,
an explicit effect correspondence, and the checked support-to-chance bridge.

The finite application has one demand and two currently established connection
modes. Left works in the false mode, right in the true mode. An acquired mode
reading costs one unit, each single route costs one, and genuinely parallel
support costs two. Mode is stable through this read/use interval; a paid reading
is faithful. These are supplied local physical/observation laws, not universal
costs or future-outcome knowledge. Budget is deducted in the actual state.
Menus stipulate independently permitted routes. Search cost and a separate
physical clock are not modeled; the units are not automatically time bounds.
Repertoire failure means no listed plan, not no conceivable implementation.
-/
namespace ObservableContinuation

theorem selected_execution_gives_continuation_bound
    {Ω S Q A : Type} (domain : List Ω) (weight : Ω → Nat)
    (demand oldWorks newWorks : Ω → Bool) (initial : Ω → S)
    (m : AlignmentInquiry.Interface S Q A) (states : List S)
    (plans : List (AlignmentInquiry.Plan Q A)) (p : AlignmentInquiry.Plan Q A)
    (selected : AlignmentInquiry.choose m states plans = some p)
    (covered : ∀ h ∈ domain, initial h ∈ states)
    (effect : ∀ h ∈ domain, ChanceAdequacy.target demand oldWorks h = true →
      ∀ final, AlignmentInquiry.run m p (initial h) = some final →
        m.achieved final = true → newWorks h = true)
    (positive : 0 < ChanceAdequacy.total domain weight) :
    ChanceAdequacy.Fulfilled domain demand oldWorks newWorks ∧
    0 < ChanceAdequacy.total domain weight ∧
    ChanceAdequacy.mass domain weight (ChanceAdequacy.target demand oldWorks) ≤
      ChanceAdequacy.mass domain weight newWorks ∧
    ChanceAdequacy.mass domain weight newWorks ≤ ChanceAdequacy.total domain weight := by
  have fulfilled : ChanceAdequacy.Fulfilled domain demand oldWorks newWorks := by
    intro h member needed
    obtain ⟨final, executed, achieved⟩ :=
      (AlignmentInquiry.chosen_sound m states plans p selected).2.2 (initial h) (covered h member)
    exact effect h member needed final executed achieved
  exact ⟨fulfilled,
    ChanceAdequacy.fulfillment_gives_chance_floor domain weight demand oldWorks newWorks
      positive fulfilled⟩

inductive Query where
  | blind
  | sense
  deriving DecidableEq, Repr

inductive Action where
  | left
  | right
  | parallel
  deriving DecidableEq, Repr

structure State where
  mode : Bool
  budget : Nat
  supported : Bool
  deriving DecidableEq, Repr

def queryCost : Query → Nat
  | .blind => 0
  | .sense => 1

def actionCost : Action → Nat
  | .left => 1
  | .right => 1
  | .parallel => 2

def routeWorks (mode : Bool) : Action → Bool
  | .left => !mode
  | .right => mode
  | .parallel => true

def probe (s : State) (q : Query) : Option (Bool × State) :=
  if queryCost q ≤ s.budget then
    some ((if q = .sense then s.mode else false),
      {s with budget := s.budget - queryCost q})
  else none

def respond (s : State) (a : Action) : Option State :=
  if actionCost a ≤ s.budget then
    some {s with budget := s.budget - actionCost a, supported := routeWorks s.mode a}
  else none

def interface (goal : Bool → Bool) : AlignmentInquiry.Interface State Query Action :=
  ⟨probe, respond, fun s => !goal s.mode || s.supported⟩

def initial (budget : Nat) (mode : Bool) : State := ⟨mode, budget, false⟩

def states (budget : Nat) : List State := [initial budget false, initial budget true]

def oldWorks (mode : Bool) : Bool := !mode

def candidate (mode : Bool) : Bool := mode

def extension : Bool → Bool := ChanceAdequacy.repair (fun _ => true) oldWorks candidate

def singlePlans : List (AlignmentInquiry.Plan Query Action) :=
  AlignmentInquiry.repertoire [.blind, .sense] [.left, .right]

def expandedPlans : List (AlignmentInquiry.Plan Query Action) :=
  AlignmentInquiry.repertoire [.blind, .sense] [.left, .right, .parallel]

def maintain : AlignmentInquiry.Plan Query Action := ⟨.blind, .left, .left⟩

def inspect : AlignmentInquiry.Plan Query Action := ⟨.sense, .left, .right⟩

/- The positive branch is not reached by the blind query. This is the first
valid parallel plan in the inherited enumeration, not a unique fair policy. -/
def parallelPlan : AlignmentInquiry.Plan Query Action := ⟨.blind, .parallel, .left⟩

def support (p : AlignmentInquiry.Plan Query Action) (budget : Nat) (mode : Bool) : Bool :=
  (AlignmentInquiry.run (interface extension) p (initial budget mode)).any (fun s => s.supported)

/-- The event union is full, but the one-unit single-route repertoire cannot
realize it. The weaker old maintenance task remains actually executable. -/
theorem limited_budget_preserves_maintenance_but_not_extension :
    AlignmentInquiry.choose (interface oldWorks) (states 1) singlePlans = some maintain ∧
    (∀ mode, AlignmentInquiry.run (interface oldWorks) maintain (initial 1 mode) =
      some ⟨mode, 0, !mode⟩) ∧
    ChanceAdequacy.Fulfilled [false, true] (fun _ => true) oldWorks (support maintain 1) ∧
    (∀ mode, extension mode = true) ∧
    AlignmentInquiry.choose (interface extension) (states 1) singlePlans = none := by
  decide

/-- A funded current-mode probe followed by a single route realizes the union.
Probe and response consume separate units of the same actual budget. -/
theorem funded_observation_realizes_extension :
    AlignmentInquiry.choose (interface extension) (states 2) singlePlans = some inspect ∧
    (∀ mode, probe (initial 2 mode) .sense = some (mode, ⟨mode, 1, false⟩) ∧
      AlignmentInquiry.run (interface extension) inspect (initial 2 mode) =
        some ⟨mode, 0, true⟩) ∧
    ChanceAdequacy.Fulfilled [false, true] (fun _ => true) oldWorks (support inspect 2) ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) oldWorks = 1 ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) (support inspect 2) = 2 ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) oldWorks <
      ChanceAdequacy.mass [false, true] (fun _ => 1) (support inspect 2) := by
  decide

/-- A genuinely available two-unit parallel route realizes the same extension
without acquiring the mode. This changes actions, not the hidden observation. -/
theorem funded_parallel_support_realizes_extension :
    AlignmentInquiry.choose (interface extension) (states 2) expandedPlans = some parallelPlan ∧
    (∀ mode, probe (initial 2 mode) .blind = some (false, initial 2 mode) ∧
      AlignmentInquiry.run (interface extension) parallelPlan (initial 2 mode) =
        some ⟨mode, 0, true⟩) ∧
    ChanceAdequacy.Fulfilled [false, true] (fun _ => true) oldWorks (support parallelPlan 2) ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) oldWorks = 1 ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) (support parallelPlan 2) = 2 ∧
    ChanceAdequacy.mass [false, true] (fun _ => 1) oldWorks <
      ChanceAdequacy.mass [false, true] (fun _ => 1) (support parallelPlan 2) := by
  decide

end ObservableContinuation
