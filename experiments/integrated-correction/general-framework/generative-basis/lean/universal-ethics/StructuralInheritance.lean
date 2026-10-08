import RecurrentAssembly

/-!
Structural differences change attachment under one fixed local interaction.
The next admitted token is the penultimate token of the actual strand; there
is no inherited rule tag or assigned reproductive fitness. Cleavage retains
actual components and internal edges. Perturbation is an accounted exchange.
This is an abstract two-token templating law, not a molecular model.
-/
namespace StructuralInheritance
open RecurrentAssembly (Strand Supply path fragment size size_append required)

def wanted (s : Strand) : Bool :=
  match s.cells.reverse with
  | _::y::_ => y
  | x::[] => !x
  | [] => false

def attach (s : Strand) (r : Supply) : Strand × Supply :=
  if s.cells.length < 8 ∧ wanted s ∈ r.pool ∧ 0 < r.free then
    (⟨s.cells++[wanted s],if s.cells.isEmpty then s.bonds else
       (s.cells.length-1,s.cells.length)::s.bonds⟩,
     ⟨r.pool.erase (wanted s),r.free-1,r.spent+1⟩)
  else (s,r)

def grow : Nat → Strand → Supply → Strand × Supply
  | 0, s, r => (s,r)
  | n+1, s, r => let t := attach s r; grow n t.1 t.2

theorem attach_material (s : Strand) (r : Supply) :
    (attach s r).1.cells.length + (attach s r).2.pool.length = s.cells.length+r.pool.length := by
  unfold attach
  split
  · rename_i h
    have he := List.length_erase_of_mem h.2.1
    have hp : r.pool.length > 0 := List.length_pos_iff.mpr (List.ne_nil_of_mem h.2.1)
    simp only [List.length_append,List.length_singleton]
    omega
  · rfl

theorem attach_support (s : Strand) (r : Supply) :
    (attach s r).2.free+(attach s r).2.spent = r.free+r.spent := by
  unfold attach
  split <;> simp_all <;> omega

theorem attach_tokens (s : Strand) (r : Supply) :
    (s.cells++r.pool).Perm ((attach s r).1.cells++(attach s r).2.pool) := by
  unfold attach
  split
  · rename_i h
    simpa [List.append_assoc] using (List.perm_cons_erase h.2.1).append_left s.cells
  · exact List.Perm.refl _

theorem grow_tokens (n : Nat) (s : Strand) (r : Supply) :
    (s.cells++r.pool).Perm ((grow n s r).1.cells++(grow n s r).2.pool) := by
  induction n generalizing s r with
  | zero => exact List.Perm.refl _
  | succ n ih => exact (attach_tokens s r).trans (ih _ _)

theorem attach_preserves_path (s : Strand) (r : Supply) (h : s.bonds = path s.cells.length) :
    (attach s r).1.bonds = path (attach s r).1.cells.length := by
  unfold attach
  split
  · simp only [List.length_append,List.length_singleton,path]
    cases hs : s.cells <;> simp_all [path]
  · exact h

theorem grow_accounts (n : Nat) (s : Strand) (r : Supply) :
    (grow n s r).1.cells.length+(grow n s r).2.pool.length = s.cells.length+r.pool.length ∧
    (grow n s r).2.free+(grow n s r).2.spent = r.free+r.spent := by
  induction n generalizing s r with
  | zero => exact ⟨rfl,rfl⟩
  | succ n ih =>
    obtain ⟨hm,hs⟩ := ih (attach s r).1 (attach s r).2
    exact ⟨hm.trans (attach_material s r),hs.trans (attach_support s r)⟩

theorem grow_preserves_path (n : Nat) (s : Strand) (r : Supply)
    (h : s.bonds = path s.cells.length) :
    (grow n s r).1.bonds = path (grow n s r).1.cells.length := by
  induction n generalizing s r with
  | zero => exact h
  | succ n ih => exact ih _ _ (attach_preserves_path s r h)

def reproduce (s : Strand) (r : Supply) : List Strand × Supply :=
  if s.cells.length = 8 ∧ s.bonds = path 8 ∧ 0 < r.free then
    let a := grow 4 (fragment s 0 4) ⟨r.pool,r.free-1,r.spent+1⟩
    let b := grow 4 (fragment s 4 4) a.2
    ([a.1,b.1],b.2)
  else ([s],r)

theorem reproduce_accounts (s : Strand) (r : Supply) :
    size (reproduce s r).1+(reproduce s r).2.pool.length = s.cells.length+r.pool.length ∧
    (reproduce s r).2.free+(reproduce s r).2.spent = r.free+r.spent := by
  unfold reproduce
  split
  · rename_i h
    have ha := grow_accounts 4 (fragment s 0 4) ⟨r.pool,r.free-1,r.spent+1⟩
    have hb := grow_accounts 4 (fragment s 4 4)
      (grow 4 (fragment s 0 4) ⟨r.pool,r.free-1,r.spent+1⟩).2
    simp only [size,fragment,List.drop_zero,List.length_take,List.length_drop] at *
    omega
  · simp [size]

def generation : List Strand → Supply → List Strand × Supply
  | [], r => ([],r)
  | s::ss, r =>
      let first := reproduce s r
      let rest := generation ss first.2
      (first.1++rest.1,rest.2)

theorem generation_accounts (ss : List Strand) (r : Supply) :
    size (generation ss r).1+(generation ss r).2.pool.length = size ss+r.pool.length ∧
    (generation ss r).2.free+(generation ss r).2.spent = r.free+r.spent := by
  induction ss generalizing r with
  | nil => simp [generation,size]
  | cons s ss ih =>
    have h := reproduce_accounts s r
    have hi := ih (reproduce s r).2
    simp only [generation,size_append,size]
    omega

def rounds : Nat → List Strand → Supply → List Strand × Supply
  | 0, ss, r => (ss,r)
  | n+1, ss, r => let t := generation ss r; rounds n t.1 t.2

theorem rounds_accounts (n : Nat) (ss : List Strand) (r : Supply) :
    size (rounds n ss r).1+(rounds n ss r).2.pool.length = size ss+r.pool.length ∧
    (rounds n ss r).2.free+(rounds n ss r).2.spent = r.free+r.spent := by
  induction n generalizing ss r with
  | zero => exact ⟨rfl,rfl⟩
  | succ n ih =>
    have h := generation_accounts ss r
    have hi := ih (generation ss r).1 (generation ss r).2
    exact ⟨hi.1.trans h.1,hi.2.trans h.2⟩

/-- A target for checking, never assigned by attachment or reproduction. -/
def form (a b : Bool) : Strand := ⟨[a,b,a,b,a,b,a,b],path 8⟩
def block (a b : Bool) : List Bool := [a,b,a,b,a,b,a,b]
def blocks (a b : Bool) : Nat → List Bool
  | 0 => []
  | n+1 => block a b ++ blocks a b n

theorem prepared_alternating_recovered (tail : List Bool) (free spent : Nat) :
    grow 8 ⟨[],[]⟩ ⟨MaterialMaturation.canonical++tail,free+8,spent⟩ =
      (RecurrentAssembly.mature,⟨tail,free,spent+8⟩) := by
  simp [grow,attach,wanted,MaterialMaturation.canonical,RecurrentAssembly.mature,path]

theorem prepared_output_enters (pool tail : List Bool) (free spent : Nat)
    (h : MaterialMaturation.route MaterialMaturation.canonical pool 8 = some ([],0)) :
    grow 8 ⟨[],[]⟩
      ⟨(MaterialMaturation.routeTrace MaterialMaturation.canonical pool 8).placed++tail,free+8,spent⟩ =
      (form false true,⟨tail,free,spent+8⟩) := by
  rw [(RecurrentAssembly.completed_routing_output pool h).1]
  exact prepared_alternating_recovered tail free spent

theorem same_law_different_continuation :
    wanted ⟨[false,false],path 2⟩ = false ∧
    wanted ⟨[true,false],path 2⟩ = true := by decide +kernel

theorem fragments_carry_pattern (a b : Bool) :
    fragment (form a b) 0 4 = ⟨[a,b,a,b],path 4⟩ ∧
    fragment (form a b) 4 4 = ⟨[a,b,a,b],path 4⟩ := by
  cases a <;> cases b <;> decide +kernel

theorem supported_reproduction (a b : Bool) (tail : List Bool) (free spent : Nat) :
    reproduce (form a b) ⟨block a b++tail,free+9,spent⟩ =
      ([form a b,form a b],⟨tail,free,spent+9⟩) := by
  cases a <;> cases b <;>
    simp [reproduce,grow,attach,wanted,fragment,block,form,path]

theorem blocks_add (a b : Bool) (n m : Nat) :
    blocks a b (n+m) = blocks a b n++blocks a b m := by
  induction n with
  | zero => simp [blocks]
  | succ n ih =>
    have h : n+1+m = n+m+1 := by omega
    rw [h,blocks,ih,blocks,List.append_assoc]

theorem supported_generation (a b : Bool) (n : Nat) (tail : List Bool) (free spent : Nat) :
    generation (List.replicate n (form a b)) ⟨blocks a b n++tail,free+9*n,spent⟩ =
      (List.replicate (2*n) (form a b),⟨tail,free,spent+9*n⟩) := by
  induction n generalizing free spent with
  | zero => simp [generation,blocks]
  | succ n ih =>
    simp only [List.replicate_succ,generation,blocks,List.append_assoc]
    have hw : free+9*(n+1) = (free+9*n)+9 := by omega
    rw [hw,supported_reproduction]
    simp only
    rw [ih]
    have hr : 2*(n+1) = (2*n+1)+1 := by omega
    rw [hr]
    simp only [List.replicate_succ,List.cons_append,List.nil_append]
    congr 2
    omega

theorem inherited_pattern_all_rounds (a b : Bool) (n k : Nat) (tail : List Bool) (free spent : Nat) :
    rounds n (List.replicate k (form a b))
      ⟨blocks a b (required n k)++tail,free+9*required n k,spent⟩ =
      (List.replicate (k*2^n) (form a b),⟨tail,free,spent+9*required n k⟩) := by
  induction n generalizing k spent with
  | zero => simp [rounds,required,blocks]
  | succ n ih =>
    simp only [rounds,required,blocks_add,List.append_assoc]
    have hw : free+9*(k+required n (2*k)) = (free+9*required n (2*k))+9*k := by omega
    rw [hw,supported_generation,ih]
    have hp : (2*k)*2^n = k*2^(n+1) := by
      simp [Nat.pow_succ,Nat.mul_assoc,Nat.mul_comm]
    rw [hp]
    congr 2
    omega

/-- Exchange an actual token at an existing position; its old token returns to
shared supply. Preservation of the connections is a supplied repair premise. -/
def exchange (i : Nat) (x : Bool) (s : Strand) (r : Supply) : Strand × Supply :=
  match s.cells[i]? with
  | none => (s,r)
  | some old =>
    if x ∈ r.pool ∧ 0 < r.free then
      (⟨s.cells.set i x,s.bonds⟩,⟨old::r.pool.erase x,r.free-1,r.spent+1⟩)
    else (s,r)

theorem exchange_accounts (i : Nat) (x : Bool) (s : Strand) (r : Supply) :
    (exchange i x s r).1.cells.length+(exchange i x s r).2.pool.length =
      s.cells.length+r.pool.length ∧
    (exchange i x s r).2.free+(exchange i x s r).2.spent = r.free+r.spent := by
  unfold exchange
  split
  · exact ⟨rfl,rfl⟩
  · split
    · rename_i h
      have he := List.length_erase_of_mem h.1
      have hp : r.pool.length > 0 := List.length_pos_iff.mpr (List.ne_nil_of_mem h.1)
      simp only [List.length_set,List.length_cons]
      omega
    · exact ⟨rfl,rfl⟩

def changed : Strand := (exchange 7 false (form false true) ⟨[false],1,0⟩).1

theorem one_local_exchange :
    exchange 7 false (form false true) ⟨[false],1,0⟩ =
      (⟨[false,true,false,true,false,true,false,false],path 8⟩,⟨[true],0,1⟩) := by
  decide +kernel

/-- Whole history: the released B and unconsumed stock continue into development. -/
def perturbedHistory : List Strand × Supply :=
  let initial := exchange 7 false (form false true)
    ⟨List.replicate 20 false++List.replicate 8 true,28,0⟩
  rounds 2 [initial.1] initial.2

theorem perturbation_forms_inherited_variant :
    perturbedHistory.1 = [form false true,form false true,
      ⟨[false,true,false,false,false,false,false,false],path 8⟩,form false false] ∧
    perturbedHistory.2 = ⟨[false,false,true,true],0,28⟩ := by decide +kernel

theorem mutation_absent_keeps_alternation :
    rounds 2 [form false true] ⟨blocks false true 3,27,0⟩ =
      (List.replicate 4 (form false true),⟨[],0,27⟩) := by
  simpa [required,blocks] using inherited_pattern_all_rounds false true 2 1 [] 0 0

/-- A census; it never deletes uncounted partial structures from the process. -/
def completeCount (a b : Bool) (ss : List Strand) : Nat :=
  (ss.filter (fun s => s == form a b)).length

theorem shared_material_selects_different_patterns :
    let t := generation [form false false,form true true] ⟨List.replicate 8 false,18,0⟩
    (completeCount false false t.1,completeCount true true t.1) = (2,0) ∧
    t.1.map (fun s => s.cells.length) = [8,8,4,4] ∧ t.2 = ⟨[],8,10⟩ := by decide +kernel

theorem changing_supply_reverses_amplification :
    let t := generation [form false false,form true true] ⟨List.replicate 8 true,18,0⟩
    (completeCount false false t.1,completeCount true true t.1) = (0,2) ∧
    t.1.map (fun s => s.cells.length) = [4,4,8,8] ∧ t.2 = ⟨[],8,10⟩ := by decide +kernel

theorem no_difference_with_jointly_sufficient_supply :
    let t := generation [form false false,form true true]
      ⟨List.replicate 8 false++List.replicate 8 true,18,0⟩
    (completeCount false false t.1,completeCount true true t.1) = (2,2) ∧
    t.2 = ⟨[],0,18⟩ := by decide +kernel

theorem competition_order_changes_output :
    let r : Supply := ⟨List.replicate 4 false++List.replicate 4 true,18,0⟩
    let first := generation [form false false,form false true] r
    let second := generation [form false true,form false false] r
    (completeCount false false first.1,completeCount false true first.1) = (1,0) ∧
    (completeCount false false second.1,completeCount false true second.1) = (0,2) := by
  decide +kernel

theorem complete_count_is_not_all_continuation :
    let t := generation [form false false,form true true] ⟨List.replicate 8 false,18,0⟩
    grow 4 (t.1[2]?.getD (form false false)) ⟨List.replicate 4 true,4,10⟩ =
      (form true true,⟨[],0,14⟩) := by decide +kernel

end StructuralInheritance
