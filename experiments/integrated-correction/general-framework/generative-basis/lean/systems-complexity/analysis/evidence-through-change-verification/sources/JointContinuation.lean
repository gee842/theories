import ContinuationAdequacy

/-! Local plans share one actual process. Projection fidelity and actual joint
executability are distinct supplied conditions. No normative ordering is added. -/
namespace JointContinuation
open ContinuationAdequacy
variable {X A B U V O P : Type}

def zipPlan : {n : Nat} → Plan U O n → Plan V P n → Plan (U × V) (O × P) n
  | _, .stop, .stop => .stop
  | _, .act u f, .act v g => .act (u,v) (fun o => zipPlan (f o.1) (g o.2))

/-- Records the operational obligation, without assuming the local good conditions. -/
def compatible (step : X → (U × V) → X → Prop) (obs : X → O × P)
    (allow : X → (U × V) → Prop) :
    {n : Nat} → Plan U O n → Plan V P n → (X → Prop) → Prop
  | _, .stop, .stop, _ => True
  | _, .act u f, .act v g, C => usable step allow C (u,v) ∧
      ∀ o, compatible step obs allow (f o.1) (g o.2) (post step obs C (u,v) o)

theorem joint_plan_composition
    (joint : X → (U × V) → X → Prop) (left : A → U → A → Prop)
    (right : B → V → B → Prop) (pa : X → A) (pb : X → B)
    (oa : A → O) (ob : B → P) (ga : A → Prop) (gb : B → Prop)
    (la : A → U → Prop) (lb : B → V → Prop) (lj : X → (U × V) → Prop)
    (project : ∀ x uv y, joint x uv y → left (pa x) uv.1 (pa y) ∧ right (pb x) uv.2 (pb y))
    (n : Nat) : ∀ (p : Plan U O n) (q : Plan V P n) C Ca Cb,
    (∀ x, C x → Ca (pa x) ∧ Cb (pb x)) →
    works left oa ga la p Ca → works right ob gb lb q Cb →
    compatible joint (fun x => (oa (pa x),ob (pb x))) lj p q C →
    works joint (fun x => (oa (pa x),ob (pb x)))
      (fun x => ga (pa x) ∧ gb (pb x)) lj (zipPlan p q) C := by
  induction n with
  | zero =>
    intro p q C Ca Cb cover hp hq _
    cases p; cases q
    intro x hx
    exact ⟨hp _ (cover x hx).1,hq _ (cover x hx).2⟩
  | succ n ih =>
    intro p q C Ca Cb cover hp hq hc
    cases p with
    | act u f =>
      cases q with
      | act v g =>
        refine ⟨(fun x hx => ⟨hp.1 _ (cover x hx).1,hq.1 _ (cover x hx).2⟩),hc.1,?_⟩
        intro o
        apply ih (f o.1) (g o.2) _ (post left oa Ca u o.1) (post right ob Cb v o.2)
        · rintro y ⟨x,hx,hs,ho⟩
          have pp := project x (u,v) y hs
          exact ⟨⟨x |> pa,(cover x hx).1,pp.1,congrArg Prod.fst ho⟩,
            ⟨x |> pb,(cover x hx).2,pp.2,congrArg Prod.snd ho⟩⟩
        · exact hp.2.2 o.1
        · exact hq.2.2 o.2
        · exact hc.2 o

/-- A successful joint plan must satisfy every joint operational obligation. -/
theorem compatibility_necessary
    (joint : X → (U × V) → X → Prop) (obs : X → O × P)
    (good : X → Prop) (allow : X → (U × V) → Prop) (n : Nat) :
    ∀ (p : Plan U O n) (q : Plan V P n) C,
    works joint obs good allow (zipPlan p q) C → compatible joint obs allow p q C := by
  induction n with
  | zero => intro p q C _; cases p; cases q; trivial
  | succ n ih =>
    intro p q C h
    cases p with
    | act u f =>
      cases q with
      | act v g => exact ⟨h.2.1,fun o => ih (f o.1) (g o.2) _ (h.2.2 o)⟩

theorem incompatible_blocks_joint
    (joint : X → (U × V) → X → Prop) (obs : X → O × P)
    (good : X → Prop) (allow : X → (U × V) → Prop) (n : Nat)
    (p : Plan U O n) (q : Plan V P n) (C : X → Prop)
    (h : ¬ compatible joint obs allow p q C) :
    ¬ works joint obs good allow (zipPlan p q) C :=
  fun hw => h (compatibility_necessary joint obs good allow n p q C hw)

/-- Projection has no assumption that the global state is the product of its views. -/
theorem actual_joint_post_projects
    (joint : X → (U × V) → X → Prop) (left : A → U → A → Prop)
    (right : B → V → B → Prop) (pa : X → A) (pb : X → B)
    (oa : A → O) (ob : B → P) (C : X → Prop) (Ca : A → Prop) (Cb : B → Prop)
    (cover : ∀ x, C x → Ca (pa x) ∧ Cb (pb x))
    (project : ∀ x uv y, joint x uv y → left (pa x) uv.1 (pa y) ∧ right (pb x) uv.2 (pb y))
    (uv : U × V) (o : O × P) :
    ∀ y, post joint (fun x => (oa (pa x),ob (pb x))) C uv o y →
      post left oa Ca uv.1 o.1 (pa y) ∧ post right ob Cb uv.2 o.2 (pb y) := by
  rintro y ⟨x,hx,hs,ho⟩
  exact ⟨⟨pa x,(cover x hx).1,(project x uv y hs).1,congrArg Prod.fst ho⟩,
    ⟨pb x,(cover x hx).2,(project x uv y hs).2,congrArg Prod.snd ho⟩⟩

-- Consumable shared support: a local event costs one, a paired event costs two.
-- Serializing the same consumptions without replenishment does not restore them.
def spend (cost : Nat) (x y : Nat) : Prop := cost ≤ x ∧ y = x-cost

theorem spend_conserves (cost x y : Nat) (h : spend cost x y) : y+cost=x := by
  dsimp [spend] at h
  omega

theorem successive_spends (a b x z : Nat) :
    (∃ y, spend a x y ∧ spend b y z) ↔ spend (a+b) x z := by
  simp only [spend]
  constructor
  · rintro ⟨y,⟨ha,rfl⟩,hb,hz⟩; omega
  · rintro ⟨h,hz⟩; refine ⟨x-a,?_,?_,?_⟩ <;> omega

theorem separate_checks_miss_total : (1 ≤ (1:Nat)) ∧ (1 ≤ (1:Nat)) ∧ ¬ spend (1+1) 1 0 := by
  simp [spend]

theorem all_pairs_fit_triple_fails :
    (1+1 ≤ (2:Nat)) ∧ (1+1 ≤ (2:Nat)) ∧ (1+1 ≤ (2:Nat)) ∧ ¬ ∃ y, spend (1+1+1) 2 y := by
  simp [spend]

/-- Explicit reservations suffice for the selected total demand. They are not
independent copies of the full shared stock. -/
theorem reserved_demands_fit (l r a b total : Nat)
    (ha : a ≤ l) (hb : b ≤ r) (budget : l+r ≤ total) :
    ∃ remaining, spend (a+b) total remaining := by
  exact ⟨total-(a+b),by dsimp [spend]; omega⟩

theorem residual_reservations_conserve (l r a b : Nat) (ha : a ≤ l) (hb : b ≤ r) :
    (l-a)+(r-b)+(a+b)=l+r := by omega

def localStep (x : Nat) (_ : Unit) (y : Nat) := spend 1 x y
def jointStep (x : Nat) (_ : Unit × Unit) (y : Nat) := spend 2 x y
def quiet (_ : Nat) : Unit := ()
def jointQuiet (_ : Nat) : Unit × Unit := ((),())
def fine (_ : Nat) := True
def localAllowed (_ : Nat) (_ : Unit) := True
def jointAllowed (_ : Nat) (_ : Unit × Unit) := True
def exactStock (r : Nat) (x : Nat) := x = r
def twice : Plan Unit Unit 2 := .act () (fun _ => .act () (fun _ => .stop))
def once : Plan Unit Unit 1 := .act () (fun _ => .stop)

theorem each_local_twice : works localStep quiet fine localAllowed twice (exactStock 2) := by
  simp [works, twice, usable, post, localStep, spend, quiet, fine, localAllowed, exactStock]

theorem joint_first_step : works jointStep jointQuiet fine jointAllowed (zipPlan once once) (exactStock 2) := by
  simp [works, zipPlan, once, usable, post, jointStep, spend, jointQuiet, fine, jointAllowed, exactStock]

theorem joint_second_step_fails : ¬ works jointStep jointQuiet fine jointAllowed (zipPlan twice twice) (exactStock 2) := by
  simp [works, zipPlan, twice, usable, post, jointStep, spend, jointQuiet, fine, jointAllowed, exactStock]

theorem sufficient_stock_repairs : works jointStep jointQuiet fine jointAllowed (zipPlan twice twice) (exactStock 4) := by
  simp [works, zipPlan, twice, usable, post, jointStep, spend, jointQuiet, fine, jointAllowed, exactStock]

theorem shared_effect_breaks_isolated_projection :
    jointStep 2 ((),()) 0 ∧ ¬ localStep 2 () 0 := by simp [jointStep, localStep, spend]

theorem serialization_without_renewal_fails :
    ¬ ∃ a b c d, spend 1 2 a ∧ spend 1 a b ∧ spend 1 b c ∧ spend 1 c d := by
  simp only [spend]
  omega

end JointContinuation

#print axioms JointContinuation.joint_plan_composition
#print axioms JointContinuation.compatibility_necessary
#print axioms JointContinuation.incompatible_blocks_joint
#print axioms JointContinuation.actual_joint_post_projects
#print axioms JointContinuation.spend_conserves
#print axioms JointContinuation.successive_spends
#print axioms JointContinuation.separate_checks_miss_total
#print axioms JointContinuation.all_pairs_fit_triple_fails
#print axioms JointContinuation.each_local_twice
#print axioms JointContinuation.joint_first_step
#print axioms JointContinuation.joint_second_step_fails
#print axioms JointContinuation.sufficient_stock_repairs
#print axioms JointContinuation.shared_effect_breaks_isolated_projection
#print axioms JointContinuation.serialization_without_renewal_fails

#print axioms JointContinuation.reserved_demands_fit
#print axioms JointContinuation.residual_reservations_conserve
