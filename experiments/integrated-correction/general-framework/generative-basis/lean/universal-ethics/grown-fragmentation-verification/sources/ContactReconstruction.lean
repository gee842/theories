import AssemblyDerivedSelection

/-!
Actual transmitted components and internal contact opportunities determine
reconstruction. Bonds start absent and are formed by paid encounters, never
copied from a parental Boolean. Uniform sampling with replacement, binary
compatibility, the partition and stocks are explicit local premises.
-/
namespace ContactReconstruction

abbrev Edge := Nat × Nat

structure Seed where
  members : List Nat
  contacts : List Edge
  deriving DecidableEq, Repr

def internal (xs : List Nat) (e : Edge) : Bool :=
  xs.contains e.1 && xs.contains e.2

def transmit (xs : List Nat) (contacts : List Edge) : Seed :=
  ⟨xs, contacts.filter (internal xs)⟩

def compatible (labels : Nat → Bool) (s : Seed) (e : Edge) : Bool :=
  internal s.members e && (labels e.1 != labels e.2)

structure State where
  free : Nat
  used : Nat
  bond : Option Edge
  deriving DecidableEq, Repr

def encounter (labels : Nat → Bool) (seed : Seed) (e : Edge) (s : State) : State :=
  if s.bond.isSome || s.free == 0 then s else
    ⟨s.free-1,s.used+1,if compatible labels seed e then some e else none⟩

def project (s : State) : AssemblyDerivedSelection.Local :=
  ⟨s.free,s.used,s.bond.isSome,0⟩

theorem encounter_projection (labels : Nat → Bool) (seed : Seed) (e : Edge) (s : State) :
    project (encounter labels seed e s) =
      AssemblyDerivedSelection.attempt (compatible labels seed e) (project s) := by
  simp only [encounter,project,AssemblyDerivedSelection.attempt]
  split <;> simp_all
  split <;> simp_all

theorem encounter_accounts (labels : Nat → Bool) (seed : Seed) (e : Edge) (s : State) :
    (encounter labels seed e s).free+(encounter labels seed e s).used = s.free+s.used := by
  have h := AssemblyDerivedSelection.attempt_accounts (compatible labels seed e) (project s)
  rw [← encounter_projection] at h
  exact h.1

def replay (labels : Nat → Bool) (seed : Seed) : List Edge → State → State
  | [], s => s
  | e::es, s => replay labels seed es (encounter labels seed e s)

theorem replay_accounts (labels : Nat → Bool) (seed : Seed) (es : List Edge) (s : State) :
    (replay labels seed es s).free+(replay labels seed es s).used = s.free+s.used := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    rw [replay,ih,encounter_accounts]

theorem formed_bond_has_transmitted_endpoints (labels : Nat → Bool) (seed : Seed)
    (e f : Edge) (b u : Nat)
    (h : (encounter labels seed e ⟨b,u,none⟩).bond = some f) :
    f = e ∧ e.1 ∈ seed.members ∧ e.2 ∈ seed.members ∧ labels e.1 ≠ labels e.2 := by
  simp only [encounter] at h
  split at h
  · simp_all
  · split at h
    · simp_all [compatible,internal]
    · simp_all

def total {α : Type} (f : α → Rat) : List α → Rat
  | [] => 0
  | x::xs => f x + total f xs

def hits (labels : Nat → Bool) (seed : Seed) : Nat :=
  (seed.contacts.filter (compatible labels seed)).length

def rate (labels : Nat → Bool) (seed : Seed) : Rat :=
  (hits labels seed : Rat)/(seed.contacts.length : Rat)

theorem total_binary {α : Type} (test : α → Bool) (xs : List α) (yes no : Rat) :
    total (fun x => if test x then yes else no) xs =
      ((xs.filter test).length:Rat)*yes+
        ((xs.length:Rat)-((xs.filter test).length:Rat))*no := by
  induction xs with
  | nil => simp [total]; grind
  | cons x xs ih =>
    cases hx : test x <;> simp [total,hx,ih,Rat.natCast_add] <;> grind

theorem rate_bounds (labels : Nat → Bool) (seed : Seed) :
    0 ≤ rate labels seed ∧ rate labels seed ≤ 1 := by
  have hn : hits labels seed ≤ seed.contacts.length := List.length_filter_le _ _
  have hnq : (hits labels seed:Rat) ≤ (seed.contacts.length:Rat) := by exact_mod_cast hn
  by_cases hz : seed.contacts.length = 0
  · have hh : hits labels seed = 0 := by omega
    simp [rate,hz,hh]
    grind
  have hp : 0 < (seed.contacts.length:Rat) := by exact_mod_cast (show 0 < seed.contacts.length by omega)
  have hi := Rat.inv_pos.mpr hp
  constructor
  · change 0 ≤ (hits labels seed:Rat)*(seed.contacts.length:Rat)⁻¹
    exact Rat.mul_nonneg (Rat.natCast_nonneg) (by grind)
  · unfold rate
    have hh := Rat.mul_le_mul_of_nonneg_right hnq (show 0 ≤ (seed.contacts.length:Rat)⁻¹ by grind)
    grind

def meanDraw (labels : Nat → Bool) (seed : Seed) (f : State → Rat) (s : State) : Rat :=
  total (fun e => f (encounter labels seed e s)) seed.contacts / (seed.contacts.length:Rat)

theorem draw_reduction (labels : Nat → Bool) (seed : Seed) (hne : seed.contacts.length ≠ 0)
    (f : AssemblyDerivedSelection.Local → Rat) (s : State) :
    meanDraw labels seed (fun s => f (project s)) s =
      rate labels seed*f (AssemblyDerivedSelection.attempt true (project s))+
      (1-rate labels seed)*f (AssemblyDerivedSelection.attempt false (project s)) := by
  have heq : (fun e => f (project (encounter labels seed e s))) =
      (fun e => if compatible labels seed e then
        f (AssemblyDerivedSelection.attempt true (project s)) else
        f (AssemblyDerivedSelection.attempt false (project s))) := by
    funext e
    rw [encounter_projection]
    cases compatible labels seed e <;> rfl
  unfold meanDraw
  rw [heq,total_binary]
  have hq : (seed.contacts.length:Rat) ≠ 0 := by exact_mod_cast hne
  unfold rate hits
  grind

/-- Finite independent uniform encounters, with replacement. A stopped
    trajectory incurs no further cost even if a nominal draw is present. -/
def expected (labels : Nat → Bool) (seed : Seed) : Nat → (State → Rat) → State → Rat
  | 0, f, s => f s
  | n+1, f, s => if seed.contacts.isEmpty then f s else
      meanDraw labels seed (expected labels seed n f) s

def binaryExpected (p : Rat) : Nat → (AssemblyDerivedSelection.Local → Rat) →
    AssemblyDerivedSelection.Local → Rat
  | 0, f, s => f s
  | n+1, f, s => p*binaryExpected p n f (AssemblyDerivedSelection.attempt true s)+
      (1-p)*binaryExpected p n f (AssemblyDerivedSelection.attempt false s)

theorem expectation_projection (labels : Nat → Bool) (seed : Seed)
    (hne : seed.contacts.length ≠ 0) (n : Nat)
    (f : AssemblyDerivedSelection.Local → Rat) (s : State) :
    expected labels seed n (fun s => f (project s)) s =
      binaryExpected (rate labels seed) n f (project s) := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
    have hempty : seed.contacts.isEmpty = false := by
      cases h : seed.contacts <;> simp_all
    simp only [expected,hempty,Bool.false_eq_true,↓reduceIte]
    have hf : expected labels seed n (fun s => f (project s)) =
        (fun s => binaryExpected (rate labels seed) n f (project s)) := by
      funext s; exact ih s
    rw [hf,draw_reduction labels seed hne]
    rfl

theorem stopped_binary (p : Rat) (n : Nat) (f : AssemblyDerivedSelection.Local → Rat)
    (s : AssemblyDerivedSelection.Local) (h : (s.linked || s.free == 0) = true) :
    binaryExpected p n f s = f s := by
  induction n with
  | zero => rfl
  | succ n ih => simp [binaryExpected,AssemblyDerivedSelection.attempt,h,ih]; grind

theorem binary_is_tree (p : Rat) (n : Nat) (f : AssemblyDerivedSelection.Local → Rat)
    (s : AssemblyDerivedSelection.Local) :
    binaryExpected p n f s = AssemblyDerivedSelection.average p f (AssemblyDerivedSelection.tree n s) := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
    by_cases hs : (s.linked || s.free == 0) = true
    · rw [stopped_binary p (n+1) f s hs]
      simp [AssemblyDerivedSelection.tree,hs,AssemblyDerivedSelection.average]
    · have hh : (AssemblyDerivedSelection.attempt true s).linked = true := by
        simp [AssemblyDerivedSelection.attempt,hs]
      rw [binaryExpected,stopped_binary p n f _ (by simp [hh]),ih]
      simp [AssemblyDerivedSelection.tree,hs,AssemblyDerivedSelection.average]

theorem expected_mass (labels : Nat → Bool) (seed : Seed)
    (hne : seed.contacts.length ≠ 0) (n : Nat) (s : State) :
    expected labels seed n (fun _ => 1) s = 1 := by
  have h := expectation_projection labels seed hne n (fun _ => 1) s
  rw [binary_is_tree] at h
  exact h.trans (AssemblyDerivedSelection.average_mass _ _)

def reconstructed (s : State) : Rat := if s.bond.isSome then 1 else 0

theorem reconstruction_from_contacts (labels : Nat → Bool) (seed : Seed)
    (hne : seed.contacts.length ≠ 0) (n b : Nat) (hb : n ≤ b) :
    expected labels seed n reconstructed ⟨b,0,none⟩ =
      AssemblyDerivedSelection.success (rate labels seed) n := by
  have h := expectation_projection labels seed hne n (fun s => if s.linked then 1 else 0) ⟨b,0,none⟩
  rw [binary_is_tree] at h
  exact h.trans (AssemblyDerivedSelection.success_from_tree _ n b 0 0 hb)

theorem cost_from_contacts (labels : Nat → Bool) (seed : Seed)
    (hne : seed.contacts.length ≠ 0) (n b : Nat) (hb : n ≤ b) :
    expected labels seed n (fun s => (s.used:Rat)) ⟨b,0,none⟩ =
      AssemblyDerivedSelection.cost (rate labels seed) n := by
  have h := expectation_projection labels seed hne n (fun s => (s.used:Rat)) ⟨b,0,none⟩
  rw [binary_is_tree] at h
  have ht := (AssemblyDerivedSelection.tree_expectations (rate labels seed) n b 0 0 hb).2.2
  have ht2 : AssemblyDerivedSelection.average (rate labels seed) (fun s => (s.used:Rat))
      (AssemblyDerivedSelection.tree n (project ⟨b,0,none⟩)) = AssemblyDerivedSelection.cost (rate labels seed) n := by
    change _ = _ at ht
    dsimp [project]
    grind
  exact h.trans ht2

theorem singleton_cannot_reconstruct (labels : Nat → Bool) (x : Nat) (es : List Edge) :
    hits labels (transmit [x] es) = 0 := by
  unfold hits
  have hf : ∀ e, compatible labels (transmit [x] es) e = false := by
    intro e
    simp [compatible,transmit,internal]
    grind
  simp [hf]

theorem empty_contacts_stay_unbonded (labels : Nat → Bool) (members : List Nat) (n b : Nat) :
    expected labels ⟨members,[]⟩ n reconstructed ⟨b,0,none⟩ = 0 := by
  cases n <;> simp [expected,reconstructed]

theorem zero_rate_never_succeeds (n : Nat) : AssemblyDerivedSelection.success 0 n = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp [AssemblyDerivedSelection.success,ih]; grind

theorem singleton_no_reconstruction (labels : Nat → Bool) (x : Nat) (es : List Edge)
    (n b : Nat) (hb : n ≤ b) :
    expected labels (transmit [x] es) n reconstructed ⟨b,0,none⟩ = 0 := by
  by_cases he : (transmit [x] es).contacts.length = 0
  · have hempty : (transmit [x] es).contacts = [] := List.eq_nil_of_length_eq_zero he
    have hseed : transmit [x] es = ⟨[x],[]⟩ := by
      change Seed.mk [x] (transmit [x] es).contacts = _
      rw [hempty]
    rw [hseed]
    exact empty_contacts_stay_unbonded labels [x] n b
  · rw [reconstruction_from_contacts labels _ he n b hb]
    have hr : rate labels (transmit [x] es) = 0 := by
      unfold rate
      rw [singleton_cannot_reconstruct]
      grind
    rw [hr,zero_rate_never_succeeds]

/-- For two independently reconstructed seeds, averaging contact rates loses
    the variation term. No biological superiority follows from this identity. -/
theorem two_attempt_heterogeneity (p q : Rat) :
    AssemblyDerivedSelection.success p 2+AssemblyDerivedSelection.success q 2 =
      2*AssemblyDerivedSelection.success ((p+q)/2) 2-(p-q)^2/2 := by
  simp [AssemblyDerivedSelection.success,Rat.pow_succ]
  grind

theorem two_attempt_cost_equal (p q : Rat) :
    AssemblyDerivedSelection.cost p 2+AssemblyDerivedSelection.cost q 2 =
      2*AssemblyDerivedSelection.cost ((p+q)/2) 2 := by
  simp [AssemblyDerivedSelection.cost]
  grind

theorem one_attempt_mean_suffices (p q : Rat) :
    AssemblyDerivedSelection.success p 1+AssemblyDerivedSelection.success q 1 =
      2*AssemblyDerivedSelection.success ((p+q)/2) 1 := by
  simp [AssemblyDerivedSelection.success]
  grind

theorem strict_heterogeneity_loss (p q : Rat) (hne : p ≠ q) :
    AssemblyDerivedSelection.success p 2+AssemblyDerivedSelection.success q 2 <
      2*AssemblyDerivedSelection.success ((p+q)/2) 2 := by
  have hs : 0 < (p-q)^2 := by
    by_cases hp : p < q
    · have hh := Rat.mul_pos (show 0 < q-p by grind) (show 0 < q-p by grind)
      simp only [Rat.pow_succ] at *
      grind
    · have hh := Rat.mul_pos (show 0 < p-q by grind) (show 0 < p-q by grind)
      simp only [Rat.pow_succ] at *
      grind
  rw [two_attempt_heterogeneity]
  grind

def parentComponents : List Nat := [0,1,2,3,4,5,6,7]
def parentContacts : List Edge := [(0,1),(2,3),(4,5),(6,7)]
def labels (i : Nat) : Bool := [3,5,6,7].contains i
def concentrated : List Seed :=
  [transmit [0,1,6,7] parentContacts,transmit [2,3,4,5] parentContacts]
def distributed : List Seed :=
  [transmit [0,1,2,3] parentContacts,transmit [4,5,6,7] parentContacts]
def severed : List Seed :=
  [transmit [0,2,4,6] parentContacts,transmit [1,3,5,7] parentContacts]

theorem actual_partitions :
    (concentrated.flatMap Seed.members).length = parentComponents.length ∧
    (distributed.flatMap Seed.members).length = parentComponents.length ∧
    parentComponents.all (fun i => (concentrated.flatMap Seed.members).count i == 1) = true ∧
    parentComponents.all (fun i => (distributed.flatMap Seed.members).count i == 1) = true ∧
    parentContacts.all (fun e => (concentrated.flatMap Seed.contacts).count e == 1) = true ∧
    parentContacts.all (fun e => (distributed.flatMap Seed.contacts).count e == 1) = true ∧
    concentrated.map (fun s => s.members.length) = [4,4] ∧
    distributed.map (fun s => s.members.length) = [4,4] ∧
    concentrated.map (fun s => s.contacts.length) = [2,2] ∧
    distributed.map (fun s => s.contacts.length) = [2,2] := by decide +kernel

theorem actual_rates :
    concentrated.map (rate labels) = [0,1] ∧
    distributed.map (rate labels) = [1/2,1/2] ∧
    total (rate labels) concentrated = total (rate labels) distributed ∧
    concentrated.map (hits labels) = [0,2] ∧
    distributed.map (hits labels) = [1,1] := by decide +kernel

def batchOutput (n : Nat) (ss : List Seed) : Rat :=
  total (fun seed => expected labels seed n reconstructed ⟨n,0,none⟩) ss

def batchCost (n : Nat) (ss : List Seed) : Rat :=
  total (fun seed => expected labels seed n (fun s => (s.used:Rat)) ⟨n,0,none⟩) ss

theorem same_first_different_second :
    batchOutput 1 concentrated = 1 ∧ batchOutput 1 distributed = 1 ∧
    batchOutput 2 concentrated = 1 ∧ batchOutput 2 distributed = 3/2 ∧
    batchCost 2 concentrated = 3 ∧ batchCost 2 distributed = 3 := by decide +kernel

theorem opposed_cycle_comparison :
    batchOutput 2 concentrated < 5/4 ∧ 5/4 < batchOutput 2 distributed := by decide +kernel

theorem severed_partition_preserves_components_loses_contacts :
    (severed.flatMap Seed.members).length = parentComponents.length ∧
    parentComponents.all (fun i => (severed.flatMap Seed.members).count i == 1) = true ∧
    severed.map (fun s => s.contacts.length) = [0,0] ∧
    batchOutput 2 severed = 0 ∧ batchCost 2 severed = 0 := by decide +kernel

/-- Counts of distinct unorganized seed types cannot in general be collapsed
    to one P count. This is a failure of that projection, not of matrix models. -/
theorem no_aggregate_return_coefficient (p q : Rat)
    (hne : AssemblyDerivedSelection.success p 2 ≠ AssemblyDerivedSelection.success q 2) :
    ¬ ∃ r : Rat, ∀ u v : Rat, 0 ≤ u → 0 ≤ v →
      AssemblyDerivedSelection.success p 2*u+AssemblyDerivedSelection.success q 2*v = r*(u+v) := by
  rintro ⟨r,hr⟩
  have h1 := hr 1 0 (by decide) (by decide)
  have h2 := hr 0 1 (by decide) (by decide)
  grind

/-- Conditional stage model: a prepared mature unit produces one seed of
    each type; seeds return with their derived probabilities; failures exit.
    Mature preparation, replenishment and equal stage timing remain supplied. -/
structure Stages where
  mature : Rat
  first : Rat
  second : Rat

def next (p q : Rat) (s : Stages) : Stages :=
  ⟨AssemblyDerivedSelection.success p 2*s.first+
    AssemblyDerivedSelection.success q 2*s.second,s.mature,s.mature⟩

theorem typed_two_step (p q : Rat) (s : Stages) :
    (next p q (next p q s)).mature =
      (AssemblyDerivedSelection.success p 2+AssemblyDerivedSelection.success q 2)*s.mature ∧
    (next p q s).first = (next p q s).second := by
  simp only [next]
  constructor <;> grind

theorem balanced_stage_reduction (p q : Rat) (s : Stages) (h : s.first = s.second) :
    (next p q s).mature =
      ((AssemblyDerivedSelection.success p 2+AssemblyDerivedSelection.success q 2)/2)*
        (s.first+s.second) := by
  simp only [next]
  grind

def cycles (p q o : Rat) : Nat → Stages
  | 0 => ⟨o,0,0⟩
  | n+1 => next p q (next p q (cycles p q o n))

theorem conditional_cycle_return (p q o : Rat) (n : Nat) :
    (cycles p q o n).mature =
      (AssemblyDerivedSelection.success p 2+AssemblyDerivedSelection.success q 2)^n*o := by
  induction n with
  | zero => simp [cycles]
  | succ n ih =>
    change (next p q (next p q (cycles p q o n))).mature = _
    rw [(typed_two_step p q _).1,ih,Rat.pow_succ]
    grind

end ContactReconstruction
