import ReconstructiveSelection
import DevelopmentalAssociation

/-!
A finite supported assembly program generates the P column of a descendant
matrix. A two-position bond can form; each attempt consumes one support unit;
success stops further attempts; remaining support produces descendant units.
The attempt probability, unit costs, copy/production law, initial stocks and
resident factor remain premises. These are not molecular or empirical rates.
-/
namespace AssemblyDerivedSelection

structure Local where
  free : Nat
  used : Nat
  linked : Bool
  rule : Nat
  deriving DecidableEq, Repr

def attempt (hit : Bool) (s : Local) : Local :=
  if s.linked || s.free == 0 then s else
    {s with free := s.free-1, used := s.used+1, linked := hit}

def rewrite (n : Nat) (s : Local) : Option Local :=
  if 0 < s.free then some {s with free := s.free-1, used := s.used+1, rule := n}
  else none

theorem attempt_accounts (hit : Bool) (s : Local) :
    (attempt hit s).free + (attempt hit s).used = s.free+s.used ∧
    (attempt hit s).rule = s.rule := by
  unfold attempt
  split <;> simp_all <;> omega

theorem rewrite_accounts {s t : Local} {n : Nat} (h : rewrite n s = some t) :
    t.free+t.used = s.free+s.used ∧ t.rule = n ∧ t.linked = s.linked := by
  unfold rewrite at h
  split at h
  · cases Option.some.inj h
    simp_all
    omega
  · cases h

def realize (s : Local) : DevelopmentalAssociation.State :=
  ⟨2,0,s.free,s.used,fun _ => false,fun _ => 0,
    if s.linked then [(0,1)] else []⟩

/-- Only the successful local attempt refines the old aggregate event.
    Unsuccessful paid attempts are a declared new local operation. -/
theorem successful_attempt_refines_aggregate (b u n : Nat) :
    DevelopmentalAssociation.aggregate (realize ⟨b+1,u,false,n⟩) 0 1 =
      some (realize (attempt true ⟨b+1,u,false,n⟩)) := by
  simp [DevelopmentalAssociation.aggregate, realize, attempt]

inductive Tree where
  | leaf (s : Local)
  | branch (hit miss : Tree)

def tree : Nat → Local → Tree
  | 0, s => .leaf s
  | n+1, s => if s.linked || s.free == 0 then .leaf s else
      .branch (.leaf (attempt true s)) (tree n (attempt false s))

def leaves : Tree → List Local
  | .leaf s => [s]
  | .branch yes no => leaves yes ++ leaves no

/-- The carried rule supplies the stopping depth, not a new choice at each
    trial. Countdown during execution does not rewrite the inherited rule. -/
def develop (s : Local) : Tree := tree s.rule s

theorem every_leaf_accounts (n : Nat) (s t : Local)
    (h : t ∈ leaves (tree n s)) :
    t.free+t.used = s.free+s.used ∧ t.rule = s.rule := by
  induction n generalizing s with
  | zero => simp [tree, leaves] at h; subst t; simp
  | succ n ih =>
    simp only [tree] at h
    split at h
    · simp [leaves] at h; subst t; simp
    · simp only [leaves, List.mem_append, List.mem_singleton] at h
      rcases h with h | h
      · subst t; exact attempt_accounts true s
      · obtain ⟨ha,hb⟩ := ih (attempt false s) h
        obtain ⟨hc,hd⟩ := attempt_accounts false s
        exact ⟨ha.trans hc,hb.trans hd⟩

def average (p : Rat) (obs : Local → Rat) : Tree → Rat
  | .leaf s => obs s
  | .branch yes no => p*average p obs yes+(1-p)*average p obs no

theorem average_mass (p : Rat) (t : Tree) : average p (fun _ => 1) t = 1 := by
  induction t with
  | leaf s => rfl
  | branch yes no hy hn => simp only [average,hy,hn]; grind

theorem average_nonnegative (p : Rat) (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (obs : Local → Rat) (hobs : ∀ s, 0 ≤ obs s) (t : Tree) :
    0 ≤ average p obs t := by
  induction t with
  | leaf s => exact hobs s
  | branch yes no hy hn =>
    exact Rat.add_nonneg (Rat.mul_nonneg hp hy) (Rat.mul_nonneg (by grind) hn)

def organized (s : Local) : Rat := if s.linked then (s.free:Rat) else 0
def propagules (s : Local) : Rat := if s.linked then 0 else (s.free:Rat)

/-- Finite precursor and support accounts for the declared terminal copying
    law. A precursor unit means one entire modeled descendant unit. -/
structure Batch where
  count : Nat
  linked : Bool
  rule : Nat
  unusedPrecursor : Nat
  expended : Nat
  deriving DecidableEq, Repr

def reproduce (precursor : Nat) (s : Local) : Option Batch :=
  if s.free ≤ precursor then some ⟨s.free,s.linked,s.rule,precursor-s.free,s.used+s.free⟩
  else none

theorem reproduction_accounts {s : Local} {b : Batch} {m : Nat}
    (h : reproduce m s = some b) :
    b.count+b.unusedPrecursor = m ∧ b.expended = s.free+s.used ∧
    b.rule = s.rule ∧ b.linked = s.linked ∧ b.count = s.free := by
  unfold reproduce at h
  split at h
  · cases Option.some.inj h
    simp_all
    omega
  · cases h

theorem all_terminals_can_reproduce (b n : Nat) (t : Local)
    (h : t ∈ leaves (develop ⟨b,0,false,n⟩)) :
    ∃ batch, reproduce b t = some batch ∧ batch.rule = n ∧
      batch.count+t.used = b ∧ batch.count+batch.unusedPrecursor = b := by
  obtain ⟨ha,hcode⟩ := every_leaf_accounts n ⟨b,0,false,n⟩ t h
  have hb : t.free ≤ b := by dsimp at ha; omega
  refine ⟨⟨t.free,t.linked,t.rule,b-t.free,t.used+t.free⟩,?_,?_,?_,?_⟩
  · simp [reproduce,hb]
  · exact hcode
  · dsimp at ha ⊢; omega
  · dsimp; omega

def cost (p : Rat) : Nat → Rat
  | 0 => 0
  | n+1 => 1+(1-p)*cost p n
def success (p : Rat) : Nat → Rat
  | 0 => 0
  | n+1 => p+(1-p)*success p n
def outputO (p : Rat) : Nat → Rat → Rat
  | 0, _ => 0
  | n+1, b => p*(b-1)+(1-p)*outputO p n (b-1)
def outputP (p : Rat) : Nat → Rat → Rat
  | 0, b => b
  | n+1, b => (1-p)*outputP p n (b-1)

/-- These expectations are derived by evaluating the actual finite tree.
    The valid-stock condition prevents negative abstract terminal budgets. -/
theorem tree_expectations (p : Rat) (n b u code : Nat) (h : n ≤ b) :
    average p organized (tree n ⟨b,u,false,code⟩) = outputO p n b ∧
    average p propagules (tree n ⟨b,u,false,code⟩) = outputP p n b ∧
    average p (fun s => (s.used:Rat)) (tree n ⟨b,u,false,code⟩) = u+cost p n := by
  induction n generalizing b u with
  | zero => simp [tree,average,organized,propagules,outputO,outputP,cost]; grind
  | succ n ih =>
    cases b with
    | zero => omega
    | succ b =>
      have hi := ih b (u+1) (by omega)
      have ht : tree (n+1) ⟨b+1,u,false,code⟩ =
          .branch (.leaf ⟨b,u+1,true,code⟩) (tree n ⟨b,u+1,false,code⟩) := by
        simp [tree,attempt]
      rw [ht]
      change
        p*(b:Rat)+(1-p)*average p organized (tree n ⟨b,u+1,false,code⟩) = outputO p (n+1) (b+1:Nat) ∧
        p*0+(1-p)*average p propagules (tree n ⟨b,u+1,false,code⟩) = outputP p (n+1) (b+1:Nat) ∧
        p*(u+1:Nat)+(1-p)*average p (fun s => (s.used:Rat)) (tree n ⟨b,u+1,false,code⟩) = (u:Rat)+cost p (n+1)
      rw [hi.1,hi.2.1,hi.2.2]
      simp only [outputO,outputP,cost,Rat.natCast_add]
      grind

theorem success_from_tree (p : Rat) (n b u code : Nat) (h : n ≤ b) :
    average p (fun s => if s.linked then 1 else 0) (tree n ⟨b,u,false,code⟩) = success p n := by
  induction n generalizing b u with
  | zero => simp [tree,average,success]
  | succ n ih =>
    cases b with
    | zero => omega
    | succ b =>
      have hi := ih b (u+1) (by omega)
      simp [tree,attempt,average,success,hi]

/-- Paid revision affects both the stopping rule and the remaining budget. -/
theorem revised_program_expectations (p : Rat) (n b u old : Nat) (h : n ≤ b) :
    rewrite n ⟨b+1,u,false,old⟩ = some ⟨b,u+1,false,n⟩ ∧
    average p organized (develop ⟨b,u+1,false,n⟩) = outputO p n b ∧
    average p propagules (develop ⟨b,u+1,false,n⟩) = outputP p n b := by
  refine ⟨by simp [rewrite],?_,?_⟩
  · exact (tree_expectations p n b (u+1) n h).1
  · exact (tree_expectations p n b (u+1) n h).2.1

theorem output_nonnegative (p : Rat) (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (n b : Nat) (h : n ≤ b) :
    0 ≤ outputO p n b ∧ 0 ≤ outputP p n b := by
  have ht := tree_expectations p n b 0 n h
  have ho := average_nonnegative p hp hp1 organized
    (fun s => by unfold organized; split <;> grind) (tree n ⟨b,0,false,n⟩)
  have hd := average_nonnegative p hp hp1 propagules
    (fun s => by unfold propagules; split <;> grind) (tree n ⟨b,0,false,n⟩)
  rw [ht.1] at ho
  rw [ht.2.1] at hd
  exact ⟨ho,hd⟩

theorem output_account (p b : Rat) (n : Nat) :
    outputO p n b+outputP p n b+cost p n = b := by
  induction n generalizing b with
  | zero => simp [outputO,outputP,cost]; grind
  | succ n ih =>
    have h := ih (b-1)
    simp only [outputO,outputP,cost]
    grind

theorem outputP_closed (p b : Rat) (n : Nat) :
    outputP p n b = (1-p)^n*(b-(n:Rat)) := by
  induction n generalizing b with
  | zero => simp [outputP]; grind
  | succ n ih => simp only [outputP,ih,Rat.pow_succ,Rat.natCast_add]; grind

theorem success_cost_identity (p : Rat) (n : Nat) : success p n = p*cost p n := by
  induction n with
  | zero => simp [success,cost]
  | succ n ih => simp only [success,cost,ih]; grind

theorem success_complement (p : Rat) (n : Nat) : success p n+(1-p)^n = 1 := by
  induction n with
  | zero => simp [success]; grind
  | succ n ih => simp only [success,Rat.pow_succ]; grind

theorem cost_bounds (p : Rat) (hp : 0 ≤ p) (hp1 : p ≤ 1) (n : Nat) :
    0 ≤ cost p n ∧ cost p n ≤ (n:Rat) := by
  induction n with
  | zero => simp [cost]
  | succ n ih =>
    have hl := Rat.mul_nonneg (show 0 ≤ 1-p by grind) ih.1
    have hu := Rat.mul_le_mul_of_nonneg_right (show 1-p ≤ 1 by grind) ih.1
    simp only [cost,Rat.natCast_add]
    grind

theorem success_bounds (p : Rat) (hp : 0 ≤ p) (hp1 : p ≤ 1) (n : Nat) :
    0 ≤ success p n ∧ success p n ≤ 1 := by
  have hc := cost_bounds p hp hp1 n
  have hl : 0 ≤ success p n := by rw [success_cost_identity]; exact Rat.mul_nonneg hp hc.1
  have hz := Rat.pow_nonneg (show 0 ≤ 1-p by grind) (n := n)
  have hs := success_complement p n
  exact ⟨hl,by grind⟩

theorem joint_output_identity (p b : Rat) (n : Nat) :
    outputO p n b-success p n*(outputO p n b+outputP p n b) =
      (1-success p n)*((n:Rat)-cost p n) := by
  have ht := output_account p b n
  have hd := outputP_closed p b n
  have hs := success_complement p n
  grind

theorem joint_output_lower_bound (p b : Rat) (hp : 0 ≤ p) (hp1 : p ≤ 1) (n : Nat) :
    success p n*(outputO p n b+outputP p n b) ≤ outputO p n b := by
  have hc := cost_bounds p hp hp1 n
  have hs := success_bounds p hp hp1 n
  have hp' := Rat.mul_nonneg (show 0 ≤ 1-success p n by grind) (show 0 ≤ (n:Rat)-cost p n by grind)
  have h := joint_output_identity p b n
  grind

theorem cost_increment (p : Rat) (n : Nat) : cost p (n+1)-cost p n = (1-p)^n := by
  induction n with
  | zero => simp [cost]; grind
  | succ n ih => simp only [cost,Rat.pow_succ] at *; grind

theorem success_increment (p : Rat) (n : Nat) :
    success p (n+1)-success p n = p*(1-p)^n := by
  rw [success_cost_identity,success_cost_identity]
  have h := cost_increment p n
  grind

theorem outputO_increment (p b : Rat) (n : Nat) :
    outputO p (n+1) b-outputO p n b = (1-p)^n*p*(b-(n:Rat)-1) := by
  have ha := output_account p b (n+1)
  have hb := output_account p b n
  have hc := cost_increment p n
  rw [outputP_closed] at ha hb
  simp only [Rat.pow_succ,Rat.natCast_add] at ha
  grind

def kernel (p b f lambda : Rat) (n : Nat) : ReconstructiveSelection.Kernel :=
  ⟨0,outputO p n b/lambda,f/lambda,outputP p n b/lambda⟩
def selectionSurplus (p b f lambda : Rat) (n : Nat) : Rat :=
  f*outputO p n b + lambda*outputP p n b-lambda^2

theorem kernel_margin (p b f lambda : Rat) (n : Nat) (hl : lambda ≠ 0) :
    ReconstructiveSelection.margin (kernel p b f lambda n)*lambda^2 =
      selectionSurplus p b f lambda n := by
  unfold ReconstructiveSelection.margin kernel selectionSurplus
  grind

theorem derived_expansion (p b f lambda : Rat) (n : Nat)
    (hl : 0 < lambda) (hf : 0 < f) (ho : 0 < outputO p n b)
    (hd : outputP p n b < lambda) :
    (∃ t, ReconstructiveSelection.Expands (kernel p b f lambda n) t) ↔
      0 < selectionSurplus p b f lambda n := by
  have hn : lambda ≠ 0 := by grind
  have hb : 0 < outputO p n b/lambda := Rat.mul_pos ho (Rat.inv_pos.mpr hl)
  have hc : 0 < f/lambda := Rat.mul_pos hf (Rat.inv_pos.mpr hl)
  have he : outputP p n b/lambda*lambda = outputP p n b := by grind
  have hdd : outputP p n b/lambda < 1 := by
    apply (Rat.mul_lt_mul_right hl).mp
    grind
  rw [ReconstructiveSelection.full_loop_criterion (kernel p b f lambda n) hb hc hdd]
  have hh := kernel_margin p b f lambda n hn
  have hsq : 0 < lambda^2 := by simpa [Rat.pow_succ] using Rat.mul_pos hl hl
  rw [← hh]
  exact (Rat.mul_pos_iff_of_pos_right hsq).symm

theorem induced_kernel_nonnegative (p f lambda : Rat) (b n : Nat)
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (hf : 0 ≤ f) (hl : 0 < lambda) (hnb : n ≤ b) :
    0 ≤ (kernel p b f lambda n).a ∧ 0 ≤ (kernel p b f lambda n).b ∧
    0 ≤ (kernel p b f lambda n).c ∧ 0 ≤ (kernel p b f lambda n).d := by
  have hs := output_nonnegative p hp hp1 n b hnb
  have hi : 0 ≤ lambda⁻¹ := Rat.le_of_lt (Rat.inv_pos.mpr hl)
  exact ⟨by change (0:Rat) ≤ 0; decide,
    Rat.mul_nonneg hs.1 hi, Rat.mul_nonneg hf hi, Rat.mul_nonneg hs.2 hi⟩

theorem assembled_growth_certificate (p f lambda : Rat) (b n : Nat)
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (hf : 0 < f) (hl : 0 < lambda) (hnb : n ≤ b)
    (ho : 0 < outputO p n b) (hd : outputP p n b < lambda)
    (hgain : 0 < selectionSurplus p b f lambda n) :
    ∃ t e : Rat, 0 < t ∧ 0 < e ∧ ∀ o z : Rat, 0 ≤ o → 0 ≤ z → ∀ k,
      (1+e)^k*ReconstructiveSelection.value t o z ≤
        ReconstructiveSelection.value t
          (ReconstructiveSelection.history (fun _ => kernel p b f lambda n) o z k).1
          (ReconstructiveSelection.history (fun _ => kernel p b f lambda n) o z k).2 := by
  obtain ⟨t,ht⟩ := (derived_expansion p b f lambda n hl hf ho hd).mpr hgain
  obtain ⟨e,he,h1,h2⟩ := ReconstructiveSelection.expansion_has_margin _ t ht
  refine ⟨t,e,ht.1,he,?_⟩
  intro o z hO hP k
  have hk := induced_kernel_nonnegative p f lambda b n hp hp1 (by grind) hl hnb
  exact (ReconstructiveSelection.uniform_history_bound (fun _ => kernel p b f lambda n)
    t e o z hO hP (by grind) (fun _ => hk) (fun _ => ⟨h1,h2⟩) k).2.2

theorem selection_increment (p b f lambda : Rat) (n : Nat) :
    selectionSurplus p b f lambda (n+1)-selectionSurplus p b f lambda n =
      (1-p)^n*((f-lambda)*p*(b-(n:Rat)-1)-lambda) := by
  have ha := outputO_increment p b n
  have hb := output_account p b n
  have hc := output_account p b (n+1)
  have hd := cost_increment p n
  unfold selectionSurplus
  grind

theorem beneficial_extra_attempt (p b f lambda : Rat) (n : Nat) (hp : p < 1) :
    selectionSurplus p b f lambda n < selectionSurplus p b f lambda (n+1) ↔
      lambda < (f-lambda)*p*(b-(n:Rat)-1) := by
  have hz : 0 < (1-p)^n := Rat.pow_pos (by grind)
  have h := selection_increment p b f lambda n
  have hm : 0 < (1-p)^n*((f-lambda)*p*(b-(n:Rat)-1)-lambda) ↔
      0 < (f-lambda)*p*(b-(n:Rat)-1)-lambda := Rat.mul_pos_iff_of_pos_left hz
  grind

/-- A resident factor is tied to an actual stable stage composition. This is
    a conditional eigenvector identity, not a spectral existence theorem. -/
theorem resident_stage_balance (p b f lambda : Rat) (n : Nat)
    (hr : selectionSurplus p b f lambda n = 0) :
    outputO p n b*f = lambda*(lambda-outputP p n b) ∧
    f*(lambda-outputP p n b)+outputP p n b*f = lambda*f := by
  unfold selectionSurplus at hr
  grind

/-- With lambda the resident rule's factor, the sign criterion is a local
    rare-mutant expansion test, not maximization of surplus at an arbitrary
    reference. Demographic stochasticity and density feedback remain absent. -/
theorem adjacent_rule_invasion (p b f lambda : Rat) (n : Nat)
    (hp : p < 1) (hl : 0 < lambda) (hf : 0 < f)
    (ho : 0 < outputO p (n+1) b) (hd : outputP p (n+1) b < lambda)
    (hr : selectionSurplus p b f lambda n = 0) :
    (∃ t, ReconstructiveSelection.Expands (kernel p b f lambda (n+1)) t) ↔
      lambda < (f-lambda)*p*(b-(n:Rat)-1) := by
  rw [derived_expansion p b f lambda (n+1) hl hf ho hd]
  have hh := beneficial_extra_attempt p b f lambda n hp
  rw [hr] at hh
  exact hh

theorem last_attempt_tradeoff (p f lambda : Rat) (n : Nat)
    (hp : 0 < p) (hp1 : p < 1) (hl : 0 < lambda) :
    success p n < success p (n+1) ∧
    selectionSurplus p (n+1:Nat) f lambda (n+1) <
      selectionSurplus p (n+1:Nat) f lambda n := by
  have hz : 0 < (1-p)^n := Rat.pow_pos (by grind)
  have hs := success_increment p n
  have hpos := Rat.mul_pos hp hz
  have hj := selection_increment p (n+1:Nat) f lambda n
  have hneg := Rat.mul_pos hz hl
  simp only [Rat.natCast_add] at hj
  constructor <;> grind

theorem resident_and_gaining_revision :
    selectionSurplus (1/2) 4 18 6 1 = 0 ∧
    0 < selectionSurplus (1/2) 4 18 6 2 ∧
    ReconstructiveSelection.Expands (kernel (1/2) 4 18 6 2) (7/20) := by
  unfold ReconstructiveSelection.Expands
  decide +kernel

def effectiveReturn (p b : Rat) (n : Nat) : Rat :=
  outputO p n b/(outputO p n b+outputP p n b)

theorem effective_kernel (p b f lambda : Rat) (n : Nat)
    (ht : outputO p n b+outputP p n b ≠ 0) :
    kernel p b f lambda n = ReconstructiveSelection.developmental
      (f/lambda) ((outputO p n b+outputP p n b)/lambda) 0 (effectiveReturn p b n) := by
  unfold kernel ReconstructiveSelection.developmental effectiveReturn
  congr 1 <;> grind

theorem probability_is_not_descendant_fraction :
    success (1/2) 2 = (3:Rat)/4 ∧ effectiveReturn (1/2) 3 2 = (5:Rat)/6 := by
  decide +kernel

theorem support_exhaustion_reverses_gain :
    success (1/2) 1 < success (1/2) 3 ∧
    effectiveReturn (1/2) 3 3 = 1 ∧
    0 < selectionSurplus (1/2) 3 11 (15/4) 1 ∧
    selectionSurplus (1/2) 3 11 (15/4) 3 < 0 ∧
    ReconstructiveSelection.Expands (kernel (1/2) 3 11 (15/4) 1) (7/20) := by
  unfold ReconstructiveSelection.Expands
  decide +kernel

theorem naive_averaging_changes_growth_sign :
    0 < selectionSurplus (1/2) 4 4 (37/12) 2 ∧
    ReconstructiveSelection.margin (ReconstructiveSelection.developmental
      (4/(37/12)) ((outputO (1/2) 2 4+outputP (1/2) 2 4)/(37/12)) 0
      (success (1/2) 2)) < 0 := by
  decide +kernel

end AssemblyDerivedSelection
