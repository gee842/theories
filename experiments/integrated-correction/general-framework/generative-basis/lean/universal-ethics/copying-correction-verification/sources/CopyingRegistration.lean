import StructuralCopying

/-!
Retained arrangement, formed registration contacts and growing material are
roles in one evolving configuration. Docking consumes a connector and support;
loss returns the connector without refunding support; slip changes its source.
Copy steps read the actual contact, rather than the desired next template bit.
Selective docking of indexed sites, transduction, access, rearrangement and
event occurrence remain local premises. No origin of all copying chemistry or
probabilistic fidelity law is asserted.
-/
namespace CopyingRegistration
open RecurrentAssembly

structure State where
  template : Strand
  work : StructuralCopying.CopyState
  contacts : List (Nat × Nat)
  spare : Nat
  deriving DecidableEq, Repr

def initial (p : Strand) (r : Supply) (spare : Nat) : State :=
  ⟨p,StructuralCopying.start p r,[],spare⟩

def readAt (s : State) (i : Nat) : Option Bool :=
  (s.contacts.find? (fun e => e.1 == i)).bind (fun e => s.template.cells[e.2]?)

def spendOne (w : StructuralCopying.CopyState) : StructuralCopying.CopyState :=
  {w with supply := ⟨w.supply.pool,w.supply.free-1,w.supply.spent+1⟩}

def dock (i j : Nat) (s : State) : State :=
  if i = j ∧ i < s.template.cells.length ∧
      !(s.contacts.any (fun e => e.1 == i)) ∧ 0 < s.spare ∧ 0 < s.work.supply.free then
    {s with contacts := (i,j)::s.contacts, spare := s.spare-1, work := spendOne s.work}
  else s

def lose (i : Nat) (s : State) : State :=
  let kept := s.contacts.filter (fun e => e.1 != i)
  {s with contacts := kept, spare := s.spare+(s.contacts.length-kept.length)}

def slip (i j : Nat) (s : State) : State :=
  if j < s.template.cells.length ∧ s.contacts.any (fun e => e.1 == i) ∧ 0 < s.work.supply.free then
    {s with
      contacts := s.contacts.map (fun e => if e.1 == i then (i,j) else e)
      work := spendOne s.work}
  else s

def tick (law : StructuralCopying.Law) (s : State) : State :=
  match s.work.pending, readAt s s.work.built.cells.length with
  | _::xs, some x =>
    let c := StructuralCopying.charge law s.work.previous x
    if x ∈ s.work.supply.pool ∧ c ≤ s.work.supply.free then
      {s with work := ⟨some x,xs,StructuralCopying.extend s.work.built x,
        ⟨s.work.supply.pool.erase x,s.work.supply.free-c,s.work.supply.spent+c⟩⟩}
    else s
  | _, _ => s

def operate (law : StructuralCopying.Law) : Nat → State → State
  | 0, s => s
  | n+1, s => operate law n (tick law s)

def Aligned (s : State) : Prop := ∀ e ∈ s.contacts, e.1 = e.2

def Registered (s : State) : Prop :=
  ∀ i < s.template.cells.length, readAt s i = s.template.cells[i]?

def Tracks (s : State) : Prop := s.template.cells = s.work.built.cells++s.work.pending

theorem dock_forms_actual_contact (s : State) (i j : Nat)
    (h : (dock i j s).contacts ≠ s.contacts) :
    i = j ∧ i < s.template.cells.length ∧
      (dock i j s).contacts = (i,j)::s.contacts ∧
      (dock i j s).spare+1 = s.spare ∧
      (dock i j s).work.supply.spent = s.work.supply.spent+1 := by
  unfold dock at h ⊢
  split at h
  · rename_i hd
    simp only [if_pos hd]
    exact ⟨hd.1,hd.2.1,True.intro,by omega,rfl⟩
  · exact False.elim (h rfl)

theorem dock_preserves_alignment (s : State) (i j : Nat) (h : Aligned s) : Aligned (dock i j s) := by
  unfold dock
  split
  · rename_i hd
    intro e he
    simp only [List.mem_cons] at he
    rcases he with rfl | he
    · exact hd.1
    · exact h e he
  · exact h

theorem loss_preserves_alignment (s : State) (i : Nat) (h : Aligned s) : Aligned (lose i s) := by
  intro e he
  exact h e (List.mem_filter.mp he).1

theorem dock_accounts (s : State) (i j : Nat) :
    (dock i j s).contacts.length+(dock i j s).spare = s.contacts.length+s.spare ∧
    (dock i j s).work.built.cells.length+(dock i j s).work.supply.pool.length =
      s.work.built.cells.length+s.work.supply.pool.length ∧
    (dock i j s).work.supply.free+(dock i j s).work.supply.spent =
      s.work.supply.free+s.work.supply.spent := by
  unfold dock
  split <;> simp_all [spendOne] <;> omega

theorem loss_accounts (s : State) (i : Nat) :
    (lose i s).contacts.length+(lose i s).spare = s.contacts.length+s.spare ∧
    (lose i s).work = s.work := by
  have h := List.length_filter_le (fun e : Nat × Nat => e.1 != i) s.contacts
  simp only [lose]
  exact ⟨by omega,True.intro⟩

theorem slip_accounts (s : State) (i j : Nat) :
    (slip i j s).contacts.length+(slip i j s).spare = s.contacts.length+s.spare ∧
    (slip i j s).work.built.cells.length+(slip i j s).work.supply.pool.length =
      s.work.built.cells.length+s.work.supply.pool.length ∧
    (slip i j s).work.supply.free+(slip i j s).work.supply.spent =
      s.work.supply.free+s.work.supply.spent := by
  unfold slip
  split <;> simp_all [spendOne] <;> omega

theorem tick_accounts (law : StructuralCopying.Law) (s : State) :
    (tick law s).contacts = s.contacts ∧ (tick law s).spare = s.spare ∧
    (tick law s).work.built.cells.length+(tick law s).work.supply.pool.length =
      s.work.built.cells.length+s.work.supply.pool.length ∧
    (tick law s).work.supply.free+(tick law s).work.supply.spent =
      s.work.supply.free+s.work.supply.spent := by
  unfold tick
  split
  · dsimp only
    split
    · rename_i h
      have he := List.length_erase_of_mem h.1
      have hp := List.length_pos_iff.mpr (List.ne_nil_of_mem h.1)
      simp only [StructuralCopying.extend,List.length_append,List.length_singleton]
      exact ⟨True.intro,True.intro,by omega,by omega⟩
    · exact ⟨rfl,rfl,rfl,rfl⟩
  · exact ⟨rfl,rfl,rfl,rfl⟩

theorem tick_tokens (law : StructuralCopying.Law) (s : State) :
    (s.work.built.cells++s.work.supply.pool).Perm
      ((tick law s).work.built.cells++(tick law s).work.supply.pool) := by
  unfold tick
  split
  · dsimp only
    split
    · rename_i h
      simpa [StructuralCopying.extend,List.append_assoc] using
        (List.perm_cons_erase h.1).append_left s.work.built.cells
    · exact List.Perm.refl _
  · exact List.Perm.refl _

theorem correct_read_refines_old_tick (law : StructuralCopying.Law) (s : State)
    (h : readAt s s.work.built.cells.length = s.work.pending.head?) :
    (tick law s).work = StructuralCopying.tick law s.work := by
  cases hp : s.work.pending with
  | nil => simp [tick,StructuralCopying.tick,hp]
  | cons x xs =>
    simp only [hp,List.head?_cons] at h
    simp [tick,StructuralCopying.tick,hp,h]
    split <;> rfl

theorem registered_read_is_correct (s : State) (hr : Registered s) (ht : Tracks s)
    (hn : s.work.pending ≠ []) :
    readAt s s.work.built.cells.length = s.work.pending.head? := by
  have hlen : s.work.built.cells.length < s.template.cells.length := by
    have hp := List.length_pos_iff.mpr hn
    unfold Tracks at ht
    rw [ht,List.length_append]
    omega
  rw [hr _ hlen,ht,List.getElem?_append_right (Nat.le_refl _)]
  simp only [Nat.sub_self]
  cases s.work.pending <;> rfl

theorem tick_keeps_registered (law : StructuralCopying.Law) (s : State) (h : Registered s) :
    Registered (tick law s) := by
  unfold tick
  split
  · dsimp only
    split <;> exact h
  · exact h

theorem tick_keeps_tracks (law : StructuralCopying.Law) (s : State)
    (hr : Registered s) (ht : Tracks s) : Tracks (tick law s) := by
  by_cases hn : s.work.pending = []
  · simpa [tick,hn] using ht
  have he := correct_read_refines_old_tick law s (registered_read_is_correct s hr ht hn)
  have hs := StructuralCopying.tick_keeps_template_order law s.work
  have hp : (tick law s).template = s.template := by
    unfold tick; split
    · dsimp only; split <;> rfl
    · rfl
  unfold Tracks
  rw [hp,he,hs]
  exact ht

theorem registered_operation_refines (law : StructuralCopying.Law) (n : Nat) (s : State)
    (hr : Registered s) (ht : Tracks s) :
    (operate law n s).work = StructuralCopying.steps law n s.work := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
    rw [operate, ih (tick law s) (tick_keeps_registered law s hr) (tick_keeps_tracks law s hr ht)]
    by_cases hn : s.work.pending = []
    · simp [tick,StructuralCopying.steps,StructuralCopying.tick,hn]
    · rw [correct_read_refines_old_tick law s (registered_read_is_correct s hr ht hn)]
      rfl

theorem registered_inheritance (law : StructuralCopying.Law) (p : Strand)
    (hp : p.bonds = path p.cells.length) (hn : p.cells ≠ [])
    (tail : List Bool) (free spent : Nat) (contacts : List (Nat × Nat)) (spare : Nat)
    (hreg : Registered ⟨p,StructuralCopying.start p
      ⟨p.cells++tail,free+StructuralCopying.cost law none p.cells,spent⟩,contacts,spare⟩) :
    (operate law p.cells.length ⟨p,StructuralCopying.start p
      ⟨p.cells++tail,free+StructuralCopying.cost law none p.cells,spent⟩,contacts,spare⟩).work.built = p := by
  rw [registered_operation_refines law _ _ hreg (by simp [Tracks,StructuralCopying.start])]
  have h := StructuralCopying.copied_structure_inherits law p hp hn tail free spent
  simpa [StructuralCopying.copy,hp,hn] using h.2.1

inductive Event where
  | dock (i j : Nat)
  | lose (i : Nat)
  | slip (i j : Nat)
  | copy
  deriving DecidableEq, Repr

def step (law : StructuralCopying.Law) (s : State) : Event → State
  | .dock i j => dock i j s
  | .lose i => lose i s
  | .slip i j => slip i j s
  | .copy => tick law s

def run (law : StructuralCopying.Law) : List Event → State → State
  | [], s => s
  | e::es, s => run law es (step law s e)

def process (law : StructuralCopying.Law) : Generative.Process State Event :=
  ⟨fun s e t => step law s e = t⟩

theorem run_is_trace (law : StructuralCopying.Law) (es : List Event) (s : State) :
    Generative.Trace (process law) s es (run law es s) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons rfl (ih _)

theorem step_accounts (law : StructuralCopying.Law) (s : State) (e : Event) :
    (step law s e).contacts.length+(step law s e).spare = s.contacts.length+s.spare ∧
    (step law s e).work.built.cells.length+(step law s e).work.supply.pool.length =
      s.work.built.cells.length+s.work.supply.pool.length ∧
    (step law s e).work.supply.free+(step law s e).work.supply.spent =
      s.work.supply.free+s.work.supply.spent := by
  cases e with
  | dock i j => exact dock_accounts s i j
  | lose i => obtain ⟨h1,h2⟩ := loss_accounts s i; exact ⟨h1,by simp [step,h2],by simp [step,h2]⟩
  | slip i j => exact slip_accounts s i j
  | copy => obtain ⟨h1,h2,h3,h4⟩ := tick_accounts law s; exact ⟨by simp [step,h1,h2],h3,h4⟩

theorem history_accounts (law : StructuralCopying.Law) (es : List Event) (s : State) :
    (run law es s).contacts.length+(run law es s).spare = s.contacts.length+s.spare ∧
    (run law es s).work.built.cells.length+(run law es s).work.supply.pool.length =
      s.work.built.cells.length+s.work.supply.pool.length ∧
    (run law es s).work.supply.free+(run law es s).work.supply.spent =
      s.work.supply.free+s.work.supply.spent := by
  induction es generalizing s with
  | nil => exact ⟨rfl,rfl,rfl⟩
  | cons e es ih =>
    obtain ⟨h1,h2,h3⟩ := ih (step law s e)
    obtain ⟨h4,h5,h6⟩ := step_accounts law s e
    exact ⟨h1.trans h4,h2.trans h5,h3.trans h6⟩

theorem step_retains_built_prefix (law : StructuralCopying.Law) (s : State) (e : Event) :
    ∃ tail, (step law s e).work.built.cells = s.work.built.cells++tail := by
  cases e with
  | dock i j =>
    simp only [step]
    unfold dock
    split <;> exact ⟨[],by simp [spendOne]⟩
  | lose i => exact ⟨[],by simp [step,lose]⟩
  | slip i j =>
    simp only [step]
    unfold slip
    split <;> exact ⟨[],by simp [spendOne]⟩
  | copy =>
    simp only [step]
    unfold tick
    split
    · dsimp only
      split
      · exact ⟨[_],rfl⟩
      · exact ⟨[],by simp⟩
    · exact ⟨[],by simp⟩

theorem history_retains_built_prefix (law : StructuralCopying.Law) (es : List Event) (s : State) :
    ∃ tail, (run law es s).work.built.cells = s.work.built.cells++tail := by
  induction es generalizing s with
  | nil => exact ⟨[],by simp [run]⟩
  | cons e es ih =>
    obtain ⟨a,ha⟩ := step_retains_built_prefix law s e
    obtain ⟨b,hb⟩ := ih (step law s e)
    exact ⟨a++b,by simp only [run,hb,ha,List.append_assoc]⟩

def formation : List Event := [.dock 0 0,.dock 1 1,.dock 2 2,.dock 3 3]
def copying : List Event := [.copy,.copy,.copy,.copy]
def prepared (budget : Nat) : State :=
  run StructuralCopying.alternatingEasy formation
    (initial StructuralCopying.alternating ⟨[false,false,false,true,true],budget,0⟩ 4)

theorem actual_contacts_are_formed :
    (prepared 12).contacts = [(3,3),(2,2),(1,1),(0,0)] ∧
    (prepared 12).spare = 0 ∧ (prepared 12).work.supply.free = 8 ∧
    (prepared 12).work.supply.spent = 4 := by decide

theorem formed_registration_is_complete : Registered (prepared 12) := by
  intro i hi
  have hlt : i < 4 := hi
  have h : i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3 := by omega
  rcases h with rfl | rfl | rfl | rfl <;> decide

theorem no_contact_no_copy :
    operate StructuralCopying.alternatingEasy 4
      (initial StructuralCopying.alternating ⟨StructuralCopying.feed,12,0⟩ 4) =
      initial StructuralCopying.alternating ⟨StructuralCopying.feed,12,0⟩ 4 := by decide

theorem incompatible_docking_is_not_registration :
    (dock 1 0 (initial StructuralCopying.alternating ⟨[],12,0⟩ 4)).contacts = [] := by decide

theorem formation_then_faithful_copy :
    let s := run StructuralCopying.alternatingEasy copying (prepared 12)
    s.work.built = StructuralCopying.alternating ∧
    (StructuralCopying.release s.work).1 = true ∧
    (StructuralCopying.release s.work).2.supply = ⟨[false],3,9⟩ := by decide

theorem slip_changes_actual_copy :
    let s := run StructuralCopying.alternatingEasy (.slip 1 0::copying) (prepared 12)
    s.work.built.cells = [false,false,false,true] ∧
    (StructuralCopying.release s.work).1 = true ∧
    (StructuralCopying.release s.work).2.supply = ⟨[true],0,12⟩ := by decide

theorem loss_stalls_with_stock_remaining :
    let s := run StructuralCopying.alternatingEasy (.lose 1::copying) (prepared 12)
    s.work.built.cells = [false] ∧ s.work.pending = [true,false,true] ∧
    s.work.supply.free = 7 ∧ s.spare = 1 := by decide

theorem rebinding_restores_fidelity :
    let s := run StructuralCopying.alternatingEasy
      ([.slip 1 0,.lose 1,.dock 1 1]++copying) (prepared 12)
    s.work.built = StructuralCopying.alternating ∧
    (StructuralCopying.release s.work).1 = true ∧
    (StructuralCopying.release s.work).2.supply = ⟨[false],1,11⟩ := by decide

theorem correcting_contact_does_not_rewrite_past :
    let s := run StructuralCopying.alternatingEasy
      [.copy,.slip 1 0,.copy,.lose 1,.dock 1 1,.copy,.copy] (prepared 12)
    s.work.built.cells = [false,false,false,true] ∧
    s.contacts = [(1,1),(3,3),(2,2),(0,0)] ∧
    s.work.pending = [] ∧ s.work.supply.free = 0 ∧
    (StructuralCopying.release s.work).1 = false := by decide

theorem altered_contact_can_preserve_this_signal :
    readAt (slip 0 2 (prepared 12)) 0 = readAt (prepared 12) 0 ∧
    (slip 0 2 (prepared 12)).contacts ≠ (prepared 12).contacts := by decide

def census (s : State) : Nat × Nat × Nat × Nat × List Bool × List Bool :=
  (s.contacts.length,s.spare,s.work.supply.free,s.work.supply.spent,
    s.work.supply.pool,s.work.built.cells)

def copiedCells (s : State) : List Bool :=
  (operate StructuralCopying.alternatingEasy 4 s).work.built.cells

theorem matched_difference_is_contact :
    let good := slip 0 2 (prepared 12)
    let bad := slip 1 0 (prepared 12)
    good.template = bad.template ∧ good.work = bad.work ∧ good.spare = bad.spare ∧
    good.contacts.length = bad.contacts.length ∧ good.contacts ≠ bad.contacts := by decide

theorem matched_totals_different_copy :
    census (slip 0 2 (prepared 12)) = census (slip 1 0 (prepared 12)) ∧
    copiedCells (slip 0 2 (prepared 12)) = [false,true,false,true] ∧
    copiedCells (slip 1 0 (prepared 12)) = [false,false,false,true] := by decide

theorem no_census_only_copy
    (f : (Nat × Nat × Nat × Nat × List Bool × List Bool) → List Bool)
    (h : ∀ s, f (census s) = copiedCells s) : False := by
  have he := congrArg f matched_totals_different_copy.1
  rw [h,h,matched_totals_different_copy.2.1,matched_totals_different_copy.2.2] at he
  cases he

theorem erroneous_daughter_can_be_faithfully_inherited :
    let s := run StructuralCopying.alternatingEasy (.slip 1 0::copying) (prepared 12)
    let daughter := (StructuralCopying.release s.work).2.built
    (StructuralCopying.reproduce StructuralCopying.alternatingEasy daughter
      ⟨[false,false,false,true],7,12⟩).1 = true ∧
    (StructuralCopying.reproduce StructuralCopying.alternatingEasy daughter
      ⟨[false,false,false,true],7,12⟩).2.built.cells = [false,false,false,true] := by decide

end CopyingRegistration
