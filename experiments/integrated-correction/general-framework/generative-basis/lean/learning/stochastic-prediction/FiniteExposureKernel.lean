import Exposure

namespace StochasticPrediction

abbrev Weighted (α : Type) := List (α × Nat)

def mass {α : Type} : Weighted α → Nat
  | [] => 0
  | (_,w)::xs => w+mass xs

def image {α β : Type} (f : α → β) (xs : Weighted α) : Weighted β :=
  xs.map (fun (x,w) => (f x,w))

def scale {α : Type} (w : Nat) (xs : Weighted α) : Weighted α :=
  xs.map (fun (x,v) => (x,w*v))

def bind {α β : Type} (xs : Weighted α) (f : α → Weighted β) : Weighted β :=
  xs.flatMap (fun (x,w) => scale w (f x))

theorem mass_append {α : Type} (xs ys : Weighted α) :
    mass (xs++ys) = mass xs+mass ys := by
  induction xs with
  | nil => simp [mass]
  | cons x xs ih => obtain ⟨x,w⟩ := x; simp [mass, ih, Nat.add_assoc]

theorem mass_image {α β : Type} (f : α → β) (xs : Weighted α) :
    mass (image f xs) = mass xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => obtain ⟨x,w⟩ := x; simp [image, mass] at *; omega

theorem mass_scale {α : Type} (w : Nat) (xs : Weighted α) :
    mass (scale w xs) = w*mass xs := by
  induction xs with
  | nil => simp [scale, mass]
  | cons x xs ih => obtain ⟨x,v⟩ := x; simp [scale, mass, Nat.mul_add] at *; omega

theorem mass_bind {α β : Type} (xs : Weighted α) (f : α → Weighted β) (d : Nat)
    (h : ∀ x w, (x,w) ∈ xs → mass (f x) = d) :
    mass (bind xs f) = mass xs*d := by
  induction xs with
  | nil => simp [bind, mass]
  | cons x xs ih =>
    obtain ⟨x,w⟩ := x
    have hx := h x w (by simp)
    have ht := ih (by intro y v hv; exact h y v (by simp [hv]))
    simp only [bind, List.flatMap_cons, mass_append, mass_scale, hx, mass,
      Nat.add_mul]
    exact congrArg (fun n => w*d+n) ht

/-- The two formation coins remain explicit even where the current state or arm
ignores them. Zero-weight availability outcomes are retained, never normalized. -/
def seeds (k n : Nat) : Weighted Seed :=
  [ (⟨false,false,false⟩, n-k), (⟨false,false,true⟩, k),
    (⟨false,true,false⟩, n-k), (⟨false,true,true⟩, k),
    (⟨true,false,false⟩, n-k), (⟨true,false,true⟩, k),
    (⟨true,true,false⟩, n-k), (⟨true,true,true⟩, k) ]

theorem seed_mass (k n : Nat) (h : k ≤ n) : mass (seeds k n) = 4*n := by
  simp [seeds, mass]; omega

def kernel (p : Parameters) (a : Arm) (z : Bool) (k n : Nat) (s : State) : Weighted Result :=
  image (fun b => exposure p a z b s) (seeds k n)

theorem exposure_mass (p : Parameters) (a : Arm) (z : Bool) (k n : Nat) (s : State)
    (h : k ≤ n) : mass (kernel p a z k n s) = 4*n := by
  rw [kernel, mass_image, seed_mass k n h]

/-- Every path keeps its full exposure outcomes. The schedule is fixed here;
no selection on future receipts or successful writes is performed. -/
def paths (p : Parameters) (a : Arm) (k n : Nat) (s : State) : List Bool → Weighted (List Result)
  | [] => [([],1)]
  | z::zs => bind (kernel p a z k n s)
      (fun r => image (fun rs => r::rs) (paths p a k n r.state zs))

theorem paths_mass (p : Parameters) (a : Arm) (k n : Nat) (s : State) (zs : List Bool)
    (h : k ≤ n) : mass (paths p a k n s zs) = (4*n)^zs.length := by
  induction zs generalizing s with
  | nil => simp [paths, mass]
  | cons z zs ih =>
    simp only [paths]
    rw [mass_bind _ _ ((4*n)^zs.length)]
    · rw [exposure_mass p a z k n s h]
      simp [Nat.pow_succ, Nat.mul_comm]
    · intro r w _
      rw [mass_image, ih]

theorem positive_history_denominator (n horizon : Nat) (h : 0 < n) :
    0 < (4*n)^horizon := by
  have hn : 0 < 4*n := by omega
  exact Nat.pow_pos hn

/-- An inherited finite mixture keeps all its mass and every actual reserve.
Uncommissioned or non-working states may be present in the supplied mixture. -/
def inheritedPaths (p : Parameters) (a : Arm) (k n : Nat)
    (initial : Weighted State) (zs : List Bool) : Weighted (List Result) :=
  bind initial (fun s => paths p a k n s zs)

theorem inherited_mass (p : Parameters) (a : Arm) (k n : Nat)
    (initial : Weighted State) (zs : List Bool) (h : k ≤ n) :
    mass (inheritedPaths p a k n initial zs) = mass initial * (4*n)^zs.length := by
  exact mass_bind initial _ _ (by intro s _ _; exact paths_mass p a k n s zs h)

/-- An actual whole-call history, with no absorbing reinterpretation of any
status and no reset of its continuing state. -/
inductive Realized (p : Parameters) (a : Arm) : State → List Bool → List Result → Prop where
  | nil (s : State) : Realized p a s [] []
  | cons (s : State) (z : Bool) (b : Seed) {zs : List Bool} {rs : List Result} :
      Realized p a (exposure p a z b s).state zs rs →
      Realized p a s (z::zs) (exposure p a z b s :: rs)

theorem kernel_member (p : Parameters) (a : Arm) (z : Bool) (k n : Nat) (s : State)
    (r : Result) (w : Nat) (h : (r,w) ∈ kernel p a z k n s) :
    ∃ b, r = exposure p a z b s := by
  simp only [kernel, image, List.mem_map] at h
  obtain ⟨⟨b,v⟩,_,he⟩ := h
  cases he
  exact ⟨b,rfl⟩

theorem paths_realized (p : Parameters) (a : Arm) (k n : Nat) (s : State)
    (zs : List Bool) (rs : List Result) (w : Nat)
    (h : (rs,w) ∈ paths p a k n s zs) : Realized p a s zs rs := by
  induction zs generalizing s rs w with
  | nil =>
    simp only [paths, List.mem_cons, List.not_mem_nil, or_false, Prod.mk.injEq] at h
    obtain ⟨rfl,rfl⟩ := h
    exact .nil s
  | cons z zs ih =>
    simp only [paths, bind, List.mem_flatMap] at h
    obtain ⟨⟨r,v⟩,hr,h⟩ := h
    simp only [scale, List.mem_map, image] at h
    obtain ⟨⟨tail,u⟩,ht,he⟩ := h
    obtain ⟨⟨rest,j⟩,hrest,hpair⟩ := ht
    cases hpair
    cases he
    obtain ⟨b,rfl⟩ := kernel_member p a z k n s r v hr
    exact .cons s z b (ih _ _ _ hrest)

theorem realized_account (p : Parameters) (a : Arm) (s : State)
    (zs : List Bool) (rs : List Result) (h : Realized p a s zs rs)
    (hp : maintenance p ≤ p.packet) :
    (finalState s rs).fuel+charges rs = s.fuel+zs.length*p.packet := by
  induction h with
  | nil s => simp [finalState,charges]
  | cons s z b _ ih =>
    have he := exposure_account p a z b s hp
    simp only [final_cons, charges, List.map_cons, List.sum_cons,
      List.length_cons, Nat.add_mul, Nat.one_mul] at *
    omega

theorem every_weighted_history_account (p : Parameters) (a : Arm) (k n : Nat)
    (s : State) (zs : List Bool) (rs : List Result) (w : Nat)
    (h : (rs,w) ∈ paths p a k n s zs) (hp : maintenance p ≤ p.packet) :
    (finalState s rs).fuel+charges rs = s.fuel+zs.length*p.packet :=
  realized_account p a s zs rs (paths_realized p a k n s zs rs w h) hp

/-- Finite provision is debited even for no-work calls. The residual source is
not reset to its initial value at a successful continuation. -/
theorem closed_source_account (p : Parameters) (a : Arm) (k n : Nat)
    (s : State) (zs : List Bool) (rs : List Result) (w packets : Nat)
    (h : (rs,w) ∈ paths p a k n s zs) (hp : maintenance p ≤ p.packet)
    (hs : zs.length ≤ packets) :
    (finalState s rs).fuel+(packets-zs.length)*p.packet+charges rs =
      s.fuel+packets*p.packet := by
  have he := every_weighted_history_account p a k n s zs rs w h hp
  have hm : (packets-zs.length)*p.packet+zs.length*p.packet = packets*p.packet := by
    rw [← Nat.add_mul, Nat.sub_add_cancel hs]
  omega

/-- Local equality of the complete marked exposure yields equality of all finite
history distributions, not merely equality conditioned on successful writing. -/
def compose {S O : Type} (step : S → Bool → Weighted (O × S))
    (s : S) : List Bool → Weighted (List O × S)
  | [] => [(([],s),1)]
  | z::zs => bind (step s z) (fun (o,t) =>
      image (fun (os,u) => (o::os,u)) (compose step t zs))

theorem complete_kernel_composition {S O : Type}
    (f g : S → Bool → Weighted (O × S)) (h : ∀ s z, f s z = g s z)
    (s : S) (zs : List Bool) : compose f s zs = compose g s zs := by
  have he : f = g := by funext s z; exact h s z
  rw [he]

/-- Matching the tape evaluation suffices for full finite exposure-kernel
identity, including unused seeds and failed opportunities. -/
theorem tape_kernel_identity {α : Type} (f g : Seed → α) (k n : Nat)
    (h : ∀ b, f b = g b) : image f (seeds k n) = image g (seeds k n) := by
  have he : f = g := funext h
  rw [he]

end StochasticPrediction

#print axioms StochasticPrediction.mass_append
#print axioms StochasticPrediction.mass_image
#print axioms StochasticPrediction.mass_scale
#print axioms StochasticPrediction.mass_bind
#print axioms StochasticPrediction.seed_mass
#print axioms StochasticPrediction.exposure_mass
#print axioms StochasticPrediction.paths_mass
#print axioms StochasticPrediction.positive_history_denominator
#print axioms StochasticPrediction.inherited_mass
#print axioms StochasticPrediction.kernel_member
#print axioms StochasticPrediction.paths_realized
#print axioms StochasticPrediction.realized_account
#print axioms StochasticPrediction.every_weighted_history_account
#print axioms StochasticPrediction.closed_source_account
#print axioms StochasticPrediction.complete_kernel_composition
#print axioms StochasticPrediction.tape_kernel_identity
