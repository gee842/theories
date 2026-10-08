import SeededContinuation

namespace EvidenceThroughChange
open ContinuationAdequacy JointContinuation SeededContinuation
variable {X A B U V O P : Type}

/-- Possible states at use, propagated from the evidence at acquisition. -/
def transport (change : X → X → Prop) (C : X → Prop) (y : X) : Prop :=
  ∃ x, C x ∧ change x y

def certifies (change : X → X → Prop) (C I : X → Prop) : Prop :=
  ∀ x y, C x → change x y → I y

theorem actual_remains_covered (change : X → X → Prop) (C : X → Prop)
    (x y : X) (hx : C x) (h : change x y) : transport change C y := ⟨x,hx,h⟩

theorem certificate_iff_transport (change : X → X → Prop) (C I : X → Prop) :
    certifies change C I ↔ ∀ y, transport change C y → I y := by
  constructor
  · rintro h y ⟨x,hx,hd⟩; exact h x y hx hd
  · intro h x y hx hd; exact h y ⟨x,hx,hd⟩

theorem transport_composes (first second : X → X → Prop) (C : X → Prop) (z : X) :
    transport second (transport first C) z ↔
      transport (fun x z => ∃ y, first x y ∧ second y z) C z := by
  constructor
  · rintro ⟨y,⟨x,hx,hxy⟩,hyz⟩; exact ⟨x,hx,y,hxy,hyz⟩
  · rintro ⟨x,hx,y,hxy,hyz⟩; exact ⟨y,⟨x,hx,hxy⟩,hyz⟩

theorem smaller_envelope_retains_certificate
    (large small : X → X → Prop) (C I : X → Prop)
    (sub : ∀ x y, small x y → large x y) (h : certifies large C I) :
    certifies small C I := fun x y hx hd => h x y hx (sub x y hd)

/-- Any finite admitted change history, including zero changes. -/
inductive Reach (change : X → X → Prop) : X → X → Prop
  | refl (x) : Reach change x x
  | next {x y z} : Reach change x y → change y z → Reach change x z

theorem stable_certificate (change : X → X → Prop) (C I : X → Prop)
    (initial : ∀ x, C x → I x)
    (stable : ∀ x y, I x → change x y → I y) : certifies (Reach change) C I := by
  intro x y hx path
  induction path with
  | refl => exact initial x hx
  | next _ edge ih => exact stable _ _ ih edge

/-- Delayed evidence must cover both shared support and local plan domains. -/
theorem delayed_seeded_plan
    (change : X → X → Prop) (C : X → Prop)
    (joint : X → (U × V) → X → Prop) (left : A → U → A → Prop)
    (right : B → V → B → Prop) (pa : X → A) (pb : X → B)
    (oa : A → O) (ob : B → P) (ga : A → Prop) (gb : B → Prop)
    (la : A → U → Prop) (lb : B → V → Prop) (lj : X → (U × V) → Prop)
    (r s : X → Prop)
    (project : ∀ x uv y, joint x uv y → left (pa x) uv.1 (pa y) ∧ right (pb x) uv.2 (pb y))
    (ready : ∀ x u v, r x → s x → la (pa x) u → lb (pb x) v →
      lj x (u,v) ∧ ∃ y, joint x (u,v) y)
    (keepR : ∀ x uv y, r x → s x → joint x uv y → r y)
    (keepS : ∀ x uv y, r x → s x → joint x uv y → s y)
    (n : Nat) (p : Plan U O n) (q : Plan V P n) (Ca : A → Prop) (Cb : B → Prop)
    (evidence : certifies change C (fun x =>
      (Ca (pa x) ∧ Cb (pb x)) ∧ (r x ∧ s x)))
    (hp : works left oa ga la p Ca) (hq : works right ob gb lb q Cb) :
    works joint (fun x => (oa (pa x),ob (pb x)))
      (fun x => ga (pa x) ∧ gb (pb x)) lj (zipPlan p q) (transport change C) := by
  have atUse := (certificate_iff_transport change C _).mp evidence
  exact seeded_joint_plan joint left right pa pb oa ob ga gb la lb lj r s
    project ready keepR keepS n p q (transport change C) Ca Cb
    (fun x hx => (atUse x hx).1) (fun x hx => (atUse x hx).2) hp hq

-- An acquired record and the actual availability it once measured can diverge.
structure State where
  available : Bool
  held : Bool
  record : Bool
  deriving DecidableEq

def readNow (x : State) : State := {x with record := x.available}
def usableNow (x : State) : Prop := x.available=true

def takeElsewhere (x y : State) : Prop :=
  x.available=true ∧ x.held=false ∧ y={x with available:=false}
def reserve (x y : State) : Prop :=
  x.available=true ∧ x.held=false ∧ y={x with held:=true,record:=true}
def admittedChange (x y : State) : Prop := y=x ∨ takeElsewhere x y
def reservedSupport (x : State) : Prop := x.available=true ∧ x.held=true

def start : State := ⟨true,false,false⟩
def checked : State := readNow start
def lost : State := {checked with available:=false}

theorem truthful_read_can_expire :
    usableNow checked ∧ checked.record=true ∧ takeElsewhere checked lost ∧
    lost.record=checked.record ∧ ¬ usableNow lost := by
  simp [usableNow,checked,lost,readNow,start,takeElsewhere]

theorem no_exact_record_only_decision :
    ¬ ∃ decideUse : Bool → Prop, ∀ x, (x=checked ∨ x=lost) →
      (decideUse x.record ↔ usableNow x) := by
  rintro ⟨f,h⟩
  have hc := h checked (Or.inl rfl)
  have hl := h lost (Or.inr rfl)
  have eqr : lost.record=checked.record := rfl
  have good : usableNow checked := rfl
  have bad : ¬ usableNow lost := by simp [usableNow,lost]
  apply bad
  apply hl.mp
  rw [eqr]
  exact hc.mpr good

theorem stale_evidence_not_certificate :
    ¬ certifies admittedChange (fun x => x=checked) usableNow := by
  intro h
  have bad := h checked lost rfl (Or.inr truthful_read_can_expire.2.2.1)
  exact truthful_read_can_expire.2.2.2.2 bad

theorem reserve_establishes_protection (x y : State) (h : reserve x y) :
    reservedSupport y ∧ y.record=true := by
  rcases h with ⟨ha,_,rfl⟩
  exact ⟨⟨ha,rfl⟩,rfl⟩

theorem admitted_change_preserves_protection (x y : State)
    (hx : reservedSupport x) (h : admittedChange x y) : reservedSupport y := by
  rcases h with h | h
  · simpa [h] using hx
  · have impossible : (true:Bool)=false := hx.2.symm.trans h.2.1
    cases impossible

theorem reservation_survives_finite_changes (x y z : State)
    (h : reserve x y) (path : Reach admittedChange y z) : usableNow z := by
  have certified := stable_certificate admittedChange (fun t => t=y) reservedSupport
    (by intro t ht; subst t; exact (reserve_establishes_protection x y h).1)
    admitted_change_preserves_protection
  exact (certified y z rfl path).1

theorem actual_reservation_exists : ∃ y, reserve checked y := by
  exact ⟨⟨true,true,true⟩,rfl,rfl,rfl⟩

theorem duplicate_reservation_blocked (x y : State) (h : reserve x y) :
    ¬ ∃ z, reserve y z := by
  rintro ⟨z,hz⟩
  have held := (reserve_establishes_protection x y h).1.2
  have impossible : (true:Bool)=false := held.symm.trans hz.2.1
  cases impossible

/-- A destructive change outside the admitted law defeats this protection. -/
theorem unmediated_loss_breaks_protection :
    ∃ x y : State, reservedSupport x ∧ y={x with available:=false} ∧ ¬ usableNow y := by
  exact ⟨⟨true,true,true⟩,⟨false,true,true⟩,⟨rfl,rfl⟩,rfl,by simp [usableNow]⟩

end EvidenceThroughChange

#print axioms EvidenceThroughChange.actual_remains_covered
#print axioms EvidenceThroughChange.certificate_iff_transport
#print axioms EvidenceThroughChange.transport_composes
#print axioms EvidenceThroughChange.smaller_envelope_retains_certificate
#print axioms EvidenceThroughChange.stable_certificate
#print axioms EvidenceThroughChange.delayed_seeded_plan
#print axioms EvidenceThroughChange.truthful_read_can_expire
#print axioms EvidenceThroughChange.no_exact_record_only_decision
#print axioms EvidenceThroughChange.stale_evidence_not_certificate
#print axioms EvidenceThroughChange.reserve_establishes_protection
#print axioms EvidenceThroughChange.admitted_change_preserves_protection
#print axioms EvidenceThroughChange.reservation_survives_finite_changes
#print axioms EvidenceThroughChange.actual_reservation_exists
#print axioms EvidenceThroughChange.duplicate_reservation_blocked
#print axioms EvidenceThroughChange.unmediated_loss_breaks_protection
