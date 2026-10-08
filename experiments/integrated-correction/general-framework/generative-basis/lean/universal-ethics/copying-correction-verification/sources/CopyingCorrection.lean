import CopyingRegistration

/-!
Copying, checking and editing differentiate within the same retained material
history. A formed route couples one retained source position to one built site.
Inspection consumes support even when an exchange cannot occur. Exchange moves
an available component into the product and returns the displaced component.
No correctness predicate guides the operation: correctness is a subsequent
relation to the retained template. Binding geometry, comparison, atomic editing,
component reuse, local costs and the occurrence of events remain supplied.
-/
namespace CopyingCorrection
open RecurrentAssembly

structure State where
  assembly : CopyingRegistration.State
  routes : List (Nat × Nat)
  deriving DecidableEq, Repr

def reference (s : State) (i : Nat) : Option Bool :=
  (s.routes.find? (fun e => e.1 == i)).bind (fun e => s.assembly.template.cells[e.2]?)

def connect (i j : Nat) (s : State) : State :=
  if i < s.assembly.work.built.cells.length ∧ j < s.assembly.template.cells.length ∧
      !(s.routes.any (fun e => e.1 == i)) ∧ 0 < s.assembly.spare ∧ 0 < s.assembly.work.supply.free then
    {assembly := {s.assembly with
      spare := s.assembly.spare-1
      work := CopyingRegistration.spendOne s.assembly.work}
     routes := (i,j)::s.routes}
  else s

def exchange (i : Nat) (x : Bool) (w : StructuralCopying.CopyState) : StructuralCopying.CopyState :=
  match w.built.cells[i]? with
  | none => w
  | some old =>
    if old ≠ x ∧ x ∈ w.supply.pool ∧ 0 < w.supply.free then
      let cells := w.built.cells.set i x
      {w with
        built := {w.built with cells := cells}
        previous := cells.getLast?
        supply := ⟨w.supply.pool.erase x++[old],w.supply.free-1,w.supply.spent+1⟩}
    else w

def inspect (i : Nat) (s : State) : State :=
  match reference s i, s.assembly.work.built.cells[i]? with
  | some x, some _ =>
    if 0 < s.assembly.work.supply.free then
      {s with assembly := {s.assembly with
        work := exchange i x (CopyingRegistration.spendOne s.assembly.work)}}
    else s
  | _, _ => s

def Faithful (s : State) : Prop :=
  ∀ i x, reference s i = some x → s.assembly.template.cells[i]? = some x

def defects : List Bool → List Bool → Nat
  | a::as, b::bs => (if a = b then 0 else 1)+defects as bs
  | _, _ => 0

theorem set_correct_reduces (t b : List Bool) (i : Nat) (x old : Bool)
    (ht : t[i]? = some x) (hb : b[i]? = some old) (hne : old ≠ x) :
    defects t (b.set i x)+1 = defects t b := by
  induction t generalizing b i with
  | nil => simp at ht
  | cons a as ih =>
    cases b with
    | nil => simp at hb
    | cons c cs =>
      cases i with
      | zero => simp_all [defects,eq_comm,Nat.add_comm]
      | succ i =>
        simp only [List.getElem?_cons_succ] at ht hb
        have h := ih cs i ht hb
        simp only [List.set,defects]
        omega

theorem set_exchanges_components (xs : List Bool) (i : Nat) (old x : Bool)
    (h : xs[i]? = some old) : (x::xs).Perm (old::xs.set i x) := by
  induction xs generalizing i with
  | nil => simp at h
  | cons a as ih =>
    cases i with
    | zero =>
      simp only [List.getElem?_cons_zero,Option.some.injEq] at h
      subst a
      exact List.Perm.swap _ _ _
    | succ i =>
      simp only [List.getElem?_cons_succ] at h
      exact (List.Perm.swap _ _ _).trans ((ih i h).cons a) |>.trans (List.Perm.swap _ _ _)

theorem exchange_material (i : Nat) (x : Bool) (w : StructuralCopying.CopyState) :
    (w.built.cells++w.supply.pool).Perm
      ((exchange i x w).built.cells++(exchange i x w).supply.pool) := by
  unfold exchange
  split
  · exact List.Perm.refl _
  · rename_i old ho
    split
    · rename_i h
      have hp := (List.perm_cons_erase h.2.1).append_left w.built.cells
      have hs := set_exchanges_components w.built.cells i old x ho
      have hc : (w.built.cells++x::w.supply.pool.erase x).Perm
          ((x::w.built.cells)++w.supply.pool.erase x) := by
        simpa only [List.cons_append] using List.perm_middle
      have hd := hs.append_right (w.supply.pool.erase x)
      have he : ((old::w.built.cells.set i x)++w.supply.pool.erase x).Perm
          (w.built.cells.set i x++(w.supply.pool.erase x++[old])) := by
        simpa [List.append_assoc] using
          (List.perm_append_comm : ([old]++(w.built.cells.set i x++w.supply.pool.erase x)).Perm
            ((w.built.cells.set i x++w.supply.pool.erase x)++[old]))
      exact hp.trans (hc.trans (hd.trans he))
    · exact List.Perm.refl _

theorem exchange_shape (i : Nat) (x : Bool) (w : StructuralCopying.CopyState) :
    (exchange i x w).built.cells.length = w.built.cells.length ∧
    (exchange i x w).built.bonds = w.built.bonds ∧
    (exchange i x w).pending = w.pending := by
  unfold exchange
  split
  · exact ⟨rfl,rfl,rfl⟩
  · split <;> simp [List.length_set]

theorem exchange_support (i : Nat) (x : Bool) (w : StructuralCopying.CopyState) :
    (exchange i x w).supply.free+(exchange i x w).supply.spent =
      w.supply.free+w.supply.spent := by
  unfold exchange
  split
  · rfl
  · split <;> simp_all <;> omega

theorem exchange_other_site (i j : Nat) (x : Bool) (w : StructuralCopying.CopyState)
    (h : i ≠ j) : (exchange i x w).built.cells[j]? = w.built.cells[j]? := by
  unfold exchange
  split
  · rfl
  · split <;> simp [List.getElem?_set_ne h]

theorem exchange_reduces_or_keeps (t : List Bool) (i : Nat) (x : Bool)
    (w : StructuralCopying.CopyState) (ht : t[i]? = some x) :
    defects t (exchange i x w).built.cells ≤ defects t w.built.cells := by
  unfold exchange
  split
  · exact Nat.le_refl _
  · rename_i old ho
    split
    · rename_i h
      have hd := set_correct_reduces t w.built.cells i x old ht ho h.1
      dsimp only
      omega
    · exact Nat.le_refl _

theorem inspection_uses_actual_reference (s : State) (i : Nat)
    (h : reference s i = none) : inspect i s = s := by simp [inspect,h]

theorem inspection_preserves_organization (s : State) (i : Nat) :
    (inspect i s).assembly.template = s.assembly.template ∧
    (inspect i s).assembly.contacts = s.assembly.contacts ∧
    (inspect i s).assembly.spare = s.assembly.spare ∧
    (inspect i s).routes = s.routes := by
  unfold inspect
  split
  · split <;> exact ⟨rfl,rfl,rfl,rfl⟩
  · exact ⟨rfl,rfl,rfl,rfl⟩

theorem inspection_improves_or_keeps (s : State) (i : Nat) (h : Faithful s) :
    defects (inspect i s).assembly.template.cells (inspect i s).assembly.work.built.cells ≤
      defects s.assembly.template.cells s.assembly.work.built.cells := by
  unfold inspect
  split
  · rename_i x old hx _
    split
    · exact exchange_reduces_or_keeps _ i x _ (h i x hx)
    · exact Nat.le_refl _
  · exact Nat.le_refl _

theorem inspection_retains_faithful_reference (s : State) (i : Nat) (h : Faithful s) :
    Faithful (inspect i s) := by
  have hp := inspection_preserves_organization s i
  intro j x hx
  simp only [reference,hp.2.2.2,hp.1] at hx
  rw [hp.1]
  exact h j x hx

def scan : List Nat → State → State
  | [],s => s
  | i::is,s => scan is (inspect i s)

theorem inspection_scan_retains_reference (s : State) (is : List Nat) (h : Faithful s) :
    Faithful (scan is s) := by
  induction is generalizing s with
  | nil => exact h
  | cons i is ih => exact ih _ (inspection_retains_faithful_reference s i h)

theorem inspection_scan_does_not_increase_defects (s : State) (is : List Nat) (h : Faithful s) :
    defects (scan is s).assembly.template.cells (scan is s).assembly.work.built.cells ≤
      defects s.assembly.template.cells s.assembly.work.built.cells := by
  induction is generalizing s with
  | nil => exact Nat.le_refl _
  | cons i is ih =>
    exact Nat.le_trans (ih _ (inspection_retains_faithful_reference s i h))
      (inspection_improves_or_keeps s i h)

theorem inspection_matches_reference_iff (s : State) (i : Nat) (x old : Bool)
    (hr : reference s i = some x) (hb : s.assembly.work.built.cells[i]? = some old)
    (hne : old ≠ x) :
    (inspect i s).assembly.work.built.cells[i]? = some x ↔
      2 ≤ s.assembly.work.supply.free ∧ x ∈ s.assembly.work.supply.pool := by
  have hi : i < s.assembly.work.built.cells.length := List.getElem?_eq_some_iff.mp hb |>.1
  simp only [inspect,hr,hb]
  split
  · rename_i hs
    simp only [exchange,CopyingRegistration.spendOne,hb]
    split
    · rename_i he
      simp only [List.getElem?_set_self hi,true_iff]
      exact ⟨by omega,he.2.1⟩
    · rename_i he
      simp only [hb,Option.some.injEq]
      constructor
      · exact fun h => False.elim (hne h)
      · intro h
        exact False.elim (he ⟨hne,h.2,by omega⟩)
  · rename_i hs
    simp only [hb,Option.some.injEq]
    constructor
    · exact fun h => False.elim (hne h)
    · intro h
      omega

def connectors (s : State) : Nat := s.assembly.contacts.length+s.routes.length+s.assembly.spare

def material (s : State) : Nat := s.assembly.work.built.cells.length+s.assembly.work.supply.pool.length

def support (s : State) : Nat := s.assembly.work.supply.free+s.assembly.work.supply.spent

theorem connect_accounts (s : State) (i j : Nat) :
    connectors (connect i j s) = connectors s ∧ material (connect i j s) = material s ∧
      support (connect i j s) = support s := by
  unfold connect
  split <;> simp_all [connectors,material,support,CopyingRegistration.spendOne] <;> omega

theorem inspect_accounts (s : State) (i : Nat) :
    connectors (inspect i s) = connectors s ∧ material (inspect i s) = material s ∧
      support (inspect i s) = support s := by
  unfold inspect
  split
  · split
    · rename_i x old _ _ hf
      have hm := (exchange_material i x (CopyingRegistration.spendOne s.assembly.work)).length_eq
      simp only [List.length_append,CopyingRegistration.spendOne] at hm
      refine ⟨rfl,hm.symm,?_⟩
      dsimp only [support]
      rw [exchange_support]
      dsimp only [CopyingRegistration.spendOne]
      omega
    · exact ⟨rfl,rfl,rfl⟩
  · exact ⟨rfl,rfl,rfl⟩

inductive Event where
  | assembly (event : CopyingRegistration.Event)
  | connect (i j : Nat)
  | inspect (i : Nat)
  deriving DecidableEq, Repr

def step (law : StructuralCopying.Law) (s : State) : Event → State
  | .assembly e => {s with assembly := CopyingRegistration.step law s.assembly e}
  | .connect i j => connect i j s
  | .inspect i => inspect i s

def run (law : StructuralCopying.Law) : List Event → State → State
  | [],s => s
  | e::es,s => run law es (step law s e)

def process (law : StructuralCopying.Law) : Generative.Process State Event :=
  ⟨fun s e t => step law s e = t⟩

theorem run_is_trace (law : StructuralCopying.Law) (es : List Event) (s : State) :
    Generative.Trace (process law) s es (run law es s) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons rfl (ih _)

theorem step_accounts (law : StructuralCopying.Law) (s : State) (e : Event) :
    connectors (step law s e) = connectors s ∧ material (step law s e) = material s ∧
      support (step law s e) = support s := by
  cases e with
  | assembly e =>
    have h := CopyingRegistration.step_accounts law s.assembly e
    exact ⟨by dsimp [step,connectors]; omega,h.2.1,h.2.2⟩
  | connect i j => exact connect_accounts s i j
  | inspect i => exact inspect_accounts s i

theorem history_accounts (law : StructuralCopying.Law) (es : List Event) (s : State) :
    connectors (run law es s) = connectors s ∧ material (run law es s) = material s ∧
      support (run law es s) = support s := by
  induction es generalizing s with
  | nil => exact ⟨rfl,rfl,rfl⟩
  | cons e es ih =>
    obtain ⟨a,b,c⟩ := ih (step law s e)
    obtain ⟨d,e,f⟩ := step_accounts law s e
    exact ⟨a.trans d,b.trans e,c.trans f⟩

def damaged (budget : Nat) : State :=
  ⟨CopyingRegistration.run StructuralCopying.alternatingEasy
    (.slip 1 0::CopyingRegistration.copying) (CopyingRegistration.prepared budget),[]⟩

def repairPlan : List Event := [.assembly (.lose 1),.connect 1 1,.inspect 1]

def repaired (budget : Nat) : State := run StructuralCopying.alternatingEasy repairPlan (damaged budget)

theorem damaged_producer_enters_repair :
    (damaged 15).assembly.work.built.cells = [false,false,false,true] ∧
    (damaged 15).assembly.work.supply = ⟨[true],4,11⟩ ∧
    (damaged 15).assembly.spare = 0 ∧ (damaged 15).routes = [] := by decide

theorem formed_route_edits_actual_product :
    (repaired 15).assembly.work.built = StructuralCopying.alternating ∧
    (repaired 15).routes = [(1,1)] ∧
    (repaired 15).assembly.spare = 0 ∧ connectors (repaired 15) = 4 ∧
    (StructuralCopying.release (repaired 15).assembly.work).1 = true ∧
    (StructuralCopying.release (repaired 15).assembly.work).2.supply = ⟨[false],0,15⟩ := by decide

theorem shared_wrong_source_hides_error :
    let s := run StructuralCopying.alternatingEasy
      [.assembly (.lose 1),.connect 1 0,.inspect 1] (damaged 15)
    reference s 1 = some false ∧ s.assembly.work.built.cells[1]? = some false ∧
    s.assembly.template.cells[1]? = some true ∧
    s.assembly.work.built.cells = [false,false,false,true] := by decide

theorem wrong_reference_damages_correct_product :
    let good : State := ⟨CopyingRegistration.run StructuralCopying.alternatingEasy
      CopyingRegistration.copying (CopyingRegistration.prepared 15),[]⟩
    let s := run StructuralCopying.alternatingEasy
      [.assembly (.lose 1),.connect 1 0,.inspect 1] good
    good.assembly.work.built = StructuralCopying.alternating ∧
    s.assembly.work.built.cells = [false,false,false,true] := by decide

theorem checking_can_exhaust_editing_support :
    (StructuralCopying.release (damaged 13).assembly.work).1 = true ∧
    (repaired 13).assembly.work.built.cells = [false,false,false,true] ∧
    (repaired 13).assembly.work.supply = ⟨[true],0,13⟩ ∧
    (StructuralCopying.release (repaired 13).assembly.work).1 = false := by decide

theorem corrected_product_can_remain_unreleased :
    (repaired 14).assembly.work.built = StructuralCopying.alternating ∧
    (repaired 14).assembly.work.supply.free = 0 ∧
    (StructuralCopying.release (repaired 14).assembly.work).1 = false := by decide

theorem no_formed_route_no_edit : inspect 1 (damaged 15) = damaged 15 := by decide

theorem corrected_daughter_enters_inheritance :
    let daughter := (StructuralCopying.release (repaired 15).assembly.work).2.built
    (StructuralCopying.reproduce StructuralCopying.alternatingEasy daughter
      ⟨StructuralCopying.feed,5,15⟩).1 = true ∧
    (StructuralCopying.reproduce StructuralCopying.alternatingEasy daughter
      ⟨StructuralCopying.feed,5,15⟩).2.built = StructuralCopying.alternating := by decide

end CopyingCorrection
