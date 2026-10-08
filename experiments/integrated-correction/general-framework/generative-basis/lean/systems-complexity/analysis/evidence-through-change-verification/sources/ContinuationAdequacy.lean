import Mathlib.Tactic

/-! Finite-horizon adequacy of retained information within a joint process.
The transition, observation and admissibility correspondences are supplied.
No statistical calibration, moral warrant or infinite continuation is inferred. -/
namespace ContinuationAdequacy
variable {X U O : Type}

def post (step : X → U → X → Prop) (obs : X → O)
    (B : X → Prop) (u : U) (o : O) (y : X) : Prop :=
  ∃ x, B x ∧ step x u y ∧ obs y = o

def usable (step : X → U → X → Prop) (allowed : X → U → Prop)
    (B : X → Prop) (u : U) : Prop :=
  ∀ x, B x → allowed x u ∧ ∃ y, step x u y

def viable (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) : Nat → (X → Prop) → Prop
  | 0, B => ∀ x, B x → good x
  | n+1, B => (∀ x, B x → good x) ∧
      ∃ u, usable step allowed B u ∧ ∀ o, viable step obs good allowed n (post step obs B u o)

theorem actual_in_post (step : X → U → X → Prop) (obs : X → O)
    (B : X → Prop) (u : U) (x y : X) (hx : B x) (h : step x u y) :
    post step obs B u (obs y) y := ⟨x, hx, h, rfl⟩

theorem post_mono (step : X → U → X → Prop) (obs : X → O)
    (B C : X → Prop) (h : ∀ x, B x → C x) (u : U) (o : O) :
    ∀ y, post step obs B u o y → post step obs C u o y := by
  rintro y ⟨x,hx,hs,ho⟩
  exact ⟨x,h x hx,hs,ho⟩

theorem viable_mono (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) :
    ∀ B C, (∀ x, B x → C x) → viable step obs good allowed n C →
      viable step obs good allowed n B := by
  induction n with
  | zero => intro B C h v x hx; exact v x (h x hx)
  | succ n ih =>
    rintro B C h ⟨g,u,hu,hv⟩
    exact ⟨fun x hx => g x (h x hx), u,
      (fun x hx => hu x (h x hx)),
      fun o => ih _ _ (post_mono step obs B C h u o) (hv o)⟩

theorem viable_now (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) (B : X → Prop)
    (h : viable step obs good allowed n B) : ∀ x, B x → good x := by
  cases n with
  | zero => exact h
  | succ n => exact h.1

theorem viable_shorter (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) :
    ∀ B, viable step obs good allowed (n+1) B → viable step obs good allowed n B := by
  induction n with
  | zero => intro B h; exact h.1
  | succ n ih =>
    rintro B ⟨g,u,hu,hv⟩
    exact ⟨g,u,hu,fun o => ih _ (hv o)⟩

/-- Empty observation branches impose no demand if a response type is inhabited. -/
theorem viable_empty [Nonempty U] (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) :
    viable step obs good allowed n (fun _ => False) := by
  induction n with
  | zero => intro x hx; exact False.elim hx
  | succ n ih =>
    obtain ⟨u⟩ := ‹Nonempty U›
    refine ⟨fun _ hx => False.elim hx, u, (fun _ hx => False.elim hx), ?_⟩
    intro o
    apply viable_mono step obs good allowed n _ (fun _ => False) _ ih
    rintro y ⟨x,hx,_,_⟩
    exact hx

/-- Refining future observations preserves feasible plans when transitions and
admissibility stay identical. Acquisition costs are not erased by this claim. -/
theorem observation_refinement {F : Type} (step : X → U → X → Prop)
    (coarse : X → O) (fine : X → F) (forget : F → O)
    (consistent : ∀ x, forget (fine x) = coarse x)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) :
    ∀ B, viable step coarse good allowed n B → viable step fine good allowed n B := by
  induction n with
  | zero => intro B h; exact h
  | succ n ih =>
    rintro B ⟨g,u,hu,hv⟩
    refine ⟨g,u,hu,?_⟩
    intro f
    apply viable_mono step fine good allowed n _ (post step coarse B u (forget f))
    · rintro y ⟨x,hx,hs,hy⟩
      exact ⟨x,hx,hs,by rw [← consistent y,hy]⟩
    · exact ih _ (hv (forget f))

inductive Plan (U O : Type) : Nat → Type where
  | stop : Plan U O 0
  | act {n : Nat} (u : U) (next : O → Plan U O n) : Plan U O (n+1)

def works (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) :
    {n : Nat} → Plan U O n → (X → Prop) → Prop
  | _, .stop, B => ∀ x, B x → good x
  | _, .act u next, B => (∀ x, B x → good x) ∧ usable step allowed B u ∧
      ∀ o, works step obs good allowed (next o) (post step obs B u o)

theorem viable_iff_plan (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) :
    ∀ B, viable step obs good allowed n B ↔ ∃ p : Plan U O n, works step obs good allowed p B := by
  classical
  induction n with
  | zero =>
    intro B
    constructor
    · intro h; exact ⟨.stop,h⟩
    · rintro ⟨p,h⟩; cases p; exact h
  | succ n ih =>
    intro B
    constructor
    · rintro ⟨g,u,hu,hv⟩
      have hp : ∀ o, ∃ p : Plan U O n, works step obs good allowed p (post step obs B u o) :=
        fun o => (ih _).mp (hv o)
      choose ps hs using hp
      exact ⟨.act u ps,g,hu,hs⟩
    · rintro ⟨p,h⟩
      cases p with
      | act u ps => exact ⟨h.1,u,h.2.1,fun o => (ih _).mpr ⟨ps o,h.2.2 o⟩⟩

/-- Every compatible successor remains in a viable information class. -/
theorem viable_successor (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) (B : X → Prop)
    (h : viable step obs good allowed (n+1) B) :
    ∃ u, usable step allowed B u ∧ ∀ x y, B x → step x u y →
      post step obs B u (obs y) y ∧ viable step obs good allowed n (post step obs B u (obs y)) := by
  obtain ⟨_,u,hu,hv⟩ := h
  exact ⟨u,hu,fun x y hx hs => ⟨actual_in_post step obs B u x y hx hs,hv (obs y)⟩⟩

/-- Invariant information classes support every finite horizon; not infinite-plan extraction. -/
theorem maintained_class (step : X → U → X → Prop) (obs : X → O)
    (good : X → Prop) (allowed : X → U → Prop) (C : (X → Prop) → Prop)
    (safe : ∀ B, C B → ∀ x, B x → good x)
    (closed : ∀ B, C B → ∃ u, usable step allowed B u ∧ ∀ o, C (post step obs B u o))
    (n : Nat) : ∀ B, C B → viable step obs good allowed n B := by
  induction n with
  | zero => exact safe
  | succ n ih =>
    intro B hb
    obtain ⟨u,hu,hnext⟩ := closed B hb
    exact ⟨safe B hb,u,hu,fun o => ih _ (hnext o)⟩

-- A finite branching witness. Both initial histories permit a first step.
-- Without the next distinction, they require incompatible second responses.
inductive Stage where | seed | need | done | lost deriving DecidableEq, Fintype
abbrev State := Stage × Bool
def good (x : State) : Prop := x.1 ≠ .lost
def allowed (_ : State) (_ : Bool) : Prop := True
def advance (x : State) (u : Bool) : State :=
  match x.1 with
  | .seed => (.need,x.2)
  | .need => if u = x.2 then (.done,x.2) else (.lost,x.2)
  | .done => x
  | .lost => x
def step (x : State) (u : Bool) (y : State) : Prop := y = advance x u
def seeds (x : State) : Prop := x.1 = .seed
def blind (_ : State) : Unit := ()
def sensed (x : State) : Bool := x.2

set_option maxRecDepth 4000
set_option maxHeartbeats 1000000

theorem shared_first_step : viable step blind good allowed 1 seeds := by
  simp [viable, usable, post, step, advance, seeds, good, allowed, blind]

theorem blind_second_step_fails : ¬ viable step blind good allowed 2 seeds := by
  simp [viable, usable, post, step, advance, seeds, good, allowed, blind]

theorem sensing_repairs_two_steps : viable step sensed good allowed 2 seeds := by
  simp [viable, usable, post, step, advance, seeds, good, allowed, sensed]

/-- This alternative changes the actual dependency; it does not just erase its record. -/
def settle (x : State) (_ : Bool) (y : State) : Prop := y = (Stage.done,x.2)

theorem settling_repairs_blind_two_steps : viable settle blind good allowed 2 seeds := by
  simp [viable, usable, post, settle, seeds, good, allowed, blind]

end ContinuationAdequacy

#print axioms ContinuationAdequacy.actual_in_post
#print axioms ContinuationAdequacy.post_mono
#print axioms ContinuationAdequacy.viable_mono
#print axioms ContinuationAdequacy.viable_now
#print axioms ContinuationAdequacy.viable_shorter
#print axioms ContinuationAdequacy.viable_empty
#print axioms ContinuationAdequacy.viable_iff_plan
#print axioms ContinuationAdequacy.viable_successor
#print axioms ContinuationAdequacy.maintained_class
#print axioms ContinuationAdequacy.shared_first_step
#print axioms ContinuationAdequacy.blind_second_step_fails
#print axioms ContinuationAdequacy.sensing_repairs_two_steps
#print axioms ContinuationAdequacy.settling_repairs_blind_two_steps

#print axioms ContinuationAdequacy.observation_refinement
