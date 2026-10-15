import Becoming.Keeping
import JointContinuation

/-!
# Finite continuation and joint plans as instances of the core's keeping

`ContinuationAdequacy` states, for supplied transitions, observations of the configuration
reached, a target and admissibility, that `n`-step viability is equivalent to an
observation-branching `n`-step plan that works (`viable_iff_plan`), and `JointContinuation` that
two local plans run together as a joint plan keeping both endpoint requirements, under projection,
initial cover and recursive joint executability (`joint_plan_composition`), which every working
joint plan has (`compatibility_necessary`). `Becoming.Keeping` states these for every process,
every registration of its steps, every guard and every condition on moves.

This periphery module reads the earlier models in the core. The transitions are a process
(`processOf`), observing the configuration reached is a registration of the step (`successor`),
the class after a response and an observation is the core's `Seen` (`post_eq_seen`), and
viability is `KeptFor` (`viable_iff_keptFor`). Plans translate both ways, keeping what works
(`works_iff_keeps`, `keeps_iff_works`). So `viable_iff_plan` follows from the core's
`keptFor_iff_plan_of_choice`, with choice over the observations from Lean's `Classical.choice`
(`viable_iff_plan_by_core`); where the observations are listed it needs none
(`viable_iff_plan_listed`), and the core's `plans_iff_choice` says that for arbitrary observations
choice is exactly what the converse needs. The pairing of plans is the core's `Plan.zip`
(`toPlan_zip`), recursive joint executability is `Plan.Compatible` (`compatible_iff`), and the two
joint theorems follow from `Plan.zip_keeps` and `Plan.compatible_of_zip_keeps`
(`joint_plan_composition_by_core`, `compatibility_necessary_by_core`). The core does not import
this module; the earlier modules keep their scope.
-/

namespace Becoming.ContinuationCorrespondence

open Generative Becoming.Viability

section Continuation

variable {X U O : Type}

/-- The transitions of `ContinuationAdequacy` as a process. -/
def processOf (step : X → U → X → Prop) : Process X U := ⟨step⟩

/-- Observing the configuration a step reaches, as a registration of the step. -/
def successor (obs : X → O) : X → U → X → O := fun _ _ y => obs y

/-- The class after a response and an observation is the core's `Seen`. -/
theorem post_eq_seen (step : X → U → X → Prop) (obs : X → O) (B : X → Prop) (u : U) (o : O) :
    ContinuationAdequacy.post step obs B u o = Seen (processOf step) (successor obs) B u o :=
  rfl

/-- A usable response is the core's `Usable`. -/
theorem usable_iff (step : X → U → X → Prop) (allowed : X → U → Prop) (B : X → Prop) (u : U) :
    ContinuationAdequacy.usable step allowed B u ↔ Usable (processOf step) allowed B u :=
  Iff.rfl

/-- **Viability is the core's `KeptFor`**, the observation registering the configuration
reached. -/
theorem viable_iff_keptFor (step : X → U → X → Prop) (obs : X → O) (good : X → Prop)
    (allowed : X → U → Prop) :
    ∀ n B, ContinuationAdequacy.viable step obs good allowed n B ↔
      KeptFor (processOf step) (successor obs) good allowed n B
  | 0, _ => Iff.rfl
  | n + 1, _ =>
    ⟨fun ⟨within, u, usable, next⟩ =>
      ⟨within, u, usable, fun o => (viable_iff_keptFor step obs good allowed n _).mp (next o)⟩,
     fun ⟨within, u, usable, next⟩ =>
      ⟨within, u, usable, fun o => (viable_iff_keptFor step obs good allowed n _).mpr (next o)⟩⟩

/-- An earlier plan as a core plan. -/
def toPlan : {n : Nat} → ContinuationAdequacy.Plan U O n → Plan U O n
  | _, .stop => .stop
  | _, .act u next => .act u fun o => toPlan (next o)

/-- A core plan as an earlier plan. -/
def ofPlan : {n : Nat} → Plan U O n → ContinuationAdequacy.Plan U O n
  | 0, _ => .stop
  | _ + 1, p => .act p.first fun o => ofPlan (p.rest o)

/-- **An earlier plan works exactly where, as a core plan, it keeps the guard.** -/
theorem works_iff_keeps (step : X → U → X → Prop) (obs : X → O) (good : X → Prop)
    (allowed : X → U → Prop) :
    ∀ {n} (p : ContinuationAdequacy.Plan U O n) (B : X → Prop),
      ContinuationAdequacy.works step obs good allowed p B ↔
        (toPlan p).Keeps (processOf step) (successor obs) good allowed B
  | _, .stop, _ => Iff.rfl
  | _, .act _ next, _ =>
    ⟨fun ⟨within, usable, rest⟩ => ⟨within, usable,
       fun o => (works_iff_keeps step obs good allowed (next o) _).mp (rest o)⟩,
     fun ⟨within, usable, rest⟩ => ⟨within, usable,
       fun o => (works_iff_keeps step obs good allowed (next o) _).mpr (rest o)⟩⟩

/-- **A core plan keeps the guard exactly where, as an earlier plan, it works.** -/
theorem keeps_iff_works (step : X → U → X → Prop) (obs : X → O) (good : X → Prop)
    (allowed : X → U → Prop) :
    ∀ {n} (p : Plan U O n) (B : X → Prop),
      p.Keeps (processOf step) (successor obs) good allowed B ↔
        ContinuationAdequacy.works step obs good allowed (ofPlan p) B
  | 0, _, _ => Iff.rfl
  | _ + 1, p, _ =>
    ⟨fun ⟨within, usable, rest⟩ => ⟨within, usable,
       fun o => (keeps_iff_works step obs good allowed (p.rest o) _).mp (rest o)⟩,
     fun ⟨within, usable, rest⟩ => ⟨within, usable,
       fun o => (keeps_iff_works step obs good allowed (p.rest o) _).mpr (rest o)⟩⟩

/-- Some plan works exactly where some core plan keeps the guard. -/
theorem works_exists_iff (step : X → U → X → Prop) (obs : X → O) (good : X → Prop)
    (allowed : X → U → Prop) (n : Nat) (B : X → Prop) :
    (∃ p : Plan U O n, p.Keeps (processOf step) (successor obs) good allowed B) ↔
      ∃ p : ContinuationAdequacy.Plan U O n, ContinuationAdequacy.works step obs good allowed p B :=
  ⟨fun ⟨p, keeps⟩ => ⟨ofPlan p, (keeps_iff_works step obs good allowed p B).mp keeps⟩,
   fun ⟨p, works⟩ => ⟨toPlan p, (works_iff_keeps step obs good allowed p B).mp works⟩⟩

/-- Choice over the observations from Lean's `Classical.choice`, the periphery's standard axiom. -/
theorem classicalChoice {α : Type} : ChoiceOver O α :=
  fun _ each => ⟨fun o => Classical.choose (each o), fun o => Classical.choose_spec (each o)⟩

/-- **`ContinuationAdequacy.viable_iff_plan` from the core**: `keptFor_iff_plan_of_choice` with
choice over the observations. -/
theorem viable_iff_plan_by_core (step : X → U → X → Prop) (obs : X → O) (good : X → Prop)
    (allowed : X → U → Prop) (n : Nat) (B : X → Prop) :
    ContinuationAdequacy.viable step obs good allowed n B ↔
      ∃ p : ContinuationAdequacy.Plan U O n, ContinuationAdequacy.works step obs good allowed p B :=
  (viable_iff_keptFor step obs good allowed n B).trans
    ((keptFor_iff_plan_of_choice fun _ => classicalChoice).trans
      (works_exists_iff step obs good allowed n B))

/-- **Where the observations are listed, viability is a working plan with no axiom**: the core's
`keptFor_iff_plan`. -/
theorem viable_iff_plan_listed {k : Nat} (step : X → U → X → Prop) (obs : X → Fin k)
    (good : X → Prop) (allowed : X → U → Prop) (n : Nat) (B : X → Prop) :
    ContinuationAdequacy.viable step obs good allowed n B ↔
      ∃ p : ContinuationAdequacy.Plan U (Fin k) n,
        ContinuationAdequacy.works step obs good allowed p B :=
  (viable_iff_keptFor step obs good allowed n B).trans
    (keptFor_iff_plan.trans (works_exists_iff step obs good allowed n B))

end Continuation

section Joint

variable {X Y Z U V O Q : Type}

/-- **The pairing of plans is the core's `Plan.zip`.** -/
theorem toPlan_zip : ∀ {n} (p : ContinuationAdequacy.Plan U O n)
    (q : ContinuationAdequacy.Plan V Q n),
    toPlan (JointContinuation.zipPlan p q) = Plan.zip (toPlan p) (toPlan q)
  | _, .stop, .stop => rfl
  | _, .act u f, .act v g =>
    congrArg (Plan.act (u, v)) (funext fun o => toPlan_zip (f o.1) (g o.2))

/-- **Recursive joint executability is the core's `Plan.Compatible`.** -/
theorem compatible_iff (joint : X → U × V → X → Prop) (obs : X → O × Q)
    (allow : X → U × V → Prop) :
    ∀ {n} (p : ContinuationAdequacy.Plan U O n) (q : ContinuationAdequacy.Plan V Q n)
      (C : X → Prop),
      JointContinuation.compatible joint obs allow p q C ↔
        Plan.Compatible (processOf joint) (successor obs) allow (toPlan p) (toPlan q) C
  | _, .stop, .stop, _ => Iff.rfl
  | _, .act _ f, .act _ g, _ =>
    ⟨fun ⟨usable, rest⟩ => ⟨usable,
       fun o => (compatible_iff joint obs allow (f o.1) (g o.2) _).mp (rest o)⟩,
     fun ⟨usable, rest⟩ => ⟨usable,
       fun o => (compatible_iff joint obs allow (f o.1) (g o.2) _).mpr (rest o)⟩⟩

/-- **`JointContinuation.joint_plan_composition` from the core's `Plan.zip_keeps`.** -/
theorem joint_plan_composition_by_core
    (joint : X → (U × V) → X → Prop) (left : Y → U → Y → Prop)
    (right : Z → V → Z → Prop) (pa : X → Y) (pb : X → Z)
    (oa : Y → O) (ob : Z → Q) (ga : Y → Prop) (gb : Z → Prop)
    (la : Y → U → Prop) (lb : Z → V → Prop) (lj : X → (U × V) → Prop)
    (project : ∀ x uv y, joint x uv y → left (pa x) uv.1 (pa y) ∧ right (pb x) uv.2 (pb y))
    {n : Nat} (p : ContinuationAdequacy.Plan U O n) (q : ContinuationAdequacy.Plan V Q n)
    (C : X → Prop) (Ca : Y → Prop) (Cb : Z → Prop)
    (cover : ∀ x, C x → Ca (pa x) ∧ Cb (pb x))
    (hp : ContinuationAdequacy.works left oa ga la p Ca)
    (hq : ContinuationAdequacy.works right ob gb lb q Cb)
    (hc : JointContinuation.compatible joint (fun x => (oa (pa x), ob (pb x))) lj p q C) :
    ContinuationAdequacy.works joint (fun x => (oa (pa x), ob (pb x)))
      (fun x => ga (pa x) ∧ gb (pb x)) lj (JointContinuation.zipPlan p q) C :=
  (works_iff_keeps joint (fun x => (oa (pa x), ob (pb x))) (fun x => ga (pa x) ∧ gb (pb x)) lj
      (JointContinuation.zipPlan p q) C).mpr
    (Eq.subst (motive := fun z => z.Keeps (processOf joint)
        (successor fun x => (oa (pa x), ob (pb x))) (fun x => ga (pa x) ∧ gb (pb x)) lj C)
      (toPlan_zip p q).symm
      (Plan.zip_keeps (P := processOf joint) (PX := processOf left) (PY := processOf right)
        (left := successor oa) (right := successor ob) project cover
        ((works_iff_keeps left oa ga la p Ca).mp hp) ((works_iff_keeps right ob gb lb q Cb).mp hq)
        ((compatible_iff joint (fun x => (oa (pa x), ob (pb x))) lj p q C).mp hc)))

/-- **`JointContinuation.compatibility_necessary` from the core's
`Plan.compatible_of_zip_keeps`.** -/
theorem compatibility_necessary_by_core
    (joint : X → (U × V) → X → Prop) (obs : X → O × Q)
    (good : X → Prop) (allow : X → (U × V) → Prop) {n : Nat}
    (p : ContinuationAdequacy.Plan U O n) (q : ContinuationAdequacy.Plan V Q n) (C : X → Prop)
    (works : ContinuationAdequacy.works joint obs good allow (JointContinuation.zipPlan p q) C) :
    JointContinuation.compatible joint obs allow p q C :=
  (compatible_iff joint obs allow p q C).mpr
    (Plan.compatible_of_zip_keeps
      (Eq.subst (motive := fun z => z.Keeps (processOf joint) (successor obs) good allow C)
        (toPlan_zip p q) ((works_iff_keeps joint obs good allow _ C).mp works)))

end Joint

end Becoming.ContinuationCorrespondence
