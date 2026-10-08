import GroundRelationTransport

/-! Source-free use of a given binding preserves arbitrary ground relations.
This derives a restricted logical-relations property from the existing syntax;
it does not postulate uniformity or ground the syntax/metatheory itself. -/
namespace Generative.RecognitionalBinding
open InferentialGrounds GroundRelationTransport
universe u
variable {Ground : Nat → Type u} {context : List Form} {a : Form}

def SourceFree : Term Ground context a → Prop
  | .source _ _ => False
  | .use _ => True
  | .pair x y => SourceFree x ∧ SourceFree y
  | .first x => SourceFree x
  | .second x => SourceFree x
  | .abstract x => SourceFree x
  | .apply f x => SourceFree f ∧ SourceFree x

/-- No separate source-adequacy premise is needed in this restricted fragment.
Both evaluations are positions in the same displayed term construction. -/
theorem source_free_related (R : ∀ i, Ground i → Ground i → Prop)
    (term : Term Ground context a) : SourceFree term →
    ∀ (left right : ContextGround Ground context), EnvsRelated R left right →
      Related R a (extract term left) (extract term right) := by
  induction term with
  | source i g => intro pure; exact pure.elim
  | use p => intro _ left right envs; exact envs p
  | pair x y ihx ihy =>
    intro pure left right envs
    exact ⟨ihx pure.1 left right envs, ihy pure.2 left right envs⟩
  | first x ih => intro pure left right envs; exact (ih pure left right envs).1
  | second x ih => intro pure left right envs; exact (ih pure left right envs).2
  | abstract body ih =>
    intro pure left right envs x y xy
    exact ih pure (extendContext x left) (extendContext y right)
      (extend_related R left right envs x y xy)
  | apply f x ihf ihx =>
    intro pure left right envs
    exact ihf pure.1 left right envs (extract x left) (extract x right)
      (ihx pure.2 left right envs)

theorem no_closed_source_free_atom (term : Term Ground [] (.atom i))
    (pure : SourceFree term) : False := by
  exact source_free_related (fun _ _ _ => False) term pure
    (emptyContext Ground) (emptyContext Ground) (fun p => nomatch p)

/-- Arbitrary finite terms of this shape, not just one written identity term.
The same carrier is used at all atomic indices; there are no ground sources,
ambient assumptions, base inspections or recursive term constructors. -/
theorem closed_identity_forced (G : Type u)
    (term : Term (fun _ => G) [] (.arrow (.atom i) (.atom i)))
    (pure : SourceFree term) (g : G) :
    extract term (emptyContext (fun _ => G)) g = g := by
  have related := source_free_related (fun _ x _ => x = g) term pure
    (emptyContext (fun _ => G)) (emptyContext (fun _ => G)) (fun p => nomatch p)
  exact related g g rfl

theorem closed_identity_preserves (G : Type u)
    (term : Term (fun _ => G) [] (.arrow (.atom i) (.atom i)))
    (pure : SourceFree term) (criterion : G → Prop) (g : G) (h : criterion g) :
    criterion (extract term (emptyContext (fun _ => G)) g) := by
  rw [closed_identity_forced G term pure g]
  exact h

def boundIdentity (G : Nat → Type u) (i : Nat) :
    Term G [] (.arrow (.atom i) (.atom i)) := .abstract (.use .here)

theorem bound_identity_spec (G : Nat → Type u) (i : Nat) :
    SourceFree (boundIdentity G i) ∧
      ∀ g, extract (boundIdentity G i) (emptyContext G) g = g :=
  ⟨True.intro, fun _ => rfl⟩

def ambientChoice : Term (fun _ => Bool) [.atom 0] (.arrow (.atom 0) (.atom 0)) :=
  .abstract (.use (.there .here))

/-- It uses no source constant, but an additional context ground is available. -/
theorem ambient_ground_can_replace : SourceFree ambientChoice ∧
    extract ambientChoice (extendContext true (emptyContext (fun _ => Bool))) false = true :=
  ⟨True.intro, rfl⟩

def introducedChoice : Term (fun _ => Bool) [] (.arrow (.atom 0) (.atom 0)) :=
  .abstract (.source 0 true)

/-- Empty ambient context alone does not prohibit an introduced ground. -/
theorem introduced_ground_can_replace : ¬ SourceFree introducedChoice ∧
    extract introducedChoice (emptyContext (fun _ => Bool)) false = true :=
  ⟨fun h => h, rfl⟩

end Generative.RecognitionalBinding

#print axioms Generative.RecognitionalBinding.source_free_related
#print axioms Generative.RecognitionalBinding.no_closed_source_free_atom
#print axioms Generative.RecognitionalBinding.closed_identity_forced
#print axioms Generative.RecognitionalBinding.closed_identity_preserves
#print axioms Generative.RecognitionalBinding.bound_identity_spec
#print axioms Generative.RecognitionalBinding.ambient_ground_can_replace
#print axioms Generative.RecognitionalBinding.introduced_ground_can_replace
