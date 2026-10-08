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
    simp [List.replicate_succ,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm]

end RecurrentAssembly
