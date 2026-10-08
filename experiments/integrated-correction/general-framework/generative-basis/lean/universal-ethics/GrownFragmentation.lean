import MaterialMaturation

/-!
Local division forms the graph whose actual cuts determine transmitted pools.
Alternating daughter differentiation, event order, cut occurrence, reaction
opportunities along retained edges, finite stocks and the old routing recipe
are declared local laws. No mechanical force or universal tree law is claimed.
-/
namespace GrownFragmentation

abbrev Edge := Nat × Nat

structure Growing where
  body : DevelopmentalAssociation.State
  kind : Nat → Bool

def enabled (s : Growing) (p : Nat) : Bool :=
  decide (p < s.body.count ∧ 0 < s.body.precursor ∧ 0 < s.body.available)

def birth (s : Growing) (p : Nat) : Growing :=
  match DevelopmentalAssociation.divide s.body p with
  | none => s
  | some t => ⟨t, fun i => if i = s.body.count then !s.kind p else s.kind i⟩

def develop : List Nat → Growing → Growing
  | [], s => s
  | p::ps, s => develop ps (birth s p)

def legal : List Nat → Growing → Bool
  | [], _ => true
  | p::ps, s => enabled s p && legal ps (birth s p)

theorem enabled_birth (s : Growing) (p : Nat) (h : enabled s p = true) :
    DevelopmentalAssociation.divide s.body p = some (birth s p).body := by
  simp only [enabled, decide_eq_true_eq] at h
  simp [birth, DevelopmentalAssociation.divide, h]

theorem actual_development (ps : List Nat) (s : Growing) (h : legal ps s = true) :
    DevelopmentalAssociation.run (ps.map DevelopmentalAssociation.Event.divide) s.body =
      some (develop ps s).body := by
  induction ps generalizing s with
  | nil => rfl
  | cons p ps ih =>
    simp only [legal, Bool.and_eq_true] at h
    simp only [List.map_cons, DevelopmentalAssociation.run, DevelopmentalAssociation.step,
      enabled_birth s p h.1, Option.bind_some, develop]
    exact ih _ h.2

theorem development_accounts (ps : List Nat) (s : Growing) (h : legal ps s = true) :
    DevelopmentalAssociation.material (develop ps s).body = DevelopmentalAssociation.material s.body ∧
    (develop ps s).body.available + (develop ps s).body.spent = s.body.available + s.body.spent ∧
    ps.length + (develop ps s).body.available = s.body.available := by
  have ht := (DevelopmentalAssociation.run_iff_core_trace _ _ _).mp (actual_development ps s h)
  simpa using DevelopmentalAssociation.core_trace_accounts ht

theorem daughter_differentiates (s : Growing) (p : Nat) (h : enabled s p = true) :
    (birth s p).kind s.body.count = !s.kind p := by
  simp only [enabled, decide_eq_true_eq] at h
  simp [birth, DevelopmentalAssociation.divide, h]

def initial : Growing :=
  ⟨⟨1,7,9,0,fun _ => true,fun _ => 0,[]⟩,fun _ => false⟩

def chainWord : List Nat := [0,1,2,3,4,5,6]
def branchedWord : List Nat := [0,0,0,0,1,1,1]
def chain : Growing := develop chainWord initial
def branched : Growing := develop branchedWord initial

theorem histories_legal : legal chainWord initial = true ∧ legal branchedWord initial = true := by
  decide +kernel

theorem grown_observations :
    (chain.body.count, chain.body.precursor, chain.body.available, chain.body.spent) = (8,0,2,7) ∧
    (branched.body.count, branched.body.precursor, branched.body.available, branched.body.spent) = (8,0,2,7) ∧
    (List.range 8).map chain.kind = [false,true,false,true,false,true,false,true] ∧
    (List.range 8).map branched.kind = [false,true,true,true,true,false,false,false] ∧
    chain.body.bonds = [(6,7),(5,6),(4,5),(3,4),(2,3),(1,2),(0,1)] ∧
    branched.body.bonds = [(1,7),(1,6),(1,5),(0,4),(0,3),(0,2),(0,1)] := by
  decide +kernel

def neighbors (es : List Edge) (v : Nat) : List Nat :=
  es.flatMap (fun e => if e.1 = v then [e.2] else if e.2 = v then [e.1] else [])

theorem neighbor_connected {es : List Edge} {a b : Nat} (h : b ∈ neighbors es a) :
    DevelopmentalAssociation.Connected es a b := by
  simp only [neighbors, List.mem_flatMap] at h
  obtain ⟨⟨x,y⟩, he, hb⟩ := h
  dsimp at hb
  split at hb
  · simp_all
    exact .bond he
  · split at hb
    · simp_all
      exact .symm (.bond he)
    · simp_all

/-- Bounded graph traversal. Completeness is certified below, not presumed
    merely because a traversal budget was chosen. -/
def flood (es : List Edge) : Nat → List Nat → List Nat → List Nat
  | 0, _, seen => seen
  | _+1, [], seen => seen
  | n+1, v::todo, seen =>
      if v ∈ seen then flood es n todo seen
      else flood es n (todo ++ neighbors es v) (v::seen)

theorem flood_sound (es : List Edge) (r n : Nat) (todo seen : List Nat)
    (ht : ∀ v ∈ todo, DevelopmentalAssociation.Connected es r v)
    (hs : ∀ v ∈ seen, DevelopmentalAssociation.Connected es r v) :
    ∀ v ∈ flood es n todo seen, DevelopmentalAssociation.Connected es r v := by
  induction n generalizing todo seen with
  | zero => exact hs
  | succ n ih =>
    cases todo with
    | nil => exact hs
    | cons v todo =>
      simp only [flood]
      split
      · exact ih todo seen (fun x hx => ht x (by simp [hx])) hs
      · apply ih
        · intro x hx
          rcases List.mem_append.mp hx with old | fresh
          · exact ht x (by simp [old])
          · exact .trans (ht v (by simp)) (neighbor_connected fresh)
        · intro x hx
          rcases List.mem_cons.mp hx with rfl | old
          · exact ht x (by simp)
          · exact hs x old

def component (count : Nat) (es : List Edge) (r : Nat) : List Nat :=
  (List.range count).filter (fun v => (flood es (2*es.length+1) [r] []).contains v)

theorem component_sound {count : Nat} {es : List Edge} {r v : Nat}
    (h : v ∈ component count es r) : DevelopmentalAssociation.Connected es r v := by
  have hm := (List.mem_filter.mp h).2
  simp only [List.contains_iff_mem] at hm
  exact flood_sound es r _ [r] [] (by intro x hx; simp only [List.mem_singleton] at hx; subst x; exact .refl r)
    (by simp) v hm

/-- Closure is checked on every represented edge; this plus soundness certifies
    an exact component even when a generic traversal completeness bound is absent. -/
def closed (es : List Edge) (xs : List Nat) : Bool :=
  es.all (fun e => xs.contains e.1 == xs.contains e.2)

theorem connected_same_side {es : List Edge} {xs : List Nat} {a b : Nat}
    (hc : closed es xs = true) (h : DevelopmentalAssociation.Connected es a b) :
    a ∈ xs ↔ b ∈ xs := by
  induction h with
  | refl => rfl
  | bond he =>
    have hh := List.all_eq_true.mp hc _ he
    simpa using hh
  | symm _ ih => exact ih.symm
  | trans _ _ ih1 ih2 => exact ih1.trans ih2

theorem certified_component {count : Nat} {es : List Edge} {r v : Nat}
    (hr : r ∈ component count es r) (hc : closed es (component count es r) = true) :
    v ∈ component count es r ↔ DevelopmentalAssociation.Connected es r v := by
  constructor
  · exact component_sound
  · intro h
    exact (connected_same_side hc h).mp hr

def cutEdges (es : List Edge) (e : Edge) : List Edge := es.filter (fun f => f != e)

def cut (s : Growing) (e : Edge) : Option Growing :=
  (DevelopmentalAssociation.detach s.body e.1 e.2).map (fun t => ⟨t,s.kind⟩)

theorem cut_accounts {s t : Growing} {e : Edge} (h : cut s e = some t) :
    t.body.count = s.body.count ∧ t.kind = s.kind ∧
    t.body.bonds = cutEdges s.body.bonds e ∧
    t.body.available + 1 = s.body.available ∧ t.body.spent = s.body.spent+1 := by
  unfold cut DevelopmentalAssociation.detach at h
  split at h
  · rename_i enabled
    simp only [Option.map_some, Option.some.injEq] at h
    cases h
    simp only [cutEdges, true_and, and_true]
    omega
  · cases h

def cutComponents (s : Growing) (e : Edge) : List (List Nat) :=
  [component s.body.count (cutEdges s.body.bonds e) e.1,
   component s.body.count (cutEdges s.body.bonds e) e.2]

def cutCertificate (s : Growing) (e : Edge) : Bool :=
  let es := cutEdges s.body.bonds e
  let a := component s.body.count es e.1
  let b := component s.body.count es e.2
  a.contains e.1 && b.contains e.2 && closed es a && closed es b &&
  (List.range s.body.count).all (fun i => a.contains i != b.contains i)

theorem certificate_exact_split {s : Growing} {e : Edge} (h : cutCertificate s e = true) :
    (∀ v, v ∈ component s.body.count (cutEdges s.body.bonds e) e.1 ↔
      DevelopmentalAssociation.Connected (cutEdges s.body.bonds e) e.1 v) ∧
    (∀ v, v ∈ component s.body.count (cutEdges s.body.bonds e) e.2 ↔
      DevelopmentalAssociation.Connected (cutEdges s.body.bonds e) e.2 v) ∧
    (∀ v < s.body.count,
      (v ∈ component s.body.count (cutEdges s.body.bonds e) e.1 ↔
       v ∉ component s.body.count (cutEdges s.body.bonds e) e.2)) := by
  simp only [cutCertificate, Bool.and_eq_true, List.contains_iff_mem] at h
  obtain ⟨⟨⟨⟨ha,hb⟩,ca⟩,cb⟩,cover⟩ := h
  refine ⟨fun v => certified_component ha ca,fun v => certified_component hb cb,?_⟩
  intro v hv
  have hvv := List.all_eq_true.mp cover v (List.mem_range.mpr hv)
  simp at hvv
  grind

theorem every_tree_cut_certified :
    chain.body.bonds.all (cutCertificate chain) = true ∧
    branched.body.bonds.all (cutCertificate branched) = true := by decide +kernel

theorem central_cut_pools :
    cutComponents chain (3,4) = [[0,1,2,3],[4,5,6,7]] ∧
    cutComponents branched (0,1) = [[0,2,3,4],[1,5,6,7]] := by decide +kernel

theorem only_equal_tree_cuts :
    chain.body.bonds.filter (fun e => (cutComponents chain e).all (fun xs => xs.length == 4)) = [(3,4)] ∧
    branched.body.bonds.filter (fun e => (cutComponents branched e).all (fun xs => xs.length == 4)) = [(0,1)] := by decide +kernel

/-- Mechanical retention and catalytic contact are different roles of a
    surviving edge in this supplied local model. No new mechanical bond is
    claimed to be created by the later catalytic encounter. -/
def seeds (s : Growing) (e : Edge) : List ContactReconstruction.Seed :=
  (cutComponents s e).map (fun xs => ContactReconstruction.transmit xs (cutEdges s.body.bonds e))

def joined (s : Growing) (seed : ContactReconstruction.Seed) : Rat :=
  ContactReconstruction.expected s.kind seed 2
    (fun t => if t.bond.isSome then MaterialMaturation.growReturn false (seed.members.map s.kind) else 0)
    ⟨2,0,none⟩

def cutReturn (s : Growing) (e : Edge) : Option Rat :=
  if (cut s e).isSome && cutCertificate s e then
    some (ContactReconstruction.total (joined s) (seeds s e)) else none

theorem joined_factorization (s : Growing) (seed : ContactReconstruction.Seed)
    (hne : seed.contacts.length ≠ 0) :
    joined s seed = AssemblyDerivedSelection.success (ContactReconstruction.rate s.kind seed) 2 *
      MaterialMaturation.growReturn false (seed.members.map s.kind) := by
  unfold joined
  have he : (fun t : ContactReconstruction.State => if t.bond.isSome then
      MaterialMaturation.growReturn false (seed.members.map s.kind) else 0) =
      (fun t => ContactReconstruction.reconstructed t *
        MaterialMaturation.growReturn false (seed.members.map s.kind)) := by
    funext t
    unfold ContactReconstruction.reconstructed
    split <;> grind
  rw [he,MaterialMaturation.contact_expected_scale]
  rw [ContactReconstruction.reconstruction_from_contacts _ _ hne 2 2 (by decide)]

theorem central_seed_properties :
    (seeds chain (3,4)).map (ContactReconstruction.rate chain.kind) = [1,1] ∧
    (seeds branched (0,1)).map (ContactReconstruction.rate branched.kind) = [1,1] ∧
    (seeds chain (3,4)).map (fun s => ((s.members.map chain.kind).count false,(s.members.map chain.kind).count true)) = [(2,2),(2,2)] ∧
    (seeds branched (0,1)).map (fun s => ((s.members.map branched.kind).count false,(s.members.map branched.kind).count true)) = [(1,3),(3,1)] := by decide +kernel

def countJoined (s : Growing) (seed : ContactReconstruction.Seed) : Rat :=
  if seed.contacts.isEmpty then 0 else
    AssemblyDerivedSelection.success (ContactReconstruction.rate s.kind seed) 2 *
    MaterialMaturation.countExpected false 4 MaterialMaturation.balanced
      ((seed.members.map s.kind).count false) ((seed.members.map s.kind).count true)

theorem joined_projection (s : Growing) (seed : ContactReconstruction.Seed) :
    joined s seed = countJoined s seed := by
  by_cases he : seed.contacts = []
  · simp [joined,countJoined,ContactReconstruction.expected,he]
  · have hn : seed.contacts.length ≠ 0 := by simpa using he
    rw [joined_factorization s seed hn]
    have hg : MaterialMaturation.growReturn false (seed.members.map s.kind) =
        MaterialMaturation.countExpected false 4 MaterialMaturation.balanced
          ((seed.members.map s.kind).count false) ((seed.members.map s.kind).count true) := by
      by_cases hm : seed.members.map s.kind = []
      · rw [hm]
        decide +kernel
      · exact MaterialMaturation.return_from_composition false _ hm
    rw [hg]
    simp [countJoined,he]

def countCutReturn (s : Growing) (e : Edge) : Option Rat :=
  if (cut s e).isSome && cutCertificate s e then
    some (ContactReconstruction.total (countJoined s) (seeds s e)) else none

theorem cut_return_projection (s : Growing) (e : Edge) :
    cutReturn s e = countCutReturn s e := by
  have h : joined s = countJoined s := by funext seed; exact joined_projection s seed
  simp only [cutReturn,countCutReturn,h]

theorem all_cut_returns :
    chain.body.bonds.map (cutReturn chain) = [some 0,some 0,some 0,some (18/35),some 0,some 0,some 0] ∧
    branched.body.bonds.map (cutReturn branched) = [some 0,some 0,some 0,some 0,some 0,some 0,some (6/35)] := by
  have h (s : Growing) : cutReturn s = countCutReturn s := by
    funext e; exact cut_return_projection s e
  rw [h chain,h branched]
  decide +kernel

theorem central_returns : cutReturn chain (3,4) = some (18/35) ∧
    cutReturn branched (0,1) = some (6/35) := by
  rw [cut_return_projection,cut_return_projection]
  decide +kernel

def meanCutReturn (s : Growing) : Rat :=
  ContactReconstruction.total (fun e => (cutReturn s e).getD 0) s.body.bonds / s.body.bonds.length

/-- This average applies to the two certified trees under a supplied uniform
    choice of one actual edge. getD does not assign fitness to uncertified cuts. -/
theorem uniform_cut_returns : meanCutReturn chain = 18/245 ∧ meanCutReturn branched = 6/245 := by
  have h (s : Growing) : (fun e => (cutReturn s e).getD 0) =
      (fun e => (countCutReturn s e).getD 0) := by
    funext e; rw [cut_return_projection]
  simp only [meanCutReturn,h]
  decide +kernel

theorem fragmentation_changes_prepared_return :
    meanCutReturn chain = 3*meanCutReturn branched ∧ meanCutReturn branched > 0 := by
  obtain ⟨h1,h2⟩ := uniform_cut_returns
  rw [h1,h2]
  decide +kernel

def oldestReturn (s : Growing) : Option Rat :=
  s.body.bonds.getLast?.bind (cutReturn s)

theorem oldest_cut_reverses_ranking :
    oldestReturn chain = some 0 ∧ oldestReturn branched = some (6/35) ∧
    meanCutReturn branched < meanCutReturn chain := by
  have h (s : Growing) : cutReturn s = countCutReturn s := by
    funext e; exact cut_return_projection s e
  refine ⟨?_,?_,?_⟩
  · simp only [oldestReturn,h]
    decide +kernel
  · simp only [oldestReturn,h]
    decide +kernel
  · obtain ⟨h1,h2⟩ := uniform_cut_returns
    rw [h1,h2]
    decide +kernel

def parentSummary (s : Growing) : Nat × Nat × Nat × Nat :=
  (((List.range s.body.count).map s.kind).count false,
   ((List.range s.body.count).map s.kind).count true,s.body.bonds.length,s.body.spent)

theorem matched_parent_summaries :
    parentSummary chain = (4,4,7,7) ∧ parentSummary branched = (4,4,7,7) := by decide +kernel

theorem no_parent_summary_predictor :
    ¬∃ f : (Nat × Nat × Nat × Nat) → Rat,
      meanCutReturn chain = f (parentSummary chain) ∧
      meanCutReturn branched = f (parentSummary branched) := by
  obtain ⟨h1,h2⟩ := matched_parent_summaries
  obtain ⟨r1,r2⟩ := uniform_cut_returns
  rw [h1,h2,r1,r2]
  intro ⟨f,ha,hb⟩
  grind

/-- One additional effective retention relation. aggregate is a native graph
    operation; it is not a physical model of entanglement formation. -/
def reinforced : Growing :=
  ⟨(DevelopmentalAssociation.aggregate chain.body 0 7).getD chain.body,chain.kind⟩

theorem reinforcement_is_actual :
    DevelopmentalAssociation.aggregate chain.body 0 7 = some reinforced.body := by
  simp [reinforced,DevelopmentalAssociation.aggregate,chain,chainWord,develop,birth,
    DevelopmentalAssociation.divide,initial]

theorem bypass_survives_cut :
    component reinforced.body.count (cutEdges reinforced.body.bonds (3,4)) 3 = List.range 8 ∧
    component reinforced.body.count (cutEdges reinforced.body.bonds (3,4)) 4 = List.range 8 ∧
    closed (cutEdges reinforced.body.bonds (3,4)) (List.range 8) = true ∧
    cutCertificate reinforced (3,4) = false ∧ cutReturn reinforced (3,4) = none := by
  rw [cut_return_projection]
  decide +kernel

theorem bypass_really_connects :
    DevelopmentalAssociation.Connected (cutEdges reinforced.body.bonds (3,4)) 3 4 := by
  apply component_sound (count := 8)
  decide +kernel

theorem cut_spends_without_fragmenting :
    ((cut reinforced (3,4)).map (fun t => (t.body.count,t.body.available,t.body.spent))) = some (8,0,9) ∧
    ((cut chain (3,4)).map (fun t => (t.body.count,t.body.available,t.body.spent))) = some (8,1,8) := by
  decide +kernel

end GrownFragmentation
