import GrownFragmentation

/-!
Prepared material enters an actual alternating end-attachment process. Its
formed chain is cut, its fragments retain their internal links, and those
fragments undergo the same end attachment again. Each material token is removed
from one shared finite pool. Attachment compatibility, the size-eight cleavage
law, and the availability/order of operations remain supplied local premises.
-/
namespace RecurrentAssembly

abbrev Edge := Nat × Nat

structure Strand where
  cells : List Bool
  bonds : List Edge
  deriving DecidableEq, Repr

structure Supply where
  pool : List Bool
  free : Nat
  spent : Nat
  deriving DecidableEq, Repr

def path : Nat → List Edge
  | 0 => []
  | n+1 => if n = 0 then [] else (n-1,n)::path n

def wanted (s : Strand) : Bool :=
  match s.cells.getLast? with
  | none => false
  | some x => !x

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

def mature : Strand :=
  ⟨[false,true,false,true,false,true,false,true],path 8⟩

def fragment (s : Strand) (start len : Nat) : Strand :=
  ⟨(s.cells.drop start).take len,
    (s.bonds.filter (fun e => decide (start ≤ e.1 ∧ e.1 < start+len ∧
      start ≤ e.2 ∧ e.2 < start+len))).map (fun e => (e.1-start,e.2-start))⟩

def reproduce (s : Strand) (r : Supply) : List Strand × Supply :=
  if s.cells.length = 8 ∧ s.bonds = path 8 ∧ 0 < r.free then
    let a := grow 4 (fragment s 0 4) ⟨r.pool,r.free-1,r.spent+1⟩
    let b := grow 4 (fragment s 4 4) a.2
    ([a.1,b.1],b.2)
  else ([s],r)

def size : List Strand → Nat
  | [] => 0
  | s::ss => s.cells.length+size ss

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

theorem size_append (xs ys : List Strand) : size (xs++ys) = size xs+size ys := by
  induction xs with
  | nil => simp [size]
  | cons x xs ih => simp [size,ih,Nat.add_assoc]

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

theorem prepared_material_assembles (tail : List Bool) (free spent : Nat) :
    grow 8 ⟨[],[]⟩ ⟨MaterialMaturation.canonical++tail,free+8,spent⟩ =
      (mature,⟨tail,free,spent+8⟩) := by
  simp [grow,attach,wanted,MaterialMaturation.canonical,mature,path]

theorem completed_routing_output (pool : List Bool)
    (h : MaterialMaturation.route MaterialMaturation.canonical pool 8 = some ([],0)) :
    (MaterialMaturation.routeTrace MaterialMaturation.canonical pool 8).placed = MaterialMaturation.canonical ∧
    (MaterialMaturation.routeTrace MaterialMaturation.canonical pool 8).leftover = [] := by
  rw [MaterialMaturation.route_trace_projection] at h
  split at h <;> simp_all

theorem prepared_output_rebuilds (pool tail : List Bool) (free spent : Nat)
    (h : MaterialMaturation.route MaterialMaturation.canonical pool 8 = some ([],0)) :
    grow 8 ⟨[],[]⟩
      ⟨(MaterialMaturation.routeTrace MaterialMaturation.canonical pool 8).placed++tail,free+8,spent⟩ =
      (mature,⟨tail,free,spent+8⟩) := by
  rw [(completed_routing_output pool h).1,prepared_material_assembles]

theorem formed_graph_matches_previous :
    mature.cells = (List.range 8).map GrownFragmentation.chain.kind ∧
    mature.bonds = GrownFragmentation.chain.body.bonds := by decide +kernel

theorem fragments_retain_real_links :
    fragment mature 0 4 = ⟨[false,true,false,true],path 4⟩ ∧
    fragment mature 4 4 = ⟨[false,true,false,true],path 4⟩ ∧
    GrownFragmentation.cutComponents GrownFragmentation.chain (3,4) =
      [[0,1,2,3],[4,5,6,7]] := by decide +kernel

theorem supported_reproduction (tail : List Bool) (free spent : Nat) :
    reproduce mature ⟨MaterialMaturation.canonical++tail,free+9,spent⟩ =
      ([mature,mature],⟨tail,free,spent+9⟩) := by
  simp [reproduce,grow,attach,wanted,fragment,MaterialMaturation.canonical,mature,path]

def blocks : Nat → List Bool
  | 0 => []
  | n+1 => MaterialMaturation.canonical++blocks n

theorem blocks_length (n : Nat) : (blocks n).length = 8*n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [blocks,ih,MaterialMaturation.canonical]; omega

theorem blocks_add (n m : Nat) : blocks (n+m) = blocks n++blocks m := by
  induction n with
  | zero => simp [blocks]
  | succ n ih =>
    have h : n+1+m = n+m+1 := by omega
    rw [h,blocks,ih,blocks,List.append_assoc]

theorem size_replicate (n : Nat) : size (List.replicate n mature) = 8*n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [List.replicate_succ,size,ih]
    change 8+8*n = 8*(n+1)
    omega

theorem supported_generation (n : Nat) (tail : List Bool) (free spent : Nat) :
    generation (List.replicate n mature) ⟨blocks n++tail,free+9*n,spent⟩ =
      (List.replicate (2*n) mature,⟨tail,free,spent+9*n⟩) := by
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

def required : Nat → Nat → Nat
  | 0, _ => 0
  | n+1, k => k+required n (2*k)

theorem required_as_growth (n k : Nat) : required n k+k = k*2^n := by
  induction n generalizing k with
  | zero => simp [required]
  | succ n ih =>
    have h := ih (2*k)
    have hp : (2*k)*2^n = k*2^(n+1) := by
      simp [Nat.pow_succ,Nat.mul_assoc,Nat.mul_comm]
    simp only [required]
    omega

theorem supported_rounds (n k : Nat) (tail : List Bool) (free spent : Nat) :
    rounds n (List.replicate k mature) ⟨blocks (required n k)++tail,free+9*required n k,spent⟩ =
      (List.replicate (k*2^n) mature,⟨tail,free,spent+9*required n k⟩) := by
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

theorem prepared_repeated_generation (n : Nat) (pool tail : List Bool) (free spent : Nat)
    (h : MaterialMaturation.route MaterialMaturation.canonical pool 8 = some ([],0)) :
    let a := grow 8 ⟨[],[]⟩
      ⟨(MaterialMaturation.routeTrace MaterialMaturation.canonical pool 8).placed++
        (blocks (required n 1)++tail), (free+9*required n 1)+8, spent⟩
    rounds n [a.1] a.2 =
      (List.replicate (2^n) mature,⟨tail,free,(spent+8)+9*required n 1⟩) := by
  rw [(completed_routing_output pool h).1,prepared_material_assembles]
  simpa using supported_rounds n 1 tail free (spent+8)

def process : Generative.Process (List Strand × Supply) Unit where
  step s _ t := generation s.1 s.2 = t

theorem rounds_are_trace (n : Nat) (ss : List Strand) (r : Supply) :
    Generative.Trace process (ss,r) (List.replicate n ()) (rounds n ss r) := by
  induction n generalizing ss r with
  | zero => exact .nil _
  | succ n ih =>
    exact .cons rfl (ih (generation ss r).1 (generation ss r).2)

theorem finite_material_bound (n : Nat) (ss : List Strand) (r : Supply) (count : Nat)
    (h : (rounds n ss r).1 = List.replicate count mature) :
    8*count ≤ size ss+r.pool.length := by
  have hm := (rounds_accounts n ss r).1
  rw [h,size_replicate] at hm
  omega

theorem zero_support_stops (ss : List Strand) (pool : List Bool) (spent : Nat) :
    generation ss ⟨pool,0,spent⟩ = (ss,⟨pool,0,spent⟩) := by
  induction ss with
  | nil => rfl
  | cons s ss ih => simp [generation,reproduce,ih]

theorem two_generations_realized :
    rounds 2 [mature] ⟨blocks 3,27,0⟩ = (List.replicate 4 mature,⟨[],0,27⟩) := by
  simpa [required,blocks] using supported_rounds 2 1 [] 0 0

theorem partial_failure_keeps_material :
    let t := rounds 2 [mature] ⟨blocks 3,26,0⟩
    t.1.map (fun s => s.cells.length) = [8,8,8,7] ∧
    t.2 = ⟨[true],0,26⟩ ∧ size t.1+t.2.pool.length = 32 := by decide +kernel

theorem missing_kind_stalls_with_work_remaining :
    grow 8 ⟨[],[]⟩ ⟨List.replicate 8 false,8,0⟩ =
      (⟨[false],[]⟩,⟨List.replicate 7 false,7,1⟩) := by decide +kernel

theorem wrong_structure_is_not_reset :
    reproduce ⟨mature.cells,[]⟩ ⟨blocks 1,9,0⟩ =
      ([⟨mature.cells,[]⟩],⟨blocks 1,9,0⟩) := by decide +kernel

end RecurrentAssembly
