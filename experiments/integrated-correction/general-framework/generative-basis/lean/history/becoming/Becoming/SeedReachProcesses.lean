import Becoming.Bridge
import Becoming.SeedReach

/-!
# Seed closures as reach in a process

`WholeGroundCoverage` and `CutCoverageAudit` state laws of the closure of seeds under edges, and
`EvaluatorGrounding` of chains of small steps between profiles. `Becoming.Bridge` proves that
the chains are reachability on the process whose steps are the edges (`chain_iff_reach`). This
module reads the edges off a process: the edges of a process are its moves, one step under some
label, and the closure of seeds under them is what the process reaches from a seed (`reached_iff`,
`cutReach_iff`). `Moves`, `FromSeed` and the laws of reach from seeds (the least invariant,
separation and what a reach claim needs) are stated in the core, `Becoming.SeedReach`, with the
full names they had here. At the edge process these are the seed–edge closure of
`Becoming.EdgeClosure` (`reached_iff_closure`, `cutReach_iff_closure`). A local atlas of
`WholeGroundCoverage` is a process whose labels are its scopes (`atlasProcess`, with one scope's
edges alone as `scopeProcess`), and a family of atlases indexed by histories is a process on the
positions of every history (`historyProcess`). The laws of the periphery modules are then stated
of these processes and proved through them.

* **Scopes of an atlas.** What one scope's edges reach the atlas's process reaches
  (`scope_reach_in_atlas`); grounds compatible on overlaps and carried by every local edge hold
  wherever the atlas's process reaches from grounded seeds (`glued_on_reach`). In the alternating
  atlas the process reaches the finish from the start although neither scope's edges alone do
  (`alternating_beyond_scopes`); in the unconnected atlas every position lies in a scope and a seed
  exists, yet the process does not reach the finish (`unconnected_coverage_insufficient`).
* **Histories.** The process of a family of atlases never leaves a history along any path
  (`history_reach_keeps`); it reaches a position of a history from a seed exactly where that
  history's atlas process reaches it from a seed of that history (`history_fromSeed_iff`), and a
  reason sound in each history holds wherever it reaches from seeds the reason holds at
  (`history_sound_on_reach`).
* **Cuts.** A reverse-closed cut avoiding the seeds and holding a configuration is the complement
  of a property separating it from the seeds (`hasCut_iff_separated`), so it exists exactly where
  the process does not reach it from a seed (`cut_iff_not_fromSeed`); where that reach is decided,
  no such cut exists exactly where it is reached (`noCut_iff_fromSeed_of_decidable`); and absence
  of a cut gives reach in every process exactly where double-negation elimination holds
  (`upgrade_iff_dne`), the core's `fromSeed_of_not_separated_iff_dne`.
* **Chains of small steps.** Under supervenience, S0 and tolerance, where every reachable living
  occurrence's profile is reached from an own living one in the process of small steps between
  profiles, living significance holds of the reachable occurrences with the standpoint's
  significance as positive relevance, on the frame of the reachable inventory
  (`reachable_living_significance`).

S0, supervenience and tolerance are premises the theorem names; living significance is concluded
from them, not asserted. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

universe u v w

namespace SeedReachProcesses

section Moves

variable {S : Type u} {A : Type v}

/-- **The closure of seeds under edges that are a process's moves is what the process reaches
from a seed.** -/
theorem reached_iff {P : Process S A} {edge : S → S → Prop} (moves : ∀ x y, edge x y ↔ Moves P x y)
    {seed : S → Prop} {x : S} : WholeGroundCoverage.Reached seed edge x ↔ FromSeed P seed x := by
  constructor
  · intro h
    induction h with
    | seed held => exact ⟨_, held, Reach.refl _ _⟩
    | step _ e ih =>
      obtain ⟨s, held, path⟩ := ih
      obtain ⟨a, st⟩ := (moves _ _).mp e
      exact ⟨s, held, path.trans (Reach.of_step st)⟩
  · intro ⟨s, held, path⟩
    exact Invariant.reach (P := P) (I := WholeGroundCoverage.Reached seed edge)
      (fun _ a _ st r => .step r ((moves _ _).mpr ⟨a, st⟩)) path (.seed held)

/-- **The same for the closure of `CutCoverageAudit`.** -/
theorem cutReach_iff {P : Process S A} {edge : S → S → Prop}
    (moves : ∀ x y, edge x y ↔ Moves P x y) {seed : S → Prop} {x : S} :
    UniversalEthics.CutCoverageAudit.Reach seed edge x ↔ FromSeed P seed x := by
  constructor
  · intro h
    induction h with
    | root held => exact ⟨_, held, Reach.refl _ _⟩
    | step _ e ih =>
      obtain ⟨s, held, path⟩ := ih
      obtain ⟨a, st⟩ := (moves _ _).mp e
      exact ⟨s, held, path.trans (Reach.of_step st)⟩
  · intro ⟨s, held, path⟩
    exact Invariant.reach (P := P) (I := UniversalEthics.CutCoverageAudit.Reach seed edge)
      (fun _ a _ st r => .step r ((moves _ _).mpr ⟨a, st⟩)) path (.root held)

/-- A property is admissible for the moves of a process exactly where it holds at the seeds and is
invariant under the process. -/
theorem admissible_iff {P : Process S A} {seed I : S → Prop} :
    WholeGroundCoverage.Admissible seed (Moves P) I ↔ (∀ s, seed s → I s) ∧ Invariant P I :=
  ⟨fun ⟨seeds, carry⟩ => ⟨seeds, fun x a y st held => carry x y ⟨a, st⟩ held⟩,
   fun ⟨seeds, inv⟩ => ⟨seeds, fun x y ⟨a, st⟩ held => inv x a y st held⟩⟩

end Moves

/-! ## A local atlas is a process whose labels are its scopes -/

section Atlas

variable {Pos : Type u} {Sc : Type v}

/-- **A local atlas as a process.** Its labels are the scopes; a step under a scope is a local
edge between positions in that scope's domain. -/
def atlasProcess (atlas : WholeGroundCoverage.LocalAtlas Pos Sc) : Process Pos Sc :=
  ⟨fun p i q => WholeGroundCoverage.ScopedEdge atlas i p q⟩

/-- One scope's local edges alone, as a process. -/
def scopeProcess (atlas : WholeGroundCoverage.LocalAtlas Pos Sc) (i : Sc) : Process Pos Unit :=
  ⟨fun p _ q => WholeGroundCoverage.ScopedEdge atlas i p q⟩

/-- The joined edges of an atlas are the moves of its process. -/
theorem joined_iff_moves (atlas : WholeGroundCoverage.LocalAtlas Pos Sc) (p q : Pos) :
    WholeGroundCoverage.JoinedEdge atlas p q ↔ Moves (atlasProcess atlas) p q :=
  Iff.rfl

/-- One scope's edges are the moves of its process. -/
theorem scoped_iff_moves (atlas : WholeGroundCoverage.LocalAtlas Pos Sc) (i : Sc) (p q : Pos) :
    WholeGroundCoverage.ScopedEdge atlas i p q ↔ Moves (scopeProcess atlas i) p q :=
  ⟨fun e => ⟨(), e⟩, fun ⟨_, e⟩ => e⟩

/-- **What one scope's edges reach from a seed, the atlas's process reaches.** -/
theorem scope_reach_in_atlas (atlas : WholeGroundCoverage.LocalAtlas Pos Sc) (i : Sc)
    {seed : Pos → Prop} {p : Pos} (reached : FromSeed (scopeProcess atlas i) seed p) :
    FromSeed (atlasProcess atlas) seed p :=
  (reached_iff (joined_iff_moves atlas)).mp
    (WholeGroundCoverage.local_reach_in_joined atlas i
      ((reached_iff (scoped_iff_moves atlas i)).mpr reached))

/-- **Grounds compatible on overlaps and carried by every local edge hold wherever the atlas's
process reaches from grounded seeds.** -/
theorem glued_on_reach {atlas : WholeGroundCoverage.LocalAtlas Pos Sc} {seed : Pos → Prop}
    {Ground : (i : Sc) → {p : Pos // atlas.domain i p} → Prop}
    (compatible : WholeGroundCoverage.CompatibleGrounds atlas Ground)
    (carried : ∀ i p q, atlas.edge i p q → Ground i p → Ground i q)
    (seeds : ∀ p, seed p → WholeGroundCoverage.GluedGround atlas Ground p) {p : Pos}
    (reached : FromSeed (atlasProcess atlas) seed p) :
    WholeGroundCoverage.GluedGround atlas Ground p :=
  WholeGroundCoverage.jointly_grounded_scope_inheritance compatible carried seeds
    ((reached_iff (joined_iff_moves atlas)).mpr reached)

end Atlas

open WholeGroundCoverage in
/-- **Alternating scopes reach beyond each scope.** The process of the alternating atlas reaches
the finish from the start, and neither scope's edges alone reach it. -/
theorem alternating_beyond_scopes :
    FromSeed (atlasProcess alternatingAtlas) firstSeed .finish ∧
      ¬ FromSeed (scopeProcess alternatingAtlas .first) firstSeed .finish ∧
      ¬ FromSeed (scopeProcess alternatingAtlas .second) firstSeed .finish :=
  match alternating_beyond_separate_closures with
  | ⟨joined, first, second⟩ =>
    ⟨(reached_iff (joined_iff_moves alternatingAtlas)).mp joined,
     fun reached => first ((reached_iff (scoped_iff_moves alternatingAtlas .first)).mpr reached),
     fun reached => second ((reached_iff (scoped_iff_moves alternatingAtlas .second)).mpr reached)⟩

open WholeGroundCoverage in
/-- **Covering every position by a scope does not give reach.** In the unconnected atlas every
position lies in a scope's domain and a seed exists, yet its process does not reach the finish
from a seed. -/
theorem unconnected_coverage_insufficient :
    (∀ p, ∃ i, unconnectedAtlas.domain i p) ∧ (∃ p, firstSeed p) ∧
      ¬ FromSeed (atlasProcess unconnectedAtlas) firstSeed .finish :=
  match local_domain_coverage_insufficient with
  | ⟨cover, seeded, unreached⟩ =>
    ⟨cover, seeded,
     fun reached => unreached ((reached_iff (joined_iff_moves unconnectedAtlas)).mpr reached)⟩

/-! ## Histories -/

section Histories

variable {History : Type u} {Position : History → Type v} {Scope : History → Type w}

/-- **A family of atlases indexed by histories as one process** on the positions of every history:
a step is a joined edge within one history. -/
def historyProcess (atlas : (h : History) → WholeGroundCoverage.LocalAtlas (Position h) (Scope h)) :
    Process (Sigma Position) Unit :=
  ⟨fun x _ y => WholeGroundCoverage.HistoryEdge atlas x y⟩

theorem history_iff_moves (atlas : (h : History) → WholeGroundCoverage.LocalAtlas (Position h) (Scope h))
    (x y : Sigma Position) :
    WholeGroundCoverage.HistoryEdge atlas x y ↔ Moves (historyProcess atlas) x y :=
  ⟨fun e => ⟨(), e⟩, fun ⟨_, e⟩ => e⟩

/-- **No path of the process of a family of atlases leaves a history.** -/
theorem history_reach_keeps
    {atlas : (h : History) → WholeGroundCoverage.LocalAtlas (Position h) (Scope h)}
    {x y : Sigma Position} (path : Reach (historyProcess atlas) x y) : x.fst = y.fst :=
  Invariant.reach (P := historyProcess atlas) (I := fun z => x.fst = z.fst)
    (fun _ _ _ e same => same.trans (WholeGroundCoverage.history_edge_preserves_history e))
    path rfl

/-- **The process of a family of atlases reaches a position of a history from a seed exactly
where that history's atlas process reaches it from a seed of that history.** -/
theorem history_fromSeed_iff
    (atlas : (h : History) → WholeGroundCoverage.LocalAtlas (Position h) (Scope h))
    (seed : Sigma Position → Prop) (h : History) (p : Position h) :
    FromSeed (historyProcess atlas) seed ⟨h, p⟩ ↔
      FromSeed (atlasProcess (atlas h)) (fun q => seed ⟨h, q⟩) p :=
  (reached_iff (history_iff_moves atlas)).symm.trans
    ((WholeGroundCoverage.history_reach_iff atlas seed h p).trans
      (reached_iff (joined_iff_moves (atlas h))))

/-- **A reason sound within each history holds wherever the process of the family reaches from
seeds it holds at.** -/
theorem history_sound_on_reach
    {atlas : (h : History) → WholeGroundCoverage.LocalAtlas (Position h) (Scope h)}
    {seed : Sigma Position → Prop} {Reason : (h : History) → Position h → Prop}
    (seeds : ∀ h p, seed ⟨h, p⟩ → Reason h p)
    (sound : ∀ h, WholeGroundCoverage.LocalSound (atlas h) (Reason h))
    {h : History} {p : Position h} (reached : FromSeed (historyProcess atlas) seed ⟨h, p⟩) :
    Reason h p :=
  WholeGroundCoverage.history_local_sound_gives_global seeds sound
    ((reached_iff (history_iff_moves atlas)).mpr reached)

end Histories

/-! ## Cuts -/

section Cuts

variable {S : Type u} {A : Type v}

open UniversalEthics.CutCoverageAudit

/-- A reverse-closed cut avoiding the seeds and holding `t` is the complement of a property
separating `t` from the seeds. -/
theorem hasCut_iff_separated {P : Process S A} {seed : S → Prop} {t : S} :
    HasCut seed (Moves P) t ↔ Separated P seed t :=
  ⟨fun ⟨cut, held, avoids, closed⟩ =>
    ⟨fun x => ¬ cut x, avoids, fun x a y step clear inside => clear (closed x y ⟨a, step⟩ inside),
     fun clear => clear held⟩,
   fun ⟨I, seeds, inv, fails⟩ =>
    ⟨fun x => ¬ I x, fails, fun x held fails' => fails' (seeds x held),
     fun x y ⟨a, step⟩ fails' held => fails' (inv x a y step held)⟩⟩

/-- **A reverse-closed cut avoiding the seeds and holding `t` exists exactly where the process does
not reach `t` from a seed.** -/
theorem cut_iff_not_fromSeed {P : Process S A} {seed : S → Prop} {t : S} :
    HasCut seed (Moves P) t ↔ ¬ FromSeed P seed t :=
  hasCut_iff_separated.trans separated_iff_not_fromSeed

/-- **Where reach from a seed is decided, no cut exists exactly where it is reached.** -/
theorem noCut_iff_fromSeed_of_decidable {P : Process S A} {seed : S → Prop} {t : S}
    (decision : Decidable (FromSeed P seed t)) : NoCut seed (Moves P) t ↔ FromSeed P seed t :=
  ⟨fun none => (fromSeed_iff_not_separated_of_decidable decision).mpr
      (fun separated => none (hasCut_iff_separated.mpr separated)),
   fun reached cut => cut_iff_not_fromSeed.mp cut reached⟩

end Cuts

open UniversalEthics.CutCoverageAudit in
/-- **Absence of a cut gives reach in every process exactly where double-negation elimination
holds**: the core's `fromSeed_of_not_separated_iff_dne`, a cut being the complement of a
separating property. -/
theorem upgrade_iff_dne :
    (∀ (S A : Type u) (P : Process S A) (seed : S → Prop) (t : S),
        NoCut seed (Moves P) t → FromSeed P seed t) ↔ DoubleNegationElimination :=
  ⟨fun upgrade => fromSeed_of_not_separated_iff_dne.{u}.mp
      (fun S A P seed t joined =>
        upgrade S A P seed t (fun cut => joined (hasCut_iff_separated.mp cut))),
   fun dne S A P seed t none => fromSeed_of_not_separated_iff_dne.{u}.mpr dne S A P seed t
      (fun separated => none (hasCut_iff_separated.mpr separated))⟩

/-! ## Chains of small steps between profiles -/

section Profiles

variable {Gen Prof : Type}

/-- **Living significance of the reachable occurrences, along the process of small steps.** Under
supervenience, S0 and tolerance, where the profile of every reachable living occurrence is reached
from that of an own living occurrence in the process whose steps are the small steps between
profiles, living significance holds on the frame of the reachable inventory with the standpoint's
significance as positive relevance. -/
theorem reachable_living_significance (s : EvaluatorGrounding.Standpoint Gen Prof)
    (val : Prof → Prop) (step : Prof → Prof → Prop) (sup : EvaluatorGrounding.Supervenes s val)
    (self : EvaluatorGrounding.SelfGood s) (tol : EvaluatorGrounding.Tolerant val step)
    (reach : ∀ g', s.reach g' → s.living g' →
      ∃ g, s.own g ∧ s.living g ∧ Reach (edgeProcess step) (s.prof g) (s.prof g')) :
    G0 (Frame.ofInventory (EvaluatorGrounding.reachableInventory s)) s.living
      (fun _ g => s.sig g) :=
  EvaluatorGrounding.self_good_derives_reachable_g0 s val step sup self tol
    (fun g' reached alive => match reach g' reached alive with
      | ⟨g, own, alive', path⟩ => ⟨g, own, alive', chain_iff_reach.mpr path⟩)

end Profiles

end SeedReachProcesses

/-- **The periphery's closure of seeds under edges is the seed–edge closure**: the edge process's
moves are the edges, so this is `SeedReachProcesses.reached_iff` there. -/
theorem reached_iff_closure {X : Type u} {seed : X → Prop} {edge : X → X → Prop} {x : X} :
    WholeGroundCoverage.Reached seed edge x ↔ Closure seed edge x :=
  SeedReachProcesses.reached_iff (P := edgeProcess edge)
    (fun _ _ => ⟨fun e => ⟨(), e⟩, fun ⟨_, e⟩ => e⟩)

/-- **The audit's closure of roots under edges is the seed–edge closure**, as
`SeedReachProcesses.cutReach_iff` at the edge process. -/
theorem cutReach_iff_closure {X : Type u} {seed : X → Prop} {edge : X → X → Prop} {x : X} :
    UniversalEthics.CutCoverageAudit.Reach seed edge x ↔ Closure seed edge x :=
  SeedReachProcesses.cutReach_iff (P := edgeProcess edge)
    (fun _ _ => ⟨fun e => ⟨(), e⟩, fun ⟨_, e⟩ => e⟩)

end Becoming
