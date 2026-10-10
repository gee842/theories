import Std

/-!
# Joint continuation information before ethical classification

`History` represents whole continuations at one declared scope. `Claim` denotes
identified relations or realizations within those histories, including temporal
relations when relevant. Neither type consists of primitive independent owners.
Their adequacy, stable meanings and coverage are application obligations.

The theorem relates two descriptions of SAME-HISTORY possibility preservation.
Its universal bundle range is explicit; it is not derived from a finite list of
capabilities. The reverse proof uses the entire represented realization profile
of one admitted history. This profile is jointly realized by that history itself,
so no impossible combination is assumed. Preservation is existential separately
for each old history. It supplies neither a uniform causal intervention nor a
policy guarantee, probability comparison or actual realized outcome.

No ethical ranking, positive relevance, practical reason or obligation is a
parameter or conclusion. This audit removes one representational shortcut; it
does not settle first ethical warrant or prove that every possibility is good.
Empty Lean axiom reports would not eliminate these supplied formal definitions,
application correspondences, the local witness law or the logical background.
-/

namespace JointContinuationClassification

universe u v w x

structure Continuations (History : Type u) (Claim : Type v) where
  feasible : History → Prop
  realized : History → Claim → Prop

def Jointly {History : Type u} {Claim : Type v}
    (continuations : Continuations History Claim) (bundle : Claim → Prop) : Prop :=
  ∃ history, continuations.feasible history ∧
    ∀ claim, bundle claim → continuations.realized history claim

def CarriesWholeProfiles {Old : Type u} {New : Type w} {Claim : Type v}
    (before : Continuations Old Claim) (after : Continuations New Claim) : Prop :=
  ∀ old, before.feasible old → ∃ new, after.feasible new ∧
    ∀ claim, before.realized old claim → after.realized new claim

def PreservesJointBundles {Old : Type u} {New : Type w} {Claim : Type v}
    (before : Continuations Old Claim) (after : Continuations New Claim) : Prop :=
  ∀ bundle, Jointly before bundle → Jointly after bundle

/-- Exact correspondence, including potentially infinite represented profiles. -/
theorem whole_profile_preservation_iff_joint_bundle_preservation
    {Old : Type u} {New : Type w} {Claim : Type v}
    (before : Continuations Old Claim) (after : Continuations New Claim) :
    CarriesWholeProfiles before after ↔ PreservesJointBundles before after := by
  constructor
  · intro carries bundle possible
    obtain ⟨old, feasible, realized⟩ := possible
    obtain ⟨new, admitted, contains⟩ := carries old feasible
    exact ⟨new, admitted, fun claim present => contains claim (realized claim present)⟩
  · intro preserves old feasible
    exact preserves (before.realized old) ⟨old, feasible, fun _ present => present⟩

/-- Composes witnesses through the same intermediate continuation, not through
separate witnesses for each claim. All three descriptions share claim meanings. -/
theorem whole_profile_preservation_composes
    {First : Type u} {Second : Type w} {Third : Type x} {Claim : Type v}
    {first : Continuations First Claim} {second : Continuations Second Claim}
    {third : Continuations Third Claim}
    (left : CarriesWholeProfiles first second)
    (right : CarriesWholeProfiles second third) : CarriesWholeProfiles first third := by
  intro initial feasible
  obtain ⟨middle, admitted, firstContains⟩ := left initial feasible
  obtain ⟨final, permitted, secondContains⟩ := right middle admitted
  exact ⟨final, permitted, fun claim present => secondContains claim (firstContains claim present)⟩

/-- A causal or representational transport supports joint preservation only when
its actual mapped history is feasible and retains every represented realization.
This is a sufficient concrete certificate; the converse uniform map is not claimed. -/
theorem faithful_history_transport_preserves_joint_bundles
    {Old : Type u} {New : Type w} {Claim : Type v}
    {before : Continuations Old Claim} {after : Continuations New Claim}
    (transport : Old → New)
    (feasible : ∀ old, before.feasible old → after.feasible (transport old))
    (faithful : ∀ old claim, before.feasible old →
      before.realized old claim → after.realized (transport old) claim) :
    PreservesJointBundles before after := by
  apply (whole_profile_preservation_iff_joint_bundle_preservation before after).mp
  exact fun old admitted =>
    ⟨transport old, feasible old admitted, fun claim present => faithful old claim admitted present⟩

/-- A complete signed factual language and a selected realization language do
different work. If preservation retains every true claim, including the exact
complement of each claim, then the matched history has no newly true represented
claim. Constructively this forbids an explicit strict-extension witness; no
double-negation elimination or classical truth-reflection claim is hidden here.
The assumptions concern the matched feasible histories, not ethical valuations. -/
theorem complement_closed_preservation_excludes_new_realization
    {Old : Type u} {New : Type w} {Claim : Type v}
    {before : Continuations Old Claim} {after : Continuations New Claim}
    (complement : Claim → Claim) {old : Old} {new : New}
    (oldFeasible : before.feasible old) (newFeasible : after.feasible new)
    (oldComplement : ∀ history, before.feasible history → ∀ claim,
      before.realized history (complement claim) ↔ ¬ before.realized history claim)
    (newComplement : ∀ history, after.feasible history → ∀ claim,
      after.realized history (complement claim) ↔ ¬ after.realized history claim)
    (carries : ∀ claim, before.realized old claim → after.realized new claim) :
    ¬ ∃ claim, after.realized new claim ∧ ¬ before.realized old claim := by
  intro extension
  obtain ⟨claim, newRealization, oldAbsence⟩ := extension
  have oldNegative := (oldComplement old oldFeasible claim).mpr oldAbsence
  have newNegative := carries (complement claim) oldNegative
  exact (newComplement new newFeasible claim).mp newNegative newRealization

/-! A single supplied relational event law. The initial configuration can retain
or release a coupling. The retained coupling permits left, right or joint
activation; after release only one-sided activation fits this finite opportunity.
These are positions in one configuration, not independent agents. All complete
histories retain the common initial state, the intervening configuration and its
actual activation. This is a structural witness, not an empirical law or an
ethical verdict about releasing a coupling. Other consequences are not modeled.
-/

inductive Configuration where
  | initial | coupled | released | leftActive | rightActive | bothActive
  deriving DecidableEq

inductive Event where
  | retain | release | activateLeft | activateRight | activateTogether
  deriving DecidableEq

inductive Step : Configuration → Event → Configuration → Prop where
  | retainCoupling : Step .initial .retain .coupled
  | releaseCoupling : Step .initial .release .released
  | activateLeftCoupled : Step .coupled .activateLeft .leftActive
  | activateRightCoupled : Step .coupled .activateRight .rightActive
  | activateTogether : Step .coupled .activateTogether .bothActive
  | activateLeftReleased : Step .released .activateLeft .leftActive
  | activateRightReleased : Step .released .activateRight .rightActive

structure History where
  first : Event
  middle : Configuration
  second : Event
  final : Configuration

def Admissible (history : History) : Prop :=
  Step .initial history.first history.middle ∧
    Step history.middle history.second history.final

inductive Claim where
  | leftRealized | rightRealized
  deriving DecidableEq

def Realized (history : History) : Claim → Prop
  | .leftRealized => history.final = .leftActive ∨ history.final = .bothActive
  | .rightRealized => history.final = .rightActive ∨ history.final = .bothActive

def retained : Continuations History Claim where
  feasible := fun history => Admissible history ∧ history.first = .retain
  realized := Realized

def released : Continuations History Claim where
  feasible := fun history => Admissible history ∧ history.first = .release
  realized := Realized

def together : History := ⟨.retain, .coupled, .activateTogether, .bothActive⟩

def leftOnly : History := ⟨.release, .released, .activateLeft, .leftActive⟩

def rightOnly : History := ⟨.release, .released, .activateRight, .rightActive⟩

/-- Every marginal realization is retained, but a jointly realized bundle is
lost under this one law and common initial configuration. Marginal capability
lists therefore cannot certify even this represented joint-preservation test. -/
theorem same_marginal_realizations_can_lose_a_joint_bundle :
    (∀ claim, (∃ history, retained.feasible history ∧ retained.realized history claim) ↔
      (∃ history, released.feasible history ∧ released.realized history claim)) ∧
    Jointly retained (fun _ => True) ∧ ¬ Jointly released (fun _ => True) := by
  have kept : retained.feasible together := ⟨⟨.retainCoupling, .activateTogether⟩, rfl⟩
  have joint : ∀ claim, retained.realized together claim := by
    intro claim
    cases claim <;> exact Or.inr rfl
  refine ⟨?_, ⟨together, kept, fun claim _ => joint claim⟩, ?_⟩
  · intro claim
    constructor
    · intro _
      cases claim
      · exact ⟨leftOnly, ⟨⟨.releaseCoupling, .activateLeftReleased⟩, rfl⟩, Or.inl rfl⟩
      · exact ⟨rightOnly, ⟨⟨.releaseCoupling, .activateRightReleased⟩, rfl⟩, Or.inl rfl⟩
    · intro _
      exact ⟨together, kept, joint claim⟩
  · intro possible
    obtain ⟨⟨first, middle, second, final⟩, ⟨⟨firstStep, secondStep⟩, firstIsRelease⟩,
      realizes⟩ := possible
    cases firstIsRelease
    cases firstStep
    cases secondStep with
    | activateLeftReleased =>
      have right := realizes Claim.rightRealized True.intro
      rcases right with impossible | impossible <;> cases impossible
    | activateRightReleased =>
      have left := realizes Claim.leftRealized True.intro
      rcases left with impossible | impossible <;> cases impossible

end JointContinuationClassification
