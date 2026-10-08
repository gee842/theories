import RecurrentAssembly

/-!
One retained arrangement directs successive token transfers into another
connected arrangement. The same local law reads adjacent types, not a supplied
fitness or variant label. Rearrangement, copying, release and depletion belong
to one material-accounted history. Template accessibility, exact copying,
local support costs, sequential operation and a unit release cost are explicit
premises. This is not an RNA polymerase or an origin-of-copying derivation.
-/
namespace StructuralCopying
open RecurrentAssembly

structure Law where
  equal : Nat
  unequal : Nat
  deriving DecidableEq, Repr

def charge (law : Law) (previous : Option Bool) (x : Bool) : Nat :=
  match previous with
  | none => 1
  | some y => if y = x then law.equal else law.unequal

def cost (law : Law) : Option Bool → List Bool → Nat
  | _, [] => 0
  | previous, x::xs => charge law previous x + cost law (some x) xs

-- The supplied scan reads the retained template in its actual order. A failed
-- operation leaves the remaining instructions and partial strand available.
structure CopyState where
  previous : Option Bool
  pending : List Bool
  built : Strand
  supply : Supply
  deriving DecidableEq, Repr

def extend (s : Strand) (x : Bool) : Strand :=
  ⟨s.cells++[x], if s.cells.isEmpty then s.bonds else
     (s.cells.length-1,s.cells.length)::s.bonds⟩

def tick (law : Law) (s : CopyState) : CopyState :=
  match s.pending with
  | [] => s
  | x::xs =>
    let c := charge law s.previous x
    if x ∈ s.supply.pool ∧ c ≤ s.supply.free then
      ⟨some x, xs,
       extend s.built x,
       ⟨s.supply.pool.erase x,s.supply.free-c,s.supply.spent+c⟩⟩
    else s

def steps (law : Law) : Nat → CopyState → CopyState
  | 0, s => s
  | n+1, s => steps law n (tick law s)

def start (parent : Strand) (r : Supply) : CopyState :=
  ⟨none,parent.cells,⟨[],[]⟩,r⟩

def copy (law : Law) (parent : Strand) (r : Supply) : CopyState :=
  if parent.bonds = path parent.cells.length ∧ parent.cells ≠ [] then
    steps law parent.cells.length (start parent r)
  else start parent r

-- Release moves one unit into spent support; uncompleted material is retained.
def release (s : CopyState) : Bool × CopyState :=
  if s.pending = [] ∧ s.built.cells ≠ [] ∧ 0 < s.supply.free then
    (true,{s with supply := ⟨s.supply.pool,s.supply.free-1,s.supply.spent+1⟩})
  else (false,s)

def reproduce (law : Law) (parent : Strand) (r : Supply) : Bool × CopyState :=
  release (copy law parent r)

theorem tick_accounts (law : Law) (s : CopyState) :
    (tick law s).built.cells.length + (tick law s).supply.pool.length =
      s.built.cells.length+s.supply.pool.length ∧
    (tick law s).supply.free+(tick law s).supply.spent =
      s.supply.free+s.supply.spent := by
  unfold tick
  split
  · exact ⟨rfl,rfl⟩
  · dsimp only
    split
    · rename_i h
      have he := List.length_erase_of_mem h.1
      have hn := List.length_pos_iff.mpr (List.ne_nil_of_mem h.1)
      simp only [extend,List.length_append,List.length_singleton]
      omega
    · exact ⟨rfl,rfl⟩

theorem tick_keeps_template_order (law : Law) (s : CopyState) :
    (tick law s).built.cells ++ (tick law s).pending =
      s.built.cells ++ s.pending := by
  unfold tick
  split
  · rfl
  · dsimp only
    split <;> simp_all [extend,List.append_assoc]

theorem tick_preserves_tokens (law : Law) (s : CopyState) :
    (s.built.cells++s.supply.pool).Perm ((tick law s).built.cells++(tick law s).supply.pool) := by
  unfold tick
  split
  · exact List.Perm.refl _
  · dsimp only
    split
    · rename_i h
      simpa [extend,List.append_assoc] using (List.perm_cons_erase h.1).append_left s.built.cells
    · exact List.Perm.refl _

theorem steps_preserve_tokens (law : Law) (n : Nat) (s : CopyState) :
    (s.built.cells++s.supply.pool).Perm ((steps law n s).built.cells++(steps law n s).supply.pool) := by
  induction n generalizing s with
  | zero => exact List.Perm.refl _
  | succ n ih => exact (tick_preserves_tokens law s).trans (ih _)

theorem tick_preserves_path (law : Law) (s : CopyState)
    (h : s.built.bonds = path s.built.cells.length) :
    (tick law s).built.bonds = path (tick law s).built.cells.length := by
  unfold tick
  split
  · exact h
  · dsimp only
    split
    · simp only [extend,List.length_append,List.length_singleton,path]
      cases hs : s.built.cells <;> simp_all [path]
    · exact h

theorem steps_invariants (law : Law) (n : Nat) (s : CopyState) :
    (steps law n s).built.cells.length+(steps law n s).supply.pool.length =
      s.built.cells.length+s.supply.pool.length ∧
    (steps law n s).supply.free+(steps law n s).supply.spent =
      s.supply.free+s.supply.spent ∧
    (steps law n s).built.cells++(steps law n s).pending = s.built.cells++s.pending := by
  induction n generalizing s with
  | zero => exact ⟨rfl,rfl,rfl⟩
  | succ n ih =>
    obtain ⟨hm,hw,ho⟩ := ih (tick law s)
    obtain ⟨h1,h2⟩ := tick_accounts law s
    exact ⟨hm.trans h1,hw.trans h2,ho.trans (tick_keeps_template_order law s)⟩

theorem steps_preserve_path (law : Law) (n : Nat) (s : CopyState)
    (h : s.built.bonds = path s.built.cells.length) :
    (steps law n s).built.bonds = path (steps law n s).built.cells.length := by
  induction n generalizing s with
  | zero => exact h
  | succ n ih => exact ih _ (tick_preserves_path law s h)

-- The exact budget follows the physical order read; no return coefficient is input.
theorem supported_scan (law : Law) (word : List Bool) (previous : Option Bool)
    (built : Strand) (tail : List Bool) (free spent : Nat) :
    let t := steps law word.length
      ⟨previous,word,built,⟨word++tail,free+cost law previous word,spent⟩⟩
    t.pending = [] ∧ t.built.cells = built.cells++word ∧
      t.supply = ⟨tail,free,spent+cost law previous word⟩ := by
  induction word generalizing previous built free spent with
  | nil => simp [steps,cost]
  | cons x xs ih =>
    simp only [List.length_cons,steps,tick,List.cons_append,List.mem_cons, true_or,
      cost, List.erase_cons_head,extend]
    simp only [show charge law previous x ≤ free+(charge law previous x+cost law (some x) xs) by omega,
      and_self, ↓reduceIte]
    have ha : free+(charge law previous x+cost law (some x) xs)-charge law previous x =
        free+cost law (some x) xs := by omega
    rw [ha]
    obtain ⟨hp,hb,hs⟩ := ih (some x)
      ⟨built.cells++[x],if built.cells.isEmpty then built.bonds else
         (built.cells.length-1,built.cells.length)::built.bonds⟩ free (spent+charge law previous x)
    exact ⟨hp,by simpa [List.append_assoc] using hb,by simpa [Nat.add_assoc] using hs⟩

theorem copied_structure_inherits (law : Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ [])
    (tail : List Bool) (free spent : Nat) :
    let t := copy law parent ⟨parent.cells++tail,free+cost law none parent.cells,spent⟩
    t.pending = [] ∧ t.built = parent ∧
      t.supply = ⟨tail,free,spent+cost law none parent.cells⟩ := by
  simp only [copy, if_pos (And.intro hp hn), start]
  obtain ⟨h1,h2,h3⟩ := supported_scan law parent.cells none ⟨[],[]⟩ tail free spent
  have h4 := steps_preserve_path law parent.cells.length
    (⟨none,parent.cells,⟨[],[]⟩,⟨parent.cells++tail,free+cost law none parent.cells,spent⟩⟩ : CopyState) (by rfl)
  simp only [List.nil_append] at h2
  refine ⟨h1,?_,h3⟩
  have hb : (steps law parent.cells.length
    ⟨none,parent.cells,⟨[],[]⟩,⟨parent.cells++tail,free+cost law none parent.cells,spent⟩⟩).built.bonds = parent.bonds := by
    rw [h4,h2,hp]
  cases he : (steps law parent.cells.length
    ⟨none,parent.cells,⟨[],[]⟩,⟨parent.cells++tail,free+cost law none parent.cells,spent⟩⟩).built
  cases parent
  simp_all

theorem reproduction_inherits (law : Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ [])
    (tail : List Bool) (free spent : Nat) :
    let t := reproduce law parent
      ⟨parent.cells++tail,free+cost law none parent.cells+1,spent⟩
    t.1 = true ∧ t.2.built = parent ∧
      t.2.supply = ⟨tail,free,spent+cost law none parent.cells+1⟩ := by
  have h := copied_structure_inherits law parent hp hn tail (free+1) spent
  have he : free+cost law none parent.cells+1 = (free+1)+cost law none parent.cells := by omega
  simp only [reproduce,he,release]
  obtain ⟨h1,h2,h3⟩ := h
  simp [h1,h2,h3,hn]

theorem reproduction_accounts (law : Law) (parent : Strand) (r : Supply) :
    (reproduce law parent r).2.built.cells.length + (reproduce law parent r).2.supply.pool.length =
      r.pool.length ∧
    (reproduce law parent r).2.supply.free+(reproduce law parent r).2.supply.spent = r.free+r.spent := by
  have h : (copy law parent r).built.cells.length+(copy law parent r).supply.pool.length = r.pool.length ∧
      (copy law parent r).supply.free+(copy law parent r).supply.spent = r.free+r.spent := by
    unfold copy
    split
    · obtain ⟨a,b,_⟩ := steps_invariants law parent.cells.length (start parent r)
      exact ⟨by simpa [start] using a,by simpa [start] using b⟩
    · simp [start]
  unfold reproduce release
  split <;> simp_all <;> omega

theorem tick_cost_balance (law : Law) (s : CopyState) :
    (tick law s).supply.spent + cost law (tick law s).previous (tick law s).pending =
      s.supply.spent + cost law s.previous s.pending := by
  unfold tick
  split
  · rfl
  · dsimp only
    split <;> simp_all [cost,Nat.add_assoc]

theorem steps_cost_balance (law : Law) (n : Nat) (s : CopyState) :
    (steps law n s).supply.spent + cost law (steps law n s).previous (steps law n s).pending =
      s.supply.spent + cost law s.previous s.pending := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih => exact (ih (tick law s)).trans (tick_cost_balance law s)

theorem completed_copy_requires_cost (law : Law) (parent : Strand) (r : Supply)
    (h : (copy law parent r).pending = []) :
    (copy law parent r).supply.spent = r.spent + cost law none parent.cells := by
  unfold copy at h ⊢
  split
  · have hc := steps_cost_balance law parent.cells.length (start parent r)
    simp_all [start,cost]
  · simp_all [start,cost]

theorem exact_reproduction_budget (law : Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ [])
    (tail : List Bool) (budget spent : Nat) :
    (reproduce law parent ⟨parent.cells++tail,budget,spent⟩).1 = true ↔
      cost law none parent.cells+1 ≤ budget := by
  constructor
  · intro h
    simp only [reproduce,release] at h
    split at h
    · rename_i hr
      have hc := completed_copy_requires_cost law parent
        ⟨parent.cells++tail,budget,spent⟩ hr.1
      have hs : (copy law parent ⟨parent.cells++tail,budget,spent⟩).supply.free +
          (copy law parent ⟨parent.cells++tail,budget,spent⟩).supply.spent = budget+spent := by
        have hi := steps_invariants law parent.cells.length
          (start parent ⟨parent.cells++tail,budget,spent⟩)
        simpa [copy,hp,hn,start] using hi.2.1
      dsimp only at hc
      have hpos := hr.2.2
      omega
    · simp at h
  · intro hb
    have he : budget = (budget-(cost law none parent.cells+1))+cost law none parent.cells+1 := by omega
    rw [he]
    exact (reproduction_inherits law parent hp hn tail _ spent).1

-- Each new daughter continues the selected lineage; retained parents and
-- unsuccessful partial products remain in the resulting material account.
def descendants (law : Law) : Nat → Strand → Supply → List Strand × Supply
  | 0, p, r => ([p],r)
  | n+1, p, r =>
    let t := reproduce law p r
    if t.1 then
      let rest := descendants law n t.2.built t.2.supply
      (p::rest.1,rest.2)
    else ([p,t.2.built],t.2.supply)

def repeatedFeed (word : List Bool) : Nat → List Bool
  | 0 => []
  | n+1 => word++repeatedFeed word n

theorem finite_lineage_inherits (law : Law) (parent : Strand)
    (hp : parent.bonds = path parent.cells.length) (hn : parent.cells ≠ [])
    (n : Nat) (tail : List Bool) (free spent : Nat) :
    descendants law n parent
      ⟨repeatedFeed parent.cells n++tail,free+n*(cost law none parent.cells+1),spent⟩ =
      (List.replicate (n+1) parent,⟨tail,free,spent+n*(cost law none parent.cells+1)⟩) := by
  induction n generalizing free spent with
  | zero => simp [descendants,repeatedFeed]
  | succ n ih =>
    have he : free+(n+1)*(cost law none parent.cells+1) =
        (free+n*(cost law none parent.cells+1))+cost law none parent.cells+1 := by
      simp [Nat.add_mul]; omega
    simp only [descendants,repeatedFeed,List.append_assoc,he]
    obtain ⟨h1,h2,h3⟩ := reproduction_inherits law parent hp hn
      (repeatedFeed parent.cells n++tail) (free+n*(cost law none parent.cells+1)) spent
    rw [h1,if_pos rfl,h2,h3,ih]
    simp only [List.replicate_succ]
    congr 2
    omega

theorem lineage_accounts (law : Law) (n : Nat) (p : Strand) (r : Supply) :
    size (descendants law n p r).1+(descendants law n p r).2.pool.length = p.cells.length+r.pool.length ∧
    (descendants law n p r).2.free+(descendants law n p r).2.spent = r.free+r.spent := by
  induction n generalizing p r with
  | zero => simp [descendants,size]
  | succ n ih =>
    have h := reproduction_accounts law p r
    have hi := ih (reproduce law p r).2.built (reproduce law p r).2.supply
    simp only [descendants]
    split <;> simp only [size] <;> omega

-- Material exchange changes order, not component identities or the path domain.
def exchange (s : Strand) (r : Supply) : Strand × Supply :=
  match s.cells with
  | a::b::c::rest =>
    if 0 < r.free then (⟨a::c::b::rest,s.bonds⟩,⟨r.pool,r.free-1,r.spent+1⟩) else (s,r)
  | _ => (s,r)

theorem exchange_preserves_material (s : Strand) (r : Supply) :
    s.cells.Perm (exchange s r).1.cells ∧
    (exchange s r).2.pool = r.pool ∧
    (exchange s r).2.free+(exchange s r).2.spent = r.free+r.spent := by
  unfold exchange
  split
  · split
    · refine ⟨?_,rfl,?_⟩
      · simp_all only
        exact List.Perm.cons _ (List.Perm.swap _ _ _)
      · simp; omega
    · exact ⟨List.Perm.refl _,rfl,rfl⟩
  · exact ⟨List.Perm.refl _,rfl,rfl⟩

theorem exchange_preserves_path (s : Strand) (r : Supply) (hp : s.bonds = path s.cells.length) :
    (exchange s r).1.bonds = path (exchange s r).1.cells.length := by
  unfold exchange
  split
  · split <;> simp_all
  · exact hp

def alternating : Strand := ⟨[false,true,false,true],path 4⟩
def clustered : Strand := ⟨[false,false,true,true],path 4⟩
def mixed : Strand := ⟨[false,true,true,false],path 4⟩
def alternatingEasy : Law := ⟨2,1⟩
def clusteredEasy : Law := ⟨1,2⟩
def feed : List Bool := [false,false,true,true]

theorem previous_fragment_is_template :
    RecurrentAssembly.fragment RecurrentAssembly.mature 0 4 = alternating := by decide

theorem actual_exchange_forms_variant :
    exchange alternating ⟨[],1,0⟩ = (clustered,⟨[],0,1⟩) := by decide

theorem formed_variant_enters_copying :
    let changed := exchange alternating ⟨feed,8,0⟩
    let result := reproduce alternatingEasy changed.1 changed.2
    result.1 = true ∧ result.2.built = clustered ∧ result.2.supply = ⟨[],0,8⟩ := by decide

theorem inherited_variant_changes_cost (law : Law) :
    cost law none alternating.cells = 1+3*law.unequal ∧
    cost law none clustered.cells = 1+2*law.equal+law.unequal := by
  simp [cost,charge,alternating,clustered]; omega

theorem exact_local_ranking (law : Law) :
    cost law none alternating.cells < cost law none clustered.cells ↔ law.unequal < law.equal := by
  obtain ⟨a,b⟩ := inherited_variant_changes_cost law
  rw [a,b]; omega

-- Once the two local costs are fixed, the third arrangement is constrained.
-- Independent per-variant costs need not satisfy this held-out relation.
theorem third_structure_cost_constraint (law : Law) :
    2 * (cost law none mixed.cells+1) =
      (cost law none alternating.cells+1)+(cost law none clustered.cells+1) := by
  simp [cost,charge,mixed,alternating,clustered]; omega

theorem two_costs_determine_third (a b : Law)
    (ha : cost a none alternating.cells = cost b none alternating.cells)
    (hb : cost a none clustered.cells = cost b none clustered.cells) :
    cost a none mixed.cells = cost b none mixed.cells := by
  have h1 := third_structure_cost_constraint a
  have h2 := third_structure_cost_constraint b
  omega

theorem equal_census_different_organization :
    alternating.cells.Perm clustered.cells ∧ alternating.bonds = clustered.bonds ∧
      alternating.cells ≠ clustered.cells := by decide

theorem inherited_variant_reproduces :
    (reproduce alternatingEasy clustered ⟨feed,7,0⟩).1 = true ∧
    (reproduce alternatingEasy clustered ⟨feed,7,0⟩).2.built = clustered ∧
    (reproduce alternatingEasy
      (reproduce alternatingEasy clustered ⟨feed,7,0⟩).2.built ⟨feed,7,7⟩).1 = true := by decide

theorem common_budget_discriminates :
    (reproduce alternatingEasy alternating ⟨feed,5,0⟩).1 = true ∧
    (reproduce alternatingEasy clustered ⟨feed,5,0⟩).1 = false ∧
    (reproduce alternatingEasy clustered ⟨feed,5,0⟩).2.built.cells = [false,false,true] ∧
    (reproduce alternatingEasy clustered ⟨feed,5,0⟩).2.supply = ⟨[true],1,4⟩ := by decide

theorem changed_local_law_reverses_advantage :
    (reproduce clusteredEasy clustered ⟨feed,6,0⟩).1 = true ∧
    (reproduce clusteredEasy alternating ⟨feed,6,0⟩).1 = false := by decide

-- A built daughter can still be unreleased: the census cannot erase this state.
theorem full_copy_need_not_be_released :
    (reproduce alternatingEasy alternating ⟨feed,4,0⟩).2.built = alternating ∧
    (reproduce alternatingEasy alternating ⟨feed,4,0⟩).1 = false := by decide

def batch (law : Law) : List Strand → Supply → List (Bool × Strand) × Supply
  | [], r => ([],r)
  | p::ps, r =>
    let t := reproduce law p r
    let rest := batch law ps t.2.supply
    ((t.1,t.2.built)::rest.1,rest.2)

def made : List (Bool × Strand) → Nat
  | [] => 0
  | p::ps => p.2.cells.length+made ps

theorem batch_accounts (law : Law) (ps : List Strand) (r : Supply) :
    made (batch law ps r).1+(batch law ps r).2.pool.length = r.pool.length ∧
    (batch law ps r).2.free+(batch law ps r).2.spent = r.free+r.spent := by
  induction ps generalizing r with
  | nil => simp [batch,made]
  | cons p ps ih =>
    have h := reproduction_accounts law p r
    have hi := ih (reproduce law p r).2.supply
    simp only [batch,made]
    omega

theorem shared_supply_order_matters :
    ((batch alternatingEasy [alternating,clustered] ⟨feed++feed,9,0⟩).1.map Prod.fst) = [true,false] ∧
    ((batch alternatingEasy [clustered,alternating] ⟨feed++feed,9,0⟩).1.map Prod.fst) = [true,false] := by decide

-- No function of component counts and path alone can recover both outcomes.
def census (s : Strand) : Nat × Nat × List Edge :=
  (s.cells.count false,s.cells.count true,s.bonds)

theorem no_census_only_completion :
    ¬ ∃ f : (Nat × Nat × List Edge) → Bool,
      f (census alternating) = (reproduce alternatingEasy alternating ⟨feed,5,0⟩).1 ∧
      f (census clustered) = (reproduce alternatingEasy clustered ⟨feed,5,0⟩).1 := by
  rintro ⟨f,ha,hb⟩
  have he : census alternating = census clustered := by decide
  rw [he] at ha
  have ht := common_budget_discriminates
  rw [ht.1] at ha
  rw [ht.2.1] at hb
  simp_all

end StructuralCopying
