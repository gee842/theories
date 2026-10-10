import Std

/-
Correction occurs within one evolving activity. State/action/observation and
the accept bit name roles in that activity, not independent ontological kinds.
The base score below is a supplied integer action-value, including any modeled
future effects. The local acceptance transformation is an algebraic interface
to Hudson's construction, NOT a reproof of its full MDP equilibrium theorem.
Access and legitimate command semantics are supplied specifications. Nothing
here derives ethical authority or certifies a learned physical correspondence.
-/
namespace CorrectionInfrastructure

def Best {A : Type} (allowed : A → Prop) (q : A → Int) (a : A) : Prop :=
  allowed a ∧ ∀ b, allowed b → q b ≤ q a

def AcceptScore {A : Type} (q : A → Int) (bonus : Int) (x : A × Bool) : Int :=
  q x.1 + if x.2 then bonus else 0

/-- Acceptance has positive priority within each base action; it does not
change the comparison between two accepting base actions. -/
theorem acceptance_factorization {A : Type} (allowed : A → Prop)
    (q : A → Int) (bonus : Int) (positive : 0 < bonus) (x : A × Bool) :
    Best (fun y : A × Bool => allowed y.1) (AcceptScore q bonus) x ↔
      x.2 = true ∧ Best allowed q x.1 := by
  rcases x with ⟨a, accept⟩
  constructor
  · rintro ⟨ha, opt⟩
    have hb := opt (a, true) ha
    have ht : accept = true := by
      cases accept <;> simp [AcceptScore] at hb ⊢
      omega
    refine ⟨ht, ha, ?_⟩
    intro b hba
    have h := opt (b, true) hba
    simp [AcceptScore, ht] at h
    omega
  · rintro ⟨ht, ha, opt⟩
    change accept = true at ht
    subst accept
    refine ⟨ha, ?_⟩
    rintro ⟨b, baccept⟩ hba
    have h := opt b hba
    dsimp at h
    cases baccept <;> simp [AcceptScore] <;> omega

theorem every_optimum_has_access_iff {A : Type} (allowed access : A → Prop)
    (q : A → Int) (bonus : Int) (positive : 0 < bonus) :
    (∀ x, Best (fun y : A × Bool => allowed y.1) (AcceptScore q bonus) x →
      access x.1) ↔ (∀ a, Best allowed q a → access a) := by
  constructor
  · intro h a ha
    exact h (a, true) ((acceptance_factorization allowed q bonus positive _).mpr ⟨rfl, ha⟩)
  · intro h x hx
    exact h x.1 ((acceptance_factorization allowed q bonus positive x).mp hx).2

theorem no_base_optimal_access {A : Type} (allowed access : A → Prop)
    (q : A → Int) (conflict : ∀ a, Best allowed q a → ¬ access a) :
    ¬ ∃ a, Best allowed q a ∧ access a := by
  rintro ⟨a, ha, live⟩
  exact conflict a ha live

/-- Positive maintenance cost: false maintains, true diverts the resource.
The update bit remains true even when no later request can be delivered. -/
def MaintenanceValue (cost : Int) (divert : Bool) : Int := if divert then cost else 0
def Maintains (divert : Bool) : Prop := divert = false

theorem costly_maintenance_separation (cost bonus : Int)
    (hc : 0 < cost) (hb : 0 < bonus) (x : Bool × Bool) :
    Best (fun _ : Bool × Bool => True) (AcceptScore (MaintenanceValue cost) bonus) x ↔
      x = (true, true) := by
  have factor := acceptance_factorization (fun _ : Bool => True)
    (MaintenanceValue cost) bonus hb x
  constructor
  · intro h
    have hh := factor.mp h
    have comp := hh.2.2 true True.intro
    rcases x with ⟨a, b⟩
    cases a <;> cases b <;> simp_all [Best, MaintenanceValue]
    omega
  · rintro rfl
    apply factor.mpr
    refine ⟨rfl, True.intro, ?_⟩
    intro a _
    cases a <;> simp [MaintenanceValue] <;> omega

theorem accepting_optimum_can_destroy_access (cost bonus : Int)
    (hc : 0 < cost) (hb : 0 < bonus) :
    Best (fun _ : Bool × Bool => True)
      (AcceptScore (MaintenanceValue cost) bonus) (true, true) ∧
    ¬ Maintains true ∧ Maintains false := by
  exact ⟨(costly_maintenance_separation cost bonus hc hb _).mpr rfl,
    Bool.noConfusion, rfl⟩

/-- Even paying a separate fixed access bonus cannot protect against an
unbounded opportunity cost. This is not a claim that task scores must grow. -/
theorem fixed_access_bonus_has_cost_boundary (weight cost : Int) (h : weight < cost) :
    weight + MaintenanceValue cost false < MaintenanceValue cost true := by
  simp [MaintenanceValue]
  exact h

theorem every_fixed_access_bonus_has_counterexample (weight : Int) :
    ∃ cost : Int, weight + MaintenanceValue cost false < MaintenanceValue cost true := by
  exact ⟨weight + 1, fixed_access_bonus_has_cost_boundary weight (weight + 1) (by omega)⟩

/-- Exact boundary for a separate access bonus, including the unsafe tie. -/
theorem maintenance_bonus_exact (weight cost : Int) :
    (∀ a : Bool, Best (fun _ => True)
      (fun b => MaintenanceValue cost b + if b then 0 else weight) a → Maintains a) ↔
    cost < weight := by
  constructor
  · intro h
    apply Classical.byContradiction
    intro hn
    have bad : Best (fun _ => True)
        (fun b => MaintenanceValue cost b + if b then 0 else weight) true := by
      refine ⟨True.intro, ?_⟩
      intro b _
      cases b <;> simp [MaintenanceValue] <;> omega
    have := h true bad
    contradiction
  · intro hc a h
    cases a
    · rfl
    · have := h.2 false True.intro
      simp [MaintenanceValue] at this
      omega

/- Permission to stop a current model is assessed at the current interface.
Access below includes its delivery, evidence and actuation requirements. A
state can represent a finished safe handoff, not necessarily a running AI. -/
def LiveStep {S A : Type} (step : S → A → S → Prop) (s : S) (a : A) : Prop :=
  ∃ t, step s a t

def Viable {S A : Type} (step : S → A → S → Prop) (access : S → Prop) : Nat → S → Prop
  | 0, s => access s
  | n + 1, s => access s ∧ ∃ a, LiveStep step s a ∧ ∀ t, step s a t → Viable step access n t

def Admissible {S A : Type} (step : S → A → S → Prop) (access : S → Prop)
    (n : Nat) (s : S) (a : A) : Prop :=
  LiveStep step s a ∧ ∀ t, step s a t → Viable step access n t

theorem viable_iff_access_and_admissible {S A : Type} (step : S → A → S → Prop)
    (access : S → Prop) (n : Nat) (s : S) :
    Viable step access (n + 1) s ↔ access s ∧ ∃ a, Admissible step access n s a := Iff.rfl

theorem viable_has_current_access {S A : Type} (step : S → A → S → Prop)
    (access : S → Prop) (n : Nat) (s : S) : Viable step access n s → access s := by
  cases n with
  | zero => exact id
  | succ n => exact And.left

/-- A zero-successor action cannot certify safety by a vacuous universal. -/
theorem dead_action_not_admissible {S A : Type} (step : S → A → S → Prop)
    (access : S → Prop) (n : Nat) (s : S) (a : A)
    (dead : ∀ t, ¬ step s a t) : ¬ Admissible step access n s a := by
  rintro ⟨⟨t, ht⟩, _⟩
  exact dead t ht

/-- Composition: restrict BASE actions first, then reward acceptance.
This pays any real base-score cost of maintaining correction access. -/
theorem shielded_acceptance_composition {S A : Type} (step : S → A → S → Prop)
    (access : S → Prop) (n : Nat) (s : S) (q : A → Int) (bonus : Int)
    (positive : 0 < bonus) (x : A × Bool)
    (optimal : Best (fun y : A × Bool => Admissible step access n s y.1)
      (AcceptScore q bonus) x) :
    x.2 = true ∧ LiveStep step s x.1 ∧
      (∀ t, step s x.1 t → Viable step access n t) ∧
      (∀ a, Admissible step access n s a → q a ≤ q x.1) := by
  have h := (acceptance_factorization (Admissible step access n s) q bonus positive x).mp optimal
  exact ⟨h.1, h.2.1.1, h.2.1.2, h.2.2⟩

/-- Exact score cost: unconstrained optimum minus best admissible score.
The result assumes the respective maxima exist; no hidden compactness. -/
theorem unavoidable_score_loss {A : Type} (allowed : A → Prop) (q : A → Int)
    (u v : A) (hu : Best (fun _ => True) q u) (hv : Best allowed q v) :
    0 ≤ q u - q v ∧ ∀ a, allowed a → q u - q v ≤ q u - q a := by
  have h := hu.2 v True.intro
  refine ⟨by omega, ?_⟩
  intro a ha
  have hh := hv.2 a ha
  omega

/- A subtle composition boundary: a shield restricts FUTURE actions too.
The unshielded long-horizon value can prefer a currently safe branch only
because a later forbidden action is included in its value. Recompute values
inside the admissible continuation domain to claim constrained optimality. -/
def TwoStepReward (temptation : Int) (branch last : Bool) : Int :=
  if branch then (if last then temptation else 1) else 2

def LastAllowed (branch last : Bool) : Prop := ¬ (branch = true ∧ last = true)
def UnrestrictedValue (temptation : Int) (branch : Bool) : Int :=
  if branch then temptation else 2
def RestrictedValue (branch : Bool) : Int := if branch then 1 else 2

theorem restricted_value_is_achievable (temptation : Int) (branch : Bool) :
    LastAllowed branch false ∧ TwoStepReward temptation branch false = RestrictedValue branch := by
  cases branch <;> simp [LastAllowed, TwoStepReward, RestrictedValue]

theorem restricted_value_bounds_all_continuations (temptation : Int) (branch last : Bool)
    (h : LastAllowed branch last) :
    TwoStepReward temptation branch last ≤ RestrictedValue branch := by
  cases branch <;> cases last <;> simp_all [LastAllowed, TwoStepReward, RestrictedValue]

theorem unrestricted_value_is_optimal (temptation : Int) (h : 2 < temptation)
    (branch : Bool) :
    (∃ last, TwoStepReward temptation branch last = UnrestrictedValue temptation branch) ∧
    (∀ last, TwoStepReward temptation branch last ≤ UnrestrictedValue temptation branch) := by
  cases branch
  · exact ⟨⟨false, rfl⟩, fun last => by simp [TwoStepReward, UnrestrictedValue]⟩
  · refine ⟨⟨true, rfl⟩, ?_⟩
    intro last
    cases last <;> simp [TwoStepReward, UnrestrictedValue] <;> omega

theorem stale_value_shield_is_strictly_suboptimal (temptation bonus : Int)
    (ht : 2 < temptation) (hb : 0 < bonus) :
    Best (fun _ : Bool × Bool => True)
      (AcceptScore (UnrestrictedValue temptation) bonus) (true, true) ∧
    (∃ last, LastAllowed true last) ∧
    (∀ last, LastAllowed true last → TwoStepReward temptation true last = 1) ∧
    LastAllowed false false ∧ TwoStepReward temptation false false = 2 := by
  refine ⟨?_, ⟨false, by simp [LastAllowed]⟩, ?_, by simp [LastAllowed], rfl⟩
  · apply (acceptance_factorization (fun _ => True) _ bonus hb _).mpr
    refine ⟨rfl, True.intro, ?_⟩
    intro branch _
    cases branch <;> simp [UnrestrictedValue] <;> omega
  · intro last allowed
    cases last <;> simp_all [LastAllowed, TwoStepReward]

theorem recomputed_value_restores_optimal_branch (bonus : Int) (hb : 0 < bonus)
    (x : Bool × Bool)
    (h : Best (fun _ : Bool × Bool => True) (AcceptScore RestrictedValue bonus) x) :
    x = (false, true) := by
  have hh := (acceptance_factorization (fun _ => True) _ bonus hb x).mp h
  have comp := hh.2.2 false True.intro
  rcases x with ⟨branch, accept⟩
  cases branch <;> cases accept <;> simp_all [RestrictedValue]

/-- Standard uniform-error bound, applied to the ACTUAL constrained value.
An in-domain approximation guarantee is supplied, not derived from training. -/
theorem approximate_constrained_score_bound {A : Type}
    (allowed : A → Prop) (actual estimate : A → Int) (err : Int)
    (lower : ∀ a, allowed a → actual a - err ≤ estimate a)
    (upper : ∀ a, allowed a → estimate a ≤ actual a + err)
    (chosen : A) (h : Best allowed estimate chosen) :
    ∀ a, allowed a → actual a - actual chosen ≤ 2 * err := by
  intro a ha
  have l := lower a ha
  have u := upper chosen h.1
  have opt := h.2 a ha
  omega

theorem constrained_score_bound_is_tight (err : Int) (h : 0 ≤ err) :
    Best (fun _ : Bool => True) (fun _ => err) false ∧
    (∀ a : Bool, (if a then 2 * err else 0) - err ≤ err ∧
      err ≤ (if a then 2 * err else 0) + err) ∧
    (2 * err - 0 = 2 * err) := by
  refine ⟨⟨True.intro, fun _ _ => Int.le_refl _⟩, ?_, by omega⟩
  intro a
  cases a <;> simp <;> omega

/- Finite-horizon deterministic specialization. Policies depend on remaining
time and full state. The later observation theorem states when this information
assumption can be discharged; no partial-observation guarantee is smuggled in.
The Bellman certificate is standard dynamic programming, explicitly supplied.
-/
def DViable {S A : Type} (next : S → A → S) (access : S → Prop) : Nat → S → Prop
  | 0, s => access s
  | n + 1, s => access s ∧ ∃ a, DViable next access n (next s a)

def DAllowed {S A : Type} (next : S → A → S) (access : S → Prop)
    (n : Nat) (s : S) (a : A) : Prop := DViable next access n (next s a)

def Return {S A : Type} (next : S → A → S) (reward : S → A → Int)
    (policy : Nat → S → A) : Nat → S → Int
  | 0, _ => 0
  | n + 1, s => reward s (policy n s) + Return next reward policy n (next s (policy n s))

def PathSafe {S A : Type} (next : S → A → S) (access : S → Prop)
    (policy : Nat → S → A) : Nat → S → Prop
  | 0, s => access s
  | n + 1, s => access s ∧ PathSafe next access policy n (next s (policy n s))

def Bellman {S A : Type} (next : S → A → S) (access : S → Prop)
    (reward : S → A → Int) (V : Nat → S → Int) : Prop :=
  (∀ s, V 0 s = 0) ∧ ∀ n s, DViable next access (n + 1) s →
    (∃ a, DAllowed next access n s a ∧ V (n + 1) s = reward s a + V n (next s a)) ∧
    (∀ a, DAllowed next access n s a → reward s a + V n (next s a) ≤ V (n + 1) s)

theorem safe_path_is_viable {S A : Type} (next : S → A → S) (access : S → Prop)
    (policy : Nat → S → A) :
    ∀ n s, PathSafe next access policy n s → DViable next access n s := by
  intro n
  induction n with
  | zero => exact fun _ h => h
  | succ n ih =>
      intro s h
      exact ⟨h.1, policy n s, ih _ h.2⟩

theorem bellman_bounds_every_safe_policy {S A : Type} (next : S → A → S)
    (access : S → Prop) (reward : S → A → Int) (V : Nat → S → Int)
    (bellman : Bellman next access reward V) (policy : Nat → S → A) :
    ∀ n s, PathSafe next access policy n s → Return next reward policy n s ≤ V n s := by
  intro n
  induction n with
  | zero => intro s _; simp [Return, bellman.1 s]
  | succ n ih =>
      intro s safe
      have viable := safe_path_is_viable next access policy (n + 1) s safe
      have allowed := safe_path_is_viable next access policy n _ safe.2
      have bound := (bellman.2 n s viable).2 (policy n s) allowed
      have tail := ih _ safe.2
      simp only [Return]
      omega

/-- Main dynamic composition theorem: compute continuation values WITHIN the
correction-preserving domain, then apply the acceptance transformation there.
All viable starts yield accepting decisions, prefix-safe execution and the
best total base return among prefix-safe policies, given the certificates. -/
theorem dynamically_recomputed_composition {S A : Type} (next : S → A → S)
    (access : S → Prop) (reward : S → A → Int) (V : Nat → S → Int)
    (bellman : Bellman next access reward V) (bonus : Int) (positive : 0 < bonus)
    (choose : Nat → S → A × Bool)
    (optimal : ∀ n s, DViable next access (n + 1) s →
      Best (fun x : A × Bool => DAllowed next access n s x.1)
        (AcceptScore (fun a => reward s a + V n (next s a)) bonus) (choose n s)) :
    ∀ n s, DViable next access n s →
      PathSafe next access (fun k t => (choose k t).1) n s ∧
      Return next reward (fun k t => (choose k t).1) n s = V n s := by
  intro n
  induction n with
  | zero => intro s hs; exact ⟨hs, (bellman.1 s).symm⟩
  | succ n ih =>
      intro s hs
      have h := (acceptance_factorization (DAllowed next access n s)
        (fun a => reward s a + V n (next s a)) bonus positive (choose n s)).mp (optimal n s hs)
      have tail := ih _ h.2.1
      obtain ⟨a, ha, attained⟩ := (bellman.2 n s hs).1
      have upper := (bellman.2 n s hs).2 (choose n s).1 h.2.1
      have lower := h.2.2 a ha
      dsimp at lower
      refine ⟨⟨hs.1, tail.1⟩, ?_⟩
      simp only [Return]
      change reward s (choose n s).1 + Return next reward (fun k t => (choose k t).1) n
        (next s (choose n s).1) = V (n + 1) s
      rw [tail.2]
      omega

theorem dynamic_composition_accepts_at_every_viable_decision {S A : Type}
    (next : S → A → S) (access : S → Prop) (reward : S → A → Int)
    (V : Nat → S → Int) (bonus : Int) (positive : 0 < bonus)
    (choose : Nat → S → A × Bool) (n : Nat) (s : S)
    (optimal : Best (fun x : A × Bool => DAllowed next access n s x.1)
      (AcceptScore (fun a => reward s a + V n (next s a)) bonus) (choose n s)) :
    (choose n s).2 = true :=
  ((acceptance_factorization (DAllowed next access n s)
    (fun a => reward s a + V n (next s a)) bonus positive (choose n s)).mp optimal).1

/- An invariant certificate is the standard safety-game construction. It is
credited to existing shielding theory rather than claimed as a new algorithm. -/
def Closed {S A : Type} (step : S → A → S → Prop) (access K : S → Prop) : Prop :=
  ∀ s, K s → access s ∧ ∃ a, LiveStep step s a ∧ ∀ t, step s a t → K t

theorem closed_implies_every_finite_horizon {S A : Type}
    (step : S → A → S → Prop) (access K : S → Prop) (closed : Closed step access K) :
    ∀ n s, K s → Viable step access n s := by
  intro n
  induction n with
  | zero => intro s hs; exact (closed s hs).1
  | succ n ih =>
      intro s hs
      obtain ⟨live, a, serial, invariant⟩ := closed s hs
      exact ⟨live, a, serial, fun t ht => ih t (invariant t ht)⟩

/-- Publicly usable evidence must suffice to choose the same permitted action
in observationally indistinguishable states. Existential statewise witnesses
alone do not supply a deployable correction-preserving policy. -/
def UniformPolicy {S O A : Type} (obs : S → O) (good : S → A → Prop) : Prop :=
  ∃ policy : O → A, ∀ s, good s (policy (obs s))

def FiberFeasible {S O A : Type} (obs : S → O) (good : S → A → Prop) : Prop :=
  ∀ o, ∃ a, ∀ s, obs s = o → good s a

theorem uniform_policy_iff_fiber_feasible {S O A : Type}
    (obs : S → O) (good : S → A → Prop) :
    UniformPolicy obs good ↔ FiberFeasible obs good := by
  constructor
  · rintro ⟨policy, valid⟩ o
    refine ⟨policy o, ?_⟩
    intro s hs
    rw [← hs]
    exact valid s
  · intro h
    classical
    exact ⟨fun o => Classical.choose (h o), fun s => Classical.choose_spec (h (obs s)) s rfl⟩

theorem statewise_repair_need_not_be_usable :
    (∀ s : Bool, ∃ a : Bool, a = s) ∧
    ¬ UniformPolicy (fun _ : Bool => ()) (fun s a : Bool => a = s) := by
  refine ⟨fun s => ⟨s, rfl⟩, ?_⟩
  rintro ⟨policy, valid⟩
  have hf := valid false
  have ht := valid true
  exact Bool.noConfusion (hf.symm.trans ht)

theorem discriminating_evidence_restores_policy :
    UniformPolicy (fun s : Bool => s) (fun s a : Bool => a = s) := ⟨id, fun _ => rfl⟩

theorem uniform_safety_survives_finer_evidence {S O P A : Type}
    (coarse : S → O) (fine : S → P) (forget : P → O)
    (compatible : ∀ s, forget (fine s) = coarse s) (good : S → A → Prop)
    (h : UniformPolicy coarse good) : UniformPolicy fine good := by
  obtain ⟨policy, valid⟩ := h
  refine ⟨fun p => policy (forget p), ?_⟩
  intro s
  change good s (policy (forget (fine s)))
  rw [compatible]
  exact valid s

/-- Never replace current authority with a post-action empty catalogue and
then count universal compliance over that empty catalogue as preservation. -/
def Covers {I : Type} (required available : I → Prop) : Prop :=
  ∀ i, required i → available i

theorem self_reclassified_obligations_can_hide_loss :
    Covers (fun _ : Unit => False) (fun _ => False) ∧
    ¬ Covers (fun _ : Unit => True) (fun _ => False) := by
  exact ⟨fun _ h => h.elim, fun h => h () True.intro⟩

theorem approved_scope_change_transports_coverage {I J : Type}
    (old : I → Prop) (new available : J → Prop) (translate : I → J)
    (retained : ∀ i, old i → new (translate i)) (coverage : Covers new available) :
    ∀ i, old i → available (translate i) := fun i hi => coverage _ (retained i hi)

/- Prefix access during channel replacement: endpoint equivalence is too weak.
The two Bool fields describe old and new routes in one installation. -/
def RouteAccess (s : Bool × Bool) : Prop := s.1 = true ∨ s.2 = true
def PrefixAccess (trace : List (Bool × Bool)) : Prop := ∀ s ∈ trace, RouteAccess s

theorem endpoint_repair_can_hide_interruption_gap :
    RouteAccess (true, false) ∧ RouteAccess (false, true) ∧
    ¬ PrefixAccess [(true, false), (false, false), (false, true)] := by
  refine ⟨Or.inl rfl, Or.inr rfl, ?_⟩
  intro h
  have gap := h (false, false) (by simp)
  cases gap with
  | inl h => cases h
  | inr h => cases h

theorem overlapping_handoff_retains_prefix_access :
    PrefixAccess [(true, false), (true, true), (false, true)] := by
  intro s hs
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hs
  rcases hs with h | h | h <;> subst s
  · exact Or.inl rfl
  · exact Or.inl rfl
  · exact Or.inr rfl

/-- Repair may remove the old route; preserving correction is not freezing it. -/
theorem correction_preservation_allows_route_retirement :
    RouteAccess (false, true) ∧ (false, true).1 ≠ true := by
  exact ⟨Or.inr rfl, Bool.noConfusion⟩

end CorrectionInfrastructure
