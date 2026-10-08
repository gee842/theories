import InferentialGrounds

/-!
Construction can preserve a correspondence through every compound term.
The correspondence is a relation on actual ground values, not a Boolean label
attached to the completed result. Atomic correspondence remains explicit.
This standard logical-relations argument is not an ultimate foundation.
-/

namespace Generative.GroundRelationTransport

open InferentialGrounds

universe u v

variable {Left : Nat → Type u} {Right : Nat → Type v}

def mapSources (f : ∀ i, Left i → Right i) :
    Term Left context a → Term Right context a
  | .source i g => .source i (f i g)
  | .use p => .use p
  | .pair x y => .pair (mapSources f x) (mapSources f y)
  | .first x => .first (mapSources f x)
  | .second x => .second (mapSources f x)
  | .abstract body => .abstract (mapSources f body)
  | .apply fn x => .apply (mapSources f fn) (mapSources f x)

def Related (R : ∀ i, Left i → Right i → Prop) :
    (a : Form) → GroundFor Left a → GroundFor Right a → Prop
  | .atom i, x, y => R i x y
  | .both a b, x, y => Related R a x.1 y.1 ∧ Related R b x.2 y.2
  | .arrow a b, f, g => ∀ x y, Related R a x y → Related R b (f x) (g y)

def EnvsRelated (R : ∀ i, Left i → Right i → Prop)
    (left : ContextGround Left context) (right : ContextGround Right context) : Prop :=
  ∀ {a} (p : Position context a), Related R a (left p) (right p)

theorem extend_related (R : ∀ i, Left i → Right i → Prop)
    (left : ContextGround Left context) (right : ContextGround Right context)
    (envs : EnvsRelated R left right)
    (x : GroundFor Left a) (y : GroundFor Right a) (xy : Related R a x y) :
    EnvsRelated R (extendContext x left) (extendContext y right) := by
  intro b p
  cases p with
  | here => exact xy
  | there p => exact envs p

/-- A compound correspondence is derived from the common formation and
    its atomic links; it is not a separate correctness input at every node. -/
theorem extract_transport (R : ∀ i, Left i → Right i → Prop)
    (f : ∀ i, Left i → Right i) (sources : ∀ i x, R i x (f i x))
    (term : Term Left context a)
    (left : ContextGround Left context) (right : ContextGround Right context)
    (envs : EnvsRelated R left right) :
    Related R a (extract term left) (extract (mapSources f term) right) := by
  induction term with
  | source i x => exact sources i x
  | use p => exact envs p
  | pair x y ihx ihy => exact ⟨ihx left right envs, ihy left right envs⟩
  | first x ih => exact (ih left right envs).1
  | second x ih => exact (ih left right envs).2
  | abstract body ih =>
    intro x y xy
    exact ih (extendContext x left) (extendContext y right)
      (extend_related R left right envs x y xy)
  | apply fn x ihfn ihx =>
    exact ihfn left right envs (extract x left) (extract (mapSources f x) right)
      (ihx left right envs)

/-- The exact remaining burden: transport for every closed term is equivalent
    to the atomic links. Formation discharges propagation, not those links. -/
theorem closed_transport_iff_sources (R : ∀ i, Left i → Right i → Prop)
    (f : ∀ i, Left i → Right i) :
    (∀ {a} (term : Term Left [] a),
      Related R a (extract term (emptyContext Left))
        (extract (mapSources f term) (emptyContext Right))) ↔
    (∀ i x, R i x (f i x)) := by
  constructor
  · intro all i x
    exact all (.source i x)
  · intro sources a term
    apply extract_transport R f sources term
    intro b p
    exact nomatch p

/-- A witnessed case: replacing each source by its paired representation
    earns both projection links by construction. This is logical reuse,
    not physical duplication or a proof of any unrelated empirical claim. -/
theorem paired_representation_transport (Left : Nat → Type u)
    {a : Form} (term : Term Left [] a) :
    Related (Right := fun i => Left i × Left i)
      (fun _ x y => y.1 = x ∧ y.2 = x) a
      (extract term (emptyContext Left))
      (extract (mapSources (fun _ x => (x, x)) term)
        (emptyContext (fun i => Left i × Left i))) := by
  apply (closed_transport_iff_sources
    (fun _ x y => y.1 = x ∧ y.2 = x) (fun _ x => (x, x))).mpr
  intro i x
  exact ⟨rfl, rfl⟩

#print axioms extend_related
#print axioms extract_transport
#print axioms closed_transport_iff_sources
#print axioms paired_representation_transport

end Generative.GroundRelationTransport
