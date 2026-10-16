import Std

/-!
# Ground-preserving coverage within one generative history

The unary reachability/least-interpretation result formalizes the inherited
HUIGEN-REASON-TRANSPORT argument. It is not a newly derived ethical ground.
Seeds stand for independently warranted instances; edges stand for justified
implications preserving their complete grounds and current scope. A causal
connection, matching label, endorsement or successful action is not such a
certificate merely by being represented here.

The additional interface combines local scopes over claim-positions in one history.
A Position must identify the intended reason claim, its ground/application and its
occurrence, not merely a bare physical location or event. Distinct reason kinds or
authority scopes at the same occurrence need not have the same warranted status.
Locally specified grounds can glue when their shared claim and scope relevance are
independently justified and they agree on the resulting overlaps. Occurrence
equality alone does not justify that compatibility premise. Certified steps can
alternate scopes, but cannot splice positions from different histories. Domains
covering every position do not themselves establish grounded coverage.

All types can be infinite. No actor/patient product, fixed goal, probability,
universal causal connectivity, ethical ranking or favorable direction is imposed.
The logical converse concerns only these stated positive unary premises, not an
exhaustive characterization of ethical truth. Interpretations are Prop-valued so
the least interpretation is constructive; the result does not assume that every
reason has an available Boolean decision procedure. Joint-premise arguments need
their own proof rule and cannot be replaced by an arbitrary unary edge.
-/

namespace WholeGroundCoverage

universe u v w

inductive Reached {Position : Type u}
    (Seed : Position → Prop) (Edge : Position → Position → Prop) : Position → Prop where
  | seed {p : Position} : Seed p → Reached Seed Edge p
  | step {p q : Position} : Reached Seed Edge p → Edge p q → Reached Seed Edge q

def Admissible {Position : Type u}
    (Seed : Position → Prop) (Edge : Position → Position → Prop)
    (Reason : Position → Prop) : Prop :=
  (∀ p, Seed p → Reason p) ∧
    (∀ p q, Edge p q → Reason p → Reason q)

def Entails {Position : Type u}
    (Seed : Position → Prop) (Edge : Position → Position → Prop) (p : Position) : Prop :=
  ∀ Reason, Admissible Seed Edge Reason → Reason p

theorem reason_inheritance {Position : Type u}
    {Seed Reason : Position → Prop} {Edge : Position → Position → Prop}
    (sound : Admissible Seed Edge Reason) {p : Position}
    (derivation : Reached Seed Edge p) : Reason p := by
  induction derivation with
  | seed hs => exact sound.1 _ hs
  | step _ he ih => exact sound.2 _ _ he ih

theorem reached_is_admissible {Position : Type u}
    (Seed : Position → Prop) (Edge : Position → Position → Prop) :
    Admissible Seed Edge (Reached Seed Edge) :=
  ⟨fun _ hs => .seed hs, fun _ _ he hr => .step hr he⟩

theorem reached_iff_entails {Position : Type u}
    (Seed : Position → Prop) (Edge : Position → Position → Prop) (p : Position) :
    Reached Seed Edge p ↔ Entails Seed Edge p := by
  constructor
  · intro hr Reason sound
    exact reason_inheritance sound hr
  · intro forced
    exact forced (Reached Seed Edge) (reached_is_admissible Seed Edge)

/-- Universal means all independently declared targets, not all initially admitted ones. -/
theorem universal_target_coverage_iff {Position : Type u}
    (Seed Target : Position → Prop) (Edge : Position → Position → Prop) :
    (∀ p, Target p → Reached Seed Edge p) ↔
      (∀ Reason, Admissible Seed Edge Reason → ∀ p, Target p → Reason p) := by
  constructor
  · intro coverage Reason sound p hp
    exact reason_inheritance sound (coverage p hp)
  · intro all p hp
    exact all (Reached Seed Edge) (reached_is_admissible Seed Edge) p hp

/-- An uncovered target is not entailed by this premise family; it is not refuted ethically. -/
theorem uncovered_has_admissible_omission {Position : Type u}
    {Seed : Position → Prop} {Edge : Position → Position → Prop} {p : Position}
    (missing : ¬ Reached Seed Edge p) :
    ∃ Reason, Admissible Seed Edge Reason ∧ ¬ Reason p :=
  ⟨Reached Seed Edge, reached_is_admissible Seed Edge, missing⟩

theorem reached_mono {Position : Type u}
    {Seed Seed' : Position → Prop} {Edge Edge' : Position → Position → Prop}
    (seeds : ∀ p, Seed p → Seed' p) (edges : ∀ p q, Edge p q → Edge' p q)
    {p : Position} (hr : Reached Seed Edge p) : Reached Seed' Edge' p := by
  induction hr with
  | seed hs => exact .seed (seeds _ hs)
  | step _ he ih => exact .step ih (edges _ _ he)

/-- Replacing a seed by its already grounded derivation does not add independent authority. -/
theorem substitute_grounded_seeds {Position : Type u}
    {Seed Seed' : Position → Prop} {Edge : Position → Position → Prop}
    (seeds : ∀ p, Seed' p → Reached Seed Edge p)
    {p : Position} (hr : Reached Seed' Edge p) : Reached Seed Edge p := by
  induction hr with
  | seed hs => exact seeds _ hs
  | step _ he ih => exact .step ih he

structure LocalAtlas (Position : Type u) (Scope : Type v) where
  domain : Scope → Position → Prop
  edge : (i : Scope) → {p : Position // domain i p} → {p : Position // domain i p} → Prop

def ScopedEdge {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope) (i : Scope) (p q : Position) : Prop :=
  ∃ hp : atlas.domain i p, ∃ hq : atlas.domain i q,
    atlas.edge i ⟨p, hp⟩ ⟨q, hq⟩

def JoinedEdge {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope) (p q : Position) : Prop :=
  ∃ i, ScopedEdge atlas i p q

def LocalSound {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope) (Reason : Position → Prop) : Prop :=
  ∀ i (p q : {p : Position // atlas.domain i p}),
    atlas.edge i p q → Reason p.val → Reason q.val

theorem local_sound_iff_joined_sound {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope) (Reason : Position → Prop) :
    LocalSound atlas Reason ↔
      ∀ p q, JoinedEdge atlas p q → Reason p → Reason q := by
  constructor
  · intro localProof p q hedge hr
    obtain ⟨i, hp, hq, he⟩ := hedge
    exact localProof i ⟨p, hp⟩ ⟨q, hq⟩ he hr
  · intro global i p q he hr
    exact global p.val q.val ⟨i, p.property, q.property, he⟩ hr

theorem local_sound_gives_global_inheritance {Position : Type u} {Scope : Type v}
    {atlas : LocalAtlas Position Scope} {Seed Reason : Position → Prop}
    (seeds : ∀ p, Seed p → Reason p) (localProof : LocalSound atlas Reason)
    {p : Position} (hr : Reached Seed (JoinedEdge atlas) p) : Reason p :=
  reason_inheritance ⟨seeds, (local_sound_iff_joined_sound atlas Reason).mp localProof⟩ hr

theorem local_reach_in_joined {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope) (i : Scope) {Seed : Position → Prop}
    {p : Position} (hr : Reached Seed (ScopedEdge atlas i) p) :
    Reached Seed (JoinedEdge atlas) p :=
  reached_mono (fun _ hs => hs) (fun _ _ he => ⟨i, he⟩) hr

/-- Compatibility is supplied for the SAME intended claim at a shared position,
    with relevance and application scope preserved. It is not inferred from bare
    occurrence equality: distinct kinds of reason, grounds or authority claims
    arising at one event may legitimately have different statuses. -/
def CompatibleGrounds {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope)
    (Ground : (i : Scope) → {p : Position // atlas.domain i p} → Prop) : Prop :=
  ∀ i j p (hi : atlas.domain i p) (hj : atlas.domain j p),
    Ground i ⟨p, hi⟩ ↔ Ground j ⟨p, hj⟩

def GluedGround {Position : Type u} {Scope : Type v}
    (atlas : LocalAtlas Position Scope)
    (Ground : (i : Scope) → {p : Position // atlas.domain i p} → Prop)
    (p : Position) : Prop :=
  ∃ i, ∃ hp : atlas.domain i p, Ground i ⟨p, hp⟩

theorem glued_ground_iff_local {Position : Type u} {Scope : Type v}
    {atlas : LocalAtlas Position Scope}
    {Ground : (i : Scope) → {p : Position // atlas.domain i p} → Prop}
    (compatible : CompatibleGrounds atlas Ground)
    (i : Scope) (p : {p : Position // atlas.domain i p}) :
    GluedGround atlas Ground p.val ↔ Ground i p := by
  constructor
  · rintro ⟨j, hj, hground⟩
    exact (compatible j i p.val hj p.property).mp hground
  · intro hground
    exact ⟨i, p.property, hground⟩

/-- Overlap agreement and certified local transport suffice for global transport.
    Overlap agreement alone does not justify any local ground. -/
theorem compatible_local_ground_transport_glues {Position : Type u} {Scope : Type v}
    {atlas : LocalAtlas Position Scope}
    {Ground : (i : Scope) → {p : Position // atlas.domain i p} → Prop}
    (compatible : CompatibleGrounds atlas Ground)
    (localProof : ∀ i p q, atlas.edge i p q → Ground i p → Ground i q) :
    LocalSound atlas (GluedGround atlas Ground) := by
  intro i p q he hg
  exact (glued_ground_iff_local compatible i q).mpr
    (localProof i p q he ((glued_ground_iff_local compatible i p).mp hg))

theorem jointly_grounded_scope_inheritance {Position : Type u} {Scope : Type v}
    {atlas : LocalAtlas Position Scope} {Seed : Position → Prop}
    {Ground : (i : Scope) → {p : Position // atlas.domain i p} → Prop}
    (compatible : CompatibleGrounds atlas Ground)
    (localProof : ∀ i p q, atlas.edge i p q → Ground i p → Ground i q)
    (seeds : ∀ p, Seed p → GluedGround atlas Ground p)
    {p : Position} (hr : Reached Seed (JoinedEdge atlas) p) :
    GluedGround atlas Ground p :=
  local_sound_gives_global_inheritance seeds
    (compatible_local_ground_transport_glues compatible localProof) hr

/-! A history index is retained in the position type. The model does not infer
    real-world reference from the index: a claimed interpretation must establish it.
    Cross-history analogy requires a separate justified interface, never this one. -/

inductive HistoryEdge {History : Type u} {Position : History → Type v}
    {Scope : History → Type w}
    (atlas : (h : History) → LocalAtlas (Position h) (Scope h)) :
    Sigma Position → Sigma Position → Prop where
  | within (h : History) (p q : Position h) :
      JoinedEdge (atlas h) p q → HistoryEdge atlas ⟨h, p⟩ ⟨h, q⟩

theorem history_edge_preserves_history {History : Type u}
    {Position : History → Type v} {Scope : History → Type w}
    {atlas : (h : History) → LocalAtlas (Position h) (Scope h)}
    {x y : Sigma Position} (edge : HistoryEdge atlas x y) : x.fst = y.fst := by
  cases edge
  rfl

theorem history_reach_projects {History : Type u}
    {Position : History → Type v} {Scope : History → Type w}
    {atlas : (h : History) → LocalAtlas (Position h) (Scope h)}
    {Seed : Sigma Position → Prop} {x : Sigma Position}
    (hr : Reached Seed (HistoryEdge atlas) x) :
    Reached (fun p => Seed ⟨x.fst, p⟩) (JoinedEdge (atlas x.fst)) x.snd := by
  induction hr with
  | seed hs => exact .seed hs
  | step _ he ih =>
    cases he with
    | within h p q hedge => exact .step ih hedge

theorem history_reach_lifts {History : Type u}
    {Position : History → Type v} {Scope : History → Type w}
    {atlas : (h : History) → LocalAtlas (Position h) (Scope h)}
    {Seed : Sigma Position → Prop} {h : History} {p : Position h}
    (hr : Reached (fun q => Seed ⟨h, q⟩) (JoinedEdge (atlas h)) p) :
    Reached Seed (HistoryEdge atlas) ⟨h, p⟩ := by
  induction hr with
  | seed hs => exact .seed hs
  | step _ he ih => exact .step ih (.within h _ _ he)

/-- Exact fiberwise reachability: the global presentation cannot borrow another
    history's grounded occurrence merely because local labels coincide. -/
theorem history_reach_iff {History : Type u}
    {Position : History → Type v} {Scope : History → Type w}
    (atlas : (h : History) → LocalAtlas (Position h) (Scope h))
    (Seed : Sigma Position → Prop) (h : History) (p : Position h) :
    Reached Seed (HistoryEdge atlas) ⟨h, p⟩ ↔
      Reached (fun q => Seed ⟨h, q⟩) (JoinedEdge (atlas h)) p :=
  ⟨history_reach_projects, history_reach_lifts⟩

theorem history_local_sound_gives_global {History : Type u}
    {Position : History → Type v} {Scope : History → Type w}
    {atlas : (h : History) → LocalAtlas (Position h) (Scope h)}
    {Seed : Sigma Position → Prop} {Reason : (h : History) → Position h → Prop}
    (seeds : ∀ h p, Seed ⟨h, p⟩ → Reason h p)
    (localProof : ∀ h, LocalSound (atlas h) (Reason h))
    {h : History} {p : Position h} (hr : Reached Seed (HistoryEdge atlas) ⟨h, p⟩) :
    Reason h p :=
  local_sound_gives_global_inheritance (seeds h) (localProof h) (history_reach_projects hr)

/-! Two small logical witnesses delimit the general interface. Their labels are
    not moral patients and their edges are not asserted to be ethical truths. -/

inductive Place where
  | start
  | middle
  | finish

inductive Window where
  | first
  | second

def firstSeed (p : Place) : Prop := p = .start

inductive InWindow : Window → Place → Prop where
  | firstStart : InWindow .first .start
  | firstMiddle : InWindow .first .middle
  | secondMiddle : InWindow .second .middle
  | secondFinish : InWindow .second .finish

inductive WindowStep : Window → Place → Place → Prop where
  | first : WindowStep .first .start .middle
  | second : WindowStep .second .middle .finish

def alternatingAtlas : LocalAtlas Place Window where
  domain := InWindow
  edge i p q := WindowStep i p.val q.val

theorem alternating_domains_cover (p : Place) :
    ∃ i, alternatingAtlas.domain i p := by
  cases p with
  | start => exact ⟨.first, .firstStart⟩
  | middle => exact ⟨.first, .firstMiddle⟩
  | finish => exact ⟨.second, .secondFinish⟩

theorem alternating_first_step : ScopedEdge alternatingAtlas .first .start .middle :=
  ⟨.firstStart, .firstMiddle, .first⟩

theorem alternating_second_step : ScopedEdge alternatingAtlas .second .middle .finish :=
  ⟨.secondMiddle, .secondFinish, .second⟩

theorem alternating_join_reaches_finish :
    Reached firstSeed (JoinedEdge alternatingAtlas) .finish :=
  .step (.step (.seed rfl) ⟨.first, alternating_first_step⟩)
    ⟨.second, alternating_second_step⟩

theorem first_scope_reach_stays_inside {p : Place}
    (hr : Reached firstSeed (ScopedEdge alternatingAtlas .first) p) :
    alternatingAtlas.domain .first p := by
  induction hr with
  | seed hs => cases hs; exact InWindow.firstStart
  | step _ he _ =>
    obtain ⟨_, hq, _⟩ := he
    exact hq

theorem second_scope_reach_stays_at_seed {p : Place}
    (hr : Reached firstSeed (ScopedEdge alternatingAtlas .second) p) : p = .start := by
  induction hr with
  | seed hs => exact hs
  | step _ he ih =>
    cases ih
    obtain ⟨hp, _, _⟩ := he
    cases hp

theorem alternating_beyond_separate_closures :
    Reached firstSeed (JoinedEdge alternatingAtlas) .finish ∧
      ¬ Reached firstSeed (ScopedEdge alternatingAtlas .first) .finish ∧
      ¬ Reached firstSeed (ScopedEdge alternatingAtlas .second) .finish := by
  refine ⟨alternating_join_reaches_finish, ?_, ?_⟩
  · intro hr
    cases first_scope_reach_stays_inside hr
  · intro hr
    cases second_scope_reach_stays_at_seed hr

def unconnectedAtlas : LocalAtlas Place Unit where
  domain _ _ := True
  edge _ _ _ := False

theorem unconnected_reach_is_seed {p : Place}
    (hr : Reached firstSeed (JoinedEdge unconnectedAtlas) p) : firstSeed p := by
  induction hr with
  | seed hs => exact hs
  | step _ he _ =>
    obtain ⟨_, _, _, impossible⟩ := he
    exact False.elim impossible

/-- Every occurrence belongs to a local domain and a seed exists, yet a target
    remains ungrounded. This is about the stated premises, not moral exclusion. -/
theorem local_domain_coverage_insufficient :
    (∀ p, ∃ i, unconnectedAtlas.domain i p) ∧
      (∃ p, firstSeed p) ∧
      ¬ Reached firstSeed (JoinedEdge unconnectedAtlas) .finish := by
  refine ⟨fun _ => ⟨(), True.intro⟩, ⟨.start, rfl⟩, ?_⟩
  intro hr
  cases unconnected_reach_is_seed hr

#print axioms reason_inheritance
#print axioms reached_is_admissible
#print axioms reached_iff_entails
#print axioms universal_target_coverage_iff
#print axioms uncovered_has_admissible_omission
#print axioms reached_mono
#print axioms substitute_grounded_seeds
#print axioms local_sound_iff_joined_sound
#print axioms local_sound_gives_global_inheritance
#print axioms local_reach_in_joined
#print axioms glued_ground_iff_local
#print axioms compatible_local_ground_transport_glues
#print axioms jointly_grounded_scope_inheritance
#print axioms history_edge_preserves_history
#print axioms history_reach_projects
#print axioms history_reach_lifts
#print axioms history_reach_iff
#print axioms history_local_sound_gives_global
#print axioms alternating_domains_cover
#print axioms alternating_first_step
#print axioms alternating_second_step
#print axioms alternating_join_reaches_finish
#print axioms first_scope_reach_stays_inside
#print axioms second_scope_reach_stays_at_seed
#print axioms alternating_beyond_separate_closures
#print axioms unconnected_reach_is_seed
#print axioms local_domain_coverage_insufficient

end WholeGroundCoverage
