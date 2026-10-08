import ContactReconstruction

/-!
Composition-dependent growth and paid routing replace a free common-parent
reset in a finite contact-reconstruction continuation. Local production law,
uniform catalyst sampling, routing recipe, stocks and partition remain explicit.
-/
namespace MaterialMaturation

structure Stock where
  cells : List Bool
  precursor : Nat
  free : Nat
  used : Nat
  deriving DecidableEq, Repr

def product (cross parent : Bool) : Bool := if cross then !parent else parent

def produce (cross parent : Bool) (s : Stock) : Stock :=
  if s.precursor == 0 || s.free == 0 then s else
    ⟨product cross parent :: s.cells,s.precursor-1,s.free-1,s.used+1⟩

theorem produce_accounts (cross parent : Bool) (s : Stock) :
    (produce cross parent s).cells.length+(produce cross parent s).precursor =
      s.cells.length+s.precursor ∧
    (produce cross parent s).free+(produce cross parent s).used = s.free+s.used := by
  unfold produce
  split <;> simp_all <;> omega

def run (cross : Bool) : List Bool → Stock → Stock
  | [], s => s
  | x::xs, s => run cross xs (produce cross x s)

theorem run_accounts (cross : Bool) (xs : List Bool) (s : Stock) :
    (run cross xs s).cells.length+(run cross xs s).precursor = s.cells.length+s.precursor ∧
    (run cross xs s).free+(run cross xs s).used = s.free+s.used := by
  induction xs generalizing s with
  | nil => exact ⟨rfl,rfl⟩
  | cons x xs ih =>
    obtain ⟨ha,hb⟩ := ih (produce cross x s)
    obtain ⟨hc,hd⟩ := produce_accounts cross x s
    exact ⟨ha.trans hc,hb.trans hd⟩

theorem supported_run (cross : Bool) (xs : List Bool) (s : Stock)
    (hm : xs.length ≤ s.precursor) (hw : xs.length ≤ s.free) :
    (run cross xs s).cells.length = s.cells.length+xs.length ∧
    (run cross xs s).precursor+xs.length = s.precursor ∧
    (run cross xs s).free+xs.length = s.free ∧
    (run cross xs s).used = s.used+xs.length := by
  induction xs generalizing s with
  | nil => simp [run]
  | cons x xs ih =>
    have hp : 0 < s.precursor := by simp at hm; omega
    have hf : 0 < s.free := by simp at hw; omega
    have he : produce cross x s =
        ⟨product cross x::s.cells,s.precursor-1,s.free-1,s.used+1⟩ := by
      simp [produce,Nat.ne_of_gt hp,Nat.ne_of_gt hf]
    have ht := ih (produce cross x s) (by rw [he]; simp; simp at hm; omega)
      (by rw [he]; simp; simp at hw; omega)
    simp only [run]
    rw [he]
    rw [he] at ht
    dsimp at ht
    simp only [List.length_cons]
    omega

theorem counts_length (xs : List Bool) : xs.count false+xs.count true = xs.length := by
  induction xs with
  | nil => rfl
  | cons x xs ih => cases x <;> simp_all <;> omega

theorem total_by_kind (xs : List Bool) (f : Bool → Rat) :
    ContactReconstruction.total f xs = (xs.count false:Rat)*f false+(xs.count true:Rat)*f true := by
  induction xs with
  | nil => simp [ContactReconstruction.total]; grind
  | cons x xs ih => cases x <;> simp [ContactReconstruction.total,ih,Rat.natCast_add] <;> grind

def expected (cross : Bool) : Nat → (Stock → Rat) → Stock → Rat
  | 0, f, s => f s
  | n+1, f, s => if s.cells.isEmpty || s.precursor == 0 || s.free == 0 then f s else
      ContactReconstruction.total (fun x => expected cross n f (produce cross x s)) s.cells /
        (s.cells.length:Rat)

/-- Rates are read from the actual catalyst counts. cross=false produces its
    own type; cross=true produces the other type. Both use one precursor. -/
def countExpected (cross : Bool) : Nat → (Nat → Nat → Rat) → Nat → Nat → Rat
  | 0, f, a, b => f a b
  | n+1, f, a, b =>
      ((b:Rat)/(a+b:Nat))*
        countExpected cross n f (if cross then a+1 else a) (if cross then b else b+1)+
      (1-(b:Rat)/(a+b:Nat))*
        countExpected cross n f (if cross then a else a+1) (if cross then b+1 else b)

theorem growth_projection (cross : Bool) (n : Nat) (f : Nat → Nat → Rat) (s : Stock)
    (hne : s.cells ≠ []) (hm : n ≤ s.precursor) (hw : n ≤ s.free) :
    expected cross n (fun t => f (t.cells.count false) (t.cells.count true)) s =
      countExpected cross n f (s.cells.count false) (s.cells.count true) := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
    have hp : 0 < s.precursor := by omega
    have hf : 0 < s.free := by omega
    have hstop : (s.cells.isEmpty || s.precursor == 0 || s.free == 0) = false := by
      cases hc : s.cells <;> simp_all <;> omega
    have he (x : Bool) : produce cross x s =
        ⟨product cross x::s.cells,s.precursor-1,s.free-1,s.used+1⟩ := by
      simp [produce,Nat.ne_of_gt hp,Nat.ne_of_gt hf]
    have hh (x : Bool) := ih (produce cross x s) (by rw [he]; simp)
      (by rw [he]; simp; omega) (by rw [he]; simp; omega)
    simp only [expected,hstop,Bool.false_eq_true,↓reduceIte]
    rw [total_by_kind,hh false,hh true,he false,he true]
    have hl := counts_length s.cells
    have hlq : (s.cells.count false:Rat)+(s.cells.count true:Rat) = (s.cells.length:Rat) := by
      exact_mod_cast hl
    have hlen : (s.cells.length:Rat) ≠ 0 := by
      have : s.cells.length ≠ 0 := by simp_all
      exact_mod_cast this
    simp only [countExpected]
    rw [hl]
    cases cross <;> simp [product] <;> grind

def canonical : List Bool := [false,false,false,true,false,true,true,true]

theorem count_expected_mass (cross : Bool) (n a b : Nat) :
    countExpected cross n (fun _ _ => 1) a b = 1 := by
  induction n generalizing a b with
  | zero => rfl
  | succ n ih => simp only [countExpected,ih]; grind

theorem expected_mass (cross : Bool) (n : Nat) (s : Stock)
    (hne : s.cells ≠ []) (hm : n ≤ s.precursor) (hw : n ≤ s.free) :
    expected cross n (fun _ => 1) s = 1 := by
  have h := growth_projection cross n (fun _ _ => 1) s hne hm hw
  exact h.trans (count_expected_mass cross n _ _)

/-- Routing physically removes an available token for each requested slot.
    The recipe is supplied; it does not manufacture a missing component. -/
def route : List Bool → List Bool → Nat → Option (List Bool × Nat)
  | [], pool, fuel => some (pool,fuel)
  | x::xs, pool, fuel => if x ∈ pool ∧ 0 < fuel then route xs (pool.erase x) (fuel-1) else none

structure Routing where
  leftover : List Bool
  placed : List Bool
  free : Nat
  deriving DecidableEq, Repr

/-- Failed preparation keeps the partially placed tokens, remaining pool and
    unused work. No failure is silently counted as costless or material loss. -/
def routeTrace : List Bool → List Bool → Nat → Routing
  | [], pool, fuel => ⟨pool,[],fuel⟩
  | x::xs, pool, fuel => if x ∈ pool ∧ 0 < fuel then
      let t := routeTrace xs (pool.erase x) (fuel-1)
      ⟨t.leftover,x::t.placed,t.free⟩
    else ⟨pool,[],fuel⟩

theorem routing_trace_accounts (target pool : List Bool) (fuel : Nat) :
    let t := routeTrace target pool fuel
    pool.Perm (t.placed++t.leftover) ∧ t.free+t.placed.length = fuel ∧
      t.placed.length ≤ target.length := by
  induction target generalizing pool fuel with
  | nil => simp [routeTrace]
  | cons x xs ih =>
    simp only [routeTrace]
    split
    · obtain ⟨hm,hf⟩ := ‹x ∈ pool ∧ 0 < fuel›
      obtain ⟨ha,hb,hc⟩ := ih (pool.erase x) (fuel-1)
      refine ⟨(List.perm_cons_erase hm).trans (List.Perm.cons x ha),?_,?_⟩
      · simp only [List.length_cons]; omega
      · simp only [List.length_cons]; omega
    · simp

theorem route_trace_projection (target pool : List Bool) (fuel : Nat) :
    route target pool fuel =
      if (routeTrace target pool fuel).placed = target then
        some ((routeTrace target pool fuel).leftover,(routeTrace target pool fuel).free) else none := by
  induction target generalizing pool fuel with
  | nil => rfl
  | cons x xs ih =>
    simp only [route,routeTrace]
    split
    · simp only [List.cons.injEq,true_and]
      exact ih (pool.erase x) (fuel-1)
    · simp

theorem canonical_slots_match_parent :
    (List.range 8).map (fun i => canonical[i]!) =
      ContactReconstruction.parentComponents.map ContactReconstruction.labels := by decide +kernel

theorem partial_routing_preserves_unused_components_and_work :
    routeTrace canonical [false,false,false,false,false,false,false,true] 8 =
      ⟨[false,false,false],[false,false,false,true,false],3⟩ := by decide +kernel

theorem route_sound (target pool : List Bool) (fuel : Nat) (rest : List Bool) (left : Nat)
    (h : route target pool fuel = some (rest,left)) :
    pool.Perm (target++rest) ∧ left+target.length = fuel := by
  induction target generalizing pool fuel with
  | nil => simp [route] at h; obtain ⟨rfl,rfl⟩ := h; simp
  | cons x xs ih =>
    simp only [route] at h
    split at h
    · obtain ⟨hm,hf⟩ := ‹x ∈ pool ∧ 0 < fuel›
      obtain ⟨ha,hb⟩ := ih (pool.erase x) (fuel-1) h
      refine ⟨(List.perm_cons_erase hm).trans (List.Perm.cons x ha),?_⟩
      simp only [List.length_cons]
      omega
    · cases h

theorem route_complete (target pool : List Bool) (fuel : Nat)
    (hp : pool.Perm target) (hf : target.length ≤ fuel) :
    route target pool fuel = some ([],fuel-target.length) := by
  induction target generalizing pool fuel with
  | nil => have h : pool = [] := List.perm_nil.mp hp; simp [route,h]
  | cons x xs ih =>
    have hm : x ∈ pool := hp.mem_iff.mpr (by simp)
    have hpos : 0 < fuel := by simp at hf; omega
    have hrem : (pool.erase x).Perm xs := by
      have he := hp.erase x
      simpa using he
    have hi := ih (pool.erase x) (fuel-1) hrem (by simp at hf; omega)
    simp only [route,hm,hpos,and_self,↓reduceIte,hi]
    congr 2
    simp only [List.length_cons]
    omega

theorem canonical_iff_counts (pool : List Bool) :
    pool.Perm canonical ↔ pool.count false = 4 ∧ pool.count true = 4 := by
  rw [List.perm_iff_count]
  constructor
  · intro h; exact ⟨h false,h true⟩
  · intro h b; cases b <;> simp_all [canonical]

theorem actual_preparation_iff (pool : List Bool) :
    route canonical pool 8 = some ([],0) ↔ pool.count false = 4 ∧ pool.count true = 4 := by
  constructor
  · intro h
    have hp := (route_sound canonical pool 8 [] 0 h).1
    simp only [List.append_nil] at hp
    exact (canonical_iff_counts pool).mp hp
  · intro h
    have hp := (canonical_iff_counts pool).mpr h
    exact route_complete canonical pool 8 hp (by decide)

def ready (s : Stock) : Rat := if route canonical s.cells 8 = some ([],0) then 1 else 0
def balanced (a b : Nat) : Rat := if a = 4 ∧ b = 4 then 1 else 0

theorem ready_is_balance (s : Stock) : ready s = balanced (s.cells.count false) (s.cells.count true) := by
  simp only [ready,balanced,actual_preparation_iff]

def growReturn (cross : Bool) (xs : List Bool) : Rat :=
  expected cross 4 ready ⟨xs,4,4,0⟩

theorem return_from_composition (cross : Bool) (xs : List Bool) (hne : xs ≠ []) :
    growReturn cross xs = countExpected cross 4 balanced (xs.count false) (xs.count true) := by
  unfold growReturn
  have heq : ready = (fun s => balanced (s.cells.count false) (s.cells.count true)) := by
    funext s; exact ready_is_balance s
  rw [heq]
  exact growth_projection cross 4 balanced ⟨xs,4,4,0⟩ hne (by change 4 ≤ 4; decide) (by change 4 ≤ 4; decide)

theorem exact_maturation_rates :
    countExpected false 4 balanced 2 2 = 9/35 ∧
    countExpected false 4 balanced 3 1 = 3/35 ∧
    countExpected false 4 balanced 1 3 = 3/35 ∧
    countExpected true 4 balanced 2 2 = 52/105 ∧
    countExpected true 4 balanced 3 1 = 47/105 ∧
    countExpected true 4 balanced 1 3 = 47/105 := by decide +kernel

def seedCells (s : ContactReconstruction.Seed) : List Bool := s.members.map ContactReconstruction.labels

/-- Contact support, growth stock and eight routing work units are separately
    allocated. Growth begins only after a formed contact, and uses fresh draws
    from the changing list. Contact identity does not alter the growth law. -/
def pipeline (cross : Bool) (seed : ContactReconstruction.Seed) : Rat :=
  ContactReconstruction.expected ContactReconstruction.labels seed 2
    (fun s => if s.bond.isSome then growReturn cross (seedCells seed) else 0) ⟨2,0,none⟩

def batchReturn (cross : Bool) (seeds : List ContactReconstruction.Seed) : Rat :=
  ContactReconstruction.total (pipeline cross) seeds

theorem total_scale {α : Type} (xs : List α) (f : α → Rat) (c : Rat) :
    ContactReconstruction.total (fun x => f x*c) xs = ContactReconstruction.total f xs*c := by
  induction xs with
  | nil => simp [ContactReconstruction.total]
  | cons x xs ih => simp only [ContactReconstruction.total,ih]; grind

theorem contact_expected_scale (lab : Nat → Bool) (seed : ContactReconstruction.Seed)
    (n : Nat) (f : ContactReconstruction.State → Rat) (c : Rat) (s : ContactReconstruction.State) :
    ContactReconstruction.expected lab seed n (fun t => f t*c) s =
      ContactReconstruction.expected lab seed n f s*c := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
    simp only [ContactReconstruction.expected]
    split
    · rfl
    · simp only [ContactReconstruction.meanDraw]
      have he : (fun e => ContactReconstruction.expected lab seed n (fun t => f t*c)
          (ContactReconstruction.encounter lab seed e s)) =
          (fun e => ContactReconstruction.expected lab seed n f
            (ContactReconstruction.encounter lab seed e s)*c) := by
        funext e; exact ih _
      rw [he,total_scale]
      grind

theorem pipeline_factorization (cross : Bool) (seed : ContactReconstruction.Seed)
    (hne : seed.contacts.length ≠ 0) :
    pipeline cross seed =
      AssemblyDerivedSelection.success (ContactReconstruction.rate ContactReconstruction.labels seed) 2*
        growReturn cross (seedCells seed) := by
  unfold pipeline
  have he : (fun s : ContactReconstruction.State =>
      if s.bond.isSome then growReturn cross (seedCells seed) else 0) =
      (fun s => ContactReconstruction.reconstructed s*growReturn cross (seedCells seed)) := by
    funext s
    unfold ContactReconstruction.reconstructed
    split <;> grind
  rw [he,contact_expected_scale]
  rw [ContactReconstruction.reconstruction_from_contacts _ _ hne 2 2 (by decide)]

theorem actual_compositions :
    ContactReconstruction.concentrated.map (fun s => ((seedCells s).count false,(seedCells s).count true)) = [(2,2),(2,2)] ∧
    ContactReconstruction.distributed.map (fun s => ((seedCells s).count false,(seedCells s).count true)) = [(3,1),(1,3)] := by decide +kernel

theorem exact_joint_returns :
    batchReturn false ContactReconstruction.concentrated = 9/35 ∧
    batchReturn false ContactReconstruction.distributed = 9/70 ∧
    batchReturn true ContactReconstruction.concentrated = 52/105 ∧
    batchReturn true ContactReconstruction.distributed = 47/70 := by decide +kernel

theorem maturation_reverses_contact_ranking :
    ContactReconstruction.batchOutput 2 ContactReconstruction.concentrated <
      ContactReconstruction.batchOutput 2 ContactReconstruction.distributed ∧
    batchReturn false ContactReconstruction.distributed <
      batchReturn false ContactReconstruction.concentrated ∧
    batchReturn true ContactReconstruction.concentrated <
      batchReturn true ContactReconstruction.distributed := by
  have h := exact_joint_returns
  have hc := ContactReconstruction.same_first_different_second
  grind

theorem both_laws_below_replacement :
    batchReturn false ContactReconstruction.concentrated < 1 ∧
    batchReturn false ContactReconstruction.distributed < 1 ∧
    batchReturn true ContactReconstruction.concentrated < 1 ∧
    batchReturn true ContactReconstruction.distributed < 1 := by
  have h := exact_joint_returns
  grind

theorem same_type_cannot_invent_missing_kind (parent : Bool) (s : Stock)
    (hm : parent ∈ s.cells) (ha : true ∉ s.cells) :
    true ∉ (produce false parent s).cells := by
  have hp : parent = false := by cases parent <;> simp_all
  unfold produce
  split <;> simp_all [product]

theorem opposite_production_can_form_missing_kind :
    (produce true false ⟨[false],1,1,0⟩).cells = [true,false] := by decide +kernel

end MaterialMaturation
