import Becoming.SeedReach

/-!
# Reach through scopes, and within histories

A process whose labels are scopes moves under one scope at a time; one scope's steps alone are
`only P i`. What one scope's steps reach from a seed the whole process reaches (`only_reach`), a
property is invariant under the process exactly where it is invariant under each scope's steps
(`invariant_iff_only`), and reach under the whole process can go beyond what each scope reaches
alone.

* **Grounds glued across scopes.** Each scope has a domain and gives a ground on it. Where the
  grounds agree wherever two domains meet (`Agree`), the glued ground (`Glued`: some scope's domain
  holds the configuration and that scope's ground holds there) is that scope's ground anywhere in
  its domain (`glued_iff_local`). Where every step stays in its scope's domain and carries that
  scope's ground, the glued ground is invariant (`glued_invariant`) and holds wherever the process
  reaches from seeds where it holds (`glued_on_reach`).
* **Within histories.** A family of processes indexed by histories is one process on the
  configurations of every history whose steps stay within one history (`within`). No path of it
  leaves a history (`within_keeps`); it reaches a configuration of a history from a seed exactly
  where that history's process reaches it from a seed of that history (`fromSeed_within_iff`); a
  property invariant in each history holds wherever it reaches from seeds the property holds at
  (`invariant_on_within_reach`).
* **Witnesses.** In the alternating process, two scopes overlapping at the middle
  (`alternating_steps`), what one scope's steps reach from the start stays in its domain or at the
  start (`first_scope_stays_inside`, `second_scope_stays_at_seed`), and the process reaches the
  finish from the start although neither scope's steps alone do (`alternating_beyond_scopes`); in the halted process every configuration lies in a scope's domain
  and a seed exists, yet the finish is not reached (`halted_coverage_insufficient`).

`WholeGroundCoverage` states these of a local atlas, whose edges are between configurations of a
scope's domain by their type; here that is the hypothesis that every step stays in its scope's
domain. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace ScopedReach

open SeedReachProcesses

section Scopes

variable {S : Type u} {L : Type v}

/-- One scope's steps alone. -/
def only (P : Process S L) (i : L) : Process S Unit := ⟨fun x _ y => P.step x i y⟩

/-- **What one scope's steps reach from a seed, the whole process reaches.** -/
theorem only_reach {P : Process S L} {i : L} {seed : S → Prop} {x : S}
    (reached : FromSeed (only P i) seed x) : FromSeed P seed x :=
  match reached with
  | ⟨s, held, path⟩ =>
    ⟨s, held, Invariant.reach (P := only P i) (I := Reach P s)
      (fun _ _ _ step r => r.trans (Reach.of_step step)) path (Reach.refl P s)⟩

/-- **A property is invariant under the process exactly where each scope's steps carry it.** -/
theorem invariant_iff_only {P : Process S L} {R : S → Prop} :
    Invariant P R ↔ ∀ i, Invariant (only P i) R :=
  ⟨fun inv i x _ y step held => inv x i y step held,
   fun all x i y step held => all i x () y step held⟩

/-- The grounds agree wherever two scopes' domains meet. -/
def Agree (domain ground : L → S → Prop) : Prop :=
  ∀ i j p, domain i p → domain j p → (ground i p ↔ ground j p)

/-- The glued ground: some scope's domain holds the configuration and that scope's ground holds
there. -/
def Glued (domain ground : L → S → Prop) (p : S) : Prop := ∃ i, domain i p ∧ ground i p

/-- **Where the grounds agree on overlaps, the glued ground is each scope's ground in its
domain.** -/
theorem glued_iff_local {domain ground : L → S → Prop} (agree : Agree domain ground) {i : L}
    {p : S} (inside : domain i p) : Glued domain ground p ↔ ground i p :=
  ⟨fun ⟨j, there, held⟩ => (agree j i p there inside).mp held, fun held => ⟨i, inside, held⟩⟩

/-- **Agreeing grounds carried by each scope's steps glue to an invariant**, where every step stays
in its scope's domain. -/
theorem glued_invariant {P : Process S L} {domain ground : L → S → Prop}
    (agree : Agree domain ground) (inside : ∀ i x y, P.step x i y → domain i x ∧ domain i y)
    (carried : ∀ i x y, P.step x i y → ground i x → ground i y) :
    Invariant P (Glued domain ground) :=
  fun x i y step glued =>
    (glued_iff_local agree (inside i x y step).2).mpr
      (carried i x y step ((glued_iff_local agree (inside i x y step).1).mp glued))

/-- **The glued ground holds wherever the process reaches from seeds where it holds.** -/
theorem glued_on_reach {P : Process S L} {domain ground : L → S → Prop} {seed : S → Prop}
    (agree : Agree domain ground) (inside : ∀ i x y, P.step x i y → domain i x ∧ domain i y)
    (carried : ∀ i x y, P.step x i y → ground i x → ground i y)
    (seeds : ∀ p, seed p → Glued domain ground p) {p : S} (reached : FromSeed P seed p) :
    Glued domain ground p :=
  fromSeed_iff_invariant.mp reached _ seeds (glued_invariant agree inside carried)

end Scopes

/-! ## Within histories -/

section Histories

variable {H : Type u} {X : H → Type v} {L : Type w}

/-- A step of the family within one history. -/
inductive WithinStep (Q : (h : H) → Process (X h) L) : Sigma X → L → Sigma X → Prop where
  | within (h : H) (p : X h) (a : L) (q : X h) : (Q h).step p a q → WithinStep Q ⟨h, p⟩ a ⟨h, q⟩

/-- **A family of processes indexed by histories as one process**, whose steps stay within one
history. -/
def within (Q : (h : H) → Process (X h) L) : Process (Sigma X) L := ⟨WithinStep Q⟩

/-- **No path of the family's process leaves a history.** -/
theorem within_keeps {Q : (h : H) → Process (X h) L} {x y : Sigma X}
    (path : Reach (within Q) x y) : x.1 = y.1 :=
  Invariant.reach (P := within Q) (I := fun z => x.1 = z.1)
    (fun _ _ _ step same => match step, same with
      | .within _ _ _ _ _, same => same)
    path rfl

/-- **The family's process reaches a configuration of a history from a seed exactly where that
history's process reaches it from a seed of that history.** -/
theorem fromSeed_within_iff (Q : (h : H) → Process (X h) L) (seed : Sigma X → Prop) (h : H)
    (p : X h) :
    FromSeed (within Q) seed ⟨h, p⟩ ↔ FromSeed (Q h) (fun q => seed ⟨h, q⟩) p :=
  ⟨fun reached =>
    fromSeed_iff_invariant.mp reached (fun y => FromSeed (Q y.1) (fun q => seed ⟨y.1, q⟩) y.2)
      (fun y held => ⟨y.2, held, Reach.refl _ _⟩)
      (fun _ _ _ step r => match step, r with
        | .within _ _ _ _ st, r => r.step st),
   fun ⟨s, held, path⟩ =>
    Invariant.reach (P := Q h) (I := fun q => FromSeed (within Q) seed ⟨h, q⟩)
      (fun _ a _ st r => r.step (WithinStep.within h _ a _ st)) path
      ⟨⟨h, s⟩, held, Reach.refl _ _⟩⟩

/-- **A property invariant in each history holds wherever the family's process reaches from
seeds it holds at.** -/
theorem invariant_on_within_reach {Q : (h : H) → Process (X h) L} {seed : Sigma X → Prop}
    {R : (h : H) → X h → Prop} (seeds : ∀ h p, seed ⟨h, p⟩ → R h p)
    (inv : ∀ h, Invariant (Q h) (R h)) {h : H} {p : X h}
    (reached : FromSeed (within Q) seed ⟨h, p⟩) : R h p :=
  match (fromSeed_within_iff Q seed h p).mp reached with
  | ⟨_, held, path⟩ => (inv h).reach path (seeds h _ held)

end Histories

/-! ## Witnesses -/

/-- Three configurations. -/
inductive Place where
  | start
  | middle
  | finish

/-- Two scopes meeting at the middle: `false` holds the start and the middle, `true` the middle
and the finish. -/
def domain : Bool → Place → Prop
  | false, .start => True
  | false, .middle => True
  | false, .finish => False
  | true, .start => False
  | true, .middle => True
  | true, .finish => True

/-- The alternating process: scope `false` steps from the start to the middle, scope `true` from
the middle to the finish. -/
def alternating : Process Place Bool :=
  ⟨fun x i y => (i = false ∧ x = .start ∧ y = .middle) ∨ (i = true ∧ x = .middle ∧ y = .finish)⟩

/-- Every configuration lies in a scope's domain. -/
theorem domain_covers : ∀ p, ∃ i, domain i p
  | .start => ⟨false, trivial⟩
  | .middle => ⟨false, trivial⟩
  | .finish => ⟨true, trivial⟩

/-- Every step of the alternating process stays in its scope's domain. -/
theorem alternating_inside : ∀ i x y, alternating.step x i y → domain i x ∧ domain i y := by
  intro i x y step
  rcases step with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ <;> exact ⟨trivial, trivial⟩

/-- The alternating process's two steps: scope `false` from the start to the middle, scope `true`
from the middle to the finish. -/
theorem alternating_steps :
    alternating.step Place.start false Place.middle ∧ alternating.step Place.middle true Place.finish :=
  ⟨Or.inl ⟨rfl, rfl, rfl⟩, Or.inr ⟨rfl, rfl, rfl⟩⟩

/-- What scope `false`'s steps alone reach from the start stays in its domain. -/
theorem first_scope_stays_inside {p : Place}
    (reached : FromSeed (only alternating false) (fun x => x = Place.start) p) : domain false p :=
  fromSeed_iff_invariant.mp reached (domain false) (fun _ start => start ▸ trivial)
    (fun _ _ _ step _ => (alternating_inside false _ _ step).2)

/-- What scope `true`'s steps alone reach from the start is the start. -/
theorem second_scope_stays_at_seed {p : Place}
    (reached : FromSeed (only alternating true) (fun x => x = Place.start) p) : p = Place.start :=
  fromSeed_iff_invariant.mp reached (fun x => x = Place.start) (fun _ start => start)
    (fun _ _ _ step atStart => match step with
      | .inl ⟨same, _, _⟩ => Bool.noConfusion same
      | .inr ⟨_, atMiddle, _⟩ => Place.noConfusion (atStart.symm.trans atMiddle))

/-- **Alternating scopes reach beyond each scope.** The alternating process reaches the finish
from the start, and neither scope's steps alone reach it. -/
theorem alternating_beyond_scopes :
    FromSeed alternating (fun x => x = Place.start) Place.finish ∧
      ¬ FromSeed (only alternating false) (fun x => x = Place.start) Place.finish ∧
      ¬ FromSeed (only alternating true) (fun x => x = Place.start) Place.finish :=
  ⟨⟨.start, rfl, [false, true],
    .cons (Or.inl ⟨rfl, rfl, rfl⟩) (.cons (Or.inr ⟨rfl, rfl, rfl⟩) (.nil Place.finish))⟩,
   fun reached => first_scope_stays_inside reached,
   fun reached =>
    have atStart : Place.finish = Place.start := second_scope_stays_at_seed reached
    nomatch atStart⟩

/-- The halted process: no step under any scope. -/
def halted : Process Place Unit := ⟨fun _ _ _ => False⟩

/-- **Covering every configuration by a scope does not give reach.** Every configuration lies in
the one scope's domain and a seed exists, yet the halted process does not reach the finish from
the start. -/
theorem halted_coverage_insufficient :
    (∀ p : Place, ∃ i : Unit, (fun _ _ => True : Unit → Place → Prop) i p) ∧
      (∃ p, (fun x => x = Place.start) p) ∧ ¬ FromSeed halted (fun x => x = Place.start) Place.finish :=
  ⟨fun _ => ⟨(), trivial⟩, ⟨.start, rfl⟩,
   fun reached =>
    have atStart : Place.finish = Place.start :=
      (fromSeed_iff_seed_of_no_moves (P := halted) (seed := fun x => x = Place.start)
        (x := Place.finish) (fun _ _ ⟨_, step⟩ => step)).mp reached
    nomatch atStart⟩

end ScopedReach

end Becoming
